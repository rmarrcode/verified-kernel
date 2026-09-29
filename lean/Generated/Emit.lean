/-
  GENERATED FILE -- do not edit.

  Written by verified_kernel.vk.compile. Each task below carries a
  `theorem` instantiating its family's correctness theorem at the exact
  numbers the generator chose. `lake build` checking this file is what
  makes the corresponding kernel in generated/ a verified kernel.
-/
import VerifiedKernel

open VerifiedKernel

-- t007: reducing family, 2 inputs, 268435456 outputs, reduced extent 64
--   contraction: batch=1 M=8192 K=64 N=32768
def t007_g : GenRed :=
  { nout := 268435456, K := 64
  , offs := fun b => ([(IE.add (IE.mul (IE.add (IE.mul (IE.lit 0) (IE.lit 8192)) (IE.modi (IE.divi (IE.pid 0) (IE.lit 32768)) (IE.lit 8192))) (IE.lit 64)) IE.rk), (IE.add (IE.mul (IE.add (IE.mul (IE.lit 0) (IE.lit 64)) IE.rk) (IE.lit 32768)) (IE.modi (IE.pid 0) (IE.lit 32768)))]).getD b (IE.lit 0)
  , inRange := BE.tt
  , body := (SE.bin .mul (SE.inp 0) (SE.inp 1))
  , postOffs := fun b => ([(IE.lit 0), (IE.lit 0)]).getD b (IE.lit 0)
  , post := (SE.inp 0)
  , outGuard := BE.tt
  , nInp := 2 }
def t007_block : Nat := 64
def t007_nkb : Nat := 1

