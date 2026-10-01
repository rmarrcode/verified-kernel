# Status

Measured numbers come from `python harness/run_all.py`; the run summary it prints
is the source of truth. This file records what is built, what is not, and the
design problems standing between the measured numbers and the whole benchmark.

## Measured (RTX 4070, 12GB; torch 2.14, triton 3.8, Lean 4.34.1)

| Level | Tasks | Lowered | Certified by Lean | Matched | Matched, fp32 reference |
|---|---|---|---|---|---|
| 1 — single operators | 100 | 100 | **100** | **100** | 100 |
| 2 — fused chains | 100 | 100 | **100** | **99-100** † | 100 |
| 3 — whole architectures | 50 | **49** | **49** | **42** | **44** |
| 4 — HuggingFace models | 20 | **19** | **19** | **10** ‡ | 10 |
| **total** | **270** | **268** | **268** | **251-252** | **254** |

‡ Six more Level 4 tasks are certified but cannot run on this card at any size: the
three gpt-neo-2.7B tasks (10.6GB of weights), and three whose attention scores,
summed over their layers, do not fit even at batch one. Of Level 3's remaining
seven, four are ill-conditioned problems, two are the TF32 cases below, and one
does not fit; Level 4's three mismatches are references measurably further from
the float64 truth than the kernel. See *The mismatches that are not defects*.

Each level was measured in its own run of `run_all.py`, in the order 3, 1, 2, 4.
Level 2 needed a second run after a frontend fix -- see *A wrong spec caught by its
shape* -- and Level 4 its final run after two harness fixes.

The last column runs the reference at full float32 rather than PyTorch's default
TF32; see *The reference's precision* below for why the two differ and why both are
reported. † One Level 2 task sits on the tolerance boundary and fails
intermittently -- twice in three full runs. It is not a defect in the kernel (see
below), but the Level 2 figure is 99 or 100 depending on the draw, and quoting 100
without that qualification would be picking the good run.

Levels 1 and 2 are complete: every task lowers to a formal specification, carries a
Lean-checked correctness certificate, and matches PyTorch under KernelBench's own
criterion (5 trials, `allclose` at 1e-2). Of the 270 tasks, two do not lower: Level
3's task 35, whose forward draws `torch.randn` (there is no function to specify),
and Level 4's block-sparse BigBird (task 5), which writes into module state in
place.

One caveat on Level 2's hundredth, because it is a coin-flip rather than a pass: task
14 fails intermittently, and it is not a defect in the kernel. It is a
1024x8192 by 8192x8192 product, halved, then
summed along the row -- 67 million products per output, with outputs of magnitude
~2600. Measured against a float64 ground truth over the whole output:

| | max error vs float64 |
|---|---|
| this kernel | 2.0e-3 |
| PyTorch, TF32 off | 1.9e-2 |
| PyTorch, TF32 on (its default on this card) | 3.1 |

The kernel is the more accurate of the two. It fails anyway, intermittently, and
always the same way: some row's 8192 terms cancel down to a value near zero, and
`allclose`'s absolute term is then the binding one. On the draw sampled here the true
value was 0.4291, PyTorch gave 0.4451 (off by 1.6e-2, past the 1e-2 floor) and the
kernel gave 0.4290 -- off by 1.15e-4, **140 times closer to the truth than the
reference it is being checked against**.

Nothing here can be fixed by proving more, and the criterion is KernelBench's own, so
it is reported as a failure rather than argued away. It is the rounding gap the
trusted base already names -- the theorem is over an exact ordered field -- showing
up from the unexpected direction: not the kernel drifting from the reference, but the
reference drifting from the mathematics both of them are approximating.

Certificates depend only on `propext`, `Quot.sound` and `Classical.choice`; there is
no `sorryAx`. Spot-checked on the hardest cases -- ResNet101 (454 stages), DenseNet121
(concatenations throughout), and an Inception module:

```
't006_correct' depends on axioms: [propext, Classical.choice, Quot.sound]
't010_correct' depends on axioms: [propext, Classical.choice, Quot.sound]
't015_correct' depends on axioms: [propext, Classical.choice, Quot.sound]
```

