/-
  GENERATED FILE -- do not edit.

  Written by verified_kernel.vk.compile. Each task below carries a
  `theorem` instantiating its family's correctness theorem at the exact
  numbers the generator chose. `lake build` checking this file is what
  makes the corresponding kernel in generated/ a verified kernel.
-/
import VerifiedKernel

open VerifiedKernel

-- t090: a chain of 2 stage(s), 4 input buffer(s)
--   fused <function leaky_relu at 0x7a682a1b1620> into stage 0; fused <built-in method clamp of type object at 0x7a68a58a5640> into stage 1; fused <built-in function gelu> into stage 1
def t090_sz : Sizes
  | 4 => some 220430336
  | 5 => some 220430336
  | _ => none

def t090_s0_g : GenRed :=
  { nout := 220430336, K := 216
  , offs := fun b => ([(IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 3444224)) (IE.lit 8)) (IE.divi IE.rk (IE.lit 27))) (IE.lit 16)) (IE.add (IE.modi (IE.divi (IE.pid 0) (IE.lit 3844)) (IE.lit 14)) (IE.modi (IE.divi IE.rk (IE.lit 9)) (IE.lit 3)))) (IE.lit 64)) (IE.add (IE.modi (IE.divi (IE.pid 0) (IE.lit 62)) (IE.lit 62)) (IE.modi (IE.divi IE.rk (IE.lit 3)) (IE.lit 3)))) (IE.lit 64)) (IE.add (IE.modi (IE.pid 0) (IE.lit 62)) (IE.modi IE.rk (IE.lit 3)))), (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 53816)) (IE.lit 64)) (IE.lit 8)) (IE.divi IE.rk (IE.lit 27))) (IE.lit 3)) (IE.modi (IE.divi IE.rk (IE.lit 9)) (IE.lit 3))) (IE.lit 3)) (IE.modi (IE.divi IE.rk (IE.lit 3)) (IE.lit 3))) (IE.lit 3)) (IE.modi IE.rk (IE.lit 3))), (IE.lit 0), (IE.lit 0), (IE.lit 0)]).getD b (IE.lit 0)
  , inRange := (BE.and (BE.and (BE.cmp .lt (IE.add (IE.modi (IE.divi (IE.pid 0) (IE.lit 3844)) (IE.lit 14)) (IE.modi (IE.divi IE.rk (IE.lit 9)) (IE.lit 3))) (IE.lit 16)) (BE.cmp .lt (IE.add (IE.modi (IE.divi (IE.pid 0) (IE.lit 62)) (IE.lit 62)) (IE.modi (IE.divi IE.rk (IE.lit 3)) (IE.lit 3))) (IE.lit 64))) (BE.cmp .lt (IE.add (IE.modi (IE.pid 0) (IE.lit 62)) (IE.modi IE.rk (IE.lit 3))) (IE.lit 64)))
  , body := (SE.bin .mul (SE.inp 0) (SE.inp 1))
  , postOffs := fun b => ([(IE.lit 0), (IE.lit 0), (IE.modi (IE.divi (IE.pid 0) (IE.lit 53816)) (IE.lit 64)), (IE.lit 0), (IE.lit 0)]).getD b (IE.lit 0)
  , post := (SE.selLe (SE.bin .add (SE.inp 0) (SE.inp 3)) (SE.lit false 0 1) (SE.bin .mul (SE.lit false 1 5) (SE.bin .add (SE.inp 0) (SE.inp 3))) (SE.bin .add (SE.inp 0) (SE.inp 3)))
  , outGuard := BE.tt
  , nInp := 5, idxSlot := 1048576 }
def t090_s0_block : Nat := 128
def t090_s0_nkb : Nat := 2

