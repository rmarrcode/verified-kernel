/-
The element-wise family.

One spec language, one kernel template, one proof -- covering every L1 task whose
output element depends only on the input elements at the same flat index. That is
all fourteen activations, the scalar and diagonal products, and the pointwise
stage of every loss.

The theorem is generic over the entire body language `SE`, so *no per-task proof
obligation exists*. What must be checked when a particular task is compiled is
only the two decidable side conditions (`0 < block` and
`outSize ≤ nblocks * block`), which the generator checks before it will emit.
This is the same division of labour a verified compiler uses: prove the
translation once, check the instance's preconditions each time.
-/
import VerifiedKernel.Emit
import VerifiedKernel.AccFree

namespace VerifiedKernel

open ExactScalar

/-- Pointwise scalar expressions. Closed (no `α` parameter) and therefore
directly serializable, which is what lets the Python frontend hand one to the
Lean backend as data.

Constants are *rationals*, not floats: a spec that says `0.044715` should mean the
exact number 44715/1000000, and committing to a float literal in the spec would
bake a rounding decision into the thing being proved. -/
inductive SE where
  | inp (b : Nat)
  /-- `(if neg then -1 else 1) * num / den` -/
  | lit (neg : Bool) (num den : Nat)
  | bin (op : Bop) (a b : SE)
  | un (f : Fn1) (a : SE)
  | recip (a : SE)
  /-- `if a ≤ b then t else e` -/
  | selLe (a b t e : SE)
  deriving Repr, Inhabited

namespace SE

variable {α : Type} [ExactScalar α]

def denote (get : Nat → α) : SE → α
  | .inp b => get b
  | .lit neg num den =>
      if neg then
        ExactScalar.neg (ExactScalar.mul (ExactScalar.ofNat num)
          (ExactScalar.inv (ExactScalar.ofNat den)))
      else
        ExactScalar.mul (ExactScalar.ofNat num) (ExactScalar.inv (ExactScalar.ofNat den))
  | .bin op a b => op.apply (a.denote get) (b.denote get)
  | .un f a => ExactScalar.fn1 f (a.denote get)
  | .recip a => ExactScalar.inv (a.denote get)
  | .selLe a b t e =>
      if ExactScalar.le (a.denote get) (b.denote get)
      then t.denote get else e.denote get

/-- The specification of a pointwise op: output element `q` is the body evaluated
at the inputs' element `q`. -/
def spec (se : SE) (arity n : Nat) : Spec α :=
  { arity := arity
  , outSize := n
  , out := fun ins q => se.denote (fun b => ins b q) }

/-- **The substitution combinator.** Translate a spec body to a kernel body by
saying, once, what each input slot compiles to. Every family in the framework
reuses this: the element-wise family maps slot `b` to a masked load at the lane's
own index, while the reduce family maps slot 0 to an already-reduced tile
expression and the rest to loads at the output index. -/
def toFEWith (f : Nat → FE) : SE → FE
  | .inp b => f b
  | .lit neg num den =>
      if neg then
        .bin .sub .zeroC (.bin .mul (.ofI (.lit num)) (.recip (.ofI (.lit den))))
      else .bin .mul (.ofI (.lit num)) (.recip (.ofI (.lit den)))
  | .bin op a b => .bin op (toFEWith f a) (toFEWith f b)
  | .un fn a => .un fn (toFEWith f a)
  | .recip a => .recip (toFEWith f a)
  | .selLe a b t e =>
      .selLe (toFEWith f a) (toFEWith f b) (toFEWith f t) (toFEWith f e)

