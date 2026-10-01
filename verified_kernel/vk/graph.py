"""Compiling a whole PyTorch graph into a chain of verified stages.

Level 1 is one operator per task, so each task could be a single family instance.
Levels 2 and 3 are *sequences* -- a fused operator, or a convolutional network --
and need a compiler: walk the traced graph, emit one or more stages per node, and
hand the chain to `stages_correct`.

Buffer numbering is fixed by position and never reassigned: inputs and parameters
occupy `0 .. arity-1`, and stage `j` writes buffer `arity + j`. That is what lets the
launcher append intermediates to the input list with no renumbering, and what makes
each stage's locality obligation a statement about buffers below its own index.

This module owns the *shape* of the compilation. The per-operator index maps live in
`frontend.py` and are reused unchanged -- a convolution emitted here is the same
`GenRed` a Level 1 convolution was, at the same theorem.
"""

from __future__ import annotations

import math
import operator
from dataclasses import dataclass, field
from fractions import Fraction
from typing import Any, Dict, List, Optional, Tuple

import torch
import torch.fx as fx
import torch.nn as nn
import torch.nn.functional as F

from . import ie as I
from . import se as S
from .frontend import (NO_IDX_SLOT, Lowered, Unsupported, _prod, op_name, pack,
                       table_get, unpack)


@dataclass
class Val:
    """A materialised tensor: which buffer holds it, and its shape."""
    buf: int
    shape: Tuple[int, ...]

    @property
    def numel(self) -> int:
        return _prod(self.shape)


# A stage narrow enough that one program per output leaves the GPU idle, and long
# enough that splitting it pays for the extra pass.
TREE_STAGE_MAX_OUT = 1024
TREE_STAGE_MIN_K = 1 << 16
TREE_STAGE_PARTIALS = 256


def _worth_splitting(st: Lowered, shape: Tuple[int, ...]) -> bool:
    """Only sums split this way. A max has no identity, so its family clamps the
    reduction range rather than masking it, and a short final chunk would not be
    harmless -- see `MaxRed`.
    """
    return (st.family == "genred" and st.K > TREE_STAGE_MIN_K
            and _prod(shape) <= TREE_STAGE_MAX_OUT)


@dataclass
class Chain:
    """A compilation in progress."""
    # inputs and parameters, in buffer order
    arg_index: List[int] = field(default_factory=list)
    param_paths: List[str] = field(default_factory=list)
    stages: List[Lowered] = field(default_factory=list)
    sizes: List[int] = field(default_factory=list)
    shapes: List[Tuple[int, ...]] = field(default_factory=list)
    notes: List[str] = field(default_factory=list)
    # diagnostics: the node each stage was emitted for, and the node being walked
    node_of: List[str] = field(default_factory=list)
    # the node a stage was *emitted* for; `node_of` moves to the last node fused
    # into it, so both are needed to check a fused group as a unit
    node_src: List[str] = field(default_factory=list)
    cur_node: str = "?"

    @property
    def arity(self) -> int:
        return len(self.arg_index) + len(self.param_paths)

    @property
    def nbuf(self) -> int:
        return self.arity + len(self.stages)

    def add_param(self, path: str) -> int:
        """Promote a module parameter to an input buffer.

        Parameters must be allocated before any stage, since buffer numbering puts
        every input below every intermediate. Callers therefore declare a node's
        parameters up front.
        """
        if self.stages:
            raise Unsupported("parameters must be allocated before any stage")
        self.param_paths.append(path)
        return self.arity - 1

    def emit(self, st: Lowered, shape: Tuple[int, ...]) -> Val:
        """Append a stage writing a fresh buffer, and return the value it holds."""
        if _worth_splitting(st, shape):
            return self._emit_tree(st, shape)
        return self._emit1(st, shape)

    def _emit1(self, st: Lowered, shape: Tuple[int, ...]) -> Val:
        buf = self.arity + len(self.stages)
        self.node_of.append(self.cur_node)
        self.node_src.append(self.cur_node)
        st.out_shape = tuple(shape)
        st.out_size = _prod(shape)
        self.stages.append(st)
        self.sizes.append(st.out_size)
        self.shapes.append(tuple(shape))
        return Val(buf, tuple(shape))

    def _emit_tree(self, st: Lowered, shape: Tuple[int, ...]) -> Val:
        """Emit a long, narrow reduction as two stages instead of one.

        A stage with sixteen outputs and sixteen million summands each -- a
        BatchNorm's mean, say -- is one program per output looping the whole way.
        It is just as verified as any other, but it is not worth running. The split
        is the same idea `tree_split` uses for a whole-tensor reduction, done to one
        link of a chain: the first stage computes `P` partial sums per output, the
        second sums those. Nothing new is proved. Both halves are the same reducing
        family at the same theorem, and `stages_correct` already composes stage
        lists of any length.

        The lane of the first stage carries `(output, chunk)` packed together, so
        the original index map is reindexed at both placeholders at once: `pid`
        becomes the output half, `rk` the chunk offset.
        """
        n_out, K = _prod(shape), st.K
        P = min(TREE_STAGE_PARTIALS, K)
        chunk = (K + P - 1) // P
        q, p_ = I.Pid() // I.Lit(P), I.Pid() % I.Lit(P)
        k = p_ * I.Lit(chunk) + I.Rk()

        first = Lowered(
            family="genred", body=st.body, arity=st.arity,
            out_size=n_out * P, out_shape=(n_out, P),
            tensor_arg_index=list(st.tensor_arg_index), K=chunk,
            offs=[I.subst(o, q, k) for o in st.offs],
            post_offs=[I.Lit(0)] * len(st.offs),
            # Beyond the end the summand is masked to zero, so a short final chunk
            # contributes nothing and the partials still sum to the whole.
            in_range=I.all_of([I.subst(st.in_range, q, k), I.lt(k, I.Lit(K))]),
            post=S.Inp(0),
            notes=[f"tree stage 1: {P} partial sums of {chunk} each, per output"])
        tv = self._emit1(first, (n_out, P))

        w = self.nbuf + 1
        second = Lowered(
            family="genred", body=S.Inp(tv.buf), arity=w,
            out_size=n_out, out_shape=tuple(shape),
            tensor_arg_index=list(st.tensor_arg_index), K=P,
            offs=[(I.Pid() * I.Lit(P) + I.Rk()) if b == tv.buf else I.Lit(0)
                  for b in range(w)],
            post_offs=[st.post_offs[b] if b < len(st.post_offs) else I.Lit(0)
                       for b in range(w)],
            post=st.post,
            notes=[f"tree stage 2: sum of the {P} partials"])
        self.notes.append(
            f"split a {n_out}-output reduction over {K} into {P} partials")
        return self._emit1(second, shape)

    def record_bounds(self) -> None:
        """For every stage, how it stays inside each intermediate buffer.

        A stage may read any buffer written before it, so the obligation covers all
        of them; where it does not touch one the map is the constant 0 and the bound
        is trivial.

        When an index map's range is not evident from its *shape*, the map is
        clamped into the buffer. That is a no-op on any well-formed graph -- the
        index is already in range, because the producing stage wrote exactly this
        tensor -- and it makes the obligation uniform rather than a growing list of
        recognised arithmetic. It also makes the kernel memory-safe by construction:
        a chain stage cannot read past what an earlier stage wrote, whatever the
        frontend got wrong. The claim the frontend still owns is that the clamp never
        fires, which is the same shape-correctness claim it already makes everywhere.
        """
        for j, st in enumerate(self.stages):
            if st.family == "recur":
                # A loop's own reads are its initial state and its views, whose
                # ranges are side conditions of `Recur.Local`; its body's reads are
                # bounded when the body is placed (`finish_recurrences`).
                st.bounds = {}
                continue
            bound_stage(st, self.arity, self.sizes, self.shapes)

    def finish_recurrences(self) -> None:
        """Number each loop body's buffers above every outer buffer, and bound its
        reads against the sizes the loop proof uses: the outer intermediates, then
        the state, the views and the body's own."""
        from .rnn import finish_recur
        base = self.arity + len(self.stages)
        for st in self.stages:
            if st.family == "recur":
                finish_recur(st, base, self.arity, self.sizes, self.shapes)

    def pad(self, entries: Dict[int, I.IE], extra: int = 1) -> List[I.IE]:
        """Index maps for every buffer a stage may see: all inputs, every earlier
        intermediate, and the one it is about to write."""
        n = self.nbuf + extra
        return [entries.get(b, I.Lit(0)) for b in range(n)]


def bound_stage(st: Lowered, arity: int, sizes: List[int],
                shapes: List[Tuple[int, ...]]) -> None:
    """Record how `st` stays inside each intermediate buffer `arity + i`, of
    `sizes[i]` elements, clamping any read whose range is not evident from its
    shape. See `Chain.record_bounds`."""
    bounds: Dict[str, Tuple] = {}
    for b in range(arity, arity + len(sizes)):
        size = sizes[b - arity]
        shp = shapes[b - arity]
        for tag, lst in (("b", st.offs), ("p", st.post_offs)):
            e = lst[b] if b < len(lst) else I.Lit(0)
            bd = buffer_bound(e, size, st.out_size, shp)
            if bd is None:
                e = I.Sub(e, I.Sub(e, I.Lit(size - 1)))   # min(e, size-1)
                while b >= len(lst):
                    lst.append(I.Lit(0))
                lst[b] = e
                bd = ("clamp", size)
                st.notes.append(f"read of buffer {b} clamped into range")
            bounds[f"{tag}{b}"] = bd
    st.bounds = bounds


def identity_stage(ch: Chain, v: Val, body: S.SE, shape: Tuple[int, ...],
                   note: str, extra_offs: Optional[Dict[int, I.IE]] = None) -> Lowered:
    """A pointwise stage: `K = 1`, every input read at the output index.

    Expressed as a degenerate reduction so it reuses the same theorem as everything
    else -- there is no separate pointwise kernel path at this level.
    """
    offs = {v.buf: I.Pid()}
    if extra_offs:
        offs.update(extra_offs)
    return Lowered(
        family="genred", body=body, arity=ch.nbuf + 1,
        out_size=_prod(shape), out_shape=tuple(shape),
        tensor_arg_index=list(ch.arg_index), K=1,
        offs=ch.pad(offs), post_offs=ch.pad({}), post=S.Inp(0),
        notes=[note])


# ---------------------------------------------------------------------------
# Relocating a standalone lowering into a chain
# ---------------------------------------------------------------------------

def _subst_slot0(e: S.SE, repl: S.SE) -> S.SE:
    """Replace slot 0 -- this operator's input -- by the expression producing it."""
    if isinstance(e, S.Inp):
        return repl if e.b == 0 else e
    if isinstance(e, S.Lit):
        return e
    if isinstance(e, S.Bin):
        return S.Bin(e.op, _subst_slot0(e.a, repl), _subst_slot0(e.b, repl))
    if isinstance(e, S.Un):
        return S.Un(e.f, _subst_slot0(e.a, repl))
    if isinstance(e, S.Recip):
        return S.Recip(_subst_slot0(e.a, repl))
    if isinstance(e, S.SelLe):
        return S.SelLe(*(_subst_slot0(x, repl) for x in (e.a, e.b, e.t, e.e)))
    raise Unsupported(f"cannot substitute in {type(e).__name__}")


def _remap_se(e: S.SE, f) -> S.SE:
    """Rewrite every input slot of a spec body through `f`."""
    if isinstance(e, S.Inp):
        return S.Inp(f(e.b))
    if isinstance(e, S.Lit):
        return e
    if isinstance(e, S.Bin):
        return S.Bin(e.op, _remap_se(e.a, f), _remap_se(e.b, f))
    if isinstance(e, S.Un):
        return S.Un(e.f, _remap_se(e.a, f))
    if isinstance(e, S.Recip):
        return S.Recip(_remap_se(e.a, f))
    if isinstance(e, S.SelLe):
        return S.SelLe(*(_remap_se(x, f) for x in (e.a, e.b, e.t, e.e)))
    raise Unsupported(f"cannot remap {type(e).__name__}")


def _lit(e) -> Optional[int]:
    return e.n if isinstance(e, I.Lit) else None


def split_pack(e: I.IE, dims: List[int]) -> Optional[List[I.IE]]:
    """Recover the coordinates of a row-major index map, if that is its shape.

    `pack` builds `((c0*d1 + c1)*d2 + c2)...`, and the smart constructors fold away
    any axis of extent one, so those contribute no structure and their coordinate is
    the constant 0.
    """
    coords: List[I.IE] = []
    cur = e
    for d in reversed(dims[1:]):
        if d == 1:
            coords.append(I.Lit(0))
            continue
        if (isinstance(cur, I.Add) and isinstance(cur.a, I.Mul)
                and _lit(cur.a.b) == d):
            coords.append(cur.b)
            cur = cur.a.a
        elif isinstance(cur, I.Mul) and _lit(cur.b) == d:
            coords.append(FOLDED_ZERO)      # trailing coordinate folded away
            cur = cur.a
        else:
            return None
    coords.append(cur)
    return list(reversed(coords))


class _FoldedZero(I.IE):
    """A zero coordinate that `pack` folded out of the index map entirely: the map
    reads `a * d`, not `a * d + 0`, and its bound must say so (`bound_packz`)."""
    def to_lean(self) -> str:
        return "(IE.lit 0)"


FOLDED_ZERO = _FoldedZero()


