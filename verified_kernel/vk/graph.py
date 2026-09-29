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


@dataclass
class Chain:
    """A compilation in progress."""
    # inputs and parameters, in buffer order
    arg_index: List[int] = field(default_factory=list)
    param_paths: List[str] = field(default_factory=list)
    stages: List[Lowered] = field(default_factory=list)
    sizes: List[int] = field(default_factory=list)
    notes: List[str] = field(default_factory=list)

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
        buf = self.arity + len(self.stages)
        st.out_shape = tuple(shape)
        st.out_size = _prod(shape)
        self.stages.append(st)
        self.sizes.append(st.out_size)
        return Val(buf, tuple(shape))

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


def compile_chain(model: nn.Module, example_args: List[Any], mode) -> Lowered:
    """Compile a whole graph into a chain of stages.

    Each non-pointwise node is lowered by the Level 1 frontend and *relocated* into
    the chain's buffer numbering, so a convolution here is the same `GenRed`, at the
    same theorem, as a convolution on its own. Runs of pointwise operators are folded
    into the producing stage's `post` rather than materialised, which keeps both the
    memory traffic and the number of locality obligations down.
    """
    gm = fx.symbolic_trace(model)
    gm.graph.lint()
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
        if op_name(n.target) == "getattr" and len(n.args) > 1 and n.args[1] == "T":
            continue                      # a transpose is emitted directly
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

    for n in nodes:
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
            last = ch.stages[-1]
            return Lowered(
                family="chain", body=last.body, arity=ch.arity,
                out_size=out.numel, out_shape=out.shape,
                tensor_arg_index=list(ch.arg_index),
                param_paths=list(ch.param_paths),
                stages=list(ch.stages), sizes=list(ch.sizes),
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

        # `x.T` is a relabelling of the *index map*, not of the buffer, so it is one
        # stage rather than an alias.
        if op_name(n.target) == "getattr" and len(n.args) > 1 and n.args[1] == "T":
            src = n.args[0]
            sv = env[src].shape
            if len(sv) != 2:
                raise Unsupported(f".T on a {len(sv)}-D tensor")
            a_, b_ = sv
            q = I.Pid()
            st = Lowered(
                family="genred", body=S.Inp(env[src].buf), arity=ch.nbuf + 1,
                out_size=a_ * b_, out_shape=(b_, a_),
                tensor_arg_index=list(ch.arg_index), K=1,
                offs=ch.pad({env[src].buf: (q % I.Lit(a_)) * I.Lit(b_)
                             + q // I.Lit(a_)}),
                post_offs=ch.pad({}), post=S.Inp(0),
                notes=[f"transpose {sv} -> {(b_, a_)}"])
            env[n] = ch.emit(st, (b_, a_))
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
                prev = ch.stages[-1]
                prev.post = _remap_se(_pointwise_se(n, gm, se_args),
                                      lambda b: 0 if b == 0 else b)
                prev.post = S.Bin("mul", prev.post, S.lit(1)) if False else prev.post
                env[n] = env[src]
                produced_by[n] = produced_by[src]
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
            for j, sub in enumerate(low.stages):
                nbuf = ch.nbuf + 1
                for i in range(len(low.stages) - 1):
                    if base + i in bmap:
                        continue
                bm = dict(bmap)
                for i in range(j):
                    bm[base + i] = ch.arity + len(ch.stages) - (j - i)
                stg = relocate(sub, bm, nbuf, NO_IDX_SLOT)
                stg.family = sub.family
                shape = shapes[n] if j == len(low.stages) - 1 else (sizes[j],)
                ch.emit(stg, shape)
            env[n] = Val(ch.nbuf - 1, shapes[n])
            produced_by[n] = len(ch.stages) - 1
            continue

        raise Unsupported(f"{n.target}: family {low.family} not chainable")

    raise Unsupported("graph has no output node")
