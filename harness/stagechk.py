"""Find the first stage of a chain whose buffer disagrees with the graph it came from.

    KB_LEVEL=4 python harness/stagechk.py <task number>

Runs the *rewritten, traced graph* the chain was lowered from on real tensors, and
compares every stage's buffer against the value of the node that stage holds. It
also compares that graph's output against the reference module itself, which
separates a tracing or rewriting error (the graph is not the model) from a lowering
error (a stage is not its node). Uses the plan the last run recorded, so it checks
the kernel that was measured. Nothing here is part of any certificate.
"""

from __future__ import annotations

import copy
import json
import math
import os
import sys

import torch
import torch.fx as fx

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(os.path.dirname(HERE), "verified_kernel"))

import evaluate as E
from tasks import load, task_files
from run_l1 import make_plan
from vk import graph
from vk.runtime import load_kernel

torch.backends.cuda.matmul.allow_tf32 = False
torch.backends.cudnn.allow_tf32 = False


def main() -> None:
    num = int(sys.argv[1])
    key = f"t{num:03d}"
    rec = json.load(open(os.path.join(HERE, "_plans.json")))[key]
    task = load(*[t for t in task_files() if t[0] == num][0])
    p, _ = make_plan(task, E.budget_bytes(), rec["scale"])
    low = p.low

    torch.manual_seed(0)
    ref = task.module.Model(*task.module.get_init_inputs()).cuda()
    named = dict(ref.named_parameters())
    named.update(dict(ref.named_buffers()))
    consts = torch.load(rec["consts"]) if rec.get("consts") else {}

    def resolve(nm):
        if nm in named:
            return named[nm]
        if nm in consts:
            return consts[nm].cuda()
        obj = ref
        for part in nm.split("."):
            obj = getattr(obj, part)
        return obj
    prm = [resolve(nm) for nm in low.param_paths]

    torch.manual_seed(1234)
    xs = [x.cuda().contiguous() if isinstance(x, torch.Tensor) else x
          for x in E.shrink(task.module.get_inputs(), rec["scale"])]

    # the graph the lowering saw, over the reference's own parameters
    from torch._subclasses.fake_tensor import FakeTensorMode
    mode = FakeTensorMode(allow_non_fake_inputs=True)
    twin = copy.deepcopy(ref).cpu()       # traced beside fake CPU inputs
    with mode:
        fake = [torch.empty(x.shape, dtype=x.dtype) if isinstance(x, torch.Tensor) else x
                for x in xs]
    gm, _ = graph.prepare_graph(twin, fake, mode)
    for n in gm.graph.nodes:              # constants the trace lifted, real-valued
        if n.op == "get_attr" and n.target in consts:
            setattr(gm, n.target, consts[n.target].cuda())
    gm = gm.cuda()

    vals = {}

    class Rec(fx.Interpreter):
        def call_method(self, target, args, kwargs):
            # `.to(device)` was traced with the device the shape tracer reports
            # (the CPU); the lowering treats it as the relabelling it is.
            if target == "to":
                return args[0]
            return super().call_method(target, args, kwargs)

        def run_node(self, n):
            r = super().run_node(n)
            # tensors the forward creates (`ones`, `arange`) were traced on the CPU
            if isinstance(r, torch.Tensor) and not r.is_cuda:
                r = r.cuda()
            if isinstance(r, tuple) and r and isinstance(r[0], torch.Tensor):
                vals[n.name] = r[0]
            elif isinstance(r, torch.Tensor):
                vals[n.name] = r
            return r

    with torch.no_grad():
        g_out = Rec(gm).run(*[x for x in xs])
        m_out = ref(*xs)
    if isinstance(g_out, (tuple, list)):
        g_out = g_out[0]
    d = (g_out.float() - m_out.float()).abs().max().item()
    print(f"graph vs module: max|diff| {d:.3e}  (|v|max {m_out.abs().max().item():.3e})")

    kept, real = [], torch.empty

    def spy(*a, **k):
        r = real(*a, **k)
        kept.append(r)
        return r
    launch = load_kernel(key)
    out = real(tuple(low.out_shape), device="cuda", dtype=torch.float32)
    ins = []
    for i in low.tensor_arg_index:
        t = xs[i]
        ins.append(t.float().contiguous() if t.dtype != torch.float32 else t)
    ins += [t.float().contiguous() for t in prm]
    torch.empty = spy
    try:
        with torch.no_grad():
            launch(out, ins)
    finally:
        torch.empty = real
    bufs = kept[:len(low.stages) - 1] + [out]

    bad = 0
    for j, nm in enumerate(low.stage_nodes):
        if nm not in vals or j >= len(bufs):
            continue
        v = vals[nm].float()
        b = bufs[j]
        if b.numel() != v.numel():
            continue
        diff = (b.reshape(-1) - v.reshape(-1)).abs().max().item()
        scale = v.abs().max().item()
        if diff > 1e-3 * max(scale, 1.0):
            print(f"  stage {j:4d} {low.stage_src[j]} -> {nm}: max|diff| {diff:.3e} "
                  f"|v|max {scale:.3e}   {(low.stages[j].notes[:1] or [''])[0][:70]}")
            bad += 1
            if bad >= 6:
                break
    print(f"  {bad} stage(s) reported" if bad else "  every comparable stage agrees")


if __name__ == "__main__":
    main()
