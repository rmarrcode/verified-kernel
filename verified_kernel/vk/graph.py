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

from dataclasses import dataclass, field
from fractions import Fraction
from typing import Any, Dict, List, Optional, Tuple

import torch
import torch.fx as fx
import torch.nn as nn

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
            bounds: Dict[str, Tuple] = {}
            for b in range(self.arity, self.arity + len(self.stages)):
                size = self.sizes[b - self.arity]
                shp = self.shapes[b - self.arity]
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

    def pad(self, entries: Dict[int, I.IE], extra: int = 1) -> List[I.IE]:
        """Index maps for every buffer a stage may see: all inputs, every earlier
        intermediate, and the one it is about to write."""
        n = self.nbuf + extra
        return [entries.get(b, I.Lit(0)) for b in range(n)]


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
            coords.append(I.Lit(0))         # trailing coordinate folded away
            cur = cur.a
        else:
            return None
    coords.append(cur)
    return list(reversed(coords))


def _is_clamp(c: I.IE, d: int) -> bool:
    """`a - (a - (d-1))` is `min a (d-1)`, hence below `d`."""
    return (isinstance(c, I.Sub) and isinstance(c.b, I.Sub)
            and c.b.a == c.a and _lit(c.b.b) == d - 1)


def coord_bound(c: I.IE, d: int, nout: int) -> Optional[Tuple]:
    """How to prove one coordinate is below its axis extent."""
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
    for b, e in enumerate(st.offs):
        if b == st.idx_slot:
            continue
        if b in bmap:
            offs[bmap[b]] = e
    for b, e in enumerate(st.post_offs):
        if b in bmap:
            post_offs[bmap[b]] = e

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


def _wrap(fn, n: int) -> nn.Module:
    return {1: _Wrap1, 2: _Wrap2, 3: _Wrap3}[n](fn)


# ---------------------------------------------------------------------------
# The walker
# ---------------------------------------------------------------------------

def _node_shapes(gm: fx.GraphModule, args: List[Any]) -> Dict[fx.Node, Tuple[int, ...]]:
    """Every node's output shape, by interpreting the graph on fake tensors."""
    shapes: Dict[fx.Node, Tuple[int, ...]] = {}

    class Rec(fx.Interpreter):
        def run_node(self, n):
            out = super().run_node(n)
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
             "squeeze", "unsqueeze", "to", "float", "type_as", "expand_as"}


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
        if idx == 0:
            return src
        return None
    if nm == "getattr" and len(node.args) > 1 and node.args[1] == "values":
        # `torch.max(x, dim)` returns a named tuple; `.values` is the values
        return src
    return None


def _const_of(node: fx.Node):
    """The literal a constant-tensor node denotes."""
    if op_name(node.target) == "tensor" and node.args and isinstance(
            node.args[0], (int, float)):
        return S.lit(node.args[0])
    raise Unsupported(f"{node.target} is not a constant")


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
    """Resolve a subscript into, per input axis, `(start, step, extent_or_None)`.

    `None` as the extent means the axis is indexed by a plain integer and so does not
    appear in the output at all. Returns `None` for anything not handled -- a boolean
    mask, a tensor index, `None`/newaxis -- rather than guessing.
    """
    items = list(idx) if isinstance(idx, tuple) else [idx]
    if any(it is Ellipsis for it in items):
        n_given = sum(1 for it in items if it is not Ellipsis)
        pos = next(i for i, it in enumerate(items) if it is Ellipsis)
        items[pos:pos + 1] = [slice(None)] * (len(in_shape) - n_given)
    if len(items) > len(in_shape):
        return None
    items += [slice(None)] * (len(in_shape) - len(items))
    plan = []
    for it, n in zip(items, in_shape):
        if isinstance(it, int):
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
        if ext is None:
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
    if op_name(n.target) != "cat":
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


def _pointwise_se(node: fx.Node, gm: fx.GraphModule, args: List[Any]) -> S.SE:
    from .frontend import POINTWISE_FUNCS, POINTWISE_MODULES
    if node.op == "call_module":
        sub = gm.get_submodule(node.target)
        return POINTWISE_MODULES[type(sub)](sub, args)
    return table_get(POINTWISE_FUNCS, node.target)(args, node)


def _bind(node: fx.Node, target) -> Any:
    """A callable taking just this node's tensor inputs, with its other arguments
    (a `dim`, a `p`, a scalar) already supplied.

    Re-lowering a node on its own means calling it outside the graph, where those
    arguments are no longer implicit in the call site.
    """
    positions = [i for i, a in enumerate(node.args) if isinstance(a, fx.Node)]
    base = list(node.args)
    kw = dict(node.kwargs)

    is_method = isinstance(target, str)

    def fn(*tensors):
        args = list(base)
        for t, pos in zip(tensors, positions):
            args[pos] = t
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


