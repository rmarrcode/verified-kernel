/-
  GENERATED FILE -- do not edit.

  Written by verified_kernel.vk.compile. Each task below carries a
  `theorem` instantiating its family's correctness theorem at the exact
  numbers the generator chose. `lake build` checking this file is what
  makes the corresponding kernel in generated/ a verified kernel.
-/
import VerifiedKernel

open VerifiedKernel

-- t010: a chain of 3 stage(s), 3 input buffer(s)
--   fused hardtanh into stage 1; fused <built-in method tanh of type object at 0x77f82f4a5640> into stage 2
def t010_sz : Sizes
  | 3 => some 536870912
  | 4 => some 134217728
  | 5 => some 8192
  | _ => none

def t010_s0_g : GenRed :=
  { nout := 536870912, K := 576
  , offs := fun b => ([(IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 4194304)) (IE.lit 64)) (IE.add (IE.mul (IE.divi (IE.modi (IE.divi (IE.pid 0) (IE.lit 65536)) (IE.lit 64)) (IE.lit 64)) (IE.lit 64)) (IE.divi IE.rk (IE.lit 9)))) (IE.lit 256)) (IE.sub (IE.add (IE.modi (IE.divi (IE.pid 0) (IE.lit 256)) (IE.lit 256)) (IE.lit 1)) (IE.modi (IE.divi IE.rk (IE.lit 3)) (IE.lit 3)))) (IE.lit 256)) (IE.sub (IE.add (IE.modi (IE.pid 0) (IE.lit 256)) (IE.lit 1)) (IE.modi IE.rk (IE.lit 3)))), (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.modi (IE.divi (IE.pid 0) (IE.lit 65536)) (IE.lit 64)) (IE.lit 64)) (IE.lit 64)) (IE.divi IE.rk (IE.lit 9))) (IE.lit 64)) (IE.modi (IE.modi (IE.divi (IE.pid 0) (IE.lit 65536)) (IE.lit 64)) (IE.lit 64))) (IE.lit 3)) (IE.modi (IE.divi IE.rk (IE.lit 3)) (IE.lit 3))) (IE.lit 3)) (IE.modi IE.rk (IE.lit 3))), (IE.lit 0), (IE.lit 0)]).getD b (IE.lit 0)
  , inRange := (BE.and (BE.and (BE.and (BE.and (BE.and (BE.cmp .le (IE.modi (IE.divi IE.rk (IE.lit 3)) (IE.lit 3)) (IE.add (IE.modi (IE.divi (IE.pid 0) (IE.lit 256)) (IE.lit 256)) (IE.lit 1))) (BE.cmp .eq (IE.lit 0) (IE.lit 0))) (BE.cmp .lt (IE.sub (IE.add (IE.modi (IE.divi (IE.pid 0) (IE.lit 256)) (IE.lit 256)) (IE.lit 1)) (IE.modi (IE.divi IE.rk (IE.lit 3)) (IE.lit 3))) (IE.lit 256))) (BE.cmp .le (IE.modi IE.rk (IE.lit 3)) (IE.add (IE.modi (IE.pid 0) (IE.lit 256)) (IE.lit 1)))) (BE.cmp .eq (IE.lit 0) (IE.lit 0))) (BE.cmp .lt (IE.sub (IE.add (IE.modi (IE.pid 0) (IE.lit 256)) (IE.lit 1)) (IE.modi IE.rk (IE.lit 3))) (IE.lit 256)))
  , body := (SE.bin .mul (SE.inp 0) (SE.inp 1))
  , postOffs := fun b => ([(IE.lit 0), (IE.lit 0), (IE.modi (IE.divi (IE.pid 0) (IE.lit 65536)) (IE.lit 64)), (IE.lit 0)]).getD b (IE.lit 0)
  , post := (SE.bin .add (SE.inp 0) (SE.inp 3))
  , outGuard := BE.tt
  , nInp := 4, idxSlot := 1048576 }
def t010_s0_block : Nat := 512
def t010_s0_nkb : Nat := 2

theorem t010_s0_wf : t010_s0_g.Wf :=
  { offs_ok := IE.qkOnly_getD _ (by decide)
  , post_ok := IE.qkOnly_getD _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

theorem t010_s0_impl {α : Type} [ExactScalar α] :
    Implements (t010_s0_g.prog t010_s0_block t010_s0_nkb) (t010_s0_g.spec (α := α)) :=
  GenRed.prog_implements t010_s0_g t010_s0_block t010_s0_nkb t010_s0_wf (by decide) (by decide)

def t010_s1_g : MaxRed :=
  { nout := 134217728, K := 4
  , offs := fun b => ([(IE.lit 0), (IE.lit 0), (IE.lit 0), (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 1048576)) (IE.lit 64)) (IE.modi (IE.divi (IE.pid 0) (IE.lit 16384)) (IE.lit 64))) (IE.lit 256)) (IE.sub (IE.add (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 128)) (IE.lit 128)) (IE.lit 2)) (IE.sub (IE.add (IE.divi IE.rk (IE.lit 2)) (IE.sub (IE.sub (IE.lit 0) (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 128)) (IE.lit 128)) (IE.lit 2))) (IE.divi IE.rk (IE.lit 2)))) (IE.sub (IE.add (IE.divi IE.rk (IE.lit 2)) (IE.sub (IE.sub (IE.lit 0) (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 128)) (IE.lit 128)) (IE.lit 2))) (IE.divi IE.rk (IE.lit 2)))) (IE.sub (IE.lit 255) (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 128)) (IE.lit 128)) (IE.lit 2)))))) (IE.sub (IE.add (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 128)) (IE.lit 128)) (IE.lit 2)) (IE.sub (IE.add (IE.divi IE.rk (IE.lit 2)) (IE.sub (IE.sub (IE.lit 0) (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 128)) (IE.lit 128)) (IE.lit 2))) (IE.divi IE.rk (IE.lit 2)))) (IE.sub (IE.add (IE.divi IE.rk (IE.lit 2)) (IE.sub (IE.sub (IE.lit 0) (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 128)) (IE.lit 128)) (IE.lit 2))) (IE.divi IE.rk (IE.lit 2)))) (IE.sub (IE.lit 255) (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 128)) (IE.lit 128)) (IE.lit 2)))))) (IE.lit 255)))) (IE.lit 256)) (IE.sub (IE.add (IE.mul (IE.modi (IE.pid 0) (IE.lit 128)) (IE.lit 2)) (IE.sub (IE.add (IE.modi IE.rk (IE.lit 2)) (IE.sub (IE.sub (IE.lit 0) (IE.mul (IE.modi (IE.pid 0) (IE.lit 128)) (IE.lit 2))) (IE.modi IE.rk (IE.lit 2)))) (IE.sub (IE.add (IE.modi IE.rk (IE.lit 2)) (IE.sub (IE.sub (IE.lit 0) (IE.mul (IE.modi (IE.pid 0) (IE.lit 128)) (IE.lit 2))) (IE.modi IE.rk (IE.lit 2)))) (IE.sub (IE.lit 255) (IE.mul (IE.modi (IE.pid 0) (IE.lit 128)) (IE.lit 2)))))) (IE.sub (IE.add (IE.mul (IE.modi (IE.pid 0) (IE.lit 128)) (IE.lit 2)) (IE.sub (IE.add (IE.modi IE.rk (IE.lit 2)) (IE.sub (IE.sub (IE.lit 0) (IE.mul (IE.modi (IE.pid 0) (IE.lit 128)) (IE.lit 2))) (IE.modi IE.rk (IE.lit 2)))) (IE.sub (IE.add (IE.modi IE.rk (IE.lit 2)) (IE.sub (IE.sub (IE.lit 0) (IE.mul (IE.modi (IE.pid 0) (IE.lit 128)) (IE.lit 2))) (IE.modi IE.rk (IE.lit 2)))) (IE.sub (IE.lit 255) (IE.mul (IE.modi (IE.pid 0) (IE.lit 128)) (IE.lit 2)))))) (IE.lit 255)))), (IE.lit 0)]).getD b (IE.lit 0)
  , body := (SE.inp 3)
  , postOffs := fun b => ([(IE.lit 0), (IE.lit 0), (IE.lit 0), (IE.lit 0), (IE.lit 0)]).getD b (IE.lit 0)
  , post := (SE.bin .min (SE.bin .max (SE.inp 0) (SE.lit true 1 1)) (SE.lit false 1 1))
  , nInp := 5, idxSlot := 1048576 }
def t010_s1_block : Nat := 4
def t010_s1_nkb : Nat := 1

theorem t010_s1_wf : t010_s1_g.Wf :=
  { offs_ok := IE.qkOnly_getD _ (by decide)
  , post_ok := IE.qkOnly_getD _ (by decide) }

