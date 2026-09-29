"""Correctness evaluation, using KernelBench's own criterion.

KernelBench declares a kernel correct when, over several trials with fresh random
inputs, `torch.allclose(reference, ours, atol=1e-2, rtol=1e-2)` holds and the
shapes match (see `src/kernelbench/eval.py`). The same criterion is applied here
so the numbers are comparable.

Two kinds of run are reported separately and never conflated:

  `full`    -- the task at its declared shape.
  `reduced` -- the task with its leading dimension shrunk to fit in GPU memory.
               34 of the 100 L1 tasks need 18-24GB for inputs plus both outputs
               and cannot be run at full size on a 12GB card at all. For those,
               note that the correctness *theorem* is generic in the shape, so it
               already covers the full size; the reduced run is what exercises
               the untrusted part -- the renderer and the modelled `tl.*`
               semantics -- not the algorithm.
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Any, List, Optional, Tuple

import os

import torch

TOL = 1e-2
TRIALS = 5


@dataclass
class Result:
    ok: bool
    mode: str                  # "full" | "reduced" | "skipped"
    detail: str = ""
    max_diff: Optional[float] = None
    scale: int = 1             # leading-dim divisor used


def budget_bytes(frac: float = 0.60) -> int:
    free, _ = torch.cuda.mem_get_info()
    # The reference module allocates temporaries of its own (a GELU or a sigmoid
    # materialises one or more full-size intermediates), and those are invisible
    # to the static estimate. A conservative fraction is cheaper than discovering
    # the shortfall as an OOM midway through a run.
    return int(free * frac)


def _bytes_for(inputs: List[Any], out: torch.Tensor) -> int:
    tot = out.numel() * 4 * 2          # reference + ours
    for t in inputs:
        if isinstance(t, torch.Tensor):
            tot += t.numel() * 4
    return tot


def plan(task, model, inputs) -> Tuple[str, int]:
    """Decide whether the task can run at full size, and if not by what integer
    factor its leading dimension must shrink."""
    with torch.no_grad():
        out = model(*inputs)
    need = _bytes_for(list(inputs), out)
    have = budget_bytes()
    if need <= have:
        return "full", 1
    scale = 1
    while need // scale > have and scale < 1 << 20:
        scale *= 2
    return "reduced", scale


def shrink(inputs: List[Any], scale: int) -> List[Any]:
    """Shrink the leading dimension to fit the task in memory.

    Which tensors may shrink is not a free choice: shrinking *every* input breaks
    an operator with a shape constraint between its inputs -- a contraction whose
    operands are `(M, K)` and `(K, N)` stops type-checking if both leading
    dimensions move. So when the inputs do not all share one shape, only the first
    is shrunk (the batch or row axis), which is shape-legal for every family here:
    a contraction's `M`, a convolution's `N`.

    The reduced task is then *re-lowered* from scratch, because a reducing
    family's index maps are derived from the shapes. Reusing the full-size spec at
    a reduced size would verify one kernel and run a different one.
    """
    if scale == 1:
        return list(inputs)
    tensors = [t for t in inputs if isinstance(t, torch.Tensor)]
    same = len({tuple(t.shape) for t in tensors}) <= 1
    out, first = [], True
    for t in inputs:
        if isinstance(t, torch.Tensor) and t.dim() >= 1 and (same or first):
            n = max(1, t.shape[0] // scale)
            out.append(t[:n].contiguous())
            first = False
        else:
            out.append(t)
            if isinstance(t, torch.Tensor):
                first = False
    return out


CHUNK = 1 << 24          # 16M elements = 64MB per comparison temporary


def close_chunked(ref: torch.Tensor, got: torch.Tensor, tol: float = TOL):
    """`allclose` over a bounded working set.

    `torch.allclose` on a billion-element tensor materialises full-size
    temporaries for `|a-b|` and `atol + rtol*|b|`, which on these task sizes costs
    more memory than the tensors being compared. Chunking keeps the extra
    allocation at 64MB and does not change the criterion: the whole tensor is
    within tolerance exactly when every chunk is.
    """
    r, g = ref.reshape(-1), got.reshape(-1)
    worst = 0.0
    for i in range(0, r.numel(), CHUNK):
        a, b = r[i:i + CHUNK], g[i:i + CHUNK]
        if not torch.allclose(a, b, atol=tol, rtol=tol):
            d = (a - b).abs().max().item()
            return False, d
        worst = max(worst, (a - b).abs().max().item())
    return True, worst


#: With `VK_FP32_REF=1`, the reference runs at full float32 instead of PyTorch's
#: default TF32 for convolutions and matrix products. TF32 keeps 10 mantissa bits,
#: so on a deep network the reference is the less accurate of the two things being
#: compared and the difference measured is mostly its own. KernelBench does not do
#: this, so it is off by default and reported as a separate column.
FP32_REF = os.environ.get("VK_FP32_REF", "") == "1"


def check(ref_model, new_model, make_inputs, trials: int = TRIALS) -> Result:
    """Run the KernelBench correctness criterion."""
    if FP32_REF:
        torch.backends.cudnn.allow_tf32 = False
        torch.backends.cuda.matmul.allow_tf32 = False
    worst = 0.0
    with torch.no_grad():
        for trial in range(trials):
            torch.manual_seed(1234 + trial)
            inputs = make_inputs()
            ref = ref_model(*inputs)
            got = new_model(*inputs)
            if ref.shape != got.shape:
                return Result(False, "n/a",
                              f"shape mismatch: expected {tuple(ref.shape)}, "
                              f"got {tuple(got.shape)}")
            close = torch.allclose(ref, got, atol=TOL, rtol=TOL)
            if not close:
                # Only now is it worth materialising the difference.
                d = (ref - got).abs().max().item()
                del ref, got, inputs
                torch.cuda.empty_cache()
                return Result(False, "n/a",
                              f"value mismatch on trial {trial}: max |diff| = {d:.3e}",
                              max_diff=d)
            del ref, got, inputs
            torch.cuda.empty_cache()
    return Result(True, "n/a", max_diff=None)
