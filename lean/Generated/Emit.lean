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

-- slc0: a chain of 1 stage(s), 1 input buffer(s)
--   fused <built-in function mul> into stage 0
def slc0_sizes : List Nat := [60]
def slc0_sz : Sizes := Sizes.ofList 1 slc0_sizes
theorem slc0_sz_pos : ∀ b n, slc0_sz b = some n → 0 < n :=
  Sizes.ofList_pos (by decide)

def slc0_s0_g : GenRed :=
  { nout := 60, K := 1
  , offs := (IE.split 1 (IE.sparse [(0, (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 30)) (IE.lit 9)) (IE.add (IE.modi (IE.divi (IE.pid 0) (IE.lit 6)) (IE.lit 5)) (IE.lit 2))) (IE.lit 12)) (IE.mul (IE.modi (IE.pid 0) (IE.lit 6)) (IE.lit 2))))]) (IE.sparse []))
  , inRange := BE.tt
  , body := (SE.inp 0)
  , postOffs := (IE.split 1 (IE.sparse []) (IE.sparse []))
  , post := (SE.bin .mul (SE.inp 0) (SE.lit false 2 1))
  , outGuard := BE.tt
  , nInp := 2, idxSlot := 1048576 }
def slc0_s0_block : Nat := 1
def slc0_s0_nkb : Nat := 1

theorem slc0_s0_wf : slc0_s0_g.Wf :=
  { offs_ok := IE.qkOnly_split (IE.qkOnly_sparse _ (by decide)) (IE.qkOnly_sparse _ (by decide))
  , post_ok := IE.qkOnly_split (IE.qkOnly_sparse _ (by decide)) (IE.qkOnly_sparse _ (by decide))
  , range_ok := by decide
  , guard_ok := by decide }

theorem slc0_s0_impl {α : Type} [ExactScalar α] :
    Implements (slc0_s0_g.prog slc0_s0_block slc0_s0_nkb) (slc0_s0_g.spec (α := α)) :=
  GenRed.prog_implements slc0_s0_g slc0_s0_block slc0_s0_nkb slc0_s0_wf (by decide) (by decide)

/-- Stage 0 reads no intermediate past what was written there. -/
theorem slc0_s0_loc {α : Type} [ExactScalar α] :
    SpecLocal slc0_sz (slc0_s0_g.spec (α := α)) :=
  GenRed.specLocal slc0_s0_g slc0_sz
    (fun b nn hn q kk hq hk => by
      have hb : 1 ≤ b := Sizes.ofList_le hn
      have hz : slc0_s0_g.offs b = IE.lit 0 := by
        simp [slc0_s0_g, IE.split_ge hb, IE.sparse]
      rw [hz]
      exact slc0_sz_pos b nn hn)
    (fun b nn hn q hq => by
      have hb : 1 ≤ b := Sizes.ofList_le hn
      have hz : slc0_s0_g.postOffs b = IE.lit 0 := by
        simp [slc0_s0_g, IE.split_ge hb, IE.sparse]
      rw [hz]
      exact slc0_sz_pos b nn hn)

def slc0_chain (α : Type) [ExactScalar α] : List (Stage α) := [⟨slc0_s0_g.prog slc0_s0_block slc0_s0_nkb, slc0_s0_g.spec (α := α), 1⟩]

theorem slc0_imp {α : Type} [ExactScalar α] :
    ∀ st ∈ slc0_chain α, Implements st.prog st.spec :=
  List.forall_mem_cons.mpr ⟨slc0_s0_impl,
  List.forall_mem_nil _⟩

theorem slc0_szok {α : Type} [ExactScalar α] :
    ∀ st ∈ slc0_chain α, slc0_sz st.out = some st.spec.outSize :=
  List.forall_mem_cons.mpr ⟨rfl,
  List.forall_mem_nil _⟩

theorem slc0_loc {α : Type} [ExactScalar α] :
    ∀ st ∈ slc0_chain α, SpecLocal slc0_sz st.spec :=
  List.forall_mem_cons.mpr ⟨slc0_s0_loc,
  List.forall_mem_nil _⟩

/-- Correctness certificate for slc0: the whole chain. -/
theorem slc0_correct {α : Type} [ExactScalar α] :
    ∀ (f : Nat → Buf α) (m : Mem α),
      Compat (sizesAfter (slc0_chain α) emptySizes)
        (runStages (slc0_chain α) f m) (specStages (slc0_chain α) f) :=
  fun f m => stages_correct slc0_sz (slc0_chain α) emptySizes f f m
    (Compat.refl _ _) (emptySizes_sub slc0_sz)
    slc0_szok slc0_imp slc0_loc

def slc0_s0_kernel : ReduceKernel :=
  { name := "slc0_s0", arity := 1, block := slc0_s0_block, nkb := slc0_s0_nkb, nout := 60, init := FE.zeroC, step := slc0_s0_g.step slc0_s0_block, stored := slc0_s0_g.stored slc0_s0_block }
def slc0_kernel : ChainKernel :=
  { name := "slc0", arity := 1, sizes := [60],
    stages := [slc0_s0_kernel] }

-- slc1: a chain of 1 stage(s), 1 input buffer(s)
--   fused <built-in function add> into stage 0
def slc1_sizes : List Nat := [24]
def slc1_sz : Sizes := Sizes.ofList 1 slc1_sizes
theorem slc1_sz_pos : ∀ b n, slc1_sz b = some n → 0 < n :=
  Sizes.ofList_pos (by decide)

def slc1_s0_g : GenRed :=
  { nout := 24, K := 1
  , offs := (IE.split 1 (IE.sparse [(0, (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 12)) (IE.lit 9)) (IE.lit 3)) (IE.lit 12)) (IE.modi (IE.pid 0) (IE.lit 12))))]) (IE.sparse []))
  , inRange := BE.tt
  , body := (SE.inp 0)
  , postOffs := (IE.split 1 (IE.sparse []) (IE.sparse []))
  , post := (SE.bin .add (SE.inp 0) (SE.lit false 1 1))
  , outGuard := BE.tt
  , nInp := 2, idxSlot := 1048576 }
def slc1_s0_block : Nat := 1
def slc1_s0_nkb : Nat := 1