/-- Index maps mention only the output and reduction indices. -/
theorem t007_wf : t007_g.Wf :=
  { offs_ok := IE.qkOnly_getD _ (by decide)
  , post_ok := IE.qkOnly_getD _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

/-- Correctness certificate for t007. -/
theorem t007_correct {α : Type} [ExactScalar α] :
    Implements (t007_g.prog t007_block t007_nkb) (t007_g.spec (α := α)) :=
  GenRed.prog_implements t007_g t007_block t007_nkb t007_wf (by decide) (by decide)

def t007_kernel : ReduceKernel :=
  { name := "t007", arity := 2, block := t007_block
  , nkb := t007_nkb, nout := 268435456
  , init := FE.zeroC
  , step := t007_g.step t007_block
  , stored := t007_g.stored t007_block }

-- t009: reducing family, 2 inputs, 268435456 outputs, reduced extent 32
--   contraction: batch=1 M=8192 K=32 N=32768
def t009_g : GenRed :=
  { nout := 268435456, K := 32
  , offs := fun b => ([(IE.add (IE.mul (IE.add (IE.mul (IE.lit 0) (IE.lit 8192)) (IE.modi (IE.divi (IE.pid 0) (IE.lit 32768)) (IE.lit 8192))) (IE.lit 32)) IE.rk), (IE.add (IE.mul (IE.add (IE.mul (IE.lit 0) (IE.lit 32)) IE.rk) (IE.lit 32768)) (IE.modi (IE.pid 0) (IE.lit 32768)))]).getD b (IE.lit 0)
  , inRange := BE.tt
  , body := (SE.bin .mul (SE.inp 0) (SE.inp 1))
  , postOffs := fun b => ([(IE.lit 0), (IE.lit 0)]).getD b (IE.lit 0)
  , post := (SE.inp 0)
  , outGuard := BE.tt
  , nInp := 2 }
def t009_block : Nat := 32
def t009_nkb : Nat := 1

/-- Index maps mention only the output and reduction indices. -/
theorem t009_wf : t009_g.Wf :=
  { offs_ok := IE.qkOnly_getD _ (by decide)
  , post_ok := IE.qkOnly_getD _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

/-- Correctness certificate for t009. -/
theorem t009_correct {α : Type} [ExactScalar α] :
    Implements (t009_g.prog t009_block t009_nkb) (t009_g.spec (α := α)) :=
  GenRed.prog_implements t009_g t009_block t009_nkb t009_wf (by decide) (by decide)

def t009_kernel : ReduceKernel :=
  { name := "t009", arity := 2, block := t009_block
  , nkb := t009_nkb, nout := 268435456
  , init := FE.zeroC
  , step := t009_g.step t009_block
  , stored := t009_g.stored t009_block }

-- t019: pointwise, arity 1, 201326592 outputs
def t019_se : SE := (SE.bin .max (SE.inp 0) (SE.lit false 0 1))
def t019_block : Nat := 1024
def t019_n : Nat := 201326592
def t019_nblocks : Nat := 196608
def t019_kernel : FlatKernel :=
  { name := "t019", arity := 1, block := t019_block
  , n := t019_n, nblocks := t019_nblocks
  , val := SE.toFE t019_block t019_n t019_se }

/-- Correctness certificate for t019. -/
theorem t019_correct {α : Type} [ExactScalar α] :
    Implements (Prog.flat1d t019_nblocks t019_block t019_n
                 (SE.toFE t019_block t019_n t019_se))
               (SE.spec (α := α) t019_se 1 t019_n) :=
  SE.flat_correct 1 t019_se (by decide) (by decide)

-- t020: pointwise, arity 1, 201326592 outputs
def t020_se : SE := (SE.selLe (SE.inp 0) (SE.lit false 0 1) (SE.bin .mul (SE.lit false 1 100) (SE.inp 0)) (SE.inp 0))
def t020_block : Nat := 1024
def t020_n : Nat := 201326592
def t020_nblocks : Nat := 196608
def t020_kernel : FlatKernel :=
  { name := "t020", arity := 1, block := t020_block
  , n := t020_n, nblocks := t020_nblocks
  , val := SE.toFE t020_block t020_n t020_se }

/-- Correctness certificate for t020. -/
theorem t020_correct {α : Type} [ExactScalar α] :
    Implements (Prog.flat1d t020_nblocks t020_block t020_n
                 (SE.toFE t020_block t020_n t020_se))
               (SE.spec (α := α) t020_se 1 t020_n) :=
  SE.flat_correct 1 t020_se (by decide) (by decide)

-- t021: pointwise, arity 1, 201326592 outputs
def t021_se : SE := (SE.recip (SE.bin .add (SE.lit false 1 1) (SE.un .exp (SE.bin .sub (SE.lit false 0 1) (SE.inp 0)))))
def t021_block : Nat := 1024
def t021_n : Nat := 201326592
def t021_nblocks : Nat := 196608
def t021_kernel : FlatKernel :=
  { name := "t021", arity := 1, block := t021_block
  , n := t021_n, nblocks := t021_nblocks
  , val := SE.toFE t021_block t021_n t021_se }

/-- Correctness certificate for t021. -/
theorem t021_correct {α : Type} [ExactScalar α] :
    Implements (Prog.flat1d t021_nblocks t021_block t021_n
                 (SE.toFE t021_block t021_n t021_se))
               (SE.spec (α := α) t021_se 1 t021_n) :=
  SE.flat_correct 1 t021_se (by decide) (by decide)

-- t022: pointwise, arity 1, 201326592 outputs
def t022_se : SE := (SE.un .tanh (SE.inp 0))
def t022_block : Nat := 1024
def t022_n : Nat := 201326592
def t022_nblocks : Nat := 196608
def t022_kernel : FlatKernel :=
  { name := "t022", arity := 1, block := t022_block
  , n := t022_n, nblocks := t022_nblocks
  , val := SE.toFE t022_block t022_n t022_se }

/-- Correctness certificate for t022. -/
theorem t022_correct {α : Type} [ExactScalar α] :
    Implements (Prog.flat1d t022_nblocks t022_block t022_n
                 (SE.toFE t022_block t022_n t022_se))
               (SE.spec (α := α) t022_se 1 t022_n) :=
  SE.flat_correct 1 t022_se (by decide) (by decide)

-- t023: two-stage pipeline, 1 input(s), 512-element intermediate at buffer 1
--   row normalisation over dim 1 of (512, 393216): outer=512 K=393216 inner=1, intermediate 512
def t023_s1_g : GenRed :=
  { nout := 512, K := 393216
  , offs := fun b => ([(IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 1)) (IE.lit 393216)) IE.rk) (IE.lit 1)) (IE.modi (IE.pid 0) (IE.lit 1)))]).getD b (IE.lit 0)
  , inRange := BE.tt
  , body := (SE.un .exp (SE.inp 0))
  , postOffs := fun b => ([(IE.lit 0)]).getD b (IE.lit 0)
  , post := (SE.inp 0)
  , outGuard := BE.tt
  , nInp := 1 }
