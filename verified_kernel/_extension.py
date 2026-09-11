"""Loads the compiled CUDA extension.

Prefers an ahead-of-time build (``pip install -e .``) and falls back to a JIT
build via ``torch.utils.cpp_extension.load``, so the package is usable from a
plain checkout with no install step.
"""

from __future__ import annotations

import os
from pathlib import Path
from typing import Any

_CSRC = Path(__file__).resolve().parent.parent / "csrc"
_SOURCES = [_CSRC / "matmul.cpp", _CSRC / "matmul.cu"]

_extension: Any = None


def load_extension() -> Any:
    """Return the compiled extension module, building it on first use."""
    global _extension
    if _extension is not None:
        return _extension

    try:
        from . import _C  # type: ignore[attr-defined]

        _extension = _C
        return _extension
    except ImportError:
        pass

    from torch.utils.cpp_extension import load

    missing = [str(p) for p in _SOURCES if not p.exists()]
    if missing:
        raise RuntimeError(
            "verified_kernel: cannot JIT-build, missing sources: " + ", ".join(missing)
        )

    _extension = load(
        name="verified_kernel_C",
        sources=[str(p) for p in _SOURCES],
        extra_cflags=["-O3"],
        # Deliberately no --use_fast_math: it enables flush-to-zero and other
        # value-changing transforms, which would make the kernel's numerics
        # depend on a compiler flag rather than on the code being read.
        extra_cuda_cflags=["-O3"],
        verbose=bool(os.environ.get("VERIFIED_KERNEL_VERBOSE_BUILD")),
    )
    return _extension

