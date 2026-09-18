"""Package metadata for the Triton-backed kernel."""

from setuptools import find_packages, setup

setup(
    name="verified-kernel",
    version="0.0.1",
    description="Custom Triton kernels exposed as PyTorch ops",
    packages=find_packages(include=["verified_kernel", "verified_kernel.*"]),
    install_requires=["torch", "triton"],
    python_requires=">=3.9",
)
