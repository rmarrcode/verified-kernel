/-
  GENERATED FILE -- do not edit.

  Written by verified_kernel.vk.compile. Each task below carries a
  `theorem` instantiating its family's correctness theorem at the exact
  numbers the generator chose. `lake build` checking this file is what
  makes the corresponding kernel in generated/ a verified kernel.
-/
import VerifiedKernel

open VerifiedKernel

-- t001: reducing family, 2 inputs, 16777216 outputs, reduced extent 4096
--   contraction: batch=1 M=4096 K=4096 N=4096
def t001_g : GenRed :=
  { nout := 16777216, K := 4096
  , offs := fun b => ([(IE.add (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 4096)) (IE.lit 4096)) (IE.lit 4096)) IE.rk), (IE.add (IE.mul IE.rk (IE.lit 4096)) (IE.modi (IE.pid 0) (IE.lit 4096)))]).getD b (IE.lit 0)
  , inRange := BE.tt
  , body := (SE.bin .mul (SE.inp 0) (SE.inp 1))
  , postOffs := fun b => ([(IE.lit 0), (IE.lit 0)]).getD b (IE.lit 0)
  , post := (SE.inp 0)
  , outGuard := BE.tt
  , nInp := 2 }
def t001_block : Nat := 1024
def t001_nkb : Nat := 4

/-- Index maps mention only the output and reduction indices. -/
theorem t001_wf : t001_g.Wf :=
  { offs_ok := IE.qkOnly_getD _ (by decide)
  , post_ok := IE.qkOnly_getD _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

/-- Correctness certificate for t001. -/
theorem t001_correct {α : Type} [ExactScalar α] :
    Implements (t001_g.prog t001_block t001_nkb) (t001_g.spec (α := α)) :=
  GenRed.prog_implements t001_g t001_block t001_nkb t001_wf (by decide) (by decide)

def t001_kernel : ReduceKernel :=
  { name := "t001", arity := 2, block := t001_block
  , nkb := t001_nkb, nout := 16777216
  , init := FE.zeroC
  , step := t001_g.step t001_block
  , stored := t001_g.stored t001_block }

-- t002: reducing family, 2 inputs, 8388608 outputs, reduced extent 8192
--   contraction: batch=1 M=2048 K=8192 N=4096
def t002_g : GenRed :=
  { nout := 8388608, K := 8192
  , offs := fun b => ([(IE.add (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 4096)) (IE.lit 2048)) (IE.lit 8192)) IE.rk), (IE.add (IE.mul IE.rk (IE.lit 4096)) (IE.modi (IE.pid 0) (IE.lit 4096)))]).getD b (IE.lit 0)
  , inRange := BE.tt
  , body := (SE.bin .mul (SE.inp 0) (SE.inp 1))
  , postOffs := fun b => ([(IE.lit 0), (IE.lit 0)]).getD b (IE.lit 0)
  , post := (SE.inp 0)
  , outGuard := BE.tt
  , nInp := 2 }
def t002_block : Nat := 1024
def t002_nkb : Nat := 8

/-- Index maps mention only the output and reduction indices. -/
theorem t002_wf : t002_g.Wf :=
  { offs_ok := IE.qkOnly_getD _ (by decide)
  , post_ok := IE.qkOnly_getD _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

/-- Correctness certificate for t002. -/
theorem t002_correct {α : Type} [ExactScalar α] :
    Implements (t002_g.prog t002_block t002_nkb) (t002_g.spec (α := α)) :=
  GenRed.prog_implements t002_g t002_block t002_nkb t002_wf (by decide) (by decide)

def t002_kernel : ReduceKernel :=
  { name := "t002", arity := 2, block := t002_block
  , nkb := t002_nkb, nout := 8388608
  , init := FE.zeroC
  , step := t002_g.step t002_block
  , stored := t002_g.stored t002_block }

-- t003: reducing family, 2 inputs, 134217728 outputs, reduced extent 1024
--   contraction: batch=128 M=512 K=1024 N=2048
def t003_g : GenRed :=
  { nout := 134217728, K := 1024
  , offs := fun b => ([(IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 1048576)) (IE.lit 512)) (IE.modi (IE.divi (IE.pid 0) (IE.lit 2048)) (IE.lit 512))) (IE.lit 1024)) IE.rk), (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 1048576)) (IE.lit 1024)) IE.rk) (IE.lit 2048)) (IE.modi (IE.pid 0) (IE.lit 2048)))]).getD b (IE.lit 0)
  , inRange := BE.tt
  , body := (SE.bin .mul (SE.inp 0) (SE.inp 1))
  , postOffs := fun b => ([(IE.lit 0), (IE.lit 0)]).getD b (IE.lit 0)
  , post := (SE.inp 0)
  , outGuard := BE.tt
  , nInp := 2 }
def t003_block : Nat := 1024
def t003_nkb : Nat := 1

/-- Index maps mention only the output and reduction indices. -/
theorem t003_wf : t003_g.Wf :=
  { offs_ok := IE.qkOnly_getD _ (by decide)
  , post_ok := IE.qkOnly_getD _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

/-- Correctness certificate for t003. -/
theorem t003_correct {α : Type} [ExactScalar α] :
    Implements (t003_g.prog t003_block t003_nkb) (t003_g.spec (α := α)) :=
  GenRed.prog_implements t003_g t003_block t003_nkb t003_wf (by decide) (by decide)

def t003_kernel : ReduceKernel :=
  { name := "t003", arity := 2, block := t003_block
  , nkb := t003_nkb, nout := 134217728
  , init := FE.zeroC
  , step := t003_g.step t003_block
  , stored := t003_g.stored t003_block }

-- t004: reducing family, 2 inputs, 1024 outputs, reduced extent 1048576
--   contraction: batch=1 M=1024 K=1048576 N=1
def t004_g : GenRed :=
  { nout := 1024, K := 1048576
  , offs := fun b => ([(IE.add (IE.mul (IE.modi (IE.pid 0) (IE.lit 1024)) (IE.lit 1048576)) IE.rk), IE.rk]).getD b (IE.lit 0)
  , inRange := BE.tt
  , body := (SE.bin .mul (SE.inp 0) (SE.inp 1))
  , postOffs := fun b => ([(IE.lit 0), (IE.lit 0)]).getD b (IE.lit 0)
  , post := (SE.inp 0)
  , outGuard := BE.tt
  , nInp := 2 }
def t004_block : Nat := 1024
def t004_nkb : Nat := 1024

/-- Index maps mention only the output and reduction indices. -/
theorem t004_wf : t004_g.Wf :=
  { offs_ok := IE.qkOnly_getD _ (by decide)
  , post_ok := IE.qkOnly_getD _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

/-- Correctness certificate for t004. -/
theorem t004_correct {α : Type} [ExactScalar α] :
    Implements (t004_g.prog t004_block t004_nkb) (t004_g.spec (α := α)) :=
  GenRed.prog_implements t004_g t004_block t004_nkb t004_wf (by decide) (by decide)

def t004_kernel : ReduceKernel :=
  { name := "t004", arity := 2, block := t004_block
  , nkb := t004_nkb, nout := 1024
  , init := FE.zeroC
  , step := t004_g.step t004_block
  , stored := t004_g.stored t004_block }

-- t005: pointwise, arity 1, 268435456 outputs
def t005_se : SE := (SE.bin .mul (SE.inp 0) (SE.lit false 157 50))
def t005_block : Nat := 1024
def t005_n : Nat := 268435456
def t005_nblocks : Nat := 262144
def t005_kernel : FlatKernel :=
  { name := "t005", arity := 1, block := t005_block
  , n := t005_n, nblocks := t005_nblocks
  , val := SE.toFE t005_block t005_n t005_se }

/-- Correctness certificate for t005. -/
theorem t005_correct {α : Type} [ExactScalar α] :
    Implements (Prog.flat1d t005_nblocks t005_block t005_n
                 (SE.toFE t005_block t005_n t005_se))
               (SE.spec (α := α) t005_se 1 t005_n) :=
  SE.flat_correct 1 t005_se (by decide) (by decide)

-- t006: reducing family, 2 inputs, 65536 outputs, reduced extent 524288
--   contraction: batch=1 M=256 K=524288 N=256
def t006_g : GenRed :=
  { nout := 65536, K := 524288
  , offs := fun b => ([(IE.add (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 256)) (IE.lit 256)) (IE.lit 524288)) IE.rk), (IE.add (IE.mul IE.rk (IE.lit 256)) (IE.modi (IE.pid 0) (IE.lit 256)))]).getD b (IE.lit 0)
  , inRange := BE.tt
  , body := (SE.bin .mul (SE.inp 0) (SE.inp 1))
  , postOffs := fun b => ([(IE.lit 0), (IE.lit 0)]).getD b (IE.lit 0)
  , post := (SE.inp 0)
  , outGuard := BE.tt
  , nInp := 2 }
def t006_block : Nat := 1024
def t006_nkb : Nat := 512

/-- Index maps mention only the output and reduction indices. -/
theorem t006_wf : t006_g.Wf :=
  { offs_ok := IE.qkOnly_getD _ (by decide)
  , post_ok := IE.qkOnly_getD _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

/-- Correctness certificate for t006. -/
theorem t006_correct {α : Type} [ExactScalar α] :
    Implements (t006_g.prog t006_block t006_nkb) (t006_g.spec (α := α)) :=
  GenRed.prog_implements t006_g t006_block t006_nkb t006_wf (by decide) (by decide)

def t006_kernel : ReduceKernel :=
  { name := "t006", arity := 2, block := t006_block
  , nkb := t006_nkb, nout := 65536
  , init := FE.zeroC
  , step := t006_g.step t006_block
  , stored := t006_g.stored t006_block }

-- t007: reducing family, 2 inputs, 536870912 outputs, reduced extent 64
--   contraction: batch=1 M=16384 K=64 N=32768
def t007_g : GenRed :=
  { nout := 536870912, K := 64
  , offs := fun b => ([(IE.add (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 32768)) (IE.lit 16384)) (IE.lit 64)) IE.rk), (IE.add (IE.mul IE.rk (IE.lit 32768)) (IE.modi (IE.pid 0) (IE.lit 32768)))]).getD b (IE.lit 0)
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
  , nkb := t007_nkb, nout := 536870912
  , init := FE.zeroC
  , step := t007_g.step t007_block
  , stored := t007_g.stored t007_block }

-- t008: reducing family, 2 inputs, 48581805 outputs, reduced extent 2949
--   contraction: batch=1 M=8205 K=2949 N=5921
def t008_g : GenRed :=
  { nout := 48581805, K := 2949
  , offs := fun b => ([(IE.add (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 5921)) (IE.lit 8205)) (IE.lit 2949)) IE.rk), (IE.add (IE.mul IE.rk (IE.lit 5921)) (IE.modi (IE.pid 0) (IE.lit 5921)))]).getD b (IE.lit 0)
  , inRange := BE.tt
  , body := (SE.bin .mul (SE.inp 0) (SE.inp 1))
  , postOffs := fun b => ([(IE.lit 0), (IE.lit 0)]).getD b (IE.lit 0)
  , post := (SE.inp 0)
  , outGuard := BE.tt
  , nInp := 2 }
def t008_block : Nat := 1024
def t008_nkb : Nat := 3

/-- Index maps mention only the output and reduction indices. -/
theorem t008_wf : t008_g.Wf :=
  { offs_ok := IE.qkOnly_getD _ (by decide)
  , post_ok := IE.qkOnly_getD _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

/-- Correctness certificate for t008. -/
theorem t008_correct {α : Type} [ExactScalar α] :
    Implements (t008_g.prog t008_block t008_nkb) (t008_g.spec (α := α)) :=
  GenRed.prog_implements t008_g t008_block t008_nkb t008_wf (by decide) (by decide)

def t008_kernel : ReduceKernel :=
  { name := "t008", arity := 2, block := t008_block
  , nkb := t008_nkb, nout := 48581805
  , init := FE.zeroC
  , step := t008_g.step t008_block
  , stored := t008_g.stored t008_block }

-- t009: reducing family, 2 inputs, 536870912 outputs, reduced extent 32
--   contraction: batch=1 M=16384 K=32 N=32768
def t009_g : GenRed :=
  { nout := 536870912, K := 32
  , offs := fun b => ([(IE.add (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 32768)) (IE.lit 16384)) (IE.lit 32)) IE.rk), (IE.add (IE.mul IE.rk (IE.lit 32768)) (IE.modi (IE.pid 0) (IE.lit 32768)))]).getD b (IE.lit 0)
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
  , nkb := t009_nkb, nout := 536870912
  , init := FE.zeroC
  , step := t009_g.step t009_block
  , stored := t009_g.stored t009_block }

-- t010: reducing family, 2 inputs, 12582912 outputs, reduced extent 2048
--   contraction: batch=16 M=1024 K=2048 N=768
def t010_g : GenRed :=
  { nout := 12582912, K := 2048
  , offs := fun b => ([(IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 786432)) (IE.lit 1024)) (IE.modi (IE.divi (IE.pid 0) (IE.lit 768)) (IE.lit 1024))) (IE.lit 2048)) IE.rk), (IE.add (IE.mul IE.rk (IE.lit 768)) (IE.modi (IE.pid 0) (IE.lit 768)))]).getD b (IE.lit 0)
  , inRange := BE.tt
  , body := (SE.bin .mul (SE.inp 0) (SE.inp 1))
  , postOffs := fun b => ([(IE.lit 0), (IE.lit 0)]).getD b (IE.lit 0)
  , post := (SE.inp 0)
  , outGuard := BE.tt
  , nInp := 2 }
def t010_block : Nat := 1024
def t010_nkb : Nat := 2

/-- Index maps mention only the output and reduction indices. -/
theorem t010_wf : t010_g.Wf :=
  { offs_ok := IE.qkOnly_getD _ (by decide)
  , post_ok := IE.qkOnly_getD _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

/-- Correctness certificate for t010. -/
theorem t010_correct {α : Type} [ExactScalar α] :
    Implements (t010_g.prog t010_block t010_nkb) (t010_g.spec (α := α)) :=
  GenRed.prog_implements t010_g t010_block t010_nkb t010_wf (by decide) (by decide)

def t010_kernel : ReduceKernel :=
  { name := "t010", arity := 2, block := t010_block
  , nkb := t010_nkb, nout := 12582912
  , init := FE.zeroC
  , step := t010_g.step t010_block
  , stored := t010_g.stored t010_block }

-- t011: reducing family, 2 inputs, 402653184 outputs, reduced extent 256
--   contraction: batch=1024 M=512 K=256 N=768
def t011_g : GenRed :=
  { nout := 402653184, K := 256
  , offs := fun b => ([(IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 393216)) (IE.lit 512)) (IE.modi (IE.divi (IE.pid 0) (IE.lit 768)) (IE.lit 512))) (IE.lit 256)) IE.rk), (IE.add (IE.mul IE.rk (IE.lit 768)) (IE.modi (IE.pid 0) (IE.lit 768)))]).getD b (IE.lit 0)
  , inRange := BE.tt
  , body := (SE.bin .mul (SE.inp 0) (SE.inp 1))
  , postOffs := fun b => ([(IE.lit 0), (IE.lit 0)]).getD b (IE.lit 0)
  , post := (SE.inp 0)
  , outGuard := BE.tt
  , nInp := 2 }
def t011_block : Nat := 256
def t011_nkb : Nat := 1

/-- Index maps mention only the output and reduction indices. -/
theorem t011_wf : t011_g.Wf :=
  { offs_ok := IE.qkOnly_getD _ (by decide)
  , post_ok := IE.qkOnly_getD _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

/-- Correctness certificate for t011. -/
theorem t011_correct {α : Type} [ExactScalar α] :
    Implements (t011_g.prog t011_block t011_nkb) (t011_g.spec (α := α)) :=
  GenRed.prog_implements t011_g t011_block t011_nkb t011_wf (by decide) (by decide)

def t011_kernel : ReduceKernel :=
  { name := "t011", arity := 2, block := t011_block
  , nkb := t011_nkb, nout := 402653184
  , init := FE.zeroC
  , step := t011_g.step t011_block
  , stored := t011_g.stored t011_block }

-- t012: reducing family, 2 inputs, 16777216 outputs, reduced extent 1
--   broadcast map: [(4096, 1), (4096, 4096)] -> (4096, 4096)
def t012_g : GenRed :=
  { nout := 16777216, K := 1
  , offs := fun b => ([(IE.divi (IE.pid 0) (IE.lit 4096)), (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 4096)) (IE.lit 4096)) (IE.modi (IE.pid 0) (IE.lit 4096)))]).getD b (IE.lit 0)
  , inRange := BE.tt
  , body := (SE.bin .mul (SE.inp 0) (SE.inp 1))
  , postOffs := fun b => ([(IE.lit 0), (IE.lit 0)]).getD b (IE.lit 0)
  , post := (SE.inp 0)
  , outGuard := BE.tt
  , nInp := 2 }
def t012_block : Nat := 1
def t012_nkb : Nat := 1

/-- Index maps mention only the output and reduction indices. -/
theorem t012_wf : t012_g.Wf :=
  { offs_ok := IE.qkOnly_getD _ (by decide)
  , post_ok := IE.qkOnly_getD _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

/-- Correctness certificate for t012. -/
theorem t012_correct {α : Type} [ExactScalar α] :
    Implements (t012_g.prog t012_block t012_nkb) (t012_g.spec (α := α)) :=
  GenRed.prog_implements t012_g t012_block t012_nkb t012_wf (by decide) (by decide)

def t012_kernel : ReduceKernel :=
  { name := "t012", arity := 2, block := t012_block
  , nkb := t012_nkb, nout := 16777216
  , init := FE.zeroC
  , step := t012_g.step t012_block
  , stored := t012_g.stored t012_block }

-- t013: reducing family, 2 inputs, 16777216 outputs, reduced extent 4096
--   contraction: batch=1 M=4096 K=4096 N=4096
def t013_g : GenRed :=
  { nout := 16777216, K := 4096
  , offs := fun b => ([(IE.add (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 4096)) (IE.lit 4096)) (IE.lit 4096)) IE.rk), (IE.add (IE.mul IE.rk (IE.lit 4096)) (IE.modi (IE.pid 0) (IE.lit 4096)))]).getD b (IE.lit 0)
  , inRange := BE.tt
  , body := (SE.bin .mul (SE.inp 0) (SE.inp 1))
  , postOffs := fun b => ([(IE.lit 0), (IE.lit 0)]).getD b (IE.lit 0)
  , post := (SE.inp 0)
  , outGuard := BE.tt
  , nInp := 2 }
def t013_block : Nat := 1024
def t013_nkb : Nat := 4

/-- Index maps mention only the output and reduction indices. -/
theorem t013_wf : t013_g.Wf :=
  { offs_ok := IE.qkOnly_getD _ (by decide)
  , post_ok := IE.qkOnly_getD _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

/-- Correctness certificate for t013. -/
theorem t013_correct {α : Type} [ExactScalar α] :
    Implements (t013_g.prog t013_block t013_nkb) (t013_g.spec (α := α)) :=
  GenRed.prog_implements t013_g t013_block t013_nkb t013_wf (by decide) (by decide)

def t013_kernel : ReduceKernel :=
  { name := "t013", arity := 2, block := t013_block
  , nkb := t013_nkb, nout := 16777216
  , init := FE.zeroC
  , step := t013_g.step t013_block
  , stored := t013_g.stored t013_block }

-- t014: reducing family, 2 inputs, 16777216 outputs, reduced extent 4096
--   contraction: batch=1 M=4096 K=4096 N=4096, triu mask
def t014_g : GenRed :=
  { nout := 16777216, K := 4096
  , offs := fun b => ([(IE.add (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 4096)) (IE.lit 4096)) (IE.lit 4096)) IE.rk), (IE.add (IE.mul IE.rk (IE.lit 4096)) (IE.modi (IE.pid 0) (IE.lit 4096)))]).getD b (IE.lit 0)
  , inRange := BE.tt
  , body := (SE.bin .mul (SE.inp 0) (SE.inp 1))
  , postOffs := fun b => ([(IE.lit 0), (IE.lit 0)]).getD b (IE.lit 0)
  , post := (SE.inp 0)
  , outGuard := (BE.cmp .le (IE.modi (IE.divi (IE.pid 0) (IE.lit 4096)) (IE.lit 4096)) (IE.modi (IE.pid 0) (IE.lit 4096)))
  , nInp := 2 }
def t014_block : Nat := 1024
def t014_nkb : Nat := 4

/-- Index maps mention only the output and reduction indices. -/
theorem t014_wf : t014_g.Wf :=
  { offs_ok := IE.qkOnly_getD _ (by decide)
  , post_ok := IE.qkOnly_getD _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

/-- Correctness certificate for t014. -/
theorem t014_correct {α : Type} [ExactScalar α] :
    Implements (t014_g.prog t014_block t014_nkb) (t014_g.spec (α := α)) :=
  GenRed.prog_implements t014_g t014_block t014_nkb t014_wf (by decide) (by decide)

def t014_kernel : ReduceKernel :=
  { name := "t014", arity := 2, block := t014_block
  , nkb := t014_nkb, nout := 16777216
  , init := FE.zeroC
  , step := t014_g.step t014_block
  , stored := t014_g.stored t014_block }

-- t015: reducing family, 2 inputs, 16777216 outputs, reduced extent 4096
--   contraction: batch=1 M=4096 K=4096 N=4096, tril mask
def t015_g : GenRed :=
  { nout := 16777216, K := 4096
  , offs := fun b => ([(IE.add (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 4096)) (IE.lit 4096)) (IE.lit 4096)) IE.rk), (IE.add (IE.mul IE.rk (IE.lit 4096)) (IE.modi (IE.pid 0) (IE.lit 4096)))]).getD b (IE.lit 0)
  , inRange := BE.tt
  , body := (SE.bin .mul (SE.inp 0) (SE.inp 1))
  , postOffs := fun b => ([(IE.lit 0), (IE.lit 0)]).getD b (IE.lit 0)
  , post := (SE.inp 0)
  , outGuard := (BE.cmp .le (IE.modi (IE.pid 0) (IE.lit 4096)) (IE.modi (IE.divi (IE.pid 0) (IE.lit 4096)) (IE.lit 4096)))
  , nInp := 2 }
def t015_block : Nat := 1024
def t015_nkb : Nat := 4

/-- Index maps mention only the output and reduction indices. -/
theorem t015_wf : t015_g.Wf :=
  { offs_ok := IE.qkOnly_getD _ (by decide)
  , post_ok := IE.qkOnly_getD _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

/-- Correctness certificate for t015. -/
theorem t015_correct {α : Type} [ExactScalar α] :
    Implements (t015_g.prog t015_block t015_nkb) (t015_g.spec (α := α)) :=
  GenRed.prog_implements t015_g t015_block t015_nkb t015_wf (by decide) (by decide)

def t015_kernel : ReduceKernel :=
  { name := "t015", arity := 2, block := t015_block
  , nkb := t015_nkb, nout := 16777216
  , init := FE.zeroC
  , step := t015_g.step t015_block
  , stored := t015_g.stored t015_block }

-- t016: reducing family, 2 inputs, 8388608 outputs, reduced extent 8192
--   contraction: batch=1 M=2048 K=8192 N=4096, lhs^T
def t016_g : GenRed :=
  { nout := 8388608, K := 8192
  , offs := fun b => ([(IE.add (IE.mul IE.rk (IE.lit 2048)) (IE.modi (IE.divi (IE.pid 0) (IE.lit 4096)) (IE.lit 2048))), (IE.add (IE.mul IE.rk (IE.lit 4096)) (IE.modi (IE.pid 0) (IE.lit 4096)))]).getD b (IE.lit 0)
  , inRange := BE.tt
  , body := (SE.bin .mul (SE.inp 0) (SE.inp 1))
  , postOffs := fun b => ([(IE.lit 0), (IE.lit 0)]).getD b (IE.lit 0)
  , post := (SE.inp 0)
  , outGuard := BE.tt
  , nInp := 2 }
def t016_block : Nat := 1024
def t016_nkb : Nat := 8

/-- Index maps mention only the output and reduction indices. -/
theorem t016_wf : t016_g.Wf :=
  { offs_ok := IE.qkOnly_getD _ (by decide)
  , post_ok := IE.qkOnly_getD _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

/-- Correctness certificate for t016. -/
theorem t016_correct {α : Type} [ExactScalar α] :
    Implements (t016_g.prog t016_block t016_nkb) (t016_g.spec (α := α)) :=
  GenRed.prog_implements t016_g t016_block t016_nkb t016_wf (by decide) (by decide)

def t016_kernel : ReduceKernel :=
  { name := "t016", arity := 2, block := t016_block
  , nkb := t016_nkb, nout := 8388608
  , init := FE.zeroC
  , step := t016_g.step t016_block
  , stored := t016_g.stored t016_block }

-- t017: reducing family, 2 inputs, 8388608 outputs, reduced extent 8192
--   contraction: batch=1 M=2048 K=8192 N=4096, rhs^T
def t017_g : GenRed :=
  { nout := 8388608, K := 8192
  , offs := fun b => ([(IE.add (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 4096)) (IE.lit 2048)) (IE.lit 8192)) IE.rk), (IE.add (IE.mul (IE.modi (IE.pid 0) (IE.lit 4096)) (IE.lit 8192)) IE.rk)]).getD b (IE.lit 0)
  , inRange := BE.tt
  , body := (SE.bin .mul (SE.inp 0) (SE.inp 1))
  , postOffs := fun b => ([(IE.lit 0), (IE.lit 0)]).getD b (IE.lit 0)
  , post := (SE.inp 0)
  , outGuard := BE.tt
  , nInp := 2 }
def t017_block : Nat := 1024
def t017_nkb : Nat := 8