theorem slc1_s0_wf : slc1_s0_g.Wf :=
  { offs_ok := IE.qkOnly_split (IE.qkOnly_sparse _ (by decide)) (IE.qkOnly_sparse _ (by decide))
  , post_ok := IE.qkOnly_split (IE.qkOnly_sparse _ (by decide)) (IE.qkOnly_sparse _ (by decide))
  , range_ok := by decide
  , guard_ok := by decide }

theorem slc1_s0_impl {α : Type} [ExactScalar α] :
    Implements (slc1_s0_g.prog slc1_s0_block slc1_s0_nkb) (slc1_s0_g.spec (α := α)) :=
  GenRed.prog_implements slc1_s0_g slc1_s0_block slc1_s0_nkb slc1_s0_wf (by decide) (by decide)

/-- Stage 0 reads no intermediate past what was written there. -/
theorem slc1_s0_loc {α : Type} [ExactScalar α] :
    SpecLocal slc1_sz (slc1_s0_g.spec (α := α)) :=
  GenRed.specLocal slc1_s0_g slc1_sz
    (fun b nn hn q kk hq hk => by
      have hb : 1 ≤ b := Sizes.ofList_le hn
      have hz : slc1_s0_g.offs b = IE.lit 0 := by
        simp [slc1_s0_g, IE.split_ge hb, IE.sparse]
      rw [hz]
      exact slc1_sz_pos b nn hn)
    (fun b nn hn q hq => by
      have hb : 1 ≤ b := Sizes.ofList_le hn
      have hz : slc1_s0_g.postOffs b = IE.lit 0 := by
        simp [slc1_s0_g, IE.split_ge hb, IE.sparse]
      rw [hz]
      exact slc1_sz_pos b nn hn)

def slc1_chain (α : Type) [ExactScalar α] : List (Stage α) := [⟨slc1_s0_g.prog slc1_s0_block slc1_s0_nkb, slc1_s0_g.spec (α := α), 1⟩]

theorem slc1_imp {α : Type} [ExactScalar α] :
    ∀ st ∈ slc1_chain α, Implements st.prog st.spec :=
  List.forall_mem_cons.mpr ⟨slc1_s0_impl,
  List.forall_mem_nil _⟩

theorem slc1_szok {α : Type} [ExactScalar α] :
    ∀ st ∈ slc1_chain α, slc1_sz st.out = some st.spec.outSize :=
  List.forall_mem_cons.mpr ⟨rfl,
  List.forall_mem_nil _⟩

theorem slc1_loc {α : Type} [ExactScalar α] :
    ∀ st ∈ slc1_chain α, SpecLocal slc1_sz st.spec :=
  List.forall_mem_cons.mpr ⟨slc1_s0_loc,
  List.forall_mem_nil _⟩

/-- Correctness certificate for slc1: the whole chain. -/
theorem slc1_correct {α : Type} [ExactScalar α] :
    ∀ (f : Nat → Buf α) (m : Mem α),
      Compat (sizesAfter (slc1_chain α) emptySizes)
        (runStages (slc1_chain α) f m) (specStages (slc1_chain α) f) :=
  fun f m => stages_correct slc1_sz (slc1_chain α) emptySizes f f m
    (Compat.refl _ _) (emptySizes_sub slc1_sz)
    slc1_szok slc1_imp slc1_loc

def slc1_s0_kernel : ReduceKernel :=
  { name := "slc1_s0", arity := 1, block := slc1_s0_block, nkb := slc1_s0_nkb, nout := 24, init := FE.zeroC, step := slc1_s0_g.step slc1_s0_block, stored := slc1_s0_g.stored slc1_s0_block }
def slc1_kernel : ChainKernel :=
  { name := "slc1", arity := 1, sizes := [24],
    stages := [slc1_s0_kernel] }

-- slc2: a chain of 1 stage(s), 1 input buffer(s)
--   
def slc2_sizes : List Nat := [72]
def slc2_sz : Sizes := Sizes.ofList 1 slc2_sizes
theorem slc2_sz_pos : ∀ b n, slc2_sz b = some n → 0 < n :=
  Sizes.ofList_pos (by decide)

def slc2_s0_g : GenRed :=
  { nout := 72, K := 1
  , offs := (IE.split 1 (IE.sparse [(0, (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 36)) (IE.lit 9)) (IE.modi (IE.divi (IE.pid 0) (IE.lit 4)) (IE.lit 9))) (IE.lit 12)) (IE.add (IE.modi (IE.pid 0) (IE.lit 4)) (IE.lit 1))))]) (IE.sparse []))
  , inRange := BE.tt
  , body := (SE.inp 0)
  , postOffs := (IE.split 1 (IE.sparse []) (IE.sparse []))
  , post := (SE.inp 0)
  , outGuard := BE.tt
  , nInp := 2, idxSlot := 1048576 }
def slc2_s0_block : Nat := 1
def slc2_s0_nkb : Nat := 1

theorem slc2_s0_wf : slc2_s0_g.Wf :=
  { offs_ok := IE.qkOnly_split (IE.qkOnly_sparse _ (by decide)) (IE.qkOnly_sparse _ (by decide))
  , post_ok := IE.qkOnly_split (IE.qkOnly_sparse _ (by decide)) (IE.qkOnly_sparse _ (by decide))
  , range_ok := by decide
  , guard_ok := by decide }

theorem slc2_s0_impl {α : Type} [ExactScalar α] :
    Implements (slc2_s0_g.prog slc2_s0_block slc2_s0_nkb) (slc2_s0_g.spec (α := α)) :=
  GenRed.prog_implements slc2_s0_g slc2_s0_block slc2_s0_nkb slc2_s0_wf (by decide) (by decide)

/-- Stage 0 reads no intermediate past what was written there. -/
theorem slc2_s0_loc {α : Type} [ExactScalar α] :
    SpecLocal slc2_sz (slc2_s0_g.spec (α := α)) :=
  GenRed.specLocal slc2_s0_g slc2_sz
    (fun b nn hn q kk hq hk => by
      have hb : 1 ≤ b := Sizes.ofList_le hn
      have hz : slc2_s0_g.offs b = IE.lit 0 := by
        simp [slc2_s0_g, IE.split_ge hb, IE.sparse]
      rw [hz]
      exact slc2_sz_pos b nn hn)
    (fun b nn hn q hq => by
      have hb : 1 ≤ b := Sizes.ofList_le hn
      have hz : slc2_s0_g.postOffs b = IE.lit 0 := by
        simp [slc2_s0_g, IE.split_ge hb, IE.sparse]
      rw [hz]
      exact slc2_sz_pos b nn hn)

