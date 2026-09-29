/-
Two-stage pipelines, and why they are needed.

A softmax, a layer norm, an RMS norm -- every row-normalising operator -- reduces a
row and then uses the reduced value at *every* element of that row. One kernel of
the shape this framework proves cannot do that: it writes one output per program,
and here the reduction's consumers outnumber its producers. The reduced values have
to be materialised in an intermediate buffer and read back by a second kernel.

`two_stage` is the compositionality theorem. Its content is small, which is the
point: if stage 1 implements its spec and stage 2 implements its spec, the pair
implements the composed spec -- *provided* stage 2 only reads the intermediate
buffer where stage 1 actually wrote. That proviso is not a technicality. Stage 1
writes `s1.outSize` elements and leaves the rest of the buffer as it found it, so a
stage 2 that indexed past the end would be reading uninitialised memory, and the
composed theorem would be false. `hloc` is where that obligation lives, and
`GenRed.spec_locality` is how a reducing stage discharges it.
-/
import VerifiedKernel.Kernels.GenRed
import VerifiedKernel.Kernels.MaxRed

namespace VerifiedKernel

open ExactScalar

variable {α : Type} [ExactScalar α]

/-- Replace buffer `t` with `v`. -/
def subst (bufs : Nat → Buf α) (t : Nat) (v : Buf α) : Nat → Buf α :=
  fun b => if b = t then v else bufs b

@[simp] theorem subst_same (bufs : Nat → Buf α) (t : Nat) (v : Buf α) :
    subst bufs t v t = v := by simp [subst]

@[simp] theorem subst_other {bufs : Nat → Buf α} {t b : Nat} {v : Buf α} (h : b ≠ t) :
    subst bufs t v b = bufs b := by simp [subst, h]

/-- Run stage 1 into buffer `t`, then stage 2. -/
def runTwo (p1 p2 : Prog) (t : Nat) (bufs : Nat → Buf α) (m1 m2 : Mem α) : Mem α :=
  p2.run (subst bufs t (p1.run bufs m1)) m2

/--
**Compositionality.** Two stages that each implement their spec implement the
composition, as long as stage 2 reads the intermediate buffer only within the range
stage 1 wrote (`hloc`).
-/
theorem two_stage {p1 p2 : Prog} {s1 s2 : Spec α} {t : Nat}
    (h1 : Implements p1 s1) (h2 : Implements p2 s2)
    (hloc : ∀ (bufs : Nat → Buf α) (u v : Buf α),
        (∀ i, i < s1.outSize → u i = v i) →
        ∀ q, q < s2.outSize →
          s2.out (subst bufs t u) q = s2.out (subst bufs t v) q) :
    ∀ (bufs : Nat → Buf α) (m1 m2 : Mem α) (q : Nat), q < s2.outSize →
      runTwo p1 p2 t bufs m1 m2 q
        = s2.out (subst bufs t (fun i => s1.out bufs i)) q := by
  intro bufs m1 m2 q hq
  show p2.run (subst bufs t (p1.run bufs m1)) m2 q = _
  rw [h2 (subst bufs t (p1.run bufs m1)) m2 q hq]
  exact hloc bufs (p1.run bufs m1) (fun i => s1.out bufs i)
    (fun i hi => h1 bufs m1 i hi) q hq

/-! ## Discharging `hloc` for a reducing stage -/

/-- A spec body reads its inputs only through `get`. -/
theorem SE.denote_congr {get get' : Nat → α} (h : ∀ b, get b = get' b) :
    ∀ (se : SE), se.denote get = se.denote get'
  | .inp b => h b
  | .lit _ _ _ => rfl
  | .bin op a b => by simp only [SE.denote, denote_congr h a, denote_congr h b]
  | .un f a => by simp only [SE.denote, denote_congr h a]
  | .recip a => by simp only [SE.denote, denote_congr h a]
  | .selLe a b s e => by
      simp only [SE.denote, denote_congr h a, denote_congr h b,
        denote_congr h s, denote_congr h e]

namespace GenRed

/--
**Locality of a reducing spec.** If every index this stage takes into buffer `t`
lands below `n1`, its output does not depend on what buffer `t` holds above `n1`.

The two bounds are the real obligations, and they are what a generated pipeline
certificate has to prove: for a row-normalising stage they amount to
`q / inner < outer`, which is exactly `Nat.div_lt_of_lt_mul`.
-/
theorem spec_locality (g : GenRed) (t n1 : Nat)
    (hb1 : ∀ q k, q < g.nout → k < g.K → (g.offs t).evalQK q k < n1)
    (hb2 : ∀ q, q < g.nout → (g.postOffs t).evalQK q 0 < n1) :
    ∀ (bufs : Nat → Buf α) (u v : Buf α),
      (∀ i, i < n1 → u i = v i) →
      ∀ q, q < g.nout →
        (g.spec (α := α)).out (subst bufs t u) q
          = (g.spec (α := α)).out (subst bufs t v) q := by
  intro bufs u v huv q hq
  have hget : ∀ (idx : Nat → Nat) (bnd : ∀ b, b = t → idx b < n1) (b : Nat),
      subst bufs t u b (idx b) = subst bufs t v b (idx b) := by
    intro idx bnd b
    by_cases hbt : b = t
    · subst hbt
      simp only [subst_same]
      exact huv (idx b) (bnd b rfl)
    · simp only [subst_other hbt]
  show (if _ then _ else _) = (if _ then _ else _)
  have hred : ExactScalar.sum g.K (fun k =>
        if (g.inRange).evalQK q k
        then g.body.denote (fun b => if b = g.idxSlot then ExactScalar.ofNat k
                                     else subst bufs t u b ((g.offs b).evalQK q k))
        else ExactScalar.zero)
      = ExactScalar.sum g.K (fun k =>
        if (g.inRange).evalQK q k
        then g.body.denote (fun b => if b = g.idxSlot then ExactScalar.ofNat k
                                     else subst bufs t v b ((g.offs b).evalQK q k))
        else ExactScalar.zero) := by
    refine ExactScalar.sum_congr (fun k hk => ?_)
    by_cases hr : (g.inRange).evalQK q k = true
    · simp only [hr, if_true]
      refine SE.denote_congr (fun b => ?_) g.body
      -- the index slot reads no memory, so it agrees on the nose
      by_cases hs : b = g.idxSlot
      · simp only [hs, if_true]
      · simp only [hs, if_false]
        exact hget (fun b => (g.offs b).evalQK q k)
          (fun b hbt => by rw [hbt]; exact hb1 q k hq hk) b
    · simp only [Bool.not_eq_true] at hr
      simp only [hr, Bool.false_eq_true, if_false]
  by_cases hg : (g.outGuard).evalQK q 0 = true
  · simp only [hg, if_true]
    refine SE.denote_congr (fun b => ?_) g.post
    cases b with
    | zero => exact hred
    | succ b' =>
      exact hget (fun b => (g.postOffs b).evalQK q 0)
        (fun b hbt => by subst hbt; exact hb2 q hq) b'
  · simp only [Bool.not_eq_true] at hg
    simp only [hg, Bool.false_eq_true, if_false]