theorem t010_s1_impl {α : Type} [ExactScalar α] :
    Implements (t010_s1_g.prog t010_s1_block t010_s1_nkb) (t010_s1_g.spec (α := α)) :=
  MaxRed.prog_implements t010_s1_g t010_s1_block t010_s1_nkb t010_s1_wf (by decide) (by decide) (by decide)


def t010_s2_g : GenRed :=
  { nout := 8192, K := 16384
  , offs := fun b => ([(IE.lit 0), (IE.lit 0), (IE.lit 0), (IE.lit 0), (IE.add (IE.mul (IE.pid 0) (IE.lit 16384)) IE.rk), (IE.lit 0)]).getD b (IE.lit 0)
  , inRange := BE.tt
  , body := (SE.inp 4)
  , postOffs := fun b => ([(IE.lit 0), (IE.lit 0), (IE.lit 0), (IE.lit 0), (IE.lit 0), (IE.lit 0)]).getD b (IE.lit 0)
  , post := (SE.un .tanh (SE.bin .mul (SE.inp 0) (SE.lit false 1 16384)))
  , outGuard := BE.tt
  , nInp := 6, idxSlot := 1048576 }
def t010_s2_block : Nat := 1024
def t010_s2_nkb : Nat := 16

theorem t010_s2_wf : t010_s2_g.Wf :=
  { offs_ok := IE.qkOnly_getD _ (by decide)
  , post_ok := IE.qkOnly_getD _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

theorem t010_s2_impl {α : Type} [ExactScalar α] :
    Implements (t010_s2_g.prog t010_s2_block t010_s2_nkb) (t010_s2_g.spec (α := α)) :=
  GenRed.prog_implements t010_s2_g t010_s2_block t010_s2_nkb t010_s2_wf (by decide) (by decide)

/-- Stage 0 reads no intermediate past what was written there. -/
theorem t010_s0_loc {α : Type} [ExactScalar α] :
    SpecLocal t010_sz (t010_s0_g.spec (α := α)) :=
  GenRed.specLocal t010_s0_g t010_sz
    (fun b nn hn q kk hq hk => by
      match b, hn with
      | 0, hn => simp [t010_sz] at hn
      | 1, hn => simp [t010_sz] at hn
      | 2, hn => simp [t010_sz] at hn
      | 3, hn => simp [t010_sz] at hn; subst hn; exact (by decide : (0 : Nat) < 536870912)
      | 4, hn => simp [t010_sz] at hn; subst hn; exact (by decide : (0 : Nat) < 134217728)
      | 5, hn => simp [t010_sz] at hn; subst hn; exact (by decide : (0 : Nat) < 8192)
      | (_ + 6), hn => simp [t010_sz] at hn)
    (fun b nn hn q hq => by
      match b, hn with
      | 0, hn => simp [t010_sz] at hn
      | 1, hn => simp [t010_sz] at hn
      | 2, hn => simp [t010_sz] at hn
      | 3, hn => simp [t010_sz] at hn; subst hn; exact (by decide : (0 : Nat) < 536870912)
      | 4, hn => simp [t010_sz] at hn; subst hn; exact (by decide : (0 : Nat) < 134217728)
      | 5, hn => simp [t010_sz] at hn; subst hn; exact (by decide : (0 : Nat) < 8192)
      | (_ + 6), hn => simp [t010_sz] at hn)

/-- Stage 1 reads no intermediate past what was written there. -/
theorem t010_s1_loc {α : Type} [ExactScalar α] :
    SpecLocal t010_sz (t010_s1_g.spec (α := α)) :=
  MaxRed.specLocal t010_s1_g t010_sz (by decide)
    (fun b nn hn q kk hq hk => by
      match b, hn with
      | 0, hn => simp [t010_sz] at hn
      | 1, hn => simp [t010_sz] at hn
      | 2, hn => simp [t010_sz] at hn
      | 3, hn => simp [t010_sz] at hn; subst hn; exact (bound_pack (A := 2097152) (B := 256) (bound_pack (A := 8192) (B := 256) (bound_pack (A := 128) (B := 64) (bound_div (a := 128) (d := 1048576) hq) (bound_mod (c := 64) (by decide : (0 : Nat) < 64))) (ExactScalar.clamp_lt (c := 256) (by decide : (0 : Nat) < 256))) (ExactScalar.clamp_lt (c := 256) (by decide : (0 : Nat) < 256)))
      | 4, hn => simp [t010_sz] at hn; subst hn; exact (by decide : (0 : Nat) < 134217728)
      | 5, hn => simp [t010_sz] at hn; subst hn; exact (by decide : (0 : Nat) < 8192)
      | (_ + 6), hn => simp [t010_sz] at hn)
    (fun b nn hn q hq => by
      match b, hn with
      | 0, hn => simp [t010_sz] at hn
      | 1, hn => simp [t010_sz] at hn
      | 2, hn => simp [t010_sz] at hn
      | 3, hn => simp [t010_sz] at hn; subst hn; exact (by decide : (0 : Nat) < 536870912)
      | 4, hn => simp [t010_sz] at hn; subst hn; exact (by decide : (0 : Nat) < 134217728)
      | 5, hn => simp [t010_sz] at hn; subst hn; exact (by decide : (0 : Nat) < 8192)
      | (_ + 6), hn => simp [t010_sz] at hn)

/-- Stage 2 reads no intermediate past what was written there. -/
theorem t010_s2_loc {α : Type} [ExactScalar α] :
    SpecLocal t010_sz (t010_s2_g.spec (α := α)) :=
  GenRed.specLocal t010_s2_g t010_sz
    (fun b nn hn q kk hq hk => by
      match b, hn with
      | 0, hn => simp [t010_sz] at hn
      | 1, hn => simp [t010_sz] at hn
      | 2, hn => simp [t010_sz] at hn
      | 3, hn => simp [t010_sz] at hn; subst hn; exact (by decide : (0 : Nat) < 536870912)
      | 4, hn => simp [t010_sz] at hn; subst hn; exact (bound_pack (A := 8192) (B := 16384) hq hk)
      | 5, hn => simp [t010_sz] at hn; subst hn; exact (by decide : (0 : Nat) < 8192)
      | (_ + 6), hn => simp [t010_sz] at hn)
    (fun b nn hn q hq => by
      match b, hn with
      | 0, hn => simp [t010_sz] at hn
      | 1, hn => simp [t010_sz] at hn
      | 2, hn => simp [t010_sz] at hn
      | 3, hn => simp [t010_sz] at hn; subst hn; exact (by decide : (0 : Nat) < 536870912)
      | 4, hn => simp [t010_sz] at hn; subst hn; exact (by decide : (0 : Nat) < 134217728)
      | 5, hn => simp [t010_sz] at hn; subst hn; exact (by decide : (0 : Nat) < 8192)
      | (_ + 6), hn => simp [t010_sz] at hn)

def t010_chain (α : Type) [ExactScalar α] : List (Stage α) := [⟨t010_s0_g.prog t010_s0_block t010_s0_nkb, t010_s0_g.spec (α := α), 3⟩, ⟨t010_s1_g.prog t010_s1_block t010_s1_nkb, t010_s1_g.spec (α := α), 4⟩, ⟨t010_s2_g.prog t010_s2_block t010_s2_nkb, t010_s2_g.spec (α := α), 5⟩]

theorem t010_imp {α : Type} [ExactScalar α] :
    ∀ st ∈ t010_chain α, Implements st.prog st.spec := by
  intro st hst
  simp only [t010_chain, List.mem_cons, List.not_mem_nil, or_false] at hst
  rcases hst with rfl | rfl | rfl
  · exact t010_s0_impl
  · exact t010_s1_impl
  · exact t010_s2_impl

theorem t010_szok {α : Type} [ExactScalar α] :
    ∀ st ∈ t010_chain α, t010_sz st.out = some st.spec.outSize := by
  intro st hst
  simp only [t010_chain, List.mem_cons, List.not_mem_nil, or_false] at hst
  rcases hst with rfl | rfl | rfl
  · rfl
  · rfl
  · rfl

theorem t010_loc {α : Type} [ExactScalar α] :
    ∀ st ∈ t010_chain α, SpecLocal t010_sz st.spec := by
  intro st hst
  simp only [t010_chain, List.mem_cons, List.not_mem_nil, or_false] at hst
  rcases hst with rfl | rfl | rfl
  · exact t010_s0_loc
  · exact t010_s1_loc
  · exact t010_s2_loc

/-- Correctness certificate for t010: the whole chain. -/
theorem t010_correct {α : Type} [ExactScalar α] :
    ∀ (f : Nat → Buf α) (m : Mem α),
      Compat (sizesAfter (t010_chain α) emptySizes)
        (runStages (t010_chain α) f m) (specStages (t010_chain α) f) :=
  fun f m => stages_correct t010_sz (t010_chain α) emptySizes f f m
    (Compat.refl _ _) (emptySizes_sub t010_sz)
    t010_szok t010_imp t010_loc

def t010_s0_kernel : ReduceKernel :=
  { name := "t010_s0", arity := 3, block := t010_s0_block, nkb := t010_s0_nkb, nout := 536870912, init := FE.zeroC, step := t010_s0_g.step t010_s0_block, stored := t010_s0_g.stored t010_s0_block }
def t010_s1_kernel : ReduceKernel :=
  { name := "t010_s1", arity := 4, block := t010_s1_block, nkb := t010_s1_nkb, nout := 134217728, init := t010_s1_g.seed, step := t010_s1_g.step t010_s1_block, stored := t010_s1_g.stored t010_s1_block }
def t010_s2_kernel : ReduceKernel :=
  { name := "t010_s2", arity := 5, block := t010_s2_block, nkb := t010_s2_nkb, nout := 8192, init := FE.zeroC, step := t010_s2_g.step t010_s2_block, stored := t010_s2_g.stored t010_s2_block }
def t010_kernel : ChainKernel :=
  { name := "t010", arity := 3, sizes := [536870912, 134217728, 8192],
    stages := [t010_s0_kernel, t010_s1_kernel, t010_s2_kernel] }

-- t024: a chain of 4 stage(s), 3 input buffer(s)
--   
def t024_sz : Sizes
  | 3 => some 60825600
  | 4 => some 2764800
  | 5 => some 115200
  | 6 => some 2764800
  | _ => none

def t024_s0_g : GenRed :=
  { nout := 60825600, K := 81
  , offs := fun b => ([(IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 475200)) (IE.lit 3)) (IE.divi IE.rk (IE.lit 27))) (IE.lit 24)) (IE.add (IE.modi (IE.divi (IE.pid 0) (IE.lit 900)) (IE.lit 22)) (IE.modi (IE.divi IE.rk (IE.lit 9)) (IE.lit 3)))) (IE.lit 32)) (IE.add (IE.modi (IE.divi (IE.pid 0) (IE.lit 30)) (IE.lit 30)) (IE.modi (IE.divi IE.rk (IE.lit 3)) (IE.lit 3)))) (IE.lit 32)) (IE.add (IE.modi (IE.pid 0) (IE.lit 30)) (IE.modi IE.rk (IE.lit 3)))), (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 19800)) (IE.lit 24)) (IE.lit 3)) (IE.divi IE.rk (IE.lit 27))) (IE.lit 3)) (IE.modi (IE.divi IE.rk (IE.lit 9)) (IE.lit 3))) (IE.lit 3)) (IE.modi (IE.divi IE.rk (IE.lit 3)) (IE.lit 3))) (IE.lit 3)) (IE.modi IE.rk (IE.lit 3))), (IE.lit 0), (IE.lit 0)]).getD b (IE.lit 0)
  , inRange := (BE.and (BE.and (BE.cmp .lt (IE.add (IE.modi (IE.divi (IE.pid 0) (IE.lit 900)) (IE.lit 22)) (IE.modi (IE.divi IE.rk (IE.lit 9)) (IE.lit 3))) (IE.lit 24)) (BE.cmp .lt (IE.add (IE.modi (IE.divi (IE.pid 0) (IE.lit 30)) (IE.lit 30)) (IE.modi (IE.divi IE.rk (IE.lit 3)) (IE.lit 3))) (IE.lit 32))) (BE.cmp .lt (IE.add (IE.modi (IE.pid 0) (IE.lit 30)) (IE.modi IE.rk (IE.lit 3))) (IE.lit 32)))
  , body := (SE.bin .mul (SE.inp 0) (SE.inp 1))
  , postOffs := fun b => ([(IE.lit 0), (IE.lit 0), (IE.modi (IE.divi (IE.pid 0) (IE.lit 19800)) (IE.lit 24)), (IE.lit 0)]).getD b (IE.lit 0)
  , post := (SE.bin .add (SE.inp 0) (SE.inp 3))
  , outGuard := BE.tt
  , nInp := 4, idxSlot := 1048576 }
