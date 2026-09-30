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

-- pool0: max reduction, 1 input(s), 288 outputs, extent 9
--   maxpool2d: N=2 C=4 k=(3, 3) stride=(2, 2) pad=(0, 0) dil=(1, 1); coordinates clamped rather than masked
def pool0_g : MaxRed :=
  { nout := 288, K := 9
  , offs := IE.sparse [(0, (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 144)) (IE.lit 4)) (IE.modi (IE.divi (IE.pid 0) (IE.lit 36)) (IE.lit 4))) (IE.lit 13)) (IE.sub (IE.add (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 6)) (IE.lit 6)) (IE.lit 2)) (IE.sub (IE.add (IE.divi IE.rk (IE.lit 3)) (IE.sub (IE.sub (IE.lit 0) (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 6)) (IE.lit 6)) (IE.lit 2))) (IE.divi IE.rk (IE.lit 3)))) (IE.sub (IE.add (IE.divi IE.rk (IE.lit 3)) (IE.sub (IE.sub (IE.lit 0) (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 6)) (IE.lit 6)) (IE.lit 2))) (IE.divi IE.rk (IE.lit 3)))) (IE.sub (IE.lit 12) (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 6)) (IE.lit 6)) (IE.lit 2)))))) (IE.sub (IE.add (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 6)) (IE.lit 6)) (IE.lit 2)) (IE.sub (IE.add (IE.divi IE.rk (IE.lit 3)) (IE.sub (IE.sub (IE.lit 0) (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 6)) (IE.lit 6)) (IE.lit 2))) (IE.divi IE.rk (IE.lit 3)))) (IE.sub (IE.add (IE.divi IE.rk (IE.lit 3)) (IE.sub (IE.sub (IE.lit 0) (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 6)) (IE.lit 6)) (IE.lit 2))) (IE.divi IE.rk (IE.lit 3)))) (IE.sub (IE.lit 12) (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 6)) (IE.lit 6)) (IE.lit 2)))))) (IE.lit 12)))) (IE.lit 13)) (IE.sub (IE.add (IE.mul (IE.modi (IE.pid 0) (IE.lit 6)) (IE.lit 2)) (IE.sub (IE.add (IE.modi IE.rk (IE.lit 3)) (IE.sub (IE.sub (IE.lit 0) (IE.mul (IE.modi (IE.pid 0) (IE.lit 6)) (IE.lit 2))) (IE.modi IE.rk (IE.lit 3)))) (IE.sub (IE.add (IE.modi IE.rk (IE.lit 3)) (IE.sub (IE.sub (IE.lit 0) (IE.mul (IE.modi (IE.pid 0) (IE.lit 6)) (IE.lit 2))) (IE.modi IE.rk (IE.lit 3)))) (IE.sub (IE.lit 12) (IE.mul (IE.modi (IE.pid 0) (IE.lit 6)) (IE.lit 2)))))) (IE.sub (IE.add (IE.mul (IE.modi (IE.pid 0) (IE.lit 6)) (IE.lit 2)) (IE.sub (IE.add (IE.modi IE.rk (IE.lit 3)) (IE.sub (IE.sub (IE.lit 0) (IE.mul (IE.modi (IE.pid 0) (IE.lit 6)) (IE.lit 2))) (IE.modi IE.rk (IE.lit 3)))) (IE.sub (IE.add (IE.modi IE.rk (IE.lit 3)) (IE.sub (IE.sub (IE.lit 0) (IE.mul (IE.modi (IE.pid 0) (IE.lit 6)) (IE.lit 2))) (IE.modi IE.rk (IE.lit 3)))) (IE.sub (IE.lit 12) (IE.mul (IE.modi (IE.pid 0) (IE.lit 6)) (IE.lit 2)))))) (IE.lit 12)))))]
  , body := (SE.inp 0)
  , postOffs := IE.sparse []
  , post := (SE.inp 0)
  , nInp := 1, idxSlot := 1 }
def pool0_block : Nat := 8
def pool0_nkb : Nat := 2

theorem pool0_wf : pool0_g.Wf :=
  { offs_ok := IE.qkOnly_sparse _ (by decide)
  , post_ok := IE.qkOnly_sparse _ (by decide) }