One caveat on reproducing this: `Generated/Emit.lean` holds only the most recent
*round* of a run, since a retry at a reduced size rewrites it. The certificates were
checked when written, but to inspect one afterwards it has to be regenerated. Check
it with:

```bash
cd lean && echo 'import Generated.Emit
#print axioms t001_correct' > /tmp/ax.lean && lake env lean /tmp/ax.lean
```

Note on performance: these kernels are correctness-first, not tuned. The reducing
family runs one program per output element with no data reuse, so a large
contraction is orders of magnitude off cuBLAS. KernelBench also scores speedup; that
is not attempted here.

## Why not 270

A perfect score was looked for, and on this machine there is none to be had without
making the kernel something other than the verified kernel. What stands between
the measured total and 270 falls in exactly two kinds, and neither is a kernel
defect or a missing operator:

**The reference is not the mathematics, and cannot be reproduced.** ResNet101,
MobileNetV2, UNet, EfficientNetB2, both Mamba2 tasks, BART and OPT: in each the
PyTorch reference is measurably further from a float64 ground truth than the
kernel is, or no float32 computation is close (*The mismatches that are not
defects*). Matching such a reference means reproducing its rounding, not its
arithmetic. That was tried in the one place it looked possible -- cuDNN computes
convolutions in TF32, and rounding a convolution's operands to TF32 before an exact
float32 convolution is cheap to emulate. Measured, in PyTorch, on the four
convolutional networks:

| | emulated TF32 vs the TF32 reference | plain float32 vs the TF32 reference |
|---|---|---|
| ResNet101 | 0.20 (round-to-nearest) - 0.24 (truncate) | 0.13 |
| MobileNetV2 | 0.042 - 0.044 | 0.023 |
| UNetSoftmax | 0.10 - 0.32 | 0.063 |
| EfficientNetB2 | 1.0 - 1.5 | 1.4 |

Emulation lands *further* from the reference than plain float32, under every
rounding mode: cuDNN's TF32 kernels round inside their own accumulation, in an
order nothing outside them can see. The remaining ways to match are to call
PyTorch from inside the kernel or to loosen the tolerance, and either would make
the score stop meaning what it says.

**The card is too small.** gpt-neo-2.7B's weights are 10.6GB in float32 -- the
reference alone does not fit in the ~10GB this 12GB card has free, before any
kernel runs.

Everything else that was blocking has been fixed (*Getting to the ceiling*, below),
which puts the ceiling on this machine at 100 + 100 + 44 + 11 = 255, with Level 2's
task 14 a coin-flip on the same terms as above.

## The reference's precision

Worth stating before the numbers, because it moves several of them. PyTorch defaults
to TF32 for convolutions and matrix products on this card -- 10 mantissa bits, not
24. These kernels compute in float32. So on a deep network the reference is the less
accurate of the two things being compared, and most of the measured difference is
its own:

| | max error vs the reference | vs the reference at full float32 |
|---|---|---|
| ResNet101 | 1.3e-1 (6576 elements fail) | 3.0e-4 (none fail) |
| MobileNetV2 | 2.1e-2 (384 fail) | 2.2e-5 (none fail) |

KernelBench does not disable TF32, so neither does the harness by default; both
numbers are reported, and `VK_FP32_REF=1` gives the second column.

## Softmax, and a gap the certificate cannot see

Worth recording as the clearest example of what a correctness certificate here does
and does not cover. Found by chasing an intermittent `nan` out of UNet.

PyTorch computes `softmax` as `exp(x - rowmax) / sum exp(x - rowmax)`. The lowering
computed `exp(x) / sum exp(x)`. Over an exact ordered field those are *the same
function* -- the shift cancels -- so the certificate was valid, and had nothing to
say about the difference. Over float32 they are not the same at all: `exp` overflows
above about 88, and the unshifted form then divides `inf` by `inf`. UNet's softmax
input measures max 62, min -80, moving by draw, which is why the `nan` appeared on
some runs and not others.

Now fixed, by shifting each row by its maximum, which costs a third stage and proves
nothing new: `MaxRed` supplies the row maximum, `three_stage` composes the three, and
`_emit_pipeline3` already dispatched per stage on its family, so a max first stage
alongside two sums needed no change to the emitter. Checked against PyTorch at an
input scale where the unshifted form yields 93 nans out of 512 and this yields none.

