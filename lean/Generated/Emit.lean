/-
  GENERATED FILE -- do not edit.

  Written by verified_kernel.vk.compile. Each task below carries a
  `theorem` instantiating its family's correctness theorem at the exact
  numbers the generator chose. `lake build` checking this file is what
  makes the corresponding kernel in generated/ a verified kernel.
-/
import VerifiedKernel

open VerifiedKernel

-- t012: a chain of 1 stage(s), 3 input buffer(s)
--   fused <built-in function mul> into stage 0; fused leaky_relu into stage 0
def t012_sz : Sizes
  | 3 => some 8388608
  | _ => none

def t012_s0_g : GenRed :=
  { nout := 8388608, K := 8192
  , offs := fun b => ([(IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 8192)) (IE.lit 8192)) IE.rk), (IE.add (IE.mul (IE.modi (IE.pid 0) (IE.lit 8192)) (IE.lit 8192)) IE.rk), (IE.lit 0), (IE.lit 0)]).getD b (IE.lit 0)
  , inRange := BE.tt
  , body := (SE.bin .mul (SE.inp 0) (SE.inp 1))
  , postOffs := fun b => ([(IE.lit 0), (IE.lit 0), (IE.modi (IE.pid 0) (IE.lit 8192)), (IE.lit 0)]).getD b (IE.lit 0)
  , post := (SE.selLe (SE.bin .mul (SE.bin .add (SE.inp 0) (SE.inp 3)) (SE.lit false 2 1)) (SE.lit false 0 1) (SE.bin .mul (SE.lit false 1 10) (SE.bin .mul (SE.bin .add (SE.inp 0) (SE.inp 3)) (SE.lit false 2 1))) (SE.bin .mul (SE.bin .add (SE.inp 0) (SE.inp 3)) (SE.lit false 2 1)))
  , outGuard := BE.tt
  , nInp := 4, idxSlot := 1048576 }
def t012_s0_block : Nat := 1024
def t012_s0_nkb : Nat := 8

