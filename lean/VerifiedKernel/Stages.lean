/-
Pipelines of arbitrarily many stages.

`two_stage` and `three_stage` are fixed arity, which is enough for a single fused
operator but not for a chain of five, let alone a convolutional network. This file
replaces them with one theorem over a *list* of stages.

The bookkeeping is all about locality. Stage `j` reads buffers written by stages
before it, and each of those was written only up to its own size -- past that the
buffer holds whatever it held before. So the invariant carried through the induction
is not "the run and the spec agree" but "they agree *as far as anything has been
written*", which is what `Compat` says. `SpecLocal` is the matching obligation on a
stage: its output must not depend on what lies beyond those sizes.

Requiring each stage to be local with respect to the *final* size map, rather than
the map in force when it runs, costs nothing (`Compat` at an earlier map implies it
at a later one) and means each stage carries one obligation rather than one per
earlier stage -- linear rather than quadratic in the length of the chain.
-/
import VerifiedKernel.Pipeline

namespace VerifiedKernel

open ExactScalar

variable {α : Type} [ExactScalar α]

/-- How much of each buffer has been written. `none` means "this buffer is an input,
untouched, and the two environments agree on all of it". -/
abbrev Sizes := Nat → Option Nat

/-- Two buffer environments agree as far as anything has been written. -/
def Compat (sz : Sizes) (f g : Nat → Buf α) : Prop :=
  ∀ b i, (∀ n, sz b = some n → i < n) → f b i = g b i

theorem Compat.refl (sz : Sizes) (f : Nat → Buf α) : Compat sz f f :=
  fun _ _ _ => rfl

