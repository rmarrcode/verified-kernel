/-
  GENERATED FILE -- do not edit.

  Written by verified_kernel.vk.compile. Each task below carries a
  `theorem` instantiating its family's correctness theorem at the exact
  numbers the generator chose. `lake build` checking this file is what
  makes the corresponding kernel in generated/ a verified kernel.
-/
import VerifiedKernel

open VerifiedKernel

-- t099: three-stage normalisation, 3 input buffer(s), intermediates 32768 and 32768 at buffers 3 and 4
--   triplet margin loss: batch 32768, 8192 features, margin=1.0, eps=1e-06
def t099_s1_g : GenRed :=
  { nout := 32768, K := 8192
  , offs := fun b => ([(IE.add (IE.mul (IE.pid 0) (IE.lit 8192)) IE.rk), (IE.add (IE.mul (IE.pid 0) (IE.lit 8192)) IE.rk), (IE.lit 0), (IE.lit 0), (IE.lit 0)]).getD b (IE.lit 0)
  , inRange := BE.tt
  , body := (SE.bin .mul (SE.bin .add (SE.bin .sub (SE.inp 0) (SE.inp 1)) (SE.lit false 1 1000000)) (SE.bin .add (SE.bin .sub (SE.inp 0) (SE.inp 1)) (SE.lit false 1 1000000)))
  , postOffs := fun b => ([(IE.lit 0), (IE.lit 0), (IE.lit 0), (IE.lit 0), (IE.lit 0)]).getD b (IE.lit 0)
  , post := (SE.inp 0)
  , outGuard := BE.tt
  , nInp := 3 }
def t099_s1_block : Nat := 1024
def t099_s1_nkb : Nat := 8