/-- Correctness certificate for pool0. -/
theorem pool0_correct {α : Type} [ExactScalar α] :
    Implements (pool0_g.prog pool0_block pool0_nkb) (pool0_g.spec (α := α)) :=
  MaxRed.prog_implements pool0_g pool0_block pool0_nkb pool0_wf (by decide) (by decide) (by decide)

def pool0_kernel : ReduceKernel :=
  { name := "pool0", arity := 1, block := pool0_block
  , nkb := pool0_nkb, nout := 288
  , init := pool0_g.seed
  , step := pool0_g.step pool0_block
  , stored := pool0_g.stored pool0_block }

-- pool1: max reduction, 1 input(s), 512 outputs, extent 9
--   maxpool2d: N=2 C=4 k=(3, 3) stride=(2, 2) pad=(1, 1) dil=(1, 1); coordinates clamped rather than masked
def pool1_g : MaxRed :=
  { nout := 512, K := 9
  , offs := IE.sparse [(0, (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 256)) (IE.lit 4)) (IE.modi (IE.divi (IE.pid 0) (IE.lit 64)) (IE.lit 4))) (IE.lit 14)) (IE.sub (IE.sub (IE.add (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 8)) (IE.lit 8)) (IE.lit 2)) (IE.sub (IE.add (IE.divi IE.rk (IE.lit 3)) (IE.sub (IE.sub (IE.lit 1) (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 8)) (IE.lit 8)) (IE.lit 2))) (IE.divi IE.rk (IE.lit 3)))) (IE.sub (IE.add (IE.divi IE.rk (IE.lit 3)) (IE.sub (IE.sub (IE.lit 1) (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 8)) (IE.lit 8)) (IE.lit 2))) (IE.divi IE.rk (IE.lit 3)))) (IE.sub (IE.lit 14) (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 8)) (IE.lit 8)) (IE.lit 2)))))) (IE.lit 1)) (IE.sub (IE.sub (IE.add (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 8)) (IE.lit 8)) (IE.lit 2)) (IE.sub (IE.add (IE.divi IE.rk (IE.lit 3)) (IE.sub (IE.sub (IE.lit 1) (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 8)) (IE.lit 8)) (IE.lit 2))) (IE.divi IE.rk (IE.lit 3)))) (IE.sub (IE.add (IE.divi IE.rk (IE.lit 3)) (IE.sub (IE.sub (IE.lit 1) (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 8)) (IE.lit 8)) (IE.lit 2))) (IE.divi IE.rk (IE.lit 3)))) (IE.sub (IE.lit 14) (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 8)) (IE.lit 8)) (IE.lit 2)))))) (IE.lit 1)) (IE.lit 13)))) (IE.lit 14)) (IE.sub (IE.sub (IE.add (IE.mul (IE.modi (IE.pid 0) (IE.lit 8)) (IE.lit 2)) (IE.sub (IE.add (IE.modi IE.rk (IE.lit 3)) (IE.sub (IE.sub (IE.lit 1) (IE.mul (IE.modi (IE.pid 0) (IE.lit 8)) (IE.lit 2))) (IE.modi IE.rk (IE.lit 3)))) (IE.sub (IE.add (IE.modi IE.rk (IE.lit 3)) (IE.sub (IE.sub (IE.lit 1) (IE.mul (IE.modi (IE.pid 0) (IE.lit 8)) (IE.lit 2))) (IE.modi IE.rk (IE.lit 3)))) (IE.sub (IE.lit 14) (IE.mul (IE.modi (IE.pid 0) (IE.lit 8)) (IE.lit 2)))))) (IE.lit 1)) (IE.sub (IE.sub (IE.add (IE.mul (IE.modi (IE.pid 0) (IE.lit 8)) (IE.lit 2)) (IE.sub (IE.add (IE.modi IE.rk (IE.lit 3)) (IE.sub (IE.sub (IE.lit 1) (IE.mul (IE.modi (IE.pid 0) (IE.lit 8)) (IE.lit 2))) (IE.modi IE.rk (IE.lit 3)))) (IE.sub (IE.add (IE.modi IE.rk (IE.lit 3)) (IE.sub (IE.sub (IE.lit 1) (IE.mul (IE.modi (IE.pid 0) (IE.lit 8)) (IE.lit 2))) (IE.modi IE.rk (IE.lit 3)))) (IE.sub (IE.lit 14) (IE.mul (IE.modi (IE.pid 0) (IE.lit 8)) (IE.lit 2)))))) (IE.lit 1)) (IE.lit 13)))))]
  , body := (SE.inp 0)
  , postOffs := IE.sparse []
  , post := (SE.inp 0)
  , nInp := 1, idxSlot := 1 }
