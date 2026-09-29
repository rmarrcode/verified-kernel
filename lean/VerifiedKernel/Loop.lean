/-
The accumulator-loop machinery, shared by every family that reduces.

Isolated here because three different families -- plain axis reductions,
contractions (matmul), and windowed reductions (convolution, pooling) -- all
compile to the same loop shape and need exactly these lemmas about it.
-/
import VerifiedKernel.Kernels.Elementwise
import VerifiedKernel.AccFree

namespace VerifiedKernel

open ExactScalar

variable {α : Type} [ExactScalar α]

/-! ## The accumulator loop, shared by every reducing family -/

/-- The accumulator value after `n` iterations, matching `Stmt.exec`'s `forAcc`. -/
def accOf (env : Env α) (n : Nat) (init stp : FE) : Nat → Nat → α :=
  Nat.rec (motive := fun _ => Nat → Nat → α)
    (fun i j => init.eval env i j)
    (fun k a => fun i j => stp.eval (env.pushStep k a) i j)
    n

theorem forAcc_exec (env : Env α) (m : Mem α) (n : Nat) (init stp : FE) (bd : Stmt) :
    (Stmt.forAcc n init stp bd).exec env m
      = bd.exec (env.pushAcc (accOf env n init stp)) m := rfl

/-- **The accumulator is a sum.** If the summand cannot see the accumulator, the
loop computes exactly `∑_{k<n}` of it. -/
theorem accOf_sum {env : Env α} {g : FE} (hg : g.accFree = true) (i j : Nat) (n : Nat) :
    accOf env n .zeroC (.bin .add (.acc 0) g) i j
      = ExactScalar.sum n (fun k => g.eval (env.pushStep k (fun _ _ => ExactScalar.zero)) i j) := by
  induction n with
  | zero => rfl
  | succ k ih =>
    show Bop.apply .add _ _ = _
    rw [ExactScalar.sum_succ]
    show ExactScalar.add (accOf env k .zeroC (.bin .add (.acc 0) g) i j) _ = _
    rw [ih]
    exact congrArg _ (FE.eval_accFree
      (env := env.pushStep k (accOf env k .zeroC (.bin .add (.acc 0) g)))
      (env' := env.pushStep k (fun _ _ => ExactScalar.zero))
      rfl rfl rfl g hg i j)


/-- **The rearrangement.** A tiled, masked accumulator sums to the same thing as a
single contiguous fold. Reading the rewrites in order: exchange the lane/step
nesting, flatten `(kb, p)` into a single index, drop the masked tail, then discard
the mask on what remains.

Every step here is an equality of *exact* field elements. None of them holds over
`Float`, which is why the framework proves algorithms in an abstract field and
treats rounding as a separate quantitative question. -/
theorem sum_tile_mask (block nkb K : Nat) (f : Nat → α) (hK : K ≤ nkb * block) :
    ExactScalar.sum block (fun p => ExactScalar.sum nkb
        (fun kb => if kb * block + p < K then f (kb * block + p) else ExactScalar.zero))
      = ExactScalar.sum K f := by
  rw [ExactScalar.sum_comm block nkb
    (fun p kb => if kb * block + p < K then f (kb * block + p) else ExactScalar.zero)]
  rw [← ExactScalar.sum_mul_split nkb block
    (fun i => if i < K then f i else ExactScalar.zero)]
  rw [ExactScalar.sum_eq_of_zero_beyond hK (fun i h1 _ => if_neg (Nat.not_lt.mpr h1))]
  exact ExactScalar.sum_congr (fun i hi => if_pos hi)


end VerifiedKernel
