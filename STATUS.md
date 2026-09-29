# Status

Measured numbers come from `python harness/run_all.py`; the run summary it prints
is the source of truth. This file records what is built, what is not, and the
design problems standing between here and 100% on Level 1.

## Measured (RTX 4070, 12GB; torch 2.14, triton 3.8, Lean 4.34.1)

```
  KernelBench Level 1                     100
  lowered to a specification               91
  correctness certificate checked by Lean   91
  matched PyTorch on this GPU               91   (43 at declared size, 48 reduced)
  mismatched or errored                      0
```

Every task that lowers both certifies and runs correctly: 91 of 91, with no
mismatch in any run of any family.

The gap to 100 is **coverage**, not correctness — tasks the frontend declines to
lower, since it refuses rather than guesses — plus 5 that are certified but whose
present shape is one program looping a million times, and so are not worth running
until a tree reduction exists (tasks 37, 94, 96, 98, 100).

Certificates depend only on `propext`, `Quot.sound` and `Classical.choice`; there is
no `sorryAx`. Check it with:

```bash
cd lean && echo 'import Generated.Emit
#print axioms t001_correct' > /tmp/ax.lean && lake env lean /tmp/ax.lean
```

Note on performance: these kernels are correctness-first, not tuned. The reducing
family runs one program per output element with no data reuse, so a large
contraction is orders of magnitude off cuBLAS. KernelBench also scores speedup;
that is not attempted here.

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
| `Pipeline.lean`, `Pipeline3.lean` | `two_stage`, `three_stage`, and the `Loc` obligations |

**Families and what they cover:**

| Family | Tasks |
|---|---|
| element-wise | 14 activations and pointwise ops |
| general reduction | axis reductions, losses, contractions, all 34 convolutions, average pooling, broadcasting |
| max/min reduction | max pooling, max/min over a dimension |
| two-stage pipeline | softmax, log-softmax, RMS/L1/L2 norms, tree reductions, depthwise-separable conv |
| three-stage pipeline | batch/instance/group/layer norm, Frobenius norm, triplet loss |

**Pipeline** (`verified_kernel/vk/`, `harness/`): fx-based frontend, Lean certificate
generator, Triton runtime, subprocess-isolated orchestrator, and
`harness/axiom_tests.py` validating the trusted Triton model.

Each task compiles to a `theorem` in `lean/Generated/Emit.lean` instantiating its
family's theorem at the chosen block size and grid; `lake build` checking that file
is the gate on emission.

## Not built, and what each needs

Nine tasks remain. None is more plumbing of the same kind; each needs a distinct
piece of design, and they are listed with what that piece actually is.

### 1. Scans — 5 tasks
Tasks 89–93 (cumsum, cumprod, reverse, exclusive, masked).

Needs an **IR extension**. Every family here stores *after* its accumulator loop,
because every family here computes one output per program. A scan writes one output
per *iteration*, so `Stmt` needs a form that threads memory as well as the
accumulator through the loop, and its correctness proof needs two injectivity
obligations the present families never incur: that a program's stores across
iterations land on distinct addresses, and that different programs' stores are
disjoint.

Expressing a scan inside the existing reducing family *is* possible — `out[q]` is a
reduction guarded by `rk <= k(q)` — and would be correct, but it is quadratic:
3.5 x 10^13 operations for task 89. Not a real option.

### 2. Argmax / argmin — 2 tasks
Tasks 51, 52. The reduced value is an *index*, so the accumulator must carry a pair
and the comparison must break ties the way PyTorch does (first occurrence). Needs a
product accumulator in the IR, and an integer output dtype in the runtime, which
currently allocates `float32` unconditionally.

### 3. Cross-entropy — 1 task
Task 95 needs a **data-dependent index map**: the log-probability is gathered at an
integer label read from another tensor. `IE.qkOnly` deliberately forbids this —
index maps are functions of the output and reduction indices only, which is what
makes `instK_eval` true and every tiling argument sound. Lifting it is a real
extension, not a missing case.

### 4. Attention — 1 task
Task 97 is two contractions around a softmax: four or five stages. `two_stage` and
`three_stage` are fixed-arity; this wants the list-based pipeline, whose
compositionality theorem is an induction over the stage list rather than the
two unfoldings written out.

### 5. Rounding
No error bound is proved. Certificates state exact-arithmetic equivalence; that this
implies agreement within KernelBench's 1e-2 is empirical (every kernel that has run
has matched), not proved. A bound would need a Flocq-style IEEE-754 development,
which does not exist usably for Lean 4.

## Measurement caveat: this GPU

34 of the 100 L1 tasks need 18–24GB for their inputs plus both outputs; this
machine has a 12GB RTX 4070 with ~10GB free. Those tasks are lowered, certified
and run at a reduced leading dimension, and **each reduced run is separately
lowered and certified at the size it runs** — nothing is verified at one shape and
measured at another. Because the family theorems are generic in every shape, the
certificate for the declared size holds regardless; only the empirical check is
size-limited. The run summary reports reduced and full-size passes separately.
