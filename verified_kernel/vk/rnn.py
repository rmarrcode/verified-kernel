"""Lowering `nn.LSTM` and `nn.GRU` as certified loops.

A recurrent layer is the same few operations at every time step, each reading the
state the step before wrote. Unrolled, a six-layer LSTM over 512 steps is thousands
of stages; here each layer and direction is

  1. a *projection* stage: the input's contribution to every gate at every step,
     `P[t, b, o] = sum_k x[t, b, k] W_ih[o, k] + b_ih[o]` -- one ordinary reduction
     over the whole sequence, since it does not depend on the state;
  2. an *initial state* stage, laying out `h0` (and `c0`) as the loop's state;
  3. a *recurrence* (`Recur.lean`): a short body chain run `T` times, reading the
     state and the step's window of `P`, writing the next state. The loop's output
     is the whole history of states, `(T+1) * S` elements.

The next layer's projection, and the module's outputs, are read out of the
histories by index maps. A reverse direction is a forward loop over the reversed
projection, `P[t] = x[T-1-t] ...`, and its history is read back reversed.

The body is limited by one fact about the reducing family: a stage reads each
buffer at a single index map. So the gates are separate stages -- each a reduction
over the hidden state, with its activation and the projection added in `post` -- and
a last stage combines them into the next state. PyTorch's definitions, per step:

  LSTM  i, f, g, o = σ, σ, tanh, σ of (P + h W_hh^T + b_hh), gate by gate
        c' = f c + i g ;  h' = o tanh(c')          state = [h ; c]
  GRU   r = σ(P_r + h W_hr^T + b_hr) ;  z = σ(P_z + h W_hz^T + b_hz)
        n = tanh(P_n + r (h W_hn^T + b_hn)) ;  h' = (1 - z) n + z h     state = h
"""

from __future__ import annotations

from fractions import Fraction
from typing import Any, Dict, List, Optional, Tuple

import torch.nn as nn

from . import ie as I
from . import se as S
from .frontend import NO_IDX_SLOT, Lowered, Unsupported, _prod

RNN_MODULES = (nn.LSTM, nn.GRU)


def rnn_param_names(m: nn.Module) -> List[str]:
    names = []
    for l in range(m.num_layers):
        for d in range(2 if m.bidirectional else 1):
            sfx = f"l{l}" + ("_reverse" if d else "")
            names += [f"weight_ih_{sfx}", f"weight_hh_{sfx}"]
            if m.bias:
                names += [f"bias_ih_{sfx}", f"bias_hh_{sfx}"]
    return names


def _check(m: nn.Module) -> None:
    if getattr(m, "proj_size", 0):
        raise Unsupported("LSTM with proj_size")
    if m.training and m.dropout and m.num_layers > 1:
        raise Unsupported("recurrent dropout in training mode")


def _pad(entries: Dict[int, I.IE], n: int) -> List[I.IE]:
    return [entries.get(b, I.Lit(0)) for b in range(n)]


def _select(n: int, cases: List[Tuple[I.BE, S.SE]], offs: Dict[int, I.IE],
            post_offs: Dict[int, I.IE], shape, note: str, arg_index) -> Lowered:
    """A `K = len(cases)` stage where exactly one `k` owns each lane: `cases[k]`'s
    guard says which, and its expression is the value. `concat`'s device, used to
    write two things into one buffer or read one of several."""
    if len(cases) == 1:
        guard, body = cases[0]
        return Lowered(family="genred", body=body, arity=n, out_size=_prod(shape),
                       out_shape=tuple(shape), tensor_arg_index=list(arg_index), K=1,
                       offs=_pad(offs, n), post_offs=_pad(post_offs, n),
                       in_range=guard, post=S.Inp(0), notes=[note])
    islot = n
    k = I.Rk()
    live = I.any_of([I.all_of([I.eq(k, I.Lit(i)), g]) for i, (g, _) in enumerate(cases)])
    body = cases[-1][1]
    for i in range(len(cases) - 2, -1, -1):
        body = S.SelLe(S.Inp(islot), S.lit(i + Fraction(1, 2)), cases[i][1], body)
    return Lowered(family="genred", body=body, arity=n, out_size=_prod(shape),
                   out_shape=tuple(shape), tensor_arg_index=list(arg_index),
                   K=len(cases), offs=_pad(offs, n), post_offs=_pad(post_offs, n),
                   in_range=live, post=S.Inp(0), idx_slot=islot, notes=[note])


