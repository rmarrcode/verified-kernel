"""Time the custom matmul against torch.matmul.

Usage (from the verified-kernel directory, so the package is importable):
    python -m bench.bench_matmul [--tf32]

Reports median wall-clock time per call measured with CUDA events. By default
TF32 is disabled so both sides do the same arithmetic; pass --tf32 to compare
against what PyTorch would actually do on an Ampere-or-newer device.
"""

from __future__ import annotations

import argparse
import statistics
from typing import Callable

import torch

import verified_kernel

SHAPES = [
    (512, 512, 512),
    (1024, 1024, 1024),
    (2048, 2048, 2048),
    (4096, 1024, 4096),
]


def time_ms(fn: Callable[[], torch.Tensor], warmup: int = 10, iters: int = 50) -> float:
    """Median time of one call, in milliseconds."""
    for _ in range(warmup):
        fn()
    torch.cuda.synchronize()

    samples = []
    start, end = torch.cuda.Event(enable_timing=True), torch.cuda.Event(enable_timing=True)
    for _ in range(iters):
        start.record()
        fn()
        end.record()
        torch.cuda.synchronize()
        samples.append(start.elapsed_time(end))
    return statistics.median(samples)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--tf32", action="store_true", help="let torch.matmul use TF32 tensor cores"
    )
    args = parser.parse_args()

    if not torch.cuda.is_available():
        raise SystemExit("no CUDA device available")
    torch.backends.cuda.matmul.allow_tf32 = args.tf32

    print(f"device: {torch.cuda.get_device_name()}   tf32 reference: {args.tf32}")
    print(f"{'M x K x N':>20}  {'ours (ms)':>10}  {'torch (ms)':>11}  {'speedup':>8}")

    for M, K, N in SHAPES:
        A = torch.randn(M, K, device="cuda", dtype=torch.float32)
        B = torch.randn(K, N, device="cuda", dtype=torch.float32)

        ours = time_ms(lambda: verified_kernel.matmul(A, B))
        theirs = time_ms(lambda: A @ B)
        print(f"{f'{M} x {K} x {N}':>20}  {ours:10.3f}  {theirs:11.3f}  {theirs / ours:7.2f}x")


if __name__ == "__main__":
    main()