theorem t090_s0_wf : t090_s0_g.Wf :=
  { offs_ok := IE.qkOnly_getD _ (by decide)
  , post_ok := IE.qkOnly_getD _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

theorem t090_s0_impl {α : Type} [ExactScalar α] :
    Implements (t090_s0_g.prog t090_s0_block t090_s0_nkb) (t090_s0_g.spec (α := α)) :=
  GenRed.prog_implements t090_s0_g t090_s0_block t090_s0_nkb t090_s0_wf (by decide) (by decide)

def t090_s1_g : GenRed :=
  { nout := 220430336, K := 1
  , offs := fun b => ([(IE.lit 0), (IE.lit 0), (IE.lit 0), (IE.modi (IE.divi (IE.pid 0) (IE.lit 53816)) (IE.lit 64)), (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 3444224)) (IE.lit 64)) (IE.modi (IE.divi (IE.pid 0) (IE.lit 53816)) (IE.lit 64))) (IE.lit 14)) (IE.modi (IE.divi (IE.pid 0) (IE.lit 3844)) (IE.lit 14))) (IE.lit 62)) (IE.modi (IE.divi (IE.pid 0) (IE.lit 62)) (IE.lit 62))) (IE.lit 62)) (IE.modi (IE.pid 0) (IE.lit 62))), (IE.lit 0)]).getD b (IE.lit 0)
  , inRange := BE.tt
  , body := (SE.bin .add (SE.inp 4) (SE.inp 3))
  , postOffs := fun b => ([(IE.lit 0), (IE.lit 0), (IE.lit 0), (IE.lit 0), (IE.lit 0), (IE.lit 0)]).getD b (IE.lit 0)
  , post := (SE.bin .mul (SE.bin .mul (SE.lit false 1 2) (SE.bin .min (SE.bin .max (SE.inp 0) (SE.lit true 1 1)) (SE.lit false 1 1))) (SE.bin .add (SE.lit false 1 1) (SE.un .erf (SE.bin .mul (SE.bin .min (SE.bin .max (SE.inp 0) (SE.lit true 1 1)) (SE.lit false 1 1)) (SE.recip (SE.un .sqrt (SE.lit false 2 1)))))))
  , outGuard := BE.tt
  , nInp := 6, idxSlot := 1048576 }
def t090_s1_block : Nat := 1
def t090_s1_nkb : Nat := 1