def slc2_chain (α : Type) [ExactScalar α] : List (Stage α) := [⟨slc2_s0_g.prog slc2_s0_block slc2_s0_nkb, slc2_s0_g.spec (α := α), 1⟩]

theorem slc2_imp {α : Type} [ExactScalar α] :
    ∀ st ∈ slc2_chain α, Implements st.prog st.spec :=
  List.forall_mem_cons.mpr ⟨slc2_s0_impl,
  List.forall_mem_nil _⟩

theorem slc2_szok {α : Type} [ExactScalar α] :
    ∀ st ∈ slc2_chain α, slc2_sz st.out = some st.spec.outSize :=
  List.forall_mem_cons.mpr ⟨rfl,
  List.forall_mem_nil _⟩

theorem slc2_loc {α : Type} [ExactScalar α] :
    ∀ st ∈ slc2_chain α, SpecLocal slc2_sz st.spec :=
  List.forall_mem_cons.mpr ⟨slc2_s0_loc,
  List.forall_mem_nil _⟩

/-- Correctness certificate for slc2: the whole chain. -/
theorem slc2_correct {α : Type} [ExactScalar α] :
    ∀ (f : Nat → Buf α) (m : Mem α),
      Compat (sizesAfter (slc2_chain α) emptySizes)
        (runStages (slc2_chain α) f m) (specStages (slc2_chain α) f) :=
  fun f m => stages_correct slc2_sz (slc2_chain α) emptySizes f f m
    (Compat.refl _ _) (emptySizes_sub slc2_sz)
    slc2_szok slc2_imp slc2_loc

def slc2_s0_kernel : ReduceKernel :=
  { name := "slc2_s0", arity := 1, block := slc2_s0_block, nkb := slc2_s0_nkb, nout := 72, init := FE.zeroC, step := slc2_s0_g.step slc2_s0_block, stored := slc2_s0_g.stored slc2_s0_block }
def slc2_kernel : ChainKernel :=
  { name := "slc2", arity := 1, sizes := [72],
    stages := [slc2_s0_kernel] }

-- slc3: a chain of 4 stage(s), 1 input buffer(s)
--   
def slc3_sizes : List Nat := [72, 72, 72, 72]
def slc3_sz : Sizes := Sizes.ofList 1 slc3_sizes
theorem slc3_sz_pos : ∀ b n, slc3_sz b = some n → 0 < n :=
  Sizes.ofList_pos (by decide)

def slc3_s0_g : GenRed :=
  { nout := 72, K := 1
  , offs := (IE.split 1 (IE.sparse [(0, (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 36)) (IE.lit 9)) (IE.modi (IE.divi (IE.pid 0) (IE.lit 4)) (IE.lit 9))) (IE.lit 12)) (IE.modi (IE.pid 0) (IE.lit 4))))]) (IE.sparse []))
  , inRange := BE.tt
  , body := (SE.inp 0)
  , postOffs := (IE.split 1 (IE.sparse []) (IE.sparse []))
  , post := (SE.inp 0)
  , outGuard := BE.tt
  , nInp := 2, idxSlot := 1048576 }
def slc3_s0_block : Nat := 1
def slc3_s0_nkb : Nat := 1

theorem slc3_s0_wf : slc3_s0_g.Wf :=
  { offs_ok := IE.qkOnly_split (IE.qkOnly_sparse _ (by decide)) (IE.qkOnly_sparse _ (by decide))
  , post_ok := IE.qkOnly_split (IE.qkOnly_sparse _ (by decide)) (IE.qkOnly_sparse _ (by decide))
  , range_ok := by decide
  , guard_ok := by decide }

theorem slc3_s0_impl {α : Type} [ExactScalar α] :
    Implements (slc3_s0_g.prog slc3_s0_block slc3_s0_nkb) (slc3_s0_g.spec (α := α)) :=
  GenRed.prog_implements slc3_s0_g slc3_s0_block slc3_s0_nkb slc3_s0_wf (by decide) (by decide)

def slc3_s1_g : GenRed :=
  { nout := 72, K := 1
  , offs := (IE.split 1 (IE.sparse [(0, (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 36)) (IE.lit 9)) (IE.modi (IE.divi (IE.pid 0) (IE.lit 4)) (IE.lit 9))) (IE.lit 12)) (IE.add (IE.modi (IE.pid 0) (IE.lit 4)) (IE.lit 4))))]) (IE.sparse []))
  , inRange := BE.tt
  , body := (SE.inp 0)
  , postOffs := (IE.split 1 (IE.sparse []) (IE.sparse []))
  , post := (SE.inp 0)
  , outGuard := BE.tt
  , nInp := 3, idxSlot := 1048576 }
def slc3_s1_block : Nat := 1
def slc3_s1_nkb : Nat := 1

theorem slc3_s1_wf : slc3_s1_g.Wf :=
  { offs_ok := IE.qkOnly_split (IE.qkOnly_sparse _ (by decide)) (IE.qkOnly_sparse _ (by decide))
  , post_ok := IE.qkOnly_split (IE.qkOnly_sparse _ (by decide)) (IE.qkOnly_sparse _ (by decide))
  , range_ok := by decide
  , guard_ok := by decide }

theorem slc3_s1_impl {α : Type} [ExactScalar α] :
    Implements (slc3_s1_g.prog slc3_s1_block slc3_s1_nkb) (slc3_s1_g.spec (α := α)) :=
  GenRed.prog_implements slc3_s1_g slc3_s1_block slc3_s1_nkb slc3_s1_wf (by decide) (by decide)

def slc3_s2_g : GenRed :=
  { nout := 72, K := 1
  , offs := (IE.split 1 (IE.sparse [(0, (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 36)) (IE.lit 9)) (IE.modi (IE.divi (IE.pid 0) (IE.lit 4)) (IE.lit 9))) (IE.lit 12)) (IE.add (IE.modi (IE.pid 0) (IE.lit 4)) (IE.lit 8))))]) (IE.sparse []))
  , inRange := BE.tt
  , body := (SE.inp 0)
  , postOffs := (IE.split 1 (IE.sparse []) (IE.sparse []))
  , post := (SE.inp 0)
  , outGuard := BE.tt
  , nInp := 4, idxSlot := 1048576 }
