/-
Translation from `TritonIR` to a rank-annotated model of the Triton subset we
emit, together with the theorem that translation preserves denotation.

Why this step is not vacuous. The IR is deliberately coordinate-free: `row` and
`col` are the current tile coordinate, so broadcasting is invisible and cannot be
got wrong. Real Triton has no such luxury -- a rank-1 `tl.arange(0, R)` must be
spelled `[:, None]` to vary along rows and `[None, :]` to vary along columns, and
choosing wrong is a classic silent-wrong-answer bug (the tile still has a legal
shape; it just transposes your kernel). Emission must therefore *reconstruct*
rank information that the IR does not carry, and `emit_ie_sound` below is the
statement that it reconstructs it correctly.

What remains trusted after this file: that `PT.eval` is a faithful model of
Triton's own `tl.arange / tl.load / tl.store / tl.dot / tl.sum` and of its
broadcasting rules. That assumption is discharged empirically by
`harness/axiom_tests.py`, which differential-tests each modeled operation
against real Triton, and it is listed in the README's trusted base.
-/
import VerifiedKernel.Coverage

namespace VerifiedKernel

open ExactScalar

/-! ## Ranks

The four broadcast shapes a 2-D Triton tile program can have. Tracking this
finite lattice is enough to model Triton's broadcasting exactly. -/

inductive Rk | sc | rv | cv | mt
  deriving DecidableEq, Repr, Inhabited

namespace Rk

/-- Triton's broadcast join. -/
def join : Rk → Rk → Rk
  | sc, r => r
  | r, sc => r
  | rv, rv => rv
  | cv, cv => cv
  | _, _ => mt

-- Note: `Rk` is carried as a computed annotation for the renderer and for
-- validation. Nothing below depends on a soundness theorem about it, because the
-- broadcast choice is made explicit in the target AST itself (`arangeRows` vs
-- `arangeCols`) rather than inferred -- which is what `emitIE_sound` pins down.

end Rk

/-! ## The target language

A model of the Triton subset the backend emits. Unlike `IE`/`FE`, tiles here are
explicitly ranked, and `arange` must say which axis it spans. -/

inductive PIE where
  /-- `tl.program_id(axis)` -- scalar -/
  | pid (axis : Nat)
  /-- `tl.arange(0, n)[:, None]` -- varies along rows -/
  | arangeRows (n : Nat)
  /-- `tl.arange(0, n)[None, :]` -- varies along columns -/
  | arangeCols (n : Nat)
  /-- `tl.arange(0, n)` at rank 1, used when the tile has a single row -/
  | arangeFlat (n : Nat)
  | lit (n : Nat)
  /-- a Python-level loop variable -/
  | loopVar (k : Nat)
  | add (a b : PIE) | mul (a b : PIE) | sub (a b : PIE)
  | divi (a b : PIE) | modi (a b : PIE)
  deriving Repr, Inhabited

/-- Denotation of a target index expression, at tile coordinate `(i, j)`. -/
def PIE.eval (env : Env α) (i j : Nat) : PIE → Nat
  | .pid a => env.pid a
  | .arangeRows _ => i
  | .arangeCols _ => j
  | .arangeFlat _ => j
  | .lit n => n
  | .loopVar k => env.ivs k
  | .add a b => a.eval env i j + b.eval env i j
  | .mul a b => a.eval env i j * b.eval env i j
  | .sub a b => a.eval env i j - b.eval env i j
  | .divi a b => a.eval env i j / b.eval env i j
  | .modi a b => a.eval env i j % b.eval env i j

/-- Rank of a target index expression, computed structurally. -/
def PIE.rank : PIE → Rk
  | .pid _ => .sc
  | .lit _ => .sc
  | .loopVar _ => .sc
  | .arangeRows _ => .cv
  | .arangeCols _ => .rv
  | .arangeFlat _ => .rv
  | .add a b | .mul a b | .sub a b | .divi a b | .modi a b =>
      Rk.join a.rank b.rank

/-! ## Translation

`tileRank` records the shape of the tile being emitted: a single-row tile emits
rank-1 `tl.arange`, a genuinely 2-D tile emits the broadcast forms. Getting this
wrong is exactly the bug class the theorem below excludes. -/

/-- Whether the enclosing tile has more than one row. -/
inductive TileKind | flat | twoD
  deriving DecidableEq, Repr