/-- Index maps mention only the output and reduction indices. -/
theorem t017_wf : t017_g.Wf :=
  { offs_ok := IE.qkOnly_getD _ (by decide)
  , post_ok := IE.qkOnly_getD _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

/-- Correctness certificate for t017. -/
theorem t017_correct {α : Type} [ExactScalar α] :
    Implements (t017_g.prog t017_block t017_nkb) (t017_g.spec (α := α)) :=
  GenRed.prog_implements t017_g t017_block t017_nkb t017_wf (by decide) (by decide)

def t017_kernel : ReduceKernel :=
  { name := "t017", arity := 2, block := t017_block
  , nkb := t017_nkb, nout := 8388608
  , init := FE.zeroC
  , step := t017_g.step t017_block
  , stored := t017_g.stored t017_block }

-- t018: reducing family, 2 inputs, 8388608 outputs, reduced extent 8192
--   contraction: batch=1 M=2048 K=8192 N=4096, lhs^T, rhs^T
def t018_g : GenRed :=
  { nout := 8388608, K := 8192
  , offs := fun b => ([(IE.add (IE.mul IE.rk (IE.lit 2048)) (IE.modi (IE.divi (IE.pid 0) (IE.lit 4096)) (IE.lit 2048))), (IE.add (IE.mul (IE.modi (IE.pid 0) (IE.lit 4096)) (IE.lit 8192)) IE.rk)]).getD b (IE.lit 0)
  , inRange := BE.tt
  , body := (SE.bin .mul (SE.inp 0) (SE.inp 1))
  , postOffs := fun b => ([(IE.lit 0), (IE.lit 0)]).getD b (IE.lit 0)
  , post := (SE.inp 0)
  , outGuard := BE.tt
  , nInp := 2 }
def t018_block : Nat := 1024
def t018_nkb : Nat := 8

/-- Index maps mention only the output and reduction indices. -/
theorem t018_wf : t018_g.Wf :=
  { offs_ok := IE.qkOnly_getD _ (by decide)
  , post_ok := IE.qkOnly_getD _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

/-- Correctness certificate for t018. -/
theorem t018_correct {α : Type} [ExactScalar α] :
    Implements (t018_g.prog t018_block t018_nkb) (t018_g.spec (α := α)) :=
  GenRed.prog_implements t018_g t018_block t018_nkb t018_wf (by decide) (by decide)

def t018_kernel : ReduceKernel :=
  { name := "t018", arity := 2, block := t018_block
  , nkb := t018_nkb, nout := 8388608
  , init := FE.zeroC
  , step := t018_g.step t018_block
  , stored := t018_g.stored t018_block }

-- t019: pointwise, arity 1, 402653184 outputs
def t019_se : SE := (SE.bin .max (SE.inp 0) (SE.lit false 0 1))
def t019_block : Nat := 1024
def t019_n : Nat := 402653184
def t019_nblocks : Nat := 393216
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

-- t020: pointwise, arity 1, 402653184 outputs
def t020_se : SE := (SE.selLe (SE.inp 0) (SE.lit false 0 1) (SE.bin .mul (SE.lit false 1 100) (SE.inp 0)) (SE.inp 0))
def t020_block : Nat := 1024
def t020_n : Nat := 402653184
def t020_nblocks : Nat := 393216
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

-- t021: pointwise, arity 1, 402653184 outputs
def t021_se : SE := (SE.recip (SE.bin .add (SE.lit false 1 1) (SE.un .exp (SE.bin .sub (SE.lit false 0 1) (SE.inp 0)))))
def t021_block : Nat := 1024
def t021_n : Nat := 402653184
def t021_nblocks : Nat := 393216
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

-- t022: pointwise, arity 1, 402653184 outputs
def t022_se : SE := (SE.un .tanh (SE.inp 0))
def t022_block : Nat := 1024
def t022_n : Nat := 402653184
def t022_nblocks : Nat := 393216
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

-- t023: two-stage pipeline, 1 input(s), 1024-element intermediate at buffer 1
--   row normalisation over dim 1 of (1024, 393216): outer=1024 K=393216 inner=1, intermediate 1024
def t023_s1_g : GenRed :=
  { nout := 1024, K := 393216
  , offs := fun b => ([(IE.add (IE.mul (IE.pid 0) (IE.lit 393216)) IE.rk)]).getD b (IE.lit 0)
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
  { nout := 402653184, K := 1
  , offs := fun b => ([(IE.pid 0), (IE.divi (IE.pid 0) (IE.lit 393216))]).getD b (IE.lit 0)
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
  GenRed.spec_locality t023_s2_g 1 1024
    (fun q k hq hk => (bound_div (a := 1024) (d := 393216) hq))
    (fun _ _ => (by decide : (0 : Nat) < 1024))

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
  { name := "t023_s1", arity := 1, block := t023_s1_block, nkb := t023_s1_nkb, nout := 1024, init := FE.zeroC, step := t023_s1_g.step t023_s1_block, stored := t023_s1_g.stored t023_s1_block }
def t023_s2_kernel : ReduceKernel :=
  { name := "t023_s2", arity := 2, block := t023_s2_block, nkb := t023_s2_nkb, nout := 402653184, init := FE.zeroC, step := t023_s2_g.step t023_s2_block, stored := t023_s2_g.stored t023_s2_block }
def t023_kernel : PipelineKernel :=
  { name := "t023", arity := 1, n1 := 1024, stage1 := t023_s1_kernel, stage2 := t023_s2_kernel }

-- t024: two-stage pipeline, 1 input(s), 1024-element intermediate at buffer 1
--   row normalisation over dim 1 of (1024, 393216): outer=1024 K=393216 inner=1, intermediate 1024
def t024_s1_g : GenRed :=
  { nout := 1024, K := 393216
  , offs := fun b => ([(IE.add (IE.mul (IE.pid 0) (IE.lit 393216)) IE.rk)]).getD b (IE.lit 0)
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
  { nout := 402653184, K := 1
  , offs := fun b => ([(IE.pid 0), (IE.divi (IE.pid 0) (IE.lit 393216))]).getD b (IE.lit 0)
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
  GenRed.spec_locality t024_s2_g 1 1024
    (fun q k hq hk => (bound_div (a := 1024) (d := 393216) hq))
    (fun _ _ => (by decide : (0 : Nat) < 1024))

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
  { name := "t024_s1", arity := 1, block := t024_s1_block, nkb := t024_s1_nkb, nout := 1024, init := FE.zeroC, step := t024_s1_g.step t024_s1_block, stored := t024_s1_g.stored t024_s1_block }
def t024_s2_kernel : ReduceKernel :=
  { name := "t024_s2", arity := 2, block := t024_s2_block, nkb := t024_s2_nkb, nout := 402653184, init := FE.zeroC, step := t024_s2_g.step t024_s2_block, stored := t024_s2_g.stored t024_s2_block }
def t024_kernel : PipelineKernel :=
  { name := "t024", arity := 1, n1 := 1024, stage1 := t024_s1_kernel, stage2 := t024_s2_kernel }

-- t025: pointwise, arity 1, 402653184 outputs
def t025_se : SE := (SE.bin .mul (SE.inp 0) (SE.recip (SE.bin .add (SE.lit false 1 1) (SE.un .exp (SE.bin .sub (SE.lit false 0 1) (SE.inp 0))))))
def t025_block : Nat := 1024
def t025_n : Nat := 402653184
def t025_nblocks : Nat := 393216
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

-- t026: pointwise, arity 1, 402653184 outputs
def t026_se : SE := (SE.bin .mul (SE.bin .mul (SE.lit false 1 2) (SE.inp 0)) (SE.bin .add (SE.lit false 1 1) (SE.un .erf (SE.bin .mul (SE.inp 0) (SE.recip (SE.un .sqrt (SE.lit false 2 1)))))))
def t026_block : Nat := 1024
def t026_n : Nat := 402653184
def t026_nblocks : Nat := 393216
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

-- t027: pointwise, arity 1, 402653184 outputs
def t027_se : SE := (SE.bin .mul (SE.lit false 955375017913994 909273931795369) (SE.selLe (SE.inp 0) (SE.lit false 0 1) (SE.bin .mul (SE.lit false 1432529283788243 856129058194449) (SE.bin .sub (SE.un .exp (SE.inp 0)) (SE.lit false 1 1))) (SE.inp 0)))
def t027_block : Nat := 1024
def t027_n : Nat := 402653184
def t027_nblocks : Nat := 393216
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

-- t028: pointwise, arity 1, 402653184 outputs
def t028_se : SE := (SE.bin .min (SE.bin .max (SE.bin .add (SE.bin .div (SE.inp 0) (SE.lit false 6 1)) (SE.lit false 1 2)) (SE.lit false 0 1)) (SE.lit false 1 1))
def t028_block : Nat := 1024
def t028_n : Nat := 402653184
def t028_nblocks : Nat := 393216
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

-- t029: pointwise, arity 1, 402653184 outputs
def t029_se : SE := (SE.un .log (SE.bin .add (SE.lit false 1 1) (SE.un .exp (SE.inp 0))))
def t029_block : Nat := 1024
def t029_n : Nat := 402653184
def t029_nblocks : Nat := 393216
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

-- t030: pointwise, arity 1, 402653184 outputs
def t030_se : SE := (SE.bin .div (SE.inp 0) (SE.bin .add (SE.lit false 1 1) (SE.un .abs (SE.inp 0))))
def t030_block : Nat := 1024
def t030_n : Nat := 402653184
def t030_nblocks : Nat := 393216
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

-- t031: pointwise, arity 1, 402653184 outputs
def t031_se : SE := (SE.selLe (SE.inp 0) (SE.lit false 0 1) (SE.bin .mul (SE.lit false 1 1) (SE.bin .sub (SE.un .exp (SE.inp 0)) (SE.lit false 1 1))) (SE.inp 0))
def t031_block : Nat := 1024
def t031_n : Nat := 402653184
def t031_nblocks : Nat := 393216
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

-- t032: pointwise, arity 1, 402653184 outputs
def t032_se : SE := (SE.bin .min (SE.bin .max (SE.inp 0) (SE.lit true 1 1)) (SE.lit false 1 1))
def t032_block : Nat := 1024
def t032_n : Nat := 402653184
def t032_nblocks : Nat := 393216
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

-- t033: three-stage normalisation, 3 input buffer(s), intermediates 64 and 64 at buffers 3 and 4
--   BatchNorm2d on (16, 64, 512, 512): 64 statistics over 4194304 elements, eps=1e-05, affine
def t033_s1_g : GenRed :=
  { nout := 64, K := 4194304
  , offs := fun b => ([(IE.add (IE.mul (IE.add (IE.mul (IE.divi IE.rk (IE.lit 262144)) (IE.lit 64)) (IE.pid 0)) (IE.lit 262144)) (IE.modi IE.rk (IE.lit 262144))), (IE.lit 0), (IE.lit 0), (IE.lit 0), (IE.lit 0)]).getD b (IE.lit 0)
  , inRange := BE.tt
  , body := (SE.inp 0)
  , postOffs := fun b => ([(IE.lit 0), (IE.lit 0), (IE.lit 0), (IE.lit 0), (IE.lit 0)]).getD b (IE.lit 0)
  , post := (SE.inp 0)
  , outGuard := BE.tt
  , nInp := 1 }
def t033_s1_block : Nat := 1024
def t033_s1_nkb : Nat := 4096

theorem t033_s1_wf : t033_s1_g.Wf :=
  { offs_ok := IE.qkOnly_getD _ (by decide)
  , post_ok := IE.qkOnly_getD _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

theorem t033_s1_impl {α : Type} [ExactScalar α] :
    Implements (t033_s1_g.prog t033_s1_block t033_s1_nkb) (t033_s1_g.spec (α := α)) :=
  GenRed.prog_implements t033_s1_g t033_s1_block t033_s1_nkb t033_s1_wf (by decide) (by decide)

def t033_s2_g : GenRed :=
  { nout := 64, K := 4194304
  , offs := fun b => ([(IE.add (IE.mul (IE.add (IE.mul (IE.divi IE.rk (IE.lit 262144)) (IE.lit 64)) (IE.pid 0)) (IE.lit 262144)) (IE.modi IE.rk (IE.lit 262144))), (IE.lit 0), (IE.lit 0), (IE.pid 0), (IE.lit 0)]).getD b (IE.lit 0)
  , inRange := BE.tt
  , body := (SE.bin .mul (SE.bin .sub (SE.inp 0) (SE.bin .mul (SE.inp 3) (SE.lit false 1 4194304))) (SE.bin .sub (SE.inp 0) (SE.bin .mul (SE.inp 3) (SE.lit false 1 4194304))))
  , postOffs := fun b => ([(IE.lit 0), (IE.lit 0), (IE.lit 0), (IE.lit 0), (IE.lit 0)]).getD b (IE.lit 0)
  , post := (SE.inp 0)
  , outGuard := BE.tt
  , nInp := 4 }
def t033_s2_block : Nat := 1024
def t033_s2_nkb : Nat := 4096

theorem t033_s2_wf : t033_s2_g.Wf :=
  { offs_ok := IE.qkOnly_getD _ (by decide)
  , post_ok := IE.qkOnly_getD _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

theorem t033_s2_impl {α : Type} [ExactScalar α] :
    Implements (t033_s2_g.prog t033_s2_block t033_s2_nkb) (t033_s2_g.spec (α := α)) :=
  GenRed.prog_implements t033_s2_g t033_s2_block t033_s2_nkb t033_s2_wf (by decide) (by decide)

def t033_s3_g : GenRed :=
  { nout := 268435456, K := 1
  , offs := fun b => ([(IE.pid 0), (IE.modi (IE.divi (IE.pid 0) (IE.lit 262144)) (IE.lit 64)), (IE.modi (IE.divi (IE.pid 0) (IE.lit 262144)) (IE.lit 64)), (IE.modi (IE.divi (IE.pid 0) (IE.lit 262144)) (IE.lit 64)), (IE.modi (IE.divi (IE.pid 0) (IE.lit 262144)) (IE.lit 64))]).getD b (IE.lit 0)
  , inRange := BE.tt
  , body := (SE.bin .add (SE.bin .mul (SE.bin .mul (SE.bin .sub (SE.inp 0) (SE.bin .mul (SE.inp 3) (SE.lit false 1 4194304))) (SE.recip (SE.un .sqrt (SE.bin .add (SE.bin .mul (SE.inp 4) (SE.lit false 1 4194304)) (SE.lit false 1 100000))))) (SE.inp 1)) (SE.inp 2))
  , postOffs := fun b => ([(IE.lit 0), (IE.lit 0), (IE.lit 0), (IE.lit 0), (IE.lit 0)]).getD b (IE.lit 0)
  , post := (SE.inp 0)
  , outGuard := BE.tt
  , nInp := 5 }
def t033_s3_block : Nat := 1
def t033_s3_nkb : Nat := 1

theorem t033_s3_wf : t033_s3_g.Wf :=
  { offs_ok := IE.qkOnly_getD _ (by decide)
  , post_ok := IE.qkOnly_getD _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

theorem t033_s3_impl {α : Type} [ExactScalar α] :
    Implements (t033_s3_g.prog t033_s3_block t033_s3_nkb) (t033_s3_g.spec (α := α)) :=
  GenRed.prog_implements t033_s3_g t033_s3_block t033_s3_nkb t033_s3_wf (by decide) (by decide)

/-- Stage 2 reads the first intermediate only where stage 1 wrote it. -/
theorem t033_l2 {α : Type} [ExactScalar α] :
    Loc (t033_s2_g.spec (α := α)) 3 64 :=
  GenRed.loc t033_s2_g 3 64 (fun q _ hq _ => hq) (fun _ _ => (by decide : (0 : Nat) < 64))

/-- Stage 3 reads each intermediate only where its stage wrote it. -/
theorem t033_l3a {α : Type} [ExactScalar α] :
    Loc (t033_s3_g.spec (α := α)) 3 64 :=
  GenRed.loc t033_s3_g 3 64 (fun q k hq hk => (bound_mod (c := 64) (by decide : (0 : Nat) < 64))) (fun _ _ => (by decide : (0 : Nat) < 64))

theorem t033_l3b {α : Type} [ExactScalar α] :
    Loc (t033_s3_g.spec (α := α)) 4 64 :=
  GenRed.loc t033_s3_g 4 64 (fun q k hq hk => (bound_mod (c := 64) (by decide : (0 : Nat) < 64))) (fun _ _ => (by decide : (0 : Nat) < 64))

/-- Correctness certificate for t033: the composed three-stage pipeline. -/
theorem t033_correct {α : Type} [ExactScalar α] :
    ∀ (bufs : Nat → Buf α) (m1 m2 m3 : Mem α) (q : Nat),
      q < (t033_s3_g.spec (α := α)).outSize →
      runThree (t033_s1_g.prog t033_s1_block t033_s1_nkb)
               (t033_s2_g.prog t033_s2_block t033_s2_nkb)
               (t033_s3_g.prog t033_s3_block t033_s3_nkb) 3 4 bufs m1 m2 m3 q
        = compose3 (t033_s1_g.spec (α := α)) (t033_s2_g.spec (α := α))
            (t033_s3_g.spec (α := α)) 3 4 bufs q :=
  three_stage (by decide) t033_s1_impl t033_s2_impl t033_s3_impl t033_l2 t033_l3a t033_l3b

def t033_s1_kernel : ReduceKernel :=
  { name := "t033_s1", arity := 1, block := t033_s1_block, nkb := t033_s1_nkb, nout := 64, init := FE.zeroC, step := t033_s1_g.step t033_s1_block, stored := t033_s1_g.stored t033_s1_block }
def t033_s2_kernel : ReduceKernel :=
  { name := "t033_s2", arity := 4, block := t033_s2_block, nkb := t033_s2_nkb, nout := 64, init := FE.zeroC, step := t033_s2_g.step t033_s2_block, stored := t033_s2_g.stored t033_s2_block }
def t033_s3_kernel : ReduceKernel :=
  { name := "t033_s3", arity := 5, block := t033_s3_block, nkb := t033_s3_nkb, nout := 268435456, init := FE.zeroC, step := t033_s3_g.step t033_s3_block, stored := t033_s3_g.stored t033_s3_block }
def t033_kernel : PipelineKernel3 :=
  { name := "t033", arity := 3, n1 := 64, n2 := 64, stage1 := t033_s1_kernel, stage2 := t033_s2_kernel, stage3 := t033_s3_kernel }

-- t034: three-stage normalisation, 1 input buffer(s), intermediates 896 and 896 at buffers 1 and 2
--   InstanceNorm2d on (14, 64, 512, 512): 896 statistics over 262144 elements, eps=1e-05
def t034_s1_g : GenRed :=
  { nout := 896, K := 262144
  , offs := fun b => ([(IE.add (IE.mul (IE.pid 0) (IE.lit 262144)) IE.rk), (IE.lit 0), (IE.lit 0)]).getD b (IE.lit 0)
  , inRange := BE.tt
  , body := (SE.inp 0)
  , postOffs := fun b => ([(IE.lit 0), (IE.lit 0), (IE.lit 0)]).getD b (IE.lit 0)
  , post := (SE.inp 0)
  , outGuard := BE.tt
  , nInp := 1 }
def t034_s1_block : Nat := 1024
def t034_s1_nkb : Nat := 256

theorem t034_s1_wf : t034_s1_g.Wf :=
  { offs_ok := IE.qkOnly_getD _ (by decide)
  , post_ok := IE.qkOnly_getD _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

theorem t034_s1_impl {α : Type} [ExactScalar α] :
    Implements (t034_s1_g.prog t034_s1_block t034_s1_nkb) (t034_s1_g.spec (α := α)) :=
  GenRed.prog_implements t034_s1_g t034_s1_block t034_s1_nkb t034_s1_wf (by decide) (by decide)

def t034_s2_g : GenRed :=
  { nout := 896, K := 262144
  , offs := fun b => ([(IE.add (IE.mul (IE.pid 0) (IE.lit 262144)) IE.rk), (IE.pid 0), (IE.lit 0)]).getD b (IE.lit 0)
  , inRange := BE.tt
  , body := (SE.bin .mul (SE.bin .sub (SE.inp 0) (SE.bin .mul (SE.inp 1) (SE.lit false 1 262144))) (SE.bin .sub (SE.inp 0) (SE.bin .mul (SE.inp 1) (SE.lit false 1 262144))))
  , postOffs := fun b => ([(IE.lit 0), (IE.lit 0), (IE.lit 0)]).getD b (IE.lit 0)
  , post := (SE.inp 0)
  , outGuard := BE.tt
  , nInp := 2 }
def t034_s2_block : Nat := 1024
def t034_s2_nkb : Nat := 256

theorem t034_s2_wf : t034_s2_g.Wf :=
  { offs_ok := IE.qkOnly_getD _ (by decide)
  , post_ok := IE.qkOnly_getD _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

theorem t034_s2_impl {α : Type} [ExactScalar α] :
    Implements (t034_s2_g.prog t034_s2_block t034_s2_nkb) (t034_s2_g.spec (α := α)) :=
  GenRed.prog_implements t034_s2_g t034_s2_block t034_s2_nkb t034_s2_wf (by decide) (by decide)

def t034_s3_g : GenRed :=
  { nout := 234881024, K := 1
  , offs := fun b => ([(IE.pid 0), (IE.divi (IE.pid 0) (IE.lit 262144)), (IE.divi (IE.pid 0) (IE.lit 262144))]).getD b (IE.lit 0)
  , inRange := BE.tt
  , body := (SE.bin .mul (SE.bin .sub (SE.inp 0) (SE.bin .mul (SE.inp 1) (SE.lit false 1 262144))) (SE.recip (SE.un .sqrt (SE.bin .add (SE.bin .mul (SE.inp 2) (SE.lit false 1 262144)) (SE.lit false 1 100000)))))
  , postOffs := fun b => ([(IE.lit 0), (IE.lit 0), (IE.lit 0)]).getD b (IE.lit 0)
  , post := (SE.inp 0)
  , outGuard := BE.tt
  , nInp := 3 }
def t034_s3_block : Nat := 1
def t034_s3_nkb : Nat := 1

theorem t034_s3_wf : t034_s3_g.Wf :=
  { offs_ok := IE.qkOnly_getD _ (by decide)
  , post_ok := IE.qkOnly_getD _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

theorem t034_s3_impl {α : Type} [ExactScalar α] :
    Implements (t034_s3_g.prog t034_s3_block t034_s3_nkb) (t034_s3_g.spec (α := α)) :=
  GenRed.prog_implements t034_s3_g t034_s3_block t034_s3_nkb t034_s3_wf (by decide) (by decide)

/-- Stage 2 reads the first intermediate only where stage 1 wrote it. -/
theorem t034_l2 {α : Type} [ExactScalar α] :
    Loc (t034_s2_g.spec (α := α)) 1 896 :=
  GenRed.loc t034_s2_g 1 896 (fun q _ hq _ => hq) (fun _ _ => (by decide : (0 : Nat) < 896))

/-- Stage 3 reads each intermediate only where its stage wrote it. -/
theorem t034_l3a {α : Type} [ExactScalar α] :
    Loc (t034_s3_g.spec (α := α)) 1 896 :=
  GenRed.loc t034_s3_g 1 896 (fun q k hq hk => (bound_div (a := 896) (d := 262144) hq)) (fun _ _ => (by decide : (0 : Nat) < 896))

theorem t034_l3b {α : Type} [ExactScalar α] :
    Loc (t034_s3_g.spec (α := α)) 2 896 :=
  GenRed.loc t034_s3_g 2 896 (fun q k hq hk => (bound_div (a := 896) (d := 262144) hq)) (fun _ _ => (by decide : (0 : Nat) < 896))

/-- Correctness certificate for t034: the composed three-stage pipeline. -/
theorem t034_correct {α : Type} [ExactScalar α] :
    ∀ (bufs : Nat → Buf α) (m1 m2 m3 : Mem α) (q : Nat),
      q < (t034_s3_g.spec (α := α)).outSize →
      runThree (t034_s1_g.prog t034_s1_block t034_s1_nkb)
               (t034_s2_g.prog t034_s2_block t034_s2_nkb)
               (t034_s3_g.prog t034_s3_block t034_s3_nkb) 1 2 bufs m1 m2 m3 q
        = compose3 (t034_s1_g.spec (α := α)) (t034_s2_g.spec (α := α))
            (t034_s3_g.spec (α := α)) 1 2 bufs q :=
  three_stage (by decide) t034_s1_impl t034_s2_impl t034_s3_impl t034_l2 t034_l3a t034_l3b

def t034_s1_kernel : ReduceKernel :=
  { name := "t034_s1", arity := 1, block := t034_s1_block, nkb := t034_s1_nkb, nout := 896, init := FE.zeroC, step := t034_s1_g.step t034_s1_block, stored := t034_s1_g.stored t034_s1_block }
def t034_s2_kernel : ReduceKernel :=
  { name := "t034_s2", arity := 2, block := t034_s2_block, nkb := t034_s2_nkb, nout := 896, init := FE.zeroC, step := t034_s2_g.step t034_s2_block, stored := t034_s2_g.stored t034_s2_block }
def t034_s3_kernel : ReduceKernel :=
  { name := "t034_s3", arity := 3, block := t034_s3_block, nkb := t034_s3_nkb, nout := 234881024, init := FE.zeroC, step := t034_s3_g.step t034_s3_block, stored := t034_s3_g.stored t034_s3_block }
def t034_kernel : PipelineKernel3 :=
  { name := "t034", arity := 1, n1 := 896, n2 := 896, stage1 := t034_s1_kernel, stage2 := t034_s2_kernel, stage3 := t034_s3_kernel }

-- t035: three-stage normalisation, 3 input buffer(s), intermediates 112 and 112 at buffers 3 and 4
--   GroupNorm on (14, 64, 512, 512): 112 statistics over 2097152 elements, eps=1e-05, affine
def t035_s1_g : GenRed :=
  { nout := 112, K := 2097152
  , offs := fun b => ([(IE.add (IE.mul (IE.add (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 8)) (IE.lit 64)) (IE.mul (IE.modi (IE.pid 0) (IE.lit 8)) (IE.lit 8))) (IE.divi IE.rk (IE.lit 262144))) (IE.lit 262144)) (IE.modi IE.rk (IE.lit 262144))), (IE.lit 0), (IE.lit 0), (IE.lit 0), (IE.lit 0)]).getD b (IE.lit 0)
  , inRange := BE.tt
  , body := (SE.inp 0)
  , postOffs := fun b => ([(IE.lit 0), (IE.lit 0), (IE.lit 0), (IE.lit 0), (IE.lit 0)]).getD b (IE.lit 0)
  , post := (SE.inp 0)
  , outGuard := BE.tt
  , nInp := 1 }
def t035_s1_block : Nat := 1024
def t035_s1_nkb : Nat := 2048

theorem t035_s1_wf : t035_s1_g.Wf :=
  { offs_ok := IE.qkOnly_getD _ (by decide)
  , post_ok := IE.qkOnly_getD _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

theorem t035_s1_impl {α : Type} [ExactScalar α] :
    Implements (t035_s1_g.prog t035_s1_block t035_s1_nkb) (t035_s1_g.spec (α := α)) :=
  GenRed.prog_implements t035_s1_g t035_s1_block t035_s1_nkb t035_s1_wf (by decide) (by decide)

def t035_s2_g : GenRed :=
  { nout := 112, K := 2097152
  , offs := fun b => ([(IE.add (IE.mul (IE.add (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 8)) (IE.lit 64)) (IE.mul (IE.modi (IE.pid 0) (IE.lit 8)) (IE.lit 8))) (IE.divi IE.rk (IE.lit 262144))) (IE.lit 262144)) (IE.modi IE.rk (IE.lit 262144))), (IE.lit 0), (IE.lit 0), (IE.pid 0), (IE.lit 0)]).getD b (IE.lit 0)
  , inRange := BE.tt
  , body := (SE.bin .mul (SE.bin .sub (SE.inp 0) (SE.bin .mul (SE.inp 3) (SE.lit false 1 2097152))) (SE.bin .sub (SE.inp 0) (SE.bin .mul (SE.inp 3) (SE.lit false 1 2097152))))
  , postOffs := fun b => ([(IE.lit 0), (IE.lit 0), (IE.lit 0), (IE.lit 0), (IE.lit 0)]).getD b (IE.lit 0)
  , post := (SE.inp 0)
  , outGuard := BE.tt
  , nInp := 4 }
def t035_s2_block : Nat := 1024
def t035_s2_nkb : Nat := 2048

theorem t035_s2_wf : t035_s2_g.Wf :=
  { offs_ok := IE.qkOnly_getD _ (by decide)
  , post_ok := IE.qkOnly_getD _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

theorem t035_s2_impl {α : Type} [ExactScalar α] :
    Implements (t035_s2_g.prog t035_s2_block t035_s2_nkb) (t035_s2_g.spec (α := α)) :=
  GenRed.prog_implements t035_s2_g t035_s2_block t035_s2_nkb t035_s2_wf (by decide) (by decide)

def t035_s3_g : GenRed :=
  { nout := 234881024, K := 1
  , offs := fun b => ([(IE.pid 0), (IE.modi (IE.divi (IE.pid 0) (IE.lit 262144)) (IE.lit 64)), (IE.modi (IE.divi (IE.pid 0) (IE.lit 262144)) (IE.lit 64)), (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 16777216)) (IE.lit 8)) (IE.divi (IE.modi (IE.divi (IE.pid 0) (IE.lit 262144)) (IE.lit 64)) (IE.lit 8))), (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 16777216)) (IE.lit 8)) (IE.divi (IE.modi (IE.divi (IE.pid 0) (IE.lit 262144)) (IE.lit 64)) (IE.lit 8)))]).getD b (IE.lit 0)
  , inRange := BE.tt
  , body := (SE.bin .add (SE.bin .mul (SE.bin .mul (SE.bin .sub (SE.inp 0) (SE.bin .mul (SE.inp 3) (SE.lit false 1 2097152))) (SE.recip (SE.un .sqrt (SE.bin .add (SE.bin .mul (SE.inp 4) (SE.lit false 1 2097152)) (SE.lit false 1 100000))))) (SE.inp 1)) (SE.inp 2))
  , postOffs := fun b => ([(IE.lit 0), (IE.lit 0), (IE.lit 0), (IE.lit 0), (IE.lit 0)]).getD b (IE.lit 0)
  , post := (SE.inp 0)
  , outGuard := BE.tt
  , nInp := 5 }
def t035_s3_block : Nat := 1
def t035_s3_nkb : Nat := 1

theorem t035_s3_wf : t035_s3_g.Wf :=
  { offs_ok := IE.qkOnly_getD _ (by decide)
  , post_ok := IE.qkOnly_getD _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

theorem t035_s3_impl {α : Type} [ExactScalar α] :
    Implements (t035_s3_g.prog t035_s3_block t035_s3_nkb) (t035_s3_g.spec (α := α)) :=
  GenRed.prog_implements t035_s3_g t035_s3_block t035_s3_nkb t035_s3_wf (by decide) (by decide)

/-- Stage 2 reads the first intermediate only where stage 1 wrote it. -/
theorem t035_l2 {α : Type} [ExactScalar α] :
    Loc (t035_s2_g.spec (α := α)) 3 112 :=
  GenRed.loc t035_s2_g 3 112 (fun q _ hq _ => hq) (fun _ _ => (by decide : (0 : Nat) < 112))

/-- Stage 3 reads each intermediate only where its stage wrote it. -/
theorem t035_l3a {α : Type} [ExactScalar α] :
    Loc (t035_s3_g.spec (α := α)) 3 112 :=
  GenRed.loc t035_s3_g 3 112 (fun q k hq hk => (bound_pack (A := 14) (B := 8) (bound_div (a := 14) (d := 16777216) hq) (bound_group (C := 64) (CG := 8) (G := 8) (x := q / 262144) (by decide) (by decide) (by decide)))) (fun _ _ => (by decide : (0 : Nat) < 112))

theorem t035_l3b {α : Type} [ExactScalar α] :
    Loc (t035_s3_g.spec (α := α)) 4 112 :=
  GenRed.loc t035_s3_g 4 112 (fun q k hq hk => (bound_pack (A := 14) (B := 8) (bound_div (a := 14) (d := 16777216) hq) (bound_group (C := 64) (CG := 8) (G := 8) (x := q / 262144) (by decide) (by decide) (by decide)))) (fun _ _ => (by decide : (0 : Nat) < 112))

/-- Correctness certificate for t035: the composed three-stage pipeline. -/
theorem t035_correct {α : Type} [ExactScalar α] :
    ∀ (bufs : Nat → Buf α) (m1 m2 m3 : Mem α) (q : Nat),
      q < (t035_s3_g.spec (α := α)).outSize →
      runThree (t035_s1_g.prog t035_s1_block t035_s1_nkb)
               (t035_s2_g.prog t035_s2_block t035_s2_nkb)
               (t035_s3_g.prog t035_s3_block t035_s3_nkb) 3 4 bufs m1 m2 m3 q
        = compose3 (t035_s1_g.spec (α := α)) (t035_s2_g.spec (α := α))
            (t035_s3_g.spec (α := α)) 3 4 bufs q :=
  three_stage (by decide) t035_s1_impl t035_s2_impl t035_s3_impl t035_l2 t035_l3a t035_l3b

def t035_s1_kernel : ReduceKernel :=
  { name := "t035_s1", arity := 1, block := t035_s1_block, nkb := t035_s1_nkb, nout := 112, init := FE.zeroC, step := t035_s1_g.step t035_s1_block, stored := t035_s1_g.stored t035_s1_block }
def t035_s2_kernel : ReduceKernel :=
  { name := "t035_s2", arity := 4, block := t035_s2_block, nkb := t035_s2_nkb, nout := 112, init := FE.zeroC, step := t035_s2_g.step t035_s2_block, stored := t035_s2_g.stored t035_s2_block }
def t035_s3_kernel : ReduceKernel :=
  { name := "t035_s3", arity := 5, block := t035_s3_block, nkb := t035_s3_nkb, nout := 234881024, init := FE.zeroC, step := t035_s3_g.step t035_s3_block, stored := t035_s3_g.stored t035_s3_block }
def t035_kernel : PipelineKernel3 :=
  { name := "t035", arity := 3, n1 := 112, n2 := 112, stage1 := t035_s1_kernel, stage2 := t035_s2_kernel, stage3 := t035_s3_kernel }

-- t036: two-stage pipeline, 1 input(s), 3670016-element intermediate at buffer 1
--   row normalisation over dim 1 of (14, 64, 512, 512): outer=14 K=64 inner=262144, intermediate 3670016
def t036_s1_g : GenRed :=
  { nout := 3670016, K := 64
  , offs := fun b => ([(IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 262144)) (IE.lit 64)) IE.rk) (IE.lit 262144)) (IE.modi (IE.pid 0) (IE.lit 262144)))]).getD b (IE.lit 0)
  , inRange := BE.tt
  , body := (SE.bin .mul (SE.inp 0) (SE.inp 0))
  , postOffs := fun b => ([(IE.lit 0)]).getD b (IE.lit 0)
  , post := (SE.inp 0)
  , outGuard := BE.tt
  , nInp := 1 }
def t036_s1_block : Nat := 64
def t036_s1_nkb : Nat := 1

theorem t036_s1_wf : t036_s1_g.Wf :=
  { offs_ok := IE.qkOnly_getD _ (by decide)
  , post_ok := IE.qkOnly_getD _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

theorem t036_s1_impl {α : Type} [ExactScalar α] :
    Implements (t036_s1_g.prog t036_s1_block t036_s1_nkb) (t036_s1_g.spec (α := α)) :=
  GenRed.prog_implements t036_s1_g t036_s1_block t036_s1_nkb t036_s1_wf (by decide) (by decide)

def t036_s2_g : GenRed :=
  { nout := 234881024, K := 1
  , offs := fun b => ([(IE.pid 0), (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.mul (IE.lit 64) (IE.lit 262144))) (IE.lit 262144)) (IE.modi (IE.pid 0) (IE.lit 262144)))]).getD b (IE.lit 0)
  , inRange := BE.tt
  , body := (SE.bin .div (SE.inp 0) (SE.un .sqrt (SE.bin .add (SE.bin .mul (SE.inp 1) (SE.lit false 1 64)) (SE.lit false 1 100000))))
  , postOffs := fun b => ([(IE.lit 0), (IE.lit 0)]).getD b (IE.lit 0)
  , post := (SE.inp 0)
  , outGuard := BE.tt
  , nInp := 2 }
def t036_s2_block : Nat := 1
def t036_s2_nkb : Nat := 1

