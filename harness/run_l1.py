"""End-to-end run over KernelBench Level 1.

    python harness/run_l1.py [--only 19,20] [--no-eval]

Pipeline per task: lower to a spec, choose a grid, emit a Lean certificate,
typecheck every certificate in one `lake build`, render the Triton kernels, then
check each against the PyTorch reference with KernelBench's own criterion.

The two numbers reported at the end mean different things and are kept apart:

  verified  -- the task lowered to a spec and Lean accepted its correctness
               certificate. Shape-generic, so it holds at the declared size.
  passing   -- the emitted kernel also matched the PyTorch reference on GPU.
               Limited by device memory, not by the proof.
"""

from __future__ import annotations

import argparse
import gc
import os
import sys
import traceback
from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Tuple

import torch

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "verified_kernel"))

import evaluate as E
from tasks import all_tasks, fake_instance
from vk import compile as C
from vk import frontend
from vk import graph
from vk.runtime import GeneratedModel

GB = 1024 ** 3


@dataclass
class Plan:
    task: Any
    low: frontend.Lowered
    key: str
    mode: str
    scale: int
    out_size: int
    out_shape: Tuple[int, ...]


def make_plan(task, budget: int, min_scale: int = 1) -> Tuple[Optional[Plan], List[str]]:
    """Lower the task at the largest size that fits in `budget`.

    The search re-lowers at each candidate scale rather than rescaling a
    full-size lowering: a reducing family's index maps are functions of the
    shapes, so the spec that gets verified must be the spec of the kernel that
    gets run.
    """
    reasons: List[str] = []
    scale = min_scale
    while scale <= (1 << 24):
        mode_fake, model, inputs = fake_instance(task)
        with mode_fake:
            red = E.shrink(list(inputs), scale)
            low, reasons = frontend.lower(model, red)
        if low is None:
            # A single-operator lowering did not apply; compile the whole graph as
            # a chain of stages instead.
            try:
                low = graph.compile_chain(model, red, mode_fake)
            except Exception as e:
                return None, reasons + [f"compile_chain: {type(e).__name__}: {e}"]
        with mode_fake:
            out = model(*red)
            # reference output + our output + headroom for the reference module's
            # own temporaries, plus the inputs and any weights
            need = out.numel() * 4 * 3 + sum(
                t.numel() * 4 for t in red if isinstance(t, torch.Tensor))
            for nm in low.param_paths:
                p_ = dict(model.named_parameters()).get(nm)
                if p_ is None:
                    p_ = dict(model.named_buffers()).get(nm)
                if p_ is not None:
                    need += p_.numel() * 4
            fits = need <= budget
            out_shape, out_size = tuple(out.shape), out.numel()
        if fits:
            return Plan(task=task, low=low, key=f"t{task.num:03d}",
                        mode="full" if scale == 1 else "reduced", scale=scale,
                        out_size=out_size, out_shape=out_shape), reasons
        scale *= 2
    return None, reasons + ["does not fit in GPU memory at any scale"]


