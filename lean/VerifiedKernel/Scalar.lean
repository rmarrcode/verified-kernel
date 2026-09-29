/-
The abstract scalar domain in which specifications and kernels are compared.

Design note. Proofs in this framework are carried out over an *abstract ordered
field* with opaque elementary functions, not over `Float`. This is deliberate:

  * `Float` is not associative, so no interesting algebraic rewriting is sound
    over it, and every proof about a tiled reduction would immediately die.
  * The bugs that actually occur in generated kernels are indexing, masking,
    boundary, tiling and reduction-structure bugs. Those are all visible at this
    level of abstraction, and are exactly what these proofs rule out.
  * Rounding is a *quantitative* question, handled separately by an error bound
    (see `Rounding.lean`), not by the equivalence proof.

So a theorem `⟦prog⟧ = spec` here means "same value in exact arithmetic, for all
inputs and all shapes" — the algorithm is right. It does not by itself mean the
float result is bit-identical, and it is not claimed to.
-/

namespace VerifiedKernel

/-- Opaque elementary functions. These carry no algebraic axioms: they are
uninterpreted, so a spec mentioning `tanh` can only be matched by a kernel that
applies `tanh` at the same place. That is the point. -/
inductive Fn1
  | exp | log | tanh | sqrt | erf | abs | floorF
  deriving DecidableEq, Repr, Inhabited

/-- An ordered field with opaque elementary functions.

Theorems are stated generically over any instance, so they hold in every model
(in particular in the reals). No `Float` instance is provided or possible. -/
class ExactScalar (α : Type) where
  zero : α
  one  : α
  add  : α → α → α
  mul  : α → α → α
  neg  : α → α
  /-- Multiplicative inverse; `inv zero` is left unspecified. -/
  inv  : α → α
  /-- Decidable total order. -/
  le   : α → α → Bool
  /-- Opaque elementary functions. -/
  fn1  : Fn1 → α → α

  -- additive commutative group
  add_comm   : ∀ a b : α, add a b = add b a
  add_assoc  : ∀ a b c : α, add (add a b) c = add a (add b c)
  add_zero   : ∀ a : α, add a zero = a
  add_neg    : ∀ a : α, add a (neg a) = zero
  -- multiplicative commutative monoid
  mul_comm   : ∀ a b : α, mul a b = mul b a
  mul_assoc  : ∀ a b c : α, mul (mul a b) c = mul a (mul b c)
  mul_one    : ∀ a : α, mul a one = a
  mul_zero   : ∀ a : α, mul a zero = zero
  -- distributivity
  mul_add    : ∀ a b c : α, mul a (add b c) = add (mul a b) (mul a c)
  -- total order, compatible with the group structure
  le_refl    : ∀ a : α, le a a = true
  le_trans   : ∀ a b c : α, le a b = true → le b c = true → le a c = true
  le_antisymm : ∀ a b : α, le a b = true → le b a = true → a = b
  le_total   : ∀ a b : α, le a b = true ∨ le b a = true

attribute [simp] ExactScalar.add_zero ExactScalar.mul_one ExactScalar.mul_zero
attribute [simp] ExactScalar.le_refl

namespace ExactScalar

variable {α : Type} [ExactScalar α]

/-- `a - b`. -/
def sub (a b : α) : α := add a (neg b)
/-- `a / b`. -/
def div (a b : α) : α := mul a (inv b)

def max (a b : α) : α := if le a b then b else a
def min (a b : α) : α := if le a b then a else b

/-- Embedding of the naturals, used for literals and for counts (e.g. the `1/n`
in a mean). Defined by iterated `add one` so that `ofNat` facts are provable by
induction rather than assumed. -/
def ofNat : Nat → α
  | 0 => zero
  | n + 1 => add (ofNat n) one

instance : Add α := ⟨add⟩
instance : Mul α := ⟨mul⟩
instance : Neg α := ⟨neg⟩
instance : Sub α := ⟨sub⟩
instance : Zero α := ⟨zero⟩
instance : One α := ⟨one⟩

/-- `∑_{i<n} f i`, the reduction primitive every reduce/matmul spec is built
from. Folds from the left so it matches the shape of an accumulator loop. -/
def sum (n : Nat) (f : Nat → α) : α :=
  Nat.rec zero (fun i acc => add acc (f i)) n