def pool1_block : Nat := 8
def pool1_nkb : Nat := 2

theorem pool1_wf : pool1_g.Wf :=
  { offs_ok := IE.qkOnly_sparse _ (by decide)
  , post_ok := IE.qkOnly_sparse _ (by decide) }

/-- Correctness certificate for pool1. -/
theorem pool1_correct {α : Type} [ExactScalar α] :
    Implements (pool1_g.prog pool1_block pool1_nkb) (pool1_g.spec (α := α)) :=
  MaxRed.prog_implements pool1_g pool1_block pool1_nkb pool1_wf (by decide) (by decide) (by decide)

def pool1_kernel : ReduceKernel :=
  { name := "pool1", arity := 1, block := pool1_block
  , nkb := pool1_nkb, nout := 512
  , init := pool1_g.seed
  , step := pool1_g.step pool1_block
  , stored := pool1_g.stored pool1_block }

-- pool2: max reduction, 1 input(s), 288 outputs, extent 9
--   maxpool2d: N=2 C=4 k=(3, 3) stride=(2, 2) pad=(0, 0) dil=(1, 1); coordinates clamped rather than masked
def pool2_g : MaxRed :=
  { nout := 288, K := 9
  , offs := IE.sparse [(0, (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 144)) (IE.lit 4)) (IE.modi (IE.divi (IE.pid 0) (IE.lit 36)) (IE.lit 4))) (IE.lit 13)) (IE.sub (IE.add (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 6)) (IE.lit 6)) (IE.lit 2)) (IE.sub (IE.add (IE.divi IE.rk (IE.lit 3)) (IE.sub (IE.sub (IE.lit 0) (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 6)) (IE.lit 6)) (IE.lit 2))) (IE.divi IE.rk (IE.lit 3)))) (IE.sub (IE.add (IE.divi IE.rk (IE.lit 3)) (IE.sub (IE.sub (IE.lit 0) (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 6)) (IE.lit 6)) (IE.lit 2))) (IE.divi IE.rk (IE.lit 3)))) (IE.sub (IE.lit 12) (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 6)) (IE.lit 6)) (IE.lit 2)))))) (IE.sub (IE.add (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 6)) (IE.lit 6)) (IE.lit 2)) (IE.sub (IE.add (IE.divi IE.rk (IE.lit 3)) (IE.sub (IE.sub (IE.lit 0) (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 6)) (IE.lit 6)) (IE.lit 2))) (IE.divi IE.rk (IE.lit 3)))) (IE.sub (IE.add (IE.divi IE.rk (IE.lit 3)) (IE.sub (IE.sub (IE.lit 0) (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 6)) (IE.lit 6)) (IE.lit 2))) (IE.divi IE.rk (IE.lit 3)))) (IE.sub (IE.lit 12) (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 6)) (IE.lit 6)) (IE.lit 2)))))) (IE.lit 12)))) (IE.lit 13)) (IE.sub (IE.add (IE.mul (IE.modi (IE.pid 0) (IE.lit 6)) (IE.lit 2)) (IE.sub (IE.add (IE.modi IE.rk (IE.lit 3)) (IE.sub (IE.sub (IE.lit 0) (IE.mul (IE.modi (IE.pid 0) (IE.lit 6)) (IE.lit 2))) (IE.modi IE.rk (IE.lit 3)))) (IE.sub (IE.add (IE.modi IE.rk (IE.lit 3)) (IE.sub (IE.sub (IE.lit 0) (IE.mul (IE.modi (IE.pid 0) (IE.lit 6)) (IE.lit 2))) (IE.modi IE.rk (IE.lit 3)))) (IE.sub (IE.lit 12) (IE.mul (IE.modi (IE.pid 0) (IE.lit 6)) (IE.lit 2)))))) (IE.sub (IE.add (IE.mul (IE.modi (IE.pid 0) (IE.lit 6)) (IE.lit 2)) (IE.sub (IE.add (IE.modi IE.rk (IE.lit 3)) (IE.sub (IE.sub (IE.lit 0) (IE.mul (IE.modi (IE.pid 0) (IE.lit 6)) (IE.lit 2))) (IE.modi IE.rk (IE.lit 3)))) (IE.sub (IE.add (IE.modi IE.rk (IE.lit 3)) (IE.sub (IE.sub (IE.lit 0) (IE.mul (IE.modi (IE.pid 0) (IE.lit 6)) (IE.lit 2))) (IE.modi IE.rk (IE.lit 3)))) (IE.sub (IE.lit 12) (IE.mul (IE.modi (IE.pid 0) (IE.lit 6)) (IE.lit 2)))))) (IE.lit 12)))))]
  , body := (SE.inp 0)
  , postOffs := IE.sparse []
  , post := (SE.inp 0)
  , nInp := 1, idxSlot := 1 }
