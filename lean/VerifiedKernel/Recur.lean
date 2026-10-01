/-
Recurrences: one certified body, run `T` times.

A recurrent network is the same few operations applied at every time step, each
step reading the state the last one wrote. Unrolled into a chain that is one stage
list per step -- thousands of stages for a six-layer LSTM over 512 steps, each with
its own kernel and its own certificate. Nothing about step 400 needs proving that
step 3 did not, so this file proves the loop once.

The construction:

  * `GStage` generalises `Stage` from "a kernel" to "anything that computes one
    buffer", with `GImpl` for what `Implements` said. `gstages_correct` is
    `stages_correct` over that, and an ordinary stage is one (`GStage.ofStage`).
  * `Recur` is a `GStage` whose computation is a loop. Step `t` runs a body chain in
    an environment where one buffer (`st`) holds the current state and each view
    buffer holds a window `src[t*stride ..]` of an outer buffer -- a time step of
    the input. The body's last stage writes the next state. The output is the whole
    history, `(T+1) * S` elements, state `t` at offset `t * S`.
  * `Recur.impl` proves the loop implements its specification, by induction on the
    step, from the body's own chain certificate (`stages_correct`). `Recur.spec_local`
    proves it reads no outer buffer past what was written there, which is what lets
    it sit inside a chain like any other stage.

The launcher runs the body's kernels `T` times, passing tensor *views* for the state
and input windows. That a view of a contiguous buffer at offset `o` reads element
`o + i` as its element `i` is the one new assumption about the runtime, and it is
what `Recur.envAt` states.
-/
import VerifiedKernel.Stages

namespace VerifiedKernel

open ExactScalar

variable {α : Type} [ExactScalar α]

/-! ## Generalised stages -/

/-- A stage that computes one buffer, by whatever means. -/
structure GStage (α : Type) where
  run  : (Nat → Buf α) → Mem α → Buf α
  spec : Spec α
  out  : Nat

/-- What `Implements` says of a kernel, for a generalised stage. -/
def GImpl (s : GStage α) : Prop :=
  ∀ (f : Nat → Buf α) (m : Mem α) (q : Nat), q < s.spec.outSize → s.run f m q = s.spec.out f q

/-- A kernel stage is a generalised one. -/
def GStage.ofStage (st : Stage α) : GStage α := ⟨fun f m => st.prog.run f m, st.spec, st.out⟩

theorem GStage.ofStage_impl {st : Stage α} (h : Implements st.prog st.spec) :
    GImpl (GStage.ofStage st) :=
  fun f m q hq => h f m q hq

def runG (ss : List (GStage α)) (f : Nat → Buf α) (m : Mem α) : Nat → Buf α :=
  match ss with
  | [] => f
  | st :: rest => runG rest (subst f st.out (st.run f m)) m

def specG (ss : List (GStage α)) (g : Nat → Buf α) : Nat → Buf α :=
  match ss with
  | [] => g
  | st :: rest => specG rest (subst g st.out (fun i => st.spec.out g i))

def sizesAfterG (ss : List (GStage α)) (sz : Sizes) : Sizes :=
  match ss with
  | [] => sz
  | st :: rest => sizesAfterG rest (setSize st.out st.spec.outSize sz)

/-- `stages_correct`, for generalised stages. The proof is the same induction. -/
theorem gstages_correct (szF : Sizes) :
    ∀ (ss : List (GStage α)) (sz : Sizes) (f g : Nat → Buf α) (m : Mem α),
      Compat sz f g →
      (∀ b n, sz b = some n → szF b = some n) →
      (∀ st ∈ ss, szF st.out = some st.spec.outSize) →
      (∀ st ∈ ss, GImpl st) →
      (∀ st ∈ ss, SpecLocal szF st.spec) →
      Compat (sizesAfterG ss sz) (runG ss f m) (specG ss g) := by
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
    have hhead : ∀ i, i < st.spec.outSize → st.run f m i = st.spec.out g i := by
      intro i hi
      rw [himp st hmem f m i hi]
      exact hloc st hmem f g (hfg.weaken hsub) i hi
    have hstep : Compat (setSize st.out st.spec.outSize sz)
        (subst f st.out (st.run f m))
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

