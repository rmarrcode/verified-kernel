/-
  GENERATED FILE -- do not edit.

  Written by verified_kernel.vk.compile. Each task below carries a
  `theorem` instantiating its family's correctness theorem at the exact
  numbers the generator chose. `lake build` checking this file is what
  makes the corresponding kernel in generated/ a verified kernel.
-/
import VerifiedKernel

open VerifiedKernel

-- A chain of several hundred stages puts a list of that length in front of
-- the elaborator. Recursion depth is an elaboration limit, not a checking
-- one: raising it changes nothing about what counts as a proof, and the
-- kernel still checks every term. `#print axioms` remains the real test.
set_option maxRecDepth 100000
-- Likewise a budget, not a criterion. Reading the last of a chain's several
-- hundred recorded sizes means walking the list to it, so the size
-- obligation costs more the longer the chain is.
set_option maxHeartbeats 4000000

-- sm0: three-stage normalisation, 1 input buffer(s), intermediates 8 and 8 at buffers 1 and 2
--   softmax over dim 1 of (8, 64): row max, then sum of exp(x - max), then divide
def sm0_s1_g : MaxRed :=
  { nout := 8, K := 64
  , offs := IE.sparse [(0, (IE.add (IE.mul (IE.pid 0) (IE.lit 64)) IE.rk))]
  , body := (SE.inp 0)
  , postOffs := IE.sparse []
  , post := (SE.inp 0)
  , nInp := 1, idxSlot := 1 }
def sm0_s1_block : Nat := 64
def sm0_s1_nkb : Nat := 1

theorem sm0_s1_wf : sm0_s1_g.Wf :=
  { offs_ok := IE.qkOnly_sparse _ (by decide)
  , post_ok := IE.qkOnly_sparse _ (by decide) }

theorem sm0_s1_impl {α : Type} [ExactScalar α] :
    Implements (sm0_s1_g.prog sm0_s1_block sm0_s1_nkb) (sm0_s1_g.spec (α := α)) :=
  MaxRed.prog_implements sm0_s1_g sm0_s1_block sm0_s1_nkb sm0_s1_wf (by decide) (by decide) (by decide)


def sm0_s2_g : GenRed :=
  { nout := 8, K := 64
  , offs := IE.sparse [(0, (IE.add (IE.mul (IE.pid 0) (IE.lit 64)) IE.rk)), (1, (IE.pid 0))]
  , inRange := BE.tt
  , body := (SE.un .exp (SE.bin .sub (SE.inp 0) (SE.inp 1)))
  , postOffs := IE.sparse []
  , post := (SE.inp 0)
  , outGuard := BE.tt
  , nInp := 2, idxSlot := 1048576 }
def sm0_s2_block : Nat := 64
def sm0_s2_nkb : Nat := 1