/-- `∏_{i<n} f i`. -/
def prod (n : Nat) (f : Nat → α) : α :=
  Nat.rec one (fun i acc => mul acc (f i)) n

@[simp] theorem sum_zero (f : Nat → α) : sum 0 f = zero := rfl

@[simp] theorem sum_succ (n : Nat) (f : Nat → α) :
    sum (n + 1) f = add (sum n f) (f n) := rfl

@[simp] theorem prod_zero (f : Nat → α) : prod 0 f = one := rfl

@[simp] theorem prod_succ (n : Nat) (f : Nat → α) :
    prod (n + 1) f = mul (prod n f) (f n) := rfl

theorem zero_add (a : α) : add zero a = a := by
  rw [add_comm]; exact add_zero a

theorem sum_congr {n : Nat} {f g : Nat → α} (h : ∀ i, i < n → f i = g i) :
    sum n f = sum n g := by
  induction n with
  | zero => rfl
  | succ k ih =>
    simp only [sum_succ]
    rw [ih (fun i hi => h i (Nat.lt_succ_of_lt hi)), h k (Nat.lt_succ_self k)]

theorem prod_congr {n : Nat} {f g : Nat → α} (h : ∀ i, i < n → f i = g i) :
    prod n f = prod n g := by
  induction n with
  | zero => rfl
  | succ k ih =>
    simp only [prod_succ]
    rw [ih (fun i hi => h i (Nat.lt_succ_of_lt hi)), h k (Nat.lt_succ_self k)]

/-- Terms that are zero do not contribute to a sum. This is the workhorse lemma
for masking: a masked-off lane contributes `zero`, so a padded tile computes the
same sum as the unpadded range. -/
theorem sum_eq_of_zero_beyond {n m : Nat} {f : Nat → α} (hnm : n ≤ m)
    (hz : ∀ i, n ≤ i → i < m → f i = zero) :
    sum m f = sum n f := by
  induction m with
  | zero =>
    have : n = 0 := Nat.le_zero.mp hnm
    subst this; rfl
  | succ k ih =>
    rcases Nat.lt_or_ge k n with hk | hk
    · -- k < n and n ≤ k+1 forces n = k+1
      have : n = k + 1 := Nat.le_antisymm hnm (Nat.succ_le_of_lt hk)
      subst this; rfl
    · have hnk : n ≤ k := hk
      simp only [sum_succ]
      rw [hz k hk (Nat.lt_succ_self k), add_zero]
      exact ih hnk (fun i h1 h2 => hz i h1 (Nat.lt_succ_of_lt h2))

/-- Splitting a sum at `n`: the basis of every tiled reduction proof. -/
theorem sum_add_sum (n m : Nat) (f : Nat → α) :
    sum (n + m) f = add (sum n f) (sum m (fun i => f (n + i))) := by
  induction m with
  | zero => simp [add_zero]
  | succ k ih =>
    show sum (n + k + 1) f = _
    simp only [sum_succ]
    rw [ih, add_assoc]

/-! ### Order facts, for max/min reductions

A masked *sum* is easy: excluded lanes contribute `zero`, the additive identity. A
masked *max* has no identity to contribute -- an ordered field has no least element,
and adding one would make these axioms inconsistent (`le bot a` for every `a` gives
`bot ≤ bot - 1 < bot`). The framework therefore never masks a max: index maps clamp
instead, so every lane reads a genuine element of the window, and the fold is over a
multiset that may contain duplicates but no junk.

Duplicates are why these proofs go through the *characterisation* of a maximum --
it is an upper bound, and it is attained -- rather than through a rearrangement
lemma. Idempotence then costs nothing. -/

theorem le_max_left (a b : α) : le a (max a b) = true := by
  unfold max
  by_cases h : le a b = true
  · simp [h]
  · simp only [Bool.not_eq_true] at h
    simp [h]

theorem le_max_right (a b : α) : le b (max a b) = true := by
  unfold max
  by_cases h : le a b = true
  · simp [h]
  · simp only [Bool.not_eq_true] at h
    simp only [h, Bool.false_eq_true, if_false]
    rcases le_total a b with hab | hba
    · rw [h] at hab; exact absurd hab (by simp)
    · exact hba