theorem t099_s1_wf : t099_s1_g.Wf :=
  { offs_ok := IE.qkOnly_getD _ (by decide)
  , post_ok := IE.qkOnly_getD _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

theorem t099_s1_impl {α : Type} [ExactScalar α] :
    Implements (t099_s1_g.prog t099_s1_block t099_s1_nkb) (t099_s1_g.spec (α := α)) :=
  GenRed.prog_implements t099_s1_g t099_s1_block t099_s1_nkb t099_s1_wf (by decide) (by decide)

def t099_s2_g : GenRed :=
  { nout := 32768, K := 8192
  , offs := fun b => ([(IE.add (IE.mul (IE.pid 0) (IE.lit 8192)) IE.rk), (IE.lit 0), (IE.add (IE.mul (IE.pid 0) (IE.lit 8192)) IE.rk), (IE.lit 0), (IE.lit 0)]).getD b (IE.lit 0)
  , inRange := BE.tt
  , body := (SE.bin .mul (SE.bin .add (SE.bin .sub (SE.inp 0) (SE.inp 2)) (SE.lit false 1 1000000)) (SE.bin .add (SE.bin .sub (SE.inp 0) (SE.inp 2)) (SE.lit false 1 1000000)))
  , postOffs := fun b => ([(IE.lit 0), (IE.lit 0), (IE.lit 0), (IE.lit 0), (IE.lit 0)]).getD b (IE.lit 0)
  , post := (SE.inp 0)
  , outGuard := BE.tt
  , nInp := 4 }
def t099_s2_block : Nat := 1024
def t099_s2_nkb : Nat := 8

theorem t099_s2_wf : t099_s2_g.Wf :=
  { offs_ok := IE.qkOnly_getD _ (by decide)
  , post_ok := IE.qkOnly_getD _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

theorem t099_s2_impl {α : Type} [ExactScalar α] :
    Implements (t099_s2_g.prog t099_s2_block t099_s2_nkb) (t099_s2_g.spec (α := α)) :=
  GenRed.prog_implements t099_s2_g t099_s2_block t099_s2_nkb t099_s2_wf (by decide) (by decide)

def t099_s3_g : GenRed :=
  { nout := 1, K := 32768
  , offs := fun b => ([(IE.lit 0), (IE.lit 0), (IE.lit 0), IE.rk, IE.rk]).getD b (IE.lit 0)
  , inRange := BE.tt
  , body := (SE.bin .max (SE.bin .add (SE.bin .sub (SE.un .sqrt (SE.inp 3)) (SE.un .sqrt (SE.inp 4))) (SE.lit false 1 1)) (SE.lit false 0 1))
  , postOffs := fun b => ([(IE.lit 0), (IE.lit 0), (IE.lit 0), (IE.lit 0), (IE.lit 0)]).getD b (IE.lit 0)
  , post := (SE.bin .mul (SE.inp 0) (SE.lit false 1 32768))
  , outGuard := BE.tt
  , nInp := 5 }
def t099_s3_block : Nat := 1024
def t099_s3_nkb : Nat := 32

theorem t099_s3_wf : t099_s3_g.Wf :=
  { offs_ok := IE.qkOnly_getD _ (by decide)
  , post_ok := IE.qkOnly_getD _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

theorem t099_s3_impl {α : Type} [ExactScalar α] :
    Implements (t099_s3_g.prog t099_s3_block t099_s3_nkb) (t099_s3_g.spec (α := α)) :=
  GenRed.prog_implements t099_s3_g t099_s3_block t099_s3_nkb t099_s3_wf (by decide) (by decide)

/-- Stage 2 reads the first intermediate only where stage 1 wrote it. -/
theorem t099_l2 {α : Type} [ExactScalar α] :
    Loc (t099_s2_g.spec (α := α)) 3 32768 :=
  GenRed.loc t099_s2_g 3 32768 (fun _ _ _ _ => (by decide : (0 : Nat) < 32768)) (fun _ _ => (by decide : (0 : Nat) < 32768))

/-- Stage 3 reads each intermediate only where its stage wrote it. -/
theorem t099_l3a {α : Type} [ExactScalar α] :
    Loc (t099_s3_g.spec (α := α)) 3 32768 :=
  GenRed.loc t099_s3_g 3 32768 (fun _ k _ hk => hk) (fun _ _ => (by decide : (0 : Nat) < 32768))

theorem t099_l3b {α : Type} [ExactScalar α] :
    Loc (t099_s3_g.spec (α := α)) 4 32768 :=
  GenRed.loc t099_s3_g 4 32768 (fun _ k _ hk => hk) (fun _ _ => (by decide : (0 : Nat) < 32768))

/-- Correctness certificate for t099: the composed three-stage pipeline. -/
theorem t099_correct {α : Type} [ExactScalar α] :
    ∀ (bufs : Nat → Buf α) (m1 m2 m3 : Mem α) (q : Nat),
      q < (t099_s3_g.spec (α := α)).outSize →
      runThree (t099_s1_g.prog t099_s1_block t099_s1_nkb)
               (t099_s2_g.prog t099_s2_block t099_s2_nkb)
               (t099_s3_g.prog t099_s3_block t099_s3_nkb) 3 4 bufs m1 m2 m3 q
        = compose3 (t099_s1_g.spec (α := α)) (t099_s2_g.spec (α := α))
            (t099_s3_g.spec (α := α)) 3 4 bufs q :=
  three_stage (by decide) t099_s1_impl t099_s2_impl t099_s3_impl t099_l2 t099_l3a t099_l3b

def t099_s1_kernel : ReduceKernel :=
  { name := "t099_s1", arity := 3, block := t099_s1_block, nkb := t099_s1_nkb, nout := 32768, init := FE.zeroC, step := t099_s1_g.step t099_s1_block, stored := t099_s1_g.stored t099_s1_block }
def t099_s2_kernel : ReduceKernel :=
  { name := "t099_s2", arity := 4, block := t099_s2_block, nkb := t099_s2_nkb, nout := 32768, init := FE.zeroC, step := t099_s2_g.step t099_s2_block, stored := t099_s2_g.stored t099_s2_block }
def t099_s3_kernel : ReduceKernel :=
  { name := "t099_s3", arity := 5, block := t099_s3_block, nkb := t099_s3_nkb, nout := 1, init := FE.zeroC, step := t099_s3_g.step t099_s3_block, stored := t099_s3_g.stored t099_s3_block }
def t099_kernel : PipelineKernel3 :=
  { name := "t099", arity := 3, n1 := 32768, n2 := 32768, stage1 := t099_s1_kernel, stage2 := t099_s2_kernel, stage3 := t099_s3_kernel }

def main : IO Unit := do
  IO.FS.writeFile "../generated/t099.py" t099_kernel.render
