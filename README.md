# verified-kernel

Verified kernel uses neuro-symbolic AI to build kernels from pytorch source. 

## Layout

```
csrc/matmul.cu          tiled fp32 kernel + launcher
csrc/matmul.cpp         argument validation + pybind11 module
verified_kernel/        Python package
  matmul.py             matmul() interface, autograd wrapper
  _extension.py         AOT-or-JIT extension loader
tests/test_matmul.py    correctness vs torch.matmul
bench/bench_matmul.py   wall-clock comparison vs torch.matmul
```

## Usage

```python
import torch
import verified_kernel

A = torch.randn(512, 256, device="cuda")
B = torch.randn(256, 128, device="cuda")
C = verified_kernel.matmul(A, B)   # calls the CUDA kernel
```

`matmul` is an autograd `Function`, so it works inside a training graph. The
backward pass computes `dA = dC @ Bᵀ` and `dB = Aᵀ @ dC` with the same kernel,
so a kernel bug surfaces in gradients rather than being masked by cuBLAS.

### Supported inputs

2-D, float32, CUDA, same device, with `A.shape[1] == B.shape[0]`. Anything else
raises. Non-contiguous operands are copied. No batching, no mixed precision, no
`out=` — the contract is deliberately small.

## Building

No install step is required: the extension JIT-compiles on first call via
`torch.utils.cpp_extension.load` and is cached in the Torch extensions dir. Set
`VERIFIED_KERNEL_VERBOSE_BUILD=1` to see the compiler invocation.

For an ahead-of-time build:

```bash
pip install -e .          # requires a CUDA toolkit matching your torch build
```

## Testing and benchmarking

```bash
pytest tests/                    # skips entirely without a CUDA device
python -m bench.bench_matmul     # add --tf32 to let the reference use tensor cores
```

Both disable TF32 for `torch.matmul` by default so the reference accumulates in
true fp32. Tests compare at `rtol=1e-4, atol=1e-3`, far tighter than
KernelBench's `1e-2` default, but still a tolerance — the tiled kernel sums in a
different order than cuBLAS, so agreement is never bitwise.

## Kernel notes

`matmul_tiled_kernel` is the textbook shared-memory tiling: a 16×16 block
computes a 16×16 output tile, staging the matching A and B tiles in shared
memory so each loaded element is reused 16 times. Out-of-range lanes stage
zeros, which keeps the inner loop branch-free and keeps every thread reaching
both `__syncthreads()` barriers regardless of matrix size.

It is not competitive with cuBLAS — no register tiling, no vectorized loads, no
double buffering, no tensor cores. It is meant to be simple enough to state a
specification about.