The lesson is the one the trusted base already states, in its sharpest form: these
theorems are over an exact ordered field, and *every* float question -- including
whether a value is representable at all -- lives outside them.

## Level 3, and what it cost

**The locality obligation was quadratic in the chain length.** `stages_correct` asks
each stage to prove it reads no intermediate buffer past what was written there. The
*theorem* is one fact per stage, but the generated *proof* enumerated every buffer in
the chain, discharging each by unfolding the size map. At Level 2, chains are 1 to 9
stages and that is nothing. Level 3 reaches **454 stages**, and the cost was
measurable: 61.6 MB of Lean for twelve tasks, with even ResNet18's 91 stages
exhausting the elaborator.

Three things fixed it, none of them assuming anything new:

  * An index map is a table of the buffers it actually indexes (`IE.sparse`), split
    at the chain's arity (`IE.split`). A locality obligation only ever fires at or
    above that line, so the half a stage reasons about holds its one or two real
    reads. The obvious version -- keying on how far a dense list extends -- does not
    help, because a linear chain still leaves one arm per buffer below that point.
  * Sizes are a list (`Sizes.ofList`), which makes "every recorded size is positive"
    one fact for the whole chain instead of a case inside every stage.
  * The three `∀ st ∈ chain, …` obligations were unfolding the stage list and
    `rcases`-ing an n-deep `Or`. Nesting `List.forall_mem_cons` is a linear term.

ResNet18 went from timing out to 4.4 seconds. ResNet101 -- 454 stages -- certifies,
and `#print axioms t010_correct` gives exactly `propext`, `Classical.choice` and
`Quot.sound`. `maxRecDepth` and `maxHeartbeats` are raised in the generated file:
both are budgets, not criteria, and the kernel still checks every term.

**Operator coverage.** Surveyed across all 50 tasks by asking, per task, which
*node* cannot be lowered -- rather than which family declined last, which is what the
error text says and is much less useful:

| Missing | Tasks it blocks | Status |
|---|---|---|
| `torch.cat` | 7 as the sole blocker | **done**, and without touching the IR |
| `transpose` / `permute` / `.T` | 3 | **done**, frontend only |
| `ReLU6` | 4 | **done**, one table entry |
| `nn.LSTM` / `nn.GRU` / `nn.RNN` | 8 | **done** since: a proved loop (*Recurrences*, below) |
| dynamic slicing on traced shapes | 3 | **done** since (*Level 3: what else it took*) |
| data-dependent control flow | 2 | **done** since: it was Swin's constructor, not its forward |
| `unfold`, `expand`, `TransformerEncoder` | 1 (task 28) | **done** since |
| `einsum` | 2 | **done** since: any number of operands is one contraction |

Three of these looked like they needed the IR extended and did not, which is the
pattern worth recording:

**`ReLU6`** is a `Hardtanh` by inheritance; the table was keyed on the exact type.

**A permutation** is a relabelling of the index map of the stage that *reads* the
result, so it is absorbed there and never materialised -- exactly the way `unsqueeze`
already was. The IR deliberately cannot express a reshape, and does not need to.

**Concatenation** is the interesting one, because it really looks like it needs a
per-slot guard: each output element comes from one of several inputs, and the
family's mask is shared across input slots, so a body that selected between them per
lane is not expressible. The way through is to take the reduced axis to run over the
*inputs*. Then `inRange` says which input owns the lane -- so exactly one `k`
contributes -- and `idxSlot`, which is already there to give an argmax its index,
hands the body `k` as a scalar so it can select that input's slot. Every other slot
is loaded and thrown away, which the shared mask makes unavoidable and which is
harmless: those reads are clamped into their own buffer. It is `GenRed` at the same
theorem as a convolution, and `GenRed.prog_implements` was not reopened.

The eight recurrent tasks looked like the hard floor, and were not; see below.

## Recurrences: one body, proved once

