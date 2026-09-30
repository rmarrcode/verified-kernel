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

-- t017: a chain of 4 stage(s), 7 input buffer(s)
--   fused squeeze_activation into stage 0; fused expand1x1_activation into stage 1; fused expand3x3_activation into stage 2
def t017_sizes : List Nat := [12582912, 134217728, 134217728, 268435456]
def t017_sz : Sizes := Sizes.ofList 7 t017_sizes
theorem t017_sz_pos : ∀ b n, t017_sz b = some n → 0 < n :=
  Sizes.ofList_pos (by decide)

def t017_s0_g : GenRed :=
  { nout := 12582912, K := 3
  , offs := (IE.split 7 (IE.sparse [(0, (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 393216)) (IE.lit 3)) IE.rk) (IE.lit 256)) (IE.modi (IE.divi (IE.pid 0) (IE.lit 256)) (IE.lit 256))) (IE.lit 256)) (IE.modi (IE.pid 0) (IE.lit 256)))), (1, (IE.add (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 65536)) (IE.lit 6)) (IE.lit 3)) IE.rk))]) (IE.sparse []))
  , inRange := (BE.and (BE.cmp .lt (IE.modi (IE.divi (IE.pid 0) (IE.lit 256)) (IE.lit 256)) (IE.lit 256)) (BE.cmp .lt (IE.modi (IE.pid 0) (IE.lit 256)) (IE.lit 256)))
  , body := (SE.bin .mul (SE.inp 0) (SE.inp 1))
  , postOffs := (IE.split 7 (IE.sparse [(2, (IE.modi (IE.divi (IE.pid 0) (IE.lit 65536)) (IE.lit 6)))]) (IE.sparse []))
  , post := (SE.bin .max (SE.bin .add (SE.inp 0) (SE.inp 3)) (SE.lit false 0 1))
  , outGuard := BE.tt
  , nInp := 8, idxSlot := 1048576 }
def t017_s0_block : Nat := 2
def t017_s0_nkb : Nat := 2

theorem t017_s0_wf : t017_s0_g.Wf :=
  { offs_ok := IE.qkOnly_split (IE.qkOnly_sparse _ (by decide)) (IE.qkOnly_sparse _ (by decide))
  , post_ok := IE.qkOnly_split (IE.qkOnly_sparse _ (by decide)) (IE.qkOnly_sparse _ (by decide))
  , range_ok := by decide
  , guard_ok := by decide }

theorem t017_s0_impl {α : Type} [ExactScalar α] :
    Implements (t017_s0_g.prog t017_s0_block t017_s0_nkb) (t017_s0_g.spec (α := α)) :=
  GenRed.prog_implements t017_s0_g t017_s0_block t017_s0_nkb t017_s0_wf (by decide) (by decide)

def t017_s1_g : GenRed :=
  { nout := 134217728, K := 6
  , offs := (IE.split 7 (IE.sparse [(3, (IE.add (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 65536)) (IE.lit 64)) (IE.lit 6)) IE.rk))]) (IE.sparse [(7, (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 4194304)) (IE.lit 6)) IE.rk) (IE.lit 256)) (IE.modi (IE.divi (IE.pid 0) (IE.lit 256)) (IE.lit 256))) (IE.lit 256)) (IE.modi (IE.pid 0) (IE.lit 256))))]))
  , inRange := (BE.and (BE.cmp .lt (IE.modi (IE.divi (IE.pid 0) (IE.lit 256)) (IE.lit 256)) (IE.lit 256)) (BE.cmp .lt (IE.modi (IE.pid 0) (IE.lit 256)) (IE.lit 256)))
  , body := (SE.bin .mul (SE.inp 7) (SE.inp 3))
  , postOffs := (IE.split 7 (IE.sparse [(4, (IE.modi (IE.divi (IE.pid 0) (IE.lit 65536)) (IE.lit 64)))]) (IE.sparse []))
  , post := (SE.bin .max (SE.bin .add (SE.inp 0) (SE.inp 5)) (SE.lit false 0 1))
  , outGuard := BE.tt
  , nInp := 9, idxSlot := 1048576 }
def t017_s1_block : Nat := 4
def t017_s1_nkb : Nat := 2

theorem t017_s1_wf : t017_s1_g.Wf :=
  { offs_ok := IE.qkOnly_split (IE.qkOnly_sparse _ (by decide)) (IE.qkOnly_sparse _ (by decide))
  , post_ok := IE.qkOnly_split (IE.qkOnly_sparse _ (by decide)) (IE.qkOnly_sparse _ (by decide))
  , range_ok := by decide
  , guard_ok := by decide }

theorem t017_s1_impl {α : Type} [ExactScalar α] :
    Implements (t017_s1_g.prog t017_s1_block t017_s1_nkb) (t017_s1_g.spec (α := α)) :=
  GenRed.prog_implements t017_s1_g t017_s1_block t017_s1_nkb t017_s1_wf (by decide) (by decide)

def t017_s2_g : GenRed :=
  { nout := 134217728, K := 54
  , offs := (IE.split 7 (IE.sparse [(5, (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 65536)) (IE.lit 64)) (IE.lit 6)) (IE.divi IE.rk (IE.lit 9))) (IE.lit 3)) (IE.modi (IE.divi IE.rk (IE.lit 3)) (IE.lit 3))) (IE.lit 3)) (IE.modi IE.rk (IE.lit 3))))]) (IE.sparse [(7, (IE.sub (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 4194304)) (IE.lit 6)) (IE.divi IE.rk (IE.lit 9))) (IE.lit 256)) (IE.sub (IE.add (IE.modi (IE.divi (IE.pid 0) (IE.lit 256)) (IE.lit 256)) (IE.modi (IE.divi IE.rk (IE.lit 3)) (IE.lit 3))) (IE.lit 1))) (IE.lit 256)) (IE.sub (IE.add (IE.modi (IE.pid 0) (IE.lit 256)) (IE.modi IE.rk (IE.lit 3))) (IE.lit 1))) (IE.sub (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 4194304)) (IE.lit 6)) (IE.divi IE.rk (IE.lit 9))) (IE.lit 256)) (IE.sub (IE.add (IE.modi (IE.divi (IE.pid 0) (IE.lit 256)) (IE.lit 256)) (IE.modi (IE.divi IE.rk (IE.lit 3)) (IE.lit 3))) (IE.lit 1))) (IE.lit 256)) (IE.sub (IE.add (IE.modi (IE.pid 0) (IE.lit 256)) (IE.modi IE.rk (IE.lit 3))) (IE.lit 1))) (IE.lit 12582911))))]))
  , inRange := (BE.and (BE.and (BE.and (BE.cmp .le (IE.lit 1) (IE.add (IE.modi (IE.divi (IE.pid 0) (IE.lit 256)) (IE.lit 256)) (IE.modi (IE.divi IE.rk (IE.lit 3)) (IE.lit 3)))) (BE.cmp .lt (IE.add (IE.modi (IE.divi (IE.pid 0) (IE.lit 256)) (IE.lit 256)) (IE.modi (IE.divi IE.rk (IE.lit 3)) (IE.lit 3))) (IE.lit 257))) (BE.cmp .le (IE.lit 1) (IE.add (IE.modi (IE.pid 0) (IE.lit 256)) (IE.modi IE.rk (IE.lit 3))))) (BE.cmp .lt (IE.add (IE.modi (IE.pid 0) (IE.lit 256)) (IE.modi IE.rk (IE.lit 3))) (IE.lit 257)))
  , body := (SE.bin .mul (SE.inp 7) (SE.inp 5))
  , postOffs := (IE.split 7 (IE.sparse [(6, (IE.modi (IE.divi (IE.pid 0) (IE.lit 65536)) (IE.lit 64)))]) (IE.sparse []))
  , post := (SE.bin .max (SE.bin .add (SE.inp 0) (SE.inp 7)) (SE.lit false 0 1))
  , outGuard := BE.tt
  , nInp := 10, idxSlot := 1048576 }
def t017_s2_block : Nat := 32
def t017_s2_nkb : Nat := 2

theorem t017_s2_wf : t017_s2_g.Wf :=
  { offs_ok := IE.qkOnly_split (IE.qkOnly_sparse _ (by decide)) (IE.qkOnly_sparse _ (by decide))
  , post_ok := IE.qkOnly_split (IE.qkOnly_sparse _ (by decide)) (IE.qkOnly_sparse _ (by decide))
  , range_ok := by decide
  , guard_ok := by decide }

theorem t017_s2_impl {α : Type} [ExactScalar α] :
    Implements (t017_s2_g.prog t017_s2_block t017_s2_nkb) (t017_s2_g.spec (α := α)) :=
  GenRed.prog_implements t017_s2_g t017_s2_block t017_s2_nkb t017_s2_wf (by decide) (by decide)

def t017_s3_g : GenRed :=
  { nout := 268435456, K := 2
  , offs := (IE.split 7 (IE.sparse []) (IE.sparse [(8, (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 8388608)) (IE.lit 64)) (IE.sub (IE.modi (IE.divi (IE.pid 0) (IE.lit 65536)) (IE.lit 128)) (IE.sub (IE.modi (IE.divi (IE.pid 0) (IE.lit 65536)) (IE.lit 128)) (IE.lit 63)))) (IE.lit 256)) (IE.modi (IE.divi (IE.pid 0) (IE.lit 256)) (IE.lit 256))) (IE.lit 256)) (IE.modi (IE.pid 0) (IE.lit 256)))), (9, (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 8388608)) (IE.lit 64)) (IE.sub (IE.sub (IE.modi (IE.divi (IE.pid 0) (IE.lit 65536)) (IE.lit 128)) (IE.lit 64)) (IE.sub (IE.sub (IE.modi (IE.divi (IE.pid 0) (IE.lit 65536)) (IE.lit 128)) (IE.lit 64)) (IE.lit 63)))) (IE.lit 256)) (IE.modi (IE.divi (IE.pid 0) (IE.lit 256)) (IE.lit 256))) (IE.lit 256)) (IE.modi (IE.pid 0) (IE.lit 256))))]))
  , inRange := (BE.or (BE.and (BE.and (BE.cmp .eq IE.rk (IE.lit 0)) (BE.cmp .le (IE.lit 0) (IE.modi (IE.divi (IE.pid 0) (IE.lit 65536)) (IE.lit 128)))) (BE.cmp .lt (IE.modi (IE.divi (IE.pid 0) (IE.lit 65536)) (IE.lit 128)) (IE.lit 64))) (BE.and (BE.and (BE.cmp .eq IE.rk (IE.lit 1)) (BE.cmp .le (IE.lit 64) (IE.modi (IE.divi (IE.pid 0) (IE.lit 65536)) (IE.lit 128)))) (BE.cmp .lt (IE.modi (IE.divi (IE.pid 0) (IE.lit 65536)) (IE.lit 128)) (IE.lit 128))))
  , body := (SE.selLe (SE.inp 11) (SE.lit false 1 2) (SE.inp 8) (SE.inp 9))
  , postOffs := (IE.split 7 (IE.sparse []) (IE.sparse []))
  , post := (SE.inp 0)
  , outGuard := BE.tt
  , nInp := 11, idxSlot := 11 }
def t017_s3_block : Nat := 2
def t017_s3_nkb : Nat := 1

theorem t017_s3_wf : t017_s3_g.Wf :=
  { offs_ok := IE.qkOnly_split (IE.qkOnly_sparse _ (by decide)) (IE.qkOnly_sparse _ (by decide))
  , post_ok := IE.qkOnly_split (IE.qkOnly_sparse _ (by decide)) (IE.qkOnly_sparse _ (by decide))
  , range_ok := by decide
  , guard_ok := by decide }

theorem t017_s3_impl {α : Type} [ExactScalar α] :
    Implements (t017_s3_g.prog t017_s3_block t017_s3_nkb) (t017_s3_g.spec (α := α)) :=
  GenRed.prog_implements t017_s3_g t017_s3_block t017_s3_nkb t017_s3_wf (by decide) (by decide)

/-- Stage 0 reads no intermediate past what was written there. -/
theorem t017_s0_loc {α : Type} [ExactScalar α] :
    SpecLocal t017_sz (t017_s0_g.spec (α := α)) :=
  GenRed.specLocal t017_s0_g t017_sz
    (fun b nn hn q kk hq hk => by
      have hb : 7 ≤ b := Sizes.ofList_le hn
      have hz : t017_s0_g.offs b = IE.lit 0 := by
        simp [t017_s0_g, IE.split_ge hb, IE.sparse]
      rw [hz]
      exact t017_sz_pos b nn hn)
    (fun b nn hn q hq => by
      have hb : 7 ≤ b := Sizes.ofList_le hn
      have hz : t017_s0_g.postOffs b = IE.lit 0 := by
        simp [t017_s0_g, IE.split_ge hb, IE.sparse]
      rw [hz]
      exact t017_sz_pos b nn hn)

/-- Stage 1 reads no intermediate past what was written there. -/
theorem t017_s1_loc {α : Type} [ExactScalar α] :
    SpecLocal t017_sz (t017_s1_g.spec (α := α)) :=
  GenRed.specLocal t017_s1_g t017_sz
    (fun b nn hn q kk hq hk => by
      by_cases h7 : b = 7
      · subst h7
        have hs : nn = 12582912 :=
          Sizes.ofList_some (by decide) (by decide) hn
        subst hs
        exact (bound_pack (A := 49152) (B := 256) (bound_pack (A := 192) (B := 256) (bound_pack (A := 32) (B := 6) (bound_div (a := 32) (d := 4194304) hq) hk) (bound_mod (c := 256) (by decide : (0 : Nat) < 256))) (bound_mod (c := 256) (by decide : (0 : Nat) < 256)))
      have hb : 7 ≤ b := Sizes.ofList_le hn
      have hz : t017_s1_g.offs b = IE.lit 0 := by
        simp [t017_s1_g, IE.split_ge hb, IE.sparse, h7]
      rw [hz]
      exact t017_sz_pos b nn hn)
    (fun b nn hn q hq => by
      have hb : 7 ≤ b := Sizes.ofList_le hn
      have hz : t017_s1_g.postOffs b = IE.lit 0 := by
        simp [t017_s1_g, IE.split_ge hb, IE.sparse]
      rw [hz]
      exact t017_sz_pos b nn hn)

/-- Stage 2 reads no intermediate past what was written there. -/
theorem t017_s2_loc {α : Type} [ExactScalar α] :
    SpecLocal t017_sz (t017_s2_g.spec (α := α)) :=
  GenRed.specLocal t017_s2_g t017_sz
    (fun b nn hn q kk hq hk => by
      by_cases h7 : b = 7
      · subst h7
        have hs : nn = 12582912 :=
          Sizes.ofList_some (by decide) (by decide) hn
        subst hs
        exact (ExactScalar.clamp_lt (c := 12582912) (by decide : (0 : Nat) < 12582912))
      have hb : 7 ≤ b := Sizes.ofList_le hn
      have hz : t017_s2_g.offs b = IE.lit 0 := by
        simp [t017_s2_g, IE.split_ge hb, IE.sparse, h7]
      rw [hz]
      exact t017_sz_pos b nn hn)
    (fun b nn hn q hq => by
      have hb : 7 ≤ b := Sizes.ofList_le hn
      have hz : t017_s2_g.postOffs b = IE.lit 0 := by
        simp [t017_s2_g, IE.split_ge hb, IE.sparse]
      rw [hz]
      exact t017_sz_pos b nn hn)

/-- Stage 3 reads no intermediate past what was written there. -/
theorem t017_s3_loc {α : Type} [ExactScalar α] :
    SpecLocal t017_sz (t017_s3_g.spec (α := α)) :=
  GenRed.specLocal t017_s3_g t017_sz
    (fun b nn hn q kk hq hk => by
      by_cases h8 : b = 8
      · subst h8
        have hs : nn = 134217728 :=
          Sizes.ofList_some (by decide) (by decide) hn
        subst hs
        exact (bound_pack (A := 524288) (B := 256) (bound_pack (A := 2048) (B := 256) (bound_pack (A := 32) (B := 64) (bound_div (a := 32) (d := 8388608) hq) (ExactScalar.clamp_lt (c := 64) (by decide : (0 : Nat) < 64))) (bound_mod (c := 256) (by decide : (0 : Nat) < 256))) (bound_mod (c := 256) (by decide : (0 : Nat) < 256)))
      by_cases h9 : b = 9
      · subst h9
        have hs : nn = 134217728 :=
          Sizes.ofList_some (by decide) (by decide) hn
        subst hs
        exact (bound_pack (A := 524288) (B := 256) (bound_pack (A := 2048) (B := 256) (bound_pack (A := 32) (B := 64) (bound_div (a := 32) (d := 8388608) hq) (ExactScalar.clamp_lt (c := 64) (by decide : (0 : Nat) < 64))) (bound_mod (c := 256) (by decide : (0 : Nat) < 256))) (bound_mod (c := 256) (by decide : (0 : Nat) < 256)))
      have hb : 7 ≤ b := Sizes.ofList_le hn
      have hz : t017_s3_g.offs b = IE.lit 0 := by
        simp [t017_s3_g, IE.split_ge hb, IE.sparse, h8, h9]
      rw [hz]
      exact t017_sz_pos b nn hn)
    (fun b nn hn q hq => by
      have hb : 7 ≤ b := Sizes.ofList_le hn
      have hz : t017_s3_g.postOffs b = IE.lit 0 := by
        simp [t017_s3_g, IE.split_ge hb, IE.sparse]
      rw [hz]
      exact t017_sz_pos b nn hn)

def t017_chain (α : Type) [ExactScalar α] : List (Stage α) := [⟨t017_s0_g.prog t017_s0_block t017_s0_nkb, t017_s0_g.spec (α := α), 7⟩, ⟨t017_s1_g.prog t017_s1_block t017_s1_nkb, t017_s1_g.spec (α := α), 8⟩, ⟨t017_s2_g.prog t017_s2_block t017_s2_nkb, t017_s2_g.spec (α := α), 9⟩, ⟨t017_s3_g.prog t017_s3_block t017_s3_nkb, t017_s3_g.spec (α := α), 10⟩]

theorem t017_imp {α : Type} [ExactScalar α] :
    ∀ st ∈ t017_chain α, Implements st.prog st.spec :=
  List.forall_mem_cons.mpr ⟨t017_s0_impl,
  List.forall_mem_cons.mpr ⟨t017_s1_impl,
  List.forall_mem_cons.mpr ⟨t017_s2_impl,
  List.forall_mem_cons.mpr ⟨t017_s3_impl,
  List.forall_mem_nil _⟩⟩⟩⟩

theorem t017_szok {α : Type} [ExactScalar α] :
    ∀ st ∈ t017_chain α, t017_sz st.out = some st.spec.outSize :=
  List.forall_mem_cons.mpr ⟨rfl,
  List.forall_mem_cons.mpr ⟨rfl,
  List.forall_mem_cons.mpr ⟨rfl,
  List.forall_mem_cons.mpr ⟨rfl,
  List.forall_mem_nil _⟩⟩⟩⟩

theorem t017_loc {α : Type} [ExactScalar α] :
    ∀ st ∈ t017_chain α, SpecLocal t017_sz st.spec :=
  List.forall_mem_cons.mpr ⟨t017_s0_loc,
  List.forall_mem_cons.mpr ⟨t017_s1_loc,
  List.forall_mem_cons.mpr ⟨t017_s2_loc,
  List.forall_mem_cons.mpr ⟨t017_s3_loc,
  List.forall_mem_nil _⟩⟩⟩⟩

/-- Correctness certificate for t017: the whole chain. -/
theorem t017_correct {α : Type} [ExactScalar α] :
    ∀ (f : Nat → Buf α) (m : Mem α),
      Compat (sizesAfter (t017_chain α) emptySizes)
        (runStages (t017_chain α) f m) (specStages (t017_chain α) f) :=
  fun f m => stages_correct t017_sz (t017_chain α) emptySizes f f m
    (Compat.refl _ _) (emptySizes_sub t017_sz)
    t017_szok t017_imp t017_loc

def t017_s0_kernel : ReduceKernel :=
  { name := "t017_s0", arity := 7, block := t017_s0_block, nkb := t017_s0_nkb, nout := 12582912, init := FE.zeroC, step := t017_s0_g.step t017_s0_block, stored := t017_s0_g.stored t017_s0_block }
def t017_s1_kernel : ReduceKernel :=
  { name := "t017_s1", arity := 8, block := t017_s1_block, nkb := t017_s1_nkb, nout := 134217728, init := FE.zeroC, step := t017_s1_g.step t017_s1_block, stored := t017_s1_g.stored t017_s1_block }
def t017_s2_kernel : ReduceKernel :=
  { name := "t017_s2", arity := 9, block := t017_s2_block, nkb := t017_s2_nkb, nout := 134217728, init := FE.zeroC, step := t017_s2_g.step t017_s2_block, stored := t017_s2_g.stored t017_s2_block }
def t017_s3_kernel : ReduceKernel :=
  { name := "t017_s3", arity := 10, block := t017_s3_block, nkb := t017_s3_nkb, nout := 268435456, init := FE.zeroC, step := t017_s3_g.step t017_s3_block, stored := t017_s3_g.stored t017_s3_block }
def t017_kernel : ChainKernel :=
  { name := "t017", arity := 7, sizes := [12582912, 134217728, 134217728, 268435456],
    stages := [t017_s0_kernel, t017_s1_kernel, t017_s2_kernel, t017_s3_kernel] }

-- t018: a chain of 38 stage(s), 53 input buffer(s)
--   fused features.1 into stage 0; fused features.3.squeeze_activation into stage 2; fused features.3.expand1x1_activation into stage 3
def t018_sizes : List Nat := [196635648, 48771072, 8128512, 32514048, 32514048, 65028096, 8128512, 32514048, 32514048, 65028096, 16257024, 65028096, 65028096, 130056192, 32514048, 4064256, 16257024, 16257024, 32514048, 6096384, 24385536, 24385536, 48771072, 6096384, 24385536, 24385536, 48771072, 8128512, 32514048, 32514048, 65028096, 15745024, 1968128, 7872512, 7872512, 15745024, 30752000, 32000]
def t018_sz : Sizes := Sizes.ofList 53 t018_sizes
theorem t018_sz_pos : ∀ b n, t018_sz b = some n → 0 < n :=
  Sizes.ofList_pos (by decide)

def t018_s0_g : GenRed :=
  { nout := 196635648, K := 147
  , offs := (IE.split 53 (IE.sparse [(0, (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 6144864)) (IE.lit 3)) (IE.divi IE.rk (IE.lit 49))) (IE.lit 512)) (IE.add (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 253)) (IE.lit 253)) (IE.lit 2)) (IE.modi (IE.divi IE.rk (IE.lit 7)) (IE.lit 7)))) (IE.lit 512)) (IE.add (IE.mul (IE.modi (IE.pid 0) (IE.lit 253)) (IE.lit 2)) (IE.modi IE.rk (IE.lit 7))))), (1, (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 64009)) (IE.lit 96)) (IE.lit 3)) (IE.divi IE.rk (IE.lit 49))) (IE.lit 7)) (IE.modi (IE.divi IE.rk (IE.lit 7)) (IE.lit 7))) (IE.lit 7)) (IE.modi IE.rk (IE.lit 7))))]) (IE.sparse []))
  , inRange := (BE.and (BE.cmp .lt (IE.add (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 253)) (IE.lit 253)) (IE.lit 2)) (IE.modi (IE.divi IE.rk (IE.lit 7)) (IE.lit 7))) (IE.lit 512)) (BE.cmp .lt (IE.add (IE.mul (IE.modi (IE.pid 0) (IE.lit 253)) (IE.lit 2)) (IE.modi IE.rk (IE.lit 7))) (IE.lit 512)))
  , body := (SE.bin .mul (SE.inp 0) (SE.inp 1))
  , postOffs := (IE.split 53 (IE.sparse [(2, (IE.modi (IE.divi (IE.pid 0) (IE.lit 64009)) (IE.lit 96)))]) (IE.sparse []))
  , post := (SE.bin .max (SE.bin .add (SE.inp 0) (SE.inp 3)) (SE.lit false 0 1))
  , outGuard := BE.tt
  , nInp := 54, idxSlot := 1048576 }
def t018_s0_block : Nat := 128
def t018_s0_nkb : Nat := 2

theorem t018_s0_wf : t018_s0_g.Wf :=
  { offs_ok := IE.qkOnly_split (IE.qkOnly_sparse _ (by decide)) (IE.qkOnly_sparse _ (by decide))
  , post_ok := IE.qkOnly_split (IE.qkOnly_sparse _ (by decide)) (IE.qkOnly_sparse _ (by decide))
  , range_ok := by decide
  , guard_ok := by decide }

theorem t018_s0_impl {α : Type} [ExactScalar α] :
    Implements (t018_s0_g.prog t018_s0_block t018_s0_nkb) (t018_s0_g.spec (α := α)) :=
  GenRed.prog_implements t018_s0_g t018_s0_block t018_s0_nkb t018_s0_wf (by decide) (by decide)

def t018_s1_g : MaxRed :=
  { nout := 48771072, K := 9
  , offs := (IE.split 53 (IE.sparse []) (IE.sparse [(53, (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 1524096)) (IE.lit 96)) (IE.modi (IE.divi (IE.pid 0) (IE.lit 15876)) (IE.lit 96))) (IE.lit 253)) (IE.sub (IE.add (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 126)) (IE.lit 126)) (IE.lit 2)) (IE.sub (IE.add (IE.divi IE.rk (IE.lit 3)) (IE.sub (IE.sub (IE.lit 0) (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 126)) (IE.lit 126)) (IE.lit 2))) (IE.divi IE.rk (IE.lit 3)))) (IE.sub (IE.add (IE.divi IE.rk (IE.lit 3)) (IE.sub (IE.sub (IE.lit 0) (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 126)) (IE.lit 126)) (IE.lit 2))) (IE.divi IE.rk (IE.lit 3)))) (IE.sub (IE.lit 252) (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 126)) (IE.lit 126)) (IE.lit 2)))))) (IE.sub (IE.add (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 126)) (IE.lit 126)) (IE.lit 2)) (IE.sub (IE.add (IE.divi IE.rk (IE.lit 3)) (IE.sub (IE.sub (IE.lit 0) (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 126)) (IE.lit 126)) (IE.lit 2))) (IE.divi IE.rk (IE.lit 3)))) (IE.sub (IE.add (IE.divi IE.rk (IE.lit 3)) (IE.sub (IE.sub (IE.lit 0) (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 126)) (IE.lit 126)) (IE.lit 2))) (IE.divi IE.rk (IE.lit 3)))) (IE.sub (IE.lit 252) (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 126)) (IE.lit 126)) (IE.lit 2)))))) (IE.lit 252)))) (IE.lit 253)) (IE.sub (IE.add (IE.mul (IE.modi (IE.pid 0) (IE.lit 126)) (IE.lit 2)) (IE.sub (IE.add (IE.modi IE.rk (IE.lit 3)) (IE.sub (IE.sub (IE.lit 0) (IE.mul (IE.modi (IE.pid 0) (IE.lit 126)) (IE.lit 2))) (IE.modi IE.rk (IE.lit 3)))) (IE.sub (IE.add (IE.modi IE.rk (IE.lit 3)) (IE.sub (IE.sub (IE.lit 0) (IE.mul (IE.modi (IE.pid 0) (IE.lit 126)) (IE.lit 2))) (IE.modi IE.rk (IE.lit 3)))) (IE.sub (IE.lit 252) (IE.mul (IE.modi (IE.pid 0) (IE.lit 126)) (IE.lit 2)))))) (IE.sub (IE.add (IE.mul (IE.modi (IE.pid 0) (IE.lit 126)) (IE.lit 2)) (IE.sub (IE.add (IE.modi IE.rk (IE.lit 3)) (IE.sub (IE.sub (IE.lit 0) (IE.mul (IE.modi (IE.pid 0) (IE.lit 126)) (IE.lit 2))) (IE.modi IE.rk (IE.lit 3)))) (IE.sub (IE.add (IE.modi IE.rk (IE.lit 3)) (IE.sub (IE.sub (IE.lit 0) (IE.mul (IE.modi (IE.pid 0) (IE.lit 126)) (IE.lit 2))) (IE.modi IE.rk (IE.lit 3)))) (IE.sub (IE.lit 252) (IE.mul (IE.modi (IE.pid 0) (IE.lit 126)) (IE.lit 2)))))) (IE.lit 252)))))]))
  , body := (SE.inp 53)
  , postOffs := (IE.split 53 (IE.sparse []) (IE.sparse []))
  , post := (SE.inp 0)
  , nInp := 55, idxSlot := 1048576 }
