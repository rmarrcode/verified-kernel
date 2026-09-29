/-
  GENERATED FILE -- do not edit.

  Written by verified_kernel.vk.compile. Each task below carries a
  `theorem` instantiating its family's correctness theorem at the exact
  numbers the generator chose. `lake build` checking this file is what
  makes the corresponding kernel in generated/ a verified kernel.
-/
import VerifiedKernel

open VerifiedKernel

-- t097: three-stage normalisation, 3 input buffer(s), intermediates 134217728 and 262144 at buffers 3 and 4
--   attention: batch 16, 32 heads, 512 positions, embedding 1024
def t097_s1_g : GenRed :=
  { nout := 134217728, K := 1024
  , offs := fun b => ([(IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 262144)) (IE.lit 512)) (IE.modi (IE.divi (IE.pid 0) (IE.lit 512)) (IE.lit 512))) (IE.lit 1024)) IE.rk), (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 262144)) (IE.lit 512)) (IE.modi (IE.pid 0) (IE.lit 512))) (IE.lit 1024)) IE.rk), (IE.lit 0), (IE.lit 0), (IE.lit 0)]).getD b (IE.lit 0)
  , inRange := BE.tt
  , body := (SE.bin .mul (SE.inp 0) (SE.inp 1))
  , postOffs := fun b => ([(IE.lit 0), (IE.lit 0), (IE.lit 0), (IE.lit 0), (IE.lit 0)]).getD b (IE.lit 0)
  , post := (SE.bin .mul (SE.inp 0) (SE.recip (SE.un .sqrt (SE.lit false 1024 1))))
  , outGuard := BE.tt
  , nInp := 2, idxSlot := 1048576 }
def t097_s1_block : Nat := 1024
def t097_s1_nkb : Nat := 1

theorem t097_s1_wf : t097_s1_g.Wf :=
  { offs_ok := IE.qkOnly_getD _ (by decide)
  , post_ok := IE.qkOnly_getD _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

theorem t097_s1_impl {α : Type} [ExactScalar α] :
    Implements (t097_s1_g.prog t097_s1_block t097_s1_nkb) (t097_s1_g.spec (α := α)) :=
  GenRed.prog_implements t097_s1_g t097_s1_block t097_s1_nkb t097_s1_wf (by decide) (by decide)

def t097_s2_g : GenRed :=
  { nout := 262144, K := 512
  , offs := fun b => ([(IE.lit 0), (IE.lit 0), (IE.lit 0), (IE.add (IE.mul (IE.pid 0) (IE.lit 512)) IE.rk), (IE.lit 0)]).getD b (IE.lit 0)
  , inRange := BE.tt
  , body := (SE.un .exp (SE.inp 3))
  , postOffs := fun b => ([(IE.lit 0), (IE.lit 0), (IE.lit 0), (IE.lit 0), (IE.lit 0)]).getD b (IE.lit 0)
  , post := (SE.inp 0)
  , outGuard := BE.tt
  , nInp := 4, idxSlot := 1048576 }
def t097_s2_block : Nat := 512
def t097_s2_nkb : Nat := 1

theorem t097_s2_wf : t097_s2_g.Wf :=
  { offs_ok := IE.qkOnly_getD _ (by decide)
  , post_ok := IE.qkOnly_getD _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

theorem t097_s2_impl {α : Type} [ExactScalar α] :
    Implements (t097_s2_g.prog t097_s2_block t097_s2_nkb) (t097_s2_g.spec (α := α)) :=
  GenRed.prog_implements t097_s2_g t097_s2_block t097_s2_nkb t097_s2_wf (by decide) (by decide)

def t097_s3_g : GenRed :=
  { nout := 268435456, K := 512
  , offs := fun b => ([(IE.lit 0), (IE.lit 0), (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 524288)) (IE.lit 512)) IE.rk) (IE.lit 1024)) (IE.modi (IE.pid 0) (IE.lit 1024))), (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 1024)) (IE.lit 512)) IE.rk), (IE.lit 0)]).getD b (IE.lit 0)
  , inRange := BE.tt
  , body := (SE.bin .mul (SE.un .exp (SE.inp 3)) (SE.inp 2))
  , postOffs := fun b => ([(IE.lit 0), (IE.lit 0), (IE.lit 0), (IE.lit 0), (IE.divi (IE.pid 0) (IE.lit 1024))]).getD b (IE.lit 0)
  , post := (SE.bin .mul (SE.inp 0) (SE.recip (SE.inp 5)))
  , outGuard := BE.tt
  , nInp := 5, idxSlot := 1048576 }
