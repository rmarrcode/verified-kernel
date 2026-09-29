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

The gap to 100 is **coverage**, not correctness: nine tasks the frontend declines to
lower, because it refuses rather than guesses. Nothing is left in a
"certified but not run" state — the tree reduction retired that category.

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
