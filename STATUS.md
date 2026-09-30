# Status

Measured numbers come from `python harness/run_all.py`; the run summary it prints
is the source of truth. This file records what is built, what is not, and the
design problems standing between here and 100% on Level 1.

## Measured (RTX 4070, 12GB; torch 2.14, triton 3.8, Lean 4.34.1)

| Level | Tasks | Lowered | Certified by Lean | Matched | Matched, fp32 reference |
|---|---|---|---|---|---|
| 1 — single operators | 100 | 100 | **100** | **100** | 100 |
| 2 — fused chains | 100 | 100 | **100** | **99-100** † | 100 |
| 3 — whole architectures | 50 | 29 | **29** | **25** | pending |
| 4 — HuggingFace models | 20 | — | — | — | — |
| **total** | **270** | **229** | **229** | **224-225** | pending |

The last column runs the reference at full float32 rather than PyTorch's default
TF32; see *The reference's precision* below for why the two differ and why both are
reported. † One Level 2 task sits on the tolerance boundary and fails
intermittently -- twice in three full runs. It is not a defect in the kernel (see
below), but the Level 2 figure is 99 or 100 depending on the draw, and quoting 100
without that qualification would be picking the good run.

Levels 1 and 2 are complete: every task lowers to a formal specification, carries a
Lean-checked correctness certificate, and matches PyTorch under KernelBench's own
criterion (5 trials, `allclose` at 1e-2).

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
| `nn.LSTM` / `nn.GRU` / `nn.RNN` | 8 | out of reach -- cuDNN-fused, `fx` does not trace in |
| dynamic slicing on traced shapes | 3 | open |
| data-dependent control flow | 2 | out of reach -- `fx` cannot trace it |
| `unfold`, `expand`, `TransformerEncoder` | 1 (task 28) | open |
| `einsum` | 2 | open |

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

The eight recurrent tasks are the hard floor.

## Level 4

Not reachable on this machine: `transformers` is not installed, and the 20 tasks are
traced HuggingFace models, which need `transformers.utils.fx` rather than plain
symbolic tracing.

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

Neither was catchable by proof. Running the kernels is what found them.

### The trusted last mile
`Render.lean` (one string template per node), the modelled `tl.*` semantics
(differential-tested by `harness/axiom_tests.py`), the Lean kernel, and Triton's
own compiler.

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