def t024_s0_block : Nat := 64
def t024_s0_nkb : Nat := 2

theorem t024_s0_wf : t024_s0_g.Wf :=
  { offs_ok := IE.qkOnly_getD _ (by decide)
  , post_ok := IE.qkOnly_getD _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

theorem t024_s0_impl {α : Type} [ExactScalar α] :
    Implements (t024_s0_g.prog t024_s0_block t024_s0_nkb) (t024_s0_g.spec (α := α)) :=
  GenRed.prog_implements t024_s0_g t024_s0_block t024_s0_nkb t024_s0_wf (by decide) (by decide)

def t024_s1_g : MaxRed :=
  { nout := 2764800, K := 22
  , offs := fun b => ([(IE.lit 0), (IE.lit 0), (IE.lit 0), (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 900)) (IE.lit 22)) IE.rk) (IE.lit 900)) (IE.modi (IE.pid 0) (IE.lit 900))), (IE.lit 0)]).getD b (IE.lit 0)
  , body := (SE.bin .sub (SE.lit false 0 1) (SE.inp 3))
  , postOffs := fun b => ([(IE.lit 0), (IE.lit 0), (IE.lit 0), (IE.lit 0), (IE.lit 0)]).getD b (IE.lit 0)
  , post := (SE.bin .sub (SE.lit false 0 1) (SE.inp 0))
  , nInp := 5, idxSlot := 1048576 }
def t024_s1_block : Nat := 16
def t024_s1_nkb : Nat := 2

theorem t024_s1_wf : t024_s1_g.Wf :=
  { offs_ok := IE.qkOnly_getD _ (by decide)
  , post_ok := IE.qkOnly_getD _ (by decide) }

theorem t024_s1_impl {α : Type} [ExactScalar α] :
    Implements (t024_s1_g.prog t024_s1_block t024_s1_nkb) (t024_s1_g.spec (α := α)) :=
  MaxRed.prog_implements t024_s1_g t024_s1_block t024_s1_nkb t024_s1_wf (by decide) (by decide) (by decide)


def t024_s2_g : GenRed :=
  { nout := 115200, K := 24
  , offs := fun b => ([(IE.lit 0), (IE.lit 0), (IE.lit 0), (IE.lit 0), (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 900)) (IE.lit 24)) IE.rk) (IE.lit 900)) (IE.modi (IE.pid 0) (IE.lit 900))), (IE.lit 0)]).getD b (IE.lit 0)
  , inRange := BE.tt
  , body := (SE.un .exp (SE.inp 4))
  , postOffs := fun b => ([(IE.lit 0), (IE.lit 0), (IE.lit 0), (IE.lit 0), (IE.lit 0), (IE.lit 0)]).getD b (IE.lit 0)
  , post := (SE.inp 0)
  , outGuard := BE.tt
  , nInp := 6, idxSlot := 1048576 }
def t024_s2_block : Nat := 16
def t024_s2_nkb : Nat := 2

theorem t024_s2_wf : t024_s2_g.Wf :=
  { offs_ok := IE.qkOnly_getD _ (by decide)
  , post_ok := IE.qkOnly_getD _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

theorem t024_s2_impl {α : Type} [ExactScalar α] :
    Implements (t024_s2_g.prog t024_s2_block t024_s2_nkb) (t024_s2_g.spec (α := α)) :=
  GenRed.prog_implements t024_s2_g t024_s2_block t024_s2_nkb t024_s2_wf (by decide) (by decide)

def t024_s3_g : GenRed :=
  { nout := 2764800, K := 1
  , offs := fun b => ([(IE.lit 0), (IE.lit 0), (IE.lit 0), (IE.lit 0), (IE.pid 0), (IE.sub (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.mul (IE.lit 24) (IE.lit 900))) (IE.lit 900)) (IE.modi (IE.pid 0) (IE.lit 900))) (IE.sub (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.mul (IE.lit 24) (IE.lit 900))) (IE.lit 900)) (IE.modi (IE.pid 0) (IE.lit 900))) (IE.lit 115199))), (IE.lit 0)]).getD b (IE.lit 0)
  , inRange := BE.tt
  , body := (SE.bin .mul (SE.un .exp (SE.inp 4)) (SE.recip (SE.inp 5)))
  , postOffs := fun b => ([(IE.lit 0), (IE.lit 0), (IE.lit 0), (IE.lit 0), (IE.lit 0), (IE.lit 0), (IE.lit 0)]).getD b (IE.lit 0)
  , post := (SE.inp 0)
  , outGuard := BE.tt
  , nInp := 7, idxSlot := 1048576 }
def t024_s3_block : Nat := 1
def t024_s3_nkb : Nat := 1

