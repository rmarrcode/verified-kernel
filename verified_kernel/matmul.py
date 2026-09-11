"""PyTorch interface to the tiled CUDA matmul kernel."""

from __future__ import annotations

from typing import Any

import torch

from ._extension import load_extension


def _call_kernel(A: torch.Tensor, B: torch.Tensor) -> torch.Tensor:
    """Materialize contiguous operands and dispatch to the CUDA kernel.

    Argument validation lives in csrc/matmul.cpp; this only handles layout,
    which the kernel cannot express as a precondition on the caller.
    """
    return load_extension().matmul(A.contiguous(), B.contiguous())


class _MatmulFunction(torch.autograd.Function):
    """Autograd wrapper so the kernel composes with the rest of PyTorch.

    Both backward products are computed with the same kernel, so a bug in it
    shows up in gradients too rather than being masked by cuBLAS.
    """

    @staticmethod
    def forward(ctx: Any, A: torch.Tensor, B: torch.Tensor) -> torch.Tensor:
        ctx.save_for_backward(A, B)
        return _call_kernel(A, B)

    @staticmethod
    def backward(ctx: Any, grad_C: torch.Tensor):
        A, B = ctx.saved_tensors
        grad_A = grad_B = None
        if ctx.needs_input_grad[0]:
            # dA = dC @ B^T
            grad_A = _call_kernel(grad_C, B.t())
        if ctx.needs_input_grad[1]:
            # dB = A^T @ dC
            grad_B = _call_kernel(A.t(), grad_C)
        return grad_A, grad_B


def matmul(A: torch.Tensor, B: torch.Tensor) -> torch.Tensor:
    """Matrix product ``A @ B`` computed by the custom CUDA kernel.

    Drop-in for ``torch.matmul`` on the 2-D fp32 CUDA case only. Both operands
    must be 2-D float32 CUDA tensors on the same device with ``A.shape[1] ==
    B.shape[0]``; anything else raises. Non-contiguous inputs are copied.

    Note that the kernel accumulates in a different order than cuBLAS, so
    results agree with ``torch.matmul`` to floating-point tolerance, not bitwise.
    """
    return _MatmulFunction.apply(A, B)


def is_available() -> bool:
    """True if CUDA is present and the extension builds and loads."""
    if not torch.cuda.is_available():
        return False
    try:
        load_extension()
    except Exception:
        return False
    return True

