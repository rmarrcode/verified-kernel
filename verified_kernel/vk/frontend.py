"""PyTorch module -> formal specification.

This is the framework's own step, and the one place in the pipeline with no proof
behind it: there is no formal semantics of PyTorch on the other side to prove it
against. It is therefore written to fail loudly. Every operator must be in the
table below, every shape assumption is asserted, and anything unrecognised
returns `None` with a reason rather than guessing. A frontend that silently
mis-lowers would produce a kernel that is provably equal to the *wrong* spec,
which is the one failure mode this design cannot rule out by proof -- so it is
ruled out by refusing to lower what it does not understand.
"""

from __future__ import annotations

import math
import operator
from dataclasses import dataclass, field
from fractions import Fraction
from typing import Any, Callable, Dict, List, Optional, Tuple

import torch
import torch.fx as fx
import torch.nn as nn
import torch.nn.functional as F

from . import ie as I
from . import se as S


@dataclass
class Lowered:
    """A successfully lowered task."""
    family: str
    body: S.SE
    arity: int                  # number of *tensor* inputs
    out_size: int               # flat element count of the output
    out_shape: Tuple[int, ...]
    tensor_arg_index: List[int] = field(default_factory=list)
    notes: List[str] = field(default_factory=list)
    # Module parameters/buffers promoted to input buffers, in buffer order after
    # the forward arguments. Convolution needs this: its weights are state, not
    # arguments, but to the kernel they are just more memory to read.
    param_paths: List[str] = field(default_factory=list)
    # `pipeline` family only: the two stages, and the intermediate buffer's size
    stages: List["Lowered"] = field(default_factory=list)
    n1: int = 0
    outer: int = 1
    inner: int = 1
    # `genred` family: out[q] = guard(q) * post(sum_{k<K} range(q,k) * body(ins at offs(q,k)))
    K: int = 0
    offs: List[I.IE] = field(default_factory=list)
    post_offs: List[I.IE] = field(default_factory=list)
    in_range: I.BE = field(default_factory=I.TT)
    out_guard: I.BE = field(default_factory=I.TT)
    post: Optional[S.SE] = None


class Unsupported(Exception):
    """Raised when the frontend does not understand something. Never swallowed
    into a guess."""


# ---------------------------------------------------------------------------
# Pointwise operator table
# ---------------------------------------------------------------------------

def _kw(node: fx.Node, name: str, pos: int, default):
    if name in node.kwargs:
        return node.kwargs[name]
    if len(node.args) > pos:
        return node.args[pos]
    return default


def _pointwise_functions() -> Dict[Any, Callable]:
    """Maps an fx call target to a builder taking (args, node) -> SE."""
    T: Dict[Any, Callable] = {}

    def reg(keys, fn):
        for k in keys:
            T[k] = fn

    reg([torch.relu, F.relu, torch.relu_, F.relu_, "relu"],
        lambda a, n: S.relu(a[0]))
    reg([torch.sigmoid, F.sigmoid, "sigmoid"],
        lambda a, n: S.sigmoid(a[0]))
    reg([torch.tanh, F.tanh, "tanh"],
        lambda a, n: S.tanh(a[0]))
    reg([F.silu], lambda a, n: S.silu(a[0]))
    reg([F.softplus],
        lambda a, n: S.softplus(a[0]))
    reg([F.softsign], lambda a, n: S.softsign(a[0]))
    reg([F.hardsigmoid], lambda a, n: S.hardsigmoid(a[0]))
    reg([F.selu, torch.selu], lambda a, n: S.selu(a[0]))
    reg([F.elu], lambda a, n: S.elu(a[0], _kw(n, "alpha", 1, 1.0)))
    reg([F.leaky_relu],
        lambda a, n: S.leaky_relu(a[0], _kw(n, "negative_slope", 1, 0.01)))
    reg([F.hardtanh],
        lambda a, n: S.hardtanh(a[0], _kw(n, "min_val", 1, -1.0),
                                _kw(n, "max_val", 2, 1.0)))

    def _gelu(a, n):
        approx = _kw(n, "approximate", 1, "none")
        return S.gelu_tanh(a[0]) if approx == "tanh" else S.gelu_exact(a[0])
    reg([F.gelu], _gelu)

    reg([torch.exp, "exp"], lambda a, n: S.exp(a[0]))
    reg([torch.log, "log"], lambda a, n: S.log(a[0]))
    reg([torch.sqrt, "sqrt"], lambda a, n: S.sqrt(a[0]))
    reg([torch.abs, abs, "abs"], lambda a, n: S.absv(a[0]))
    reg([torch.erf, "erf"], lambda a, n: S.erf(a[0]))
    reg([torch.neg, operator.neg, "neg"], lambda a, n: -S.lift(a[0]))

    reg([operator.add, torch.add, "add"], lambda a, n: S.lift(a[0]) + S.lift(a[1]))
    reg([operator.sub, torch.sub, "sub"], lambda a, n: S.lift(a[0]) - S.lift(a[1]))
    reg([operator.mul, torch.mul, "mul"], lambda a, n: S.lift(a[0]) * S.lift(a[1]))
    reg([operator.truediv, torch.div, "div", "divide"],
        lambda a, n: S.lift(a[0]) / S.lift(a[1]))

    def _binmax(a, n):
        # `torch.max(x, dim=d)` is a reduction, not a pointwise op; only the
        # two-operand form belongs here.
        if len(a) != 2 or "dim" in n.kwargs:
            raise Unsupported("torch.max/min with a dim is a reduction")
        return S.maxv(a[0], a[1])

    def _binmin(a, n):
        if len(a) != 2 or "dim" in n.kwargs:
            raise Unsupported("torch.max/min with a dim is a reduction")
        return S.minv(a[0], a[1])
    reg([torch.maximum, torch.max], _binmax)
    reg([torch.minimum, torch.min], _binmin)

    def _clamp(a, n):
        lo = _kw(n, "min", 1, None)
        hi = _kw(n, "max", 2, None)
        out = S.lift(a[0])
        if lo is not None:
            out = S.maxv(out, lo)
        if hi is not None:
            out = S.minv(out, hi)
        return out
    reg([torch.clamp, "clamp", torch.clip, "clip"], _clamp)

    def _pow(a, n):
        e = a[1]
        if isinstance(e, float) and e.is_integer():
            e = int(e)
        if not isinstance(e, int):
            raise Unsupported(f"non-integer exponent {e!r}")
        return S.powi(a[0], e)
    reg([torch.pow, operator.pow, "pow"], _pow)

    return T


POINTWISE_FUNCS = _pointwise_functions()