theorem sm0_s2_wf : sm0_s2_g.Wf :=
  { offs_ok := IE.qkOnly_sparse _ (by decide)
  , post_ok := IE.qkOnly_sparse _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

theorem sm0_s2_impl {α : Type} [ExactScalar α] :
    Implements (sm0_s2_g.prog sm0_s2_block sm0_s2_nkb) (sm0_s2_g.spec (α := α)) :=
  GenRed.prog_implements sm0_s2_g sm0_s2_block sm0_s2_nkb sm0_s2_wf (by decide) (by decide)

def sm0_s3_g : GenRed :=
  { nout := 512, K := 1
  , offs := IE.sparse [(0, (IE.pid 0)), (1, (IE.divi (IE.pid 0) (IE.lit 64))), (2, (IE.divi (IE.pid 0) (IE.lit 64)))]
  , inRange := BE.tt
  , body := (SE.bin .mul (SE.un .exp (SE.bin .sub (SE.inp 0) (SE.inp 1))) (SE.recip (SE.inp 2)))
  , postOffs := IE.sparse []
  , post := (SE.inp 0)
  , outGuard := BE.tt
  , nInp := 3, idxSlot := 1048576 }
def sm0_s3_block : Nat := 1
def sm0_s3_nkb : Nat := 1

theorem sm0_s3_wf : sm0_s3_g.Wf :=
  { offs_ok := IE.qkOnly_sparse _ (by decide)
  , post_ok := IE.qkOnly_sparse _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

theorem sm0_s3_impl {α : Type} [ExactScalar α] :
    Implements (sm0_s3_g.prog sm0_s3_block sm0_s3_nkb) (sm0_s3_g.spec (α := α)) :=
  GenRed.prog_implements sm0_s3_g sm0_s3_block sm0_s3_nkb sm0_s3_wf (by decide) (by decide)

/-- Stage 2 reads the first intermediate only where stage 1 wrote it. -/
theorem sm0_l2 {α : Type} [ExactScalar α] :
    Loc (sm0_s2_g.spec (α := α)) 1 8 :=
  GenRed.loc sm0_s2_g 1 8 (fun q _ hq _ => hq) (fun _ _ => (by decide : (0 : Nat) < 8))

/-- Stage 3 reads each intermediate only where its stage wrote it. -/
theorem sm0_l3a {α : Type} [ExactScalar α] :
    Loc (sm0_s3_g.spec (α := α)) 1 8 :=
  GenRed.loc sm0_s3_g 1 8 (fun q k hq hk => (bound_div (a := 8) (d := 64) hq)) (fun _ _ => (by decide : (0 : Nat) < 8))

theorem sm0_l3b {α : Type} [ExactScalar α] :
    Loc (sm0_s3_g.spec (α := α)) 2 8 :=
  GenRed.loc sm0_s3_g 2 8 (fun q k hq hk => (bound_div (a := 8) (d := 64) hq)) (fun _ _ => (by decide : (0 : Nat) < 8))

/-- Correctness certificate for sm0: the composed three-stage pipeline. -/
theorem sm0_correct {α : Type} [ExactScalar α] :
    ∀ (bufs : Nat → Buf α) (m1 m2 m3 : Mem α) (q : Nat),
      q < (sm0_s3_g.spec (α := α)).outSize →
      runThree (sm0_s1_g.prog sm0_s1_block sm0_s1_nkb)
               (sm0_s2_g.prog sm0_s2_block sm0_s2_nkb)
               (sm0_s3_g.prog sm0_s3_block sm0_s3_nkb) 1 2 bufs m1 m2 m3 q
        = compose3 (sm0_s1_g.spec (α := α)) (sm0_s2_g.spec (α := α))
            (sm0_s3_g.spec (α := α)) 1 2 bufs q :=
  three_stage (by decide) sm0_s1_impl sm0_s2_impl sm0_s3_impl sm0_l2 sm0_l3a sm0_l3b

def sm0_s1_kernel : ReduceKernel :=
  { name := "sm0_s1", arity := 1, block := sm0_s1_block, nkb := sm0_s1_nkb, nout := 8, init := sm0_s1_g.seed, step := sm0_s1_g.step sm0_s1_block, stored := sm0_s1_g.stored sm0_s1_block }
def sm0_s2_kernel : ReduceKernel :=
  { name := "sm0_s2", arity := 2, block := sm0_s2_block, nkb := sm0_s2_nkb, nout := 8, init := FE.zeroC, step := sm0_s2_g.step sm0_s2_block, stored := sm0_s2_g.stored sm0_s2_block }
def sm0_s3_kernel : ReduceKernel :=
  { name := "sm0_s3", arity := 3, block := sm0_s3_block, nkb := sm0_s3_nkb, nout := 512, init := FE.zeroC, step := sm0_s3_g.step sm0_s3_block, stored := sm0_s3_g.stored sm0_s3_block }
def sm0_kernel : PipelineKernel3 :=
  { name := "sm0", arity := 1, n1 := 8, n2 := 8, stage1 := sm0_s1_kernel, stage2 := sm0_s2_kernel, stage3 := sm0_s3_kernel }

-- sm1: three-stage normalisation, 1 input buffer(s), intermediates 64 and 64 at buffers 1 and 2
--   softmax over dim 0 of (8, 64): row max, then sum of exp(x - max), then divide
def sm1_s1_g : MaxRed :=
  { nout := 64, K := 8
  , offs := IE.sparse [(0, (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 64)) (IE.lit 8)) IE.rk) (IE.lit 64)) (IE.modi (IE.pid 0) (IE.lit 64))))]
  , body := (SE.inp 0)
  , postOffs := IE.sparse []
  , post := (SE.inp 0)
  , nInp := 1, idxSlot := 1 }