def pool2_block : Nat := 8
def pool2_nkb : Nat := 2

theorem pool2_wf : pool2_g.Wf :=
  { offs_ok := IE.qkOnly_sparse _ (by decide)
  , post_ok := IE.qkOnly_sparse _ (by decide) }

/-- Correctness certificate for pool2. -/
theorem pool2_correct {α : Type} [ExactScalar α] :
    Implements (pool2_g.prog pool2_block pool2_nkb) (pool2_g.spec (α := α)) :=
  MaxRed.prog_implements pool2_g pool2_block pool2_nkb pool2_wf (by decide) (by decide) (by decide)

def pool2_kernel : ReduceKernel :=
  { name := "pool2", arity := 1, block := pool2_block
  , nkb := pool2_nkb, nout := 288
  , init := pool2_g.seed
  , step := pool2_g.step pool2_block
  , stored := pool2_g.stored pool2_block }

-- pool3: max reduction, 1 input(s), 200 outputs, extent 4
--   maxpool2d: N=2 C=4 k=(2, 2) stride=(2, 2) pad=(0, 0) dil=(2, 2); coordinates clamped rather than masked
def pool3_g : MaxRed :=
  { nout := 200, K := 4
  , offs := IE.sparse [(0, (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 100)) (IE.lit 4)) (IE.modi (IE.divi (IE.pid 0) (IE.lit 25)) (IE.lit 4))) (IE.lit 11)) (IE.sub (IE.add (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 5)) (IE.lit 5)) (IE.lit 2)) (IE.mul (IE.sub (IE.add (IE.divi IE.rk (IE.lit 2)) (IE.sub (IE.divi (IE.add (IE.sub (IE.lit 0) (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 5)) (IE.lit 5)) (IE.lit 2))) (IE.lit 1)) (IE.lit 2)) (IE.divi IE.rk (IE.lit 2)))) (IE.sub (IE.add (IE.divi IE.rk (IE.lit 2)) (IE.sub (IE.divi (IE.add (IE.sub (IE.lit 0) (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 5)) (IE.lit 5)) (IE.lit 2))) (IE.lit 1)) (IE.lit 2)) (IE.divi IE.rk (IE.lit 2)))) (IE.divi (IE.sub (IE.lit 10) (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 5)) (IE.lit 5)) (IE.lit 2))) (IE.lit 2)))) (IE.lit 2))) (IE.sub (IE.add (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 5)) (IE.lit 5)) (IE.lit 2)) (IE.mul (IE.sub (IE.add (IE.divi IE.rk (IE.lit 2)) (IE.sub (IE.divi (IE.add (IE.sub (IE.lit 0) (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 5)) (IE.lit 5)) (IE.lit 2))) (IE.lit 1)) (IE.lit 2)) (IE.divi IE.rk (IE.lit 2)))) (IE.sub (IE.add (IE.divi IE.rk (IE.lit 2)) (IE.sub (IE.divi (IE.add (IE.sub (IE.lit 0) (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 5)) (IE.lit 5)) (IE.lit 2))) (IE.lit 1)) (IE.lit 2)) (IE.divi IE.rk (IE.lit 2)))) (IE.divi (IE.sub (IE.lit 10) (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 5)) (IE.lit 5)) (IE.lit 2))) (IE.lit 2)))) (IE.lit 2))) (IE.lit 10)))) (IE.lit 11)) (IE.sub (IE.add (IE.mul (IE.modi (IE.pid 0) (IE.lit 5)) (IE.lit 2)) (IE.mul (IE.sub (IE.add (IE.modi IE.rk (IE.lit 2)) (IE.sub (IE.divi (IE.add (IE.sub (IE.lit 0) (IE.mul (IE.modi (IE.pid 0) (IE.lit 5)) (IE.lit 2))) (IE.lit 1)) (IE.lit 2)) (IE.modi IE.rk (IE.lit 2)))) (IE.sub (IE.add (IE.modi IE.rk (IE.lit 2)) (IE.sub (IE.divi (IE.add (IE.sub (IE.lit 0) (IE.mul (IE.modi (IE.pid 0) (IE.lit 5)) (IE.lit 2))) (IE.lit 1)) (IE.lit 2)) (IE.modi IE.rk (IE.lit 2)))) (IE.divi (IE.sub (IE.lit 10) (IE.mul (IE.modi (IE.pid 0) (IE.lit 5)) (IE.lit 2))) (IE.lit 2)))) (IE.lit 2))) (IE.sub (IE.add (IE.mul (IE.modi (IE.pid 0) (IE.lit 5)) (IE.lit 2)) (IE.mul (IE.sub (IE.add (IE.modi IE.rk (IE.lit 2)) (IE.sub (IE.divi (IE.add (IE.sub (IE.lit 0) (IE.mul (IE.modi (IE.pid 0) (IE.lit 5)) (IE.lit 2))) (IE.lit 1)) (IE.lit 2)) (IE.modi IE.rk (IE.lit 2)))) (IE.sub (IE.add (IE.modi IE.rk (IE.lit 2)) (IE.sub (IE.divi (IE.add (IE.sub (IE.lit 0) (IE.mul (IE.modi (IE.pid 0) (IE.lit 5)) (IE.lit 2))) (IE.lit 1)) (IE.lit 2)) (IE.modi IE.rk (IE.lit 2)))) (IE.divi (IE.sub (IE.lit 10) (IE.mul (IE.modi (IE.pid 0) (IE.lit 5)) (IE.lit 2))) (IE.lit 2)))) (IE.lit 2))) (IE.lit 10)))))]
  , body := (SE.inp 0)
  , postOffs := IE.sparse []
  , post := (SE.inp 0)
  , nInp := 1, idxSlot := 1 }