def t023_s1_block : Nat := 1024
def t023_s1_nkb : Nat := 384

theorem t023_s1_wf : t023_s1_g.Wf :=
  { offs_ok := IE.qkOnly_getD _ (by decide)
  , post_ok := IE.qkOnly_getD _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

theorem t023_s1_impl {α : Type} [ExactScalar α] :
    Implements (t023_s1_g.prog t023_s1_block t023_s1_nkb) (t023_s1_g.spec (α := α)) :=
  GenRed.prog_implements t023_s1_g t023_s1_block t023_s1_nkb t023_s1_wf (by decide) (by decide)

def t023_s2_g : GenRed :=
  { nout := 201326592, K := 1
  , offs := fun b => ([(IE.pid 0), (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.mul (IE.lit 393216) (IE.lit 1))) (IE.lit 1)) (IE.modi (IE.pid 0) (IE.lit 1)))]).getD b (IE.lit 0)
  , inRange := BE.tt
  , body := (SE.bin .mul (SE.un .exp (SE.inp 0)) (SE.recip (SE.inp 1)))
  , postOffs := fun b => ([(IE.lit 0), (IE.lit 0)]).getD b (IE.lit 0)
  , post := (SE.inp 0)
  , outGuard := BE.tt
  , nInp := 2 }
def t023_s2_block : Nat := 1
def t023_s2_nkb : Nat := 1