def sm1_s1_block : Nat := 8
def sm1_s1_nkb : Nat := 1

theorem sm1_s1_wf : sm1_s1_g.Wf :=
  { offs_ok := IE.qkOnly_sparse _ (by decide)
  , post_ok := IE.qkOnly_sparse _ (by decide) }

theorem sm1_s1_impl {α : Type} [ExactScalar α] :
    Implements (sm1_s1_g.prog sm1_s1_block sm1_s1_nkb) (sm1_s1_g.spec (α := α)) :=
  MaxRed.prog_implements sm1_s1_g sm1_s1_block sm1_s1_nkb sm1_s1_wf (by decide) (by decide) (by decide)


def sm1_s2_g : GenRed :=
  { nout := 64, K := 8
  , offs := IE.sparse [(0, (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 64)) (IE.lit 8)) IE.rk) (IE.lit 64)) (IE.modi (IE.pid 0) (IE.lit 64)))), (1, (IE.pid 0))]
  , inRange := BE.tt
  , body := (SE.un .exp (SE.bin .sub (SE.inp 0) (SE.inp 1)))
  , postOffs := IE.sparse []
  , post := (SE.inp 0)
  , outGuard := BE.tt
  , nInp := 2, idxSlot := 1048576 }
def sm1_s2_block : Nat := 8
def sm1_s2_nkb : Nat := 1

theorem sm1_s2_wf : sm1_s2_g.Wf :=
  { offs_ok := IE.qkOnly_sparse _ (by decide)
  , post_ok := IE.qkOnly_sparse _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

theorem sm1_s2_impl {α : Type} [ExactScalar α] :
    Implements (sm1_s2_g.prog sm1_s2_block sm1_s2_nkb) (sm1_s2_g.spec (α := α)) :=
  GenRed.prog_implements sm1_s2_g sm1_s2_block sm1_s2_nkb sm1_s2_wf (by decide) (by decide)

def sm1_s3_g : GenRed :=
  { nout := 512, K := 1
  , offs := IE.sparse [(0, (IE.pid 0)), (1, (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.mul (IE.lit 8) (IE.lit 64))) (IE.lit 64)) (IE.modi (IE.pid 0) (IE.lit 64)))), (2, (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.mul (IE.lit 8) (IE.lit 64))) (IE.lit 64)) (IE.modi (IE.pid 0) (IE.lit 64))))]
  , inRange := BE.tt
  , body := (SE.bin .mul (SE.un .exp (SE.bin .sub (SE.inp 0) (SE.inp 1))) (SE.recip (SE.inp 2)))
  , postOffs := IE.sparse []
  , post := (SE.inp 0)
  , outGuard := BE.tt
  , nInp := 3, idxSlot := 1048576 }
def sm1_s3_block : Nat := 1
def sm1_s3_nkb : Nat := 1

