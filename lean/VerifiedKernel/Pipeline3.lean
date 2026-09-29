/-
Three-stage pipelines.

`two_stage` carries one intermediate buffer, which is enough for softmax and for any
norm expressible from a single row reduction. It is *not* enough for a layer norm,
an instance norm, a group norm or a batch norm: each needs a mean **and** a variance
of the same input, i.e. two reductions whose results are both live at the final
stage.

The chain is `sum x` -> `sum (x - mean)^2` -> normalise, and this file says that such
a chain is correct when each stage is. The extra bookkeeping over `two_stage` is
entirely about *locality*: stage 3 reads two intermediate buffers, so it must be
insensitive to what lies beyond the end of each, and stage 2 reads the first. The
`Loc` abbreviation below names that obligation once so the three instances of it read
the same.
-/
import VerifiedKernel.Pipeline

namespace VerifiedKernel

open ExactScalar

variable {α : Type} [ExactScalar α]

/-- `Loc s t n`: the spec `s` does not depend on buffer `t` beyond index `n`.

Quantified over the base buffers, so it applies equally to a plain input environment
and to one that already has an intermediate substituted into it -- which is what lets
the same obligation be reused at every stage. -/
def Loc (s : Spec α) (t n : Nat) : Prop :=
  ∀ (bufs : Nat → Buf α) (u v : Buf α),
    (∀ i, i < n → u i = v i) →
    ∀ q, q < s.outSize → s.out (subst bufs t u) q = s.out (subst bufs t v) q

/-- Substitutions at distinct buffer indices commute. -/
theorem subst_comm {bufs : Nat → Buf α} {t1 t2 : Nat} (h : t1 ≠ t2) (u v : Buf α) :
    subst (subst bufs t1 u) t2 v = subst (subst bufs t2 v) t1 u := by
  funext b
  by_cases h2 : b = t2
  · subst h2
    simp only [subst_same, subst_other (Ne.symm h) , subst_same]
  · by_cases h1 : b = t1
    · subst h1
      simp only [subst_other h2, subst_same, subst_same]
    · simp only [subst_other h2, subst_other h1]

/-- Run three stages, threading two intermediate buffers. -/
def runThree (p1 p2 p3 : Prog) (t1 t2 : Nat)
    (bufs : Nat → Buf α) (m1 m2 m3 : Mem α) : Mem α :=
  p3.run (subst (subst bufs t1 (p1.run bufs m1)) t2
           (p2.run (subst bufs t1 (p1.run bufs m1)) m2)) m3

/-- The composed specification of a three-stage chain. -/
def compose3 (s1 s2 s3 : Spec α) (t1 t2 : Nat) (bufs : Nat → Buf α) (q : Nat) : α :=
  s3.out (subst (subst bufs t1 (fun i => s1.out bufs i)) t2
           (fun i => s2.out (subst bufs t1 (fun j => s1.out bufs j)) i)) q

/--
**Compositionality for three stages.**

