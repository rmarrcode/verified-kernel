/-
The reduction family.

Covers every L1 task whose output element is a fold over one axis of the input,
optionally post-processed: sum/mean/max/min over a dimension, the losses (a fold
over *everything*, with `outer = inner = 1`), and the reduction stage of the
norms and of softmax.

The kernel shape is one program per output element, tiling the reduced axis with a
`block`-lane accumulator:

    acc = 0                       -- a tile of `block` partial sums
    for kb in range(nkb):         -- forAcc
      acc += masked(body)         -- lane `j` handles k = kb*block + j
    out[pid] = post(tl.sum(acc))  -- a 1x1 store

The proof has to reconcile three different orders of summation: the spec folds
once over `k < K`; the kernel folds over loop steps *within* each lane and then
across lanes. `sum_comm` exchanges the nesting, `sum_mul_split` flattens
`(kb, j)` to `k`, and `sum_eq_of_zero_beyond` discards the masked tail. That this
rearrangement is sound is precisely what an abstract field buys and `Float` does
not.
-/
import VerifiedKernel.Loop

namespace VerifiedKernel

open ExactScalar

/-- A reduction task.

`post` uses a slot convention: slot `0` is the *reduced value*, and slot `b+1` is
input buffer `b` read at the output index. That lets a task like a mean
(`sum * (1/K)`) or a normalisation be expressed without a second family. -/
structure RedSpec where
  /-- number of output rows -/
  outer : Nat
  /-- extent of the reduced axis -/
  K : Nat
  /-- number of trailing (un-reduced) elements per row -/
  inner : Nat
  /-- the summand, read at the reduced index -/
  body : SE
  /-- post-processing; slot 0 is the reduced value -/
  post : SE
  /-- number of input buffers -/
  nInp : Nat

namespace RedSpec

variable {α : Type} [ExactScalar α]

/-- Flat input index contributing to output `q` at reduction step `k`, for an
input laid out as `[outer, K, inner]`. -/
def inIdx (r : RedSpec) (q k : Nat) : Nat :=
  ((q / r.inner) * r.K + k) * r.inner + (q % r.inner)

/-- The specification. -/
def spec (r : RedSpec) : Spec α :=
  { arity := r.nInp
  , outSize := r.outer * r.inner
  , out := fun ins q =>
      let red := ExactScalar.sum r.K
        (fun k => r.body.denote (fun b => ins b (r.inIdx q k)))
      r.post.denote (fun b => match b with | 0 => red | b + 1 => ins b q) }

/-! ### The kernel -/

/-- `k = iv0 * block + col`: the reduction index this lane handles this iteration. -/
def kIE (block : Nat) : IE := .add (.mul (.iv 0) (.lit block)) .col

/-- `k < K`: masks both the loads and the summand, so out-of-range lanes neither
fault nor contribute. Masking the *summand* (not just the load) is essential --
a body like `exp x` maps a masked-to-zero load to `1`, not to `0`. -/
def kMask (block K : Nat) : BE := .cmp .lt (kIE block) (.lit K)

/-- The load offset, mirroring `inIdx` with `q := pid 0`. -/
def offIE (r : RedSpec) (block : Nat) : IE :=
  .add (.mul (.add (.mul (.divi (.pid 0) (.lit r.inner)) (.lit r.K)) (kIE block))
             (.lit r.inner))
       (.modi (.pid 0) (.lit r.inner))

/-- The masked summand. -/
def summand (r : RedSpec) (block : Nat) : FE :=
  .sel (kMask block r.K)
    (SE.toFEWith (fun b => .load b (r.offIE block) (kMask block r.K)) r.body)
    .zeroC

/-- The loop step: `acc + summand`. -/
def step (r : RedSpec) (block : Nat) : FE :=
  .bin .add (.acc 0) (r.summand block)

/-- The stored value: `post` with slot 0 bound to the cross-lane sum. -/
def stored (r : RedSpec) (block : Nat) : FE :=
  SE.toFEWith
    (fun b => match b with
      | 0 => .redCol .sum block (.acc 0)
      | b + 1 => .load b (.pid 0) .tt)
    r.post

def prog (r : RedSpec) (block nkb : Nat) : Prog :=
  { grid0 := r.outer * r.inner, grid1 := 1
  , body := .forAcc nkb .zeroC (r.step block) (.store 1 1 (.pid 0) (r.stored block) .tt) }

/-! ### Correctness -/

theorem summand_accFree (r : RedSpec) (block : Nat) :
    (r.summand block).accFree = true := by
  have h := SE.toFEWith_accFree
    (f := fun b => FE.load b (r.offIE block) (kMask block r.K)) (fun _ => rfl) r.body
  simp [summand, FE.accFree, h]

