/-
  GENERATED FILE -- do not edit.

  Written by verified_kernel.vk.compile. Each task below carries a
  `theorem` instantiating its family's correctness theorem at the exact
  numbers the generator chose. `lake build` checking this file is what
  makes the corresponding kernel in generated/ a verified kernel.
-/
import VerifiedKernel

open VerifiedKernel

-- t041: max reduction, 1 input(s), 201286656 outputs, extent 8
--   maxpool1d: N=16 C=192 k=(8,) stride=(1,) pad=(4,) dil=(3,); coordinates clamped rather than masked
def t041_g : MaxRed :=
  { nout := 201286656, K := 8
  , offs := fun b => ([(IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 12580416)) (IE.lit 192)) (IE.modi (IE.divi (IE.pid 0) (IE.lit 65523)) (IE.lit 192))) (IE.lit 65536)) (IE.sub (IE.add (IE.mul (IE.modi (IE.pid 0) (IE.lit 65523)) (IE.lit 1)) (IE.mul (IE.sub (IE.add IE.rk (IE.sub (IE.divi (IE.add (IE.sub (IE.lit 4) (IE.mul (IE.modi (IE.pid 0) (IE.lit 65523)) (IE.lit 1))) (IE.lit 2)) (IE.lit 3)) IE.rk)) (IE.sub (IE.add IE.rk (IE.sub (IE.divi (IE.add (IE.sub (IE.lit 4) (IE.mul (IE.modi (IE.pid 0) (IE.lit 65523)) (IE.lit 1))) (IE.lit 2)) (IE.lit 3)) IE.rk)) (IE.divi (IE.sub (IE.lit 65539) (IE.mul (IE.modi (IE.pid 0) (IE.lit 65523)) (IE.lit 1))) (IE.lit 3)))) (IE.lit 3))) (IE.lit 4)))]).getD b (IE.lit 0)
  , body := (SE.inp 0)
  , postOffs := fun b => ([(IE.lit 0)]).getD b (IE.lit 0)
  , post := (SE.inp 0)
  , nInp := 1 }
def t041_block : Nat := 8
def t041_nkb : Nat := 1

theorem t041_wf : t041_g.Wf :=
  { offs_ok := IE.qkOnly_getD _ (by decide)
  , post_ok := IE.qkOnly_getD _ (by decide) }

/-- Correctness certificate for t041. -/
theorem t041_correct {α : Type} [ExactScalar α] :
    Implements (t041_g.prog t041_block t041_nkb) (t041_g.spec (α := α)) :=
  MaxRed.prog_implements t041_g t041_block t041_nkb t041_wf (by decide) (by decide) (by decide)

def t041_kernel : ReduceKernel :=
  { name := "t041", arity := 1, block := t041_block
  , nkb := t041_nkb, nout := 201286656
  , init := t041_g.seed
  , step := t041_g.step t041_block
  , stored := t041_g.stored t041_block }

def main : IO Unit := do
  IO.FS.writeFile "../generated/t041.py" t041_kernel.render