Reading the hypotheses: stage 2 must not depend on buffer `t1` past what stage 1
wrote (`l2`), and stage 3 must not depend on either intermediate past what wrote it
(`l3a`, `l3b`). `t1 ≠ t2` is needed because the two intermediates must be distinct
buffers -- if they collided, stage 3 would read one where it meant the other, and
the statement would be false rather than merely unprovable.
-/
theorem three_stage {p1 p2 p3 : Prog} {s1 s2 s3 : Spec α} {t1 t2 : Nat}
    (hne : t1 ≠ t2)
    (h1 : Implements p1 s1) (h2 : Implements p2 s2) (h3 : Implements p3 s3)
    (l2 : Loc s2 t1 s1.outSize)
    (l3a : Loc s3 t1 s1.outSize) (l3b : Loc s3 t2 s2.outSize) :
    ∀ (bufs : Nat → Buf α) (m1 m2 m3 : Mem α) (q : Nat), q < s3.outSize →
      runThree p1 p2 p3 t1 t2 bufs m1 m2 m3 q = compose3 s1 s2 s3 t1 t2 bufs q := by
  intro bufs m1 m2 m3 q hq
  -- the buffers after stage 1, as run and as specified
  have hB1 : ∀ i, i < s1.outSize → (p1.run bufs m1) i = (fun i => s1.out bufs i) i :=
    fun i hi => h1 bufs m1 i hi
  -- stage 2's output agrees with its spec read against the *specified* stage 1
  have hstage2 : ∀ i, i < s2.outSize →
      (p2.run (subst bufs t1 (p1.run bufs m1)) m2) i
        = s2.out (subst bufs t1 (fun j => s1.out bufs j)) i := by
    intro i hi
    rw [h2 (subst bufs t1 (p1.run bufs m1)) m2 i hi]
    exact l2 bufs (p1.run bufs m1) (fun j => s1.out bufs j) hB1 i hi
  show p3.run (subst (subst bufs t1 (p1.run bufs m1)) t2
        (p2.run (subst bufs t1 (p1.run bufs m1)) m2)) m3 q
      = s3.out (subst (subst bufs t1 (fun i => s1.out bufs i)) t2
          (fun i => s2.out (subst bufs t1 (fun j => s1.out bufs j)) i)) q
  rw [h3 _ m3 q hq]
  rw [l3b (subst bufs t1 (p1.run bufs m1))
        (p2.run (subst bufs t1 (p1.run bufs m1)) m2)
        (fun i => s2.out (subst bufs t1 (fun j => s1.out bufs j)) i)
        hstage2 q hq]
  -- both sides now differ only in buffer `t1`; commute the substitutions so the
  -- difference is outermost and `l3a` applies
  have hc1 : subst (subst bufs t1 (p1.run bufs m1)) t2
        (fun i => s2.out (subst bufs t1 (fun j => s1.out bufs j)) i)
      = subst (subst bufs t2
          (fun i => s2.out (subst bufs t1 (fun j => s1.out bufs j)) i)) t1
          (p1.run bufs m1) := subst_comm hne _ _
  have hc2 : subst (subst bufs t1 (fun i => s1.out bufs i)) t2
        (fun i => s2.out (subst bufs t1 (fun j => s1.out bufs j)) i)
      = subst (subst bufs t2
          (fun i => s2.out (subst bufs t1 (fun j => s1.out bufs j)) i)) t1
          (fun i => s1.out bufs i) := subst_comm hne _ _
  rw [hc1, hc2]
  exact l3a _ (p1.run bufs m1) (fun i => s1.out bufs i) hB1 q hq

/-! ## Bounds helpers for normalisation stages -/

/-- `a * B + b < A * B` from `a < A` and `b < B`: the bound for a statistic index
built by packing two coordinates, as a group norm's `(n, g)` is. -/
theorem bound_pack {A B a b : Nat} (ha : a < A) (hb : b < B) : a * B + b < A * B :=
  calc a * B + b < a * B + B := Nat.add_lt_add_left hb _
    _ = (a + 1) * B := by rw [Nat.succ_mul]
    _ ≤ A * B := Nat.mul_le_mul_right B (Nat.succ_le_of_lt ha)

/-- A group norm's group index is in range: with `C = G * CG` channels split into `G`
groups of `CG`, the group of any channel is below `G`. -/
theorem bound_group {C CG G x : Nat} (hC : C = G * CG) (hG : 0 < G) (hCG : 0 < CG) :
    (x % C) / CG < G := by
  have hCpos : 0 < C := by rw [hC]; exact Nat.mul_pos hG hCG
  have h1 : x % C < C := Nat.mod_lt x hCpos
  have h2 : x % C < CG * G := by
    rw [Nat.mul_comm, ← hC]; exact h1
  exact Nat.div_lt_of_lt_mul h2

/-- A statistic index taken modulo its extent is in range -- the bound for a batch
norm, whose statistics are indexed by channel. -/
theorem bound_mod {n c : Nat} (hc : 0 < c) : n % c < c := Nat.mod_lt _ hc

/-! ## Discharging `Loc` for a reducing stage -/

/-- A `GenRed` stage is local in buffer `t` whenever every index it takes there is
below `n`. This is `GenRed.spec_locality` repackaged as `Loc`. -/
theorem GenRed.loc (g : GenRed) (t n : Nat)
    (hb1 : ∀ q k, q < g.nout → k < g.K → (g.offs t).evalQK q k < n)
    (hb2 : ∀ q, q < g.nout → (g.postOffs t).evalQK q 0 < n) :
    Loc (g.spec (α := α)) t n :=
  fun bufs u v huv q hq => GenRed.spec_locality g t n hb1 hb2 bufs u v huv q hq

/-- The same, for a multiplicative stage. -/
theorem ProdRed.loc (g : ProdRed) (t n : Nat)
    (hb1 : ∀ q k, q < g.nout → k < g.K → (g.offs t).evalQK q k < n)
    (hb2 : ∀ q, q < g.nout → (g.postOffs t).evalQK q 0 < n) :
    Loc (g.spec (α := α)) t n :=
  fun bufs u v huv q hq => ProdRed.spec_locality g t n hb1 hb2 bufs u v huv q hq

end VerifiedKernel
