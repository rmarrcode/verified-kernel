/-
Coverage and collision-freedom.

Every kernel proof needs the same two facts about a masked store: the output
element `q` *is* written (coverage), and it is written by exactly one lane
(collision-freedom), so the value landing in memory is the one that lane
computed. Proving these once, generically, is what keeps per-kernel proofs
short -- and forcing them to be proved at all is what rules out the silent
out-of-bounds and double-write bugs that testing misses.
-/
import VerifiedKernel.Ir

namespace VerifiedKernel

open ExactScalar

variable {α : Type} [ExactScalar α]

/-- The generic masked write-fold. Both the inner loop of `storeTile` and the
grid loop of `Prog.run` are instances of this shape. -/
def writeFold (n : Nat) (offf : Nat → Nat) (valf : Nat → α) (mk : Nat → Bool)
    (m : Mem α) : Mem α :=
  Nat.rec (motive := fun _ => Mem α) m
    (fun j mj => if mk j then mj.upd (offf j) (valf j) else mj) n

@[simp] theorem writeFold_zero (offf valf mk) (m : Mem α) :
    writeFold 0 offf valf mk m = m := rfl

@[simp] theorem writeFold_succ (n offf) (valf : Nat → α) (mk) (m : Mem α) :
    writeFold (n + 1) offf valf mk m
      = (if mk n then (writeFold n offf valf mk m).upd (offf n) (valf n)
         else writeFold n offf valf mk m) := rfl

/-- If no enabled lane targets `q`, memory at `q` is untouched. -/
theorem writeFold_miss {n : Nat} {offf : Nat → Nat} {valf : Nat → α}
    {mk : Nat → Bool} {m : Mem α} {q : Nat}
    (h : ∀ j, j < n → mk j = true → offf j ≠ q) :
    writeFold n offf valf mk m q = m q := by
  induction n with
  | zero => rfl
  | succ k ih =>
    rw [writeFold_succ]
    by_cases hk : mk k = true
    · simp only [hk, if_true]
      rw [Mem.upd_other (Ne.symm (h k (Nat.lt_succ_self k) hk))]
      exact ih (fun j hj => h j (Nat.lt_succ_of_lt hj))
    · simp only [Bool.not_eq_true] at hk
      simp only [hk, Bool.false_eq_true, if_false]
      exact ih (fun j hj => h j (Nat.lt_succ_of_lt hj))

/-- If exactly one enabled lane targets `q`, memory at `q` holds that lane's
value. `huniq` is the collision-freedom obligation, discharged per kernel from
the injectivity of its offset arithmetic. -/
theorem writeFold_hit {n : Nat} {offf : Nat → Nat} {valf : Nat → α}
    {mk : Nat → Bool} {m : Mem α} {q j0 : Nat}
    (hj0 : j0 < n) (hmk : mk j0 = true) (hoff : offf j0 = q)
    (huniq : ∀ j, j < n → mk j = true → offf j = q → j = j0) :
    writeFold n offf valf mk m q = valf j0 := by
  induction n with
  | zero => exact absurd hj0 (Nat.not_lt_zero _)
  | succ k ih =>
    rw [writeFold_succ]
    rcases Nat.lt_or_ge j0 k with hlt | hge
    · -- the last lane cannot also target q, so the earlier write survives
      have hlast : ∀ j, j = k → mk j = true → offf j ≠ q := by
        intro j hjk hmj hoq
        subst hjk
        exact absurd (huniq j (Nat.lt_succ_self _) hmj hoq) (Nat.ne_of_gt hlt)
      by_cases hk : mk k = true
      · simp only [hk, if_true]
        rw [Mem.upd_other (Ne.symm (hlast k rfl hk))]
        exact ih hlt (fun j hj hm ho => huniq j (Nat.lt_succ_of_lt hj) hm ho)
      · simp only [Bool.not_eq_true] at hk
        simp only [hk, Bool.false_eq_true, if_false]
        exact ih hlt (fun j hj hm ho => huniq j (Nat.lt_succ_of_lt hj) hm ho)
    · -- j0 = k: the last lane is the one
      have hj0k : j0 = k := Nat.le_antisymm (Nat.le_of_lt_succ hj0) hge
      subst hj0k
      simp only [hmk, if_true, hoff, Mem.upd_same]

/-! ## Instantiating at a single-row tile -/

/-- A `1 × cols` tile store is exactly a `writeFold` over its column lanes. -/
theorem storeTile_row1 (cols : Nat) (off : IE) (val : FE) (mask : BE)
    (env : Env α) (m : Mem α) :
    storeTile 1 cols off val mask env m
      = writeFold cols (fun j => off.eval env 0 j) (fun j => val.eval env 0 j)
          (fun j => mask.eval env 0 j) m := rfl