def t018_s1_block : Nat := 8
def t018_s1_nkb : Nat := 2

theorem t018_s1_wf : t018_s1_g.Wf :=
  { offs_ok := IE.qkOnly_split (IE.qkOnly_sparse _ (by decide)) (IE.qkOnly_sparse _ (by decide))
  , post_ok := IE.qkOnly_split (IE.qkOnly_sparse _ (by decide)) (IE.qkOnly_sparse _ (by decide)) }

theorem t018_s1_impl {α : Type} [ExactScalar α] :
    Implements (t018_s1_g.prog t018_s1_block t018_s1_nkb) (t018_s1_g.spec (α := α)) :=
  MaxRed.prog_implements t018_s1_g t018_s1_block t018_s1_nkb t018_s1_wf (by decide) (by decide) (by decide)


def t018_s2_g : GenRed :=
  { nout := 8128512, K := 96
  , offs := (IE.split 53 (IE.sparse [(3, (IE.add (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 15876)) (IE.lit 16)) (IE.lit 96)) IE.rk))]) (IE.sparse [(54, (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 254016)) (IE.lit 96)) IE.rk) (IE.lit 126)) (IE.modi (IE.divi (IE.pid 0) (IE.lit 126)) (IE.lit 126))) (IE.lit 126)) (IE.modi (IE.pid 0) (IE.lit 126))))]))
  , inRange := (BE.and (BE.cmp .lt (IE.modi (IE.divi (IE.pid 0) (IE.lit 126)) (IE.lit 126)) (IE.lit 126)) (BE.cmp .lt (IE.modi (IE.pid 0) (IE.lit 126)) (IE.lit 126)))
  , body := (SE.bin .mul (SE.inp 54) (SE.inp 3))
  , postOffs := (IE.split 53 (IE.sparse [(4, (IE.modi (IE.divi (IE.pid 0) (IE.lit 15876)) (IE.lit 16)))]) (IE.sparse []))
  , post := (SE.bin .max (SE.bin .add (SE.inp 0) (SE.inp 5)) (SE.lit false 0 1))
  , outGuard := BE.tt
  , nInp := 56, idxSlot := 1048576 }
def t018_s2_block : Nat := 64
def t018_s2_nkb : Nat := 2

theorem t018_s2_wf : t018_s2_g.Wf :=
  { offs_ok := IE.qkOnly_split (IE.qkOnly_sparse _ (by decide)) (IE.qkOnly_sparse _ (by decide))
  , post_ok := IE.qkOnly_split (IE.qkOnly_sparse _ (by decide)) (IE.qkOnly_sparse _ (by decide))
  , range_ok := by decide
  , guard_ok := by decide }

theorem t018_s2_impl {α : Type} [ExactScalar α] :
    Implements (t018_s2_g.prog t018_s2_block t018_s2_nkb) (t018_s2_g.spec (α := α)) :=
  GenRed.prog_implements t018_s2_g t018_s2_block t018_s2_nkb t018_s2_wf (by decide) (by decide)

def t018_s3_g : GenRed :=
  { nout := 32514048, K := 16
  , offs := (IE.split 53 (IE.sparse [(5, (IE.add (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 15876)) (IE.lit 64)) (IE.lit 16)) IE.rk))]) (IE.sparse [(55, (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 1016064)) (IE.lit 16)) IE.rk) (IE.lit 126)) (IE.modi (IE.divi (IE.pid 0) (IE.lit 126)) (IE.lit 126))) (IE.lit 126)) (IE.modi (IE.pid 0) (IE.lit 126))))]))
  , inRange := (BE.and (BE.cmp .lt (IE.modi (IE.divi (IE.pid 0) (IE.lit 126)) (IE.lit 126)) (IE.lit 126)) (BE.cmp .lt (IE.modi (IE.pid 0) (IE.lit 126)) (IE.lit 126)))
  , body := (SE.bin .mul (SE.inp 55) (SE.inp 5))
  , postOffs := (IE.split 53 (IE.sparse [(6, (IE.modi (IE.divi (IE.pid 0) (IE.lit 15876)) (IE.lit 64)))]) (IE.sparse []))
  , post := (SE.bin .max (SE.bin .add (SE.inp 0) (SE.inp 7)) (SE.lit false 0 1))
  , outGuard := BE.tt
  , nInp := 57, idxSlot := 1048576 }
def t018_s3_block : Nat := 16
def t018_s3_nkb : Nat := 1

theorem t018_s3_wf : t018_s3_g.Wf :=
  { offs_ok := IE.qkOnly_split (IE.qkOnly_sparse _ (by decide)) (IE.qkOnly_sparse _ (by decide))
  , post_ok := IE.qkOnly_split (IE.qkOnly_sparse _ (by decide)) (IE.qkOnly_sparse _ (by decide))
  , range_ok := by decide
  , guard_ok := by decide }

theorem t018_s3_impl {α : Type} [ExactScalar α] :
    Implements (t018_s3_g.prog t018_s3_block t018_s3_nkb) (t018_s3_g.spec (α := α)) :=
  GenRed.prog_implements t018_s3_g t018_s3_block t018_s3_nkb t018_s3_wf (by decide) (by decide)

def t018_s4_g : GenRed :=
  { nout := 32514048, K := 144
  , offs := (IE.split 53 (IE.sparse [(7, (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 15876)) (IE.lit 64)) (IE.lit 16)) (IE.divi IE.rk (IE.lit 9))) (IE.lit 3)) (IE.modi (IE.divi IE.rk (IE.lit 3)) (IE.lit 3))) (IE.lit 3)) (IE.modi IE.rk (IE.lit 3))))]) (IE.sparse [(55, (IE.sub (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 1016064)) (IE.lit 16)) (IE.divi IE.rk (IE.lit 9))) (IE.lit 126)) (IE.sub (IE.add (IE.modi (IE.divi (IE.pid 0) (IE.lit 126)) (IE.lit 126)) (IE.modi (IE.divi IE.rk (IE.lit 3)) (IE.lit 3))) (IE.lit 1))) (IE.lit 126)) (IE.sub (IE.add (IE.modi (IE.pid 0) (IE.lit 126)) (IE.modi IE.rk (IE.lit 3))) (IE.lit 1))) (IE.sub (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 1016064)) (IE.lit 16)) (IE.divi IE.rk (IE.lit 9))) (IE.lit 126)) (IE.sub (IE.add (IE.modi (IE.divi (IE.pid 0) (IE.lit 126)) (IE.lit 126)) (IE.modi (IE.divi IE.rk (IE.lit 3)) (IE.lit 3))) (IE.lit 1))) (IE.lit 126)) (IE.sub (IE.add (IE.modi (IE.pid 0) (IE.lit 126)) (IE.modi IE.rk (IE.lit 3))) (IE.lit 1))) (IE.lit 8128511))))]))
  , inRange := (BE.and (BE.and (BE.and (BE.cmp .le (IE.lit 1) (IE.add (IE.modi (IE.divi (IE.pid 0) (IE.lit 126)) (IE.lit 126)) (IE.modi (IE.divi IE.rk (IE.lit 3)) (IE.lit 3)))) (BE.cmp .lt (IE.add (IE.modi (IE.divi (IE.pid 0) (IE.lit 126)) (IE.lit 126)) (IE.modi (IE.divi IE.rk (IE.lit 3)) (IE.lit 3))) (IE.lit 127))) (BE.cmp .le (IE.lit 1) (IE.add (IE.modi (IE.pid 0) (IE.lit 126)) (IE.modi IE.rk (IE.lit 3))))) (BE.cmp .lt (IE.add (IE.modi (IE.pid 0) (IE.lit 126)) (IE.modi IE.rk (IE.lit 3))) (IE.lit 127)))
  , body := (SE.bin .mul (SE.inp 55) (SE.inp 7))
  , postOffs := (IE.split 53 (IE.sparse [(8, (IE.modi (IE.divi (IE.pid 0) (IE.lit 15876)) (IE.lit 64)))]) (IE.sparse []))
  , post := (SE.bin .max (SE.bin .add (SE.inp 0) (SE.inp 9)) (SE.lit false 0 1))
  , outGuard := BE.tt
  , nInp := 58, idxSlot := 1048576 }
def t018_s4_block : Nat := 128
def t018_s4_nkb : Nat := 2

theorem t018_s4_wf : t018_s4_g.Wf :=
  { offs_ok := IE.qkOnly_split (IE.qkOnly_sparse _ (by decide)) (IE.qkOnly_sparse _ (by decide))
  , post_ok := IE.qkOnly_split (IE.qkOnly_sparse _ (by decide)) (IE.qkOnly_sparse _ (by decide))
  , range_ok := by decide
  , guard_ok := by decide }

theorem t018_s4_impl {α : Type} [ExactScalar α] :
    Implements (t018_s4_g.prog t018_s4_block t018_s4_nkb) (t018_s4_g.spec (α := α)) :=
  GenRed.prog_implements t018_s4_g t018_s4_block t018_s4_nkb t018_s4_wf (by decide) (by decide)

def t018_s5_g : GenRed :=
  { nout := 65028096, K := 2
  , offs := (IE.split 53 (IE.sparse []) (IE.sparse [(56, (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 2032128)) (IE.lit 64)) (IE.sub (IE.modi (IE.divi (IE.pid 0) (IE.lit 15876)) (IE.lit 128)) (IE.sub (IE.modi (IE.divi (IE.pid 0) (IE.lit 15876)) (IE.lit 128)) (IE.lit 63)))) (IE.lit 126)) (IE.modi (IE.divi (IE.pid 0) (IE.lit 126)) (IE.lit 126))) (IE.lit 126)) (IE.modi (IE.pid 0) (IE.lit 126)))), (57, (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 2032128)) (IE.lit 64)) (IE.sub (IE.sub (IE.modi (IE.divi (IE.pid 0) (IE.lit 15876)) (IE.lit 128)) (IE.lit 64)) (IE.sub (IE.sub (IE.modi (IE.divi (IE.pid 0) (IE.lit 15876)) (IE.lit 128)) (IE.lit 64)) (IE.lit 63)))) (IE.lit 126)) (IE.modi (IE.divi (IE.pid 0) (IE.lit 126)) (IE.lit 126))) (IE.lit 126)) (IE.modi (IE.pid 0) (IE.lit 126))))]))
  , inRange := (BE.or (BE.and (BE.and (BE.cmp .eq IE.rk (IE.lit 0)) (BE.cmp .le (IE.lit 0) (IE.modi (IE.divi (IE.pid 0) (IE.lit 15876)) (IE.lit 128)))) (BE.cmp .lt (IE.modi (IE.divi (IE.pid 0) (IE.lit 15876)) (IE.lit 128)) (IE.lit 64))) (BE.and (BE.and (BE.cmp .eq IE.rk (IE.lit 1)) (BE.cmp .le (IE.lit 64) (IE.modi (IE.divi (IE.pid 0) (IE.lit 15876)) (IE.lit 128)))) (BE.cmp .lt (IE.modi (IE.divi (IE.pid 0) (IE.lit 15876)) (IE.lit 128)) (IE.lit 128))))
  , body := (SE.selLe (SE.inp 59) (SE.lit false 1 2) (SE.inp 56) (SE.inp 57))
  , postOffs := (IE.split 53 (IE.sparse []) (IE.sparse []))
  , post := (SE.inp 0)
  , outGuard := BE.tt
  , nInp := 59, idxSlot := 59 }
def t018_s5_block : Nat := 2
def t018_s5_nkb : Nat := 1

theorem t018_s5_wf : t018_s5_g.Wf :=
  { offs_ok := IE.qkOnly_split (IE.qkOnly_sparse _ (by decide)) (IE.qkOnly_sparse _ (by decide))
  , post_ok := IE.qkOnly_split (IE.qkOnly_sparse _ (by decide)) (IE.qkOnly_sparse _ (by decide))
  , range_ok := by decide
  , guard_ok := by decide }

theorem t018_s5_impl {α : Type} [ExactScalar α] :
    Implements (t018_s5_g.prog t018_s5_block t018_s5_nkb) (t018_s5_g.spec (α := α)) :=
  GenRed.prog_implements t018_s5_g t018_s5_block t018_s5_nkb t018_s5_wf (by decide) (by decide)

def t018_s6_g : GenRed :=
  { nout := 8128512, K := 128
  , offs := (IE.split 53 (IE.sparse [(9, (IE.add (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 15876)) (IE.lit 16)) (IE.lit 128)) IE.rk))]) (IE.sparse [(58, (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 254016)) (IE.lit 128)) IE.rk) (IE.lit 126)) (IE.modi (IE.divi (IE.pid 0) (IE.lit 126)) (IE.lit 126))) (IE.lit 126)) (IE.modi (IE.pid 0) (IE.lit 126))))]))
  , inRange := (BE.and (BE.cmp .lt (IE.modi (IE.divi (IE.pid 0) (IE.lit 126)) (IE.lit 126)) (IE.lit 126)) (BE.cmp .lt (IE.modi (IE.pid 0) (IE.lit 126)) (IE.lit 126)))
  , body := (SE.bin .mul (SE.inp 58) (SE.inp 9))
  , postOffs := (IE.split 53 (IE.sparse [(10, (IE.modi (IE.divi (IE.pid 0) (IE.lit 15876)) (IE.lit 16)))]) (IE.sparse []))
  , post := (SE.bin .max (SE.bin .add (SE.inp 0) (SE.inp 11)) (SE.lit false 0 1))
  , outGuard := BE.tt
  , nInp := 60, idxSlot := 1048576 }
def t018_s6_block : Nat := 128
def t018_s6_nkb : Nat := 1

theorem t018_s6_wf : t018_s6_g.Wf :=
  { offs_ok := IE.qkOnly_split (IE.qkOnly_sparse _ (by decide)) (IE.qkOnly_sparse _ (by decide))
  , post_ok := IE.qkOnly_split (IE.qkOnly_sparse _ (by decide)) (IE.qkOnly_sparse _ (by decide))
  , range_ok := by decide
  , guard_ok := by decide }

theorem t018_s6_impl {α : Type} [ExactScalar α] :
    Implements (t018_s6_g.prog t018_s6_block t018_s6_nkb) (t018_s6_g.spec (α := α)) :=
  GenRed.prog_implements t018_s6_g t018_s6_block t018_s6_nkb t018_s6_wf (by decide) (by decide)

def t018_s7_g : GenRed :=
  { nout := 32514048, K := 16
  , offs := (IE.split 53 (IE.sparse [(11, (IE.add (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 15876)) (IE.lit 64)) (IE.lit 16)) IE.rk))]) (IE.sparse [(59, (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 1016064)) (IE.lit 16)) IE.rk) (IE.lit 126)) (IE.modi (IE.divi (IE.pid 0) (IE.lit 126)) (IE.lit 126))) (IE.lit 126)) (IE.modi (IE.pid 0) (IE.lit 126))))]))
  , inRange := (BE.and (BE.cmp .lt (IE.modi (IE.divi (IE.pid 0) (IE.lit 126)) (IE.lit 126)) (IE.lit 126)) (BE.cmp .lt (IE.modi (IE.pid 0) (IE.lit 126)) (IE.lit 126)))
  , body := (SE.bin .mul (SE.inp 59) (SE.inp 11))
  , postOffs := (IE.split 53 (IE.sparse [(12, (IE.modi (IE.divi (IE.pid 0) (IE.lit 15876)) (IE.lit 64)))]) (IE.sparse []))
  , post := (SE.bin .max (SE.bin .add (SE.inp 0) (SE.inp 13)) (SE.lit false 0 1))
  , outGuard := BE.tt
  , nInp := 61, idxSlot := 1048576 }
def t018_s7_block : Nat := 16
def t018_s7_nkb : Nat := 1

theorem t018_s7_wf : t018_s7_g.Wf :=
  { offs_ok := IE.qkOnly_split (IE.qkOnly_sparse _ (by decide)) (IE.qkOnly_sparse _ (by decide))
  , post_ok := IE.qkOnly_split (IE.qkOnly_sparse _ (by decide)) (IE.qkOnly_sparse _ (by decide))
  , range_ok := by decide
  , guard_ok := by decide }

theorem t018_s7_impl {α : Type} [ExactScalar α] :
    Implements (t018_s7_g.prog t018_s7_block t018_s7_nkb) (t018_s7_g.spec (α := α)) :=
  GenRed.prog_implements t018_s7_g t018_s7_block t018_s7_nkb t018_s7_wf (by decide) (by decide)

def t018_s8_g : GenRed :=
  { nout := 32514048, K := 144
  , offs := (IE.split 53 (IE.sparse [(13, (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 15876)) (IE.lit 64)) (IE.lit 16)) (IE.divi IE.rk (IE.lit 9))) (IE.lit 3)) (IE.modi (IE.divi IE.rk (IE.lit 3)) (IE.lit 3))) (IE.lit 3)) (IE.modi IE.rk (IE.lit 3))))]) (IE.sparse [(59, (IE.sub (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 1016064)) (IE.lit 16)) (IE.divi IE.rk (IE.lit 9))) (IE.lit 126)) (IE.sub (IE.add (IE.modi (IE.divi (IE.pid 0) (IE.lit 126)) (IE.lit 126)) (IE.modi (IE.divi IE.rk (IE.lit 3)) (IE.lit 3))) (IE.lit 1))) (IE.lit 126)) (IE.sub (IE.add (IE.modi (IE.pid 0) (IE.lit 126)) (IE.modi IE.rk (IE.lit 3))) (IE.lit 1))) (IE.sub (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 1016064)) (IE.lit 16)) (IE.divi IE.rk (IE.lit 9))) (IE.lit 126)) (IE.sub (IE.add (IE.modi (IE.divi (IE.pid 0) (IE.lit 126)) (IE.lit 126)) (IE.modi (IE.divi IE.rk (IE.lit 3)) (IE.lit 3))) (IE.lit 1))) (IE.lit 126)) (IE.sub (IE.add (IE.modi (IE.pid 0) (IE.lit 126)) (IE.modi IE.rk (IE.lit 3))) (IE.lit 1))) (IE.lit 8128511))))]))
  , inRange := (BE.and (BE.and (BE.and (BE.cmp .le (IE.lit 1) (IE.add (IE.modi (IE.divi (IE.pid 0) (IE.lit 126)) (IE.lit 126)) (IE.modi (IE.divi IE.rk (IE.lit 3)) (IE.lit 3)))) (BE.cmp .lt (IE.add (IE.modi (IE.divi (IE.pid 0) (IE.lit 126)) (IE.lit 126)) (IE.modi (IE.divi IE.rk (IE.lit 3)) (IE.lit 3))) (IE.lit 127))) (BE.cmp .le (IE.lit 1) (IE.add (IE.modi (IE.pid 0) (IE.lit 126)) (IE.modi IE.rk (IE.lit 3))))) (BE.cmp .lt (IE.add (IE.modi (IE.pid 0) (IE.lit 126)) (IE.modi IE.rk (IE.lit 3))) (IE.lit 127)))
  , body := (SE.bin .mul (SE.inp 59) (SE.inp 13))
  , postOffs := (IE.split 53 (IE.sparse [(14, (IE.modi (IE.divi (IE.pid 0) (IE.lit 15876)) (IE.lit 64)))]) (IE.sparse []))
  , post := (SE.bin .max (SE.bin .add (SE.inp 0) (SE.inp 15)) (SE.lit false 0 1))
  , outGuard := BE.tt
  , nInp := 62, idxSlot := 1048576 }
def t018_s8_block : Nat := 128
def t018_s8_nkb : Nat := 2

theorem t018_s8_wf : t018_s8_g.Wf :=
  { offs_ok := IE.qkOnly_split (IE.qkOnly_sparse _ (by decide)) (IE.qkOnly_sparse _ (by decide))
  , post_ok := IE.qkOnly_split (IE.qkOnly_sparse _ (by decide)) (IE.qkOnly_sparse _ (by decide))
  , range_ok := by decide
  , guard_ok := by decide }

theorem t018_s8_impl {α : Type} [ExactScalar α] :
    Implements (t018_s8_g.prog t018_s8_block t018_s8_nkb) (t018_s8_g.spec (α := α)) :=
  GenRed.prog_implements t018_s8_g t018_s8_block t018_s8_nkb t018_s8_wf (by decide) (by decide)

def t018_s9_g : GenRed :=
  { nout := 65028096, K := 2
  , offs := (IE.split 53 (IE.sparse []) (IE.sparse [(60, (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 2032128)) (IE.lit 64)) (IE.sub (IE.modi (IE.divi (IE.pid 0) (IE.lit 15876)) (IE.lit 128)) (IE.sub (IE.modi (IE.divi (IE.pid 0) (IE.lit 15876)) (IE.lit 128)) (IE.lit 63)))) (IE.lit 126)) (IE.modi (IE.divi (IE.pid 0) (IE.lit 126)) (IE.lit 126))) (IE.lit 126)) (IE.modi (IE.pid 0) (IE.lit 126)))), (61, (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 2032128)) (IE.lit 64)) (IE.sub (IE.sub (IE.modi (IE.divi (IE.pid 0) (IE.lit 15876)) (IE.lit 128)) (IE.lit 64)) (IE.sub (IE.sub (IE.modi (IE.divi (IE.pid 0) (IE.lit 15876)) (IE.lit 128)) (IE.lit 64)) (IE.lit 63)))) (IE.lit 126)) (IE.modi (IE.divi (IE.pid 0) (IE.lit 126)) (IE.lit 126))) (IE.lit 126)) (IE.modi (IE.pid 0) (IE.lit 126))))]))
  , inRange := (BE.or (BE.and (BE.and (BE.cmp .eq IE.rk (IE.lit 0)) (BE.cmp .le (IE.lit 0) (IE.modi (IE.divi (IE.pid 0) (IE.lit 15876)) (IE.lit 128)))) (BE.cmp .lt (IE.modi (IE.divi (IE.pid 0) (IE.lit 15876)) (IE.lit 128)) (IE.lit 64))) (BE.and (BE.and (BE.cmp .eq IE.rk (IE.lit 1)) (BE.cmp .le (IE.lit 64) (IE.modi (IE.divi (IE.pid 0) (IE.lit 15876)) (IE.lit 128)))) (BE.cmp .lt (IE.modi (IE.divi (IE.pid 0) (IE.lit 15876)) (IE.lit 128)) (IE.lit 128))))
  , body := (SE.selLe (SE.inp 63) (SE.lit false 1 2) (SE.inp 60) (SE.inp 61))
  , postOffs := (IE.split 53 (IE.sparse []) (IE.sparse []))
  , post := (SE.inp 0)
  , outGuard := BE.tt
  , nInp := 63, idxSlot := 63 }
def t018_s9_block : Nat := 2
def t018_s9_nkb : Nat := 1

theorem t018_s9_wf : t018_s9_g.Wf :=
  { offs_ok := IE.qkOnly_split (IE.qkOnly_sparse _ (by decide)) (IE.qkOnly_sparse _ (by decide))
  , post_ok := IE.qkOnly_split (IE.qkOnly_sparse _ (by decide)) (IE.qkOnly_sparse _ (by decide))
  , range_ok := by decide
  , guard_ok := by decide }

theorem t018_s9_impl {α : Type} [ExactScalar α] :
    Implements (t018_s9_g.prog t018_s9_block t018_s9_nkb) (t018_s9_g.spec (α := α)) :=
  GenRed.prog_implements t018_s9_g t018_s9_block t018_s9_nkb t018_s9_wf (by decide) (by decide)

def t018_s10_g : GenRed :=
  { nout := 16257024, K := 128
  , offs := (IE.split 53 (IE.sparse [(15, (IE.add (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 15876)) (IE.lit 32)) (IE.lit 128)) IE.rk))]) (IE.sparse [(62, (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 508032)) (IE.lit 128)) IE.rk) (IE.lit 126)) (IE.modi (IE.divi (IE.pid 0) (IE.lit 126)) (IE.lit 126))) (IE.lit 126)) (IE.modi (IE.pid 0) (IE.lit 126))))]))
  , inRange := (BE.and (BE.cmp .lt (IE.modi (IE.divi (IE.pid 0) (IE.lit 126)) (IE.lit 126)) (IE.lit 126)) (BE.cmp .lt (IE.modi (IE.pid 0) (IE.lit 126)) (IE.lit 126)))
  , body := (SE.bin .mul (SE.inp 62) (SE.inp 15))
  , postOffs := (IE.split 53 (IE.sparse [(16, (IE.modi (IE.divi (IE.pid 0) (IE.lit 15876)) (IE.lit 32)))]) (IE.sparse []))
  , post := (SE.bin .max (SE.bin .add (SE.inp 0) (SE.inp 17)) (SE.lit false 0 1))
  , outGuard := BE.tt
  , nInp := 64, idxSlot := 1048576 }
def t018_s10_block : Nat := 128
def t018_s10_nkb : Nat := 1

theorem t018_s10_wf : t018_s10_g.Wf :=
  { offs_ok := IE.qkOnly_split (IE.qkOnly_sparse _ (by decide)) (IE.qkOnly_sparse _ (by decide))
  , post_ok := IE.qkOnly_split (IE.qkOnly_sparse _ (by decide)) (IE.qkOnly_sparse _ (by decide))
  , range_ok := by decide
  , guard_ok := by decide }

