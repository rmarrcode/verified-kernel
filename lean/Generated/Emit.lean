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

-- iso0: reducing family, 2 inputs, 16 outputs, reduced extent 9
--   conv2d: N=2 Cin=8 Cout=8 groups=8 k=(3, 3) stride=(2, 2) pad=(1, 1) dil=(1, 1) K=9
def iso0_g : GenRed :=
  { nout := 16, K := 9
  , offs := IE.sparse [(0, (IE.add (IE.add (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 8)) (IE.lit 8)) (IE.modi (IE.pid 0) (IE.lit 8))) (IE.sub (IE.modi (IE.divi IE.rk (IE.lit 3)) (IE.lit 3)) (IE.lit 1))) (IE.sub (IE.modi IE.rk (IE.lit 3)) (IE.lit 1)))), (1, (IE.add (IE.mul (IE.add (IE.mul (IE.modi (IE.pid 0) (IE.lit 8)) (IE.lit 3)) (IE.modi (IE.divi IE.rk (IE.lit 3)) (IE.lit 3))) (IE.lit 3)) (IE.modi IE.rk (IE.lit 3))))]
  , inRange := (BE.and (BE.and (BE.and (BE.cmp .le (IE.lit 1) (IE.modi (IE.divi IE.rk (IE.lit 3)) (IE.lit 3))) (BE.cmp .lt (IE.modi (IE.divi IE.rk (IE.lit 3)) (IE.lit 3)) (IE.lit 2))) (BE.cmp .le (IE.lit 1) (IE.modi IE.rk (IE.lit 3)))) (BE.cmp .lt (IE.modi IE.rk (IE.lit 3)) (IE.lit 2)))
  , body := (SE.bin .mul (SE.inp 0) (SE.inp 1))
  , postOffs := IE.sparse []
  , post := (SE.inp 0)
  , outGuard := BE.tt
  , nInp := 2, idxSlot := 1048576 }
def iso0_block : Nat := 8
def iso0_nkb : Nat := 2

/-- Index maps mention only the output and reduction indices. -/
theorem iso0_wf : iso0_g.Wf :=
  { offs_ok := IE.qkOnly_sparse _ (by decide)
  , post_ok := IE.qkOnly_sparse _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

/-- Correctness certificate for iso0. -/
theorem iso0_correct {α : Type} [ExactScalar α] :
    Implements (iso0_g.prog iso0_block iso0_nkb) (iso0_g.spec (α := α)) :=
  GenRed.prog_implements iso0_g iso0_block iso0_nkb iso0_wf (by decide) (by decide)

def iso0_kernel : ReduceKernel :=
  { name := "iso0", arity := 2, block := iso0_block
  , nkb := iso0_nkb, nout := 16
  , init := FE.zeroC
  , step := iso0_g.step iso0_block
  , stored := iso0_g.stored iso0_block }

-- iso1: reducing family, 2 inputs, 16 outputs, reduced extent 9
--   conv2d: N=2 Cin=8 Cout=8 groups=8 k=(3, 3) stride=(1, 1) pad=(1, 1) dil=(1, 1) K=9
def iso1_g : GenRed :=
  { nout := 16, K := 9
  , offs := IE.sparse [(0, (IE.add (IE.add (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 8)) (IE.lit 8)) (IE.modi (IE.pid 0) (IE.lit 8))) (IE.sub (IE.modi (IE.divi IE.rk (IE.lit 3)) (IE.lit 3)) (IE.lit 1))) (IE.sub (IE.modi IE.rk (IE.lit 3)) (IE.lit 1)))), (1, (IE.add (IE.mul (IE.add (IE.mul (IE.modi (IE.pid 0) (IE.lit 8)) (IE.lit 3)) (IE.modi (IE.divi IE.rk (IE.lit 3)) (IE.lit 3))) (IE.lit 3)) (IE.modi IE.rk (IE.lit 3))))]
  , inRange := (BE.and (BE.and (BE.and (BE.cmp .le (IE.lit 1) (IE.modi (IE.divi IE.rk (IE.lit 3)) (IE.lit 3))) (BE.cmp .lt (IE.modi (IE.divi IE.rk (IE.lit 3)) (IE.lit 3)) (IE.lit 2))) (BE.cmp .le (IE.lit 1) (IE.modi IE.rk (IE.lit 3)))) (BE.cmp .lt (IE.modi IE.rk (IE.lit 3)) (IE.lit 2)))
  , body := (SE.bin .mul (SE.inp 0) (SE.inp 1))
  , postOffs := IE.sparse []
  , post := (SE.inp 0)
  , outGuard := BE.tt
  , nInp := 2, idxSlot := 1048576 }
