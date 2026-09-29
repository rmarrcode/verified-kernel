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
from .frontend import NO_IDX_SLOT, Lowered, Unsupported, _prod, pack, unpack


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