theorem t018_s10_impl {α : Type} [ExactScalar α] :
    Implements (t018_s10_g.prog t018_s10_block t018_s10_nkb) (t018_s10_g.spec (α := α)) :=
  GenRed.prog_implements t018_s10_g t018_s10_block t018_s10_nkb t018_s10_wf (by decide) (by decide)

def t018_s11_g : GenRed :=
  { nout := 65028096, K := 32
  , offs := (IE.split 53 (IE.sparse [(17, (IE.add (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 15876)) (IE.lit 128)) (IE.lit 32)) IE.rk))]) (IE.sparse [(63, (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 2032128)) (IE.lit 32)) IE.rk) (IE.lit 126)) (IE.modi (IE.divi (IE.pid 0) (IE.lit 126)) (IE.lit 126))) (IE.lit 126)) (IE.modi (IE.pid 0) (IE.lit 126))))]))
  , inRange := (BE.and (BE.cmp .lt (IE.modi (IE.divi (IE.pid 0) (IE.lit 126)) (IE.lit 126)) (IE.lit 126)) (BE.cmp .lt (IE.modi (IE.pid 0) (IE.lit 126)) (IE.lit 126)))
  , body := (SE.bin .mul (SE.inp 63) (SE.inp 17))
  , postOffs := (IE.split 53 (IE.sparse [(18, (IE.modi (IE.divi (IE.pid 0) (IE.lit 15876)) (IE.lit 128)))]) (IE.sparse []))
  , post := (SE.bin .max (SE.bin .add (SE.inp 0) (SE.inp 19)) (SE.lit false 0 1))
  , outGuard := BE.tt
  , nInp := 65, idxSlot := 1048576 }
def t018_s11_block : Nat := 32
def t018_s11_nkb : Nat := 1

theorem t018_s11_wf : t018_s11_g.Wf :=
  { offs_ok := IE.qkOnly_split (IE.qkOnly_sparse _ (by decide)) (IE.qkOnly_sparse _ (by decide))
  , post_ok := IE.qkOnly_split (IE.qkOnly_sparse _ (by decide)) (IE.qkOnly_sparse _ (by decide))
  , range_ok := by decide
  , guard_ok := by decide }

theorem t018_s11_impl {α : Type} [ExactScalar α] :
    Implements (t018_s11_g.prog t018_s11_block t018_s11_nkb) (t018_s11_g.spec (α := α)) :=
  GenRed.prog_implements t018_s11_g t018_s11_block t018_s11_nkb t018_s11_wf (by decide) (by decide)

def t018_s12_g : GenRed :=
  { nout := 65028096, K := 288
  , offs := (IE.split 53 (IE.sparse [(19, (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 15876)) (IE.lit 128)) (IE.lit 32)) (IE.divi IE.rk (IE.lit 9))) (IE.lit 3)) (IE.modi (IE.divi IE.rk (IE.lit 3)) (IE.lit 3))) (IE.lit 3)) (IE.modi IE.rk (IE.lit 3))))]) (IE.sparse [(63, (IE.sub (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 2032128)) (IE.lit 32)) (IE.divi IE.rk (IE.lit 9))) (IE.lit 126)) (IE.sub (IE.add (IE.modi (IE.divi (IE.pid 0) (IE.lit 126)) (IE.lit 126)) (IE.modi (IE.divi IE.rk (IE.lit 3)) (IE.lit 3))) (IE.lit 1))) (IE.lit 126)) (IE.sub (IE.add (IE.modi (IE.pid 0) (IE.lit 126)) (IE.modi IE.rk (IE.lit 3))) (IE.lit 1))) (IE.sub (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 2032128)) (IE.lit 32)) (IE.divi IE.rk (IE.lit 9))) (IE.lit 126)) (IE.sub (IE.add (IE.modi (IE.divi (IE.pid 0) (IE.lit 126)) (IE.lit 126)) (IE.modi (IE.divi IE.rk (IE.lit 3)) (IE.lit 3))) (IE.lit 1))) (IE.lit 126)) (IE.sub (IE.add (IE.modi (IE.pid 0) (IE.lit 126)) (IE.modi IE.rk (IE.lit 3))) (IE.lit 1))) (IE.lit 16257023))))]))
  , inRange := (BE.and (BE.and (BE.and (BE.cmp .le (IE.lit 1) (IE.add (IE.modi (IE.divi (IE.pid 0) (IE.lit 126)) (IE.lit 126)) (IE.modi (IE.divi IE.rk (IE.lit 3)) (IE.lit 3)))) (BE.cmp .lt (IE.add (IE.modi (IE.divi (IE.pid 0) (IE.lit 126)) (IE.lit 126)) (IE.modi (IE.divi IE.rk (IE.lit 3)) (IE.lit 3))) (IE.lit 127))) (BE.cmp .le (IE.lit 1) (IE.add (IE.modi (IE.pid 0) (IE.lit 126)) (IE.modi IE.rk (IE.lit 3))))) (BE.cmp .lt (IE.add (IE.modi (IE.pid 0) (IE.lit 126)) (IE.modi IE.rk (IE.lit 3))) (IE.lit 127)))
  , body := (SE.bin .mul (SE.inp 63) (SE.inp 19))
  , postOffs := (IE.split 53 (IE.sparse [(20, (IE.modi (IE.divi (IE.pid 0) (IE.lit 15876)) (IE.lit 128)))]) (IE.sparse []))
  , post := (SE.bin .max (SE.bin .add (SE.inp 0) (SE.inp 21)) (SE.lit false 0 1))
  , outGuard := BE.tt
  , nInp := 66, idxSlot := 1048576 }
def t018_s12_block : Nat := 256
def t018_s12_nkb : Nat := 2

theorem t018_s12_wf : t018_s12_g.Wf :=
  { offs_ok := IE.qkOnly_split (IE.qkOnly_sparse _ (by decide)) (IE.qkOnly_sparse _ (by decide))
  , post_ok := IE.qkOnly_split (IE.qkOnly_sparse _ (by decide)) (IE.qkOnly_sparse _ (by decide))
  , range_ok := by decide
  , guard_ok := by decide }

theorem t018_s12_impl {α : Type} [ExactScalar α] :
    Implements (t018_s12_g.prog t018_s12_block t018_s12_nkb) (t018_s12_g.spec (α := α)) :=
  GenRed.prog_implements t018_s12_g t018_s12_block t018_s12_nkb t018_s12_wf (by decide) (by decide)

def t018_s13_g : GenRed :=
  { nout := 130056192, K := 2
  , offs := (IE.split 53 (IE.sparse []) (IE.sparse [(64, (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 4064256)) (IE.lit 128)) (IE.sub (IE.modi (IE.divi (IE.pid 0) (IE.lit 15876)) (IE.lit 256)) (IE.sub (IE.modi (IE.divi (IE.pid 0) (IE.lit 15876)) (IE.lit 256)) (IE.lit 127)))) (IE.lit 126)) (IE.modi (IE.divi (IE.pid 0) (IE.lit 126)) (IE.lit 126))) (IE.lit 126)) (IE.modi (IE.pid 0) (IE.lit 126)))), (65, (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 4064256)) (IE.lit 128)) (IE.sub (IE.sub (IE.modi (IE.divi (IE.pid 0) (IE.lit 15876)) (IE.lit 256)) (IE.lit 128)) (IE.sub (IE.sub (IE.modi (IE.divi (IE.pid 0) (IE.lit 15876)) (IE.lit 256)) (IE.lit 128)) (IE.lit 127)))) (IE.lit 126)) (IE.modi (IE.divi (IE.pid 0) (IE.lit 126)) (IE.lit 126))) (IE.lit 126)) (IE.modi (IE.pid 0) (IE.lit 126))))]))
  , inRange := (BE.or (BE.and (BE.and (BE.cmp .eq IE.rk (IE.lit 0)) (BE.cmp .le (IE.lit 0) (IE.modi (IE.divi (IE.pid 0) (IE.lit 15876)) (IE.lit 256)))) (BE.cmp .lt (IE.modi (IE.divi (IE.pid 0) (IE.lit 15876)) (IE.lit 256)) (IE.lit 128))) (BE.and (BE.and (BE.cmp .eq IE.rk (IE.lit 1)) (BE.cmp .le (IE.lit 128) (IE.modi (IE.divi (IE.pid 0) (IE.lit 15876)) (IE.lit 256)))) (BE.cmp .lt (IE.modi (IE.divi (IE.pid 0) (IE.lit 15876)) (IE.lit 256)) (IE.lit 256))))
  , body := (SE.selLe (SE.inp 67) (SE.lit false 1 2) (SE.inp 64) (SE.inp 65))
  , postOffs := (IE.split 53 (IE.sparse []) (IE.sparse []))
  , post := (SE.inp 0)
  , outGuard := BE.tt
  , nInp := 67, idxSlot := 67 }
def t018_s13_block : Nat := 2
def t018_s13_nkb : Nat := 1

theorem t018_s13_wf : t018_s13_g.Wf :=
  { offs_ok := IE.qkOnly_split (IE.qkOnly_sparse _ (by decide)) (IE.qkOnly_sparse _ (by decide))
  , post_ok := IE.qkOnly_split (IE.qkOnly_sparse _ (by decide)) (IE.qkOnly_sparse _ (by decide))
  , range_ok := by decide
  , guard_ok := by decide }

theorem t018_s13_impl {α : Type} [ExactScalar α] :
    Implements (t018_s13_g.prog t018_s13_block t018_s13_nkb) (t018_s13_g.spec (α := α)) :=
  GenRed.prog_implements t018_s13_g t018_s13_block t018_s13_nkb t018_s13_wf (by decide) (by decide)

def t018_s14_g : MaxRed :=
  { nout := 32514048, K := 9
  , offs := (IE.split 53 (IE.sparse []) (IE.sparse [(66, (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 1016064)) (IE.lit 256)) (IE.modi (IE.divi (IE.pid 0) (IE.lit 3969)) (IE.lit 256))) (IE.lit 126)) (IE.sub (IE.add (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 63)) (IE.lit 63)) (IE.lit 2)) (IE.sub (IE.add (IE.divi IE.rk (IE.lit 3)) (IE.sub (IE.sub (IE.lit 0) (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 63)) (IE.lit 63)) (IE.lit 2))) (IE.divi IE.rk (IE.lit 3)))) (IE.sub (IE.add (IE.divi IE.rk (IE.lit 3)) (IE.sub (IE.sub (IE.lit 0) (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 63)) (IE.lit 63)) (IE.lit 2))) (IE.divi IE.rk (IE.lit 3)))) (IE.sub (IE.lit 125) (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 63)) (IE.lit 63)) (IE.lit 2)))))) (IE.sub (IE.add (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 63)) (IE.lit 63)) (IE.lit 2)) (IE.sub (IE.add (IE.divi IE.rk (IE.lit 3)) (IE.sub (IE.sub (IE.lit 0) (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 63)) (IE.lit 63)) (IE.lit 2))) (IE.divi IE.rk (IE.lit 3)))) (IE.sub (IE.add (IE.divi IE.rk (IE.lit 3)) (IE.sub (IE.sub (IE.lit 0) (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 63)) (IE.lit 63)) (IE.lit 2))) (IE.divi IE.rk (IE.lit 3)))) (IE.sub (IE.lit 125) (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 63)) (IE.lit 63)) (IE.lit 2)))))) (IE.lit 125)))) (IE.lit 126)) (IE.sub (IE.add (IE.mul (IE.modi (IE.pid 0) (IE.lit 63)) (IE.lit 2)) (IE.sub (IE.add (IE.modi IE.rk (IE.lit 3)) (IE.sub (IE.sub (IE.lit 0) (IE.mul (IE.modi (IE.pid 0) (IE.lit 63)) (IE.lit 2))) (IE.modi IE.rk (IE.lit 3)))) (IE.sub (IE.add (IE.modi IE.rk (IE.lit 3)) (IE.sub (IE.sub (IE.lit 0) (IE.mul (IE.modi (IE.pid 0) (IE.lit 63)) (IE.lit 2))) (IE.modi IE.rk (IE.lit 3)))) (IE.sub (IE.lit 125) (IE.mul (IE.modi (IE.pid 0) (IE.lit 63)) (IE.lit 2)))))) (IE.sub (IE.add (IE.mul (IE.modi (IE.pid 0) (IE.lit 63)) (IE.lit 2)) (IE.sub (IE.add (IE.modi IE.rk (IE.lit 3)) (IE.sub (IE.sub (IE.lit 0) (IE.mul (IE.modi (IE.pid 0) (IE.lit 63)) (IE.lit 2))) (IE.modi IE.rk (IE.lit 3)))) (IE.sub (IE.add (IE.modi IE.rk (IE.lit 3)) (IE.sub (IE.sub (IE.lit 0) (IE.mul (IE.modi (IE.pid 0) (IE.lit 63)) (IE.lit 2))) (IE.modi IE.rk (IE.lit 3)))) (IE.sub (IE.lit 125) (IE.mul (IE.modi (IE.pid 0) (IE.lit 63)) (IE.lit 2)))))) (IE.lit 125)))))]))
  , body := (SE.inp 66)
  , postOffs := (IE.split 53 (IE.sparse []) (IE.sparse []))
  , post := (SE.inp 0)
  , nInp := 68, idxSlot := 1048576 }
def t018_s14_block : Nat := 8
def t018_s14_nkb : Nat := 2

theorem t018_s14_wf : t018_s14_g.Wf :=
  { offs_ok := IE.qkOnly_split (IE.qkOnly_sparse _ (by decide)) (IE.qkOnly_sparse _ (by decide))
  , post_ok := IE.qkOnly_split (IE.qkOnly_sparse _ (by decide)) (IE.qkOnly_sparse _ (by decide)) }

theorem t018_s14_impl {α : Type} [ExactScalar α] :
    Implements (t018_s14_g.prog t018_s14_block t018_s14_nkb) (t018_s14_g.spec (α := α)) :=
  MaxRed.prog_implements t018_s14_g t018_s14_block t018_s14_nkb t018_s14_wf (by decide) (by decide) (by decide)


def t018_s15_g : GenRed :=
  { nout := 4064256, K := 256
  , offs := (IE.split 53 (IE.sparse [(21, (IE.add (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 3969)) (IE.lit 32)) (IE.lit 256)) IE.rk))]) (IE.sparse [(67, (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 127008)) (IE.lit 256)) IE.rk) (IE.lit 63)) (IE.modi (IE.divi (IE.pid 0) (IE.lit 63)) (IE.lit 63))) (IE.lit 63)) (IE.modi (IE.pid 0) (IE.lit 63))))]))
  , inRange := (BE.and (BE.cmp .lt (IE.modi (IE.divi (IE.pid 0) (IE.lit 63)) (IE.lit 63)) (IE.lit 63)) (BE.cmp .lt (IE.modi (IE.pid 0) (IE.lit 63)) (IE.lit 63)))
  , body := (SE.bin .mul (SE.inp 67) (SE.inp 21))
  , postOffs := (IE.split 53 (IE.sparse [(22, (IE.modi (IE.divi (IE.pid 0) (IE.lit 3969)) (IE.lit 32)))]) (IE.sparse []))
  , post := (SE.bin .max (SE.bin .add (SE.inp 0) (SE.inp 23)) (SE.lit false 0 1))
  , outGuard := BE.tt
  , nInp := 69, idxSlot := 1048576 }
def t018_s15_block : Nat := 256
def t018_s15_nkb : Nat := 1

theorem t018_s15_wf : t018_s15_g.Wf :=
  { offs_ok := IE.qkOnly_split (IE.qkOnly_sparse _ (by decide)) (IE.qkOnly_sparse _ (by decide))
  , post_ok := IE.qkOnly_split (IE.qkOnly_sparse _ (by decide)) (IE.qkOnly_sparse _ (by decide))
  , range_ok := by decide
  , guard_ok := by decide }

theorem t018_s15_impl {α : Type} [ExactScalar α] :
    Implements (t018_s15_g.prog t018_s15_block t018_s15_nkb) (t018_s15_g.spec (α := α)) :=
  GenRed.prog_implements t018_s15_g t018_s15_block t018_s15_nkb t018_s15_wf (by decide) (by decide)

def t018_s16_g : GenRed :=
  { nout := 16257024, K := 32
  , offs := (IE.split 53 (IE.sparse [(23, (IE.add (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 3969)) (IE.lit 128)) (IE.lit 32)) IE.rk))]) (IE.sparse [(68, (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 508032)) (IE.lit 32)) IE.rk) (IE.lit 63)) (IE.modi (IE.divi (IE.pid 0) (IE.lit 63)) (IE.lit 63))) (IE.lit 63)) (IE.modi (IE.pid 0) (IE.lit 63))))]))
  , inRange := (BE.and (BE.cmp .lt (IE.modi (IE.divi (IE.pid 0) (IE.lit 63)) (IE.lit 63)) (IE.lit 63)) (BE.cmp .lt (IE.modi (IE.pid 0) (IE.lit 63)) (IE.lit 63)))
  , body := (SE.bin .mul (SE.inp 68) (SE.inp 23))
  , postOffs := (IE.split 53 (IE.sparse [(24, (IE.modi (IE.divi (IE.pid 0) (IE.lit 3969)) (IE.lit 128)))]) (IE.sparse []))
  , post := (SE.bin .max (SE.bin .add (SE.inp 0) (SE.inp 25)) (SE.lit false 0 1))
  , outGuard := BE.tt
  , nInp := 70, idxSlot := 1048576 }
def t018_s16_block : Nat := 32
def t018_s16_nkb : Nat := 1

theorem t018_s16_wf : t018_s16_g.Wf :=
  { offs_ok := IE.qkOnly_split (IE.qkOnly_sparse _ (by decide)) (IE.qkOnly_sparse _ (by decide))
  , post_ok := IE.qkOnly_split (IE.qkOnly_sparse _ (by decide)) (IE.qkOnly_sparse _ (by decide))
  , range_ok := by decide
  , guard_ok := by decide }

theorem t018_s16_impl {α : Type} [ExactScalar α] :
    Implements (t018_s16_g.prog t018_s16_block t018_s16_nkb) (t018_s16_g.spec (α := α)) :=
  GenRed.prog_implements t018_s16_g t018_s16_block t018_s16_nkb t018_s16_wf (by decide) (by decide)

def t018_s17_g : GenRed :=
  { nout := 16257024, K := 288
  , offs := (IE.split 53 (IE.sparse [(25, (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 3969)) (IE.lit 128)) (IE.lit 32)) (IE.divi IE.rk (IE.lit 9))) (IE.lit 3)) (IE.modi (IE.divi IE.rk (IE.lit 3)) (IE.lit 3))) (IE.lit 3)) (IE.modi IE.rk (IE.lit 3))))]) (IE.sparse [(68, (IE.sub (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 508032)) (IE.lit 32)) (IE.divi IE.rk (IE.lit 9))) (IE.lit 63)) (IE.sub (IE.add (IE.modi (IE.divi (IE.pid 0) (IE.lit 63)) (IE.lit 63)) (IE.modi (IE.divi IE.rk (IE.lit 3)) (IE.lit 3))) (IE.lit 1))) (IE.lit 63)) (IE.sub (IE.add (IE.modi (IE.pid 0) (IE.lit 63)) (IE.modi IE.rk (IE.lit 3))) (IE.lit 1))) (IE.sub (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 508032)) (IE.lit 32)) (IE.divi IE.rk (IE.lit 9))) (IE.lit 63)) (IE.sub (IE.add (IE.modi (IE.divi (IE.pid 0) (IE.lit 63)) (IE.lit 63)) (IE.modi (IE.divi IE.rk (IE.lit 3)) (IE.lit 3))) (IE.lit 1))) (IE.lit 63)) (IE.sub (IE.add (IE.modi (IE.pid 0) (IE.lit 63)) (IE.modi IE.rk (IE.lit 3))) (IE.lit 1))) (IE.lit 4064255))))]))
  , inRange := (BE.and (BE.and (BE.and (BE.cmp .le (IE.lit 1) (IE.add (IE.modi (IE.divi (IE.pid 0) (IE.lit 63)) (IE.lit 63)) (IE.modi (IE.divi IE.rk (IE.lit 3)) (IE.lit 3)))) (BE.cmp .lt (IE.add (IE.modi (IE.divi (IE.pid 0) (IE.lit 63)) (IE.lit 63)) (IE.modi (IE.divi IE.rk (IE.lit 3)) (IE.lit 3))) (IE.lit 64))) (BE.cmp .le (IE.lit 1) (IE.add (IE.modi (IE.pid 0) (IE.lit 63)) (IE.modi IE.rk (IE.lit 3))))) (BE.cmp .lt (IE.add (IE.modi (IE.pid 0) (IE.lit 63)) (IE.modi IE.rk (IE.lit 3))) (IE.lit 64)))
  , body := (SE.bin .mul (SE.inp 68) (SE.inp 25))
  , postOffs := (IE.split 53 (IE.sparse [(26, (IE.modi (IE.divi (IE.pid 0) (IE.lit 3969)) (IE.lit 128)))]) (IE.sparse []))
  , post := (SE.bin .max (SE.bin .add (SE.inp 0) (SE.inp 27)) (SE.lit false 0 1))
  , outGuard := BE.tt
  , nInp := 71, idxSlot := 1048576 }
def t018_s17_block : Nat := 256
def t018_s17_nkb : Nat := 2

theorem t018_s17_wf : t018_s17_g.Wf :=
  { offs_ok := IE.qkOnly_split (IE.qkOnly_sparse _ (by decide)) (IE.qkOnly_sparse _ (by decide))
  , post_ok := IE.qkOnly_split (IE.qkOnly_sparse _ (by decide)) (IE.qkOnly_sparse _ (by decide))
  , range_ok := by decide
  , guard_ok := by decide }

theorem t018_s17_impl {α : Type} [ExactScalar α] :
    Implements (t018_s17_g.prog t018_s17_block t018_s17_nkb) (t018_s17_g.spec (α := α)) :=
  GenRed.prog_implements t018_s17_g t018_s17_block t018_s17_nkb t018_s17_wf (by decide) (by decide)

def t018_s18_g : GenRed :=
  { nout := 32514048, K := 2
  , offs := (IE.split 53 (IE.sparse []) (IE.sparse [(69, (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 1016064)) (IE.lit 128)) (IE.sub (IE.modi (IE.divi (IE.pid 0) (IE.lit 3969)) (IE.lit 256)) (IE.sub (IE.modi (IE.divi (IE.pid 0) (IE.lit 3969)) (IE.lit 256)) (IE.lit 127)))) (IE.lit 63)) (IE.modi (IE.divi (IE.pid 0) (IE.lit 63)) (IE.lit 63))) (IE.lit 63)) (IE.modi (IE.pid 0) (IE.lit 63)))), (70, (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 1016064)) (IE.lit 128)) (IE.sub (IE.sub (IE.modi (IE.divi (IE.pid 0) (IE.lit 3969)) (IE.lit 256)) (IE.lit 128)) (IE.sub (IE.sub (IE.modi (IE.divi (IE.pid 0) (IE.lit 3969)) (IE.lit 256)) (IE.lit 128)) (IE.lit 127)))) (IE.lit 63)) (IE.modi (IE.divi (IE.pid 0) (IE.lit 63)) (IE.lit 63))) (IE.lit 63)) (IE.modi (IE.pid 0) (IE.lit 63))))]))
  , inRange := (BE.or (BE.and (BE.and (BE.cmp .eq IE.rk (IE.lit 0)) (BE.cmp .le (IE.lit 0) (IE.modi (IE.divi (IE.pid 0) (IE.lit 3969)) (IE.lit 256)))) (BE.cmp .lt (IE.modi (IE.divi (IE.pid 0) (IE.lit 3969)) (IE.lit 256)) (IE.lit 128))) (BE.and (BE.and (BE.cmp .eq IE.rk (IE.lit 1)) (BE.cmp .le (IE.lit 128) (IE.modi (IE.divi (IE.pid 0) (IE.lit 3969)) (IE.lit 256)))) (BE.cmp .lt (IE.modi (IE.divi (IE.pid 0) (IE.lit 3969)) (IE.lit 256)) (IE.lit 256))))
  , body := (SE.selLe (SE.inp 72) (SE.lit false 1 2) (SE.inp 69) (SE.inp 70))
  , postOffs := (IE.split 53 (IE.sparse []) (IE.sparse []))
  , post := (SE.inp 0)
  , outGuard := BE.tt
  , nInp := 72, idxSlot := 72 }
def t018_s18_block : Nat := 2
def t018_s18_nkb : Nat := 1

theorem t018_s18_wf : t018_s18_g.Wf :=
  { offs_ok := IE.qkOnly_split (IE.qkOnly_sparse _ (by decide)) (IE.qkOnly_sparse _ (by decide))
  , post_ok := IE.qkOnly_split (IE.qkOnly_sparse _ (by decide)) (IE.qkOnly_sparse _ (by decide))
  , range_ok := by decide
  , guard_ok := by decide }

theorem t018_s18_impl {α : Type} [ExactScalar α] :
    Implements (t018_s18_g.prog t018_s18_block t018_s18_nkb) (t018_s18_g.spec (α := α)) :=
  GenRed.prog_implements t018_s18_g t018_s18_block t018_s18_nkb t018_s18_wf (by decide) (by decide)

def t018_s19_g : GenRed :=
  { nout := 6096384, K := 256
  , offs := (IE.split 53 (IE.sparse [(27, (IE.add (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 3969)) (IE.lit 48)) (IE.lit 256)) IE.rk))]) (IE.sparse [(71, (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 190512)) (IE.lit 256)) IE.rk) (IE.lit 63)) (IE.modi (IE.divi (IE.pid 0) (IE.lit 63)) (IE.lit 63))) (IE.lit 63)) (IE.modi (IE.pid 0) (IE.lit 63))))]))
  , inRange := (BE.and (BE.cmp .lt (IE.modi (IE.divi (IE.pid 0) (IE.lit 63)) (IE.lit 63)) (IE.lit 63)) (BE.cmp .lt (IE.modi (IE.pid 0) (IE.lit 63)) (IE.lit 63)))
  , body := (SE.bin .mul (SE.inp 71) (SE.inp 27))
  , postOffs := (IE.split 53 (IE.sparse [(28, (IE.modi (IE.divi (IE.pid 0) (IE.lit 3969)) (IE.lit 48)))]) (IE.sparse []))
  , post := (SE.bin .max (SE.bin .add (SE.inp 0) (SE.inp 29)) (SE.lit false 0 1))
  , outGuard := BE.tt
  , nInp := 73, idxSlot := 1048576 }
def t018_s19_block : Nat := 256
def t018_s19_nkb : Nat := 1

theorem t018_s19_wf : t018_s19_g.Wf :=
  { offs_ok := IE.qkOnly_split (IE.qkOnly_sparse _ (by decide)) (IE.qkOnly_sparse _ (by decide))
  , post_ok := IE.qkOnly_split (IE.qkOnly_sparse _ (by decide)) (IE.qkOnly_sparse _ (by decide))
  , range_ok := by decide
  , guard_ok := by decide }

