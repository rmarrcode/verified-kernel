"""Rewriting fused `torch.nn` modules as the arithmetic they perform.

`nn.MultiheadAttention` and `nn.TransformerEncoderLayer` are leaves to `fx`: a trace
records one opaque call, and PyTorch runs a fused kernel behind it. Their definitions
are not opaque, though -- they are a handful of contractions, a softmax and two
norms -- so before tracing, each is replaced by a module that spells that arithmetic
out. The graph that results is made of operators the chain compiler already lowers.

Two things keep this honest. The replacement *shares* the original's parameters under
the original's names, so the parameter paths recorded in the lowering are the paths
the reference module has, and the kernel reads the very tensors the reference reads.
And anything the rewrite does not model -- a mask, a separate key/value dimension, a
bias on the key/value sequence -- is refused rather than dropped: this is the
frontend, where a mis-lowering would produce a kernel provably equal to the wrong
spec.
"""

from __future__ import annotations

import math

import torch
import torch.nn as nn
import torch.nn.functional as F

from .frontend import Unsupported


class ExplicitMHA(nn.Module):
    """`nn.MultiheadAttention`, self- or cross-attention, without masks.

    PyTorch's definition: project with the packed `in_proj_weight`, split into heads,
    `softmax(q k^T / sqrt(d)) v` per head, concatenate, project with `out_proj`.
    """

    def __init__(self, m: nn.MultiheadAttention):
        super().__init__()
        if not m._qkv_same_embed_dim:
            raise Unsupported("MultiheadAttention with separate k/v dimensions")
        if m.bias_k is not None or m.bias_v is not None or m.add_zero_attn:
            raise Unsupported("MultiheadAttention with bias_k/bias_v/add_zero_attn")
        self.in_proj_weight = m.in_proj_weight
        self.in_proj_bias = m.in_proj_bias
        self.out_proj = m.out_proj
        self.embed_dim = m.embed_dim
        self.num_heads = m.num_heads
        self.batch_first = m.batch_first
        self.dropout = m.dropout

    def forward(self, query, key, value, key_padding_mask=None, need_weights=True,
                attn_mask=None, average_attn_weights=True, is_causal=False):
        if key_padding_mask is not None or attn_mask is not None or is_causal:
            raise Unsupported("MultiheadAttention with a mask")
        E, H = self.embed_dim, self.num_heads
        D = E // H
        if not self.batch_first:
            query, key, value = (t.transpose(0, 1) for t in (query, key, value))
        N, L = query.shape[0], query.shape[1]
        S_ = key.shape[1]
        W, b = self.in_proj_weight, self.in_proj_bias
        bq = b[0:E] if b is not None else None
        bk = b[E:2 * E] if b is not None else None
        bv = b[2 * E:3 * E] if b is not None else None
        q = F.linear(query, W[0:E], bq)
        k = F.linear(key, W[E:2 * E], bk)
        v = F.linear(value, W[2 * E:3 * E], bv)
        q = q.reshape(N, L, H, D).transpose(1, 2)            # (N, H, L, D)
        k = k.reshape(N, S_, H, D).transpose(1, 2)           # (N, H, S, D)
        v = v.reshape(N, S_, H, D).transpose(1, 2)
        att = torch.matmul(q, k.transpose(2, 3)) / math.sqrt(D)
        att = F.softmax(att, dim=-1)
        y = torch.matmul(att, v)                             # (N, H, L, D)
        y = y.transpose(1, 2).reshape(N, L, E)
        y = self.out_proj(y)
        if not self.batch_first:
            y = y.transpose(0, 1)
        return y, None


class ExplicitEncoderLayer(nn.Module):
    """`nn.TransformerEncoderLayer`, post- or pre-norm, without masks."""

    def __init__(self, m: nn.TransformerEncoderLayer):
        super().__init__()
        self.self_attn = ExplicitMHA(m.self_attn)
        self.linear1, self.linear2 = m.linear1, m.linear2
        self.norm1, self.norm2 = m.norm1, m.norm2
        self.norm_first = m.norm_first
        act = m.activation
        if act is F.relu or isinstance(act, nn.ReLU):
            self.act = "relu"
        elif act is F.gelu or isinstance(act, nn.GELU):
            self.act = "gelu"
        else:
            raise Unsupported(f"TransformerEncoderLayer activation {act!r}")

    def _sa(self, x):
        return self.self_attn(x, x, x)[0]

    def _ff(self, x):
        h = self.linear1(x)
        h = F.relu(h) if self.act == "relu" else F.gelu(h)
        return self.linear2(h)

    def forward(self, src, src_mask=None, src_key_padding_mask=None, is_causal=False):
        if src_mask is not None or src_key_padding_mask is not None or is_causal:
            raise Unsupported("TransformerEncoderLayer with a mask")
        x = src
        if self.norm_first:
            x = x + self._sa(self.norm1(x))
            x = x + self._ff(self.norm2(x))
        else:
            x = self.norm1(x + self._sa(x))
            x = self.norm2(x + self._ff(x))
        return x


class ExplicitEncoder(nn.Module):
    """`nn.TransformerEncoder`: its layers in order, then its optional norm."""

    def __init__(self, m: nn.TransformerEncoder):
        super().__init__()
        self.layers = nn.ModuleList([ExplicitEncoderLayer(l) for l in m.layers])
        self.norm = m.norm

    def forward(self, src, mask=None, src_key_padding_mask=None, is_causal=None):
        if mask is not None or src_key_padding_mask is not None or is_causal:
            raise Unsupported("TransformerEncoder with a mask")
        x = src
        for layer in self.layers:
            x = layer(x)
        if self.norm is not None:
            x = self.norm(x)
        return x


REWRITES = [
    (nn.TransformerEncoder, ExplicitEncoder),
    (nn.TransformerEncoderLayer, ExplicitEncoderLayer),
    (nn.MultiheadAttention, ExplicitMHA),
]


def make_explicit(model: nn.Module) -> int:
    """Replace, in place, every fused module this file knows by its explicit form.
    Returns how many were replaced."""
    count = 0
    for name, child in list(model.named_children()):
        for cls, repl in REWRITES:
            if type(child) is cls:
                setattr(model, name, repl(child))
                count += 1
                break
        else:
            count += make_explicit(child)
    return count


def settle_runtime_switches(model: nn.Module, example_args) -> None:
    """Make, before tracing, the module swaps a forward would make while running.

    BigBird's forward replaces its attention modules with full attention when the
    sequence is too short for its block-sparse pattern -- a module created in the
    middle of a trace, which `fx` cannot place. The condition depends only on the
    sequence length, so it is decided here, the same way, and the trace then sees
    the modules the forward would have used.
    """
    for m in model.modules():
        if getattr(m, "attention_type", None) != "block_sparse" or \
                not hasattr(m, "set_attention_type") or not hasattr(m, "config"):
            continue
        cfg = m.config
        seq = None
        for a in example_args:
            if isinstance(a, torch.Tensor) and a.dim() >= 2:
                seq = a.shape[1]
                break
        if seq is None:
            continue
        if seq <= (5 + 2 * cfg.num_random_blocks) * cfg.block_size:
            m.set_attention_type("original_full")
