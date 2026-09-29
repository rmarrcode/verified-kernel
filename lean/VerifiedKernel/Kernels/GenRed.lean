/-
The general reducing family: one output per program, reducing over a window,
with a caller-supplied **index map** per input.

This one family and one theorem cover structurally different-looking operators:

  axis reduction   input index = ((q/inner)*K + k)*inner + q%inner
  matrix product   A at (q/N)*K + k,  B at k*N + q%N
  convolution      unpack q into (n, oc, oh, ow), unpack k into (ic, kh, kw),
                   then index the input at the corresponding window position
  pooling          the same, with the window but no weights

What differs between them is arithmetic on `pid` and `rk`; what is identical is
the loop, the masking, and the store. Sharing the proof means a new operator costs
an index map and a frontend rule, not a new verification effort.

`rk` is the placeholder for the reduction index. A spec evaluates it directly via
`IE.evalQK`; the backend replaces it with the lane/step decomposition
`iv 0 * block + col` via `IE.instK`. `instK_eval` is the theorem that those two
readings agree, and it is what licenses tiling an arbitrary index map.
-/
import VerifiedKernel.Loop

namespace VerifiedKernel

open ExactScalar

/-! ## Index maps -/

/-- An index map may mention only the program id and the reduction index. Tile
coordinates and loop counters are the *backend's* business; a spec that reached
for them would be describing an implementation, not a specification. -/
def IE.qkOnly : IE → Bool
  -- only axis 0: this family launches a 1-D grid, so `pid 1` has no meaning here
  | .pid a => a == 0
  | .rk | .lit _ => true
  | .row | .col | .iv _ => false
  | .add a b | .mul a b | .sub a b | .divi a b | .modi a b => a.qkOnly && b.qkOnly

/-- Spec-side reading of an index map at output index `q` and reduction index `k`. -/
def IE.evalQK (q k : Nat) : IE → Nat
  | .pid _ => q
  | .rk => k
  | .lit n => n
  | .row | .col => 0
  | .iv _ => 0
  | .add a b => a.evalQK q k + b.evalQK q k
  | .mul a b => a.evalQK q k * b.evalQK q k
  | .sub a b => a.evalQK q k - b.evalQK q k
  | .divi a b => a.evalQK q k / b.evalQK q k
  | .modi a b => a.evalQK q k % b.evalQK q k

/-- `k = iv 0 * block + col`: the reduction index this lane covers this iteration. -/
def kIE (block : Nat) : IE := .add (.mul (.iv 0) (.lit block)) .col

/-- Backend-side reading: replace the placeholder by the lane/step decomposition. -/
def IE.instK (block : Nat) : IE → IE
  | .rk => kIE block
  | .pid a => .pid a
  | .lit n => .lit n
  | .row => .row
  | .col => .col
  | .iv k => .iv k
  | .add a b => .add (a.instK block) (b.instK block)
  | .mul a b => .mul (a.instK block) (b.instK block)
  | .sub a b => .sub (a.instK block) (b.instK block)
  | .divi a b => .divi (a.instK block) (b.instK block)
  | .modi a b => .modi (a.instK block) (b.instK block)

variable {α : Type} [ExactScalar α]

/-- **Index maps tile correctly.** The substituted map, evaluated in the kernel's
environment at lane `j` of step `kb`, gives the same index as the spec's map read
at `k = kb*block + j`.