theorem t012_s0_wf : t012_s0_g.Wf :=
  { offs_ok := IE.qkOnly_getD _ (by decide)
  , post_ok := IE.qkOnly_getD _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

theorem t012_s0_impl {α : Type} [ExactScalar α] :
    Implements (t012_s0_g.prog t012_s0_block t012_s0_nkb) (t012_s0_g.spec (α := α)) :=
  GenRed.prog_implements t012_s0_g t012_s0_block t012_s0_nkb t012_s0_wf (by decide) (by decide)

/-- Stage 0 reads no intermediate past what was written there. -/
theorem t012_s0_loc {α : Type} [ExactScalar α] :
    SpecLocal t012_sz (t012_s0_g.spec (α := α)) :=
  GenRed.specLocal t012_s0_g t012_sz
    (fun b nn hn q kk hq hk => by
      match b, hn with
      | 0, hn => simp [t012_sz] at hn
      | 1, hn => simp [t012_sz] at hn
      | 2, hn => simp [t012_sz] at hn
      | 3, hn => simp [t012_sz] at hn; subst hn; exact (by decide : (0 : Nat) < 8388608)
      | (_ + 4), hn => simp [t012_sz] at hn)
    (fun b nn hn q hq => by
      match b, hn with
      | 0, hn => simp [t012_sz] at hn
      | 1, hn => simp [t012_sz] at hn
      | 2, hn => simp [t012_sz] at hn
      | 3, hn => simp [t012_sz] at hn; subst hn; exact (by decide : (0 : Nat) < 8388608)
      | (_ + 4), hn => simp [t012_sz] at hn)

def t012_chain (α : Type) [ExactScalar α] : List (Stage α) := [⟨t012_s0_g.prog t012_s0_block t012_s0_nkb, t012_s0_g.spec (α := α), 3⟩]

theorem t012_imp {α : Type} [ExactScalar α] :
    ∀ st ∈ t012_chain α, Implements st.prog st.spec := by
  intro st hst
  simp only [t012_chain, List.mem_cons, List.not_mem_nil, or_false] at hst
  rcases hst with rfl
  · exact t012_s0_impl

theorem t012_szok {α : Type} [ExactScalar α] :
    ∀ st ∈ t012_chain α, t012_sz st.out = some st.spec.outSize := by
  intro st hst
  simp only [t012_chain, List.mem_cons, List.not_mem_nil, or_false] at hst
  rcases hst with rfl
  · rfl

theorem t012_loc {α : Type} [ExactScalar α] :
    ∀ st ∈ t012_chain α, SpecLocal t012_sz st.spec := by
  intro st hst
  simp only [t012_chain, List.mem_cons, List.not_mem_nil, or_false] at hst
  rcases hst with rfl
  · exact t012_s0_loc

/-- Correctness certificate for t012: the whole chain. -/
theorem t012_correct {α : Type} [ExactScalar α] :
    ∀ (f : Nat → Buf α) (m : Mem α),
      Compat (sizesAfter (t012_chain α) emptySizes)
        (runStages (t012_chain α) f m) (specStages (t012_chain α) f) :=
  fun f m => stages_correct t012_sz (t012_chain α) emptySizes f f m
    (Compat.refl _ _) (emptySizes_sub t012_sz)
    t012_szok t012_imp t012_loc

def t012_s0_kernel : ReduceKernel :=
  { name := "t012_s0", arity := 3, block := t012_s0_block, nkb := t012_s0_nkb, nout := 8388608, init := FE.zeroC, step := t012_s0_g.step t012_s0_block, stored := t012_s0_g.stored t012_s0_block }
def t012_kernel : ChainKernel :=
  { name := "t012", arity := 3, sizes := [8388608],
    stages := [t012_s0_kernel] }

-- t100: a chain of 1 stage(s), 3 input buffer(s)
--   fused <built-in method clamp of type object at 0x7aa48d8a5640> into stage 0; fused <built-in function truediv> into stage 0
def t100_sz : Sizes
  | 3 => some 434355200
  | _ => none

def t100_s0_g : GenRed :=
  { nout := 434355200, K := 1728
  , offs := fun b => ([(IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 54294400)) (IE.lit 64)) (IE.add (IE.mul (IE.divi (IE.modi (IE.divi (IE.pid 0) (IE.lit 424175)) (IE.lit 128)) (IE.lit 128)) (IE.lit 64)) (IE.divi IE.rk (IE.lit 27)))) (IE.lit 24)) (IE.divi (IE.sub (IE.add (IE.modi (IE.divi (IE.pid 0) (IE.lit 9025)) (IE.lit 47)) (IE.lit 1)) (IE.modi (IE.divi IE.rk (IE.lit 9)) (IE.lit 3))) (IE.lit 2))) (IE.lit 48)) (IE.divi (IE.sub (IE.add (IE.modi (IE.divi (IE.pid 0) (IE.lit 95)) (IE.lit 95)) (IE.lit 1)) (IE.modi (IE.divi IE.rk (IE.lit 3)) (IE.lit 3))) (IE.lit 2))) (IE.lit 48)) (IE.divi (IE.sub (IE.add (IE.modi (IE.pid 0) (IE.lit 95)) (IE.lit 1)) (IE.modi IE.rk (IE.lit 3))) (IE.lit 2))), (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.modi (IE.divi (IE.pid 0) (IE.lit 424175)) (IE.lit 128)) (IE.lit 128)) (IE.lit 64)) (IE.divi IE.rk (IE.lit 27))) (IE.lit 128)) (IE.modi (IE.modi (IE.divi (IE.pid 0) (IE.lit 424175)) (IE.lit 128)) (IE.lit 128))) (IE.lit 3)) (IE.modi (IE.divi IE.rk (IE.lit 9)) (IE.lit 3))) (IE.lit 3)) (IE.modi (IE.divi IE.rk (IE.lit 3)) (IE.lit 3))) (IE.lit 3)) (IE.modi IE.rk (IE.lit 3))), (IE.lit 0), (IE.lit 0)]).getD b (IE.lit 0)
  , inRange := (BE.and (BE.and (BE.and (BE.and (BE.and (BE.and (BE.and (BE.and (BE.cmp .le (IE.modi (IE.divi IE.rk (IE.lit 9)) (IE.lit 3)) (IE.add (IE.modi (IE.divi (IE.pid 0) (IE.lit 9025)) (IE.lit 47)) (IE.lit 1))) (BE.cmp .eq (IE.modi (IE.sub (IE.add (IE.modi (IE.divi (IE.pid 0) (IE.lit 9025)) (IE.lit 47)) (IE.lit 1)) (IE.modi (IE.divi IE.rk (IE.lit 9)) (IE.lit 3))) (IE.lit 2)) (IE.lit 0))) (BE.cmp .lt (IE.divi (IE.sub (IE.add (IE.modi (IE.divi (IE.pid 0) (IE.lit 9025)) (IE.lit 47)) (IE.lit 1)) (IE.modi (IE.divi IE.rk (IE.lit 9)) (IE.lit 3))) (IE.lit 2)) (IE.lit 24))) (BE.cmp .le (IE.modi (IE.divi IE.rk (IE.lit 3)) (IE.lit 3)) (IE.add (IE.modi (IE.divi (IE.pid 0) (IE.lit 95)) (IE.lit 95)) (IE.lit 1)))) (BE.cmp .eq (IE.modi (IE.sub (IE.add (IE.modi (IE.divi (IE.pid 0) (IE.lit 95)) (IE.lit 95)) (IE.lit 1)) (IE.modi (IE.divi IE.rk (IE.lit 3)) (IE.lit 3))) (IE.lit 2)) (IE.lit 0))) (BE.cmp .lt (IE.divi (IE.sub (IE.add (IE.modi (IE.divi (IE.pid 0) (IE.lit 95)) (IE.lit 95)) (IE.lit 1)) (IE.modi (IE.divi IE.rk (IE.lit 3)) (IE.lit 3))) (IE.lit 2)) (IE.lit 48))) (BE.cmp .le (IE.modi IE.rk (IE.lit 3)) (IE.add (IE.modi (IE.pid 0) (IE.lit 95)) (IE.lit 1)))) (BE.cmp .eq (IE.modi (IE.sub (IE.add (IE.modi (IE.pid 0) (IE.lit 95)) (IE.lit 1)) (IE.modi IE.rk (IE.lit 3))) (IE.lit 2)) (IE.lit 0))) (BE.cmp .lt (IE.divi (IE.sub (IE.add (IE.modi (IE.pid 0) (IE.lit 95)) (IE.lit 1)) (IE.modi IE.rk (IE.lit 3))) (IE.lit 2)) (IE.lit 48)))
  , body := (SE.bin .mul (SE.inp 0) (SE.inp 1))
  , postOffs := fun b => ([(IE.lit 0), (IE.lit 0), (IE.modi (IE.divi (IE.pid 0) (IE.lit 424175)) (IE.lit 128)), (IE.lit 0)]).getD b (IE.lit 0)
  , post := (SE.bin .div (SE.bin .max (SE.bin .add (SE.inp 0) (SE.inp 3)) (SE.lit true 1 1)) (SE.lit false 2 1))
  , outGuard := BE.tt
  , nInp := 4, idxSlot := 1048576 }