def iso1_block : Nat := 8
def iso1_nkb : Nat := 2

/-- Index maps mention only the output and reduction indices. -/
theorem iso1_wf : iso1_g.Wf :=
  { offs_ok := IE.qkOnly_sparse _ (by decide)
  , post_ok := IE.qkOnly_sparse _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

/-- Correctness certificate for iso1. -/
theorem iso1_correct {α : Type} [ExactScalar α] :
    Implements (iso1_g.prog iso1_block iso1_nkb) (iso1_g.spec (α := α)) :=
  GenRed.prog_implements iso1_g iso1_block iso1_nkb iso1_wf (by decide) (by decide)

def iso1_kernel : ReduceKernel :=
  { name := "iso1", arity := 2, block := iso1_block
  , nkb := iso1_nkb, nout := 16
  , init := FE.zeroC
  , step := iso1_g.step iso1_block
  , stored := iso1_g.stored iso1_block }

-- iso2: reducing family, 2 inputs, 16 outputs, reduced extent 9
--   conv2d: N=2 Cin=8 Cout=8 groups=8 k=(3, 3) stride=(2, 2) pad=(1, 1) dil=(1, 1) K=9
def iso2_g : GenRed :=
  { nout := 16, K := 9
  , offs := IE.sparse [(0, (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 8)) (IE.lit 8)) (IE.modi (IE.pid 0) (IE.lit 8))) (IE.lit 2)) (IE.sub (IE.modi (IE.divi IE.rk (IE.lit 3)) (IE.lit 3)) (IE.lit 1))) (IE.lit 2)) (IE.sub (IE.modi IE.rk (IE.lit 3)) (IE.lit 1)))), (1, (IE.add (IE.mul (IE.add (IE.mul (IE.modi (IE.pid 0) (IE.lit 8)) (IE.lit 3)) (IE.modi (IE.divi IE.rk (IE.lit 3)) (IE.lit 3))) (IE.lit 3)) (IE.modi IE.rk (IE.lit 3))))]
  , inRange := (BE.and (BE.and (BE.and (BE.cmp .le (IE.lit 1) (IE.modi (IE.divi IE.rk (IE.lit 3)) (IE.lit 3))) (BE.cmp .lt (IE.modi (IE.divi IE.rk (IE.lit 3)) (IE.lit 3)) (IE.lit 3))) (BE.cmp .le (IE.lit 1) (IE.modi IE.rk (IE.lit 3)))) (BE.cmp .lt (IE.modi IE.rk (IE.lit 3)) (IE.lit 3)))
  , body := (SE.bin .mul (SE.inp 0) (SE.inp 1))
  , postOffs := IE.sparse []
  , post := (SE.inp 0)
  , outGuard := BE.tt
  , nInp := 2, idxSlot := 1048576 }
def iso2_block : Nat := 8
def iso2_nkb : Nat := 2