# nn.Module classes that are pointwise, mapped to the same builders.
POINTWISE_MODULES: Dict[type, Callable] = {
    nn.ReLU: lambda m, a: S.relu(a[0]),
    nn.Sigmoid: lambda m, a: S.sigmoid(a[0]),
    nn.Tanh: lambda m, a: S.tanh(a[0]),
    nn.SiLU: lambda m, a: S.silu(a[0]),
    nn.Softplus: lambda m, a: S.softplus(a[0]),
    nn.Softsign: lambda m, a: S.softsign(a[0]),
    nn.Hardsigmoid: lambda m, a: S.hardsigmoid(a[0]),
    nn.SELU: lambda m, a: S.selu(a[0]),
    nn.ELU: lambda m, a: S.elu(a[0], m.alpha),
    nn.LeakyReLU: lambda m, a: S.leaky_relu(a[0], m.negative_slope),
    nn.Hardtanh: lambda m, a: S.hardtanh(a[0], m.min_val, m.max_val),
    nn.GELU: lambda m, a: (S.gelu_tanh(a[0]) if getattr(m, "approximate", "none") == "tanh"
                           else S.gelu_exact(a[0])),
}


# ---------------------------------------------------------------------------
# Lowering
# ---------------------------------------------------------------------------

def _shapes(gm: fx.GraphModule, args: List[Any]) -> Dict[str, Any]:
    """Annotate every node with the value it produces, by interpretation."""
    from torch.fx.passes.shape_prop import ShapeProp
    ShapeProp(gm).propagate(*args)
    return {n.name: n.meta.get("tensor_meta", None) for n in gm.graph.nodes}


def lower_pointwise(model: nn.Module, example_args: List[Any]) -> Lowered:
    """Lower a module whose output element depends only on the input elements at
    the same flat index.

    Every tensor input must have exactly the output's shape: broadcasting is a
    different family (the index map is no longer the identity) and is refused
    here rather than approximated.
    """
    gm = fx.symbolic_trace(model)
    gm.graph.lint()

    with torch.no_grad():
        out_val = model(*example_args)
    if not isinstance(out_val, torch.Tensor):
        raise Unsupported(f"output is {type(out_val).__name__}, not a Tensor")
    out_shape = tuple(out_val.shape)

    tensor_idx: List[int] = []
    env: Dict[fx.Node, Any] = {}
    ph = 0
    notes: List[str] = []

    for node in gm.graph.nodes:
        if node.op == "placeholder":
            v = example_args[ph]
            if isinstance(v, torch.Tensor):
                if tuple(v.shape) != out_shape:
                    raise Unsupported(
                        f"input {ph} has shape {tuple(v.shape)} != output {out_shape}"
                        " (broadcasting is a separate family)")
                env[node] = S.Inp(len(tensor_idx))
                tensor_idx.append(ph)
            elif isinstance(v, (int, float, Fraction)):
                env[node] = S.lit(v)
                notes.append(f"input {ph} is the scalar {v!r}, lowered as a literal")
            else:
                raise Unsupported(f"placeholder {ph} is {type(v).__name__}")
            ph += 1

        elif node.op in ("call_function", "call_method"):
            key = node.target
            if key not in POINTWISE_FUNCS:
                raise Unsupported(f"{node.op} {key!r} is not a pointwise operator")
            args = [env[a] if isinstance(a, fx.Node) else a for a in node.args]
            env[node] = POINTWISE_FUNCS[key](args, node)

        elif node.op == "call_module":
            sub = gm.get_submodule(node.target)
            cls = type(sub)
            if cls not in POINTWISE_MODULES:
                raise Unsupported(f"module {cls.__name__} is not a pointwise operator")
            args = [env[a] if isinstance(a, fx.Node) else a for a in node.args]
            env[node] = POINTWISE_MODULES[cls](sub, args)

        elif node.op == "get_attr":
            raise Unsupported("module has parameters/buffers (not pointwise)")

        elif node.op == "output":
            res = node.args[0]
            if not isinstance(res, fx.Node):
                raise Unsupported("output is not a single value")
            body = env[res]
            return Lowered(
                family="pointwise", body=body, arity=len(tensor_idx),
                out_size=out_val.numel(), out_shape=out_shape,
                tensor_arg_index=tensor_idx, notes=notes)
        else:
            raise Unsupported(f"unhandled fx op {node.op}")

    raise Unsupported("graph has no output node")


# ---------------------------------------------------------------------------
# The reduction family
# ---------------------------------------------------------------------------

def huber_elementwise(p, t, beta: float = 1.0) -> S.SE:
    """PyTorch's `smooth_l1_loss` summand: quadratic near zero, linear outside."""
    d = S.absv(S.lift(p) - S.lift(t))
    quad = S.lit(0.5) * d * d / S.lit(beta)
    lin = d - S.lit(0.5 * beta)
    return S.SelLe(d, S.lit(beta), quad, lin)


@dataclass
class RedNode:
    """A recognised reduction: a pointwise summand, an axis, and a divisor."""
    body: S.SE
    dim: Optional[int]          # None means "over every element"
    divide_by: str              # "none" | "K" | "outer"


def _reduce_functions() -> Dict[Any, Callable]:
    T: Dict[Any, Callable] = {}

    def dim_of(node: fx.Node):
        return _kw(node, "dim", 1, None)

    T[torch.sum] = lambda a, n: RedNode(S.lift(a[0]), dim_of(n), "none")
    T["sum"] = T[torch.sum]
    T[torch.mean] = lambda a, n: RedNode(S.lift(a[0]), dim_of(n), "K")
    T["mean"] = T[torch.mean]

    def _mse(a, n):
        d = S.lift(a[0]) - S.lift(a[1])
        return RedNode(d * d, None, "K")
    T[F.mse_loss] = _mse

    def _huber(a, n):
        beta = _kw(n, "beta", 4, 1.0)
        return RedNode(huber_elementwise(a[0], a[1], beta), None, "K")
    T[F.smooth_l1_loss] = _huber
    T[F.huber_loss] = _huber

    def _kl(a, n):
        # `kl_div(x, t)` has summand `t * (log t - x)`; the model passes
        # `x = log p`, so this is the usual `t * (log t - log p)`.
        red = _kw(n, "reduction", 3, "mean")
        if red != "batchmean":
            raise Unsupported(f"kl_div reduction={red!r}")
        x, t = S.lift(a[0]), S.lift(a[1])
        return RedNode(t * (S.log(t) - x), None, "outer")
    T[F.kl_div] = _kl

    return T


REDUCE_FUNCS = _reduce_functions()


