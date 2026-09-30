"""Coding test: implement scaled dot-product attention and multi-head attention.

Fill in every function/method marked with `raise NotImplementedError`.
Do not change any signature, attribute name, or return type -- the tests in
`test_attention.py` depend on the exact contract described in each docstring.

Allowed: torch, torch.nn, torch.nn.functional (softmax, dropout, linear, matmul...).
Not allowed: torch.nn.MultiheadAttention, torch.nn.functional.scaled_dot_product_attention,
torch.nn.TransformerEncoderLayer, or any other prebuilt attention block. The point is
to write the math yourself.
"""

from __future__ import annotations

import math
from typing import Optional, Tuple

import torch
import torch.nn as nn
import torch.nn.functional as F


# ---------------------------------------------------------------------------
# Part 1 -- scaled dot-product attention
# ---------------------------------------------------------------------------
def scaled_dot_product_attention(
    query: torch.Tensor,
    key: torch.Tensor,
    value: torch.Tensor,
    mask: Optional[torch.Tensor] = None,
    dropout_p: float = 0.0,
    is_causal: bool = False,
) -> Tuple[torch.Tensor, torch.Tensor]:
    """Compute softmax(QK^T / sqrt(d_k)) V.

    Args:
        query: (*batch, Lq, d_k) -- `*batch` is any number of leading dims (0, 1, 2, ...).
        key:   (*batch, Lk, d_k)
        value: (*batch, Lk, d_v)
        mask:  optional bool tensor broadcastable to (*batch, Lq, Lk).
               `True` means "this key IS allowed to be attended to",
               `False` means "mask this position out".
               (Note: this is F.scaled_dot_product_attention's convention, and the
               *opposite* of nn.MultiheadAttention's `attn_mask`. Getting this
               backwards is the single most common bug in this exercise.)
        dropout_p: dropout probability applied to the attention *weights*
               (after softmax, before multiplying by value). Always applied in
               training mode -- pass 0.0 to disable.
        is_causal: if True, additionally forbid each query position i from
               attending to any key position j > i (upper triangle, strictly
               above the diagonal, is masked). Combines with `mask` via AND.

    Returns:
        (output, attn_weights)
          output:       (*batch, Lq, d_v)
          attn_weights: (*batch, Lq, Lk), post-softmax, pre-dropout, non-negative,
                        each row summing to 1.

    Requirements:
      * Must not modify `query`, `key`, or `value` in place.
      * Must be numerically safe for large logits (use a proper masked fill with
        -inf / a large negative number, not multiplication by 0).
      * Must be differentiable end to end.
    """
    raise NotImplementedError("implement scaled_dot_product_attention")


# ---------------------------------------------------------------------------
# Part 2 -- multi-head attention
# ---------------------------------------------------------------------------
class MultiHeadAttention(nn.Module):
    """Multi-head attention, batch-first.

    Parameter contract (the tests read these attributes by name, and load their
    weights into a reference `nn.MultiheadAttention` to check you numerically):

        self.w_q: nn.Linear(d_model, d_model, bias=bias)
        self.w_k: nn.Linear(d_model, d_model, bias=bias)
        self.w_v: nn.Linear(d_model, d_model, bias=bias)
        self.w_o: nn.Linear(d_model, d_model, bias=bias)

    Head layout: after projecting to (B, L, d_model), head `h` owns the
    contiguous slice `[h * d_head : (h + 1) * d_head]` of the feature dim.
    (i.e. reshape to (B, L, num_heads, d_head), then transpose to
    (B, num_heads, L, d_head) -- do NOT split the feature dim the other way.)
    """

    def __init__(
        self,
        d_model: int,
        num_heads: int,
        dropout: float = 0.0,
        bias: bool = True,
    ) -> None:
        """Set up the four projections.

        Must raise ValueError if `d_model` is not divisible by `num_heads`.
        Store `d_model`, `num_heads`, `d_head` (= d_model // num_heads) and
        `dropout` as attributes.
        """
        super().__init__()
        raise NotImplementedError("implement MultiHeadAttention.__init__")

    def _split_heads(self, x: torch.Tensor) -> torch.Tensor:
        """(B, L, d_model) -> (B, num_heads, L, d_head)."""
        raise NotImplementedError("implement MultiHeadAttention._split_heads")

    def _merge_heads(self, x: torch.Tensor) -> torch.Tensor:
        """(B, num_heads, L, d_head) -> (B, L, d_model). Inverse of _split_heads."""
        raise NotImplementedError("implement MultiHeadAttention._merge_heads")

    def forward(
        self,
        query: torch.Tensor,
        key: torch.Tensor,
        value: torch.Tensor,
        mask: Optional[torch.Tensor] = None,
        is_causal: bool = False,
    ) -> Tuple[torch.Tensor, torch.Tensor]:
        """Run multi-head attention.

        Args:
            query: (B, Lq, d_model)
            key:   (B, Lk, d_model)
            value: (B, Lk, d_model)   -- same length as key; cross-attention means Lk != Lq
            mask:  optional bool tensor, `True` = keep, broadcastable to
                   (B, num_heads, Lq, Lk). Callers commonly pass:
                     (Lq, Lk)          a shared attention mask
                     (B, 1, 1, Lk)     a key-padding mask
                     (B, 1, Lq, Lk)    a per-example mask
                   Your code should broadcast, not assume one specific rank.
            is_causal: as in `scaled_dot_product_attention`.

        Returns:
            (output, attn_weights)
              output:       (B, Lq, d_model)
              attn_weights: (B, num_heads, Lq, Lk) -- per head, NOT averaged.

        Dropout must respect `self.training` (active in train mode, off in eval).
        Reuse `scaled_dot_product_attention` above rather than reimplementing it.
        """
        raise NotImplementedError("implement MultiHeadAttention.forward")


# ---------------------------------------------------------------------------
# Part 3 (bonus) -- incremental decoding with a KV cache
# ---------------------------------------------------------------------------
class CachedSelfAttention(MultiHeadAttention):
    """Causal self-attention that supports one-token-at-a-time decoding.

    Bonus round. The tests for this part only run with `pytest -m bonus`.
    """

    def forward_step(
        self,
        x: torch.Tensor,
        cache: Optional[Tuple[torch.Tensor, torch.Tensor]] = None,
    ) -> Tuple[torch.Tensor, Tuple[torch.Tensor, torch.Tensor]]:
        """Attend a single new timestep against all previous ones.

        Args:
            x: (B, 1, d_model) -- the new token's hidden state.
            cache: optional (k_cache, v_cache), each (B, num_heads, L_past, d_head),
                   as returned by the previous call. None on the first step.

        Returns:
            (output, new_cache)
              output:    (B, 1, d_model)
              new_cache: (k_cache, v_cache) each (B, num_heads, L_past + 1, d_head)

        Feeding a sequence through one step at a time must produce exactly the
        same outputs as one `forward` call over the whole sequence with
        `is_causal=True`.
        """
        raise NotImplementedError("bonus: implement CachedSelfAttention.forward_step")

