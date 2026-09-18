"""PyTorch interface to the tiled Triton matmul kernel."""

from __future__ import annotations

from typing import Any

import torch
import triton
import triton.language as tl


@triton.jit
def _matmul_kernel(
    A,
    B,
    C,
    M: tl.constexpr,
    N: tl.constexpr,
    K: tl.constexpr,
    BLOCK: tl.constexpr,
):
    pid_m = tl.program_id(0)
    pid_n = tl.program_id(1)

    offs_m = pid_m * BLOCK + tl.arange(0, BLOCK)
    offs_n = pid_n * BLOCK + tl.arange(0, BLOCK)
    offs_k = tl.arange(0, BLOCK)

    acc = tl.zeros((BLOCK, BLOCK), dtype=tl.float32)
    for k0 in range(0, K, BLOCK):
        k = k0 + offs_k
        a = tl.load(
            A + offs_m[:, None] * K + k[None, :],
            mask=(offs_m[:, None] < M) & (k[None, :] < K),
            other=0.0,
        )
        b = tl.load(
            B + k[:, None] * N + offs_n[None, :],
            mask=(k[:, None] < K) & (offs_n[None, :] < N),
            other=0.0,
        )
        acc += tl.dot(a, b, input_precision="ieee")

    tl.store(
        C + offs_m[:, None] * N + offs_n[None, :],
        acc,
        mask=(offs_m[:, None] < M) & (offs_n[None, :] < N),
    )


def _check_inputs(A: torch.Tensor, B: torch.Tensor) -> None:
    if not A.is_cuda:
        raise RuntimeError(f"matmul: A must be a CUDA tensor, got {A.device}")
    if not B.is_cuda:
        raise RuntimeError(f"matmul: B must be a CUDA tensor, got {B.device}")
    if A.device != B.device:
        raise RuntimeError(
            f"matmul: A and B must be on the same device, got {A.device} and {B.device}"
        )
    if A.dtype is not torch.float32:
        raise RuntimeError(f"matmul: A must be float32, got {A.dtype}")
    if B.dtype is not torch.float32:
        raise RuntimeError(f"matmul: B must be float32, got {B.dtype}")
    if A.dim() != 2:
        raise RuntimeError(f"matmul: A must be 2-D, got {A.dim()}-D")
    if B.dim() != 2:
        raise RuntimeError(f"matmul: B must be 2-D, got {B.dim()}-D")
    if A.shape[1] != B.shape[0]:
        raise RuntimeError(f"matmul: shape mismatch, A is {A.shape} and B is {B.shape}")


def _call_kernel(A: torch.Tensor, B: torch.Tensor) -> torch.Tensor:
    """Materialize contiguous operands and dispatch to the Triton kernel.

    The Triton kernel indexes row-major contiguous tensors directly, so
    non-contiguous inputs are copied before launch.
    """
    _check_inputs(A, B)
    A = A.contiguous()
    B = B.contiguous()
    M, K = A.shape
    _, N = B.shape
    C = torch.empty((M, N), device=A.device, dtype=A.dtype)

    if M == 0 or N == 0:
        return C
    if K == 0:
        return torch.zeros_like(C)

    block = 16
    grid = (triton.cdiv(M, block), triton.cdiv(N, block))
    _matmul_kernel[grid](A, B, C, M, N, K, BLOCK=block)
    return C


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
    """Matrix product ``A @ B`` computed by the custom Triton kernel.

    Drop-in for ``torch.matmul`` on the 2-D fp32 CUDA case only. Both operands
    must be 2-D float32 CUDA tensors on the same device with ``A.shape[1] ==
    B.shape[0]``; anything else raises. Non-contiguous inputs are copied.

    Note that the kernel accumulates in a different order than cuBLAS, so
    results agree with ``torch.matmul`` to floating-point tolerance, not bitwise.
    """
    return _MatmulFunction.apply(A, B)


def is_available() -> bool:
    """True if CUDA and Triton are available."""
    if not torch.cuda.is_available():
        return False
    try:
        import triton  # noqa: F401
    except Exception:
        return False
    return True