/-- Index maps mention only the output and reduction indices. -/
theorem iso2_wf : iso2_g.Wf :=
  { offs_ok := IE.qkOnly_sparse _ (by decide)
  , post_ok := IE.qkOnly_sparse _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

/-- Correctness certificate for iso2. -/
theorem iso2_correct {α : Type} [ExactScalar α] :
    Implements (iso2_g.prog iso2_block iso2_nkb) (iso2_g.spec (α := α)) :=
  GenRed.prog_implements iso2_g iso2_block iso2_nkb iso2_wf (by decide) (by decide)

def iso2_kernel : ReduceKernel :=
  { name := "iso2", arity := 2, block := iso2_block
  , nkb := iso2_nkb, nout := 16
  , init := FE.zeroC
  , step := iso2_g.step iso2_block
  , stored := iso2_g.stored iso2_block }

-- iso3: reducing family, 2 inputs, 32 outputs, reduced extent 72
--   conv2d: N=2 Cin=8 Cout=16 groups=1 k=(3, 3) stride=(1, 1) pad=(1, 1) dil=(1, 1) K=72
def iso3_g : GenRed :=
  { nout := 32, K := 72
  , offs := IE.sparse [(0, (IE.add (IE.add (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 16)) (IE.lit 8)) (IE.divi IE.rk (IE.lit 9))) (IE.sub (IE.modi (IE.divi IE.rk (IE.lit 3)) (IE.lit 3)) (IE.lit 1))) (IE.sub (IE.modi IE.rk (IE.lit 3)) (IE.lit 1)))), (1, (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.modi (IE.pid 0) (IE.lit 16)) (IE.lit 8)) (IE.divi IE.rk (IE.lit 9))) (IE.lit 3)) (IE.modi (IE.divi IE.rk (IE.lit 3)) (IE.lit 3))) (IE.lit 3)) (IE.modi IE.rk (IE.lit 3))))]
  , inRange := (BE.and (BE.and (BE.and (BE.cmp .le (IE.lit 1) (IE.modi (IE.divi IE.rk (IE.lit 3)) (IE.lit 3))) (BE.cmp .lt (IE.modi (IE.divi IE.rk (IE.lit 3)) (IE.lit 3)) (IE.lit 2))) (BE.cmp .le (IE.lit 1) (IE.modi IE.rk (IE.lit 3)))) (BE.cmp .lt (IE.modi IE.rk (IE.lit 3)) (IE.lit 2)))
  , body := (SE.bin .mul (SE.inp 0) (SE.inp 1))
  , postOffs := IE.sparse []
  , post := (SE.inp 0)
  , outGuard := BE.tt
  , nInp := 2, idxSlot := 1048576 }
def iso3_block : Nat := 64
def iso3_nkb : Nat := 2

/-- Index maps mention only the output and reduction indices. -/
theorem iso3_wf : iso3_g.Wf :=
  { offs_ok := IE.qkOnly_sparse _ (by decide)
  , post_ok := IE.qkOnly_sparse _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

/-- Correctness certificate for iso3. -/
theorem iso3_correct {α : Type} [ExactScalar α] :
    Implements (iso3_g.prog iso3_block iso3_nkb) (iso3_g.spec (α := α)) :=
  GenRed.prog_implements iso3_g iso3_block iso3_nkb iso3_wf (by decide) (by decide)

def iso3_kernel : ReduceKernel :=
  { name := "iso3", arity := 2, block := iso3_block
  , nkb := iso3_nkb, nout := 32
  , init := FE.zeroC
  , step := iso3_g.step iso3_block
  , stored := iso3_g.stored iso3_block }

-- iso4: reducing family, 2 inputs, 192 outputs, reduced extent 24
--   conv2d: N=2 Cin=24 Cout=96 groups=1 k=(1, 1) stride=(1, 1) pad=(0, 0) dil=(1, 1) K=24
def iso4_g : GenRed :=
  { nout := 192, K := 24
  , offs := IE.sparse [(0, (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 96)) (IE.lit 24)) IE.rk)), (1, (IE.add (IE.mul (IE.modi (IE.pid 0) (IE.lit 96)) (IE.lit 24)) IE.rk))]
  , inRange := (BE.and (BE.cmp .lt (IE.lit 0) (IE.lit 1)) (BE.cmp .lt (IE.lit 0) (IE.lit 1)))
  , body := (SE.bin .mul (SE.inp 0) (SE.inp 1))
  , postOffs := IE.sparse []
  , post := (SE.inp 0)
  , outGuard := BE.tt
  , nInp := 2, idxSlot := 1048576 }
