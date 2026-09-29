/-
  GENERATED FILE -- do not edit.

  Written by verified_kernel.vk.compile. Each task below carries a
  `theorem` instantiating its family's correctness theorem at the exact
  numbers the generator chose. `lake build` checking this file is what
  makes the corresponding kernel in generated/ a verified kernel.
-/
import VerifiedKernel

open VerifiedKernel

-- t033: three-stage normalisation, 3 input buffer(s), intermediates 64 and 64 at buffers 3 and 4
--   BatchNorm2d on (16, 64, 512, 512): 64 statistics over 4194304 elements, eps=1e-05, affine
def t033_s1_g : GenRed :=
  { nout := 64, K := 4194304
  , offs := fun b => ([(IE.add (IE.mul (IE.add (IE.mul (IE.divi IE.rk (IE.lit 262144)) (IE.lit 64)) (IE.pid 0)) (IE.lit 262144)) (IE.modi IE.rk (IE.lit 262144))), (IE.lit 0), (IE.lit 0), (IE.lit 0), (IE.lit 0)]).getD b (IE.lit 0)
  , inRange := BE.tt
  , body := (SE.inp 0)
  , postOffs := fun b => ([(IE.lit 0), (IE.lit 0), (IE.lit 0), (IE.lit 0), (IE.lit 0)]).getD b (IE.lit 0)
  , post := (SE.inp 0)
  , outGuard := BE.tt
  , nInp := 1 }
def t033_s1_block : Nat := 1024
def t033_s1_nkb : Nat := 4096

