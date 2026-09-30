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

-- t090: a chain of 2 stage(s), 4 input buffer(s)
--   fused <function leaky_relu at 0x7989a1bad620> into stage 0; fused <built-in method clamp of type object at 0x798a1d2a5640> into stage 1; fused <built-in function gelu> into stage 1
def t090_sizes : List Nat := [220430336, 220430336]
def t090_sz : Sizes := Sizes.ofList 4 t090_sizes
theorem t090_sz_pos : ∀ b n, t090_sz b = some n → 0 < n :=
  Sizes.ofList_pos (by decide)

def t090_s0_g : GenRed :=
  { nout := 220430336, K := 216
  , offs := (IE.split 4 (IE.sparse [(0, (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 3444224)) (IE.lit 8)) (IE.divi IE.rk (IE.lit 27))) (IE.lit 16)) (IE.add (IE.modi (IE.divi (IE.pid 0) (IE.lit 3844)) (IE.lit 14)) (IE.modi (IE.divi IE.rk (IE.lit 9)) (IE.lit 3)))) (IE.lit 64)) (IE.add (IE.modi (IE.divi (IE.pid 0) (IE.lit 62)) (IE.lit 62)) (IE.modi (IE.divi IE.rk (IE.lit 3)) (IE.lit 3)))) (IE.lit 64)) (IE.add (IE.modi (IE.pid 0) (IE.lit 62)) (IE.modi IE.rk (IE.lit 3))))), (1, (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 53816)) (IE.lit 64)) (IE.lit 8)) (IE.divi IE.rk (IE.lit 27))) (IE.lit 3)) (IE.modi (IE.divi IE.rk (IE.lit 9)) (IE.lit 3))) (IE.lit 3)) (IE.modi (IE.divi IE.rk (IE.lit 3)) (IE.lit 3))) (IE.lit 3)) (IE.modi IE.rk (IE.lit 3))))]) (IE.sparse []))
  , inRange := (BE.and (BE.and (BE.cmp .lt (IE.add (IE.modi (IE.divi (IE.pid 0) (IE.lit 3844)) (IE.lit 14)) (IE.modi (IE.divi IE.rk (IE.lit 9)) (IE.lit 3))) (IE.lit 16)) (BE.cmp .lt (IE.add (IE.modi (IE.divi (IE.pid 0) (IE.lit 62)) (IE.lit 62)) (IE.modi (IE.divi IE.rk (IE.lit 3)) (IE.lit 3))) (IE.lit 64))) (BE.cmp .lt (IE.add (IE.modi (IE.pid 0) (IE.lit 62)) (IE.modi IE.rk (IE.lit 3))) (IE.lit 64)))
  , body := (SE.bin .mul (SE.inp 0) (SE.inp 1))
  , postOffs := (IE.split 4 (IE.sparse [(2, (IE.modi (IE.divi (IE.pid 0) (IE.lit 53816)) (IE.lit 64)))]) (IE.sparse []))
  , post := (SE.selLe (SE.bin .add (SE.inp 0) (SE.inp 3)) (SE.lit false 0 1) (SE.bin .mul (SE.lit false 1 5) (SE.bin .add (SE.inp 0) (SE.inp 3))) (SE.bin .add (SE.inp 0) (SE.inp 3)))
  , outGuard := BE.tt
  , nInp := 5, idxSlot := 1048576 }
def t090_s0_block : Nat := 128
def t090_s0_nkb : Nat := 2

theorem t090_s0_wf : t090_s0_g.Wf :=
  { offs_ok := IE.qkOnly_split (IE.qkOnly_sparse _ (by decide)) (IE.qkOnly_sparse _ (by decide))
  , post_ok := IE.qkOnly_split (IE.qkOnly_sparse _ (by decide)) (IE.qkOnly_sparse _ (by decide))
  , range_ok := by decide
  , guard_ok := by decide }

theorem t090_s0_impl {α : Type} [ExactScalar α] :
    Implements (t090_s0_g.prog t090_s0_block t090_s0_nkb) (t090_s0_g.spec (α := α)) :=
  GenRed.prog_implements t090_s0_g t090_s0_block t090_s0_nkb t090_s0_wf (by decide) (by decide)