theorem sm1_s3_wf : sm1_s3_g.Wf :=
  { offs_ok := IE.qkOnly_sparse _ (by decide)
  , post_ok := IE.qkOnly_sparse _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

theorem sm1_s3_impl {α : Type} [ExactScalar α] :
    Implements (sm1_s3_g.prog sm1_s3_block sm1_s3_nkb) (sm1_s3_g.spec (α := α)) :=
  GenRed.prog_implements sm1_s3_g sm1_s3_block sm1_s3_nkb sm1_s3_wf (by decide) (by decide)

/-- Stage 2 reads the first intermediate only where stage 1 wrote it. -/
theorem sm1_l2 {α : Type} [ExactScalar α] :
    Loc (sm1_s2_g.spec (α := α)) 1 64 :=
  GenRed.loc sm1_s2_g 1 64 (fun q _ hq _ => hq) (fun _ _ => (by decide : (0 : Nat) < 64))

/-- Stage 3 reads each intermediate only where its stage wrote it. -/
theorem sm1_l3a {α : Type} [ExactScalar α] :
    Loc (sm1_s3_g.spec (α := α)) 1 64 :=
  GenRed.loc sm1_s3_g 1 64 (fun q k hq hk => (bound_row (outer := 1) (K := 8) (inner := 64) (by decide) hq)) (fun _ _ => (by decide : (0 : Nat) < 64))

theorem sm1_l3b {α : Type} [ExactScalar α] :
    Loc (sm1_s3_g.spec (α := α)) 2 64 :=
  GenRed.loc sm1_s3_g 2 64 (fun q k hq hk => (bound_row (outer := 1) (K := 8) (inner := 64) (by decide) hq)) (fun _ _ => (by decide : (0 : Nat) < 64))

/-- Correctness certificate for sm1: the composed three-stage pipeline. -/
theorem sm1_correct {α : Type} [ExactScalar α] :
    ∀ (bufs : Nat → Buf α) (m1 m2 m3 : Mem α) (q : Nat),
      q < (sm1_s3_g.spec (α := α)).outSize →
      runThree (sm1_s1_g.prog sm1_s1_block sm1_s1_nkb)
               (sm1_s2_g.prog sm1_s2_block sm1_s2_nkb)
               (sm1_s3_g.prog sm1_s3_block sm1_s3_nkb) 1 2 bufs m1 m2 m3 q
        = compose3 (sm1_s1_g.spec (α := α)) (sm1_s2_g.spec (α := α))
            (sm1_s3_g.spec (α := α)) 1 2 bufs q :=
  three_stage (by decide) sm1_s1_impl sm1_s2_impl sm1_s3_impl sm1_l2 sm1_l3a sm1_l3b

def sm1_s1_kernel : ReduceKernel :=
  { name := "sm1_s1", arity := 1, block := sm1_s1_block, nkb := sm1_s1_nkb, nout := 64, init := sm1_s1_g.seed, step := sm1_s1_g.step sm1_s1_block, stored := sm1_s1_g.stored sm1_s1_block }
def sm1_s2_kernel : ReduceKernel :=
  { name := "sm1_s2", arity := 2, block := sm1_s2_block, nkb := sm1_s2_nkb, nout := 64, init := FE.zeroC, step := sm1_s2_g.step sm1_s2_block, stored := sm1_s2_g.stored sm1_s2_block }
def sm1_s3_kernel : ReduceKernel :=
  { name := "sm1_s3", arity := 3, block := sm1_s3_block, nkb := sm1_s3_nkb, nout := 512, init := FE.zeroC, step := sm1_s3_g.step sm1_s3_block, stored := sm1_s3_g.stored sm1_s3_block }
def sm1_kernel : PipelineKernel3 :=
  { name := "sm1", arity := 1, n1 := 64, n2 := 64, stage1 := sm1_s1_kernel, stage2 := sm1_s2_kernel, stage3 := sm1_s3_kernel }

-- sm2: three-stage normalisation, 1 input buffer(s), intermediates 8 and 8 at buffers 1 and 2
--   log_softmax over dim 1 of (8, 64): row max, then sum of exp(x - max), then divide
def sm2_s1_g : MaxRed :=
  { nout := 8, K := 64
  , offs := IE.sparse [(0, (IE.add (IE.mul (IE.pid 0) (IE.lit 64)) IE.rk))]
  , body := (SE.inp 0)
  , postOffs := IE.sparse []
  , post := (SE.inp 0)
  , nInp := 1, idxSlot := 1 }
def sm2_s1_block : Nat := 64
def sm2_s1_nkb : Nat := 1

theorem sm2_s1_wf : sm2_s1_g.Wf :=
  { offs_ok := IE.qkOnly_sparse _ (by decide)
  , post_ok := IE.qkOnly_sparse _ (by decide) }

theorem sm2_s1_impl {α : Type} [ExactScalar α] :
    Implements (sm2_s1_g.prog sm2_s1_block sm2_s1_nkb) (sm2_s1_g.spec (α := α)) :=
  MaxRed.prog_implements sm2_s1_g sm2_s1_block sm2_s1_nkb sm2_s1_wf (by decide) (by decide) (by decide)


def sm2_s2_g : GenRed :=
  { nout := 8, K := 64
  , offs := IE.sparse [(0, (IE.add (IE.mul (IE.pid 0) (IE.lit 64)) IE.rk)), (1, (IE.pid 0))]
  , inRange := BE.tt
  , body := (SE.un .exp (SE.bin .sub (SE.inp 0) (SE.inp 1)))
  , postOffs := IE.sparse []
  , post := (SE.inp 0)
  , outGuard := BE.tt
  , nInp := 2, idxSlot := 1048576 }
def sm2_s2_block : Nat := 64
def sm2_s2_nkb : Nat := 1

theorem sm2_s2_wf : sm2_s2_g.Wf :=
  { offs_ok := IE.qkOnly_sparse _ (by decide)
  , post_ok := IE.qkOnly_sparse _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

theorem sm2_s2_impl {α : Type} [ExactScalar α] :
    Implements (sm2_s2_g.prog sm2_s2_block sm2_s2_nkb) (sm2_s2_g.spec (α := α)) :=
  GenRed.prog_implements sm2_s2_g sm2_s2_block sm2_s2_nkb sm2_s2_wf (by decide) (by decide)

def sm2_s3_g : GenRed :=
  { nout := 512, K := 1
  , offs := IE.sparse [(0, (IE.pid 0)), (1, (IE.divi (IE.pid 0) (IE.lit 64))), (2, (IE.divi (IE.pid 0) (IE.lit 64)))]
  , inRange := BE.tt
  , body := (SE.bin .sub (SE.bin .sub (SE.inp 0) (SE.inp 1)) (SE.un .log (SE.inp 2)))
  , postOffs := IE.sparse []
  , post := (SE.inp 0)
  , outGuard := BE.tt
  , nInp := 3, idxSlot := 1048576 }
def sm2_s3_block : Nat := 1
def sm2_s3_nkb : Nat := 1

theorem sm2_s3_wf : sm2_s3_g.Wf :=
  { offs_ok := IE.qkOnly_sparse _ (by decide)
  , post_ok := IE.qkOnly_sparse _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

theorem sm2_s3_impl {α : Type} [ExactScalar α] :
    Implements (sm2_s3_g.prog sm2_s3_block sm2_s3_nkb) (sm2_s3_g.spec (α := α)) :=
  GenRed.prog_implements sm2_s3_g sm2_s3_block sm2_s3_nkb sm2_s3_wf (by decide) (by decide)

/-- Stage 2 reads the first intermediate only where stage 1 wrote it. -/
theorem sm2_l2 {α : Type} [ExactScalar α] :
    Loc (sm2_s2_g.spec (α := α)) 1 8 :=
  GenRed.loc sm2_s2_g 1 8 (fun q _ hq _ => hq) (fun _ _ => (by decide : (0 : Nat) < 8))

/-- Stage 3 reads each intermediate only where its stage wrote it. -/
theorem sm2_l3a {α : Type} [ExactScalar α] :
    Loc (sm2_s3_g.spec (α := α)) 1 8 :=
  GenRed.loc sm2_s3_g 1 8 (fun q k hq hk => (bound_div (a := 8) (d := 64) hq)) (fun _ _ => (by decide : (0 : Nat) < 8))

theorem sm2_l3b {α : Type} [ExactScalar α] :
    Loc (sm2_s3_g.spec (α := α)) 2 8 :=
  GenRed.loc sm2_s3_g 2 8 (fun q k hq hk => (bound_div (a := 8) (d := 64) hq)) (fun _ _ => (by decide : (0 : Nat) < 8))

/-- Correctness certificate for sm2: the composed three-stage pipeline. -/
theorem sm2_correct {α : Type} [ExactScalar α] :
    ∀ (bufs : Nat → Buf α) (m1 m2 m3 : Mem α) (q : Nat),
      q < (sm2_s3_g.spec (α := α)).outSize →
      runThree (sm2_s1_g.prog sm2_s1_block sm2_s1_nkb)
               (sm2_s2_g.prog sm2_s2_block sm2_s2_nkb)
               (sm2_s3_g.prog sm2_s3_block sm2_s3_nkb) 1 2 bufs m1 m2 m3 q
        = compose3 (sm2_s1_g.spec (α := α)) (sm2_s2_g.spec (α := α))
            (sm2_s3_g.spec (α := α)) 1 2 bufs q :=
  three_stage (by decide) sm2_s1_impl sm2_s2_impl sm2_s3_impl sm2_l2 sm2_l3a sm2_l3b

def sm2_s1_kernel : ReduceKernel :=
  { name := "sm2_s1", arity := 1, block := sm2_s1_block, nkb := sm2_s1_nkb, nout := 8, init := sm2_s1_g.seed, step := sm2_s1_g.step sm2_s1_block, stored := sm2_s1_g.stored sm2_s1_block }
def sm2_s2_kernel : ReduceKernel :=
  { name := "sm2_s2", arity := 2, block := sm2_s2_block, nkb := sm2_s2_nkb, nout := 8, init := FE.zeroC, step := sm2_s2_g.step sm2_s2_block, stored := sm2_s2_g.stored sm2_s2_block }
def sm2_s3_kernel : ReduceKernel :=
  { name := "sm2_s3", arity := 3, block := sm2_s3_block, nkb := sm2_s3_nkb, nout := 512, init := FE.zeroC, step := sm2_s3_g.step sm2_s3_block, stored := sm2_s3_g.stored sm2_s3_block }
def sm2_kernel : PipelineKernel3 :=
  { name := "sm2", arity := 1, n1 := 8, n2 := 8, stage1 := sm2_s1_kernel, stage2 := sm2_s2_kernel, stage3 := sm2_s3_kernel }

-- sm3: three-stage normalisation, 1 input buffer(s), intermediates 32 and 32 at buffers 1 and 2
--   softmax over dim 1 of (4, 16, 8): row max, then sum of exp(x - max), then divide
def sm3_s1_g : MaxRed :=
  { nout := 32, K := 16
  , offs := IE.sparse [(0, (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 8)) (IE.lit 16)) IE.rk) (IE.lit 8)) (IE.modi (IE.pid 0) (IE.lit 8))))]
  , body := (SE.inp 0)
  , postOffs := IE.sparse []
  , post := (SE.inp 0)
  , nInp := 1, idxSlot := 1 }
