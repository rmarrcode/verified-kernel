"""Loading a generated kernel and presenting it as a `torch.nn.Module`.

Thin by design: all this does is allocate the output, hand the input pointers to
the generated launcher, and reshape. Any logic here would be logic outside the
verified core.
"""

from __future__ import annotations

import importlib.util
import os
from typing import Any, List, Optional, Sequence, Tuple

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
                 params: Sequence[torch.Tensor] = (),
                 out_dtype: Optional[str] = None):
        super().__init__()
        self.launch = load_kernel(key)
        self.out_shape = tuple(out_shape)
        self.tensor_arg_index = list(tensor_arg_index)
        # Module state promoted to input buffers (convolution weights and bias).
        # Held by reference to the reference module's tensors so the comparison
        # tests the kernel rather than an initialisation difference.
        self.extra = [p for p in params]
        # The kernel always writes float32. An argmax's result is an integer index,
        # and the cast back is exact -- indices here are far below 2^24, where
        # float32 represents every integer.
        self.out_dtype = getattr(torch, out_dtype) if out_dtype else None

    def forward(self, *args: Any) -> torch.Tensor:
        ins: List[torch.Tensor] = []
        for i in self.tensor_arg_index:
            ins.append(_check(args[i], f"input {i}"))
        for j, p in enumerate(self.extra):
            ins.append(_check(p, f"parameter {j}"))
        dev = ins[0].device if ins else torch.device("cuda")
        out = torch.empty(self.out_shape, device=dev, dtype=torch.float32)
        self.launch(out, ins)
        return out.to(self.out_dtype) if self.out_dtype is not None else out


def _check(t: torch.Tensor, what: str) -> torch.Tensor:
    if not isinstance(t, torch.Tensor):
        raise RuntimeError(f"{what} is {type(t).__name__}, expected a Tensor")
    if not t.is_cuda:
        raise RuntimeError(f"{what} is on {t.device}, expected CUDA")
    if t.dtype is torch.bool:
        # A boolean mask denotes 0 and 1, and `False -> 0.0`, `True -> 1.0` is an
        # exact embedding into the reals the spec quantifies over -- which is also
        # what PyTorch does when such a tensor meets a float in an arithmetic op.
        # Every other dtype is refused rather than coerced: an int64 conversion
        # would be lossy above 2^24, and a float64 one changes the arithmetic.
        return t.to(torch.float32).contiguous()
    if t.dtype in (torch.int32, torch.int64):
        # Integer labels denote exactly the integers the spec quantifies over.
        # float32 represents every integer below 2^24; rather than assume the
        # values are in range, check the round trip -- it is one cheap comparison
        # against silently wrong answers.
        f = t.to(torch.float32)
        if not torch.equal(f.to(t.dtype), t):
            raise RuntimeError(
                f"{what} has integer values that float32 cannot represent exactly")
        return f.contiguous()
    if t.dtype is not torch.float32:
        raise RuntimeError(f"{what} is {t.dtype}, expected float32 (or bool/int)")
    return t.contiguous()
