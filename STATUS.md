# Status

Measured numbers come from `python harness/run_all.py`; the run summary it prints
is the source of truth. This file records what is built, what is not, and the
design problems standing between here and 100% on Level 1.

## Measured (RTX 4070, 12GB; torch 2.14, triton 3.8, Lean 4.34.1)

```
  KernelBench Level 1                     100
  lowered to a specification               89
  correctness certificate checked by Lean   89
  matched PyTorch on this GPU               84   (41 at declared size, 43 reduced)
  certified, not run (serial)                5
  mismatched or errored                      0
```

Every kernel that ran matched: 84 of 84, across four runs and every family.

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

## Not built, and what each needs

### 1. Longer pipelines — 4 tasks
Tasks 86 (depthwise-separable), 95 (cross-entropy), 97 (attention), 99 (triplet
margin).

Two- and three-stage pipelines are built (`two_stage`, `three_stage`) and cover
softmax, log-softmax, the RMS/Frobenius/L1/L2 norms, and all four
mean-and-variance normalisations. What remains:

- **86** is two convolutions in sequence, so `two_stage` already fits; the work is
  the locality bound, which for a conv index map is a nest of `bound_pack`.
- **99** is two row reductions, a pointwise combination, and a final full
  reduction — reachable with `three_stage`, though its last stage would be serial.
- **97** (attention) is two contractions around a softmax, so four or five stages;
  it wants a list-based pipeline rather than another fixed arity.
- **95** needs a *data-dependent* index map: gathering a log-probability by an
  integer label. `IE.qkOnly` deliberately forbids that — index maps are functions
  of the output and reduction indices only — so this is a real IR extension, not
  plumbing.

A tree reduction (again, the list-based pipeline) is also what makes the full
reductions **runnable** rather than merely verified: tasks 37, 94, 96, 98, 100 have
one output, so the present family gives one program looping a million times.
Certified, but pointlessly serial, and the harness reports them as such rather than
pretending otherwise.

### 2. Max/min reductions — built (5 tasks)
Tasks 41–43 (max pooling), 49, 53 (max/min over a dimension) all pass.

Recorded because the design took a wrong turn first. A masked sum is easy: excluded
lanes contribute `zero`, the additive identity. A masked *max* has no identity, and
the tempting fix — adding a bottom element to `ExactScalar` — is **unsound and
quietly so**: `le bot a` for every `a` plus the field axioms yields
`bot ≤ bot - 1 < bot`, the axioms become inconsistent, and every theorem in the
framework silently turns vacuous.

A float sentinel with an explicit input precondition would be sound but would make
those certificates *conditional*. Neither is necessary. `MaxRed` never masks: its
index maps **clamp**, so every lane reads a genuine element and lanes past the end
read a duplicate, which a max does not notice. `Nat` truncating subtraction supplies
the clamp with no new IR node.

One real bug came out of this, and it is the kind only running the kernel finds:
clamping a pooling *coordinate* is sound for a contiguous window but not a dilated
one, where the window is a strided set. Clamping the *tap index* instead fixes it.
That the clamp lands in the window is a frontend obligation — a fact about what the
PyTorch module means — which is exactly the part of the pipeline no proof covers.

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