class RnnLowering:
    """The stages for one recurrent module call, emitted into a chain `ch`."""

    def __init__(self, ch, node, m: nn.Module, x_val, h0_val, c0_val, param_buf):
        _check(m)
        self.ch, self.m = ch, m
        self.lstm = isinstance(m, nn.LSTM)
        self.G = 4 if self.lstm else 3
        self.H = m.hidden_size
        self.L = m.num_layers
        self.D = 2 if m.bidirectional else 1
        self.bf = m.batch_first
        xs = tuple(x_val.shape)
        if len(xs) != 3:
            raise Unsupported(f"recurrent input of rank {len(xs)}")
        self.T, self.B = (xs[1], xs[0]) if self.bf else (xs[0], xs[1])
        self.I = xs[2]
        self.BH = self.B * self.H
        self.S = (2 if self.lstm else 1) * self.BH
        self.x, self.h0, self.c0 = x_val, h0_val, c0_val
        self.pb = param_buf                  # parameter name -> buffer
        self.hist: Dict[Tuple[int, int], int] = {}
        self.note = f"{type(m).__name__} L={self.L} D={self.D} T={self.T} B={self.B} H={self.H}"

    # -- helpers ----------------------------------------------------------------

    def _w(self, name: str, l: int, d: int) -> int:
        return self.pb(f"{name}_l{l}" + ("_reverse" if d else ""))

    def _hist_h(self, l: int, d: int, t: I.IE, b: I.IE, j: I.IE) -> I.IE:
        """Where the layer's `h` at *time* `t` lives in its history: state `t+1`
        of a forward loop, state `T-t` of a reverse one."""
        s = (t + I.Lit(1)) if d == 0 else (I.Lit(self.T) - t)
        return s * I.Lit(self.S) + b * I.Lit(self.H) + j

    # -- the stages ---------------------------------------------------------------

    def emit(self) -> None:
        for l in range(self.L):
            for d in range(self.D):
                p = self._projection(l, d)
                init = self._init(l, d)
                self.hist[(l, d)] = self._recur(l, d, p, init)

    def _projection(self, l: int, d: int) -> int:
        ch, T, B, G, H = self.ch, self.T, self.B, self.G, self.H
        if l > 0 and self.D == 2:
            return ch.emit(self._projection2(l, d), (T * B * G * H,)).buf
        GH = G * H
        q = I.Pid()
        t = q // I.Lit(B * GH)
        b = (q // I.Lit(GH)) % I.Lit(B)
        o = q % I.Lit(GH)
        ts = t if d == 0 else I.Lit(T - 1) - t      # the source time step
        k = I.Rk()
        n = ch.nbuf + 1
        wih = self._w("weight_ih", l, d)
        if l == 0:
            Kin = self.I
            xi = ((b * I.Lit(T) + ts) if self.bf else (ts * I.Lit(B) + b)) * I.Lit(Kin) + k
            src = self.x.buf
            offs = {src: xi}
        else:
            # the layer below's `h` at this time step
            Kin = H
            src = self.hist[(l - 1, 0)]
            offs = {src: self._hist_h(l - 1, 0, ts, b, k)}
        offs[wih] = o * I.Lit(Kin) + k
        post, post_offs = self._bias_post(l, d, o)
        st = Lowered(family="genred", body=S.Inp(src) * S.Inp(wih), arity=n,
                     out_size=T * B * GH, out_shape=(T * B * GH,),
                     tensor_arg_index=list(ch.arg_index), K=Kin, offs=_pad(offs, n),
                     post_offs=_pad(post_offs, n), post=post,
                     notes=[f"{self.note}: layer {l} dir {d} input projection"])
        return ch.emit(st, (T * B * GH,)).buf

    def _bias_post(self, l: int, d: int, o: I.IE):
        """`+ b_ih[o]`, and for an LSTM `+ b_hh[o]` too: both of its biases add
        straight into every gate, where a GRU's `b_hn` sits inside `r * (...)`."""
        post: S.SE = S.Inp(0)
        post_offs: Dict[int, I.IE] = {}
        if self.m.bias:
            bih = self._w("bias_ih", l, d)
            post_offs[bih] = o
            post = post + S.Inp(bih + 1)
            if self.lstm:
                bhh = self._w("bias_hh", l, d)
                post_offs[bhh] = o
                post = post + S.Inp(bhh + 1)
        return post, post_offs

    def _projection2(self, l: int, d: int) -> Lowered:
        """A bidirectional layer above the first reads both directions of the layer
        below. Its input feature `k` is forward `h` for `k < H` and backward `h`
        after; summing both halves in one reduction over `k < H` keeps one index map
        per buffer."""
        ch, T, B, G, H = self.ch, self.T, self.B, self.G, self.H
        GH = G * H
        q = I.Pid()
        t = q // I.Lit(B * GH)
        b = (q // I.Lit(GH)) % I.Lit(B)
        o = q % I.Lit(GH)
        ts = t if d == 0 else I.Lit(T - 1) - t
        k = I.Rk()
        n = ch.nbuf + 1
        wih = self._w("weight_ih", l, d)
        hf, hb = self.hist[(l - 1, 0)], self.hist[(l - 1, 1)]
        # W_ih is (GH, 2H): column `k < H` weighs forward `h[k]`, column `H + k`
        # backward `h[k]`. The reduction runs over all 2H columns, reads both
        # directions at `k mod H`, and the body keeps the one the column belongs to.
        kk = k % I.Lit(H)
        offs = {hf: self._hist_h(l - 1, 0, ts, b, kk),
                hb: self._hist_h(l - 1, 1, ts, b, kk),
                wih: o * I.Lit(2 * H) + k}
        # `k` runs over 2H; the body picks the direction the column belongs to
        islot = n
        body = S.SelLe(S.Inp(islot), S.lit(H - Fraction(1, 2)),
                       S.Inp(hf), S.Inp(hb)) * S.Inp(wih)
        post, post_offs = self._bias_post(l, d, o)
        return Lowered(family="genred", body=body, arity=n, out_size=T * B * GH,
                       out_shape=(T * B * GH,), tensor_arg_index=list(ch.arg_index),
                       K=2 * H, offs=_pad(offs, n), post_offs=_pad(post_offs, n),
                       post=post, idx_slot=islot,
                       notes=[f"{self.note}: layer {l} dir {d} input projection "
                              "from both directions below"])

    def _init(self, l: int, d: int) -> int:
        ch, BH = self.ch, self.BH
        idx = l * self.D + d
        n = ch.nbuf + 1
        q = I.Pid()
        if self.h0 is None:
            raise Unsupported("recurrent module called without an initial state")
        if not self.lstm:
            st = Lowered(family="genred", body=S.Inp(self.h0.buf), arity=n,
                         out_size=BH, out_shape=(BH,), tensor_arg_index=list(ch.arg_index),
                         K=1, offs=_pad({self.h0.buf: I.mk_add(q, I.Lit(idx * BH))}, n),
                         post_offs=_pad({}, n), post=S.Inp(0),
                         notes=[f"{self.note}: initial state of layer {l} dir {d}"])
            return ch.emit(st, (BH,)).buf
        if self.c0 is None:
            raise Unsupported("LSTM called without c0")
        r = q % I.Lit(BH)
        st = _select(
            n, [(I.lt(q, I.Lit(BH)), S.Inp(self.h0.buf)),
                (I.le(I.Lit(BH), q), S.Inp(self.c0.buf))],
            {self.h0.buf: I.mk_add(r, I.Lit(idx * BH)),
             self.c0.buf: I.mk_add(r, I.Lit(idx * BH))}, {}, (2 * BH,),
            f"{self.note}: initial [h; c] of layer {l} dir {d}", ch.arg_index)
        return ch.emit(st, (2 * BH,)).buf

    def _recur(self, l: int, d: int, p: int, init: int) -> int:
        """The loop. Its body is numbered locally -- state at `L0`, the projection
        window at `L0 + 1`, body stages after -- and renumbered above every outer
        buffer once the chain is complete (`finish_recur`)."""
        ch, T, B, G, H, BH = self.ch, self.T, self.B, self.G, self.H, self.BH
        L0 = ch.nbuf + 1                 # the loop itself will write ch.nbuf
        stv, pv = L0, L0 + 1
        GH = G * H
        whh = self._w("weight_hh", l, d)
        bhh = self._w("bias_hh", l, d) if self.m.bias else None
        body: List[Lowered] = []
        sizes: List[int] = []

        def own(i: int) -> int:           # the buffer body stage i writes
            return L0 + 2 + i

        q = I.Pid()
        bq, jq = q // I.Lit(H), q % I.Lit(H)
        k = I.Rk()

        def gate(g: int, act, extra=None) -> Lowered:
            """`act(h . W_hh[g] + P[g] (+ ...))`, one lane per (b, j)."""
            n = own(len(body)) + 1
            offs = {stv: bq * I.Lit(H) + k, whh: (I.Lit(g * H) + jq) * I.Lit(H) + k}
            post_offs = {pv: bq * I.Lit(GH) + I.Lit(g * H) + jq}
            pre = S.Inp(0)
            if bhh is not None and not self.lstm:
                post_offs[bhh] = I.mk_add(jq, I.Lit(g * H))
                pre = pre + S.Inp(bhh + 1)
            if extra is None:
                post = act(pre + S.Inp(pv + 1))
            else:
                post = extra(pre, post_offs)
            return Lowered(family="genred", body=S.Inp(stv) * S.Inp(whh), arity=n,
                           out_size=BH, out_shape=(BH,),
                           tensor_arg_index=list(ch.arg_index), K=H,
                           offs=_pad(offs, n), post_offs=_pad(post_offs, n), post=post,
                           notes=[f"{self.note}: layer {l} dir {d} gate {g}"])

        if self.lstm:
            acts = [S.sigmoid, S.sigmoid, S.tanh, S.sigmoid]     # i, f, g, o
            for g in range(4):
                body.append(gate(g, acts[g])); sizes.append(BH)
            gi, gf, gg, go = (own(i) for i in range(4))
            n = own(4) + 1
            r = q % I.Lit(BH)
            c = S.Inp(gf) * S.Inp(stv) + S.Inp(gi) * S.Inp(gg)
            h = S.Inp(go) * S.tanh(c)
            st = _select(n, [(I.lt(q, I.Lit(BH)), h), (I.le(I.Lit(BH), q), c)],
                         {gi: r, gf: r, gg: r, go: r, stv: I.mk_add(r, I.Lit(BH))}, {},
                         (2 * BH,), f"{self.note}: layer {l} dir {d} next [h; c]",
                         ch.arg_index)
            body.append(st); sizes.append(2 * BH)
        else:
            body.append(gate(0, S.sigmoid)); sizes.append(BH)       # r
            body.append(gate(1, S.sigmoid)); sizes.append(BH)       # z
            rb = own(0)

            def n_gate(pre, post_offs):
                post_offs[rb] = q
                return S.tanh(S.Inp(pv + 1) + S.Inp(rb + 1) * pre)
            body.append(gate(2, None, n_gate)); sizes.append(BH)    # n
            zb, nb = own(1), own(2)
            n = own(3) + 1
            hnew = (S.lit(1) - S.Inp(zb)) * S.Inp(nb) + S.Inp(zb) * S.Inp(stv)
            body.append(Lowered(family="genred", body=hnew, arity=n, out_size=BH,
                                out_shape=(BH,), tensor_arg_index=list(ch.arg_index),
                                K=1, offs=_pad({zb: q, nb: q, stv: q}, n),
                                post_offs=_pad({}, n), post=S.Inp(0),
                                notes=[f"{self.note}: layer {l} dir {d} next h"]))
            sizes.append(BH)

        S_ = self.S
        low = Lowered(family="recur", body=S.Inp(0), arity=ch.nbuf + 1,
                      out_size=(T + 1) * S_, out_shape=((T + 1) * S_,),
                      tensor_arg_index=list(ch.arg_index),
                      recur={"T": T, "S": S_, "init": init, "views": [(p, B * GH)],
                             "body": body, "body_sizes": sizes, "L0": L0},
                      notes=[f"{self.note}: layer {l} dir {d} recurrence, {T} steps"])
        return ch.emit(low, ((T + 1) * S_,)).buf

    # -- the module's results -----------------------------------------------------

    def output(self) -> Tuple[Lowered, Tuple[int, ...]]:
        """The top layer's `h` at every time step, directions side by side."""
        ch, T, B, H, D = self.ch, self.T, self.B, self.H, self.D
        shape = (B, T, D * H) if self.bf else (T, B, D * H)
        q = I.Pid()
        j = q % I.Lit(H)
        dd = (q // I.Lit(H)) % I.Lit(D) if D > 1 else I.Lit(0)
        bt = q // I.Lit(D * H)
        t, b = ((bt % I.Lit(T), bt // I.Lit(T)) if self.bf
                else (bt // I.Lit(B), bt % I.Lit(B)))
        n = ch.nbuf + 1
        cases, offs = [], {}
        for d in range(D):
            hb = self.hist[(self.L - 1, d)]
            offs[hb] = self._hist_h(self.L - 1, d, t, b, j)
            cases.append((I.eq(dd, I.Lit(d)) if D > 1 else I.TT(), S.Inp(hb)))
        return _select(n, cases, offs, {}, shape, f"{self.note}: output sequence",
                       ch.arg_index), shape

    def final(self, which: int) -> Tuple[Lowered, Tuple[int, ...]]:
        """`h_n` (`which = 0`) or `c_n` (`which = 1`): every layer and direction's
        state after the last step."""
        ch, T, B, H = self.ch, self.T, self.B, self.H
        LD = self.L * self.D
        shape = (LD, B, H)
        q = I.Pid()
        ld = q // I.Lit(self.BH)
        r = q % I.Lit(self.BH)
        n = ch.nbuf + 1
        cases, offs = [], {}
        for l in range(self.L):
            for d in range(self.D):
                hb = self.hist[(l, d)]
                offs[hb] = I.mk_add(r, I.Lit(T * self.S + which * self.BH))
                cases.append((I.eq(ld, I.Lit(l * self.D + d)), S.Inp(hb)))
        return _select(n, cases, offs, {}, shape,
                       f"{self.note}: final {'h' if which == 0 else 'c'}",
                       ch.arg_index), shape


def finish_recur(st: Lowered, base: int, arity: int, outer_sizes: List[int],
                 outer_shapes) -> None:
    """Renumber a loop body above every outer buffer, and bound its reads."""
    from .graph import bound_stage, relocate
    R = st.recur
    L0 = R["L0"]
    nv = len(R["views"])
    nloc = 1 + nv + len(R["body"])
    bmap = {b: b for b in range(L0)}
    bmap.update({L0 + x: base + x for x in range(nloc)})
    body = []
    for i, b in enumerate(R["body"]):
        n = base + 1 + nv + i + 1
        islot = n if b.idx_slot != NO_IDX_SLOT else NO_IDX_SLOT
        rb = relocate(b, bmap, n, islot)
        rb.family = b.family
        rb.K = b.K
        body.append(rb)
    sizes = (list(outer_sizes) + [R["S"]] + [s for (_, s) in R["views"]]
             + list(R["body_sizes"]))
    shapes = list(outer_shapes) + [(x,) for x in sizes[len(outer_sizes):]]
    for rb in body:
        bound_stage(rb, arity, sizes, shapes)
    R["body"] = body
    R["base"] = base
    R["all_sizes"] = sizes
