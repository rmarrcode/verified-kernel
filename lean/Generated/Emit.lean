/-
  GENERATED FILE -- do not edit.

  Written by verified_kernel.vk.compile. Each task below carries a
  `theorem` instantiating its family's correctness theorem at the exact
  numbers the generator chose. `lake build` checking this file is what
  makes the corresponding kernel in generated/ a verified kernel.
-/
import VerifiedKernel

open VerifiedKernel

-- t086: two-stage pipeline, 3 input(s), 134217728-element intermediate at buffer 3
--   depthwise-separable conv: 8x64x512x512 -> 8x64x512x512 -> (8, 128, 512, 512)
def t086_s1_g : GenRed :=
  { nout := 134217728, K := 9
  , offs := fun b => ([(IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 16777216)) (IE.lit 64)) (IE.modi (IE.divi (IE.pid 0) (IE.lit 262144)) (IE.lit 64))) (IE.lit 512)) (IE.sub (IE.add (IE.modi (IE.divi (IE.pid 0) (IE.lit 512)) (IE.lit 512)) (IE.divi IE.rk (IE.lit 3))) (IE.lit 1))) (IE.lit 512)) (IE.sub (IE.add (IE.modi (IE.pid 0) (IE.lit 512)) (IE.modi IE.rk (IE.lit 3))) (IE.lit 1))), (IE.add (IE.mul (IE.add (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 262144)) (IE.lit 64)) (IE.lit 3)) (IE.divi IE.rk (IE.lit 3))) (IE.lit 3)) (IE.modi IE.rk (IE.lit 3))), (IE.lit 0), (IE.lit 0)]).getD b (IE.lit 0)
  , inRange := (BE.and (BE.and (BE.and (BE.cmp .le (IE.lit 1) (IE.add (IE.modi (IE.divi (IE.pid 0) (IE.lit 512)) (IE.lit 512)) (IE.divi IE.rk (IE.lit 3)))) (BE.cmp .lt (IE.add (IE.modi (IE.divi (IE.pid 0) (IE.lit 512)) (IE.lit 512)) (IE.divi IE.rk (IE.lit 3))) (IE.lit 513))) (BE.cmp .le (IE.lit 1) (IE.add (IE.modi (IE.pid 0) (IE.lit 512)) (IE.modi IE.rk (IE.lit 3))))) (BE.cmp .lt (IE.add (IE.modi (IE.pid 0) (IE.lit 512)) (IE.modi IE.rk (IE.lit 3))) (IE.lit 513)))
  , body := (SE.bin .mul (SE.inp 0) (SE.inp 1))
  , postOffs := fun b => ([(IE.lit 0), (IE.lit 0), (IE.lit 0), (IE.lit 0)]).getD b (IE.lit 0)
  , post := (SE.inp 0)
  , outGuard := BE.tt
  , nInp := 2 }
def t086_s1_block : Nat := 8
def t086_s1_nkb : Nat := 2

theorem t086_s1_wf : t086_s1_g.Wf :=
  { offs_ok := IE.qkOnly_getD _ (by decide)
  , post_ok := IE.qkOnly_getD _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

theorem t086_s1_impl {α : Type} [ExactScalar α] :
    Implements (t086_s1_g.prog t086_s1_block t086_s1_nkb) (t086_s1_g.spec (α := α)) :=
  GenRed.prog_implements t086_s1_g t086_s1_block t086_s1_nkb t086_s1_wf (by decide) (by decide)

def t086_s2_g : GenRed :=
  { nout := 268435456, K := 64
  , offs := fun b => ([(IE.lit 0), (IE.lit 0), (IE.add (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 262144)) (IE.lit 128)) (IE.lit 64)) IE.rk), (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 33554432)) (IE.lit 64)) IE.rk) (IE.lit 512)) (IE.modi (IE.divi (IE.pid 0) (IE.lit 512)) (IE.lit 512))) (IE.lit 512)) (IE.modi (IE.pid 0) (IE.lit 512)))]).getD b (IE.lit 0)
  , inRange := BE.tt
  , body := (SE.bin .mul (SE.inp 3) (SE.inp 2))
  , postOffs := fun b => ([(IE.lit 0), (IE.lit 0), (IE.lit 0), (IE.lit 0)]).getD b (IE.lit 0)
  , post := (SE.inp 0)
  , outGuard := BE.tt
  , nInp := 4 }
def t086_s2_block : Nat := 64
def t086_s2_nkb : Nat := 1

theorem t086_s2_wf : t086_s2_g.Wf :=
  { offs_ok := IE.qkOnly_getD _ (by decide)
  , post_ok := IE.qkOnly_getD _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

theorem t086_s2_impl {α : Type} [ExactScalar α] :
    Implements (t086_s2_g.prog t086_s2_block t086_s2_nkb) (t086_s2_g.spec (α := α)) :=
  GenRed.prog_implements t086_s2_g t086_s2_block t086_s2_nkb t086_s2_wf (by decide) (by decide)

/-- Stage 2 reads the intermediate only where stage 1 wrote it. -/
theorem t086_loc {α : Type} [ExactScalar α] :
    ∀ (bufs : Nat → Buf α) (u v : Buf α),
      (∀ i, i < (t086_s1_g.spec (α := α)).outSize → u i = v i) →
      ∀ q, q < (t086_s2_g.spec (α := α)).outSize →
        (t086_s2_g.spec (α := α)).out (subst bufs 3 u) q
          = (t086_s2_g.spec (α := α)).out (subst bufs 3 v) q :=
  GenRed.spec_locality t086_s2_g 3 134217728
    (fun q k hq hk => (bound_pack (A := 262144) (B := 512) (bound_pack (A := 512) (B := 512) (bound_pack (A := 8) (B := 64) (bound_div (a := 8) (d := 33554432) hq) hk) (bound_mod (c := 512) (by decide : (0 : Nat) < 512))) (bound_mod (c := 512) (by decide : (0 : Nat) < 512))))
    (fun _ _ => (by decide : (0 : Nat) < 134217728))

/-- Correctness certificate for t086: the composed pipeline. -/
theorem t086_correct {α : Type} [ExactScalar α] :
    ∀ (bufs : Nat → Buf α) (m1 m2 : Mem α) (q : Nat),
      q < (t086_s2_g.spec (α := α)).outSize →
      runTwo (t086_s1_g.prog t086_s1_block t086_s1_nkb)
             (t086_s2_g.prog t086_s2_block t086_s2_nkb) 3 bufs m1 m2 q
        = (t086_s2_g.spec (α := α)).out
            (subst bufs 3 (fun i => (t086_s1_g.spec (α := α)).out bufs i)) q :=
  two_stage t086_s1_impl t086_s2_impl t086_loc

def t086_s1_kernel : ReduceKernel :=
  { name := "t086_s1", arity := 2, block := t086_s1_block, nkb := t086_s1_nkb, nout := 134217728, init := FE.zeroC, step := t086_s1_g.step t086_s1_block, stored := t086_s1_g.stored t086_s1_block }
def t086_s2_kernel : ReduceKernel :=
  { name := "t086_s2", arity := 4, block := t086_s2_block, nkb := t086_s2_nkb, nout := 268435456, init := FE.zeroC, step := t086_s2_g.step t086_s2_block, stored := t086_s2_g.stored t086_s2_block }
def t086_kernel : PipelineKernel :=
  { name := "t086", arity := 3, n1 := 134217728, stage1 := t086_s1_kernel, stage2 := t086_s2_kernel }

def main : IO Unit := do
  IO.FS.writeFile "../generated/t086.py" t086_kernel.render