def iso4_block : Nat := 16
def iso4_nkb : Nat := 2

/-- Index maps mention only the output and reduction indices. -/
theorem iso4_wf : iso4_g.Wf :=
  { offs_ok := IE.qkOnly_sparse _ (by decide)
  , post_ok := IE.qkOnly_sparse _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

/-- Correctness certificate for iso4. -/
theorem iso4_correct {α : Type} [ExactScalar α] :
    Implements (iso4_g.prog iso4_block iso4_nkb) (iso4_g.spec (α := α)) :=
  GenRed.prog_implements iso4_g iso4_block iso4_nkb iso4_wf (by decide) (by decide)

def iso4_kernel : ReduceKernel :=
  { name := "iso4", arity := 2, block := iso4_block
  , nkb := iso4_nkb, nout := 192
  , init := FE.zeroC
  , step := iso4_g.step iso4_block
  , stored := iso4_g.stored iso4_block }

-- iso5: reducing family, 2 inputs, 48 outputs, reduced extent 96
--   conv2d: N=2 Cin=96 Cout=24 groups=1 k=(1, 1) stride=(1, 1) pad=(0, 0) dil=(1, 1) K=96
def iso5_g : GenRed :=
  { nout := 48, K := 96
  , offs := IE.sparse [(0, (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 24)) (IE.lit 96)) IE.rk)), (1, (IE.add (IE.mul (IE.modi (IE.pid 0) (IE.lit 24)) (IE.lit 96)) IE.rk))]
  , inRange := (BE.and (BE.cmp .lt (IE.lit 0) (IE.lit 1)) (BE.cmp .lt (IE.lit 0) (IE.lit 1)))
  , body := (SE.bin .mul (SE.inp 0) (SE.inp 1))
  , postOffs := IE.sparse []
  , post := (SE.inp 0)
  , outGuard := BE.tt
  , nInp := 2, idxSlot := 1048576 }
def iso5_block : Nat := 64
def iso5_nkb : Nat := 2

/-- Index maps mention only the output and reduction indices. -/
theorem iso5_wf : iso5_g.Wf :=
  { offs_ok := IE.qkOnly_sparse _ (by decide)
  , post_ok := IE.qkOnly_sparse _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

/-- Correctness certificate for iso5. -/
theorem iso5_correct {α : Type} [ExactScalar α] :
    Implements (iso5_g.prog iso5_block iso5_nkb) (iso5_g.spec (α := α)) :=
  GenRed.prog_implements iso5_g iso5_block iso5_nkb iso5_wf (by decide) (by decide)

def iso5_kernel : ReduceKernel :=
  { name := "iso5", arity := 2, block := iso5_block
  , nkb := iso5_nkb, nout := 48
  , init := FE.zeroC
  , step := iso5_g.step iso5_block
  , stored := iso5_g.stored iso5_block }

-- iso6: reducing family, 2 inputs, 3072 outputs, reduced extent 24
--   conv2d: N=2 Cin=24 Cout=96 groups=1 k=(1, 1) stride=(1, 1) pad=(0, 0) dil=(1, 1) K=24
def iso6_g : GenRed :=
  { nout := 3072, K := 24
  , offs := IE.sparse [(0, (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 1536)) (IE.lit 24)) IE.rk) (IE.lit 4)) (IE.modi (IE.divi (IE.pid 0) (IE.lit 4)) (IE.lit 4))) (IE.lit 4)) (IE.modi (IE.pid 0) (IE.lit 4)))), (1, (IE.add (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 16)) (IE.lit 96)) (IE.lit 24)) IE.rk))]
  , inRange := (BE.and (BE.cmp .lt (IE.modi (IE.divi (IE.pid 0) (IE.lit 4)) (IE.lit 4)) (IE.lit 4)) (BE.cmp .lt (IE.modi (IE.pid 0) (IE.lit 4)) (IE.lit 4)))
  , body := (SE.bin .mul (SE.inp 0) (SE.inp 1))
  , postOffs := IE.sparse []
  , post := (SE.inp 0)
  , outGuard := BE.tt
  , nInp := 2, idxSlot := 1048576 }