theorem t018_s19_impl {α : Type} [ExactScalar α] :
    Implements (t018_s19_g.prog t018_s19_block t018_s19_nkb) (t018_s19_g.spec (α := α)) :=
  GenRed.prog_implements t018_s19_g t018_s19_block t018_s19_nkb t018_s19_wf (by decide) (by decide)

def t018_s20_g : GenRed :=
  { nout := 24385536, K := 48
  , offs := (IE.split 53 (IE.sparse [(29, (IE.add (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 3969)) (IE.lit 192)) (IE.lit 48)) IE.rk))]) (IE.sparse [(72, (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 762048)) (IE.lit 48)) IE.rk) (IE.lit 63)) (IE.modi (IE.divi (IE.pid 0) (IE.lit 63)) (IE.lit 63))) (IE.lit 63)) (IE.modi (IE.pid 0) (IE.lit 63))))]))
  , inRange := (BE.and (BE.cmp .lt (IE.modi (IE.divi (IE.pid 0) (IE.lit 63)) (IE.lit 63)) (IE.lit 63)) (BE.cmp .lt (IE.modi (IE.pid 0) (IE.lit 63)) (IE.lit 63)))
  , body := (SE.bin .mul (SE.inp 72) (SE.inp 29))
  , postOffs := (IE.split 53 (IE.sparse [(30, (IE.modi (IE.divi (IE.pid 0) (IE.lit 3969)) (IE.lit 192)))]) (IE.sparse []))
  , post := (SE.bin .max (SE.bin .add (SE.inp 0) (SE.inp 31)) (SE.lit false 0 1))
  , outGuard := BE.tt
  , nInp := 74, idxSlot := 1048576 }
def t018_s20_block : Nat := 32
def t018_s20_nkb : Nat := 2

theorem t018_s20_wf : t018_s20_g.Wf :=
  { offs_ok := IE.qkOnly_split (IE.qkOnly_sparse _ (by decide)) (IE.qkOnly_sparse _ (by decide))
  , post_ok := IE.qkOnly_split (IE.qkOnly_sparse _ (by decide)) (IE.qkOnly_sparse _ (by decide))
  , range_ok := by decide
  , guard_ok := by decide }

theorem t018_s20_impl {α : Type} [ExactScalar α] :
    Implements (t018_s20_g.prog t018_s20_block t018_s20_nkb) (t018_s20_g.spec (α := α)) :=
  GenRed.prog_implements t018_s20_g t018_s20_block t018_s20_nkb t018_s20_wf (by decide) (by decide)

def t018_s21_g : GenRed :=
  { nout := 24385536, K := 432
  , offs := (IE.split 53 (IE.sparse [(31, (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 3969)) (IE.lit 192)) (IE.lit 48)) (IE.divi IE.rk (IE.lit 9))) (IE.lit 3)) (IE.modi (IE.divi IE.rk (IE.lit 3)) (IE.lit 3))) (IE.lit 3)) (IE.modi IE.rk (IE.lit 3))))]) (IE.sparse [(72, (IE.sub (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 762048)) (IE.lit 48)) (IE.divi IE.rk (IE.lit 9))) (IE.lit 63)) (IE.sub (IE.add (IE.modi (IE.divi (IE.pid 0) (IE.lit 63)) (IE.lit 63)) (IE.modi (IE.divi IE.rk (IE.lit 3)) (IE.lit 3))) (IE.lit 1))) (IE.lit 63)) (IE.sub (IE.add (IE.modi (IE.pid 0) (IE.lit 63)) (IE.modi IE.rk (IE.lit 3))) (IE.lit 1))) (IE.sub (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 762048)) (IE.lit 48)) (IE.divi IE.rk (IE.lit 9))) (IE.lit 63)) (IE.sub (IE.add (IE.modi (IE.divi (IE.pid 0) (IE.lit 63)) (IE.lit 63)) (IE.modi (IE.divi IE.rk (IE.lit 3)) (IE.lit 3))) (IE.lit 1))) (IE.lit 63)) (IE.sub (IE.add (IE.modi (IE.pid 0) (IE.lit 63)) (IE.modi IE.rk (IE.lit 3))) (IE.lit 1))) (IE.lit 6096383))))]))
  , inRange := (BE.and (BE.and (BE.and (BE.cmp .le (IE.lit 1) (IE.add (IE.modi (IE.divi (IE.pid 0) (IE.lit 63)) (IE.lit 63)) (IE.modi (IE.divi IE.rk (IE.lit 3)) (IE.lit 3)))) (BE.cmp .lt (IE.add (IE.modi (IE.divi (IE.pid 0) (IE.lit 63)) (IE.lit 63)) (IE.modi (IE.divi IE.rk (IE.lit 3)) (IE.lit 3))) (IE.lit 64))) (BE.cmp .le (IE.lit 1) (IE.add (IE.modi (IE.pid 0) (IE.lit 63)) (IE.modi IE.rk (IE.lit 3))))) (BE.cmp .lt (IE.add (IE.modi (IE.pid 0) (IE.lit 63)) (IE.modi IE.rk (IE.lit 3))) (IE.lit 64)))
  , body := (SE.bin .mul (SE.inp 72) (SE.inp 31))
  , postOffs := (IE.split 53 (IE.sparse [(32, (IE.modi (IE.divi (IE.pid 0) (IE.lit 3969)) (IE.lit 192)))]) (IE.sparse []))
  , post := (SE.bin .max (SE.bin .add (SE.inp 0) (SE.inp 33)) (SE.lit false 0 1))
  , outGuard := BE.tt
  , nInp := 75, idxSlot := 1048576 }
def t018_s21_block : Nat := 256
def t018_s21_nkb : Nat := 2

theorem t018_s21_wf : t018_s21_g.Wf :=
  { offs_ok := IE.qkOnly_split (IE.qkOnly_sparse _ (by decide)) (IE.qkOnly_sparse _ (by decide))
  , post_ok := IE.qkOnly_split (IE.qkOnly_sparse _ (by decide)) (IE.qkOnly_sparse _ (by decide))
  , range_ok := by decide
  , guard_ok := by decide }

theorem t018_s21_impl {α : Type} [ExactScalar α] :
    Implements (t018_s21_g.prog t018_s21_block t018_s21_nkb) (t018_s21_g.spec (α := α)) :=
  GenRed.prog_implements t018_s21_g t018_s21_block t018_s21_nkb t018_s21_wf (by decide) (by decide)

def t018_s22_g : GenRed :=
  { nout := 48771072, K := 2
  , offs := (IE.split 53 (IE.sparse []) (IE.sparse [(73, (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 1524096)) (IE.lit 192)) (IE.sub (IE.modi (IE.divi (IE.pid 0) (IE.lit 3969)) (IE.lit 384)) (IE.sub (IE.modi (IE.divi (IE.pid 0) (IE.lit 3969)) (IE.lit 384)) (IE.lit 191)))) (IE.lit 63)) (IE.modi (IE.divi (IE.pid 0) (IE.lit 63)) (IE.lit 63))) (IE.lit 63)) (IE.modi (IE.pid 0) (IE.lit 63)))), (74, (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 1524096)) (IE.lit 192)) (IE.sub (IE.sub (IE.modi (IE.divi (IE.pid 0) (IE.lit 3969)) (IE.lit 384)) (IE.lit 192)) (IE.sub (IE.sub (IE.modi (IE.divi (IE.pid 0) (IE.lit 3969)) (IE.lit 384)) (IE.lit 192)) (IE.lit 191)))) (IE.lit 63)) (IE.modi (IE.divi (IE.pid 0) (IE.lit 63)) (IE.lit 63))) (IE.lit 63)) (IE.modi (IE.pid 0) (IE.lit 63))))]))
  , inRange := (BE.or (BE.and (BE.and (BE.cmp .eq IE.rk (IE.lit 0)) (BE.cmp .le (IE.lit 0) (IE.modi (IE.divi (IE.pid 0) (IE.lit 3969)) (IE.lit 384)))) (BE.cmp .lt (IE.modi (IE.divi (IE.pid 0) (IE.lit 3969)) (IE.lit 384)) (IE.lit 192))) (BE.and (BE.and (BE.cmp .eq IE.rk (IE.lit 1)) (BE.cmp .le (IE.lit 192) (IE.modi (IE.divi (IE.pid 0) (IE.lit 3969)) (IE.lit 384)))) (BE.cmp .lt (IE.modi (IE.divi (IE.pid 0) (IE.lit 3969)) (IE.lit 384)) (IE.lit 384))))
  , body := (SE.selLe (SE.inp 76) (SE.lit false 1 2) (SE.inp 73) (SE.inp 74))
  , postOffs := (IE.split 53 (IE.sparse []) (IE.sparse []))
  , post := (SE.inp 0)
  , outGuard := BE.tt
  , nInp := 76, idxSlot := 76 }
def t018_s22_block : Nat := 2
def t018_s22_nkb : Nat := 1

theorem t018_s22_wf : t018_s22_g.Wf :=
  { offs_ok := IE.qkOnly_split (IE.qkOnly_sparse _ (by decide)) (IE.qkOnly_sparse _ (by decide))
  , post_ok := IE.qkOnly_split (IE.qkOnly_sparse _ (by decide)) (IE.qkOnly_sparse _ (by decide))
  , range_ok := by decide
  , guard_ok := by decide }

theorem t018_s22_impl {α : Type} [ExactScalar α] :
    Implements (t018_s22_g.prog t018_s22_block t018_s22_nkb) (t018_s22_g.spec (α := α)) :=
  GenRed.prog_implements t018_s22_g t018_s22_block t018_s22_nkb t018_s22_wf (by decide) (by decide)

def t018_s23_g : GenRed :=
  { nout := 6096384, K := 384
  , offs := (IE.split 53 (IE.sparse [(33, (IE.add (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 3969)) (IE.lit 48)) (IE.lit 384)) IE.rk))]) (IE.sparse [(75, (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 190512)) (IE.lit 384)) IE.rk) (IE.lit 63)) (IE.modi (IE.divi (IE.pid 0) (IE.lit 63)) (IE.lit 63))) (IE.lit 63)) (IE.modi (IE.pid 0) (IE.lit 63))))]))
  , inRange := (BE.and (BE.cmp .lt (IE.modi (IE.divi (IE.pid 0) (IE.lit 63)) (IE.lit 63)) (IE.lit 63)) (BE.cmp .lt (IE.modi (IE.pid 0) (IE.lit 63)) (IE.lit 63)))
  , body := (SE.bin .mul (SE.inp 75) (SE.inp 33))
  , postOffs := (IE.split 53 (IE.sparse [(34, (IE.modi (IE.divi (IE.pid 0) (IE.lit 3969)) (IE.lit 48)))]) (IE.sparse []))
  , post := (SE.bin .max (SE.bin .add (SE.inp 0) (SE.inp 35)) (SE.lit false 0 1))
  , outGuard := BE.tt
  , nInp := 77, idxSlot := 1048576 }
def t018_s23_block : Nat := 256
def t018_s23_nkb : Nat := 2

theorem t018_s23_wf : t018_s23_g.Wf :=
  { offs_ok := IE.qkOnly_split (IE.qkOnly_sparse _ (by decide)) (IE.qkOnly_sparse _ (by decide))
  , post_ok := IE.qkOnly_split (IE.qkOnly_sparse _ (by decide)) (IE.qkOnly_sparse _ (by decide))
  , range_ok := by decide
  , guard_ok := by decide }

theorem t018_s23_impl {α : Type} [ExactScalar α] :
    Implements (t018_s23_g.prog t018_s23_block t018_s23_nkb) (t018_s23_g.spec (α := α)) :=
  GenRed.prog_implements t018_s23_g t018_s23_block t018_s23_nkb t018_s23_wf (by decide) (by decide)

def t018_s24_g : GenRed :=
  { nout := 24385536, K := 48
  , offs := (IE.split 53 (IE.sparse [(35, (IE.add (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 3969)) (IE.lit 192)) (IE.lit 48)) IE.rk))]) (IE.sparse [(76, (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 762048)) (IE.lit 48)) IE.rk) (IE.lit 63)) (IE.modi (IE.divi (IE.pid 0) (IE.lit 63)) (IE.lit 63))) (IE.lit 63)) (IE.modi (IE.pid 0) (IE.lit 63))))]))
  , inRange := (BE.and (BE.cmp .lt (IE.modi (IE.divi (IE.pid 0) (IE.lit 63)) (IE.lit 63)) (IE.lit 63)) (BE.cmp .lt (IE.modi (IE.pid 0) (IE.lit 63)) (IE.lit 63)))
  , body := (SE.bin .mul (SE.inp 76) (SE.inp 35))
  , postOffs := (IE.split 53 (IE.sparse [(36, (IE.modi (IE.divi (IE.pid 0) (IE.lit 3969)) (IE.lit 192)))]) (IE.sparse []))
  , post := (SE.bin .max (SE.bin .add (SE.inp 0) (SE.inp 37)) (SE.lit false 0 1))
  , outGuard := BE.tt
  , nInp := 78, idxSlot := 1048576 }
def t018_s24_block : Nat := 32
def t018_s24_nkb : Nat := 2

theorem t018_s24_wf : t018_s24_g.Wf :=
  { offs_ok := IE.qkOnly_split (IE.qkOnly_sparse _ (by decide)) (IE.qkOnly_sparse _ (by decide))
  , post_ok := IE.qkOnly_split (IE.qkOnly_sparse _ (by decide)) (IE.qkOnly_sparse _ (by decide))
  , range_ok := by decide
  , guard_ok := by decide }

theorem t018_s24_impl {α : Type} [ExactScalar α] :
    Implements (t018_s24_g.prog t018_s24_block t018_s24_nkb) (t018_s24_g.spec (α := α)) :=
  GenRed.prog_implements t018_s24_g t018_s24_block t018_s24_nkb t018_s24_wf (by decide) (by decide)

def t018_s25_g : GenRed :=
  { nout := 24385536, K := 432
  , offs := (IE.split 53 (IE.sparse [(37, (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 3969)) (IE.lit 192)) (IE.lit 48)) (IE.divi IE.rk (IE.lit 9))) (IE.lit 3)) (IE.modi (IE.divi IE.rk (IE.lit 3)) (IE.lit 3))) (IE.lit 3)) (IE.modi IE.rk (IE.lit 3))))]) (IE.sparse [(76, (IE.sub (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 762048)) (IE.lit 48)) (IE.divi IE.rk (IE.lit 9))) (IE.lit 63)) (IE.sub (IE.add (IE.modi (IE.divi (IE.pid 0) (IE.lit 63)) (IE.lit 63)) (IE.modi (IE.divi IE.rk (IE.lit 3)) (IE.lit 3))) (IE.lit 1))) (IE.lit 63)) (IE.sub (IE.add (IE.modi (IE.pid 0) (IE.lit 63)) (IE.modi IE.rk (IE.lit 3))) (IE.lit 1))) (IE.sub (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 762048)) (IE.lit 48)) (IE.divi IE.rk (IE.lit 9))) (IE.lit 63)) (IE.sub (IE.add (IE.modi (IE.divi (IE.pid 0) (IE.lit 63)) (IE.lit 63)) (IE.modi (IE.divi IE.rk (IE.lit 3)) (IE.lit 3))) (IE.lit 1))) (IE.lit 63)) (IE.sub (IE.add (IE.modi (IE.pid 0) (IE.lit 63)) (IE.modi IE.rk (IE.lit 3))) (IE.lit 1))) (IE.lit 6096383))))]))
  , inRange := (BE.and (BE.and (BE.and (BE.cmp .le (IE.lit 1) (IE.add (IE.modi (IE.divi (IE.pid 0) (IE.lit 63)) (IE.lit 63)) (IE.modi (IE.divi IE.rk (IE.lit 3)) (IE.lit 3)))) (BE.cmp .lt (IE.add (IE.modi (IE.divi (IE.pid 0) (IE.lit 63)) (IE.lit 63)) (IE.modi (IE.divi IE.rk (IE.lit 3)) (IE.lit 3))) (IE.lit 64))) (BE.cmp .le (IE.lit 1) (IE.add (IE.modi (IE.pid 0) (IE.lit 63)) (IE.modi IE.rk (IE.lit 3))))) (BE.cmp .lt (IE.add (IE.modi (IE.pid 0) (IE.lit 63)) (IE.modi IE.rk (IE.lit 3))) (IE.lit 64)))
  , body := (SE.bin .mul (SE.inp 76) (SE.inp 37))
  , postOffs := (IE.split 53 (IE.sparse [(38, (IE.modi (IE.divi (IE.pid 0) (IE.lit 3969)) (IE.lit 192)))]) (IE.sparse []))
  , post := (SE.bin .max (SE.bin .add (SE.inp 0) (SE.inp 39)) (SE.lit false 0 1))
  , outGuard := BE.tt
  , nInp := 79, idxSlot := 1048576 }
def t018_s25_block : Nat := 256
def t018_s25_nkb : Nat := 2

theorem t018_s25_wf : t018_s25_g.Wf :=
  { offs_ok := IE.qkOnly_split (IE.qkOnly_sparse _ (by decide)) (IE.qkOnly_sparse _ (by decide))
  , post_ok := IE.qkOnly_split (IE.qkOnly_sparse _ (by decide)) (IE.qkOnly_sparse _ (by decide))
  , range_ok := by decide
  , guard_ok := by decide }

theorem t018_s25_impl {α : Type} [ExactScalar α] :
    Implements (t018_s25_g.prog t018_s25_block t018_s25_nkb) (t018_s25_g.spec (α := α)) :=
  GenRed.prog_implements t018_s25_g t018_s25_block t018_s25_nkb t018_s25_wf (by decide) (by decide)

def t018_s26_g : GenRed :=
  { nout := 48771072, K := 2
  , offs := (IE.split 53 (IE.sparse []) (IE.sparse [(77, (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 1524096)) (IE.lit 192)) (IE.sub (IE.modi (IE.divi (IE.pid 0) (IE.lit 3969)) (IE.lit 384)) (IE.sub (IE.modi (IE.divi (IE.pid 0) (IE.lit 3969)) (IE.lit 384)) (IE.lit 191)))) (IE.lit 63)) (IE.modi (IE.divi (IE.pid 0) (IE.lit 63)) (IE.lit 63))) (IE.lit 63)) (IE.modi (IE.pid 0) (IE.lit 63)))), (78, (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 1524096)) (IE.lit 192)) (IE.sub (IE.sub (IE.modi (IE.divi (IE.pid 0) (IE.lit 3969)) (IE.lit 384)) (IE.lit 192)) (IE.sub (IE.sub (IE.modi (IE.divi (IE.pid 0) (IE.lit 3969)) (IE.lit 384)) (IE.lit 192)) (IE.lit 191)))) (IE.lit 63)) (IE.modi (IE.divi (IE.pid 0) (IE.lit 63)) (IE.lit 63))) (IE.lit 63)) (IE.modi (IE.pid 0) (IE.lit 63))))]))
  , inRange := (BE.or (BE.and (BE.and (BE.cmp .eq IE.rk (IE.lit 0)) (BE.cmp .le (IE.lit 0) (IE.modi (IE.divi (IE.pid 0) (IE.lit 3969)) (IE.lit 384)))) (BE.cmp .lt (IE.modi (IE.divi (IE.pid 0) (IE.lit 3969)) (IE.lit 384)) (IE.lit 192))) (BE.and (BE.and (BE.cmp .eq IE.rk (IE.lit 1)) (BE.cmp .le (IE.lit 192) (IE.modi (IE.divi (IE.pid 0) (IE.lit 3969)) (IE.lit 384)))) (BE.cmp .lt (IE.modi (IE.divi (IE.pid 0) (IE.lit 3969)) (IE.lit 384)) (IE.lit 384))))
  , body := (SE.selLe (SE.inp 80) (SE.lit false 1 2) (SE.inp 77) (SE.inp 78))
  , postOffs := (IE.split 53 (IE.sparse []) (IE.sparse []))
  , post := (SE.inp 0)
  , outGuard := BE.tt
  , nInp := 80, idxSlot := 80 }
def t018_s26_block : Nat := 2
def t018_s26_nkb : Nat := 1

theorem t018_s26_wf : t018_s26_g.Wf :=
  { offs_ok := IE.qkOnly_split (IE.qkOnly_sparse _ (by decide)) (IE.qkOnly_sparse _ (by decide))
  , post_ok := IE.qkOnly_split (IE.qkOnly_sparse _ (by decide)) (IE.qkOnly_sparse _ (by decide))
  , range_ok := by decide
  , guard_ok := by decide }

theorem t018_s26_impl {α : Type} [ExactScalar α] :
    Implements (t018_s26_g.prog t018_s26_block t018_s26_nkb) (t018_s26_g.spec (α := α)) :=
  GenRed.prog_implements t018_s26_g t018_s26_block t018_s26_nkb t018_s26_wf (by decide) (by decide)

def t018_s27_g : GenRed :=
  { nout := 8128512, K := 384
  , offs := (IE.split 53 (IE.sparse [(39, (IE.add (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 3969)) (IE.lit 64)) (IE.lit 384)) IE.rk))]) (IE.sparse [(79, (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 254016)) (IE.lit 384)) IE.rk) (IE.lit 63)) (IE.modi (IE.divi (IE.pid 0) (IE.lit 63)) (IE.lit 63))) (IE.lit 63)) (IE.modi (IE.pid 0) (IE.lit 63))))]))
  , inRange := (BE.and (BE.cmp .lt (IE.modi (IE.divi (IE.pid 0) (IE.lit 63)) (IE.lit 63)) (IE.lit 63)) (BE.cmp .lt (IE.modi (IE.pid 0) (IE.lit 63)) (IE.lit 63)))
  , body := (SE.bin .mul (SE.inp 79) (SE.inp 39))
  , postOffs := (IE.split 53 (IE.sparse [(40, (IE.modi (IE.divi (IE.pid 0) (IE.lit 3969)) (IE.lit 64)))]) (IE.sparse []))
  , post := (SE.bin .max (SE.bin .add (SE.inp 0) (SE.inp 41)) (SE.lit false 0 1))
  , outGuard := BE.tt
  , nInp := 81, idxSlot := 1048576 }
def t018_s27_block : Nat := 256
def t018_s27_nkb : Nat := 2

theorem t018_s27_wf : t018_s27_g.Wf :=
  { offs_ok := IE.qkOnly_split (IE.qkOnly_sparse _ (by decide)) (IE.qkOnly_sparse _ (by decide))
  , post_ok := IE.qkOnly_split (IE.qkOnly_sparse _ (by decide)) (IE.qkOnly_sparse _ (by decide))
  , range_ok := by decide
  , guard_ok := by decide }

theorem t018_s27_impl {α : Type} [ExactScalar α] :
    Implements (t018_s27_g.prog t018_s27_block t018_s27_nkb) (t018_s27_g.spec (α := α)) :=
  GenRed.prog_implements t018_s27_g t018_s27_block t018_s27_nkb t018_s27_wf (by decide) (by decide)

def t018_s28_g : GenRed :=
  { nout := 32514048, K := 64
  , offs := (IE.split 53 (IE.sparse [(41, (IE.add (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 3969)) (IE.lit 256)) (IE.lit 64)) IE.rk))]) (IE.sparse [(80, (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 1016064)) (IE.lit 64)) IE.rk) (IE.lit 63)) (IE.modi (IE.divi (IE.pid 0) (IE.lit 63)) (IE.lit 63))) (IE.lit 63)) (IE.modi (IE.pid 0) (IE.lit 63))))]))
  , inRange := (BE.and (BE.cmp .lt (IE.modi (IE.divi (IE.pid 0) (IE.lit 63)) (IE.lit 63)) (IE.lit 63)) (BE.cmp .lt (IE.modi (IE.pid 0) (IE.lit 63)) (IE.lit 63)))
  , body := (SE.bin .mul (SE.inp 80) (SE.inp 41))
  , postOffs := (IE.split 53 (IE.sparse [(42, (IE.modi (IE.divi (IE.pid 0) (IE.lit 3969)) (IE.lit 256)))]) (IE.sparse []))
  , post := (SE.bin .max (SE.bin .add (SE.inp 0) (SE.inp 43)) (SE.lit false 0 1))
  , outGuard := BE.tt
  , nInp := 82, idxSlot := 1048576 }
def t018_s28_block : Nat := 64
def t018_s28_nkb : Nat := 1

theorem t018_s28_wf : t018_s28_g.Wf :=
  { offs_ok := IE.qkOnly_split (IE.qkOnly_sparse _ (by decide)) (IE.qkOnly_sparse _ (by decide))
  , post_ok := IE.qkOnly_split (IE.qkOnly_sparse _ (by decide)) (IE.qkOnly_sparse _ (by decide))
  , range_ok := by decide
  , guard_ok := by decide }

theorem t018_s28_impl {α : Type} [ExactScalar α] :
    Implements (t018_s28_g.prog t018_s28_block t018_s28_nkb) (t018_s28_g.spec (α := α)) :=
  GenRed.prog_implements t018_s28_g t018_s28_block t018_s28_nkb t018_s28_wf (by decide) (by decide)

def t018_s29_g : GenRed :=
  { nout := 32514048, K := 576
  , offs := (IE.split 53 (IE.sparse [(43, (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 3969)) (IE.lit 256)) (IE.lit 64)) (IE.divi IE.rk (IE.lit 9))) (IE.lit 3)) (IE.modi (IE.divi IE.rk (IE.lit 3)) (IE.lit 3))) (IE.lit 3)) (IE.modi IE.rk (IE.lit 3))))]) (IE.sparse [(80, (IE.sub (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 1016064)) (IE.lit 64)) (IE.divi IE.rk (IE.lit 9))) (IE.lit 63)) (IE.sub (IE.add (IE.modi (IE.divi (IE.pid 0) (IE.lit 63)) (IE.lit 63)) (IE.modi (IE.divi IE.rk (IE.lit 3)) (IE.lit 3))) (IE.lit 1))) (IE.lit 63)) (IE.sub (IE.add (IE.modi (IE.pid 0) (IE.lit 63)) (IE.modi IE.rk (IE.lit 3))) (IE.lit 1))) (IE.sub (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 1016064)) (IE.lit 64)) (IE.divi IE.rk (IE.lit 9))) (IE.lit 63)) (IE.sub (IE.add (IE.modi (IE.divi (IE.pid 0) (IE.lit 63)) (IE.lit 63)) (IE.modi (IE.divi IE.rk (IE.lit 3)) (IE.lit 3))) (IE.lit 1))) (IE.lit 63)) (IE.sub (IE.add (IE.modi (IE.pid 0) (IE.lit 63)) (IE.modi IE.rk (IE.lit 3))) (IE.lit 1))) (IE.lit 8128511))))]))
  , inRange := (BE.and (BE.and (BE.and (BE.cmp .le (IE.lit 1) (IE.add (IE.modi (IE.divi (IE.pid 0) (IE.lit 63)) (IE.lit 63)) (IE.modi (IE.divi IE.rk (IE.lit 3)) (IE.lit 3)))) (BE.cmp .lt (IE.add (IE.modi (IE.divi (IE.pid 0) (IE.lit 63)) (IE.lit 63)) (IE.modi (IE.divi IE.rk (IE.lit 3)) (IE.lit 3))) (IE.lit 64))) (BE.cmp .le (IE.lit 1) (IE.add (IE.modi (IE.pid 0) (IE.lit 63)) (IE.modi IE.rk (IE.lit 3))))) (BE.cmp .lt (IE.add (IE.modi (IE.pid 0) (IE.lit 63)) (IE.modi IE.rk (IE.lit 3))) (IE.lit 64)))
  , body := (SE.bin .mul (SE.inp 80) (SE.inp 43))
  , postOffs := (IE.split 53 (IE.sparse [(44, (IE.modi (IE.divi (IE.pid 0) (IE.lit 3969)) (IE.lit 256)))]) (IE.sparse []))
  , post := (SE.bin .max (SE.bin .add (SE.inp 0) (SE.inp 45)) (SE.lit false 0 1))
  , outGuard := BE.tt
  , nInp := 83, idxSlot := 1048576 }