/-- Recording *more* sizes only weakens the agreement demanded, so a `Compat` from
earlier in the chain still holds against a later size map. This is what lets every
stage's obligation be stated once, against the final map, instead of once per
earlier stage -- linear rather than quadratic in the length of the chain. -/
theorem Compat.weaken {sz sz' : Sizes} {f g : Nat → Buf α}
    (hmono : ∀ b n, sz b = some n → sz' b = some n)
    (h : Compat sz f g) : Compat sz' f g :=
  fun b i hi => h b i (fun n hn => hi n (hmono b n hn))

/-- A spec that does not look past the recorded sizes. -/
def SpecLocal (sz : Sizes) (s : Spec α) : Prop :=
  ∀ (f g : Nat → Buf α), Compat sz f g → ∀ q, q < s.outSize → s.out f q = s.out g q

/-- Nothing written yet: the starting point of any chain. -/
def emptySizes : Sizes := fun _ => none

theorem emptySizes_sub (szF : Sizes) :
    ∀ b n, emptySizes b = some n → szF b = some n := by
  intro b n h
  simp [emptySizes] at h

/-- Record that buffer `t` now holds `n` written elements. -/
def setSize (t n : Nat) (sz : Sizes) : Sizes :=
  fun b => if b = t then some n else sz b

/-- One stage: what to run, what it computes, and which buffer it writes. -/
structure Stage (α : Type) where
  prog : Prog
  spec : Spec α
  out  : Nat

/-- Run a chain of stages, each substituting its own output buffer. -/
def runStages (ss : List (Stage α)) (f : Nat → Buf α) (m : Mem α) : Nat → Buf α :=
  match ss with
  | [] => f
  | st :: rest => runStages rest (subst f st.out (st.prog.run f m)) m

/-- The same chain, specified. -/
def specStages (ss : List (Stage α)) (g : Nat → Buf α) : Nat → Buf α :=
  match ss with
  | [] => g
  | st :: rest => specStages rest (subst g st.out (fun i => st.spec.out g i))

/-- The sizes in force after the whole chain. -/
def sizesAfter (ss : List (Stage α)) (sz : Sizes) : Sizes :=
  match ss with
  | [] => sz
  | st :: rest => sizesAfter rest (setSize st.out st.spec.outSize sz)

/--
**Compositionality for a chain of stages.**

If every stage implements its spec, and every stage's spec is local with respect to
the final size map `szF`, then running the chain agrees with specifying it -- as far
as anything has been written.

`szF` is supplied up front and must already record each stage's output size. That is
what makes the locality obligation per-stage rather than per-pair: a stage says "I do
not read past any recorded size", once, and it holds wherever in the chain it sits.
-/
theorem stages_correct (szF : Sizes) :
    ∀ (ss : List (Stage α)) (sz : Sizes) (f g : Nat → Buf α) (m : Mem α),
      Compat sz f g →
      (∀ b n, sz b = some n → szF b = some n) →
      (∀ st ∈ ss, szF st.out = some st.spec.outSize) →
      (∀ st ∈ ss, Implements st.prog st.spec) →
      (∀ st ∈ ss, SpecLocal szF st.spec) →
      Compat (sizesAfter ss sz) (runStages ss f m) (specStages ss g) := by
  intro ss
  induction ss with
  | nil => intro sz f g m h _ _ _ _; exact h
  | cons st rest ih =>
    intro sz f g m hfg hsub hsizes himp hloc
    have hmem : st ∈ st :: rest := by simp
    have hsetT : setSize st.out st.spec.outSize sz st.out = some st.spec.outSize := by
      simp [setSize]
    have hsetN : ∀ b, b ≠ st.out →
        setSize st.out st.spec.outSize sz b = sz b := by
      intro b hb; simp [setSize, hb]
    -- the head stage's output agrees with its spec, read against `g`
    have hhead : ∀ i, i < st.spec.outSize → (st.prog.run f m) i = st.spec.out g i := by
      intro i hi
      rw [himp st hmem f m i hi]
      exact hloc st hmem f g (hfg.weaken hsub) i hi
    have hstep : Compat (setSize st.out st.spec.outSize sz)
        (subst f st.out (st.prog.run f m))
        (subst g st.out (fun i => st.spec.out g i)) := by
      intro b i hi
      by_cases hb : b = st.out
      · subst hb
        simp only [subst_same]
        exact hhead i (hi st.spec.outSize hsetT)
      · simp only [subst_other hb]
        exact hfg b i (fun n hn => hi n (by rw [hsetN b hb]; exact hn))
    have hsub' : ∀ b n,
        (setSize st.out st.spec.outSize sz) b = some n → szF b = some n := by
      intro b n hn
      by_cases hb : b = st.out
      · subst hb
        rw [hsetT] at hn
        have : n = st.spec.outSize := (Option.some.inj hn).symm
        subst this
        exact hsizes st hmem
      · rw [hsetN b hb] at hn
        exact hsub b n hn
    exact ih _ _ _ m hstep hsub'
      (fun s hs => hsizes s (List.mem_cons_of_mem _ hs))
      (fun s hs => himp s (List.mem_cons_of_mem _ hs))
      (fun s hs => hloc s (List.mem_cons_of_mem _ hs))

/-! ## Discharging `SpecLocal` for a reducing stage

One obligation per stage, not one per earlier stage: the bounds are quantified over
every buffer at once, so a stage says "I do not read past any recorded size" once. -/

namespace GenRed

theorem specLocal (g : GenRed) (sz : Sizes)
    (hb1 : ∀ b n, sz b = some n → ∀ q k, q < g.nout → k < g.K →
      (g.offs b).evalQK q k < n)
    (hb2 : ∀ b n, sz b = some n → ∀ q, q < g.nout → (g.postOffs b).evalQK q 0 < n) :
    SpecLocal sz (g.spec (α := α)) := by
  intro e1 e2 hc q hq
  show (if _ then _ else _) = (if _ then _ else _)
  have hred : ExactScalar.sum g.K (fun k =>
        if (g.inRange).evalQK q k
        then g.body.denote (fun b => if b = g.idxSlot then ExactScalar.ofNat k
                                     else e1 b ((g.offs b).evalQK q k))
        else ExactScalar.zero)
      = ExactScalar.sum g.K (fun k =>
        if (g.inRange).evalQK q k
        then g.body.denote (fun b => if b = g.idxSlot then ExactScalar.ofNat k
                                     else e2 b ((g.offs b).evalQK q k))
        else ExactScalar.zero) := by
    refine ExactScalar.sum_congr (fun k hk => ?_)
    by_cases hr : (g.inRange).evalQK q k = true
    · simp only [hr, if_true]
      refine SE.denote_congr (fun b => ?_) g.body
      by_cases hs : b = g.idxSlot
      · simp only [hs, if_true]
      · simp only [hs, if_false]
        exact hc b _ (fun n hn => hb1 b n hn q k hq hk)
    · simp only [Bool.not_eq_true] at hr
      simp only [hr, Bool.false_eq_true, if_false]
  by_cases hg : (g.outGuard).evalQK q 0 = true
  · simp only [hg, if_true]
    refine SE.denote_congr (fun b => ?_) g.post
    cases b with
    | zero => exact hred
    | succ b' => exact hc b' _ (fun n hn => hb2 b' n hn q hq)
  · simp only [Bool.not_eq_true] at hg
    simp only [hg, Bool.false_eq_true, if_false]

end GenRed

namespace ProdRed

theorem specLocal (g : ProdRed) (sz : Sizes)
    (hb1 : ∀ b n, sz b = some n → ∀ q k, q < g.nout → k < g.K →
      (g.offs b).evalQK q k < n)
    (hb2 : ∀ b n, sz b = some n → ∀ q, q < g.nout → (g.postOffs b).evalQK q 0 < n) :
    SpecLocal sz (g.spec (α := α)) := by
  intro e1 e2 hc q hq
  show (if _ then _ else _) = (if _ then _ else _)
  have hred : ExactScalar.prod g.K (fun k =>
        if (g.inRange).evalQK q k
        then g.body.denote (fun b => if b = g.idxSlot then ExactScalar.ofNat k
                                     else e1 b ((g.offs b).evalQK q k))
        else ExactScalar.one)
      = ExactScalar.prod g.K (fun k =>
        if (g.inRange).evalQK q k
        then g.body.denote (fun b => if b = g.idxSlot then ExactScalar.ofNat k
                                     else e2 b ((g.offs b).evalQK q k))
        else ExactScalar.one) := by
    refine ExactScalar.prod_congr (fun k hk => ?_)
    by_cases hr : (g.inRange).evalQK q k = true
    · simp only [hr, if_true]
      refine SE.denote_congr (fun b => ?_) g.body
      by_cases hs : b = g.idxSlot
      · simp only [hs, if_true]
      · simp only [hs, if_false]
        exact hc b _ (fun n hn => hb1 b n hn q k hq hk)
    · simp only [Bool.not_eq_true] at hr
      simp only [hr, Bool.false_eq_true, if_false]
  by_cases hg : (g.outGuard).evalQK q 0 = true
  · simp only [hg, if_true]
    refine SE.denote_congr (fun b => ?_) g.post
    cases b with
    | zero => exact hred
    | succ b' => exact hc b' _ (fun n hn => hb2 b' n hn q hq)
  · simp only [Bool.not_eq_true] at hg
    simp only [hg, Bool.false_eq_true, if_false]

end ProdRed

namespace MaxRed

theorem specLocal (g : MaxRed) (sz : Sizes) (hK : 0 < g.K)
    (hb1 : ∀ b n, sz b = some n → ∀ q k, q < g.nout → k < g.K →
      (g.offs b).evalQK q k < n)
    (hb2 : ∀ b n, sz b = some n → ∀ q, q < g.nout → (g.postOffs b).evalQK q 0 < n) :
    SpecLocal sz (g.spec (α := α)) := by
  intro e1 e2 hc q hq
  have helem : ∀ k, k < g.K → g.elem e1 q k = g.elem e2 q k := by
    intro k hk
    refine SE.denote_congr (fun b => ?_) g.body
    by_cases hs : b = g.idxSlot
    · simp only [hs, if_true]
    · simp only [hs, if_false]
      exact hc b _ (fun n hn => hb1 b n hn q k hq hk)
  refine SE.denote_congr (fun b => ?_) g.post
  cases b with
  | zero => exact ExactScalar.foldMax_congr (helem 0 hK) (fun i hi => helem i hi)
  | succ b' => exact hc b' _ (fun n hn => hb2 b' n hn q hq)

end MaxRed

end VerifiedKernel