theorem t023_s2_wf : t023_s2_g.Wf :=
  { offs_ok := IE.qkOnly_getD _ (by decide)
  , post_ok := IE.qkOnly_getD _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

theorem t023_s2_impl {α : Type} [ExactScalar α] :
    Implements (t023_s2_g.prog t023_s2_block t023_s2_nkb) (t023_s2_g.spec (α := α)) :=
  GenRed.prog_implements t023_s2_g t023_s2_block t023_s2_nkb t023_s2_wf (by decide) (by decide)

/-- Stage 2 reads the intermediate only where stage 1 wrote it. -/
theorem t023_loc {α : Type} [ExactScalar α] :
    ∀ (bufs : Nat → Buf α) (u v : Buf α),
      (∀ i, i < (t023_s1_g.spec (α := α)).outSize → u i = v i) →
      ∀ q, q < (t023_s2_g.spec (α := α)).outSize →
        (t023_s2_g.spec (α := α)).out (subst bufs 1 u) q
          = (t023_s2_g.spec (α := α)).out (subst bufs 1 v) q :=
  GenRed.spec_locality t023_s2_g 1 512
    (fun q _ hq _ => bound_row (outer := 512) (K := 393216)
      (inner := 1) (by decide) hq)
    (fun _ _ => (by decide : (0 : Nat) < 512))

/-- Correctness certificate for t023: the composed pipeline. -/
theorem t023_correct {α : Type} [ExactScalar α] :
    ∀ (bufs : Nat → Buf α) (m1 m2 : Mem α) (q : Nat),
      q < (t023_s2_g.spec (α := α)).outSize →
      runTwo (t023_s1_g.prog t023_s1_block t023_s1_nkb)
             (t023_s2_g.prog t023_s2_block t023_s2_nkb) 1 bufs m1 m2 q
        = (t023_s2_g.spec (α := α)).out
            (subst bufs 1 (fun i => (t023_s1_g.spec (α := α)).out bufs i)) q :=
  two_stage t023_s1_impl t023_s2_impl t023_loc

def t023_s1_kernel : ReduceKernel :=
  { name := "t023_s1", arity := 1, block := t023_s1_block, nkb := t023_s1_nkb, nout := 512, init := FE.zeroC, step := t023_s1_g.step t023_s1_block, stored := t023_s1_g.stored t023_s1_block }
def t023_s2_kernel : ReduceKernel :=
  { name := "t023_s2", arity := 2, block := t023_s2_block, nkb := t023_s2_nkb, nout := 201326592, init := FE.zeroC, step := t023_s2_g.step t023_s2_block, stored := t023_s2_g.stored t023_s2_block }
def t023_kernel : PipelineKernel :=
  { name := "t023", arity := 1, n1 := 512, stage1 := t023_s1_kernel, stage2 := t023_s2_kernel }

-- t024: two-stage pipeline, 1 input(s), 512-element intermediate at buffer 1
--   row normalisation over dim 1 of (512, 393216): outer=512 K=393216 inner=1, intermediate 512
def t024_s1_g : GenRed :=
  { nout := 512, K := 393216
  , offs := fun b => ([(IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 1)) (IE.lit 393216)) IE.rk) (IE.lit 1)) (IE.modi (IE.pid 0) (IE.lit 1)))]).getD b (IE.lit 0)
  , inRange := BE.tt
  , body := (SE.un .exp (SE.inp 0))
  , postOffs := fun b => ([(IE.lit 0)]).getD b (IE.lit 0)
  , post := (SE.inp 0)
  , outGuard := BE.tt
  , nInp := 1 }
def t024_s1_block : Nat := 1024
def t024_s1_nkb : Nat := 384

theorem t024_s1_wf : t024_s1_g.Wf :=
  { offs_ok := IE.qkOnly_getD _ (by decide)
  , post_ok := IE.qkOnly_getD _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

theorem t024_s1_impl {α : Type} [ExactScalar α] :
    Implements (t024_s1_g.prog t024_s1_block t024_s1_nkb) (t024_s1_g.spec (α := α)) :=
  GenRed.prog_implements t024_s1_g t024_s1_block t024_s1_nkb t024_s1_wf (by decide) (by decide)

def t024_s2_g : GenRed :=
  { nout := 201326592, K := 1
  , offs := fun b => ([(IE.pid 0), (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.mul (IE.lit 393216) (IE.lit 1))) (IE.lit 1)) (IE.modi (IE.pid 0) (IE.lit 1)))]).getD b (IE.lit 0)
  , inRange := BE.tt
  , body := (SE.bin .sub (SE.inp 0) (SE.un .log (SE.inp 1)))
  , postOffs := fun b => ([(IE.lit 0), (IE.lit 0)]).getD b (IE.lit 0)
  , post := (SE.inp 0)
  , outGuard := BE.tt
  , nInp := 2 }
def t024_s2_block : Nat := 1
def t024_s2_nkb : Nat := 1