def t018_s29_block : Nat := 512
def t018_s29_nkb : Nat := 2

theorem t018_s29_wf : t018_s29_g.Wf :=
  { offs_ok := IE.qkOnly_split (IE.qkOnly_sparse _ (by decide)) (IE.qkOnly_sparse _ (by decide))
  , post_ok := IE.qkOnly_split (IE.qkOnly_sparse _ (by decide)) (IE.qkOnly_sparse _ (by decide))
  , range_ok := by decide
  , guard_ok := by decide }

theorem t018_s29_impl {α : Type} [ExactScalar α] :
    Implements (t018_s29_g.prog t018_s29_block t018_s29_nkb) (t018_s29_g.spec (α := α)) :=
  GenRed.prog_implements t018_s29_g t018_s29_block t018_s29_nkb t018_s29_wf (by decide) (by decide)

def t018_s30_g : GenRed :=
  { nout := 65028096, K := 2
  , offs := (IE.split 53 (IE.sparse []) (IE.sparse [(81, (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 2032128)) (IE.lit 256)) (IE.sub (IE.modi (IE.divi (IE.pid 0) (IE.lit 3969)) (IE.lit 512)) (IE.sub (IE.modi (IE.divi (IE.pid 0) (IE.lit 3969)) (IE.lit 512)) (IE.lit 255)))) (IE.lit 63)) (IE.modi (IE.divi (IE.pid 0) (IE.lit 63)) (IE.lit 63))) (IE.lit 63)) (IE.modi (IE.pid 0) (IE.lit 63)))), (82, (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 2032128)) (IE.lit 256)) (IE.sub (IE.sub (IE.modi (IE.divi (IE.pid 0) (IE.lit 3969)) (IE.lit 512)) (IE.lit 256)) (IE.sub (IE.sub (IE.modi (IE.divi (IE.pid 0) (IE.lit 3969)) (IE.lit 512)) (IE.lit 256)) (IE.lit 255)))) (IE.lit 63)) (IE.modi (IE.divi (IE.pid 0) (IE.lit 63)) (IE.lit 63))) (IE.lit 63)) (IE.modi (IE.pid 0) (IE.lit 63))))]))
  , inRange := (BE.or (BE.and (BE.and (BE.cmp .eq IE.rk (IE.lit 0)) (BE.cmp .le (IE.lit 0) (IE.modi (IE.divi (IE.pid 0) (IE.lit 3969)) (IE.lit 512)))) (BE.cmp .lt (IE.modi (IE.divi (IE.pid 0) (IE.lit 3969)) (IE.lit 512)) (IE.lit 256))) (BE.and (BE.and (BE.cmp .eq IE.rk (IE.lit 1)) (BE.cmp .le (IE.lit 256) (IE.modi (IE.divi (IE.pid 0) (IE.lit 3969)) (IE.lit 512)))) (BE.cmp .lt (IE.modi (IE.divi (IE.pid 0) (IE.lit 3969)) (IE.lit 512)) (IE.lit 512))))
  , body := (SE.selLe (SE.inp 84) (SE.lit false 1 2) (SE.inp 81) (SE.inp 82))
  , postOffs := (IE.split 53 (IE.sparse []) (IE.sparse []))
  , post := (SE.inp 0)
  , outGuard := BE.tt
  , nInp := 84, idxSlot := 84 }
def t018_s30_block : Nat := 2
def t018_s30_nkb : Nat := 1

theorem t018_s30_wf : t018_s30_g.Wf :=
  { offs_ok := IE.qkOnly_split (IE.qkOnly_sparse _ (by decide)) (IE.qkOnly_sparse _ (by decide))
  , post_ok := IE.qkOnly_split (IE.qkOnly_sparse _ (by decide)) (IE.qkOnly_sparse _ (by decide))
  , range_ok := by decide
  , guard_ok := by decide }

theorem t018_s30_impl {α : Type} [ExactScalar α] :
    Implements (t018_s30_g.prog t018_s30_block t018_s30_nkb) (t018_s30_g.spec (α := α)) :=
  GenRed.prog_implements t018_s30_g t018_s30_block t018_s30_nkb t018_s30_wf (by decide) (by decide)

def t018_s31_g : MaxRed :=
  { nout := 15745024, K := 9
  , offs := (IE.split 53 (IE.sparse []) (IE.sparse [(83, (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 492032)) (IE.lit 512)) (IE.modi (IE.divi (IE.pid 0) (IE.lit 961)) (IE.lit 512))) (IE.lit 63)) (IE.sub (IE.add (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 31)) (IE.lit 31)) (IE.lit 2)) (IE.sub (IE.add (IE.divi IE.rk (IE.lit 3)) (IE.sub (IE.sub (IE.lit 0) (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 31)) (IE.lit 31)) (IE.lit 2))) (IE.divi IE.rk (IE.lit 3)))) (IE.sub (IE.add (IE.divi IE.rk (IE.lit 3)) (IE.sub (IE.sub (IE.lit 0) (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 31)) (IE.lit 31)) (IE.lit 2))) (IE.divi IE.rk (IE.lit 3)))) (IE.sub (IE.lit 62) (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 31)) (IE.lit 31)) (IE.lit 2)))))) (IE.sub (IE.add (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 31)) (IE.lit 31)) (IE.lit 2)) (IE.sub (IE.add (IE.divi IE.rk (IE.lit 3)) (IE.sub (IE.sub (IE.lit 0) (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 31)) (IE.lit 31)) (IE.lit 2))) (IE.divi IE.rk (IE.lit 3)))) (IE.sub (IE.add (IE.divi IE.rk (IE.lit 3)) (IE.sub (IE.sub (IE.lit 0) (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 31)) (IE.lit 31)) (IE.lit 2))) (IE.divi IE.rk (IE.lit 3)))) (IE.sub (IE.lit 62) (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 31)) (IE.lit 31)) (IE.lit 2)))))) (IE.lit 62)))) (IE.lit 63)) (IE.sub (IE.add (IE.mul (IE.modi (IE.pid 0) (IE.lit 31)) (IE.lit 2)) (IE.sub (IE.add (IE.modi IE.rk (IE.lit 3)) (IE.sub (IE.sub (IE.lit 0) (IE.mul (IE.modi (IE.pid 0) (IE.lit 31)) (IE.lit 2))) (IE.modi IE.rk (IE.lit 3)))) (IE.sub (IE.add (IE.modi IE.rk (IE.lit 3)) (IE.sub (IE.sub (IE.lit 0) (IE.mul (IE.modi (IE.pid 0) (IE.lit 31)) (IE.lit 2))) (IE.modi IE.rk (IE.lit 3)))) (IE.sub (IE.lit 62) (IE.mul (IE.modi (IE.pid 0) (IE.lit 31)) (IE.lit 2)))))) (IE.sub (IE.add (IE.mul (IE.modi (IE.pid 0) (IE.lit 31)) (IE.lit 2)) (IE.sub (IE.add (IE.modi IE.rk (IE.lit 3)) (IE.sub (IE.sub (IE.lit 0) (IE.mul (IE.modi (IE.pid 0) (IE.lit 31)) (IE.lit 2))) (IE.modi IE.rk (IE.lit 3)))) (IE.sub (IE.add (IE.modi IE.rk (IE.lit 3)) (IE.sub (IE.sub (IE.lit 0) (IE.mul (IE.modi (IE.pid 0) (IE.lit 31)) (IE.lit 2))) (IE.modi IE.rk (IE.lit 3)))) (IE.sub (IE.lit 62) (IE.mul (IE.modi (IE.pid 0) (IE.lit 31)) (IE.lit 2)))))) (IE.lit 62)))))]))
  , body := (SE.inp 83)
  , postOffs := (IE.split 53 (IE.sparse []) (IE.sparse []))
  , post := (SE.inp 0)
  , nInp := 85, idxSlot := 1048576 }
def t018_s31_block : Nat := 8
def t018_s31_nkb : Nat := 2

theorem t018_s31_wf : t018_s31_g.Wf :=
  { offs_ok := IE.qkOnly_split (IE.qkOnly_sparse _ (by decide)) (IE.qkOnly_sparse _ (by decide))
  , post_ok := IE.qkOnly_split (IE.qkOnly_sparse _ (by decide)) (IE.qkOnly_sparse _ (by decide)) }

theorem t018_s31_impl {α : Type} [ExactScalar α] :
    Implements (t018_s31_g.prog t018_s31_block t018_s31_nkb) (t018_s31_g.spec (α := α)) :=
  MaxRed.prog_implements t018_s31_g t018_s31_block t018_s31_nkb t018_s31_wf (by decide) (by decide) (by decide)


def t018_s32_g : GenRed :=
  { nout := 1968128, K := 512
  , offs := (IE.split 53 (IE.sparse [(45, (IE.add (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 961)) (IE.lit 64)) (IE.lit 512)) IE.rk))]) (IE.sparse [(84, (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 61504)) (IE.lit 512)) IE.rk) (IE.lit 31)) (IE.modi (IE.divi (IE.pid 0) (IE.lit 31)) (IE.lit 31))) (IE.lit 31)) (IE.modi (IE.pid 0) (IE.lit 31))))]))
  , inRange := (BE.and (BE.cmp .lt (IE.modi (IE.divi (IE.pid 0) (IE.lit 31)) (IE.lit 31)) (IE.lit 31)) (BE.cmp .lt (IE.modi (IE.pid 0) (IE.lit 31)) (IE.lit 31)))
  , body := (SE.bin .mul (SE.inp 84) (SE.inp 45))
  , postOffs := (IE.split 53 (IE.sparse [(46, (IE.modi (IE.divi (IE.pid 0) (IE.lit 961)) (IE.lit 64)))]) (IE.sparse []))
  , post := (SE.bin .max (SE.bin .add (SE.inp 0) (SE.inp 47)) (SE.lit false 0 1))
  , outGuard := BE.tt
  , nInp := 86, idxSlot := 1048576 }
def t018_s32_block : Nat := 512
def t018_s32_nkb : Nat := 1

theorem t018_s32_wf : t018_s32_g.Wf :=
  { offs_ok := IE.qkOnly_split (IE.qkOnly_sparse _ (by decide)) (IE.qkOnly_sparse _ (by decide))
  , post_ok := IE.qkOnly_split (IE.qkOnly_sparse _ (by decide)) (IE.qkOnly_sparse _ (by decide))
  , range_ok := by decide
  , guard_ok := by decide }

theorem t018_s32_impl {α : Type} [ExactScalar α] :
    Implements (t018_s32_g.prog t018_s32_block t018_s32_nkb) (t018_s32_g.spec (α := α)) :=
  GenRed.prog_implements t018_s32_g t018_s32_block t018_s32_nkb t018_s32_wf (by decide) (by decide)

def t018_s33_g : GenRed :=
  { nout := 7872512, K := 64
  , offs := (IE.split 53 (IE.sparse [(47, (IE.add (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 961)) (IE.lit 256)) (IE.lit 64)) IE.rk))]) (IE.sparse [(85, (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 246016)) (IE.lit 64)) IE.rk) (IE.lit 31)) (IE.modi (IE.divi (IE.pid 0) (IE.lit 31)) (IE.lit 31))) (IE.lit 31)) (IE.modi (IE.pid 0) (IE.lit 31))))]))
  , inRange := (BE.and (BE.cmp .lt (IE.modi (IE.divi (IE.pid 0) (IE.lit 31)) (IE.lit 31)) (IE.lit 31)) (BE.cmp .lt (IE.modi (IE.pid 0) (IE.lit 31)) (IE.lit 31)))
  , body := (SE.bin .mul (SE.inp 85) (SE.inp 47))
  , postOffs := (IE.split 53 (IE.sparse [(48, (IE.modi (IE.divi (IE.pid 0) (IE.lit 961)) (IE.lit 256)))]) (IE.sparse []))
  , post := (SE.bin .max (SE.bin .add (SE.inp 0) (SE.inp 49)) (SE.lit false 0 1))
  , outGuard := BE.tt
  , nInp := 87, idxSlot := 1048576 }
def t018_s33_block : Nat := 64
def t018_s33_nkb : Nat := 1

theorem t018_s33_wf : t018_s33_g.Wf :=
  { offs_ok := IE.qkOnly_split (IE.qkOnly_sparse _ (by decide)) (IE.qkOnly_sparse _ (by decide))
  , post_ok := IE.qkOnly_split (IE.qkOnly_sparse _ (by decide)) (IE.qkOnly_sparse _ (by decide))
  , range_ok := by decide
  , guard_ok := by decide }

theorem t018_s33_impl {α : Type} [ExactScalar α] :
    Implements (t018_s33_g.prog t018_s33_block t018_s33_nkb) (t018_s33_g.spec (α := α)) :=
  GenRed.prog_implements t018_s33_g t018_s33_block t018_s33_nkb t018_s33_wf (by decide) (by decide)

def t018_s34_g : GenRed :=
  { nout := 7872512, K := 576
  , offs := (IE.split 53 (IE.sparse [(49, (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 961)) (IE.lit 256)) (IE.lit 64)) (IE.divi IE.rk (IE.lit 9))) (IE.lit 3)) (IE.modi (IE.divi IE.rk (IE.lit 3)) (IE.lit 3))) (IE.lit 3)) (IE.modi IE.rk (IE.lit 3))))]) (IE.sparse [(85, (IE.sub (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 246016)) (IE.lit 64)) (IE.divi IE.rk (IE.lit 9))) (IE.lit 31)) (IE.sub (IE.add (IE.modi (IE.divi (IE.pid 0) (IE.lit 31)) (IE.lit 31)) (IE.modi (IE.divi IE.rk (IE.lit 3)) (IE.lit 3))) (IE.lit 1))) (IE.lit 31)) (IE.sub (IE.add (IE.modi (IE.pid 0) (IE.lit 31)) (IE.modi IE.rk (IE.lit 3))) (IE.lit 1))) (IE.sub (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 246016)) (IE.lit 64)) (IE.divi IE.rk (IE.lit 9))) (IE.lit 31)) (IE.sub (IE.add (IE.modi (IE.divi (IE.pid 0) (IE.lit 31)) (IE.lit 31)) (IE.modi (IE.divi IE.rk (IE.lit 3)) (IE.lit 3))) (IE.lit 1))) (IE.lit 31)) (IE.sub (IE.add (IE.modi (IE.pid 0) (IE.lit 31)) (IE.modi IE.rk (IE.lit 3))) (IE.lit 1))) (IE.lit 1968127))))]))
  , inRange := (BE.and (BE.and (BE.and (BE.cmp .le (IE.lit 1) (IE.add (IE.modi (IE.divi (IE.pid 0) (IE.lit 31)) (IE.lit 31)) (IE.modi (IE.divi IE.rk (IE.lit 3)) (IE.lit 3)))) (BE.cmp .lt (IE.add (IE.modi (IE.divi (IE.pid 0) (IE.lit 31)) (IE.lit 31)) (IE.modi (IE.divi IE.rk (IE.lit 3)) (IE.lit 3))) (IE.lit 32))) (BE.cmp .le (IE.lit 1) (IE.add (IE.modi (IE.pid 0) (IE.lit 31)) (IE.modi IE.rk (IE.lit 3))))) (BE.cmp .lt (IE.add (IE.modi (IE.pid 0) (IE.lit 31)) (IE.modi IE.rk (IE.lit 3))) (IE.lit 32)))
  , body := (SE.bin .mul (SE.inp 85) (SE.inp 49))
  , postOffs := (IE.split 53 (IE.sparse [(50, (IE.modi (IE.divi (IE.pid 0) (IE.lit 961)) (IE.lit 256)))]) (IE.sparse []))
  , post := (SE.bin .max (SE.bin .add (SE.inp 0) (SE.inp 51)) (SE.lit false 0 1))
  , outGuard := BE.tt
  , nInp := 88, idxSlot := 1048576 }
def t018_s34_block : Nat := 512
def t018_s34_nkb : Nat := 2

theorem t018_s34_wf : t018_s34_g.Wf :=
  { offs_ok := IE.qkOnly_split (IE.qkOnly_sparse _ (by decide)) (IE.qkOnly_sparse _ (by decide))
  , post_ok := IE.qkOnly_split (IE.qkOnly_sparse _ (by decide)) (IE.qkOnly_sparse _ (by decide))
  , range_ok := by decide
  , guard_ok := by decide }

theorem t018_s34_impl {α : Type} [ExactScalar α] :
    Implements (t018_s34_g.prog t018_s34_block t018_s34_nkb) (t018_s34_g.spec (α := α)) :=
  GenRed.prog_implements t018_s34_g t018_s34_block t018_s34_nkb t018_s34_wf (by decide) (by decide)

def t018_s35_g : GenRed :=
  { nout := 15745024, K := 2
  , offs := (IE.split 53 (IE.sparse []) (IE.sparse [(86, (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 492032)) (IE.lit 256)) (IE.sub (IE.modi (IE.divi (IE.pid 0) (IE.lit 961)) (IE.lit 512)) (IE.sub (IE.modi (IE.divi (IE.pid 0) (IE.lit 961)) (IE.lit 512)) (IE.lit 255)))) (IE.lit 31)) (IE.modi (IE.divi (IE.pid 0) (IE.lit 31)) (IE.lit 31))) (IE.lit 31)) (IE.modi (IE.pid 0) (IE.lit 31)))), (87, (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 492032)) (IE.lit 256)) (IE.sub (IE.sub (IE.modi (IE.divi (IE.pid 0) (IE.lit 961)) (IE.lit 512)) (IE.lit 256)) (IE.sub (IE.sub (IE.modi (IE.divi (IE.pid 0) (IE.lit 961)) (IE.lit 512)) (IE.lit 256)) (IE.lit 255)))) (IE.lit 31)) (IE.modi (IE.divi (IE.pid 0) (IE.lit 31)) (IE.lit 31))) (IE.lit 31)) (IE.modi (IE.pid 0) (IE.lit 31))))]))
  , inRange := (BE.or (BE.and (BE.and (BE.cmp .eq IE.rk (IE.lit 0)) (BE.cmp .le (IE.lit 0) (IE.modi (IE.divi (IE.pid 0) (IE.lit 961)) (IE.lit 512)))) (BE.cmp .lt (IE.modi (IE.divi (IE.pid 0) (IE.lit 961)) (IE.lit 512)) (IE.lit 256))) (BE.and (BE.and (BE.cmp .eq IE.rk (IE.lit 1)) (BE.cmp .le (IE.lit 256) (IE.modi (IE.divi (IE.pid 0) (IE.lit 961)) (IE.lit 512)))) (BE.cmp .lt (IE.modi (IE.divi (IE.pid 0) (IE.lit 961)) (IE.lit 512)) (IE.lit 512))))
  , body := (SE.selLe (SE.inp 89) (SE.lit false 1 2) (SE.inp 86) (SE.inp 87))
  , postOffs := (IE.split 53 (IE.sparse []) (IE.sparse []))
  , post := (SE.inp 0)
  , outGuard := BE.tt
  , nInp := 89, idxSlot := 89 }
def t018_s35_block : Nat := 2
def t018_s35_nkb : Nat := 1

theorem t018_s35_wf : t018_s35_g.Wf :=
  { offs_ok := IE.qkOnly_split (IE.qkOnly_sparse _ (by decide)) (IE.qkOnly_sparse _ (by decide))
  , post_ok := IE.qkOnly_split (IE.qkOnly_sparse _ (by decide)) (IE.qkOnly_sparse _ (by decide))
  , range_ok := by decide
  , guard_ok := by decide }

theorem t018_s35_impl {α : Type} [ExactScalar α] :
    Implements (t018_s35_g.prog t018_s35_block t018_s35_nkb) (t018_s35_g.spec (α := α)) :=
  GenRed.prog_implements t018_s35_g t018_s35_block t018_s35_nkb t018_s35_wf (by decide) (by decide)

def t018_s36_g : GenRed :=
  { nout := 30752000, K := 512
  , offs := (IE.split 53 (IE.sparse [(51, (IE.add (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 961)) (IE.lit 1000)) (IE.lit 512)) IE.rk))]) (IE.sparse [(88, (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 961000)) (IE.lit 512)) IE.rk) (IE.lit 31)) (IE.modi (IE.divi (IE.pid 0) (IE.lit 31)) (IE.lit 31))) (IE.lit 31)) (IE.modi (IE.pid 0) (IE.lit 31))))]))
  , inRange := (BE.and (BE.cmp .lt (IE.modi (IE.divi (IE.pid 0) (IE.lit 31)) (IE.lit 31)) (IE.lit 31)) (BE.cmp .lt (IE.modi (IE.pid 0) (IE.lit 31)) (IE.lit 31)))
  , body := (SE.bin .mul (SE.inp 88) (SE.inp 51))
  , postOffs := (IE.split 53 (IE.sparse [(52, (IE.modi (IE.divi (IE.pid 0) (IE.lit 961)) (IE.lit 1000)))]) (IE.sparse []))
  , post := (SE.bin .max (SE.bin .add (SE.inp 0) (SE.inp 53)) (SE.lit false 0 1))
  , outGuard := BE.tt
  , nInp := 90, idxSlot := 1048576 }
def t018_s36_block : Nat := 512
def t018_s36_nkb : Nat := 1

theorem t018_s36_wf : t018_s36_g.Wf :=
  { offs_ok := IE.qkOnly_split (IE.qkOnly_sparse _ (by decide)) (IE.qkOnly_sparse _ (by decide))
  , post_ok := IE.qkOnly_split (IE.qkOnly_sparse _ (by decide)) (IE.qkOnly_sparse _ (by decide))
  , range_ok := by decide
  , guard_ok := by decide }

theorem t018_s36_impl {α : Type} [ExactScalar α] :
    Implements (t018_s36_g.prog t018_s36_block t018_s36_nkb) (t018_s36_g.spec (α := α)) :=
  GenRed.prog_implements t018_s36_g t018_s36_block t018_s36_nkb t018_s36_wf (by decide) (by decide)

def t018_s37_g : GenRed :=
  { nout := 32000, K := 961
  , offs := (IE.split 53 (IE.sparse []) (IE.sparse [(89, (IE.add (IE.mul (IE.pid 0) (IE.lit 961)) IE.rk))]))
  , inRange := BE.tt
  , body := (SE.inp 89)
  , postOffs := (IE.split 53 (IE.sparse []) (IE.sparse []))
  , post := (SE.bin .mul (SE.inp 0) (SE.lit false 1 961))
  , outGuard := BE.tt
  , nInp := 91, idxSlot := 1048576 }
def t018_s37_block : Nat := 512
def t018_s37_nkb : Nat := 2

theorem t018_s37_wf : t018_s37_g.Wf :=
  { offs_ok := IE.qkOnly_split (IE.qkOnly_sparse _ (by decide)) (IE.qkOnly_sparse _ (by decide))
  , post_ok := IE.qkOnly_split (IE.qkOnly_sparse _ (by decide)) (IE.qkOnly_sparse _ (by decide))
  , range_ok := by decide
  , guard_ok := by decide }

theorem t018_s37_impl {α : Type} [ExactScalar α] :
    Implements (t018_s37_g.prog t018_s37_block t018_s37_nkb) (t018_s37_g.spec (α := α)) :=
  GenRed.prog_implements t018_s37_g t018_s37_block t018_s37_nkb t018_s37_wf (by decide) (by decide)

/-- Stage 0 reads no intermediate past what was written there. -/
theorem t018_s0_loc {α : Type} [ExactScalar α] :
    SpecLocal t018_sz (t018_s0_g.spec (α := α)) :=
  GenRed.specLocal t018_s0_g t018_sz
    (fun b nn hn q kk hq hk => by
      have hb : 53 ≤ b := Sizes.ofList_le hn
      have hz : t018_s0_g.offs b = IE.lit 0 := by
        simp [t018_s0_g, IE.split_ge hb, IE.sparse]
      rw [hz]
      exact t018_sz_pos b nn hn)
    (fun b nn hn q hq => by
      have hb : 53 ≤ b := Sizes.ofList_le hn
      have hz : t018_s0_g.postOffs b = IE.lit 0 := by
        simp [t018_s0_g, IE.split_ge hb, IE.sparse]
      rw [hz]
      exact t018_sz_pos b nn hn)

/-- Stage 1 reads no intermediate past what was written there. -/
theorem t018_s1_loc {α : Type} [ExactScalar α] :
    SpecLocal t018_sz (t018_s1_g.spec (α := α)) :=
  MaxRed.specLocal t018_s1_g t018_sz (by decide)
    (fun b nn hn q kk hq hk => by
      by_cases h53 : b = 53
      · subst h53
        have hs : nn = 196635648 :=
          Sizes.ofList_some (by decide) (by decide) hn
        subst hs
        exact (bound_pack (A := 777216) (B := 253) (bound_pack (A := 3072) (B := 253) (bound_pack (A := 32) (B := 96) (bound_div (a := 32) (d := 1524096) hq) (bound_mod (c := 96) (by decide : (0 : Nat) < 96))) (ExactScalar.clamp_lt (c := 253) (by decide : (0 : Nat) < 253))) (ExactScalar.clamp_lt (c := 253) (by decide : (0 : Nat) < 253)))
      have hb : 53 ≤ b := Sizes.ofList_le hn
      have hz : t018_s1_g.offs b = IE.lit 0 := by
        simp [t018_s1_g, IE.split_ge hb, IE.sparse, h53]
      rw [hz]
      exact t018_sz_pos b nn hn)
    (fun b nn hn q hq => by
      have hb : 53 ≤ b := Sizes.ofList_le hn
      have hz : t018_s1_g.postOffs b = IE.lit 0 := by
        simp [t018_s1_g, IE.split_ge hb, IE.sparse]
      rw [hz]
      exact t018_sz_pos b nn hn)