theorem t036_s2_wf : t036_s2_g.Wf :=
  { offs_ok := IE.qkOnly_getD _ (by decide)
  , post_ok := IE.qkOnly_getD _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

theorem t036_s2_impl {α : Type} [ExactScalar α] :
    Implements (t036_s2_g.prog t036_s2_block t036_s2_nkb) (t036_s2_g.spec (α := α)) :=
  GenRed.prog_implements t036_s2_g t036_s2_block t036_s2_nkb t036_s2_wf (by decide) (by decide)

/-- Stage 2 reads the intermediate only where stage 1 wrote it. -/
theorem t036_loc {α : Type} [ExactScalar α] :
    ∀ (bufs : Nat → Buf α) (u v : Buf α),
      (∀ i, i < (t036_s1_g.spec (α := α)).outSize → u i = v i) →
      ∀ q, q < (t036_s2_g.spec (α := α)).outSize →
        (t036_s2_g.spec (α := α)).out (subst bufs 1 u) q
          = (t036_s2_g.spec (α := α)).out (subst bufs 1 v) q :=
  GenRed.spec_locality t036_s2_g 1 3670016
    (fun q k hq hk => (bound_row (outer := 14) (K := 64) (inner := 262144) (by decide) hq))
    (fun _ _ => (by decide : (0 : Nat) < 3670016))

/-- Correctness certificate for t036: the composed pipeline. -/
theorem t036_correct {α : Type} [ExactScalar α] :
    ∀ (bufs : Nat → Buf α) (m1 m2 : Mem α) (q : Nat),
      q < (t036_s2_g.spec (α := α)).outSize →
      runTwo (t036_s1_g.prog t036_s1_block t036_s1_nkb)
             (t036_s2_g.prog t036_s2_block t036_s2_nkb) 1 bufs m1 m2 q
        = (t036_s2_g.spec (α := α)).out
            (subst bufs 1 (fun i => (t036_s1_g.spec (α := α)).out bufs i)) q :=
  two_stage t036_s1_impl t036_s2_impl t036_loc

def t036_s1_kernel : ReduceKernel :=
  { name := "t036_s1", arity := 1, block := t036_s1_block, nkb := t036_s1_nkb, nout := 3670016, init := FE.zeroC, step := t036_s1_g.step t036_s1_block, stored := t036_s1_g.stored t036_s1_block }
def t036_s2_kernel : ReduceKernel :=
  { name := "t036_s2", arity := 2, block := t036_s2_block, nkb := t036_s2_nkb, nout := 234881024, init := FE.zeroC, step := t036_s2_g.step t036_s2_block, stored := t036_s2_g.stored t036_s2_block }
def t036_kernel : PipelineKernel :=
  { name := "t036", arity := 1, n1 := 3670016, stage1 := t036_s1_kernel, stage2 := t036_s2_kernel }

-- t037: three-stage normalisation, 1 input buffer(s), intermediates 4096 and 1 at buffers 1 and 2
--   whole-tensor normalisation over (14, 64, 512, 512): tree reduction of 234881024 elements via 4096 partials
def t037_s1_g : GenRed :=
  { nout := 4096, K := 57344
  , offs := fun b => ([(IE.add (IE.mul (IE.pid 0) (IE.lit 57344)) IE.rk), (IE.lit 0), (IE.lit 0)]).getD b (IE.lit 0)
  , inRange := (BE.cmp .lt (IE.add (IE.mul (IE.pid 0) (IE.lit 57344)) IE.rk) (IE.lit 234881024))
  , body := (SE.bin .mul (SE.inp 0) (SE.inp 0))
  , postOffs := fun b => ([(IE.lit 0), (IE.lit 0), (IE.lit 0)]).getD b (IE.lit 0)
  , post := (SE.inp 0)
  , outGuard := BE.tt
  , nInp := 1 }
def t037_s1_block : Nat := 1024
def t037_s1_nkb : Nat := 56

theorem t037_s1_wf : t037_s1_g.Wf :=
  { offs_ok := IE.qkOnly_getD _ (by decide)
  , post_ok := IE.qkOnly_getD _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

theorem t037_s1_impl {α : Type} [ExactScalar α] :
    Implements (t037_s1_g.prog t037_s1_block t037_s1_nkb) (t037_s1_g.spec (α := α)) :=
  GenRed.prog_implements t037_s1_g t037_s1_block t037_s1_nkb t037_s1_wf (by decide) (by decide)

def t037_s2_g : GenRed :=
  { nout := 1, K := 4096
  , offs := fun b => ([(IE.lit 0), IE.rk, (IE.lit 0)]).getD b (IE.lit 0)
  , inRange := BE.tt
  , body := (SE.inp 1)
  , postOffs := fun b => ([(IE.lit 0), (IE.lit 0), (IE.lit 0)]).getD b (IE.lit 0)
  , post := (SE.inp 0)
  , outGuard := BE.tt
  , nInp := 2 }
def t037_s2_block : Nat := 1024
def t037_s2_nkb : Nat := 4

theorem t037_s2_wf : t037_s2_g.Wf :=
  { offs_ok := IE.qkOnly_getD _ (by decide)
  , post_ok := IE.qkOnly_getD _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

theorem t037_s2_impl {α : Type} [ExactScalar α] :
    Implements (t037_s2_g.prog t037_s2_block t037_s2_nkb) (t037_s2_g.spec (α := α)) :=
  GenRed.prog_implements t037_s2_g t037_s2_block t037_s2_nkb t037_s2_wf (by decide) (by decide)

def t037_s3_g : GenRed :=
  { nout := 234881024, K := 1
  , offs := fun b => ([(IE.pid 0), (IE.lit 0), (IE.lit 0)]).getD b (IE.lit 0)
  , inRange := BE.tt
  , body := (SE.bin .div (SE.inp 0) (SE.un .sqrt (SE.inp 2)))
  , postOffs := fun b => ([(IE.lit 0), (IE.lit 0), (IE.lit 0)]).getD b (IE.lit 0)
  , post := (SE.inp 0)
  , outGuard := BE.tt
  , nInp := 3 }
def t037_s3_block : Nat := 1
def t037_s3_nkb : Nat := 1

theorem t037_s3_wf : t037_s3_g.Wf :=
  { offs_ok := IE.qkOnly_getD _ (by decide)
  , post_ok := IE.qkOnly_getD _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

theorem t037_s3_impl {α : Type} [ExactScalar α] :
    Implements (t037_s3_g.prog t037_s3_block t037_s3_nkb) (t037_s3_g.spec (α := α)) :=
  GenRed.prog_implements t037_s3_g t037_s3_block t037_s3_nkb t037_s3_wf (by decide) (by decide)

/-- Stage 2 reads the first intermediate only where stage 1 wrote it. -/
theorem t037_l2 {α : Type} [ExactScalar α] :
    Loc (t037_s2_g.spec (α := α)) 1 4096 :=
  GenRed.loc t037_s2_g 1 4096 (fun _ k _ hk => hk) (fun _ _ => (by decide : (0 : Nat) < 4096))

/-- Stage 3 reads each intermediate only where its stage wrote it. -/
theorem t037_l3a {α : Type} [ExactScalar α] :
    Loc (t037_s3_g.spec (α := α)) 1 4096 :=
  GenRed.loc t037_s3_g 1 4096 (fun _ _ _ _ => (by decide : (0 : Nat) < 4096)) (fun _ _ => (by decide : (0 : Nat) < 4096))

theorem t037_l3b {α : Type} [ExactScalar α] :
    Loc (t037_s3_g.spec (α := α)) 2 1 :=
  GenRed.loc t037_s3_g 2 1 (fun _ _ _ _ => (by decide : (0 : Nat) < 1)) (fun _ _ => (by decide : (0 : Nat) < 1))

/-- Correctness certificate for t037: the composed three-stage pipeline. -/
theorem t037_correct {α : Type} [ExactScalar α] :
    ∀ (bufs : Nat → Buf α) (m1 m2 m3 : Mem α) (q : Nat),
      q < (t037_s3_g.spec (α := α)).outSize →
      runThree (t037_s1_g.prog t037_s1_block t037_s1_nkb)
               (t037_s2_g.prog t037_s2_block t037_s2_nkb)
               (t037_s3_g.prog t037_s3_block t037_s3_nkb) 1 2 bufs m1 m2 m3 q
        = compose3 (t037_s1_g.spec (α := α)) (t037_s2_g.spec (α := α))
            (t037_s3_g.spec (α := α)) 1 2 bufs q :=
  three_stage (by decide) t037_s1_impl t037_s2_impl t037_s3_impl t037_l2 t037_l3a t037_l3b

def t037_s1_kernel : ReduceKernel :=
  { name := "t037_s1", arity := 1, block := t037_s1_block, nkb := t037_s1_nkb, nout := 4096, init := FE.zeroC, step := t037_s1_g.step t037_s1_block, stored := t037_s1_g.stored t037_s1_block }
def t037_s2_kernel : ReduceKernel :=
  { name := "t037_s2", arity := 2, block := t037_s2_block, nkb := t037_s2_nkb, nout := 1, init := FE.zeroC, step := t037_s2_g.step t037_s2_block, stored := t037_s2_g.stored t037_s2_block }
def t037_s3_kernel : ReduceKernel :=
  { name := "t037_s3", arity := 3, block := t037_s3_block, nkb := t037_s3_nkb, nout := 234881024, init := FE.zeroC, step := t037_s3_g.step t037_s3_block, stored := t037_s3_g.stored t037_s3_block }
def t037_kernel : PipelineKernel3 :=
  { name := "t037", arity := 1, n1 := 4096, n2 := 1, stage1 := t037_s1_kernel, stage2 := t037_s2_kernel, stage3 := t037_s3_kernel }

-- t038: two-stage pipeline, 1 input(s), 4096-element intermediate at buffer 1
--   row normalisation over dim 1 of (4096, 65535): outer=4096 K=65535 inner=1, intermediate 4096
def t038_s1_g : GenRed :=
  { nout := 4096, K := 65535
  , offs := fun b => ([(IE.add (IE.mul (IE.pid 0) (IE.lit 65535)) IE.rk)]).getD b (IE.lit 0)
  , inRange := BE.tt
  , body := (SE.un .abs (SE.inp 0))
  , postOffs := fun b => ([(IE.lit 0)]).getD b (IE.lit 0)
  , post := (SE.inp 0)
  , outGuard := BE.tt
  , nInp := 1 }
def t038_s1_block : Nat := 1024
def t038_s1_nkb : Nat := 64

theorem t038_s1_wf : t038_s1_g.Wf :=
  { offs_ok := IE.qkOnly_getD _ (by decide)
  , post_ok := IE.qkOnly_getD _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

theorem t038_s1_impl {α : Type} [ExactScalar α] :
    Implements (t038_s1_g.prog t038_s1_block t038_s1_nkb) (t038_s1_g.spec (α := α)) :=
  GenRed.prog_implements t038_s1_g t038_s1_block t038_s1_nkb t038_s1_wf (by decide) (by decide)

def t038_s2_g : GenRed :=
  { nout := 268431360, K := 1
  , offs := fun b => ([(IE.pid 0), (IE.divi (IE.pid 0) (IE.lit 65535))]).getD b (IE.lit 0)
  , inRange := BE.tt
  , body := (SE.bin .div (SE.inp 0) (SE.bin .mul (SE.inp 1) (SE.lit false 1 65535)))
  , postOffs := fun b => ([(IE.lit 0), (IE.lit 0)]).getD b (IE.lit 0)
  , post := (SE.inp 0)
  , outGuard := BE.tt
  , nInp := 2 }
def t038_s2_block : Nat := 1
def t038_s2_nkb : Nat := 1

theorem t038_s2_wf : t038_s2_g.Wf :=
  { offs_ok := IE.qkOnly_getD _ (by decide)
  , post_ok := IE.qkOnly_getD _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

theorem t038_s2_impl {α : Type} [ExactScalar α] :
    Implements (t038_s2_g.prog t038_s2_block t038_s2_nkb) (t038_s2_g.spec (α := α)) :=
  GenRed.prog_implements t038_s2_g t038_s2_block t038_s2_nkb t038_s2_wf (by decide) (by decide)

/-- Stage 2 reads the intermediate only where stage 1 wrote it. -/
theorem t038_loc {α : Type} [ExactScalar α] :
    ∀ (bufs : Nat → Buf α) (u v : Buf α),
      (∀ i, i < (t038_s1_g.spec (α := α)).outSize → u i = v i) →
      ∀ q, q < (t038_s2_g.spec (α := α)).outSize →
        (t038_s2_g.spec (α := α)).out (subst bufs 1 u) q
          = (t038_s2_g.spec (α := α)).out (subst bufs 1 v) q :=
  GenRed.spec_locality t038_s2_g 1 4096
    (fun q k hq hk => (bound_div (a := 4096) (d := 65535) hq))
    (fun _ _ => (by decide : (0 : Nat) < 4096))

/-- Correctness certificate for t038: the composed pipeline. -/
theorem t038_correct {α : Type} [ExactScalar α] :
    ∀ (bufs : Nat → Buf α) (m1 m2 : Mem α) (q : Nat),
      q < (t038_s2_g.spec (α := α)).outSize →
      runTwo (t038_s1_g.prog t038_s1_block t038_s1_nkb)
             (t038_s2_g.prog t038_s2_block t038_s2_nkb) 1 bufs m1 m2 q
        = (t038_s2_g.spec (α := α)).out
            (subst bufs 1 (fun i => (t038_s1_g.spec (α := α)).out bufs i)) q :=
  two_stage t038_s1_impl t038_s2_impl t038_loc

def t038_s1_kernel : ReduceKernel :=
  { name := "t038_s1", arity := 1, block := t038_s1_block, nkb := t038_s1_nkb, nout := 4096, init := FE.zeroC, step := t038_s1_g.step t038_s1_block, stored := t038_s1_g.stored t038_s1_block }
def t038_s2_kernel : ReduceKernel :=
  { name := "t038_s2", arity := 2, block := t038_s2_block, nkb := t038_s2_nkb, nout := 268431360, init := FE.zeroC, step := t038_s2_g.step t038_s2_block, stored := t038_s2_g.stored t038_s2_block }
def t038_kernel : PipelineKernel :=
  { name := "t038", arity := 1, n1 := 4096, stage1 := t038_s1_kernel, stage2 := t038_s2_kernel }

-- t039: two-stage pipeline, 1 input(s), 4096-element intermediate at buffer 1
--   row normalisation over dim 1 of (4096, 65535): outer=4096 K=65535 inner=1, intermediate 4096
def t039_s1_g : GenRed :=
  { nout := 4096, K := 65535
  , offs := fun b => ([(IE.add (IE.mul (IE.pid 0) (IE.lit 65535)) IE.rk)]).getD b (IE.lit 0)
  , inRange := BE.tt
  , body := (SE.bin .mul (SE.inp 0) (SE.inp 0))
  , postOffs := fun b => ([(IE.lit 0)]).getD b (IE.lit 0)
  , post := (SE.inp 0)
  , outGuard := BE.tt
  , nInp := 1 }
def t039_s1_block : Nat := 1024
def t039_s1_nkb : Nat := 64

theorem t039_s1_wf : t039_s1_g.Wf :=
  { offs_ok := IE.qkOnly_getD _ (by decide)
  , post_ok := IE.qkOnly_getD _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

theorem t039_s1_impl {α : Type} [ExactScalar α] :
    Implements (t039_s1_g.prog t039_s1_block t039_s1_nkb) (t039_s1_g.spec (α := α)) :=
  GenRed.prog_implements t039_s1_g t039_s1_block t039_s1_nkb t039_s1_wf (by decide) (by decide)

def t039_s2_g : GenRed :=
  { nout := 268431360, K := 1
  , offs := fun b => ([(IE.pid 0), (IE.divi (IE.pid 0) (IE.lit 65535))]).getD b (IE.lit 0)
  , inRange := BE.tt
  , body := (SE.bin .div (SE.inp 0) (SE.un .sqrt (SE.inp 1)))
  , postOffs := fun b => ([(IE.lit 0), (IE.lit 0)]).getD b (IE.lit 0)
  , post := (SE.inp 0)
  , outGuard := BE.tt
  , nInp := 2 }
def t039_s2_block : Nat := 1
def t039_s2_nkb : Nat := 1

theorem t039_s2_wf : t039_s2_g.Wf :=
  { offs_ok := IE.qkOnly_getD _ (by decide)
  , post_ok := IE.qkOnly_getD _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

theorem t039_s2_impl {α : Type} [ExactScalar α] :
    Implements (t039_s2_g.prog t039_s2_block t039_s2_nkb) (t039_s2_g.spec (α := α)) :=
  GenRed.prog_implements t039_s2_g t039_s2_block t039_s2_nkb t039_s2_wf (by decide) (by decide)

/-- Stage 2 reads the intermediate only where stage 1 wrote it. -/
theorem t039_loc {α : Type} [ExactScalar α] :
    ∀ (bufs : Nat → Buf α) (u v : Buf α),
      (∀ i, i < (t039_s1_g.spec (α := α)).outSize → u i = v i) →
      ∀ q, q < (t039_s2_g.spec (α := α)).outSize →
        (t039_s2_g.spec (α := α)).out (subst bufs 1 u) q
          = (t039_s2_g.spec (α := α)).out (subst bufs 1 v) q :=
  GenRed.spec_locality t039_s2_g 1 4096
    (fun q k hq hk => (bound_div (a := 4096) (d := 65535) hq))
    (fun _ _ => (by decide : (0 : Nat) < 4096))

/-- Correctness certificate for t039: the composed pipeline. -/
theorem t039_correct {α : Type} [ExactScalar α] :
    ∀ (bufs : Nat → Buf α) (m1 m2 : Mem α) (q : Nat),
      q < (t039_s2_g.spec (α := α)).outSize →
      runTwo (t039_s1_g.prog t039_s1_block t039_s1_nkb)
             (t039_s2_g.prog t039_s2_block t039_s2_nkb) 1 bufs m1 m2 q
        = (t039_s2_g.spec (α := α)).out
            (subst bufs 1 (fun i => (t039_s1_g.spec (α := α)).out bufs i)) q :=
  two_stage t039_s1_impl t039_s2_impl t039_loc

def t039_s1_kernel : ReduceKernel :=
  { name := "t039_s1", arity := 1, block := t039_s1_block, nkb := t039_s1_nkb, nout := 4096, init := FE.zeroC, step := t039_s1_g.step t039_s1_block, stored := t039_s1_g.stored t039_s1_block }
def t039_s2_kernel : ReduceKernel :=
  { name := "t039_s2", arity := 2, block := t039_s2_block, nkb := t039_s2_nkb, nout := 268431360, init := FE.zeroC, step := t039_s2_g.step t039_s2_block, stored := t039_s2_g.stored t039_s2_block }
def t039_kernel : PipelineKernel :=
  { name := "t039", arity := 1, n1 := 4096, stage1 := t039_s1_kernel, stage2 := t039_s2_kernel }

-- t040: three-stage normalisation, 3 input buffer(s), intermediates 16 and 16 at buffers 3 and 4
--   LayerNorm on (16, 64, 256, 256): 16 statistics over 4194304 elements, eps=1e-05, affine
def t040_s1_g : GenRed :=
  { nout := 16, K := 4194304
  , offs := fun b => ([(IE.add (IE.mul (IE.pid 0) (IE.lit 4194304)) IE.rk), (IE.lit 0), (IE.lit 0), (IE.lit 0), (IE.lit 0)]).getD b (IE.lit 0)
  , inRange := BE.tt
  , body := (SE.inp 0)
  , postOffs := fun b => ([(IE.lit 0), (IE.lit 0), (IE.lit 0), (IE.lit 0), (IE.lit 0)]).getD b (IE.lit 0)
  , post := (SE.inp 0)
  , outGuard := BE.tt
  , nInp := 1 }
def t040_s1_block : Nat := 1024
def t040_s1_nkb : Nat := 4096

theorem t040_s1_wf : t040_s1_g.Wf :=
  { offs_ok := IE.qkOnly_getD _ (by decide)
  , post_ok := IE.qkOnly_getD _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

theorem t040_s1_impl {α : Type} [ExactScalar α] :
    Implements (t040_s1_g.prog t040_s1_block t040_s1_nkb) (t040_s1_g.spec (α := α)) :=
  GenRed.prog_implements t040_s1_g t040_s1_block t040_s1_nkb t040_s1_wf (by decide) (by decide)

def t040_s2_g : GenRed :=
  { nout := 16, K := 4194304
  , offs := fun b => ([(IE.add (IE.mul (IE.pid 0) (IE.lit 4194304)) IE.rk), (IE.lit 0), (IE.lit 0), (IE.pid 0), (IE.lit 0)]).getD b (IE.lit 0)
  , inRange := BE.tt
  , body := (SE.bin .mul (SE.bin .sub (SE.inp 0) (SE.bin .mul (SE.inp 3) (SE.lit false 1 4194304))) (SE.bin .sub (SE.inp 0) (SE.bin .mul (SE.inp 3) (SE.lit false 1 4194304))))
  , postOffs := fun b => ([(IE.lit 0), (IE.lit 0), (IE.lit 0), (IE.lit 0), (IE.lit 0)]).getD b (IE.lit 0)
  , post := (SE.inp 0)
  , outGuard := BE.tt
  , nInp := 4 }
def t040_s2_block : Nat := 1024
def t040_s2_nkb : Nat := 4096

theorem t040_s2_wf : t040_s2_g.Wf :=
  { offs_ok := IE.qkOnly_getD _ (by decide)
  , post_ok := IE.qkOnly_getD _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

theorem t040_s2_impl {α : Type} [ExactScalar α] :
    Implements (t040_s2_g.prog t040_s2_block t040_s2_nkb) (t040_s2_g.spec (α := α)) :=
  GenRed.prog_implements t040_s2_g t040_s2_block t040_s2_nkb t040_s2_wf (by decide) (by decide)

def t040_s3_g : GenRed :=
  { nout := 67108864, K := 1
  , offs := fun b => ([(IE.pid 0), (IE.modi (IE.pid 0) (IE.lit 4194304)), (IE.modi (IE.pid 0) (IE.lit 4194304)), (IE.divi (IE.pid 0) (IE.lit 4194304)), (IE.divi (IE.pid 0) (IE.lit 4194304))]).getD b (IE.lit 0)
  , inRange := BE.tt
  , body := (SE.bin .add (SE.bin .mul (SE.bin .mul (SE.bin .sub (SE.inp 0) (SE.bin .mul (SE.inp 3) (SE.lit false 1 4194304))) (SE.recip (SE.un .sqrt (SE.bin .add (SE.bin .mul (SE.inp 4) (SE.lit false 1 4194304)) (SE.lit false 1 100000))))) (SE.inp 1)) (SE.inp 2))
  , postOffs := fun b => ([(IE.lit 0), (IE.lit 0), (IE.lit 0), (IE.lit 0), (IE.lit 0)]).getD b (IE.lit 0)
  , post := (SE.inp 0)
  , outGuard := BE.tt
  , nInp := 5 }
def t040_s3_block : Nat := 1
def t040_s3_nkb : Nat := 1

theorem t040_s3_wf : t040_s3_g.Wf :=
  { offs_ok := IE.qkOnly_getD _ (by decide)
  , post_ok := IE.qkOnly_getD _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

theorem t040_s3_impl {α : Type} [ExactScalar α] :
    Implements (t040_s3_g.prog t040_s3_block t040_s3_nkb) (t040_s3_g.spec (α := α)) :=
  GenRed.prog_implements t040_s3_g t040_s3_block t040_s3_nkb t040_s3_wf (by decide) (by decide)

/-- Stage 2 reads the first intermediate only where stage 1 wrote it. -/
theorem t040_l2 {α : Type} [ExactScalar α] :
    Loc (t040_s2_g.spec (α := α)) 3 16 :=
  GenRed.loc t040_s2_g 3 16 (fun q _ hq _ => hq) (fun _ _ => (by decide : (0 : Nat) < 16))

/-- Stage 3 reads each intermediate only where its stage wrote it. -/
theorem t040_l3a {α : Type} [ExactScalar α] :
    Loc (t040_s3_g.spec (α := α)) 3 16 :=
  GenRed.loc t040_s3_g 3 16 (fun q k hq hk => (bound_div (a := 16) (d := 4194304) hq)) (fun _ _ => (by decide : (0 : Nat) < 16))

theorem t040_l3b {α : Type} [ExactScalar α] :
    Loc (t040_s3_g.spec (α := α)) 4 16 :=
  GenRed.loc t040_s3_g 4 16 (fun q k hq hk => (bound_div (a := 16) (d := 4194304) hq)) (fun _ _ => (by decide : (0 : Nat) < 16))

/-- Correctness certificate for t040: the composed three-stage pipeline. -/
theorem t040_correct {α : Type} [ExactScalar α] :
    ∀ (bufs : Nat → Buf α) (m1 m2 m3 : Mem α) (q : Nat),
      q < (t040_s3_g.spec (α := α)).outSize →
      runThree (t040_s1_g.prog t040_s1_block t040_s1_nkb)
               (t040_s2_g.prog t040_s2_block t040_s2_nkb)
               (t040_s3_g.prog t040_s3_block t040_s3_nkb) 3 4 bufs m1 m2 m3 q
        = compose3 (t040_s1_g.spec (α := α)) (t040_s2_g.spec (α := α))
            (t040_s3_g.spec (α := α)) 3 4 bufs q :=
  three_stage (by decide) t040_s1_impl t040_s2_impl t040_s3_impl t040_l2 t040_l3a t040_l3b

def t040_s1_kernel : ReduceKernel :=
  { name := "t040_s1", arity := 1, block := t040_s1_block, nkb := t040_s1_nkb, nout := 16, init := FE.zeroC, step := t040_s1_g.step t040_s1_block, stored := t040_s1_g.stored t040_s1_block }
def t040_s2_kernel : ReduceKernel :=
  { name := "t040_s2", arity := 4, block := t040_s2_block, nkb := t040_s2_nkb, nout := 16, init := FE.zeroC, step := t040_s2_g.step t040_s2_block, stored := t040_s2_g.stored t040_s2_block }
def t040_s3_kernel : ReduceKernel :=
  { name := "t040_s3", arity := 5, block := t040_s3_block, nkb := t040_s3_nkb, nout := 67108864, init := FE.zeroC, step := t040_s3_g.step t040_s3_block, stored := t040_s3_g.stored t040_s3_block }
def t040_kernel : PipelineKernel3 :=
  { name := "t040", arity := 3, n1 := 16, n2 := 16, stage1 := t040_s1_kernel, stage2 := t040_s2_kernel, stage3 := t040_s3_kernel }

-- t041: max reduction, 1 input(s), 402573312 outputs, extent 8
--   maxpool1d: N=32 C=192 k=(8,) stride=(1,) pad=(4,) dil=(3,); coordinates clamped rather than masked
def t041_g : MaxRed :=
  { nout := 402573312, K := 8
  , offs := fun b => ([(IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 12580416)) (IE.lit 192)) (IE.modi (IE.divi (IE.pid 0) (IE.lit 65523)) (IE.lit 192))) (IE.lit 65536)) (IE.sub (IE.add (IE.modi (IE.pid 0) (IE.lit 65523)) (IE.mul (IE.sub (IE.add IE.rk (IE.sub (IE.divi (IE.add (IE.sub (IE.lit 4) (IE.modi (IE.pid 0) (IE.lit 65523))) (IE.lit 2)) (IE.lit 3)) IE.rk)) (IE.sub (IE.add IE.rk (IE.sub (IE.divi (IE.add (IE.sub (IE.lit 4) (IE.modi (IE.pid 0) (IE.lit 65523))) (IE.lit 2)) (IE.lit 3)) IE.rk)) (IE.divi (IE.sub (IE.lit 65539) (IE.modi (IE.pid 0) (IE.lit 65523))) (IE.lit 3)))) (IE.lit 3))) (IE.lit 4)))]).getD b (IE.lit 0)
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
  , nkb := t041_nkb, nout := 402573312
  , init := t041_g.seed
  , step := t041_g.step t041_block
  , stored := t041_g.stored t041_block }

-- t042: max reduction, 1 input(s), 267387904 outputs, extent 16
--   maxpool2d: N=16 C=64 k=(4, 4) stride=(1, 1) pad=(1, 1) dil=(1, 1); coordinates clamped rather than masked
def t042_g : MaxRed :=
  { nout := 267387904, K := 16
  , offs := fun b => ([(IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 16711744)) (IE.lit 64)) (IE.modi (IE.divi (IE.pid 0) (IE.lit 261121)) (IE.lit 64))) (IE.lit 512)) (IE.sub (IE.add (IE.modi (IE.divi (IE.pid 0) (IE.lit 511)) (IE.lit 511)) (IE.sub (IE.add (IE.divi IE.rk (IE.lit 4)) (IE.sub (IE.sub (IE.lit 1) (IE.modi (IE.divi (IE.pid 0) (IE.lit 511)) (IE.lit 511))) (IE.divi IE.rk (IE.lit 4)))) (IE.sub (IE.add (IE.divi IE.rk (IE.lit 4)) (IE.sub (IE.sub (IE.lit 1) (IE.modi (IE.divi (IE.pid 0) (IE.lit 511)) (IE.lit 511))) (IE.divi IE.rk (IE.lit 4)))) (IE.sub (IE.lit 512) (IE.modi (IE.divi (IE.pid 0) (IE.lit 511)) (IE.lit 511)))))) (IE.lit 1))) (IE.lit 512)) (IE.sub (IE.add (IE.modi (IE.pid 0) (IE.lit 511)) (IE.sub (IE.add (IE.modi IE.rk (IE.lit 4)) (IE.sub (IE.sub (IE.lit 1) (IE.modi (IE.pid 0) (IE.lit 511))) (IE.modi IE.rk (IE.lit 4)))) (IE.sub (IE.add (IE.modi IE.rk (IE.lit 4)) (IE.sub (IE.sub (IE.lit 1) (IE.modi (IE.pid 0) (IE.lit 511))) (IE.modi IE.rk (IE.lit 4)))) (IE.sub (IE.lit 512) (IE.modi (IE.pid 0) (IE.lit 511)))))) (IE.lit 1)))]).getD b (IE.lit 0)
  , body := (SE.inp 0)
  , postOffs := fun b => ([(IE.lit 0)]).getD b (IE.lit 0)
  , post := (SE.inp 0)
  , nInp := 1 }
def t042_block : Nat := 16
def t042_nkb : Nat := 1

theorem t042_wf : t042_g.Wf :=
  { offs_ok := IE.qkOnly_getD _ (by decide)
  , post_ok := IE.qkOnly_getD _ (by decide) }

/-- Correctness certificate for t042. -/
theorem t042_correct {α : Type} [ExactScalar α] :
    Implements (t042_g.prog t042_block t042_nkb) (t042_g.spec (α := α)) :=
  MaxRed.prog_implements t042_g t042_block t042_nkb t042_wf (by decide) (by decide) (by decide)

def t042_kernel : ReduceKernel :=
  { name := "t042", arity := 1, block := t042_block
  , nkb := t042_nkb, nout := 267387904
  , init := t042_g.seed
  , step := t042_g.step t042_block
  , stored := t042_g.stored t042_block }

-- t043: max reduction, 1 input(s), 122023936 outputs, extent 27
--   maxpool3d: N=16 C=32 k=(3, 3, 3) stride=(2, 2, 2) pad=(1, 1, 1) dil=(3, 3, 3); coordinates clamped rather than masked
def t043_g : MaxRed :=
  { nout := 122023936, K := 27
  , offs := fun b => ([(IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 7626496)) (IE.lit 32)) (IE.modi (IE.divi (IE.pid 0) (IE.lit 238328)) (IE.lit 32))) (IE.lit 128)) (IE.sub (IE.add (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 3844)) (IE.lit 62)) (IE.lit 2)) (IE.mul (IE.sub (IE.add (IE.divi IE.rk (IE.lit 9)) (IE.sub (IE.divi (IE.add (IE.sub (IE.lit 1) (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 3844)) (IE.lit 62)) (IE.lit 2))) (IE.lit 2)) (IE.lit 3)) (IE.divi IE.rk (IE.lit 9)))) (IE.sub (IE.add (IE.divi IE.rk (IE.lit 9)) (IE.sub (IE.divi (IE.add (IE.sub (IE.lit 1) (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 3844)) (IE.lit 62)) (IE.lit 2))) (IE.lit 2)) (IE.lit 3)) (IE.divi IE.rk (IE.lit 9)))) (IE.divi (IE.sub (IE.lit 128) (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 3844)) (IE.lit 62)) (IE.lit 2))) (IE.lit 3)))) (IE.lit 3))) (IE.lit 1))) (IE.lit 128)) (IE.sub (IE.add (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 62)) (IE.lit 62)) (IE.lit 2)) (IE.mul (IE.sub (IE.add (IE.modi (IE.divi IE.rk (IE.lit 3)) (IE.lit 3)) (IE.sub (IE.divi (IE.add (IE.sub (IE.lit 1) (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 62)) (IE.lit 62)) (IE.lit 2))) (IE.lit 2)) (IE.lit 3)) (IE.modi (IE.divi IE.rk (IE.lit 3)) (IE.lit 3)))) (IE.sub (IE.add (IE.modi (IE.divi IE.rk (IE.lit 3)) (IE.lit 3)) (IE.sub (IE.divi (IE.add (IE.sub (IE.lit 1) (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 62)) (IE.lit 62)) (IE.lit 2))) (IE.lit 2)) (IE.lit 3)) (IE.modi (IE.divi IE.rk (IE.lit 3)) (IE.lit 3)))) (IE.divi (IE.sub (IE.lit 128) (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 62)) (IE.lit 62)) (IE.lit 2))) (IE.lit 3)))) (IE.lit 3))) (IE.lit 1))) (IE.lit 128)) (IE.sub (IE.add (IE.mul (IE.modi (IE.pid 0) (IE.lit 62)) (IE.lit 2)) (IE.mul (IE.sub (IE.add (IE.modi IE.rk (IE.lit 3)) (IE.sub (IE.divi (IE.add (IE.sub (IE.lit 1) (IE.mul (IE.modi (IE.pid 0) (IE.lit 62)) (IE.lit 2))) (IE.lit 2)) (IE.lit 3)) (IE.modi IE.rk (IE.lit 3)))) (IE.sub (IE.add (IE.modi IE.rk (IE.lit 3)) (IE.sub (IE.divi (IE.add (IE.sub (IE.lit 1) (IE.mul (IE.modi (IE.pid 0) (IE.lit 62)) (IE.lit 2))) (IE.lit 2)) (IE.lit 3)) (IE.modi IE.rk (IE.lit 3)))) (IE.divi (IE.sub (IE.lit 128) (IE.mul (IE.modi (IE.pid 0) (IE.lit 62)) (IE.lit 2))) (IE.lit 3)))) (IE.lit 3))) (IE.lit 1)))]).getD b (IE.lit 0)
  , body := (SE.inp 0)
  , postOffs := fun b => ([(IE.lit 0)]).getD b (IE.lit 0)
  , post := (SE.inp 0)
  , nInp := 1 }
def t043_block : Nat := 16
def t043_nkb : Nat := 2

theorem t043_wf : t043_g.Wf :=
  { offs_ok := IE.qkOnly_getD _ (by decide)
  , post_ok := IE.qkOnly_getD _ (by decide) }

/-- Correctness certificate for t043. -/
theorem t043_correct {α : Type} [ExactScalar α] :
    Implements (t043_g.prog t043_block t043_nkb) (t043_g.spec (α := α)) :=
  MaxRed.prog_implements t043_g t043_block t043_nkb t043_wf (by decide) (by decide) (by decide)

def t043_kernel : ReduceKernel :=
  { name := "t043", arity := 1, block := t043_block
  , nkb := t043_nkb, nout := 122023936
  , init := t043_g.seed
  , step := t043_g.step t043_block
  , stored := t043_g.stored t043_block }

-- t044: reducing family, 1 inputs, 268439552 outputs, reduced extent 8
--   avgpool1d: N=32 C=128 k=(8,) stride=(1,) pad=(4,) window=8
def t044_g : GenRed :=
  { nout := 268439552, K := 8
  , offs := fun b => ([(IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 8388736)) (IE.lit 128)) (IE.modi (IE.divi (IE.pid 0) (IE.lit 65537)) (IE.lit 128))) (IE.lit 65536)) (IE.sub (IE.add (IE.modi (IE.pid 0) (IE.lit 65537)) IE.rk) (IE.lit 4)))]).getD b (IE.lit 0)
  , inRange := (BE.and (BE.cmp .le (IE.lit 4) (IE.add (IE.modi (IE.pid 0) (IE.lit 65537)) IE.rk)) (BE.cmp .lt (IE.add (IE.modi (IE.pid 0) (IE.lit 65537)) IE.rk) (IE.lit 65540)))
  , body := (SE.inp 0)
  , postOffs := fun b => ([(IE.lit 0)]).getD b (IE.lit 0)
  , post := (SE.bin .mul (SE.inp 0) (SE.lit false 1 8))
  , outGuard := BE.tt
  , nInp := 1 }
def t044_block : Nat := 8
def t044_nkb : Nat := 1

/-- Index maps mention only the output and reduction indices. -/
theorem t044_wf : t044_g.Wf :=
  { offs_ok := IE.qkOnly_getD _ (by decide)
  , post_ok := IE.qkOnly_getD _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

/-- Correctness certificate for t044. -/
theorem t044_correct {α : Type} [ExactScalar α] :
    Implements (t044_g.prog t044_block t044_nkb) (t044_g.spec (α := α)) :=
  GenRed.prog_implements t044_g t044_block t044_nkb t044_wf (by decide) (by decide)

def t044_kernel : ReduceKernel :=
  { name := "t044", arity := 1, block := t044_block
  , nkb := t044_nkb, nout := 268439552
  , init := FE.zeroC
  , step := t044_g.step t044_block
  , stored := t044_g.stored t044_block }

-- t045: reducing family, 1 inputs, 8856576 outputs, reduced extent 121
--   avgpool2d: N=4 C=64 k=(11, 11) stride=(11, 11) pad=(0, 0) window=121
def t045_g : GenRed :=
  { nout := 8856576, K := 121
  , offs := fun b => ([(IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 2214144)) (IE.lit 64)) (IE.modi (IE.divi (IE.pid 0) (IE.lit 34596)) (IE.lit 64))) (IE.lit 2048)) (IE.add (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 186)) (IE.lit 186)) (IE.lit 11)) (IE.divi IE.rk (IE.lit 11)))) (IE.lit 2048)) (IE.add (IE.mul (IE.modi (IE.pid 0) (IE.lit 186)) (IE.lit 11)) (IE.modi IE.rk (IE.lit 11))))]).getD b (IE.lit 0)
  , inRange := (BE.and (BE.and (BE.and (BE.cmp .le (IE.lit 0) (IE.add (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 186)) (IE.lit 186)) (IE.lit 11)) (IE.divi IE.rk (IE.lit 11)))) (BE.cmp .lt (IE.add (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 186)) (IE.lit 186)) (IE.lit 11)) (IE.divi IE.rk (IE.lit 11))) (IE.lit 2048))) (BE.cmp .le (IE.lit 0) (IE.add (IE.mul (IE.modi (IE.pid 0) (IE.lit 186)) (IE.lit 11)) (IE.modi IE.rk (IE.lit 11))))) (BE.cmp .lt (IE.add (IE.mul (IE.modi (IE.pid 0) (IE.lit 186)) (IE.lit 11)) (IE.modi IE.rk (IE.lit 11))) (IE.lit 2048)))
  , body := (SE.inp 0)
  , postOffs := fun b => ([(IE.lit 0)]).getD b (IE.lit 0)
  , post := (SE.bin .mul (SE.inp 0) (SE.lit false 1 121))
  , outGuard := BE.tt
  , nInp := 1 }