def slc3_s2_block : Nat := 1
def slc3_s2_nkb : Nat := 1

theorem slc3_s2_wf : slc3_s2_g.Wf :=
  { offs_ok := IE.qkOnly_split (IE.qkOnly_sparse _ (by decide)) (IE.qkOnly_sparse _ (by decide))
  , post_ok := IE.qkOnly_split (IE.qkOnly_sparse _ (by decide)) (IE.qkOnly_sparse _ (by decide))
  , range_ok := by decide
  , guard_ok := by decide }

theorem slc3_s2_impl {α : Type} [ExactScalar α] :
    Implements (slc3_s2_g.prog slc3_s2_block slc3_s2_nkb) (slc3_s2_g.spec (α := α)) :=
  GenRed.prog_implements slc3_s2_g slc3_s2_block slc3_s2_nkb slc3_s2_wf (by decide) (by decide)

def slc3_s3_g : GenRed :=
  { nout := 72, K := 1
  , offs := (IE.split 1 (IE.sparse []) (IE.sparse [(1, (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 36)) (IE.lit 9)) (IE.modi (IE.divi (IE.pid 0) (IE.lit 4)) (IE.lit 9))) (IE.lit 4)) (IE.modi (IE.pid 0) (IE.lit 4)))), (3, (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 36)) (IE.lit 9)) (IE.modi (IE.divi (IE.pid 0) (IE.lit 4)) (IE.lit 9))) (IE.lit 4)) (IE.modi (IE.pid 0) (IE.lit 4))))]))
  , inRange := BE.tt
  , body := (SE.bin .add (SE.inp 1) (SE.inp 3))
  , postOffs := (IE.split 1 (IE.sparse []) (IE.sparse []))
  , post := (SE.inp 0)
  , outGuard := BE.tt
  , nInp := 5, idxSlot := 1048576 }
def slc3_s3_block : Nat := 1
def slc3_s3_nkb : Nat := 1

theorem slc3_s3_wf : slc3_s3_g.Wf :=
  { offs_ok := IE.qkOnly_split (IE.qkOnly_sparse _ (by decide)) (IE.qkOnly_sparse _ (by decide))
  , post_ok := IE.qkOnly_split (IE.qkOnly_sparse _ (by decide)) (IE.qkOnly_sparse _ (by decide))
  , range_ok := by decide
  , guard_ok := by decide }

theorem slc3_s3_impl {α : Type} [ExactScalar α] :
    Implements (slc3_s3_g.prog slc3_s3_block slc3_s3_nkb) (slc3_s3_g.spec (α := α)) :=
  GenRed.prog_implements slc3_s3_g slc3_s3_block slc3_s3_nkb slc3_s3_wf (by decide) (by decide)

/-- Stage 0 reads no intermediate past what was written there. -/
theorem slc3_s0_loc {α : Type} [ExactScalar α] :
    SpecLocal slc3_sz (slc3_s0_g.spec (α := α)) :=
  GenRed.specLocal slc3_s0_g slc3_sz
    (fun b nn hn q kk hq hk => by
      have hb : 1 ≤ b := Sizes.ofList_le hn
      have hz : slc3_s0_g.offs b = IE.lit 0 := by
        simp [slc3_s0_g, IE.split_ge hb, IE.sparse]
      rw [hz]
      exact slc3_sz_pos b nn hn)
    (fun b nn hn q hq => by
      have hb : 1 ≤ b := Sizes.ofList_le hn
      have hz : slc3_s0_g.postOffs b = IE.lit 0 := by
        simp [slc3_s0_g, IE.split_ge hb, IE.sparse]
      rw [hz]
      exact slc3_sz_pos b nn hn)

/-- Stage 1 reads no intermediate past what was written there. -/
theorem slc3_s1_loc {α : Type} [ExactScalar α] :
    SpecLocal slc3_sz (slc3_s1_g.spec (α := α)) :=
  GenRed.specLocal slc3_s1_g slc3_sz
    (fun b nn hn q kk hq hk => by
      have hb : 1 ≤ b := Sizes.ofList_le hn
      have hz : slc3_s1_g.offs b = IE.lit 0 := by
        simp [slc3_s1_g, IE.split_ge hb, IE.sparse]
      rw [hz]
      exact slc3_sz_pos b nn hn)
    (fun b nn hn q hq => by
      have hb : 1 ≤ b := Sizes.ofList_le hn
      have hz : slc3_s1_g.postOffs b = IE.lit 0 := by
        simp [slc3_s1_g, IE.split_ge hb, IE.sparse]
      rw [hz]
      exact slc3_sz_pos b nn hn)

/-- Stage 2 reads no intermediate past what was written there. -/
theorem slc3_s2_loc {α : Type} [ExactScalar α] :
    SpecLocal slc3_sz (slc3_s2_g.spec (α := α)) :=
  GenRed.specLocal slc3_s2_g slc3_sz
    (fun b nn hn q kk hq hk => by
      have hb : 1 ≤ b := Sizes.ofList_le hn
      have hz : slc3_s2_g.offs b = IE.lit 0 := by
        simp [slc3_s2_g, IE.split_ge hb, IE.sparse]
      rw [hz]
      exact slc3_sz_pos b nn hn)
    (fun b nn hn q hq => by
      have hb : 1 ≤ b := Sizes.ofList_le hn
      have hz : slc3_s2_g.postOffs b = IE.lit 0 := by
        simp [slc3_s2_g, IE.split_ge hb, IE.sparse]
      rw [hz]
      exact slc3_sz_pos b nn hn)

