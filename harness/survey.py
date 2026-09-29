"""Report, for every L1 task, whether the frontend can lower it and what it costs
to run. This is the project's progress meter."""

from __future__ import annotations

import sys

import torch

from tasks import all_tasks, fake_instance, out_bytes
from vk import frontend

GB = 1024 ** 3


def main() -> None:
    ok, fail = [], []
    for t in all_tasks():
        try:
            mode, model, inputs = fake_instance(t)
            with mode:
                low, reasons = frontend.lower(model, list(inputs))
        except Exception as e:
            low, reasons = None, [f"load: {type(e).__name__}: {e}"]
        nb = out_bytes(t)
        mem = f"{nb/GB:5.2f}GB" if nb else "   ?  "
        if low is not None:
            ok.append((t, low, nb))
            print(f"  OK  {t.label[:52]:52s} {mem}  {low.family} arity={low.arity} n={low.out_size}")
        else:
            fail.append((t, reasons, nb))

    print(f"\n=== lowered {len(ok)}/{len(ok)+len(fail)} ===\n")
    from collections import Counter
    c = Counter()
    for t, reasons, nb in fail:
        r = reasons[-1] if reasons else "?"
        r = r.split(": ", 1)[-1]
        c[r[:70]] += 1
    for r, k in c.most_common(30):
        print(f"  {k:3d}  {r}")


if __name__ == "__main__":
    main()