/-- Stage 2 reads no intermediate past what was written there. -/
theorem t018_s2_loc {α : Type} [ExactScalar α] :
    SpecLocal t018_sz (t018_s2_g.spec (α := α)) :=
  GenRed.specLocal t018_s2_g t018_sz
    (fun b nn hn q kk hq hk => by
      by_cases h54 : b = 54
      · subst h54
        have hs : nn = 48771072 :=
          Sizes.ofList_some (by decide) (by decide) hn
        subst hs
        exact (bound_pack (A := 387072) (B := 126) (bound_pack (A := 3072) (B := 126) (bound_pack (A := 32) (B := 96) (bound_div (a := 32) (d := 254016) hq) hk) (bound_mod (c := 126) (by decide : (0 : Nat) < 126))) (bound_mod (c := 126) (by decide : (0 : Nat) < 126)))
      have hb : 53 ≤ b := Sizes.ofList_le hn
      have hz : t018_s2_g.offs b = IE.lit 0 := by
        simp [t018_s2_g, IE.split_ge hb, IE.sparse, h54]
      rw [hz]
      exact t018_sz_pos b nn hn)
    (fun b nn hn q hq => by
      have hb : 53 ≤ b := Sizes.ofList_le hn
      have hz : t018_s2_g.postOffs b = IE.lit 0 := by
        simp [t018_s2_g, IE.split_ge hb, IE.sparse]
      rw [hz]
      exact t018_sz_pos b nn hn)

/-- Stage 3 reads no intermediate past what was written there. -/
theorem t018_s3_loc {α : Type} [ExactScalar α] :
    SpecLocal t018_sz (t018_s3_g.spec (α := α)) :=
  GenRed.specLocal t018_s3_g t018_sz
    (fun b nn hn q kk hq hk => by
      by_cases h55 : b = 55
      · subst h55
        have hs : nn = 8128512 :=
          Sizes.ofList_some (by decide) (by decide) hn
        subst hs
        exact (bound_pack (A := 64512) (B := 126) (bound_pack (A := 512) (B := 126) (bound_pack (A := 32) (B := 16) (bound_div (a := 32) (d := 1016064) hq) hk) (bound_mod (c := 126) (by decide : (0 : Nat) < 126))) (bound_mod (c := 126) (by decide : (0 : Nat) < 126)))
      have hb : 53 ≤ b := Sizes.ofList_le hn
      have hz : t018_s3_g.offs b = IE.lit 0 := by
        simp [t018_s3_g, IE.split_ge hb, IE.sparse, h55]
      rw [hz]
      exact t018_sz_pos b nn hn)
    (fun b nn hn q hq => by
      have hb : 53 ≤ b := Sizes.ofList_le hn
      have hz : t018_s3_g.postOffs b = IE.lit 0 := by
        simp [t018_s3_g, IE.split_ge hb, IE.sparse]
      rw [hz]
      exact t018_sz_pos b nn hn)

/-- Stage 4 reads no intermediate past what was written there. -/
theorem t018_s4_loc {α : Type} [ExactScalar α] :
    SpecLocal t018_sz (t018_s4_g.spec (α := α)) :=
  GenRed.specLocal t018_s4_g t018_sz
    (fun b nn hn q kk hq hk => by
      by_cases h55 : b = 55
      · subst h55
        have hs : nn = 8128512 :=
          Sizes.ofList_some (by decide) (by decide) hn
        subst hs
        exact (ExactScalar.clamp_lt (c := 8128512) (by decide : (0 : Nat) < 8128512))
      have hb : 53 ≤ b := Sizes.ofList_le hn
      have hz : t018_s4_g.offs b = IE.lit 0 := by
        simp [t018_s4_g, IE.split_ge hb, IE.sparse, h55]
      rw [hz]
      exact t018_sz_pos b nn hn)
    (fun b nn hn q hq => by
      have hb : 53 ≤ b := Sizes.ofList_le hn
      have hz : t018_s4_g.postOffs b = IE.lit 0 := by
        simp [t018_s4_g, IE.split_ge hb, IE.sparse]
      rw [hz]
      exact t018_sz_pos b nn hn)

/-- Stage 5 reads no intermediate past what was written there. -/
theorem t018_s5_loc {α : Type} [ExactScalar α] :
    SpecLocal t018_sz (t018_s5_g.spec (α := α)) :=
  GenRed.specLocal t018_s5_g t018_sz
    (fun b nn hn q kk hq hk => by
      by_cases h56 : b = 56
      · subst h56
        have hs : nn = 32514048 :=
          Sizes.ofList_some (by decide) (by decide) hn
        subst hs
        exact (bound_pack (A := 258048) (B := 126) (bound_pack (A := 2048) (B := 126) (bound_pack (A := 32) (B := 64) (bound_div (a := 32) (d := 2032128) hq) (ExactScalar.clamp_lt (c := 64) (by decide : (0 : Nat) < 64))) (bound_mod (c := 126) (by decide : (0 : Nat) < 126))) (bound_mod (c := 126) (by decide : (0 : Nat) < 126)))
      by_cases h57 : b = 57
      · subst h57
        have hs : nn = 32514048 :=
          Sizes.ofList_some (by decide) (by decide) hn
        subst hs
        exact (bound_pack (A := 258048) (B := 126) (bound_pack (A := 2048) (B := 126) (bound_pack (A := 32) (B := 64) (bound_div (a := 32) (d := 2032128) hq) (ExactScalar.clamp_lt (c := 64) (by decide : (0 : Nat) < 64))) (bound_mod (c := 126) (by decide : (0 : Nat) < 126))) (bound_mod (c := 126) (by decide : (0 : Nat) < 126)))
      have hb : 53 ≤ b := Sizes.ofList_le hn
      have hz : t018_s5_g.offs b = IE.lit 0 := by
        simp [t018_s5_g, IE.split_ge hb, IE.sparse, h56, h57]
      rw [hz]
      exact t018_sz_pos b nn hn)
    (fun b nn hn q hq => by
      have hb : 53 ≤ b := Sizes.ofList_le hn
      have hz : t018_s5_g.postOffs b = IE.lit 0 := by
        simp [t018_s5_g, IE.split_ge hb, IE.sparse]
      rw [hz]
      exact t018_sz_pos b nn hn)

/-- Stage 6 reads no intermediate past what was written there. -/
theorem t018_s6_loc {α : Type} [ExactScalar α] :
    SpecLocal t018_sz (t018_s6_g.spec (α := α)) :=
  GenRed.specLocal t018_s6_g t018_sz
    (fun b nn hn q kk hq hk => by
      by_cases h58 : b = 58
      · subst h58
        have hs : nn = 65028096 :=
          Sizes.ofList_some (by decide) (by decide) hn
        subst hs
        exact (bound_pack (A := 516096) (B := 126) (bound_pack (A := 4096) (B := 126) (bound_pack (A := 32) (B := 128) (bound_div (a := 32) (d := 254016) hq) hk) (bound_mod (c := 126) (by decide : (0 : Nat) < 126))) (bound_mod (c := 126) (by decide : (0 : Nat) < 126)))
      have hb : 53 ≤ b := Sizes.ofList_le hn
      have hz : t018_s6_g.offs b = IE.lit 0 := by
        simp [t018_s6_g, IE.split_ge hb, IE.sparse, h58]
      rw [hz]
      exact t018_sz_pos b nn hn)
    (fun b nn hn q hq => by
      have hb : 53 ≤ b := Sizes.ofList_le hn
      have hz : t018_s6_g.postOffs b = IE.lit 0 := by
        simp [t018_s6_g, IE.split_ge hb, IE.sparse]
      rw [hz]
      exact t018_sz_pos b nn hn)

/-- Stage 7 reads no intermediate past what was written there. -/
theorem t018_s7_loc {α : Type} [ExactScalar α] :
    SpecLocal t018_sz (t018_s7_g.spec (α := α)) :=
  GenRed.specLocal t018_s7_g t018_sz
    (fun b nn hn q kk hq hk => by
      by_cases h59 : b = 59
      · subst h59
        have hs : nn = 8128512 :=
          Sizes.ofList_some (by decide) (by decide) hn
        subst hs
        exact (bound_pack (A := 64512) (B := 126) (bound_pack (A := 512) (B := 126) (bound_pack (A := 32) (B := 16) (bound_div (a := 32) (d := 1016064) hq) hk) (bound_mod (c := 126) (by decide : (0 : Nat) < 126))) (bound_mod (c := 126) (by decide : (0 : Nat) < 126)))
      have hb : 53 ≤ b := Sizes.ofList_le hn
      have hz : t018_s7_g.offs b = IE.lit 0 := by
        simp [t018_s7_g, IE.split_ge hb, IE.sparse, h59]
      rw [hz]
      exact t018_sz_pos b nn hn)
    (fun b nn hn q hq => by
      have hb : 53 ≤ b := Sizes.ofList_le hn
      have hz : t018_s7_g.postOffs b = IE.lit 0 := by
        simp [t018_s7_g, IE.split_ge hb, IE.sparse]
      rw [hz]
      exact t018_sz_pos b nn hn)

/-- Stage 8 reads no intermediate past what was written there. -/
theorem t018_s8_loc {α : Type} [ExactScalar α] :
    SpecLocal t018_sz (t018_s8_g.spec (α := α)) :=
  GenRed.specLocal t018_s8_g t018_sz
    (fun b nn hn q kk hq hk => by
      by_cases h59 : b = 59
      · subst h59
        have hs : nn = 8128512 :=
          Sizes.ofList_some (by decide) (by decide) hn
        subst hs
        exact (ExactScalar.clamp_lt (c := 8128512) (by decide : (0 : Nat) < 8128512))
      have hb : 53 ≤ b := Sizes.ofList_le hn
      have hz : t018_s8_g.offs b = IE.lit 0 := by
        simp [t018_s8_g, IE.split_ge hb, IE.sparse, h59]
      rw [hz]
      exact t018_sz_pos b nn hn)
    (fun b nn hn q hq => by
      have hb : 53 ≤ b := Sizes.ofList_le hn
      have hz : t018_s8_g.postOffs b = IE.lit 0 := by
        simp [t018_s8_g, IE.split_ge hb, IE.sparse]
      rw [hz]
      exact t018_sz_pos b nn hn)

/-- Stage 9 reads no intermediate past what was written there. -/
theorem t018_s9_loc {α : Type} [ExactScalar α] :
    SpecLocal t018_sz (t018_s9_g.spec (α := α)) :=
  GenRed.specLocal t018_s9_g t018_sz
    (fun b nn hn q kk hq hk => by
      by_cases h60 : b = 60
      · subst h60
        have hs : nn = 32514048 :=
          Sizes.ofList_some (by decide) (by decide) hn
        subst hs
        exact (bound_pack (A := 258048) (B := 126) (bound_pack (A := 2048) (B := 126) (bound_pack (A := 32) (B := 64) (bound_div (a := 32) (d := 2032128) hq) (ExactScalar.clamp_lt (c := 64) (by decide : (0 : Nat) < 64))) (bound_mod (c := 126) (by decide : (0 : Nat) < 126))) (bound_mod (c := 126) (by decide : (0 : Nat) < 126)))
      by_cases h61 : b = 61
      · subst h61
        have hs : nn = 32514048 :=
          Sizes.ofList_some (by decide) (by decide) hn
        subst hs
        exact (bound_pack (A := 258048) (B := 126) (bound_pack (A := 2048) (B := 126) (bound_pack (A := 32) (B := 64) (bound_div (a := 32) (d := 2032128) hq) (ExactScalar.clamp_lt (c := 64) (by decide : (0 : Nat) < 64))) (bound_mod (c := 126) (by decide : (0 : Nat) < 126))) (bound_mod (c := 126) (by decide : (0 : Nat) < 126)))
      have hb : 53 ≤ b := Sizes.ofList_le hn
      have hz : t018_s9_g.offs b = IE.lit 0 := by
        simp [t018_s9_g, IE.split_ge hb, IE.sparse, h60, h61]
      rw [hz]
      exact t018_sz_pos b nn hn)
    (fun b nn hn q hq => by
      have hb : 53 ≤ b := Sizes.ofList_le hn
      have hz : t018_s9_g.postOffs b = IE.lit 0 := by
        simp [t018_s9_g, IE.split_ge hb, IE.sparse]
      rw [hz]
      exact t018_sz_pos b nn hn)

/-- Stage 10 reads no intermediate past what was written there. -/
theorem t018_s10_loc {α : Type} [ExactScalar α] :
    SpecLocal t018_sz (t018_s10_g.spec (α := α)) :=
  GenRed.specLocal t018_s10_g t018_sz
    (fun b nn hn q kk hq hk => by
      by_cases h62 : b = 62
      · subst h62
        have hs : nn = 65028096 :=
          Sizes.ofList_some (by decide) (by decide) hn
        subst hs
        exact (bound_pack (A := 516096) (B := 126) (bound_pack (A := 4096) (B := 126) (bound_pack (A := 32) (B := 128) (bound_div (a := 32) (d := 508032) hq) hk) (bound_mod (c := 126) (by decide : (0 : Nat) < 126))) (bound_mod (c := 126) (by decide : (0 : Nat) < 126)))
      have hb : 53 ≤ b := Sizes.ofList_le hn
      have hz : t018_s10_g.offs b = IE.lit 0 := by
        simp [t018_s10_g, IE.split_ge hb, IE.sparse, h62]
      rw [hz]
      exact t018_sz_pos b nn hn)
    (fun b nn hn q hq => by
      have hb : 53 ≤ b := Sizes.ofList_le hn
      have hz : t018_s10_g.postOffs b = IE.lit 0 := by
        simp [t018_s10_g, IE.split_ge hb, IE.sparse]
      rw [hz]
      exact t018_sz_pos b nn hn)

/-- Stage 11 reads no intermediate past what was written there. -/
theorem t018_s11_loc {α : Type} [ExactScalar α] :
    SpecLocal t018_sz (t018_s11_g.spec (α := α)) :=
  GenRed.specLocal t018_s11_g t018_sz
    (fun b nn hn q kk hq hk => by
      by_cases h63 : b = 63
      · subst h63
        have hs : nn = 16257024 :=
          Sizes.ofList_some (by decide) (by decide) hn
        subst hs
        exact (bound_pack (A := 129024) (B := 126) (bound_pack (A := 1024) (B := 126) (bound_pack (A := 32) (B := 32) (bound_div (a := 32) (d := 2032128) hq) hk) (bound_mod (c := 126) (by decide : (0 : Nat) < 126))) (bound_mod (c := 126) (by decide : (0 : Nat) < 126)))
      have hb : 53 ≤ b := Sizes.ofList_le hn
      have hz : t018_s11_g.offs b = IE.lit 0 := by
        simp [t018_s11_g, IE.split_ge hb, IE.sparse, h63]
      rw [hz]
      exact t018_sz_pos b nn hn)
    (fun b nn hn q hq => by
      have hb : 53 ≤ b := Sizes.ofList_le hn
      have hz : t018_s11_g.postOffs b = IE.lit 0 := by
        simp [t018_s11_g, IE.split_ge hb, IE.sparse]
      rw [hz]
      exact t018_sz_pos b nn hn)

/-- Stage 12 reads no intermediate past what was written there. -/
theorem t018_s12_loc {α : Type} [ExactScalar α] :
    SpecLocal t018_sz (t018_s12_g.spec (α := α)) :=
  GenRed.specLocal t018_s12_g t018_sz
    (fun b nn hn q kk hq hk => by
      by_cases h63 : b = 63
      · subst h63
        have hs : nn = 16257024 :=
          Sizes.ofList_some (by decide) (by decide) hn
        subst hs
        exact (ExactScalar.clamp_lt (c := 16257024) (by decide : (0 : Nat) < 16257024))
      have hb : 53 ≤ b := Sizes.ofList_le hn
      have hz : t018_s12_g.offs b = IE.lit 0 := by
        simp [t018_s12_g, IE.split_ge hb, IE.sparse, h63]
      rw [hz]
      exact t018_sz_pos b nn hn)
    (fun b nn hn q hq => by
      have hb : 53 ≤ b := Sizes.ofList_le hn
      have hz : t018_s12_g.postOffs b = IE.lit 0 := by
        simp [t018_s12_g, IE.split_ge hb, IE.sparse]
      rw [hz]
      exact t018_sz_pos b nn hn)

/-- Stage 13 reads no intermediate past what was written there. -/
theorem t018_s13_loc {α : Type} [ExactScalar α] :
    SpecLocal t018_sz (t018_s13_g.spec (α := α)) :=
  GenRed.specLocal t018_s13_g t018_sz
    (fun b nn hn q kk hq hk => by
      by_cases h64 : b = 64
      · subst h64
        have hs : nn = 65028096 :=
          Sizes.ofList_some (by decide) (by decide) hn
        subst hs
        exact (bound_pack (A := 516096) (B := 126) (bound_pack (A := 4096) (B := 126) (bound_pack (A := 32) (B := 128) (bound_div (a := 32) (d := 4064256) hq) (ExactScalar.clamp_lt (c := 128) (by decide : (0 : Nat) < 128))) (bound_mod (c := 126) (by decide : (0 : Nat) < 126))) (bound_mod (c := 126) (by decide : (0 : Nat) < 126)))
      by_cases h65 : b = 65
      · subst h65
        have hs : nn = 65028096 :=
          Sizes.ofList_some (by decide) (by decide) hn
        subst hs
        exact (bound_pack (A := 516096) (B := 126) (bound_pack (A := 4096) (B := 126) (bound_pack (A := 32) (B := 128) (bound_div (a := 32) (d := 4064256) hq) (ExactScalar.clamp_lt (c := 128) (by decide : (0 : Nat) < 128))) (bound_mod (c := 126) (by decide : (0 : Nat) < 126))) (bound_mod (c := 126) (by decide : (0 : Nat) < 126)))
      have hb : 53 ≤ b := Sizes.ofList_le hn
      have hz : t018_s13_g.offs b = IE.lit 0 := by
        simp [t018_s13_g, IE.split_ge hb, IE.sparse, h64, h65]
      rw [hz]
      exact t018_sz_pos b nn hn)
    (fun b nn hn q hq => by
      have hb : 53 ≤ b := Sizes.ofList_le hn
      have hz : t018_s13_g.postOffs b = IE.lit 0 := by
        simp [t018_s13_g, IE.split_ge hb, IE.sparse]
      rw [hz]
      exact t018_sz_pos b nn hn)

/-- Stage 14 reads no intermediate past what was written there. -/
theorem t018_s14_loc {α : Type} [ExactScalar α] :
    SpecLocal t018_sz (t018_s14_g.spec (α := α)) :=
  MaxRed.specLocal t018_s14_g t018_sz (by decide)
    (fun b nn hn q kk hq hk => by
      by_cases h66 : b = 66
      · subst h66
        have hs : nn = 130056192 :=
          Sizes.ofList_some (by decide) (by decide) hn
        subst hs
        exact (bound_pack (A := 1032192) (B := 126) (bound_pack (A := 8192) (B := 126) (bound_pack (A := 32) (B := 256) (bound_div (a := 32) (d := 1016064) hq) (bound_mod (c := 256) (by decide : (0 : Nat) < 256))) (ExactScalar.clamp_lt (c := 126) (by decide : (0 : Nat) < 126))) (ExactScalar.clamp_lt (c := 126) (by decide : (0 : Nat) < 126)))
      have hb : 53 ≤ b := Sizes.ofList_le hn
      have hz : t018_s14_g.offs b = IE.lit 0 := by
        simp [t018_s14_g, IE.split_ge hb, IE.sparse, h66]
      rw [hz]
      exact t018_sz_pos b nn hn)
    (fun b nn hn q hq => by
      have hb : 53 ≤ b := Sizes.ofList_le hn
      have hz : t018_s14_g.postOffs b = IE.lit 0 := by
        simp [t018_s14_g, IE.split_ge hb, IE.sparse]
      rw [hz]
      exact t018_sz_pos b nn hn)

/-- Stage 15 reads no intermediate past what was written there. -/
theorem t018_s15_loc {α : Type} [ExactScalar α] :
    SpecLocal t018_sz (t018_s15_g.spec (α := α)) :=
  GenRed.specLocal t018_s15_g t018_sz
    (fun b nn hn q kk hq hk => by
      by_cases h67 : b = 67
      · subst h67
        have hs : nn = 32514048 :=
          Sizes.ofList_some (by decide) (by decide) hn
        subst hs
        exact (bound_pack (A := 516096) (B := 63) (bound_pack (A := 8192) (B := 63) (bound_pack (A := 32) (B := 256) (bound_div (a := 32) (d := 127008) hq) hk) (bound_mod (c := 63) (by decide : (0 : Nat) < 63))) (bound_mod (c := 63) (by decide : (0 : Nat) < 63)))
      have hb : 53 ≤ b := Sizes.ofList_le hn
      have hz : t018_s15_g.offs b = IE.lit 0 := by
        simp [t018_s15_g, IE.split_ge hb, IE.sparse, h67]
      rw [hz]
      exact t018_sz_pos b nn hn)
    (fun b nn hn q hq => by
      have hb : 53 ≤ b := Sizes.ofList_le hn
      have hz : t018_s15_g.postOffs b = IE.lit 0 := by
        simp [t018_s15_g, IE.split_ge hb, IE.sparse]
      rw [hz]
      exact t018_sz_pos b nn hn)

/-- Stage 16 reads no intermediate past what was written there. -/
theorem t018_s16_loc {α : Type} [ExactScalar α] :
    SpecLocal t018_sz (t018_s16_g.spec (α := α)) :=
  GenRed.specLocal t018_s16_g t018_sz
    (fun b nn hn q kk hq hk => by
      by_cases h68 : b = 68
      · subst h68
        have hs : nn = 4064256 :=
          Sizes.ofList_some (by decide) (by decide) hn
        subst hs
        exact (bound_pack (A := 64512) (B := 63) (bound_pack (A := 1024) (B := 63) (bound_pack (A := 32) (B := 32) (bound_div (a := 32) (d := 508032) hq) hk) (bound_mod (c := 63) (by decide : (0 : Nat) < 63))) (bound_mod (c := 63) (by decide : (0 : Nat) < 63)))
      have hb : 53 ≤ b := Sizes.ofList_le hn
      have hz : t018_s16_g.offs b = IE.lit 0 := by
        simp [t018_s16_g, IE.split_ge hb, IE.sparse, h68]
      rw [hz]
      exact t018_sz_pos b nn hn)
    (fun b nn hn q hq => by
      have hb : 53 ≤ b := Sizes.ofList_le hn
      have hz : t018_s16_g.postOffs b = IE.lit 0 := by
        simp [t018_s16_g, IE.split_ge hb, IE.sparse]
      rw [hz]
      exact t018_sz_pos b nn hn)

/-- Stage 17 reads no intermediate past what was written there. -/
theorem t018_s17_loc {α : Type} [ExactScalar α] :
    SpecLocal t018_sz (t018_s17_g.spec (α := α)) :=
  GenRed.specLocal t018_s17_g t018_sz
    (fun b nn hn q kk hq hk => by
      by_cases h68 : b = 68
      · subst h68
        have hs : nn = 4064256 :=
          Sizes.ofList_some (by decide) (by decide) hn
        subst hs
        exact (ExactScalar.clamp_lt (c := 4064256) (by decide : (0 : Nat) < 4064256))
      have hb : 53 ≤ b := Sizes.ofList_le hn
      have hz : t018_s17_g.offs b = IE.lit 0 := by
        simp [t018_s17_g, IE.split_ge hb, IE.sparse, h68]
      rw [hz]
      exact t018_sz_pos b nn hn)
    (fun b nn hn q hq => by
      have hb : 53 ≤ b := Sizes.ofList_le hn
      have hz : t018_s17_g.postOffs b = IE.lit 0 := by
        simp [t018_s17_g, IE.split_ge hb, IE.sparse]
      rw [hz]
      exact t018_sz_pos b nn hn)

/-- Stage 18 reads no intermediate past what was written there. -/
theorem t018_s18_loc {α : Type} [ExactScalar α] :
    SpecLocal t018_sz (t018_s18_g.spec (α := α)) :=
  GenRed.specLocal t018_s18_g t018_sz
    (fun b nn hn q kk hq hk => by
      by_cases h69 : b = 69
      · subst h69
        have hs : nn = 16257024 :=
          Sizes.ofList_some (by decide) (by decide) hn
        subst hs
        exact (bound_pack (A := 258048) (B := 63) (bound_pack (A := 4096) (B := 63) (bound_pack (A := 32) (B := 128) (bound_div (a := 32) (d := 1016064) hq) (ExactScalar.clamp_lt (c := 128) (by decide : (0 : Nat) < 128))) (bound_mod (c := 63) (by decide : (0 : Nat) < 63))) (bound_mod (c := 63) (by decide : (0 : Nat) < 63)))
      by_cases h70 : b = 70
      · subst h70
        have hs : nn = 16257024 :=
          Sizes.ofList_some (by decide) (by decide) hn
        subst hs
        exact (bound_pack (A := 258048) (B := 63) (bound_pack (A := 4096) (B := 63) (bound_pack (A := 32) (B := 128) (bound_div (a := 32) (d := 1016064) hq) (ExactScalar.clamp_lt (c := 128) (by decide : (0 : Nat) < 128))) (bound_mod (c := 63) (by decide : (0 : Nat) < 63))) (bound_mod (c := 63) (by decide : (0 : Nat) < 63)))
      have hb : 53 ≤ b := Sizes.ofList_le hn
      have hz : t018_s18_g.offs b = IE.lit 0 := by
        simp [t018_s18_g, IE.split_ge hb, IE.sparse, h69, h70]
      rw [hz]
      exact t018_sz_pos b nn hn)
    (fun b nn hn q hq => by
      have hb : 53 ≤ b := Sizes.ofList_le hn
      have hz : t018_s18_g.postOffs b = IE.lit 0 := by
        simp [t018_s18_g, IE.split_ge hb, IE.sparse]
      rw [hz]
      exact t018_sz_pos b nn hn)

/-- Stage 19 reads no intermediate past what was written there. -/
theorem t018_s19_loc {α : Type} [ExactScalar α] :
    SpecLocal t018_sz (t018_s19_g.spec (α := α)) :=
  GenRed.specLocal t018_s19_g t018_sz
    (fun b nn hn q kk hq hk => by
      by_cases h71 : b = 71
      · subst h71
        have hs : nn = 32514048 :=
          Sizes.ofList_some (by decide) (by decide) hn
        subst hs
        exact (bound_pack (A := 516096) (B := 63) (bound_pack (A := 8192) (B := 63) (bound_pack (A := 32) (B := 256) (bound_div (a := 32) (d := 190512) hq) hk) (bound_mod (c := 63) (by decide : (0 : Nat) < 63))) (bound_mod (c := 63) (by decide : (0 : Nat) < 63)))
      have hb : 53 ≤ b := Sizes.ofList_le hn
      have hz : t018_s19_g.offs b = IE.lit 0 := by
        simp [t018_s19_g, IE.split_ge hb, IE.sparse, h71]
      rw [hz]
      exact t018_sz_pos b nn hn)
    (fun b nn hn q hq => by
      have hb : 53 ≤ b := Sizes.ofList_le hn
      have hz : t018_s19_g.postOffs b = IE.lit 0 := by
        simp [t018_s19_g, IE.split_ge hb, IE.sparse]
      rw [hz]
      exact t018_sz_pos b nn hn)

