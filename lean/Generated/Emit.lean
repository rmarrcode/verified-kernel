/-
  GENERATED FILE -- do not edit.

  Written by verified_kernel.vk.compile. Each task below carries a
  `theorem` instantiating its family's correctness theorem at the exact
  numbers the generator chose. `lake build` checking this file is what
  makes the corresponding kernel in generated/ a verified kernel.
-/
import VerifiedKernel

open VerifiedKernel

-- t095: three-stage normalisation, 2 input buffer(s), intermediates 32768 and 32768 at buffers 2 and 3
--   cross entropy: batch 32768, 4096 classes
def t095_s1_g : GenRed :=
  { nout := 32768, K := 4096
  , offs := fun b => ([(IE.add (IE.mul (IE.pid 0) (IE.lit 4096)) IE.rk), (IE.lit 0), (IE.lit 0), (IE.lit 0)]).getD b (IE.lit 0)
  , inRange := BE.tt
  , body := (SE.un .exp (SE.inp 0))
  , postOffs := fun b => ([(IE.lit 0), (IE.lit 0), (IE.lit 0), (IE.lit 0)]).getD b (IE.lit 0)
  , post := (SE.inp 0)
  , outGuard := BE.tt
  , nInp := 1, idxSlot := 1048576 }
def t095_s1_block : Nat := 1024
def t095_s1_nkb : Nat := 4