/-- Emit an index expression. `rows`/`cols` are the enclosing tile extents. -/
def emitIE (tk : TileKind) (rows cols : Nat) : IE → PIE
  | .pid a => .pid a
  | .row => match tk with
      | .flat => .lit 0          -- a flat tile has exactly one row, so `row` is 0
      | .twoD => .arangeRows rows
  | .col => match tk with
      | .flat => .arangeFlat cols
      | .twoD => .arangeCols cols
  | .lit n => .lit n
  | .iv k => .loopVar k
  -- `rk` must be eliminated by `IE.instK` before emission; reaching here would
  -- mean a family handed the backend an un-substituted index map.
  | .rk => .lit 0
  | .add a b => .add (emitIE tk rows cols a) (emitIE tk rows cols b)
  | .mul a b => .mul (emitIE tk rows cols a) (emitIE tk rows cols b)
  | .sub a b => .sub (emitIE tk rows cols a) (emitIE tk rows cols b)
  | .divi a b => .divi (emitIE tk rows cols a) (emitIE tk rows cols b)
  | .modi a b => .modi (emitIE tk rows cols a) (emitIE tk rows cols b)

/--
**Soundness of index emission.** For a flat tile the claim is conditional on the
row coordinate being `0`, which is exactly the invariant a `1 × cols` tile
satisfies -- and `storeTile_row1` is what establishes it at the use site. For a
2-D tile the claim is unconditional.

This is the theorem that pins down the `[:, None]` / `[None, :]` choice: swapping
`arangeRows` for `arangeCols` in `emitIE` makes it unprovable.
-/
theorem emitIE_sound (env : Env α) (rows cols : Nat) :
    ∀ (e : IE) (i j : Nat),
      (tk : TileKind) → (tk = .flat → i = 0) →
      (emitIE tk rows cols e).eval env i j = e.eval env i j := by
  intro e
  induction e with
  | pid a => intro i j tk _; rfl
  | row =>
    intro i j tk h
    cases tk with
    | flat => exact (h rfl).symm
    | twoD => rfl
  | col => intro i j tk _; cases tk <;> rfl
  | lit n => intro i j tk _; rfl
  | iv k => intro i j tk _; rfl
  | rk => intro i j tk _; rfl
  | add a b ha hb => intro i j tk h; simp only [emitIE, PIE.eval, IE.eval, ha i j tk h, hb i j tk h]
  | mul a b ha hb => intro i j tk h; simp only [emitIE, PIE.eval, IE.eval, ha i j tk h, hb i j tk h]
  | sub a b ha hb => intro i j tk h; simp only [emitIE, PIE.eval, IE.eval, ha i j tk h, hb i j tk h]
  | divi a b ha hb => intro i j tk h; simp only [emitIE, PIE.eval, IE.eval, ha i j tk h, hb i j tk h]
  | modi a b ha hb => intro i j tk h; simp only [emitIE, PIE.eval, IE.eval, ha i j tk h, hb i j tk h]

/-- Target mask expressions. -/
inductive PBE where
  | tt
  | cmp (c : Cmp) (a b : PIE)
  | and (a b : PBE) | or (a b : PBE) | not (a : PBE)
  deriving Repr, Inhabited

def PBE.eval (env : Env α) (i j : Nat) : PBE → Bool
  | .tt => true
  | .cmp c a b => c.apply (a.eval env i j) (b.eval env i j)
  | .and a b => a.eval env i j && b.eval env i j
  | .or a b => a.eval env i j || b.eval env i j
  | .not a => !(a.eval env i j)

/-! ## Scalar expression emission

`PFE` mirrors `FE` but with target index expressions in the offset and mask
positions. The structural part of the translation is uninteresting; the content
is that the index positions go through `emitIE`, and that `dot`/`redRow` -- the
two nodes that evaluate a subexpression at a *different row* -- are rejected in
flat mode, where the row coordinate is pinned to 0. -/

inductive PFE where
  | zeroC
  | ofI (e : PIE)
  | load (buf : Nat) (off : PIE) (mask : PBE)
  | bin (op : Bop) (a b : PFE)
  | un (f : Fn1) (a : PFE)
  | recip (a : PFE)
  | sel (c : PBE) (a b : PFE)
  | selLe (a b t e : PFE)
  | acc (k : Nat)
  | dot (kdim : Nat) (a b : PFE)
  | redCol (op : RedOp) (n : Nat) (a : PFE)
  | redRow (op : RedOp) (n : Nat) (a : PFE)
  deriving Repr, Inhabited

variable {α : Type} [ExactScalar α]