/-- Specifying a chain is local: two environments that agree as far as anything is
written give specified results that agree as far as anything is written. The
spec-only half of `stages_correct`, needed to show a loop is itself local. -/
theorem specStages_compat (szF : Sizes) :
    ∀ (ss : List (Stage α)) (sz : Sizes) (f g : Nat → Buf α),
      Compat sz f g →
      (∀ b n, sz b = some n → szF b = some n) →
      (∀ st ∈ ss, szF st.out = some st.spec.outSize) →
      (∀ st ∈ ss, SpecLocal szF st.spec) →
      Compat (sizesAfter ss sz) (specStages ss f) (specStages ss g) := by
  intro ss
  induction ss with
  | nil => intro sz f g h _ _ _; exact h
  | cons st rest ih =>
    intro sz f g hfg hsub hsizes hloc
    have hmem : st ∈ st :: rest := by simp
    have hsetT : setSize st.out st.spec.outSize sz st.out = some st.spec.outSize := by
      simp [setSize]
    have hsetN : ∀ b, b ≠ st.out →
        setSize st.out st.spec.outSize sz b = sz b := by
      intro b hb; simp [setSize, hb]
    have hstep : Compat (setSize st.out st.spec.outSize sz)
        (subst f st.out (fun i => st.spec.out f i))
        (subst g st.out (fun i => st.spec.out g i)) := by
      intro b i hi
      by_cases hb : b = st.out
      · subst hb
        simp only [subst_same]
        exact hloc st hmem f g (hfg.weaken hsub) i (hi st.spec.outSize hsetT)
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
    exact ih _ _ _ hstep hsub'
      (fun s hs => hsizes s (List.mem_cons_of_mem _ hs))
      (fun s hs => hloc s (List.mem_cons_of_mem _ hs))

/-! ## The recurrence -/

/-- A view of buffer `src`: at step `t`, element `i` is `src`'s `t * stride + i`. -/
structure View where
  buf    : Nat
  src    : Nat
  stride : Nat

/-- The view installed at buffer `b`, if any -- the first, if several claim it. -/
def viewOf : List View → Nat → Option View
  | [], _ => none
  | v :: vs, b => if v.buf = b then some v else viewOf vs b

theorem viewOf_mem {vs : List View} {b : Nat} {v : View} :
    viewOf vs b = some v → v ∈ vs ∧ v.buf = b := by
  induction vs with
  | nil => simp [viewOf]
  | cons u vs ih =>
    intro h
    by_cases hb : u.buf = b
    · simp [viewOf, hb] at h; subst h; exact ⟨by simp, hb⟩
    · simp only [viewOf, hb, ite_false] at h
      exact ⟨List.mem_cons_of_mem _ (ih h).1, (ih h).2⟩

omit [ExactScalar α] in
/-- The sizes after a chain whose last stage is `st` record `st`'s output. -/
theorem sizesAfter_last (st : Stage α) :
    ∀ (ss : List (Stage α)) (sz : Sizes),
      sizesAfter (ss ++ [st]) sz st.out = some st.spec.outSize := by
  intro ss
  induction ss with
  | nil => intro sz; simp [sizesAfter, setSize]
  | cons a rest ih => intro sz; exact ih _

/-- Recording more intermediates after the ones already recorded changes none of
them. -/
theorem Sizes.ofList_append_sub (A : Nat) (l extra : List Nat) :
    ∀ b n, Sizes.ofList A l b = some n → Sizes.ofList A (l ++ extra) b = some n := by
  intro b n h
  have hb : A ≤ b := Sizes.ofList_le h
  rw [Sizes.ofList_ge hb] at h ⊢
  rw [List.getElem?_append_left (by
    rcases Nat.lt_or_ge (b - A) l.length with hl | hl
    · exact hl
    · rw [List.getElem?_eq_none hl] at h; exact absurd h (by simp))]
  exact h