theorem t090_s1_wf : t090_s1_g.Wf :=
  { offs_ok := IE.qkOnly_getD _ (by decide)
  , post_ok := IE.qkOnly_getD _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

theorem t090_s1_impl {α : Type} [ExactScalar α] :
    Implements (t090_s1_g.prog t090_s1_block t090_s1_nkb) (t090_s1_g.spec (α := α)) :=
  GenRed.prog_implements t090_s1_g t090_s1_block t090_s1_nkb t090_s1_wf (by decide) (by decide)

/-- Stage 0 reads no intermediate past what was written there. -/
theorem t090_s0_loc {α : Type} [ExactScalar α] :
    SpecLocal t090_sz (t090_s0_g.spec (α := α)) :=
  GenRed.specLocal t090_s0_g t090_sz
    (fun b nn hn q kk hq hk => by
      match b, hn with
      | 0, hn => simp [t090_sz] at hn
      | 1, hn => simp [t090_sz] at hn
      | 2, hn => simp [t090_sz] at hn
      | 3, hn => simp [t090_sz] at hn
      | 4, hn => simp [t090_sz] at hn; subst hn; exact (by decide : (0 : Nat) < 220430336)
      | 5, hn => simp [t090_sz] at hn; subst hn; exact (by decide : (0 : Nat) < 220430336)
      | (_ + 6), hn => simp [t090_sz] at hn)
    (fun b nn hn q hq => by
      match b, hn with
      | 0, hn => simp [t090_sz] at hn
      | 1, hn => simp [t090_sz] at hn
      | 2, hn => simp [t090_sz] at hn
      | 3, hn => simp [t090_sz] at hn
      | 4, hn => simp [t090_sz] at hn; subst hn; exact (by decide : (0 : Nat) < 220430336)
      | 5, hn => simp [t090_sz] at hn; subst hn; exact (by decide : (0 : Nat) < 220430336)
      | (_ + 6), hn => simp [t090_sz] at hn)

/-- Stage 1 reads no intermediate past what was written there. -/
theorem t090_s1_loc {α : Type} [ExactScalar α] :
    SpecLocal t090_sz (t090_s1_g.spec (α := α)) :=
  GenRed.specLocal t090_s1_g t090_sz
    (fun b nn hn q kk hq hk => by
      match b, hn with
      | 0, hn => simp [t090_sz] at hn
      | 1, hn => simp [t090_sz] at hn
      | 2, hn => simp [t090_sz] at hn
      | 3, hn => simp [t090_sz] at hn
      | 4, hn => simp [t090_sz] at hn; subst hn; exact (bound_pack (A := 3555328) (B := 62) (bound_pack (A := 57344) (B := 62) (bound_pack (A := 4096) (B := 14) (bound_pack (A := 64) (B := 64) (bound_div (a := 64) (d := 3444224) hq) (bound_mod (c := 64) (by decide : (0 : Nat) < 64))) (bound_mod (c := 14) (by decide : (0 : Nat) < 14))) (bound_mod (c := 62) (by decide : (0 : Nat) < 62))) (bound_mod (c := 62) (by decide : (0 : Nat) < 62)))
      | 5, hn => simp [t090_sz] at hn; subst hn; exact (by decide : (0 : Nat) < 220430336)
      | (_ + 6), hn => simp [t090_sz] at hn)
    (fun b nn hn q hq => by
      match b, hn with
      | 0, hn => simp [t090_sz] at hn
      | 1, hn => simp [t090_sz] at hn
      | 2, hn => simp [t090_sz] at hn
      | 3, hn => simp [t090_sz] at hn
      | 4, hn => simp [t090_sz] at hn; subst hn; exact (by decide : (0 : Nat) < 220430336)
      | 5, hn => simp [t090_sz] at hn; subst hn; exact (by decide : (0 : Nat) < 220430336)
      | (_ + 6), hn => simp [t090_sz] at hn)

def t090_chain (α : Type) [ExactScalar α] : List (Stage α) := [⟨t090_s0_g.prog t090_s0_block t090_s0_nkb, t090_s0_g.spec (α := α), 4⟩, ⟨t090_s1_g.prog t090_s1_block t090_s1_nkb, t090_s1_g.spec (α := α), 5⟩]

theorem t090_imp {α : Type} [ExactScalar α] :
    ∀ st ∈ t090_chain α, Implements st.prog st.spec := by
  intro st hst
  simp only [t090_chain, List.mem_cons, List.not_mem_nil, or_false] at hst
  rcases hst with rfl | rfl
  · exact t090_s0_impl
  · exact t090_s1_impl

theorem t090_szok {α : Type} [ExactScalar α] :
    ∀ st ∈ t090_chain α, t090_sz st.out = some st.spec.outSize := by
  intro st hst
  simp only [t090_chain, List.mem_cons, List.not_mem_nil, or_false] at hst
  rcases hst with rfl | rfl
  · rfl
  · rfl

theorem t090_loc {α : Type} [ExactScalar α] :
    ∀ st ∈ t090_chain α, SpecLocal t090_sz st.spec := by
  intro st hst
  simp only [t090_chain, List.mem_cons, List.not_mem_nil, or_false] at hst
  rcases hst with rfl | rfl
  · exact t090_s0_loc
  · exact t090_s1_loc

/-- Correctness certificate for t090: the whole chain. -/
theorem t090_correct {α : Type} [ExactScalar α] :
    ∀ (f : Nat → Buf α) (m : Mem α),
      Compat (sizesAfter (t090_chain α) emptySizes)
        (runStages (t090_chain α) f m) (specStages (t090_chain α) f) :=
  fun f m => stages_correct t090_sz (t090_chain α) emptySizes f f m
    (Compat.refl _ _) (emptySizes_sub t090_sz)
    t090_szok t090_imp t090_loc

def t090_s0_kernel : ReduceKernel :=
  { name := "t090_s0", arity := 4, block := t090_s0_block, nkb := t090_s0_nkb, nout := 220430336, init := FE.zeroC, step := t090_s0_g.step t090_s0_block, stored := t090_s0_g.stored t090_s0_block }
def t090_s1_kernel : ReduceKernel :=
  { name := "t090_s1", arity := 5, block := t090_s1_block, nkb := t090_s1_nkb, nout := 220430336, init := FE.zeroC, step := t090_s1_g.step t090_s1_block, stored := t090_s1_g.stored t090_s1_block }
def t090_kernel : ChainKernel :=
  { name := "t090", arity := 4, sizes := [220430336, 220430336],
    stages := [t090_s0_kernel, t090_s1_kernel] }

-- t100: a chain of 1 stage(s), 3 input buffer(s)
--   fused <built-in method clamp of type object at 0x7a68a58a5640> into stage 0; fused <built-in function truediv> into stage 0
def t100_sz : Sizes
  | 3 => some 217177600
  | _ => none

def t100_s0_g : GenRed :=
  { nout := 217177600, K := 1728
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
      | 3, hn => simp [t100_sz] at hn; subst hn; exact (by decide : (0 : Nat) < 217177600)
      | (_ + 4), hn => simp [t100_sz] at hn)
    (fun b nn hn q hq => by
      match b, hn with
      | 0, hn => simp [t100_sz] at hn
      | 1, hn => simp [t100_sz] at hn
      | 2, hn => simp [t100_sz] at hn
      | 3, hn => simp [t100_sz] at hn; subst hn; exact (by decide : (0 : Nat) < 217177600)
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
  { name := "t100_s0", arity := 3, block := t100_s0_block, nkb := t100_s0_nkb, nout := 217177600, init := FE.zeroC, step := t100_s0_g.step t100_s0_block, stored := t100_s0_g.stored t100_s0_block }
def t100_kernel : ChainKernel :=
  { name := "t100", arity := 3, sizes := [217177600],
    stages := [t100_s0_kernel] }

def main : IO Unit := do
  IO.FS.writeFile "../generated/t090.py" t090_kernel.render
  IO.FS.writeFile "../generated/t100.py" t100_kernel.render
