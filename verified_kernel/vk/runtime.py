"""Loading a generated kernel and presenting it as a `torch.nn.Module`.

Thin by design: all this does is allocate the output, hand the input pointers to
the generated launcher, and reshape. Any logic here would be logic outside the
verified core.
"""

from __future__ import annotations

import importlib.util
import os
from typing import Any, List, Sequence, Tuple

import torch
import torch.nn as nn

GEN_PY = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
    "generated")


def load_kernel(key: str):
    """Import `generated/<key>.py` and return its launcher function."""
    path = os.path.join(GEN_PY, f"{key}.py")
    spec = importlib.util.spec_from_file_location(f"vk_gen_{key}", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return getattr(mod, key)


class GeneratedModel(nn.Module):
    """Wraps a generated kernel with the interface KernelBench expects."""

    def __init__(self, key: str, out_shape: Tuple[int, ...],
                 tensor_arg_index: Sequence[int],
                 params: Sequence[torch.Tensor] = ()):
        super().__init__()
        self.launch = load_kernel(key)
        self.out_shape = tuple(out_shape)
        self.tensor_arg_index = list(tensor_arg_index)
        # Module state promoted to input buffers (convolution weights and bias).
        # Held by reference to the reference module's tensors so the comparison
        # tests the kernel rather than an initialisation difference.
        self.extra = [p for p in params]

    def forward(self, *args: Any) -> torch.Tensor:
        ins: List[torch.Tensor] = []
        for i in self.tensor_arg_index:
            ins.append(_check(args[i], f"input {i}"))
        for j, p in enumerate(self.extra):
            ins.append(_check(p, f"parameter {j}"))
        dev = ins[0].device if ins else torch.device("cuda")
        out = torch.empty(self.out_shape, device=dev, dtype=torch.float32)
        self.launch(out, ins)
        return out


def _check(t: torch.Tensor, what: str) -> torch.Tensor:
    if not isinstance(t, torch.Tensor):
        raise RuntimeError(f"{what} is {type(t).__name__}, expected a Tensor")
    if not t.is_cuda:
        raise RuntimeError(f"{what} is on {t.device}, expected CUDA")
    if t.dtype is not torch.float32:
        raise RuntimeError(f"{what} is {t.dtype}, expected float32")
    return t.contiguous()
