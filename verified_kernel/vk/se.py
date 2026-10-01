"""The spec expression language `SE`, mirroring `VerifiedKernel.SE` in Lean.

This module is the Python half of the spec language. It exists so the frontend
can build a spec as data and hand it to the Lean backend, which is the only thing
that renders Triton. Keeping one language on both sides is what makes the
generated per-task certificate meaningful: the Lean file names the *same* `SE`
term that the frontend derived from the PyTorch module.

Constants are exact rationals, never floats -- see the note in `Elementwise.lean`.
`of_float` converts a Python float to the exact rational it denotes when it is a
short decimal, and otherwise to a rational within ~1e-15 of it; the conversion is
recorded so the generator can report which specs carry an approximated constant.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from typing import Tuple

# Operators, matching the Lean `Bop` / `Fn1` constructors by name.
BOPS = ("add", "mul", "sub", "div", "max", "min")
FN1S = ("exp", "log", "tanh", "sqrt", "erf", "abs", "floorF")


class SE:
    """Base class. Subclasses mirror the Lean constructors one for one."""

    def to_lean(self) -> str:  # pragma: no cover - overridden
        raise NotImplementedError

    # convenience builders so callers read like arithmetic
    def __add__(self, o: "SE") -> "SE": return Bin("add", self, lift(o))
    def __radd__(self, o: "SE") -> "SE": return Bin("add", lift(o), self)
    def __mul__(self, o: "SE") -> "SE": return Bin("mul", self, lift(o))
    def __rmul__(self, o: "SE") -> "SE": return Bin("mul", lift(o), self)
    def __sub__(self, o: "SE") -> "SE": return Bin("sub", self, lift(o))
    def __rsub__(self, o: "SE") -> "SE": return Bin("sub", lift(o), self)
    def __truediv__(self, o: "SE") -> "SE": return Bin("div", self, lift(o))
    def __rtruediv__(self, o: "SE") -> "SE": return Bin("div", lift(o), self)
    def __neg__(self) -> "SE": return Bin("sub", lit(0), self)


@dataclass(frozen=True)
class Inp(SE):
    """Input buffer `b` at the current flat output index."""
    b: int

    def to_lean(self) -> str:
        return f"(SE.inp {self.b})"


@dataclass(frozen=True)
class Lit(SE):
    """The exact rational `(-1)^neg * num / den`."""
    neg: bool
    num: int
    den: int

    def to_lean(self) -> str:
        return f"(SE.lit {str(self.neg).lower()} {self.num} {self.den})"


@dataclass(frozen=True)
class Bin(SE):
    op: str
    a: SE
    b: SE

    def to_lean(self) -> str:
        assert self.op in BOPS, self.op
        return f"(SE.bin .{self.op} {self.a.to_lean()} {self.b.to_lean()})"


@dataclass(frozen=True)
class Un(SE):
    f: str
    a: SE

    def to_lean(self) -> str:
        assert self.f in FN1S, self.f
        return f"(SE.un .{self.f} {self.a.to_lean()})"


@dataclass(frozen=True)
class Recip(SE):
    a: SE

    def to_lean(self) -> str:
        return f"(SE.recip {self.a.to_lean()})"


@dataclass(frozen=True)
class SelLe(SE):
    """`if a <= b then t else e`."""
    a: SE
    b: SE
    t: SE
    e: SE

    def to_lean(self) -> str:
        return (f"(SE.selLe {self.a.to_lean()} {self.b.to_lean()} "
                f"{self.t.to_lean()} {self.e.to_lean()})")


# Constants whose exact value is irrational, so the spec necessarily carries a
# rational approximation. Recorded rather than hidden.
APPROXIMATED: set = set()

_MAX_DEN = 10 ** 15


def lit(x) -> Lit:
    """An exact rational literal.

    An `int` or `Fraction` is exact. A `float` is first read as the decimal it
    prints as -- `0.5` really means 1/2, not the binary float -- and only falls
    back to a bounded-denominator approximation when it has no short decimal
    form, in which case the value is recorded in `APPROXIMATED`.
    """
    if isinstance(x, Lit):
        return x
    if type(x).__module__ == "numpy":
        # a numpy scalar -- `np.float64(...)` -- is the Python number it holds
        x = x.item()
    if isinstance(x, bool):
        x = int(x)
    if isinstance(x, int):
        fr = Fraction(x)
    elif isinstance(x, Fraction):
        fr = x
    elif isinstance(x, float):
        exact = Fraction(repr(x))          # decimal reading, e.g. '0.044715'
        if exact.denominator <= _MAX_DEN:
            fr = exact
        else:
            fr = Fraction(x).limit_denominator(_MAX_DEN)
            APPROXIMATED.add(repr(x))
    else:
        raise TypeError(f"not a literal: {x!r}")
    return Lit(fr < 0, abs(fr.numerator), fr.denominator)


def lift(x) -> SE:
    return x if isinstance(x, SE) else lit(x)


# ---------------------------------------------------------------------------
# Derived pointwise operations.
#
# Each is written so that the *spec* is the mathematical definition, with no
# float rounding baked in: `sqrt 2` is the opaque `sqrt` applied to the exact
# rational 2, not 1.4142135623730951.
# ---------------------------------------------------------------------------

def sqrt(x) -> SE: return Un("sqrt", lift(x))
def exp(x) -> SE: return Un("exp", lift(x))
def log(x) -> SE: return Un("log", lift(x))
def tanh(x) -> SE: return Un("tanh", lift(x))
def erf(x) -> SE: return Un("erf", lift(x))
def absv(x) -> SE: return Un("abs", lift(x))


def maxv(a, b) -> SE: return Bin("max", lift(a), lift(b))
def minv(a, b) -> SE: return Bin("min", lift(a), lift(b))
def clamp(x, lo, hi) -> SE: return minv(maxv(x, lo), hi)


def sigmoid(x) -> SE:
    x = lift(x)
    return Recip(lit(1) + exp(-x))


def relu(x) -> SE:
    return maxv(x, 0)


def leaky_relu(x, slope) -> SE:
    x = lift(x)
    return SelLe(x, lit(0), lift(slope) * x, x)


def elu(x, alpha=1.0) -> SE:
    x = lift(x)
    return SelLe(x, lit(0), lift(alpha) * (exp(x) - lit(1)), x)


def selu(x) -> SE:
    # PyTorch's constants, to their full printed precision.
    scale = lit(1.0507009873554805)
    alpha = lit(1.6732632423543772)
    x = lift(x)
    return scale * SelLe(x, lit(0), alpha * (exp(x) - lit(1)), x)


def softplus(x) -> SE:
    return log(lit(1) + exp(x))


def softsign(x) -> SE:
    x = lift(x)
    return x / (lit(1) + absv(x))


def hardsigmoid(x) -> SE:
    return clamp(lift(x) / lit(6) + lit(Fraction(1, 2)), 0, 1)


def hardtanh(x, lo=-1.0, hi=1.0) -> SE:
    return clamp(x, lo, hi)


def silu(x) -> SE:
    x = lift(x)
    return x * sigmoid(x)


def gelu_exact(x) -> SE:
    """The exact GELU: `x/2 * (1 + erf(x/sqrt 2))`.

    Note `sqrt 2` is the opaque square root of the exact rational 2 -- the spec
    does not commit to a floating-point value for it.
    """
    x = lift(x)
    return lit(Fraction(1, 2)) * x * (lit(1) + erf(x * Recip(sqrt(lit(2)))))


def gelu_tanh(x) -> SE:
    """The tanh approximation, as used by `88_MinGPTNewGelu`.

    `sqrt(2/pi)` is written as the opaque `sqrt` of the exact rational 2/pi's
    rational approximation; pi itself is irrational, so this constant is
    recorded in `APPROXIMATED`.
    """
    import math
    x = lift(x)
    c = lit(math.sqrt(2.0 / math.pi))
    inner = c * (x + lit(0.044715) * x * x * x)
    return lit(Fraction(1, 2)) * x * (lit(1) + tanh(inner))


def mish(x) -> SE:
    """`x * tanh(softplus(x))`."""
    x = lift(x)
    return x * tanh(softplus(x))


def hardswish(x) -> SE:
    """`x * clamp(x + 3, 0, 6) / 6`."""
    x = lift(x)
    return x * clamp(x + lit(3), 0, 6) / lit(6)


def powi(x, n: int) -> SE:
    """Integer power, as repeated multiplication -- exact, unlike `exp(n log x)`."""
    assert n >= 0
    if n == 0:
        return lit(1)
    x = lift(x)
    out = x
    for _ in range(n - 1):
        out = out * x
    return out