This is the crux of the generalisation. It holds for *any* `qkOnly` map -- affine,
div/mod, nested -- so convolution's index unpacking is licensed by the same lemma
as a plain axis reduction's. -/
theorem IE.instK_eval {block : Nat} {env : Env α} {q kb : Nat} (j : Nat)
    (hpid : env.pid 0 = q) (hiv : env.ivs 0 = kb) :
    ∀ (e : IE), e.qkOnly = true →
      (e.instK block).eval env 0 j = e.evalQK q (kb * block + j) := by
  intro e
  induction e with
  | pid x =>
    intro h
    have hx : x = 0 := by simpa [IE.qkOnly] using h
    subst hx
    exact hpid
  | rk =>
    intro _
    show env.ivs 0 * block + j = kb * block + j
    rw [hiv]
  | lit n => intro _; rfl
  | row => intro h; exact absurd h (by simp [IE.qkOnly])
  | col => intro h; exact absurd h (by simp [IE.qkOnly])
  | iv k => intro h; exact absurd h (by simp [IE.qkOnly])
  | add x y hx hy =>
    intro h
    simp only [IE.qkOnly, Bool.and_eq_true] at h
    simp only [IE.instK, IE.eval, IE.evalQK, hx h.1, hy h.2]
  | mul x y hx hy =>
    intro h
    simp only [IE.qkOnly, Bool.and_eq_true] at h
    simp only [IE.instK, IE.eval, IE.evalQK, hx h.1, hy h.2]
  | sub x y hx hy =>
    intro h
    simp only [IE.qkOnly, Bool.and_eq_true] at h
    simp only [IE.instK, IE.eval, IE.evalQK, hx h.1, hy h.2]
  | divi x y hx hy =>
    intro h
    simp only [IE.qkOnly, Bool.and_eq_true] at h
    simp only [IE.instK, IE.eval, IE.evalQK, hx h.1, hy h.2]
  | modi x y hx hy =>
    intro h
    simp only [IE.qkOnly, Bool.and_eq_true] at h
    simp only [IE.instK, IE.eval, IE.evalQK, hx h.1, hy h.2]

/-- Index maps are generated as a list; this bridges to the `Nat → IE` the family
takes, so a generated certificate can discharge well-formedness with a single
`decide` over the list instead of a case split per input. -/
theorem IE.qkOnly_getD (l : List IE) (h : l.all (fun e => e.qkOnly) = true) :
    ∀ (b : Nat), ((l.getD b (.lit 0)).qkOnly) = true := by
  induction l with
  | nil => intro b; simp [List.getD_nil, IE.qkOnly]
  | cons e t ih =>
    simp only [List.all_cons, Bool.and_eq_true] at h
    intro b
    cases b with
    | zero => simpa [List.getD_cons_zero] using h.1
    | succ b' => simpa [List.getD_cons_succ] using ih h.2 b'

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
structure GenRed where
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

/-- An index map is well-formed when it mentions only `pid` and `rk`. -/
def BE.qkOnly : BE → Bool
  | .tt => true
  | .cmp _ a b => a.qkOnly && b.qkOnly
  | .and a b | .or a b => a.qkOnly && b.qkOnly
  | .not a => a.qkOnly

def BE.evalQK (q k : Nat) : BE → Bool
  | .tt => true
  | .cmp c a b => c.apply (a.evalQK q k) (b.evalQK q k)
  | .and a b => a.evalQK q k && b.evalQK q k
  | .or a b => a.evalQK q k || b.evalQK q k
  | .not a => !(a.evalQK q k)

def BE.instK (block : Nat) : BE → BE
  | .tt => .tt
  | .cmp c a b => .cmp c (a.instK block) (b.instK block)
  | .and a b => .and (a.instK block) (b.instK block)
  | .or a b => .or (a.instK block) (b.instK block)
  | .not a => .not (a.instK block)

theorem BE.instK_eval {block : Nat} {env : Env α} {q kb : Nat} (j : Nat)
    (hpid : env.pid 0 = q) (hiv : env.ivs 0 = kb) :
    ∀ (e : BE), e.qkOnly = true →
      (e.instK block).eval env 0 j = e.evalQK q (kb * block + j) := by
  intro e
  induction e with
  | tt => intro _; rfl
  | cmp c x y =>
    intro h
    simp only [BE.qkOnly, Bool.and_eq_true] at h
    simp only [BE.instK, BE.eval, BE.evalQK,
      IE.instK_eval j hpid hiv _ h.1, IE.instK_eval j hpid hiv _ h.2]
  | and x y hx hy =>
    intro h
    simp only [BE.qkOnly, Bool.and_eq_true] at h
    simp only [BE.instK, BE.eval, BE.evalQK, hx h.1, hy h.2]
  | or x y hx hy =>
    intro h
    simp only [BE.qkOnly, Bool.and_eq_true] at h
    simp only [BE.instK, BE.eval, BE.evalQK, hx h.1, hy h.2]
  | not x hx =>
    intro h
    simp only [BE.qkOnly] at h
    simp only [BE.instK, BE.eval, BE.evalQK, hx h]