def sm3_s1_block : Nat := 16
def sm3_s1_nkb : Nat := 1

theorem sm3_s1_wf : sm3_s1_g.Wf :=
  { offs_ok := IE.qkOnly_sparse _ (by decide)
  , post_ok := IE.qkOnly_sparse _ (by decide) }

theorem sm3_s1_impl {α : Type} [ExactScalar α] :
    Implements (sm3_s1_g.prog sm3_s1_block sm3_s1_nkb) (sm3_s1_g.spec (α := α)) :=
  MaxRed.prog_implements sm3_s1_g sm3_s1_block sm3_s1_nkb sm3_s1_wf (by decide) (by decide) (by decide)


def sm3_s2_g : GenRed :=
  { nout := 32, K := 16
  , offs := IE.sparse [(0, (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 8)) (IE.lit 16)) IE.rk) (IE.lit 8)) (IE.modi (IE.pid 0) (IE.lit 8)))), (1, (IE.pid 0))]
  , inRange := BE.tt
  , body := (SE.un .exp (SE.bin .sub (SE.inp 0) (SE.inp 1)))
  , postOffs := IE.sparse []
  , post := (SE.inp 0)
  , outGuard := BE.tt
  , nInp := 2, idxSlot := 1048576 }
def sm3_s2_block : Nat := 16
def sm3_s2_nkb : Nat := 1

