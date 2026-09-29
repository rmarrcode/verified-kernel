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

    def __add__(self, o) -> "IE": return mk_add(self, _i(o))
    def __radd__(self, o) -> "IE": return mk_add(_i(o), self)
    def __mul__(self, o) -> "IE": return mk_mul(self, _i(o))
    def __rmul__(self, o) -> "IE": return mk_mul(_i(o), self)
    def __sub__(self, o) -> "IE": return mk_sub(self, _i(o))
    def __rsub__(self, o) -> "IE": return mk_sub(_i(o), self)
    def __floordiv__(self, o) -> "IE": return mk_div(self, _i(o))
    def __mod__(self, o) -> "IE": return mk_mod(self, _i(o))


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


def _is(e, n: int) -> bool:
    return isinstance(e, Lit) and e.n == n


# Smart constructors folding the `Nat` identities. These are exact, not heuristic,
# and they matter for more than tidiness: a locality bound is discharged by matching
# an index map against a lemma's conclusion, and `((q/W) % H) * 1 + 0 * 1` does not
# match `(q/W) % H` even though it denotes it.
def mk_add(a: IE, b: IE) -> IE:
    if _is(a, 0):
        return b
    if _is(b, 0):
        return a
    return Add(a, b)


def mk_mul(a: IE, b: IE) -> IE:
    if _is(a, 0) or _is(b, 0):
        return Lit(0)
    if _is(a, 1):
        return b
    if _is(b, 1):
        return a
    return Mul(a, b)


def mk_sub(a: IE, b: IE) -> IE:
    return a if _is(b, 0) else Sub(a, b)


def mk_div(a: IE, b: IE) -> IE:
    return a if _is(b, 1) else Div(a, b)


def mk_mod(a: IE, b: IE) -> IE:
    return Lit(0) if _is(b, 1) else Mod(a, b)


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


def subst_rk(e, repl: IE):
    """Replace the reduction placeholder `Rk` by `repl` throughout an index or mask
    expression.

    Used to split a reduction into a tree: the outer stage's lane `p` covers the
    chunk starting at `p * chunk`, so its index map is the original one with `rk`
    replaced by `pid * chunk + rk`.
    """
    if isinstance(e, Rk):
        return repl
    if isinstance(e, (Pid, Lit, TT)):
        return e
    if isinstance(e, Cmp):
        return Cmp(e.op, subst_rk(e.a, repl), subst_rk(e.b, repl))
    if isinstance(e, And):
        return And(subst_rk(e.a, repl), subst_rk(e.b, repl))
    if hasattr(e, "a") and hasattr(e, "b"):
        return type(e)(subst_rk(e.a, repl), subst_rk(e.b, repl))
    raise TypeError(f"cannot substitute in {type(e).__name__}")


def subst(e, pid: IE, rk: IE):
    """Simultaneously replace the two placeholders `Pid` and `Rk`.

    `subst_rk` covers splitting a reduction whose output is a single element, where
    the lane index is free. Splitting a *stage* of a chain needs both at once: the
    lane now carries an output coordinate and a chunk number packed together, so the
    original `pid` becomes one half of it and `rk` is offset by the other.
    """
    if isinstance(e, Pid):
        return pid
    if isinstance(e, Rk):
        return rk
    if isinstance(e, (Lit, TT)):
        return e
    if isinstance(e, Cmp):
        return Cmp(e.op, subst(e.a, pid, rk), subst(e.b, pid, rk))
    if isinstance(e, And):
        return And(subst(e.a, pid, rk), subst(e.b, pid, rk))
    if hasattr(e, "a") and hasattr(e, "b"):
        return type(e)(subst(e.a, pid, rk), subst(e.b, pid, rk))
    raise TypeError(f"cannot substitute in {type(e).__name__}")


def lean_list(es) -> str:
    return "[" + ", ".join(e.to_lean() for e in es) + "]"
