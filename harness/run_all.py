"""Orchestrate the whole Level 1 run: lower, certify, then evaluate each kernel in
its own process under a timeout.

    python harness/run_all.py [--only 1,19] [--timeout 180]

Reports three distinct numbers, which must not be conflated:

  lowered     the frontend produced a specification from the PyTorch module.
  certified   Lean accepted the correctness certificate for that specification at
              the exact block size and grid the generator chose. This is
              shape-generic, so it covers the task at its declared size.
  matched     the emitted Triton kernel also agreed with PyTorch on this GPU,
              under KernelBench's criterion (5 trials, allclose at 1e-2).

`matched` is bounded by the hardware, not by the proof: 34 of the 100 L1 tasks
need 18-24GB for their inputs and both outputs, so on a 12GB card they are run at
a reduced leading dimension. Each reduced run is separately lowered and certified
at the size it runs, so nothing is verified at one shape and measured at another.
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from typing import Dict, List, Optional, Tuple

import torch

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "verified_kernel"))

import evaluate as E
from run_l1 import Plan, make_plan
from tasks import all_tasks
from vk import compile as C

HERE = os.path.dirname(os.path.abspath(__file__))
GB = 1024 ** 3


def build(plans: List[Plan], verbose: bool = True) -> Tuple[set, Dict[str, C.Instance]]:
    instances = [
        C.Instance(
            key=p.key, low=p.low,
            block=(C.choose_block_red(p.low.K) if p.low.family == "genred"
                   else C.choose_block(p.out_size)),
            out_size=p.out_size)
        for p in plans]
    report = C.compile_all(instances, verbose=verbose)
    if not report["ok"]:
        print("\n[FAIL] certificates did not typecheck:")
        for e in report["proof_errors"][:20]:
            print("   ", e)
        if "emit_error" in report:
            print("   emit:", report["emit_error"][:1500])
        sys.exit(1)
    return set(report["emitted"]), {i.key: i for i in instances}


def dump_plans(plans: List[Plan], path: str, acc: Dict[str, dict]) -> None:
    """Record each plan so the evaluation subprocess measures the kernel whose
    certificate was checked.

    Accumulates across retry rounds and writes through a context manager: a later
    round must not be able to drop an earlier round's entry, and the file must be
    flushed before any subprocess reads it.
    """
    for p in plans:
        acc[p.key] = {"num": p.task.num, "scale": p.scale, "mode": p.mode,
                      "out_shape": list(p.out_shape),
                      "tensor_arg_index": list(p.low.tensor_arg_index),
                      "param_paths": list(p.low.param_paths),
                      "out_dtype": p.low.out_dtype}
    with open(path, "w") as f:
        json.dump(acc, f)
        f.flush()
        os.fsync(f.fileno())


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", default=None)
    ap.add_argument("--timeout", type=int, default=240,
                    help="seconds per task before it is recorded as too slow")
    ap.add_argument("--rounds", type=int, default=3)
    args = ap.parse_args()

    tasks = all_tasks()
    if args.only:
        want = {int(x) for x in args.only.split(",")}
        tasks = [t for t in tasks if t.num in want]

    print(f"GPU: {torch.cuda.get_device_name()}   usable {E.budget_bytes()/GB:.2f}GB")
    print(f"L1 tasks: {len(tasks)}\n", flush=True)

    min_scale = {t.num: 1 for t in tasks}
    declined: List[Tuple[object, List[str]]] = []
    verdict: Dict[str, Tuple[str, str]] = {}
    labels: Dict[str, str] = {}
    scales: Dict[str, int] = {}
    certified: set = set()
    pending = list(tasks)
    plan_path = os.path.join(HERE, "_plans.json")
    plan_acc: Dict[str, dict] = {}

    for rnd in range(max(1, args.rounds)):
        if not pending:
            break
        plans: List[Plan] = []
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
                labels[p.key] = t.label
                scales[p.key] = p.scale
        if not plans:
            break

        if rnd == 0:
            print(f"[lower] {len(plans)} of {len(tasks)} lowered to a spec "
                  f"({len(declined)} declined)", flush=True)
        else:
            print(f"\n[round {rnd+1}] retrying {len(plans)} task(s) smaller", flush=True)

        emitted, insts = build(plans, verbose=(rnd == 0))
        certified |= emitted
        if rnd == 0:
            print(f"[proof] {len(certified)} certificates checked by Lean\n", flush=True)
        dump_plans(plans, plan_path, plan_acc)

        retry = []
        for p in plans:
            if p.key not in emitted:
                continue
            inst = insts[p.key]
            if inst.serial:
                verdict[p.key] = ("serial", f"{inst.nkb} iterations over "
                                            f"{p.out_size} program(s)")
                print(f"  SKIP  {labels[p.key][:52]:52s} verified; would run serially",
                      flush=True)
                continue
            line = ""
            try:
                proc = subprocess.run(
                    [sys.executable, os.path.join(HERE, "eval_one.py"), plan_path, p.key],
                    capture_output=True, text=True, timeout=args.timeout)
                for ln in proc.stdout.splitlines():
                    if ln.startswith("RESULT "):
                        line = ln
            except subprocess.TimeoutExpired:
                verdict[p.key] = ("slow", f"exceeded {args.timeout}s")
                print(f"  SLOW  {labels[p.key][:52]:52s} verified; exceeded "
                      f"{args.timeout}s", flush=True)
                continue
            if not line:
                tail = (proc.stderr or proc.stdout).strip().splitlines()
                verdict[p.key] = ("fail", tail[-1][:200] if tail else "no result line")
                print(f"  ERR   {labels[p.key][:52]:52s} {verdict[p.key][1][:70]}",
                      flush=True)
                continue
            _, _, status, *rest = line.split(" ", 3) + [""]
            detail = rest[0] if rest else ""
            if status == "oom":
                min_scale[p.task.num] = p.scale * 2
                retry.append(p.task)
                print(f"  OOM   {labels[p.key][:52]:52s} at 1/{p.scale}; retrying",
                      flush=True)
                continue
            verdict[p.key] = (status, detail)
            tag = "PASS" if status == "pass" else "FAIL"
            extra = f" (1/{p.scale})" if p.scale > 1 else ""
            print(f"  {tag}  {labels[p.key][:52]:52s}{extra}  {detail[:60]}", flush=True)
        pending = retry

    # ---- summary ----------------------------------------------------------
    npass = [k for k, (st, _) in verdict.items() if st == "pass"]
    full = [k for k in npass if scales[k] == 1]
    nfail = [(k, d) for k, (st, d) in verdict.items() if st == "fail"]
    nserial = [k for k, (st, _) in verdict.items() if st == "serial"]
    nslow = [k for k, (st, _) in verdict.items() if st == "slow"]
    unrun = [t.num for t in pending]

    print("\n" + "=" * 70)
    print(f"  KernelBench Level 1                     {len(tasks)}")
    print(f"  lowered to a specification              {len(labels)}")
    print(f"  correctness certificate checked by Lean {len(certified)}")
    print(f"  matched PyTorch on this GPU             {len(npass)}"
          f"   ({len(full)} at declared size, {len(npass)-len(full)} reduced)")
    if nfail:
        print(f"  mismatched or errored                   {len(nfail)}")
    if nserial:
        print(f"  certified, not run (serial)             {len(nserial)}")
    if nslow:
        print(f"  certified, not run (too slow)           {len(nslow)}")
    if unrun:
        print(f"  certified, out of memory                {len(unrun)}")
    print("=" * 70)

    if nfail:
        print("\nmismatches:")
        for k, d in nfail:
            print(f"  {labels.get(k,k)}: {d[:150]}")
    if declined:
        from collections import Counter
        c = Counter()
        for t, reasons in declined:
            r = (reasons[-1] if reasons else "?").split(": ", 1)[-1]
            c[r[:64]] += 1
        print(f"\nnot yet lowered ({len(declined)} tasks), by reason:")
        for r, n in c.most_common(14):
            print(f"  {n:3d}  {r}")


if __name__ == "__main__":
    main()
