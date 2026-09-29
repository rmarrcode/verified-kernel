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
from typing import Dict, List, Optional

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
    def serial(self) -> bool:
        """True when this instance would run essentially without parallelism: few
        programs, each looping many times. Such a kernel is still *verified* -- the
        theorem does not care -- but evaluating it on a GPU is not worth the wall
        clock. A two-stage (tree) reduction is the proper fix and is not yet built.
        """
        return (self.low.family == "genred"
                and self.low.K > 0 and self.out_size < 1024 and self.nkb > 4096)

    def check_side_conditions(self) -> None:
        """The decidable facts the family theorem needs. Checked here so a
        generator bug is caught before Lean is even invoked."""
        assert self.block > 0, f"{self.key}: block must be positive"
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