/-! ## The flat 1-D tiling theorem

This is the workhorse. A great many kernels have exactly this shape: a 1-D grid
of `nblocks` programs, each storing one `1 × block` tile at offsets
`pid*block + col`, masked by `pid*block + col < n`. The theorem below says such a
kernel writes, at every `q < n`, the value its owning lane computed -- and it
follows that the whole output is covered with no collisions. -/

/-- `off = pid 0 * block + col`. -/
def flatOff (block : Nat) : IE := .add (.mul (.pid 0) (.lit block)) .col

/-- `mask = pid 0 * block + col < n`. -/
def flatMask (block n : Nat) : BE := .cmp .lt (flatOff block) (.lit n)

theorem flatOff_eval (block : Nat) (env : Env α) (i j : Nat) :
    (flatOff block).eval env i j = env.pid 0 * block + j := rfl

/-- One program of a flat 1-D kernel writes precisely the lanes of its own block
that are in range, and nothing else. -/
theorem flat_block_at {block n : Nat} (val : FE) (env : Env α) (m : Mem α)
    (q : Nat) (hb : 0 < block) (hq : q < n)
    (hown : env.pid 0 = q / block) :
    storeTile 1 block (flatOff block) val (flatMask block n) env m q
      = val.eval env 0 (q % block) := by
  rw [storeTile_row1]
  have hmod : q % block < block := Nat.mod_lt _ hb
  have hrecomp : env.pid 0 * block + q % block = q := by
    rw [hown]; exact Nat.div_add_mod' q block
  have hoffq : (flatOff block).eval env 0 (q % block) = q := by
    rw [flatOff_eval]; exact hrecomp
  refine writeFold_hit hmod ?_ hoffq ?_
  · show (flatMask block n).eval env 0 (q % block) = true
    simp only [flatMask, BE.eval, hoffq, Cmp.apply]
    exact decide_eq_true hq
  · intro j _ _ hoq
    rw [flatOff_eval] at hoq
    exact Nat.add_left_cancel (hoq.trans hrecomp.symm)

/-- A program that does not own `q` leaves it alone. -/
theorem flat_block_skip {block n : Nat} (val : FE) (env : Env α) (m : Mem α)
    (q : Nat) (hb : 0 < block) (hown : env.pid 0 ≠ q / block) :
    storeTile 1 block (flatOff block) val (flatMask block n) env m q = m q := by
  rw [storeTile_row1]
  refine writeFold_miss ?_
  intro j hj _ hoq
  rw [flatOff_eval] at hoq
  -- q = pid*block + j with j < block forces pid = q / block
  apply hown
  rw [← hoq, Nat.mul_comm (env.pid 0) block, Nat.mul_add_div hb,
      Nat.div_eq_of_lt hj, Nat.add_zero]

/-! ## Lifting a per-block fact to the whole launch grid -/

/-- Generic grid fold: if exactly one program id affects `q`, the final memory at
`q` is what that program wrote. -/
theorem gridFold_at {n : Nat} {step : Nat → Mem α → Mem α} {m : Mem α} {q p0 : Nat}
    {v : α} (hp0 : p0 < n)
    (hhit : ∀ mm, step p0 mm q = v)
    (hskip : ∀ p mm, p ≠ p0 → step p mm q = mm q) :
    (Nat.rec (motive := fun _ => Mem α) m (fun p mp => step p mp) n : Mem α) q = v := by
  induction n with
  | zero => exact absurd hp0 (Nat.not_lt_zero _)
  | succ k ih =>
    rcases Nat.lt_or_ge p0 k with hlt | hge
    · show step k _ q = v
      rw [hskip k _ (Nat.ne_of_gt hlt)]
      exact ih hlt
    · have : p0 = k := Nat.le_antisymm (Nat.le_of_lt_succ hp0) hge
      subst this
      exact hhit _

/-- The environment a flat 1-D kernel sees at program id `b0`. -/
def flatEnv (bufs : Nat → Buf α) (b0 : Nat) : Env α :=
  { pid := fun a => if a == 0 then b0 else 0
  , ivs := fun _ => 0
  , accs := fun _ _ _ => ExactScalar.zero
  , bufs := bufs }

@[simp] theorem flatEnv_pid0 (bufs : Nat → Buf α) (b0 : Nat) :
    (flatEnv bufs b0).pid 0 = b0 := rfl

@[simp] theorem flatEnv_bufs (bufs : Nat → Buf α) (b0 : Nat) :
    (flatEnv bufs b0).bufs = bufs := rfl

