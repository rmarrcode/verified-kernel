# Status

Measured numbers come from `python harness/run_all.py`; the run summary it prints
is the source of truth. This file records what is built, what is not, and the
design problems standing between here and 100% on Level 1.

## Built

**Verified core** (`lean/`, ~1800 lines, no `sorry` and no `native_decide`):

- `Scalar.lean` — the abstract ordered field with opaque elementary functions,
  plus the reduction algebra: `sum_comm` (Fubini), `sum_mul_split` (tiling),
  `sum_eq_of_zero_beyond` (masking), `sum_add_distrib`.
- `Ir.lean` — `TritonIR` syntax and denotational semantics. Tile expressions
  denote functions of a tile coordinate, so broadcasting is not expressible and
  `dot`/`reduce` are coordinate binders.
- `Coverage.lean` — `writeFold_hit` / `writeFold_miss` / `gridFold_at`: every
  output element is written exactly once, by the lane that computed it. Coverage
  and collision-freedom are obligations discharged, not assumptions.
- `AccFree.lean` — an accumulator loop's summand cannot see the accumulator.
- `Loop.lean` — `accOf_sum`, `sum_tile_mask`: a blocked masked accumulator equals
  a contiguous fold.
- `Emit.lean` — translation to a rank-annotated target language with
  `emitIE_sound` / `emitBE_sound` / `emitFE_sound`.
- `Render.lean` — target language to Triton text. **Trusted**, one template per
  node.
- `Kernels/Elementwise.lean` — `SE.flat_correct`.
- `Pipeline.lean` — `two_stage`, the compositionality theorem, plus
  `GenRed.spec_locality` and `bound_row` for discharging its locality obligation.
- `Kernels/GenRed.lean` — `GenRed.prog_implements`, the general reducing family:
  per-input index maps, a validity guard for padding, and an output guard for
  masked results. `IE.instK_eval` licenses tiling any map built from the output
  and reduction indices.

**Pipeline** (`verified_kernel/vk/`, `harness/`): fx-based frontend, Lean
certificate generator, Triton runtime, subprocess-isolated L1 orchestrator, and
`harness/axiom_tests.py` validating the trusted Triton model (all pass).

Each task compiles to a `theorem` in `lean/Generated/Emit.lean` instantiating its
family theorem at the chosen block size and grid; `lake build` checking that file
is the gate on emission. Side conditions (`0 < block`, grid covers the output,
loop covers the reduced axis) are discharged by `decide`.

## Not built, and what each needs

### 1. Pipelines with more than one intermediate — 8 tasks
Tasks 33 (BatchNorm), 34 (InstanceNorm), 35 (GroupNorm), 40 (LayerNorm), 86
(depthwise-separable), 95 (cross-entropy), 97 (attention), 99 (triplet margin).

Two-stage pipelines with *one* intermediate are built and cover softmax,
log-softmax, and the RMS/Frobenius/L1/L2 norms. What these eight need is more:

- The four remaining norms need a **mean and a variance**, i.e. two reductions of
  the same input. `two_stage` carries one intermediate buffer, so this needs either
  a three-stage chain (`sum x` → `sum (x - mean)²` → normalise) or one stage
  writing a buffer of `2 * outer` elements with the body switching on the program
  id — which the family cannot express, because `body` has no access to `pid`.
  The three-stage chain is the cleaner route and reduces to nesting `two_stage`,
  which needs a list-based version of `runTwo`.
- Attention (97) is three stages including two contractions; cross-entropy (95)
  needs a gather by an integer label tensor, which the IR has no node for.

A tree reduction (the same list-based pipeline) is also what makes the full
reductions **runnable** rather than merely verified: tasks 94, 96, 98, 100 have
`outer = inner = 1`, so the present family gives one program looping a million
times. Certified, but pointlessly serial, and the harness reports them as such
rather than pretending otherwise.

### 2. Max/min reductions — 5 tasks
Tasks 41–43 (max pooling), 49, 53 (max/min over a dimension).

Harder than it looks, and the reason is worth recording. A masked sum is easy:
excluded lanes contribute `zero`, the additive identity. A masked *max* has no
identity — an ordered field has no least element. Three options:

- **Seed with a known element.** Fails for pooling: which taps are valid depends
  on the output index, so no fixed tap index is always valid.
- **Add a bottom element to `ExactScalar`.** *Unsound, and quietly so.* From
  `le bot a` for all `a` plus the field axioms one derives `bot ≤ bot - 1 < bot`.
  The axioms become inconsistent and every theorem in the framework turns vacuous.
  This must not be done.
- **A float sentinel plus an explicit precondition** — render `-3.4e38` and carry
  the hypothesis `∀ valid taps, sentinel ≤ f(k)` into the theorem. Sound, honest,
  and the resulting certificate is *conditional* on a property of the input values
  that cannot be checked statically. This is the right route.

Also needs the order-theoretic tiling lemmas (`max` is associative, commutative
and idempotent), most cheaply via the characterisation "the fold is an upper bound
and is attained", then antisymmetry.

### 3. Scans — 5 tasks
Tasks 89–93 (cumsum, cumprod, reverse, exclusive, masked). A prefix scan is not a
reduction: output `q` depends on a *prefix*, so the family's one-output-per-program
shape does not fit. Needs a scan family (`tl.cumsum` modelled, with a
carry across blocks) and its own correctness theorem.

### 4. Argmax / argmin — 2 tasks
Tasks 51, 52. The reduced value is an *index*, not a scalar, so the accumulator
must carry a pair and the comparison must break ties the way PyTorch does (first
occurrence). Needs a product accumulator in the IR.

### 5. Rounding
No error bound is proved yet. Certificates state exact-arithmetic equivalence; the
claim that this implies agreement within KernelBench's 1e-2 is currently empirical,
not proved. A bound would need a `Flocq`-style IEEE-754 development, which does not
exist for Lean 4 in usable form.

## Measurement caveat: this GPU

34 of the 100 L1 tasks need 18–24GB for their inputs plus both outputs; this
machine has a 12GB RTX 4070 with ~10GB free. Those tasks are lowered, certified
and run at a reduced leading dimension, and **each reduced run is separately
lowered and certified at the size it runs** — nothing is verified at one shape and
measured at another. Because the family theorems are generic in every shape, the
certificate for the declared size holds regardless; only the empirical check is
size-limited. The run summary reports reduced and full-size passes separately.