theorem t024_s3_wf : t024_s3_g.Wf :=
  { offs_ok := IE.qkOnly_getD _ (by decide)
  , post_ok := IE.qkOnly_getD _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

theorem t024_s3_impl {α : Type} [ExactScalar α] :
    Implements (t024_s3_g.prog t024_s3_block t024_s3_nkb) (t024_s3_g.spec (α := α)) :=
  GenRed.prog_implements t024_s3_g t024_s3_block t024_s3_nkb t024_s3_wf (by decide) (by decide)

/-- Stage 0 reads no intermediate past what was written there. -/
theorem t024_s0_loc {α : Type} [ExactScalar α] :
    SpecLocal t024_sz (t024_s0_g.spec (α := α)) :=
  GenRed.specLocal t024_s0_g t024_sz
    (fun b nn hn q kk hq hk => by
      match b, hn with
      | 0, hn => simp [t024_sz] at hn
      | 1, hn => simp [t024_sz] at hn
      | 2, hn => simp [t024_sz] at hn
      | 3, hn => simp [t024_sz] at hn; subst hn; exact (by decide : (0 : Nat) < 60825600)
      | 4, hn => simp [t024_sz] at hn; subst hn; exact (by decide : (0 : Nat) < 2764800)
      | 5, hn => simp [t024_sz] at hn; subst hn; exact (by decide : (0 : Nat) < 115200)
      | 6, hn => simp [t024_sz] at hn; subst hn; exact (by decide : (0 : Nat) < 2764800)
      | (_ + 7), hn => simp [t024_sz] at hn)
    (fun b nn hn q hq => by
      match b, hn with
      | 0, hn => simp [t024_sz] at hn
      | 1, hn => simp [t024_sz] at hn
      | 2, hn => simp [t024_sz] at hn
      | 3, hn => simp [t024_sz] at hn; subst hn; exact (by decide : (0 : Nat) < 60825600)
      | 4, hn => simp [t024_sz] at hn; subst hn; exact (by decide : (0 : Nat) < 2764800)
      | 5, hn => simp [t024_sz] at hn; subst hn; exact (by decide : (0 : Nat) < 115200)
      | 6, hn => simp [t024_sz] at hn; subst hn; exact (by decide : (0 : Nat) < 2764800)
      | (_ + 7), hn => simp [t024_sz] at hn)

/-- Stage 1 reads no intermediate past what was written there. -/
theorem t024_s1_loc {α : Type} [ExactScalar α] :
    SpecLocal t024_sz (t024_s1_g.spec (α := α)) :=
  MaxRed.specLocal t024_s1_g t024_sz (by decide)
    (fun b nn hn q kk hq hk => by
      match b, hn with
      | 0, hn => simp [t024_sz] at hn
      | 1, hn => simp [t024_sz] at hn
      | 2, hn => simp [t024_sz] at hn
      | 3, hn => simp [t024_sz] at hn; subst hn; exact (bound_pack (A := 67584) (B := 900) (bound_pack (A := 3072) (B := 22) (bound_div (a := 3072) (d := 900) hq) hk) (bound_mod (c := 900) (by decide : (0 : Nat) < 900)))
      | 4, hn => simp [t024_sz] at hn; subst hn; exact (by decide : (0 : Nat) < 2764800)
      | 5, hn => simp [t024_sz] at hn; subst hn; exact (by decide : (0 : Nat) < 115200)
      | 6, hn => simp [t024_sz] at hn; subst hn; exact (by decide : (0 : Nat) < 2764800)
      | (_ + 7), hn => simp [t024_sz] at hn)
    (fun b nn hn q hq => by
      match b, hn with
      | 0, hn => simp [t024_sz] at hn
      | 1, hn => simp [t024_sz] at hn
      | 2, hn => simp [t024_sz] at hn
      | 3, hn => simp [t024_sz] at hn; subst hn; exact (by decide : (0 : Nat) < 60825600)
      | 4, hn => simp [t024_sz] at hn; subst hn; exact (by decide : (0 : Nat) < 2764800)
      | 5, hn => simp [t024_sz] at hn; subst hn; exact (by decide : (0 : Nat) < 115200)
      | 6, hn => simp [t024_sz] at hn; subst hn; exact (by decide : (0 : Nat) < 2764800)
      | (_ + 7), hn => simp [t024_sz] at hn)

/-- Stage 2 reads no intermediate past what was written there. -/
theorem t024_s2_loc {α : Type} [ExactScalar α] :
    SpecLocal t024_sz (t024_s2_g.spec (α := α)) :=
  GenRed.specLocal t024_s2_g t024_sz
    (fun b nn hn q kk hq hk => by
      match b, hn with
      | 0, hn => simp [t024_sz] at hn
      | 1, hn => simp [t024_sz] at hn
      | 2, hn => simp [t024_sz] at hn
      | 3, hn => simp [t024_sz] at hn; subst hn; exact (by decide : (0 : Nat) < 60825600)
      | 4, hn => simp [t024_sz] at hn; subst hn; exact (bound_pack (A := 3072) (B := 900) (bound_pack (A := 128) (B := 24) (bound_div (a := 128) (d := 900) hq) hk) (bound_mod (c := 900) (by decide : (0 : Nat) < 900)))
      | 5, hn => simp [t024_sz] at hn; subst hn; exact (by decide : (0 : Nat) < 115200)
      | 6, hn => simp [t024_sz] at hn; subst hn; exact (by decide : (0 : Nat) < 2764800)
      | (_ + 7), hn => simp [t024_sz] at hn)
    (fun b nn hn q hq => by
      match b, hn with
      | 0, hn => simp [t024_sz] at hn
      | 1, hn => simp [t024_sz] at hn
      | 2, hn => simp [t024_sz] at hn
      | 3, hn => simp [t024_sz] at hn; subst hn; exact (by decide : (0 : Nat) < 60825600)
      | 4, hn => simp [t024_sz] at hn; subst hn; exact (by decide : (0 : Nat) < 2764800)
      | 5, hn => simp [t024_sz] at hn; subst hn; exact (by decide : (0 : Nat) < 115200)
      | 6, hn => simp [t024_sz] at hn; subst hn; exact (by decide : (0 : Nat) < 2764800)
      | (_ + 7), hn => simp [t024_sz] at hn)

/-- Stage 3 reads no intermediate past what was written there. -/
theorem t024_s3_loc {α : Type} [ExactScalar α] :
    SpecLocal t024_sz (t024_s3_g.spec (α := α)) :=
  GenRed.specLocal t024_s3_g t024_sz
    (fun b nn hn q kk hq hk => by
      match b, hn with
      | 0, hn => simp [t024_sz] at hn
      | 1, hn => simp [t024_sz] at hn
      | 2, hn => simp [t024_sz] at hn
      | 3, hn => simp [t024_sz] at hn; subst hn; exact (by decide : (0 : Nat) < 60825600)
      | 4, hn => simp [t024_sz] at hn; subst hn; exact hq
      | 5, hn => simp [t024_sz] at hn; subst hn; exact (ExactScalar.clamp_lt (c := 115200) (by decide : (0 : Nat) < 115200))
      | 6, hn => simp [t024_sz] at hn; subst hn; exact (by decide : (0 : Nat) < 2764800)
      | (_ + 7), hn => simp [t024_sz] at hn)
    (fun b nn hn q hq => by
      match b, hn with
      | 0, hn => simp [t024_sz] at hn
      | 1, hn => simp [t024_sz] at hn
      | 2, hn => simp [t024_sz] at hn
      | 3, hn => simp [t024_sz] at hn; subst hn; exact (by decide : (0 : Nat) < 60825600)
      | 4, hn => simp [t024_sz] at hn; subst hn; exact (by decide : (0 : Nat) < 2764800)
      | 5, hn => simp [t024_sz] at hn; subst hn; exact (by decide : (0 : Nat) < 115200)
      | 6, hn => simp [t024_sz] at hn; subst hn; exact (by decide : (0 : Nat) < 2764800)
      | (_ + 7), hn => simp [t024_sz] at hn)

def t024_chain (α : Type) [ExactScalar α] : List (Stage α) := [⟨t024_s0_g.prog t024_s0_block t024_s0_nkb, t024_s0_g.spec (α := α), 3⟩, ⟨t024_s1_g.prog t024_s1_block t024_s1_nkb, t024_s1_g.spec (α := α), 4⟩, ⟨t024_s2_g.prog t024_s2_block t024_s2_nkb, t024_s2_g.spec (α := α), 5⟩, ⟨t024_s3_g.prog t024_s3_block t024_s3_nkb, t024_s3_g.spec (α := α), 6⟩]

theorem t024_imp {α : Type} [ExactScalar α] :
    ∀ st ∈ t024_chain α, Implements st.prog st.spec := by
  intro st hst
  simp only [t024_chain, List.mem_cons, List.not_mem_nil, or_false] at hst
  rcases hst with rfl | rfl | rfl | rfl
  · exact t024_s0_impl
  · exact t024_s1_impl
  · exact t024_s2_impl
  · exact t024_s3_impl

theorem t024_szok {α : Type} [ExactScalar α] :
    ∀ st ∈ t024_chain α, t024_sz st.out = some st.spec.outSize := by
  intro st hst
  simp only [t024_chain, List.mem_cons, List.not_mem_nil, or_false] at hst
  rcases hst with rfl | rfl | rfl | rfl
  · rfl
  · rfl
  · rfl
  · rfl

theorem t024_loc {α : Type} [ExactScalar α] :
    ∀ st ∈ t024_chain α, SpecLocal t024_sz st.spec := by
  intro st hst
  simp only [t024_chain, List.mem_cons, List.not_mem_nil, or_false] at hst
  rcases hst with rfl | rfl | rfl | rfl
  · exact t024_s0_loc
  · exact t024_s1_loc
  · exact t024_s2_loc
  · exact t024_s3_loc

/-- Correctness certificate for t024: the whole chain. -/
theorem t024_correct {α : Type} [ExactScalar α] :
    ∀ (f : Nat → Buf α) (m : Mem α),
      Compat (sizesAfter (t024_chain α) emptySizes)
        (runStages (t024_chain α) f m) (specStages (t024_chain α) f) :=
  fun f m => stages_correct t024_sz (t024_chain α) emptySizes f f m
    (Compat.refl _ _) (emptySizes_sub t024_sz)
    t024_szok t024_imp t024_loc

def t024_s0_kernel : ReduceKernel :=
  { name := "t024_s0", arity := 3, block := t024_s0_block, nkb := t024_s0_nkb, nout := 60825600, init := FE.zeroC, step := t024_s0_g.step t024_s0_block, stored := t024_s0_g.stored t024_s0_block }
def t024_s1_kernel : ReduceKernel :=
  { name := "t024_s1", arity := 4, block := t024_s1_block, nkb := t024_s1_nkb, nout := 2764800, init := t024_s1_g.seed, step := t024_s1_g.step t024_s1_block, stored := t024_s1_g.stored t024_s1_block }
def t024_s2_kernel : ReduceKernel :=
  { name := "t024_s2", arity := 5, block := t024_s2_block, nkb := t024_s2_nkb, nout := 115200, init := FE.zeroC, step := t024_s2_g.step t024_s2_block, stored := t024_s2_g.stored t024_s2_block }
def t024_s3_kernel : ReduceKernel :=
  { name := "t024_s3", arity := 6, block := t024_s3_block, nkb := t024_s3_nkb, nout := 2764800, init := FE.zeroC, step := t024_s3_g.step t024_s3_block, stored := t024_s3_g.stored t024_s3_block }
def t024_kernel : ChainKernel :=
  { name := "t024", arity := 3, sizes := [60825600, 2764800, 115200, 2764800],
    stages := [t024_s0_kernel, t024_s1_kernel, t024_s2_kernel, t024_s3_kernel] }

-- t055: a chain of 3 stage(s), 3 input buffer(s)
--   fused <built-in function mul> into stage 2
def t055_sz : Sizes
  | 3 => some 4194304
  | 4 => some 2097152
  | 5 => some 128
  | _ => none

def t055_s0_g : GenRed :=
  { nout := 4194304, K := 32768
  , offs := fun b => ([(IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 32768)) (IE.lit 32768)) IE.rk), (IE.add (IE.mul (IE.modi (IE.pid 0) (IE.lit 32768)) (IE.lit 32768)) IE.rk), (IE.lit 0), (IE.lit 0)]).getD b (IE.lit 0)
  , inRange := BE.tt
  , body := (SE.bin .mul (SE.inp 0) (SE.inp 1))
  , postOffs := fun b => ([(IE.lit 0), (IE.lit 0), (IE.modi (IE.pid 0) (IE.lit 32768)), (IE.lit 0)]).getD b (IE.lit 0)
  , post := (SE.bin .add (SE.inp 0) (SE.inp 3))
  , outGuard := BE.tt
  , nInp := 4, idxSlot := 1048576 }
