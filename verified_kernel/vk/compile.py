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
        if self.low.family == "pipeline":
            out = []
            for st, nout in zip(self.low.stages, (self.low.n1, self.out_size)):
                b = choose_block_red(st.K)
                out.append((b, (st.K + b - 1) // b, nout))
            return out
        if self.low.family == "genred":
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
        if self.low.family == "pipeline":
            for i, (st, (b, nkb, _)) in enumerate(zip(self.low.stages,
                                                      self.stage_blocks)):
                assert b > 0 and st.K <= nkb * b, (
                    f"{self.key}: stage {i+1} loop {nkb}x{b} does not cover "
                    f"the reduced axis of extent {st.K}")
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
    ]
    for inst in instances:
        k, low = inst.key, inst.low
        if low.family == "pipeline":
            out += _emit_pipeline(inst)
            continue
        if low.family == "genred":
            from . import ie as I
            out += [
                f"-- {k}: reducing family, {low.arity} inputs, {inst.out_size} outputs,"
                f" reduced extent {low.K}",
                f"--   {'; '.join(low.notes)}",
                f"def {k}_g : GenRed :=",
                f"  {{ nout := {inst.out_size}, K := {low.K}",
                f"  , offs := fun b => ({I.lean_list(low.offs)}).getD b (IE.lit 0)",
                f"  , inRange := {low.in_range.to_lean()}",
                f"  , body := {low.body.to_lean()}",
                f"  , postOffs := fun b => ({I.lean_list(low.post_offs)}).getD b (IE.lit 0)",
                f"  , post := {low.post.to_lean()}",
                f"  , outGuard := {low.out_guard.to_lean()}",
                f"  , nInp := {low.arity} }}",
                f"def {k}_block : Nat := {inst.block}",
                f"def {k}_nkb : Nat := {inst.nkb}",
                "",
                f"/-- Index maps mention only the output and reduction indices. -/",
                f"theorem {k}_wf : {k}_g.Wf :=",
                f"  {{ offs_ok := IE.qkOnly_getD _ (by decide)",
                f"  , post_ok := IE.qkOnly_getD _ (by decide)",
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


def _genred_defs(name: str, low, block: int, nkb: int, nout: int) -> List[str]:
    """The `GenRed` value, its well-formedness, and its correctness certificate."""
    from . import ie as I
    return [
        f"def {name}_g : GenRed :=",
        f"  {{ nout := {nout}, K := {low.K}",
        f"  , offs := fun b => ({I.lean_list(low.offs)}).getD b (IE.lit 0)",
        f"  , inRange := {low.in_range.to_lean()}",
        f"  , body := {low.body.to_lean()}",
        f"  , postOffs := fun b => ({I.lean_list(low.post_offs)}).getD b (IE.lit 0)",
        f"  , post := {low.post.to_lean()}",
        f"  , outGuard := {low.out_guard.to_lean()}",
        f"  , nInp := {low.arity} }}",
        f"def {name}_block : Nat := {block}",
        f"def {name}_nkb : Nat := {nkb}",
        "",
        f"theorem {name}_wf : {name}_g.Wf :=",
        f"  {{ offs_ok := IE.qkOnly_getD _ (by decide)",
        f"  , post_ok := IE.qkOnly_getD _ (by decide)",
        f"  , range_ok := by decide",
        f"  , guard_ok := by decide }}",
        "",
        f"theorem {name}_impl {{α : Type}} [ExactScalar α] :",
        f"    Implements ({name}_g.prog {name}_block {name}_nkb) ({name}_g.spec (α := α)) :=",
        f"  GenRed.prog_implements {name}_g {name}_block {name}_nkb {name}_wf"
        f" (by decide) (by decide)",
        "",
    ]


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
        f"    (fun q _ hq _ => bound_row (outer := {low.outer}) (K := {s1.K})",
        f"      (inner := {low.inner}) (by decide) hq)",
        # A type ascription lets `decide` see a closed proposition; the lambda's
        # body is then checked against the expected type by defeq, which reduces
        # the index map away.
        f"    (fun _ _ => (by decide : (0 : Nat) < {low.n1}))",
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
        f" nkb := {k}_s1_nkb, nout := {low.n1},"
        f" step := {k}_s1_g.step {k}_s1_block,"
        f" stored := {k}_s1_g.stored {k}_s1_block }}",
        f"def {k}_s2_kernel : ReduceKernel :=",
        f"  {{ name := \"{k}_s2\", arity := {s2.arity}, block := {k}_s2_block,"
        f" nkb := {k}_s2_nkb, nout := {inst.out_size},"
        f" step := {k}_s2_g.step {k}_s2_block,"
        f" stored := {k}_s2_g.stored {k}_s2_block }}",
        f"def {k}_kernel : PipelineKernel :=",
        f"  {{ name := \"{k}\", arity := {low.arity}, n1 := {low.n1},"
        f" stage1 := {k}_s1_kernel, stage2 := {k}_s2_kernel }}",
        "",
    ]
    return out


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
