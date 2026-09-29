/-
Max (and min) reductions: max pooling, and max/min over a dimension.

These cannot reuse the summing family, and the reason is worth stating. A masked sum
excludes a lane by having it contribute `zero`, the additive identity. A max has no
identity to contribute: an ordered field has no least element, and *adding* one is
not an option -- `le bot a` for every `a` together with the field axioms yields
`bot ≤ bot - 1 < bot`, so the axiom set becomes inconsistent and every theorem in
the framework silently turns vacuous.

So this family never masks. Instead its index maps **clamp**: the reduction index is
substituted with `min(iv*block + col, K-1)`, so every lane -- in range or not --
reads a genuine element of the window. Lanes past the end read a duplicate, which a
max does not notice. The cost is that the kernel's fold ranges over a multiset with
duplicates while the spec's fold ranges over `[0, K)`, so the proof goes through the
*characterisation* of a maximum (it is an upper bound, and it is attained) rather
than through a rearrangement lemma. `Nat`'s truncating subtraction supplies the
clamp for free: `a - (a - (K-1))` is `min a (K-1)`, needing no new IR node.

The frontend's job is to make the clamp meaningful -- for pooling it must clamp the
*spatial* coordinate into the input, and that this lands inside the window is the
small geometric fact that if a window `[ws, we]` has `ws < 0 ≤ we` then `0` is in
it. That is the frontend's obligation, where "what does this PyTorch module mean"
always lives.
-/
import VerifiedKernel.Kernels.GenRed

namespace VerifiedKernel

open ExactScalar

/-- The clamped reduction index: `min(iv 0 * block + col, K - 1)`, written with
truncating subtraction so no `min` node is needed. -/
def kIEclamped (block K : Nat) : IE :=
  .sub (kIE block) (.sub (kIE block) (.lit (K - 1)))

variable {α : Type} [ExactScalar α]

theorem kIEclamped_eval {block K : Nat} (env : Env α) (i j : Nat) :
    (kIEclamped block K).eval env i j
      = (env.ivs 0 * block + j) - ((env.ivs 0 * block + j) - (K - 1)) := rfl

/-- A max-reducing task. There is no `inRange`: this family clamps rather than
masks, so every lane contributes. -/
structure MaxRed where
  nout : Nat
  /-- reduction extent; must be positive, since a max over nothing is undefined -/
  K : Nat
  offs : Nat → IE
  body : SE
  postOffs : Nat → IE
  post : SE
  nInp : Nat
  /-- A distinguished slot of `body` denoting the *reduction index itself*, as a
  scalar, rather than a buffer read. An argmax needs it: its summand is
  "this position, if it holds the maximum", and the position is `k`. Putting it in
  the slot map keeps `SE` unchanged -- extending `SE.denote` with an index argument
  would have rippled through every family's proofs. -/
  idxSlot : Nat

namespace MaxRed

variable {α : Type} [ExactScalar α]

/-- The element at reduction index `k`. -/
def elem (g : MaxRed) (bufs : Nat → Buf α) (q k : Nat) : α :=
  g.body.denote (fun b => if b = g.idxSlot then ExactScalar.ofNat k
                          else bufs b ((g.offs b).evalQK q k))

def spec (g : MaxRed) : Spec α :=
  { arity := g.nInp
  , outSize := g.nout
  , out := fun ins q =>
      g.post.denote (fun b => match b with
        | 0 => ExactScalar.foldMax g.K (fun k => g.elem ins q k)
        | b + 1 => ins b ((g.postOffs b).evalQK q 0)) }

/-- The element this lane reads, at the clamped reduction index. -/
def summand (g : MaxRed) (block : Nat) : FE :=
  SE.toFEWith
    (fun b => if b = g.idxSlot then .ofI (kIEclamped block g.K)
              else .load b (IE.instWith (kIEclamped block g.K) (g.offs b)) .tt) g.body

/-- The seed: the element at reduction index 0, a genuine element rather than a
sentinel. -/
def seed (g : MaxRed) : FE :=
  SE.toFEWith (fun b => if b = g.idxSlot then .ofI (.lit 0)
                        else .load b (IE.instWith (.lit 0) (g.offs b)) .tt) g.body

def step (g : MaxRed) (block : Nat) : FE := .bin .max (.acc 0) (g.summand block)

def stored (g : MaxRed) (block : Nat) : FE :=
  SE.toFEWith
    (fun b => match b with
      | 0 => .redCol .max block (.acc 0)
      | b + 1 => .load b ((g.postOffs b).instK block) .tt)
    g.post

def prog (g : MaxRed) (block nkb : Nat) : Prog :=
  { grid0 := g.nout, grid1 := 1
  , body := .forAcc nkb g.seed (g.step block)
      (.store 1 1 (.pid 0) (g.stored block) .tt) }