def trace_model(model: nn.Module, example_args: List[Any], mode) -> fx.GraphModule:
    """Trace, falling back to a shape-aware trace for models that compute with
    their own shapes."""
    try:
        gm = fx.symbolic_trace(model)
        gm.graph.lint()
        return gm
    except Exception as first:
        tracer = ShapeTracer(mode)
        with mode:
            tracer._args = [torch.empty(tuple(a.shape), dtype=a.dtype)
                            if isinstance(a, torch.Tensor) else a
                            for a in example_args]
        try:
            graph = tracer.trace(model)
        except Exception:
            raise first
        gm = fx.GraphModule(tracer.root, graph)
        gm.graph.lint()
        return gm


def compile_chain(model: nn.Module, example_args: List[Any], mode) -> Lowered:
    """Compile a whole graph into a chain of stages.

    Each non-pointwise node is lowered by the Level 1 frontend and *relocated* into
    the chain's buffer numbering, so a convolution here is the same `GenRed`, at the
    same theorem, as a convolution on its own. Runs of pointwise operators are folded
    into the producing stage's `post` rather than materialised, which keeps both the
    memory traffic and the number of locality obligations down.
    """
    gm = trace_model(model, example_args, mode)
    with mode:
        shapes = _node_shapes(gm, list(example_args))

    nodes = [n for n in gm.graph.nodes]
    uses: Dict[fx.Node, int] = {n: 0 for n in nodes}
    for n in nodes:
        for a in n.all_input_nodes:
            uses[a] += 1

    # --- pass 1: which parameters does each node need, and in what order
    for n in nodes:
        if n.op == "get_attr":
            shapes[n] = tuple(dict(gm.named_parameters()).get(
                n.target, dict(gm.named_buffers()).get(n.target)).shape)
    subs: Dict[fx.Node, Any] = {}
    lowered: Dict[fx.Node, Lowered] = {}
    params: List[str] = []
    for n in nodes:
        if n.op == "get_attr":
            params.append(n.target)
            continue
        if n.op not in ("call_module", "call_function", "call_method"):
            continue
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
        if _split_parts(n, shapes) is not None:
            continue                      # a split names sub-ranges, it computes nothing
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
        low = _lower_one(sub, ins, mode, n)
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
            v = example_args[ph]
            if not isinstance(v, torch.Tensor):
                raise Unsupported(f"placeholder {ph} is {type(v).__name__}")
            ch.arg_index.append(ph)
            env[n] = Val(len(ch.arg_index) - 1, tuple(v.shape))
            ph += 1
    for pp in params:
        ch.param_paths.append(pp)
    return _walk(ch, gm, nodes, env, shapes, uses, subs, lowered, produced_by, params)


def _walk(ch: Chain, gm, nodes, env, shapes, uses, subs, lowered, produced_by,
          params) -> Lowered:
    """Second pass: emit the stages, with buffer numbering now fixed."""
    pnames = list(params)
    splits: Dict[fx.Node, Tuple[Val, int, List[int]]] = {}

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
        if n.op == "get_attr":
            # `self.bias` as an `nn.Parameter` is data the kernel reads, no
            # different from an argument.
            env[n] = Val(len(ch.arg_index) + pnames.index(n.target), shapes[n])
            continue

        if n.op in ("call_function", "call_method") and n not in shapes:
            continue                      # shape arithmetic produces no buffer
        if op_name(n.target) == "tensor":
            continue                      # a literal constant, folded into the body
        # a pure relabelling reuses the buffer it was given
        if n.op in ("call_function", "call_method"):
            al = _alias_of(n, shapes)
            if al is not None and al in env:
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

        ca = _cat_args(n, shapes)
        if ca is not None and all(a in env for a in ca[0]):
            env[n] = _emit_cat(ch, n, env, shapes, ca[0], ca[1])
            produced_by[n] = len(ch.stages) - 1
            continue

        ins = [env[a] for a in n.all_input_nodes if a in env]
        if _is_pointwise(n, gm):
            # fold into the producing stage when this is its only consumer
            src = n.all_input_nodes[0] if n.all_input_nodes else None
            fuse = (src is not None and src in produced_by and uses[src] == 1
                    and produced_by[src] == len(ch.stages) - 1
                    and shapes.get(n) == env[src].shape
                    and len(ins) == 1 and ins[0].buf == env[src].buf)
            se_args = [S.Inp(0) if (isinstance(a, fx.Node) and a is src)
                       else (S.Inp(env[a].buf) if isinstance(a, fx.Node) and a in env
                             else (_const_of(a) if isinstance(a, fx.Node) else a))
                       for a in n.args]
            if fuse:
                # Compose with the stage's existing `post`, do not replace it: that
                # `post` may already add a bias, and slot 0 there is the reduced
                # value, not this operator's input.
                prev = ch.stages[-1]
                prev.post = _subst_slot0(_pointwise_se(n, gm, se_args), prev.post)
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
                (S.Inp(env[a].buf) if a in env else _const_of(a))
                if isinstance(a, fx.Node) else a for a in n.args])
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
