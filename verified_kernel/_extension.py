"""Loads the compiled CUDA extension.

Prefers an ahead-of-time build (``pip install -e .``) and falls back to a JIT
build via ``torch.utils.cpp_extension.load``, so the package is usable from a
plain checkout with no install step.
"""

from __future__ import annotations

import importlib.util
import os
from pathlib import Path
from typing import Any

_CSRC = Path(__file__).resolve().parent.parent / "csrc"
_SOURCES = [_CSRC / "matmul.cpp", _CSRC / "matmul.cu"]

_extension: Any = None


def _load_cached_extension() -> Any | None:
    """Load a previously JIT-built extension without invoking the compiler."""
    if os.environ.get("VERIFIED_KERNEL_FORCE_REBUILD"):
        return None

    try:
        from torch.utils.cpp_extension import _get_build_directory
    except ImportError:
        return None

    build_dir = Path(_get_build_directory("verified_kernel_C", verbose=False))
    extension_path = build_dir / "verified_kernel_C.so"
    if not extension_path.exists():
        return None

    spec = importlib.util.spec_from_file_location("verified_kernel_C", extension_path)
    if spec is None or spec.loader is None:
        return None

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


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

    cached = _load_cached_extension()
    if cached is not None:
        _extension = cached
        return _extension

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
