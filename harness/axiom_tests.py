"""Differential tests for the *trusted* part of the pipeline.

The Lean proofs establish that a kernel's IR computes its spec. They rest on an
assumption they cannot discharge: that the framework's model of Triton's
primitives matches what Triton actually does. That assumption is this file's
subject. Each test pins one modelled operation against an independent reference,
so a divergence between the model and the hardware shows up here rather than as a
mysteriously wrong kernel.

The cases that matter most are the ones where the model and Triton do *not*
trivially agree:

  * `IE.sub` denotes truncating `Nat` subtraction. Rendered as a bare `-` it would
    be unsound wherever an index can go negative -- a padded convolution, for
    instance -- so it renders as `tl.maximum(a - b, 0)`, and this file checks that
    the rendering really saturates.
  * Triton 3.8 has no `tl.tanh`; the renderer emits `2*sigmoid(2x) - 1`, an exact
    identity whose floating-point behaviour still needs checking.
  * `tl.arange(0, n)[:, None]` must vary along rows and `[None, :]` along columns.
    Swapping them still yields a legal shape, so nothing catches it but a test
    like this one (or the `emitIE_sound` theorem, which pins the choice in the IR).

Run:  python harness/axiom_tests.py
"""

from __future__ import annotations

import math
import sys

import torch
import triton
import triton.language as tl

TOL = 1e-5
FAILS: list = []


def report(name: str, ok: bool, detail: str = "") -> None:
    print(f"  {'ok  ' if ok else 'FAIL'}  {name}{('  ' + detail) if detail else ''}")
    if not ok:
        FAILS.append(name)


def agree(name: str, got: torch.Tensor, want: torch.Tensor, tol: float = TOL) -> None:
    got, want = got.float(), want.float()
    d = (got - want).abs()
    rel = d / want.abs().clamp_min(1e-6)
    ok = bool((d <= tol).all() or (rel <= tol).all())
    report(name, ok, f"max|diff|={d.max().item():.3e}")


# --------------------------------------------------------------------------
# Elementary functions, as `renderFn1` emits them
# --------------------------------------------------------------------------

@triton.jit
def _fn1(x_ptr, o_ptr, n, WHICH: tl.constexpr, BLOCK: tl.constexpr):
    off = tl.program_id(0) * BLOCK + tl.arange(0, BLOCK)
    m = off < n
    x = tl.load(x_ptr + off, mask=m, other=0.0)
    if WHICH == 0:
        y = tl.exp(x)
    elif WHICH == 1:
        y = tl.log(x)
    elif WHICH == 2:
        y = 2.0 * tl.sigmoid(2.0 * x) - 1.0        # the tanh rendering
    elif WHICH == 3:
        y = tl.sqrt(x)
    elif WHICH == 4:
        y = tl.erf(x)
    elif WHICH == 5:
        y = tl.abs(x)
    else:
        y = tl.floor(x)
    tl.store(o_ptr + off, y, mask=m)


def test_fn1() -> None:
    print("elementary functions (renderFn1):")
    n, BLOCK = 4096, 256
    cases = [
        (0, "exp", lambda t: torch.exp(t), (-8.0, 8.0)),
        (1, "log", lambda t: torch.log(t), (1e-3, 20.0)),
        (2, "tanh  [2*sigmoid(2x)-1]", lambda t: torch.tanh(t), (-8.0, 8.0)),
        (3, "sqrt", lambda t: torch.sqrt(t), (0.0, 50.0)),
        (4, "erf", lambda t: torch.erf(t), (-4.0, 4.0)),
        (5, "abs", lambda t: torch.abs(t), (-10.0, 10.0)),
        (6, "floor", lambda t: torch.floor(t), (-10.0, 10.0)),
    ]
    for which, name, ref, (lo, hi) in cases:
        x = torch.rand(n, device="cuda") * (hi - lo) + lo
        o = torch.empty_like(x)
        _fn1[(triton.cdiv(n, BLOCK),)](x, o, n, which, BLOCK=BLOCK)
        agree(name, o, ref(x), tol=2e-5)


# --------------------------------------------------------------------------
# Truncating subtraction: the `IE.sub` rendering
# --------------------------------------------------------------------------

@triton.jit
def _trunc_sub(a_ptr, b_ptr, o_ptr, n, BLOCK: tl.constexpr):
    off = tl.program_id(0) * BLOCK + tl.arange(0, BLOCK)
    m = off < n
    a = tl.load(a_ptr + off, mask=m, other=0)
    b = tl.load(b_ptr + off, mask=m, other=0)
    tl.store(o_ptr + off, tl.maximum(a - b, 0), mask=m)


def test_trunc_sub() -> None:
    print("truncating subtraction (IE.sub):")
    n, BLOCK = 1024, 256
    a = torch.randint(0, 50, (n,), device="cuda", dtype=torch.int32)
    b = torch.randint(0, 50, (n,), device="cuda", dtype=torch.int32)
    o = torch.empty_like(a)
    _trunc_sub[(triton.cdiv(n, BLOCK),)](a, b, o, n, BLOCK=BLOCK)
    want = (a - b).clamp_min(0)          # Nat subtraction saturates at zero
    report("tl.maximum(a-b,0) == Nat sub", bool((o == want).all()))
    report("saturates rather than wrapping", bool((o >= 0).all()))