theorem t033_s1_wf : t033_s1_g.Wf :=
  { offs_ok := IE.qkOnly_getD _ (by decide)
  , post_ok := IE.qkOnly_getD _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

theorem t033_s1_impl {α : Type} [ExactScalar α] :
    Implements (t033_s1_g.prog t033_s1_block t033_s1_nkb) (t033_s1_g.spec (α := α)) :=
  GenRed.prog_implements t033_s1_g t033_s1_block t033_s1_nkb t033_s1_wf (by decide) (by decide)

def t033_s2_g : GenRed :=
  { nout := 64, K := 4194304
  , offs := fun b => ([(IE.add (IE.mul (IE.add (IE.mul (IE.divi IE.rk (IE.lit 262144)) (IE.lit 64)) (IE.pid 0)) (IE.lit 262144)) (IE.modi IE.rk (IE.lit 262144))), (IE.lit 0), (IE.lit 0), (IE.pid 0), (IE.lit 0)]).getD b (IE.lit 0)
  , inRange := BE.tt
  , body := (SE.bin .mul (SE.bin .sub (SE.inp 0) (SE.bin .mul (SE.inp 3) (SE.lit false 1 4194304))) (SE.bin .sub (SE.inp 0) (SE.bin .mul (SE.inp 3) (SE.lit false 1 4194304))))
  , postOffs := fun b => ([(IE.lit 0), (IE.lit 0), (IE.lit 0), (IE.lit 0), (IE.lit 0)]).getD b (IE.lit 0)
  , post := (SE.inp 0)
  , outGuard := BE.tt
  , nInp := 4 }
def t033_s2_block : Nat := 1024
def t033_s2_nkb : Nat := 4096

theorem t033_s2_wf : t033_s2_g.Wf :=
  { offs_ok := IE.qkOnly_getD _ (by decide)
  , post_ok := IE.qkOnly_getD _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

theorem t033_s2_impl {α : Type} [ExactScalar α] :
    Implements (t033_s2_g.prog t033_s2_block t033_s2_nkb) (t033_s2_g.spec (α := α)) :=
  GenRed.prog_implements t033_s2_g t033_s2_block t033_s2_nkb t033_s2_wf (by decide) (by decide)

def t033_s3_g : GenRed :=
  { nout := 268435456, K := 1
  , offs := fun b => ([(IE.pid 0), (IE.modi (IE.divi (IE.pid 0) (IE.lit 262144)) (IE.lit 64)), (IE.modi (IE.divi (IE.pid 0) (IE.lit 262144)) (IE.lit 64)), (IE.modi (IE.divi (IE.pid 0) (IE.lit 262144)) (IE.lit 64)), (IE.modi (IE.divi (IE.pid 0) (IE.lit 262144)) (IE.lit 64))]).getD b (IE.lit 0)
  , inRange := BE.tt
  , body := (SE.bin .add (SE.bin .mul (SE.bin .mul (SE.bin .sub (SE.inp 0) (SE.bin .mul (SE.inp 3) (SE.lit false 1 4194304))) (SE.recip (SE.un .sqrt (SE.bin .add (SE.bin .mul (SE.inp 4) (SE.lit false 1 4194304)) (SE.lit false 1 100000))))) (SE.inp 1)) (SE.inp 2))
  , postOffs := fun b => ([(IE.lit 0), (IE.lit 0), (IE.lit 0), (IE.lit 0), (IE.lit 0)]).getD b (IE.lit 0)
  , post := (SE.inp 0)
  , outGuard := BE.tt
  , nInp := 5 }
def t033_s3_block : Nat := 1
def t033_s3_nkb : Nat := 1

theorem t033_s3_wf : t033_s3_g.Wf :=
  { offs_ok := IE.qkOnly_getD _ (by decide)
  , post_ok := IE.qkOnly_getD _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

theorem t033_s3_impl {α : Type} [ExactScalar α] :
    Implements (t033_s3_g.prog t033_s3_block t033_s3_nkb) (t033_s3_g.spec (α := α)) :=
  GenRed.prog_implements t033_s3_g t033_s3_block t033_s3_nkb t033_s3_wf (by decide) (by decide)

/-- Stage 2 reads the first intermediate only where stage 1 wrote it. -/
theorem t033_l2 {α : Type} [ExactScalar α] :
    Loc (t033_s2_g.spec (α := α)) 3 64 :=
  GenRed.loc t033_s2_g 3 64 (fun q _ hq _ => hq) (fun _ _ => (by decide : (0 : Nat) < 64))

/-- Stage 3 reads each intermediate only where its stage wrote it. -/
theorem t033_l3a {α : Type} [ExactScalar α] :
    Loc (t033_s3_g.spec (α := α)) 3 64 :=
  GenRed.loc t033_s3_g 3 64 (fun q _ _ _ => bound_mod (c := 64) (by decide : (0 : Nat) < 64)) (fun _ _ => (by decide : (0 : Nat) < 64))

theorem t033_l3b {α : Type} [ExactScalar α] :
    Loc (t033_s3_g.spec (α := α)) 4 64 :=
  GenRed.loc t033_s3_g 4 64 (fun q _ _ _ => bound_mod (c := 64) (by decide : (0 : Nat) < 64)) (fun _ _ => (by decide : (0 : Nat) < 64))

/-- Correctness certificate for t033: the composed three-stage pipeline. -/
theorem t033_correct {α : Type} [ExactScalar α] :
    ∀ (bufs : Nat → Buf α) (m1 m2 m3 : Mem α) (q : Nat),
      q < (t033_s3_g.spec (α := α)).outSize →
      runThree (t033_s1_g.prog t033_s1_block t033_s1_nkb)
               (t033_s2_g.prog t033_s2_block t033_s2_nkb)
               (t033_s3_g.prog t033_s3_block t033_s3_nkb) 3 4 bufs m1 m2 m3 q
        = compose3 (t033_s1_g.spec (α := α)) (t033_s2_g.spec (α := α))
            (t033_s3_g.spec (α := α)) 3 4 bufs q :=
  three_stage (by decide) t033_s1_impl t033_s2_impl t033_s3_impl t033_l2 t033_l3a t033_l3b

def t033_s1_kernel : ReduceKernel :=
  { name := "t033_s1", arity := 1, block := t033_s1_block, nkb := t033_s1_nkb, nout := 64, init := FE.zeroC, step := t033_s1_g.step t033_s1_block, stored := t033_s1_g.stored t033_s1_block }
def t033_s2_kernel : ReduceKernel :=
  { name := "t033_s2", arity := 4, block := t033_s2_block, nkb := t033_s2_nkb, nout := 64, init := FE.zeroC, step := t033_s2_g.step t033_s2_block, stored := t033_s2_g.stored t033_s2_block }
def t033_s3_kernel : ReduceKernel :=
  { name := "t033_s3", arity := 5, block := t033_s3_block, nkb := t033_s3_nkb, nout := 268435456, init := FE.zeroC, step := t033_s3_g.step t033_s3_block, stored := t033_s3_g.stored t033_s3_block }
def t033_kernel : PipelineKernel3 :=
  { name := "t033", arity := 3, n1 := 64, n2 := 64, stage1 := t033_s1_kernel, stage2 := t033_s2_kernel, stage3 := t033_s3_kernel }

-- t034: three-stage normalisation, 1 input buffer(s), intermediates 896 and 896 at buffers 1 and 2
--   InstanceNorm2d on (14, 64, 512, 512): 896 statistics over 262144 elements, eps=1e-05
def t034_s1_g : GenRed :=
  { nout := 896, K := 262144
  , offs := fun b => ([(IE.add (IE.mul (IE.pid 0) (IE.lit 262144)) IE.rk), (IE.lit 0), (IE.lit 0)]).getD b (IE.lit 0)
  , inRange := BE.tt
  , body := (SE.inp 0)
  , postOffs := fun b => ([(IE.lit 0), (IE.lit 0), (IE.lit 0)]).getD b (IE.lit 0)
  , post := (SE.inp 0)
  , outGuard := BE.tt
  , nInp := 1 }
def t034_s1_block : Nat := 1024
def t034_s1_nkb : Nat := 256

theorem t034_s1_wf : t034_s1_g.Wf :=
  { offs_ok := IE.qkOnly_getD _ (by decide)
  , post_ok := IE.qkOnly_getD _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

theorem t034_s1_impl {α : Type} [ExactScalar α] :
    Implements (t034_s1_g.prog t034_s1_block t034_s1_nkb) (t034_s1_g.spec (α := α)) :=
  GenRed.prog_implements t034_s1_g t034_s1_block t034_s1_nkb t034_s1_wf (by decide) (by decide)

def t034_s2_g : GenRed :=
  { nout := 896, K := 262144
  , offs := fun b => ([(IE.add (IE.mul (IE.pid 0) (IE.lit 262144)) IE.rk), (IE.pid 0), (IE.lit 0)]).getD b (IE.lit 0)
  , inRange := BE.tt
  , body := (SE.bin .mul (SE.bin .sub (SE.inp 0) (SE.bin .mul (SE.inp 1) (SE.lit false 1 262144))) (SE.bin .sub (SE.inp 0) (SE.bin .mul (SE.inp 1) (SE.lit false 1 262144))))
  , postOffs := fun b => ([(IE.lit 0), (IE.lit 0), (IE.lit 0)]).getD b (IE.lit 0)
  , post := (SE.inp 0)
  , outGuard := BE.tt
  , nInp := 2 }
def t034_s2_block : Nat := 1024
def t034_s2_nkb : Nat := 256

theorem t034_s2_wf : t034_s2_g.Wf :=
  { offs_ok := IE.qkOnly_getD _ (by decide)
  , post_ok := IE.qkOnly_getD _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

theorem t034_s2_impl {α : Type} [ExactScalar α] :
    Implements (t034_s2_g.prog t034_s2_block t034_s2_nkb) (t034_s2_g.spec (α := α)) :=
  GenRed.prog_implements t034_s2_g t034_s2_block t034_s2_nkb t034_s2_wf (by decide) (by decide)

def t034_s3_g : GenRed :=
  { nout := 234881024, K := 1
  , offs := fun b => ([(IE.pid 0), (IE.divi (IE.pid 0) (IE.lit 262144)), (IE.divi (IE.pid 0) (IE.lit 262144))]).getD b (IE.lit 0)
  , inRange := BE.tt
  , body := (SE.bin .mul (SE.bin .sub (SE.inp 0) (SE.bin .mul (SE.inp 1) (SE.lit false 1 262144))) (SE.recip (SE.un .sqrt (SE.bin .add (SE.bin .mul (SE.inp 2) (SE.lit false 1 262144)) (SE.lit false 1 100000)))))
  , postOffs := fun b => ([(IE.lit 0), (IE.lit 0), (IE.lit 0)]).getD b (IE.lit 0)
  , post := (SE.inp 0)
  , outGuard := BE.tt
  , nInp := 3 }
def t034_s3_block : Nat := 1
def t034_s3_nkb : Nat := 1

theorem t034_s3_wf : t034_s3_g.Wf :=
  { offs_ok := IE.qkOnly_getD _ (by decide)
  , post_ok := IE.qkOnly_getD _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

theorem t034_s3_impl {α : Type} [ExactScalar α] :
    Implements (t034_s3_g.prog t034_s3_block t034_s3_nkb) (t034_s3_g.spec (α := α)) :=
  GenRed.prog_implements t034_s3_g t034_s3_block t034_s3_nkb t034_s3_wf (by decide) (by decide)

/-- Stage 2 reads the first intermediate only where stage 1 wrote it. -/
theorem t034_l2 {α : Type} [ExactScalar α] :
    Loc (t034_s2_g.spec (α := α)) 1 896 :=
  GenRed.loc t034_s2_g 1 896 (fun q _ hq _ => hq) (fun _ _ => (by decide : (0 : Nat) < 896))

/-- Stage 3 reads each intermediate only where its stage wrote it. -/
theorem t034_l3a {α : Type} [ExactScalar α] :
    Loc (t034_s3_g.spec (α := α)) 1 896 :=
  GenRed.loc t034_s3_g 1 896 (fun q _ hq _ => bound_div (a := 896) (d := 262144) hq) (fun _ _ => (by decide : (0 : Nat) < 896))

theorem t034_l3b {α : Type} [ExactScalar α] :
    Loc (t034_s3_g.spec (α := α)) 2 896 :=
  GenRed.loc t034_s3_g 2 896 (fun q _ hq _ => bound_div (a := 896) (d := 262144) hq) (fun _ _ => (by decide : (0 : Nat) < 896))

/-- Correctness certificate for t034: the composed three-stage pipeline. -/
theorem t034_correct {α : Type} [ExactScalar α] :
    ∀ (bufs : Nat → Buf α) (m1 m2 m3 : Mem α) (q : Nat),
      q < (t034_s3_g.spec (α := α)).outSize →
      runThree (t034_s1_g.prog t034_s1_block t034_s1_nkb)
               (t034_s2_g.prog t034_s2_block t034_s2_nkb)
               (t034_s3_g.prog t034_s3_block t034_s3_nkb) 1 2 bufs m1 m2 m3 q
        = compose3 (t034_s1_g.spec (α := α)) (t034_s2_g.spec (α := α))
            (t034_s3_g.spec (α := α)) 1 2 bufs q :=
  three_stage (by decide) t034_s1_impl t034_s2_impl t034_s3_impl t034_l2 t034_l3a t034_l3b

def t034_s1_kernel : ReduceKernel :=
  { name := "t034_s1", arity := 1, block := t034_s1_block, nkb := t034_s1_nkb, nout := 896, init := FE.zeroC, step := t034_s1_g.step t034_s1_block, stored := t034_s1_g.stored t034_s1_block }
def t034_s2_kernel : ReduceKernel :=
  { name := "t034_s2", arity := 2, block := t034_s2_block, nkb := t034_s2_nkb, nout := 896, init := FE.zeroC, step := t034_s2_g.step t034_s2_block, stored := t034_s2_g.stored t034_s2_block }
def t034_s3_kernel : ReduceKernel :=
  { name := "t034_s3", arity := 3, block := t034_s3_block, nkb := t034_s3_nkb, nout := 234881024, init := FE.zeroC, step := t034_s3_g.step t034_s3_block, stored := t034_s3_g.stored t034_s3_block }
def t034_kernel : PipelineKernel3 :=
  { name := "t034", arity := 1, n1 := 896, n2 := 896, stage1 := t034_s1_kernel, stage2 := t034_s2_kernel, stage3 := t034_s3_kernel }

-- t035: three-stage normalisation, 3 input buffer(s), intermediates 112 and 112 at buffers 3 and 4
--   GroupNorm on (14, 64, 512, 512): 112 statistics over 2097152 elements, eps=1e-05, affine
def t035_s1_g : GenRed :=
  { nout := 112, K := 2097152
  , offs := fun b => ([(IE.add (IE.mul (IE.add (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 8)) (IE.lit 64)) (IE.mul (IE.modi (IE.pid 0) (IE.lit 8)) (IE.lit 8))) (IE.divi IE.rk (IE.lit 262144))) (IE.lit 262144)) (IE.modi IE.rk (IE.lit 262144))), (IE.lit 0), (IE.lit 0), (IE.lit 0), (IE.lit 0)]).getD b (IE.lit 0)
  , inRange := BE.tt
  , body := (SE.inp 0)
  , postOffs := fun b => ([(IE.lit 0), (IE.lit 0), (IE.lit 0), (IE.lit 0), (IE.lit 0)]).getD b (IE.lit 0)
  , post := (SE.inp 0)
  , outGuard := BE.tt
  , nInp := 1 }
def t035_s1_block : Nat := 1024
def t035_s1_nkb : Nat := 2048

theorem t035_s1_wf : t035_s1_g.Wf :=
  { offs_ok := IE.qkOnly_getD _ (by decide)
  , post_ok := IE.qkOnly_getD _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

theorem t035_s1_impl {α : Type} [ExactScalar α] :
    Implements (t035_s1_g.prog t035_s1_block t035_s1_nkb) (t035_s1_g.spec (α := α)) :=
  GenRed.prog_implements t035_s1_g t035_s1_block t035_s1_nkb t035_s1_wf (by decide) (by decide)

def t035_s2_g : GenRed :=
  { nout := 112, K := 2097152
  , offs := fun b => ([(IE.add (IE.mul (IE.add (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 8)) (IE.lit 64)) (IE.mul (IE.modi (IE.pid 0) (IE.lit 8)) (IE.lit 8))) (IE.divi IE.rk (IE.lit 262144))) (IE.lit 262144)) (IE.modi IE.rk (IE.lit 262144))), (IE.lit 0), (IE.lit 0), (IE.pid 0), (IE.lit 0)]).getD b (IE.lit 0)
  , inRange := BE.tt
  , body := (SE.bin .mul (SE.bin .sub (SE.inp 0) (SE.bin .mul (SE.inp 3) (SE.lit false 1 2097152))) (SE.bin .sub (SE.inp 0) (SE.bin .mul (SE.inp 3) (SE.lit false 1 2097152))))
  , postOffs := fun b => ([(IE.lit 0), (IE.lit 0), (IE.lit 0), (IE.lit 0), (IE.lit 0)]).getD b (IE.lit 0)
  , post := (SE.inp 0)
  , outGuard := BE.tt
  , nInp := 4 }
def t035_s2_block : Nat := 1024
def t035_s2_nkb : Nat := 2048

theorem t035_s2_wf : t035_s2_g.Wf :=
  { offs_ok := IE.qkOnly_getD _ (by decide)
  , post_ok := IE.qkOnly_getD _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

theorem t035_s2_impl {α : Type} [ExactScalar α] :
    Implements (t035_s2_g.prog t035_s2_block t035_s2_nkb) (t035_s2_g.spec (α := α)) :=
  GenRed.prog_implements t035_s2_g t035_s2_block t035_s2_nkb t035_s2_wf (by decide) (by decide)

def t035_s3_g : GenRed :=
  { nout := 234881024, K := 1
  , offs := fun b => ([(IE.pid 0), (IE.modi (IE.divi (IE.pid 0) (IE.lit 262144)) (IE.lit 64)), (IE.modi (IE.divi (IE.pid 0) (IE.lit 262144)) (IE.lit 64)), (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 16777216)) (IE.lit 8)) (IE.divi (IE.modi (IE.divi (IE.pid 0) (IE.lit 262144)) (IE.lit 64)) (IE.lit 8))), (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 16777216)) (IE.lit 8)) (IE.divi (IE.modi (IE.divi (IE.pid 0) (IE.lit 262144)) (IE.lit 64)) (IE.lit 8)))]).getD b (IE.lit 0)
  , inRange := BE.tt
  , body := (SE.bin .add (SE.bin .mul (SE.bin .mul (SE.bin .sub (SE.inp 0) (SE.bin .mul (SE.inp 3) (SE.lit false 1 2097152))) (SE.recip (SE.un .sqrt (SE.bin .add (SE.bin .mul (SE.inp 4) (SE.lit false 1 2097152)) (SE.lit false 1 100000))))) (SE.inp 1)) (SE.inp 2))
  , postOffs := fun b => ([(IE.lit 0), (IE.lit 0), (IE.lit 0), (IE.lit 0), (IE.lit 0)]).getD b (IE.lit 0)
  , post := (SE.inp 0)
  , outGuard := BE.tt
  , nInp := 5 }