/-- Stage 3 reads no intermediate past what was written there. -/
theorem slc3_s3_loc {α : Type} [ExactScalar α] :
    SpecLocal slc3_sz (slc3_s3_g.spec (α := α)) :=
  GenRed.specLocal slc3_s3_g slc3_sz
    (fun b nn hn q kk hq hk => by
      by_cases h1 : b = 1
      · subst h1
        have hs : nn = 72 :=
          Sizes.ofList_some (by decide) (by decide) hn
        subst hs
        exact (bound_pack (A := 18) (B := 4) (bound_pack (A := 2) (B := 9) (bound_div (a := 2) (d := 36) hq) (bound_mod (c := 9) (by decide : (0 : Nat) < 9))) (bound_mod (c := 4) (by decide : (0 : Nat) < 4)))
      by_cases h3 : b = 3
      · subst h3
        have hs : nn = 72 :=
          Sizes.ofList_some (by decide) (by decide) hn
        subst hs
        exact (bound_pack (A := 18) (B := 4) (bound_pack (A := 2) (B := 9) (bound_div (a := 2) (d := 36) hq) (bound_mod (c := 9) (by decide : (0 : Nat) < 9))) (bound_mod (c := 4) (by decide : (0 : Nat) < 4)))
      have hb : 1 ≤ b := Sizes.ofList_le hn
      have hz : slc3_s3_g.offs b = IE.lit 0 := by
        simp [slc3_s3_g, IE.split_ge hb, IE.sparse, h1, h3]
      rw [hz]
      exact slc3_sz_pos b nn hn)
    (fun b nn hn q hq => by
      have hb : 1 ≤ b := Sizes.ofList_le hn
      have hz : slc3_s3_g.postOffs b = IE.lit 0 := by
        simp [slc3_s3_g, IE.split_ge hb, IE.sparse]
      rw [hz]
      exact slc3_sz_pos b nn hn)

def slc3_chain (α : Type) [ExactScalar α] : List (Stage α) := [⟨slc3_s0_g.prog slc3_s0_block slc3_s0_nkb, slc3_s0_g.spec (α := α), 1⟩, ⟨slc3_s1_g.prog slc3_s1_block slc3_s1_nkb, slc3_s1_g.spec (α := α), 2⟩, ⟨slc3_s2_g.prog slc3_s2_block slc3_s2_nkb, slc3_s2_g.spec (α := α), 3⟩, ⟨slc3_s3_g.prog slc3_s3_block slc3_s3_nkb, slc3_s3_g.spec (α := α), 4⟩]

theorem slc3_imp {α : Type} [ExactScalar α] :
    ∀ st ∈ slc3_chain α, Implements st.prog st.spec :=
  List.forall_mem_cons.mpr ⟨slc3_s0_impl,
  List.forall_mem_cons.mpr ⟨slc3_s1_impl,
  List.forall_mem_cons.mpr ⟨slc3_s2_impl,
  List.forall_mem_cons.mpr ⟨slc3_s3_impl,
  List.forall_mem_nil _⟩⟩⟩⟩

theorem slc3_szok {α : Type} [ExactScalar α] :
    ∀ st ∈ slc3_chain α, slc3_sz st.out = some st.spec.outSize :=
  List.forall_mem_cons.mpr ⟨rfl,
  List.forall_mem_cons.mpr ⟨rfl,
  List.forall_mem_cons.mpr ⟨rfl,
  List.forall_mem_cons.mpr ⟨rfl,
  List.forall_mem_nil _⟩⟩⟩⟩

theorem slc3_loc {α : Type} [ExactScalar α] :
    ∀ st ∈ slc3_chain α, SpecLocal slc3_sz st.spec :=
  List.forall_mem_cons.mpr ⟨slc3_s0_loc,
  List.forall_mem_cons.mpr ⟨slc3_s1_loc,
  List.forall_mem_cons.mpr ⟨slc3_s2_loc,
  List.forall_mem_cons.mpr ⟨slc3_s3_loc,
  List.forall_mem_nil _⟩⟩⟩⟩

/-- Correctness certificate for slc3: the whole chain. -/
theorem slc3_correct {α : Type} [ExactScalar α] :
    ∀ (f : Nat → Buf α) (m : Mem α),
      Compat (sizesAfter (slc3_chain α) emptySizes)
        (runStages (slc3_chain α) f m) (specStages (slc3_chain α) f) :=
  fun f m => stages_correct slc3_sz (slc3_chain α) emptySizes f f m
    (Compat.refl _ _) (emptySizes_sub slc3_sz)
    slc3_szok slc3_imp slc3_loc

def slc3_s0_kernel : ReduceKernel :=
  { name := "slc3_s0", arity := 1, block := slc3_s0_block, nkb := slc3_s0_nkb, nout := 72, init := FE.zeroC, step := slc3_s0_g.step slc3_s0_block, stored := slc3_s0_g.stored slc3_s0_block }
def slc3_s1_kernel : ReduceKernel :=
  { name := "slc3_s1", arity := 2, block := slc3_s1_block, nkb := slc3_s1_nkb, nout := 72, init := FE.zeroC, step := slc3_s1_g.step slc3_s1_block, stored := slc3_s1_g.stored slc3_s1_block }
def slc3_s2_kernel : ReduceKernel :=
  { name := "slc3_s2", arity := 3, block := slc3_s2_block, nkb := slc3_s2_nkb, nout := 72, init := FE.zeroC, step := slc3_s2_g.step slc3_s2_block, stored := slc3_s2_g.stored slc3_s2_block }
def slc3_s3_kernel : ReduceKernel :=
  { name := "slc3_s3", arity := 4, block := slc3_s3_block, nkb := slc3_s3_nkb, nout := 72, init := FE.zeroC, step := slc3_s3_g.step slc3_s3_block, stored := slc3_s3_g.stored slc3_s3_block }
def slc3_kernel : ChainKernel :=
  { name := "slc3", arity := 1, sizes := [72, 72, 72, 72],
    stages := [slc3_s0_kernel, slc3_s1_kernel, slc3_s2_kernel, slc3_s3_kernel] }

-- slc4: a chain of 3 stage(s), 1 input buffer(s)
--   
def slc4_sizes : List Nat := [96, 96, 192]
def slc4_sz : Sizes := Sizes.ofList 1 slc4_sizes
theorem slc4_sz_pos : ∀ b n, slc4_sz b = some n → 0 < n :=
  Sizes.ofList_pos (by decide)