def t100_s0_block : Nat := 1024
def t100_s0_nkb : Nat := 2

theorem t100_s0_wf : t100_s0_g.Wf :=
  { offs_ok := IE.qkOnly_getD _ (by decide)
  , post_ok := IE.qkOnly_getD _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

theorem t100_s0_impl {α : Type} [ExactScalar α] :
    Implements (t100_s0_g.prog t100_s0_block t100_s0_nkb) (t100_s0_g.spec (α := α)) :=
  GenRed.prog_implements t100_s0_g t100_s0_block t100_s0_nkb t100_s0_wf (by decide) (by decide)

/-- Stage 0 reads no intermediate past what was written there. -/
theorem t100_s0_loc {α : Type} [ExactScalar α] :
    SpecLocal t100_sz (t100_s0_g.spec (α := α)) :=
  GenRed.specLocal t100_s0_g t100_sz
    (fun b nn hn q kk hq hk => by
      match b, hn with
      | 0, hn => simp [t100_sz] at hn
      | 1, hn => simp [t100_sz] at hn
      | 2, hn => simp [t100_sz] at hn
      | 3, hn => simp [t100_sz] at hn; subst hn; exact (by decide : (0 : Nat) < 434355200)
      | (_ + 4), hn => simp [t100_sz] at hn)
    (fun b nn hn q hq => by
      match b, hn with
      | 0, hn => simp [t100_sz] at hn
      | 1, hn => simp [t100_sz] at hn
      | 2, hn => simp [t100_sz] at hn
      | 3, hn => simp [t100_sz] at hn; subst hn; exact (by decide : (0 : Nat) < 434355200)
      | (_ + 4), hn => simp [t100_sz] at hn)

def t100_chain (α : Type) [ExactScalar α] : List (Stage α) := [⟨t100_s0_g.prog t100_s0_block t100_s0_nkb, t100_s0_g.spec (α := α), 3⟩]

theorem t100_imp {α : Type} [ExactScalar α] :
    ∀ st ∈ t100_chain α, Implements st.prog st.spec := by
  intro st hst
  simp only [t100_chain, List.mem_cons, List.not_mem_nil, or_false] at hst
  rcases hst with rfl
  · exact t100_s0_impl

theorem t100_szok {α : Type} [ExactScalar α] :
    ∀ st ∈ t100_chain α, t100_sz st.out = some st.spec.outSize := by
  intro st hst
  simp only [t100_chain, List.mem_cons, List.not_mem_nil, or_false] at hst
  rcases hst with rfl
  · rfl

theorem t100_loc {α : Type} [ExactScalar α] :
    ∀ st ∈ t100_chain α, SpecLocal t100_sz st.spec := by
  intro st hst
  simp only [t100_chain, List.mem_cons, List.not_mem_nil, or_false] at hst
  rcases hst with rfl
  · exact t100_s0_loc

/-- Correctness certificate for t100: the whole chain. -/
theorem t100_correct {α : Type} [ExactScalar α] :
    ∀ (f : Nat → Buf α) (m : Mem α),
      Compat (sizesAfter (t100_chain α) emptySizes)
        (runStages (t100_chain α) f m) (specStages (t100_chain α) f) :=
  fun f m => stages_correct t100_sz (t100_chain α) emptySizes f f m
    (Compat.refl _ _) (emptySizes_sub t100_sz)
    t100_szok t100_imp t100_loc

def t100_s0_kernel : ReduceKernel :=
  { name := "t100_s0", arity := 3, block := t100_s0_block, nkb := t100_s0_nkb, nout := 434355200, init := FE.zeroC, step := t100_s0_g.step t100_s0_block, stored := t100_s0_g.stored t100_s0_block }
def t100_kernel : ChainKernel :=
  { name := "t100", arity := 3, sizes := [434355200],
    stages := [t100_s0_kernel] }

def main : IO Unit := do
  IO.FS.writeFile "../generated/t012.py" t012_kernel.render
  IO.FS.writeFile "../generated/t100.py" t100_kernel.render