The eight recurrent tasks were the hard floor, and the reason was scale rather than
expressiveness: an LSTM step is four reductions and a pointwise update, all in the
reducing family, but unrolled over 512 steps and six layers it is thousands of
stages, each its own kernel and its own certificate. `Recur.lean` proves the loop
instead.

  * `GStage` generalises a stage from "a kernel" to "anything that computes one
    buffer", and `gstages_correct` is `stages_correct` over it -- the same
    induction. An ordinary stage is one (`GStage.ofStage`).
  * A `Recur` runs a body chain `T` times. Step `t` sees the state in one buffer
    and, in each view buffer, the window `src[t*stride ..]` of an outer buffer -- the
    step's slice of a precomputed input projection. The body's last stage writes
    the next state; the loop's output is the history, state `t` at offset `t*S`.
  * `Recur.impl`: the loop implements its specification, by induction on the step,
    from the body's own chain certificate. `Recur.spec_local`: it reads no outer
    buffer past what was written, so it sits in an outer chain like any stage.
    Every per-task side condition is decidable or `rfl`, and the certificates
    depend only on `propext`, `Classical.choice` and `Quot.sound`.

Per layer and direction the frontend (`vk/rnn.py`) emits a projection stage over the
whole sequence (the input's share of every gate, which does not depend on the
state), an initial-state stage, and the loop. A reverse direction is a forward loop
over the reversed projection, read back reversed. The body is shaped by one fact
about the family -- a stage reads each buffer at one index map -- so the gates are
separate reductions, each applying its activation and adding its slice of the
projection in `post`, and a last stage combines them. An LSTM's state is `[h ; c]`,
written by one stage through the same `concat` device as `torch.cat`.

What this adds to the trusted base is the launcher's loop (`Render3.lean`,
`ChainItem.call`): it runs the body's kernels `T` times, passing a *slice* of a
flat tensor for the state and for each view. That a slice at offset `o` reads
element `o + i` as its `i` is exactly `Recur.envAt`'s view.

One Lean detail cost a debugging round and is worth recording: the history's size is
a field, `H`, with `H = T * S + S` a side condition checked by `decide`. Stated as
the product, the certificate's `rfl` for the outer size map made Lean unfold the
multiplication one unit at a time -- it does not multiply `r.T * r.S` as numerals
even though each reduces to one -- and a state of 5120 elements overflowed the
kernel's recursion limit where GRU's 2560 had not.

## Level 3: what else it took

Surveyed per blocking *node*, as before:

| Was missing | Tasks | How |
|---|---|---|
| `nn.LSTM` / `nn.GRU` | 36-42 | **done**: `Recur`, above |
| Python loop over time, `torch.stack` | 34 | **done**: unrolled (1033 stages); `stack` is `cat` of unit axes |
| stateful `self.hidden` (`copy_`) | 33 | **done**: later reads redirected to the copied value |
| `nn.MultiheadAttention`, `TransformerEncoder(Layer)` | 28, 31, 32 | **done**: rewritten as their arithmetic, sharing the original parameters |
| `masked_fill(-inf)` before softmax / relu / exp | 43, 44, 48, 49, 50 | **done**: folded into the consumer (`rewrite_neg_inf`) |
| `unfold`, `expand`, `pad`, `roll`, `index` by a tensor | 28, 29, 30 | **done**: index maps; a gather is a masked sum |
| `einsum` (any operands), einops `rearrange` | 48, 49 | **done**: one contraction; `rearrange` traced as reshape/permute |
| constructor that calls `.item()` | 29, 30 | **done**: module built for real on the CPU, inputs fake |
| weights larger than the memory budget | 2 | **done**: weights are exact and shared, so they need no margin |
| `torch.randn` inside `forward` | 35 | **refused**: the reference is random, so there is no function to specify |

Two frontend rules introduced here deserve naming, since the frontend is where a
wrong lowering would go unnoticed by the proof:

**`-inf` is never a value.** The field the specs are stated over has no `-inf`, and
`masked_fill(x, m, -inf)` appears only as a device to make the *next* operator
ignore entries. It is folded into that operator: `relu` and `exp` of it become a
`where` with 0, and a softmax becomes `e / sum(e)` with `e = where(m, 0, exp(x -
c))`. The shift `c` cancels in exact arithmetic; it is chosen for the floats, as the
maximum over the *unmasked* entries (`max(where(m, rowmin, x))`), which is what
PyTorch uses. Any other consumer of a `-inf` fill is refused.

