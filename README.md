# verified-kernel

Verified kernel uses neuro-symbolic AI to build kernels from pytorch source. 

## Layout

```
verified_kernel/        Python package
  matmul.py             Triton matmul kernel, interface, autograd wrapper
tests/test_matmul.py    correctness vs torch.matmul
bench/bench_matmul.py   wall-clock comparison vs torch.matmul
```

## Usage

```python
import torch
import verified_kernel

A = torch.randn(512, 256, device="cuda")
B = torch.randn(256, 128, device="cuda")
C = verified_kernel.matmul(A, B)   # calls the Triton kernel
```

`matmul` is an autograd `Function`, so it works inside a training graph. The
backward pass computes `dA = dC @ Bᵀ` and `dB = Aᵀ @ dC` with the same kernel,
so a kernel bug surfaces in gradients rather than being masked by cuBLAS.

### Supported inputs

2-D, float32, CUDA, same device, with `A.shape[1] == B.shape[0]`. Anything else
raises. Non-contiguous operands are copied. No batching, no mixed precision, no
`out=` — the contract is deliberately small.

## Building

No separate C++/CUDA build is required. Triton JIT-compiles the Python kernel on
first use and caches it.

```bash
pip install -e .
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

The Triton kernel computes a 16×16 output tile per program. It masks boundary
loads and stores, so dimensions do not need to be multiples of 16, and it uses
`input_precision="ieee"` so the fp32 reference is not compared against TF32
math.

It is not competitive with cuBLAS — no register tiling, no vectorized loads, no
double buffering, no tensor cores. It is meant to be simple enough to state a
specification about.