structure Wf (g : MaxRed) : Prop where
  offs_ok : ∀ b, (g.offs b).qkOnly = true
  post_ok : ∀ b, (g.postOffs b).qkOnly = true

theorem summand_accFree (g : MaxRed) (block : Nat) :
    (g.summand block).accFree = true :=
  SE.toFEWith_accFree (fun b => by by_cases h : b = g.idxSlot <;> simp [h, FE.accFree]) g.body

theorem seed_accFree (g : MaxRed) : g.seed.accFree = true :=
  SE.toFEWith_accFree (fun b => by by_cases h : b = g.idxSlot <;> simp [h, FE.accFree]) g.body

/-- The lane reads the element at the clamped index. -/
theorem summand_eval (g : MaxRed) (block : Nat) (hw : Wf g) (bufs : Nat → Buf α)
    (q kb j : Nat) (a : Nat → Nat → α) :
    (g.summand block).eval ((flatEnv bufs q).pushStep kb a) 0 j
      = g.elem bufs q ((kb * block + j) - ((kb * block + j) - (g.K - 1))) := by
  refine SE.toFEWith_eval (fun b => ?_) g.body
  by_cases hb : b = g.idxSlot
  · simp only [hb, if_true, FE.eval, kIEclamped_eval, Env.pushStep_ivs0]
  · have h := IE.instWith_eval
      (env := (flatEnv bufs q).pushStep kb a) (q := q)
      (kIEclamped block g.K) 0 j rfl (g.offs b) (hw.offs_ok b)
    simp only [hb, if_false, FE.eval, BE.eval, if_true, h, Env.pushStep_bufs,
      flatEnv_bufs]
    rfl

/-- The seed reads the element at index 0. -/
theorem seed_eval (g : MaxRed) (hw : Wf g) (bufs : Nat → Buf α) (q : Nat)
    (i j : Nat) :
    g.seed.eval (flatEnv bufs q) i j = g.elem bufs q 0 := by
  refine SE.toFEWith_eval (fun b => ?_) g.body
  by_cases hb : b = g.idxSlot
  · simp only [hb, if_true, FE.eval, IE.eval]
  · have h := IE.instWith_eval
      (env := flatEnv bufs q) (q := q) (.lit 0) i j rfl (g.offs b) (hw.offs_ok b)
    simp only [hb, if_false, FE.eval, BE.eval, if_true, h, flatEnv_bufs]
    rfl

/-- The accumulator of lane `j`: a seeded max-fold over the loop steps.

No appeal to accumulator-independence is needed here: the step is literally
`max acc summand`, and `summand_eval` already holds for an arbitrary accumulator. -/
theorem accOf_max (g : MaxRed) (block : Nat) (hw : Wf g) (bufs : Nat → Buf α)
    (q j : Nat) (nkb : Nat) :
    accOf (flatEnv bufs q) nkb g.seed (g.step block) 0 j
      = ExactScalar.foldMaxFrom (g.elem bufs q 0) nkb
          (fun kb => g.elem bufs q ((kb * block + j) - ((kb * block + j) - (g.K - 1)))) := by
  induction nkb with
  | zero => exact seed_eval g hw bufs q 0 j
  | succ k ih =>
    show ExactScalar.max
      (accOf (flatEnv bufs q) k g.seed (g.step block) 0 j)
      ((g.summand block).eval ((flatEnv bufs q).pushStep k
          (accOf (flatEnv bufs q) k g.seed (g.step block))) 0 j) = _
    rw [ih, summand_eval g block hw bufs q k j _, ExactScalar.foldMaxFrom_succ]

/--
**The max-reduction theorem.** For a positive reduction extent and a loop long
enough to cover it, the clamping kernel computes the spec's max.