def _is_clamp(c: I.IE, d: int) -> bool:
    """`a - (a - (d-1))` is `min a (d-1)`, hence below `d`."""
    return (isinstance(c, I.Sub) and isinstance(c.b, I.Sub)
            and c.b.a == c.a and _lit(c.b.b) == d - 1)


def coord_bound(c: I.IE, d: int, nout: int) -> Optional[Tuple]:
    """How to prove one coordinate is below its axis extent."""
    if c is FOLDED_ZERO:
        return ("zfold", d)
    if _is_clamp(c, d):
        return ("clamp", d)
    if _lit(c) == 0:
        return ("zerolt", d)
    if isinstance(c, I.Rk):
        return ("hk",)
    if isinstance(c, I.Pid):
        return ("hq",) if d == nout else None
    if isinstance(c, I.Div) and isinstance(c.a, I.Pid) and _lit(c.b) is not None:
        return ("div", d, _lit(c.b))
    if isinstance(c, I.Mod) and _lit(c.b) == d:
        return ("mod", d)                   # `q % d` or `(q / x) % d`
    return None


def buffer_bound(e: I.IE, size: int, nout: int,
                 shape: Optional[Tuple[int, ...]] = None) -> Optional[Tuple]:
    """How to prove this index map stays inside a buffer of `size` elements.

    Reading past a written buffer is reading uninitialised memory, which is exactly
    what the locality obligation exists to rule out -- so anything unrecognised
    returns `None` and the caller refuses to emit rather than guessing.
    """
    if _lit(e) == 0:
        return ("zerolt", size)                 # not read at all
    if isinstance(e, I.Pid) and size == nout:
        return ("hq",)                          # read at the output index
    if shape and len(shape) > 1:
        coords = split_pack(e, list(shape))
        if coords is not None:
            # An axis of extent one contributes no structure to the index map (the
            # identities fold it away), so it must be dropped from the bound chain
            # too; it does not change the product being bounded.
            keep = [(c, d) for c, d in zip(coords, shape) if d != 1]
            bs = [coord_bound(c, d, nout) for c, d in keep]
            if keep and all(b is not None for b in bs):
                return ("packs", bs, [d for _, d in keep])
    # A reduction views the buffer it consumes as `[outer, K, inner]` rather than by
    # its logical shape, so try that reading too.
    if isinstance(e, I.Add) and isinstance(e.a, I.Mul) and isinstance(e.a.a, I.Pid):
        x = _lit(e.a.b)
        if x is not None and isinstance(e.b, I.Rk) and nout * x == size:
            return ("packs", [("hq",), ("hk",)], [nout, x])
    if isinstance(e, I.Add) and isinstance(e.a, I.Mul):
        inner = _lit(e.a.b)
        if inner is not None and inner > 0 and size % inner == 0:
            mid = e.a.a
            if (isinstance(mid, I.Add) and isinstance(mid.a, I.Mul)
                    and isinstance(mid.b, I.Rk)):
                K = _lit(mid.a.b)
                row = mid.a.a
                if K is not None and K > 0 and size % (K * inner) == 0:
                    outer = size // (K * inner)
                    cb = coord_bound(row, outer, nout)
                    tb = coord_bound(e.b, inner, nout)
                    if cb is not None and tb is not None:
                        return ("packs", [cb, ("hk",), tb], [outer, K, inner])
    return None


def relocate(st: Lowered, bmap: Dict[int, int], nbuf: int, idx_slot: int) -> Lowered:
    """Renumber a standalone stage's buffers into a chain's numbering.

    A lowering produced on its own numbers its inputs `0, 1, ...`; in a chain those
    same tensors live at whatever buffers the chain assigned. Only the numbering
    changes -- the index maps, the body, the guards and therefore the theorem are
    untouched, which is the point of doing it this way rather than re-deriving each
    operator for the chain.

    `post`'s slot convention shifts by one (slot 0 is the reduced value), so its
    remap is `b -> bmap[b] + 1`.
    """
    def m(b: int) -> int:
        if b == st.idx_slot:
            return idx_slot
        if b not in bmap:
            raise Unsupported(f"stage reads buffer {b}, which the chain did not map")
        return bmap[b]

    offs = [I.Lit(0)] * nbuf
    post_offs = [I.Lit(0)] * nbuf
    # Two slots of the standalone lowering may land on one chain buffer (the same
    # tensor passed twice). A stage reads a buffer at one index map, so that is
    # only sound when the two maps agree; otherwise one would silently replace the
    # other, which is exactly how `cat([h, h])` once went wrong.
    placed: Dict[Tuple[str, int], I.IE] = {}

    def place(tag, lst, b, e):
        t = bmap[b]
        if (tag, t) in placed and placed[(tag, t)] != e and not (
                isinstance(e, I.Lit) and e.n == 0):
            raise Unsupported(f"two operands read buffer {t} at different index maps")
        if not (isinstance(e, I.Lit) and e.n == 0):
            placed[(tag, t)] = e
            lst[t] = e
    for b, e in enumerate(st.offs):
        if b == st.idx_slot:
            continue
        if b in bmap:
            place("b", offs, b, e)
    for b, e in enumerate(st.post_offs):
        if b in bmap:
            place("p", post_offs, b, e)

    return Lowered(
        family=st.family, body=_remap_se(st.body, m), arity=nbuf,
        out_size=st.out_size, out_shape=st.out_shape,
        tensor_arg_index=st.tensor_arg_index, K=st.K,
        offs=offs, post_offs=post_offs,
        in_range=st.in_range, out_guard=st.out_guard,
        post=_remap_se(st.post, lambda b: 0 if b == 0 else m(b - 1) + 1),
        idx_slot=idx_slot, out_dtype=st.out_dtype,
        notes=list(st.notes))


class _Wrap1(nn.Module):
    """A one-node module, so an existing Level 1 lowering can be reused verbatim.

    Fixed arity rather than `*args`: `fx` cannot trace a starred argument.
    """
    def __init__(self, fn): super().__init__(); self.fn = fn
    def forward(self, x): return self.fn(x)


class _Wrap2(nn.Module):
    def __init__(self, fn): super().__init__(); self.fn = fn
    def forward(self, x, y): return self.fn(x, y)


class _Wrap3(nn.Module):
    def __init__(self, fn): super().__init__(); self.fn = fn
    def forward(self, x, y, z): return self.fn(x, y, z)


_WRAPS: Dict[int, type] = {1: _Wrap1, 2: _Wrap2, 3: _Wrap3}


def _wrap(fn, n: int) -> nn.Module:
    """A module whose forward takes exactly `n` named tensors. Beyond three the
    class is generated, since `fx` needs the arity spelled out in the signature."""
    if n not in _WRAPS:
        names = ", ".join(f"a{i}" for i in range(n))
        ns: Dict[str, Any] = {}
        exec(f"def forward(self, {names}): return self.fn({names})", ns)
        _WRAPS[n] = type(f"_Wrap{n}", (_Wrap1,), {"forward": ns["forward"]})
    return _WRAPS[n](fn)


# ---------------------------------------------------------------------------
# The walker
# ---------------------------------------------------------------------------

def _node_shapes(gm: fx.GraphModule, args: List[Any],
                 dtypes: Optional[Dict[fx.Node, Any]] = None
                 ) -> Dict[fx.Node, Tuple[int, ...]]:
    """Every node's output shape, by interpreting the graph on fake tensors; and,
    given a dict to fill, every tensor node's dtype."""
    shapes: Dict[fx.Node, Tuple[int, ...]] = {}

    class Rec(fx.Interpreter):
        def run_node(self, n):
            out = super().run_node(n)
            if isinstance(out, torch.Tensor) and dtypes is not None:
                dtypes[n] = out.dtype
            if isinstance(out, torch.Tensor):
                shapes[n] = tuple(out.shape)
            elif (isinstance(out, tuple) and out
                  and isinstance(out[0], torch.Tensor)):
                # `min`/`max` over a dim return `(values, indices)`; the chain
                # follows the values.
                shapes[n] = tuple(out[0].shape)
            return out

    Rec(gm).run(*args)
    return shapes


# Operators that only relabel a tensor: the data is untouched and row-major order is
# preserved, so the buffer is reused as it stands and no stage is emitted.
ALIAS_FNS = {"view", "reshape", "clone", "detach", "contiguous", "flatten",
             "squeeze", "unsqueeze", "to", "float", "type_as", "expand_as",
             # an expand that adds no elements; one that broadcasts is a stage
             # (`_relabel_of`), which is checked first
             "expand", "broadcast_to"}


def _alias_of(node: fx.Node, shapes) -> Optional[fx.Node]:
    """If this node is a pure relabelling of one input, return that input.

    A `getitem` is included only when it selects field 0 of a `(values, indices)`
    pair -- taking the indices would be an argmax, which is a different computation,
    not a relabelling.
    """
    tgt = node.target
    nm = tgt if isinstance(tgt, str) else getattr(tgt, "__name__", str(tgt))
    src = node.all_input_nodes[0] if node.all_input_nodes else None
    if src is None:
        return None
    if nm in ALIAS_FNS:
        return src
    if nm == "getitem":
        idx = node.args[1] if len(node.args) > 1 else None
        # Field 0 of a `(values, indices)` pair, whose recorded shape is the
        # values' -- not `x[0]` on a tensor, which drops an axis and is a slice.
        if idx == 0 and not isinstance(idx, bool) and node in shapes \
                and src in shapes and shapes[node] == shapes[src]:
            return src
        return None
    if nm == "getattr" and len(node.args) > 1 and node.args[1] == "values":
        # `torch.max(x, dim)` returns a named tuple; `.values` is the values
        return src
    return None


def _const_of(node: fx.Node, gm: Optional[fx.GraphModule] = None):
    """The value a constant node denotes, as a spec expression.

    A literal `torch.tensor(c)`, or a pointwise operator applied to constants --
    `torch.log(torch.tensor(100.))` -- which is kept symbolic rather than evaluated,
    so the spec says `log 100` and not a float near it.
    """
    if op_name(node.target) == "tensor" and node.args and isinstance(
            node.args[0], (int, float)):
        return S.lit(node.args[0])
    if gm is not None and node.op in ("call_function", "call_method") \
            and _is_pointwise(node, gm) and node.all_input_nodes:
        args = [_const_of(a, gm) if isinstance(a, fx.Node) else a for a in node.args]
        return _pointwise_se(node, gm, args)
    raise Unsupported(f"{node.target} is not a constant")


def _is_const(node: fx.Node, gm: fx.GraphModule) -> bool:
    try:
        _const_of(node, gm)
        return True
    except Unsupported:
        return False


def _is_pointwise(node: fx.Node, gm: fx.GraphModule) -> bool:
    from .frontend import POINTWISE_FUNCS, POINTWISE_MODULES
    if node.op == "call_module":
        return type(gm.get_submodule(node.target)) in POINTWISE_MODULES
    if node.op in ("call_function", "call_method"):
        if table_get(POINTWISE_FUNCS, node.target) is None:
            return False
        # `min`/`max` are pointwise with two operands and a *reduction* with a
        # `dim`; the same name means different things.
        nm = node.target if isinstance(node.target, str) else getattr(
            node.target, "__name__", "")
        if nm in ("min", "max", "amin", "amax"):
            has_dim = "dim" in node.kwargs or (
                len(node.args) > 1 and isinstance(node.args[1], int))
            return not has_dim
        return True
    return False