def t055_s0_block : Nat := 1024
def t055_s0_nkb : Nat := 32

theorem t055_s0_wf : t055_s0_g.Wf :=
  { offs_ok := IE.qkOnly_getD _ (by decide)
  , post_ok := IE.qkOnly_getD _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

theorem t055_s0_impl {α : Type} [ExactScalar α] :
    Implements (t055_s0_g.prog t055_s0_block t055_s0_nkb) (t055_s0_g.spec (α := α)) :=
  GenRed.prog_implements t055_s0_g t055_s0_block t055_s0_nkb t055_s0_wf (by decide) (by decide)

def t055_s1_g : MaxRed :=
  { nout := 2097152, K := 2
  , offs := fun b => ([(IE.lit 0), (IE.lit 0), (IE.lit 0), (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 16384)) (IE.lit 32768)) (IE.sub (IE.add (IE.mul (IE.modi (IE.pid 0) (IE.lit 16384)) (IE.lit 2)) (IE.sub (IE.add IE.rk (IE.sub (IE.sub (IE.lit 0) (IE.mul (IE.modi (IE.pid 0) (IE.lit 16384)) (IE.lit 2))) IE.rk)) (IE.sub (IE.add IE.rk (IE.sub (IE.sub (IE.lit 0) (IE.mul (IE.modi (IE.pid 0) (IE.lit 16384)) (IE.lit 2))) IE.rk)) (IE.sub (IE.lit 32767) (IE.mul (IE.modi (IE.pid 0) (IE.lit 16384)) (IE.lit 2)))))) (IE.sub (IE.add (IE.mul (IE.modi (IE.pid 0) (IE.lit 16384)) (IE.lit 2)) (IE.sub (IE.add IE.rk (IE.sub (IE.sub (IE.lit 0) (IE.mul (IE.modi (IE.pid 0) (IE.lit 16384)) (IE.lit 2))) IE.rk)) (IE.sub (IE.add IE.rk (IE.sub (IE.sub (IE.lit 0) (IE.mul (IE.modi (IE.pid 0) (IE.lit 16384)) (IE.lit 2))) IE.rk)) (IE.sub (IE.lit 32767) (IE.mul (IE.modi (IE.pid 0) (IE.lit 16384)) (IE.lit 2)))))) (IE.lit 32767)))), (IE.lit 0)]).getD b (IE.lit 0)
  , body := (SE.inp 3)
  , postOffs := fun b => ([(IE.lit 0), (IE.lit 0), (IE.lit 0), (IE.lit 0), (IE.lit 0)]).getD b (IE.lit 0)
  , post := (SE.inp 0)
  , nInp := 5, idxSlot := 1048576 }
def t055_s1_block : Nat := 2
def t055_s1_nkb : Nat := 1

theorem t055_s1_wf : t055_s1_g.Wf :=
  { offs_ok := IE.qkOnly_getD _ (by decide)
  , post_ok := IE.qkOnly_getD _ (by decide) }

theorem t055_s1_impl {α : Type} [ExactScalar α] :
    Implements (t055_s1_g.prog t055_s1_block t055_s1_nkb) (t055_s1_g.spec (α := α)) :=
  MaxRed.prog_implements t055_s1_g t055_s1_block t055_s1_nkb t055_s1_wf (by decide) (by decide) (by decide)


def t055_s2_g : GenRed :=
  { nout := 128, K := 16384
  , offs := fun b => ([(IE.lit 0), (IE.lit 0), (IE.lit 0), (IE.lit 0), (IE.add (IE.mul (IE.pid 0) (IE.lit 16384)) IE.rk), (IE.lit 0)]).getD b (IE.lit 0)
  , inRange := BE.tt
  , body := (SE.inp 4)
  , postOffs := fun b => ([(IE.lit 0), (IE.lit 0), (IE.lit 0), (IE.lit 0), (IE.lit 0), (IE.lit 0)]).getD b (IE.lit 0)
  , post := (SE.bin .mul (SE.inp 0) (SE.lit false 1 2))
  , outGuard := BE.tt
  , nInp := 6, idxSlot := 1048576 }
def t055_s2_block : Nat := 1024
def t055_s2_nkb : Nat := 16