**Randomness is refused, not sampled.** A `torch.randn` inside a forward runs
eagerly during a trace with constant shapes, and the draw would have become a
constant of the spec -- a deterministic function the reference is not. Every
random factory now raises during tracing.

### The mismatches that are not defects

Three Level 3 tasks fail KernelBench's criterion for the same reason Level 2's task
14 does: the reference is further from the mathematics than the kernel, or no
float32 computation is close to it. Measured against a float64 ground truth:

| | ours vs float64 | PyTorch fp32 vs float64 | PyTorch default (TF32) vs float64 |
|---|---|---|---|
| EfficientNetB2 | 0.18 - 1.5 | 1.07 - 1.24 | 1.11 - 1.47 |
| UNetSoftmax | 7e-5 - 1.1e-2 | 3e-4 - 3.3e-2 | 0.08 - 0.98 |
| Mamba2ReturnY (outputs up to 1e22) | ~1.2% relative at the worst element | ~1-2% | 3e18 absolute |

EfficientNetB2 is ill-conditioned by construction: after its first block every
tensor is 1x1 spatial, so each train-mode BatchNorm normalises over the *two*
values of the batch, `(a - b) / sqrt((a - b)^2/4 + eps)`, which flips sign with the
rounding of `a - b`. Mamba2's outputs are exponentials of cumulative sums of
`randn` parameters. UNet is the TF32 case in its sharpest form: our kernel is closer
to float64 than PyTorch at full float32 on every trial.

## Level 4

`transformers` 5.18, with the checkpoints fetched from the HuggingFace hub. The same
compiler as Level 3, traced through the HuggingFace modules with the shape-aware
tracer; what Level 4 added was operators, not machinery:

| Needed | Models | How |
|---|---|---|
| `nn.Embedding`, `F.embedding`, `torch.gather`, `index_select` | all | a gather is a masked sum, with the index read as a value |
| `scaled_dot_product_attention` (causal, or with a mask) | gpt2, OPT, BART | rewritten as its definition; the causal mask becomes a `-inf` fill folded into the softmax |
| `addmm` | gpt2's `Conv1D` | one contraction, the weight read untransposed |
| `logsumexp`, `rsqrt`, `F.dropout` (off) | Reformer, BART | a max-shifted reduction; a reciprocal square root; the identity |
| an empty key/value cache concatenated on | gpt2, BART | an empty part contributes nothing to a `cat` |
| a forward that swaps its own attention module | BigBird | the swap is made before tracing, under the same condition |
| float16 weights | OPT | widened exactly to float32; the result rounded to the reference's dtype |

| Model | Tasks | Result |
|---|---|---|
| gpt2 | 7, 16, 19 | **matched** (16 at declared size) |
| electra-small | 11, 12, 14 | **matched** (11 at declared size) |
| bigbird-roberta-base, short sequences | 9, 10 | **matched**, reduced |
| reformer-enwik8 | 13, 15 | **matched**, reduced |
| bart-large | 6, 17, 20 | 6 does not fit; 17 and 20 mismatch, the reference being the less accurate |
| opt-1.3b | 2, 4, 8 | 2 and 4 do not fit; 8 mismatches, the reference being the less accurate |
| gpt-neo-2.7B | 1, 3, 18 | certified; weights exceed this card |
| bigbird, block-sparse | 5 | not lowered |

Against a float64 ground truth (`max |diff|`, one batch):

| | ours | PyTorch, as the benchmark runs it |
|---|---|---|
| bart-large, bs32 seq256 | 5.4e-2 | 1.4 |
| bart-large, bs1024 seq32 | 5.6e-2 - 6.1e-2 | 7.6 - 35 |
| opt-1.3b (a float16 checkpoint), bs512 seq32 | 6.3e-3 - 6.9e-3 | 5.5e-2 - 6.2e-2 |

BART-large's activations carry large outliers, so a float32 `q . k` sums large terms
that cancel; PyTorch's result moves by whole units in the logits. OPT's reference
computes in float16. In both the kernel, computing in float32, is an order of
magnitude or more closer to the mathematics than what it is checked against.

### Two bugs Level 4 found, neither visible to a proof