namespace GenRed

variable {α : Type} [ExactScalar α]

/-- Whether the lane's `(q, k)` contributes: in range of the reduction *and*
passing the family's guard. -/
def live (g : GenRed) : BE := .and (.cmp .lt .rk (.lit g.K)) g.inRange

def spec (g : GenRed) : Spec α :=
  { arity := g.nInp
  , outSize := g.nout
  , out := fun ins q =>
      let red := ExactScalar.sum g.K (fun k =>
        if (g.inRange).evalQK q k
        then g.body.denote (fun b => ins b ((g.offs b).evalQK q k))
        else ExactScalar.zero)
      if (g.outGuard).evalQK q 0 then
        g.post.denote (fun b => match b with
          | 0 => red
          | b + 1 => ins b ((g.postOffs b).evalQK q 0))
      else ExactScalar.zero }

/-- The masked summand. Note the mask guards the *summand*, not merely the loads:
a body like `exp x` sends a zeroed load to `1`, which would corrupt the sum. -/
def summand (g : GenRed) (block : Nat) : FE :=
  .sel ((g.live).instK block)
    (SE.toFEWith (fun b => .load b ((g.offs b).instK block) ((g.live).instK block)) g.body)
    .zeroC

def step (g : GenRed) (block : Nat) : FE := .bin .add (.acc 0) (g.summand block)

def stored (g : GenRed) (block : Nat) : FE :=
  .sel ((g.outGuard).instK block)
    (SE.toFEWith
      (fun b => match b with
        | 0 => .redCol .sum block (.acc 0)
        | b + 1 => .load b ((g.postOffs b).instK block) .tt)
      g.post)
    .zeroC

def prog (g : GenRed) (block nkb : Nat) : Prog :=
  { grid0 := g.nout, grid1 := 1
  , body := .forAcc nkb .zeroC (g.step block)
      (.store 1 1 (.pid 0) (g.stored block) .tt) }

/-- Well-formedness: every index map and the guard mention only `pid` and `rk`. -/
structure Wf (g : GenRed) : Prop where
  offs_ok : ∀ b, (g.offs b).qkOnly = true
  post_ok : ∀ b, (g.postOffs b).qkOnly = true
  range_ok : g.inRange.qkOnly = true
  guard_ok : g.outGuard.qkOnly = true

theorem summand_accFree (g : GenRed) (block : Nat) :
    (g.summand block).accFree = true := by
  have h := SE.toFEWith_accFree
    (f := fun b => FE.load b ((g.offs b).instK block) ((g.live).instK block))
    (fun _ => rfl) g.body
  simp [summand, FE.accFree, h]

theorem live_eval (g : GenRed) (block : Nat) (hw : Wf g) (bufs : Nat → Buf α)
    (q kb j : Nat) (a : Nat → Nat → α) :
    ((g.live).instK block).eval ((flatEnv bufs q).pushStep kb a) 0 j
      = (decide (kb * block + j < g.K) && (g.inRange).evalQK q (kb * block + j)) := by
  have hq : (g.live).qkOnly = true := by
    simp [live, BE.qkOnly, IE.qkOnly, hw.range_ok]
  rw [BE.instK_eval (block := block) (env := (flatEnv bufs q).pushStep kb a)
    (q := q) (kb := kb) j rfl rfl _ hq]
  rfl

