"""Evaluate one already-compiled kernel, in its own process.

Run out-of-process so that neither a memory leak nor a pathologically slow kernel
can affect the rest of the run: the orchestrator imposes a wall-clock timeout and
the OS reclaims the device on exit. Reads the plan the orchestrator recorded, so
the kernel being measured is the one whose certificate was checked.

    python harness/eval_one.py <plans.json> <key>

Prints one line: `RESULT <key> <pass|fail|oom|slow> <detail>`.
"""

from __future__ import annotations

import json
import os
import sys

import torch
import torch.fx

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "verified_kernel"))

import evaluate as E
from tasks import load, task_files
from vk.runtime import GeneratedModel, resolve_param

# `fx` names each literal tensor it lifts out of a forward `_tensor_constant<n>`.
CONST_PREFIX = "_tensor_constant"


def main() -> int:
    plans = json.load(open(sys.argv[1]))
    key = sys.argv[2]
    p = plans[key]

    num = p["num"]
    ent = [t for t in task_files() if t[0] == num]
    if not ent:
        print(f"RESULT {key} fail task {num} not found")
        return 0
    task = load(*ent[0])

    try:
        init = task.module.get_init_inputs()
        # KernelBench does not put the reference in eval mode, and for BatchNorm the
        # two modes compute different things (running statistics vs batch
        # statistics). Matching it keeps the measurement comparable -- and keeps the
        # reference consistent with what the frontend lowered.
        ref = task.module.Model(*init).cuda()
        named = dict(ref.named_parameters())
        named.update(dict(ref.named_buffers()))
        # `fx` lifts literal tensors in a forward into attributes named
        # `_tensor_constant*`, which are neither parameters nor registered buffers.
        # Their *numbering* is not stable: each trace installs a fresh attribute on
        # the root, so a model the frontend retried 17 lowerings against recorded
        # `_tensor_constant17` for what a clean trace calls `_tensor_constant0`. The
        # order they appear in is stable, so match on that rather than on the name.
        wanted = [nm for nm in p["param_paths"] if nm not in named
                  and nm.startswith(CONST_PREFIX)]
        const: dict = {}
        if wanted and p.get("consts"):
            # Recorded when the task was lowered: the values the certified spec
            # was built against, rather than a second trace that must agree with it.
            saved = torch.load(p["consts"])
            const = {nm: saved[nm].cuda() for nm in wanted}
        elif wanted:
            gm = torch.fx.symbolic_trace(ref)
            have = [n.target for n in gm.graph.nodes
                    if n.op == "get_attr" and str(n.target).startswith(CONST_PREFIX)]
            if len(have) != len(wanted):
                raise RuntimeError(
                    f"traced {len(have)} lifted constants, plan names {len(wanted)}")
            # These are installed by the trace itself, so they missed the
            # model's `.cuda()` and are still on the host.
            const = {nm: getattr(gm, tgt).cuda()
                     for nm, tgt in zip(wanted, have)}
        # A tied weight is listed by `named_parameters` once, under its other name;
        # `resolve_param` finds it in the module tree, and turns a fresh-draw path
        # into the draw.
        params = [const[nm] if nm in const else resolve_param(ref, nm, named)
                  for nm in p["param_paths"]]
        new = GeneratedModel(key, tuple(p["out_shape"]), p["tensor_arg_index"],
                             params, p.get("out_dtype"))

        def make_inputs():
            raw = task.module.get_inputs()
            red = E.shrink(raw, p["scale"])
            return [x.cuda().contiguous() if isinstance(x, torch.Tensor) else x
                    for x in red]

        r = E.check(ref, new, make_inputs)
        if r.ok:
            print(f"RESULT {key} pass max|diff|={r.max_diff:.3e}"
                  if r.max_diff is not None else f"RESULT {key} pass")
        else:
            print(f"RESULT {key} fail {r.detail}")
    except torch.OutOfMemoryError:
        print(f"RESULT {key} oom at 1/{p['scale']} size")
    except Exception as e:
        print(f"RESULT {key} fail {type(e).__name__}: {e}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
