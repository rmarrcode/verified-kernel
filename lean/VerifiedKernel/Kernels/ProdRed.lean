/-
The multiplicative twin of `GenRed`, for cumulative products.

Everything is the additive family with `mul` for `add` and `one` for `zero`. That
substitution is sound because a product *has* an identity, so masked-off lanes can
contribute `one` and no clamping is needed -- the manoeuvre `MaxRed` had to make
because an ordered field has no least element.

The proof is the same three-step rearrangement: exchange the lane/step nesting
(`prod_comm`), flatten `(kb, j)` into one index (`prod_mul_split`), and drop the
masked tail (`prod_eq_of_one_beyond`).
-/
import VerifiedKernel.Kernels.GenRed

namespace VerifiedKernel

open ExactScalar

variable {α : Type} [ExactScalar α]

/-! ## The family -/

/--
A reducing task: `out[q] = post(∑_{k<K} body(inputs at offs[b](q,k)))`.

`offs b` is input `b`'s index map for the reduced stage, and `postOffs b` its map
for the post stage (where `rk` is unused). `post` uses slot `0` for the reduced
value and slot `b+1` for input `b`.

`inRange` is an extra guard evaluated on `(q, k)`: a convolution's window runs off
the edge of a padded input, and those taps must contribute zero rather than read
out of bounds. Restricting `K` alone cannot express that, because which taps are
valid depends on `q`.
-/
structure ProdRed where
  /-- number of outputs (also the grid size) -/
  nout : Nat
  /-- reduction extent -/
  K : Nat
  /-- index map per input, reduced stage -/
  offs : Nat → IE
  /-- extra validity guard on `(q, k)`, e.g. padding bounds -/
  inRange : BE
  /-- the summand -/
  body : SE
  /-- index map per input, post stage -/
  postOffs : Nat → IE
  /-- post-processing; slot 0 is the reduced value -/
  post : SE
  /-- a guard on the *output* index: where it fails the output is zero. This is
  what expresses `triu`/`tril` of a product, or any masked output, without a
  second pass. Mentions `pid` only. -/
  outGuard : BE
  nInp : Nat
  /-- A distinguished slot of `body` denoting the *reduction index itself*, as a
  scalar, rather than a buffer read. A gather uses it: "this element, if its
  position equals the label" is a comparison against `k`, which keeps the index map
  a function of `q` and `k` alone and so keeps `instK_eval` true. Set it outside the
  buffer range when unused. -/
  idxSlot : Nat

/-! ## The loop and the tiling, multiplicatively -/