def pool3_block : Nat := 4
def pool3_nkb : Nat := 1

theorem pool3_wf : pool3_g.Wf :=
  { offs_ok := IE.qkOnly_sparse _ (by decide)
  , post_ok := IE.qkOnly_sparse _ (by decide) }

/-- Correctness certificate for pool3. -/
theorem pool3_correct {α : Type} [ExactScalar α] :
    Implements (pool3_g.prog pool3_block pool3_nkb) (pool3_g.spec (α := α)) :=
  MaxRed.prog_implements pool3_g pool3_block pool3_nkb pool3_wf (by decide) (by decide) (by decide)

def pool3_kernel : ReduceKernel :=
  { name := "pool3", arity := 1, block := pool3_block
  , nkb := pool3_nkb, nout := 200
  , init := pool3_g.seed
  , step := pool3_g.step pool3_block
  , stored := pool3_g.stored pool3_block }

-- pool4: max reduction, 1 input(s), 288 outputs, extent 4
--   maxpool2d: N=2 C=4 k=(2, 2) stride=(2, 2) pad=(0, 0) dil=(1, 1); coordinates clamped rather than masked
def pool4_g : MaxRed :=
  { nout := 288, K := 4
  , offs := IE.sparse [(0, (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 144)) (IE.lit 4)) (IE.modi (IE.divi (IE.pid 0) (IE.lit 36)) (IE.lit 4))) (IE.lit 12)) (IE.sub (IE.add (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 6)) (IE.lit 6)) (IE.lit 2)) (IE.sub (IE.add (IE.divi IE.rk (IE.lit 2)) (IE.sub (IE.sub (IE.lit 0) (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 6)) (IE.lit 6)) (IE.lit 2))) (IE.divi IE.rk (IE.lit 2)))) (IE.sub (IE.add (IE.divi IE.rk (IE.lit 2)) (IE.sub (IE.sub (IE.lit 0) (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 6)) (IE.lit 6)) (IE.lit 2))) (IE.divi IE.rk (IE.lit 2)))) (IE.sub (IE.lit 11) (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 6)) (IE.lit 6)) (IE.lit 2)))))) (IE.sub (IE.add (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 6)) (IE.lit 6)) (IE.lit 2)) (IE.sub (IE.add (IE.divi IE.rk (IE.lit 2)) (IE.sub (IE.sub (IE.lit 0) (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 6)) (IE.lit 6)) (IE.lit 2))) (IE.divi IE.rk (IE.lit 2)))) (IE.sub (IE.add (IE.divi IE.rk (IE.lit 2)) (IE.sub (IE.sub (IE.lit 0) (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 6)) (IE.lit 6)) (IE.lit 2))) (IE.divi IE.rk (IE.lit 2)))) (IE.sub (IE.lit 11) (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 6)) (IE.lit 6)) (IE.lit 2)))))) (IE.lit 11)))) (IE.lit 12)) (IE.sub (IE.add (IE.mul (IE.modi (IE.pid 0) (IE.lit 6)) (IE.lit 2)) (IE.sub (IE.add (IE.modi IE.rk (IE.lit 2)) (IE.sub (IE.sub (IE.lit 0) (IE.mul (IE.modi (IE.pid 0) (IE.lit 6)) (IE.lit 2))) (IE.modi IE.rk (IE.lit 2)))) (IE.sub (IE.add (IE.modi IE.rk (IE.lit 2)) (IE.sub (IE.sub (IE.lit 0) (IE.mul (IE.modi (IE.pid 0) (IE.lit 6)) (IE.lit 2))) (IE.modi IE.rk (IE.lit 2)))) (IE.sub (IE.lit 11) (IE.mul (IE.modi (IE.pid 0) (IE.lit 6)) (IE.lit 2)))))) (IE.sub (IE.add (IE.mul (IE.modi (IE.pid 0) (IE.lit 6)) (IE.lit 2)) (IE.sub (IE.add (IE.modi IE.rk (IE.lit 2)) (IE.sub (IE.sub (IE.lit 0) (IE.mul (IE.modi (IE.pid 0) (IE.lit 6)) (IE.lit 2))) (IE.modi IE.rk (IE.lit 2)))) (IE.sub (IE.add (IE.modi IE.rk (IE.lit 2)) (IE.sub (IE.sub (IE.lit 0) (IE.mul (IE.modi (IE.pid 0) (IE.lit 6)) (IE.lit 2))) (IE.modi IE.rk (IE.lit 2)))) (IE.sub (IE.lit 11) (IE.mul (IE.modi (IE.pid 0) (IE.lit 6)) (IE.lit 2)))))) (IE.lit 11)))))]
  , body := (SE.inp 0)
  , postOffs := IE.sparse []
  , post := (SE.inp 0)
  , nInp := 1, idxSlot := 1 }