/-- **The substitution lemma.** If each slot's kernel expression evaluates to the
value the spec reads from that slot, the whole body agrees. This is the only
lemma any family needs about spec bodies; everything family-specific reduces to
establishing its hypothesis. -/
theorem toFEWith_eval {f : Nat → FE} {env : Env α} {i j : Nat} {get : Nat → α}
    (h : ∀ b, (f b).eval env i j = get b) (se : SE) :
    (toFEWith f se).eval env i j = se.denote get := by
  induction se with
  | inp b => exact h b
  | lit neg num den =>
    cases neg <;>
      simp [toFEWith, denote, FE.eval, Bop.apply, IE.eval, ExactScalar.sub,
        ExactScalar.zero_add]
  | bin op a b ha hb => simp only [toFEWith, FE.eval, denote, ha, hb]
  | un fn a ha => simp only [toFEWith, FE.eval, denote, ha]
  | recip a ha => simp only [toFEWith, FE.eval, denote, ha]
  | selLe a b t e ha hb ht he => simp only [toFEWith, FE.eval, denote, ha, hb, ht, he]

/-- Every slot compiles to a load, so no `dot`/`redRow` appears and the body is
legal in a single-row tile. -/
theorem toFEWith_flatOk {f : Nat → FE} (hf : ∀ b, (f b).flatOk = true) (se : SE) :
    (toFEWith f se).flatOk = true := by
  induction se with
  | inp b => exact hf b
  | lit neg num den => cases neg <;> rfl
  | bin op a b ha hb => simp [toFEWith, FE.flatOk, ha, hb]
  | un fn a ha => simp [toFEWith, FE.flatOk, ha]
  | recip a ha => simp [toFEWith, FE.flatOk, ha]
  | selLe a b t e ha hb ht he => simp [toFEWith, FE.flatOk, ha, hb, ht, he]

/-- A body built from loads mentions no accumulator. -/
theorem toFEWith_accFree {f : Nat → FE} (hf : ∀ b, (f b).accFree = true) (se : SE) :
    (toFEWith f se).accFree = true := by
  induction se with
  | inp b => exact hf b
  | lit neg num den => cases neg <;> rfl
  | bin op a b ha hb => simp [toFEWith, FE.accFree, ha, hb]
  | un fn a ha => simp [toFEWith, FE.accFree, ha]
  | recip a ha => simp [toFEWith, FE.accFree, ha]
  | selLe a b t e ha hb ht he => simp [toFEWith, FE.accFree, ha, hb, ht, he]

/-- The element-wise kernel body: each input read at this lane's own flat index. -/
def toFE (block n : Nat) (se : SE) : FE :=
  toFEWith (fun b => .load b (flatOff block) (flatMask block n)) se

theorem toFE_flatOk (block n : Nat) (se : SE) : (toFE block n se).flatOk = true :=
  toFEWith_flatOk (fun _ => rfl) se

/-- **The lane lemma.** The lane that owns output index `q` evaluates the body at
exactly the inputs' element `q`. -/
theorem toFE_eval {block n : Nat} (hb : 0 < block) (bufs : Nat → Buf α)
    (q : Nat) (hq : q < n) (se : SE) :
    (toFE block n se).eval (flatEnv bufs (q / block)) 0 (q % block)
      = se.denote (fun b => bufs b q) := by
  refine toFEWith_eval (fun b => ?_) se
  simp only [FE.eval, flat_lane_mask hb hq bufs, if_true, flat_lane_off hb bufs q,
    flatEnv_bufs]

/--
**The element-wise theorem.** For every body `se`, every block size and every
grid that covers the output, the flat 1-D kernel implements the pointwise spec.

Note what the hypotheses buy. Drop `hcover` and the tail of the output is never
written; shrink `block` to zero and nothing is. Neither failure is detectable by
the theorem's conclusion being weaker -- the theorem simply cannot be proved, so
the generator cannot emit.
-/
theorem flat_correct {block nblocks n : Nat} (arity : Nat) (se : SE)
    (hb : 0 < block) (hcover : n ≤ nblocks * block) :
    Implements (Prog.flat1d nblocks block n (toFE block n se))
               (se.spec (α := α) arity n) := by
  have h : (se.spec (α := α) arity n).outSize = n := rfl
  refine flat1d_implements (s := se.spec (α := α) arity n) hb (by rw [h]; exact hcover) ?_
  intro bufs q hq
  rw [h] at hq
  exact toFE_eval hb bufs q hq se

end SE
end VerifiedKernel