end GenRed

namespace MaxRed

/-- **Locality of a max-reducing spec**, the analogue of `GenRed.spec_locality`.
Needed so an argmax can be two composed max stages: the second reads the first's
maximum out of an intermediate buffer.

`hidx` rules out the degenerate case where the substituted buffer *is* the index
slot, which denotes the reduction index rather than any memory. -/
theorem spec_locality (g : MaxRed) (t n : Nat) (hK : 0 < g.K)
    (hidx : t ≠ g.idxSlot)
    (hb1 : ∀ q k, q < g.nout → k < g.K → (g.offs t).evalQK q k < n)
    (hb2 : ∀ q, q < g.nout → (g.postOffs t).evalQK q 0 < n) :
    ∀ (bufs : Nat → Buf α) (u v : Buf α),
      (∀ i, i < n → u i = v i) →
      ∀ q, q < g.nout →
        (g.spec (α := α)).out (subst bufs t u) q
          = (g.spec (α := α)).out (subst bufs t v) q := by
  intro bufs u v huv q hq
  -- Reads of ordinary buffers agree; used for both `elem` and `post`.
  have hbuf : ∀ (idx : Nat → Nat), (∀ b, b = t → idx b < n) → ∀ b,
      subst bufs t u b (idx b) = subst bufs t v b (idx b) := by
    intro idx bnd b
    by_cases hbt : b = t
    · rw [hbt]
      simp only [subst_same]
      exact huv (idx t) (bnd t rfl)
    · simp only [subst_other hbt]
  -- `elem`'s slot map additionally pins the index slot to a value that does not
  -- come from memory at all, so it agrees on the nose.
  have helem : ∀ k, k < g.K →
      g.elem (subst bufs t u) q k = g.elem (subst bufs t v) q k := by
    intro k hk
    refine SE.denote_congr (fun b => ?_) g.body
    by_cases hs : b = g.idxSlot
    · simp only [hs, if_true]
    · simp only [hs, if_false]
      exact hbuf (fun b => (g.offs b).evalQK q k)
        (fun b hbt => by rw [hbt]; exact hb1 q k hq hk) b
  refine SE.denote_congr (fun b => ?_) g.post
  cases b with
  | zero =>
    exact ExactScalar.foldMax_congr (helem 0 hK) (fun i hi => helem i hi)
  | succ b' =>
    exact hbuf (fun b => (g.postOffs b).evalQK q 0)
      (fun b hbt => by rw [hbt]; exact hb2 q hq) b'

end MaxRed

/-! ## Bounds helpers

The index maps a row-normalising stage takes into the intermediate buffer are a
short list of shapes. These are the lemmas a generated certificate cites. -/

/-- `q / d < a` whenever `q < a * d`: the bound for a stage that reads one reduced
value per row. -/
theorem bound_div {a d q : Nat} (hq : q < a * d) : q / d < a :=
  Nat.div_lt_of_lt_mul (by rw [Nat.mul_comm] at hq; exact hq)

/--
The bound a row-normalising stage 2 needs: reading one reduced value per row, the
index it takes into the intermediate buffer stays inside it.

For an input viewed as `[outer, K, inner]` reduced along `K`, output element `q`
reads the intermediate at `(q / (K*inner)) * inner + q % inner`, and this says that
index is below `outer * inner`. Worth stating as a lemma rather than leaving to
`omega`: the term is nonlinear in the quotient, so linear arithmetic cannot see it.
-/
theorem bound_row {outer K inner q : Nat} (hi : 0 < inner)
    (hq : q < outer * (K * inner)) :
    (q / (K * inner)) * inner + q % inner < outer * inner := by
  have ho : q / (K * inner) < outer := bound_div hq
  have hm : q % inner < inner := Nat.mod_lt _ hi
  calc (q / (K * inner)) * inner + q % inner
      < (q / (K * inner)) * inner + inner := Nat.add_lt_add_left hm _
    _ = ((q / (K * inner)) + 1) * inner := by rw [Nat.succ_mul]
    _ ≤ outer * inner := Nat.mul_le_mul_right inner (Nat.succ_le_of_lt ho)

/-- The bound for a stage reading a single global value. -/
theorem bound_zero {n : Nat} (h : 0 < n) : 0 < n := h

end VerifiedKernel
