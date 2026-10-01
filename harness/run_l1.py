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
#: The fraction of free device memory `evaluate.budget_bytes` hands out.
BUDGET_FRAC = 0.60
#: The fraction of free memory weights may occupy before the activations' margin.
WEIGHT_FRAC = 0.92


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
    prev_shapes = None
    while scale <= (1 << 24):
        mode_fake, model, inputs = fake_instance(task)
        with mode_fake:
            red = E.shrink(list(inputs), scale)
            shapes_now = [tuple(t.shape) for t in red if isinstance(t, torch.Tensor)]
            if shapes_now == prev_shapes:
                # Shrinking no longer changes anything -- the batch is already
                # one -- so no size this card can run exists. The lowering at this
                # size is still certified; it is reported as not runnable here,
                # not as not lowered.
                return Plan(task=task, low=last_low, key=f"t{task.num:03d}",
                            mode="nofit", scale=scale // 2,
                            out_size=last_out[1], out_shape=last_out[0]), reasons
            prev_shapes = shapes_now
            low, reasons = frontend.lower(model, red)
        if low is None:
            # A single-operator lowering did not apply; compile the whole graph as
            # a chain of stages instead.
            try:
                low = graph.compile_chain(model, red, mode_fake)
            except Exception as e:
                return None, reasons + [f"compile_chain: {type(e).__name__}: {e}"]
        with mode_fake:
            try:
                out = model(*red)
            except Exception:
                # A forward that reads a value back (`.item()`) cannot run on fake
                # tensors. The lowering has already derived the output's shape
                # from the trace, which is all this needs.
                out = torch.empty(tuple(low.out_shape), dtype=torch.float32)
            # reference output + our output + headroom for the reference module's
            # own temporaries, plus the inputs
            need = out.numel() * 4 * 3 + sum(
                t.numel() * 4 for t in red if isinstance(t, torch.Tensor))
            # A chain's intermediates count too. A model that broadcasts a table to
            # the whole batch before selecting from it -- Reformer's axial
            # position embedding -- is decided by this term.
            if low.family == "chain":
                # The launcher allocates each intermediate when its stage runs and
                # releases it after its last reader, so what counts is the most
                # alive at once.
                from vk.compile import chain_lifetimes
                need += 4 * chain_lifetimes(low)[1]
            wbytes = 0
            for nm in low.param_paths:
                p_ = dict(model.named_parameters()).get(nm)
                if p_ is None:
                    p_ = dict(model.named_buffers()).get(nm)
                if p_ is None:
                    p_ = getattr(model, nm, None)
                if p_ is not None:
                    # The kernel reads float32. A half-precision weight is widened
                    # (exactly) into a copy, so the reference's tensor and the copy
                    # are both resident.
                    extra = p_.element_size() if p_.dtype != torch.float32 else 0
                    wbytes += p_.numel() * (4 + extra)
            # `budget` is a fraction of free memory, and the margin it leaves is
            # for what cannot be estimated: the reference's temporaries, which
            # scale with the activations. Weights are exact and shared -- the kernel
            # reads the reference's own tensors -- so they need no margin. Without
            # this a model whose weights alone exceed the fraction (a 2G-parameter
            # MLP) is refused even though weights plus activations fit.
            free = budget / BUDGET_FRAC
            fits = (need + wbytes <= budget
                    or need <= BUDGET_FRAC * (WEIGHT_FRAC * free - wbytes))
            out_shape, out_size = tuple(out.shape), out.numel()
            if out.dtype in (torch.float16, torch.bfloat16) and low.out_dtype is None:
                # A reduced-precision reference is compared at its own precision:
                # the kernel computes in float32 and its result is rounded to the
                # reference's dtype on the way out.
                low.out_dtype = str(out.dtype).replace("torch.", "")
        if fits:
            # A "reduction" that changed nothing -- the batch was already one -- is
            # the declared size, and is reported as such.
            same = [tuple(t.shape) for t in inputs if isinstance(t, torch.Tensor)] \
                == shapes_now
            eff = 1 if same else scale
            return Plan(task=task, low=low, key=f"t{task.num:03d}",
                        mode="full" if eff == 1 else "reduced", scale=eff,
                        out_size=out_size, out_shape=out_shape), reasons
        last_low, last_out = low, (out_shape, out_size)
        if wbytes > WEIGHT_FRAC * free:
            # The weights alone exceed the device, and shrinking the batch does not
            # shrink them. The lowering is still a lowering and its certificate
            # still checks; what cannot happen here is running it. Certify at
            # the declared size and say so, rather than re-lowering at two dozen
            # sizes that cannot help.
            return Plan(task=task, low=low, key=f"t{task.num:03d}", mode="nofit",
                        scale=scale, out_size=out_size, out_shape=out_shape), reasons
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
