"""Ahead-of-time build for the CUDA extension.

Optional: without it the package JIT-builds on first use. Install with
``pip install -e .`` from this directory (requires a CUDA toolkit whose version
matches the one PyTorch was built against).
"""

from setuptools import find_packages, setup
from torch.utils.cpp_extension import BuildExtension, CUDAExtension

setup(
    name="verified-kernel",
    version="0.0.1",
    description="Custom CUDA kernels exposed as PyTorch ops",
    packages=find_packages(include=["verified_kernel", "verified_kernel.*"]),
    ext_modules=[
        CUDAExtension(
            name="verified_kernel._C",
            sources=["csrc/matmul.cpp", "csrc/matmul.cu"],
            extra_compile_args={"cxx": ["-O3"], "nvcc": ["-O3"]},
        )
    ],
    cmdclass={"build_ext": BuildExtension},
    install_requires=["torch"],
    python_requires=">=3.9",
)