def slc4_s0_g : GenRed :=
  { nout := 96, K := 1
  , offs := (IE.split 1 (IE.sparse [(0, (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 48)) (IE.lit 8)) (IE.modi (IE.divi (IE.pid 0) (IE.lit 12)) (IE.lit 4))) (IE.lit 12)) (IE.modi (IE.pid 0) (IE.lit 12))))]) (IE.sparse []))
  , inRange := BE.tt
  , body := (SE.inp 0)
  , postOffs := (IE.split 1 (IE.sparse []) (IE.sparse []))
  , post := (SE.inp 0)
  , outGuard := BE.tt
  , nInp := 2, idxSlot := 1048576 }
def slc4_s0_block : Nat := 1
def slc4_s0_nkb : Nat := 1

theorem slc4_s0_wf : slc4_s0_g.Wf :=
  { offs_ok := IE.qkOnly_split (IE.qkOnly_sparse _ (by decide)) (IE.qkOnly_sparse _ (by decide))
  , post_ok := IE.qkOnly_split (IE.qkOnly_sparse _ (by decide)) (IE.qkOnly_sparse _ (by decide))
  , range_ok := by decide
  , guard_ok := by decide }

theorem slc4_s0_impl {α : Type} [ExactScalar α] :
    Implements (slc4_s0_g.prog slc4_s0_block slc4_s0_nkb) (slc4_s0_g.spec (α := α)) :=
  GenRed.prog_implements slc4_s0_g slc4_s0_block slc4_s0_nkb slc4_s0_wf (by decide) (by decide)

def slc4_s1_g : GenRed :=
  { nout := 96, K := 1
  , offs := (IE.split 1 (IE.sparse [(0, (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 48)) (IE.lit 8)) (IE.add (IE.modi (IE.divi (IE.pid 0) (IE.lit 12)) (IE.lit 4)) (IE.lit 4))) (IE.lit 12)) (IE.modi (IE.pid 0) (IE.lit 12))))]) (IE.sparse []))
  , inRange := BE.tt
  , body := (SE.inp 0)
  , postOffs := (IE.split 1 (IE.sparse []) (IE.sparse []))
  , post := (SE.inp 0)
  , outGuard := BE.tt
  , nInp := 3, idxSlot := 1048576 }
def slc4_s1_block : Nat := 1
def slc4_s1_nkb : Nat := 1

theorem slc4_s1_wf : slc4_s1_g.Wf :=
  { offs_ok := IE.qkOnly_split (IE.qkOnly_sparse _ (by decide)) (IE.qkOnly_sparse _ (by decide))
  , post_ok := IE.qkOnly_split (IE.qkOnly_sparse _ (by decide)) (IE.qkOnly_sparse _ (by decide))
  , range_ok := by decide
  , guard_ok := by decide }

theorem slc4_s1_impl {α : Type} [ExactScalar α] :
    Implements (slc4_s1_g.prog slc4_s1_block slc4_s1_nkb) (slc4_s1_g.spec (α := α)) :=
  GenRed.prog_implements slc4_s1_g slc4_s1_block slc4_s1_nkb slc4_s1_wf (by decide) (by decide)

def slc4_s2_g : GenRed :=
  { nout := 192, K := 2
  , offs := (IE.split 1 (IE.sparse []) (IE.sparse [(1, (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 96)) (IE.lit 4)) (IE.sub (IE.sub (IE.modi (IE.divi (IE.pid 0) (IE.lit 12)) (IE.lit 8)) (IE.lit 4)) (IE.sub (IE.sub (IE.modi (IE.divi (IE.pid 0) (IE.lit 12)) (IE.lit 8)) (IE.lit 4)) (IE.lit 3)))) (IE.lit 12)) (IE.modi (IE.pid 0) (IE.lit 12)))), (2, (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 96)) (IE.lit 4)) (IE.sub (IE.modi (IE.divi (IE.pid 0) (IE.lit 12)) (IE.lit 8)) (IE.sub (IE.modi (IE.divi (IE.pid 0) (IE.lit 12)) (IE.lit 8)) (IE.lit 3)))) (IE.lit 12)) (IE.modi (IE.pid 0) (IE.lit 12))))]))
  , inRange := (BE.or (BE.and (BE.and (BE.cmp .eq IE.rk (IE.lit 0)) (BE.cmp .le (IE.lit 0) (IE.modi (IE.divi (IE.pid 0) (IE.lit 12)) (IE.lit 8)))) (BE.cmp .lt (IE.modi (IE.divi (IE.pid 0) (IE.lit 12)) (IE.lit 8)) (IE.lit 4))) (BE.and (BE.and (BE.cmp .eq IE.rk (IE.lit 1)) (BE.cmp .le (IE.lit 4) (IE.modi (IE.divi (IE.pid 0) (IE.lit 12)) (IE.lit 8)))) (BE.cmp .lt (IE.modi (IE.divi (IE.pid 0) (IE.lit 12)) (IE.lit 8)) (IE.lit 8))))
  , body := (SE.selLe (SE.inp 4) (SE.lit false 1 2) (SE.inp 2) (SE.inp 1))
  , postOffs := (IE.split 1 (IE.sparse []) (IE.sparse []))
  , post := (SE.inp 0)
  , outGuard := BE.tt
  , nInp := 4, idxSlot := 4 }
def slc4_s2_block : Nat := 2
def slc4_s2_nkb : Nat := 1

theorem slc4_s2_wf : slc4_s2_g.Wf :=
  { offs_ok := IE.qkOnly_split (IE.qkOnly_sparse _ (by decide)) (IE.qkOnly_sparse _ (by decide))
  , post_ok := IE.qkOnly_split (IE.qkOnly_sparse _ (by decide)) (IE.qkOnly_sparse _ (by decide))
  , range_ok := by decide
  , guard_ok := by decide }

theorem slc4_s2_impl {α : Type} [ExactScalar α] :
    Implements (slc4_s2_g.prog slc4_s2_block slc4_s2_nkb) (slc4_s2_g.spec (α := α)) :=
  GenRed.prog_implements slc4_s2_g slc4_s2_block slc4_s2_nkb slc4_s2_wf (by decide) (by decide)