theorem sm3_s2_wf : sm3_s2_g.Wf :=
  { offs_ok := IE.qkOnly_sparse _ (by decide)
  , post_ok := IE.qkOnly_sparse _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

theorem sm3_s2_impl {α : Type} [ExactScalar α] :
    Implements (sm3_s2_g.prog sm3_s2_block sm3_s2_nkb) (sm3_s2_g.spec (α := α)) :=
  GenRed.prog_implements sm3_s2_g sm3_s2_block sm3_s2_nkb sm3_s2_wf (by decide) (by decide)

def sm3_s3_g : GenRed :=
  { nout := 512, K := 1
  , offs := IE.sparse [(0, (IE.pid 0)), (1, (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.mul (IE.lit 16) (IE.lit 8))) (IE.lit 8)) (IE.modi (IE.pid 0) (IE.lit 8)))), (2, (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.mul (IE.lit 16) (IE.lit 8))) (IE.lit 8)) (IE.modi (IE.pid 0) (IE.lit 8))))]
  , inRange := BE.tt
  , body := (SE.bin .mul (SE.un .exp (SE.bin .sub (SE.inp 0) (SE.inp 1))) (SE.recip (SE.inp 2)))
  , postOffs := IE.sparse []
  , post := (SE.inp 0)
  , outGuard := BE.tt
  , nInp := 3, idxSlot := 1048576 }
def sm3_s3_block : Nat := 1
def sm3_s3_nkb : Nat := 1