def eval_plan(p: Plan, inst) -> Optional[E.Result]:
    """Evaluate one plan. Returns `None` if it ran out of memory (the caller then
    retries at a smaller size)."""
    ref = new = None
    try:
        gc.collect()
        torch.cuda.empty_cache()
        init = p.task.module.get_init_inputs()
        ref = p.task.module.Model(*init).cuda().eval()
        # Convolution weights live in the reference module; the kernel reads the
        # very same tensors, so any mismatch is the kernel's.
        named = dict(ref.named_parameters())
        named.update(dict(ref.named_buffers()))
        params = [named[nm] for nm in p.low.param_paths]
        new = GeneratedModel(p.key, p.out_shape, p.low.tensor_arg_index, params)

        def make_inputs(p=p):
            raw = p.task.module.get_inputs()
            red = E.shrink(raw, p.scale)
            return [x.cuda().contiguous() if isinstance(x, torch.Tensor) else x
                    for x in red]

        r = E.check(ref, new, make_inputs)
        r.mode, r.scale = p.mode, p.scale
        return r
    except torch.OutOfMemoryError:
        return None
    except Exception as e:
        return E.Result(False, p.mode, f"{type(e).__name__}: {e}")
    finally:
        del ref, new
        gc.collect()
        torch.cuda.empty_cache()


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", default=None, help="comma-separated task numbers")
    ap.add_argument("--no-eval", action="store_true")
    ap.add_argument("--rounds", type=int, default=4,
                    help="retry rounds for tasks that run out of memory")
    args = ap.parse_args()

    tasks = all_tasks()
    if args.only:
        want = {int(x) for x in args.only.split(",")}
        tasks = [t for t in tasks if t.num in want]

    print(f"GPU: {torch.cuda.get_device_name()}   "
          f"usable {E.budget_bytes()/GB:.2f}GB")
    print(f"tasks: {len(tasks)}\n")

    min_scale: Dict[int, int] = {t.num: 1 for t in tasks}
    results: Dict[str, E.Result] = {}
    serial: List[str] = []
    verified: set = set()
    all_plans: Dict[str, Plan] = {}
    declined: List[Tuple[Any, List[str]]] = []
    pending = list(tasks)

    for rnd in range(max(1, args.rounds)):
        if not pending:
            break
        plans: List[Plan] = []
        declined = [] if rnd == 0 else declined
        for t in pending:
            try:
                p, reasons = make_plan(t, E.budget_bytes(), min_scale[t.num])
            except Exception as e:
                p, reasons = None, [f"{type(e).__name__}: {e}"]
            if p is None:
                if rnd == 0:
                    declined.append((t, reasons))
            else:
                plans.append(p)
                all_plans[p.key] = p
        if not plans:
            break

        if rnd == 0:
            print(f"[lower] {len(plans)} lowered, {len(declined)} declined")
        else:
            print(f"\n[round {rnd+1}] retrying {len(plans)} task(s) at a smaller size")

        instances = [
            C.Instance(
                key=p.key, low=p.low,
                block=(C.choose_block_red(p.low.K) if p.low.family == "genred"
                       else C.choose_block(p.out_size)),
                out_size=p.out_size)
            for p in plans]
        by_key = {i.key: i for i in instances}
        report = C.compile_all(instances, verbose=(rnd == 0))
        if not report["ok"]:
            print("\n[FAIL] certificates did not typecheck:")
            for e in report["proof_errors"][:20]:
                print("   ", e)
            if "emit_error" in report:
                print("   emit:", report["emit_error"][:800])
            sys.exit(1)
        verified |= set(report["emitted"])
        if rnd == 0:
            print(f"[proof] {len(verified)} certificates checked by Lean\n")
        if args.no_eval:
            _summary(list(all_plans.values()), verified, {}, declined, [], [])
            return

        retry: List[Any] = []
        for p in plans:
            if p.key not in verified:
                continue
            inst = by_key[p.key]
            if inst.serial:
                if p.key not in serial:
                    serial.append(p.key)
                    print(f"  SKIP  {p.task.label[:50]:50s}  verified; would run "
                          f"serially ({inst.nkb} iterations, {p.out_size} program(s))")
                continue
            r = eval_plan(p, inst)
            if r is None:
                min_scale[p.task.num] = p.scale * 2
                retry.append(p.task)
                print(f"  OOM   {p.task.label[:50]:50s}  at 1/{p.scale}; retrying smaller")
                continue
            results[p.key] = r
            flag = "PASS" if r.ok else "FAIL"
            extra = f" (1/{p.scale} size)" if p.scale > 1 else ""
            print(f"  {flag}  {p.task.label[:50]:50s}{extra}  {r.detail}")
        pending = retry

    _summary(list(all_plans.values()), verified, results, declined, serial, pending)


def _summary(plans, verified, results, declined, serial, unrun) -> None:
    total = len(plans) + len(declined)
    passing = [k for k, r in results.items() if r.ok]
    full = [k for k, r in results.items() if r.ok and r.scale == 1]
    print("\n" + "=" * 68)
    print(f"  L1 tasks                 {total}")
    print(f"  lowered to a spec        {len(plans)}")
    print(f"  certificates checked     {len(verified)}")
    if results:
        print(f"  matched PyTorch          {len(passing)}"
              f"   ({len(full)} at full size,"
              f" {len(passing)-len(full)} at reduced size)")
        if serial:
            print(f"  verified, not run        {len(serial)}"
                  f"   (would be serial: needs a two-stage reduction)")
        if unrun:
            print(f"  verified, out of memory  {len(unrun)}"
                  f"   (exceeds this GPU even at the smallest retried size)")
        bad = [(k, r) for k, r in results.items() if not r.ok]
        if bad:
            print(f"  mismatches               {len(bad)}")
            for k, r in bad[:10]:
                print(f"      {k}: {r.detail}")
    print("=" * 68)
    if declined:
        from collections import Counter
        c = Counter()
        for t, reasons in declined:
            r = (reasons[-1] if reasons else "?").split(": ", 1)[-1]
            c[r[:62]] += 1
        print("\nnot yet lowered, by reason:")
        for r, k in c.most_common(12):
            print(f"  {k:3d}  {r}")


if __name__ == "__main__":
    main()
