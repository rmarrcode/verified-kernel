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

-- t100: two-stage pipeline, 2 input(s), 4096-element intermediate at buffer 2
--   reduce over dim None of (16384, 32768) (inputs [(16384, 32768), (32768,)]): outer=1 K=536870912 inner=1; tree reduction: 536870912 elements -> 4096 partials
def t100_s1_g : GenRed :=
  { nout := 4096, K := 131072
  , offs := IE.sparse [(0, (IE.add (IE.mul (IE.divi (IE.add (IE.mul (IE.pid 0) (IE.lit 131072)) IE.rk) (IE.lit 32768)) (IE.lit 32768)) (IE.modi (IE.add (IE.mul (IE.pid 0) (IE.lit 131072)) IE.rk) (IE.lit 32768)))), (1, (IE.modi (IE.add (IE.mul (IE.pid 0) (IE.lit 131072)) IE.rk) (IE.lit 32768)))]
  , inRange := (BE.cmp .lt (IE.add (IE.mul (IE.pid 0) (IE.lit 131072)) IE.rk) (IE.lit 536870912))
  , body := (SE.bin .max (SE.bin .sub (SE.lit false 1 1) (SE.bin .mul (SE.inp 0) (SE.inp 1))) (SE.lit false 0 1))
  , postOffs := IE.sparse []
  , post := (SE.inp 0)
  , outGuard := BE.tt
  , nInp := 2, idxSlot := 1048576 }
def t100_s1_block : Nat := 1024
def t100_s1_nkb : Nat := 128

theorem t100_s1_wf : t100_s1_g.Wf :=
  { offs_ok := IE.qkOnly_sparse _ (by decide)
  , post_ok := IE.qkOnly_sparse _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

theorem t100_s1_impl {α : Type} [ExactScalar α] :
    Implements (t100_s1_g.prog t100_s1_block t100_s1_nkb) (t100_s1_g.spec (α := α)) :=
  GenRed.prog_implements t100_s1_g t100_s1_block t100_s1_nkb t100_s1_wf (by decide) (by decide)

def t100_s2_g : GenRed :=
  { nout := 1, K := 4096
  , offs := IE.sparse [(2, IE.rk)]
  , inRange := BE.tt
  , body := (SE.inp 2)
  , postOffs := IE.sparse []
  , post := (SE.bin .mul (SE.inp 0) (SE.lit false 1 536870912))
  , outGuard := BE.tt
  , nInp := 3, idxSlot := 1048576 }
def t100_s2_block : Nat := 1024
def t100_s2_nkb : Nat := 4

theorem t100_s2_wf : t100_s2_g.Wf :=
  { offs_ok := IE.qkOnly_sparse _ (by decide)
  , post_ok := IE.qkOnly_sparse _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

theorem t100_s2_impl {α : Type} [ExactScalar α] :
    Implements (t100_s2_g.prog t100_s2_block t100_s2_nkb) (t100_s2_g.spec (α := α)) :=
  GenRed.prog_implements t100_s2_g t100_s2_block t100_s2_nkb t100_s2_wf (by decide) (by decide)

/-- Stage 2 reads the intermediate only where stage 1 wrote it. -/
theorem t100_loc {α : Type} [ExactScalar α] :
    ∀ (bufs : Nat → Buf α) (u v : Buf α),
      (∀ i, i < (t100_s1_g.spec (α := α)).outSize → u i = v i) →
      ∀ q, q < (t100_s2_g.spec (α := α)).outSize →
        (t100_s2_g.spec (α := α)).out (subst bufs 2 u) q
          = (t100_s2_g.spec (α := α)).out (subst bufs 2 v) q :=
  GenRed.spec_locality t100_s2_g 2 4096
    (fun _ k _ hk => hk)
    (fun _ _ => (by decide : (0 : Nat) < 4096))

/-- Correctness certificate for t100: the composed pipeline. -/
theorem t100_correct {α : Type} [ExactScalar α] :
    ∀ (bufs : Nat → Buf α) (m1 m2 : Mem α) (q : Nat),
      q < (t100_s2_g.spec (α := α)).outSize →
      runTwo (t100_s1_g.prog t100_s1_block t100_s1_nkb)
             (t100_s2_g.prog t100_s2_block t100_s2_nkb) 2 bufs m1 m2 q
        = (t100_s2_g.spec (α := α)).out
            (subst bufs 2 (fun i => (t100_s1_g.spec (α := α)).out bufs i)) q :=
  two_stage t100_s1_impl t100_s2_impl t100_loc

def t100_s1_kernel : ReduceKernel :=
  { name := "t100_s1", arity := 2, block := t100_s1_block, nkb := t100_s1_nkb, nout := 4096, init := FE.zeroC, step := t100_s1_g.step t100_s1_block, stored := t100_s1_g.stored t100_s1_block }
def t100_s2_kernel : ReduceKernel :=
  { name := "t100_s2", arity := 3, block := t100_s2_block, nkb := t100_s2_nkb, nout := 1, init := FE.zeroC, step := t100_s2_g.step t100_s2_block, stored := t100_s2_g.stored t100_s2_block }
def t100_kernel : PipelineKernel :=
  { name := "t100", arity := 2, n1 := 4096, stage1 := t100_s1_kernel, stage2 := t100_s2_kernel }

def main : IO Unit := do
  IO.FS.writeFile "../generated/t100.py" t100_kernel.render