/-- The accumulator of a product loop, the analogue of `accOf_sum`. -/
theorem accOf_prod {env : Env α} {g : FE} (hg : g.accFree = true) (i j : Nat) (n : Nat) :
    accOf env n .oneC (.bin .mul (.acc 0) g) i j
      = ExactScalar.prod n
          (fun k => g.eval (env.pushStep k (fun _ _ => ExactScalar.zero)) i j) := by
  induction n with
  | zero => rfl
  | succ k ih =>
    show Bop.apply .mul _ _ = _
    rw [ExactScalar.prod_succ]
    show ExactScalar.mul (accOf env k .oneC (.bin .mul (.acc 0) g) i j) _ = _
    rw [ih]
    exact congrArg _ (FE.eval_accFree
      (env := env.pushStep k (accOf env k .oneC (.bin .mul (.acc 0) g)))
      (env' := env.pushStep k (fun _ _ => ExactScalar.zero))
      rfl rfl rfl g hg i j)

/-- A tiled, masked product equals the contiguous one: exchange the lane/step
nesting, flatten the index, drop the masked tail. -/
theorem prod_tile_mask (block nkb K : Nat) (f : Nat → α) (hK : K ≤ nkb * block) :
    ExactScalar.prod block (fun p => ExactScalar.prod nkb
        (fun kb => if kb * block + p < K then f (kb * block + p) else ExactScalar.one))
      = ExactScalar.prod K f := by
  rw [ExactScalar.prod_comm block nkb
    (fun p kb => if kb * block + p < K then f (kb * block + p) else ExactScalar.one)]
  rw [← ExactScalar.prod_mul_split nkb block
    (fun i => if i < K then f i else ExactScalar.one)]
  rw [ExactScalar.prod_eq_of_one_beyond hK (fun i h1 _ => if_neg (Nat.not_lt.mpr h1))]
  exact ExactScalar.prod_congr (fun i hi => if_pos hi)

namespace ProdRed

variable {α : Type} [ExactScalar α]

/-- Whether the lane's `(q, k)` contributes: in range of the reduction *and*
passing the family's guard. -/
def live (g : ProdRed) : BE := .and (.cmp .lt .rk (.lit g.K)) g.inRange

def spec (g : ProdRed) : Spec α :=
  { arity := g.nInp
  , outSize := g.nout
  , out := fun ins q =>
      let red := ExactScalar.prod g.K (fun k =>
        if (g.inRange).evalQK q k
        then g.body.denote (fun b => if b = g.idxSlot then ExactScalar.ofNat k
                                     else ins b ((g.offs b).evalQK q k))
        else ExactScalar.one)
      if (g.outGuard).evalQK q 0 then
        g.post.denote (fun b => match b with
          | 0 => red
          | b + 1 => ins b ((g.postOffs b).evalQK q 0))
      else ExactScalar.one }

/-- The masked summand. Note the mask guards the *summand*, not merely the loads:
a body like `exp x` sends a zeroed load to `1`, which would corrupt the sum. -/
def summand (g : ProdRed) (block : Nat) : FE :=
  .sel ((g.live).instK block)
    (SE.toFEWith
      (fun b => if b = g.idxSlot then .ofI (kIE block)
                else .load b ((g.offs b).instK block) ((g.live).instK block)) g.body)
    FE.oneC

def step (g : ProdRed) (block : Nat) : FE := .bin .mul (.acc 0) (g.summand block)

def stored (g : ProdRed) (block : Nat) : FE :=
  .sel ((g.outGuard).instK block)
    (SE.toFEWith
      (fun b => match b with
        | 0 => .redCol .prod block (.acc 0)
        | b + 1 => .load b ((g.postOffs b).instK block) .tt)
      g.post)
    FE.oneC

def prog (g : ProdRed) (block nkb : Nat) : Prog :=
  { grid0 := g.nout, grid1 := 1
  , body := .forAcc nkb FE.oneC (g.step block)
      (.store 1 1 (.pid 0) (g.stored block) .tt) }

/-- Well-formedness: every index map and the guard mention only `pid` and `rk`. -/
structure Wf (g : ProdRed) : Prop where
  offs_ok : ∀ b, (g.offs b).qkOnly = true
  post_ok : ∀ b, (g.postOffs b).qkOnly = true
  range_ok : g.inRange.qkOnly = true
  guard_ok : g.outGuard.qkOnly = true

theorem summand_accFree (g : ProdRed) (block : Nat) :
    (g.summand block).accFree = true := by
  have h := SE.toFEWith_accFree
    (f := fun b => if b = g.idxSlot then FE.ofI (kIE block)
                   else FE.load b ((g.offs b).instK block) ((g.live).instK block))
    (fun b => by by_cases hb : b = g.idxSlot <;> simp [hb, FE.accFree]) g.body
  simp [summand, FE.accFree, h]

theorem live_eval (g : ProdRed) (block : Nat) (hw : Wf g) (bufs : Nat → Buf α)
    (q kb j : Nat) (a : Nat → Nat → α) :
    ((g.live).instK block).eval ((flatEnv bufs q).pushStep kb a) 0 j
      = (decide (kb * block + j < g.K) && (g.inRange).evalQK q (kb * block + j)) := by
  have hq : (g.live).qkOnly = true := by
    simp [live, BE.qkOnly, IE.qkOnly, hw.range_ok]
  rw [BE.instK_eval (block := block) (env := (flatEnv bufs q).pushStep kb a)
    (q := q) (kb := kb) j rfl rfl _ hq]
  rfl

/-- The summand evaluates to the spec's masked summand. -/
theorem summand_eval (g : ProdRed) (block : Nat) (hw : Wf g) (bufs : Nat → Buf α)
    (q kb j : Nat) (a : Nat → Nat → α) :
    (g.summand block).eval ((flatEnv bufs q).pushStep kb a) 0 j
      = (if kb * block + j < g.K then
           (if (g.inRange).evalQK q (kb * block + j)
            then g.body.denote (fun b =>
                if b = g.idxSlot then ExactScalar.ofNat (kb * block + j)
                else bufs b ((g.offs b).evalQK q (kb * block + j)))
            else ExactScalar.one)
         else ExactScalar.one) := by
  have hl := live_eval g block hw bufs q kb j a
  simp only [summand, FE.eval, hl]
  by_cases h1 : kb * block + j < g.K
  · by_cases h2 : (g.inRange).evalQK q (kb * block + j) = true
    · simp only [h1, h2, decide_true, Bool.and_true, if_true]
      refine SE.toFEWith_eval (fun b => ?_) g.body
      by_cases hb : b = g.idxSlot
      · simp only [hb, if_true, FE.eval, kIE, IE.eval, Env.pushStep_ivs0]
      · simp only [hb, if_false, FE.eval, hl, h1, h2, decide_true, Bool.and_true,
          if_true,
          IE.instK_eval (block := block) (env := (flatEnv bufs q).pushStep kb a)
            (q := q) (kb := kb) j rfl rfl _ (hw.offs_ok b),
          Env.pushStep_bufs, flatEnv_bufs]
    · simp only [Bool.not_eq_true] at h2
      simp only [h1, h2, decide_true, Bool.and_false, Bool.false_eq_true, if_false,
        if_true]
  · simp only [h1, decide_false, Bool.false_and, Bool.false_eq_true, if_false]

/--
**The general reduction theorem.** For any well-formed index map, any block size,
and any loop long enough to cover the reduced axis, the kernel implements the
spec.
-/
theorem prog_implements (g : ProdRed) (block nkb : Nat) (hw : Wf g)
    (hb : 0 < block) (hK : g.K ≤ nkb * block) :
    Implements (g.prog block nkb) (g.spec (α := α)) := by
  intro bufs m q hq
  have hq' : q < g.nout := hq
  have hred : ExactScalar.prod block
      (fun p => accOf (flatEnv bufs q) nkb FE.oneC (g.step block) 0 p)
      = ExactScalar.prod g.K (fun k =>
          if (g.inRange).evalQK q k
          then g.body.denote (fun b => if b = g.idxSlot then ExactScalar.ofNat k
                                       else bufs b ((g.offs b).evalQK q k))
          else ExactScalar.one) := by
    have hstep : ∀ p : Nat,
        accOf (flatEnv bufs q) nkb FE.oneC (g.step block) 0 p
          = ExactScalar.prod nkb (fun kb =>
              if kb * block + p < g.K then
                (if (g.inRange).evalQK q (kb * block + p)
                 then g.body.denote (fun b =>
                        if b = g.idxSlot then ExactScalar.ofNat (kb * block + p)
                        else bufs b ((g.offs b).evalQK q (kb * block + p)))
                 else ExactScalar.one)
              else ExactScalar.one) := by
      intro p
      rw [show g.step block = FE.bin .mul (.acc 0) (g.summand block) from rfl,
          accOf_prod (summand_accFree g block) 0 p nkb]
      exact ExactScalar.prod_congr (fun kb _ => summand_eval g block hw bufs q kb p _)
    rw [ExactScalar.prod_congr (fun p _ => hstep p)]
    exact prod_tile_mask block nkb g.K
      (fun i => if (g.inRange).evalQK q i
                then g.body.denote (fun b => if b = g.idxSlot then ExactScalar.ofNat i
                                             else bufs b ((g.offs b).evalQK q i))
                else ExactScalar.one) hK
  have hguard : ((g.outGuard).instK block).eval ((flatEnv bufs q).pushAcc
      (accOf (flatEnv bufs q) nkb FE.oneC (g.step block))) 0 0
        = (g.outGuard).evalQK q 0 := by
    have h := BE.instK_eval (block := block)
      (env := (flatEnv bufs q).pushAcc (accOf (flatEnv bufs q) nkb FE.oneC (g.step block)))
      (q := q) (kb := 0) 0 rfl rfl _ hw.guard_ok
    simpa using h
  have hpost : ∀ b : Nat,
      ((fun b => match b with
        | 0 => FE.redCol .prod block (.acc 0)
        | b + 1 => FE.load b ((g.postOffs b).instK block) .tt) b).eval
          ((flatEnv bufs q).pushAcc (accOf (flatEnv bufs q) nkb FE.oneC (g.step block))) 0 0
        = (match b with
           | 0 => ExactScalar.prod g.K (fun k =>
                    if (g.inRange).evalQK q k
                    then g.body.denote (fun b =>
                           if b = g.idxSlot then ExactScalar.ofNat k
                           else bufs b ((g.offs b).evalQK q k))
                    else ExactScalar.one)
           | b + 1 => bufs b ((g.postOffs b).evalQK q 0)) := by
    intro b
    cases b with
    | zero =>
      show ExactScalar.prod block
        (fun p => accOf (flatEnv bufs q) nkb FE.oneC (g.step block) 0 p) = _
      exact hred
    | succ b' =>
      have hoff := IE.instK_eval (block := block)
        (env := (flatEnv bufs q).pushAcc (accOf (flatEnv bufs q) nkb FE.oneC (g.step block)))
        (q := q) (kb := 0) 0 rfl rfl _ (hw.post_ok b')
      simp only [Nat.zero_mul, Nat.add_zero] at hoff
      simp only [FE.eval, BE.eval, if_true, hoff, Env.pushAcc_bufs, flatEnv_bufs]
  have hval : (g.stored block).eval ((flatEnv bufs q).pushAcc
      (accOf (flatEnv bufs q) nkb FE.oneC (g.step block))) 0 0
        = (g.spec (α := α)).out bufs q := by
    show (if _ then _ else _) = (if _ then _ else _)
    rw [hguard]
    by_cases hg : (g.outGuard).evalQK q 0 = true
    · simp only [hg, if_true]
      exact SE.toFEWith_eval hpost g.post
    · simp only [Bool.not_eq_true] at hg
      simp only [hg, Bool.false_eq_true, if_false]
      rfl
  rw [show g.prog block nkb = Prog.mk g.nout 1
        (.forAcc nkb FE.oneC (g.step block) (.store 1 1 (.pid 0) (g.stored block) .tt))
      from rfl, Prog.run_grid1]
  refine gridFold_at (v := (g.spec (α := α)).out bufs q) hq' ?_ ?_
  · intro mm
    rw [forAcc_exec]
    simp only [Stmt.exec]
    rw [store11_at _ _ _ _ q rfl]
    exact hval
  · intro p mm hne
    rw [forAcc_exec]
    simp only [Stmt.exec]
    exact store11_skip _ _ _ _ q (fun h => hne h)

end ProdRed
end VerifiedKernel