def t045_block : Nat := 64
def t045_nkb : Nat := 2

/-- Index maps mention only the output and reduction indices. -/
theorem t045_wf : t045_g.Wf :=
  { offs_ok := IE.qkOnly_getD _ (by decide)
  , post_ok := IE.qkOnly_getD _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

/-- Correctness certificate for t045. -/
theorem t045_correct {α : Type} [ExactScalar α] :
    Implements (t045_g.prog t045_block t045_nkb) (t045_g.spec (α := α)) :=
  GenRed.prog_implements t045_g t045_block t045_nkb t045_wf (by decide) (by decide)

def t045_kernel : ReduceKernel :=
  { name := "t045", arity := 1, block := t045_block
  , nkb := t045_nkb, nout := 8856576
  , init := FE.zeroC
  , step := t045_g.step t045_block
  , stored := t045_g.stored t045_block }

-- t046: reducing family, 1 inputs, 134217728 outputs, reduced extent 27
--   avgpool3d: N=8 C=32 k=(3, 3, 3) stride=(2, 2, 2) pad=(1, 1, 1) window=27
def t046_g : GenRed :=
  { nout := 134217728, K := 27
  , offs := fun b => ([(IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 16777216)) (IE.lit 32)) (IE.modi (IE.divi (IE.pid 0) (IE.lit 524288)) (IE.lit 32))) (IE.lit 128)) (IE.sub (IE.add (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 8192)) (IE.lit 64)) (IE.lit 2)) (IE.divi IE.rk (IE.lit 9))) (IE.lit 1))) (IE.lit 128)) (IE.sub (IE.add (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 128)) (IE.lit 64)) (IE.lit 2)) (IE.modi (IE.divi IE.rk (IE.lit 3)) (IE.lit 3))) (IE.lit 1))) (IE.lit 256)) (IE.sub (IE.add (IE.mul (IE.modi (IE.pid 0) (IE.lit 128)) (IE.lit 2)) (IE.modi IE.rk (IE.lit 3))) (IE.lit 1)))]).getD b (IE.lit 0)
  , inRange := (BE.and (BE.and (BE.and (BE.and (BE.and (BE.cmp .le (IE.lit 1) (IE.add (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 8192)) (IE.lit 64)) (IE.lit 2)) (IE.divi IE.rk (IE.lit 9)))) (BE.cmp .lt (IE.add (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 8192)) (IE.lit 64)) (IE.lit 2)) (IE.divi IE.rk (IE.lit 9))) (IE.lit 129))) (BE.cmp .le (IE.lit 1) (IE.add (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 128)) (IE.lit 64)) (IE.lit 2)) (IE.modi (IE.divi IE.rk (IE.lit 3)) (IE.lit 3))))) (BE.cmp .lt (IE.add (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 128)) (IE.lit 64)) (IE.lit 2)) (IE.modi (IE.divi IE.rk (IE.lit 3)) (IE.lit 3))) (IE.lit 129))) (BE.cmp .le (IE.lit 1) (IE.add (IE.mul (IE.modi (IE.pid 0) (IE.lit 128)) (IE.lit 2)) (IE.modi IE.rk (IE.lit 3))))) (BE.cmp .lt (IE.add (IE.mul (IE.modi (IE.pid 0) (IE.lit 128)) (IE.lit 2)) (IE.modi IE.rk (IE.lit 3))) (IE.lit 257)))
  , body := (SE.inp 0)
  , postOffs := fun b => ([(IE.lit 0)]).getD b (IE.lit 0)
  , post := (SE.bin .mul (SE.inp 0) (SE.lit false 1 27))
  , outGuard := BE.tt
  , nInp := 1 }
def t046_block : Nat := 16
def t046_nkb : Nat := 2

/-- Index maps mention only the output and reduction indices. -/
theorem t046_wf : t046_g.Wf :=
  { offs_ok := IE.qkOnly_getD _ (by decide)
  , post_ok := IE.qkOnly_getD _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

/-- Correctness certificate for t046. -/
theorem t046_correct {α : Type} [ExactScalar α] :
    Implements (t046_g.prog t046_block t046_nkb) (t046_g.spec (α := α)) :=
  GenRed.prog_implements t046_g t046_block t046_nkb t046_wf (by decide) (by decide)

def t046_kernel : ReduceKernel :=
  { name := "t046", arity := 1, block := t046_block
  , nkb := t046_nkb, nout := 134217728
  , init := FE.zeroC
  , step := t046_g.step t046_block
  , stored := t046_g.stored t046_block }

-- t047: reducing family, 1 inputs, 262080 outputs, reduced extent 4096
--   reduce over dim 1 of (64, 4096, 4095) (inputs [(64, 4096, 4095)]): outer=64 K=4096 inner=4095
def t047_g : GenRed :=
  { nout := 262080, K := 4096
  , offs := fun b => ([(IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 4095)) (IE.lit 4096)) IE.rk) (IE.lit 4095)) (IE.modi (IE.pid 0) (IE.lit 4095)))]).getD b (IE.lit 0)
  , inRange := BE.tt
  , body := (SE.inp 0)
  , postOffs := fun b => ([(IE.lit 0)]).getD b (IE.lit 0)
  , post := (SE.inp 0)
  , outGuard := BE.tt
  , nInp := 1 }
def t047_block : Nat := 1024
def t047_nkb : Nat := 4

/-- Index maps mention only the output and reduction indices. -/
theorem t047_wf : t047_g.Wf :=
  { offs_ok := IE.qkOnly_getD _ (by decide)
  , post_ok := IE.qkOnly_getD _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

/-- Correctness certificate for t047. -/
theorem t047_correct {α : Type} [ExactScalar α] :
    Implements (t047_g.prog t047_block t047_nkb) (t047_g.spec (α := α)) :=
  GenRed.prog_implements t047_g t047_block t047_nkb t047_wf (by decide) (by decide)

def t047_kernel : ReduceKernel :=
  { name := "t047", arity := 1, block := t047_block
  , nkb := t047_nkb, nout := 262080
  , init := FE.zeroC
  , step := t047_g.step t047_block
  , stored := t047_g.stored t047_block }

-- t048: reducing family, 1 inputs, 262080 outputs, reduced extent 4096
--   reduce over dim 1 of (64, 4096, 4095) (inputs [(64, 4096, 4095)]): outer=64 K=4096 inner=4095
def t048_g : GenRed :=
  { nout := 262080, K := 4096
  , offs := fun b => ([(IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 4095)) (IE.lit 4096)) IE.rk) (IE.lit 4095)) (IE.modi (IE.pid 0) (IE.lit 4095)))]).getD b (IE.lit 0)
  , inRange := BE.tt
  , body := (SE.inp 0)
  , postOffs := fun b => ([(IE.lit 0)]).getD b (IE.lit 0)
  , post := (SE.bin .mul (SE.inp 0) (SE.lit false 1 4096))
  , outGuard := BE.tt
  , nInp := 1 }
def t048_block : Nat := 1024
def t048_nkb : Nat := 4

/-- Index maps mention only the output and reduction indices. -/
theorem t048_wf : t048_g.Wf :=
  { offs_ok := IE.qkOnly_getD _ (by decide)
  , post_ok := IE.qkOnly_getD _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

/-- Correctness certificate for t048. -/
theorem t048_correct {α : Type} [ExactScalar α] :
    Implements (t048_g.prog t048_block t048_nkb) (t048_g.spec (α := α)) :=
  GenRed.prog_implements t048_g t048_block t048_nkb t048_wf (by decide) (by decide)

def t048_kernel : ReduceKernel :=
  { name := "t048", arity := 1, block := t048_block
  , nkb := t048_nkb, nout := 262080
  , init := FE.zeroC
  , step := t048_g.step t048_block
  , stored := t048_g.stored t048_block }

-- t049: max reduction, 1 input(s), 262080 outputs, extent 4096
--   max over dim 1 of (64, 4096, 4095): outer=64 K=4096 inner=4095
def t049_g : MaxRed :=
  { nout := 262080, K := 4096
  , offs := fun b => ([(IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 4095)) (IE.lit 4096)) IE.rk) (IE.lit 4095)) (IE.modi (IE.pid 0) (IE.lit 4095)))]).getD b (IE.lit 0)
  , body := (SE.inp 0)
  , postOffs := fun b => ([(IE.lit 0)]).getD b (IE.lit 0)
  , post := (SE.inp 0)
  , nInp := 1 }
def t049_block : Nat := 1024
def t049_nkb : Nat := 4

theorem t049_wf : t049_g.Wf :=
  { offs_ok := IE.qkOnly_getD _ (by decide)
  , post_ok := IE.qkOnly_getD _ (by decide) }

/-- Correctness certificate for t049. -/
theorem t049_correct {α : Type} [ExactScalar α] :
    Implements (t049_g.prog t049_block t049_nkb) (t049_g.spec (α := α)) :=
  MaxRed.prog_implements t049_g t049_block t049_nkb t049_wf (by decide) (by decide) (by decide)

def t049_kernel : ReduceKernel :=
  { name := "t049", arity := 1, block := t049_block
  , nkb := t049_nkb, nout := 262080
  , init := t049_g.seed
  , step := t049_g.step t049_block
  , stored := t049_g.stored t049_block }

-- t050: reducing family, 3 inputs, 74342400 outputs, reduced extent 363
--   conv2d: N=256 Cin=3 Cout=96 groups=1 k=(11, 11) stride=(4, 4) pad=(2, 2) dil=(1, 1) K=363 +bias
def t050_g : GenRed :=
  { nout := 74342400, K := 363
  , offs := fun b => ([(IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 290400)) (IE.lit 3)) (IE.divi IE.rk (IE.lit 121))) (IE.lit 224)) (IE.sub (IE.add (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 55)) (IE.lit 55)) (IE.lit 4)) (IE.modi (IE.divi IE.rk (IE.lit 11)) (IE.lit 11))) (IE.lit 2))) (IE.lit 224)) (IE.sub (IE.add (IE.mul (IE.modi (IE.pid 0) (IE.lit 55)) (IE.lit 4)) (IE.modi IE.rk (IE.lit 11))) (IE.lit 2))), (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 3025)) (IE.lit 96)) (IE.lit 3)) (IE.divi IE.rk (IE.lit 121))) (IE.lit 11)) (IE.modi (IE.divi IE.rk (IE.lit 11)) (IE.lit 11))) (IE.lit 11)) (IE.modi IE.rk (IE.lit 11))), (IE.lit 0)]).getD b (IE.lit 0)
  , inRange := (BE.and (BE.and (BE.and (BE.cmp .le (IE.lit 2) (IE.add (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 55)) (IE.lit 55)) (IE.lit 4)) (IE.modi (IE.divi IE.rk (IE.lit 11)) (IE.lit 11)))) (BE.cmp .lt (IE.add (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 55)) (IE.lit 55)) (IE.lit 4)) (IE.modi (IE.divi IE.rk (IE.lit 11)) (IE.lit 11))) (IE.lit 226))) (BE.cmp .le (IE.lit 2) (IE.add (IE.mul (IE.modi (IE.pid 0) (IE.lit 55)) (IE.lit 4)) (IE.modi IE.rk (IE.lit 11))))) (BE.cmp .lt (IE.add (IE.mul (IE.modi (IE.pid 0) (IE.lit 55)) (IE.lit 4)) (IE.modi IE.rk (IE.lit 11))) (IE.lit 226)))
  , body := (SE.bin .mul (SE.inp 0) (SE.inp 1))
  , postOffs := fun b => ([(IE.lit 0), (IE.lit 0), (IE.modi (IE.divi (IE.pid 0) (IE.lit 3025)) (IE.lit 96))]).getD b (IE.lit 0)
  , post := (SE.bin .add (SE.inp 0) (SE.inp 3))
  , outGuard := BE.tt
  , nInp := 3 }
def t050_block : Nat := 256
def t050_nkb : Nat := 2

/-- Index maps mention only the output and reduction indices. -/
theorem t050_wf : t050_g.Wf :=
  { offs_ok := IE.qkOnly_getD _ (by decide)
  , post_ok := IE.qkOnly_getD _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

/-- Correctness certificate for t050. -/
theorem t050_correct {α : Type} [ExactScalar α] :
    Implements (t050_g.prog t050_block t050_nkb) (t050_g.spec (α := α)) :=
  GenRed.prog_implements t050_g t050_block t050_nkb t050_wf (by decide) (by decide)

def t050_kernel : ReduceKernel :=
  { name := "t050", arity := 3, block := t050_block
  , nkb := t050_nkb, nout := 74342400
  , init := FE.zeroC
  , step := t050_g.step t050_block
  , stored := t050_g.stored t050_block }

-- t053: max reduction, 1 input(s), 262080 outputs, extent 4096
--   min over dim 1 of (64, 4096, 4095): outer=64 K=4096 inner=4095, via -max(-x)
def t053_g : MaxRed :=
  { nout := 262080, K := 4096
  , offs := fun b => ([(IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 4095)) (IE.lit 4096)) IE.rk) (IE.lit 4095)) (IE.modi (IE.pid 0) (IE.lit 4095)))]).getD b (IE.lit 0)
  , body := (SE.bin .sub (SE.lit false 0 1) (SE.inp 0))
  , postOffs := fun b => ([(IE.lit 0)]).getD b (IE.lit 0)
  , post := (SE.bin .sub (SE.lit false 0 1) (SE.inp 0))
  , nInp := 1 }
def t053_block : Nat := 1024
def t053_nkb : Nat := 4

theorem t053_wf : t053_g.Wf :=
  { offs_ok := IE.qkOnly_getD _ (by decide)
  , post_ok := IE.qkOnly_getD _ (by decide) }

/-- Correctness certificate for t053. -/
theorem t053_correct {α : Type} [ExactScalar α] :
    Implements (t053_g.prog t053_block t053_nkb) (t053_g.spec (α := α)) :=
  MaxRed.prog_implements t053_g t053_block t053_nkb t053_wf (by decide) (by decide) (by decide)

def t053_kernel : ReduceKernel :=
  { name := "t053", arity := 1, block := t053_block
  , nkb := t053_nkb, nout := 262080
  , init := t053_g.seed
  , step := t053_g.step t053_block
  , stored := t053_g.stored t053_block }

-- t054: reducing family, 2 inputs, 244047872 outputs, reduced extent 81
--   conv3d: N=16 Cin=3 Cout=64 groups=1 k=(3, 3, 3) stride=(1, 1, 1) pad=(0, 0, 0) dil=(1, 1, 1) K=81
def t054_g : GenRed :=
  { nout := 244047872, K := 81
  , offs := fun b => ([(IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 15252992)) (IE.lit 3)) (IE.divi IE.rk (IE.lit 27))) (IE.lit 64)) (IE.add (IE.modi (IE.divi (IE.pid 0) (IE.lit 3844)) (IE.lit 62)) (IE.modi (IE.divi IE.rk (IE.lit 9)) (IE.lit 3)))) (IE.lit 64)) (IE.add (IE.modi (IE.divi (IE.pid 0) (IE.lit 62)) (IE.lit 62)) (IE.modi (IE.divi IE.rk (IE.lit 3)) (IE.lit 3)))) (IE.lit 64)) (IE.add (IE.modi (IE.pid 0) (IE.lit 62)) (IE.modi IE.rk (IE.lit 3)))), (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 238328)) (IE.lit 64)) (IE.lit 3)) (IE.divi IE.rk (IE.lit 27))) (IE.lit 3)) (IE.modi (IE.divi IE.rk (IE.lit 9)) (IE.lit 3))) (IE.lit 3)) (IE.modi (IE.divi IE.rk (IE.lit 3)) (IE.lit 3))) (IE.lit 3)) (IE.modi IE.rk (IE.lit 3)))]).getD b (IE.lit 0)
  , inRange := (BE.and (BE.and (BE.cmp .lt (IE.add (IE.modi (IE.divi (IE.pid 0) (IE.lit 3844)) (IE.lit 62)) (IE.modi (IE.divi IE.rk (IE.lit 9)) (IE.lit 3))) (IE.lit 64)) (BE.cmp .lt (IE.add (IE.modi (IE.divi (IE.pid 0) (IE.lit 62)) (IE.lit 62)) (IE.modi (IE.divi IE.rk (IE.lit 3)) (IE.lit 3))) (IE.lit 64))) (BE.cmp .lt (IE.add (IE.modi (IE.pid 0) (IE.lit 62)) (IE.modi IE.rk (IE.lit 3))) (IE.lit 64)))
  , body := (SE.bin .mul (SE.inp 0) (SE.inp 1))
  , postOffs := fun b => ([(IE.lit 0), (IE.lit 0)]).getD b (IE.lit 0)
  , post := (SE.inp 0)
  , outGuard := BE.tt
  , nInp := 2 }
def t054_block : Nat := 64
def t054_nkb : Nat := 2

/-- Index maps mention only the output and reduction indices. -/
theorem t054_wf : t054_g.Wf :=
  { offs_ok := IE.qkOnly_getD _ (by decide)
  , post_ok := IE.qkOnly_getD _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

/-- Correctness certificate for t054. -/
theorem t054_correct {α : Type} [ExactScalar α] :
    Implements (t054_g.prog t054_block t054_nkb) (t054_g.spec (α := α)) :=
  GenRed.prog_implements t054_g t054_block t054_nkb t054_wf (by decide) (by decide)

def t054_kernel : ReduceKernel :=
  { name := "t054", arity := 2, block := t054_block
  , nkb := t054_nkb, nout := 244047872
  , init := FE.zeroC
  , step := t054_g.step t054_block
  , stored := t054_g.stored t054_block }

-- t055: reducing family, 2 inputs, 266864640 outputs, reduced extent 576
--   conv2d: N=4 Cin=64 Cout=128 groups=1 k=(3, 3) stride=(1, 1) pad=(0, 0) dil=(1, 1) K=576
def t055_g : GenRed :=
  { nout := 266864640, K := 576
  , offs := fun b => ([(IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 66716160)) (IE.lit 64)) (IE.divi IE.rk (IE.lit 9))) (IE.lit 512)) (IE.add (IE.modi (IE.divi (IE.pid 0) (IE.lit 1022)) (IE.lit 510)) (IE.modi (IE.divi IE.rk (IE.lit 3)) (IE.lit 3)))) (IE.lit 1024)) (IE.add (IE.modi (IE.pid 0) (IE.lit 1022)) (IE.modi IE.rk (IE.lit 3)))), (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 521220)) (IE.lit 128)) (IE.lit 64)) (IE.divi IE.rk (IE.lit 9))) (IE.lit 3)) (IE.modi (IE.divi IE.rk (IE.lit 3)) (IE.lit 3))) (IE.lit 3)) (IE.modi IE.rk (IE.lit 3)))]).getD b (IE.lit 0)
  , inRange := (BE.and (BE.cmp .lt (IE.add (IE.modi (IE.divi (IE.pid 0) (IE.lit 1022)) (IE.lit 510)) (IE.modi (IE.divi IE.rk (IE.lit 3)) (IE.lit 3))) (IE.lit 512)) (BE.cmp .lt (IE.add (IE.modi (IE.pid 0) (IE.lit 1022)) (IE.modi IE.rk (IE.lit 3))) (IE.lit 1024)))
  , body := (SE.bin .mul (SE.inp 0) (SE.inp 1))
  , postOffs := fun b => ([(IE.lit 0), (IE.lit 0)]).getD b (IE.lit 0)
  , post := (SE.inp 0)
  , outGuard := BE.tt
  , nInp := 2 }
def t055_block : Nat := 512
def t055_nkb : Nat := 2

/-- Index maps mention only the output and reduction indices. -/
theorem t055_wf : t055_g.Wf :=
  { offs_ok := IE.qkOnly_getD _ (by decide)
  , post_ok := IE.qkOnly_getD _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

/-- Correctness certificate for t055. -/
theorem t055_correct {α : Type} [ExactScalar α] :
    Implements (t055_g.prog t055_block t055_nkb) (t055_g.spec (α := α)) :=
  GenRed.prog_implements t055_g t055_block t055_nkb t055_wf (by decide) (by decide)

def t055_kernel : ReduceKernel :=
  { name := "t055", arity := 2, block := t055_block
  , nkb := t055_nkb, nout := 266864640
  , init := FE.zeroC
  , step := t055_g.step t055_block
  , stored := t055_g.stored t055_block }

-- t056: reducing family, 2 inputs, 130048000 outputs, reduced extent 2240
--   conv2d: N=8 Cin=64 Cout=128 groups=1 k=(5, 7) stride=(1, 1) pad=(0, 0) dil=(1, 1) K=2240
def t056_g : GenRed :=
  { nout := 130048000, K := 2240
  , offs := fun b => ([(IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 16256000)) (IE.lit 64)) (IE.divi IE.rk (IE.lit 35))) (IE.lit 512)) (IE.add (IE.modi (IE.divi (IE.pid 0) (IE.lit 250)) (IE.lit 508)) (IE.modi (IE.divi IE.rk (IE.lit 7)) (IE.lit 5)))) (IE.lit 256)) (IE.add (IE.modi (IE.pid 0) (IE.lit 250)) (IE.modi IE.rk (IE.lit 7)))), (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 127000)) (IE.lit 128)) (IE.lit 64)) (IE.divi IE.rk (IE.lit 35))) (IE.lit 5)) (IE.modi (IE.divi IE.rk (IE.lit 7)) (IE.lit 5))) (IE.lit 7)) (IE.modi IE.rk (IE.lit 7)))]).getD b (IE.lit 0)
  , inRange := (BE.and (BE.cmp .lt (IE.add (IE.modi (IE.divi (IE.pid 0) (IE.lit 250)) (IE.lit 508)) (IE.modi (IE.divi IE.rk (IE.lit 7)) (IE.lit 5))) (IE.lit 512)) (BE.cmp .lt (IE.add (IE.modi (IE.pid 0) (IE.lit 250)) (IE.modi IE.rk (IE.lit 7))) (IE.lit 256)))
  , body := (SE.bin .mul (SE.inp 0) (SE.inp 1))
  , postOffs := fun b => ([(IE.lit 0), (IE.lit 0)]).getD b (IE.lit 0)
  , post := (SE.inp 0)
  , outGuard := BE.tt
  , nInp := 2 }
def t056_block : Nat := 1024
def t056_nkb : Nat := 3

/-- Index maps mention only the output and reduction indices. -/
theorem t056_wf : t056_g.Wf :=
  { offs_ok := IE.qkOnly_getD _ (by decide)
  , post_ok := IE.qkOnly_getD _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

/-- Correctness certificate for t056. -/
theorem t056_correct {α : Type} [ExactScalar α] :
    Implements (t056_g.prog t056_block t056_nkb) (t056_g.spec (α := α)) :=
  GenRed.prog_implements t056_g t056_block t056_nkb t056_wf (by decide) (by decide)

def t056_kernel : ReduceKernel :=
  { name := "t056", arity := 2, block := t056_block
  , nkb := t056_nkb, nout := 130048000
  , init := FE.zeroC
  , step := t056_g.step t056_block
  , stored := t056_g.stored t056_block }

-- t057: reducing family, 2 inputs, 269485056 outputs, reduced extent 576
--   transposed conv2d: N=4 Cin=64 Cout=64 groups=1 k=(3, 3) stride=(1, 1) pad=(0, 0) dil=(1, 1) K=576
def t057_g : GenRed :=
  { nout := 269485056, K := 576
  , offs := fun b => ([(IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 67371264)) (IE.lit 64)) (IE.add (IE.mul (IE.divi (IE.modi (IE.divi (IE.pid 0) (IE.lit 1052676)) (IE.lit 64)) (IE.lit 64)) (IE.lit 64)) (IE.divi IE.rk (IE.lit 9)))) (IE.lit 1024)) (IE.sub (IE.modi (IE.divi (IE.pid 0) (IE.lit 1026)) (IE.lit 1026)) (IE.modi (IE.divi IE.rk (IE.lit 3)) (IE.lit 3)))) (IE.lit 1024)) (IE.sub (IE.modi (IE.pid 0) (IE.lit 1026)) (IE.modi IE.rk (IE.lit 3)))), (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.modi (IE.divi (IE.pid 0) (IE.lit 1052676)) (IE.lit 64)) (IE.lit 64)) (IE.lit 64)) (IE.divi IE.rk (IE.lit 9))) (IE.lit 64)) (IE.modi (IE.modi (IE.divi (IE.pid 0) (IE.lit 1052676)) (IE.lit 64)) (IE.lit 64))) (IE.lit 3)) (IE.modi (IE.divi IE.rk (IE.lit 3)) (IE.lit 3))) (IE.lit 3)) (IE.modi IE.rk (IE.lit 3)))]).getD b (IE.lit 0)
  , inRange := (BE.and (BE.and (BE.and (BE.and (BE.and (BE.cmp .le (IE.modi (IE.divi IE.rk (IE.lit 3)) (IE.lit 3)) (IE.modi (IE.divi (IE.pid 0) (IE.lit 1026)) (IE.lit 1026))) (BE.cmp .eq (IE.lit 0) (IE.lit 0))) (BE.cmp .lt (IE.sub (IE.modi (IE.divi (IE.pid 0) (IE.lit 1026)) (IE.lit 1026)) (IE.modi (IE.divi IE.rk (IE.lit 3)) (IE.lit 3))) (IE.lit 1024))) (BE.cmp .le (IE.modi IE.rk (IE.lit 3)) (IE.modi (IE.pid 0) (IE.lit 1026)))) (BE.cmp .eq (IE.lit 0) (IE.lit 0))) (BE.cmp .lt (IE.sub (IE.modi (IE.pid 0) (IE.lit 1026)) (IE.modi IE.rk (IE.lit 3))) (IE.lit 1024)))
  , body := (SE.bin .mul (SE.inp 0) (SE.inp 1))
  , postOffs := fun b => ([(IE.lit 0), (IE.lit 0)]).getD b (IE.lit 0)
  , post := (SE.inp 0)
  , outGuard := BE.tt
  , nInp := 2 }
def t057_block : Nat := 512
def t057_nkb : Nat := 2

/-- Index maps mention only the output and reduction indices. -/
theorem t057_wf : t057_g.Wf :=
  { offs_ok := IE.qkOnly_getD _ (by decide)
  , post_ok := IE.qkOnly_getD _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

/-- Correctness certificate for t057. -/
theorem t057_correct {α : Type} [ExactScalar α] :
    Implements (t057_g.prog t057_block t057_nkb) (t057_g.spec (α := α)) :=
  GenRed.prog_implements t057_g t057_block t057_nkb t057_wf (by decide) (by decide)

def t057_kernel : ReduceKernel :=
  { name := "t057", arity := 2, block := t057_block
  , nkb := t057_nkb, nout := 269485056
  , init := FE.zeroC
  , step := t057_g.step t057_block
  , stored := t057_g.stored t057_block }

-- t058: reducing family, 2 inputs, 11612160 outputs, reduced extent 3360
--   transposed conv3d: N=16 Cin=32 Cout=16 groups=1 k=(3, 5, 7) stride=(1, 1, 1) pad=(0, 0, 0) dil=(1, 1, 1) K=3360
def t058_g : GenRed :=
  { nout := 11612160, K := 3360
  , offs := fun b => ([(IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 725760)) (IE.lit 32)) (IE.add (IE.mul (IE.divi (IE.modi (IE.divi (IE.pid 0) (IE.lit 45360)) (IE.lit 16)) (IE.lit 16)) (IE.lit 32)) (IE.divi IE.rk (IE.lit 105)))) (IE.lit 16)) (IE.sub (IE.modi (IE.divi (IE.pid 0) (IE.lit 2520)) (IE.lit 18)) (IE.modi (IE.divi IE.rk (IE.lit 35)) (IE.lit 3)))) (IE.lit 32)) (IE.sub (IE.modi (IE.divi (IE.pid 0) (IE.lit 70)) (IE.lit 36)) (IE.modi (IE.divi IE.rk (IE.lit 7)) (IE.lit 5)))) (IE.lit 64)) (IE.sub (IE.modi (IE.pid 0) (IE.lit 70)) (IE.modi IE.rk (IE.lit 7)))), (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.modi (IE.divi (IE.pid 0) (IE.lit 45360)) (IE.lit 16)) (IE.lit 16)) (IE.lit 32)) (IE.divi IE.rk (IE.lit 105))) (IE.lit 16)) (IE.modi (IE.modi (IE.divi (IE.pid 0) (IE.lit 45360)) (IE.lit 16)) (IE.lit 16))) (IE.lit 3)) (IE.modi (IE.divi IE.rk (IE.lit 35)) (IE.lit 3))) (IE.lit 5)) (IE.modi (IE.divi IE.rk (IE.lit 7)) (IE.lit 5))) (IE.lit 7)) (IE.modi IE.rk (IE.lit 7)))]).getD b (IE.lit 0)
  , inRange := (BE.and (BE.and (BE.and (BE.and (BE.and (BE.and (BE.and (BE.and (BE.cmp .le (IE.modi (IE.divi IE.rk (IE.lit 35)) (IE.lit 3)) (IE.modi (IE.divi (IE.pid 0) (IE.lit 2520)) (IE.lit 18))) (BE.cmp .eq (IE.lit 0) (IE.lit 0))) (BE.cmp .lt (IE.sub (IE.modi (IE.divi (IE.pid 0) (IE.lit 2520)) (IE.lit 18)) (IE.modi (IE.divi IE.rk (IE.lit 35)) (IE.lit 3))) (IE.lit 16))) (BE.cmp .le (IE.modi (IE.divi IE.rk (IE.lit 7)) (IE.lit 5)) (IE.modi (IE.divi (IE.pid 0) (IE.lit 70)) (IE.lit 36)))) (BE.cmp .eq (IE.lit 0) (IE.lit 0))) (BE.cmp .lt (IE.sub (IE.modi (IE.divi (IE.pid 0) (IE.lit 70)) (IE.lit 36)) (IE.modi (IE.divi IE.rk (IE.lit 7)) (IE.lit 5))) (IE.lit 32))) (BE.cmp .le (IE.modi IE.rk (IE.lit 7)) (IE.modi (IE.pid 0) (IE.lit 70)))) (BE.cmp .eq (IE.lit 0) (IE.lit 0))) (BE.cmp .lt (IE.sub (IE.modi (IE.pid 0) (IE.lit 70)) (IE.modi IE.rk (IE.lit 7))) (IE.lit 64)))
  , body := (SE.bin .mul (SE.inp 0) (SE.inp 1))
  , postOffs := fun b => ([(IE.lit 0), (IE.lit 0)]).getD b (IE.lit 0)
  , post := (SE.inp 0)
  , outGuard := BE.tt
  , nInp := 2 }
def t058_block : Nat := 1024
def t058_nkb : Nat := 4

/-- Index maps mention only the output and reduction indices. -/
theorem t058_wf : t058_g.Wf :=
  { offs_ok := IE.qkOnly_getD _ (by decide)
  , post_ok := IE.qkOnly_getD _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

/-- Correctness certificate for t058. -/
theorem t058_correct {α : Type} [ExactScalar α] :
    Implements (t058_g.prog t058_block t058_nkb) (t058_g.spec (α := α)) :=
  GenRed.prog_implements t058_g t058_block t058_nkb t058_wf (by decide) (by decide)

def t058_kernel : ReduceKernel :=
  { name := "t058", arity := 2, block := t058_block
  , nkb := t058_nkb, nout := 11612160
  , init := FE.zeroC
  , step := t058_g.step t058_block
  , stored := t058_g.stored t058_block }

-- t059: reducing family, 2 inputs, 330321920 outputs, reduced extent 27
--   conv3d: N=8 Cin=3 Cout=64 groups=1 k=(3, 3, 1) stride=(1, 1, 1) pad=(0, 0, 0) dil=(1, 1, 1) K=27
def t059_g : GenRed :=
  { nout := 330321920, K := 27
  , offs := fun b => ([(IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 41290240)) (IE.lit 3)) (IE.divi IE.rk (IE.lit 9))) (IE.lit 256)) (IE.add (IE.modi (IE.divi (IE.pid 0) (IE.lit 2540)) (IE.lit 254)) (IE.modi (IE.divi IE.rk (IE.lit 3)) (IE.lit 3)))) (IE.lit 256)) (IE.add (IE.modi (IE.divi (IE.pid 0) (IE.lit 10)) (IE.lit 254)) (IE.modi IE.rk (IE.lit 3)))) (IE.lit 10)) (IE.modi (IE.pid 0) (IE.lit 10))), (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 645160)) (IE.lit 64)) (IE.lit 3)) (IE.divi IE.rk (IE.lit 9))) (IE.lit 3)) (IE.modi (IE.divi IE.rk (IE.lit 3)) (IE.lit 3))) (IE.lit 3)) (IE.modi IE.rk (IE.lit 3)))]).getD b (IE.lit 0)
  , inRange := (BE.and (BE.and (BE.cmp .lt (IE.add (IE.modi (IE.divi (IE.pid 0) (IE.lit 2540)) (IE.lit 254)) (IE.modi (IE.divi IE.rk (IE.lit 3)) (IE.lit 3))) (IE.lit 256)) (BE.cmp .lt (IE.add (IE.modi (IE.divi (IE.pid 0) (IE.lit 10)) (IE.lit 254)) (IE.modi IE.rk (IE.lit 3))) (IE.lit 256))) (BE.cmp .lt (IE.modi (IE.pid 0) (IE.lit 10)) (IE.lit 10)))
  , body := (SE.bin .mul (SE.inp 0) (SE.inp 1))
  , postOffs := fun b => ([(IE.lit 0), (IE.lit 0)]).getD b (IE.lit 0)
  , post := (SE.inp 0)
  , outGuard := BE.tt
  , nInp := 2 }