theorem t055_s2_wf : t055_s2_g.Wf :=
  { offs_ok := IE.qkOnly_getD _ (by decide)
  , post_ok := IE.qkOnly_getD _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

theorem t055_s2_impl {α : Type} [ExactScalar α] :
    Implements (t055_s2_g.prog t055_s2_block t055_s2_nkb) (t055_s2_g.spec (α := α)) :=
  GenRed.prog_implements t055_s2_g t055_s2_block t055_s2_nkb t055_s2_wf (by decide) (by decide)

/-- Stage 0 reads no intermediate past what was written there. -/
theorem t055_s0_loc {α : Type} [ExactScalar α] :
    SpecLocal t055_sz (t055_s0_g.spec (α := α)) :=
  GenRed.specLocal t055_s0_g t055_sz
    (fun b nn hn q kk hq hk => by
      match b, hn with
      | 0, hn => simp [t055_sz] at hn
      | 1, hn => simp [t055_sz] at hn
      | 2, hn => simp [t055_sz] at hn
      | 3, hn => simp [t055_sz] at hn; subst hn; exact (by decide : (0 : Nat) < 4194304)
      | 4, hn => simp [t055_sz] at hn; subst hn; exact (by decide : (0 : Nat) < 2097152)
      | 5, hn => simp [t055_sz] at hn; subst hn; exact (by decide : (0 : Nat) < 128)
      | (_ + 6), hn => simp [t055_sz] at hn)
    (fun b nn hn q hq => by
      match b, hn with
      | 0, hn => simp [t055_sz] at hn
      | 1, hn => simp [t055_sz] at hn
      | 2, hn => simp [t055_sz] at hn
      | 3, hn => simp [t055_sz] at hn; subst hn; exact (by decide : (0 : Nat) < 4194304)
      | 4, hn => simp [t055_sz] at hn; subst hn; exact (by decide : (0 : Nat) < 2097152)
      | 5, hn => simp [t055_sz] at hn; subst hn; exact (by decide : (0 : Nat) < 128)
      | (_ + 6), hn => simp [t055_sz] at hn)

/-- Stage 1 reads no intermediate past what was written there. -/
theorem t055_s1_loc {α : Type} [ExactScalar α] :
    SpecLocal t055_sz (t055_s1_g.spec (α := α)) :=
  MaxRed.specLocal t055_s1_g t055_sz (by decide)
    (fun b nn hn q kk hq hk => by
      match b, hn with
      | 0, hn => simp [t055_sz] at hn
      | 1, hn => simp [t055_sz] at hn
      | 2, hn => simp [t055_sz] at hn
      | 3, hn => simp [t055_sz] at hn; subst hn; exact (bound_pack (A := 128) (B := 32768) (bound_div (a := 128) (d := 16384) hq) (ExactScalar.clamp_lt (c := 32768) (by decide : (0 : Nat) < 32768)))
      | 4, hn => simp [t055_sz] at hn; subst hn; exact (by decide : (0 : Nat) < 2097152)
      | 5, hn => simp [t055_sz] at hn; subst hn; exact (by decide : (0 : Nat) < 128)
      | (_ + 6), hn => simp [t055_sz] at hn)
    (fun b nn hn q hq => by
      match b, hn with
      | 0, hn => simp [t055_sz] at hn
      | 1, hn => simp [t055_sz] at hn
      | 2, hn => simp [t055_sz] at hn
      | 3, hn => simp [t055_sz] at hn; subst hn; exact (by decide : (0 : Nat) < 4194304)
      | 4, hn => simp [t055_sz] at hn; subst hn; exact (by decide : (0 : Nat) < 2097152)
      | 5, hn => simp [t055_sz] at hn; subst hn; exact (by decide : (0 : Nat) < 128)
      | (_ + 6), hn => simp [t055_sz] at hn)

/-- Stage 2 reads no intermediate past what was written there. -/
theorem t055_s2_loc {α : Type} [ExactScalar α] :
    SpecLocal t055_sz (t055_s2_g.spec (α := α)) :=
  GenRed.specLocal t055_s2_g t055_sz
    (fun b nn hn q kk hq hk => by
      match b, hn with
      | 0, hn => simp [t055_sz] at hn
      | 1, hn => simp [t055_sz] at hn
      | 2, hn => simp [t055_sz] at hn
      | 3, hn => simp [t055_sz] at hn; subst hn; exact (by decide : (0 : Nat) < 4194304)
      | 4, hn => simp [t055_sz] at hn; subst hn; exact (bound_pack (A := 128) (B := 16384) hq hk)
      | 5, hn => simp [t055_sz] at hn; subst hn; exact (by decide : (0 : Nat) < 128)
      | (_ + 6), hn => simp [t055_sz] at hn)
    (fun b nn hn q hq => by
      match b, hn with
      | 0, hn => simp [t055_sz] at hn
      | 1, hn => simp [t055_sz] at hn
      | 2, hn => simp [t055_sz] at hn
      | 3, hn => simp [t055_sz] at hn; subst hn; exact (by decide : (0 : Nat) < 4194304)
      | 4, hn => simp [t055_sz] at hn; subst hn; exact (by decide : (0 : Nat) < 2097152)
      | 5, hn => simp [t055_sz] at hn; subst hn; exact (by decide : (0 : Nat) < 128)
      | (_ + 6), hn => simp [t055_sz] at hn)

def t055_chain (α : Type) [ExactScalar α] : List (Stage α) := [⟨t055_s0_g.prog t055_s0_block t055_s0_nkb, t055_s0_g.spec (α := α), 3⟩, ⟨t055_s1_g.prog t055_s1_block t055_s1_nkb, t055_s1_g.spec (α := α), 4⟩, ⟨t055_s2_g.prog t055_s2_block t055_s2_nkb, t055_s2_g.spec (α := α), 5⟩]

theorem t055_imp {α : Type} [ExactScalar α] :
    ∀ st ∈ t055_chain α, Implements st.prog st.spec := by
  intro st hst
  simp only [t055_chain, List.mem_cons, List.not_mem_nil, or_false] at hst
  rcases hst with rfl | rfl | rfl
  · exact t055_s0_impl
  · exact t055_s1_impl
  · exact t055_s2_impl

theorem t055_szok {α : Type} [ExactScalar α] :
    ∀ st ∈ t055_chain α, t055_sz st.out = some st.spec.outSize := by
  intro st hst
  simp only [t055_chain, List.mem_cons, List.not_mem_nil, or_false] at hst
  rcases hst with rfl | rfl | rfl
  · rfl
  · rfl
  · rfl

theorem t055_loc {α : Type} [ExactScalar α] :
    ∀ st ∈ t055_chain α, SpecLocal t055_sz st.spec := by
  intro st hst
  simp only [t055_chain, List.mem_cons, List.not_mem_nil, or_false] at hst
  rcases hst with rfl | rfl | rfl
  · exact t055_s0_loc
  · exact t055_s1_loc
  · exact t055_s2_loc

/-- Correctness certificate for t055: the whole chain. -/
theorem t055_correct {α : Type} [ExactScalar α] :
    ∀ (f : Nat → Buf α) (m : Mem α),
      Compat (sizesAfter (t055_chain α) emptySizes)
        (runStages (t055_chain α) f m) (specStages (t055_chain α) f) :=
  fun f m => stages_correct t055_sz (t055_chain α) emptySizes f f m
    (Compat.refl _ _) (emptySizes_sub t055_sz)
    t055_szok t055_imp t055_loc

def t055_s0_kernel : ReduceKernel :=
  { name := "t055_s0", arity := 3, block := t055_s0_block, nkb := t055_s0_nkb, nout := 4194304, init := FE.zeroC, step := t055_s0_g.step t055_s0_block, stored := t055_s0_g.stored t055_s0_block }
def t055_s1_kernel : ReduceKernel :=
  { name := "t055_s1", arity := 4, block := t055_s1_block, nkb := t055_s1_nkb, nout := 2097152, init := t055_s1_g.seed, step := t055_s1_g.step t055_s1_block, stored := t055_s1_g.stored t055_s1_block }
def t055_s2_kernel : ReduceKernel :=
  { name := "t055_s2", arity := 5, block := t055_s2_block, nkb := t055_s2_nkb, nout := 128, init := FE.zeroC, step := t055_s2_g.step t055_s2_block, stored := t055_s2_g.stored t055_s2_block }
def t055_kernel : ChainKernel :=
  { name := "t055", arity := 3, sizes := [4194304, 2097152, 128],
    stages := [t055_s0_kernel, t055_s1_kernel, t055_s2_kernel] }

-- t082: a chain of 3 stage(s), 4 input buffer(s)
--   fused <built-in method tanh of type object at 0x77f82f4a5640> into stage 0; fused <built-in function mul> into stage 0
def t082_sz : Sizes
  | 4 => some 528515072
  | 5 => some 528515072
  | 6 => some 32514048
  | _ => none

def t082_s0_g : GenRed :=
  { nout := 528515072, K := 72
  , offs := fun b => ([(IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 4129024)) (IE.lit 8)) (IE.divi IE.rk (IE.lit 9))) (IE.lit 256)) (IE.add (IE.modi (IE.divi (IE.pid 0) (IE.lit 254)) (IE.lit 254)) (IE.modi (IE.divi IE.rk (IE.lit 3)) (IE.lit 3)))) (IE.lit 256)) (IE.add (IE.modi (IE.pid 0) (IE.lit 254)) (IE.modi IE.rk (IE.lit 3)))), (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 64516)) (IE.lit 64)) (IE.lit 8)) (IE.divi IE.rk (IE.lit 9))) (IE.lit 3)) (IE.modi (IE.divi IE.rk (IE.lit 3)) (IE.lit 3))) (IE.lit 3)) (IE.modi IE.rk (IE.lit 3))), (IE.lit 0), (IE.lit 0), (IE.lit 0)]).getD b (IE.lit 0)
  , inRange := (BE.and (BE.cmp .lt (IE.add (IE.modi (IE.divi (IE.pid 0) (IE.lit 254)) (IE.lit 254)) (IE.modi (IE.divi IE.rk (IE.lit 3)) (IE.lit 3))) (IE.lit 256)) (BE.cmp .lt (IE.add (IE.modi (IE.pid 0) (IE.lit 254)) (IE.modi IE.rk (IE.lit 3))) (IE.lit 256)))
  , body := (SE.bin .mul (SE.inp 0) (SE.inp 1))
  , postOffs := fun b => ([(IE.lit 0), (IE.lit 0), (IE.modi (IE.divi (IE.pid 0) (IE.lit 64516)) (IE.lit 64)), (IE.lit 0), (IE.lit 0)]).getD b (IE.lit 0)
  , post := (SE.bin .mul (SE.un .tanh (SE.bin .add (SE.inp 0) (SE.inp 3))) (SE.lit false 2 1))
  , outGuard := BE.tt
  , nInp := 5, idxSlot := 1048576 }
