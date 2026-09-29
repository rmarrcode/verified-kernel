"""The compiler driver: lowered specs -> Lean certificate file -> Triton kernels.

The generated Lean file is the project's audit trail. For each task it contains

  * the `SE` term the frontend derived from the PyTorch module,
  * the block size and grid the generator chose,
  * a `theorem` instantiating the family's correctness theorem at those numbers.

`lake build` typechecks every one of those theorems. Nothing is emitted unless
they all check, so a kernel in `generated/` is one whose correctness Lean has
accepted -- with the trusted base being the frontend that produced the `SE`, the
renderer, the modelled `tl.*` semantics, and Triton itself.
"""

from __future__ import annotations

import json
import os
import subprocess
from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple

from .frontend import Lowered

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LEAN_DIR = os.path.join(REPO, "lean")
GEN_LEAN = os.path.join(LEAN_DIR, "Generated", "Emit.lean")
GEN_PY = os.path.join(REPO, "generated")
ELAN_BIN = os.path.expanduser("~/.elan/bin")


@dataclass
class Instance:
    """One kernel to generate: a lowered spec plus the generator's choices."""
    key: str                 # a Lean/Python identifier, e.g. "t019"
    low: Lowered
    block: int
    out_size: int            # may be smaller than low.out_size for a reduced run

    @property
    def nblocks(self) -> int:
        return (self.out_size + self.block - 1) // self.block

    @property
    def nkb(self) -> int:
        """Loop iterations needed to cover the reduced axis."""
        return (self.low.K + self.block - 1) // self.block

    @property
    def stage_blocks(self) -> List[Tuple[int, int, int]]:
        """(block, nkb, nout) per stage. A single-stage family has one entry."""
        if self.low.family == "chain":
            out = []
            for st in self.low.stages:
                b = choose_block_red(st.K)
                out.append((b, (st.K + b - 1) // b, st.out_size))
            return out
        if self.low.family == "pipeline3":
            out = []
            for st, nout in zip(self.low.stages,
                                (self.low.n1, self.low.n2, self.out_size)):
                b = choose_block_red(st.K)
                out.append((b, (st.K + b - 1) // b, nout))
            return out
        if self.low.family == "pipeline":
            out = []
            for st, nout in zip(self.low.stages, (self.low.n1, self.out_size)):
                b = choose_block_red(st.K)
                out.append((b, (st.K + b - 1) // b, nout))
            return out
        if self.low.family == "pipeline_max":
            out = []
            for st, nout in zip(self.low.stages, (self.low.n1, self.out_size)):
                b = choose_block_red(st.K)
                out.append((b, (st.K + b - 1) // b, nout))
            return out
        if self.low.family in ("genred", "maxred"):
            return [(self.block, self.nkb, self.out_size)]
        return [(self.block, 1, self.out_size)]

    @property
    def serial(self) -> bool:
        """True when this instance would run essentially without parallelism: few
        programs, each looping many times. Such a kernel is still *verified* -- the
        theorem does not care -- but evaluating it on a GPU is not worth the wall
        clock. A two-stage (tree) reduction is the proper fix and is not yet built.
        """
        return any(nout < 1024 and nkb > 4096 for _, nkb, nout in self.stage_blocks)

    def check_side_conditions(self) -> None:
        """The decidable facts the family theorem needs. Checked here so a
        generator bug is caught before Lean is even invoked."""
        assert self.block > 0, f"{self.key}: block must be positive"
        if self.low.family == "chain":
            for i, st in enumerate(self.low.stages):
                b = choose_block_red(st.K)
                assert b > 0 and st.K <= ((st.K + b - 1) // b) * b, (
                    f"{self.key}: stage {i} loop does not cover extent {st.K}")
            return
        if self.low.family in ("pipeline", "pipeline3", "pipeline_max"):
            for i, (st, (b, nkb, _)) in enumerate(zip(self.low.stages,
                                                      self.stage_blocks)):
                assert b > 0 and st.K <= nkb * b, (
                    f"{self.key}: stage {i+1} loop {nkb}x{b} does not cover "
                    f"the reduced axis of extent {st.K}")
            return
        if self.low.family == "maxred":
            assert self.low.K > 0, f"{self.key}: a max over nothing is undefined"
            assert self.low.K <= self.nkb * self.block, (
                f"{self.key}: loop {self.nkb}x{self.block} does not cover "
                f"the reduced axis of extent {self.low.K}")
            return
        if self.low.family == "pointwise":
            assert self.out_size <= self.nblocks * self.block, (
                f"{self.key}: grid {self.nblocks}x{self.block} does not cover "
                f"{self.out_size} outputs")
        else:
            assert self.low.K <= self.nkb * self.block, (
                f"{self.key}: loop {self.nkb}x{self.block} does not cover "
                f"the reduced axis of extent {self.low.K}")


def choose_block(out_size: int) -> int:
    """A power-of-two block size. Correctness does not depend on this choice --
    the theorem is generic in `block` -- so it is purely a performance knob.

    Triton's `tl.arange` requires a power of two, which is the only real
    constraint here."""
    for b in (1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1):
        if b <= out_size:
            return b
    return 1


def choose_block_red(K: int) -> int:
    """Block size for a *reducing* kernel, where the block tiles the reduced axis
    rather than the output. Lanes beyond `K` would be masked off every iteration,
    so a block wider than `K` is pure waste."""
    return choose_block(max(1, min(K, 1024)))


def emit_lean(instances: List[Instance]) -> str:
    """Render the Lean certificate + emitter file."""
    out = [
        "/-",
        "  GENERATED FILE -- do not edit.",
        "",
        "  Written by verified_kernel.vk.compile. Each task below carries a",
        "  `theorem` instantiating its family's correctness theorem at the exact",
        "  numbers the generator chose. `lake build` checking this file is what",
        "  makes the corresponding kernel in generated/ a verified kernel.",
        "-/",
        "import VerifiedKernel",
        "",
        "open VerifiedKernel",
        "",
        "-- A chain of several hundred stages puts a list of that length in front of",
        "-- the elaborator. Recursion depth is an elaboration limit, not a checking",
        "-- one: raising it changes nothing about what counts as a proof, and the",
        "-- kernel still checks every term. `#print axioms` remains the real test.",
        "set_option maxRecDepth 100000",
        "-- Likewise a budget, not a criterion. Reading the last of a chain's several",
        "-- hundred recorded sizes means walking the list to it, so the size",
        "-- obligation costs more the longer the chain is.",
        "set_option maxHeartbeats 4000000",
        "",
    ]
    for inst in instances:
        k, low = inst.key, inst.low
        if low.family == "pipeline":
            out += _emit_pipeline(inst)
            continue
        if low.family == "maxred":
            out += _emit_maxred(inst)
            continue
        if low.family == "pipeline_max":
            out += _emit_pipeline_max(inst)
            continue
        if low.family == "pipeline3":
            out += _emit_pipeline3(inst)
            continue
        if low.family == "chain":
            out += _emit_chain(inst)
            continue
        if low.family == "genred":
            from . import ie as I
            # a standalone instance has no chain arity to split at
            split_at = None
            out += [
                f"-- {k}: reducing family, {low.arity} inputs, {inst.out_size} outputs,"
                f" reduced extent {low.K}",
                f"--   {'; '.join(low.notes)}",
                f"def {k}_g : GenRed :=",
                f"  {{ nout := {inst.out_size}, K := {low.K}",
                f"  , offs := {_sparse_offs(low.offs, split_at)}",
                f"  , inRange := {low.in_range.to_lean()}",
                f"  , body := {low.body.to_lean()}",
                f"  , postOffs := {_sparse_offs(low.post_offs, split_at)}",
                f"  , post := {low.post.to_lean()}",
                f"  , outGuard := {low.out_guard.to_lean()}",
                f"  , nInp := {low.arity}, idxSlot := {low.idx_slot} }}",
                f"def {k}_block : Nat := {inst.block}",
                f"def {k}_nkb : Nat := {inst.nkb}",
                "",
                f"/-- Index maps mention only the output and reduction indices. -/",
                f"theorem {k}_wf : {k}_g.Wf :=",
                f"  {{ offs_ok := {_qk(split_at)}",
                f"  , post_ok := {_qk(split_at)}",
                f"  , range_ok := by decide",
                f"  , guard_ok := by decide }}",
                "",
                f"/-- Correctness certificate for {k}. -/",
                f"theorem {k}_correct {{α : Type}} [ExactScalar α] :",
                f"    Implements ({k}_g.prog {k}_block {k}_nkb) ({k}_g.spec (α := α)) :=",
                f"  GenRed.prog_implements {k}_g {k}_block {k}_nkb {k}_wf"
                f" (by decide) (by decide)",
                "",
                f"def {k}_kernel : ReduceKernel :=",
                f"  {{ name := \"{k}\", arity := {low.arity}, block := {k}_block",
                f"  , nkb := {k}_nkb, nout := {inst.out_size}",
                f"  , init := FE.zeroC",
                f"  , step := {k}_g.step {k}_block",
                f"  , stored := {k}_g.stored {k}_block }}",
                "",
            ]
            continue
        assert low.family == "pointwise", f"unknown family {low.family}"
        out += [
            f"-- {k}: {low.family}, arity {low.arity}, {inst.out_size} outputs",
            f"def {k}_se : SE := {low.body.to_lean()}",
            f"def {k}_block : Nat := {inst.block}",
            f"def {k}_n : Nat := {inst.out_size}",
            f"def {k}_nblocks : Nat := {inst.nblocks}",
            f"def {k}_kernel : FlatKernel :=",
            f"  {{ name := \"{k}\", arity := {low.arity}, block := {k}_block",
            f"  , n := {k}_n, nblocks := {k}_nblocks",
            f"  , val := SE.toFE {k}_block {k}_n {k}_se }}",
            "",
            f"/-- Correctness certificate for {k}. -/",
            f"theorem {k}_correct {{α : Type}} [ExactScalar α] :",
            f"    Implements (Prog.flat1d {k}_nblocks {k}_block {k}_n",
            f"                 (SE.toFE {k}_block {k}_n {k}_se))",
            f"               (SE.spec (α := α) {k}_se {low.arity} {k}_n) :=",
            f"  SE.flat_correct {low.arity} {k}_se (by decide) (by decide)",
            "",
        ]
    out += ["def main : IO Unit := do"]
    if not instances:
        out += ["  pure ()"]
    for inst in instances:
        k = inst.key
        out += [f"  IO.FS.writeFile \"../generated/{k}.py\" {k}_kernel.render"]
    out += [""]
    return "\n".join(out)


def _qk(split_at) -> str:
    """The well-formedness proof for an index map, in whichever shape it was
    emitted."""
    if split_at is None:
        return "IE.qkOnly_sparse _ (by decide)"
    return ("IE.qkOnly_split (IE.qkOnly_sparse _ (by decide)) "
            "(IE.qkOnly_sparse _ (by decide))")


def _sparse_offs(lst, arity: int = None) -> str:
    """An index map as a table of the buffers it actually indexes.

    Identical in meaning to the dense list -- a buffer left out is indexed at zero,
    which is exactly what a zero entry says -- but for a chain of hundreds of
    buffers it is the difference between a line per buffer and a line per read.

    Given an arity, the table is split there. A locality obligation only ever fires
    for a buffer at or above it, so the split lets a stage's proof mention the one
    or two intermediates it reads and nothing else.
    """
    from . import ie as I
    def tbl(lo, hi):
        es = [(b, e) for b, e in enumerate(lst)
              if lo <= b < hi and not (isinstance(e, I.Lit) and e.n == 0)]
        return "IE.sparse [" + ", ".join(f"({b}, {e.to_lean()})" for b, e in es) + "]"
    if arity is None:
        return tbl(0, len(lst))
    return f"(IE.split {arity} ({tbl(0, arity)}) ({tbl(arity, len(lst))}))"


def _genred_defs(name: str, low, block: int, nkb: int, nout: int,
                 split_at: int = None) -> List[str]:
    """The `GenRed` value, its well-formedness, and its correctness certificate."""
    from . import ie as I
    return [
        f"def {name}_g : GenRed :=",
        f"  {{ nout := {nout}, K := {low.K}",
        f"  , offs := {_sparse_offs(low.offs, split_at)}",
        f"  , inRange := {low.in_range.to_lean()}",
        f"  , body := {low.body.to_lean()}",
        f"  , postOffs := {_sparse_offs(low.post_offs, split_at)}",
        f"  , post := {low.post.to_lean()}",
        f"  , outGuard := {low.out_guard.to_lean()}",
        f"  , nInp := {low.arity}, idxSlot := {low.idx_slot} }}",
        f"def {name}_block : Nat := {block}",
        f"def {name}_nkb : Nat := {nkb}",
        "",
        f"theorem {name}_wf : {name}_g.Wf :=",
        f"  {{ offs_ok := {_qk(split_at)}",
        f"  , post_ok := {_qk(split_at)}",
        f"  , range_ok := by decide",
        f"  , guard_ok := by decide }}",
        "",
        f"theorem {name}_impl {{α : Type}} [ExactScalar α] :",
        f"    Implements ({name}_g.prog {name}_block {name}_nkb) ({name}_g.spec (α := α)) :=",
        f"  GenRed.prog_implements {name}_g {name}_block {name}_nkb {name}_wf"
        f" (by decide) (by decide)",
        "",
    ]


def _maxred_defs(name: str, low, block: int, nkb: int, nout: int,
                 split_at: int = None) -> List[str]:
    """The `MaxRed` value, its well-formedness, and its correctness certificate."""
    from . import ie as I
    return [
        f"def {name}_g : MaxRed :=",
        f"  {{ nout := {nout}, K := {low.K}",
        f"  , offs := {_sparse_offs(low.offs, split_at)}",
        f"  , body := {low.body.to_lean()}",
        f"  , postOffs := {_sparse_offs(low.post_offs, split_at)}",
        f"  , post := {low.post.to_lean()}",
        f"  , nInp := {low.arity}, idxSlot := {low.idx_slot} }}",
        f"def {name}_block : Nat := {block}",
        f"def {name}_nkb : Nat := {nkb}",
        "",
        f"theorem {name}_wf : {name}_g.Wf :=",
        f"  {{ offs_ok := {_qk(split_at)}",
        f"  , post_ok := {_qk(split_at)} }}",
        "",
        f"theorem {name}_impl {{α : Type}} [ExactScalar α] :",
        f"    Implements ({name}_g.prog {name}_block {name}_nkb) ({name}_g.spec (α := α)) :=",
        f"  MaxRed.prog_implements {name}_g {name}_block {name}_nkb {name}_wf"
        f" (by decide) (by decide) (by decide)",
        "",
        f"def {name}_kernel : ReduceKernel :=",
        f"  {{ name := \"{name}\", arity := {low.arity}, block := {name}_block,"
        f" nkb := {name}_nkb, nout := {nout}, init := {name}_g.seed,"
        f" step := {name}_g.step {name}_block,"
        f" stored := {name}_g.stored {name}_block }}",
        "",
    ]


def _emit_pipeline_max(inst: "Instance") -> List[str]:
    """Two composed max reductions -- an argmax.

    Stage 1 takes the maximum of each row; stage 2 takes the *smallest index* whose
    element equals it, which is a minimum and so is the same family with the summand
    and result negated. The index enters the summand through `MaxRed`'s index slot.
    """
    k, low = inst.key, inst.low
    s1, s2 = low.stages
    t = low.arity
    out: List[str] = [
        f"-- {k}: composed max reductions, intermediate of {low.n1} at buffer {t}",
        f"--   {'; '.join(low.notes)}",
    ]
    for nm, st in ((f"{k}_s1", s1), (f"{k}_s2", s2)):
        b = choose_block_red(st.K)
        out += _maxred_defs(nm, st, b, (st.K + b - 1) // b, low.n1 if st is s1
                            else inst.out_size)
    out += [
        f"/-- Stage 2 reads the maxima only where stage 1 wrote them. -/",
        f"theorem {k}_loc {{α : Type}} [ExactScalar α] :",
        f"    ∀ (bufs : Nat → Buf α) (u v : Buf α),",
        f"      (∀ i, i < ({k}_s1_g.spec (α := α)).outSize → u i = v i) →",
        f"      ∀ q, q < ({k}_s2_g.spec (α := α)).outSize →",
        f"        ({k}_s2_g.spec (α := α)).out (subst bufs {t} u) q",
        f"          = ({k}_s2_g.spec (α := α)).out (subst bufs {t} v) q :=",
        f"  MaxRed.spec_locality {k}_s2_g {t} {low.n1} (by decide) (by decide)",
        f"    {_bound_proof(low.bounds['l2'])}",
        f"    {_bound_proof_post(low.bounds.get('l2post', ('zero', low.n1)))}",
        "",
        f"/-- Correctness certificate for {k}. -/",
        f"theorem {k}_correct {{α : Type}} [ExactScalar α] :",
        f"    ∀ (bufs : Nat → Buf α) (m1 m2 : Mem α) (q : Nat),",
        f"      q < ({k}_s2_g.spec (α := α)).outSize →",
        f"      runTwo ({k}_s1_g.prog {k}_s1_block {k}_s1_nkb)",
        f"             ({k}_s2_g.prog {k}_s2_block {k}_s2_nkb) {t} bufs m1 m2 q",
        f"        = ({k}_s2_g.spec (α := α)).out",
        f"            (subst bufs {t} (fun i => ({k}_s1_g.spec (α := α)).out bufs i)) q :=",
        f"  two_stage {k}_s1_impl {k}_s2_impl {k}_loc",
        "",
        f"def {k}_kernel : PipelineKernel :=",
        f"  {{ name := \"{k}\", arity := {low.arity}, n1 := {low.n1},"
        f" stage1 := {k}_s1_kernel, stage2 := {k}_s2_kernel }}",
        "",
    ]
    return out


def _emit_maxred(inst: "Instance") -> List[str]:
    """A max (or min) reduction. No `inRange`: this family clamps its index maps so
    every lane reads a genuine element, which is how it avoids needing an identity
    for `max` -- an ordered field has none, and adding one would make the axioms
    inconsistent."""
    from . import ie as I
    k, low = inst.key, inst.low
    block = choose_block_red(low.K)
    nkb = (low.K + block - 1) // block
    return [
        f"-- {k}: max reduction, {low.arity} input(s), {inst.out_size} outputs,"
        f" extent {low.K}",
        f"--   {'; '.join(low.notes)}",
        f"def {k}_g : MaxRed :=",
        f"  {{ nout := {inst.out_size}, K := {low.K}",
        f"  , offs := {_sparse_offs(low.offs, split_at)}",
        f"  , body := {low.body.to_lean()}",
        f"  , postOffs := {_sparse_offs(low.post_offs, split_at)}",
        f"  , post := {low.post.to_lean()}",
        f"  , nInp := {low.arity}, idxSlot := {low.idx_slot} }}",
        f"def {k}_block : Nat := {block}",
        f"def {k}_nkb : Nat := {nkb}",
        "",
        f"theorem {k}_wf : {k}_g.Wf :=",
        f"  {{ offs_ok := {_qk(split_at)}",
        f"  , post_ok := {_qk(split_at)} }}",
        "",
        f"/-- Correctness certificate for {k}. -/",
        f"theorem {k}_correct {{α : Type}} [ExactScalar α] :",
        f"    Implements ({k}_g.prog {k}_block {k}_nkb) ({k}_g.spec (α := α)) :=",
        f"  MaxRed.prog_implements {k}_g {k}_block {k}_nkb {k}_wf"
        f" (by decide) (by decide) (by decide)",
        "",
        f"def {k}_kernel : ReduceKernel :=",
        f"  {{ name := \"{k}\", arity := {low.arity}, block := {k}_block",
        f"  , nkb := {k}_nkb, nout := {inst.out_size}",
        f"  , init := {k}_g.seed",
        f"  , step := {k}_g.step {k}_block",
        f"  , stored := {k}_g.stored {k}_block }}",
        "",
    ]


def _prodred_defs(name: str, low, block: int, nkb: int, nout: int,
                  split_at: int = None) -> List[str]:
    """The `ProdRed` value and its certificate -- `_genred_defs` multiplicatively."""
    return [ln.replace("GenRed", "ProdRed").replace("init := FE.zeroC",
                                                    "init := FE.oneC")
            for ln in _genred_defs(name, low, block, nkb, nout)]


def _init_for(st, name: str) -> str:
    """The accumulator's starting value for a stage.

    Zero for a sum and one for a product -- but a *max* has no identity, so it starts
    from the element at reduction index 0. Starting it at zero silently computes
    `max(0, xs)`, which is wrong exactly when every element is negative.
    """
    if st.family == "maxred":
        return f"{name}_g.seed"
    return "FE.oneC" if st.family == "prodred" else "FE.zeroC"


def _drop_kernel_def(lines: List[str]) -> List[str]:
    """Strip a stage's `ReduceKernel` definition.

    A chain emits its own, with the arity the launcher actually passes; leaving the
    standalone one in place declares the same name twice.
    """
    out, skip = [], False
    for ln in lines:
        if ln.startswith("def ") and "_kernel : ReduceKernel" in ln:
            skip = True
            continue
        if skip:
            if ln.startswith("  {") or ln.startswith("  ,") or ln.startswith("  "):
                continue
            skip = False
        out.append(ln)
    return out


def _stage_defs(name: str, st, block: int, nkb: int, nout: int,
                split_at: int = None) -> List[str]:
    """Emit one stage, in whichever family it belongs to."""
    if st.family == "prodred":
        return _drop_kernel_def(_prodred_defs(name, st, block, nkb, nout, split_at))
    if st.family == "maxred":
        return _drop_kernel_def(_maxred_defs(name, st, block, nkb, nout, split_at))
    return _drop_kernel_def(_genred_defs(name, st, block, nkb, nout, split_at))


def _emit_pipeline(inst: "Instance") -> List[str]:
    """A two-stage pipeline: both stages certified, plus the locality obligation
    that licenses composing them.

    The locality proof is the interesting part. `two_stage` is only sound if stage 2
    reads the intermediate buffer inside the range stage 1 wrote, and that is
    `bound_row`: for an input viewed as `[outer, K, inner]`, output `q` reads the
    intermediate at `(q/(K*inner))*inner + q%inner`, which is below `outer*inner`.
    """
    k, low = inst.key, inst.low
    s1, s2 = low.stages
    t = low.arity                      # the intermediate is the last buffer
    b1 = choose_block_red(s1.K)
    nkb1 = (s1.K + b1 - 1) // b1
    b2 = choose_block_red(s2.K)
    nkb2 = (s2.K + b2 - 1) // b2
    out: List[str] = [
        f"-- {k}: two-stage pipeline, {low.arity} input(s), "
        f"{low.n1}-element intermediate at buffer {t}",
        f"--   {'; '.join(low.notes)}",
    ]
    out += _genred_defs(f"{k}_s1", s1, b1, nkb1, low.n1)
    out += _genred_defs(f"{k}_s2", s2, b2, nkb2, inst.out_size)
    out += [
        f"/-- Stage 2 reads the intermediate only where stage 1 wrote it. -/",
        f"theorem {k}_loc {{α : Type}} [ExactScalar α] :",
        f"    ∀ (bufs : Nat → Buf α) (u v : Buf α),",
        f"      (∀ i, i < ({k}_s1_g.spec (α := α)).outSize → u i = v i) →",
        f"      ∀ q, q < ({k}_s2_g.spec (α := α)).outSize →",
        f"        ({k}_s2_g.spec (α := α)).out (subst bufs {t} u) q",
        f"          = ({k}_s2_g.spec (α := α)).out (subst bufs {t} v) q :=",
        f"  GenRed.spec_locality {k}_s2_g {t} {low.n1}",
        # `hq : q < g.nout` is definitionally `q < <numeral>`, and the bound the
        # lemma wants is the same numeral written as a product, so `hq` is accepted
        # directly. `omega` cannot do this: it sees an opaque projection.
        # A tree reduction's second stage reads the intermediate at `rk`, so the
        # bound it needs is `k < K` -- a hypothesis it already has. A
        # row-normalising stage reads one value per row, and needs `bound_row`.
        "    " + _bound_proof(low.bounds["l2"]),
        # A type ascription lets `decide` see a closed proposition; the lambda's
        # body is then checked against the expected type by defeq, which reduces
        # the index map away.
        "    " + _bound_proof_post(low.bounds.get("l2post", ("zero", low.n1))),
        "",
        f"/-- Correctness certificate for {k}: the composed pipeline. -/",
        f"theorem {k}_correct {{α : Type}} [ExactScalar α] :",
        f"    ∀ (bufs : Nat → Buf α) (m1 m2 : Mem α) (q : Nat),",
        f"      q < ({k}_s2_g.spec (α := α)).outSize →",
        f"      runTwo ({k}_s1_g.prog {k}_s1_block {k}_s1_nkb)",
        f"             ({k}_s2_g.prog {k}_s2_block {k}_s2_nkb) {t} bufs m1 m2 q",
        f"        = ({k}_s2_g.spec (α := α)).out",
        f"            (subst bufs {t} (fun i => ({k}_s1_g.spec (α := α)).out bufs i)) q :=",
        f"  two_stage {k}_s1_impl {k}_s2_impl {k}_loc",
        "",
        f"def {k}_s1_kernel : ReduceKernel :=",
        f"  {{ name := \"{k}_s1\", arity := {s1.arity}, block := {k}_s1_block,"
        f" nkb := {k}_s1_nkb, nout := {low.n1}, init := FE.zeroC,"
        f" step := {k}_s1_g.step {k}_s1_block,"
        f" stored := {k}_s1_g.stored {k}_s1_block }}",
        f"def {k}_s2_kernel : ReduceKernel :=",
        f"  {{ name := \"{k}_s2\", arity := {s2.arity}, block := {k}_s2_block,"
        f" nkb := {k}_s2_nkb, nout := {inst.out_size}, init := FE.zeroC,"
        f" step := {k}_s2_g.step {k}_s2_block,"
        f" stored := {k}_s2_g.stored {k}_s2_block }}",
        f"def {k}_kernel : PipelineKernel :=",
        f"  {{ name := \"{k}\", arity := {low.arity}, n1 := {low.n1},"
        f" stage1 := {k}_s1_kernel, stage2 := {k}_s2_kernel }}",
        "",
    ]
    return out


def _bound_atom(sb: Tuple) -> str:
    """Proof that one *coordinate* of an index map is below its extent.

    Every implicit argument is supplied explicitly. Left to inference they become
    metavariables Lean must solve against a *numeral* -- `67108864 =?= ?a * ?d` has
    no unique solution, so inference either fails or drives the kernel into a deep
    unfolding. `hq : q < nout` and `hk : k < K` are accepted directly, since each is
    definitionally the numeral the lemma wants.
    """
    kind = sb[0]
    if kind == "hq":
        return "hq"
    if kind == "hk":
        return "hk"
    if kind == "zerolt":
        return f"(by decide : (0 : Nat) < {sb[1]})"
    if kind == "div":
        _, n, span = sb
        return f"(bound_div (a := {n}) (d := {span}) hq)"
    if kind == "mod":
        c = sb[1]
        return f"(bound_mod (c := {c}) (by decide : (0 : Nat) < {c}))"
    if kind == "row":
        _, outer, K, inner = sb
        return (f"(bound_row (outer := {outer}) (K := {K}) (inner := {inner})"
                f" (by decide) hq)")
    if kind == "divmod":
        # `(x % C) / CG < G`, for a coordinate split out of a packed index. Needs
        # `C = G * CG`, i.e. the block size to divide the extent.
        _, C, CG, G, xexpr = sb
        return (f"(bound_group (C := {C}) (CG := {CG}) (G := {G}) (x := {xexpr})"
                f" (by decide) (by decide) (by decide))")
    if kind == "group":
        _, C, CG, G, SP = sb
        return (f"(bound_group (C := {C}) (CG := {CG}) (G := {G}) (x := q / {SP})"
                f" (by decide) (by decide) (by decide))")
    if kind == "pack":
        _, N, G, C, SP, CG = sb
        return (f"(bound_pack (A := {N}) (B := {G})"
                f" (bound_div (a := {N}) (d := {C * SP}) hq)"
                f" (bound_group (C := {C}) (CG := {CG}) (G := {G}) (x := q / {SP})"
                f" (by decide) (by decide) (by decide)))")
    if kind == "clamp":
        d = sb[1]
        return f"(ExactScalar.clamp_lt (c := {d}) (by decide : (0 : Nat) < {d}))"
    if kind == "packs":
        # A row-major index built from several coordinates: fold `bound_pack` along
        # it, carrying the running product of extents as the bound.
        _, coords, extents = sb
        term = _bound_atom(tuple(coords[0]))
        A = extents[0]
        for c, B in zip(coords[1:], extents[1:]):
            term = f"(bound_pack (A := {A}) (B := {B}) {term} {_bound_atom(tuple(c))})"
            A *= B
        return term
    raise AssertionError(f"unknown bound {sb!r}")


def _bound_proof_post(sb: Tuple) -> str:
    """Locality proof for a stage's *post* read of an intermediate.

    `GenRed.loc`'s second obligation is quantified over `q` only -- there is no
    reduction index in the post stage -- so these lambdas take two arguments where
    the reduced-stage ones take four.
    """
    if sb[0] == "zero":
        return f"(fun _ _ => (by decide : (0 : Nat) < {sb[1]}))"
    return f"(fun q hq => {_bound_atom(sb)})"


def _bound_proof(sb: Tuple) -> str:
    """The locality proof term for one stage's reads of an intermediate buffer.

    Which lemma applies is a fact about the *shape*, so the generator records it
    during lowering rather than rediscovering it here.
    """
    kind = sb[0]
    if kind == "pid":
        return "(fun q _ hq _ => hq)"
    if kind == "rk":
        return "(fun _ k _ hk => hk)"
    if kind == "zero":
        return f"(fun _ _ _ _ => (by decide : (0 : Nat) < {sb[1]}))"
    return f"(fun q k hq hk => {_bound_atom(sb)})"


def _emit_pipeline3(inst: "Instance") -> List[str]:
    """A three-stage normalisation: sums, then squared deviations, then the affine
    correction.

    Beyond the three stage certificates, `three_stage` needs three locality facts:
    stage 2 must not depend on the first intermediate past its end, and stage 3 on
    neither intermediate past its end. Those are what `GenRed.loc` discharges, from
    the shape bounds recorded during lowering.
    """
    k, low = inst.key, inst.low
    s1, s2, s3 = low.stages
    t1 = low.arity
    t2 = low.arity + 1
    out: List[str] = [
        f"-- {k}: three-stage normalisation, {low.arity} input buffer(s),"
        f" intermediates {low.n1} and {low.n2} at buffers {t1} and {t2}",
        f"--   {'; '.join(low.notes)}",
    ]
    for nm, st, nout in ((f"{k}_s1", s1, low.n1), (f"{k}_s2", s2, low.n2),
                         (f"{k}_s3", s3, inst.out_size)):
        b = choose_block_red(st.K)
        out += _stage_defs(nm, st, b, (st.K + b - 1) // b, nout)
    b2 = _bound_proof(low.bounds["l2"])
    b3a = _bound_proof(low.bounds["l3a"])
    b3b = _bound_proof(low.bounds["l3b"])
    p2 = _bound_proof_post(low.bounds.get("l2post", ("zero", low.n1)))
    p3a = _bound_proof_post(low.bounds.get("l3apost", ("zero", low.n1)))
    p3b = _bound_proof_post(low.bounds.get("l3bpost", ("zero", low.n2)))
    out += [
        f"/-- Stage 2 reads the first intermediate only where stage 1 wrote it. -/",
        f"theorem {k}_l2 {{α : Type}} [ExactScalar α] :",
        f"    Loc ({k}_s2_g.spec (α := α)) {t1} {low.n1} :=",
        f"  {s2.family.replace('prodred','ProdRed').replace('genred','GenRed')}"
        f".loc {k}_s2_g {t1} {low.n1} {b2} {p2}",
        "",
        f"/-- Stage 3 reads each intermediate only where its stage wrote it. -/",
        f"theorem {k}_l3a {{α : Type}} [ExactScalar α] :",
        f"    Loc ({k}_s3_g.spec (α := α)) {t1} {low.n1} :=",
        f"  {s3.family.replace('prodred','ProdRed').replace('genred','GenRed')}"
        f".loc {k}_s3_g {t1} {low.n1} {b3a} {p3a}",
        "",
        f"theorem {k}_l3b {{α : Type}} [ExactScalar α] :",
        f"    Loc ({k}_s3_g.spec (α := α)) {t2} {low.n2} :=",
        f"  {s3.family.replace('prodred','ProdRed').replace('genred','GenRed')}"
        f".loc {k}_s3_g {t2} {low.n2} {b3b} {p3b}",
        "",
        f"/-- Correctness certificate for {k}: the composed three-stage pipeline. -/",
        f"theorem {k}_correct {{α : Type}} [ExactScalar α] :",
        f"    ∀ (bufs : Nat → Buf α) (m1 m2 m3 : Mem α) (q : Nat),",
        f"      q < ({k}_s3_g.spec (α := α)).outSize →",
        f"      runThree ({k}_s1_g.prog {k}_s1_block {k}_s1_nkb)",
        f"               ({k}_s2_g.prog {k}_s2_block {k}_s2_nkb)",
        f"               ({k}_s3_g.prog {k}_s3_block {k}_s3_nkb) {t1} {t2}"
        f" bufs m1 m2 m3 q",
        f"        = compose3 ({k}_s1_g.spec (α := α)) ({k}_s2_g.spec (α := α))",
        f"            ({k}_s3_g.spec (α := α)) {t1} {t2} bufs q :=",
        f"  three_stage (by decide) {k}_s1_impl {k}_s2_impl {k}_s3_impl"
        f" {k}_l2 {k}_l3a {k}_l3b",
        "",
    ]
    for nm, st, nout in ((f"{k}_s1", s1, low.n1), (f"{k}_s2", s2, low.n2),
                         (f"{k}_s3", s3, inst.out_size)):
        out += [
            f"def {nm}_kernel : ReduceKernel :=",
            f"  {{ name := \"{nm}\", arity := {st.arity}, block := {nm}_block,"
            f" nkb := {nm}_nkb, nout := {nout},"
            f" init := {_init_for(st, nm)},"
            f" step := {nm}_g.step {nm}_block,"
            f" stored := {nm}_g.stored {nm}_block }}",
        ]
    out += [
        f"def {k}_kernel : PipelineKernel3 :=",
        f"  {{ name := \"{k}\", arity := {low.arity}, n1 := {low.n1}, n2 := {low.n2},"
        f" stage1 := {k}_s1_kernel, stage2 := {k}_s2_kernel,"
        f" stage3 := {k}_s3_kernel }}",
        "",
    ]
    return out


FAM_LEAN = {"genred": "GenRed", "maxred": "MaxRed", "prodred": "ProdRed"}


def _emit_chain(inst: "Instance") -> List[str]:
    """A chain of stages, composed by `stages_correct`.

    Beyond each stage's own certificate, the composition needs one locality fact per
    stage: that it does not read any intermediate buffer past what was written there.
    Those are stated against the *final* size map, which is why there is one per
    stage rather than one per pair of stages.
    """
    k, low = inst.key, inst.low
    A = low.arity
    n = len(low.stages)
    out: List[str] = [
        f"-- {k}: a chain of {n} stage(s), {A} input buffer(s)",
        f"--   {'; '.join(low.notes[:3]) if low.notes else ''}",
        # A list rather than a match on each buffer: the positivity of every
        # recorded size is then one fact for the whole chain, instead of one case
        # per buffer inside every stage's locality proof.
        f"def {k}_sizes : List Nat := [{', '.join(str(x) for x in low.sizes)}]",
        f"def {k}_sz : Sizes := Sizes.ofList {A} {k}_sizes",
        f"theorem {k}_sz_pos : \u2200 b n, {k}_sz b = some n \u2192 0 < n :=",
        f"  Sizes.ofList_pos (by decide)",
        "",
    ]

    for j, st in enumerate(low.stages):
        b = choose_block_red(st.K)
        out += _stage_defs(f"{k}_s{j}", st, b, (st.K + b - 1) // b, st.out_size, A)

    # One locality fact per stage, and inside it one case per buffer the stage
    # actually reads -- not one per buffer in the chain. Every other buffer is the
    # constant-zero map, where the bound is `0 < n` and holds of any recorded size.
    for j, st in enumerate(low.stages):
        fam = FAM_LEAN[st.family]
        out += [
            f"/-- Stage {j} reads no intermediate past what was written there. -/",
            f"theorem {k}_s{j}_loc {{α : Type}} [ExactScalar α] :",
            f"    SpecLocal {k}_sz ({k}_s{j}_g.spec (α := α)) :=",
            f"  {fam}.specLocal {k}_s{j}_g {k}_sz"
            + (" (by decide)" if fam == "MaxRed" else ""),
        ]
        for tag, field in (("b", "offs"), ("p", "postOffs")):
            reads = _chain_reads(st, tag, A, n)
            args = "q kk hq hk" if tag == "b" else "q hq"
            out.append(f"    (fun b nn hn {args} => by")
            for i in reads:
                out += [
                    f"      by_cases h{i} : b = {i}",
                    f"      · subst h{i}",
                    f"        have hs : nn = {low.sizes[i - A]} :=",
                    f"          Sizes.ofList_some (by decide) (by decide) hn",
                    f"        subst hs",
                    f"        exact {_chain_bound(st, tag, i, low)}",
                ]
            neg = "".join(f", h{i}" for i in reads)
            out += [
                f"      have hb : {A} \u2264 b := Sizes.ofList_le hn",
                f"      have hz : {k}_s{j}_g.{field} b = IE.lit 0 := by",
                f"        simp [{k}_s{j}_g, IE.split_ge hb, IE.sparse{neg}]",
                f"      rw [hz]",
                f"      exact {k}_sz_pos b nn hn)",
            ]
        out.append("")

    stage_list = ", ".join(
        f"⟨{k}_s{j}_g.prog {k}_s{j}_block {k}_s{j}_nkb, {k}_s{j}_g.spec (α := α), {A + j}⟩"
        for j in range(n))
    out += [
        f"def {k}_chain (α : Type) [ExactScalar α] : List (Stage α) := [{stage_list}]",
        "",
        f"theorem {k}_imp {{α : Type}} [ExactScalar α] :",
        f"    ∀ st ∈ {k}_chain α, Implements st.prog st.spec :=",
    ]
    out += _forall_mem(n, lambda j: f"{k}_s{j}_impl")
    out += [
        "",
        f"theorem {k}_szok {{α : Type}} [ExactScalar α] :",
        f"    ∀ st ∈ {k}_chain α, {k}_sz st.out = some st.spec.outSize :=",
    ]
    out += _forall_mem(n, lambda j: "rfl")
    out += [
        "",
        f"theorem {k}_loc {{α : Type}} [ExactScalar α] :",
        f"    ∀ st ∈ {k}_chain α, SpecLocal {k}_sz st.spec :=",
    ]
    out += _forall_mem(n, lambda j: f"{k}_s{j}_loc")
    out += [
        "",
        f"/-- Correctness certificate for {k}: the whole chain. -/",
        f"theorem {k}_correct {{α : Type}} [ExactScalar α] :",
        f"    ∀ (f : Nat → Buf α) (m : Mem α),",
        f"      Compat (sizesAfter ({k}_chain α) emptySizes)",
        f"        (runStages ({k}_chain α) f m) (specStages ({k}_chain α) f) :=",
        f"  fun f m => stages_correct {k}_sz ({k}_chain α) emptySizes f f m",
        f"    (Compat.refl _ _) (emptySizes_sub {k}_sz)",
        f"    {k}_szok {k}_imp {k}_loc",
        "",
    ]
    for j, st in enumerate(low.stages):
        # the launcher hands stage j the inputs plus the j intermediates written so
        # far -- not its own output buffer, which it writes
        out += [
            f"def {k}_s{j}_kernel : ReduceKernel :=",
            f"  {{ name := \"{k}_s{j}\", arity := {A + j}, block := {k}_s{j}_block,"
            f" nkb := {k}_s{j}_nkb, nout := {st.out_size},"
            f" init := {_init_for(st, f'{k}_s{j}')},"
            f" step := {k}_s{j}_g.step {k}_s{j}_block,"
            f" stored := {k}_s{j}_g.stored {k}_s{j}_block }}",
        ]
    out += [
        f"def {k}_kernel : ChainKernel :=",
        f"  {{ name := \"{k}\", arity := {A}, sizes := {low.sizes},",
        f"    stages := [" + ", ".join(f"{k}_s{j}_kernel" for j in range(n)) + "] }",
        "",
    ]
    return out


def _forall_mem(n: int, proof) -> List[str]:
    """`\u2200 st \u2208 chain, P st` as a term rather than a case split.

    The tactic form -- unfold the list, then `rcases` an `n`-deep `Or` -- is
    quadratic in the length of the chain, which a 454-stage network does not
    survive. Nesting `List.forall_mem_cons` is linear and says the same thing:
    the property holds of the head, and of everything after it.
    """
    lines = []
    for j in range(n):
        lines.append("  " * 0 + f"  List.forall_mem_cons.mpr \u27e8{proof(j)},")
    lines.append("  List.forall_mem_nil _" + "\u27e9" * n)
    return lines


def _chain_reads(st, tag: str, arity: int, nstages: int) -> List[int]:
    """Which intermediate buffers this stage's index map actually reads.

    A stage that does not read a buffer maps it to the constant zero, and the
    locality bound there is `0 < n`, which every recorded size satisfies. Listing
    only the rest is what keeps a chain's proof linear in its length rather than
    quadratic.
    """
    from . import ie as I
    lst = st.offs if tag == "b" else st.post_offs
    return [b for b in range(arity, arity + nstages)
            if b < len(lst) and not (isinstance(lst[b], I.Lit) and lst[b].n == 0)]


def _chain_bound(st, tag: str, buf: int, low) -> str:
    return _bound_atom(tuple(st.bounds[f"{tag}{buf}"]))


def _env() -> Dict[str, str]:
    env = dict(os.environ)
    env["PATH"] = ELAN_BIN + os.pathsep + env.get("PATH", "")
    return env


def compile_all(instances: List[Instance], verbose: bool = True) -> Dict[str, object]:
    """Write the Lean file, typecheck it, and emit kernels.

    Returns a report. A non-empty `proof_errors` means nothing was emitted.
    """
    for inst in instances:
        inst.check_side_conditions()

    os.makedirs(os.path.dirname(GEN_LEAN), exist_ok=True)
    os.makedirs(GEN_PY, exist_ok=True)
    with open(GEN_LEAN, "w") as f:
        f.write(emit_lean(instances))

    if verbose:
        print(f"[compile] {len(instances)} instances -> {GEN_LEAN}")

    build = subprocess.run(["lake", "build", "vkemit"], cwd=LEAN_DIR, env=_env(),
                           capture_output=True, text=True)
    errors = [ln for ln in (build.stdout + build.stderr).splitlines()
              if ln.startswith("error:") or ": error:" in ln]
    if build.returncode != 0 or errors:
        return {"ok": False, "proof_errors": errors or [build.stderr[-4000:]],
                "emitted": []}

    run = subprocess.run(["lake", "exe", "vkemit"], cwd=LEAN_DIR, env=_env(),
                         capture_output=True, text=True)
    if run.returncode != 0:
        return {"ok": False, "proof_errors": [],
                "emit_error": run.stderr[-4000:], "emitted": []}

    emitted = [inst.key for inst in instances
               if os.path.exists(os.path.join(GEN_PY, f"{inst.key}.py"))]
    if verbose:
        print(f"[compile] proofs checked, {len(emitted)} kernels emitted")
    return {"ok": True, "proof_errors": [], "emitted": emitted}