def PFE.eval (env : Env α) (i j : Nat) : PFE → α
  | .zeroC => ExactScalar.zero
  | .ofI e => ExactScalar.ofNat (e.eval env i j)
  | .load b off mask =>
      if mask.eval env i j then env.bufs b (off.eval env i j) else ExactScalar.zero
  | .bin op a b => op.apply (a.eval env i j) (b.eval env i j)
  | .un f a => ExactScalar.fn1 f (a.eval env i j)
  | .recip a => ExactScalar.inv (a.eval env i j)
  | .sel c a b => if c.eval env i j then a.eval env i j else b.eval env i j
  | .selLe a b t e =>
      if ExactScalar.le (a.eval env i j) (b.eval env i j)
      then t.eval env i j else e.eval env i j
  | .acc k => env.accs k i j
  | .dot kdim a b =>
      ExactScalar.sum kdim (fun p => ExactScalar.mul (a.eval env i p) (b.eval env p j))
  | .redCol op n a => op.fold n (fun p => a.eval env i p)
  | .redRow op n a => op.fold n (fun p => a.eval env p j)

/-- Whether an expression may appear in a single-row tile. `dot` and `redRow`
evaluate an operand at a row other than the current one, so they need a genuinely
2-D tile; admitting them in flat mode is precisely the bug this rules out. -/
def FE.flatOk : FE → Bool
  | .zeroC | .ofI _ | .acc _ => true
  | .load _ _ _ => true
  | .bin _ a b => a.flatOk && b.flatOk
  | .un _ a => a.flatOk
  | .recip a => a.flatOk
  | .sel _ a b => a.flatOk && b.flatOk
  | .selLe a b t e => a.flatOk && b.flatOk && t.flatOk && e.flatOk
  | .redCol _ _ a => a.flatOk
  | .dot _ _ _ => false
  | .redRow _ _ _ => false

def emitBE (tk : TileKind) (rows cols : Nat) : BE → PBE
  | .tt => .tt
  | .cmp c a b => .cmp c (emitIE tk rows cols a) (emitIE tk rows cols b)
  | .and a b => .and (emitBE tk rows cols a) (emitBE tk rows cols b)
  | .or a b => .or (emitBE tk rows cols a) (emitBE tk rows cols b)
  | .not a => .not (emitBE tk rows cols a)

theorem emitBE_sound (env : Env α) (rows cols : Nat) :
    ∀ (e : BE) (i j : Nat) (tk : TileKind), (tk = .flat → i = 0) →
      (emitBE tk rows cols e).eval env i j = e.eval env i j := by
  intro e
  induction e with
  | tt => intro i j tk _; rfl
  | cmp c a b =>
    intro i j tk h
    simp only [emitBE, PBE.eval, BE.eval, emitIE_sound env rows cols a i j tk h,
      emitIE_sound env rows cols b i j tk h]
  | and a b ha hb => intro i j tk h; simp only [emitBE, PBE.eval, BE.eval, ha i j tk h, hb i j tk h]
  | or a b ha hb => intro i j tk h; simp only [emitBE, PBE.eval, BE.eval, ha i j tk h, hb i j tk h]
  | not a ha => intro i j tk h; simp only [emitBE, PBE.eval, BE.eval, ha i j tk h]

def emitFE (tk : TileKind) (rows cols : Nat) : FE → PFE
  | .zeroC => .zeroC
  | .ofI e => .ofI (emitIE tk rows cols e)
  | .load b off mask =>
      .load b (emitIE tk rows cols off) (emitBE tk rows cols mask)
  | .bin op a b => .bin op (emitFE tk rows cols a) (emitFE tk rows cols b)
  | .un f a => .un f (emitFE tk rows cols a)
  | .recip a => .recip (emitFE tk rows cols a)
  | .sel c a b => .sel (emitBE tk rows cols c) (emitFE tk rows cols a) (emitFE tk rows cols b)
  | .selLe a b t e =>
      .selLe (emitFE tk rows cols a) (emitFE tk rows cols b)
             (emitFE tk rows cols t) (emitFE tk rows cols e)
  | .acc k => .acc k
  | .dot kdim a b => .dot kdim (emitFE tk rows cols a) (emitFE tk rows cols b)
  | .redCol op n a => .redCol op n (emitFE tk rows cols a)
  | .redRow op n a => .redRow op n (emitFE tk rows cols a)