def lower_reduce(model: nn.Module, example_args: List[Any]) -> Lowered:
    """Lower a module that is `pointwise -> one reduction -> pointwise scaling`.

    All tensor inputs must share one shape, which is the shape being reduced. The
    post-reduction part may only scale the reduced value: referring to an input
    tensor again after the reduction would need a second index map and belongs to
    a different family.
    """
    gm = fx.symbolic_trace(model)
    gm.graph.lint()

    with torch.no_grad():
        out_val = model(*example_args)
    if not isinstance(out_val, torch.Tensor):
        raise Unsupported(f"output is {type(out_val).__name__}, not a Tensor")

    in_shapes: List[Tuple[int, ...]] = []
    tensor_idx: List[int] = []
    env: Dict[fx.Node, Any] = {}
    stage: Dict[fx.Node, str] = {}
    red: Optional[RedNode] = None
    ph = 0

    for node in gm.graph.nodes:
        if node.op == "placeholder":
            v = example_args[ph]
            if isinstance(v, torch.Tensor):
                # Inputs may broadcast against each other: the reduction happens
                # over the broadcast shape, and each input gets its own index map.
                in_shapes.append(tuple(v.shape))
                env[node] = S.Inp(len(tensor_idx))
                stage[node] = "pre"
                tensor_idx.append(ph)
            elif isinstance(v, (int, float)):
                env[node] = S.lit(v)
                stage[node] = "pre"
            else:
                raise Unsupported(f"placeholder {ph} is {type(v).__name__}")
            ph += 1

        elif node.op in ("call_function", "call_method"):
            key = node.target
            args = [env[a] if isinstance(a, fx.Node) else a for a in node.args]
            stages = [stage[a] for a in node.args if isinstance(a, fx.Node)]
            if key in REDUCE_FUNCS:
                if red is not None:
                    raise Unsupported("more than one reduction in the graph")
                if any(st == "post" for st in stages):
                    raise Unsupported("reduction applied after a reduction")
                red = REDUCE_FUNCS[key](args, node)
                env[node] = S.Inp(0)          # slot 0 is the reduced value
                stage[node] = "post"
            elif key in POINTWISE_FUNCS:
                if red is not None and any(
                        isinstance(a, fx.Node) and stage[a] == "pre" for a in node.args):
                    raise Unsupported("pointwise op mixes pre- and post-reduction values")
                env[node] = POINTWISE_FUNCS[key](args, node)
                stage[node] = "post" if any(st == "post" for st in stages) else "pre"
            else:
                raise Unsupported(f"{node.op} {key!r} is neither pointwise nor a reduction")

        elif node.op == "call_module":
            sub = gm.get_submodule(node.target)
            cls = type(sub)
            if cls not in POINTWISE_MODULES:
                raise Unsupported(f"module {cls.__name__} is neither pointwise nor a reduction")
            args = [env[a] if isinstance(a, fx.Node) else a for a in node.args]
            env[node] = POINTWISE_MODULES[cls](sub, args)
            stage[node] = "pre"

        elif node.op == "get_attr":
            raise Unsupported("module has parameters/buffers")

        elif node.op == "output":
            res = node.args[0]
            if not isinstance(res, fx.Node):
                raise Unsupported("output is not a single value")
            if red is None:
                raise Unsupported("no reduction in the graph")
            if stage[res] != "post":
                raise Unsupported("output does not depend on the reduction")
            if not in_shapes:
                raise Unsupported("no tensor inputs")
            try:
                in_shape = tuple(torch.broadcast_shapes(*in_shapes))
            except Exception as e:
                raise Unsupported(f"inputs do not broadcast: {in_shapes}") from e

            d = red.dim
            if d is None:
                outer, K, inner = 1, 1, 1
                for s_ in in_shape:
                    K *= s_
            else:
                if d < 0:
                    d += len(in_shape)
                if not (0 <= d < len(in_shape)):
                    raise Unsupported(f"dim {red.dim} out of range for {in_shape}")
                outer = 1
                for s_ in in_shape[:d]:
                    outer *= s_
                K = in_shape[d]
                inner = 1
                for s_ in in_shape[d + 1:]:
                    inner *= s_

            if outer * inner != out_val.numel():
                raise Unsupported(
                    f"reduced output has {outer*inner} elements but the module "
                    f"returned {out_val.numel()}")

            post = env[res]
            if red.divide_by == "K":
                post = post * S.lit(Fraction(1, K))
            elif red.divide_by == "outer":
                nb = in_shape[0] if in_shape else 1
                post = post * S.lit(Fraction(1, nb))

            n_out = outer * inner
            # Coordinates of the *pre-reduction* element this lane contributes:
            # the output index supplies every axis but the reduced one, and `rk`
            # supplies that one.
            if d is None:
                full = unpack(I.Rk(), list(in_shape))
            else:
                kept = [sz for ax, sz in enumerate(in_shape) if ax != d]
                oc = unpack(I.Pid(), kept) if kept else []
                full = oc[:d] + [I.Rk()] + oc[d:]
            # Each input reads at its own broadcast index: axes of extent one are
            # pinned to 0, which is what broadcasting means.
            offs: List[I.IE] = []
            for si in in_shapes:
                if not si:
                    offs.append(I.Lit(0))
                    continue
                tail = full[len(in_shape) - len(si):]
                sel = [I.Lit(0) if sz == 1 else cc for cc, sz in zip(tail, si)]
                offs.append(pack(sel, list(si)))
            return Lowered(
                family="genred", body=red.body, arity=len(tensor_idx),
                out_size=n_out, out_shape=tuple(out_val.shape),
                tensor_arg_index=tensor_idx,
                K=K, offs=offs,
                post_offs=[I.Lit(0)] * len(tensor_idx),
                post=post,
                notes=[f"reduce over dim {red.dim} of {in_shape} "
                       f"(inputs {in_shapes}): outer={outer} K={K} inner={inner}"])
        else:
            raise Unsupported(f"unhandled fx op {node.op}")

    raise Unsupported("graph has no output node")


# ---------------------------------------------------------------------------
# Contractions (matrix products)
# ---------------------------------------------------------------------------

MATMUL_TARGETS = (torch.matmul, torch.mm, torch.bmm, operator.matmul)


def _einsum_is_matmul(node: fx.Node) -> bool:
    """True for an einsum that just contracts the last axis of the lhs with the
    first axis of the rhs -- `bijl,lk->bijk`, say, which is exactly what `matmul`
    does for a 4-D lhs and a 2-D rhs. Recognising it here means one more task
    reuses the contraction path instead of needing an einsum implementation."""
    if not node.args or not isinstance(node.args[0], str):
        return False
    eq = node.args[0].replace(" ", "")
    if "->" not in eq or eq.count(",") != 1:
        return False
    ins, out = eq.split("->")
    if "," not in ins:
        return False
    a, b = ins.split(",")
    return len(b) == 2 and len(a) >= 2 and a[-1] == b[0] and out == a[:-1] + b[1]