/-- One recurrence: `T` steps of a body over a state of `S` elements. -/
structure Recur (α : Type) where
  T     : Nat
  S     : Nat
  /-- the outer buffer holding the initial state -/
  init  : Nat
  /-- the buffer the body reads the current state from -/
  st    : Nat
  views : List View
  body  : List (Stage α)
  /-- the buffer the body's last stage writes the next state to -/
  nxt   : Nat
  /-- the outer buffer this recurrence writes: the whole history -/
  out   : Nat
  /-- the history's size, `T * S + S` (`Ok.hH`). Recorded as a number, not a
  product: a certificate compares it with the outer size map by `rfl`, and Lean
  checks `n = a * b` by unfolding the product rather than multiplying. -/
  H     : Nat

namespace Recur

variable (r : Recur α)

/-- The body's environment at step `t`, with state `s`: the state at `st`, each
view's window of its source, and the outer buffers everywhere else. -/
def envAt (f : Nat → Buf α) (t : Nat) (s : Buf α) : Nat → Buf α :=
  fun b => if b = r.st then s else
    match viewOf r.views b with
    | some v => fun i => f v.src (t * v.stride + i)
    | none => f b

/-- The state after each step, running the body's kernels. -/
def runState (f : Nat → Buf α) (m : Mem α) : Nat → Buf α
  | 0 => f r.init
  | t + 1 => runStages r.body (r.envAt f t (runState f m t)) m r.nxt

/-- The state after each step, as specified. -/
def specState (f : Nat → Buf α) : Nat → Buf α
  | 0 => f r.init
  | t + 1 => specStages r.body (r.envAt f t (specState f t)) r.nxt

/-- The history: state `t` at offset `t * S`, for `T + 1` states. -/
def spec : Spec α :=
  { arity := 0, outSize := r.H,
    out := fun f i => r.specState f (i / r.S) (i % r.S) }

def toG : GStage α :=
  { run := fun f m i => r.runState f m (i / r.S) (i % r.S), spec := r.spec, out := r.out }

/-- The sizes the body starts from: the state holds `S` elements, each view its
stride, and every other buffer what the outer chain recorded. -/
def bodySizes (szO : Sizes) : Sizes :=
  fun b => if b = r.st then some r.S else
    match viewOf r.views b with
    | some v => some v.stride
    | none => szO b

/-- Everything the loop needs of its body, all certified once for the body: its
stages are correct and local against `szF`, which extends the starting sizes; and
it ends having written `S` elements to `nxt`. -/
structure Ok (szO szF : Sizes) : Prop where
  pos    : 0 < r.S
  hH     : r.H = r.T * r.S + r.S
  sub    : ∀ b n, r.bodySizes szO b = some n → szF b = some n
  outs   : ∀ st ∈ r.body, szF st.out = some st.spec.outSize
  impl   : ∀ st ∈ r.body, Implements st.prog st.spec
  loc    : ∀ st ∈ r.body, SpecLocal szF st.spec
  nxt_sz : sizesAfter r.body (r.bodySizes szO) r.nxt = some r.S

omit [ExactScalar α] in
/-- `Ok.sub` from facts a certificate can decide: the state and each view are
recorded at their sizes, and the outer sizes are kept. -/
theorem sub_of {szO szF : Sizes} (hst : szF r.st = some r.S)
    (hv : ∀ v ∈ r.views, szF v.buf = some v.stride)
    (ho : ∀ b n, szO b = some n → szF b = some n) :
    ∀ b n, r.bodySizes szO b = some n → szF b = some n := by
  intro b n h
  by_cases hb : b = r.st
  · subst hb; simp [bodySizes] at h; subst h; exact hst
  · cases hw : viewOf r.views b with
    | some v =>
      simp [bodySizes, hb, hw] at h; subst h
      have := viewOf_mem hw
      rw [← this.2]; exact hv v this.1
    | none =>
      simp [bodySizes, hb, hw] at h; exact ho b n h

