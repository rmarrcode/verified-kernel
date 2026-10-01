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


class FreshNormal:
    """An input the kernel reads that is drawn afresh, from PyTorch's generator, on
    every call -- a `torch.randn` in the reference's forward. The draw is outside
    the verified core, as it is outside the reference's arithmetic."""

    def __init__(self, shape: Tuple[int, ...]):
        self.shape = tuple(shape)


def resolve_param(module: nn.Module, name: str, named=None):
    """The tensor a lowering's parameter path names: a parameter or buffer, a tied
    weight under its other name, or a fresh draw."""
    if name.startswith("__randn__/"):
        return FreshNormal(tuple(int(d) for d in name.rsplit(":", 1)[1].split(",") if d))
    if named is not None and name in named:
        return named[name]
    obj = module
    for part in name.split("."):
        obj = getattr(obj, part)
    return obj


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
        dev = ins[0].device if ins else torch.device("cuda")
        for j, p in enumerate(self.extra):
            if isinstance(p, FreshNormal):
                ins.append(torch.randn(p.shape, device=dev, dtype=torch.float32))
            else:
                ins.append(_check(p, f"parameter {j}"))
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
    if t.dtype in (torch.float16, torch.bfloat16):
        # Every half- or bfloat16 value is exactly a float32 value, so widening is
        # the identity on what the tensor denotes. (Narrowing would not be.)
        return t.to(torch.float32).contiguous()
    if t.dtype is not torch.float32:
        raise RuntimeError(f"{what} is {t.dtype}, expected float32 (or bool/int/half)")
    return t.contiguous()