The two inequalities are the content. *Kernel ≤ spec*: every lane's clamped index is
below `K`, so every element the kernel folds is one the spec folds. *Spec ≤ kernel*:
every `k < K` is hit by lane `k % block` at step `k / block`, and clamping is the
identity there. Antisymmetry closes it. Duplicates never come up, which is exactly
why this argument is used instead of a rearrangement.
-/
theorem prog_implements (g : MaxRed) (block nkb : Nat) (hw : Wf g)
    (hb : 0 < block) (hK : 0 < g.K) (hcov : g.K ≤ nkb * block) :
    Implements (g.prog block nkb) (g.spec (α := α)) := by
  intro bufs m q hq
  have hq' : q < g.nout := hq
  -- the clamped index map
  let c : Nat → Nat := fun m => m - (m - (g.K - 1))
  have hclt : ∀ m, c m < g.K := fun m => ExactScalar.clamp_lt hK
  have hcid : ∀ m, m < g.K → c m = m := fun m h => ExactScalar.clamp_id h
  let F : Nat → α := fun k => g.elem bufs q k
  let A : Nat → α := fun j =>
    ExactScalar.foldMaxFrom (F 0) nkb (fun kb => F (c (kb * block + j)))
  have hAdef : ∀ j, A j = ExactScalar.foldMaxFrom (F 0) nkb
      (fun kb => F (c (kb * block + j))) := fun _ => rfl
  have hA : ∀ j, accOf (flatEnv bufs q) nkb g.seed (g.step block) 0 j = A j :=
    fun j => accOf_max g block hw bufs q j nkb
  -- kernel ≤ spec
  have hle1 : ExactScalar.le (ExactScalar.foldMax block A)
      (ExactScalar.foldMax g.K F) = true := by
    have hAj : ∀ j, ExactScalar.le (A j) (ExactScalar.foldMax g.K F) = true := by
      intro j
      rw [hAdef j]
      refine ExactScalar.foldMaxFrom_le ?_ (fun kb _ => ?_)
      · exact ExactScalar.le_foldMax (α := α) 0 hK
      · exact ExactScalar.le_foldMax (α := α) _ (hclt _)
    exact ExactScalar.foldMax_le (hAj 0) (fun j _ => hAj j)
  -- spec ≤ kernel
  have hle2 : ExactScalar.le (ExactScalar.foldMax g.K F)
      (ExactScalar.foldMax block A) = true := by
    refine ExactScalar.foldMax_le ?_ (fun k hk => ?_)
    · have h0 : ExactScalar.le (F 0) (A 0) = true := by
        rw [hAdef 0]; exact ExactScalar.le_foldMaxFrom_seed
      exact ExactScalar.le_trans (F 0) (A 0) (ExactScalar.foldMax block A) h0
        ExactScalar.le_foldMax_seed
    · -- lane k % block at step k / block reads exactly F k
      have hj : k % block < block := Nat.mod_lt _ hb
      have hkb : k / block < nkb :=
        Nat.div_lt_of_lt_mul (by rw [Nat.mul_comm] at hcov
                                 exact Nat.lt_of_lt_of_le hk hcov)
      have hrec : (k / block) * block + k % block = k := Nat.div_add_mod' k block
      have hstep : F k = F (c ((k / block) * block + k % block)) := by
        rw [hrec, hcid k hk]
      refine ExactScalar.le_trans (F k) (A (k % block)) (ExactScalar.foldMax block A)
        ?_ (ExactScalar.le_foldMax (α := α) (k % block) hj)
      rw [hstep, hAdef (k % block)]
      exact ExactScalar.le_foldMaxFrom (α := α) (s := F 0) (n := nkb)
        (g := fun kb => F (c (kb * block + k % block))) (k / block) hkb
  have hred : ExactScalar.foldMax block A = ExactScalar.foldMax g.K F :=
    ExactScalar.le_antisymm _ _ hle1 hle2
  -- the stored value is the spec's output
  have hpost : ∀ b : Nat,
      ((fun b => match b with
        | 0 => FE.redCol .max block (.acc 0)
        | b + 1 => FE.load b ((g.postOffs b).instK block) .tt) b).eval
          ((flatEnv bufs q).pushAcc
            (accOf (flatEnv bufs q) nkb g.seed (g.step block))) 0 0
        = (match b with
           | 0 => ExactScalar.foldMax g.K F
           | b + 1 => bufs b ((g.postOffs b).evalQK q 0)) := by
    intro b
    cases b with
    | zero =>
      show RedOp.fold .max block
        (fun p => accOf (flatEnv bufs q) nkb g.seed (g.step block) 0 p) = _
      show ExactScalar.foldMax block
        (fun p => accOf (flatEnv bufs q) nkb g.seed (g.step block) 0 p) = _
      rw [show (fun p => accOf (flatEnv bufs q) nkb g.seed (g.step block) 0 p) = A from
            funext hA]
      exact hred
    | succ b' =>
      have hoff := IE.instK_eval (block := block)
        (env := (flatEnv bufs q).pushAcc (accOf (flatEnv bufs q) nkb g.seed (g.step block)))
        (q := q) (kb := 0) 0 rfl rfl _ (hw.post_ok b')
      simp only [Nat.zero_mul, Nat.add_zero] at hoff
      simp only [FE.eval, BE.eval, if_true, hoff, Env.pushAcc_bufs, flatEnv_bufs]
  rw [show g.prog block nkb = Prog.mk g.nout 1
        (.forAcc nkb g.seed (g.step block) (.store 1 1 (.pid 0) (g.stored block) .tt))
      from rfl, Prog.run_grid1]
  refine gridFold_at (v := (g.spec (α := α)).out bufs q) hq' ?_ ?_
  · intro mm
    rw [forAcc_exec]
    simp only [Stmt.exec]
    rw [store11_at _ _ _ _ q rfl]
    exact SE.toFEWith_eval hpost g.post
  · intro p mm hne
    rw [forAcc_exec]
    simp only [Stmt.exec]
    exact store11_skip _ _ _ _ q (fun h => hne h)

end MaxRed
end VerifiedKernel