def pool4_block : Nat := 4
def pool4_nkb : Nat := 1

theorem pool4_wf : pool4_g.Wf :=
  { offs_ok := IE.qkOnly_sparse _ (by decide)
  , post_ok := IE.qkOnly_sparse _ (by decide) }

/-- Correctness certificate for pool4. -/
theorem pool4_correct {α : Type} [ExactScalar α] :
    Implements (pool4_g.prog pool4_block pool4_nkb) (pool4_g.spec (α := α)) :=
  MaxRed.prog_implements pool4_g pool4_block pool4_nkb pool4_wf (by decide) (by decide) (by decide)

def pool4_kernel : ReduceKernel :=
  { name := "pool4", arity := 1, block := pool4_block
  , nkb := pool4_nkb, nout := 288
  , init := pool4_g.seed
  , step := pool4_g.step pool4_block
  , stored := pool4_g.stored pool4_block }

-- pool5: max reduction, 1 input(s), 392 outputs, extent 9
--   maxpool2d: N=2 C=4 k=(3, 3) stride=(2, 2) pad=(1, 1) dil=(1, 1); coordinates clamped rather than masked
def pool5_g : MaxRed :=
  { nout := 392, K := 9
  , offs := IE.sparse [(0, (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 196)) (IE.lit 4)) (IE.modi (IE.divi (IE.pid 0) (IE.lit 49)) (IE.lit 4))) (IE.lit 13)) (IE.sub (IE.sub (IE.add (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 7)) (IE.lit 7)) (IE.lit 2)) (IE.sub (IE.add (IE.divi IE.rk (IE.lit 3)) (IE.sub (IE.sub (IE.lit 1) (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 7)) (IE.lit 7)) (IE.lit 2))) (IE.divi IE.rk (IE.lit 3)))) (IE.sub (IE.add (IE.divi IE.rk (IE.lit 3)) (IE.sub (IE.sub (IE.lit 1) (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 7)) (IE.lit 7)) (IE.lit 2))) (IE.divi IE.rk (IE.lit 3)))) (IE.sub (IE.lit 13) (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 7)) (IE.lit 7)) (IE.lit 2)))))) (IE.lit 1)) (IE.sub (IE.sub (IE.add (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 7)) (IE.lit 7)) (IE.lit 2)) (IE.sub (IE.add (IE.divi IE.rk (IE.lit 3)) (IE.sub (IE.sub (IE.lit 1) (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 7)) (IE.lit 7)) (IE.lit 2))) (IE.divi IE.rk (IE.lit 3)))) (IE.sub (IE.add (IE.divi IE.rk (IE.lit 3)) (IE.sub (IE.sub (IE.lit 1) (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 7)) (IE.lit 7)) (IE.lit 2))) (IE.divi IE.rk (IE.lit 3)))) (IE.sub (IE.lit 13) (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 7)) (IE.lit 7)) (IE.lit 2)))))) (IE.lit 1)) (IE.lit 12)))) (IE.lit 13)) (IE.sub (IE.sub (IE.add (IE.mul (IE.modi (IE.pid 0) (IE.lit 7)) (IE.lit 2)) (IE.sub (IE.add (IE.modi IE.rk (IE.lit 3)) (IE.sub (IE.sub (IE.lit 1) (IE.mul (IE.modi (IE.pid 0) (IE.lit 7)) (IE.lit 2))) (IE.modi IE.rk (IE.lit 3)))) (IE.sub (IE.add (IE.modi IE.rk (IE.lit 3)) (IE.sub (IE.sub (IE.lit 1) (IE.mul (IE.modi (IE.pid 0) (IE.lit 7)) (IE.lit 2))) (IE.modi IE.rk (IE.lit 3)))) (IE.sub (IE.lit 13) (IE.mul (IE.modi (IE.pid 0) (IE.lit 7)) (IE.lit 2)))))) (IE.lit 1)) (IE.sub (IE.sub (IE.add (IE.mul (IE.modi (IE.pid 0) (IE.lit 7)) (IE.lit 2)) (IE.sub (IE.add (IE.modi IE.rk (IE.lit 3)) (IE.sub (IE.sub (IE.lit 1) (IE.mul (IE.modi (IE.pid 0) (IE.lit 7)) (IE.lit 2))) (IE.modi IE.rk (IE.lit 3)))) (IE.sub (IE.add (IE.modi IE.rk (IE.lit 3)) (IE.sub (IE.sub (IE.lit 1) (IE.mul (IE.modi (IE.pid 0) (IE.lit 7)) (IE.lit 2))) (IE.modi IE.rk (IE.lit 3)))) (IE.sub (IE.lit 13) (IE.mul (IE.modi (IE.pid 0) (IE.lit 7)) (IE.lit 2)))))) (IE.lit 1)) (IE.lit 12)))))]
  , body := (SE.inp 0)
  , postOffs := IE.sparse []
  , post := (SE.inp 0)
  , nInp := 1, idxSlot := 1 }