/-- The reduction index this lane handles. -/
theorem kIE_eval (block : Nat) (env : Env α) (kb j : Nat) (a : Nat → Nat → α) :
    (kIE block).eval (env.pushStep kb a) 0 j = kb * block + j := rfl

/-- The load offset is exactly the spec's input index. -/
theorem offIE_eval (r : RedSpec) (block : Nat) (bufs : Nat → Buf α) (q kb j : Nat)
    (a : Nat → Nat → α) :
    (r.offIE block).eval ((flatEnv bufs q).pushStep kb a) 0 j
      = r.inIdx q (kb * block + j) := rfl

/-- **The masked summand.** Out of range it is zero; in range it is the spec's
summand at the corresponding input index. -/
theorem summand_eval (r : RedSpec) (block : Nat) (bufs : Nat → Buf α) (q kb j : Nat)
    (a : Nat → Nat → α) :
    (r.summand block).eval ((flatEnv bufs q).pushStep kb a) 0 j
      = (if kb * block + j < r.K
         then r.body.denote (fun b => bufs b (r.inIdx q (kb * block + j)))
         else ExactScalar.zero) := by
  have hm : (kMask block r.K).eval ((flatEnv bufs q).pushStep kb a) 0 j
      = decide (kb * block + j < r.K) := rfl
  simp only [summand, FE.eval, hm]
  by_cases h : kb * block + j < r.K
  · simp only [h, decide_true, if_true]
    refine SE.toFEWith_eval (fun b => ?_) r.body
    simp only [FE.eval, hm, h, decide_true, if_true, offIE_eval]
    rfl
  · simp only [h, decide_false, Bool.false_eq_true, if_false]

/--
**The reduction theorem.**

Hypotheses: a positive block, and a loop long enough to cover the reduced axis
(`K ≤ nkb * block`). The latter is the analogue of grid coverage for the
reduction: with too few iterations the tail of the sum is silently dropped, and
the theorem then cannot be proved.
-/
theorem prog_implements (r : RedSpec) (block nkb : Nat)
    (hb : 0 < block) (hK : r.K ≤ nkb * block) :
    Implements (r.prog block nkb) (r.spec (α := α)) := by
  intro bufs m q hq
  have hq' : q < r.outer * r.inner := hq
  have hred : ExactScalar.sum block
      (fun p => accOf (flatEnv bufs q) nkb .zeroC (r.step block) 0 p)
      = ExactScalar.sum r.K (fun k => r.body.denote (fun b => bufs b (r.inIdx q k))) := by
    have hstep : ∀ p : Nat,
        accOf (flatEnv bufs q) nkb .zeroC (r.step block) 0 p
          = ExactScalar.sum nkb (fun kb =>
              if kb * block + p < r.K
              then r.body.denote (fun b => bufs b (r.inIdx q (kb * block + p)))
              else ExactScalar.zero) := by
      intro p
      rw [show r.step block = FE.bin .add (.acc 0) (r.summand block) from rfl,
          accOf_sum (summand_accFree r block) 0 p nkb]
      exact ExactScalar.sum_congr (fun kb _ => summand_eval r block bufs q kb p _)
    rw [ExactScalar.sum_congr (fun p _ => hstep p)]
    exact sum_tile_mask block nkb r.K
      (fun i => r.body.denote (fun b => bufs b (r.inIdx q i))) hK
  have hval : (r.stored block).eval ((flatEnv bufs q).pushAcc
      (accOf (flatEnv bufs q) nkb .zeroC (r.step block))) 0 0
        = (r.spec (α := α)).out bufs q := by
    refine SE.toFEWith_eval (fun b => ?_) r.post
    cases b with
    | zero =>
      show ExactScalar.sum block
        (fun p => accOf (flatEnv bufs q) nkb .zeroC (r.step block) 0 p) = _
      exact hred
    | succ b' => rfl
  rw [show r.prog block nkb = Prog.mk (r.outer * r.inner) 1
        (.forAcc nkb .zeroC (r.step block) (.store 1 1 (.pid 0) (r.stored block) .tt))
      from rfl, Prog.run_grid1]
  refine gridFold_at (v := (r.spec (α := α)).out bufs q) hq' ?_ ?_
  · intro mm
    rw [forAcc_exec]
    simp only [Stmt.exec]
    rw [store11_at _ _ _ _ q rfl]
    exact hval
  · intro p mm hne
    rw [forAcc_exec]
    simp only [Stmt.exec]
    exact store11_skip _ _ _ _ q (fun h => hne h)

end RedSpec
end VerifiedKernel