/-- `max` is the least upper bound. -/
theorem max_le {a b c : α} (ha : le a c = true) (hb : le b c = true) :
    le (max a b) c = true := by
  unfold max
  by_cases h : le a b = true
  · simp only [h, if_true]; exact hb
  · simp only [Bool.not_eq_true] at h
    simp only [h, Bool.false_eq_true, if_false]; exact ha

@[simp] theorem max_self (a : α) : max a a = a := by simp [max]

/-- The max-fold: seeded with `f 0`, since there is no identity to seed with. -/
def foldMax (n : Nat) (f : Nat → α) : α :=
  Nat.rec (f 0) (fun k acc => max acc (f k)) n

@[simp] theorem foldMax_zero (f : Nat → α) : foldMax (α := α) 0 f = f 0 := rfl

@[simp] theorem foldMax_succ (n : Nat) (f : Nat → α) :
    foldMax (n + 1) f = max (foldMax n f) (f n) := rfl

/-- **The fold is an upper bound.** -/
theorem le_foldMax {n : Nat} {f : Nat → α} : ∀ i, i < n → le (f i) (foldMax n f) = true := by
  induction n with
  | zero => intro i hi; exact absurd hi (Nat.not_lt_zero i)
  | succ k ih =>
    intro i hi
    rw [foldMax_succ]
    rcases Nat.lt_or_ge i k with hlt | hge
    · exact le_trans _ _ _ (ih i hlt) (le_max_left _ _)
    · have : i = k := Nat.le_antisymm (Nat.le_of_lt_succ hi) hge
      subst this
      exact le_max_right _ _

/-- The seed is in the fold. -/
theorem le_foldMax_seed {n : Nat} {f : Nat → α} : le (f 0) (foldMax n f) = true := by
  induction n with
  | zero => exact le_refl _
  | succ k ih => rw [foldMax_succ]; exact le_trans _ _ _ ih (le_max_left _ _)

/-- **The fold is the least such bound.** -/
theorem foldMax_le {n : Nat} {f : Nat → α} {c : α}
    (hseed : le (f 0) c = true) (h : ∀ i, i < n → le (f i) c = true) :
    le (foldMax n f) c = true := by
  induction n with
  | zero => exact hseed
  | succ k ih =>
    rw [foldMax_succ]
    exact max_le (ih (fun i hi => h i (Nat.lt_succ_of_lt hi))) (h k (Nat.lt_succ_self k))

/-- A max-fold from an explicit seed. The kernel's accumulator loop has this shape:
each lane starts from the element at reduction index 0 (a genuine element, not a
sentinel) and folds in one element per iteration. -/
def foldMaxFrom (s : α) (n : Nat) (g : Nat → α) : α :=
  Nat.rec s (fun k acc => max acc (g k)) n

@[simp] theorem foldMaxFrom_zero (s : α) (g : Nat → α) : foldMaxFrom s 0 g = s := rfl

@[simp] theorem foldMaxFrom_succ (s : α) (n : Nat) (g : Nat → α) :
    foldMaxFrom s (n + 1) g = max (foldMaxFrom s n g) (g n) := rfl

theorem le_foldMaxFrom_seed {s : α} {n : Nat} {g : Nat → α} :
    le s (foldMaxFrom s n g) = true := by
  induction n with
  | zero => exact le_refl _
  | succ k ih => rw [foldMaxFrom_succ]; exact le_trans _ _ _ ih (le_max_left _ _)

theorem le_foldMaxFrom {s : α} {n : Nat} {g : Nat → α} :
    ∀ i, i < n → le (g i) (foldMaxFrom s n g) = true := by
  induction n with
  | zero => intro i hi; exact absurd hi (Nat.not_lt_zero i)
  | succ k ih =>
    intro i hi
    rw [foldMaxFrom_succ]
    rcases Nat.lt_or_ge i k with hlt | hge
    · exact le_trans _ _ _ (ih i hlt) (le_max_left _ _)
    · have : i = k := Nat.le_antisymm (Nat.le_of_lt_succ hi) hge
      subst this
      exact le_max_right _ _

theorem foldMaxFrom_le {s : α} {n : Nat} {g : Nat → α} {c : α}
    (hs : le s c = true) (h : ∀ i, i < n → le (g i) c = true) :
    le (foldMaxFrom s n g) c = true := by
  induction n with
  | zero => exact hs
  | succ k ih =>
    rw [foldMaxFrom_succ]
    exact max_le (ih (fun i hi => h i (Nat.lt_succ_of_lt hi))) (h k (Nat.lt_succ_self k))