/-- Stage 0 reads no intermediate past what was written there. -/
theorem slc4_s0_loc {α : Type} [ExactScalar α] :
    SpecLocal slc4_sz (slc4_s0_g.spec (α := α)) :=
  GenRed.specLocal slc4_s0_g slc4_sz
    (fun b nn hn q kk hq hk => by
      have hb : 1 ≤ b := Sizes.ofList_le hn
      have hz : slc4_s0_g.offs b = IE.lit 0 := by
        simp [slc4_s0_g, IE.split_ge hb, IE.sparse]
      rw [hz]
      exact slc4_sz_pos b nn hn)
    (fun b nn hn q hq => by
      have hb : 1 ≤ b := Sizes.ofList_le hn
      have hz : slc4_s0_g.postOffs b = IE.lit 0 := by
        simp [slc4_s0_g, IE.split_ge hb, IE.sparse]
      rw [hz]
      exact slc4_sz_pos b nn hn)

/-- Stage 1 reads no intermediate past what was written there. -/
theorem slc4_s1_loc {α : Type} [ExactScalar α] :
    SpecLocal slc4_sz (slc4_s1_g.spec (α := α)) :=
  GenRed.specLocal slc4_s1_g slc4_sz
    (fun b nn hn q kk hq hk => by
      have hb : 1 ≤ b := Sizes.ofList_le hn
      have hz : slc4_s1_g.offs b = IE.lit 0 := by
        simp [slc4_s1_g, IE.split_ge hb, IE.sparse]
      rw [hz]
      exact slc4_sz_pos b nn hn)
    (fun b nn hn q hq => by
      have hb : 1 ≤ b := Sizes.ofList_le hn
      have hz : slc4_s1_g.postOffs b = IE.lit 0 := by
        simp [slc4_s1_g, IE.split_ge hb, IE.sparse]
      rw [hz]
      exact slc4_sz_pos b nn hn)

/-- Stage 2 reads no intermediate past what was written there. -/
theorem slc4_s2_loc {α : Type} [ExactScalar α] :
    SpecLocal slc4_sz (slc4_s2_g.spec (α := α)) :=
  GenRed.specLocal slc4_s2_g slc4_sz
    (fun b nn hn q kk hq hk => by
      by_cases h1 : b = 1
      · subst h1
        have hs : nn = 96 :=
          Sizes.ofList_some (by decide) (by decide) hn
        subst hs
        exact (bound_pack (A := 8) (B := 12) (bound_pack (A := 2) (B := 4) (bound_div (a := 2) (d := 96) hq) (ExactScalar.clamp_lt (c := 4) (by decide : (0 : Nat) < 4))) (bound_mod (c := 12) (by decide : (0 : Nat) < 12)))
      by_cases h2 : b = 2
      · subst h2
        have hs : nn = 96 :=
          Sizes.ofList_some (by decide) (by decide) hn
        subst hs
        exact (bound_pack (A := 8) (B := 12) (bound_pack (A := 2) (B := 4) (bound_div (a := 2) (d := 96) hq) (ExactScalar.clamp_lt (c := 4) (by decide : (0 : Nat) < 4))) (bound_mod (c := 12) (by decide : (0 : Nat) < 12)))
      have hb : 1 ≤ b := Sizes.ofList_le hn
      have hz : slc4_s2_g.offs b = IE.lit 0 := by
        simp [slc4_s2_g, IE.split_ge hb, IE.sparse, h1, h2]
      rw [hz]
      exact slc4_sz_pos b nn hn)
    (fun b nn hn q hq => by
      have hb : 1 ≤ b := Sizes.ofList_le hn
      have hz : slc4_s2_g.postOffs b = IE.lit 0 := by
        simp [slc4_s2_g, IE.split_ge hb, IE.sparse]
      rw [hz]
      exact slc4_sz_pos b nn hn)

def slc4_chain (α : Type) [ExactScalar α] : List (Stage α) := [⟨slc4_s0_g.prog slc4_s0_block slc4_s0_nkb, slc4_s0_g.spec (α := α), 1⟩, ⟨slc4_s1_g.prog slc4_s1_block slc4_s1_nkb, slc4_s1_g.spec (α := α), 2⟩, ⟨slc4_s2_g.prog slc4_s2_block slc4_s2_nkb, slc4_s2_g.spec (α := α), 3⟩]

theorem slc4_imp {α : Type} [ExactScalar α] :
    ∀ st ∈ slc4_chain α, Implements st.prog st.spec :=
  List.forall_mem_cons.mpr ⟨slc4_s0_impl,
  List.forall_mem_cons.mpr ⟨slc4_s1_impl,
  List.forall_mem_cons.mpr ⟨slc4_s2_impl,
  List.forall_mem_nil _⟩⟩⟩

theorem slc4_szok {α : Type} [ExactScalar α] :
    ∀ st ∈ slc4_chain α, slc4_sz st.out = some st.spec.outSize :=
  List.forall_mem_cons.mpr ⟨rfl,
  List.forall_mem_cons.mpr ⟨rfl,
  List.forall_mem_cons.mpr ⟨rfl,
  List.forall_mem_nil _⟩⟩⟩

theorem slc4_loc {α : Type} [ExactScalar α] :
    ∀ st ∈ slc4_chain α, SpecLocal slc4_sz st.spec :=
  List.forall_mem_cons.mpr ⟨slc4_s0_loc,
  List.forall_mem_cons.mpr ⟨slc4_s1_loc,
  List.forall_mem_cons.mpr ⟨slc4_s2_loc,
  List.forall_mem_nil _⟩⟩⟩

/-- Correctness certificate for slc4: the whole chain. -/
theorem slc4_correct {α : Type} [ExactScalar α] :
    ∀ (f : Nat → Buf α) (m : Mem α),
      Compat (sizesAfter (slc4_chain α) emptySizes)
        (runStages (slc4_chain α) f m) (specStages (slc4_chain α) f) :=
  fun f m => stages_correct slc4_sz (slc4_chain α) emptySizes f f m
    (Compat.refl _ _) (emptySizes_sub slc4_sz)
    slc4_szok slc4_imp slc4_loc

def slc4_s0_kernel : ReduceKernel :=
  { name := "slc4_s0", arity := 1, block := slc4_s0_block, nkb := slc4_s0_nkb, nout := 96, init := FE.zeroC, step := slc4_s0_g.step slc4_s0_block, stored := slc4_s0_g.stored slc4_s0_block }