/-- **Soundness of scalar emission.** In flat mode this holds for every
`flatOk` expression at row 0; in 2-D mode it holds unconditionally. -/
theorem emitFE_sound (env : Env α) (rows cols : Nat) :
    ∀ (e : FE) (i j : Nat) (tk : TileKind),
      (tk = .flat → i = 0) → (tk = .flat → e.flatOk = true) →
      (emitFE tk rows cols e).eval env i j = e.eval env i j := by
  intro e
  induction e with
  | zeroC => intro i j tk _ _; rfl
  | acc k => intro i j tk _ _; rfl
  | ofI e => intro i j tk h _; simp only [emitFE, PFE.eval, FE.eval, emitIE_sound env rows cols e i j tk h]
  | load b off mask =>
    intro i j tk h _
    simp only [emitFE, PFE.eval, FE.eval, emitIE_sound env rows cols off i j tk h,
      emitBE_sound env rows cols mask i j tk h]
  | bin op a b ha hb =>
    intro i j tk h hf
    have hfa : tk = .flat → a.flatOk = true := fun e => by
      have := hf e; simp only [FE.flatOk, Bool.and_eq_true] at this; exact this.1
    have hfb : tk = .flat → b.flatOk = true := fun e => by
      have := hf e; simp only [FE.flatOk, Bool.and_eq_true] at this; exact this.2
    simp only [emitFE, PFE.eval, FE.eval, ha i j tk h hfa, hb i j tk h hfb]
  | un f a ha =>
    intro i j tk h hf
    simp only [emitFE, PFE.eval, FE.eval, ha i j tk h (fun e => by have := hf e; simpa [FE.flatOk] using this)]
  | recip a ha =>
    intro i j tk h hf
    simp only [emitFE, PFE.eval, FE.eval, ha i j tk h (fun e => by have := hf e; simpa [FE.flatOk] using this)]
  | sel c a b ha hb =>
    intro i j tk h hf
    have hfa : tk = .flat → a.flatOk = true := fun e => by
      have := hf e; simp only [FE.flatOk, Bool.and_eq_true] at this; exact this.1
    have hfb : tk = .flat → b.flatOk = true := fun e => by
      have := hf e; simp only [FE.flatOk, Bool.and_eq_true] at this; exact this.2
    simp only [emitFE, PFE.eval, FE.eval, emitBE_sound env rows cols c i j tk h,
      ha i j tk h hfa, hb i j tk h hfb]
  | selLe a b t e ha hb ht he =>
    intro i j tk h hf
    have H : ∀ x : Bool, ∀ y : Bool, ∀ z : Bool, ∀ w : Bool,
        (x && y && z && w) = true → x = true ∧ y = true ∧ z = true ∧ w = true := by
      intro x y z w hx
      simp only [Bool.and_eq_true] at hx
      exact ⟨hx.1.1.1, hx.1.1.2, hx.1.2, hx.2⟩
    have hs : tk = .flat → (a.flatOk = true ∧ b.flatOk = true ∧ t.flatOk = true ∧ e.flatOk = true) :=
      fun ee => by have := hf ee; simp only [FE.flatOk] at this; exact H _ _ _ _ this
    simp only [emitFE, PFE.eval, FE.eval,
      ha i j tk h (fun ee => (hs ee).1), hb i j tk h (fun ee => (hs ee).2.1),
      ht i j tk h (fun ee => (hs ee).2.2.1), he i j tk h (fun ee => (hs ee).2.2.2)]
  | redCol op n a ha =>
    intro i j tk h hf
    simp only [emitFE, PFE.eval, FE.eval]
    congr 1
    funext pp
    exact ha i pp tk h (fun e => by have := hf e; simpa [FE.flatOk] using this)
  | dot kdim a b ha hb =>
    intro i j tk h hf
    cases tk with
    | flat => exact absurd (hf rfl) (by simp [FE.flatOk])
    | twoD =>
      simp only [emitFE, PFE.eval, FE.eval]
      congr 1
      funext pp
      rw [ha i pp .twoD (by intro c; cases c) (by intro c; cases c),
          hb pp j .twoD (by intro c; cases c) (by intro c; cases c)]
  | redRow op n a ha =>
    intro i j tk h hf
    cases tk with
    | flat => exact absurd (hf rfl) (by simp [FE.flatOk])
    | twoD =>
      simp only [emitFE, PFE.eval, FE.eval]
      congr 1
      funext pp
      exact ha pp j .twoD (by intro c; cases c) (by intro c; cases c)

end VerifiedKernel