/-- The summand evaluates to the spec's masked summand. -/
theorem summand_eval (g : GenRed) (block : Nat) (hw : Wf g) (bufs : Nat → Buf α)
    (q kb j : Nat) (a : Nat → Nat → α) :
    (g.summand block).eval ((flatEnv bufs q).pushStep kb a) 0 j
      = (if kb * block + j < g.K then
           (if (g.inRange).evalQK q (kb * block + j)
            then g.body.denote (fun b => bufs b ((g.offs b).evalQK q (kb * block + j)))
            else ExactScalar.zero)
         else ExactScalar.zero) := by
  have hl := live_eval g block hw bufs q kb j a
  simp only [summand, FE.eval, hl]
  by_cases h1 : kb * block + j < g.K
  · by_cases h2 : (g.inRange).evalQK q (kb * block + j) = true
    · simp only [h1, h2, decide_true, Bool.and_true, if_true]
      refine SE.toFEWith_eval (fun b => ?_) g.body
      simp only [FE.eval, hl, h1, h2, decide_true, Bool.and_true, if_true,
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
theorem prog_implements (g : GenRed) (block nkb : Nat) (hw : Wf g)
    (hb : 0 < block) (hK : g.K ≤ nkb * block) :
    Implements (g.prog block nkb) (g.spec (α := α)) := by
  intro bufs m q hq
  have hq' : q < g.nout := hq
  have hred : ExactScalar.sum block
      (fun p => accOf (flatEnv bufs q) nkb .zeroC (g.step block) 0 p)
      = ExactScalar.sum g.K (fun k =>
          if (g.inRange).evalQK q k
          then g.body.denote (fun b => bufs b ((g.offs b).evalQK q k))
          else ExactScalar.zero) := by
    have hstep : ∀ p : Nat,
        accOf (flatEnv bufs q) nkb .zeroC (g.step block) 0 p
          = ExactScalar.sum nkb (fun kb =>
              if kb * block + p < g.K then
                (if (g.inRange).evalQK q (kb * block + p)
                 then g.body.denote (fun b => bufs b ((g.offs b).evalQK q (kb * block + p)))
                 else ExactScalar.zero)
              else ExactScalar.zero) := by
      intro p
      rw [show g.step block = FE.bin .add (.acc 0) (g.summand block) from rfl,
          accOf_sum (summand_accFree g block) 0 p nkb]
      exact ExactScalar.sum_congr (fun kb _ => summand_eval g block hw bufs q kb p _)
    rw [ExactScalar.sum_congr (fun p _ => hstep p)]
    exact sum_tile_mask block nkb g.K
      (fun i => if (g.inRange).evalQK q i
                then g.body.denote (fun b => bufs b ((g.offs b).evalQK q i))
                else ExactScalar.zero) hK
  have hguard : ((g.outGuard).instK block).eval ((flatEnv bufs q).pushAcc
      (accOf (flatEnv bufs q) nkb .zeroC (g.step block))) 0 0
        = (g.outGuard).evalQK q 0 := by
    have h := BE.instK_eval (block := block)
      (env := (flatEnv bufs q).pushAcc (accOf (flatEnv bufs q) nkb .zeroC (g.step block)))
      (q := q) (kb := 0) 0 rfl rfl _ hw.guard_ok
    simpa using h
  have hpost : ∀ b : Nat,
      ((fun b => match b with
        | 0 => FE.redCol .sum block (.acc 0)
        | b + 1 => FE.load b ((g.postOffs b).instK block) .tt) b).eval
          ((flatEnv bufs q).pushAcc (accOf (flatEnv bufs q) nkb .zeroC (g.step block))) 0 0
        = (match b with
           | 0 => ExactScalar.sum g.K (fun k =>
                    if (g.inRange).evalQK q k
                    then g.body.denote (fun b => bufs b ((g.offs b).evalQK q k))
                    else ExactScalar.zero)
           | b + 1 => bufs b ((g.postOffs b).evalQK q 0)) := by
    intro b
    cases b with
    | zero =>
      show ExactScalar.sum block
        (fun p => accOf (flatEnv bufs q) nkb .zeroC (g.step block) 0 p) = _
      exact hred
    | succ b' =>
      have hoff := IE.instK_eval (block := block)
        (env := (flatEnv bufs q).pushAcc (accOf (flatEnv bufs q) nkb .zeroC (g.step block)))
        (q := q) (kb := 0) 0 rfl rfl _ (hw.post_ok b')
      simp only [Nat.zero_mul, Nat.add_zero] at hoff
      simp only [FE.eval, BE.eval, if_true, hoff, Env.pushAcc_bufs, flatEnv_bufs]
  have hval : (g.stored block).eval ((flatEnv bufs q).pushAcc
      (accOf (flatEnv bufs q) nkb .zeroC (g.step block))) 0 0
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
        (.forAcc nkb .zeroC (g.step block) (.store 1 1 (.pid 0) (g.stored block) .tt))
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

end GenRed
end VerifiedKernel