def t035_s3_block : Nat := 1
def t035_s3_nkb : Nat := 1

theorem t035_s3_wf : t035_s3_g.Wf :=
  { offs_ok := IE.qkOnly_getD _ (by decide)
  , post_ok := IE.qkOnly_getD _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

theorem t035_s3_impl {α : Type} [ExactScalar α] :
    Implements (t035_s3_g.prog t035_s3_block t035_s3_nkb) (t035_s3_g.spec (α := α)) :=
  GenRed.prog_implements t035_s3_g t035_s3_block t035_s3_nkb t035_s3_wf (by decide) (by decide)

/-- Stage 2 reads the first intermediate only where stage 1 wrote it. -/
theorem t035_l2 {α : Type} [ExactScalar α] :
    Loc (t035_s2_g.spec (α := α)) 3 112 :=
  GenRed.loc t035_s2_g 3 112 (fun q _ hq _ => hq) (fun _ _ => (by decide : (0 : Nat) < 112))

/-- Stage 3 reads each intermediate only where its stage wrote it. -/
theorem t035_l3a {α : Type} [ExactScalar α] :
    Loc (t035_s3_g.spec (α := α)) 3 112 :=
  GenRed.loc t035_s3_g 3 112 (fun q _ hq _ => bound_pack (A := 14) (B := 8) (bound_div (a := 14) (d := 16777216) hq) (bound_group (C := 64) (CG := 8) (G := 8) (x := q / 262144) (by decide) (by decide) (by decide))) (fun _ _ => (by decide : (0 : Nat) < 112))

theorem t035_l3b {α : Type} [ExactScalar α] :
    Loc (t035_s3_g.spec (α := α)) 4 112 :=
  GenRed.loc t035_s3_g 4 112 (fun q _ hq _ => bound_pack (A := 14) (B := 8) (bound_div (a := 14) (d := 16777216) hq) (bound_group (C := 64) (CG := 8) (G := 8) (x := q / 262144) (by decide) (by decide) (by decide))) (fun _ _ => (by decide : (0 : Nat) < 112))

/-- Correctness certificate for t035: the composed three-stage pipeline. -/
theorem t035_correct {α : Type} [ExactScalar α] :
    ∀ (bufs : Nat → Buf α) (m1 m2 m3 : Mem α) (q : Nat),
      q < (t035_s3_g.spec (α := α)).outSize →
      runThree (t035_s1_g.prog t035_s1_block t035_s1_nkb)
               (t035_s2_g.prog t035_s2_block t035_s2_nkb)
               (t035_s3_g.prog t035_s3_block t035_s3_nkb) 3 4 bufs m1 m2 m3 q
        = compose3 (t035_s1_g.spec (α := α)) (t035_s2_g.spec (α := α))
            (t035_s3_g.spec (α := α)) 3 4 bufs q :=
  three_stage (by decide) t035_s1_impl t035_s2_impl t035_s3_impl t035_l2 t035_l3a t035_l3b

def t035_s1_kernel : ReduceKernel :=
  { name := "t035_s1", arity := 1, block := t035_s1_block, nkb := t035_s1_nkb, nout := 112, init := FE.zeroC, step := t035_s1_g.step t035_s1_block, stored := t035_s1_g.stored t035_s1_block }
def t035_s2_kernel : ReduceKernel :=
  { name := "t035_s2", arity := 4, block := t035_s2_block, nkb := t035_s2_nkb, nout := 112, init := FE.zeroC, step := t035_s2_g.step t035_s2_block, stored := t035_s2_g.stored t035_s2_block }
def t035_s3_kernel : ReduceKernel :=
  { name := "t035_s3", arity := 5, block := t035_s3_block, nkb := t035_s3_nkb, nout := 234881024, init := FE.zeroC, step := t035_s3_g.step t035_s3_block, stored := t035_s3_g.stored t035_s3_block }
def t035_kernel : PipelineKernel3 :=
  { name := "t035", arity := 3, n1 := 112, n2 := 112, stage1 := t035_s1_kernel, stage2 := t035_s2_kernel, stage3 := t035_s3_kernel }

-- t040: three-stage normalisation, 3 input buffer(s), intermediates 16 and 16 at buffers 3 and 4
--   LayerNorm on (16, 64, 256, 256): 16 statistics over 4194304 elements, eps=1e-05, affine
def t040_s1_g : GenRed :=
  { nout := 16, K := 4194304
  , offs := fun b => ([(IE.add (IE.mul (IE.pid 0) (IE.lit 4194304)) IE.rk), (IE.lit 0), (IE.lit 0), (IE.lit 0), (IE.lit 0)]).getD b (IE.lit 0)
  , inRange := BE.tt
  , body := (SE.inp 0)
  , postOffs := fun b => ([(IE.lit 0), (IE.lit 0), (IE.lit 0), (IE.lit 0), (IE.lit 0)]).getD b (IE.lit 0)
  , post := (SE.inp 0)
  , outGuard := BE.tt
  , nInp := 1 }
def t040_s1_block : Nat := 1024
def t040_s1_nkb : Nat := 4096

theorem t040_s1_wf : t040_s1_g.Wf :=
  { offs_ok := IE.qkOnly_getD _ (by decide)
  , post_ok := IE.qkOnly_getD _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

theorem t040_s1_impl {α : Type} [ExactScalar α] :
    Implements (t040_s1_g.prog t040_s1_block t040_s1_nkb) (t040_s1_g.spec (α := α)) :=
  GenRed.prog_implements t040_s1_g t040_s1_block t040_s1_nkb t040_s1_wf (by decide) (by decide)

def t040_s2_g : GenRed :=
  { nout := 16, K := 4194304
  , offs := fun b => ([(IE.add (IE.mul (IE.pid 0) (IE.lit 4194304)) IE.rk), (IE.lit 0), (IE.lit 0), (IE.pid 0), (IE.lit 0)]).getD b (IE.lit 0)
  , inRange := BE.tt
  , body := (SE.bin .mul (SE.bin .sub (SE.inp 0) (SE.bin .mul (SE.inp 3) (SE.lit false 1 4194304))) (SE.bin .sub (SE.inp 0) (SE.bin .mul (SE.inp 3) (SE.lit false 1 4194304))))
  , postOffs := fun b => ([(IE.lit 0), (IE.lit 0), (IE.lit 0), (IE.lit 0), (IE.lit 0)]).getD b (IE.lit 0)
  , post := (SE.inp 0)
  , outGuard := BE.tt
  , nInp := 4 }
def t040_s2_block : Nat := 1024
def t040_s2_nkb : Nat := 4096

theorem t040_s2_wf : t040_s2_g.Wf :=
  { offs_ok := IE.qkOnly_getD _ (by decide)
  , post_ok := IE.qkOnly_getD _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

theorem t040_s2_impl {α : Type} [ExactScalar α] :
    Implements (t040_s2_g.prog t040_s2_block t040_s2_nkb) (t040_s2_g.spec (α := α)) :=
  GenRed.prog_implements t040_s2_g t040_s2_block t040_s2_nkb t040_s2_wf (by decide) (by decide)

def t040_s3_g : GenRed :=
  { nout := 67108864, K := 1
  , offs := fun b => ([(IE.pid 0), (IE.modi (IE.pid 0) (IE.lit 4194304)), (IE.modi (IE.pid 0) (IE.lit 4194304)), (IE.divi (IE.pid 0) (IE.lit 4194304)), (IE.divi (IE.pid 0) (IE.lit 4194304))]).getD b (IE.lit 0)
  , inRange := BE.tt
  , body := (SE.bin .add (SE.bin .mul (SE.bin .mul (SE.bin .sub (SE.inp 0) (SE.bin .mul (SE.inp 3) (SE.lit false 1 4194304))) (SE.recip (SE.un .sqrt (SE.bin .add (SE.bin .mul (SE.inp 4) (SE.lit false 1 4194304)) (SE.lit false 1 100000))))) (SE.inp 1)) (SE.inp 2))
  , postOffs := fun b => ([(IE.lit 0), (IE.lit 0), (IE.lit 0), (IE.lit 0), (IE.lit 0)]).getD b (IE.lit 0)
  , post := (SE.inp 0)
  , outGuard := BE.tt
  , nInp := 5 }
def t040_s3_block : Nat := 1
def t040_s3_nkb : Nat := 1

theorem t040_s3_wf : t040_s3_g.Wf :=
  { offs_ok := IE.qkOnly_getD _ (by decide)
  , post_ok := IE.qkOnly_getD _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

theorem t040_s3_impl {α : Type} [ExactScalar α] :
    Implements (t040_s3_g.prog t040_s3_block t040_s3_nkb) (t040_s3_g.spec (α := α)) :=
  GenRed.prog_implements t040_s3_g t040_s3_block t040_s3_nkb t040_s3_wf (by decide) (by decide)

/-- Stage 2 reads the first intermediate only where stage 1 wrote it. -/
theorem t040_l2 {α : Type} [ExactScalar α] :
    Loc (t040_s2_g.spec (α := α)) 3 16 :=
  GenRed.loc t040_s2_g 3 16 (fun q _ hq _ => hq) (fun _ _ => (by decide : (0 : Nat) < 16))

/-- Stage 3 reads each intermediate only where its stage wrote it. -/
theorem t040_l3a {α : Type} [ExactScalar α] :
    Loc (t040_s3_g.spec (α := α)) 3 16 :=
  GenRed.loc t040_s3_g 3 16 (fun q _ hq _ => bound_div (a := 16) (d := 4194304) hq) (fun _ _ => (by decide : (0 : Nat) < 16))

theorem t040_l3b {α : Type} [ExactScalar α] :
    Loc (t040_s3_g.spec (α := α)) 4 16 :=
  GenRed.loc t040_s3_g 4 16 (fun q _ hq _ => bound_div (a := 16) (d := 4194304) hq) (fun _ _ => (by decide : (0 : Nat) < 16))

/-- Correctness certificate for t040: the composed three-stage pipeline. -/
theorem t040_correct {α : Type} [ExactScalar α] :
    ∀ (bufs : Nat → Buf α) (m1 m2 m3 : Mem α) (q : Nat),
      q < (t040_s3_g.spec (α := α)).outSize →
      runThree (t040_s1_g.prog t040_s1_block t040_s1_nkb)
               (t040_s2_g.prog t040_s2_block t040_s2_nkb)
               (t040_s3_g.prog t040_s3_block t040_s3_nkb) 3 4 bufs m1 m2 m3 q
        = compose3 (t040_s1_g.spec (α := α)) (t040_s2_g.spec (α := α))
            (t040_s3_g.spec (α := α)) 3 4 bufs q :=
  three_stage (by decide) t040_s1_impl t040_s2_impl t040_s3_impl t040_l2 t040_l3a t040_l3b

def t040_s1_kernel : ReduceKernel :=
  { name := "t040_s1", arity := 1, block := t040_s1_block, nkb := t040_s1_nkb, nout := 16, init := FE.zeroC, step := t040_s1_g.step t040_s1_block, stored := t040_s1_g.stored t040_s1_block }
def t040_s2_kernel : ReduceKernel :=
  { name := "t040_s2", arity := 4, block := t040_s2_block, nkb := t040_s2_nkb, nout := 16, init := FE.zeroC, step := t040_s2_g.step t040_s2_block, stored := t040_s2_g.stored t040_s2_block }
def t040_s3_kernel : ReduceKernel :=
  { name := "t040_s3", arity := 5, block := t040_s3_block, nkb := t040_s3_nkb, nout := 67108864, init := FE.zeroC, step := t040_s3_g.step t040_s3_block, stored := t040_s3_g.stored t040_s3_block }
def t040_kernel : PipelineKernel3 :=
  { name := "t040", arity := 3, n1 := 16, n2 := 16, stage1 := t040_s1_kernel, stage2 := t040_s2_kernel, stage3 := t040_s3_kernel }

def main : IO Unit := do
  IO.FS.writeFile "../generated/t033.py" t033_kernel.render
  IO.FS.writeFile "../generated/t034.py" t034_kernel.render
  IO.FS.writeFile "../generated/t035.py" t035_kernel.render
  IO.FS.writeFile "../generated/t040.py" t040_kernel.render