def t059_block : Nat := 16
def t059_nkb : Nat := 2

/-- Index maps mention only the output and reduction indices. -/
theorem t059_wf : t059_g.Wf :=
  { offs_ok := IE.qkOnly_getD _ (by decide)
  , post_ok := IE.qkOnly_getD _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

/-- Correctness certificate for t059. -/
theorem t059_correct {α : Type} [ExactScalar α] :
    Implements (t059_g.prog t059_block t059_nkb) (t059_g.spec (α := α)) :=
  GenRed.prog_implements t059_g t059_block t059_nkb t059_wf (by decide) (by decide)

def t059_kernel : ReduceKernel :=
  { name := "t059", arity := 2, block := t059_block
  , nkb := t059_nkb, nout := 330321920
  , init := FE.zeroC
  , step := t059_g.step t059_block
  , stored := t059_g.stored t059_block }

-- t060: reducing family, 2 inputs, 220938240 outputs, reduced extent 315
--   conv3d: N=16 Cin=3 Cout=64 groups=1 k=(3, 5, 7) stride=(1, 1, 1) pad=(0, 0, 0) dil=(1, 1, 1) K=315
def t060_g : GenRed :=
  { nout := 220938240, K := 315
  , offs := fun b => ([(IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 13808640)) (IE.lit 3)) (IE.divi IE.rk (IE.lit 105))) (IE.lit 64)) (IE.add (IE.modi (IE.divi (IE.pid 0) (IE.lit 3480)) (IE.lit 62)) (IE.modi (IE.divi IE.rk (IE.lit 35)) (IE.lit 3)))) (IE.lit 64)) (IE.add (IE.modi (IE.divi (IE.pid 0) (IE.lit 58)) (IE.lit 60)) (IE.modi (IE.divi IE.rk (IE.lit 7)) (IE.lit 5)))) (IE.lit 64)) (IE.add (IE.modi (IE.pid 0) (IE.lit 58)) (IE.modi IE.rk (IE.lit 7)))), (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 215760)) (IE.lit 64)) (IE.lit 3)) (IE.divi IE.rk (IE.lit 105))) (IE.lit 3)) (IE.modi (IE.divi IE.rk (IE.lit 35)) (IE.lit 3))) (IE.lit 5)) (IE.modi (IE.divi IE.rk (IE.lit 7)) (IE.lit 5))) (IE.lit 7)) (IE.modi IE.rk (IE.lit 7)))]).getD b (IE.lit 0)
  , inRange := (BE.and (BE.and (BE.cmp .lt (IE.add (IE.modi (IE.divi (IE.pid 0) (IE.lit 3480)) (IE.lit 62)) (IE.modi (IE.divi IE.rk (IE.lit 35)) (IE.lit 3))) (IE.lit 64)) (BE.cmp .lt (IE.add (IE.modi (IE.divi (IE.pid 0) (IE.lit 58)) (IE.lit 60)) (IE.modi (IE.divi IE.rk (IE.lit 7)) (IE.lit 5))) (IE.lit 64))) (BE.cmp .lt (IE.add (IE.modi (IE.pid 0) (IE.lit 58)) (IE.modi IE.rk (IE.lit 7))) (IE.lit 64)))
  , body := (SE.bin .mul (SE.inp 0) (SE.inp 1))
  , postOffs := fun b => ([(IE.lit 0), (IE.lit 0)]).getD b (IE.lit 0)
  , post := (SE.inp 0)
  , outGuard := BE.tt
  , nInp := 2 }
def t060_block : Nat := 256
def t060_nkb : Nat := 2

/-- Index maps mention only the output and reduction indices. -/
theorem t060_wf : t060_g.Wf :=
  { offs_ok := IE.qkOnly_getD _ (by decide)
  , post_ok := IE.qkOnly_getD _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

/-- Correctness certificate for t060. -/
theorem t060_correct {α : Type} [ExactScalar α] :
    Implements (t060_g.prog t060_block t060_nkb) (t060_g.spec (α := α)) :=
  GenRed.prog_implements t060_g t060_block t060_nkb t060_wf (by decide) (by decide)

def t060_kernel : ReduceKernel :=
  { name := "t060", arity := 2, block := t060_block
  , nkb := t060_nkb, nout := 220938240
  , init := FE.zeroC
  , step := t060_g.step t060_block
  , stored := t060_g.stored t060_block }

-- t061: reducing family, 2 inputs, 110398464 outputs, reduced extent 1296
--   transposed conv3d: N=8 Cin=48 Cout=48 groups=1 k=(3, 3, 3) stride=(1, 1, 1) pad=(0, 0, 0) dil=(1, 1, 1) K=1296
def t061_g : GenRed :=
  { nout := 110398464, K := 1296
  , offs := fun b => ([(IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 13799808)) (IE.lit 48)) (IE.add (IE.mul (IE.divi (IE.modi (IE.divi (IE.pid 0) (IE.lit 287496)) (IE.lit 48)) (IE.lit 48)) (IE.lit 48)) (IE.divi IE.rk (IE.lit 27)))) (IE.lit 64)) (IE.sub (IE.modi (IE.divi (IE.pid 0) (IE.lit 4356)) (IE.lit 66)) (IE.modi (IE.divi IE.rk (IE.lit 9)) (IE.lit 3)))) (IE.lit 64)) (IE.sub (IE.modi (IE.divi (IE.pid 0) (IE.lit 66)) (IE.lit 66)) (IE.modi (IE.divi IE.rk (IE.lit 3)) (IE.lit 3)))) (IE.lit 64)) (IE.sub (IE.modi (IE.pid 0) (IE.lit 66)) (IE.modi IE.rk (IE.lit 3)))), (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.modi (IE.divi (IE.pid 0) (IE.lit 287496)) (IE.lit 48)) (IE.lit 48)) (IE.lit 48)) (IE.divi IE.rk (IE.lit 27))) (IE.lit 48)) (IE.modi (IE.modi (IE.divi (IE.pid 0) (IE.lit 287496)) (IE.lit 48)) (IE.lit 48))) (IE.lit 3)) (IE.modi (IE.divi IE.rk (IE.lit 9)) (IE.lit 3))) (IE.lit 3)) (IE.modi (IE.divi IE.rk (IE.lit 3)) (IE.lit 3))) (IE.lit 3)) (IE.modi IE.rk (IE.lit 3)))]).getD b (IE.lit 0)
  , inRange := (BE.and (BE.and (BE.and (BE.and (BE.and (BE.and (BE.and (BE.and (BE.cmp .le (IE.modi (IE.divi IE.rk (IE.lit 9)) (IE.lit 3)) (IE.modi (IE.divi (IE.pid 0) (IE.lit 4356)) (IE.lit 66))) (BE.cmp .eq (IE.lit 0) (IE.lit 0))) (BE.cmp .lt (IE.sub (IE.modi (IE.divi (IE.pid 0) (IE.lit 4356)) (IE.lit 66)) (IE.modi (IE.divi IE.rk (IE.lit 9)) (IE.lit 3))) (IE.lit 64))) (BE.cmp .le (IE.modi (IE.divi IE.rk (IE.lit 3)) (IE.lit 3)) (IE.modi (IE.divi (IE.pid 0) (IE.lit 66)) (IE.lit 66)))) (BE.cmp .eq (IE.lit 0) (IE.lit 0))) (BE.cmp .lt (IE.sub (IE.modi (IE.divi (IE.pid 0) (IE.lit 66)) (IE.lit 66)) (IE.modi (IE.divi IE.rk (IE.lit 3)) (IE.lit 3))) (IE.lit 64))) (BE.cmp .le (IE.modi IE.rk (IE.lit 3)) (IE.modi (IE.pid 0) (IE.lit 66)))) (BE.cmp .eq (IE.lit 0) (IE.lit 0))) (BE.cmp .lt (IE.sub (IE.modi (IE.pid 0) (IE.lit 66)) (IE.modi IE.rk (IE.lit 3))) (IE.lit 64)))
  , body := (SE.bin .mul (SE.inp 0) (SE.inp 1))
  , postOffs := fun b => ([(IE.lit 0), (IE.lit 0)]).getD b (IE.lit 0)
  , post := (SE.inp 0)
  , outGuard := BE.tt
  , nInp := 2 }
def t061_block : Nat := 1024
def t061_nkb : Nat := 2

/-- Index maps mention only the output and reduction indices. -/
theorem t061_wf : t061_g.Wf :=
  { offs_ok := IE.qkOnly_getD _ (by decide)
  , post_ok := IE.qkOnly_getD _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

/-- Correctness certificate for t061. -/
theorem t061_correct {α : Type} [ExactScalar α] :
    Implements (t061_g.prog t061_block t061_nkb) (t061_g.spec (α := α)) :=
  GenRed.prog_implements t061_g t061_block t061_nkb t061_wf (by decide) (by decide)

def t061_kernel : ReduceKernel :=
  { name := "t061", arity := 2, block := t061_block
  , nkb := t061_nkb, nout := 110398464
  , init := FE.zeroC
  , step := t061_g.step t061_block
  , stored := t061_g.stored t061_block }

-- t062: reducing family, 2 inputs, 131088384 outputs, reduced extent 1440
--   conv2d: N=8 Cin=32 Cout=64 groups=1 k=(5, 9) stride=(1, 1) pad=(0, 0) dil=(1, 1) K=1440
def t062_g : GenRed :=
  { nout := 131088384, K := 1440
  , offs := fun b => ([(IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 16386048)) (IE.lit 32)) (IE.divi IE.rk (IE.lit 45))) (IE.lit 512)) (IE.add (IE.modi (IE.divi (IE.pid 0) (IE.lit 504)) (IE.lit 508)) (IE.modi (IE.divi IE.rk (IE.lit 9)) (IE.lit 5)))) (IE.lit 512)) (IE.add (IE.modi (IE.pid 0) (IE.lit 504)) (IE.modi IE.rk (IE.lit 9)))), (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 256032)) (IE.lit 64)) (IE.lit 32)) (IE.divi IE.rk (IE.lit 45))) (IE.lit 5)) (IE.modi (IE.divi IE.rk (IE.lit 9)) (IE.lit 5))) (IE.lit 9)) (IE.modi IE.rk (IE.lit 9)))]).getD b (IE.lit 0)
  , inRange := (BE.and (BE.cmp .lt (IE.add (IE.modi (IE.divi (IE.pid 0) (IE.lit 504)) (IE.lit 508)) (IE.modi (IE.divi IE.rk (IE.lit 9)) (IE.lit 5))) (IE.lit 512)) (BE.cmp .lt (IE.add (IE.modi (IE.pid 0) (IE.lit 504)) (IE.modi IE.rk (IE.lit 9))) (IE.lit 512)))
  , body := (SE.bin .mul (SE.inp 0) (SE.inp 1))
  , postOffs := fun b => ([(IE.lit 0), (IE.lit 0)]).getD b (IE.lit 0)
  , post := (SE.inp 0)
  , outGuard := BE.tt
  , nInp := 2 }
def t062_block : Nat := 1024
def t062_nkb : Nat := 2

/-- Index maps mention only the output and reduction indices. -/
theorem t062_wf : t062_g.Wf :=
  { offs_ok := IE.qkOnly_getD _ (by decide)
  , post_ok := IE.qkOnly_getD _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

/-- Correctness certificate for t062. -/
theorem t062_correct {α : Type} [ExactScalar α] :
    Implements (t062_g.prog t062_block t062_nkb) (t062_g.spec (α := α)) :=
  GenRed.prog_implements t062_g t062_block t062_nkb t062_wf (by decide) (by decide)

def t062_kernel : ReduceKernel :=
  { name := "t062", arity := 2, block := t062_block
  , nkb := t062_nkb, nout := 131088384
  , init := FE.zeroC
  , step := t062_g.step t062_block
  , stored := t062_g.stored t062_block }

-- t063: reducing family, 2 inputs, 534775808 outputs, reduced extent 144
--   conv2d: N=4 Cin=16 Cout=128 groups=1 k=(3, 3) stride=(1, 1) pad=(0, 0) dil=(1, 1) K=144
def t063_g : GenRed :=
  { nout := 534775808, K := 144
  , offs := fun b => ([(IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 133693952)) (IE.lit 16)) (IE.divi IE.rk (IE.lit 9))) (IE.lit 1024)) (IE.add (IE.modi (IE.divi (IE.pid 0) (IE.lit 1022)) (IE.lit 1022)) (IE.modi (IE.divi IE.rk (IE.lit 3)) (IE.lit 3)))) (IE.lit 1024)) (IE.add (IE.modi (IE.pid 0) (IE.lit 1022)) (IE.modi IE.rk (IE.lit 3)))), (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 1044484)) (IE.lit 128)) (IE.lit 16)) (IE.divi IE.rk (IE.lit 9))) (IE.lit 3)) (IE.modi (IE.divi IE.rk (IE.lit 3)) (IE.lit 3))) (IE.lit 3)) (IE.modi IE.rk (IE.lit 3)))]).getD b (IE.lit 0)
  , inRange := (BE.and (BE.cmp .lt (IE.add (IE.modi (IE.divi (IE.pid 0) (IE.lit 1022)) (IE.lit 1022)) (IE.modi (IE.divi IE.rk (IE.lit 3)) (IE.lit 3))) (IE.lit 1024)) (BE.cmp .lt (IE.add (IE.modi (IE.pid 0) (IE.lit 1022)) (IE.modi IE.rk (IE.lit 3))) (IE.lit 1024)))
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
  , nkb := t063_nkb, nout := 534775808
  , init := FE.zeroC
  , step := t063_g.step t063_block
  , stored := t063_g.stored t063_block }

-- t064: reducing family, 2 inputs, 268443648 outputs, reduced extent 384
--   transposed conv1d: N=32 Cin=128 Cout=128 groups=1 k=(3,) stride=(1,) pad=(0,) dil=(1,) K=384
def t064_g : GenRed :=
  { nout := 268443648, K := 384
  , offs := fun b => ([(IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 8388864)) (IE.lit 128)) (IE.add (IE.mul (IE.divi (IE.modi (IE.divi (IE.pid 0) (IE.lit 65538)) (IE.lit 128)) (IE.lit 128)) (IE.lit 128)) (IE.divi IE.rk (IE.lit 3)))) (IE.lit 65536)) (IE.sub (IE.modi (IE.pid 0) (IE.lit 65538)) (IE.modi IE.rk (IE.lit 3)))), (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.modi (IE.divi (IE.pid 0) (IE.lit 65538)) (IE.lit 128)) (IE.lit 128)) (IE.lit 128)) (IE.divi IE.rk (IE.lit 3))) (IE.lit 128)) (IE.modi (IE.modi (IE.divi (IE.pid 0) (IE.lit 65538)) (IE.lit 128)) (IE.lit 128))) (IE.lit 3)) (IE.modi IE.rk (IE.lit 3)))]).getD b (IE.lit 0)
  , inRange := (BE.and (BE.and (BE.cmp .le (IE.modi IE.rk (IE.lit 3)) (IE.modi (IE.pid 0) (IE.lit 65538))) (BE.cmp .eq (IE.lit 0) (IE.lit 0))) (BE.cmp .lt (IE.sub (IE.modi (IE.pid 0) (IE.lit 65538)) (IE.modi IE.rk (IE.lit 3))) (IE.lit 65536)))
  , body := (SE.bin .mul (SE.inp 0) (SE.inp 1))
  , postOffs := fun b => ([(IE.lit 0), (IE.lit 0)]).getD b (IE.lit 0)
  , post := (SE.inp 0)
  , outGuard := BE.tt
  , nInp := 2 }
def t064_block : Nat := 256
def t064_nkb : Nat := 2

/-- Index maps mention only the output and reduction indices. -/
theorem t064_wf : t064_g.Wf :=
  { offs_ok := IE.qkOnly_getD _ (by decide)
  , post_ok := IE.qkOnly_getD _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

/-- Correctness certificate for t064. -/
theorem t064_correct {α : Type} [ExactScalar α] :
    Implements (t064_g.prog t064_block t064_nkb) (t064_g.spec (α := α)) :=
  GenRed.prog_implements t064_g t064_block t064_nkb t064_wf (by decide) (by decide)

def t064_kernel : ReduceKernel :=
  { name := "t064", arity := 2, block := t064_block
  , nkb := t064_nkb, nout := 268443648
  , init := FE.zeroC
  , step := t064_g.step t064_block
  , stored := t064_g.stored t064_block }

-- t065: reducing family, 2 inputs, 136321024 outputs, reduced extent 1344
--   transposed conv2d: N=8 Cin=64 Cout=64 groups=1 k=(3, 7) stride=(1, 1) pad=(0, 0) dil=(1, 1) K=1344
def t065_g : GenRed :=
  { nout := 136321024, K := 1344
  , offs := fun b => ([(IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 17040128)) (IE.lit 64)) (IE.add (IE.mul (IE.divi (IE.modi (IE.divi (IE.pid 0) (IE.lit 266252)) (IE.lit 64)) (IE.lit 64)) (IE.lit 64)) (IE.divi IE.rk (IE.lit 21)))) (IE.lit 512)) (IE.sub (IE.modi (IE.divi (IE.pid 0) (IE.lit 518)) (IE.lit 514)) (IE.modi (IE.divi IE.rk (IE.lit 7)) (IE.lit 3)))) (IE.lit 512)) (IE.sub (IE.modi (IE.pid 0) (IE.lit 518)) (IE.modi IE.rk (IE.lit 7)))), (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.modi (IE.divi (IE.pid 0) (IE.lit 266252)) (IE.lit 64)) (IE.lit 64)) (IE.lit 64)) (IE.divi IE.rk (IE.lit 21))) (IE.lit 64)) (IE.modi (IE.modi (IE.divi (IE.pid 0) (IE.lit 266252)) (IE.lit 64)) (IE.lit 64))) (IE.lit 3)) (IE.modi (IE.divi IE.rk (IE.lit 7)) (IE.lit 3))) (IE.lit 7)) (IE.modi IE.rk (IE.lit 7)))]).getD b (IE.lit 0)
  , inRange := (BE.and (BE.and (BE.and (BE.and (BE.and (BE.cmp .le (IE.modi (IE.divi IE.rk (IE.lit 7)) (IE.lit 3)) (IE.modi (IE.divi (IE.pid 0) (IE.lit 518)) (IE.lit 514))) (BE.cmp .eq (IE.lit 0) (IE.lit 0))) (BE.cmp .lt (IE.sub (IE.modi (IE.divi (IE.pid 0) (IE.lit 518)) (IE.lit 514)) (IE.modi (IE.divi IE.rk (IE.lit 7)) (IE.lit 3))) (IE.lit 512))) (BE.cmp .le (IE.modi IE.rk (IE.lit 7)) (IE.modi (IE.pid 0) (IE.lit 518)))) (BE.cmp .eq (IE.lit 0) (IE.lit 0))) (BE.cmp .lt (IE.sub (IE.modi (IE.pid 0) (IE.lit 518)) (IE.modi IE.rk (IE.lit 7))) (IE.lit 512)))
  , body := (SE.bin .mul (SE.inp 0) (SE.inp 1))
  , postOffs := fun b => ([(IE.lit 0), (IE.lit 0)]).getD b (IE.lit 0)
  , post := (SE.inp 0)
  , outGuard := BE.tt
  , nInp := 2 }
def t065_block : Nat := 1024
def t065_nkb : Nat := 2

/-- Index maps mention only the output and reduction indices. -/
theorem t065_wf : t065_g.Wf :=
  { offs_ok := IE.qkOnly_getD _ (by decide)
  , post_ok := IE.qkOnly_getD _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

/-- Correctness certificate for t065. -/
theorem t065_correct {α : Type} [ExactScalar α] :
    Implements (t065_g.prog t065_block t065_nkb) (t065_g.spec (α := α)) :=
  GenRed.prog_implements t065_g t065_block t065_nkb t065_wf (by decide) (by decide)

def t065_kernel : ReduceKernel :=
  { name := "t065", arity := 2, block := t065_block
  , nkb := t065_nkb, nout := 136321024
  , init := FE.zeroC
  , step := t065_g.step t065_block
  , stored := t065_g.stored t065_block }

-- t066: reducing family, 2 inputs, 108437504 outputs, reduced extent 315
--   conv3d: N=8 Cin=3 Cout=64 groups=1 k=(3, 5, 7) stride=(1, 1, 1) pad=(0, 0, 0) dil=(1, 1, 1) K=315
def t066_g : GenRed :=
  { nout := 108437504, K := 315
  , offs := fun b => ([(IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 13554688)) (IE.lit 3)) (IE.divi IE.rk (IE.lit 105))) (IE.lit 16)) (IE.add (IE.modi (IE.divi (IE.pid 0) (IE.lit 15128)) (IE.lit 14)) (IE.modi (IE.divi IE.rk (IE.lit 35)) (IE.lit 3)))) (IE.lit 128)) (IE.add (IE.modi (IE.divi (IE.pid 0) (IE.lit 122)) (IE.lit 124)) (IE.modi (IE.divi IE.rk (IE.lit 7)) (IE.lit 5)))) (IE.lit 128)) (IE.add (IE.modi (IE.pid 0) (IE.lit 122)) (IE.modi IE.rk (IE.lit 7)))), (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 211792)) (IE.lit 64)) (IE.lit 3)) (IE.divi IE.rk (IE.lit 105))) (IE.lit 3)) (IE.modi (IE.divi IE.rk (IE.lit 35)) (IE.lit 3))) (IE.lit 5)) (IE.modi (IE.divi IE.rk (IE.lit 7)) (IE.lit 5))) (IE.lit 7)) (IE.modi IE.rk (IE.lit 7)))]).getD b (IE.lit 0)
  , inRange := (BE.and (BE.and (BE.cmp .lt (IE.add (IE.modi (IE.divi (IE.pid 0) (IE.lit 15128)) (IE.lit 14)) (IE.modi (IE.divi IE.rk (IE.lit 35)) (IE.lit 3))) (IE.lit 16)) (BE.cmp .lt (IE.add (IE.modi (IE.divi (IE.pid 0) (IE.lit 122)) (IE.lit 124)) (IE.modi (IE.divi IE.rk (IE.lit 7)) (IE.lit 5))) (IE.lit 128))) (BE.cmp .lt (IE.add (IE.modi (IE.pid 0) (IE.lit 122)) (IE.modi IE.rk (IE.lit 7))) (IE.lit 128)))
  , body := (SE.bin .mul (SE.inp 0) (SE.inp 1))
  , postOffs := fun b => ([(IE.lit 0), (IE.lit 0)]).getD b (IE.lit 0)
  , post := (SE.inp 0)
  , outGuard := BE.tt
  , nInp := 2 }
def t066_block : Nat := 256
def t066_nkb : Nat := 2

/-- Index maps mention only the output and reduction indices. -/
theorem t066_wf : t066_g.Wf :=
  { offs_ok := IE.qkOnly_getD _ (by decide)
  , post_ok := IE.qkOnly_getD _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

/-- Correctness certificate for t066. -/
theorem t066_correct {α : Type} [ExactScalar α] :
    Implements (t066_g.prog t066_block t066_nkb) (t066_g.spec (α := α)) :=
  GenRed.prog_implements t066_g t066_block t066_nkb t066_wf (by decide) (by decide)

def t066_kernel : ReduceKernel :=
  { name := "t066", arity := 2, block := t066_block
  , nkb := t066_nkb, nout := 108437504
  , init := FE.zeroC
  , step := t066_g.step t066_block
  , stored := t066_g.stored t066_block }

-- t067: reducing family, 2 inputs, 268431360 outputs, reduced extent 192
--   conv1d: N=16 Cin=64 Cout=128 groups=1 k=(3,) stride=(1,) pad=(0,) dil=(1,) K=192
def t067_g : GenRed :=
  { nout := 268431360, K := 192
  , offs := fun b => ([(IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 16776960)) (IE.lit 64)) (IE.divi IE.rk (IE.lit 3))) (IE.lit 131072)) (IE.add (IE.modi (IE.pid 0) (IE.lit 131070)) (IE.modi IE.rk (IE.lit 3)))), (IE.add (IE.mul (IE.add (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 131070)) (IE.lit 128)) (IE.lit 64)) (IE.divi IE.rk (IE.lit 3))) (IE.lit 3)) (IE.modi IE.rk (IE.lit 3)))]).getD b (IE.lit 0)
  , inRange := (BE.cmp .lt (IE.add (IE.modi (IE.pid 0) (IE.lit 131070)) (IE.modi IE.rk (IE.lit 3))) (IE.lit 131072))
  , body := (SE.bin .mul (SE.inp 0) (SE.inp 1))
  , postOffs := fun b => ([(IE.lit 0), (IE.lit 0)]).getD b (IE.lit 0)
  , post := (SE.inp 0)
  , outGuard := BE.tt
  , nInp := 2 }
def t067_block : Nat := 128
def t067_nkb : Nat := 2

/-- Index maps mention only the output and reduction indices. -/
theorem t067_wf : t067_g.Wf :=
  { offs_ok := IE.qkOnly_getD _ (by decide)
  , post_ok := IE.qkOnly_getD _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

/-- Correctness certificate for t067. -/
theorem t067_correct {α : Type} [ExactScalar α] :
    Implements (t067_g.prog t067_block t067_nkb) (t067_g.spec (α := α)) :=
  GenRed.prog_implements t067_g t067_block t067_nkb t067_wf (by decide) (by decide)

def t067_kernel : ReduceKernel :=
  { name := "t067", arity := 2, block := t067_block
  , nkb := t067_nkb, nout := 268431360
  , init := FE.zeroC
  , step := t067_g.step t067_block
  , stored := t067_g.stored t067_block }

-- t068: reducing family, 2 inputs, 312508416 outputs, reduced extent 2400
--   transposed conv3d: N=16 Cin=32 Cout=64 groups=1 k=(3, 5, 5) stride=(1, 1, 1) pad=(0, 0, 0) dil=(1, 1, 1) K=2400
def t068_g : GenRed :=
  { nout := 312508416, K := 2400
  , offs := fun b => ([(IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 19531776)) (IE.lit 32)) (IE.add (IE.mul (IE.divi (IE.modi (IE.divi (IE.pid 0) (IE.lit 305184)) (IE.lit 64)) (IE.lit 64)) (IE.lit 32)) (IE.divi IE.rk (IE.lit 75)))) (IE.lit 64)) (IE.sub (IE.modi (IE.divi (IE.pid 0) (IE.lit 4624)) (IE.lit 66)) (IE.modi (IE.divi IE.rk (IE.lit 25)) (IE.lit 3)))) (IE.lit 64)) (IE.sub (IE.modi (IE.divi (IE.pid 0) (IE.lit 68)) (IE.lit 68)) (IE.modi (IE.divi IE.rk (IE.lit 5)) (IE.lit 5)))) (IE.lit 64)) (IE.sub (IE.modi (IE.pid 0) (IE.lit 68)) (IE.modi IE.rk (IE.lit 5)))), (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.modi (IE.divi (IE.pid 0) (IE.lit 305184)) (IE.lit 64)) (IE.lit 64)) (IE.lit 32)) (IE.divi IE.rk (IE.lit 75))) (IE.lit 64)) (IE.modi (IE.modi (IE.divi (IE.pid 0) (IE.lit 305184)) (IE.lit 64)) (IE.lit 64))) (IE.lit 3)) (IE.modi (IE.divi IE.rk (IE.lit 25)) (IE.lit 3))) (IE.lit 5)) (IE.modi (IE.divi IE.rk (IE.lit 5)) (IE.lit 5))) (IE.lit 5)) (IE.modi IE.rk (IE.lit 5)))]).getD b (IE.lit 0)
  , inRange := (BE.and (BE.and (BE.and (BE.and (BE.and (BE.and (BE.and (BE.and (BE.cmp .le (IE.modi (IE.divi IE.rk (IE.lit 25)) (IE.lit 3)) (IE.modi (IE.divi (IE.pid 0) (IE.lit 4624)) (IE.lit 66))) (BE.cmp .eq (IE.lit 0) (IE.lit 0))) (BE.cmp .lt (IE.sub (IE.modi (IE.divi (IE.pid 0) (IE.lit 4624)) (IE.lit 66)) (IE.modi (IE.divi IE.rk (IE.lit 25)) (IE.lit 3))) (IE.lit 64))) (BE.cmp .le (IE.modi (IE.divi IE.rk (IE.lit 5)) (IE.lit 5)) (IE.modi (IE.divi (IE.pid 0) (IE.lit 68)) (IE.lit 68)))) (BE.cmp .eq (IE.lit 0) (IE.lit 0))) (BE.cmp .lt (IE.sub (IE.modi (IE.divi (IE.pid 0) (IE.lit 68)) (IE.lit 68)) (IE.modi (IE.divi IE.rk (IE.lit 5)) (IE.lit 5))) (IE.lit 64))) (BE.cmp .le (IE.modi IE.rk (IE.lit 5)) (IE.modi (IE.pid 0) (IE.lit 68)))) (BE.cmp .eq (IE.lit 0) (IE.lit 0))) (BE.cmp .lt (IE.sub (IE.modi (IE.pid 0) (IE.lit 68)) (IE.modi IE.rk (IE.lit 5))) (IE.lit 64)))
  , body := (SE.bin .mul (SE.inp 0) (SE.inp 1))
  , postOffs := fun b => ([(IE.lit 0), (IE.lit 0)]).getD b (IE.lit 0)
  , post := (SE.inp 0)
  , outGuard := BE.tt
  , nInp := 2 }
def t068_block : Nat := 1024
def t068_nkb : Nat := 3

/-- Index maps mention only the output and reduction indices. -/
theorem t068_wf : t068_g.Wf :=
  { offs_ok := IE.qkOnly_getD _ (by decide)
  , post_ok := IE.qkOnly_getD _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

/-- Correctness certificate for t068. -/
theorem t068_correct {α : Type} [ExactScalar α] :
    Implements (t068_g.prog t068_block t068_nkb) (t068_g.spec (α := α)) :=
  GenRed.prog_implements t068_g t068_block t068_nkb t068_wf (by decide) (by decide)

def t068_kernel : ReduceKernel :=
  { name := "t068", arity := 2, block := t068_block
  , nkb := t068_nkb, nout := 312508416
  , init := FE.zeroC
  , step := t068_g.step t068_block
  , stored := t068_g.stored t068_block }

-- t069: reducing family, 2 inputs, 276889600 outputs, reduced extent 960
--   transposed conv2d: N=64 Cin=64 Cout=128 groups=1 k=(3, 5) stride=(1, 1) pad=(0, 0) dil=(1, 1) K=960
def t069_g : GenRed :=
  { nout := 276889600, K := 960
  , offs := fun b => ([(IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 4326400)) (IE.lit 64)) (IE.add (IE.mul (IE.divi (IE.modi (IE.divi (IE.pid 0) (IE.lit 33800)) (IE.lit 128)) (IE.lit 128)) (IE.lit 64)) (IE.divi IE.rk (IE.lit 15)))) (IE.lit 128)) (IE.sub (IE.modi (IE.divi (IE.pid 0) (IE.lit 260)) (IE.lit 130)) (IE.modi (IE.divi IE.rk (IE.lit 5)) (IE.lit 3)))) (IE.lit 256)) (IE.sub (IE.modi (IE.pid 0) (IE.lit 260)) (IE.modi IE.rk (IE.lit 5)))), (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.modi (IE.divi (IE.pid 0) (IE.lit 33800)) (IE.lit 128)) (IE.lit 128)) (IE.lit 64)) (IE.divi IE.rk (IE.lit 15))) (IE.lit 128)) (IE.modi (IE.modi (IE.divi (IE.pid 0) (IE.lit 33800)) (IE.lit 128)) (IE.lit 128))) (IE.lit 3)) (IE.modi (IE.divi IE.rk (IE.lit 5)) (IE.lit 3))) (IE.lit 5)) (IE.modi IE.rk (IE.lit 5)))]).getD b (IE.lit 0)
  , inRange := (BE.and (BE.and (BE.and (BE.and (BE.and (BE.cmp .le (IE.modi (IE.divi IE.rk (IE.lit 5)) (IE.lit 3)) (IE.modi (IE.divi (IE.pid 0) (IE.lit 260)) (IE.lit 130))) (BE.cmp .eq (IE.lit 0) (IE.lit 0))) (BE.cmp .lt (IE.sub (IE.modi (IE.divi (IE.pid 0) (IE.lit 260)) (IE.lit 130)) (IE.modi (IE.divi IE.rk (IE.lit 5)) (IE.lit 3))) (IE.lit 128))) (BE.cmp .le (IE.modi IE.rk (IE.lit 5)) (IE.modi (IE.pid 0) (IE.lit 260)))) (BE.cmp .eq (IE.lit 0) (IE.lit 0))) (BE.cmp .lt (IE.sub (IE.modi (IE.pid 0) (IE.lit 260)) (IE.modi IE.rk (IE.lit 5))) (IE.lit 256)))
  , body := (SE.bin .mul (SE.inp 0) (SE.inp 1))
  , postOffs := fun b => ([(IE.lit 0), (IE.lit 0)]).getD b (IE.lit 0)
  , post := (SE.inp 0)
  , outGuard := BE.tt
  , nInp := 2 }
