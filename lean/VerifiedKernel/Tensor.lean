/-
Buffers, specifications, and row-major index arithmetic.

Shapes are *not* carried in dependent types. A buffer is a flat function from
index to value, and shape information travels as ordinary `Nat` parameters in the
spec. This keeps every obligation first-order, which matters a great deal: the
proofs below are about index arithmetic and masking, and dependent shape types
make exactly those proofs harder rather than easier.
-/
import VerifiedKernel.Scalar

namespace VerifiedKernel

open ExactScalar

/-- A flat, row-major buffer. Reads beyond the logical size are allowed to return
anything; no theorem may depend on them. -/
abbrev Buf (α : Type) : Type := Nat → α

/-- A specification: how many outputs, and what each output element is as a
function of the inputs. This is the framework's own object -- it is generated
from the PyTorch module and is never written by the model being checked. -/
structure Spec (α : Type) where
  /-- Number of input buffers. -/
  arity   : Nat
  /-- Number of elements in the (flat) output. -/
  outSize : Nat
  /-- Value of output element `i`, given the inputs. -/
  out     : (Nat → Buf α) → Nat → α

/-! ## Row-major index arithmetic

`delin` decomposes a flat row-major index into its coordinates. These are the
functions a spec uses to talk about a 4-D tensor, and the ones a kernel must
reproduce; keeping them shared means the *decomposition* is correct by
construction and the proofs can concentrate on bounds and masking. -/

namespace Idx

/-- Coordinates of flat index `i` in a rank-2 row-major tensor `[_, d1]`. -/
def de2 (d1 i : Nat) : Nat × Nat := (i / d1, i % d1)

/-- Coordinates in `[_, d1, d2]`. -/
def de3 (d1 d2 i : Nat) : Nat × Nat × Nat :=
  (i / (d1 * d2), (i / d2) % d1, i % d2)

/-- Coordinates in `[_, d1, d2, d3]`. -/
def de4 (d1 d2 d3 i : Nat) : Nat × Nat × Nat × Nat :=
  (i / (d1 * d2 * d3), (i / (d2 * d3)) % d1, (i / d3) % d2, i % d3)

/-- Coordinates in `[_, d1, d2, d3, d4]`. -/
def de5 (d1 d2 d3 d4 i : Nat) : Nat × Nat × Nat × Nat × Nat :=
  (i / (d1 * d2 * d3 * d4), (i / (d2 * d3 * d4)) % d1, (i / (d3 * d4)) % d2,
   (i / d4) % d3, i % d4)

/-- Flat index from rank-2 coordinates. -/
def li2 (d1 a b : Nat) : Nat := a * d1 + b
/-- Flat index from rank-3 coordinates. -/
def li3 (d1 d2 a b c : Nat) : Nat := (a * d1 + b) * d2 + c
/-- Flat index from rank-4 coordinates. -/
def li4 (d1 d2 d3 a b c d : Nat) : Nat := ((a * d1 + b) * d2 + c) * d3 + d
/-- Flat index from rank-5 coordinates. -/
def li5 (d1 d2 d3 d4 a b c d e : Nat) : Nat :=
  (((a * d1 + b) * d2 + c) * d3 + d) * d4 + e

/-- `de2` inverts `li2` when the minor coordinate is in range. This is the lemma
that lets a kernel use a 2-D launch grid (`program_id` pairs) while the spec talks
about a single flat output index. -/
theorem de2_li2 {d1 a b : Nat} (hb : b < d1) : de2 d1 (li2 d1 a b) = (a, b) := by
  have hd : 0 < d1 := Nat.lt_of_le_of_lt (Nat.zero_le b) hb
  unfold de2 li2
  rw [Nat.mul_comm a d1, Nat.mul_add_div hd, Nat.mul_add_mod,
      Nat.div_eq_of_lt hb, Nat.mod_eq_of_lt hb, Nat.add_zero]

/-- The minor coordinate of a flat index is always in range. -/
theorem de2_snd_lt {d1 : Nat} (hd : 0 < d1) (i : Nat) : (de2 d1 i).2 < d1 :=
  Nat.mod_lt _ hd

/-- The major coordinate of an in-range flat index is in range. Used to discharge
the store mask on the row axis. -/
theorem de2_fst_lt {d0 d1 i : Nat} (hi : i < d0 * d1) :
    (de2 d1 i).1 < d0 := by
  unfold de2
  exact Nat.div_lt_of_lt_mul (by rw [Nat.mul_comm] at hi; exact hi)

/-- Recomposing a flat index from its own coordinates is the identity. -/
theorem li2_de2 (d1 i : Nat) :
    li2 d1 (de2 d1 i).1 (de2 d1 i).2 = i := by
  unfold de2 li2
  show (i / d1) * d1 + i % d1 = i
  rw [Nat.mul_comm]
  exact Nat.div_add_mod i d1

end Idx
end VerifiedKernel
