/-
Congruence lemmas: which parts of the environment an expression can actually see.

An accumulator loop's step expression is evaluated in an environment that changes
on every iteration. To reason about such a loop at all, one needs to know that the
*summand* does not depend on the running accumulator -- otherwise the fold is not a
fold. `accFree` is that syntactic condition, and `FE.eval_accFree` is the
corresponding semantic independence.
-/
import VerifiedKernel.Ir

namespace VerifiedKernel

open ExactScalar

/-- Index expressions never read the accumulator stack. -/
theorem IE.eval_congr {α : Type} {env env' : Env α}
    (hp : env.pid = env'.pid) (hi : env.ivs = env'.ivs) :
    ∀ (e : IE) (i j : Nat), e.eval env i j = e.eval env' i j := by
  intro e
  induction e with
  | pid a => intro i j; simp only [IE.eval, hp]
  | row => intro i j; rfl
  | col => intro i j; rfl
  | lit n => intro i j; rfl
  | iv k => intro i j; simp only [IE.eval, hi]
  | rk => intro i j; rfl
  | add a b ha hb => intro i j; simp only [IE.eval, ha, hb]
  | mul a b ha hb => intro i j; simp only [IE.eval, ha, hb]
  | sub a b ha hb => intro i j; simp only [IE.eval, ha, hb]
  | divi a b ha hb => intro i j; simp only [IE.eval, ha, hb]
  | modi a b ha hb => intro i j; simp only [IE.eval, ha, hb]

theorem BE.eval_congr {α : Type} {env env' : Env α}
    (hp : env.pid = env'.pid) (hi : env.ivs = env'.ivs) :
    ∀ (e : BE) (i j : Nat), e.eval env i j = e.eval env' i j := by
  intro e
  induction e with
  | tt => intro i j; rfl
  | cmp c a b => intro i j; simp only [BE.eval, IE.eval_congr hp hi]
  | and a b ha hb => intro i j; simp only [BE.eval, ha, hb]
  | or a b ha hb => intro i j; simp only [BE.eval, ha, hb]
  | not a ha => intro i j; simp only [BE.eval, ha]

/-- An expression that mentions no accumulator. -/
def FE.accFree : FE → Bool
  | .zeroC | .ofI _ => true
  | .load _ _ _ => true
  | .acc _ => false
  | .bin _ a b => a.accFree && b.accFree
  | .un _ a => a.accFree
  | .recip a => a.accFree
  | .sel _ a b => a.accFree && b.accFree
  | .selLe a b t e => a.accFree && b.accFree && t.accFree && e.accFree
  | .dot _ a b => a.accFree && b.accFree
  | .redCol _ _ a => a.accFree
  | .redRow _ _ a => a.accFree

variable {α : Type} [ExactScalar α]

/-- **Accumulator independence.** An `accFree` expression evaluates identically in
any two environments agreeing on program ids, loop counters and buffers. This is
what makes a loop body a summand rather than a recurrence. -/
theorem FE.eval_accFree {env env' : Env α}
    (hp : env.pid = env'.pid) (hi : env.ivs = env'.ivs) (hb : env.bufs = env'.bufs) :
    ∀ (e : FE), e.accFree = true → ∀ (i j : Nat), e.eval env i j = e.eval env' i j := by
  intro e
  induction e with
  | zeroC => intro _ i j; rfl
  | ofI x => intro _ i j; simp only [FE.eval, IE.eval_congr hp hi]
  | load b off mask =>
    intro _ i j
    simp only [FE.eval, IE.eval_congr hp hi, BE.eval_congr hp hi, hb]
  | acc k => intro h; exact absurd h (by simp [FE.accFree])
  | bin op a b ha hb =>
    intro h i j
    simp only [FE.accFree, Bool.and_eq_true] at h
    simp only [FE.eval, ha h.1 i j, hb h.2 i j]
  | un f a ha =>
    intro h i j; simp only [FE.accFree] at h; simp only [FE.eval, ha h i j]
  | recip a ha =>
    intro h i j; simp only [FE.accFree] at h; simp only [FE.eval, ha h i j]
  | sel c a b ha hb =>
    intro h i j
    simp only [FE.accFree, Bool.and_eq_true] at h
    simp only [FE.eval, BE.eval_congr hp hi, ha h.1 i j, hb h.2 i j]
  | selLe a b t e ha hb ht he =>
    intro h i j
    simp only [FE.accFree, Bool.and_eq_true] at h
    simp only [FE.eval, ha h.1.1.1 i j, hb h.1.1.2 i j, ht h.1.2 i j, he h.2 i j]
  | dot k a b ha hb =>
    intro h i j
    simp only [FE.accFree, Bool.and_eq_true] at h
    simp only [FE.eval]
    exact congrArg _ (funext fun p => by rw [ha h.1 i p, hb h.2 p j])
  | redCol op n a ha =>
    intro h i j
    simp only [FE.accFree] at h
    simp only [FE.eval]
    exact congrArg _ (funext fun p => ha h i p)
  | redRow op n a ha =>
    intro h i j
    simp only [FE.accFree] at h
    simp only [FE.eval]
    exact congrArg _ (funext fun p => ha h p j)

end VerifiedKernel