theorem t095_s1_wf : t095_s1_g.Wf :=
  { offs_ok := IE.qkOnly_getD _ (by decide)
  , post_ok := IE.qkOnly_getD _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

theorem t095_s1_impl {α : Type} [ExactScalar α] :
    Implements (t095_s1_g.prog t095_s1_block t095_s1_nkb) (t095_s1_g.spec (α := α)) :=
  GenRed.prog_implements t095_s1_g t095_s1_block t095_s1_nkb t095_s1_wf (by decide) (by decide)

def t095_s2_g : GenRed :=
  { nout := 32768, K := 4096
  , offs := fun b => ([(IE.add (IE.mul (IE.pid 0) (IE.lit 4096)) IE.rk), (IE.pid 0), (IE.lit 0), (IE.lit 0)]).getD b (IE.lit 0)
  , inRange := BE.tt
  , body := (SE.selLe (SE.inp 1) (SE.inp 4) (SE.selLe (SE.inp 4) (SE.inp 1) (SE.inp 0) (SE.lit false 0 1)) (SE.lit false 0 1))
  , postOffs := fun b => ([(IE.lit 0), (IE.lit 0), (IE.lit 0), (IE.lit 0)]).getD b (IE.lit 0)
  , post := (SE.inp 0)
  , outGuard := BE.tt
  , nInp := 2, idxSlot := 4 }
def t095_s2_block : Nat := 1024
def t095_s2_nkb : Nat := 4

theorem t095_s2_wf : t095_s2_g.Wf :=
  { offs_ok := IE.qkOnly_getD _ (by decide)
  , post_ok := IE.qkOnly_getD _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

theorem t095_s2_impl {α : Type} [ExactScalar α] :
    Implements (t095_s2_g.prog t095_s2_block t095_s2_nkb) (t095_s2_g.spec (α := α)) :=
  GenRed.prog_implements t095_s2_g t095_s2_block t095_s2_nkb t095_s2_wf (by decide) (by decide)

def t095_s3_g : GenRed :=
  { nout := 1, K := 32768
  , offs := fun b => ([(IE.lit 0), (IE.lit 0), IE.rk, IE.rk]).getD b (IE.lit 0)
  , inRange := BE.tt
  , body := (SE.bin .sub (SE.un .log (SE.inp 2)) (SE.inp 3))
  , postOffs := fun b => ([(IE.lit 0), (IE.lit 0), (IE.lit 0), (IE.lit 0)]).getD b (IE.lit 0)
  , post := (SE.bin .mul (SE.inp 0) (SE.lit false 1 32768))
  , outGuard := BE.tt
  , nInp := 4, idxSlot := 1048576 }
def t095_s3_block : Nat := 1024
def t095_s3_nkb : Nat := 32

theorem t095_s3_wf : t095_s3_g.Wf :=
  { offs_ok := IE.qkOnly_getD _ (by decide)
  , post_ok := IE.qkOnly_getD _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

theorem t095_s3_impl {α : Type} [ExactScalar α] :
    Implements (t095_s3_g.prog t095_s3_block t095_s3_nkb) (t095_s3_g.spec (α := α)) :=
  GenRed.prog_implements t095_s3_g t095_s3_block t095_s3_nkb t095_s3_wf (by decide) (by decide)

/-- Stage 2 reads the first intermediate only where stage 1 wrote it. -/
theorem t095_l2 {α : Type} [ExactScalar α] :
    Loc (t095_s2_g.spec (α := α)) 2 32768 :=
  GenRed.loc t095_s2_g 2 32768 (fun _ _ _ _ => (by decide : (0 : Nat) < 32768)) (fun _ _ => (by decide : (0 : Nat) < 32768))

/-- Stage 3 reads each intermediate only where its stage wrote it. -/
theorem t095_l3a {α : Type} [ExactScalar α] :
    Loc (t095_s3_g.spec (α := α)) 2 32768 :=
  GenRed.loc t095_s3_g 2 32768 (fun _ k _ hk => hk) (fun _ _ => (by decide : (0 : Nat) < 32768))

theorem t095_l3b {α : Type} [ExactScalar α] :
    Loc (t095_s3_g.spec (α := α)) 3 32768 :=
  GenRed.loc t095_s3_g 3 32768 (fun _ k _ hk => hk) (fun _ _ => (by decide : (0 : Nat) < 32768))

/-- Correctness certificate for t095: the composed three-stage pipeline. -/
theorem t095_correct {α : Type} [ExactScalar α] :
    ∀ (bufs : Nat → Buf α) (m1 m2 m3 : Mem α) (q : Nat),
      q < (t095_s3_g.spec (α := α)).outSize →
      runThree (t095_s1_g.prog t095_s1_block t095_s1_nkb)
               (t095_s2_g.prog t095_s2_block t095_s2_nkb)
               (t095_s3_g.prog t095_s3_block t095_s3_nkb) 2 3 bufs m1 m2 m3 q
        = compose3 (t095_s1_g.spec (α := α)) (t095_s2_g.spec (α := α))
            (t095_s3_g.spec (α := α)) 2 3 bufs q :=
  three_stage (by decide) t095_s1_impl t095_s2_impl t095_s3_impl t095_l2 t095_l3a t095_l3b

def t095_s1_kernel : ReduceKernel :=
  { name := "t095_s1", arity := 1, block := t095_s1_block, nkb := t095_s1_nkb, nout := 32768, init := FE.zeroC, step := t095_s1_g.step t095_s1_block, stored := t095_s1_g.stored t095_s1_block }
def t095_s2_kernel : ReduceKernel :=
  { name := "t095_s2", arity := 2, block := t095_s2_block, nkb := t095_s2_nkb, nout := 32768, init := FE.zeroC, step := t095_s2_g.step t095_s2_block, stored := t095_s2_g.stored t095_s2_block }
def t095_s3_kernel : ReduceKernel :=
  { name := "t095_s3", arity := 4, block := t095_s3_block, nkb := t095_s3_nkb, nout := 1, init := FE.zeroC, step := t095_s3_g.step t095_s3_block, stored := t095_s3_g.stored t095_s3_block }
def t095_kernel : PipelineKernel3 :=
  { name := "t095", arity := 2, n1 := 32768, n2 := 32768, stage1 := t095_s1_kernel, stage2 := t095_s2_kernel, stage3 := t095_s3_kernel }

def main : IO Unit := do
  IO.FS.writeFile "../generated/t095.py" t095_kernel.render