def t090_s1_g : GenRed :=
  { nout := 220430336, K := 1
  , offs := (IE.split 4 (IE.sparse [(3, (IE.modi (IE.divi (IE.pid 0) (IE.lit 53816)) (IE.lit 64)))]) (IE.sparse [(4, (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 3444224)) (IE.lit 64)) (IE.modi (IE.divi (IE.pid 0) (IE.lit 53816)) (IE.lit 64))) (IE.lit 14)) (IE.modi (IE.divi (IE.pid 0) (IE.lit 3844)) (IE.lit 14))) (IE.lit 62)) (IE.modi (IE.divi (IE.pid 0) (IE.lit 62)) (IE.lit 62))) (IE.lit 62)) (IE.modi (IE.pid 0) (IE.lit 62))))]))
  , inRange := BE.tt
  , body := (SE.bin .add (SE.inp 4) (SE.inp 3))
  , postOffs := (IE.split 4 (IE.sparse []) (IE.sparse []))
  , post := (SE.bin .mul (SE.bin .mul (SE.lit false 1 2) (SE.bin .min (SE.bin .max (SE.inp 0) (SE.lit true 1 1)) (SE.lit false 1 1))) (SE.bin .add (SE.lit false 1 1) (SE.un .erf (SE.bin .mul (SE.bin .min (SE.bin .max (SE.inp 0) (SE.lit true 1 1)) (SE.lit false 1 1)) (SE.recip (SE.un .sqrt (SE.lit false 2 1)))))))
  , outGuard := BE.tt
  , nInp := 6, idxSlot := 1048576 }
def t090_s1_block : Nat := 1
def t090_s1_nkb : Nat := 1

theorem t090_s1_wf : t090_s1_g.Wf :=
  { offs_ok := IE.qkOnly_split (IE.qkOnly_sparse _ (by decide)) (IE.qkOnly_sparse _ (by decide))
  , post_ok := IE.qkOnly_split (IE.qkOnly_sparse _ (by decide)) (IE.qkOnly_sparse _ (by decide))
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
      have hb : 4 ≤ b := Sizes.ofList_le hn
      have hz : t090_s0_g.offs b = IE.lit 0 := by
        simp [t090_s0_g, IE.split_ge hb, IE.sparse]
      rw [hz]
      exact t090_sz_pos b nn hn)
    (fun b nn hn q hq => by
      have hb : 4 ≤ b := Sizes.ofList_le hn
      have hz : t090_s0_g.postOffs b = IE.lit 0 := by
        simp [t090_s0_g, IE.split_ge hb, IE.sparse]
      rw [hz]
      exact t090_sz_pos b nn hn)

/-- Stage 1 reads no intermediate past what was written there. -/
theorem t090_s1_loc {α : Type} [ExactScalar α] :
    SpecLocal t090_sz (t090_s1_g.spec (α := α)) :=
  GenRed.specLocal t090_s1_g t090_sz
    (fun b nn hn q kk hq hk => by
      by_cases h4 : b = 4
      · subst h4
        have hs : nn = 220430336 :=
          Sizes.ofList_some (by decide) (by decide) hn
        subst hs
        exact (bound_pack (A := 3555328) (B := 62) (bound_pack (A := 57344) (B := 62) (bound_pack (A := 4096) (B := 14) (bound_pack (A := 64) (B := 64) (bound_div (a := 64) (d := 3444224) hq) (bound_mod (c := 64) (by decide : (0 : Nat) < 64))) (bound_mod (c := 14) (by decide : (0 : Nat) < 14))) (bound_mod (c := 62) (by decide : (0 : Nat) < 62))) (bound_mod (c := 62) (by decide : (0 : Nat) < 62)))
      have hb : 4 ≤ b := Sizes.ofList_le hn
      have hz : t090_s1_g.offs b = IE.lit 0 := by
        simp [t090_s1_g, IE.split_ge hb, IE.sparse, h4]
      rw [hz]
      exact t090_sz_pos b nn hn)
    (fun b nn hn q hq => by
      have hb : 4 ≤ b := Sizes.ofList_le hn
      have hz : t090_s1_g.postOffs b = IE.lit 0 := by
        simp [t090_s1_g, IE.split_ge hb, IE.sparse]
      rw [hz]
      exact t090_sz_pos b nn hn)

def t090_chain (α : Type) [ExactScalar α] : List (Stage α) := [⟨t090_s0_g.prog t090_s0_block t090_s0_nkb, t090_s0_g.spec (α := α), 4⟩, ⟨t090_s1_g.prog t090_s1_block t090_s1_nkb, t090_s1_g.spec (α := α), 5⟩]

theorem t090_imp {α : Type} [ExactScalar α] :
    ∀ st ∈ t090_chain α, Implements st.prog st.spec :=
  List.forall_mem_cons.mpr ⟨t090_s0_impl,
  List.forall_mem_cons.mpr ⟨t090_s1_impl,
  List.forall_mem_nil _⟩⟩

theorem t090_szok {α : Type} [ExactScalar α] :
    ∀ st ∈ t090_chain α, t090_sz st.out = some st.spec.outSize :=
  List.forall_mem_cons.mpr ⟨rfl,
  List.forall_mem_cons.mpr ⟨rfl,
  List.forall_mem_nil _⟩⟩

theorem t090_loc {α : Type} [ExactScalar α] :
    ∀ st ∈ t090_chain α, SpecLocal t090_sz st.spec :=
  List.forall_mem_cons.mpr ⟨t090_s0_loc,
  List.forall_mem_cons.mpr ⟨t090_s1_loc,
  List.forall_mem_nil _⟩⟩

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

def main : IO Unit := do
  IO.FS.writeFile "../generated/t090.py" t090_kernel.render
