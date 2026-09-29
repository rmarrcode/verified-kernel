/-
  GENERATED FILE -- do not edit.

  Written by verified_kernel.vk.compile. Each task below carries a
  `theorem` instantiating its family's correctness theorem at the exact
  numbers the generator chose. `lake build` checking this file is what
  makes the corresponding kernel in generated/ a verified kernel.
-/
import VerifiedKernel

open VerifiedKernel

-- t012: reducing family, 2 inputs, 16777216 outputs, reduced extent 1
--   broadcast map: [(4096, 1), (4096, 4096)] -> (4096, 4096)
def t012_g : GenRed :=
  { nout := 16777216, K := 1
  , offs := fun b => ([(IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 4096)) (IE.lit 1)) (IE.lit 0)), (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 4096)) (IE.lit 4096)) (IE.modi (IE.pid 0) (IE.lit 4096)))]).getD b (IE.lit 0)
  , inRange := BE.tt
  , body := (SE.bin .mul (SE.inp 0) (SE.inp 1))
  , postOffs := fun b => ([(IE.lit 0), (IE.lit 0)]).getD b (IE.lit 0)
  , post := (SE.inp 0)
  , outGuard := BE.tt
  , nInp := 2 }
def t012_block : Nat := 1
def t012_nkb : Nat := 1

/-- Index maps mention only the output and reduction indices. -/
theorem t012_wf : t012_g.Wf :=
  { offs_ok := IE.qkOnly_getD _ (by decide)
  , post_ok := IE.qkOnly_getD _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

/-- Correctness certificate for t012. -/
theorem t012_correct {α : Type} [ExactScalar α] :
    Implements (t012_g.prog t012_block t012_nkb) (t012_g.spec (α := α)) :=
  GenRed.prog_implements t012_g t012_block t012_nkb t012_wf (by decide) (by decide)

def t012_kernel : ReduceKernel :=
  { name := "t012", arity := 2, block := t012_block
  , nkb := t012_nkb, nout := 16777216
  , step := t012_g.step t012_block
  , stored := t012_g.stored t012_block }

-- t100: reducing family, 2 inputs, 1 outputs, reduced extent 1073741824
--   reduce over dim None of (32768, 32768) (inputs [(32768, 32768), (32768,)]): outer=1 K=1073741824 inner=1
def t100_g : GenRed :=
  { nout := 1, K := 1073741824
  , offs := fun b => ([(IE.add (IE.mul (IE.divi IE.rk (IE.lit 32768)) (IE.lit 32768)) (IE.modi IE.rk (IE.lit 32768))), (IE.modi IE.rk (IE.lit 32768))]).getD b (IE.lit 0)
  , inRange := BE.tt
  , body := (SE.bin .max (SE.bin .sub (SE.lit false 1 1) (SE.bin .mul (SE.inp 0) (SE.inp 1))) (SE.lit false 0 1))
  , postOffs := fun b => ([(IE.lit 0), (IE.lit 0)]).getD b (IE.lit 0)
  , post := (SE.bin .mul (SE.inp 0) (SE.lit false 1 1073741824))
  , outGuard := BE.tt
  , nInp := 2 }
def t100_block : Nat := 1024
def t100_nkb : Nat := 1048576

/-- Index maps mention only the output and reduction indices. -/
theorem t100_wf : t100_g.Wf :=
  { offs_ok := IE.qkOnly_getD _ (by decide)
  , post_ok := IE.qkOnly_getD _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

/-- Correctness certificate for t100. -/
theorem t100_correct {α : Type} [ExactScalar α] :
    Implements (t100_g.prog t100_block t100_nkb) (t100_g.spec (α := α)) :=
  GenRed.prog_implements t100_g t100_block t100_nkb t100_wf (by decide) (by decide)

def t100_kernel : ReduceKernel :=
  { name := "t100", arity := 2, block := t100_block
  , nkb := t100_nkb, nout := 1
  , step := t100_g.step t100_block
  , stored := t100_g.stored t100_block }

def main : IO Unit := do
  IO.FS.writeFile "../generated/t012.py" t012_kernel.render
  IO.FS.writeFile "../generated/t100.py" t100_kernel.render