def t069_block : Nat := 512
def t069_nkb : Nat := 2

/-- Index maps mention only the output and reduction indices. -/
theorem t069_wf : t069_g.Wf :=
  { offs_ok := IE.qkOnly_getD _ (by decide)
  , post_ok := IE.qkOnly_getD _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

/-- Correctness certificate for t069. -/
theorem t069_correct {α : Type} [ExactScalar α] :
    Implements (t069_g.prog t069_block t069_nkb) (t069_g.spec (α := α)) :=
  GenRed.prog_implements t069_g t069_block t069_nkb t069_wf (by decide) (by decide)

def t069_kernel : ReduceKernel :=
  { name := "t069", arity := 2, block := t069_block
  , nkb := t069_nkb, nout := 276889600
  , init := FE.zeroC
  , step := t069_g.step t069_block
  , stored := t069_g.stored t069_block }

-- t070: reducing family, 2 inputs, 180708864 outputs, reduced extent 1296
--   transposed conv3d: N=8 Cin=48 Cout=24 groups=1 k=(3, 3, 3) stride=(1, 1, 1) pad=(0, 0, 0) dil=(1, 1, 1) K=1296
def t070_g : GenRed :=
  { nout := 180708864, K := 1296
  , offs := fun b => ([(IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 22588608)) (IE.lit 48)) (IE.add (IE.mul (IE.divi (IE.modi (IE.divi (IE.pid 0) (IE.lit 941192)) (IE.lit 24)) (IE.lit 24)) (IE.lit 48)) (IE.divi IE.rk (IE.lit 27)))) (IE.lit 96)) (IE.sub (IE.modi (IE.divi (IE.pid 0) (IE.lit 9604)) (IE.lit 98)) (IE.modi (IE.divi IE.rk (IE.lit 9)) (IE.lit 3)))) (IE.lit 96)) (IE.sub (IE.modi (IE.divi (IE.pid 0) (IE.lit 98)) (IE.lit 98)) (IE.modi (IE.divi IE.rk (IE.lit 3)) (IE.lit 3)))) (IE.lit 96)) (IE.sub (IE.modi (IE.pid 0) (IE.lit 98)) (IE.modi IE.rk (IE.lit 3)))), (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.modi (IE.divi (IE.pid 0) (IE.lit 941192)) (IE.lit 24)) (IE.lit 24)) (IE.lit 48)) (IE.divi IE.rk (IE.lit 27))) (IE.lit 24)) (IE.modi (IE.modi (IE.divi (IE.pid 0) (IE.lit 941192)) (IE.lit 24)) (IE.lit 24))) (IE.lit 3)) (IE.modi (IE.divi IE.rk (IE.lit 9)) (IE.lit 3))) (IE.lit 3)) (IE.modi (IE.divi IE.rk (IE.lit 3)) (IE.lit 3))) (IE.lit 3)) (IE.modi IE.rk (IE.lit 3)))]).getD b (IE.lit 0)
  , inRange := (BE.and (BE.and (BE.and (BE.and (BE.and (BE.and (BE.and (BE.and (BE.cmp .le (IE.modi (IE.divi IE.rk (IE.lit 9)) (IE.lit 3)) (IE.modi (IE.divi (IE.pid 0) (IE.lit 9604)) (IE.lit 98))) (BE.cmp .eq (IE.lit 0) (IE.lit 0))) (BE.cmp .lt (IE.sub (IE.modi (IE.divi (IE.pid 0) (IE.lit 9604)) (IE.lit 98)) (IE.modi (IE.divi IE.rk (IE.lit 9)) (IE.lit 3))) (IE.lit 96))) (BE.cmp .le (IE.modi (IE.divi IE.rk (IE.lit 3)) (IE.lit 3)) (IE.modi (IE.divi (IE.pid 0) (IE.lit 98)) (IE.lit 98)))) (BE.cmp .eq (IE.lit 0) (IE.lit 0))) (BE.cmp .lt (IE.sub (IE.modi (IE.divi (IE.pid 0) (IE.lit 98)) (IE.lit 98)) (IE.modi (IE.divi IE.rk (IE.lit 3)) (IE.lit 3))) (IE.lit 96))) (BE.cmp .le (IE.modi IE.rk (IE.lit 3)) (IE.modi (IE.pid 0) (IE.lit 98)))) (BE.cmp .eq (IE.lit 0) (IE.lit 0))) (BE.cmp .lt (IE.sub (IE.modi (IE.pid 0) (IE.lit 98)) (IE.modi IE.rk (IE.lit 3))) (IE.lit 96)))
  , body := (SE.bin .mul (SE.inp 0) (SE.inp 1))
  , postOffs := fun b => ([(IE.lit 0), (IE.lit 0)]).getD b (IE.lit 0)
  , post := (SE.inp 0)
  , outGuard := BE.tt
  , nInp := 2 }
def t070_block : Nat := 1024
def t070_nkb : Nat := 2

/-- Index maps mention only the output and reduction indices. -/
theorem t070_wf : t070_g.Wf :=
  { offs_ok := IE.qkOnly_getD _ (by decide)
  , post_ok := IE.qkOnly_getD _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

/-- Correctness certificate for t070. -/
theorem t070_correct {α : Type} [ExactScalar α] :
    Implements (t070_g.prog t070_block t070_nkb) (t070_g.spec (α := α)) :=
  GenRed.prog_implements t070_g t070_block t070_nkb t070_wf (by decide) (by decide)

def t070_kernel : ReduceKernel :=
  { name := "t070", arity := 2, block := t070_block
  , nkb := t070_nkb, nout := 180708864
  , init := FE.zeroC
  , step := t070_g.step t070_block
  , stored := t070_g.stored t070_block }

-- t071: reducing family, 2 inputs, 135005184 outputs, reduced extent 288
--   transposed conv2d: N=8 Cin=32 Cout=32 groups=1 k=(3, 3) stride=(1, 1) pad=(0, 0) dil=(1, 1) K=288
def t071_g : GenRed :=
  { nout := 135005184, K := 288
  , offs := fun b => ([(IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 16875648)) (IE.lit 32)) (IE.add (IE.mul (IE.divi (IE.modi (IE.divi (IE.pid 0) (IE.lit 527364)) (IE.lit 32)) (IE.lit 32)) (IE.lit 32)) (IE.divi IE.rk (IE.lit 9)))) (IE.lit 512)) (IE.sub (IE.modi (IE.divi (IE.pid 0) (IE.lit 1026)) (IE.lit 514)) (IE.modi (IE.divi IE.rk (IE.lit 3)) (IE.lit 3)))) (IE.lit 1024)) (IE.sub (IE.modi (IE.pid 0) (IE.lit 1026)) (IE.modi IE.rk (IE.lit 3)))), (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.modi (IE.divi (IE.pid 0) (IE.lit 527364)) (IE.lit 32)) (IE.lit 32)) (IE.lit 32)) (IE.divi IE.rk (IE.lit 9))) (IE.lit 32)) (IE.modi (IE.modi (IE.divi (IE.pid 0) (IE.lit 527364)) (IE.lit 32)) (IE.lit 32))) (IE.lit 3)) (IE.modi (IE.divi IE.rk (IE.lit 3)) (IE.lit 3))) (IE.lit 3)) (IE.modi IE.rk (IE.lit 3)))]).getD b (IE.lit 0)
  , inRange := (BE.and (BE.and (BE.and (BE.and (BE.and (BE.cmp .le (IE.modi (IE.divi IE.rk (IE.lit 3)) (IE.lit 3)) (IE.modi (IE.divi (IE.pid 0) (IE.lit 1026)) (IE.lit 514))) (BE.cmp .eq (IE.lit 0) (IE.lit 0))) (BE.cmp .lt (IE.sub (IE.modi (IE.divi (IE.pid 0) (IE.lit 1026)) (IE.lit 514)) (IE.modi (IE.divi IE.rk (IE.lit 3)) (IE.lit 3))) (IE.lit 512))) (BE.cmp .le (IE.modi IE.rk (IE.lit 3)) (IE.modi (IE.pid 0) (IE.lit 1026)))) (BE.cmp .eq (IE.lit 0) (IE.lit 0))) (BE.cmp .lt (IE.sub (IE.modi (IE.pid 0) (IE.lit 1026)) (IE.modi IE.rk (IE.lit 3))) (IE.lit 1024)))
  , body := (SE.bin .mul (SE.inp 0) (SE.inp 1))
  , postOffs := fun b => ([(IE.lit 0), (IE.lit 0)]).getD b (IE.lit 0)
  , post := (SE.inp 0)
  , outGuard := BE.tt
  , nInp := 2 }
def t071_block : Nat := 256
def t071_nkb : Nat := 2

/-- Index maps mention only the output and reduction indices. -/
theorem t071_wf : t071_g.Wf :=
  { offs_ok := IE.qkOnly_getD _ (by decide)
  , post_ok := IE.qkOnly_getD _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

/-- Correctness certificate for t071. -/
theorem t071_correct {α : Type} [ExactScalar α] :
    Implements (t071_g.prog t071_block t071_nkb) (t071_g.spec (α := α)) :=
  GenRed.prog_implements t071_g t071_block t071_nkb t071_wf (by decide) (by decide)

def t071_kernel : ReduceKernel :=
  { name := "t071", arity := 2, block := t071_block
  , nkb := t071_nkb, nout := 135005184
  , init := FE.zeroC
  , step := t071_g.step t071_block
  , stored := t071_g.stored t071_block }

-- t072: reducing family, 2 inputs, 28311552 outputs, reduced extent 840
--   transposed conv3d: N=8 Cin=32 Cout=32 groups=4 k=(3, 5, 7) stride=(2, 2, 2) pad=(1, 2, 3) dil=(1, 1, 1) K=840
def t072_g : GenRed :=
  { nout := 28311552, K := 840
  , offs := fun b => ([(IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 3538944)) (IE.lit 32)) (IE.add (IE.mul (IE.divi (IE.modi (IE.divi (IE.pid 0) (IE.lit 110592)) (IE.lit 32)) (IE.lit 8)) (IE.lit 8)) (IE.divi IE.rk (IE.lit 105)))) (IE.lit 12)) (IE.divi (IE.sub (IE.add (IE.modi (IE.divi (IE.pid 0) (IE.lit 4608)) (IE.lit 24)) (IE.lit 1)) (IE.modi (IE.divi IE.rk (IE.lit 35)) (IE.lit 3))) (IE.lit 2))) (IE.lit 24)) (IE.divi (IE.sub (IE.add (IE.modi (IE.divi (IE.pid 0) (IE.lit 96)) (IE.lit 48)) (IE.lit 2)) (IE.modi (IE.divi IE.rk (IE.lit 7)) (IE.lit 5))) (IE.lit 2))) (IE.lit 48)) (IE.divi (IE.sub (IE.add (IE.modi (IE.pid 0) (IE.lit 96)) (IE.lit 3)) (IE.modi IE.rk (IE.lit 7))) (IE.lit 2))), (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.modi (IE.divi (IE.pid 0) (IE.lit 110592)) (IE.lit 32)) (IE.lit 8)) (IE.lit 8)) (IE.divi IE.rk (IE.lit 105))) (IE.lit 8)) (IE.modi (IE.modi (IE.divi (IE.pid 0) (IE.lit 110592)) (IE.lit 32)) (IE.lit 8))) (IE.lit 3)) (IE.modi (IE.divi IE.rk (IE.lit 35)) (IE.lit 3))) (IE.lit 5)) (IE.modi (IE.divi IE.rk (IE.lit 7)) (IE.lit 5))) (IE.lit 7)) (IE.modi IE.rk (IE.lit 7)))]).getD b (IE.lit 0)
  , inRange := (BE.and (BE.and (BE.and (BE.and (BE.and (BE.and (BE.and (BE.and (BE.cmp .le (IE.modi (IE.divi IE.rk (IE.lit 35)) (IE.lit 3)) (IE.add (IE.modi (IE.divi (IE.pid 0) (IE.lit 4608)) (IE.lit 24)) (IE.lit 1))) (BE.cmp .eq (IE.modi (IE.sub (IE.add (IE.modi (IE.divi (IE.pid 0) (IE.lit 4608)) (IE.lit 24)) (IE.lit 1)) (IE.modi (IE.divi IE.rk (IE.lit 35)) (IE.lit 3))) (IE.lit 2)) (IE.lit 0))) (BE.cmp .lt (IE.divi (IE.sub (IE.add (IE.modi (IE.divi (IE.pid 0) (IE.lit 4608)) (IE.lit 24)) (IE.lit 1)) (IE.modi (IE.divi IE.rk (IE.lit 35)) (IE.lit 3))) (IE.lit 2)) (IE.lit 12))) (BE.cmp .le (IE.modi (IE.divi IE.rk (IE.lit 7)) (IE.lit 5)) (IE.add (IE.modi (IE.divi (IE.pid 0) (IE.lit 96)) (IE.lit 48)) (IE.lit 2)))) (BE.cmp .eq (IE.modi (IE.sub (IE.add (IE.modi (IE.divi (IE.pid 0) (IE.lit 96)) (IE.lit 48)) (IE.lit 2)) (IE.modi (IE.divi IE.rk (IE.lit 7)) (IE.lit 5))) (IE.lit 2)) (IE.lit 0))) (BE.cmp .lt (IE.divi (IE.sub (IE.add (IE.modi (IE.divi (IE.pid 0) (IE.lit 96)) (IE.lit 48)) (IE.lit 2)) (IE.modi (IE.divi IE.rk (IE.lit 7)) (IE.lit 5))) (IE.lit 2)) (IE.lit 24))) (BE.cmp .le (IE.modi IE.rk (IE.lit 7)) (IE.add (IE.modi (IE.pid 0) (IE.lit 96)) (IE.lit 3)))) (BE.cmp .eq (IE.modi (IE.sub (IE.add (IE.modi (IE.pid 0) (IE.lit 96)) (IE.lit 3)) (IE.modi IE.rk (IE.lit 7))) (IE.lit 2)) (IE.lit 0))) (BE.cmp .lt (IE.divi (IE.sub (IE.add (IE.modi (IE.pid 0) (IE.lit 96)) (IE.lit 3)) (IE.modi IE.rk (IE.lit 7))) (IE.lit 2)) (IE.lit 48)))
  , body := (SE.bin .mul (SE.inp 0) (SE.inp 1))
  , postOffs := fun b => ([(IE.lit 0), (IE.lit 0)]).getD b (IE.lit 0)
  , post := (SE.inp 0)
  , outGuard := BE.tt
  , nInp := 2 }
def t072_block : Nat := 512
def t072_nkb : Nat := 2

/-- Index maps mention only the output and reduction indices. -/
theorem t072_wf : t072_g.Wf :=
  { offs_ok := IE.qkOnly_getD _ (by decide)
  , post_ok := IE.qkOnly_getD _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

/-- Correctness certificate for t072. -/
theorem t072_correct {α : Type} [ExactScalar α] :
    Implements (t072_g.prog t072_block t072_nkb) (t072_g.spec (α := α)) :=
  GenRed.prog_implements t072_g t072_block t072_nkb t072_wf (by decide) (by decide)

def t072_kernel : ReduceKernel :=
  { name := "t072", arity := 2, block := t072_block
  , nkb := t072_nkb, nout := 28311552
  , init := FE.zeroC
  , step := t072_g.step t072_block
  , stored := t072_g.stored t072_block }

-- t073: reducing family, 2 inputs, 261152640 outputs, reduced extent 864
--   transposed conv3d: N=4 Cin=32 Cout=32 groups=1 k=(3, 3, 3) stride=(2, 2, 2) pad=(1, 1, 1) dil=(1, 1, 1) K=864
def t073_g : GenRed :=
  { nout := 261152640, K := 864
  , offs := fun b => ([(IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 65288160)) (IE.lit 32)) (IE.add (IE.mul (IE.divi (IE.modi (IE.divi (IE.pid 0) (IE.lit 2040255)) (IE.lit 32)) (IE.lit 32)) (IE.lit 32)) (IE.divi IE.rk (IE.lit 27)))) (IE.lit 32)) (IE.divi (IE.sub (IE.add (IE.modi (IE.divi (IE.pid 0) (IE.lit 32385)) (IE.lit 63)) (IE.lit 1)) (IE.modi (IE.divi IE.rk (IE.lit 9)) (IE.lit 3))) (IE.lit 2))) (IE.lit 64)) (IE.divi (IE.sub (IE.add (IE.modi (IE.divi (IE.pid 0) (IE.lit 255)) (IE.lit 127)) (IE.lit 1)) (IE.modi (IE.divi IE.rk (IE.lit 3)) (IE.lit 3))) (IE.lit 2))) (IE.lit 128)) (IE.divi (IE.sub (IE.add (IE.modi (IE.pid 0) (IE.lit 255)) (IE.lit 1)) (IE.modi IE.rk (IE.lit 3))) (IE.lit 2))), (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.modi (IE.divi (IE.pid 0) (IE.lit 2040255)) (IE.lit 32)) (IE.lit 32)) (IE.lit 32)) (IE.divi IE.rk (IE.lit 27))) (IE.lit 32)) (IE.modi (IE.modi (IE.divi (IE.pid 0) (IE.lit 2040255)) (IE.lit 32)) (IE.lit 32))) (IE.lit 3)) (IE.modi (IE.divi IE.rk (IE.lit 9)) (IE.lit 3))) (IE.lit 3)) (IE.modi (IE.divi IE.rk (IE.lit 3)) (IE.lit 3))) (IE.lit 3)) (IE.modi IE.rk (IE.lit 3)))]).getD b (IE.lit 0)
  , inRange := (BE.and (BE.and (BE.and (BE.and (BE.and (BE.and (BE.and (BE.and (BE.cmp .le (IE.modi (IE.divi IE.rk (IE.lit 9)) (IE.lit 3)) (IE.add (IE.modi (IE.divi (IE.pid 0) (IE.lit 32385)) (IE.lit 63)) (IE.lit 1))) (BE.cmp .eq (IE.modi (IE.sub (IE.add (IE.modi (IE.divi (IE.pid 0) (IE.lit 32385)) (IE.lit 63)) (IE.lit 1)) (IE.modi (IE.divi IE.rk (IE.lit 9)) (IE.lit 3))) (IE.lit 2)) (IE.lit 0))) (BE.cmp .lt (IE.divi (IE.sub (IE.add (IE.modi (IE.divi (IE.pid 0) (IE.lit 32385)) (IE.lit 63)) (IE.lit 1)) (IE.modi (IE.divi IE.rk (IE.lit 9)) (IE.lit 3))) (IE.lit 2)) (IE.lit 32))) (BE.cmp .le (IE.modi (IE.divi IE.rk (IE.lit 3)) (IE.lit 3)) (IE.add (IE.modi (IE.divi (IE.pid 0) (IE.lit 255)) (IE.lit 127)) (IE.lit 1)))) (BE.cmp .eq (IE.modi (IE.sub (IE.add (IE.modi (IE.divi (IE.pid 0) (IE.lit 255)) (IE.lit 127)) (IE.lit 1)) (IE.modi (IE.divi IE.rk (IE.lit 3)) (IE.lit 3))) (IE.lit 2)) (IE.lit 0))) (BE.cmp .lt (IE.divi (IE.sub (IE.add (IE.modi (IE.divi (IE.pid 0) (IE.lit 255)) (IE.lit 127)) (IE.lit 1)) (IE.modi (IE.divi IE.rk (IE.lit 3)) (IE.lit 3))) (IE.lit 2)) (IE.lit 64))) (BE.cmp .le (IE.modi IE.rk (IE.lit 3)) (IE.add (IE.modi (IE.pid 0) (IE.lit 255)) (IE.lit 1)))) (BE.cmp .eq (IE.modi (IE.sub (IE.add (IE.modi (IE.pid 0) (IE.lit 255)) (IE.lit 1)) (IE.modi IE.rk (IE.lit 3))) (IE.lit 2)) (IE.lit 0))) (BE.cmp .lt (IE.divi (IE.sub (IE.add (IE.modi (IE.pid 0) (IE.lit 255)) (IE.lit 1)) (IE.modi IE.rk (IE.lit 3))) (IE.lit 2)) (IE.lit 128)))
  , body := (SE.bin .mul (SE.inp 0) (SE.inp 1))
  , postOffs := fun b => ([(IE.lit 0), (IE.lit 0)]).getD b (IE.lit 0)
  , post := (SE.inp 0)
  , outGuard := BE.tt
  , nInp := 2 }
def t073_block : Nat := 512
def t073_nkb : Nat := 2

/-- Index maps mention only the output and reduction indices. -/
theorem t073_wf : t073_g.Wf :=
  { offs_ok := IE.qkOnly_getD _ (by decide)
  , post_ok := IE.qkOnly_getD _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

/-- Correctness certificate for t073. -/
theorem t073_correct {α : Type} [ExactScalar α] :
    Implements (t073_g.prog t073_block t073_nkb) (t073_g.spec (α := α)) :=
  GenRed.prog_implements t073_g t073_block t073_nkb t073_wf (by decide) (by decide)

def t073_kernel : ReduceKernel :=
  { name := "t073", arity := 2, block := t073_block
  , nkb := t073_nkb, nout := 261152640
  , init := FE.zeroC
  , step := t073_g.step t073_block
  , stored := t073_g.stored t073_block }

-- t074: reducing family, 2 inputs, 268460032 outputs, reduced extent 160
--   transposed conv1d: N=32 Cin=32 Cout=64 groups=1 k=(5,) stride=(1,) pad=(0,) dil=(3,) K=160
def t074_g : GenRed :=
  { nout := 268460032, K := 160
  , offs := fun b => ([(IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 8389376)) (IE.lit 32)) (IE.add (IE.mul (IE.divi (IE.modi (IE.divi (IE.pid 0) (IE.lit 131084)) (IE.lit 64)) (IE.lit 64)) (IE.lit 32)) (IE.divi IE.rk (IE.lit 5)))) (IE.lit 131072)) (IE.sub (IE.modi (IE.pid 0) (IE.lit 131084)) (IE.mul (IE.modi IE.rk (IE.lit 5)) (IE.lit 3)))), (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.modi (IE.divi (IE.pid 0) (IE.lit 131084)) (IE.lit 64)) (IE.lit 64)) (IE.lit 32)) (IE.divi IE.rk (IE.lit 5))) (IE.lit 64)) (IE.modi (IE.modi (IE.divi (IE.pid 0) (IE.lit 131084)) (IE.lit 64)) (IE.lit 64))) (IE.lit 5)) (IE.modi IE.rk (IE.lit 5)))]).getD b (IE.lit 0)
  , inRange := (BE.and (BE.and (BE.cmp .le (IE.mul (IE.modi IE.rk (IE.lit 5)) (IE.lit 3)) (IE.modi (IE.pid 0) (IE.lit 131084))) (BE.cmp .eq (IE.lit 0) (IE.lit 0))) (BE.cmp .lt (IE.sub (IE.modi (IE.pid 0) (IE.lit 131084)) (IE.mul (IE.modi IE.rk (IE.lit 5)) (IE.lit 3))) (IE.lit 131072)))
  , body := (SE.bin .mul (SE.inp 0) (SE.inp 1))
  , postOffs := fun b => ([(IE.lit 0), (IE.lit 0)]).getD b (IE.lit 0)
  , post := (SE.inp 0)
  , outGuard := BE.tt
  , nInp := 2 }
def t074_block : Nat := 128
def t074_nkb : Nat := 2

/-- Index maps mention only the output and reduction indices. -/
theorem t074_wf : t074_g.Wf :=
  { offs_ok := IE.qkOnly_getD _ (by decide)
  , post_ok := IE.qkOnly_getD _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

/-- Correctness certificate for t074. -/
theorem t074_correct {α : Type} [ExactScalar α] :
    Implements (t074_g.prog t074_block t074_nkb) (t074_g.spec (α := α)) :=
  GenRed.prog_implements t074_g t074_block t074_nkb t074_wf (by decide) (by decide)

def t074_kernel : ReduceKernel :=
  { name := "t074", arity := 2, block := t074_block
  , nkb := t074_nkb, nout := 268460032
  , init := FE.zeroC
  , step := t074_g.step t074_block
  , stored := t074_g.stored t074_block }

-- t075: reducing family, 2 inputs, 201586688 outputs, reduced extent 120
--   transposed conv2d: N=16 Cin=32 Cout=64 groups=4 k=(3, 5) stride=(2, 3) pad=(1, 2) dil=(2, 1) K=120
def t075_g : GenRed :=
  { nout := 201586688, K := 120
  , offs := fun b => ([(IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 12599168)) (IE.lit 32)) (IE.add (IE.mul (IE.divi (IE.modi (IE.divi (IE.pid 0) (IE.lit 196862)) (IE.lit 64)) (IE.lit 16)) (IE.lit 8)) (IE.divi IE.rk (IE.lit 15)))) (IE.lit 128)) (IE.divi (IE.sub (IE.add (IE.modi (IE.divi (IE.pid 0) (IE.lit 766)) (IE.lit 257)) (IE.lit 1)) (IE.mul (IE.modi (IE.divi IE.rk (IE.lit 5)) (IE.lit 3)) (IE.lit 2))) (IE.lit 2))) (IE.lit 256)) (IE.divi (IE.sub (IE.add (IE.modi (IE.pid 0) (IE.lit 766)) (IE.lit 2)) (IE.modi IE.rk (IE.lit 5))) (IE.lit 3))), (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.modi (IE.divi (IE.pid 0) (IE.lit 196862)) (IE.lit 64)) (IE.lit 16)) (IE.lit 8)) (IE.divi IE.rk (IE.lit 15))) (IE.lit 16)) (IE.modi (IE.modi (IE.divi (IE.pid 0) (IE.lit 196862)) (IE.lit 64)) (IE.lit 16))) (IE.lit 3)) (IE.modi (IE.divi IE.rk (IE.lit 5)) (IE.lit 3))) (IE.lit 5)) (IE.modi IE.rk (IE.lit 5)))]).getD b (IE.lit 0)
  , inRange := (BE.and (BE.and (BE.and (BE.and (BE.and (BE.cmp .le (IE.mul (IE.modi (IE.divi IE.rk (IE.lit 5)) (IE.lit 3)) (IE.lit 2)) (IE.add (IE.modi (IE.divi (IE.pid 0) (IE.lit 766)) (IE.lit 257)) (IE.lit 1))) (BE.cmp .eq (IE.modi (IE.sub (IE.add (IE.modi (IE.divi (IE.pid 0) (IE.lit 766)) (IE.lit 257)) (IE.lit 1)) (IE.mul (IE.modi (IE.divi IE.rk (IE.lit 5)) (IE.lit 3)) (IE.lit 2))) (IE.lit 2)) (IE.lit 0))) (BE.cmp .lt (IE.divi (IE.sub (IE.add (IE.modi (IE.divi (IE.pid 0) (IE.lit 766)) (IE.lit 257)) (IE.lit 1)) (IE.mul (IE.modi (IE.divi IE.rk (IE.lit 5)) (IE.lit 3)) (IE.lit 2))) (IE.lit 2)) (IE.lit 128))) (BE.cmp .le (IE.modi IE.rk (IE.lit 5)) (IE.add (IE.modi (IE.pid 0) (IE.lit 766)) (IE.lit 2)))) (BE.cmp .eq (IE.modi (IE.sub (IE.add (IE.modi (IE.pid 0) (IE.lit 766)) (IE.lit 2)) (IE.modi IE.rk (IE.lit 5))) (IE.lit 3)) (IE.lit 0))) (BE.cmp .lt (IE.divi (IE.sub (IE.add (IE.modi (IE.pid 0) (IE.lit 766)) (IE.lit 2)) (IE.modi IE.rk (IE.lit 5))) (IE.lit 3)) (IE.lit 256)))
  , body := (SE.bin .mul (SE.inp 0) (SE.inp 1))
  , postOffs := fun b => ([(IE.lit 0), (IE.lit 0)]).getD b (IE.lit 0)
  , post := (SE.inp 0)
  , outGuard := BE.tt
  , nInp := 2 }
def t075_block : Nat := 64
def t075_nkb : Nat := 2

/-- Index maps mention only the output and reduction indices. -/
theorem t075_wf : t075_g.Wf :=
  { offs_ok := IE.qkOnly_getD _ (by decide)
  , post_ok := IE.qkOnly_getD _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

/-- Correctness certificate for t075. -/
theorem t075_correct {α : Type} [ExactScalar α] :
    Implements (t075_g.prog t075_block t075_nkb) (t075_g.spec (α := α)) :=
  GenRed.prog_implements t075_g t075_block t075_nkb t075_wf (by decide) (by decide)

def t075_kernel : ReduceKernel :=
  { name := "t075", arity := 2, block := t075_block
  , nkb := t075_nkb, nout := 201586688
  , init := FE.zeroC
  , step := t075_g.step t075_block
  , stored := t075_g.stored t075_block }

-- t076: reducing family, 2 inputs, 357904384 outputs, reduced extent 192
--   conv1d: N=16 Cin=64 Cout=128 groups=1 k=(3,) stride=(3,) pad=(0,) dil=(4,) K=192
def t076_g : GenRed :=
  { nout := 357904384, K := 192
  , offs := fun b => ([(IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 22369024)) (IE.lit 64)) (IE.divi IE.rk (IE.lit 3))) (IE.lit 524280)) (IE.add (IE.mul (IE.modi (IE.pid 0) (IE.lit 174758)) (IE.lit 3)) (IE.mul (IE.modi IE.rk (IE.lit 3)) (IE.lit 4)))), (IE.add (IE.mul (IE.add (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 174758)) (IE.lit 128)) (IE.lit 64)) (IE.divi IE.rk (IE.lit 3))) (IE.lit 3)) (IE.modi IE.rk (IE.lit 3)))]).getD b (IE.lit 0)
  , inRange := (BE.cmp .lt (IE.add (IE.mul (IE.modi (IE.pid 0) (IE.lit 174758)) (IE.lit 3)) (IE.mul (IE.modi IE.rk (IE.lit 3)) (IE.lit 4))) (IE.lit 524280))
  , body := (SE.bin .mul (SE.inp 0) (SE.inp 1))
  , postOffs := fun b => ([(IE.lit 0), (IE.lit 0)]).getD b (IE.lit 0)
  , post := (SE.inp 0)
  , outGuard := BE.tt
  , nInp := 2 }
def t076_block : Nat := 128
def t076_nkb : Nat := 2