def pool5_block : Nat := 8
def pool5_nkb : Nat := 2

theorem pool5_wf : pool5_g.Wf :=
  { offs_ok := IE.qkOnly_sparse _ (by decide)
  , post_ok := IE.qkOnly_sparse _ (by decide) }

/-- Correctness certificate for pool5. -/
theorem pool5_correct {α : Type} [ExactScalar α] :
    Implements (pool5_g.prog pool5_block pool5_nkb) (pool5_g.spec (α := α)) :=
  MaxRed.prog_implements pool5_g pool5_block pool5_nkb pool5_wf (by decide) (by decide) (by decide)

def pool5_kernel : ReduceKernel :=
  { name := "pool5", arity := 1, block := pool5_block
  , nkb := pool5_nkb, nout := 392
  , init := pool5_g.seed
  , step := pool5_g.step pool5_block
  , stored := pool5_g.stored pool5_block }

def main : IO Unit := do
  IO.FS.writeFile "../generated/pool0.py" pool0_kernel.render
  IO.FS.writeFile "../generated/pool1.py" pool1_kernel.render
  IO.FS.writeFile "../generated/pool2.py" pool2_kernel.render
  IO.FS.writeFile "../generated/pool3.py" pool3_kernel.render
  IO.FS.writeFile "../generated/pool4.py" pool4_kernel.render
  IO.FS.writeFile "../generated/pool5.py" pool5_kernel.render
