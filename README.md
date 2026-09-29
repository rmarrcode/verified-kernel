# verified-kernel

Neuro-symbolic generation of GPU kernels from PyTorch source. A kernel is emitted
only if a machine-checked proof says it computes the same thing as the PyTorch
module it came from.

```
PyTorch module  ->  formal spec  ->  kernel + proof  ->  Triton kernel
                (framework)          (Lean, checked)     (proved translation)
```

## How it works

Specs, kernels, and proofs live in **Lean 4** (`lean/`), chosen because the
framework is meant to be driven by an LLM: Lean has by far the deepest corpus of
machine-checked proofs to have learned from, and its metaprogramming lets the
Triton backend be written and verified in the same language.

1. **Spec.** `verified_kernel/vk/frontend.py` lowers a PyTorch module to a Lean
   denotation of its output — a function over the index space, in exact
   arithmetic. This step is the framework's, never the model's, so the target of
   the proof cannot be weakened by the thing being graded against it.
2. **Kernel + proof.** The kernel is a term in `TritonIR`, a deeply embedded
   tile-level IR (`lean/VerifiedKernel/Ir.lean`), and its correctness is a
   theorem about that term's denotation. Proofs are *per family*, generic in
   every shape and block size, so a task costs a certificate instantiating the
   family theorem rather than a fresh proof.
3. **Translation.** `TritonIR` is emitted as Triton via a rank-annotated target
   language, and emission is proved denotation-preserving once
   (`Emit.lean: emitIE_sound`, `emitFE_sound`). Every kernel inherits it.

### The IR's one good idea

A tile expression denotes a *function of a tile coordinate*, `⟦e⟧ env i j`. So
broadcasting, `expand_dims` and `reshape` do not exist in the IR — `row` *is* the
row coordinate — and `dot`/`reduce` are just binders over one coordinate. Whole
classes of shape-plumbing bugs cannot be written down.

The flip side is that real Triton *does* need explicit rank: `tl.arange(0,R)` must
be spelled `[:, None]` to vary along rows. Emission therefore has to reconstruct
what the IR erased, and `emitIE_sound` is the statement that it reconstructs it
correctly — swap `arangeRows` for `arangeCols` and the proof stops going through.

### Verified families, not verified kernels

| Family | Theorem | Covers |
|---|---|---|
| element-wise | `SE.flat_correct` | activations, scalar products, pointwise stages |
| general reduction | `GenRed.prog_implements` | axis reductions, losses, **contractions**, **convolution**, average pooling, broadcasting |
| max/min reduction | `MaxRed.prog_implements` | max pooling, max/min over a dimension |
| product reduction | `ProdRed.prog_implements` | cumulative products |
| two-stage pipeline | `two_stage` | softmax, log-softmax, norms, tree reductions, separable conv |
| three-stage pipeline | `three_stage` | norms, scans, attention, cross-entropy, triplet loss |

The second is the load-bearing one. Reductions, matrix products, convolutions and
pooling are the same kernel shape — one output per program, reduce over a window —
differing only in an **index map** over the output index `q` and reduction index
`k`. Generalising the family to carry per-input index maps means a convolution
costs an index map and a frontend rule, not a verification effort. `instK_eval` is
what licenses tiling an arbitrary map: it holds for any map built from `pid`,
`rk`, and arithmetic, so convolution's div/mod index unpacking is justified by the
same lemma as a plain sum over a dimension.

The max family is separate for a reason worth knowing. A masked sum excludes a lane
by contributing `zero`; a max has no identity to contribute, and *adding* a bottom
element to the field is unsound and silent — `le bot a` for every `a` plus the field
axioms gives `bot ≤ bot − 1 < bot`, so the axioms become inconsistent and every
theorem in the framework turns vacuous. `MaxRed` instead **clamps** its index maps,
so every lane reads a genuine element and lanes past the end read a duplicate, which
a max does not notice.

The pipelines handle operators that reduce and then use the reduced value at
every element of a row, which one kernel of this shape cannot do — the reduction's
consumers outnumber its producers. `two_stage` says two certified stages compose,
*provided* stage 2 reads the intermediate buffer only where stage 1 wrote it. That
proviso is the real content: stage 1 leaves the rest of the buffer as it found it,
so a stage 2 that indexed past the end would be reading uninitialised memory and
the composed theorem would be false.

## What "correct" means