def _slice_plan(idx, in_shape: List[int]):
    """Resolve a subscript into, per output-or-input axis, `(start, step, extent)`.

    An entry with `extent` `None` is an input axis indexed by a plain integer, so
    absent from the output; an entry `(None, None, 1)` is a new axis of extent one
    (`None` in the subscript), absent from the input. Returns `None` for anything
    not handled -- a boolean mask, a tensor index -- rather than guessing.
    """
    items = list(idx) if isinstance(idx, tuple) else [idx]
    n_real = sum(1 for it in items if it is not Ellipsis and it is not None)
    if any(it is Ellipsis for it in items):
        pos = next(i for i, it in enumerate(items) if it is Ellipsis)
        items[pos:pos + 1] = [slice(None)] * (len(in_shape) - n_real)
        n_real = len(in_shape)
    if n_real > len(in_shape):
        return None
    items += [slice(None)] * (len(in_shape) - n_real)
    plan = []
    axes = iter(in_shape)
    for it in items:
        if it is None:
            plan.append((None, None, 1))
            continue
        n = next(axes)
        if isinstance(it, int) and not isinstance(it, bool):
            i = it + n if it < 0 else it
            if not (0 <= i < n):
                return None
            plan.append((i, 1, None))
        elif isinstance(it, slice):
            start, stop, step = it.indices(n)
            if step <= 0:
                return None
            plan.append((start, step, max(0, -(-(stop - start) // step))))
        else:
            return None
    return plan


def _emit_slice(ch: Chain, v: Val, plan, note: str) -> Val:
    """A slice, as a `K = 1` reducing stage whose index map carries the offsets.

    Like a permutation, this is a relabelling of coordinates rather than a
    computation, so it needs nothing the family does not already have: output
    coordinate `o` on an axis reads input coordinate `start + o * step`.
    """
    so = [ext for (_, _, ext) in plan if ext is not None]
    shape = tuple(so) if so else (1,)
    coords = unpack(I.Pid(), list(shape))
    sel, k = [], 0
    for (start, step, ext) in plan:
        if start is None:
            k += 1                        # a new axis: an output coordinate only
        elif ext is None:
            sel.append(I.Lit(start))
        else:
            c = coords[k]; k += 1
            e = c if step == 1 else c * I.Lit(step)
            sel.append(I.mk_add(e, I.Lit(start)))
    st = Lowered(
        family="genred", body=S.Inp(v.buf), arity=ch.nbuf + 1,
        out_size=_prod(shape), out_shape=shape,
        tensor_arg_index=list(ch.arg_index), K=1,
        offs=ch.pad({v.buf: pack(sel, list(v.shape))}),
        post_offs=ch.pad({}), post=S.Inp(0), notes=[note])
    return ch.emit(st, shape)


def _split_parts(n: fx.Node, shape) -> Optional[Tuple[int, List[int]]]:
    """`(dim, part sizes)` for a `split`/`chunk`, or `None` if it is neither."""
    name = op_name(n.target)
    if name not in ("split", "chunk", "tensor_split"):
        return None
    if n.all_input_nodes and n.all_input_nodes[0] in shape:
        total_shape = list(shape[n.all_input_nodes[0]])
    else:
        return None
    arg = n.args[1] if len(n.args) > 1 else n.kwargs.get(
        "split_size" if name == "split" else "chunks")
    dim = n.args[2] if len(n.args) > 2 else n.kwargs.get("dim", 0)
    if not isinstance(dim, int):
        return None
    dim %= len(total_shape)
    total = total_shape[dim]
    if isinstance(arg, (list, tuple)) and all(isinstance(x, int) for x in arg):
        return dim, list(arg)
    if not isinstance(arg, int) or arg <= 0:
        return None
    if name == "split":
        sizes = [min(arg, total - i) for i in range(0, total, arg)]
    else:
        each = -(-total // arg)
        sizes = [min(each, total - i) for i in range(0, total, each)]
    return dim, sizes


def _cat_args(n: fx.Node, shapes) -> Optional[Tuple[List[fx.Node], int]]:
    """The tensors a `cat` joins and the axis, or `None` if this is not one."""
    if op_name(n.target) not in ("cat", "concat", "concatenate", "stack"):
        return None
    xs = n.args[0] if n.args else n.kwargs.get("tensors")
    if not isinstance(xs, (list, tuple)) or not all(isinstance(a, fx.Node) for a in xs):
        return None
    dim = n.args[1] if len(n.args) > 1 else n.kwargs.get("dim", 0)
    if not isinstance(dim, int) or n not in shapes:
        return None
    return list(xs), dim % len(shapes[n])


def _emit_cat(ch: Chain, n: fx.Node, env, shapes, xs: List[fx.Node], dim: int) -> Val:
    """Concatenation, as one reducing stage over the inputs being joined.

    This is the one operator that looked like it needed the IR extended, and does
    not. The family's mask is shared across input slots, so a body that selected
    between them per lane is not expressible -- but it does not have to be. Take the
    reduced axis to run over the *inputs*: `inRange` then says which input owns this
    lane, so exactly one value of `k` contributes, and `idxSlot` -- already there, to
    give an argmax its index -- hands the body `k` as a scalar so it can read that
    input's slot. Every other slot is loaded and discarded, which is what the shared
    mask makes unavoidable and is harmless: those reads are clamped into their own
    buffer, and nothing downstream sees them.

    Nothing new is proved. It is `GenRed` at the same theorem as a convolution.
    """
    so = list(shapes[n])
    vs = [env[a] for a in xs]
    if op_name(n.target) == "stack":
        # `stack` is `cat` of inputs that each gain a unit axis at `dim`; that axis
        # is a relabelling of the same buffer, not a copy.
        vs = [Val(v.buf, tuple(v.shape[:dim]) + (1,) + tuple(v.shape[dim:]))
              for v in vs]
    return _emit_cat_vals(ch, vs, dim, so)


#: The widest concatenation emitted as one stage. Its body selects between the
#: parts with one nested `selLe` per part, and Python's parser refuses nesting past
#: about 200; wider ones are joined as a tree of narrower ones.
CAT_FANOUT = 32


def _emit_cat_vals(ch: Chain, vs: List[Val], dim: int, so: List[int]) -> Val:
    # An empty part contributes nothing -- a key/value cache that starts empty is
    # concatenated onto every step's keys -- and has no element to read.
    vs = [v for v in vs if v.numel != 0]
    if not vs:
        raise Unsupported("concatenation of empty tensors")
    if len(vs) == 1 and list(vs[0].shape) == list(so):
        return vs[0]
    # One buffer is read at one index map per stage, and each part needs its own --
    # so a tensor joined to itself (`cat([h, h])`, Reformer's reversible residual)
    # must not share a slot with its other occurrence. Before this, the second
    # part's map silently replaced the first's. A repeat gets a copy of its own.
    seen, fresh = set(), []
    for v in vs:
        if v.buf in seen:
            st = Lowered(
                family="genred", body=S.Inp(v.buf), arity=ch.nbuf + 1,
                out_size=v.numel, out_shape=tuple(v.shape),
                tensor_arg_index=list(ch.arg_index), K=1,
                offs=ch.pad({v.buf: I.Pid()}), post_offs=ch.pad({}), post=S.Inp(0),
                notes=[f"copy of buffer {v.buf}, joined to itself"])
            v = ch.emit(st, tuple(v.shape))
        seen.add(v.buf)
        fresh.append(v)
    vs = fresh
    if len(vs) > CAT_FANOUT:
        groups = [vs[i:i + CAT_FANOUT] for i in range(0, len(vs), CAT_FANOUT)]
        parts = []
        for grp in groups:
            gso = list(so)
            gso[dim] = sum(v.shape[dim] for v in grp)
            parts.append(_emit_cat_vals(ch, grp, dim, gso))
        return _emit_cat_vals(ch, parts, dim, so)
    sizes = [v.shape[dim] for v in vs]
    starts, acc = [], 0
    for sz in sizes:
        starts.append(acc)
        acc += sz
    if acc != so[dim]:
        raise Unsupported(f"cat: parts sum to {acc}, output has {so[dim]}")
    coords = unpack(I.Pid(), so)
    c = coords[dim]
    k = I.Rk()
    offs: Dict[int, I.IE] = {}
    for v, st, sz in zip(vs, starts, sizes):
        # The slot that owns this lane is read at `c - start`, which is in range.
        # The others are read too -- the mask is shared -- and their coordinate is
        # not, so clamp it here rather than leaving it to `record_bounds`, which
        # only guards reads of *intermediate* buffers. A concatenation whose parts
        # include a graph input would otherwise read off the end of it.
        t = I.mk_sub(c, I.Lit(st))
        sel = list(coords)
        sel[dim] = I.mk_sub(t, I.mk_sub(t, I.Lit(sz - 1)))     # min(t, sz - 1)
        offs[v.buf] = pack(sel, list(v.shape))
    # which input owns this lane: exactly one `k`, so exactly one summand survives
    live = I.any_of([
        I.all_of([I.eq(k, I.Lit(i)), I.le(I.Lit(st), c), I.lt(c, I.Lit(st + sz))])
        for i, (st, sz) in enumerate(zip(starts, sizes))])
    # `k` as a scalar, so the body can pick the slot that owns the lane. A slot
    # above every buffer, so it shadows none of them.
    islot = ch.nbuf + 1
    body = S.Inp(vs[-1].buf)
    for i in range(len(vs) - 2, -1, -1):
        body = S.SelLe(S.Inp(islot), S.lit(i + 0.5), S.Inp(vs[i].buf), body)
    st = Lowered(
        family="genred", body=body, arity=ch.nbuf + 1,
        out_size=_prod(so), out_shape=tuple(so),
        tensor_arg_index=list(ch.arg_index), K=len(vs),
        offs=ch.pad(offs), post_offs=ch.pad({}), post=S.Inp(0),
        in_range=live, idx_slot=islot,
        notes=[f"cat of {len(vs)} tensors along dim {dim}: "
               f"sizes {sizes} at offsets {starts}"])
    return ch.emit(st, tuple(so))


def _relabel_of(n: fx.Node, shapes) -> Optional[Tuple[str, Any]]:
    """An `expand` that really broadcasts, or a `Tensor.unfold`: operators that move
    no arithmetic, only coordinates, and that `_emit_relabel` expresses as an index
    map. `None` for anything else."""
    name = op_name(n.target)
    if n.op not in ("call_method", "call_function") or n not in shapes:
        return None
    src = n.all_input_nodes[0] if n.all_input_nodes else None
    if src is None or src not in shapes:
        return None
    if name in ("expand", "expand_as", "broadcast_to"):
        if _prod(shapes[n]) == _prod(shapes[src]):
            return None                   # a relabelling, handled as an alias
        return ("expand", None)
    if name == "unfold" and n.op == "call_method" and len(n.args) == 4 \
            and all(isinstance(a, int) for a in n.args[1:]):
        return ("unfold", tuple(n.args[1:]))
    if name == "pad" and n.op == "call_function":
        pads = n.args[1] if len(n.args) > 1 else n.kwargs.get("pad")
        pmode = n.args[2] if len(n.args) > 2 else n.kwargs.get("mode", "constant")
        value = n.args[3] if len(n.args) > 3 else n.kwargs.get("value", None)
        if pmode != "constant" or value not in (None, 0, 0.0):
            raise Unsupported(f"pad mode {pmode!r} value {value!r}")
        if not all(isinstance(p, int) and p >= 0 for p in pads):
            raise Unsupported(f"pad amounts {pads!r}")
        return ("pad", tuple(pads))
    if name == "roll":
        sh = n.args[1] if len(n.args) > 1 else n.kwargs.get("shifts")
        dims = n.args[2] if len(n.args) > 2 else n.kwargs.get("dims")
        sh = (sh,) if isinstance(sh, int) else tuple(sh)
        dims = (dims,) if isinstance(dims, int) else tuple(dims or ())
        if len(sh) != len(dims) or not dims:
            raise Unsupported("roll without matching shifts and dims")
        return ("roll", (sh, dims))
    if name in ("zeros_like", "ones_like"):
        return ("const", 0 if name == "zeros_like" else 1)
    if name in ("tril", "triu"):
        dg = n.kwargs.get("diagonal", n.args[1] if len(n.args) > 1 else 0)
        if not isinstance(dg, int):
            raise Unsupported(f"{name} with diagonal {dg!r}")
        return (name, dg)
    return None


def _emit_relabel(ch: Chain, n: fx.Node, v: Val, so: Tuple[int, ...], kind: str,
                  arg) -> Val:
    """Emit an `expand` or `unfold` as a `K = 1` stage whose index map carries it.

    `expand` pins every broadcast axis of the source to 0, exactly as a broadcasting
    pointwise operator reads its narrower input. `unfold(d, size, step)` appends a
    window axis `j` and reads source coordinate `i_d * step + j` on axis `d`.
    """
    sv = list(v.shape)
    coords = unpack(I.Pid(), list(so))
    if kind == "expand":
        if len(sv) > len(so):
            raise Unsupported(f"expand from {tuple(sv)} to {so}")
        tail = coords[len(so) - len(sv):]
        for a_, b_ in zip(sv, so[len(so) - len(sv):]):
            if a_ not in (1, b_):
                raise Unsupported(f"expand from {tuple(sv)} to {so}")
        sel = [I.Lit(0) if d == 1 else c for c, d in zip(tail, sv)]
        note = f"expand {tuple(sv)} -> {so}"
    elif kind == "unfold":
        d, size, step = arg
        d %= len(sv)
        if list(so) != sv[:d] + [(sv[d] - size) // step + 1] + sv[d + 1:] + [size]:
            raise Unsupported(f"unfold{arg} of {tuple(sv)} gives {so}")
        sel = list(coords[:-1])
        sel[d] = I.mk_add(sel[d] * I.Lit(step) if step != 1 else sel[d], coords[-1])
        note = f"unfold{arg} of {tuple(sv)}"
    elif kind == "pad":
        # Pairs from the last axis backwards. A padded lane is excluded by the
        # range guard, so its sum is empty and it holds zero; the read itself is
        # clamped into the source so that it stays in bounds regardless.
        pads = list(arg)
        guards = []
        sel = list(coords)
        for i in range(len(pads) // 2):
            d = len(sv) - 1 - i
            lo, hi = pads[2 * i], pads[2 * i + 1]
            if so[d] != sv[d] + lo + hi:
                raise Unsupported(f"pad {pads} of {tuple(sv)} gives {so}")
            if lo == 0 and hi == 0:
                continue
            c = coords[d]
            t = I.mk_sub(c, I.Lit(lo))
            sel[d] = I.mk_sub(t, I.mk_sub(t, I.Lit(sv[d] - 1)))    # min(t, n - 1)
            guards += [I.le(I.Lit(lo), c), I.lt(c, I.Lit(lo + sv[d]))]
        note = f"pad {pads} of {tuple(sv)}"
        st = Lowered(
            family="genred", body=S.Inp(v.buf), arity=ch.nbuf + 1,
            out_size=_prod(so), out_shape=tuple(so),
            tensor_arg_index=list(ch.arg_index), K=1,
            offs=ch.pad({v.buf: pack(sel, sv)}), in_range=I.all_of(guards),
            post_offs=ch.pad({}), post=S.Inp(0), notes=[note])
        return ch.emit(st, tuple(so))
    elif kind == "roll":
        # out[.., o, ..] = x[.., (o - s) mod n, ..], with the shift made
        # non-negative first so the index map stays in the naturals.
        shifts, dims = arg
        if list(so) != sv:
            raise Unsupported(f"roll changes the shape {tuple(sv)} -> {so}")
        sel = list(coords)
        for sft, d in zip(shifts, dims):
            d %= len(sv)
            r = (-sft) % sv[d]
            if r:
                sel[d] = I.mk_mod(I.mk_add(sel[d], I.Lit(r)), I.Lit(sv[d]))
        note = f"roll by {shifts} along {dims} of {tuple(sv)}"
    elif kind in ("tril", "triu"):
        # Keep the lanes on the right side of the diagonal; the others fall outside
        # the range guard, so their sum is empty and they hold zero.
        if len(so) < 2 or list(so) != sv:
            raise Unsupported(f"{kind} of {tuple(sv)}")
        row, col = coords[-2], coords[-1]
        dg = arg
        if kind == "tril":        # col - row <= dg
            keep = (I.le(col, I.mk_add(row, I.Lit(dg))) if dg >= 0
                    else I.le(I.mk_add(col, I.Lit(-dg)), row))
        else:                     # col - row >= dg
            keep = (I.le(I.mk_add(row, I.Lit(dg)), col) if dg >= 0
                    else I.le(row, I.mk_add(col, I.Lit(-dg))))
        st = Lowered(
            family="genred", body=S.Inp(v.buf), arity=ch.nbuf + 1,
            out_size=_prod(so), out_shape=tuple(so),
            tensor_arg_index=list(ch.arg_index), K=1,
            offs=ch.pad({v.buf: I.Pid()}), in_range=keep,
            post_offs=ch.pad({}), post=S.Inp(0),
            notes=[f"{kind}(diagonal={dg}) of {tuple(sv)}"])
        return ch.emit(st, tuple(so))
    else:                                                   # const
        st = Lowered(
            family="genred", body=S.lit(arg), arity=ch.nbuf + 1,
            out_size=_prod(so), out_shape=tuple(so),
            tensor_arg_index=list(ch.arg_index), K=1,
            offs=ch.pad({}), post_offs=ch.pad({}), post=S.Inp(0),
            notes=[f"constant {arg} of shape {tuple(so)}"])
        return ch.emit(st, tuple(so))
    st = Lowered(
        family="genred", body=S.Inp(v.buf), arity=ch.nbuf + 1,
        out_size=_prod(so), out_shape=tuple(so),
        tensor_arg_index=list(ch.arg_index), K=1,
        offs=ch.pad({v.buf: pack(sel, sv) if sv else I.Lit(0)}),
        post_offs=ch.pad({}), post=S.Inp(0), notes=[note])
    return ch.emit(st, tuple(so))


def _emit_gather(ch: Chain, x: Val, dim: int, index: Val, so: Tuple[int, ...]) -> Val:
    """`torch.gather(x, dim, index)`: `out[.., i, ..] = x[.., index[.., i, ..], ..]`,
    the index replacing coordinate `dim`. A masked sum over that axis, like
    `_emit_take`: `sum_k x[.., k, ..] * [index[q] = k]`."""
    sx, si = list(x.shape), list(index.shape)
    dim %= len(sx)
    if list(so) != si or len(si) != len(sx) or any(
            a > b for d, (a, b) in enumerate(zip(si, sx)) if d != dim):
        raise Unsupported(f"gather of {tuple(sx)} by {tuple(si)} along {dim}")
    coords = unpack(I.Pid(), list(so))
    sel = list(coords)
    sel[dim] = I.Rk()
    islot = ch.nbuf + 1
    k, v = S.Inp(islot), S.Inp(index.buf)
    hit = S.SelLe(v, k, S.SelLe(k, v, S.lit(1), S.lit(0)), S.lit(0))
    st = Lowered(
        family="genred", body=S.Inp(x.buf) * hit, arity=ch.nbuf + 1,
        out_size=_prod(so), out_shape=tuple(so),
        tensor_arg_index=list(ch.arg_index), K=sx[dim],
        offs=ch.pad({x.buf: pack(sel, sx), index.buf: I.Pid()}),
        post_offs=ch.pad({}), post=S.Inp(0), idx_slot=islot,
        notes=[f"gather along {dim} of {tuple(sx)} at an index of {tuple(si)}"])
    return ch.emit(st, tuple(so))


def _emit_index_select(ch: Chain, x: Val, dim: int, index: Val,
                       so: Tuple[int, ...]) -> Val:
    """`torch.index_select(x, dim, index)`: coordinate `i` on axis `dim` reads
    `x` at `index[i]`. The masked sum of `_emit_take`, along any axis."""
    sx, si = list(x.shape), list(index.shape)
    dim %= len(sx)
    if len(si) != 1 or list(so) != sx[:dim] + si + sx[dim + 1:]:
        raise Unsupported(f"index_select of {tuple(sx)} by {tuple(si)} along {dim}")
    coords = unpack(I.Pid(), list(so))
    sel = list(coords)
    sel[dim] = I.Rk()
    islot = ch.nbuf + 1
    k, v = S.Inp(islot), S.Inp(index.buf)
    hit = S.SelLe(v, k, S.SelLe(k, v, S.lit(1), S.lit(0)), S.lit(0))
    st = Lowered(
        family="genred", body=S.Inp(x.buf) * hit, arity=ch.nbuf + 1,
        out_size=_prod(so), out_shape=tuple(so),
        tensor_arg_index=list(ch.arg_index), K=sx[dim],
        offs=ch.pad({x.buf: pack(sel, sx), index.buf: coords[dim]}),
        post_offs=ch.pad({}), post=S.Inp(0), idx_slot=islot,
        notes=[f"index_select along {dim} of {tuple(sx)}, {si[0]} indices"])
    return ch.emit(st, tuple(so))


def _emit_softmax_matmul(ch: Chain, sv: Val, vv: Val, so: Tuple[int, ...]) -> Val:
    """`softmax(s, -1) @ v` in three stages, never storing the probabilities:

        m[r]    = max_j s[r, j]
        Z[r]    = sum_j exp(s[r, j] - m[r])
        out[r,d] = (sum_j exp(s[r, j] - m[r]) v[j, d]) / Z[r]

    `r` runs over the batch axes and the query axis together. The shift by `m` is
    PyTorch's own, and cancels in exact arithmetic."""
    ss, vs = list(sv.shape), list(vv.shape)
    if len(ss) < 2 or len(vs) != len(ss) or ss[:-2] != vs[:-2] or ss[-1] != vs[-2]:
        raise Unsupported(f"softmax(s) @ v with s {tuple(ss)}, v {tuple(vs)}")
    S_, D = ss[-1], vs[-1]
    R = _prod(ss[:-1])                       # rows: batch axes and queries
    Lq = ss[-2]
    q = I.Pid()
    n = ch.nbuf + 1
    m1 = Lowered(family="maxred", body=S.Inp(sv.buf), arity=n, out_size=R,
                 out_shape=(R,), tensor_arg_index=list(ch.arg_index), K=S_,
                 offs=ch.pad({sv.buf: q * I.Lit(S_) + I.Rk()}), post_offs=ch.pad({}),
                 post=S.Inp(0), idx_slot=n,
                 notes=[f"softmax-matmul: row maxima of {R} rows of {S_}"])
    mb = ch.emit(m1, (R,)).buf
    n = ch.nbuf + 1
    z = Lowered(family="genred", body=S.exp(S.Inp(sv.buf) - S.Inp(mb)), arity=n,
                out_size=R, out_shape=(R,), tensor_arg_index=list(ch.arg_index), K=S_,
                offs=ch.pad({sv.buf: q * I.Lit(S_) + I.Rk(), mb: q}),
                post_offs=ch.pad({}), post=S.Inp(0),
                notes=["softmax-matmul: row sums of exp(s - max)"])
    zb = ch.emit(z, (R,)).buf
    n = ch.nbuf + 1
    r = q // I.Lit(D)
    d = q % I.Lit(D)
    bt = r // I.Lit(Lq)                      # the batch part of the row
    o = Lowered(family="genred",
                body=S.exp(S.Inp(sv.buf) - S.Inp(mb)) * S.Inp(vv.buf), arity=n,
                out_size=R * D, out_shape=tuple(so), tensor_arg_index=list(ch.arg_index),
                K=S_,
                offs=ch.pad({sv.buf: r * I.Lit(S_) + I.Rk(), mb: r,
                             vv.buf: (bt * I.Lit(S_) + I.Rk()) * I.Lit(D) + d}),
                post_offs=ch.pad({zb: r}),
                post=S.Inp(0) * S.Recip(S.Inp(zb + 1)),
                notes=["softmax-matmul: exp-weighted values over the row sum"])
    return ch.emit(o, tuple(so))


def _emit_take(ch: Chain, table: Val, index: Val, so: Tuple[int, ...]) -> Val:
    """`table[index]` for an integer tensor `index`: a gather along axis 0.

    A gather is a masked sum, and the index map stays data-independent:
    `out[i, r] = sum_k table[k, r] * [index[i] = k]`, where `k` reaches the body as
    a scalar through `idxSlot` and `index[i]` is read as an ordinary value. The
    comparison is between two values, not an address computed from data -- which is
    what lets `qkOnly` keep forbidding data-dependent index maps.
    """
    ts, xs = list(table.shape), list(index.shape)
    rest = ts[1:]
    if list(so) != xs + rest:
        raise Unsupported(f"index of {tuple(ts)} by {tuple(xs)} gives {so}")
    nr = _prod(rest)
    q = I.Pid()
    i, r = q // I.Lit(nr), q % I.Lit(nr)
    islot = ch.nbuf + 1
    k = S.Inp(islot)
    x = S.Inp(index.buf)
    hit = S.SelLe(x, k, S.SelLe(k, x, S.lit(1), S.lit(0)), S.lit(0))
    st = Lowered(
        family="genred", body=S.Inp(table.buf) * hit, arity=ch.nbuf + 1,
        out_size=_prod(so), out_shape=tuple(so),
        tensor_arg_index=list(ch.arg_index), K=ts[0],
        offs=ch.pad({table.buf: I.Rk() * I.Lit(nr) + r if nr > 1 else I.Rk(),
                     index.buf: i if nr > 1 else q}),
        post_offs=ch.pad({}), post=S.Inp(0), idx_slot=islot,
        notes=[f"gather rows of {tuple(ts)} at an index of shape {tuple(xs)}"])
    return ch.emit(st, tuple(so))


def _perm_of(n: fx.Node, rank: Optional[int]) -> Optional[List[int]]:
    """The axis permutation this node applies, or `None` if it is not one.

    `.T`, `transpose(a, b)` and `permute(...)` differ only in how the permutation is
    written down, so they are recognised together and lowered once.
    """
    name = op_name(n.target)
    if rank is None or not n.all_input_nodes:
        return None
    if name == "getattr" and len(n.args) > 1 and n.args[1] == "T":
        if rank != 2:
            raise Unsupported(f".T on a {rank}-D tensor")
        return [1, 0]
    if name == "t":
        if rank > 2:
            raise Unsupported(f"t() on a {rank}-D tensor")
        return list(range(rank))[::-1]
    if name == "transpose" and len(n.args) == 3:
        a, b = n.args[1], n.args[2]
        if not isinstance(a, int) or not isinstance(b, int):
            return None
        a, b = a % rank, b % rank
        perm = list(range(rank))
        perm[a], perm[b] = perm[b], perm[a]
        return perm
    if name == "permute":
        dims = n.args[1] if len(n.args) == 2 and isinstance(n.args[1], (list, tuple)) \
            else list(n.args[1:])
        if len(dims) != rank or not all(isinstance(d, int) for d in dims):
            return None
        return [d % rank for d in dims]
    return None


class _Converted:
    """A node as a pointwise builder sees it: its tensor operands already turned
    into spec expressions, in keyword arguments as well as positional ones
    (`clamp(x, max=t)`). `orig` is the node itself, for a builder that needs to ask
    about the graph."""

    def __init__(self, node: fx.Node, args, kwargs):
        self.orig, self.target, self.op = node, node.target, node.op
        self.args, self.kwargs = tuple(args), dict(kwargs)


def _pointwise_se(node: fx.Node, gm: fx.GraphModule, args: List[Any],
                  conv=None) -> S.SE:
    from .frontend import POINTWISE_FUNCS, POINTWISE_MODULES
    if node.op == "call_module":
        sub = gm.get_submodule(node.target)
        return POINTWISE_MODULES[type(sub)](sub, args)
    if conv is None:
        conv = lambda a: _const_of(a, gm)
    kw = {k: (conv(v) if isinstance(v, fx.Node) else v) for k, v in node.kwargs.items()}
    return table_get(POINTWISE_FUNCS, node.target)(args, _Converted(node, args, kw))


def _bind(node: fx.Node, target) -> Any:
    """A callable taking just this node's tensor inputs, with its other arguments
    (a `dim`, a `p`, a scalar) already supplied.

    Re-lowering a node on its own means calling it outside the graph, where those
    arguments are no longer implicit in the call site. The tensors are the node's
    *distinct* inputs, in `all_input_nodes` order -- the order the caller supplies
    shapes in -- and every occurrence is replaced, in keyword arguments too
    (`F.linear(input=x, weight=w)`) and however many times one appears
    (`matmul(x, x)`).
    """
    order = list(node.all_input_nodes)
    is_method = isinstance(target, str)

    def fn(*tensors):
        env = dict(zip(order, tensors))
        args = fx.node.map_arg(node.args, lambda a: env[a])
        kw = fx.node.map_arg(node.kwargs, lambda a: env[a])
        if is_method:
            # a `call_method` node's target is the method's *name*
            out = getattr(args[0], target)(*args[1:], **kw)
        else:
            out = target(*args, **kw)
        # `min`/`max` over a dim return `(values, indices)`; the chain follows the
        # values, and a `getitem 0` on the result is treated as a relabelling.
        return out[0] if isinstance(out, tuple) else out
    return fn


def _lower_one(sub, shapes_in: List[Tuple[int, ...]], mode, node=None) -> Lowered:
    """Lower a single operator by reusing the Level 1 frontend on a one-node module."""
    from .frontend import lower
    if node is not None and node.op != "call_module":
        sub = _bind(node, sub)
    elif node is not None and node.op == "call_module" and len(node.args) > len(shapes_in):
        sub = _bind(node, sub)
    w = _wrap(sub, max(1, len(shapes_in)))
    with mode:
        fake = [torch.zeros(s) for s in shapes_in]
        low, reasons = lower(w, fake)
    if low is None:
        raise Unsupported(reasons[-1] if reasons else "no family")
    return low


class _ShapeProxy(fx.Proxy):
    """A proxy that also knows the shape of the value it stands for.

    Plain symbolic tracing makes `x.size()` a symbolic value, so a model that
    computes with its own shapes -- `B, T, C = x.size()` and then `view(B, T, ...)`
    -- cannot be traced at all: the ints are proxies, and indexing or reshaping with
    them raises. The shapes here are not actually unknown, though. KernelBench fixes
    the input shape, so tracing can be specialised to it.

    That specialisation is a real assumption and worth naming: the resulting graph is
    correct for *this* input shape, not for every one. That is already true of every
    lowering in this project -- the index maps are derived from concrete extents --
    so it narrows nothing that was not narrow before.
    """

    def __init__(self, node, tracer, meta=None):
        super().__init__(node, tracer)
        self._meta = meta

    # -- what a model is allowed to ask about a tensor without forcing its value
    @property
    def shape(self):
        return self._meta.shape

    @property
    def ndim(self):
        return self._meta.dim()

    @property
    def dtype(self):
        return self._meta.dtype

    @property
    def device(self):
        # Tracing follows the path where every tensor is on one device, which is the
        # only path that does not raise: models that compare devices do so to reject
        # a mixed placement the real run never has.
        return torch.device("cpu")

    def size(self, dim=None):
        return self._meta.size() if dim is None else self._meta.size(dim)

    def dim(self):
        return self._meta.dim()

    def numel(self):
        return self._meta.numel()

    def __len__(self):
        return self._meta.shape[0]


#: `fx` replaces both of these for the duration of a trace -- `__call__` so module
#: calls become nodes, and `__getattr__` so parameter reads do. Captured here, before
#: any of that, so a shape computation can put them back and run a module for real
#: instead of tracing it a second time. Missing the second one is subtle: the module
#: call looks like it ran, but every parameter it read came back a proxy.
_ORIG_MODULE_CALL = nn.Module.__call__
_ORIG_MODULE_GETATTR = nn.Module.__getattr__


def pytree_leaves(x):
    from torch.utils import _pytree as pytree
    return pytree.tree_leaves(x)


def _unmeta(a):
    """Replace every proxy in a structure by the fake tensor it stands for.

    Structurally, not just at the top: `torch.cat` takes a *list* of tensors, and a
    proxy left inside one would make the operation return another proxy, which then
    stands in as a shape and fails much later and much less clearly.
    """
    from torch.utils import _pytree as pytree
    return pytree.tree_map_only(_ShapeProxy, lambda p: p._meta, a)


class ShapeTracer(fx.Tracer):
    """`fx.Tracer` that carries a fake tensor alongside every proxy.

    Used only as a fallback: a model that traces normally is traced normally, so
    this cannot change a graph that already worked.
    """

    def __init__(self, mode):
        super().__init__()
        self.proxy_buffer_attributes = True
        self.mode = mode
        self._args: List[Any] = []
        self._n_ph = 0
        self._in_meta = False

    def proxy(self, node):
        return _ShapeProxy(node, self)



    def create_proxy(self, kind, target, args, kwargs, name=None, type_expr=None,
                     proxy_factory_fn=None):
        proxy = super().create_proxy(kind, target, args, kwargs, name, type_expr,
                                     proxy_factory_fn)
        if isinstance(proxy, _ShapeProxy):
            proxy._meta = self._meta_for(kind, target, args, kwargs)
        return proxy

    def _meta_for(self, kind, target, args, kwargs):
        """Run this one operation on fake tensors, to learn what it produces.

        Anything that cannot be run this way simply has nothing recorded; the proxy
        still works for everything except asking about its shape.
        """
        if self._in_meta:
            return None
        self._in_meta = True
        try:
            fa, fk = _unmeta(tuple(args)), _unmeta(dict(kwargs))
            if any(isinstance(x, fx.Proxy)
                   for x in pytree_leaves(fa) + pytree_leaves(fk)):
                return None                 # a shape we could not resolve
            # Running the operation, not tracing it: with fx's patched `__call__`
            # still in place, a module call here would be recorded a second time and
            # its module-path bookkeeping would desynchronise.
            saved = (nn.Module.__call__, nn.Module.__getattr__)
            nn.Module.__call__ = _ORIG_MODULE_CALL
            nn.Module.__getattr__ = _ORIG_MODULE_GETATTR
            try:
              with self.mode:
                if kind == "placeholder":
                    out = self._args[self._n_ph] if self._n_ph < len(self._args) else None
                    self._n_ph += 1
                elif kind == "get_attr":
                    out = _fetch_attr(self.root, target)
                elif kind == "call_function":
                    out = target(*fa, **fk)
                elif kind == "call_method":
                    out = getattr(fa[0], target)(*fa[1:], **fk)
                elif kind == "call_module":
                    out = self.root.get_submodule(target)(*fa, **fk)
                else:
                    out = None
            finally:
                nn.Module.__call__, nn.Module.__getattr__ = saved
            # Kept whatever it is, not narrowed to a tensor: `split` returns a
            # tuple, and the `getitem` that follows has to be able to index it.
            return out
        except Exception:
            return None
        finally:
            self._in_meta = False


def _fetch_attr(root, target: str):
    obj = root
    for part in target.split("."):
        obj = getattr(obj, part)
    return obj


def _parse_axes(side: str) -> List[Any]:
    """`b (c l) ... h` -> ['b', ['c', 'l'], '...', 'h']."""
    out: List[Any] = []
    group: Optional[List[str]] = None
    for tok in side.replace("(", " ( ").replace(")", " ) ").split():
        if tok == "(":
            if group is not None:
                raise Unsupported("nested parentheses in a rearrange pattern")
            group = []
        elif tok == ")":
            if group is None:
                raise Unsupported("unbalanced rearrange pattern")
            out.append(group)
            group = None
        elif group is not None:
            group.append(tok)
        else:
            out.append(tok)
    if group is not None:
        raise Unsupported("unbalanced rearrange pattern")
    return out


def rearrange_as_views(x, pattern: str, **axes_lengths):
    """`einops.rearrange`, spelled as `reshape`, `permute`, `reshape`.

    einops does not know an `fx` proxy, so a model that calls it cannot be traced
    as it stands. What `rearrange` does is fully determined by the pattern and the
    input's shape: split every grouped input axis into its parts, reorder the parts,
    merge the output groups. Written with tensor methods, that traces into nodes the
    chain already lowers -- a permutation, and relabellings. Only splitting,
    merging and reordering is modelled; an axis that appears on one side only (a
    repeat or a reduction) is refused.
    """
    lhs, rhs = (s.strip() for s in pattern.split("->"))
    L, R = _parse_axes(lhs), _parse_axes(rhs)
    shape = list(x.shape)
    n_ell = len(shape) - (len(L) - (1 if "..." in L else 0))
    ell = [f"_e{i}" for i in range(max(0, n_ell))]

    def expand(side):
        flat, groups = [], []
        for it in side:
            if it == "...":
                flat += ell
                groups += [[e] for e in ell]
            elif isinstance(it, list):
                flat += it
                groups.append(list(it))
            else:
                flat.append(it)
                groups.append([it])
        return flat, groups

    lf, lg = expand(L)
    rf, rg = expand(R)
    if sorted(lf) != sorted(rf) or len(set(lf)) != len(lf):
        raise Unsupported(f"rearrange {pattern!r} is not a pure permutation")
    if len(lg) != len(shape):
        raise Unsupported(f"rearrange {pattern!r} against rank {len(shape)}")
    size: Dict[str, int] = {}
    for grp, d in zip(lg, shape):
        known = [a for a in grp if a in axes_lengths]
        unknown = [a for a in grp if a not in axes_lengths]
        prod_known = _prod([axes_lengths[a] for a in known])
        for a in known:
            size[a] = axes_lengths[a]
        if len(unknown) > 1:
            raise Unsupported(f"rearrange {pattern!r}: cannot infer {unknown}")
        if unknown:
            if d % prod_known:
                raise Unsupported(f"rearrange {pattern!r}: {d} not divisible")
            size[unknown[0]] = d // prod_known
        elif prod_known != d:
            raise Unsupported(f"rearrange {pattern!r}: group sizes do not match {d}")
    y = x.reshape(*[size[a] for a in lf])
    perm = [lf.index(a) for a in rf]
    if perm != list(range(len(perm))):
        y = y.permute(*perm)
    return y.reshape(*[_prod([size[a] for a in g]) for g in rg])


RANDOM_FACTORIES = ("rand", "randn", "randint", "rand_like", "randn_like",
                    "randint_like", "normal", "bernoulli", "multinomial", "randperm")

_TORCH_RANDN = torch.randn
#: The tracer currently running, so a draw made during a trace can become a node.
_ACTIVE_TRACER: List[Any] = []

#: The parameter-path prefix naming a fresh standard-normal draw. Not a parameter:
#: the runtime fills that buffer with `torch.randn` on every call.
RANDN_PREFIX = "__randn__/"


def fresh_randn(shape):
    """A fresh standard-normal tensor -- the graph node a `torch.randn` in a forward
    becomes."""
    return _TORCH_RANDN(shape)


def _refuse_randomness():
    """Make random factories, for the duration of a trace, either record the draw
    or refuse.

    A forward that draws `torch.randn(...)` from constant shapes would otherwise
    run it eagerly while tracing, and the draw would become a *constant* of the
    spec -- a deterministic function the reference is not, since it draws afresh on
    every call. What `randn` becomes instead is a node, `fresh_randn`, which the
    chain gives an input buffer of its own and the runtime fills with a fresh draw
    on every call: the same random function, its randomness kept outside the
    verified core. Every other factory still refuses."""
    saved = []
    for name in RANDOM_FACTORIES:
        f = getattr(torch, name, None)
        if f is None:
            continue
        saved.append((name, f))

        def refuse(*a, _name=name, **k):
            raise Unsupported(f"torch.{_name} in forward: the reference is random")

        def record(*a, **k):
            shape = a[0] if len(a) == 1 and isinstance(a[0], (tuple, list, torch.Size)) \
                else a
            if not _ACTIVE_TRACER or not all(isinstance(d, int) for d in shape) \
                    or k.get("generator") is not None \
                    or k.get("dtype") not in (None, torch.float32):
                raise Unsupported("torch.randn in forward with a shape, dtype or "
                                  "generator this lowering does not record")
            return _ACTIVE_TRACER[-1].create_proxy(
                "call_function", fresh_randn, (tuple(int(d) for d in shape),), {})
        setattr(torch, name, record if name == "randn" else refuse)
    return saved


def _einops_patched(model: nn.Module):
    """Point every `rearrange` a model's forwards can see at `rearrange_as_views`
    for the duration of a trace. Returns what to restore."""
    try:
        import einops
    except ImportError:
        return []
    saved = []
    seen = set()
    for m in model.modules():
        g = getattr(type(m).forward, "__globals__", None)
        if g is None or id(g) in seen:
            continue
        seen.add(id(g))
        if g.get("rearrange") is einops.rearrange:
            saved.append((g, g["rearrange"]))
            g["rearrange"] = rearrange_as_views
    return saved


def trace_model(model: nn.Module, example_args: List[Any], mode) -> fx.GraphModule:
    """Trace, falling back to a shape-aware trace for models that compute with
    their own shapes."""
    from .frontend import preserved_state
    saved = _einops_patched(model)
    rng = _refuse_randomness()
    try:
        with preserved_state(model):
            gm = _trace_model(model, example_args, mode)
        # The GraphModule copied each attribute it reads while the trace's own
        # assignments were still in place; read them again from the restored
        # module, so `self.hidden` is the module's state and not a stale proxy.
        for n in gm.graph.nodes:
            if n.op == "get_attr":
                try:
                    v = _fetch_attr(model, n.target)
                except AttributeError:
                    continue            # a constant the trace itself lifted
                if isinstance(v, torch.Tensor) and not isinstance(v, nn.Parameter) \
                        and not isinstance(_fetch_attr(gm, n.target), nn.Parameter):
                    owner, _, leaf = n.target.rpartition(".")
                    setattr(gm.get_submodule(owner) if owner else gm, leaf, v)
        return gm
    finally:
        for g, f in saved:
            g["rearrange"] = f
        for name, f in rng:
            setattr(torch, name, f)


def _unpassed_defaults(model: nn.Module, n_given: int) -> Dict[str, Any]:
    """The forward arguments the task does not pass, at their defaults.

    Traced as proxies, `initial_states=None` would take the `is not None` branch --
    a proxy is not `None` -- and the graph would describe a call the task never
    makes. Binding them to the value they will actually have makes the trace follow
    the branch that runs.
    """
    import inspect
    try:
        params = list(inspect.signature(model.forward).parameters.values())
    except (TypeError, ValueError):
        return {}
    out = {}
    for p in params[n_given:]:
        if p.kind in (p.VAR_POSITIONAL, p.VAR_KEYWORD):
            break
        if p.default is not inspect.Parameter.empty:
            out[p.name] = p.default
    return out


def _drop_specialisation_guards(gm: fx.GraphModule) -> None:
    """`fx` guards a bound argument with an assertion that it still has the value it
    was bound to. The argument is never passed, so the assertion cannot fail; drop
    it, so the placeholder is visibly unused."""
    for n in list(gm.graph.nodes):
        if n.op == "call_function" and getattr(n.target, "__name__", "") == \
                "_assert_is_none":
            gm.graph.erase_node(n)
    gm.recompile()


def _trace_model(model: nn.Module, example_args: List[Any], mode) -> fx.GraphModule:
    concrete = _unpassed_defaults(model, len(example_args)) or None
    try:
        # Buffers are traced as reads, not captured as values: a mask computed from
        # a buffer (`bias[:, :, :T, :T] == 0`) is then a computation on a named
        # tensor the kernel reads, rather than a constant evaluated at trace time.
        plain = fx.Tracer()
        plain.proxy_buffer_attributes = True
        _ACTIVE_TRACER.append(plain)
        try:
            graph = plain.trace(model, concrete_args=concrete)
        finally:
            _ACTIVE_TRACER.pop()
        if any((n.op == "call_method" and n.target in ("size", "dim", "numel"))
               or (n.op == "call_function" and op_name(n.target) == "getattr"
                   and len(n.args) > 1 and n.args[1] in ("shape", "ndim"))
               for n in graph.nodes):
            # The graph computes with its own shapes as traced values; the
            # shape-aware trace specialises them to the task's actual sizes.
            raise Unsupported("graph computes with traced shapes")
        gm = fx.GraphModule(plain.root, graph)
        _drop_specialisation_guards(gm)
        gm.graph.lint()
        return gm
    except Exception as first:
        tracer = ShapeTracer(mode)
        with mode:
            tracer._args = [torch.empty(tuple(a.shape), dtype=a.dtype)
                            if isinstance(a, torch.Tensor) else a
                            for a in example_args]
        _ACTIVE_TRACER.append(tracer)
        try:
            graph = tracer.trace(model, concrete_args=concrete)
        except Exception as second:
            # The shape-aware trace gets further than the plain one whenever the
            # plain one fails on shapes, so its failure is the informative one.
            raise second from first
        finally:
            _ACTIVE_TRACER.pop()
        gm = fx.GraphModule(tracer.root, graph)
        _drop_specialisation_guards(gm)
        gm.graph.lint()
        return gm


def _is_neg_inf(v) -> bool:
    return isinstance(v, float) and v == float("-inf")


def _softmax_dim(u: fx.Node, gm: fx.GraphModule) -> Optional[int]:
    """The axis of a softmax call, or `None` if `u` is not a softmax."""
    if u.op == "call_module":
        sub = gm.get_submodule(u.target)
        return sub.dim if isinstance(sub, nn.Softmax) else None
    if op_name(u.target) == "softmax":
        d = u.kwargs.get("dim", u.args[1] if len(u.args) > 1 else None)
        if not isinstance(d, int):
            raise Unsupported("softmax without a literal dim")
        return d
    return None


def _is_relu(u: fx.Node, gm: fx.GraphModule) -> bool:
    if u.op == "call_module":
        return type(gm.get_submodule(u.target)) is nn.ReLU
    return op_name(u.target) in ("relu", "relu_")


def rewrite_sdpa(gm: fx.GraphModule, shapes, dtypes) -> None:
    """Spell `scaled_dot_product_attention` out as its definition.

        softmax(Q K^T * scale + mask) V

    with a causal mask built as `tril(ones(L, S)) == 0` and applied as
    `masked_fill(-inf)` -- which `rewrite_neg_inf` then folds into the softmax,
    since `-inf` is not a value the specs can hold. A boolean `attn_mask` is the
    same fill of its complement; a float one is added.
    """
    g = gm.graph
    for n in list(g.nodes):
        if op_name(n.target) != "scaled_dot_product_attention":
            continue
        q, k, v = n.args[:3]
        kw = dict(n.kwargs)
        extra = list(n.args[3:])
        names = ["attn_mask", "dropout_p", "is_causal", "scale", "enable_gqa"]
        for nm, a in zip(names, extra):
            kw[nm] = a
        mask = kw.get("attn_mask")
        if kw.get("dropout_p", 0.0) not in (0, 0.0) or kw.get("enable_gqa", False):
            raise Unsupported("attention with dropout or grouped heads")
        sq, sk = shapes.get(q), shapes.get(k)
        if sq is None or sk is None:
            raise Unsupported("attention operands of unknown shape")
        Lq, Sk, E = sq[-2], sk[-2], sq[-1]
        scale = kw.get("scale")
        with g.inserting_before(n):
            kt = g.call_method("transpose", (k, -2, -1))
            s = g.call_function(torch.matmul, (q, kt))
            s = g.call_function(operator.mul, (s, float(scale) if scale is not None
                                                  else 1.0 / math.sqrt(E)))
            if kw.get("is_causal", False):
                if mask is not None:
                    raise Unsupported("attention with both a mask and is_causal")
                ones = g.call_function(torch.ones, (Lq, Sk))
                keep = g.call_function(torch.tril, (ones,))
                drop = g.call_function(operator.eq, (keep, 0))
                s = g.call_method("masked_fill", (s, drop, float("-inf")))
            elif mask is not None:
                ms = shapes.get(mask)
                if ms is None:
                    raise Unsupported("attention mask of unknown shape")
                if dtypes.get(mask) is torch.bool:
                    # PyTorch's boolean mask says which entries to *keep*
                    drop = g.call_function(operator.invert, (mask,))
                    s = g.call_method("masked_fill", (s, drop, float("-inf")))
                else:
                    s = g.call_function(operator.add, (s, mask))
            a = g.call_function(F.softmax, (s,), {"dim": -1})
            out = g.call_function(torch.matmul, (a, v))
        n.replace_all_uses_with(out)
        g.erase_node(n)
    g.lint()
    gm.recompile()


def softmax_matmul(s, v):
    """`softmax(s, -1) @ v`, as one node -- what `rewrite_softmax_matmul` makes of the
    pair, so the probabilities are never stored."""
    return torch.matmul(torch.softmax(s, dim=-1), v)


def rewrite_softmax_matmul(gm: fx.GraphModule) -> None:
    """Fuse `matmul(softmax(s, dim=-1), v)` when the softmax has no other reader.

    The probabilities are as large as the scores, and nothing but the product needs
    them; `_emit_softmax_matmul` computes the product from the scores directly, so
    an attention over 16384 positions stores its scores once, not twice."""
    g = gm.graph
    for n in list(g.nodes):
        if op_name(n.target) != "matmul" or len(n.args) != 2:
            continue
        a, v = n.args
        if not isinstance(a, fx.Node) or len(a.users) != 1:
            continue
        try:
            d = _softmax_dim(a, gm)
        except Unsupported:
            continue
        if d != -1:                       # over the last axis, the one contracted
            continue
        with g.inserting_before(n):
            f = g.call_function(softmax_matmul, (a.args[0], v))
        n.replace_all_uses_with(f)
        g.erase_node(n)
        g.erase_node(a)
    g.lint()
    gm.recompile()


def rewrite_logsumexp(gm: fx.GraphModule) -> None:
    """`logsumexp(x, dim) = log(sum(exp(x - m))) + m` with `m` the maximum along
    `dim` -- PyTorch's own definition, shifted so `exp` cannot overflow. Spelled out
    so its parts lower as the reductions they are."""
    g = gm.graph
    for n in list(g.nodes):
        if op_name(n.target) != "logsumexp":
            continue
        x = n.kwargs.get("input", n.args[0])
        d = n.kwargs.get("dim", n.args[1] if len(n.args) > 1 else None)
        keep = n.kwargs.get("keepdim", n.args[2] if len(n.args) > 2 else False)
        if isinstance(d, (list, tuple)) and len(d) == 1:
            d = d[0]
        if not isinstance(d, int):
            raise Unsupported("logsumexp over several dims")
        with g.inserting_before(n):
            mx = g.call_function(torch.max, (x,), {"dim": d, "keepdim": True})
            m = g.call_function(operator.getitem, (mx, 0))
            e = g.call_function(torch.exp, (g.call_function(operator.sub, (x, m)),))
            sm = g.call_function(torch.sum, (e, d), {"keepdim": True})
            out = g.call_function(operator.add, (g.call_function(torch.log, (sm,)), m))
            if not keep:
                out = g.call_method("squeeze", (out, d))
        n.replace_all_uses_with(out)
        g.erase_node(n)
    g.lint()
    gm.recompile()


def rewrite_neg_inf(gm: fx.GraphModule) -> None:
    """Remove every `masked_fill(x, mask, -inf)` by folding it into its consumers.

    `-inf` is not an element of the ordered field the specs are stated over, so a
    tensor holding it cannot be a stage's output. It never has to be: in every
    graph where it appears it is a device for making the *next* operator ignore
    some entries, and what that operator makes of `-inf` is a finite value:

      relu(fill(x, m, -inf))    = where(m, 0, relu(x))
      exp(fill(x, m, -inf))     = where(m, 0, exp(x))
      softmax(fill(x, m, -inf)) = e / sum(e),  e = where(m, 0, exp(x - c))

    The softmax shift `c` cancels in exact arithmetic, so any value would do for
    the certificate; it is chosen for the floats, to be what PyTorch uses -- the
    maximum over the *unmasked* entries. That is `max(where(m, lo, x))` with `lo`
    the row minimum, which no unmasked entry is below. A row that is masked
    everywhere is `0/0`, as it is in PyTorch.

    These are identities over the reals extended by `-inf`, applied in the
    frontend -- the untrusted step, as every lowering rule is. Any other consumer
    of the filled tensor is refused.
    """
    g = gm.graph
    for n in list(g.nodes):
        if op_name(n.target) != "masked_fill" or n.op not in ("call_method",
                                                              "call_function"):
            continue
        val = n.kwargs.get("value", n.args[2] if len(n.args) > 2 else None)
        if not _is_neg_inf(val):
            continue
        x, m = n.args[0], n.kwargs.get("mask", n.args[1] if len(n.args) > 1 else None)
        for u in list(n.users):
            with g.inserting_before(u):
                d = _softmax_dim(u, gm)
                if d is not None:
                    lo = g.call_function(torch.min, (x,), {"dim": d, "keepdim": True})
                    lo0 = g.call_function(operator.getitem, (lo, 0))
                    xm = g.call_function(torch.where, (m, lo0, x))
                    c = g.call_function(torch.max, (xm,), {"dim": d, "keepdim": True})
                    c0 = g.call_function(operator.getitem, (c, 0))
                    sh = g.call_function(operator.sub, (x, c0))
                    ex = g.call_function(torch.exp, (sh,))
                    e = g.call_function(torch.where, (m, 0.0, ex))
                    s = g.call_function(torch.sum, (e, d), {"keepdim": True})
                    new = g.call_function(operator.truediv, (e, s))
                elif _is_relu(u, gm):
                    r = g.call_function(torch.relu, (x,))
                    new = g.call_function(torch.where, (m, 0.0, r))
                elif op_name(u.target) == "exp":
                    r = g.call_function(torch.exp, (x,))
                    new = g.call_function(torch.where, (m, 0.0, r))
                else:
                    raise Unsupported(
                        f"masked_fill with -inf feeds {op_name(u.target)!r}, whose "
                        "result on -inf is not a finite value this frontend knows")
            u.replace_all_uses_with(new)
            g.erase_node(u)
        g.erase_node(n)
    g.lint()
    gm.recompile()


#: In-place operators that change only a tensor's shape, never its values.
INPLACE_SHAPE = {"unsqueeze_": "unsqueeze", "squeeze_": "squeeze",
                 "transpose_": "transpose", "t_": "t"}
#: In-place operators that write values.
INPLACE_WRITE = {"__setitem__", "scatter_", "scatter_add_", "index_put_", "fill_",
                 "zero_", "masked_fill_", "index_fill_", "index_copy_"}


def rewrite_inplace(gm: fx.GraphModule) -> None:
    """Make in-place operators functional, or refuse them.

    A trace records `x.unsqueeze_(2)` as a node whose result nothing uses, while
    every *later* read of `x` sees the new shape -- an effect the dataflow graph does
    not show. A shape-only operator changes nothing but `x`'s own metadata (a view
    taken earlier keeps its own), so it becomes the functional operator, with every
    later use of `x` redirected to it.

    A value-writing operator is a different matter, since every alias of the
    storage sees the write. Only one case is accepted: a write into a lifted
    constant that nothing reads afterwards -- BigBird builds its `attention_probs`
    that way, and returns them only when asked to. A dead store is unobservable, so
    it is deleted. Any other write is refused.
    """
    g = gm.graph
    order = {n: i for i, n in enumerate(g.nodes)}
    for n in list(g.nodes):
        if n.op != "call_method":
            continue
        nm = n.target
        if nm in INPLACE_SHAPE:
            x = n.args[0]
            with g.inserting_after(n):
                f = g.call_method(INPLACE_SHAPE[nm], tuple(n.args), dict(n.kwargs))
            for u in list(x.users):
                if u is not n and u is not f and order.get(u, -1) > order[n]:
                    u.replace_input_with(x, f)
            g.erase_node(n)
        elif nm in INPLACE_WRITE:
            x = n.args[0]
            if n.users:
                raise Unsupported(f"the result of in-place {nm} is used")
            if x.op != "get_attr":
                raise Unsupported(f"in-place {nm} into a computed tensor")
            later = [m for m in g.nodes if order.get(m, -1) > order[n]
                     and m.op == "get_attr" and m.target == x.target
                     and any(order.get(u, -1) > order[n] and not (
                         u.op == "call_method" and u.target in INPLACE_WRITE)
                         for u in m.users)]
            if later or any(u is not n and order[u] > order[n] for u in x.users):
                raise Unsupported(f"in-place {nm} into a constant that is read later")
            g.erase_node(n)
    g.eliminate_dead_code()
    g.lint()
    gm.recompile()


def rewrite_copy_into_attr(gm: fx.GraphModule) -> List[Tuple[fx.Node, Tuple[int, ...]]]:
    """Make `self.state.copy_(src)` visible to the reads that follow it.

    The copy mutates module state, which `fx` records as a node whose result
    nothing uses: a later `self.state` is a fresh `get_attr` with no edge from the
    copy, so the graph would read the value from *before* it. Every such later read
    is redirected to `src`. A copy broadcasts, and a redirect does not, so each
    `src` is returned with the shape it must have; the caller checks it.
    """
    g = gm.graph
    checks: List[Tuple[fx.Node, Tuple[int, ...]]] = []
    order = {n: i for i, n in enumerate(g.nodes)}
    for n in list(g.nodes):
        if op_name(n.target) != "copy_" or n.op != "call_method":
            continue
        dst, src = n.args[0], n.args[1]
        if not (isinstance(dst, fx.Node) and dst.op == "get_attr"
                and isinstance(src, fx.Node)):
            raise Unsupported("copy_ into something other than module state")
        if n.users:
            raise Unsupported("the result of copy_ is used")
        checks.append((src, tuple(_fetch_attr(gm, dst.target).shape)))
        for m in list(g.nodes):
            if m.op == "get_attr" and m.target == dst.target and order[m] > order[n]:
                m.replace_all_uses_with(src)
        g.erase_node(n)
    g.eliminate_dead_code()
    gm.recompile()
    return checks


def prepare_graph(model: nn.Module, example_args: List[Any], mode):
    """Trace a model and apply every rewrite, returning the graph the chain compiler
    lowers and each node's shape. Separate so a diagnostic can run *this* graph on
    real tensors and compare it, node by node, with the kernel's buffers."""
    from .explicit import make_explicit, settle_runtime_switches
    settle_runtime_switches(model, example_args)
    make_explicit(model)
    gm = trace_model(model, example_args, mode)
    if any(op_name(n.target) == "scaled_dot_product_attention" for n in gm.graph.nodes):
        dt: Dict[fx.Node, Any] = {}
        with mode:
            sh = _node_shapes(gm, list(example_args), dt)
        rewrite_sdpa(gm, sh, dt)
    rewrite_logsumexp(gm)
    rewrite_neg_inf(gm)
    rewrite_softmax_matmul(gm)
    rewrite_inplace(gm)
    copies = rewrite_copy_into_attr(gm)
    # A value nothing reads (`out = self.fc(out[:, -1])` in a model that returns
    # the state instead) must emit no stage: the chain's result is its last one.
    gm.graph.eliminate_dead_code()
    gm.recompile()
    with mode:
        shapes = _node_shapes(gm, list(example_args))
    for src, want in copies:
        if shapes.get(src) != want:
            raise Unsupported(f"copy_ of {shapes.get(src)} into state of {want}")
    return gm, shapes


def compile_chain(model: nn.Module, example_args: List[Any], mode) -> Lowered:
    """Compile a whole graph into a chain of stages.

    Each non-pointwise node is lowered by the Level 1 frontend and *relocated* into
    the chain's buffer numbering, so a convolution here is the same `GenRed`, at the
    same theorem, as a convolution on its own. Runs of pointwise operators are folded
    into the producing stage's `post` rather than materialised, which keeps both the
    memory traffic and the number of locality obligations down.
    """
    gm, shapes = prepare_graph(model, example_args, mode)

    nodes = [n for n in gm.graph.nodes]
    uses: Dict[fx.Node, int] = {n: 0 for n in nodes}
    for n in nodes:
        for a in n.all_input_nodes:
            uses[a] += 1

    # --- pass 1: which parameters does each node need, and in what order
    for n in nodes:
        if n.op == "get_attr":
            # a parameter, a buffer, or a plain tensor attribute / lifted constant
            shapes[n] = tuple(_fetch_attr(gm, n.target).shape)
    subs: Dict[fx.Node, Any] = {}
    lowered: Dict[fx.Node, Lowered] = {}
    params: List[str] = []
    from .rnn import RNN_MODULES, rnn_param_names
    rnn_nodes: set = set()
    for n in nodes:
        if n.op == "get_attr":
            params.append(n.target)
            continue
        if n.op == "call_function" and n.target is fresh_randn:
            params.append(f"{RANDN_PREFIX}{n.name}:{','.join(map(str, n.args[0]))}")
            continue
        if n.op not in ("call_module", "call_function", "call_method"):
            continue
        if n.op == "call_module" and type(gm.get_submodule(n.target)) in RNN_MODULES:
            rnn_nodes.add(n)
            params += [f"{n.target}.{nm}"
                       for nm in rnn_param_names(gm.get_submodule(n.target))]
            continue
        if op_name(n.target) == "getitem" and n.args and n.args[0] in rnn_nodes:
            rnn_nodes.add(n)              # a result of a recurrent module
            continue
        if n.op == "call_module" and type(gm.get_submodule(n.target)) is nn.Embedding:
            params.append(f"{n.target}.weight")
            continue
        if n.op == "call_function" and op_name(n.target) == "embedding":
            continue                      # a gather, emitted directly
        if op_name(n.target) in ("gather", "index_select"):
            continue                      # likewise
        if n.op == "call_function" and n.target is softmax_matmul:
            continue                      # three stages, emitted directly
        if _is_pointwise(n, gm):
            continue
        if n.op in ("call_function", "call_method") and _alias_of(n, shapes) is not None:
            continue                      # a relabelling emits no stage
        if n not in shapes or op_name(n.target) == "tensor":
            continue                      # shape arithmetic or a literal, not data
        src0 = n.all_input_nodes[0] if n.all_input_nodes else None
        if _perm_of(n, len(shapes[src0]) if src0 in shapes else None) is not None:
            continue                      # an axis permutation is emitted directly
        if _cat_args(n, shapes) is not None:
            continue                      # a concatenation is emitted directly
        if _relabel_of(n, shapes) is not None:
            continue                      # an expand/unfold is emitted directly
        if op_name(n.target) in ("ones", "zeros", "full") and not n.all_input_nodes:
            continue                      # a constant, emitted directly
        if _split_parts(n, shapes) is not None:
            continue                      # a split names sub-ranges, it computes nothing
        if op_name(n.target) == "getitem" and len(n.args) > 1 \
                and isinstance(n.args[1], fx.Node):
            continue                      # an integer-tensor index: a gather
        if op_name(n.target) == "getitem" and len(n.args) > 1:
            # Selecting one part of a `split` is a slice of the split's *input*, not
            # an index into the part -- the recorded shape here is one part's.
            if _split_parts(src0, shapes) is not None:
                continue
            if src0 in shapes and \
                    _slice_plan(n.args[1], list(shapes[src0])) is not None:
                continue                  # a slice is emitted directly
        sub = gm.get_submodule(n.target) if n.op == "call_module" else n.target
        ins = [shapes[a] for a in n.all_input_nodes if a in shapes]
        try:
            low = _lower_one(sub, ins, mode, n)
        except Unsupported as e:
            raise Unsupported(f"node {n.name} ({op_name(n.target) or n.target}): {e}")
        subs[n], lowered[n] = sub, low
        for pp in low.param_paths:
            # the sub-lowering names parameters inside its wrapper; re-root them
            leaf = pp.split(".", 1)[1] if "." in pp else pp
            params.append(f"{n.target}.{leaf}" if n.op == "call_module" else leaf)

    ch = Chain()
    ph = 0
    env: Dict[fx.Node, Val] = {}
    produced_by: Dict[fx.Node, int] = {}      # value -> index of the stage that made it

    for n in nodes:
        if n.op == "placeholder":
            if ph >= len(example_args):
                # A forward argument with a default that the task does not pass --
                # `mask=None`, say. It still becomes a placeholder, and it is only
                # fine to drop because nothing reads it.
                if n.users:
                    raise Unsupported(
                        f"forward argument {n.name!r} has no value but is used")
                ph += 1
                continue
            v = example_args[ph]
            if not isinstance(v, torch.Tensor):
                raise Unsupported(f"placeholder {ph} is {type(v).__name__}")
            ch.arg_index.append(ph)
            env[n] = Val(len(ch.arg_index) - 1, tuple(v.shape))
            ph += 1
    for pp in params:
        ch.param_paths.append(pp)
    owned = set(dict(model.named_parameters())) | set(dict(model.named_buffers()))
    consts: Dict[str, Any] = {}
    for n in nodes:
        if n.op == "get_attr" and n.target not in owned:
            v = _fetch_attr(gm, n.target)
            from torch._subclasses.fake_tensor import FakeTensor
            if not isinstance(v, torch.Tensor) or isinstance(v, FakeTensor):
                raise Unsupported(f"constant {n.target} has no concrete value")
            consts[n.target] = v.detach().cpu().clone()
    low = _walk(ch, gm, nodes, env, shapes, uses, subs, lowered, produced_by, params)
    low.consts = consts
    return low


def _walk(ch: Chain, gm, nodes, env, shapes, uses, subs, lowered, produced_by,
          params) -> Lowered:
    """Second pass: emit the stages, with buffer numbering now fixed."""
    pnames = list(params)
    splits: Dict[fx.Node, Tuple[Val, int, List[int]]] = {}
    from .rnn import RNN_MODULES, RnnLowering
    rnns: Dict[fx.Node, Any] = {}          # module call -> its lowering
    rnn_state: Dict[fx.Node, Any] = {}     # `(h_n, c_n)` of an LSTM call

    for n in nodes:
        ch.cur_node = n.name
        if n.op == "placeholder":
            continue
        if n.op == "output":
            res = n.args[0]
            if not isinstance(res, fx.Node):
                raise Unsupported("output is not a single value")
            out = env[res]
            if out.buf < ch.arity:
                raise Unsupported("the graph returns an input unchanged")
            if out.buf != ch.nbuf - 1:
                raise Unsupported("the output is not the last stage's result")
            ch.finish_recurrences()
            ch.record_bounds()
            last = ch.stages[-1]
            return Lowered(
                family="chain", body=last.body, arity=ch.arity,
                out_size=out.numel, out_shape=out.shape,
                tensor_arg_index=list(ch.arg_index),
                param_paths=list(ch.param_paths),
                stages=list(ch.stages), sizes=list(ch.sizes),
                stage_nodes=list(ch.node_of), stage_src=list(ch.node_src),
                notes=ch.notes)
        if n.op == "call_function" and n.target is fresh_randn:
            # a fresh draw: an input buffer the runtime fills on every call
            nm = f"{RANDN_PREFIX}{n.name}:{','.join(map(str, n.args[0]))}"
            env[n] = Val(len(ch.arg_index) + pnames.index(nm), tuple(n.args[0]))
            continue
        if n.op == "get_attr":
            # `self.bias` as an `nn.Parameter` is data the kernel reads, no
            # different from an argument.
            env[n] = Val(len(ch.arg_index) + pnames.index(n.target), shapes[n])
            continue

        if n.op == "call_module" and type(gm.get_submodule(n.target)) is nn.Embedding:
            # A lookup is a gather: row `index[i]` of the table, as a masked sum.
            emb = gm.get_submodule(n.target)
            if emb.max_norm is not None:
                raise Unsupported("Embedding with max_norm renormalises its table")
            wb = len(ch.arg_index) + pnames.index(f"{n.target}.weight")
            env[n] = _emit_take(ch, Val(wb, tuple(emb.weight.shape)),
                                env[n.args[0]], shapes[n])
            produced_by[n] = len(ch.stages) - 1
            continue
        if n.op == "call_function" and n.target is softmax_matmul:
            env[n] = _emit_softmax_matmul(ch, env[n.args[0]], env[n.args[1]], shapes[n])
            produced_by[n] = len(ch.stages) - 1
            continue
        if op_name(n.target) == "index_select" and n.op in ("call_function",
                                                             "call_method"):
            x = n.kwargs.get("input", n.args[0])
            d = n.kwargs.get("dim", n.args[1] if len(n.args) > 1 else None)
            ix = n.kwargs.get("index", n.args[2] if len(n.args) > 2 else None)
            if not isinstance(d, int):
                raise Unsupported("index_select without a literal dim")
            env[n] = _emit_index_select(ch, env[x], d, env[ix], shapes[n])
            produced_by[n] = len(ch.stages) - 1
            continue
        if op_name(n.target) == "gather" and n.op in ("call_function", "call_method"):
            x = n.kwargs.get("input", n.args[0])
            d = n.kwargs.get("dim", n.args[1] if len(n.args) > 1 else None)
            ix = n.kwargs.get("index", n.args[2] if len(n.args) > 2 else None)
            if not isinstance(d, int) or n.kwargs.get("sparse_grad"):
                raise Unsupported("gather without a literal dim")
            env[n] = _emit_gather(ch, env[x], d, env[ix], shapes[n])
            produced_by[n] = len(ch.stages) - 1
            continue
        if n.op == "call_function" and op_name(n.target) == "embedding":
            idx = n.kwargs.get("input", n.args[0] if n.args else None)
            w = n.kwargs.get("weight", n.args[1] if len(n.args) > 1 else None)
            mx = n.kwargs.get("max_norm", n.args[3] if len(n.args) > 3 else None)
            if mx is not None:
                raise Unsupported("embedding with max_norm renormalises its table")
            env[n] = _emit_take(ch, env[w], env[idx], shapes[n])
            produced_by[n] = len(ch.stages) - 1
            continue
        if n.op == "call_module" and type(gm.get_submodule(n.target)) in RNN_MODULES:
            m = gm.get_submodule(n.target)
            x = n.args[0]
            hx = n.args[1] if len(n.args) > 1 else n.kwargs.get("hx")
            if isinstance(hx, (tuple, list)):
                h0, c0 = hx
            else:
                h0, c0 = hx, None
            def val(a):
                if a is None:
                    return None
                if not isinstance(a, fx.Node) or a not in env:
                    raise Unsupported(f"{n.target}: initial state is not a tensor value")
                return env[a]
            target = n.target
            lw = RnnLowering(
                ch, n, m, env[x], val(h0), val(c0),
                lambda nm, target=target: len(ch.arg_index) + pnames.index(f"{target}.{nm}"))
            lw.emit()
            rnns[n] = lw
            continue
        if op_name(n.target) == "getitem" and n.args and (
                n.args[0] in rnns or n.args[0] in rnn_state):
            src, idx = n.args[0], n.args[1]
            if src in rnns and idx == 0:
                st, shp = rnns[src].output()
            elif src in rnns and idx == 1 and rnns[src].lstm:
                rnn_state[n] = rnns[src]
                continue
            elif src in rnns and idx == 1:
                st, shp = rnns[src].final(0)
            elif src in rnn_state and idx in (0, 1):
                st, shp = rnn_state[src].final(idx)
            else:
                raise Unsupported(f"result {idx!r} of a recurrent module")
            env[n] = ch.emit(st, shp)
            produced_by[n] = len(ch.stages) - 1
            continue

        if n.op in ("call_function", "call_method") and n not in shapes:
            continue                      # shape arithmetic produces no buffer
        if op_name(n.target) == "tensor":
            continue                      # a literal constant, folded into the body
        # a pure relabelling reuses the buffer it was given
        if n.op in ("call_function", "call_method"):
            al = _alias_of(n, shapes)
            if al is not None and al in env and _relabel_of(n, shapes) is None:
                sh = shapes.get(n, env[al].shape)
                if _prod(sh) != env[al].numel:
                    raise Unsupported(f"{n.target} changes the element count")
                env[n] = Val(env[al].buf, sh)
                if al in produced_by:
                    produced_by[n] = produced_by[al]
                continue

        # A reordering of axes is a relabelling of the *index map*, not of the
        # buffer, so it is one stage rather than an alias. The IR deliberately
        # cannot express a reshape -- but it does not have to: a permutation is
        # absorbed into the index map of the stage that reads the result.
        perm = _perm_of(n, len(env[n.all_input_nodes[0]].shape)
                        if n.all_input_nodes and n.all_input_nodes[0] in env else None)
        if perm is not None:
            src = n.all_input_nodes[0]
            sv = list(env[src].shape)
            so = [sv[d] for d in perm]
            # out[i_0..i_r] = x[j_0..j_r] with j_{perm[d]} = i_d
            inv = [0] * len(perm)
            for d, pd in enumerate(perm):
                inv[pd] = d
            coords = unpack(I.Pid(), so)
            st = Lowered(
                family="genred", body=S.Inp(env[src].buf), arity=ch.nbuf + 1,
                out_size=_prod(so), out_shape=tuple(so),
                tensor_arg_index=list(ch.arg_index), K=1,
                offs=ch.pad({env[src].buf: pack([coords[inv[k]]
                                                 for k in range(len(sv))], sv)}),
                post_offs=ch.pad({}), post=S.Inp(0),
                notes=[f"permute {tuple(sv)} -> {tuple(so)} by {tuple(perm)}"])
            env[n] = ch.emit(st, tuple(so))
            produced_by[n] = len(ch.stages) - 1
            continue

        # A `split` computes nothing: it names sub-ranges of its input. Recorded
        # here, and each `getitem` that selects one becomes a slice.
        sp = _split_parts(n, shapes)
        if sp is not None and n.all_input_nodes and n.all_input_nodes[0] in env:
            splits[n] = (env[n.all_input_nodes[0]], sp[0], sp[1])
            continue
        if op_name(n.target) == "getitem" and len(n.args) > 1:
            src, idx = n.args[0], n.args[1]
            if isinstance(idx, fx.Node) and src in env and idx in env:
                env[n] = _emit_take(ch, env[src], env[idx], shapes[n])
                produced_by[n] = len(ch.stages) - 1
                continue
            if src in splits and isinstance(idx, int):
                v, dim, sizes = splits[src]
                start = sum(sizes[:idx])
                plan = [(start, 1, sizes[idx]) if d == dim else (0, 1, sz)
                        for d, sz in enumerate(v.shape)]
                env[n] = _emit_slice(ch, v, plan,
                                     f"split part {idx} of {len(sizes)} along dim {dim}")
                produced_by[n] = len(ch.stages) - 1
                continue
            if src in env and isinstance(idx, (tuple, slice, int)) \
                    and not isinstance(idx, bool):
                plan = _slice_plan(idx, list(env[src].shape))
                if plan is not None and _alias_of(n, shapes) is None:
                    env[n] = _emit_slice(ch, env[src], plan,
                                         f"slice {idx!r} of {tuple(env[src].shape)}")
                    produced_by[n] = len(ch.stages) - 1
                    continue

        if n.op == "call_function" and op_name(n.target) in ("ones", "zeros", "full") \
                and not n.all_input_nodes and n in shapes:
            # A tensor the forward builds from its shape alone: one constant stage.
            if op_name(n.target) == "full":
                c = n.args[1] if len(n.args) > 1 else n.kwargs.get("fill_value")
                if not isinstance(c, (int, float)) or not math.isfinite(c):
                    raise Unsupported(f"full with {c!r}")
            else:
                c = 1 if op_name(n.target) == "ones" else 0
            so = shapes[n]
            st = Lowered(family="genred", body=S.lit(c), arity=ch.nbuf + 1,
                         out_size=_prod(so), out_shape=tuple(so),
                         tensor_arg_index=list(ch.arg_index), K=1,
                         offs=ch.pad({}), post_offs=ch.pad({}), post=S.Inp(0),
                         notes=[f"constant {c} of shape {tuple(so)}"])
            env[n] = ch.emit(st, tuple(so))
            produced_by[n] = len(ch.stages) - 1
            continue

        rl = _relabel_of(n, shapes)
        if rl is not None and n.all_input_nodes[0] in env:
            env[n] = _emit_relabel(ch, n, env[n.all_input_nodes[0]], shapes[n], *rl)
            produced_by[n] = len(ch.stages) - 1
            continue

        ca = _cat_args(n, shapes)
        if ca is not None and all(a in env for a in ca[0]):
            env[n] = _emit_cat(ch, n, env, shapes, ca[0], ca[1])
            produced_by[n] = len(ch.stages) - 1
            continue

        ins = [env[a] for a in n.all_input_nodes if a in env]
        if _is_pointwise(n, gm):
            if not ins and _is_const(n, gm):
                continue                  # a constant, folded into its consumers
            # fold into the producing stage when this is its only consumer
            src = n.all_input_nodes[0] if n.all_input_nodes else None
            fuse = (src is not None and src in produced_by and uses[src] == 1
                    and produced_by[src] == len(ch.stages) - 1
                    and shapes.get(n) == env[src].shape
                    and len(ins) == 1 and ins[0].buf == env[src].buf)

            def conv_fused(a, src=src):
                if a is src:
                    return S.Inp(0)
                return S.Inp(env[a].buf) if a in env else _const_of(a, gm)

            def conv_plain(a):
                return S.Inp(env[a].buf) if a in env else _const_of(a, gm)
            se_args = [conv_fused(a) if isinstance(a, fx.Node) else a for a in n.args]
            if fuse:
                # Compose with the stage's existing `post`, do not replace it: that
                # `post` may already add a bias, and slot 0 there is the reduced
                # value, not this operator's input.
                prev = ch.stages[-1]
                prev.post = _subst_slot0(_pointwise_se(n, gm, se_args, conv_fused),
                                         prev.post)
                env[n] = env[src]
                produced_by[n] = produced_by[src]
                # the stage now holds *this* node's value, not the one it was
                # emitted for -- which is what a bisection against the graph has to
                # compare against
                if ch.node_of:
                    ch.node_of[-1] = n.name
                ch.notes.append(f"fused {n.target} into stage {produced_by[src]}")
                continue
            # otherwise materialise it as a K = 1 stage. Inputs need not share the
            # output's shape: broadcasting is a per-input index map that pins the
            # axes of extent one, which is what it means.
            so = shapes.get(n)
            if not ins or so is None:
                raise Unsupported(f"pointwise {n.target} with no tensor input")
            coords = unpack(I.Pid(), list(so))
            offs: Dict[int, I.IE] = {}
            for v in ins:
                sv = v.shape
                if len(sv) > len(so):
                    raise Unsupported(f"{n.target}: input rank exceeds output rank")
                for a_, b_ in zip(reversed(sv), reversed(so)):
                    if a_ not in (1, b_):
                        raise Unsupported(f"{n.target}: {sv} does not broadcast to {so}")
                if not sv:
                    offs[v.buf] = I.Lit(0)
                else:
                    tail = coords[len(so) - len(sv):]
                    sel = [I.Lit(0) if d == 1 else cc for cc, d in zip(tail, sv)]
                    offs[v.buf] = pack(sel, list(sv))
            body = _pointwise_se(n, gm, [
                conv_plain(a) if isinstance(a, fx.Node) else a for a in n.args],
                conv_plain)
            st = identity_stage(ch, ins[0], body, so, f"pointwise {n.target}",
                                extra_offs=offs)
            env[n] = ch.emit(st, shapes[n])
            produced_by[n] = len(ch.stages) - 1
            continue

        # a non-pointwise operator: reuse its Level 1 lowering, relocated
        low = lowered[n]
        # the operator's own inputs and parameters, in its numbering
        bmap: Dict[int, int] = {}
        for j, a in enumerate(n.all_input_nodes):
            bmap[j] = env[a].buf
        k = len(n.all_input_nodes)
        for pp in low.param_paths:
            leaf = pp.split(".", 1)[1] if "." in pp else pp
            full = f"{n.target}.{leaf}" if n.op == "call_module" else leaf
            bmap[k] = len(ch.arg_index) + pnames.index(full)
            k += 1

        if low.family in ("genred", "maxred", "prodred"):
            st = relocate(low, bmap, ch.nbuf + 1, NO_IDX_SLOT)
            st.family = low.family
            env[n] = ch.emit(st, shapes[n])
            produced_by[n] = len(ch.stages) - 1
            continue

        if low.family in ("pipeline", "pipeline3", "pipeline_max"):
            # A multi-stage operator contributes several stages. Its own
            # intermediates are numbered just above its inputs; each gets a fresh
            # chain buffer, allocated in order so that a later sub-stage can read an
            # earlier one exactly as it did standalone.
            sizes = ([low.n1] if low.family in ("pipeline", "pipeline_max")
                     else [low.n1, low.n2])
            base = k
            # Which chain buffer each of this operator's own sub-stages ended up
            # in. Not `nbuf - (j - i)`: a sub-stage may be emitted as more than one
            # chain stage (a long, narrow reduction is split), so the buffer a
            # later sub-stage must read is the one `emit` actually returned.
            made: List[int] = []
            for j, sub in enumerate(low.stages):
                nbuf = ch.nbuf + 1
                bm = dict(bmap)
                for i, b in enumerate(made):
                    bm[base + i] = b
                stg = relocate(sub, bm, nbuf, NO_IDX_SLOT)
                stg.family = sub.family
                shape = shapes[n] if j == len(low.stages) - 1 else (sizes[j],)
                made.append(ch.emit(stg, shape).buf)
            env[n] = Val(made[-1], shapes[n])
            produced_by[n] = len(ch.stages) - 1
            continue

        raise Unsupported(f"{n.target}: family {low.family} not chainable")

    raise Unsupported("graph has no output node")