/-- Index maps mention only the output and reduction indices. -/
theorem t076_wf : t076_g.Wf :=
  { offs_ok := IE.qkOnly_getD _ (by decide)
  , post_ok := IE.qkOnly_getD _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

/-- Correctness certificate for t076. -/
theorem t076_correct {α : Type} [ExactScalar α] :
    Implements (t076_g.prog t076_block t076_nkb) (t076_g.spec (α := α)) :=
  GenRed.prog_implements t076_g t076_block t076_nkb t076_wf (by decide) (by decide)

def t076_kernel : ReduceKernel :=
  { name := "t076", arity := 2, block := t076_block
  , nkb := t076_nkb, nout := 357904384
  , init := FE.zeroC
  , step := t076_g.step t076_block
  , stored := t076_g.stored t076_block }

-- t077: reducing family, 2 inputs, 142771200 outputs, reduced extent 864
--   transposed conv3d: N=16 Cin=32 Cout=64 groups=1 k=(3, 3, 3) stride=(2, 2, 2) pad=(1, 1, 1) dil=(2, 2, 2) K=864
def t077_g : GenRed :=
  { nout := 142771200, K := 864
  , offs := fun b => ([(IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 8923200)) (IE.lit 32)) (IE.add (IE.mul (IE.divi (IE.modi (IE.divi (IE.pid 0) (IE.lit 139425)) (IE.lit 64)) (IE.lit 64)) (IE.lit 32)) (IE.divi IE.rk (IE.lit 27)))) (IE.lit 16)) (IE.divi (IE.sub (IE.add (IE.modi (IE.divi (IE.pid 0) (IE.lit 4225)) (IE.lit 33)) (IE.lit 1)) (IE.mul (IE.modi (IE.divi IE.rk (IE.lit 9)) (IE.lit 3)) (IE.lit 2))) (IE.lit 2))) (IE.lit 32)) (IE.divi (IE.sub (IE.add (IE.modi (IE.divi (IE.pid 0) (IE.lit 65)) (IE.lit 65)) (IE.lit 1)) (IE.mul (IE.modi (IE.divi IE.rk (IE.lit 3)) (IE.lit 3)) (IE.lit 2))) (IE.lit 2))) (IE.lit 32)) (IE.divi (IE.sub (IE.add (IE.modi (IE.pid 0) (IE.lit 65)) (IE.lit 1)) (IE.mul (IE.modi IE.rk (IE.lit 3)) (IE.lit 2))) (IE.lit 2))), (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.modi (IE.divi (IE.pid 0) (IE.lit 139425)) (IE.lit 64)) (IE.lit 64)) (IE.lit 32)) (IE.divi IE.rk (IE.lit 27))) (IE.lit 64)) (IE.modi (IE.modi (IE.divi (IE.pid 0) (IE.lit 139425)) (IE.lit 64)) (IE.lit 64))) (IE.lit 3)) (IE.modi (IE.divi IE.rk (IE.lit 9)) (IE.lit 3))) (IE.lit 3)) (IE.modi (IE.divi IE.rk (IE.lit 3)) (IE.lit 3))) (IE.lit 3)) (IE.modi IE.rk (IE.lit 3)))]).getD b (IE.lit 0)
  , inRange := (BE.and (BE.and (BE.and (BE.and (BE.and (BE.and (BE.and (BE.and (BE.cmp .le (IE.mul (IE.modi (IE.divi IE.rk (IE.lit 9)) (IE.lit 3)) (IE.lit 2)) (IE.add (IE.modi (IE.divi (IE.pid 0) (IE.lit 4225)) (IE.lit 33)) (IE.lit 1))) (BE.cmp .eq (IE.modi (IE.sub (IE.add (IE.modi (IE.divi (IE.pid 0) (IE.lit 4225)) (IE.lit 33)) (IE.lit 1)) (IE.mul (IE.modi (IE.divi IE.rk (IE.lit 9)) (IE.lit 3)) (IE.lit 2))) (IE.lit 2)) (IE.lit 0))) (BE.cmp .lt (IE.divi (IE.sub (IE.add (IE.modi (IE.divi (IE.pid 0) (IE.lit 4225)) (IE.lit 33)) (IE.lit 1)) (IE.mul (IE.modi (IE.divi IE.rk (IE.lit 9)) (IE.lit 3)) (IE.lit 2))) (IE.lit 2)) (IE.lit 16))) (BE.cmp .le (IE.mul (IE.modi (IE.divi IE.rk (IE.lit 3)) (IE.lit 3)) (IE.lit 2)) (IE.add (IE.modi (IE.divi (IE.pid 0) (IE.lit 65)) (IE.lit 65)) (IE.lit 1)))) (BE.cmp .eq (IE.modi (IE.sub (IE.add (IE.modi (IE.divi (IE.pid 0) (IE.lit 65)) (IE.lit 65)) (IE.lit 1)) (IE.mul (IE.modi (IE.divi IE.rk (IE.lit 3)) (IE.lit 3)) (IE.lit 2))) (IE.lit 2)) (IE.lit 0))) (BE.cmp .lt (IE.divi (IE.sub (IE.add (IE.modi (IE.divi (IE.pid 0) (IE.lit 65)) (IE.lit 65)) (IE.lit 1)) (IE.mul (IE.modi (IE.divi IE.rk (IE.lit 3)) (IE.lit 3)) (IE.lit 2))) (IE.lit 2)) (IE.lit 32))) (BE.cmp .le (IE.mul (IE.modi IE.rk (IE.lit 3)) (IE.lit 2)) (IE.add (IE.modi (IE.pid 0) (IE.lit 65)) (IE.lit 1)))) (BE.cmp .eq (IE.modi (IE.sub (IE.add (IE.modi (IE.pid 0) (IE.lit 65)) (IE.lit 1)) (IE.mul (IE.modi IE.rk (IE.lit 3)) (IE.lit 2))) (IE.lit 2)) (IE.lit 0))) (BE.cmp .lt (IE.divi (IE.sub (IE.add (IE.modi (IE.pid 0) (IE.lit 65)) (IE.lit 1)) (IE.mul (IE.modi IE.rk (IE.lit 3)) (IE.lit 2))) (IE.lit 2)) (IE.lit 32)))
  , body := (SE.bin .mul (SE.inp 0) (SE.inp 1))
  , postOffs := fun b => ([(IE.lit 0), (IE.lit 0)]).getD b (IE.lit 0)
  , post := (SE.inp 0)
  , outGuard := BE.tt
  , nInp := 2 }
def t077_block : Nat := 512
def t077_nkb : Nat := 2

/-- Index maps mention only the output and reduction indices. -/
theorem t077_wf : t077_g.Wf :=
  { offs_ok := IE.qkOnly_getD _ (by decide)
  , post_ok := IE.qkOnly_getD _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

/-- Correctness certificate for t077. -/
theorem t077_correct {α : Type} [ExactScalar α] :
    Implements (t077_g.prog t077_block t077_nkb) (t077_g.spec (α := α)) :=
  GenRed.prog_implements t077_g t077_block t077_nkb t077_wf (by decide) (by decide)

def t077_kernel : ReduceKernel :=
  { name := "t077", arity := 2, block := t077_block
  , nkb := t077_nkb, nout := 142771200
  , init := FE.zeroC
  , step := t077_g.step t077_block
  , stored := t077_g.stored t077_block }

-- t078: reducing family, 2 inputs, 134217728 outputs, reduced extent 672
--   transposed conv2d: N=8 Cin=32 Cout=32 groups=1 k=(3, 7) stride=(1, 1) pad=(1, 3) dil=(1, 1) K=672
def t078_g : GenRed :=
  { nout := 134217728, K := 672
  , offs := fun b => ([(IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 16777216)) (IE.lit 32)) (IE.add (IE.mul (IE.divi (IE.modi (IE.divi (IE.pid 0) (IE.lit 524288)) (IE.lit 32)) (IE.lit 32)) (IE.lit 32)) (IE.divi IE.rk (IE.lit 21)))) (IE.lit 512)) (IE.sub (IE.add (IE.modi (IE.divi (IE.pid 0) (IE.lit 1024)) (IE.lit 512)) (IE.lit 1)) (IE.modi (IE.divi IE.rk (IE.lit 7)) (IE.lit 3)))) (IE.lit 1024)) (IE.sub (IE.add (IE.modi (IE.pid 0) (IE.lit 1024)) (IE.lit 3)) (IE.modi IE.rk (IE.lit 7)))), (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.modi (IE.divi (IE.pid 0) (IE.lit 524288)) (IE.lit 32)) (IE.lit 32)) (IE.lit 32)) (IE.divi IE.rk (IE.lit 21))) (IE.lit 32)) (IE.modi (IE.modi (IE.divi (IE.pid 0) (IE.lit 524288)) (IE.lit 32)) (IE.lit 32))) (IE.lit 3)) (IE.modi (IE.divi IE.rk (IE.lit 7)) (IE.lit 3))) (IE.lit 7)) (IE.modi IE.rk (IE.lit 7)))]).getD b (IE.lit 0)
  , inRange := (BE.and (BE.and (BE.and (BE.and (BE.and (BE.cmp .le (IE.modi (IE.divi IE.rk (IE.lit 7)) (IE.lit 3)) (IE.add (IE.modi (IE.divi (IE.pid 0) (IE.lit 1024)) (IE.lit 512)) (IE.lit 1))) (BE.cmp .eq (IE.lit 0) (IE.lit 0))) (BE.cmp .lt (IE.sub (IE.add (IE.modi (IE.divi (IE.pid 0) (IE.lit 1024)) (IE.lit 512)) (IE.lit 1)) (IE.modi (IE.divi IE.rk (IE.lit 7)) (IE.lit 3))) (IE.lit 512))) (BE.cmp .le (IE.modi IE.rk (IE.lit 7)) (IE.add (IE.modi (IE.pid 0) (IE.lit 1024)) (IE.lit 3)))) (BE.cmp .eq (IE.lit 0) (IE.lit 0))) (BE.cmp .lt (IE.sub (IE.add (IE.modi (IE.pid 0) (IE.lit 1024)) (IE.lit 3)) (IE.modi IE.rk (IE.lit 7))) (IE.lit 1024)))
  , body := (SE.bin .mul (SE.inp 0) (SE.inp 1))
  , postOffs := fun b => ([(IE.lit 0), (IE.lit 0)]).getD b (IE.lit 0)
  , post := (SE.inp 0)
  , outGuard := BE.tt
  , nInp := 2 }
def t078_block : Nat := 512
def t078_nkb : Nat := 2

/-- Index maps mention only the output and reduction indices. -/
theorem t078_wf : t078_g.Wf :=
  { offs_ok := IE.qkOnly_getD _ (by decide)
  , post_ok := IE.qkOnly_getD _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

/-- Correctness certificate for t078. -/
theorem t078_correct {α : Type} [ExactScalar α] :
    Implements (t078_g.prog t078_block t078_nkb) (t078_g.spec (α := α)) :=
  GenRed.prog_implements t078_g t078_block t078_nkb t078_wf (by decide) (by decide)

def t078_kernel : ReduceKernel :=
  { name := "t078", arity := 2, block := t078_block
  , nkb := t078_nkb, nout := 134217728
  , init := FE.zeroC
  , step := t078_g.step t078_block
  , stored := t078_g.stored t078_block }

-- t079: reducing family, 2 inputs, 268436480 outputs, reduced extent 96
--   transposed conv1d: N=16 Cin=32 Cout=64 groups=1 k=(3,) stride=(2,) pad=(1,) dil=(2,) K=96
def t079_g : GenRed :=
  { nout := 268436480, K := 96
  , offs := fun b => ([(IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 16777280)) (IE.lit 32)) (IE.add (IE.mul (IE.divi (IE.modi (IE.divi (IE.pid 0) (IE.lit 262145)) (IE.lit 64)) (IE.lit 64)) (IE.lit 32)) (IE.divi IE.rk (IE.lit 3)))) (IE.lit 131072)) (IE.divi (IE.sub (IE.add (IE.modi (IE.pid 0) (IE.lit 262145)) (IE.lit 1)) (IE.mul (IE.modi IE.rk (IE.lit 3)) (IE.lit 2))) (IE.lit 2))), (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.modi (IE.divi (IE.pid 0) (IE.lit 262145)) (IE.lit 64)) (IE.lit 64)) (IE.lit 32)) (IE.divi IE.rk (IE.lit 3))) (IE.lit 64)) (IE.modi (IE.modi (IE.divi (IE.pid 0) (IE.lit 262145)) (IE.lit 64)) (IE.lit 64))) (IE.lit 3)) (IE.modi IE.rk (IE.lit 3)))]).getD b (IE.lit 0)
  , inRange := (BE.and (BE.and (BE.cmp .le (IE.mul (IE.modi IE.rk (IE.lit 3)) (IE.lit 2)) (IE.add (IE.modi (IE.pid 0) (IE.lit 262145)) (IE.lit 1))) (BE.cmp .eq (IE.modi (IE.sub (IE.add (IE.modi (IE.pid 0) (IE.lit 262145)) (IE.lit 1)) (IE.mul (IE.modi IE.rk (IE.lit 3)) (IE.lit 2))) (IE.lit 2)) (IE.lit 0))) (BE.cmp .lt (IE.divi (IE.sub (IE.add (IE.modi (IE.pid 0) (IE.lit 262145)) (IE.lit 1)) (IE.mul (IE.modi IE.rk (IE.lit 3)) (IE.lit 2))) (IE.lit 2)) (IE.lit 131072)))
  , body := (SE.bin .mul (SE.inp 0) (SE.inp 1))
  , postOffs := fun b => ([(IE.lit 0), (IE.lit 0)]).getD b (IE.lit 0)
  , post := (SE.inp 0)
  , outGuard := BE.tt
  , nInp := 2 }
def t079_block : Nat := 64
def t079_nkb : Nat := 2

/-- Index maps mention only the output and reduction indices. -/
theorem t079_wf : t079_g.Wf :=
  { offs_ok := IE.qkOnly_getD _ (by decide)
  , post_ok := IE.qkOnly_getD _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

/-- Correctness certificate for t079. -/
theorem t079_correct {α : Type} [ExactScalar α] :
    Implements (t079_g.prog t079_block t079_nkb) (t079_g.spec (α := α)) :=
  GenRed.prog_implements t079_g t079_block t079_nkb t079_wf (by decide) (by decide)

def t079_kernel : ReduceKernel :=
  { name := "t079", arity := 2, block := t079_block
  , nkb := t079_nkb, nout := 268436480
  , init := FE.zeroC
  , step := t079_g.step t079_block
  , stored := t079_g.stored t079_block }

-- t080: reducing family, 2 inputs, 129007616 outputs, reduced extent 1440
--   conv2d: N=8 Cin=32 Cout=64 groups=1 k=(5, 9) stride=(1, 1) pad=(2, 4) dil=(2, 3) K=1440
def t080_g : GenRed :=
  { nout := 129007616, K := 1440
  , offs := fun b => ([(IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 16125952)) (IE.lit 32)) (IE.divi IE.rk (IE.lit 45))) (IE.lit 512)) (IE.sub (IE.add (IE.modi (IE.divi (IE.pid 0) (IE.lit 496)) (IE.lit 508)) (IE.mul (IE.modi (IE.divi IE.rk (IE.lit 9)) (IE.lit 5)) (IE.lit 2))) (IE.lit 2))) (IE.lit 512)) (IE.sub (IE.add (IE.modi (IE.pid 0) (IE.lit 496)) (IE.mul (IE.modi IE.rk (IE.lit 9)) (IE.lit 3))) (IE.lit 4))), (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 251968)) (IE.lit 64)) (IE.lit 32)) (IE.divi IE.rk (IE.lit 45))) (IE.lit 5)) (IE.modi (IE.divi IE.rk (IE.lit 9)) (IE.lit 5))) (IE.lit 9)) (IE.modi IE.rk (IE.lit 9)))]).getD b (IE.lit 0)
  , inRange := (BE.and (BE.and (BE.and (BE.cmp .le (IE.lit 2) (IE.add (IE.modi (IE.divi (IE.pid 0) (IE.lit 496)) (IE.lit 508)) (IE.mul (IE.modi (IE.divi IE.rk (IE.lit 9)) (IE.lit 5)) (IE.lit 2)))) (BE.cmp .lt (IE.add (IE.modi (IE.divi (IE.pid 0) (IE.lit 496)) (IE.lit 508)) (IE.mul (IE.modi (IE.divi IE.rk (IE.lit 9)) (IE.lit 5)) (IE.lit 2))) (IE.lit 514))) (BE.cmp .le (IE.lit 4) (IE.add (IE.modi (IE.pid 0) (IE.lit 496)) (IE.mul (IE.modi IE.rk (IE.lit 9)) (IE.lit 3))))) (BE.cmp .lt (IE.add (IE.modi (IE.pid 0) (IE.lit 496)) (IE.mul (IE.modi IE.rk (IE.lit 9)) (IE.lit 3))) (IE.lit 516)))
  , body := (SE.bin .mul (SE.inp 0) (SE.inp 1))
  , postOffs := fun b => ([(IE.lit 0), (IE.lit 0)]).getD b (IE.lit 0)
  , post := (SE.inp 0)
  , outGuard := BE.tt
  , nInp := 2 }
def t080_block : Nat := 1024
def t080_nkb : Nat := 2

/-- Index maps mention only the output and reduction indices. -/
theorem t080_wf : t080_g.Wf :=
  { offs_ok := IE.qkOnly_getD _ (by decide)
  , post_ok := IE.qkOnly_getD _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

/-- Correctness certificate for t080. -/
theorem t080_correct {α : Type} [ExactScalar α] :
    Implements (t080_g.prog t080_block t080_nkb) (t080_g.spec (α := α)) :=
  GenRed.prog_implements t080_g t080_block t080_nkb t080_wf (by decide) (by decide)

def t080_kernel : ReduceKernel :=
  { name := "t080", arity := 2, block := t080_block
  , nkb := t080_nkb, nout := 129007616
  , init := FE.zeroC
  , step := t080_g.step t080_block
  , stored := t080_g.stored t080_block }

-- t081: reducing family, 2 inputs, 207753216 outputs, reduced extent 288
--   transposed conv2d: N=16 Cin=32 Cout=64 groups=1 k=(3, 3) stride=(5, 5) pad=(1, 1) dil=(2, 2) K=288
def t081_g : GenRed :=
  { nout := 207753216, K := 288
  , offs := fun b => ([(IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 12984576)) (IE.lit 32)) (IE.add (IE.mul (IE.divi (IE.modi (IE.divi (IE.pid 0) (IE.lit 202884)) (IE.lit 64)) (IE.lit 64)) (IE.lit 32)) (IE.divi IE.rk (IE.lit 9)))) (IE.lit 64)) (IE.divi (IE.sub (IE.add (IE.modi (IE.divi (IE.pid 0) (IE.lit 638)) (IE.lit 318)) (IE.lit 1)) (IE.mul (IE.modi (IE.divi IE.rk (IE.lit 3)) (IE.lit 3)) (IE.lit 2))) (IE.lit 5))) (IE.lit 128)) (IE.divi (IE.sub (IE.add (IE.modi (IE.pid 0) (IE.lit 638)) (IE.lit 1)) (IE.mul (IE.modi IE.rk (IE.lit 3)) (IE.lit 2))) (IE.lit 5))), (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.modi (IE.divi (IE.pid 0) (IE.lit 202884)) (IE.lit 64)) (IE.lit 64)) (IE.lit 32)) (IE.divi IE.rk (IE.lit 9))) (IE.lit 64)) (IE.modi (IE.modi (IE.divi (IE.pid 0) (IE.lit 202884)) (IE.lit 64)) (IE.lit 64))) (IE.lit 3)) (IE.modi (IE.divi IE.rk (IE.lit 3)) (IE.lit 3))) (IE.lit 3)) (IE.modi IE.rk (IE.lit 3)))]).getD b (IE.lit 0)
  , inRange := (BE.and (BE.and (BE.and (BE.and (BE.and (BE.cmp .le (IE.mul (IE.modi (IE.divi IE.rk (IE.lit 3)) (IE.lit 3)) (IE.lit 2)) (IE.add (IE.modi (IE.divi (IE.pid 0) (IE.lit 638)) (IE.lit 318)) (IE.lit 1))) (BE.cmp .eq (IE.modi (IE.sub (IE.add (IE.modi (IE.divi (IE.pid 0) (IE.lit 638)) (IE.lit 318)) (IE.lit 1)) (IE.mul (IE.modi (IE.divi IE.rk (IE.lit 3)) (IE.lit 3)) (IE.lit 2))) (IE.lit 5)) (IE.lit 0))) (BE.cmp .lt (IE.divi (IE.sub (IE.add (IE.modi (IE.divi (IE.pid 0) (IE.lit 638)) (IE.lit 318)) (IE.lit 1)) (IE.mul (IE.modi (IE.divi IE.rk (IE.lit 3)) (IE.lit 3)) (IE.lit 2))) (IE.lit 5)) (IE.lit 64))) (BE.cmp .le (IE.mul (IE.modi IE.rk (IE.lit 3)) (IE.lit 2)) (IE.add (IE.modi (IE.pid 0) (IE.lit 638)) (IE.lit 1)))) (BE.cmp .eq (IE.modi (IE.sub (IE.add (IE.modi (IE.pid 0) (IE.lit 638)) (IE.lit 1)) (IE.mul (IE.modi IE.rk (IE.lit 3)) (IE.lit 2))) (IE.lit 5)) (IE.lit 0))) (BE.cmp .lt (IE.divi (IE.sub (IE.add (IE.modi (IE.pid 0) (IE.lit 638)) (IE.lit 1)) (IE.mul (IE.modi IE.rk (IE.lit 3)) (IE.lit 2))) (IE.lit 5)) (IE.lit 128)))
  , body := (SE.bin .mul (SE.inp 0) (SE.inp 1))
  , postOffs := fun b => ([(IE.lit 0), (IE.lit 0)]).getD b (IE.lit 0)
  , post := (SE.inp 0)
  , outGuard := BE.tt
  , nInp := 2 }
def t081_block : Nat := 256
def t081_nkb : Nat := 2

/-- Index maps mention only the output and reduction indices. -/
theorem t081_wf : t081_g.Wf :=
  { offs_ok := IE.qkOnly_getD _ (by decide)
  , post_ok := IE.qkOnly_getD _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

/-- Correctness certificate for t081. -/
theorem t081_correct {α : Type} [ExactScalar α] :
    Implements (t081_g.prog t081_block t081_nkb) (t081_g.spec (α := α)) :=
  GenRed.prog_implements t081_g t081_block t081_nkb t081_wf (by decide) (by decide)

def t081_kernel : ReduceKernel :=
  { name := "t081", arity := 2, block := t081_block
  , nkb := t081_nkb, nout := 207753216
  , init := FE.zeroC
  , step := t081_g.step t081_block
  , stored := t081_g.stored t081_block }

-- t082: reducing family, 2 inputs, 266342400 outputs, reduced extent 9
--   conv2d: N=16 Cin=64 Cout=64 groups=64 k=(3, 3) stride=(1, 1) pad=(0, 0) dil=(1, 1) K=9
def t082_g : GenRed :=
  { nout := 266342400, K := 9
  , offs := fun b => ([(IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 16646400)) (IE.lit 64)) (IE.modi (IE.divi (IE.pid 0) (IE.lit 260100)) (IE.lit 64))) (IE.lit 512)) (IE.add (IE.modi (IE.divi (IE.pid 0) (IE.lit 510)) (IE.lit 510)) (IE.modi (IE.divi IE.rk (IE.lit 3)) (IE.lit 3)))) (IE.lit 512)) (IE.add (IE.modi (IE.pid 0) (IE.lit 510)) (IE.modi IE.rk (IE.lit 3)))), (IE.add (IE.mul (IE.add (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 260100)) (IE.lit 64)) (IE.lit 3)) (IE.modi (IE.divi IE.rk (IE.lit 3)) (IE.lit 3))) (IE.lit 3)) (IE.modi IE.rk (IE.lit 3)))]).getD b (IE.lit 0)
  , inRange := (BE.and (BE.cmp .lt (IE.add (IE.modi (IE.divi (IE.pid 0) (IE.lit 510)) (IE.lit 510)) (IE.modi (IE.divi IE.rk (IE.lit 3)) (IE.lit 3))) (IE.lit 512)) (BE.cmp .lt (IE.add (IE.modi (IE.pid 0) (IE.lit 510)) (IE.modi IE.rk (IE.lit 3))) (IE.lit 512)))
  , body := (SE.bin .mul (SE.inp 0) (SE.inp 1))
  , postOffs := fun b => ([(IE.lit 0), (IE.lit 0)]).getD b (IE.lit 0)
  , post := (SE.inp 0)
  , outGuard := BE.tt
  , nInp := 2 }
def t082_block : Nat := 8
def t082_nkb : Nat := 2

/-- Index maps mention only the output and reduction indices. -/
theorem t082_wf : t082_g.Wf :=
  { offs_ok := IE.qkOnly_getD _ (by decide)
  , post_ok := IE.qkOnly_getD _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

/-- Correctness certificate for t082. -/
theorem t082_correct {α : Type} [ExactScalar α] :
    Implements (t082_g.prog t082_block t082_nkb) (t082_g.spec (α := α)) :=
  GenRed.prog_implements t082_g t082_block t082_nkb t082_wf (by decide) (by decide)

def t082_kernel : ReduceKernel :=
  { name := "t082", arity := 2, block := t082_block
  , nkb := t082_nkb, nout := 266342400
  , init := FE.zeroC
  , step := t082_g.step t082_block
  , stored := t082_g.stored t082_block }

-- t083: reducing family, 2 inputs, 133693440 outputs, reduced extent 3
--   conv2d: N=64 Cin=8 Cout=8 groups=8 k=(3, 1) stride=(1, 1) pad=(0, 0) dil=(1, 1) K=3
def t083_g : GenRed :=
  { nout := 133693440, K := 3
  , offs := fun b => ([(IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 2088960)) (IE.lit 8)) (IE.modi (IE.divi (IE.pid 0) (IE.lit 261120)) (IE.lit 8))) (IE.lit 512)) (IE.add (IE.modi (IE.divi (IE.pid 0) (IE.lit 512)) (IE.lit 510)) (IE.modi IE.rk (IE.lit 3)))) (IE.lit 512)) (IE.modi (IE.pid 0) (IE.lit 512))), (IE.add (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 261120)) (IE.lit 8)) (IE.lit 3)) (IE.modi IE.rk (IE.lit 3)))]).getD b (IE.lit 0)
  , inRange := (BE.and (BE.cmp .lt (IE.add (IE.modi (IE.divi (IE.pid 0) (IE.lit 512)) (IE.lit 510)) (IE.modi IE.rk (IE.lit 3))) (IE.lit 512)) (BE.cmp .lt (IE.modi (IE.pid 0) (IE.lit 512)) (IE.lit 512)))
  , body := (SE.bin .mul (SE.inp 0) (SE.inp 1))
  , postOffs := fun b => ([(IE.lit 0), (IE.lit 0)]).getD b (IE.lit 0)
  , post := (SE.inp 0)
  , outGuard := BE.tt
  , nInp := 2 }
def t083_block : Nat := 2
def t083_nkb : Nat := 2

/-- Index maps mention only the output and reduction indices. -/
theorem t083_wf : t083_g.Wf :=
  { offs_ok := IE.qkOnly_getD _ (by decide)
  , post_ok := IE.qkOnly_getD _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

/-- Correctness certificate for t083. -/
theorem t083_correct {α : Type} [ExactScalar α] :
    Implements (t083_g.prog t083_block t083_nkb) (t083_g.spec (α := α)) :=
  GenRed.prog_implements t083_g t083_block t083_nkb t083_wf (by decide) (by decide)

def t083_kernel : ReduceKernel :=
  { name := "t083", arity := 2, block := t083_block
  , nkb := t083_nkb, nout := 133693440
  , init := FE.zeroC
  , step := t083_g.step t083_block
  , stored := t083_g.stored t083_block }

-- t084: reducing family, 2 inputs, 265297920 outputs, reduced extent 9
--   conv2d: N=16 Cin=128 Cout=128 groups=128 k=(3, 3) stride=(1, 1) pad=(0, 0) dil=(1, 1) K=9
def t084_g : GenRed :=
  { nout := 265297920, K := 9
  , offs := fun b => ([(IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 16581120)) (IE.lit 128)) (IE.modi (IE.divi (IE.pid 0) (IE.lit 129540)) (IE.lit 128))) (IE.lit 256)) (IE.add (IE.modi (IE.divi (IE.pid 0) (IE.lit 510)) (IE.lit 254)) (IE.modi (IE.divi IE.rk (IE.lit 3)) (IE.lit 3)))) (IE.lit 512)) (IE.add (IE.modi (IE.pid 0) (IE.lit 510)) (IE.modi IE.rk (IE.lit 3)))), (IE.add (IE.mul (IE.add (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 129540)) (IE.lit 128)) (IE.lit 3)) (IE.modi (IE.divi IE.rk (IE.lit 3)) (IE.lit 3))) (IE.lit 3)) (IE.modi IE.rk (IE.lit 3)))]).getD b (IE.lit 0)
  , inRange := (BE.and (BE.cmp .lt (IE.add (IE.modi (IE.divi (IE.pid 0) (IE.lit 510)) (IE.lit 254)) (IE.modi (IE.divi IE.rk (IE.lit 3)) (IE.lit 3))) (IE.lit 256)) (BE.cmp .lt (IE.add (IE.modi (IE.pid 0) (IE.lit 510)) (IE.modi IE.rk (IE.lit 3))) (IE.lit 512)))
  , body := (SE.bin .mul (SE.inp 0) (SE.inp 1))
  , postOffs := fun b => ([(IE.lit 0), (IE.lit 0)]).getD b (IE.lit 0)
  , post := (SE.inp 0)
  , outGuard := BE.tt
  , nInp := 2 }
def t084_block : Nat := 8
def t084_nkb : Nat := 2

/-- Index maps mention only the output and reduction indices. -/
theorem t084_wf : t084_g.Wf :=
  { offs_ok := IE.qkOnly_getD _ (by decide)
  , post_ok := IE.qkOnly_getD _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

/-- Correctness certificate for t084. -/
theorem t084_correct {α : Type} [ExactScalar α] :
    Implements (t084_g.prog t084_block t084_nkb) (t084_g.spec (α := α)) :=
  GenRed.prog_implements t084_g t084_block t084_nkb t084_wf (by decide) (by decide)

def t084_kernel : ReduceKernel :=
  { name := "t084", arity := 2, block := t084_block
  , nkb := t084_nkb, nout := 265297920
  , init := FE.zeroC
  , step := t084_g.step t084_block
  , stored := t084_g.stored t084_block }

-- t085: reducing family, 2 inputs, 129024000 outputs, reduced extent 21
--   conv2d: N=32 Cin=128 Cout=128 groups=128 k=(3, 7) stride=(1, 1) pad=(0, 0) dil=(1, 1) K=21
def t085_g : GenRed :=
  { nout := 129024000, K := 21
  , offs := fun b => ([(IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 4032000)) (IE.lit 128)) (IE.modi (IE.divi (IE.pid 0) (IE.lit 31500)) (IE.lit 128))) (IE.lit 128)) (IE.add (IE.modi (IE.divi (IE.pid 0) (IE.lit 250)) (IE.lit 126)) (IE.modi (IE.divi IE.rk (IE.lit 7)) (IE.lit 3)))) (IE.lit 256)) (IE.add (IE.modi (IE.pid 0) (IE.lit 250)) (IE.modi IE.rk (IE.lit 7)))), (IE.add (IE.mul (IE.add (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 31500)) (IE.lit 128)) (IE.lit 3)) (IE.modi (IE.divi IE.rk (IE.lit 7)) (IE.lit 3))) (IE.lit 7)) (IE.modi IE.rk (IE.lit 7)))]).getD b (IE.lit 0)
  , inRange := (BE.and (BE.cmp .lt (IE.add (IE.modi (IE.divi (IE.pid 0) (IE.lit 250)) (IE.lit 126)) (IE.modi (IE.divi IE.rk (IE.lit 7)) (IE.lit 3))) (IE.lit 128)) (BE.cmp .lt (IE.add (IE.modi (IE.pid 0) (IE.lit 250)) (IE.modi IE.rk (IE.lit 7))) (IE.lit 256)))
  , body := (SE.bin .mul (SE.inp 0) (SE.inp 1))
  , postOffs := fun b => ([(IE.lit 0), (IE.lit 0)]).getD b (IE.lit 0)
  , post := (SE.inp 0)
  , outGuard := BE.tt
  , nInp := 2 }
def t085_block : Nat := 16
def t085_nkb : Nat := 2

