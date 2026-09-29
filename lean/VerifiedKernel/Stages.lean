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



/-! ## Stating a chain's index maps and sizes sparsely

Everything above is linear in the length of the chain. What is not, unless it is
said carefully, is the *proof* of a stage's locality obligation. Written the
obvious way -- one case per buffer, discharged by unfolding the size map -- a
454-stage network costs a case per buffer per stage, and neither the generated
text nor the elaborator survives it.

The waste is that the cases are nearly all the same. A stage reads one or two
buffers; for every other buffer its index map is the constant zero and the bound
is `0 < n`, which depends on the stage not at all. So the two definitions below
say only what is particular to a stage, and let the rest be one rewrite. -/

/-- An index map given as a table of the buffers a stage actually reads. Every
other buffer is indexed at zero, which is what a stage that does not read a buffer
does. -/
def IE.sparse : List (Nat × IE) → Nat → IE
  | [], _ => .lit 0
  | (i, e) :: rest, b => if b = i then e else IE.sparse rest b

@[simp] theorem IE.sparse_nil (b : Nat) : IE.sparse [] b = .lit 0 := rfl

@[simp] theorem IE.sparse_cons (i : Nat) (e : IE) (rest : List (Nat × IE)) (b : Nat) :
    IE.sparse ((i, e) :: rest) b = if b = i then e else IE.sparse rest b := rfl

/-- A sparse map is a map of the lane and the reduction index only, provided each
entry is. The constant-zero default trivially is. -/
theorem IE.qkOnly_sparse : ∀ (tbl : List (Nat × IE)),
    tbl.all (fun p => p.2.qkOnly) = true → ∀ b, (IE.sparse tbl b).qkOnly = true
  | [], _, _ => rfl
  | (i, e) :: rest, h, b => by
      simp only [List.all_cons, Bool.and_eq_true] at h
      by_cases hb : b = i
      · simpa [IE.sparse, hb] using h.1
      · simpa [IE.sparse, hb] using IE.qkOnly_sparse rest h.2 b

/-- A stage's index map, split at the first intermediate buffer: the inputs on one
side, the buffers earlier stages wrote on the other.

The split is what makes "this stage does not read that buffer" a rewrite instead of
a case. A locality obligation only ever fires for a buffer that was written, which
is to say one at or above `arity`; on that side the table holds only the one or two
buffers the stage really reads, and everything else is the constant zero. -/
def IE.split (arity : Nat) (inp mid : Nat -> IE) : Nat -> IE :=
  fun b => if b < arity then inp b else mid b

theorem IE.split_ge {arity : Nat} {inp mid : Nat -> IE} {b : Nat} (h : arity <= b) :
    IE.split arity inp mid b = mid b := by
  simp [IE.split, Nat.not_lt_of_le h]

theorem IE.qkOnly_split {arity : Nat} {inp mid : Nat -> IE}
    (hi : forall b, (inp b).qkOnly = true) (hm : forall b, (mid b).qkOnly = true) :
    forall b, (IE.split arity inp mid b).qkOnly = true := by
  intro b
  by_cases h : b < arity
  . simpa [IE.split, h] using hi b
  . simpa [IE.split, h] using hm b

/-- The sizes of a chain's intermediates, as a list indexed from the first one.
Buffers below `arity` are inputs and are not written at all. -/
def Sizes.ofList (arity : Nat) (l : List Nat) : Sizes :=
  fun b => if arity ≤ b then l[b - arity]? else none

@[simp] theorem Sizes.ofList_lt {arity : Nat} {l : List Nat} {b : Nat} (h : b < arity) :
    Sizes.ofList arity l b = none := by
  simp [Sizes.ofList, Nat.not_le_of_lt h]

theorem Sizes.ofList_ge {arity : Nat} {l : List Nat} {b : Nat} (h : arity ≤ b) :
    Sizes.ofList arity l b = l[b - arity]? := by
  simp [Sizes.ofList, h]

/-- A locality obligation only fires for a buffer something has written, and those
are exactly the buffers at or above the chain's arity. -/
theorem Sizes.ofList_le {arity : Nat} {l : List Nat} {b n : Nat}
    (h : Sizes.ofList arity l b = some n) : arity <= b := by
  by_cases hb : arity <= b
  . exact hb
  . rw [Sizes.ofList_lt (Nat.lt_of_not_le hb)] at h; exact absurd h (by simp)

/-- Reading one recorded size back, for the buffers a stage does read. -/
theorem Sizes.ofList_some {arity : Nat} {l : List Nat} {b n m : Nat}
    (hb : arity ≤ b) (hm : l[b - arity]? = some m)
    (h : Sizes.ofList arity l b = some n) : n = m := by
  rw [Sizes.ofList_ge hb, hm] at h
  exact (Option.some.inj h).symm

/-- Every recorded size is positive. One fact per chain, and the only thing a
stage needs to know about the buffers it does not read. -/
theorem Sizes.ofList_pos {arity : Nat} {l : List Nat} (hl : l.all (fun n => 0 < n) = true) :
    ∀ b n, Sizes.ofList arity l b = some n → 0 < n := by
  intro b n hb
  by_cases h : arity ≤ b
  · rw [Sizes.ofList_ge h] at hb
    have hmem : n ∈ l := List.mem_of_getElem? hb
    simpa using (List.all_eq_true.mp hl) n hmem
  · rw [Sizes.ofList_lt (Nat.lt_of_not_le h)] at hb; exact absurd hb (by simp)

end VerifiedKernel