/-- The flat offset a lane sees is exactly the output index it owns. -/
theorem flat_lane_off {block : Nat} (hb : 0 < block) (bufs : Nat → Buf α) (q : Nat) :
    (flatOff block).eval (flatEnv bufs (q / block)) 0 (q % block) = q := by
  rw [flatOff_eval, flatEnv_pid0]
  exact Nat.div_add_mod' q block

/-- An in-range lane is enabled. -/
theorem flat_lane_mask {block n : Nat} (hb : 0 < block) {q : Nat} (hq : q < n)
    (bufs : Nat → Buf α) :
    (flatMask block n).eval (flatEnv bufs (q / block)) 0 (q % block) = true := by
  simp only [flatMask, BE.eval, flat_lane_off hb bufs q, Cmp.apply]
  exact decide_eq_true hq

/-- A 1-D launch grid: with `grid1 = 1` the inner fold runs the body once, at
program id 0 on the second axis. -/
theorem Prog.run_grid1 (g0 : Nat) (bd : Stmt) (bufs : Nat → Buf α) (m : Mem α) :
    (Prog.mk g0 1 bd).run bufs m
      = Nat.rec (motive := fun _ => Mem α) m
          (fun b0 m0 => bd.exec (flatEnv bufs b0) m0) g0 := rfl

/-! ### Single-element stores

A kernel that computes one output per program -- every reduction has this shape --
stores a `1 × 1` tile. Coverage is then immediate from the offset being the
program id. -/

theorem store11_at (off : IE) (val : FE) (env : Env α) (m : Mem α) (q : Nat)
    (hoff : off.eval env 0 0 = q) :
    storeTile 1 1 off val .tt env m q = val.eval env 0 0 := by
  rw [storeTile_row1]
  exact writeFold_hit (Nat.lt_succ_self 0) rfl hoff
    (fun j hj _ _ => Nat.lt_one_iff.mp hj)

theorem store11_skip (off : IE) (val : FE) (env : Env α) (m : Mem α) (q : Nat)
    (hoff : off.eval env 0 0 ≠ q) :
    storeTile 1 1 off val .tt env m q = m q := by
  rw [storeTile_row1]
  refine writeFold_miss ?_
  intro j hj _
  rw [Nat.lt_one_iff.mp hj]
  exact hoff

/-- A flat 1-D kernel: `nblocks` programs, each storing one `1 × block` tile. -/
def Prog.flat1d (nblocks block n : Nat) (val : FE) : Prog :=
  { grid0 := nblocks, grid1 := 1
  , body := .store 1 block (flatOff block) val (flatMask block n) }

theorem Prog.flat1d_run (nblocks block n : Nat) (val : FE)
    (bufs : Nat → Buf α) (m : Mem α) :
    (Prog.flat1d nblocks block n val).run bufs m
      = Nat.rec (motive := fun _ => Mem α) m
          (fun b0 m0 => storeTile 1 block (flatOff block) val (flatMask block n)
            (flatEnv bufs b0) m0) nblocks := rfl

/--
**The flat-kernel theorem.** If, for every output index `q`, the lane that owns
`q` computes `spec.out bufs q`, then the flat 1-D kernel implements the spec.

The two side conditions are the real content: `block > 0` and
`outSize ≤ nblocks * block` together guarantee the grid covers the output, and
the uniqueness argument inside `flat_block_at` guarantees no element is written
twice. A kernel whose grid is one block too small does not merely score badly
here -- it fails to typecheck as a proof.
-/
theorem flat1d_implements {block nblocks : Nat} {val : FE} {s : Spec α}
    (hb : 0 < block)
    (hcover : s.outSize ≤ nblocks * block)
    (hval : ∀ (bufs : Nat → Buf α) (q : Nat), q < s.outSize →
      val.eval (flatEnv bufs (q / block)) 0 (q % block) = s.out bufs q) :
    Implements (Prog.flat1d nblocks block s.outSize val) s := by
  intro bufs m q hq
  rw [Prog.flat1d_run]
  have hpq : q / block < nblocks :=
    Nat.div_lt_of_lt_mul (by rw [Nat.mul_comm] at hcover; exact Nat.lt_of_lt_of_le hq hcover)
  refine gridFold_at (v := s.out bufs q) hpq ?_ ?_
  · intro mm
    rw [flat_block_at val (flatEnv bufs (q / block)) mm q hb hq (flatEnv_pid0 bufs _)]
    exact hval bufs q hq
  · intro p mm hne
    exact flat_block_skip val (flatEnv bufs p) mm q hb (by rw [flatEnv_pid0]; exact hne)

end VerifiedKernel