def t082_s0_block : Nat := 64
def t082_s0_nkb : Nat := 2

theorem t082_s0_wf : t082_s0_g.Wf :=
  { offs_ok := IE.qkOnly_getD _ (by decide)
  , post_ok := IE.qkOnly_getD _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

theorem t082_s0_impl {α : Type} [ExactScalar α] :
    Implements (t082_s0_g.prog t082_s0_block t082_s0_nkb) (t082_s0_g.spec (α := α)) :=
  GenRed.prog_implements t082_s0_g t082_s0_block t082_s0_nkb t082_s0_wf (by decide) (by decide)

def t082_s1_g : GenRed :=
  { nout := 528515072, K := 1
  , offs := fun b => ([(IE.lit 0), (IE.lit 0), (IE.lit 0), (IE.modi (IE.divi (IE.pid 0) (IE.lit 64516)) (IE.lit 64)), (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 4129024)) (IE.lit 64)) (IE.modi (IE.divi (IE.pid 0) (IE.lit 64516)) (IE.lit 64))) (IE.lit 254)) (IE.modi (IE.divi (IE.pid 0) (IE.lit 254)) (IE.lit 254))) (IE.lit 254)) (IE.modi (IE.pid 0) (IE.lit 254))), (IE.lit 0)]).getD b (IE.lit 0)
  , inRange := BE.tt
  , body := (SE.bin .add (SE.inp 4) (SE.inp 3))
  , postOffs := fun b => ([(IE.lit 0), (IE.lit 0), (IE.lit 0), (IE.lit 0), (IE.lit 0), (IE.lit 0)]).getD b (IE.lit 0)
  , post := (SE.inp 0)
  , outGuard := BE.tt
  , nInp := 6, idxSlot := 1048576 }
def t082_s1_block : Nat := 1
def t082_s1_nkb : Nat := 1

theorem t082_s1_wf : t082_s1_g.Wf :=
  { offs_ok := IE.qkOnly_getD _ (by decide)
  , post_ok := IE.qkOnly_getD _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

theorem t082_s1_impl {α : Type} [ExactScalar α] :
    Implements (t082_s1_g.prog t082_s1_block t082_s1_nkb) (t082_s1_g.spec (α := α)) :=
  GenRed.prog_implements t082_s1_g t082_s1_block t082_s1_nkb t082_s1_wf (by decide) (by decide)

def t082_s2_g : MaxRed :=
  { nout := 32514048, K := 16
  , offs := fun b => ([(IE.lit 0), (IE.lit 0), (IE.lit 0), (IE.lit 0), (IE.lit 0), (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 254016)) (IE.lit 64)) (IE.modi (IE.divi (IE.pid 0) (IE.lit 3969)) (IE.lit 64))) (IE.lit 254)) (IE.sub (IE.add (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 63)) (IE.lit 63)) (IE.lit 4)) (IE.sub (IE.add (IE.divi IE.rk (IE.lit 4)) (IE.sub (IE.sub (IE.lit 0) (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 63)) (IE.lit 63)) (IE.lit 4))) (IE.divi IE.rk (IE.lit 4)))) (IE.sub (IE.add (IE.divi IE.rk (IE.lit 4)) (IE.sub (IE.sub (IE.lit 0) (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 63)) (IE.lit 63)) (IE.lit 4))) (IE.divi IE.rk (IE.lit 4)))) (IE.sub (IE.lit 253) (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 63)) (IE.lit 63)) (IE.lit 4)))))) (IE.sub (IE.add (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 63)) (IE.lit 63)) (IE.lit 4)) (IE.sub (IE.add (IE.divi IE.rk (IE.lit 4)) (IE.sub (IE.sub (IE.lit 0) (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 63)) (IE.lit 63)) (IE.lit 4))) (IE.divi IE.rk (IE.lit 4)))) (IE.sub (IE.add (IE.divi IE.rk (IE.lit 4)) (IE.sub (IE.sub (IE.lit 0) (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 63)) (IE.lit 63)) (IE.lit 4))) (IE.divi IE.rk (IE.lit 4)))) (IE.sub (IE.lit 253) (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 63)) (IE.lit 63)) (IE.lit 4)))))) (IE.lit 253)))) (IE.lit 254)) (IE.sub (IE.add (IE.mul (IE.modi (IE.pid 0) (IE.lit 63)) (IE.lit 4)) (IE.sub (IE.add (IE.modi IE.rk (IE.lit 4)) (IE.sub (IE.sub (IE.lit 0) (IE.mul (IE.modi (IE.pid 0) (IE.lit 63)) (IE.lit 4))) (IE.modi IE.rk (IE.lit 4)))) (IE.sub (IE.add (IE.modi IE.rk (IE.lit 4)) (IE.sub (IE.sub (IE.lit 0) (IE.mul (IE.modi (IE.pid 0) (IE.lit 63)) (IE.lit 4))) (IE.modi IE.rk (IE.lit 4)))) (IE.sub (IE.lit 253) (IE.mul (IE.modi (IE.pid 0) (IE.lit 63)) (IE.lit 4)))))) (IE.sub (IE.add (IE.mul (IE.modi (IE.pid 0) (IE.lit 63)) (IE.lit 4)) (IE.sub (IE.add (IE.modi IE.rk (IE.lit 4)) (IE.sub (IE.sub (IE.lit 0) (IE.mul (IE.modi (IE.pid 0) (IE.lit 63)) (IE.lit 4))) (IE.modi IE.rk (IE.lit 4)))) (IE.sub (IE.add (IE.modi IE.rk (IE.lit 4)) (IE.sub (IE.sub (IE.lit 0) (IE.mul (IE.modi (IE.pid 0) (IE.lit 63)) (IE.lit 4))) (IE.modi IE.rk (IE.lit 4)))) (IE.sub (IE.lit 253) (IE.mul (IE.modi (IE.pid 0) (IE.lit 63)) (IE.lit 4)))))) (IE.lit 253)))), (IE.lit 0)]).getD b (IE.lit 0)
  , body := (SE.inp 5)
  , postOffs := fun b => ([(IE.lit 0), (IE.lit 0), (IE.lit 0), (IE.lit 0), (IE.lit 0), (IE.lit 0), (IE.lit 0)]).getD b (IE.lit 0)
  , post := (SE.inp 0)
  , nInp := 7, idxSlot := 1048576 }
def t082_s2_block : Nat := 16
def t082_s2_nkb : Nat := 1

theorem t082_s2_wf : t082_s2_g.Wf :=
  { offs_ok := IE.qkOnly_getD _ (by decide)
  , post_ok := IE.qkOnly_getD _ (by decide) }

theorem t082_s2_impl {α : Type} [ExactScalar α] :
    Implements (t082_s2_g.prog t082_s2_block t082_s2_nkb) (t082_s2_g.spec (α := α)) :=
  MaxRed.prog_implements t082_s2_g t082_s2_block t082_s2_nkb t082_s2_wf (by decide) (by decide) (by decide)