**`cat([h, h])`.** A stage reads each buffer at one index map, and concatenation kept
its maps in a table keyed by buffer -- so a tensor joined to itself, Reformer's
reversible residual, had its second part's map silently replace the first's. Every
stage was still certified, against a spec that was not the model's. Found by
`harness/stagechk.py`, which runs the traced, rewritten graph on real tensors and
compares each stage's buffer to its node. A repeat now gets a copy of its own, and
`relocate` refuses any two operands that would read one buffer through different
maps.

**The memory plan ignored intermediates.** It counted inputs, output and weights,
while the launcher allocates every intermediate up front. Reformer at batch 1024
broadcasts its axial position table to the whole batch before selecting 32
positions -- an intermediate of 1.7e10 elements. Intermediates now count, which is
what moves several Level 4 tasks to a reduced size and three to "does not fit".

### A wrong spec caught by its shape

The single-operator pointwise table read `torch.max(x, 1)` -- a reduction over axis
one -- as the elementwise maximum of `x` and the constant 1. The `logsumexp` rewrite
produced exactly that call; over an axis of extent one the shapes agree, so the
pointwise family accepted it, and two Level 2 tasks stopped lowering only because
that family cannot sit in a chain. An integer second argument to `max`/`min` is now
always a dimension.

## Built

**Verified core** (`lean/`, no `sorry` and no `native_decide`; generated certificates
depend only on `propext`, `Quot.sound` and `Classical.choice`):

| File | What it establishes |
|---|---|
| `Scalar.lean` | the abstract ordered field; `sum_comm`, `sum_mul_split`, masking, and the max-fold characterisation (upper bound, and attained) |
| `Ir.lean` | `TritonIR` syntax and denotational semantics |
| `Coverage.lean` | every output written exactly once, by the lane that computed it |
| `AccFree.lean` | a loop's summand cannot see the accumulator |
| `Loop.lean` | a blocked masked accumulator equals a contiguous fold |
| `Emit.lean` | translation to a rank-annotated target language, denotation-preserving |
| `Render.lean`, `Render3.lean` | target language to Triton text (**trusted**, one template per node) |
| `Kernels/Elementwise.lean` | `SE.flat_correct` |
| `Kernels/GenRed.lean` | `GenRed.prog_implements` — the general reducing family |
| `Kernels/MaxRed.lean` | `MaxRed.prog_implements` — clamping rather than masking |
| `Kernels/ProdRed.lean` | `ProdRed.prog_implements` — the same, multiplicatively |
| `Pipeline.lean`, `Pipeline3.lean` | `two_stage`, `three_stage`, and the `Loc` obligations |
| `Stages.lean` | `stages_correct` -- a chain of any length, with linear locality obligations |
| `Recur.lean` | `gstages_correct`, `Recur.impl`, `Recur.spec_local` -- a body chain run `T` times |

**Families and what they cover:**

| Family | Theorem | Tasks |
|---|---|---|
| general reduction | `GenRed.prog_implements` | 56 |
| element-wise | `SE.flat_correct` | 14 |
| three-stage pipeline | `three_stage` | 13 |
| two-stage pipeline | `two_stage` | 10 |
| max/min reduction | `MaxRed.prog_implements` | 5 |
| composed max (argmax) | `two_stage` over `MaxRed` | 2 |

Covering: 34 convolutions, 18 contractions, 14 activations, 8 normalisations, 7
reductions, 6 losses, 6 poolings, 5 scans, attention, and the rest.

**Pipeline** (`verified_kernel/vk/`, `harness/`): fx-based frontend, Lean certificate
generator, Triton runtime, subprocess-isolated orchestrator, and
`harness/axiom_tests.py` validating the trusted Triton model.

Each task compiles to a `theorem` in `lean/Generated/Emit.lean` instantiating its
family's theorem at the chosen block size and grid; `lake build` checking that file
is the gate on emission.

## What is not proved

### Rounding
Certificates state equivalence **in exact arithmetic**. That this implies agreement
within KernelBench's 1e-2 is empirical -- every kernel that has run has matched --
not proved. A bound would need a Flocq-style IEEE-754 development, which does not
exist usably for Lean 4. This is the single largest remaining gap in the guarantee.

