"""Index expressions and masks, mirroring `VerifiedKernel.IE` / `BE` in Lean.

An index map says where an output element's contributions live. `Pid()` is the
output index `q`; `Rk()` is the reduction index `k`. Nothing else may appear --
tile coordinates and loop counters belong to the backend, and the Lean-side
`qkOnly` predicate enforces it, so a map that reached for them would fail to
typecheck as well-formed rather than silently compile.

Truncating subtraction matters here. `Sub` denotes `Nat` subtraction, which
saturates at zero, and the renderer emits `tl.maximum(a - b, 0)` to match. A
convolution index map that would go negative is therefore *clamped*, not wrapped,
and the accompanying `inRange` guard is what actually excludes the tap.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Tuple


class IE:
    def to_lean(self) -> str:  # pragma: no cover
        raise NotImplementedError

    def __add__(self, o) -> "IE": return Add(self, _i(o))
    def __radd__(self, o) -> "IE": return Add(_i(o), self)
    def __mul__(self, o) -> "IE": return Mul(self, _i(o))
    def __rmul__(self, o) -> "IE": return Mul(_i(o), self)
    def __sub__(self, o) -> "IE": return Sub(self, _i(o))
    def __rsub__(self, o) -> "IE": return Sub(_i(o), self)
    def __floordiv__(self, o) -> "IE": return Div(self, _i(o))
    def __mod__(self, o) -> "IE": return Mod(self, _i(o))


@dataclass(frozen=True)
class Pid(IE):
    """The output (flat) index `q`."""
    def to_lean(self) -> str: return "(IE.pid 0)"


@dataclass(frozen=True)
class Rk(IE):
    """The reduction index `k`."""
    def to_lean(self) -> str: return "IE.rk"


@dataclass(frozen=True)
class Lit(IE):
    n: int
    def to_lean(self) -> str:
        assert self.n >= 0, f"negative index literal {self.n}"
        return f"(IE.lit {self.n})"


def _bin(name):
    @dataclass(frozen=True)
    class _B(IE):
        a: IE
        b: IE
        def to_lean(self) -> str:
            return f"(IE.{name} {self.a.to_lean()} {self.b.to_lean()})"
    _B.__name__ = name
    return _B


Add = _bin("add")
Mul = _bin("mul")
Sub = _bin("sub")
Div = _bin("divi")
Mod = _bin("modi")


def _i(x) -> IE:
    return x if isinstance(x, IE) else Lit(int(x))


# --- masks -----------------------------------------------------------------

class BE:
    def to_lean(self) -> str:  # pragma: no cover
        raise NotImplementedError

    def __and__(self, o: "BE") -> "BE": return And(self, o)


@dataclass(frozen=True)
class TT(BE):
    def to_lean(self) -> str: return "BE.tt"


@dataclass(frozen=True)
class Cmp(BE):
    op: str          # "lt" | "le" | "eq" | "ne"
    a: IE
    b: IE
    def to_lean(self) -> str:
        return f"(BE.cmp .{self.op} {self.a.to_lean()} {self.b.to_lean()})"


@dataclass(frozen=True)
class And(BE):
    a: BE
    b: BE
    def to_lean(self) -> str:
        return f"(BE.and {self.a.to_lean()} {self.b.to_lean()})"


def lt(a, b) -> BE: return Cmp("lt", _i(a), _i(b))
def le(a, b) -> BE: return Cmp("le", _i(a), _i(b))


def all_of(ms: List[BE]) -> BE:
    """Conjoin, dropping trivial conjuncts."""
    ms = [m for m in ms if not isinstance(m, TT)]
    if not ms:
        return TT()
    out = ms[0]
    for m in ms[1:]:
        out = And(out, m)
    return out


def lean_list(es) -> str:
    return "[" + ", ".join(e.to_lean() for e in es) + "]"