/-- Stage 0 reads no intermediate past what was written there. -/
theorem t082_s0_loc {α : Type} [ExactScalar α] :
    SpecLocal t082_sz (t082_s0_g.spec (α := α)) :=
  GenRed.specLocal t082_s0_g t082_sz
    (fun b nn hn q kk hq hk => by
      match b, hn with
      | 0, hn => simp [t082_sz] at hn
      | 1, hn => simp [t082_sz] at hn
      | 2, hn => simp [t082_sz] at hn
      | 3, hn => simp [t082_sz] at hn
      | 4, hn => simp [t082_sz] at hn; subst hn; exact (by decide : (0 : Nat) < 528515072)
      | 5, hn => simp [t082_sz] at hn; subst hn; exact (by decide : (0 : Nat) < 528515072)
      | 6, hn => simp [t082_sz] at hn; subst hn; exact (by decide : (0 : Nat) < 32514048)
      | (_ + 7), hn => simp [t082_sz] at hn)
    (fun b nn hn q hq => by
      match b, hn with
      | 0, hn => simp [t082_sz] at hn
      | 1, hn => simp [t082_sz] at hn
      | 2, hn => simp [t082_sz] at hn
      | 3, hn => simp [t082_sz] at hn
      | 4, hn => simp [t082_sz] at hn; subst hn; exact (by decide : (0 : Nat) < 528515072)
      | 5, hn => simp [t082_sz] at hn; subst hn; exact (by decide : (0 : Nat) < 528515072)
      | 6, hn => simp [t082_sz] at hn; subst hn; exact (by decide : (0 : Nat) < 32514048)
      | (_ + 7), hn => simp [t082_sz] at hn)

/-- Stage 1 reads no intermediate past what was written there. -/
theorem t082_s1_loc {α : Type} [ExactScalar α] :
    SpecLocal t082_sz (t082_s1_g.spec (α := α)) :=
  GenRed.specLocal t082_s1_g t082_sz
    (fun b nn hn q kk hq hk => by
      match b, hn with
      | 0, hn => simp [t082_sz] at hn
      | 1, hn => simp [t082_sz] at hn
      | 2, hn => simp [t082_sz] at hn
      | 3, hn => simp [t082_sz] at hn
      | 4, hn => simp [t082_sz] at hn; subst hn; exact (bound_pack (A := 2080768) (B := 254) (bound_pack (A := 8192) (B := 254) (bound_pack (A := 128) (B := 64) (bound_div (a := 128) (d := 4129024) hq) (bound_mod (c := 64) (by decide : (0 : Nat) < 64))) (bound_mod (c := 254) (by decide : (0 : Nat) < 254))) (bound_mod (c := 254) (by decide : (0 : Nat) < 254)))
      | 5, hn => simp [t082_sz] at hn; subst hn; exact (by decide : (0 : Nat) < 528515072)
      | 6, hn => simp [t082_sz] at hn; subst hn; exact (by decide : (0 : Nat) < 32514048)
      | (_ + 7), hn => simp [t082_sz] at hn)
    (fun b nn hn q hq => by
      match b, hn with
      | 0, hn => simp [t082_sz] at hn
      | 1, hn => simp [t082_sz] at hn
      | 2, hn => simp [t082_sz] at hn
      | 3, hn => simp [t082_sz] at hn
      | 4, hn => simp [t082_sz] at hn; subst hn; exact (by decide : (0 : Nat) < 528515072)
      | 5, hn => simp [t082_sz] at hn; subst hn; exact (by decide : (0 : Nat) < 528515072)
      | 6, hn => simp [t082_sz] at hn; subst hn; exact (by decide : (0 : Nat) < 32514048)
      | (_ + 7), hn => simp [t082_sz] at hn)

/-- Stage 2 reads no intermediate past what was written there. -/
theorem t082_s2_loc {α : Type} [ExactScalar α] :
    SpecLocal t082_sz (t082_s2_g.spec (α := α)) :=
  MaxRed.specLocal t082_s2_g t082_sz (by decide)
    (fun b nn hn q kk hq hk => by
      match b, hn with
      | 0, hn => simp [t082_sz] at hn
      | 1, hn => simp [t082_sz] at hn
      | 2, hn => simp [t082_sz] at hn
      | 3, hn => simp [t082_sz] at hn
      | 4, hn => simp [t082_sz] at hn; subst hn; exact (by decide : (0 : Nat) < 528515072)
      | 5, hn => simp [t082_sz] at hn; subst hn; exact (bound_pack (A := 2080768) (B := 254) (bound_pack (A := 8192) (B := 254) (bound_pack (A := 128) (B := 64) (bound_div (a := 128) (d := 254016) hq) (bound_mod (c := 64) (by decide : (0 : Nat) < 64))) (ExactScalar.clamp_lt (c := 254) (by decide : (0 : Nat) < 254))) (ExactScalar.clamp_lt (c := 254) (by decide : (0 : Nat) < 254)))
      | 6, hn => simp [t082_sz] at hn; subst hn; exact (by decide : (0 : Nat) < 32514048)
      | (_ + 7), hn => simp [t082_sz] at hn)
    (fun b nn hn q hq => by
      match b, hn with
      | 0, hn => simp [t082_sz] at hn
      | 1, hn => simp [t082_sz] at hn
      | 2, hn => simp [t082_sz] at hn
      | 3, hn => simp [t082_sz] at hn
      | 4, hn => simp [t082_sz] at hn; subst hn; exact (by decide : (0 : Nat) < 528515072)
      | 5, hn => simp [t082_sz] at hn; subst hn; exact (by decide : (0 : Nat) < 528515072)
      | 6, hn => simp [t082_sz] at hn; subst hn; exact (by decide : (0 : Nat) < 32514048)
      | (_ + 7), hn => simp [t082_sz] at hn)

def t082_chain (α : Type) [ExactScalar α] : List (Stage α) := [⟨t082_s0_g.prog t082_s0_block t082_s0_nkb, t082_s0_g.spec (α := α), 4⟩, ⟨t082_s1_g.prog t082_s1_block t082_s1_nkb, t082_s1_g.spec (α := α), 5⟩, ⟨t082_s2_g.prog t082_s2_block t082_s2_nkb, t082_s2_g.spec (α := α), 6⟩]

theorem t082_imp {α : Type} [ExactScalar α] :
    ∀ st ∈ t082_chain α, Implements st.prog st.spec := by
  intro st hst
  simp only [t082_chain, List.mem_cons, List.not_mem_nil, or_false] at hst
  rcases hst with rfl | rfl | rfl
  · exact t082_s0_impl
  · exact t082_s1_impl
  · exact t082_s2_impl

theorem t082_szok {α : Type} [ExactScalar α] :
    ∀ st ∈ t082_chain α, t082_sz st.out = some st.spec.outSize := by
  intro st hst
  simp only [t082_chain, List.mem_cons, List.not_mem_nil, or_false] at hst
  rcases hst with rfl | rfl | rfl
  · rfl
  · rfl
  · rfl

theorem t082_loc {α : Type} [ExactScalar α] :
    ∀ st ∈ t082_chain α, SpecLocal t082_sz st.spec := by
  intro st hst
  simp only [t082_chain, List.mem_cons, List.not_mem_nil, or_false] at hst
  rcases hst with rfl | rfl | rfl
  · exact t082_s0_loc
  · exact t082_s1_loc
  · exact t082_s2_loc

/-- Correctness certificate for t082: the whole chain. -/
theorem t082_correct {α : Type} [ExactScalar α] :
    ∀ (f : Nat → Buf α) (m : Mem α),
      Compat (sizesAfter (t082_chain α) emptySizes)
        (runStages (t082_chain α) f m) (specStages (t082_chain α) f) :=
  fun f m => stages_correct t082_sz (t082_chain α) emptySizes f f m
    (Compat.refl _ _) (emptySizes_sub t082_sz)
    t082_szok t082_imp t082_loc

def t082_s0_kernel : ReduceKernel :=
  { name := "t082_s0", arity := 4, block := t082_s0_block, nkb := t082_s0_nkb, nout := 528515072, init := FE.zeroC, step := t082_s0_g.step t082_s0_block, stored := t082_s0_g.stored t082_s0_block }
def t082_s1_kernel : ReduceKernel :=
  { name := "t082_s1", arity := 5, block := t082_s1_block, nkb := t082_s1_nkb, nout := 528515072, init := FE.zeroC, step := t082_s1_g.step t082_s1_block, stored := t082_s1_g.stored t082_s1_block }
def t082_s2_kernel : ReduceKernel :=
  { name := "t082_s2", arity := 6, block := t082_s2_block, nkb := t082_s2_nkb, nout := 32514048, init := t082_s2_g.seed, step := t082_s2_g.step t082_s2_block, stored := t082_s2_g.stored t082_s2_block }
def t082_kernel : ChainKernel :=
  { name := "t082", arity := 4, sizes := [528515072, 528515072, 32514048],
    stages := [t082_s0_kernel, t082_s1_kernel, t082_s2_kernel] }

def main : IO Unit := do
  IO.FS.writeFile "../generated/t010.py" t010_kernel.render
  IO.FS.writeFile "../generated/t024.py" t024_kernel.render
  IO.FS.writeFile "../generated/t055.py" t055_kernel.render
  IO.FS.writeFile "../generated/t082.py" t082_kernel.render