def _prod(xs) -> int:
    out = 1
    for x in xs:
        out *= x
    return out


def lower_matmul(model: nn.Module, example_args: List[Any]) -> Lowered:
    """Lower `A @ B`, optionally followed by `triu`/`tril`.

    Every shape variant in L1 -- square, rectangular, tall-skinny, batched,
    3-D x 2-D, 4-D x 2-D, matrix-vector -- is the same contraction with a
    different index map, so all of them go through this one path and reuse one
    correctness theorem. A triangular mask on the result becomes the family's
    output guard rather than a second kernel.
    """
    gm = fx.symbolic_trace(model)
    gm.graph.lint()
    with torch.no_grad():
        out_val = model(*example_args)

    shapes: List[Tuple[int, ...]] = []
    for v in example_args:
        if not isinstance(v, torch.Tensor):
            raise Unsupported("matmul lowering expects tensor inputs only")
        shapes.append(tuple(v.shape))

    # Find the matmul, any triangular mask on its result, and which operands are
    # transposed. A transpose is *not* materialised: it flips that operand's index
    # map, which costs nothing and keeps the task inside one kernel.
    mm_node = None
    tri: Optional[str] = None
    flipped: Dict[fx.Node, bool] = {}
    src: Dict[fx.Node, int] = {}
    ph = 0
    for node in gm.graph.nodes:
        if node.op == "placeholder":
            src[node], flipped[node] = ph, False
            ph += 1
        elif node.op in ("call_function", "call_method"):
            tgt = node.target
            is_t = (tgt is getattr and len(node.args) == 2
                    and node.args[1] in ("T", "mT")) or tgt in ("t", "T", torch.t)
            if (tgt in MATMUL_TARGETS or tgt in ("matmul", "mm", "bmm")
                    or (tgt is torch.einsum and _einsum_is_matmul(node))):
                if mm_node is not None:
                    raise Unsupported("more than one matmul")
                mm_node = node
            elif tgt in (torch.triu, torch.tril, "triu", "tril"):
                tri = tgt if isinstance(tgt, str) else tgt.__name__
            elif is_t:
                base = node.args[0]
                if base not in src:
                    raise Unsupported("transpose of a non-input")
                src[node], flipped[node] = src[base], not flipped[base]
            else:
                raise Unsupported(f"{tgt!r} alongside a matmul")
        elif node.op == "call_module":
            raise Unsupported("module call alongside a matmul")
        elif node.op == "get_attr":
            raise Unsupported("matmul lowering does not handle parameters")
    if mm_node is None:
        raise Unsupported("no matmul in the graph")
    if len(shapes) != 2:
        raise Unsupported(f"expected 2 tensor inputs, got {len(shapes)}")

    mm_args = [x for x in mm_node.args if isinstance(x, fx.Node)]
    if len(mm_args) != 2:
        raise Unsupported("matmul does not have two traced operands")
    lhs, rhs = mm_args
    if lhs not in src or rhs not in src:
        raise Unsupported("matmul operands are not inputs (or transposes of them)")
    ta, tb = flipped[lhs], flipped[rhs]
    pa, pb = shapes[src[lhs]], shapes[src[rhs]]
    if (ta and len(pa) != 2) or (tb and len(pb) != 2):
        raise Unsupported("transposed operands are only handled at rank 2")
    # logical shapes, after any transpose
    sa = (pa[1], pa[0]) if ta else pa
    sb = (pb[1], pb[0]) if tb else pb

    if len(sa) < 2:
        raise Unsupported(f"lhs is {len(sa)}-D")
    if len(sb) == 1:
        # matrix-vector: treat as N = 1
        K, N = sb[0], 1
        b_batch: Tuple[int, ...] = ()
    else:
        K, N = sb[-2], sb[-1]
        b_batch = sb[:-2]
    M = sa[-2]
    a_batch = sa[:-2]
    if sa[-1] != K:
        raise Unsupported(f"contraction mismatch: lhs {sa} vs rhs {sb}")
    if b_batch not in ((), a_batch):
        raise Unsupported(f"unsupported batch shapes {a_batch} vs {b_batch}")

    nbatch = _prod(a_batch)
    if out_val.numel() != nbatch * M * N:
        raise Unsupported(
            f"expected {nbatch*M*N} output elements, module returned {out_val.numel()}")

    # q -> (batch, i, j)
    q = I.Pid()
    j = q % I.Lit(N)
    i = (q // I.Lit(N)) % I.Lit(M)
    batch = q // I.Lit(M * N)
    a_b = batch if a_batch else I.Lit(0)
    b_b = batch if b_batch else I.Lit(0)
    # Physical offsets: a transposed operand swaps the roles of its two axes.
    off_a = (I.Rk() * I.Lit(pa[1]) + i) if ta else ((a_b * I.Lit(M) + i) * I.Lit(K) + I.Rk())
    off_b = (j * I.Lit(pb[1]) + I.Rk()) if tb else ((b_b * I.Lit(K) + I.Rk()) * I.Lit(N) + j)

    guard: I.BE = I.TT()
    if tri == "triu":
        guard = I.le(i, j)          # keep the upper triangle
    elif tri == "tril":
        guard = I.le(j, i)

    return Lowered(
        family="genred", body=S.Inp(0) * S.Inp(1), arity=2,
        out_size=out_val.numel(), out_shape=tuple(out_val.shape),
        tensor_arg_index=[src[lhs], src[rhs]],
        K=K, offs=[off_a, off_b], post_offs=[I.Lit(0), I.Lit(0)],
        out_guard=guard, post=S.Inp(0),
        notes=[f"contraction: batch={nbatch} M={M} K={K} N={N}"
               + (", lhs^T" if ta else "") + (", rhs^T" if tb else "")
               + (f", {tri} mask" if tri else "")])


# ---------------------------------------------------------------------------
# Convolution
# ---------------------------------------------------------------------------

def unpack(idx: I.IE, dims: List[int]) -> List[I.IE]:
    """Row-major coordinates of a flat index within `dims`.

    The leading coordinate needs no modulus: a flat index is assumed in range,
    which for the output index is guaranteed by the grid size and for the
    reduction index by the loop bound.
    """
    out: List[I.IE] = []
    for d in range(len(dims)):
        stride = _prod(dims[d + 1:])
        e = idx if stride == 1 else idx // I.Lit(stride)
        if d != 0:
            e = e % I.Lit(dims[d])
        out.append(e)
    return out


def pack(coords: List[I.IE], dims: List[int]) -> I.IE:
    """Flat row-major index from coordinates."""
    assert len(coords) == len(dims) and coords
    out = coords[0]
    for c, dsz in zip(coords[1:], dims[1:]):
        out = out * I.Lit(dsz) + c
    return out


CONV_FWD = (nn.Conv1d, nn.Conv2d, nn.Conv3d)
CONV_T = (nn.ConvTranspose1d, nn.ConvTranspose2d, nn.ConvTranspose3d)


def _tup(v, r: int) -> Tuple[int, ...]:
    if isinstance(v, int):
        return (v,) * r
    return tuple(v)


def lower_conv(model: nn.Module, example_args: List[Any]) -> Lowered:
    """Lower a single convolution -- forward or transposed, any rank, with
    stride, padding, dilation, groups and optional bias.

    All 35 convolution tasks in L1 are this one operator under different
    parameters, and all of them reduce to an *index map* over the family already
    proved in `GenRed.lean`. No new proof obligation is created by supporting
    them; the work is arithmetic, and the arithmetic is checked by the same
    `instK_eval` lemma that licenses a plain axis reduction.

    Two subtleties, both about `Nat` arithmetic:

      * A forward convolution's input coordinate `o*s - p + k*d` can go negative.
        Written over `Nat` it saturates at zero, so the *guard* must exclude those
        taps rather than relying on the subtraction; `pad <= t` is that guard.
      * A transposed convolution contributes only where `stride` divides
        `o + p - k*d`, which the guard states directly as a `%` test.
    """
    gm = fx.symbolic_trace(model)
    gm.graph.lint()

    conv_node = None
    for node in gm.graph.nodes:
        if node.op == "call_module":
            sub = gm.get_submodule(node.target)
            if isinstance(sub, CONV_FWD + CONV_T):
                if conv_node is not None:
                    raise Unsupported("more than one convolution")
                conv_node = node
            else:
                raise Unsupported(f"module {type(sub).__name__} alongside a convolution")
        elif node.op in ("call_function", "call_method"):
            raise Unsupported(f"{node.target!r} alongside a convolution")
    if conv_node is None:
        raise Unsupported("no convolution module in the graph")

    conv = gm.get_submodule(conv_node.target)
    transposed = isinstance(conv, CONV_T)
    x = example_args[0]
    if not isinstance(x, torch.Tensor):
        raise Unsupported("convolution input is not a tensor")
    with torch.no_grad():
        y = model(*example_args)

    sx = tuple(x.shape)
    rank = len(sx) - 2
    if rank < 1:
        raise Unsupported(f"input {sx} has no spatial dimensions")
    N, Cin = sx[0], sx[1]
    Din = list(sx[2:])
    Dout = list(y.shape[2:])
    Cout = y.shape[1]
    g = conv.groups
    stride = _tup(conv.stride, rank)
    pad = _tup(conv.padding, rank)
    dil = _tup(conv.dilation, rank)
    if any(not isinstance(pv, int) for pv in pad):
        raise Unsupported(f"non-integer padding {conv.padding!r}")
    Dk = list(conv.kernel_size)
    if Cin % g or Cout % g:
        raise Unsupported(f"groups {g} does not divide channels {Cin}/{Cout}")
    CinG, CoutG = Cin // g, Cout // g

    # output index -> (n, oc, o...)
    q = I.Pid()
    ocoords = unpack(q, [N, Cout] + Dout)
    n, oc = ocoords[0], ocoords[1]
    o = ocoords[2:]

    # reduction index -> (c', k...)  where c' runs over the per-group channels of
    # whichever tensor is contracted
    cred = CinG if not transposed else CinG
    kcoords = unpack(I.Rk(), [cred] + Dk)
    cp, kk = kcoords[0], kcoords[1:]
    K = cred * _prod(Dk)

    guards: List[I.BE] = []
    in_spatial: List[I.IE] = []
    if not transposed:
        grp = oc // I.Lit(CoutG)
        ic_abs = grp * I.Lit(CinG) + cp
        for d in range(rank):
            t = o[d] * I.Lit(stride[d]) + kk[d] * I.Lit(dil[d])
            # `t - pad` is exact only where `pad <= t`; the guard, not the
            # subtraction, is what excludes the padded taps.
            guards.append(I.le(I.Lit(pad[d]), t))
            guards.append(I.lt(t, I.Lit(Din[d] + pad[d])))
            in_spatial.append(t - I.Lit(pad[d]))
        w_dims = [Cout, CinG] + Dk
        w_coords = [oc, cp] + list(kk)
    else:
        grp = oc // I.Lit(CoutG)
        ic_abs = grp * I.Lit(CinG) + cp
        ocp = oc % I.Lit(CoutG)
        for d in range(rank):
            t = o[d] + I.Lit(pad[d])
            kd = kk[d] * I.Lit(dil[d])
            guards.append(I.le(kd, t))
            num = t - kd
            guards.append(I.Cmp("eq", num % I.Lit(stride[d]), I.Lit(0)))
            i_d = num // I.Lit(stride[d])
            guards.append(I.lt(i_d, I.Lit(Din[d])))
            in_spatial.append(i_d)
        w_dims = [Cin, CoutG] + Dk
        w_coords = [ic_abs, ocp] + list(kk)

    off_x = pack([n, ic_abs] + in_spatial, [N, Cin] + Din)
    off_w = pack(w_coords, w_dims)

    params = ["weight"]
    post: S.SE = S.Inp(0)
    post_offs: List[I.IE] = [I.Lit(0), I.Lit(0)]
    if conv.bias is not None:
        # bias is input buffer 2, hence post slot 3, read at the channel index
        params.append("bias")
        post = S.Bin("add", S.Inp(0), S.Inp(3))
        post_offs.append(oc)

    return Lowered(
        family="genred", body=S.Inp(0) * S.Inp(1), arity=1 + len(params),
        out_size=y.numel(), out_shape=tuple(y.shape),
        tensor_arg_index=[0],
        K=K, offs=[off_x, off_w] + ([I.Lit(0)] if conv.bias is not None else []),
        post_offs=post_offs, in_range=I.all_of(guards), post=post,
        param_paths=[f"{conv_node.target}.{pp}" for pp in params],
        notes=[f"{'transposed ' if transposed else ''}conv{rank}d: "
               f"N={N} Cin={Cin} Cout={Cout} groups={g} k={tuple(Dk)} "
               f"stride={stride} pad={pad} dil={dil} K={K}"
               + (" +bias" if conv.bias is not None else "")])


# ---------------------------------------------------------------------------
# Row-normalising operators: reduce along an axis, then use the reduced value at
# every element of that row. Two stages, one intermediate buffer.
# ---------------------------------------------------------------------------

@dataclass
class RowRed:
    """A recognised keepdim reduction inside a row-normalising graph.

    `wrap` turns the raw sum the kernel accumulates into the value the rest of the
    graph sees -- `sqrt` for an L2 norm, a scale for a mean. Keeping it out of
    stage 1 means stage 1 is always a plain sum and the wrap costs nothing extra in
    stage 2, where it is evaluated once per output element anyway.
    """
    body: S.SE                       # the summand, over the inputs
    dim: Optional[int]               # None = over every element
    wrap: Any                        # SE -> SE


def _rownorm_reducers() -> Dict[Any, Callable]:
    T: Dict[Any, Callable] = {}

    def keepdim_ok(n: fx.Node) -> bool:
        return bool(_kw(n, "keepdim", 2, False))

    def _sum(a, n):
        d = _kw(n, "dim", 1, None)
        if d is not None and not keepdim_ok(n):
            raise Unsupported("reduction without keepdim is not a row normalisation")
        return RowRed(S.lift(a[0]), d, lambda r: r)
    T[torch.sum] = _sum

    def _mean(a, n):
        d = _kw(n, "dim", 1, None)
        if d is not None and not keepdim_ok(n):
            raise Unsupported("reduction without keepdim is not a row normalisation")
        return RowRed(S.lift(a[0]), d, "mean")
    T[torch.mean] = _mean

    def _norm(a, n):
        pv = _kw(n, "p", 1, "fro")
        d = _kw(n, "dim", 2, None)
        if pv not in (2, 2.0, "fro", None):
            raise Unsupported(f"norm p={pv!r}")
        if d is not None and not _kw(n, "keepdim", 3, False):
            raise Unsupported("norm without keepdim")
        x = S.lift(a[0])
        return RowRed(x * x, d, S.sqrt)
    T[torch.norm] = _norm
    T[torch.linalg.norm] = _norm

    return T


ROWNORM_REDUCERS = _rownorm_reducers()

# Fused operators that are themselves row normalisations.
SOFTMAXES = {
    torch.softmax: "softmax", F.softmax: "softmax", torch.nn.Softmax: "softmax",
    torch.log_softmax: "log_softmax", F.log_softmax: "log_softmax",
}


def lower_rownorm(model: nn.Module, example_args: List[Any]) -> Lowered:
    """Lower `reduce along one axis, then combine with the original` as two stages.

    Softmax, log-softmax, RMS norm, Frobenius norm, L1 and L2 normalisation are all
    this shape. Stage 1 accumulates the row sums into an intermediate buffer of
    `outer*inner` elements; stage 2 reads the original inputs at `q` and the
    intermediate at `q`'s row, and is a `K = 1` instance of the same reducing
    family. The composition is justified by `two_stage`, whose locality obligation
    becomes `bound_row`.
    """
    gm = fx.symbolic_trace(model)
    gm.graph.lint()
    with torch.no_grad():
        out_val = model(*example_args)
    if not isinstance(out_val, torch.Tensor):
        raise Unsupported("output is not a Tensor")

    in_shape: Optional[Tuple[int, ...]] = None
    tensor_idx: List[int] = []
    env: Dict[fx.Node, Any] = {}
    stage: Dict[fx.Node, str] = {}
    red: Optional[RowRed] = None
    softmax_kind: Optional[str] = None
    ph = 0
    ARITY_SLOT = None            # filled once arity is known

    nodes = list(gm.graph.nodes)
    n_tensors = sum(1 for v in example_args if isinstance(v, torch.Tensor))
    red_slot = S.Inp(n_tensors)  # the intermediate is the last input buffer

    for node in nodes:
        if node.op == "placeholder":
            v = example_args[ph]
            if isinstance(v, torch.Tensor):
                sv = tuple(v.shape)
                if in_shape is None:
                    in_shape = sv
                elif sv != in_shape:
                    raise Unsupported(f"inputs differ in shape: {in_shape} vs {sv}")
                env[node] = S.Inp(len(tensor_idx))
                stage[node] = "pre"
                tensor_idx.append(ph)
            elif isinstance(v, (int, float)):
                env[node] = S.lit(v)
                stage[node] = "pre"
            else:
                raise Unsupported(f"placeholder {ph} is {type(v).__name__}")
            ph += 1

        elif node.op in ("call_function", "call_method", "call_module"):
            if node.op == "call_module":
                sub = gm.get_submodule(node.target)
                key: Any = type(sub)
                if key in POINTWISE_MODULES:
                    a = [env[x] if isinstance(x, fx.Node) else x for x in node.args]
                    env[node] = POINTWISE_MODULES[key](sub, a)
                    stage[node] = "pre"
                    continue
                if key in SOFTMAXES:
                    node_dim = getattr(sub, "dim", None)
                    if red is not None:
                        raise Unsupported("more than one reduction")
                    softmax_kind = SOFTMAXES[key]
                    x = env[node.args[0]]
                    red = RowRed(S.exp(x), node_dim, lambda r: r)
                    env[node] = (S.exp(x) * S.Recip(red_slot) if softmax_kind == "softmax"
                                 else x - S.log(red_slot))
                    stage[node] = "post"
                    continue
                raise Unsupported(f"module {key.__name__} in a row normalisation")

            tgt = node.target
            a = [env[x] if isinstance(x, fx.Node) else x for x in node.args]
            stages = [stage[x] for x in node.args if isinstance(x, fx.Node)]
            if tgt in SOFTMAXES:
                if red is not None:
                    raise Unsupported("more than one reduction")
                softmax_kind = SOFTMAXES[tgt]
                d = _kw(node, "dim", 1, None)
                if d is None:
                    raise Unsupported("softmax needs an explicit dim")
                x = a[0]
                red = RowRed(S.exp(x), d, lambda r: r)
                env[node] = (S.exp(x) * S.Recip(red_slot) if softmax_kind == "softmax"
                             else x - S.log(red_slot))
                stage[node] = "post"
            elif tgt in ROWNORM_REDUCERS:
                if red is not None:
                    raise Unsupported("more than one reduction")
                if any(st == "post" for st in stages):
                    raise Unsupported("reduction of an already-reduced value")
                red = ROWNORM_REDUCERS[tgt](a, node)
                env[node] = red_slot     # patched below once K is known
                stage[node] = "post"
            elif tgt in POINTWISE_FUNCS:
                env[node] = POINTWISE_FUNCS[tgt](a, node)
                stage[node] = "post" if any(st == "post" for st in stages) else "pre"
            else:
                raise Unsupported(f"{tgt!r} in a row normalisation")

        elif node.op == "get_attr":
            raise Unsupported("module has parameters")

        elif node.op == "output":
            res = node.args[0]
            if not isinstance(res, fx.Node):
                raise Unsupported("output is not a single value")
            if red is None:
                raise Unsupported("no reduction in the graph")
            if stage[res] != "post":
                raise Unsupported("output does not use the reduced value")
            if in_shape is None:
                raise Unsupported("no tensor inputs")
            if tuple(out_val.shape) != in_shape:
                raise Unsupported(
                    f"output {tuple(out_val.shape)} differs from input {in_shape}")

            d = red.dim
            if d is None:
                outer, inner = 1, 1
                K = _prod(in_shape)
            else:
                if d < 0:
                    d += len(in_shape)
                outer = _prod(in_shape[:d])
                K = in_shape[d]
                inner = _prod(in_shape[d + 1:])
            n1 = outer * inner
            arity = len(tensor_idx)

            # stage 1: the row sums
            s1_idx = ((I.Pid() // I.Lit(inner)) * I.Lit(K) + I.Rk()) * I.Lit(inner) \
                     + I.Pid() % I.Lit(inner)
            stage1 = Lowered(
                family="genred", body=red.body, arity=arity,
                out_size=n1, out_shape=(n1,), tensor_arg_index=tensor_idx,
                K=K, offs=[s1_idx] * arity, post_offs=[I.Lit(0)] * arity,
                post=S.Inp(0),
                notes=[f"stage 1: row sums, outer={outer} K={K} inner={inner}"])

            # stage 2: originals at q, the reduced value at q's row
            row = (I.Pid() // (I.Lit(K) * I.Lit(inner))) * I.Lit(inner) \
                  + I.Pid() % I.Lit(inner)
            body2 = env[res]
            if red.wrap == "mean":
                body2 = _subst_slot(body2, arity, lambda r: r * S.lit(Fraction(1, K)))
            elif callable(red.wrap) and softmax_kind is None:
                body2 = _subst_slot(body2, arity, red.wrap)
            stage2 = Lowered(
                family="genred", body=body2, arity=arity + 1,
                out_size=out_val.numel(), out_shape=tuple(out_val.shape),
                tensor_arg_index=tensor_idx,
                K=1, offs=[I.Pid()] * arity + [row],
                post_offs=[I.Lit(0)] * (arity + 1), post=S.Inp(0),
                notes=[f"stage 2: normalise, row index into a {n1}-element buffer"])

            return Lowered(
                family="pipeline", body=body2, arity=arity,
                out_size=out_val.numel(), out_shape=tuple(out_val.shape),
                tensor_arg_index=tensor_idx, stages=[stage1, stage2], n1=n1,
                K=K, offs=[], post_offs=[],
                outer=outer, inner=inner,
                notes=[f"row normalisation over dim {red.dim} of {in_shape}: "
                       f"outer={outer} K={K} inner={inner}, intermediate {n1}"])
        else:
            raise Unsupported(f"unhandled fx op {node.op}")
    raise Unsupported("graph has no output node")


def _subst_slot(e: S.SE, slot: int, f: Callable[[S.SE], S.SE]) -> S.SE:
    """Replace every `Inp(slot)` by `f(Inp(slot))`.

    Used to push a reduction's `wrap` (a `sqrt`, or a mean's scale) into stage 2, so
    stage 1 stays a plain sum.
    """
    if isinstance(e, S.Inp):
        return f(e) if e.b == slot else e
    if isinstance(e, S.Lit):
        return e
    if isinstance(e, S.Bin):
        return S.Bin(e.op, _subst_slot(e.a, slot, f), _subst_slot(e.b, slot, f))
    if isinstance(e, S.Un):
        return S.Un(e.f, _subst_slot(e.a, slot, f))
    if isinstance(e, S.Recip):
        return S.Recip(_subst_slot(e.a, slot, f))
    if isinstance(e, S.SelLe):
        return S.SelLe(*(_subst_slot(x, slot, f) for x in (e.a, e.b, e.t, e.e)))
    raise Unsupported(f"cannot substitute in {type(e).__name__}")


AVGPOOL = (nn.AvgPool1d, nn.AvgPool2d, nn.AvgPool3d)


def lower_avgpool(model: nn.Module, example_args: List[Any]) -> Lowered:
    """Lower average pooling: a windowed sum over the reduced axis, scaled.

    PyTorch's default `count_include_pad=True` divides by the *full* window area
    regardless of how much of the window is padding, and padded taps contribute
    zero. Both fall out of the family directly: the guard drops the out-of-bounds
    taps (so they contribute zero) and the post-scale is the constant `1/|window|`.
    """
    gm = fx.symbolic_trace(model)
    gm.graph.lint()
    pool = None
    for node in gm.graph.nodes:
        if node.op == "call_module":
            sub = gm.get_submodule(node.target)
            if isinstance(sub, AVGPOOL):
                if pool is not None:
                    raise Unsupported("more than one pooling layer")
                pool = sub
            else:
                raise Unsupported(f"module {type(sub).__name__} alongside pooling")
        elif node.op in ("call_function", "call_method"):
            raise Unsupported(f"{node.target!r} alongside pooling")
    if pool is None:
        raise Unsupported("no average-pooling module")
    if getattr(pool, "ceil_mode", False):
        raise Unsupported("ceil_mode pooling")
    if getattr(pool, "count_include_pad", True) is False:
        raise Unsupported("count_include_pad=False changes the divisor per window")
    if getattr(pool, "divisor_override", None) is not None:
        raise Unsupported("divisor_override")

    x = example_args[0]
    with torch.no_grad():
        y = model(*example_args)
    sx = tuple(x.shape)
    rank = len(sx) - 2
    N, C = sx[0], sx[1]
    Din, Dout = list(sx[2:]), list(y.shape[2:])
    Dk = list(_tup(pool.kernel_size, rank))
    stride = _tup(pool.stride if pool.stride is not None else pool.kernel_size, rank)
    pad = _tup(pool.padding, rank)

    q = I.Pid()
    oc = unpack(q, [N, C] + Dout)
    n, c, o = oc[0], oc[1], oc[2:]
    kk = unpack(I.Rk(), Dk)

    guards, in_spatial = [], []
    for d in range(rank):
        t = o[d] * I.Lit(stride[d]) + kk[d]
        guards.append(I.le(I.Lit(pad[d]), t))
        guards.append(I.lt(t, I.Lit(Din[d] + pad[d])))
        in_spatial.append(t - I.Lit(pad[d]))

    off = pack([n, c] + in_spatial, [N, C] + Din)
    area = _prod(Dk)
    return Lowered(
        family="genred", body=S.Inp(0), arity=1,
        out_size=y.numel(), out_shape=tuple(y.shape), tensor_arg_index=[0],
        K=area, offs=[off], post_offs=[I.Lit(0)],
        in_range=I.all_of(guards),
        post=S.Bin("mul", S.Inp(0), S.lit(Fraction(1, area))),
        notes=[f"avgpool{rank}d: N={N} C={C} k={tuple(Dk)} stride={stride} "
               f"pad={pad} window={area}"])


def lower_broadcast_pointwise(model: nn.Module, example_args: List[Any]) -> Lowered:
    """Lower a pointwise graph whose inputs *broadcast* against each other.

    Expressed as a degenerate reduction (`K = 1`) so it reuses the same verified
    family: what broadcasting really is, is a per-input index map that drops the
    axes of extent one. No separate kernel shape and no separate proof.
    """
    gm = fx.symbolic_trace(model)
    gm.graph.lint()
    with torch.no_grad():
        out_val = model(*example_args)
    if not isinstance(out_val, torch.Tensor):
        raise Unsupported("output is not a Tensor")
    so = tuple(out_val.shape)
    if not so:
        raise Unsupported("scalar output is a reduction, not a broadcast map")

    tensor_idx: List[int] = []
    in_shapes: List[Tuple[int, ...]] = []
    env: Dict[fx.Node, Any] = {}
    # Which buffer a value came from, and the *logical* shape it has at the point
    # it enters the expression. A reshape changes the latter without moving any
    # data, and it is the logical shape that decides how the input aligns under
    # broadcasting -- ignoring an `unsqueeze` silently transposes the result.
    node_buf: Dict[fx.Node, int] = {}
    logical: Dict[fx.Node, Tuple[int, ...]] = {}
    ph = 0
    for node in gm.graph.nodes:
        if node.op == "placeholder":
            v = example_args[ph]
            if isinstance(v, torch.Tensor):
                sv = tuple(v.shape)
                b = len(tensor_idx)
                env[node] = S.Inp(b)
                node_buf[node] = b
                logical[node] = sv
                tensor_idx.append(ph)
                in_shapes.append(sv)
            elif isinstance(v, (int, float)):
                env[node] = S.lit(v)
            else:
                raise Unsupported(f"placeholder {ph} is {type(v).__name__}")
            ph += 1
        elif node.op in ("call_function", "call_method"):
            if node.target in POINTWISE_FUNCS:
                a = [env[x] if isinstance(x, fx.Node) else x for x in node.args]
                env[node] = POINTWISE_FUNCS[node.target](a, node)
            elif node.target in ("unsqueeze", "reshape", "view", "squeeze",
                                 torch.unsqueeze, torch.reshape, torch.squeeze):
                # A reshape of a contiguous tensor preserves row-major order, so the
                # physical offset is still the flat index -- but over the *new*
                # shape. Record that; the index map is built from it.
                base = node.args[0]
                if base not in logical:
                    raise Unsupported("reshape of a non-input value")
                base_shape = logical[base]
                tgt = node.target
                nm = tgt if isinstance(tgt, str) else tgt.__name__
                if nm == "unsqueeze":
                    d = node.args[1] if len(node.args) > 1 else node.kwargs.get("dim")
                    if not isinstance(d, int):
                        raise Unsupported("unsqueeze without a literal dim")
                    if d < 0:
                        d += len(base_shape) + 1
                    new = base_shape[:d] + (1,) + base_shape[d:]
                elif nm == "squeeze":
                    if len(node.args) > 1 or "dim" in node.kwargs:
                        d = node.args[1] if len(node.args) > 1 else node.kwargs["dim"]
                        if d < 0:
                            d += len(base_shape)
                        if base_shape[d] != 1:
                            raise Unsupported(f"squeeze of axis {d} with extent "
                                              f"{base_shape[d]}")
                        new = base_shape[:d] + base_shape[d + 1:]
                    else:
                        new = tuple(x for x in base_shape if x != 1)
                else:                                   # reshape / view
                    dims = node.args[1:]
                    if len(dims) == 1 and isinstance(dims[0], (list, tuple)):
                        dims = tuple(dims[0])
                    if not all(isinstance(x, int) and x >= 0 for x in dims):
                        raise Unsupported(f"{nm} with non-literal shape {dims}")
                    new = tuple(dims)
                    if _prod(new) != _prod(base_shape):
                        raise Unsupported(f"{nm} changes element count")
                env[node] = env[base]
                node_buf[node] = node_buf[base]
                logical[node] = new
                bi = node_buf[base]
                if in_shapes[bi] not in (base_shape, new) and in_shapes[bi] != new:
                    raise Unsupported(f"buffer {bi} is used at two logical shapes")
                in_shapes[bi] = new
            else:
                raise Unsupported(f"{node.target!r} is not pointwise")
        elif node.op == "call_module":
            sub = gm.get_submodule(node.target)
            if type(sub) not in POINTWISE_MODULES:
                raise Unsupported(f"module {type(sub).__name__} is not pointwise")
            a = [env[x] if isinstance(x, fx.Node) else x for x in node.args]
            env[node] = POINTWISE_MODULES[type(sub)](sub, a)
        elif node.op == "get_attr":
            raise Unsupported("module has parameters")
        elif node.op == "output":
            res = node.args[0]
            if not isinstance(res, fx.Node):
                raise Unsupported("output is not a single value")
            for sv in in_shapes:
                if len(sv) > len(so):
                    raise Unsupported(f"input rank {len(sv)} exceeds output rank {len(so)}")
                for a, b2 in zip(reversed(sv), reversed(so)):
                    if a not in (1, b2):
                        raise Unsupported(f"{sv} does not broadcast to {so}")
            coords = unpack(I.Pid(), list(so))
            offs: List[I.IE] = []
            for sv in in_shapes:
                tail = coords[len(so) - len(sv):]
                sel = [I.Lit(0) if d == 1 else cc for cc, d in zip(tail, sv)]
                offs.append(pack(sel, list(sv)) if sv else I.Lit(0))
            return Lowered(
                family="genred", body=env[res], arity=len(tensor_idx),
                out_size=out_val.numel(), out_shape=so,
                tensor_arg_index=tensor_idx,
                K=1, offs=offs, post_offs=[I.Lit(0)] * len(tensor_idx),
                post=S.Inp(0),
                notes=[f"broadcast map: {in_shapes} -> {so}"])
    raise Unsupported("graph has no output node")


FAMILIES: List[Callable[[nn.Module, List[Any]], Lowered]] = [
    lower_pointwise, lower_reduce, lower_matmul, lower_conv, lower_avgpool,
    lower_rownorm, lower_broadcast_pointwise]


def lower(model: nn.Module, example_args: List[Any]) -> Tuple[Optional[Lowered], List[str]]:
    """Try each family in turn. Returns the lowering, or `None` plus the reason
    each family declined."""
    reasons: List[str] = []
    for fam in FAMILIES:
        try:
            return fam(model, example_args), reasons
        except Unsupported as e:
            reasons.append(f"{fam.__name__}: {e}")
        except Exception as e:  # tracing failures etc.
            reasons.append(f"{fam.__name__}: {type(e).__name__}: {e}")
    return None, reasons