/-- `foldMax` is the seeded fold started at the first element. -/
theorem foldMax_eq_from (n : Nat) (f : Nat → α) : foldMax n f = foldMaxFrom (f 0) n f := rfl

/-- Max-folds agree when their summands do. Agreement is needed at the seed as well
as on `[0, n)`, since the fold starts from `f 0`. -/
theorem foldMax_congr {n : Nat} {f g : Nat → α}
    (h0 : f 0 = g 0) (h : ∀ i, i < n → f i = g i) : foldMax n f = foldMax n g := by
  induction n with
  | zero => exact h0
  | succ k ih =>
    simp only [foldMax_succ, ih (fun i hi => h i (Nat.lt_succ_of_lt hi)),
      h k (Nat.lt_succ_self k)]

/-- Two max-folds over sets that bound each other are equal. This is how a tiled,
duplicate-containing fold is shown equal to a contiguous one. -/
theorem foldMax_eq {n m : Nat} {f g : Nat → α}
    (h1 : le (foldMax n f) (foldMax m g) = true)
    (h2 : le (foldMax m g) (foldMax n f) = true) :
    foldMax n f = foldMax m g :=
  le_antisymm _ _ h1 h2

/-! `a - (a - (c-1))` is `min a (c-1)` over `Nat`. Truncating subtraction gives
clamping *below* for free; this is how the backend clamps *above* without needing a
`min` node, and it is why a max reduction can avoid masking entirely -- every lane,
in range or not, reads a genuine element of the window. -/

/-- A clamped index is in range. -/
theorem clamp_lt {a c : Nat} (hc : 0 < c) : a - (a - (c - 1)) < c := by omega

/-- Clamping is the identity on indices already in range. -/
theorem clamp_id {a c : Nat} (h : a < c) : a - (a - (c - 1)) = a := by omega

/-! ### The algebra of tiled reductions

A tiled reduction computes its answer in a different order and a different
nesting from the spec's single fold. These four lemmas are what license that
rearrangement, and they are the reason the scalar domain is an abstract field
rather than `Float`: over `Float` every one of them is false. -/

@[simp] theorem sum_const_zero (n : Nat) : sum (α := α) n (fun _ => zero) = zero := by
  induction n with
  | zero => rfl
  | succ k ih => simp only [sum_succ, ih, add_zero]

/-- Sums add pointwise. -/
theorem sum_add_distrib (n : Nat) (f h : Nat → α) :
    sum n (fun i => add (f i) (h i)) = add (sum n f) (sum n h) := by
  induction n with
  | zero => simp [zero_add]
  | succ k ih =>
    simp only [sum_succ, ih]
    -- (Sf + Sh) + (f k + h k) = (Sf + f k) + (Sh + h k)
    rw [add_assoc, ← add_assoc (sum k h) (f k) (h k), add_comm (sum k h) (f k),
        add_assoc (f k) (sum k h) (h k), ← add_assoc]

/-- **Fubini for finite sums.** A tile accumulator sums over loop steps within
each lane; the spec sums over the flattened index. Exchanging the two nestings is
exactly this lemma. -/
theorem sum_comm (A B : Nat) (g : Nat → Nat → α) :
    sum A (fun a => sum B (fun b => g a b)) = sum B (fun b => sum A (fun a => g a b)) := by
  induction A with
  | zero => simp
  | succ k ih =>
    simp only [sum_succ, ih]
    exact (sum_add_distrib B (fun b => sum k (fun a => g a b)) (fun b => g k b)).symm

/-- **Splitting a flat range into tiles.** `∑_{i < A*B} g i` reassociates into a
sum over tiles of a sum over lanes. With `sum_eq_of_zero_beyond` handling the
masked tail, this is what connects a blocked loop to a contiguous reduction. -/
theorem sum_mul_split (A B : Nat) (g : Nat → α) :
    sum (A * B) g = sum A (fun a => sum B (fun b => g (a * B + b))) := by
  induction A with
  | zero => simp
  | succ k ih =>
    have hmul : (k + 1) * B = k * B + B := by rw [Nat.succ_mul]
    rw [hmul, sum_add_sum, ih, sum_succ]

end ExactScalar
end VerifiedKernel