/-- Every state the loop computes agrees with the specified one on the `S`
elements that are the state. -/
theorem state_agree {szO szF : Sizes} (h : r.Ok szO szF) (f : Nat → Buf α) (m : Mem α) :
    ∀ t i, i < r.S → r.runState f m t i = r.specState f t i := by
  intro t
  induction t with
  | zero => intro i _; rfl
  | succ t ih =>
    intro i hi
    have hc : Compat (r.bodySizes szO) (r.envAt f t (r.runState f m t))
        (r.envAt f t (r.specState f t)) := by
      intro b j hj
      by_cases hb : b = r.st
      · subst hb
        simp only [envAt, ite_true]
        exact ih j (hj r.S (by simp [bodySizes]))
      · simp only [envAt, hb, ite_false]
    have hall := stages_correct szF r.body (r.bodySizes szO) _ _ m hc h.sub h.outs h.impl
      h.loc
    exact hall r.nxt i (fun n hn => by rw [h.nxt_sz] at hn; cases hn; exact hi)

/-- **The loop implements its specification.** -/
theorem impl {szO szF : Sizes} (h : r.Ok szO szF) : GImpl r.toG := by
  intro f m q _
  exact r.state_agree h f m (q / r.S) (q % r.S) (Nat.mod_lt _ h.pos)

/-! ## Locality of the loop within an outer chain -/

/-- What makes the loop local with respect to the outer sizes `szO`: it reads the
initial state inside what was written there, and every step's view window inside
its source. Outer buffers the body reads directly are covered by the body's own
locality, since `szF` extends `szO`. -/
structure Local (szO szF : Sizes) : Prop where
  ok      : r.Ok szO szF
  init_in : (szO r.init).all (r.S ≤ ·) = true
  view_in : ∀ v ∈ r.views, (szO v.src).all (r.T * v.stride ≤ ·) = true

theorem window_lt {t T s j : Nat} (ht : t + 1 ≤ T) (hj : j < s) : t * s + j < T * s :=
  calc t * s + j < t * s + s := Nat.add_lt_add_left hj _
    _ = (t + 1) * s := (Nat.succ_mul t s).symm
    _ ≤ T * s := Nat.mul_le_mul_right s ht

theorem spec_local {szO szF : Sizes} (h : r.Local szO szF) : SpecLocal szO r.spec := by
  intro f g hfg q hq
  have hs : ∀ t, t ≤ r.T → ∀ i, i < r.S → r.specState f t i = r.specState g t i := by
    intro t
    induction t with
    | zero =>
      intro _ i hi
      exact hfg r.init i (fun n hn => Nat.lt_of_lt_of_le hi (by
        have := h.init_in; rw [hn] at this; simpa using this))
    | succ t ih =>
      intro ht i hi
      have hc : Compat (r.bodySizes szO) (r.envAt f t (r.specState f t))
          (r.envAt g t (r.specState g t)) := by
        intro b j hj
        by_cases hb : b = r.st
        · subst hb
          simp only [envAt, ite_true]
          exact ih (Nat.le_of_succ_le ht) j (hj r.S (by simp [bodySizes]))
        · cases hv : viewOf r.views b with
          | some v =>
            simp only [envAt, hb, ite_false, hv]
            have hjs : j < v.stride := hj v.stride (by simp [bodySizes, hb, hv])
            exact hfg v.src _ (fun n hn =>
              Nat.lt_of_lt_of_le (window_lt ht hjs) (by
                have := h.view_in v (viewOf_mem hv).1; rw [hn] at this; simpa using this))
          | none =>
            simp only [envAt, hb, ite_false, hv]
            exact hfg b j (fun n hn => hj n (by simp [bodySizes, hb, hv, hn]))
      have hall := specStages_compat szF r.body (r.bodySizes szO) _ _ hc h.ok.sub
        h.ok.outs h.ok.loc
      exact hall r.nxt i (fun n hn => by rw [h.ok.nxt_sz] at hn; cases hn; exact hi)
  have hS := h.ok.pos
  have hq' : q < r.S * (r.T + 1) := by
    have e : r.S * (r.T + 1) = r.T * r.S + r.S := by
      rw [Nat.mul_add_one, Nat.mul_comm]
    rw [e, ← h.ok.hH]; exact hq
  exact hs (q / r.S) (Nat.le_of_lt_succ (Nat.div_lt_of_lt_mul hq')) (q % r.S)
    (Nat.mod_lt _ hS)

end Recur

end VerifiedKernel