/-- Index maps mention only the output and reduction indices. -/
theorem t085_wf : t085_g.Wf :=
  { offs_ok := IE.qkOnly_getD _ (by decide)
  , post_ok := IE.qkOnly_getD _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

/-- Correctness certificate for t085. -/
theorem t085_correct {α : Type} [ExactScalar α] :
    Implements (t085_g.prog t085_block t085_nkb) (t085_g.spec (α := α)) :=
  GenRed.prog_implements t085_g t085_block t085_nkb t085_wf (by decide) (by decide)

def t085_kernel : ReduceKernel :=
  { name := "t085", arity := 2, block := t085_block
  , nkb := t085_nkb, nout := 129024000
  , init := FE.zeroC
  , step := t085_g.step t085_block
  , stored := t085_g.stored t085_block }

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

-- t087: reducing family, 2 inputs, 268435456 outputs, reduced extent 64
--   conv2d: N=2 Cin=64 Cout=128 groups=1 k=(1, 1) stride=(1, 1) pad=(0, 0) dil=(1, 1) K=64
def t087_g : GenRed :=
  { nout := 268435456, K := 64
  , offs := fun b => ([(IE.add (IE.mul (IE.add (IE.mul (IE.add (IE.mul (IE.divi (IE.pid 0) (IE.lit 134217728)) (IE.lit 64)) IE.rk) (IE.lit 1024)) (IE.modi (IE.divi (IE.pid 0) (IE.lit 1024)) (IE.lit 1024))) (IE.lit 1024)) (IE.modi (IE.pid 0) (IE.lit 1024))), (IE.add (IE.mul (IE.modi (IE.divi (IE.pid 0) (IE.lit 1048576)) (IE.lit 128)) (IE.lit 64)) IE.rk)]).getD b (IE.lit 0)
  , inRange := (BE.and (BE.cmp .lt (IE.modi (IE.divi (IE.pid 0) (IE.lit 1024)) (IE.lit 1024)) (IE.lit 1024)) (BE.cmp .lt (IE.modi (IE.pid 0) (IE.lit 1024)) (IE.lit 1024)))
  , body := (SE.bin .mul (SE.inp 0) (SE.inp 1))
  , postOffs := fun b => ([(IE.lit 0), (IE.lit 0)]).getD b (IE.lit 0)
  , post := (SE.inp 0)
  , outGuard := BE.tt
  , nInp := 2 }
def t087_block : Nat := 64
def t087_nkb : Nat := 1

/-- Index maps mention only the output and reduction indices. -/
theorem t087_wf : t087_g.Wf :=
  { offs_ok := IE.qkOnly_getD _ (by decide)
  , post_ok := IE.qkOnly_getD _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

/-- Correctness certificate for t087. -/
theorem t087_correct {α : Type} [ExactScalar α] :
    Implements (t087_g.prog t087_block t087_nkb) (t087_g.spec (α := α)) :=
  GenRed.prog_implements t087_g t087_block t087_nkb t087_wf (by decide) (by decide)

def t087_kernel : ReduceKernel :=
  { name := "t087", arity := 2, block := t087_block
  , nkb := t087_nkb, nout := 268435456
  , init := FE.zeroC
  , step := t087_g.step t087_block
  , stored := t087_g.stored t087_block }

-- t088: pointwise, arity 1, 67108864 outputs
def t088_se : SE := (SE.bin .mul (SE.bin .mul (SE.lit false 1 2) (SE.inp 0)) (SE.bin .add (SE.lit false 1 1) (SE.un .tanh (SE.bin .mul (SE.lit false 354576841927535 444396168752463) (SE.bin .add (SE.inp 0) (SE.bin .mul (SE.lit false 8943 200000) (SE.bin .mul (SE.bin .mul (SE.inp 0) (SE.inp 0)) (SE.inp 0))))))))
def t088_block : Nat := 1024
def t088_n : Nat := 67108864
def t088_nblocks : Nat := 65536
def t088_kernel : FlatKernel :=
  { name := "t088", arity := 1, block := t088_block
  , n := t088_n, nblocks := t088_nblocks
  , val := SE.toFE t088_block t088_n t088_se }

/-- Correctness certificate for t088. -/
theorem t088_correct {α : Type} [ExactScalar α] :
    Implements (Prog.flat1d t088_nblocks t088_block t088_n
                 (SE.toFE t088_block t088_n t088_se))
               (SE.spec (α := α) t088_se 1 t088_n) :=
  SE.flat_correct 1 t088_se (by decide) (by decide)

-- t094: two-stage pipeline, 2 input(s), 4096-element intermediate at buffer 2
--   reduce over dim None of (16384, 32768) (inputs [(16384, 32768), (16384, 32768)]): outer=1 K=536870912 inner=1; tree reduction: 536870912 elements -> 4096 partials
def t094_s1_g : GenRed :=
  { nout := 4096, K := 131072
  , offs := fun b => ([(IE.add (IE.mul (IE.divi (IE.add (IE.mul (IE.pid 0) (IE.lit 131072)) IE.rk) (IE.lit 32768)) (IE.lit 32768)) (IE.modi (IE.add (IE.mul (IE.pid 0) (IE.lit 131072)) IE.rk) (IE.lit 32768))), (IE.add (IE.mul (IE.divi (IE.add (IE.mul (IE.pid 0) (IE.lit 131072)) IE.rk) (IE.lit 32768)) (IE.lit 32768)) (IE.modi (IE.add (IE.mul (IE.pid 0) (IE.lit 131072)) IE.rk) (IE.lit 32768)))]).getD b (IE.lit 0)
  , inRange := (BE.cmp .lt (IE.add (IE.mul (IE.pid 0) (IE.lit 131072)) IE.rk) (IE.lit 536870912))
  , body := (SE.bin .mul (SE.bin .sub (SE.inp 0) (SE.inp 1)) (SE.bin .sub (SE.inp 0) (SE.inp 1)))
  , postOffs := fun b => ([(IE.lit 0), (IE.lit 0)]).getD b (IE.lit 0)
  , post := (SE.inp 0)
  , outGuard := BE.tt
  , nInp := 2 }
def t094_s1_block : Nat := 1024
def t094_s1_nkb : Nat := 128

theorem t094_s1_wf : t094_s1_g.Wf :=
  { offs_ok := IE.qkOnly_getD _ (by decide)
  , post_ok := IE.qkOnly_getD _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

theorem t094_s1_impl {α : Type} [ExactScalar α] :
    Implements (t094_s1_g.prog t094_s1_block t094_s1_nkb) (t094_s1_g.spec (α := α)) :=
  GenRed.prog_implements t094_s1_g t094_s1_block t094_s1_nkb t094_s1_wf (by decide) (by decide)

def t094_s2_g : GenRed :=
  { nout := 1, K := 4096
  , offs := fun b => ([(IE.lit 0), (IE.lit 0), IE.rk]).getD b (IE.lit 0)
  , inRange := BE.tt
  , body := (SE.inp 2)
  , postOffs := fun b => ([(IE.lit 0), (IE.lit 0), (IE.lit 0)]).getD b (IE.lit 0)
  , post := (SE.bin .mul (SE.inp 0) (SE.lit false 1 536870912))
  , outGuard := BE.tt
  , nInp := 3 }
def t094_s2_block : Nat := 1024
def t094_s2_nkb : Nat := 4

theorem t094_s2_wf : t094_s2_g.Wf :=
  { offs_ok := IE.qkOnly_getD _ (by decide)
  , post_ok := IE.qkOnly_getD _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

theorem t094_s2_impl {α : Type} [ExactScalar α] :
    Implements (t094_s2_g.prog t094_s2_block t094_s2_nkb) (t094_s2_g.spec (α := α)) :=
  GenRed.prog_implements t094_s2_g t094_s2_block t094_s2_nkb t094_s2_wf (by decide) (by decide)

/-- Stage 2 reads the intermediate only where stage 1 wrote it. -/
theorem t094_loc {α : Type} [ExactScalar α] :
    ∀ (bufs : Nat → Buf α) (u v : Buf α),
      (∀ i, i < (t094_s1_g.spec (α := α)).outSize → u i = v i) →
      ∀ q, q < (t094_s2_g.spec (α := α)).outSize →
        (t094_s2_g.spec (α := α)).out (subst bufs 2 u) q
          = (t094_s2_g.spec (α := α)).out (subst bufs 2 v) q :=
  GenRed.spec_locality t094_s2_g 2 4096
    (fun _ k _ hk => hk)
    (fun _ _ => (by decide : (0 : Nat) < 4096))

/-- Correctness certificate for t094: the composed pipeline. -/
theorem t094_correct {α : Type} [ExactScalar α] :
    ∀ (bufs : Nat → Buf α) (m1 m2 : Mem α) (q : Nat),
      q < (t094_s2_g.spec (α := α)).outSize →
      runTwo (t094_s1_g.prog t094_s1_block t094_s1_nkb)
             (t094_s2_g.prog t094_s2_block t094_s2_nkb) 2 bufs m1 m2 q
        = (t094_s2_g.spec (α := α)).out
            (subst bufs 2 (fun i => (t094_s1_g.spec (α := α)).out bufs i)) q :=
  two_stage t094_s1_impl t094_s2_impl t094_loc

def t094_s1_kernel : ReduceKernel :=
  { name := "t094_s1", arity := 2, block := t094_s1_block, nkb := t094_s1_nkb, nout := 4096, init := FE.zeroC, step := t094_s1_g.step t094_s1_block, stored := t094_s1_g.stored t094_s1_block }
def t094_s2_kernel : ReduceKernel :=
  { name := "t094_s2", arity := 3, block := t094_s2_block, nkb := t094_s2_nkb, nout := 1, init := FE.zeroC, step := t094_s2_g.step t094_s2_block, stored := t094_s2_g.stored t094_s2_block }
def t094_kernel : PipelineKernel :=
  { name := "t094", arity := 2, n1 := 4096, stage1 := t094_s1_kernel, stage2 := t094_s2_kernel }

-- t096: two-stage pipeline, 2 input(s), 4096-element intermediate at buffer 2
--   reduce over dim None of (16384, 32768) (inputs [(16384, 32768), (16384, 32768)]): outer=1 K=536870912 inner=1; tree reduction: 536870912 elements -> 4096 partials
def t096_s1_g : GenRed :=
  { nout := 4096, K := 131072
  , offs := fun b => ([(IE.add (IE.mul (IE.divi (IE.add (IE.mul (IE.pid 0) (IE.lit 131072)) IE.rk) (IE.lit 32768)) (IE.lit 32768)) (IE.modi (IE.add (IE.mul (IE.pid 0) (IE.lit 131072)) IE.rk) (IE.lit 32768))), (IE.add (IE.mul (IE.divi (IE.add (IE.mul (IE.pid 0) (IE.lit 131072)) IE.rk) (IE.lit 32768)) (IE.lit 32768)) (IE.modi (IE.add (IE.mul (IE.pid 0) (IE.lit 131072)) IE.rk) (IE.lit 32768)))]).getD b (IE.lit 0)
  , inRange := (BE.cmp .lt (IE.add (IE.mul (IE.pid 0) (IE.lit 131072)) IE.rk) (IE.lit 536870912))
  , body := (SE.selLe (SE.un .abs (SE.bin .sub (SE.inp 0) (SE.inp 1))) (SE.lit false 1 1) (SE.bin .div (SE.bin .mul (SE.bin .mul (SE.lit false 1 2) (SE.un .abs (SE.bin .sub (SE.inp 0) (SE.inp 1)))) (SE.un .abs (SE.bin .sub (SE.inp 0) (SE.inp 1)))) (SE.lit false 1 1)) (SE.bin .sub (SE.un .abs (SE.bin .sub (SE.inp 0) (SE.inp 1))) (SE.lit false 1 2)))
  , postOffs := fun b => ([(IE.lit 0), (IE.lit 0)]).getD b (IE.lit 0)
  , post := (SE.inp 0)
  , outGuard := BE.tt
  , nInp := 2 }
def t096_s1_block : Nat := 1024
def t096_s1_nkb : Nat := 128

theorem t096_s1_wf : t096_s1_g.Wf :=
  { offs_ok := IE.qkOnly_getD _ (by decide)
  , post_ok := IE.qkOnly_getD _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

theorem t096_s1_impl {α : Type} [ExactScalar α] :
    Implements (t096_s1_g.prog t096_s1_block t096_s1_nkb) (t096_s1_g.spec (α := α)) :=
  GenRed.prog_implements t096_s1_g t096_s1_block t096_s1_nkb t096_s1_wf (by decide) (by decide)

def t096_s2_g : GenRed :=
  { nout := 1, K := 4096
  , offs := fun b => ([(IE.lit 0), (IE.lit 0), IE.rk]).getD b (IE.lit 0)
  , inRange := BE.tt
  , body := (SE.inp 2)
  , postOffs := fun b => ([(IE.lit 0), (IE.lit 0), (IE.lit 0)]).getD b (IE.lit 0)
  , post := (SE.bin .mul (SE.inp 0) (SE.lit false 1 536870912))
  , outGuard := BE.tt
  , nInp := 3 }
def t096_s2_block : Nat := 1024
def t096_s2_nkb : Nat := 4

theorem t096_s2_wf : t096_s2_g.Wf :=
  { offs_ok := IE.qkOnly_getD _ (by decide)
  , post_ok := IE.qkOnly_getD _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

theorem t096_s2_impl {α : Type} [ExactScalar α] :
    Implements (t096_s2_g.prog t096_s2_block t096_s2_nkb) (t096_s2_g.spec (α := α)) :=
  GenRed.prog_implements t096_s2_g t096_s2_block t096_s2_nkb t096_s2_wf (by decide) (by decide)

/-- Stage 2 reads the intermediate only where stage 1 wrote it. -/
theorem t096_loc {α : Type} [ExactScalar α] :
    ∀ (bufs : Nat → Buf α) (u v : Buf α),
      (∀ i, i < (t096_s1_g.spec (α := α)).outSize → u i = v i) →
      ∀ q, q < (t096_s2_g.spec (α := α)).outSize →
        (t096_s2_g.spec (α := α)).out (subst bufs 2 u) q
          = (t096_s2_g.spec (α := α)).out (subst bufs 2 v) q :=
  GenRed.spec_locality t096_s2_g 2 4096
    (fun _ k _ hk => hk)
    (fun _ _ => (by decide : (0 : Nat) < 4096))

/-- Correctness certificate for t096: the composed pipeline. -/
theorem t096_correct {α : Type} [ExactScalar α] :
    ∀ (bufs : Nat → Buf α) (m1 m2 : Mem α) (q : Nat),
      q < (t096_s2_g.spec (α := α)).outSize →
      runTwo (t096_s1_g.prog t096_s1_block t096_s1_nkb)
             (t096_s2_g.prog t096_s2_block t096_s2_nkb) 2 bufs m1 m2 q
        = (t096_s2_g.spec (α := α)).out
            (subst bufs 2 (fun i => (t096_s1_g.spec (α := α)).out bufs i)) q :=
  two_stage t096_s1_impl t096_s2_impl t096_loc

def t096_s1_kernel : ReduceKernel :=
  { name := "t096_s1", arity := 2, block := t096_s1_block, nkb := t096_s1_nkb, nout := 4096, init := FE.zeroC, step := t096_s1_g.step t096_s1_block, stored := t096_s1_g.stored t096_s1_block }
def t096_s2_kernel : ReduceKernel :=
  { name := "t096_s2", arity := 3, block := t096_s2_block, nkb := t096_s2_nkb, nout := 1, init := FE.zeroC, step := t096_s2_g.step t096_s2_block, stored := t096_s2_g.stored t096_s2_block }
def t096_kernel : PipelineKernel :=
  { name := "t096", arity := 2, n1 := 4096, stage1 := t096_s1_kernel, stage2 := t096_s2_kernel }

-- t098: two-stage pipeline, 2 input(s), 4096-element intermediate at buffer 2
--   reduce over dim None of (16384, 16384) (inputs [(16384, 16384), (16384, 16384)]): outer=1 K=268435456 inner=1; tree reduction: 268435456 elements -> 4096 partials
def t098_s1_g : GenRed :=
  { nout := 4096, K := 65536
  , offs := fun b => ([(IE.add (IE.mul (IE.divi (IE.add (IE.mul (IE.pid 0) (IE.lit 65536)) IE.rk) (IE.lit 16384)) (IE.lit 16384)) (IE.modi (IE.add (IE.mul (IE.pid 0) (IE.lit 65536)) IE.rk) (IE.lit 16384))), (IE.add (IE.mul (IE.divi (IE.add (IE.mul (IE.pid 0) (IE.lit 65536)) IE.rk) (IE.lit 16384)) (IE.lit 16384)) (IE.modi (IE.add (IE.mul (IE.pid 0) (IE.lit 65536)) IE.rk) (IE.lit 16384)))]).getD b (IE.lit 0)
  , inRange := (BE.cmp .lt (IE.add (IE.mul (IE.pid 0) (IE.lit 65536)) IE.rk) (IE.lit 268435456))
  , body := (SE.bin .mul (SE.inp 1) (SE.bin .sub (SE.un .log (SE.inp 1)) (SE.un .log (SE.inp 0))))
  , postOffs := fun b => ([(IE.lit 0), (IE.lit 0)]).getD b (IE.lit 0)
  , post := (SE.inp 0)
  , outGuard := BE.tt
  , nInp := 2 }
def t098_s1_block : Nat := 1024
def t098_s1_nkb : Nat := 64

theorem t098_s1_wf : t098_s1_g.Wf :=
  { offs_ok := IE.qkOnly_getD _ (by decide)
  , post_ok := IE.qkOnly_getD _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

theorem t098_s1_impl {α : Type} [ExactScalar α] :
    Implements (t098_s1_g.prog t098_s1_block t098_s1_nkb) (t098_s1_g.spec (α := α)) :=
  GenRed.prog_implements t098_s1_g t098_s1_block t098_s1_nkb t098_s1_wf (by decide) (by decide)

def t098_s2_g : GenRed :=
  { nout := 1, K := 4096
  , offs := fun b => ([(IE.lit 0), (IE.lit 0), IE.rk]).getD b (IE.lit 0)
  , inRange := BE.tt
  , body := (SE.inp 2)
  , postOffs := fun b => ([(IE.lit 0), (IE.lit 0), (IE.lit 0)]).getD b (IE.lit 0)
  , post := (SE.bin .mul (SE.inp 0) (SE.lit false 1 16384))
  , outGuard := BE.tt
  , nInp := 3 }
def t098_s2_block : Nat := 1024
def t098_s2_nkb : Nat := 4

theorem t098_s2_wf : t098_s2_g.Wf :=
  { offs_ok := IE.qkOnly_getD _ (by decide)
  , post_ok := IE.qkOnly_getD _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

theorem t098_s2_impl {α : Type} [ExactScalar α] :
    Implements (t098_s2_g.prog t098_s2_block t098_s2_nkb) (t098_s2_g.spec (α := α)) :=
  GenRed.prog_implements t098_s2_g t098_s2_block t098_s2_nkb t098_s2_wf (by decide) (by decide)

/-- Stage 2 reads the intermediate only where stage 1 wrote it. -/
theorem t098_loc {α : Type} [ExactScalar α] :
    ∀ (bufs : Nat → Buf α) (u v : Buf α),
      (∀ i, i < (t098_s1_g.spec (α := α)).outSize → u i = v i) →
      ∀ q, q < (t098_s2_g.spec (α := α)).outSize →
        (t098_s2_g.spec (α := α)).out (subst bufs 2 u) q
          = (t098_s2_g.spec (α := α)).out (subst bufs 2 v) q :=
  GenRed.spec_locality t098_s2_g 2 4096
    (fun _ k _ hk => hk)
    (fun _ _ => (by decide : (0 : Nat) < 4096))

/-- Correctness certificate for t098: the composed pipeline. -/
theorem t098_correct {α : Type} [ExactScalar α] :
    ∀ (bufs : Nat → Buf α) (m1 m2 : Mem α) (q : Nat),
      q < (t098_s2_g.spec (α := α)).outSize →
      runTwo (t098_s1_g.prog t098_s1_block t098_s1_nkb)
             (t098_s2_g.prog t098_s2_block t098_s2_nkb) 2 bufs m1 m2 q
        = (t098_s2_g.spec (α := α)).out
            (subst bufs 2 (fun i => (t098_s1_g.spec (α := α)).out bufs i)) q :=
  two_stage t098_s1_impl t098_s2_impl t098_loc

def t098_s1_kernel : ReduceKernel :=
  { name := "t098_s1", arity := 2, block := t098_s1_block, nkb := t098_s1_nkb, nout := 4096, init := FE.zeroC, step := t098_s1_g.step t098_s1_block, stored := t098_s1_g.stored t098_s1_block }
def t098_s2_kernel : ReduceKernel :=
  { name := "t098_s2", arity := 3, block := t098_s2_block, nkb := t098_s2_nkb, nout := 1, init := FE.zeroC, step := t098_s2_g.step t098_s2_block, stored := t098_s2_g.stored t098_s2_block }
def t098_kernel : PipelineKernel :=
  { name := "t098", arity := 2, n1 := 4096, stage1 := t098_s1_kernel, stage2 := t098_s2_kernel }

-- t099: three-stage normalisation, 3 input buffer(s), intermediates 32768 and 32768 at buffers 3 and 4
--   triplet margin loss: batch 32768, 8192 features, margin=1.0, eps=1e-06
def t099_s1_g : GenRed :=
  { nout := 32768, K := 8192
  , offs := fun b => ([(IE.add (IE.mul (IE.pid 0) (IE.lit 8192)) IE.rk), (IE.add (IE.mul (IE.pid 0) (IE.lit 8192)) IE.rk), (IE.lit 0), (IE.lit 0), (IE.lit 0)]).getD b (IE.lit 0)
  , inRange := BE.tt
  , body := (SE.bin .mul (SE.bin .add (SE.bin .sub (SE.inp 0) (SE.inp 1)) (SE.lit false 1 1000000)) (SE.bin .add (SE.bin .sub (SE.inp 0) (SE.inp 1)) (SE.lit false 1 1000000)))
  , postOffs := fun b => ([(IE.lit 0), (IE.lit 0), (IE.lit 0), (IE.lit 0), (IE.lit 0)]).getD b (IE.lit 0)
  , post := (SE.inp 0)
  , outGuard := BE.tt
  , nInp := 3 }
def t099_s1_block : Nat := 1024
def t099_s1_nkb : Nat := 8

theorem t099_s1_wf : t099_s1_g.Wf :=
  { offs_ok := IE.qkOnly_getD _ (by decide)
  , post_ok := IE.qkOnly_getD _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

theorem t099_s1_impl {α : Type} [ExactScalar α] :
    Implements (t099_s1_g.prog t099_s1_block t099_s1_nkb) (t099_s1_g.spec (α := α)) :=
  GenRed.prog_implements t099_s1_g t099_s1_block t099_s1_nkb t099_s1_wf (by decide) (by decide)

def t099_s2_g : GenRed :=
  { nout := 32768, K := 8192
  , offs := fun b => ([(IE.add (IE.mul (IE.pid 0) (IE.lit 8192)) IE.rk), (IE.lit 0), (IE.add (IE.mul (IE.pid 0) (IE.lit 8192)) IE.rk), (IE.lit 0), (IE.lit 0)]).getD b (IE.lit 0)
  , inRange := BE.tt
  , body := (SE.bin .mul (SE.bin .add (SE.bin .sub (SE.inp 0) (SE.inp 2)) (SE.lit false 1 1000000)) (SE.bin .add (SE.bin .sub (SE.inp 0) (SE.inp 2)) (SE.lit false 1 1000000)))
  , postOffs := fun b => ([(IE.lit 0), (IE.lit 0), (IE.lit 0), (IE.lit 0), (IE.lit 0)]).getD b (IE.lit 0)
  , post := (SE.inp 0)
  , outGuard := BE.tt
  , nInp := 4 }
def t099_s2_block : Nat := 1024
def t099_s2_nkb : Nat := 8

theorem t099_s2_wf : t099_s2_g.Wf :=
  { offs_ok := IE.qkOnly_getD _ (by decide)
  , post_ok := IE.qkOnly_getD _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

theorem t099_s2_impl {α : Type} [ExactScalar α] :
    Implements (t099_s2_g.prog t099_s2_block t099_s2_nkb) (t099_s2_g.spec (α := α)) :=
  GenRed.prog_implements t099_s2_g t099_s2_block t099_s2_nkb t099_s2_wf (by decide) (by decide)

def t099_s3_g : GenRed :=
  { nout := 1, K := 32768
  , offs := fun b => ([(IE.lit 0), (IE.lit 0), (IE.lit 0), IE.rk, IE.rk]).getD b (IE.lit 0)
  , inRange := BE.tt
  , body := (SE.bin .max (SE.bin .add (SE.bin .sub (SE.un .sqrt (SE.inp 3)) (SE.un .sqrt (SE.inp 4))) (SE.lit false 1 1)) (SE.lit false 0 1))
  , postOffs := fun b => ([(IE.lit 0), (IE.lit 0), (IE.lit 0), (IE.lit 0), (IE.lit 0)]).getD b (IE.lit 0)
  , post := (SE.bin .mul (SE.inp 0) (SE.lit false 1 32768))
  , outGuard := BE.tt
  , nInp := 5 }
def t099_s3_block : Nat := 1024
def t099_s3_nkb : Nat := 32

theorem t099_s3_wf : t099_s3_g.Wf :=
  { offs_ok := IE.qkOnly_getD _ (by decide)
  , post_ok := IE.qkOnly_getD _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

theorem t099_s3_impl {α : Type} [ExactScalar α] :
    Implements (t099_s3_g.prog t099_s3_block t099_s3_nkb) (t099_s3_g.spec (α := α)) :=
  GenRed.prog_implements t099_s3_g t099_s3_block t099_s3_nkb t099_s3_wf (by decide) (by decide)

/-- Stage 2 reads the first intermediate only where stage 1 wrote it. -/
theorem t099_l2 {α : Type} [ExactScalar α] :
    Loc (t099_s2_g.spec (α := α)) 3 32768 :=
  GenRed.loc t099_s2_g 3 32768 (fun _ _ _ _ => (by decide : (0 : Nat) < 32768)) (fun _ _ => (by decide : (0 : Nat) < 32768))

/-- Stage 3 reads each intermediate only where its stage wrote it. -/
theorem t099_l3a {α : Type} [ExactScalar α] :
    Loc (t099_s3_g.spec (α := α)) 3 32768 :=
  GenRed.loc t099_s3_g 3 32768 (fun _ k _ hk => hk) (fun _ _ => (by decide : (0 : Nat) < 32768))

theorem t099_l3b {α : Type} [ExactScalar α] :
    Loc (t099_s3_g.spec (α := α)) 4 32768 :=
  GenRed.loc t099_s3_g 4 32768 (fun _ k _ hk => hk) (fun _ _ => (by decide : (0 : Nat) < 32768))

/-- Correctness certificate for t099: the composed three-stage pipeline. -/
theorem t099_correct {α : Type} [ExactScalar α] :
    ∀ (bufs : Nat → Buf α) (m1 m2 m3 : Mem α) (q : Nat),
      q < (t099_s3_g.spec (α := α)).outSize →
      runThree (t099_s1_g.prog t099_s1_block t099_s1_nkb)
               (t099_s2_g.prog t099_s2_block t099_s2_nkb)
               (t099_s3_g.prog t099_s3_block t099_s3_nkb) 3 4 bufs m1 m2 m3 q
        = compose3 (t099_s1_g.spec (α := α)) (t099_s2_g.spec (α := α))
            (t099_s3_g.spec (α := α)) 3 4 bufs q :=
  three_stage (by decide) t099_s1_impl t099_s2_impl t099_s3_impl t099_l2 t099_l3a t099_l3b

def t099_s1_kernel : ReduceKernel :=
  { name := "t099_s1", arity := 3, block := t099_s1_block, nkb := t099_s1_nkb, nout := 32768, init := FE.zeroC, step := t099_s1_g.step t099_s1_block, stored := t099_s1_g.stored t099_s1_block }
def t099_s2_kernel : ReduceKernel :=
  { name := "t099_s2", arity := 4, block := t099_s2_block, nkb := t099_s2_nkb, nout := 32768, init := FE.zeroC, step := t099_s2_g.step t099_s2_block, stored := t099_s2_g.stored t099_s2_block }
def t099_s3_kernel : ReduceKernel :=
  { name := "t099_s3", arity := 5, block := t099_s3_block, nkb := t099_s3_nkb, nout := 1, init := FE.zeroC, step := t099_s3_g.step t099_s3_block, stored := t099_s3_g.stored t099_s3_block }
def t099_kernel : PipelineKernel3 :=
  { name := "t099", arity := 3, n1 := 32768, n2 := 32768, stage1 := t099_s1_kernel, stage2 := t099_s2_kernel, stage3 := t099_s3_kernel }

-- t100: two-stage pipeline, 2 input(s), 4096-element intermediate at buffer 2
--   reduce over dim None of (32768, 32768) (inputs [(32768, 32768), (32768,)]): outer=1 K=1073741824 inner=1; tree reduction: 1073741824 elements -> 4096 partials
def t100_s1_g : GenRed :=
  { nout := 4096, K := 262144
  , offs := fun b => ([(IE.add (IE.mul (IE.divi (IE.add (IE.mul (IE.pid 0) (IE.lit 262144)) IE.rk) (IE.lit 32768)) (IE.lit 32768)) (IE.modi (IE.add (IE.mul (IE.pid 0) (IE.lit 262144)) IE.rk) (IE.lit 32768))), (IE.modi (IE.add (IE.mul (IE.pid 0) (IE.lit 262144)) IE.rk) (IE.lit 32768))]).getD b (IE.lit 0)
  , inRange := (BE.cmp .lt (IE.add (IE.mul (IE.pid 0) (IE.lit 262144)) IE.rk) (IE.lit 1073741824))
  , body := (SE.bin .max (SE.bin .sub (SE.lit false 1 1) (SE.bin .mul (SE.inp 0) (SE.inp 1))) (SE.lit false 0 1))
  , postOffs := fun b => ([(IE.lit 0), (IE.lit 0)]).getD b (IE.lit 0)
  , post := (SE.inp 0)
  , outGuard := BE.tt
  , nInp := 2 }
def t100_s1_block : Nat := 1024
def t100_s1_nkb : Nat := 256

theorem t100_s1_wf : t100_s1_g.Wf :=
  { offs_ok := IE.qkOnly_getD _ (by decide)
  , post_ok := IE.qkOnly_getD _ (by decide)
  , range_ok := by decide
  , guard_ok := by decide }

theorem t100_s1_impl {α : Type} [ExactScalar α] :
    Implements (t100_s1_g.prog t100_s1_block t100_s1_nkb) (t100_s1_g.spec (α := α)) :=
  GenRed.prog_implements t100_s1_g t100_s1_block t100_s1_nkb t100_s1_wf (by decide) (by decide)

def t100_s2_g : GenRed :=
  { nout := 1, K := 4096
  , offs := fun b => ([(IE.lit 0), (IE.lit 0), IE.rk]).getD b (IE.lit 0)
  , inRange := BE.tt
  , body := (SE.inp 2)
  , postOffs := fun b => ([(IE.lit 0), (IE.lit 0), (IE.lit 0)]).getD b (IE.lit 0)
  , post := (SE.bin .mul (SE.inp 0) (SE.lit false 1 1073741824))
  , outGuard := BE.tt
  , nInp := 3 }
def t100_s2_block : Nat := 1024
def t100_s2_nkb : Nat := 4

theorem t100_s2_wf : t100_s2_g.Wf :=
  { offs_ok := IE.qkOnly_getD _ (by decide)
  , post_ok := IE.qkOnly_getD _ (by decide)
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
  IO.FS.writeFile "../generated/t001.py" t001_kernel.render
  IO.FS.writeFile "../generated/t002.py" t002_kernel.render
  IO.FS.writeFile "../generated/t003.py" t003_kernel.render
  IO.FS.writeFile "../generated/t004.py" t004_kernel.render
  IO.FS.writeFile "../generated/t005.py" t005_kernel.render
  IO.FS.writeFile "../generated/t006.py" t006_kernel.render
  IO.FS.writeFile "../generated/t007.py" t007_kernel.render
  IO.FS.writeFile "../generated/t008.py" t008_kernel.render
  IO.FS.writeFile "../generated/t009.py" t009_kernel.render
  IO.FS.writeFile "../generated/t010.py" t010_kernel.render
  IO.FS.writeFile "../generated/t011.py" t011_kernel.render
  IO.FS.writeFile "../generated/t012.py" t012_kernel.render
  IO.FS.writeFile "../generated/t013.py" t013_kernel.render
  IO.FS.writeFile "../generated/t014.py" t014_kernel.render
  IO.FS.writeFile "../generated/t015.py" t015_kernel.render
  IO.FS.writeFile "../generated/t016.py" t016_kernel.render
  IO.FS.writeFile "../generated/t017.py" t017_kernel.render
  IO.FS.writeFile "../generated/t018.py" t018_kernel.render
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
  IO.FS.writeFile "../generated/t033.py" t033_kernel.render
  IO.FS.writeFile "../generated/t034.py" t034_kernel.render
  IO.FS.writeFile "../generated/t035.py" t035_kernel.render
  IO.FS.writeFile "../generated/t036.py" t036_kernel.render
  IO.FS.writeFile "../generated/t037.py" t037_kernel.render
  IO.FS.writeFile "../generated/t038.py" t038_kernel.render
  IO.FS.writeFile "../generated/t039.py" t039_kernel.render
  IO.FS.writeFile "../generated/t040.py" t040_kernel.render
  IO.FS.writeFile "../generated/t041.py" t041_kernel.render
  IO.FS.writeFile "../generated/t042.py" t042_kernel.render
  IO.FS.writeFile "../generated/t043.py" t043_kernel.render
  IO.FS.writeFile "../generated/t044.py" t044_kernel.render
  IO.FS.writeFile "../generated/t045.py" t045_kernel.render
  IO.FS.writeFile "../generated/t046.py" t046_kernel.render
  IO.FS.writeFile "../generated/t047.py" t047_kernel.render
  IO.FS.writeFile "../generated/t048.py" t048_kernel.render
  IO.FS.writeFile "../generated/t049.py" t049_kernel.render
  IO.FS.writeFile "../generated/t050.py" t050_kernel.render
  IO.FS.writeFile "../generated/t053.py" t053_kernel.render
  IO.FS.writeFile "../generated/t054.py" t054_kernel.render
  IO.FS.writeFile "../generated/t055.py" t055_kernel.render
  IO.FS.writeFile "../generated/t056.py" t056_kernel.render
  IO.FS.writeFile "../generated/t057.py" t057_kernel.render
  IO.FS.writeFile "../generated/t058.py" t058_kernel.render
  IO.FS.writeFile "../generated/t059.py" t059_kernel.render
  IO.FS.writeFile "../generated/t060.py" t060_kernel.render
  IO.FS.writeFile "../generated/t061.py" t061_kernel.render
  IO.FS.writeFile "../generated/t062.py" t062_kernel.render
  IO.FS.writeFile "../generated/t063.py" t063_kernel.render
  IO.FS.writeFile "../generated/t064.py" t064_kernel.render
  IO.FS.writeFile "../generated/t065.py" t065_kernel.render
  IO.FS.writeFile "../generated/t066.py" t066_kernel.render
  IO.FS.writeFile "../generated/t067.py" t067_kernel.render
  IO.FS.writeFile "../generated/t068.py" t068_kernel.render
  IO.FS.writeFile "../generated/t069.py" t069_kernel.render
  IO.FS.writeFile "../generated/t070.py" t070_kernel.render
  IO.FS.writeFile "../generated/t071.py" t071_kernel.render
  IO.FS.writeFile "../generated/t072.py" t072_kernel.render
  IO.FS.writeFile "../generated/t073.py" t073_kernel.render
  IO.FS.writeFile "../generated/t074.py" t074_kernel.render
  IO.FS.writeFile "../generated/t075.py" t075_kernel.render
  IO.FS.writeFile "../generated/t076.py" t076_kernel.render
  IO.FS.writeFile "../generated/t077.py" t077_kernel.render
  IO.FS.writeFile "../generated/t078.py" t078_kernel.render
  IO.FS.writeFile "../generated/t079.py" t079_kernel.render
  IO.FS.writeFile "../generated/t080.py" t080_kernel.render
  IO.FS.writeFile "../generated/t081.py" t081_kernel.render
  IO.FS.writeFile "../generated/t082.py" t082_kernel.render
  IO.FS.writeFile "../generated/t083.py" t083_kernel.render
  IO.FS.writeFile "../generated/t084.py" t084_kernel.render
  IO.FS.writeFile "../generated/t085.py" t085_kernel.render
  IO.FS.writeFile "../generated/t086.py" t086_kernel.render
  IO.FS.writeFile "../generated/t087.py" t087_kernel.render
  IO.FS.writeFile "../generated/t088.py" t088_kernel.render
  IO.FS.writeFile "../generated/t094.py" t094_kernel.render
  IO.FS.writeFile "../generated/t096.py" t096_kernel.render
  IO.FS.writeFile "../generated/t098.py" t098_kernel.render
  IO.FS.writeFile "../generated/t099.py" t099_kernel.render
  IO.FS.writeFile "../generated/t100.py" t100_kernel.render