def t097_s3_block : Nat := 512
def t097_s3_nkb : Nat := 1

theorem t097_s3_wf : t097_s3_g.Wf :=
  { offs_ok := IE.qkOnly_getD _ (by decide)
  , post_ok := IE.qkOnly_getD _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

theorem t097_s3_impl {α : Type} [ExactScalar α] :
    Implements (t097_s3_g.prog t097_s3_block t097_s3_nkb) (t097_s3_g.spec (α := α)) :=
  GenRed.prog_implements t097_s3_g t097_s3_block t097_s3_nkb t097_s3_wf (by decide) (by decide)

/-- Stage 2 reads the first intermediate only where stage 1 wrote it. -/
theorem t097_l2 {α : Type} [ExactScalar α] :
    Loc (t097_s2_g.spec (α := α)) 3 134217728 :=
  GenRed.loc t097_s2_g 3 134217728 (fun q k hq hk => (bound_pack (A := 262144) (B := 512) hq hk)) (fun _ _ => (by decide : (0 : Nat) < 134217728))

/-- Stage 3 reads each intermediate only where its stage wrote it. -/
theorem t097_l3a {α : Type} [ExactScalar α] :
    Loc (t097_s3_g.spec (α := α)) 3 134217728 :=
  GenRed.loc t097_s3_g 3 134217728 (fun q k hq hk => (bound_pack (A := 262144) (B := 512) (bound_div (a := 262144) (d := 1024) hq) hk)) (fun _ _ => (by decide : (0 : Nat) < 134217728))

theorem t097_l3b {α : Type} [ExactScalar α] :
    Loc (t097_s3_g.spec (α := α)) 4 262144 :=
  GenRed.loc t097_s3_g 4 262144 (fun _ _ _ _ => (by decide : (0 : Nat) < 262144)) (fun q hq => (bound_div (a := 262144) (d := 1024) hq))

/-- Correctness certificate for t097: the composed three-stage pipeline. -/
theorem t097_correct {α : Type} [ExactScalar α] :
    ∀ (bufs : Nat → Buf α) (m1 m2 m3 : Mem α) (q : Nat),
      q < (t097_s3_g.spec (α := α)).outSize →
      runThree (t097_s1_g.prog t097_s1_block t097_s1_nkb)
               (t097_s2_g.prog t097_s2_block t097_s2_nkb)
               (t097_s3_g.prog t097_s3_block t097_s3_nkb) 3 4 bufs m1 m2 m3 q
        = compose3 (t097_s1_g.spec (α := α)) (t097_s2_g.spec (α := α))
            (t097_s3_g.spec (α := α)) 3 4 bufs q :=
  three_stage (by decide) t097_s1_impl t097_s2_impl t097_s3_impl t097_l2 t097_l3a t097_l3b

def t097_s1_kernel : ReduceKernel :=
  { name := "t097_s1", arity := 2, block := t097_s1_block, nkb := t097_s1_nkb, nout := 134217728, init := FE.zeroC, step := t097_s1_g.step t097_s1_block, stored := t097_s1_g.stored t097_s1_block }
def t097_s2_kernel : ReduceKernel :=
  { name := "t097_s2", arity := 4, block := t097_s2_block, nkb := t097_s2_nkb, nout := 262144, init := FE.zeroC, step := t097_s2_g.step t097_s2_block, stored := t097_s2_g.stored t097_s2_block }
def t097_s3_kernel : ReduceKernel :=
  { name := "t097_s3", arity := 5, block := t097_s3_block, nkb := t097_s3_nkb, nout := 268435456, init := FE.zeroC, step := t097_s3_g.step t097_s3_block, stored := t097_s3_g.stored t097_s3_block }
def t097_kernel : PipelineKernel3 :=
  { name := "t097", arity := 3, n1 := 134217728, n2 := 262144, stage1 := t097_s1_kernel, stage2 := t097_s2_kernel, stage3 := t097_s3_kernel }

def main : IO Unit := do
  IO.FS.writeFile "../generated/t097.py" t097_kernel.render