theorem t024_s2_wf : t024_s2_g.Wf :=
  { offs_ok := IE.qkOnly_getD _ (by decide)
  , post_ok := IE.qkOnly_getD _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

theorem t024_s2_impl {α : Type} [ExactScalar α] :
    Implements (t024_s2_g.prog t024_s2_block t024_s2_nkb) (t024_s2_g.spec (α := α)) :=
  GenRed.prog_implements t024_s2_g t024_s2_block t024_s2_nkb t024_s2_wf (by decide) (by decide)

/-- Stage 2 reads the intermediate only where stage 1 wrote it. -/
theorem t024_loc {α : Type} [ExactScalar α] :
    ∀ (bufs : Nat → Buf α) (u v : Buf α),
      (∀ i, i < (t024_s1_g.spec (α := α)).outSize → u i = v i) →
      ∀ q, q < (t024_s2_g.spec (α := α)).outSize →
        (t024_s2_g.spec (α := α)).out (subst bufs 1 u) q
          = (t024_s2_g.spec (α := α)).out (subst bufs 1 v) q :=
  GenRed.spec_locality t024_s2_g 1 512
    (fun q _ hq _ => bound_row (outer := 512) (K := 393216)
      (inner := 1) (by decide) hq)
    (fun _ _ => (by decide : (0 : Nat) < 512))

/-- Correctness certificate for t024: the composed pipeline. -/
theorem t024_correct {α : Type} [ExactScalar α] :
    ∀ (bufs : Nat → Buf α) (m1 m2 : Mem α) (q : Nat),
      q < (t024_s2_g.spec (α := α)).outSize →
      runTwo (t024_s1_g.prog t024_s1_block t024_s1_nkb)
             (t024_s2_g.prog t024_s2_block t024_s2_nkb) 1 bufs m1 m2 q
        = (t024_s2_g.spec (α := α)).out
            (subst bufs 1 (fun i => (t024_s1_g.spec (α := α)).out bufs i)) q :=
  two_stage t024_s1_impl t024_s2_impl t024_loc

def t024_s1_kernel : ReduceKernel :=
  { name := "t024_s1", arity := 1, block := t024_s1_block, nkb := t024_s1_nkb, nout := 512, init := FE.zeroC, step := t024_s1_g.step t024_s1_block, stored := t024_s1_g.stored t024_s1_block }
def t024_s2_kernel : ReduceKernel :=
  { name := "t024_s2", arity := 2, block := t024_s2_block, nkb := t024_s2_nkb, nout := 201326592, init := FE.zeroC, step := t024_s2_g.step t024_s2_block, stored := t024_s2_g.stored t024_s2_block }
def t024_kernel : PipelineKernel :=
  { name := "t024", arity := 1, n1 := 512, stage1 := t024_s1_kernel, stage2 := t024_s2_kernel }

-- t025: pointwise, arity 1, 201326592 outputs
def t025_se : SE := (SE.bin .mul (SE.inp 0) (SE.recip (SE.bin .add (SE.lit false 1 1) (SE.un .exp (SE.bin .sub (SE.lit false 0 1) (SE.inp 0))))))
def t025_block : Nat := 1024
def t025_n : Nat := 201326592
def t025_nblocks : Nat := 196608
def t025_kernel : FlatKernel :=
  { name := "t025", arity := 1, block := t025_block
  , n := t025_n, nblocks := t025_nblocks
  , val := SE.toFE t025_block t025_n t025_se }

/-- Correctness certificate for t025. -/
theorem t025_correct {α : Type} [ExactScalar α] :
    Implements (Prog.flat1d t025_nblocks t025_block t025_n
                 (SE.toFE t025_block t025_n t025_se))
               (SE.spec (α := α) t025_se 1 t025_n) :=
  SE.flat_correct 1 t025_se (by decide) (by decide)

-- t026: pointwise, arity 1, 201326592 outputs
def t026_se : SE := (SE.bin .mul (SE.bin .mul (SE.lit false 1 2) (SE.inp 0)) (SE.bin .add (SE.lit false 1 1) (SE.un .erf (SE.bin .mul (SE.inp 0) (SE.recip (SE.un .sqrt (SE.lit false 2 1)))))))
def t026_block : Nat := 1024
def t026_n : Nat := 201326592
def t026_nblocks : Nat := 196608
def t026_kernel : FlatKernel :=
  { name := "t026", arity := 1, block := t026_block
  , n := t026_n, nblocks := t026_nblocks
  , val := SE.toFE t026_block t026_n t026_se }

/-- Correctness certificate for t026. -/
theorem t026_correct {α : Type} [ExactScalar α] :
    Implements (Prog.flat1d t026_nblocks t026_block t026_n
                 (SE.toFE t026_block t026_n t026_se))
               (SE.spec (α := α) t026_se 1 t026_n) :=
  SE.flat_correct 1 t026_se (by decide) (by decide)

-- t027: pointwise, arity 1, 201326592 outputs
def t027_se : SE := (SE.bin .mul (SE.lit false 955375017913994 909273931795369) (SE.selLe (SE.inp 0) (SE.lit false 0 1) (SE.bin .mul (SE.lit false 1432529283788243 856129058194449) (SE.bin .sub (SE.un .exp (SE.inp 0)) (SE.lit false 1 1))) (SE.inp 0)))
def t027_block : Nat := 1024
def t027_n : Nat := 201326592
def t027_nblocks : Nat := 196608
def t027_kernel : FlatKernel :=
  { name := "t027", arity := 1, block := t027_block
  , n := t027_n, nblocks := t027_nblocks
  , val := SE.toFE t027_block t027_n t027_se }

/-- Correctness certificate for t027. -/
theorem t027_correct {α : Type} [ExactScalar α] :
    Implements (Prog.flat1d t027_nblocks t027_block t027_n
                 (SE.toFE t027_block t027_n t027_se))
               (SE.spec (α := α) t027_se 1 t027_n) :=
  SE.flat_correct 1 t027_se (by decide) (by decide)

-- t028: pointwise, arity 1, 201326592 outputs
def t028_se : SE := (SE.bin .min (SE.bin .max (SE.bin .add (SE.bin .div (SE.inp 0) (SE.lit false 6 1)) (SE.lit false 1 2)) (SE.lit false 0 1)) (SE.lit false 1 1))
def t028_block : Nat := 1024
def t028_n : Nat := 201326592
def t028_nblocks : Nat := 196608
def t028_kernel : FlatKernel :=
  { name := "t028", arity := 1, block := t028_block
  , n := t028_n, nblocks := t028_nblocks
  , val := SE.toFE t028_block t028_n t028_se }

/-- Correctness certificate for t028. -/
theorem t028_correct {α : Type} [ExactScalar α] :
    Implements (Prog.flat1d t028_nblocks t028_block t028_n
                 (SE.toFE t028_block t028_n t028_se))
               (SE.spec (α := α) t028_se 1 t028_n) :=
  SE.flat_correct 1 t028_se (by decide) (by decide)

-- t029: pointwise, arity 1, 201326592 outputs
def t029_se : SE := (SE.un .log (SE.bin .add (SE.lit false 1 1) (SE.un .exp (SE.inp 0))))
def t029_block : Nat := 1024
def t029_n : Nat := 201326592
def t029_nblocks : Nat := 196608
def t029_kernel : FlatKernel :=
  { name := "t029", arity := 1, block := t029_block
  , n := t029_n, nblocks := t029_nblocks
  , val := SE.toFE t029_block t029_n t029_se }

/-- Correctness certificate for t029. -/
theorem t029_correct {α : Type} [ExactScalar α] :
    Implements (Prog.flat1d t029_nblocks t029_block t029_n
                 (SE.toFE t029_block t029_n t029_se))
               (SE.spec (α := α) t029_se 1 t029_n) :=
  SE.flat_correct 1 t029_se (by decide) (by decide)

-- t030: pointwise, arity 1, 201326592 outputs
def t030_se : SE := (SE.bin .div (SE.inp 0) (SE.bin .add (SE.lit false 1 1) (SE.un .abs (SE.inp 0))))
def t030_block : Nat := 1024
def t030_n : Nat := 201326592
def t030_nblocks : Nat := 196608
def t030_kernel : FlatKernel :=
  { name := "t030", arity := 1, block := t030_block
  , n := t030_n, nblocks := t030_nblocks
  , val := SE.toFE t030_block t030_n t030_se }

/-- Correctness certificate for t030. -/
theorem t030_correct {α : Type} [ExactScalar α] :
    Implements (Prog.flat1d t030_nblocks t030_block t030_n
                 (SE.toFE t030_block t030_n t030_se))
               (SE.spec (α := α) t030_se 1 t030_n) :=
  SE.flat_correct 1 t030_se (by decide) (by decide)

-- t031: pointwise, arity 1, 201326592 outputs
def t031_se : SE := (SE.selLe (SE.inp 0) (SE.lit false 0 1) (SE.bin .mul (SE.lit false 1 1) (SE.bin .sub (SE.un .exp (SE.inp 0)) (SE.lit false 1 1))) (SE.inp 0))
def t031_block : Nat := 1024
def t031_n : Nat := 201326592
def t031_nblocks : Nat := 196608
def t031_kernel : FlatKernel :=
  { name := "t031", arity := 1, block := t031_block
  , n := t031_n, nblocks := t031_nblocks
  , val := SE.toFE t031_block t031_n t031_se }

/-- Correctness certificate for t031. -/
theorem t031_correct {α : Type} [ExactScalar α] :
    Implements (Prog.flat1d t031_nblocks t031_block t031_n
                 (SE.toFE t031_block t031_n t031_se))
               (SE.spec (α := α) t031_se 1 t031_n) :=
  SE.flat_correct 1 t031_se (by decide) (by decide)

-- t032: pointwise, arity 1, 201326592 outputs
def t032_se : SE := (SE.bin .min (SE.bin .max (SE.inp 0) (SE.lit true 1 1)) (SE.lit false 1 1))
def t032_block : Nat := 1024
def t032_n : Nat := 201326592
def t032_nblocks : Nat := 196608
def t032_kernel : FlatKernel :=
  { name := "t032", arity := 1, block := t032_block
  , n := t032_n, nblocks := t032_nblocks
  , val := SE.toFE t032_block t032_n t032_se }

/-- Correctness certificate for t032. -/
theorem t032_correct {α : Type} [ExactScalar α] :
    Implements (Prog.flat1d t032_nblocks t032_block t032_n
                 (SE.toFE t032_block t032_n t032_se))
               (SE.spec (α := α) t032_se 1 t032_n) :=
  SE.flat_correct 1 t032_se (by decide) (by decide)

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

-- t063: reducing family, 2 inputs, 267387904 outputs, reduced extent 144
--   conv2d: N=2 Cin=16 Cout=128 groups=1 k=(3, 3) stride=(1, 1) pad=(0, 0) dil=(1, 1) K=144
def t063_g : GenRed :=
  { nout := 267387904, K := 144
  , offs := fun b => ([(IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 133693952)) (IE.lit 16)) (IE.add (IE.mul (IE.divi (IE.modi (IE.divi (IE.pid 0) (IE.lit 1044484)) (IE.lit 128)) (IE.lit 128)) (IE.lit 16)) (IE.divi IE.rk (IE.lit 9)))) (IE.lit 1024)) (IE.sub (IE.add (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 1022)) (IE.lit 1022)) (IE.lit 1)) (IE.mul (IE.modi (IE.divi IE.rk (IE.lit 3)) (IE.lit 3)) (IE.lit 1))) (IE.lit 0))) (IE.lit 1024)) (IE.sub (IE.add (IE.mul (IE.modi (IE.pid 0) (IE.lit 1022)) (IE.lit 1)) (IE.mul (IE.modi IE.rk (IE.lit 3)) (IE.lit 1))) (IE.lit 0))), (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 1044484)) (IE.lit 128)) (IE.lit 16)) (IE.divi IE.rk (IE.lit 9))) (IE.lit 3)) (IE.modi (IE.divi IE.rk (IE.lit 3)) (IE.lit 3))) (IE.lit 3)) (IE.modi IE.rk (IE.lit 3)))]).getD b (IE.lit 0)
  , inRange := (BE.and (BE.and (BE.and (BE.cmp .le (IE.lit 0) (IE.add (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 1022)) (IE.lit 1022)) (IE.lit 1)) (IE.mul (IE.modi (IE.divi IE.rk (IE.lit 3)) (IE.lit 3)) (IE.lit 1)))) (BE.cmp .lt (IE.add (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 1022)) (IE.lit 1022)) (IE.lit 1)) (IE.mul (IE.modi (IE.divi IE.rk (IE.lit 3)) (IE.lit 3)) (IE.lit 1))) (IE.lit 1024))) (BE.cmp .le (IE.lit 0) (IE.add (IE.mul (IE.modi (IE.pid 0) (IE.lit 1022)) (IE.lit 1)) (IE.mul (IE.modi IE.rk (IE.lit 3)) (IE.lit 1))))) (BE.cmp .lt (IE.add (IE.mul (IE.modi (IE.pid 0) (IE.lit 1022)) (IE.lit 1)) (IE.mul (IE.modi IE.rk (IE.lit 3)) (IE.lit 1))) (IE.lit 1024)))
  , body := (SE.bin .mul (SE.inp 0) (SE.inp 1))
  , postOffs := fun b => ([(IE.lit 0), (IE.lit 0)]).getD b (IE.lit 0)
  , post := (SE.inp 0)
  , outGuard := BE.tt
  , nInp := 2 }