def slc4_s1_kernel : ReduceKernel :=
  { name := "slc4_s1", arity := 2, block := slc4_s1_block, nkb := slc4_s1_nkb, nout := 96, init := FE.zeroC, step := slc4_s1_g.step slc4_s1_block, stored := slc4_s1_g.stored slc4_s1_block }
def slc4_s2_kernel : ReduceKernel :=
  { name := "slc4_s2", arity := 3, block := slc4_s2_block, nkb := slc4_s2_nkb, nout := 192, init := FE.zeroC, step := slc4_s2_g.step slc4_s2_block, stored := slc4_s2_g.stored slc4_s2_block }
def slc4_kernel : ChainKernel :=
  { name := "slc4", arity := 1, sizes := [96, 96, 192],
    stages := [slc4_s0_kernel, slc4_s1_kernel, slc4_s2_kernel] }

-- slc5: a chain of 1 stage(s), 1 input buffer(s)
--   fused <built-in function mul> into stage 0
def slc5_sizes : List Nat := [96]
def slc5_sz : Sizes := Sizes.ofList 1 slc5_sizes
theorem slc5_sz_pos : ∀ b n, slc5_sz b = some n → 0 < n :=
  Sizes.ofList_pos (by decide)

def slc5_s0_g : GenRed :=
  { nout := 96, K := 1
  , offs := (IE.split 1 (IE.sparse [(0, (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 48)) (IE.lit 9)) (IE.add (IE.modi (IE.divi (IE.pid 0) (IE.lit 12)) (IE.lit 4)) (IE.lit 5))) (IE.lit 12)) (IE.modi (IE.pid 0) (IE.lit 12))))]) (IE.sparse []))
  , inRange := BE.tt
  , body := (SE.inp 0)
  , postOffs := (IE.split 1 (IE.sparse []) (IE.sparse []))
  , post := (SE.bin .mul (SE.inp 0) (SE.lit false 3 1))
  , outGuard := BE.tt
  , nInp := 2, idxSlot := 1048576 }
def slc5_s0_block : Nat := 1
def slc5_s0_nkb : Nat := 1

theorem slc5_s0_wf : slc5_s0_g.Wf :=
  { offs_ok := IE.qkOnly_split (IE.qkOnly_sparse _ (by decide)) (IE.qkOnly_sparse _ (by decide))
  , post_ok := IE.qkOnly_split (IE.qkOnly_sparse _ (by decide)) (IE.qkOnly_sparse _ (by decide))
  , range_ok := by decide
  , guard_ok := by decide }

theorem slc5_s0_impl {α : Type} [ExactScalar α] :
    Implements (slc5_s0_g.prog slc5_s0_block slc5_s0_nkb) (slc5_s0_g.spec (α := α)) :=
  GenRed.prog_implements slc5_s0_g slc5_s0_block slc5_s0_nkb slc5_s0_wf (by decide) (by decide)

/-- Stage 0 reads no intermediate past what was written there. -/
theorem slc5_s0_loc {α : Type} [ExactScalar α] :
    SpecLocal slc5_sz (slc5_s0_g.spec (α := α)) :=
  GenRed.specLocal slc5_s0_g slc5_sz
    (fun b nn hn q kk hq hk => by
      have hb : 1 ≤ b := Sizes.ofList_le hn
      have hz : slc5_s0_g.offs b = IE.lit 0 := by
        simp [slc5_s0_g, IE.split_ge hb, IE.sparse]
      rw [hz]
      exact slc5_sz_pos b nn hn)
    (fun b nn hn q hq => by
      have hb : 1 ≤ b := Sizes.ofList_le hn
      have hz : slc5_s0_g.postOffs b = IE.lit 0 := by
        simp [slc5_s0_g, IE.split_ge hb, IE.sparse]
      rw [hz]
      exact slc5_sz_pos b nn hn)

def slc5_chain (α : Type) [ExactScalar α] : List (Stage α) := [⟨slc5_s0_g.prog slc5_s0_block slc5_s0_nkb, slc5_s0_g.spec (α := α), 1⟩]

theorem slc5_imp {α : Type} [ExactScalar α] :
    ∀ st ∈ slc5_chain α, Implements st.prog st.spec :=
  List.forall_mem_cons.mpr ⟨slc5_s0_impl,
  List.forall_mem_nil _⟩

theorem slc5_szok {α : Type} [ExactScalar α] :
    ∀ st ∈ slc5_chain α, slc5_sz st.out = some st.spec.outSize :=
  List.forall_mem_cons.mpr ⟨rfl,
  List.forall_mem_nil _⟩

theorem slc5_loc {α : Type} [ExactScalar α] :
    ∀ st ∈ slc5_chain α, SpecLocal slc5_sz st.spec :=
  List.forall_mem_cons.mpr ⟨slc5_s0_loc,
  List.forall_mem_nil _⟩

/-- Correctness certificate for slc5: the whole chain. -/
theorem slc5_correct {α : Type} [ExactScalar α] :
    ∀ (f : Nat → Buf α) (m : Mem α),
      Compat (sizesAfter (slc5_chain α) emptySizes)
        (runStages (slc5_chain α) f m) (specStages (slc5_chain α) f) :=
  fun f m => stages_correct slc5_sz (slc5_chain α) emptySizes f f m
    (Compat.refl _ _) (emptySizes_sub slc5_sz)
    slc5_szok slc5_imp slc5_loc

def slc5_s0_kernel : ReduceKernel :=
  { name := "slc5_s0", arity := 1, block := slc5_s0_block, nkb := slc5_s0_nkb, nout := 96, init := FE.zeroC, step := slc5_s0_g.step slc5_s0_block, stored := slc5_s0_g.stored slc5_s0_block }
def slc5_kernel : ChainKernel :=
  { name := "slc5", arity := 1, sizes := [96],
    stages := [slc5_s0_kernel] }

def main : IO Unit := do
  IO.FS.writeFile "../generated/slc0.py" slc0_kernel.render
  IO.FS.writeFile "../generated/slc1.py" slc1_kernel.render
  IO.FS.writeFile "../generated/slc2.py" slc2_kernel.render
  IO.FS.writeFile "../generated/slc3.py" slc3_kernel.render
  IO.FS.writeFile "../generated/slc4.py" slc4_kernel.render
  IO.FS.writeFile "../generated/slc5.py" slc5_kernel.render