/-- Stage 20 reads no intermediate past what was written there. -/
theorem t018_s20_loc {α : Type} [ExactScalar α] :
    SpecLocal t018_sz (t018_s20_g.spec (α := α)) :=
  GenRed.specLocal t018_s20_g t018_sz
    (fun b nn hn q kk hq hk => by
      by_cases h72 : b = 72
      · subst h72
        have hs : nn = 6096384 :=
          Sizes.ofList_some (by decide) (by decide) hn
        subst hs
        exact (bound_pack (A := 96768) (B := 63) (bound_pack (A := 1536) (B := 63) (bound_pack (A := 32) (B := 48) (bound_div (a := 32) (d := 762048) hq) hk) (bound_mod (c := 63) (by decide : (0 : Nat) < 63))) (bound_mod (c := 63) (by decide : (0 : Nat) < 63)))
      have hb : 53 ≤ b := Sizes.ofList_le hn
      have hz : t018_s20_g.offs b = IE.lit 0 := by
        simp [t018_s20_g, IE.split_ge hb, IE.sparse, h72]
      rw [hz]
      exact t018_sz_pos b nn hn)
    (fun b nn hn q hq => by
      have hb : 53 ≤ b := Sizes.ofList_le hn
      have hz : t018_s20_g.postOffs b = IE.lit 0 := by
        simp [t018_s20_g, IE.split_ge hb, IE.sparse]
      rw [hz]
      exact t018_sz_pos b nn hn)

/-- Stage 21 reads no intermediate past what was written there. -/
theorem t018_s21_loc {α : Type} [ExactScalar α] :
    SpecLocal t018_sz (t018_s21_g.spec (α := α)) :=
  GenRed.specLocal t018_s21_g t018_sz
    (fun b nn hn q kk hq hk => by
      by_cases h72 : b = 72
      · subst h72
        have hs : nn = 6096384 :=
          Sizes.ofList_some (by decide) (by decide) hn
        subst hs
        exact (ExactScalar.clamp_lt (c := 6096384) (by decide : (0 : Nat) < 6096384))
      have hb : 53 ≤ b := Sizes.ofList_le hn
      have hz : t018_s21_g.offs b = IE.lit 0 := by
        simp [t018_s21_g, IE.split_ge hb, IE.sparse, h72]
      rw [hz]
      exact t018_sz_pos b nn hn)
    (fun b nn hn q hq => by
      have hb : 53 ≤ b := Sizes.ofList_le hn
      have hz : t018_s21_g.postOffs b = IE.lit 0 := by
        simp [t018_s21_g, IE.split_ge hb, IE.sparse]
      rw [hz]
      exact t018_sz_pos b nn hn)

/-- Stage 22 reads no intermediate past what was written there. -/
theorem t018_s22_loc {α : Type} [ExactScalar α] :
    SpecLocal t018_sz (t018_s22_g.spec (α := α)) :=
  GenRed.specLocal t018_s22_g t018_sz
    (fun b nn hn q kk hq hk => by
      by_cases h73 : b = 73
      · subst h73
        have hs : nn = 24385536 :=
          Sizes.ofList_some (by decide) (by decide) hn
        subst hs
        exact (bound_pack (A := 387072) (B := 63) (bound_pack (A := 6144) (B := 63) (bound_pack (A := 32) (B := 192) (bound_div (a := 32) (d := 1524096) hq) (ExactScalar.clamp_lt (c := 192) (by decide : (0 : Nat) < 192))) (bound_mod (c := 63) (by decide : (0 : Nat) < 63))) (bound_mod (c := 63) (by decide : (0 : Nat) < 63)))
      by_cases h74 : b = 74
      · subst h74
        have hs : nn = 24385536 :=
          Sizes.ofList_some (by decide) (by decide) hn
        subst hs
        exact (bound_pack (A := 387072) (B := 63) (bound_pack (A := 6144) (B := 63) (bound_pack (A := 32) (B := 192) (bound_div (a := 32) (d := 1524096) hq) (ExactScalar.clamp_lt (c := 192) (by decide : (0 : Nat) < 192))) (bound_mod (c := 63) (by decide : (0 : Nat) < 63))) (bound_mod (c := 63) (by decide : (0 : Nat) < 63)))
      have hb : 53 ≤ b := Sizes.ofList_le hn
      have hz : t018_s22_g.offs b = IE.lit 0 := by
        simp [t018_s22_g, IE.split_ge hb, IE.sparse, h73, h74]
      rw [hz]
      exact t018_sz_pos b nn hn)
    (fun b nn hn q hq => by
      have hb : 53 ≤ b := Sizes.ofList_le hn
      have hz : t018_s22_g.postOffs b = IE.lit 0 := by
        simp [t018_s22_g, IE.split_ge hb, IE.sparse]
      rw [hz]
      exact t018_sz_pos b nn hn)

/-- Stage 23 reads no intermediate past what was written there. -/
theorem t018_s23_loc {α : Type} [ExactScalar α] :
    SpecLocal t018_sz (t018_s23_g.spec (α := α)) :=
  GenRed.specLocal t018_s23_g t018_sz
    (fun b nn hn q kk hq hk => by
      by_cases h75 : b = 75
      · subst h75
        have hs : nn = 48771072 :=
          Sizes.ofList_some (by decide) (by decide) hn
        subst hs
        exact (bound_pack (A := 774144) (B := 63) (bound_pack (A := 12288) (B := 63) (bound_pack (A := 32) (B := 384) (bound_div (a := 32) (d := 190512) hq) hk) (bound_mod (c := 63) (by decide : (0 : Nat) < 63))) (bound_mod (c := 63) (by decide : (0 : Nat) < 63)))
      have hb : 53 ≤ b := Sizes.ofList_le hn
      have hz : t018_s23_g.offs b = IE.lit 0 := by
        simp [t018_s23_g, IE.split_ge hb, IE.sparse, h75]
      rw [hz]
      exact t018_sz_pos b nn hn)
    (fun b nn hn q hq => by
      have hb : 53 ≤ b := Sizes.ofList_le hn
      have hz : t018_s23_g.postOffs b = IE.lit 0 := by
        simp [t018_s23_g, IE.split_ge hb, IE.sparse]
      rw [hz]
      exact t018_sz_pos b nn hn)

/-- Stage 24 reads no intermediate past what was written there. -/
theorem t018_s24_loc {α : Type} [ExactScalar α] :
    SpecLocal t018_sz (t018_s24_g.spec (α := α)) :=
  GenRed.specLocal t018_s24_g t018_sz
    (fun b nn hn q kk hq hk => by
      by_cases h76 : b = 76
      · subst h76
        have hs : nn = 6096384 :=
          Sizes.ofList_some (by decide) (by decide) hn
        subst hs
        exact (bound_pack (A := 96768) (B := 63) (bound_pack (A := 1536) (B := 63) (bound_pack (A := 32) (B := 48) (bound_div (a := 32) (d := 762048) hq) hk) (bound_mod (c := 63) (by decide : (0 : Nat) < 63))) (bound_mod (c := 63) (by decide : (0 : Nat) < 63)))
      have hb : 53 ≤ b := Sizes.ofList_le hn
      have hz : t018_s24_g.offs b = IE.lit 0 := by
        simp [t018_s24_g, IE.split_ge hb, IE.sparse, h76]
      rw [hz]
      exact t018_sz_pos b nn hn)
    (fun b nn hn q hq => by
      have hb : 53 ≤ b := Sizes.ofList_le hn
      have hz : t018_s24_g.postOffs b = IE.lit 0 := by
        simp [t018_s24_g, IE.split_ge hb, IE.sparse]
      rw [hz]
      exact t018_sz_pos b nn hn)

/-- Stage 25 reads no intermediate past what was written there. -/
theorem t018_s25_loc {α : Type} [ExactScalar α] :
    SpecLocal t018_sz (t018_s25_g.spec (α := α)) :=
  GenRed.specLocal t018_s25_g t018_sz
    (fun b nn hn q kk hq hk => by
      by_cases h76 : b = 76
      · subst h76
        have hs : nn = 6096384 :=
          Sizes.ofList_some (by decide) (by decide) hn
        subst hs
        exact (ExactScalar.clamp_lt (c := 6096384) (by decide : (0 : Nat) < 6096384))
      have hb : 53 ≤ b := Sizes.ofList_le hn
      have hz : t018_s25_g.offs b = IE.lit 0 := by
        simp [t018_s25_g, IE.split_ge hb, IE.sparse, h76]
      rw [hz]
      exact t018_sz_pos b nn hn)
    (fun b nn hn q hq => by
      have hb : 53 ≤ b := Sizes.ofList_le hn
      have hz : t018_s25_g.postOffs b = IE.lit 0 := by
        simp [t018_s25_g, IE.split_ge hb, IE.sparse]
      rw [hz]
      exact t018_sz_pos b nn hn)

/-- Stage 26 reads no intermediate past what was written there. -/
theorem t018_s26_loc {α : Type} [ExactScalar α] :
    SpecLocal t018_sz (t018_s26_g.spec (α := α)) :=
  GenRed.specLocal t018_s26_g t018_sz
    (fun b nn hn q kk hq hk => by
      by_cases h77 : b = 77
      · subst h77
        have hs : nn = 24385536 :=
          Sizes.ofList_some (by decide) (by decide) hn
        subst hs
        exact (bound_pack (A := 387072) (B := 63) (bound_pack (A := 6144) (B := 63) (bound_pack (A := 32) (B := 192) (bound_div (a := 32) (d := 1524096) hq) (ExactScalar.clamp_lt (c := 192) (by decide : (0 : Nat) < 192))) (bound_mod (c := 63) (by decide : (0 : Nat) < 63))) (bound_mod (c := 63) (by decide : (0 : Nat) < 63)))
      by_cases h78 : b = 78
      · subst h78
        have hs : nn = 24385536 :=
          Sizes.ofList_some (by decide) (by decide) hn
        subst hs
        exact (bound_pack (A := 387072) (B := 63) (bound_pack (A := 6144) (B := 63) (bound_pack (A := 32) (B := 192) (bound_div (a := 32) (d := 1524096) hq) (ExactScalar.clamp_lt (c := 192) (by decide : (0 : Nat) < 192))) (bound_mod (c := 63) (by decide : (0 : Nat) < 63))) (bound_mod (c := 63) (by decide : (0 : Nat) < 63)))
      have hb : 53 ≤ b := Sizes.ofList_le hn
      have hz : t018_s26_g.offs b = IE.lit 0 := by
        simp [t018_s26_g, IE.split_ge hb, IE.sparse, h77, h78]
      rw [hz]
      exact t018_sz_pos b nn hn)
    (fun b nn hn q hq => by
      have hb : 53 ≤ b := Sizes.ofList_le hn
      have hz : t018_s26_g.postOffs b = IE.lit 0 := by
        simp [t018_s26_g, IE.split_ge hb, IE.sparse]
      rw [hz]
      exact t018_sz_pos b nn hn)

/-- Stage 27 reads no intermediate past what was written there. -/
theorem t018_s27_loc {α : Type} [ExactScalar α] :
    SpecLocal t018_sz (t018_s27_g.spec (α := α)) :=
  GenRed.specLocal t018_s27_g t018_sz
    (fun b nn hn q kk hq hk => by
      by_cases h79 : b = 79
      · subst h79
        have hs : nn = 48771072 :=
          Sizes.ofList_some (by decide) (by decide) hn
        subst hs
        exact (bound_pack (A := 774144) (B := 63) (bound_pack (A := 12288) (B := 63) (bound_pack (A := 32) (B := 384) (bound_div (a := 32) (d := 254016) hq) hk) (bound_mod (c := 63) (by decide : (0 : Nat) < 63))) (bound_mod (c := 63) (by decide : (0 : Nat) < 63)))
      have hb : 53 ≤ b := Sizes.ofList_le hn
      have hz : t018_s27_g.offs b = IE.lit 0 := by
        simp [t018_s27_g, IE.split_ge hb, IE.sparse, h79]
      rw [hz]
      exact t018_sz_pos b nn hn)
    (fun b nn hn q hq => by
      have hb : 53 ≤ b := Sizes.ofList_le hn
      have hz : t018_s27_g.postOffs b = IE.lit 0 := by
        simp [t018_s27_g, IE.split_ge hb, IE.sparse]
      rw [hz]
      exact t018_sz_pos b nn hn)

/-- Stage 28 reads no intermediate past what was written there. -/
theorem t018_s28_loc {α : Type} [ExactScalar α] :
    SpecLocal t018_sz (t018_s28_g.spec (α := α)) :=
  GenRed.specLocal t018_s28_g t018_sz
    (fun b nn hn q kk hq hk => by
      by_cases h80 : b = 80
      · subst h80
        have hs : nn = 8128512 :=
          Sizes.ofList_some (by decide) (by decide) hn
        subst hs
        exact (bound_pack (A := 129024) (B := 63) (bound_pack (A := 2048) (B := 63) (bound_pack (A := 32) (B := 64) (bound_div (a := 32) (d := 1016064) hq) hk) (bound_mod (c := 63) (by decide : (0 : Nat) < 63))) (bound_mod (c := 63) (by decide : (0 : Nat) < 63)))
      have hb : 53 ≤ b := Sizes.ofList_le hn
      have hz : t018_s28_g.offs b = IE.lit 0 := by
        simp [t018_s28_g, IE.split_ge hb, IE.sparse, h80]
      rw [hz]
      exact t018_sz_pos b nn hn)
    (fun b nn hn q hq => by
      have hb : 53 ≤ b := Sizes.ofList_le hn
      have hz : t018_s28_g.postOffs b = IE.lit 0 := by
        simp [t018_s28_g, IE.split_ge hb, IE.sparse]
      rw [hz]
      exact t018_sz_pos b nn hn)

/-- Stage 29 reads no intermediate past what was written there. -/
theorem t018_s29_loc {α : Type} [ExactScalar α] :
    SpecLocal t018_sz (t018_s29_g.spec (α := α)) :=
  GenRed.specLocal t018_s29_g t018_sz
    (fun b nn hn q kk hq hk => by
      by_cases h80 : b = 80
      · subst h80
        have hs : nn = 8128512 :=
          Sizes.ofList_some (by decide) (by decide) hn
        subst hs
        exact (ExactScalar.clamp_lt (c := 8128512) (by decide : (0 : Nat) < 8128512))
      have hb : 53 ≤ b := Sizes.ofList_le hn
      have hz : t018_s29_g.offs b = IE.lit 0 := by
        simp [t018_s29_g, IE.split_ge hb, IE.sparse, h80]
      rw [hz]
      exact t018_sz_pos b nn hn)
    (fun b nn hn q hq => by
      have hb : 53 ≤ b := Sizes.ofList_le hn
      have hz : t018_s29_g.postOffs b = IE.lit 0 := by
        simp [t018_s29_g, IE.split_ge hb, IE.sparse]
      rw [hz]
      exact t018_sz_pos b nn hn)

/-- Stage 30 reads no intermediate past what was written there. -/
theorem t018_s30_loc {α : Type} [ExactScalar α] :
    SpecLocal t018_sz (t018_s30_g.spec (α := α)) :=
  GenRed.specLocal t018_s30_g t018_sz
    (fun b nn hn q kk hq hk => by
      by_cases h81 : b = 81
      · subst h81
        have hs : nn = 32514048 :=
          Sizes.ofList_some (by decide) (by decide) hn
        subst hs
        exact (bound_pack (A := 516096) (B := 63) (bound_pack (A := 8192) (B := 63) (bound_pack (A := 32) (B := 256) (bound_div (a := 32) (d := 2032128) hq) (ExactScalar.clamp_lt (c := 256) (by decide : (0 : Nat) < 256))) (bound_mod (c := 63) (by decide : (0 : Nat) < 63))) (bound_mod (c := 63) (by decide : (0 : Nat) < 63)))
      by_cases h82 : b = 82
      · subst h82
        have hs : nn = 32514048 :=
          Sizes.ofList_some (by decide) (by decide) hn
        subst hs
        exact (bound_pack (A := 516096) (B := 63) (bound_pack (A := 8192) (B := 63) (bound_pack (A := 32) (B := 256) (bound_div (a := 32) (d := 2032128) hq) (ExactScalar.clamp_lt (c := 256) (by decide : (0 : Nat) < 256))) (bound_mod (c := 63) (by decide : (0 : Nat) < 63))) (bound_mod (c := 63) (by decide : (0 : Nat) < 63)))
      have hb : 53 ≤ b := Sizes.ofList_le hn
      have hz : t018_s30_g.offs b = IE.lit 0 := by
        simp [t018_s30_g, IE.split_ge hb, IE.sparse, h81, h82]
      rw [hz]
      exact t018_sz_pos b nn hn)
    (fun b nn hn q hq => by
      have hb : 53 ≤ b := Sizes.ofList_le hn
      have hz : t018_s30_g.postOffs b = IE.lit 0 := by
        simp [t018_s30_g, IE.split_ge hb, IE.sparse]
      rw [hz]
      exact t018_sz_pos b nn hn)

/-- Stage 31 reads no intermediate past what was written there. -/
theorem t018_s31_loc {α : Type} [ExactScalar α] :
    SpecLocal t018_sz (t018_s31_g.spec (α := α)) :=
  MaxRed.specLocal t018_s31_g t018_sz (by decide)
    (fun b nn hn q kk hq hk => by
      by_cases h83 : b = 83
      · subst h83
        have hs : nn = 65028096 :=
          Sizes.ofList_some (by decide) (by decide) hn
        subst hs
        exact (bound_pack (A := 1032192) (B := 63) (bound_pack (A := 16384) (B := 63) (bound_pack (A := 32) (B := 512) (bound_div (a := 32) (d := 492032) hq) (bound_mod (c := 512) (by decide : (0 : Nat) < 512))) (ExactScalar.clamp_lt (c := 63) (by decide : (0 : Nat) < 63))) (ExactScalar.clamp_lt (c := 63) (by decide : (0 : Nat) < 63)))
      have hb : 53 ≤ b := Sizes.ofList_le hn
      have hz : t018_s31_g.offs b = IE.lit 0 := by
        simp [t018_s31_g, IE.split_ge hb, IE.sparse, h83]
      rw [hz]
      exact t018_sz_pos b nn hn)
    (fun b nn hn q hq => by
      have hb : 53 ≤ b := Sizes.ofList_le hn
      have hz : t018_s31_g.postOffs b = IE.lit 0 := by
        simp [t018_s31_g, IE.split_ge hb, IE.sparse]
      rw [hz]
      exact t018_sz_pos b nn hn)

/-- Stage 32 reads no intermediate past what was written there. -/
theorem t018_s32_loc {α : Type} [ExactScalar α] :
    SpecLocal t018_sz (t018_s32_g.spec (α := α)) :=
  GenRed.specLocal t018_s32_g t018_sz
    (fun b nn hn q kk hq hk => by
      by_cases h84 : b = 84
      · subst h84
        have hs : nn = 15745024 :=
          Sizes.ofList_some (by decide) (by decide) hn
        subst hs
        exact (bound_pack (A := 507904) (B := 31) (bound_pack (A := 16384) (B := 31) (bound_pack (A := 32) (B := 512) (bound_div (a := 32) (d := 61504) hq) hk) (bound_mod (c := 31) (by decide : (0 : Nat) < 31))) (bound_mod (c := 31) (by decide : (0 : Nat) < 31)))
      have hb : 53 ≤ b := Sizes.ofList_le hn
      have hz : t018_s32_g.offs b = IE.lit 0 := by
        simp [t018_s32_g, IE.split_ge hb, IE.sparse, h84]
      rw [hz]
      exact t018_sz_pos b nn hn)
    (fun b nn hn q hq => by
      have hb : 53 ≤ b := Sizes.ofList_le hn
      have hz : t018_s32_g.postOffs b = IE.lit 0 := by
        simp [t018_s32_g, IE.split_ge hb, IE.sparse]
      rw [hz]
      exact t018_sz_pos b nn hn)

/-- Stage 33 reads no intermediate past what was written there. -/
theorem t018_s33_loc {α : Type} [ExactScalar α] :
    SpecLocal t018_sz (t018_s33_g.spec (α := α)) :=
  GenRed.specLocal t018_s33_g t018_sz
    (fun b nn hn q kk hq hk => by
      by_cases h85 : b = 85
      · subst h85
        have hs : nn = 1968128 :=
          Sizes.ofList_some (by decide) (by decide) hn
        subst hs
        exact (bound_pack (A := 63488) (B := 31) (bound_pack (A := 2048) (B := 31) (bound_pack (A := 32) (B := 64) (bound_div (a := 32) (d := 246016) hq) hk) (bound_mod (c := 31) (by decide : (0 : Nat) < 31))) (bound_mod (c := 31) (by decide : (0 : Nat) < 31)))
      have hb : 53 ≤ b := Sizes.ofList_le hn
      have hz : t018_s33_g.offs b = IE.lit 0 := by
        simp [t018_s33_g, IE.split_ge hb, IE.sparse, h85]
      rw [hz]
      exact t018_sz_pos b nn hn)
    (fun b nn hn q hq => by
      have hb : 53 ≤ b := Sizes.ofList_le hn
      have hz : t018_s33_g.postOffs b = IE.lit 0 := by
        simp [t018_s33_g, IE.split_ge hb, IE.sparse]
      rw [hz]
      exact t018_sz_pos b nn hn)

/-- Stage 34 reads no intermediate past what was written there. -/
theorem t018_s34_loc {α : Type} [ExactScalar α] :
    SpecLocal t018_sz (t018_s34_g.spec (α := α)) :=
  GenRed.specLocal t018_s34_g t018_sz
    (fun b nn hn q kk hq hk => by
      by_cases h85 : b = 85
      · subst h85
        have hs : nn = 1968128 :=
          Sizes.ofList_some (by decide) (by decide) hn
        subst hs
        exact (ExactScalar.clamp_lt (c := 1968128) (by decide : (0 : Nat) < 1968128))
      have hb : 53 ≤ b := Sizes.ofList_le hn
      have hz : t018_s34_g.offs b = IE.lit 0 := by
        simp [t018_s34_g, IE.split_ge hb, IE.sparse, h85]
      rw [hz]
      exact t018_sz_pos b nn hn)
    (fun b nn hn q hq => by
      have hb : 53 ≤ b := Sizes.ofList_le hn
      have hz : t018_s34_g.postOffs b = IE.lit 0 := by
        simp [t018_s34_g, IE.split_ge hb, IE.sparse]
      rw [hz]
      exact t018_sz_pos b nn hn)

/-- Stage 35 reads no intermediate past what was written there. -/
theorem t018_s35_loc {α : Type} [ExactScalar α] :
    SpecLocal t018_sz (t018_s35_g.spec (α := α)) :=
  GenRed.specLocal t018_s35_g t018_sz
    (fun b nn hn q kk hq hk => by
      by_cases h86 : b = 86
      · subst h86
        have hs : nn = 7872512 :=
          Sizes.ofList_some (by decide) (by decide) hn
        subst hs
        exact (bound_pack (A := 253952) (B := 31) (bound_pack (A := 8192) (B := 31) (bound_pack (A := 32) (B := 256) (bound_div (a := 32) (d := 492032) hq) (ExactScalar.clamp_lt (c := 256) (by decide : (0 : Nat) < 256))) (bound_mod (c := 31) (by decide : (0 : Nat) < 31))) (bound_mod (c := 31) (by decide : (0 : Nat) < 31)))
      by_cases h87 : b = 87
      · subst h87
        have hs : nn = 7872512 :=
          Sizes.ofList_some (by decide) (by decide) hn
        subst hs
        exact (bound_pack (A := 253952) (B := 31) (bound_pack (A := 8192) (B := 31) (bound_pack (A := 32) (B := 256) (bound_div (a := 32) (d := 492032) hq) (ExactScalar.clamp_lt (c := 256) (by decide : (0 : Nat) < 256))) (bound_mod (c := 31) (by decide : (0 : Nat) < 31))) (bound_mod (c := 31) (by decide : (0 : Nat) < 31)))
      have hb : 53 ≤ b := Sizes.ofList_le hn
      have hz : t018_s35_g.offs b = IE.lit 0 := by
        simp [t018_s35_g, IE.split_ge hb, IE.sparse, h86, h87]
      rw [hz]
      exact t018_sz_pos b nn hn)
    (fun b nn hn q hq => by
      have hb : 53 ≤ b := Sizes.ofList_le hn
      have hz : t018_s35_g.postOffs b = IE.lit 0 := by
        simp [t018_s35_g, IE.split_ge hb, IE.sparse]
      rw [hz]
      exact t018_sz_pos b nn hn)

/-- Stage 36 reads no intermediate past what was written there. -/
theorem t018_s36_loc {α : Type} [ExactScalar α] :
    SpecLocal t018_sz (t018_s36_g.spec (α := α)) :=
  GenRed.specLocal t018_s36_g t018_sz
    (fun b nn hn q kk hq hk => by
      by_cases h88 : b = 88
      · subst h88
        have hs : nn = 15745024 :=
          Sizes.ofList_some (by decide) (by decide) hn
        subst hs
        exact (bound_pack (A := 507904) (B := 31) (bound_pack (A := 16384) (B := 31) (bound_pack (A := 32) (B := 512) (bound_div (a := 32) (d := 961000) hq) hk) (bound_mod (c := 31) (by decide : (0 : Nat) < 31))) (bound_mod (c := 31) (by decide : (0 : Nat) < 31)))
      have hb : 53 ≤ b := Sizes.ofList_le hn
      have hz : t018_s36_g.offs b = IE.lit 0 := by
        simp [t018_s36_g, IE.split_ge hb, IE.sparse, h88]
      rw [hz]
      exact t018_sz_pos b nn hn)
    (fun b nn hn q hq => by
      have hb : 53 ≤ b := Sizes.ofList_le hn
      have hz : t018_s36_g.postOffs b = IE.lit 0 := by
        simp [t018_s36_g, IE.split_ge hb, IE.sparse]
      rw [hz]
      exact t018_sz_pos b nn hn)

/-- Stage 37 reads no intermediate past what was written there. -/
theorem t018_s37_loc {α : Type} [ExactScalar α] :
    SpecLocal t018_sz (t018_s37_g.spec (α := α)) :=
  GenRed.specLocal t018_s37_g t018_sz
    (fun b nn hn q kk hq hk => by
      by_cases h89 : b = 89
      · subst h89
        have hs : nn = 30752000 :=
          Sizes.ofList_some (by decide) (by decide) hn
        subst hs
        exact (bound_pack (A := 32000) (B := 961) hq hk)
      have hb : 53 ≤ b := Sizes.ofList_le hn
      have hz : t018_s37_g.offs b = IE.lit 0 := by
        simp [t018_s37_g, IE.split_ge hb, IE.sparse, h89]
      rw [hz]
      exact t018_sz_pos b nn hn)
    (fun b nn hn q hq => by
      have hb : 53 ≤ b := Sizes.ofList_le hn
      have hz : t018_s37_g.postOffs b = IE.lit 0 := by
        simp [t018_s37_g, IE.split_ge hb, IE.sparse]
      rw [hz]
      exact t018_sz_pos b nn hn)

