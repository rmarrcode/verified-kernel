"""Loading KernelBench tasks and lowering them, without allocating anything.

L1 shapes are large -- several tasks have outputs in the billions of elements --
so every shape-level question is answered under `FakeTensorMode`. Real memory is
only touched when a kernel is actually evaluated.
"""

from __future__ import annotations

import importlib.util
import os
import re
import sys
from dataclasses import dataclass
from typing import Any, List, Optional, Tuple

import torch

KB_DIR = os.environ.get(
    "KERNELBENCH_DIR",
    "/tmp/claude-1000/-home-ryan-marr-Documents-secret-verified-kernel-env-verified-kernel/"
    "8e88b58b-3a38-4986-8961-f70d371a08ff/scratchpad/kb")
L1 = os.path.join(KB_DIR, "KernelBench", "level1")

_REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _REPO not in sys.path:
    sys.path.insert(0, _REPO)
sys.path.insert(0, os.path.join(_REPO, "verified_kernel"))


@dataclass
class Task:
    num: int
    name: str
    path: str
    module: Any

    @property
    def label(self) -> str:
        return f"L1/{self.num:03d} {self.name}"


def task_files() -> List[Tuple[int, str, str]]:
    out = []
    for fn in os.listdir(L1):
        if not fn.endswith(".py"):
            continue
        m = re.match(r"(\d+)_(.*)\.py$", fn)
        if not m:
            continue
        out.append((int(m.group(1)), m.group(2), os.path.join(L1, fn)))
    return sorted(out)


def load(num: int, name: str, path: str) -> Task:
    spec = importlib.util.spec_from_file_location(f"kb_l1_{num}", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return Task(num=num, name=name, path=path, module=mod)


def all_tasks() -> List[Task]:
    return [load(n, nm, p) for n, nm, p in task_files()]


def fake_instance(task: Task):
    """Instantiate the model and its inputs as fake tensors (shapes only)."""
    from torch._subclasses.fake_tensor import FakeTensorMode
    mode = FakeTensorMode(allow_non_fake_inputs=True)
    with mode:
        init = task.module.get_init_inputs()
        model = task.module.Model(*init)
        inputs = task.module.get_inputs()
    return mode, model, inputs


def out_bytes(task: Task) -> Optional[int]:
    """Total bytes of inputs + output in fp32, or None if unknown."""
    try:
        mode, model, inputs = fake_instance(task)
        with mode:
            out = model(*inputs)
        tot = 0
        for t in list(inputs) + [out]:
            if isinstance(t, torch.Tensor):
                tot += t.numel() * 4
        return tot
    except Exception:
        return None