def iso6_block : Nat := 16
def iso6_nkb : Nat := 2

/-- Index maps mention only the output and reduction indices. -/
theorem iso6_wf : iso6_g.Wf :=
  { offs_ok := IE.qkOnly_sparse _ (by decide)
  , post_ok := IE.qkOnly_sparse _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

/-- Correctness certificate for iso6. -/
theorem iso6_correct {α : Type} [ExactScalar α] :
    Implements (iso6_g.prog iso6_block iso6_nkb) (iso6_g.spec (α := α)) :=
  GenRed.prog_implements iso6_g iso6_block iso6_nkb iso6_wf (by decide) (by decide)

def iso6_kernel : ReduceKernel :=
  { name := "iso6", arity := 2, block := iso6_block
  , nkb := iso6_nkb, nout := 3072
  , init := FE.zeroC
  , step := iso6_g.step iso6_block
  , stored := iso6_g.stored iso6_block }

-- iso7: reducing family, 2 inputs, 64 outputs, reduced extent 8
--   conv2d: N=2 Cin=8 Cout=32 groups=1 k=(1, 1) stride=(1, 1) pad=(0, 0) dil=(1, 1) K=8
def iso7_g : GenRed :=
  { nout := 64, K := 8
  , offs := IE.sparse [(0, (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 32)) (IE.lit 8)) IE.rk)), (1, (IE.add (IE.mul (IE.modi (IE.pid 0) (IE.lit 32)) (IE.lit 8)) IE.rk))]
  , inRange := (BE.and (BE.cmp .lt (IE.lit 0) (IE.lit 1)) (BE.cmp .lt (IE.lit 0) (IE.lit 1)))
  , body := (SE.bin .mul (SE.inp 0) (SE.inp 1))
  , postOffs := IE.sparse []
  , post := (SE.inp 0)
  , outGuard := BE.tt
  , nInp := 2, idxSlot := 1048576 }
def iso7_block : Nat := 8
def iso7_nkb : Nat := 1

/-- Index maps mention only the output and reduction indices. -/
theorem iso7_wf : iso7_g.Wf :=
  { offs_ok := IE.qkOnly_sparse _ (by decide)
  , post_ok := IE.qkOnly_sparse _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

/-- Correctness certificate for iso7. -/
theorem iso7_correct {α : Type} [ExactScalar α] :
    Implements (iso7_g.prog iso7_block iso7_nkb) (iso7_g.spec (α := α)) :=
  GenRed.prog_implements iso7_g iso7_block iso7_nkb iso7_wf (by decide) (by decide)

def iso7_kernel : ReduceKernel :=
  { name := "iso7", arity := 2, block := iso7_block
  , nkb := iso7_nkb, nout := 64
  , init := FE.zeroC
  , step := iso7_g.step iso7_block
  , stored := iso7_g.stored iso7_block }

def main : IO Unit := do
  IO.FS.writeFile "../generated/iso0.py" iso0_kernel.render
  IO.FS.writeFile "../generated/iso1.py" iso1_kernel.render
  IO.FS.writeFile "../generated/iso2.py" iso2_kernel.render
  IO.FS.writeFile "../generated/iso3.py" iso3_kernel.render
  IO.FS.writeFile "../generated/iso4.py" iso4_kernel.render
  IO.FS.writeFile "../generated/iso5.py" iso5_kernel.render
  IO.FS.writeFile "../generated/iso6.py" iso6_kernel.render
  IO.FS.writeFile "../generated/iso7.py" iso7_kernel.render