### The frontend
There is no formal semantics of PyTorch to prove the lowering against, so a
mis-lowering produces a kernel provably equal to the *wrong* spec. It is written to
refuse rather than guess, but that is a discipline, not a proof. Both real bugs
found this way lived here:

- clamping a pooling *coordinate* is sound only for an undilated window; with
  dilation the window is a strided set (tasks 41, 43);
- ignoring an `unsqueeze` silently transposed a broadcast (task 12).

Neither was catchable by proof. Running the kernels is what found them. Two more of
the same kind turned up in Level 3's second pass, both caught before they shipped:

- `x[0]` on a tensor was treated as "field 0 of a `(values, indices)` pair" and
  aliased to `x` -- it is a slice, and drops an axis;
- a `torch.randn` inside a forward was evaluated once at trace time and would have
  become a constant of the spec. Random factories now refuse during tracing.

### The trusted last mile
`Render.lean` (one string template per node), the modelled `tl.*` semantics
(differential-tested by `harness/axiom_tests.py`), the Lean kernel, and Triton's
own compiler. Since the recurrences, also the launcher's loop in `Render3.lean`: that
a slice of a flat tensor at offset `o` reads element `o + i` as its `i`, which is
what `Recur.envAt` assumes of a view.

## Design notes worth keeping

Three things initially looked like they needed IR extensions and did not. Recording
them because the instinct to extend the IR was wrong each time:

- **A gather is a masked sum.** `x[i,label] = sum_j x[i,j] * [j = label]`, and
  `[j = label]` compares two *values* -- the label read as an ordinary element,
  against the reduction index. So `IE.qkOnly` can keep forbidding data-dependent
  index maps, which is what makes `instK_eval` and every tiling argument true.
- **A scan is three reductions.** Block sums, a prefix over blocks, an intra-block
  prefix. Work drops from `K^2` to `K*block + (K/block)^2` per row -- 7e10
  operations rather than 3.5e13.
- **Attention is three contractions.** The scores must be materialised, since a
  score is itself a reduction and this family has one reduction level.

And two traps:

- **Do not add a bottom element to the scalar field** to make `max` work.
  `le bot a` for every `a` plus the field axioms gives `bot <= bot - 1 < bot`; the
  axioms become inconsistent and every theorem turns *vacuous* rather than failing.
  `MaxRed` clamps its index maps instead. A product needs no such manoeuvre, because
  it has an identity -- which is why `ProdRed` can mask like the additive family.
- **Generated proof terms must supply every implicit argument.** Left to inference
  they become metavariables Lean must solve against a numeral
  (`67108864 =?= ?a * ?d`), which has no unique solution.

## Measurement caveat: this GPU

34 of the 100 L1 tasks need 18–24GB for their inputs plus both outputs; this
machine has a 12GB RTX 4070 with ~10GB free. Those tasks are lowered, certified
and run at a reduced leading dimension, and **each reduced run is separately
lowered and certified at the size it runs** — nothing is verified at one shape and
measured at another. Because the family theorems are generic in every shape, the
certificate for the declared size holds regardless; only the empirical check is
size-limited. The run summary reports reduced and full-size passes separately.

Three more rules, all about what gets *run*, none about what gets proved:

  * **Too slow is treated like too big.** A kernel that exceeds the per-task time
    limit is retried at an eighth of the size, re-lowered and re-certified there,
    and reported as reduced. The kernels are correctness-first (one program per
    output, no data reuse), so a 2G-parameter MLP at batch 128 does not finish in
    four minutes; at batch 16 it does.
  * **Weights need no margin.** The memory budget is 60% of free memory, the margin
    being for the reference's temporaries, which cannot be estimated. Weights are
    exact and shared with the reference, so they are counted at their size; a
    float16 weight is counted twice, since the kernel reads a widened copy.
  * **What cannot fit at any size is certified, not dropped.** When shrinking no
    longer changes the inputs (the batch is already one), or the weights alone
    exceed the card, the task is lowered and certified at that size and reported
    as "does not fit". It is not counted as matched, and not as unlowered.

Certificates are checked in batches of at most 1500 stages per Lean file: checking a
whole level at once held every certificate in memory and exhausted the machine's.
Each batch is still checked in full before any of its kernels is emitted.