def t063_block : Nat := 128
def t063_nkb : Nat := 2

/-- Index maps mention only the output and reduction indices. -/
theorem t063_wf : t063_g.Wf :=
  { offs_ok := IE.qkOnly_getD _ (by decide)
  , post_ok := IE.qkOnly_getD _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

/-- Correctness certificate for t063. -/
theorem t063_correct {α : Type} [ExactScalar α] :
    Implements (t063_g.prog t063_block t063_nkb) (t063_g.spec (α := α)) :=
  GenRed.prog_implements t063_g t063_block t063_nkb t063_wf (by decide) (by decide)

def t063_kernel : ReduceKernel :=
  { name := "t063", arity := 2, block := t063_block
  , nkb := t063_nkb, nout := 267387904
  , init := FE.zeroC
  , step := t063_g.step t063_block
  , stored := t063_g.stored t063_block }

def main : IO Unit := do
  IO.FS.writeFile "../generated/t007.py" t007_kernel.render
  IO.FS.writeFile "../generated/t009.py" t009_kernel.render
  IO.FS.writeFile "../generated/t019.py" t019_kernel.render
  IO.FS.writeFile "../generated/t020.py" t020_kernel.render
  IO.FS.writeFile "../generated/t021.py" t021_kernel.render
  IO.FS.writeFile "../generated/t022.py" t022_kernel.render
  IO.FS.writeFile "../generated/t023.py" t023_kernel.render
  IO.FS.writeFile "../generated/t024.py" t024_kernel.render
  IO.FS.writeFile "../generated/t025.py" t025_kernel.render
  IO.FS.writeFile "../generated/t026.py" t026_kernel.render
  IO.FS.writeFile "../generated/t027.py" t027_kernel.render
  IO.FS.writeFile "../generated/t028.py" t028_kernel.render
  IO.FS.writeFile "../generated/t029.py" t029_kernel.render
  IO.FS.writeFile "../generated/t030.py" t030_kernel.render
  IO.FS.writeFile "../generated/t031.py" t031_kernel.render
  IO.FS.writeFile "../generated/t032.py" t032_kernel.render
  IO.FS.writeFile "../generated/t041.py" t041_kernel.render
  IO.FS.writeFile "../generated/t063.py" t063_kernel.render