# --------------------------------------------------------------------------
# Floor division and remainder on non-negative indices
# --------------------------------------------------------------------------

@triton.jit
def _divmod(a_ptr, q_ptr, r_ptr, n, D: tl.constexpr, BLOCK: tl.constexpr):
    off = tl.program_id(0) * BLOCK + tl.arange(0, BLOCK)
    m = off < n
    a = tl.load(a_ptr + off, mask=m, other=0)
    tl.store(q_ptr + off, a // D, mask=m)
    tl.store(r_ptr + off, a % D, mask=m)


def test_divmod() -> None:
    print("index div/mod (IE.divi, IE.modi):")
    n, BLOCK, D = 1024, 256, 37
    a = torch.randint(0, 100000, (n,), device="cuda", dtype=torch.int32)
    q, r = torch.empty_like(a), torch.empty_like(a)
    _divmod[(triton.cdiv(n, BLOCK),)](a, q, r, n, D, BLOCK=BLOCK)
    report("a // d matches Nat division", bool((q == a.div(D, rounding_mode="floor")).all()))
    report("a %  d matches Nat modulus", bool((r == a % D).all()))
    report("d*(a//d) + a%d == a", bool((q * D + r == a).all()))


# --------------------------------------------------------------------------
# Masked loads substitute zero (the `other=0.0` the IR assumes)
# --------------------------------------------------------------------------

@triton.jit
def _masked(x_ptr, o_ptr, n, BLOCK: tl.constexpr):
    off = tl.program_id(0) * BLOCK + tl.arange(0, BLOCK)
    m = off < n
    tl.store(o_ptr + off, tl.load(x_ptr + off, mask=m, other=0.0),
             mask=tl.arange(0, BLOCK) < BLOCK)


def test_masked_load() -> None:
    print("masked load (FE.load):")
    BLOCK, n = 256, 100          # deliberately not a multiple of BLOCK
    x = torch.randn(n, device="cuda")
    o = torch.zeros(BLOCK, device="cuda")
    _masked[(1,)](x, o, n, BLOCK=BLOCK)
    report("in-range lanes read memory", bool(torch.equal(o[:n], x)))
    report("masked-off lanes read 0.0", bool((o[n:] == 0.0).all()))


# --------------------------------------------------------------------------
# Broadcast orientation: the choice `emitIE` has to get right
# --------------------------------------------------------------------------

@triton.jit
def _bcast(o_ptr, R: tl.constexpr, C: tl.constexpr):
    r = tl.arange(0, R)[:, None]          # must vary along rows
    c = tl.arange(0, C)[None, :]          # must vary along columns
    off = r * C + c
    tl.store(o_ptr + off, (r * 1000 + c).to(tl.float32))


def test_broadcast() -> None:
    print("broadcast orientation (emitIE row/col):")
    R, C = 8, 16
    o = torch.zeros(R * C, device="cuda")
    _bcast[(1,)](o, R, C)
    got = o.reshape(R, C)
    want = (torch.arange(R, device="cuda")[:, None] * 1000
            + torch.arange(C, device="cuda")[None, :]).float()
    report("arange[:,None] varies by row, [None,:] by column",
           bool(torch.equal(got, want)))


# --------------------------------------------------------------------------
# Cross-lane sum: `redCol` on a rank-1 tile is axis 0
# --------------------------------------------------------------------------

@triton.jit
def _lane_sum(x_ptr, o_ptr, K, BLOCK: tl.constexpr, NKB: tl.constexpr):
    acc = tl.zeros([BLOCK], dtype=tl.float32)
    for kb in range(0, NKB):
        k = kb * BLOCK + tl.arange(0, BLOCK)
        m = k < K
        acc = acc + tl.where(m, tl.load(x_ptr + k, mask=m, other=0.0), 0.0)
    tl.store(o_ptr + tl.program_id(0), tl.sum(acc, axis=0))


def test_lane_sum() -> None:
    print("tiled accumulator + cross-lane sum (GenRed):")
    K, BLOCK = 5000, 256
    NKB = triton.cdiv(K, BLOCK)
    x = torch.randn(K, device="cuda")
    o = torch.zeros(1, device="cuda")
    _lane_sum[(1,)](x, o, K, BLOCK=BLOCK, NKB=NKB)
    # A different summation order from torch.sum, so agreement is to fp tolerance.
    agree("sum over a masked, tiled range", o, x.sum().reshape(1), tol=2e-3)


def main() -> int:
    if not torch.cuda.is_available():
        print("no CUDA device; cannot validate the Triton model")
        return 2
    print(f"device: {torch.cuda.get_device_name()}   triton {triton.__version__}\n")
    for t in (test_fn1, test_trunc_sub, test_divmod, test_masked_load,
              test_broadcast, test_lane_sum):
        t()
        print()
    if FAILS:
        print(f"{len(FAILS)} assumption(s) about Triton do NOT hold: {FAILS}")
        print("The proofs are sound but the trusted model is wrong; fix the renderer.")
        return 1
    print("all modelled Triton primitives behave as the framework assumes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