Not bitwise agreement with `torch.matmul` — cuBLAS does not specify its reduction
order, so that is the wrong theorem. Proofs are carried out over an **abstract
ordered field with opaque elementary functions**, not `Float`. That is deliberate:

- `Float` is not associative, so no rearrangement of a tiled reduction is sound
  over it, and every such proof would die immediately. Over a field, `sum_comm`
  and `sum_mul_split` are exactly what licenses a blocked accumulator loop.
- The bugs that actually occur in generated kernels are indexing, masking,
  boundary, tiling and coverage bugs. All of those are visible at this
  abstraction, and are what these proofs rule out.

So a certificate means: *the algorithm is right, for every input and every shape,
in exact arithmetic.* Rounding is a separate, quantitative question. It is not yet
proved; empirically every kernel agrees with PyTorch far inside KernelBench's
1e-2 tolerance (see the run summary).

### Trusted base

The proofs do not stand alone. What is trusted, smallest-first:

1. **The renderer** (`Render.lean`) — one string template per node, no logic.
2. **The modelled Triton semantics** — that `PFE.eval` matches real `tl.*`.
   Discharged empirically by `harness/axiom_tests.py`, which differential-tests
   each modelled primitive, including the two places the model and Triton do not
   trivially agree: `IE.sub` is truncating `Nat` subtraction rendered as
   `tl.maximum(a-b,0)`, and `tanh` is rendered as `2·sigmoid(2x)−1` because
   Triton 3.8 has none.
3. **The Lean kernel**, and **Triton's own compiler**.
4. **The frontend** — and this is the real one. There is no formal semantics of
   PyTorch to prove it against, so a mis-lowering would produce a kernel provably
   equal to the *wrong* spec. It is therefore written to refuse rather than guess:
   every operator is in an explicit table, every shape assumption is asserted, and
   anything unrecognised returns a reason instead of a kernel.

## Layout

```
lean/VerifiedKernel/
  Scalar.lean      the abstract field; sum_comm, sum_mul_split, masking lemmas
  Ir.lean          TritonIR syntax + denotational semantics
  Coverage.lean    every output written exactly once (coverage, collision-freedom)
  AccFree.lean     which parts of the environment an expression can see
  Loop.lean        the accumulator loop; accOf_sum, sum_tile_mask
  Emit.lean        IR -> target language, with soundness
  Render.lean      target language -> Triton source (trusted)
  Kernels/         the families and their theorems
verified_kernel/vk/  frontend (PyTorch -> spec), compiler driver, runtime
harness/             L1 orchestration, evaluation, Triton model validation
generated/           emitted kernels (do not edit)
```

## Running it

```bash
python harness/axiom_tests.py        # validate the trusted Triton model
python harness/run_all.py            # lower, certify, and evaluate all of L1
python harness/run_all.py --only 63  # one task
```

`run_all.py` reports three numbers that must not be conflated: **lowered** (a spec
was derived), **certified** (Lean accepted the correctness certificate), and
**matched** (the emitted kernel also agreed with PyTorch on this GPU).

## Where it stands

| Level | Tasks | Lowered | Certified by Lean | Matched PyTorch |
|---|---|---|---|---|
| 1 — single operators | 100 | 100 | **100** | **100** |
| 2 — fused chains | 100 | 100 | **100** | see `STATUS.md` |
| 3 — whole architectures | 50 | 13 | — | — |
| 4 — HuggingFace models | 20 | — | — | — |

Level 1 is complete. Level 2 needed one new idea -- `stages_correct`, a
compositionality theorem over a *list* of stages -- and a compiler that walks a
traced graph emitting them; each non-pointwise node is lowered by the *same* Level 1
frontend and relocated into the chain's buffer numbering, so a convolution in a
chain is the same `GenRed`, at the same theorem, as a convolution on its own.

Level 3 is not simply more of the same, and `STATUS.md` says why: its chains reach
452 stages, and the locality obligation as currently stated is quadratic in chain
length. What is *not* proved anywhere is stated there too -- the rounding bound, and
the frontend's claim about what each PyTorch module means.

## Goal, and where it stands

100% correctness on KernelBench Level 1, then upward. Prior work (ProofWright,
arXiv 2511.12294) establishes semantic equivalence only for element-wise L1
kernels; the tiled reductions and convolutions are the interesting part, and are
what the general family covers here.

See `STATUS.md` for the current measured numbers and the remaining work.