def t018_chain (α : Type) [ExactScalar α] : List (Stage α) := [⟨t018_s0_g.prog t018_s0_block t018_s0_nkb, t018_s0_g.spec (α := α), 53⟩, ⟨t018_s1_g.prog t018_s1_block t018_s1_nkb, t018_s1_g.spec (α := α), 54⟩, ⟨t018_s2_g.prog t018_s2_block t018_s2_nkb, t018_s2_g.spec (α := α), 55⟩, ⟨t018_s3_g.prog t018_s3_block t018_s3_nkb, t018_s3_g.spec (α := α), 56⟩, ⟨t018_s4_g.prog t018_s4_block t018_s4_nkb, t018_s4_g.spec (α := α), 57⟩, ⟨t018_s5_g.prog t018_s5_block t018_s5_nkb, t018_s5_g.spec (α := α), 58⟩, ⟨t018_s6_g.prog t018_s6_block t018_s6_nkb, t018_s6_g.spec (α := α), 59⟩, ⟨t018_s7_g.prog t018_s7_block t018_s7_nkb, t018_s7_g.spec (α := α), 60⟩, ⟨t018_s8_g.prog t018_s8_block t018_s8_nkb, t018_s8_g.spec (α := α), 61⟩, ⟨t018_s9_g.prog t018_s9_block t018_s9_nkb, t018_s9_g.spec (α := α), 62⟩, ⟨t018_s10_g.prog t018_s10_block t018_s10_nkb, t018_s10_g.spec (α := α), 63⟩, ⟨t018_s11_g.prog t018_s11_block t018_s11_nkb, t018_s11_g.spec (α := α), 64⟩, ⟨t018_s12_g.prog t018_s12_block t018_s12_nkb, t018_s12_g.spec (α := α), 65⟩, ⟨t018_s13_g.prog t018_s13_block t018_s13_nkb, t018_s13_g.spec (α := α), 66⟩, ⟨t018_s14_g.prog t018_s14_block t018_s14_nkb, t018_s14_g.spec (α := α), 67⟩, ⟨t018_s15_g.prog t018_s15_block t018_s15_nkb, t018_s15_g.spec (α := α), 68⟩, ⟨t018_s16_g.prog t018_s16_block t018_s16_nkb, t018_s16_g.spec (α := α), 69⟩, ⟨t018_s17_g.prog t018_s17_block t018_s17_nkb, t018_s17_g.spec (α := α), 70⟩, ⟨t018_s18_g.prog t018_s18_block t018_s18_nkb, t018_s18_g.spec (α := α), 71⟩, ⟨t018_s19_g.prog t018_s19_block t018_s19_nkb, t018_s19_g.spec (α := α), 72⟩, ⟨t018_s20_g.prog t018_s20_block t018_s20_nkb, t018_s20_g.spec (α := α), 73⟩, ⟨t018_s21_g.prog t018_s21_block t018_s21_nkb, t018_s21_g.spec (α := α), 74⟩, ⟨t018_s22_g.prog t018_s22_block t018_s22_nkb, t018_s22_g.spec (α := α), 75⟩, ⟨t018_s23_g.prog t018_s23_block t018_s23_nkb, t018_s23_g.spec (α := α), 76⟩, ⟨t018_s24_g.prog t018_s24_block t018_s24_nkb, t018_s24_g.spec (α := α), 77⟩, ⟨t018_s25_g.prog t018_s25_block t018_s25_nkb, t018_s25_g.spec (α := α), 78⟩, ⟨t018_s26_g.prog t018_s26_block t018_s26_nkb, t018_s26_g.spec (α := α), 79⟩, ⟨t018_s27_g.prog t018_s27_block t018_s27_nkb, t018_s27_g.spec (α := α), 80⟩, ⟨t018_s28_g.prog t018_s28_block t018_s28_nkb, t018_s28_g.spec (α := α), 81⟩, ⟨t018_s29_g.prog t018_s29_block t018_s29_nkb, t018_s29_g.spec (α := α), 82⟩, ⟨t018_s30_g.prog t018_s30_block t018_s30_nkb, t018_s30_g.spec (α := α), 83⟩, ⟨t018_s31_g.prog t018_s31_block t018_s31_nkb, t018_s31_g.spec (α := α), 84⟩, ⟨t018_s32_g.prog t018_s32_block t018_s32_nkb, t018_s32_g.spec (α := α), 85⟩, ⟨t018_s33_g.prog t018_s33_block t018_s33_nkb, t018_s33_g.spec (α := α), 86⟩, ⟨t018_s34_g.prog t018_s34_block t018_s34_nkb, t018_s34_g.spec (α := α), 87⟩, ⟨t018_s35_g.prog t018_s35_block t018_s35_nkb, t018_s35_g.spec (α := α), 88⟩, ⟨t018_s36_g.prog t018_s36_block t018_s36_nkb, t018_s36_g.spec (α := α), 89⟩, ⟨t018_s37_g.prog t018_s37_block t018_s37_nkb, t018_s37_g.spec (α := α), 90⟩]

theorem t018_imp {α : Type} [ExactScalar α] :
    ∀ st ∈ t018_chain α, Implements st.prog st.spec :=
  List.forall_mem_cons.mpr ⟨t018_s0_impl,
  List.forall_mem_cons.mpr ⟨t018_s1_impl,
  List.forall_mem_cons.mpr ⟨t018_s2_impl,
  List.forall_mem_cons.mpr ⟨t018_s3_impl,
  List.forall_mem_cons.mpr ⟨t018_s4_impl,
  List.forall_mem_cons.mpr ⟨t018_s5_impl,
  List.forall_mem_cons.mpr ⟨t018_s6_impl,
  List.forall_mem_cons.mpr ⟨t018_s7_impl,
  List.forall_mem_cons.mpr ⟨t018_s8_impl,
  List.forall_mem_cons.mpr ⟨t018_s9_impl,
  List.forall_mem_cons.mpr ⟨t018_s10_impl,
  List.forall_mem_cons.mpr ⟨t018_s11_impl,
  List.forall_mem_cons.mpr ⟨t018_s12_impl,
  List.forall_mem_cons.mpr ⟨t018_s13_impl,
  List.forall_mem_cons.mpr ⟨t018_s14_impl,
  List.forall_mem_cons.mpr ⟨t018_s15_impl,
  List.forall_mem_cons.mpr ⟨t018_s16_impl,
  List.forall_mem_cons.mpr ⟨t018_s17_impl,
  List.forall_mem_cons.mpr ⟨t018_s18_impl,
  List.forall_mem_cons.mpr ⟨t018_s19_impl,
  List.forall_mem_cons.mpr ⟨t018_s20_impl,
  List.forall_mem_cons.mpr ⟨t018_s21_impl,
  List.forall_mem_cons.mpr ⟨t018_s22_impl,
  List.forall_mem_cons.mpr ⟨t018_s23_impl,
  List.forall_mem_cons.mpr ⟨t018_s24_impl,
  List.forall_mem_cons.mpr ⟨t018_s25_impl,
  List.forall_mem_cons.mpr ⟨t018_s26_impl,
  List.forall_mem_cons.mpr ⟨t018_s27_impl,
  List.forall_mem_cons.mpr ⟨t018_s28_impl,
  List.forall_mem_cons.mpr ⟨t018_s29_impl,
  List.forall_mem_cons.mpr ⟨t018_s30_impl,
  List.forall_mem_cons.mpr ⟨t018_s31_impl,
  List.forall_mem_cons.mpr ⟨t018_s32_impl,
  List.forall_mem_cons.mpr ⟨t018_s33_impl,
  List.forall_mem_cons.mpr ⟨t018_s34_impl,
  List.forall_mem_cons.mpr ⟨t018_s35_impl,
  List.forall_mem_cons.mpr ⟨t018_s36_impl,
  List.forall_mem_cons.mpr ⟨t018_s37_impl,
  List.forall_mem_nil _⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩

theorem t018_szok {α : Type} [ExactScalar α] :
    ∀ st ∈ t018_chain α, t018_sz st.out = some st.spec.outSize :=
  List.forall_mem_cons.mpr ⟨rfl,
  List.forall_mem_cons.mpr ⟨rfl,
  List.forall_mem_cons.mpr ⟨rfl,
  List.forall_mem_cons.mpr ⟨rfl,
  List.forall_mem_cons.mpr ⟨rfl,
  List.forall_mem_cons.mpr ⟨rfl,
  List.forall_mem_cons.mpr ⟨rfl,
  List.forall_mem_cons.mpr ⟨rfl,
  List.forall_mem_cons.mpr ⟨rfl,
  List.forall_mem_cons.mpr ⟨rfl,
  List.forall_mem_cons.mpr ⟨rfl,
  List.forall_mem_cons.mpr ⟨rfl,
  List.forall_mem_cons.mpr ⟨rfl,
  List.forall_mem_cons.mpr ⟨rfl,
  List.forall_mem_cons.mpr ⟨rfl,
  List.forall_mem_cons.mpr ⟨rfl,
  List.forall_mem_cons.mpr ⟨rfl,
  List.forall_mem_cons.mpr ⟨rfl,
  List.forall_mem_cons.mpr ⟨rfl,
  List.forall_mem_cons.mpr ⟨rfl,
  List.forall_mem_cons.mpr ⟨rfl,
  List.forall_mem_cons.mpr ⟨rfl,
  List.forall_mem_cons.mpr ⟨rfl,
  List.forall_mem_cons.mpr ⟨rfl,
  List.forall_mem_cons.mpr ⟨rfl,
  List.forall_mem_cons.mpr ⟨rfl,
  List.forall_mem_cons.mpr ⟨rfl,
  List.forall_mem_cons.mpr ⟨rfl,
  List.forall_mem_cons.mpr ⟨rfl,
  List.forall_mem_cons.mpr ⟨rfl,
  List.forall_mem_cons.mpr ⟨rfl,
  List.forall_mem_cons.mpr ⟨rfl,
  List.forall_mem_cons.mpr ⟨rfl,
  List.forall_mem_cons.mpr ⟨rfl,
  List.forall_mem_cons.mpr ⟨rfl,
  List.forall_mem_cons.mpr ⟨rfl,
  List.forall_mem_cons.mpr ⟨rfl,
  List.forall_mem_cons.mpr ⟨rfl,
  List.forall_mem_nil _⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩

theorem t018_loc {α : Type} [ExactScalar α] :
    ∀ st ∈ t018_chain α, SpecLocal t018_sz st.spec :=
  List.forall_mem_cons.mpr ⟨t018_s0_loc,
  List.forall_mem_cons.mpr ⟨t018_s1_loc,
  List.forall_mem_cons.mpr ⟨t018_s2_loc,
  List.forall_mem_cons.mpr ⟨t018_s3_loc,
  List.forall_mem_cons.mpr ⟨t018_s4_loc,
  List.forall_mem_cons.mpr ⟨t018_s5_loc,
  List.forall_mem_cons.mpr ⟨t018_s6_loc,
  List.forall_mem_cons.mpr ⟨t018_s7_loc,
  List.forall_mem_cons.mpr ⟨t018_s8_loc,
  List.forall_mem_cons.mpr ⟨t018_s9_loc,
  List.forall_mem_cons.mpr ⟨t018_s10_loc,
  List.forall_mem_cons.mpr ⟨t018_s11_loc,
  List.forall_mem_cons.mpr ⟨t018_s12_loc,
  List.forall_mem_cons.mpr ⟨t018_s13_loc,
  List.forall_mem_cons.mpr ⟨t018_s14_loc,
  List.forall_mem_cons.mpr ⟨t018_s15_loc,
  List.forall_mem_cons.mpr ⟨t018_s16_loc,
  List.forall_mem_cons.mpr ⟨t018_s17_loc,
  List.forall_mem_cons.mpr ⟨t018_s18_loc,
  List.forall_mem_cons.mpr ⟨t018_s19_loc,
  List.forall_mem_cons.mpr ⟨t018_s20_loc,
  List.forall_mem_cons.mpr ⟨t018_s21_loc,
  List.forall_mem_cons.mpr ⟨t018_s22_loc,
  List.forall_mem_cons.mpr ⟨t018_s23_loc,
  List.forall_mem_cons.mpr ⟨t018_s24_loc,
  List.forall_mem_cons.mpr ⟨t018_s25_loc,
  List.forall_mem_cons.mpr ⟨t018_s26_loc,
  List.forall_mem_cons.mpr ⟨t018_s27_loc,
  List.forall_mem_cons.mpr ⟨t018_s28_loc,
  List.forall_mem_cons.mpr ⟨t018_s29_loc,
  List.forall_mem_cons.mpr ⟨t018_s30_loc,
  List.forall_mem_cons.mpr ⟨t018_s31_loc,
  List.forall_mem_cons.mpr ⟨t018_s32_loc,
  List.forall_mem_cons.mpr ⟨t018_s33_loc,
  List.forall_mem_cons.mpr ⟨t018_s34_loc,
  List.forall_mem_cons.mpr ⟨t018_s35_loc,
  List.forall_mem_cons.mpr ⟨t018_s36_loc,
  List.forall_mem_cons.mpr ⟨t018_s37_loc,
  List.forall_mem_nil _⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩

/-- Correctness certificate for t018: the whole chain. -/
theorem t018_correct {α : Type} [ExactScalar α] :
    ∀ (f : Nat → Buf α) (m : Mem α),
      Compat (sizesAfter (t018_chain α) emptySizes)
        (runStages (t018_chain α) f m) (specStages (t018_chain α) f) :=
  fun f m => stages_correct t018_sz (t018_chain α) emptySizes f f m
    (Compat.refl _ _) (emptySizes_sub t018_sz)
    t018_szok t018_imp t018_loc

def t018_s0_kernel : ReduceKernel :=
  { name := "t018_s0", arity := 53, block := t018_s0_block, nkb := t018_s0_nkb, nout := 196635648, init := FE.zeroC, step := t018_s0_g.step t018_s0_block, stored := t018_s0_g.stored t018_s0_block }
def t018_s1_kernel : ReduceKernel :=
  { name := "t018_s1", arity := 54, block := t018_s1_block, nkb := t018_s1_nkb, nout := 48771072, init := t018_s1_g.seed, step := t018_s1_g.step t018_s1_block, stored := t018_s1_g.stored t018_s1_block }
def t018_s2_kernel : ReduceKernel :=
  { name := "t018_s2", arity := 55, block := t018_s2_block, nkb := t018_s2_nkb, nout := 8128512, init := FE.zeroC, step := t018_s2_g.step t018_s2_block, stored := t018_s2_g.stored t018_s2_block }
def t018_s3_kernel : ReduceKernel :=
  { name := "t018_s3", arity := 56, block := t018_s3_block, nkb := t018_s3_nkb, nout := 32514048, init := FE.zeroC, step := t018_s3_g.step t018_s3_block, stored := t018_s3_g.stored t018_s3_block }
def t018_s4_kernel : ReduceKernel :=
  { name := "t018_s4", arity := 57, block := t018_s4_block, nkb := t018_s4_nkb, nout := 32514048, init := FE.zeroC, step := t018_s4_g.step t018_s4_block, stored := t018_s4_g.stored t018_s4_block }
def t018_s5_kernel : ReduceKernel :=
  { name := "t018_s5", arity := 58, block := t018_s5_block, nkb := t018_s5_nkb, nout := 65028096, init := FE.zeroC, step := t018_s5_g.step t018_s5_block, stored := t018_s5_g.stored t018_s5_block }
def t018_s6_kernel : ReduceKernel :=
  { name := "t018_s6", arity := 59, block := t018_s6_block, nkb := t018_s6_nkb, nout := 8128512, init := FE.zeroC, step := t018_s6_g.step t018_s6_block, stored := t018_s6_g.stored t018_s6_block }
def t018_s7_kernel : ReduceKernel :=
  { name := "t018_s7", arity := 60, block := t018_s7_block, nkb := t018_s7_nkb, nout := 32514048, init := FE.zeroC, step := t018_s7_g.step t018_s7_block, stored := t018_s7_g.stored t018_s7_block }
def t018_s8_kernel : ReduceKernel :=
  { name := "t018_s8", arity := 61, block := t018_s8_block, nkb := t018_s8_nkb, nout := 32514048, init := FE.zeroC, step := t018_s8_g.step t018_s8_block, stored := t018_s8_g.stored t018_s8_block }
def t018_s9_kernel : ReduceKernel :=
  { name := "t018_s9", arity := 62, block := t018_s9_block, nkb := t018_s9_nkb, nout := 65028096, init := FE.zeroC, step := t018_s9_g.step t018_s9_block, stored := t018_s9_g.stored t018_s9_block }
def t018_s10_kernel : ReduceKernel :=
  { name := "t018_s10", arity := 63, block := t018_s10_block, nkb := t018_s10_nkb, nout := 16257024, init := FE.zeroC, step := t018_s10_g.step t018_s10_block, stored := t018_s10_g.stored t018_s10_block }
def t018_s11_kernel : ReduceKernel :=
  { name := "t018_s11", arity := 64, block := t018_s11_block, nkb := t018_s11_nkb, nout := 65028096, init := FE.zeroC, step := t018_s11_g.step t018_s11_block, stored := t018_s11_g.stored t018_s11_block }
def t018_s12_kernel : ReduceKernel :=
  { name := "t018_s12", arity := 65, block := t018_s12_block, nkb := t018_s12_nkb, nout := 65028096, init := FE.zeroC, step := t018_s12_g.step t018_s12_block, stored := t018_s12_g.stored t018_s12_block }
def t018_s13_kernel : ReduceKernel :=
  { name := "t018_s13", arity := 66, block := t018_s13_block, nkb := t018_s13_nkb, nout := 130056192, init := FE.zeroC, step := t018_s13_g.step t018_s13_block, stored := t018_s13_g.stored t018_s13_block }
def t018_s14_kernel : ReduceKernel :=
  { name := "t018_s14", arity := 67, block := t018_s14_block, nkb := t018_s14_nkb, nout := 32514048, init := t018_s14_g.seed, step := t018_s14_g.step t018_s14_block, stored := t018_s14_g.stored t018_s14_block }
def t018_s15_kernel : ReduceKernel :=
  { name := "t018_s15", arity := 68, block := t018_s15_block, nkb := t018_s15_nkb, nout := 4064256, init := FE.zeroC, step := t018_s15_g.step t018_s15_block, stored := t018_s15_g.stored t018_s15_block }
def t018_s16_kernel : ReduceKernel :=
  { name := "t018_s16", arity := 69, block := t018_s16_block, nkb := t018_s16_nkb, nout := 16257024, init := FE.zeroC, step := t018_s16_g.step t018_s16_block, stored := t018_s16_g.stored t018_s16_block }
def t018_s17_kernel : ReduceKernel :=
  { name := "t018_s17", arity := 70, block := t018_s17_block, nkb := t018_s17_nkb, nout := 16257024, init := FE.zeroC, step := t018_s17_g.step t018_s17_block, stored := t018_s17_g.stored t018_s17_block }
def t018_s18_kernel : ReduceKernel :=
  { name := "t018_s18", arity := 71, block := t018_s18_block, nkb := t018_s18_nkb, nout := 32514048, init := FE.zeroC, step := t018_s18_g.step t018_s18_block, stored := t018_s18_g.stored t018_s18_block }
def t018_s19_kernel : ReduceKernel :=
  { name := "t018_s19", arity := 72, block := t018_s19_block, nkb := t018_s19_nkb, nout := 6096384, init := FE.zeroC, step := t018_s19_g.step t018_s19_block, stored := t018_s19_g.stored t018_s19_block }
def t018_s20_kernel : ReduceKernel :=
  { name := "t018_s20", arity := 73, block := t018_s20_block, nkb := t018_s20_nkb, nout := 24385536, init := FE.zeroC, step := t018_s20_g.step t018_s20_block, stored := t018_s20_g.stored t018_s20_block }
def t018_s21_kernel : ReduceKernel :=
  { name := "t018_s21", arity := 74, block := t018_s21_block, nkb := t018_s21_nkb, nout := 24385536, init := FE.zeroC, step := t018_s21_g.step t018_s21_block, stored := t018_s21_g.stored t018_s21_block }
def t018_s22_kernel : ReduceKernel :=
  { name := "t018_s22", arity := 75, block := t018_s22_block, nkb := t018_s22_nkb, nout := 48771072, init := FE.zeroC, step := t018_s22_g.step t018_s22_block, stored := t018_s22_g.stored t018_s22_block }
def t018_s23_kernel : ReduceKernel :=
  { name := "t018_s23", arity := 76, block := t018_s23_block, nkb := t018_s23_nkb, nout := 6096384, init := FE.zeroC, step := t018_s23_g.step t018_s23_block, stored := t018_s23_g.stored t018_s23_block }
def t018_s24_kernel : ReduceKernel :=
  { name := "t018_s24", arity := 77, block := t018_s24_block, nkb := t018_s24_nkb, nout := 24385536, init := FE.zeroC, step := t018_s24_g.step t018_s24_block, stored := t018_s24_g.stored t018_s24_block }
def t018_s25_kernel : ReduceKernel :=
  { name := "t018_s25", arity := 78, block := t018_s25_block, nkb := t018_s25_nkb, nout := 24385536, init := FE.zeroC, step := t018_s25_g.step t018_s25_block, stored := t018_s25_g.stored t018_s25_block }
def t018_s26_kernel : ReduceKernel :=
  { name := "t018_s26", arity := 79, block := t018_s26_block, nkb := t018_s26_nkb, nout := 48771072, init := FE.zeroC, step := t018_s26_g.step t018_s26_block, stored := t018_s26_g.stored t018_s26_block }
def t018_s27_kernel : ReduceKernel :=
  { name := "t018_s27", arity := 80, block := t018_s27_block, nkb := t018_s27_nkb, nout := 8128512, init := FE.zeroC, step := t018_s27_g.step t018_s27_block, stored := t018_s27_g.stored t018_s27_block }
def t018_s28_kernel : ReduceKernel :=
  { name := "t018_s28", arity := 81, block := t018_s28_block, nkb := t018_s28_nkb, nout := 32514048, init := FE.zeroC, step := t018_s28_g.step t018_s28_block, stored := t018_s28_g.stored t018_s28_block }
def t018_s29_kernel : ReduceKernel :=
  { name := "t018_s29", arity := 82, block := t018_s29_block, nkb := t018_s29_nkb, nout := 32514048, init := FE.zeroC, step := t018_s29_g.step t018_s29_block, stored := t018_s29_g.stored t018_s29_block }
def t018_s30_kernel : ReduceKernel :=
  { name := "t018_s30", arity := 83, block := t018_s30_block, nkb := t018_s30_nkb, nout := 65028096, init := FE.zeroC, step := t018_s30_g.step t018_s30_block, stored := t018_s30_g.stored t018_s30_block }
def t018_s31_kernel : ReduceKernel :=
  { name := "t018_s31", arity := 84, block := t018_s31_block, nkb := t018_s31_nkb, nout := 15745024, init := t018_s31_g.seed, step := t018_s31_g.step t018_s31_block, stored := t018_s31_g.stored t018_s31_block }
def t018_s32_kernel : ReduceKernel :=
  { name := "t018_s32", arity := 85, block := t018_s32_block, nkb := t018_s32_nkb, nout := 1968128, init := FE.zeroC, step := t018_s32_g.step t018_s32_block, stored := t018_s32_g.stored t018_s32_block }
def t018_s33_kernel : ReduceKernel :=
  { name := "t018_s33", arity := 86, block := t018_s33_block, nkb := t018_s33_nkb, nout := 7872512, init := FE.zeroC, step := t018_s33_g.step t018_s33_block, stored := t018_s33_g.stored t018_s33_block }
def t018_s34_kernel : ReduceKernel :=
  { name := "t018_s34", arity := 87, block := t018_s34_block, nkb := t018_s34_nkb, nout := 7872512, init := FE.zeroC, step := t018_s34_g.step t018_s34_block, stored := t018_s34_g.stored t018_s34_block }
def t018_s35_kernel : ReduceKernel :=
  { name := "t018_s35", arity := 88, block := t018_s35_block, nkb := t018_s35_nkb, nout := 15745024, init := FE.zeroC, step := t018_s35_g.step t018_s35_block, stored := t018_s35_g.stored t018_s35_block }
def t018_s36_kernel : ReduceKernel :=
  { name := "t018_s36", arity := 89, block := t018_s36_block, nkb := t018_s36_nkb, nout := 30752000, init := FE.zeroC, step := t018_s36_g.step t018_s36_block, stored := t018_s36_g.stored t018_s36_block }
def t018_s37_kernel : ReduceKernel :=
  { name := "t018_s37", arity := 90, block := t018_s37_block, nkb := t018_s37_nkb, nout := 32000, init := FE.zeroC, step := t018_s37_g.step t018_s37_block, stored := t018_s37_g.stored t018_s37_block }
def t018_kernel : ChainKernel :=
  { name := "t018", arity := 53, sizes := [196635648, 48771072, 8128512, 32514048, 32514048, 65028096, 8128512, 32514048, 32514048, 65028096, 16257024, 65028096, 65028096, 130056192, 32514048, 4064256, 16257024, 16257024, 32514048, 6096384, 24385536, 24385536, 48771072, 6096384, 24385536, 24385536, 48771072, 8128512, 32514048, 32514048, 65028096, 15745024, 1968128, 7872512, 7872512, 15745024, 30752000, 32000],
    stages := [t018_s0_kernel, t018_s1_kernel, t018_s2_kernel, t018_s3_kernel, t018_s4_kernel, t018_s5_kernel, t018_s6_kernel, t018_s7_kernel, t018_s8_kernel, t018_s9_kernel, t018_s10_kernel, t018_s11_kernel, t018_s12_kernel, t018_s13_kernel, t018_s14_kernel, t018_s15_kernel, t018_s16_kernel, t018_s17_kernel, t018_s18_kernel, t018_s19_kernel, t018_s20_kernel, t018_s21_kernel, t018_s22_kernel, t018_s23_kernel, t018_s24_kernel, t018_s25_kernel, t018_s26_kernel, t018_s27_kernel, t018_s28_kernel, t018_s29_kernel, t018_s30_kernel, t018_s31_kernel, t018_s32_kernel, t018_s33_kernel, t018_s34_kernel, t018_s35_kernel, t018_s36_kernel, t018_s37_kernel] }

def main : IO Unit := do
  IO.FS.writeFile "../generated/t017.py" t017_kernel.render
  IO.FS.writeFile "../generated/t018.py" t018_kernel.render
