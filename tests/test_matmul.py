"""Correctness tests for the tiled CUDA matmul against torch.matmul.

The reference is ``torch.matmul`` with TF32 disabled, so both sides accumulate
in true fp32 and the only remaining difference is summation order.
"""

from __future__ import annotations

import pytest
import torch

import verified_kernel

pytestmark = pytest.mark.skipif(
    not torch.cuda.is_available(), reason="requires a CUDA device"
)

# Summation order differs from cuBLAS, so agreement is to fp32 tolerance rather
# than bitwise. These bounds are far tighter than KernelBench's 1e-2 default.
RTOL = 1e-4
ATOL = 1e-3


@pytest.fixture(autouse=True)
def _exact_fp32_reference():
    """Force torch.matmul off TF32 for the duration of each test."""
    previous = torch.backends.cuda.matmul.allow_tf32
    torch.backends.cuda.matmul.allow_tf32 = False
    yield
    torch.backends.cuda.matmul.allow_tf32 = previous


def _randn(*shape: int) -> torch.Tensor:
    return torch.randn(*shape, device="cuda", dtype=torch.float32)


# Deliberately includes sizes that are not multiples of the 16-wide tile, in
# every dimension, since the boundary guards are the easiest thing to get wrong.
SHAPES = [
    (1, 1, 1),
    (16, 16, 16),
    (17, 17, 17),
    (1, 1, 1024),
    (31, 47, 63),
    (64, 64, 64),
    (128, 256, 512),
    (255, 129, 33),
]


@pytest.mark.parametrize("M,K,N", SHAPES)
def test_matches_torch_matmul(M: int, K: int, N: int) -> None:
    A, B = _randn(M, K), _randn(K, N)
    torch.testing.assert_close(
        verified_kernel.matmul(A, B), A @ B, rtol=RTOL, atol=ATOL
    )


def test_accepts_non_contiguous_inputs() -> None:
    A = _randn(64, 96).t()  # (96, 64) via transpose
    B = _randn(64, 64)[:, :32]  # (64, 32) via slicing
    assert not A.is_contiguous() and not B.is_contiguous()
    torch.testing.assert_close(
        verified_kernel.matmul(A, B), A @ B, rtol=RTOL, atol=ATOL
    )


def test_empty_contraction_is_zero() -> None:
    A, B = _randn(8, 0), _randn(0, 8)
    torch.testing.assert_close(verified_kernel.matmul(A, B), torch.zeros(8, 8).cuda())


@pytest.mark.parametrize("shape", [(0, 8), (8, 0)])
def test_empty_output(shape: tuple[int, int]) -> None:
    M, N = shape
    out = verified_kernel.matmul(_randn(M, 4), _randn(4, N))
    assert out.shape == (M, N)


def test_backward_matches_autograd() -> None:
    A = _randn(48, 80).requires_grad_()
    B = _randn(80, 33).requires_grad_()
    A_ref = A.detach().clone().requires_grad_()
    B_ref = B.detach().clone().requires_grad_()

    grad_out = _randn(48, 33)
    verified_kernel.matmul(A, B).backward(grad_out)
    (A_ref @ B_ref).backward(grad_out)

    torch.testing.assert_close(A.grad, A_ref.grad, rtol=RTOL, atol=ATOL)
    torch.testing.assert_close(B.grad, B_ref.grad, rtol=RTOL, atol=ATOL)


# Operands are built lazily: parametrize arguments are evaluated at collection
# time, which happens even on machines where the CUDA skip applies.
BAD_INPUTS = {
    "cpu_tensor": (
        lambda: torch.randn(4, 4),
        lambda: _randn(4, 4),
        "must be a CUDA tensor",
    ),
    "wrong_dtype": (
        lambda: _randn(4, 4).double(),
        lambda: _randn(4, 4),
        "must be float32",
    ),
    "wrong_rank": (lambda: _randn(2, 4, 4), lambda: _randn(4, 4), "must be 2-D"),
    "shape_mismatch": (lambda: _randn(4, 5), lambda: _randn(4, 4), "shape mismatch"),
}


@pytest.mark.parametrize("case", list(BAD_INPUTS), ids=list(BAD_INPUTS))
def test_rejects_bad_inputs(case: str) -> None:
    make_a, make_b, message = BAD_INPUTS[case]
    with pytest.raises(RuntimeError, match=message):
        verified_kernel.matmul(make_a(), make_b())