theorem sm3_s3_wf : sm3_s3_g.Wf :=
  { offs_ok := IE.qkOnly_sparse _ (by decide)
  , post_ok := IE.qkOnly_sparse _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

theorem sm3_s3_impl {α : Type} [ExactScalar α] :
    Implements (sm3_s3_g.prog sm3_s3_block sm3_s3_nkb) (sm3_s3_g.spec (α := α)) :=
  GenRed.prog_implements sm3_s3_g sm3_s3_block sm3_s3_nkb sm3_s3_wf (by decide) (by decide)

/-- Stage 2 reads the first intermediate only where stage 1 wrote it. -/
theorem sm3_l2 {α : Type} [ExactScalar α] :
    Loc (sm3_s2_g.spec (α := α)) 1 32 :=
  GenRed.loc sm3_s2_g 1 32 (fun q _ hq _ => hq) (fun _ _ => (by decide : (0 : Nat) < 32))

/-- Stage 3 reads each intermediate only where its stage wrote it. -/
theorem sm3_l3a {α : Type} [ExactScalar α] :
    Loc (sm3_s3_g.spec (α := α)) 1 32 :=
  GenRed.loc sm3_s3_g 1 32 (fun q k hq hk => (bound_row (outer := 4) (K := 16) (inner := 8) (by decide) hq)) (fun _ _ => (by decide : (0 : Nat) < 32))

theorem sm3_l3b {α : Type} [ExactScalar α] :
    Loc (sm3_s3_g.spec (α := α)) 2 32 :=
  GenRed.loc sm3_s3_g 2 32 (fun q k hq hk => (bound_row (outer := 4) (K := 16) (inner := 8) (by decide) hq)) (fun _ _ => (by decide : (0 : Nat) < 32))

/-- Correctness certificate for sm3: the composed three-stage pipeline. -/
theorem sm3_correct {α : Type} [ExactScalar α] :
    ∀ (bufs : Nat → Buf α) (m1 m2 m3 : Mem α) (q : Nat),
      q < (sm3_s3_g.spec (α := α)).outSize →
      runThree (sm3_s1_g.prog sm3_s1_block sm3_s1_nkb)
               (sm3_s2_g.prog sm3_s2_block sm3_s2_nkb)
               (sm3_s3_g.prog sm3_s3_block sm3_s3_nkb) 1 2 bufs m1 m2 m3 q
        = compose3 (sm3_s1_g.spec (α := α)) (sm3_s2_g.spec (α := α))
            (sm3_s3_g.spec (α := α)) 1 2 bufs q :=
  three_stage (by decide) sm3_s1_impl sm3_s2_impl sm3_s3_impl sm3_l2 sm3_l3a sm3_l3b

def sm3_s1_kernel : ReduceKernel :=
  { name := "sm3_s1", arity := 1, block := sm3_s1_block, nkb := sm3_s1_nkb, nout := 32, init := sm3_s1_g.seed, step := sm3_s1_g.step sm3_s1_block, stored := sm3_s1_g.stored sm3_s1_block }
def sm3_s2_kernel : ReduceKernel :=
  { name := "sm3_s2", arity := 2, block := sm3_s2_block, nkb := sm3_s2_nkb, nout := 32, init := FE.zeroC, step := sm3_s2_g.step sm3_s2_block, stored := sm3_s2_g.stored sm3_s2_block }
def sm3_s3_kernel : ReduceKernel :=
  { name := "sm3_s3", arity := 3, block := sm3_s3_block, nkb := sm3_s3_nkb, nout := 512, init := FE.zeroC, step := sm3_s3_g.step sm3_s3_block, stored := sm3_s3_g.stored sm3_s3_block }
def sm3_kernel : PipelineKernel3 :=
  { name := "sm3", arity := 1, n1 := 32, n2 := 32, stage1 := sm3_s1_kernel, stage2 := sm3_s2_kernel, stage3 := sm3_s3_kernel }

def main : IO Unit := do
  IO.FS.writeFile "../generated/sm0.py" sm0_kernel.render
  IO.FS.writeFile "../generated/sm1.py" sm1_kernel.render
  IO.FS.writeFile "../generated/sm2.py" sm2_kernel.render
  IO.FS.writeFile "../generated/sm3.py" sm3_kernel.render
