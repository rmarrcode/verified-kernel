/-
`TritonIR`: a deeply embedded, tile-level IR for Triton kernels, with a
denotational semantics as a pure Lean function.

Central design choice: a tile expression denotes a *function of a tile
coordinate*, `⟦e⟧ env i j : α`. Consequences, all of them good:

  * Broadcasting, `expand_dims` and `reshape` vanish. `tl.arange(0,R)[:,None]`
    is just `row`, and a scalar is a constant function. Whole classes of
    shape-plumbing bugs cannot be expressed, and the proofs never mention them.
  * `dot` and `reduce` are the only non-pointwise nodes, and each is simply a
    binder over one coordinate: `⟦dot k a b⟧ env i j = ∑_{p<k} a i p * b p j`.
  * Masking is a `Bool`-valued expression at the same coordinate, so a proof
    that a boundary is handled correctly is a proof about one predicate.

Memory is written by an explicit fold over tile coordinates, mirroring hardware,
rather than by an existential reverse lookup. That makes the semantics
computable and forces the *coverage* obligation (every output element written
exactly once) to be discharged rather than assumed.
-/
import VerifiedKernel.Tensor

namespace VerifiedKernel

open ExactScalar

/-! ## Operators -/

inductive Cmp | lt | le | eq | ne
  deriving DecidableEq, Repr, Inhabited

inductive Bop | add | mul | sub | div | max | min
  deriving DecidableEq, Repr, Inhabited

inductive RedOp | sum | prod | max | min
  deriving DecidableEq, Repr, Inhabited

/-! ## Expressions -/

/-- Index-valued tile expressions: offsets, bounds, loop arithmetic.
Evaluated at a tile coordinate; `row` and `col` are that coordinate. -/
inductive IE where
  /-- `tl.program_id(axis)` -/
  | pid (axis : Nat)
  /-- the tile's row coordinate (`tl.arange(0,R)[:, None]`) -/
  | row
  /-- the tile's column coordinate (`tl.arange(0,C)[None, :]`) -/
  | col
  | lit (n : Nat)
  /-- counter of an enclosing loop, by de Bruijn level (0 = innermost) -/
  | iv (k : Nat)
  /-- **the reduction index**: a placeholder standing for `k` in a family's index
  map. A spec reads it directly; the backend substitutes the lane/step
  decomposition `iv 0 * block + col` for it (see `IE.instK`). Kernel-position
  expressions never contain it, so its `eval` below is arbitrary. -/
  | rk
  | add (a b : IE) | mul (a b : IE) | sub (a b : IE)
  | divi (a b : IE) | modi (a b : IE)
  deriving Repr, Inhabited

/-- Mask expressions. -/
inductive BE where
  | tt
  | cmp (c : Cmp) (a b : IE)
  | and (a b : BE) | or (a b : BE) | not (a : BE)
  deriving Repr, Inhabited

/-- Scalar-valued tile expressions.

Closed: no `α` appears in the syntax. Constants are built from `ofI`/`recip` as
exact rationals and masked loads always substitute zero, so a term of this type
is pure data that the backend can render to Triton source. -/
inductive FE where
  /-- the additive identity -/
  | zeroC
  /-- the multiplicative identity, which a masked-off lane of a *product*
  contributes -- the role `zeroC` plays for a sum -/
  | oneC
  /-- reinterpret an index expression as a scalar (`i.to(tl.float32)`) -/
  | ofI (e : IE)
  /-- `tl.load(buf + off, mask=mask, other=0.0)` -/
  | load (buf : Nat) (off : IE) (mask : BE)
  | bin (op : Bop) (a b : FE)
  | un (f : Fn1) (a : FE)
  | recip (a : FE)
  /-- `tl.where(c, a, b)` with an index-valued condition -/
  | sel (c : BE) (a b : FE)
  /-- `tl.where(a <= b, t, e)` -- a *scalar*-valued condition, needed for
  piecewise activations (ELU, HardSigmoid, HardTanh, Huber) that cannot be
  written with `max`/`min` alone -/
  | selLe (a b t e : FE)
  /-- an enclosing accumulator, by de Bruijn level -/
  | acc (k : Nat)
  /-- `tl.dot(a, b)` contracting `kdim`: `⟦·⟧ i j = ∑_{p<kdim} a i p * b p j` -/
  | dot (kdim : Nat) (a b : FE)
  /-- reduce `a` along its column axis over `n` lanes; result is independent of
  the column coordinate -/
  | redCol (op : RedOp) (n : Nat) (a : FE)
  /-- reduce `a` along its row axis over `n` lanes -/
  | redRow (op : RedOp) (n : Nat) (a : FE)
  deriving Inhabited

/-! ## Statements -/

inductive Stmt where
  | skip
  | seq (a b : Stmt)
  /-- `tl.store(out + off, val, mask=mask)` over a `rows × cols` tile. -/
  | store (rows cols : Nat) (off : IE) (val : FE) (mask : BE)
  /-- An accumulator loop. `acc` starts at `init`; for `k = 0 .. n-1` it becomes
  `step` evaluated with `iv 0 = k` and `acc 0` the running value. `body` then
  runs with the final accumulator bound at `acc 0`. This is the shape of every
  tiled reduction, and its semantics is a `Nat.rec`, so the corresponding proof
  is a straightforward induction with an invariant. -/
  | forAcc (n : Nat) (init : FE) (step : FE) (body : Stmt)

/-- A kernel: a 1-D or 2-D launch grid and a body. -/
structure Prog where
  grid0 : Nat
  grid1 : Nat
  body  : Stmt

/-! ## Environments -/

/-- Evaluation environment. `ivs` and `accs` are de Bruijn stacks. -/
structure Env (α : Type) where
  pid  : Nat → Nat
  ivs  : Nat → Nat
  accs : Nat → (Nat → Nat → α)
  bufs : Nat → Buf α

namespace Env
variable {α : Type}

def pushIv (e : Env α) (k : Nat) : Env α :=
  { e with ivs := fun n => match n with | 0 => k | n+1 => e.ivs n }

def pushAcc (e : Env α) (v : Nat → Nat → α) : Env α :=
  { e with accs := fun n => match n with | 0 => v | n+1 => e.accs n }

@[simp] theorem pushIv_bufs (e : Env α) (k : Nat) : (e.pushIv k).bufs = e.bufs := rfl
@[simp] theorem pushAcc_bufs (e : Env α) (v : Nat → Nat → α) :
    (e.pushAcc v).bufs = e.bufs := rfl
@[simp] theorem pushAcc_pid (e : Env α) (v : Nat → Nat → α) :
    (e.pushAcc v).pid = e.pid := rfl
@[simp] theorem pushAcc_ivs (e : Env α) (v : Nat → Nat → α) :
    (e.pushAcc v).ivs = e.ivs := rfl

/-- Push both, as `forAcc`'s step expression sees them. -/
def pushStep (e : Env α) (k : Nat) (v : Nat → Nat → α) : Env α :=
  (e.pushIv k).pushAcc v

@[simp] theorem pushStep_bufs (e : Env α) (k : Nat) (v : Nat → Nat → α) :
    (e.pushStep k v).bufs = e.bufs := rfl
@[simp] theorem pushStep_pid (e : Env α) (k : Nat) (v : Nat → Nat → α) :
    (e.pushStep k v).pid = e.pid := rfl
@[simp] theorem pushStep_ivs0 (e : Env α) (k : Nat) (v : Nat → Nat → α) :
    (e.pushStep k v).ivs 0 = k := rfl

end Env

/-! ## Semantics -/

/-- `⟦e⟧ env i j` -- index expressions. Natural subtraction is truncating, which
matches nothing in Triton; `sub` is therefore only emitted where the framework
has proved the difference non-negative. -/
def IE.eval (env : Env α) (i j : Nat) : IE → Nat
  | .pid a => env.pid a
  | .row => i
  | .col => j
  | .lit n => n
  | .iv k => env.ivs k
  | .rk => 0
  | .add a b => a.eval env i j + b.eval env i j
  | .mul a b => a.eval env i j * b.eval env i j
  | .sub a b => a.eval env i j - b.eval env i j
  | .divi a b => a.eval env i j / b.eval env i j
  | .modi a b => a.eval env i j % b.eval env i j

def Cmp.apply : Cmp → Nat → Nat → Bool
  | .lt, a, b => a < b
  | .le, a, b => a ≤ b
  | .eq, a, b => a == b
  | .ne, a, b => a != b

def BE.eval (env : Env α) (i j : Nat) : BE → Bool
  | .tt => true
  | .cmp c a b => c.apply (a.eval env i j) (b.eval env i j)
  | .and a b => a.eval env i j && b.eval env i j
  | .or a b => a.eval env i j || b.eval env i j
  | .not a => !(a.eval env i j)

variable {α : Type} [ExactScalar α]

def Bop.apply : Bop → α → α → α
  | .add, a, b => ExactScalar.add a b
  | .mul, a, b => ExactScalar.mul a b
  | .sub, a, b => ExactScalar.sub a b
  | .div, a, b => ExactScalar.div a b
  | .max, a, b => ExactScalar.max a b
  | .min, a, b => ExactScalar.min a b

/-- The identity element of a reduction. `max`/`min` have no identity in an
unbounded ordered field, so their folds are seeded with the first lane; see
`RedOp.fold`. -/
def RedOp.fold (op : RedOp) (n : Nat) (f : Nat → α) : α :=
  match op with
  | .sum => ExactScalar.sum n f
  | .prod => ExactScalar.prod n f
  | .max => Nat.rec (f 0) (fun k acc => ExactScalar.max acc (f k)) n
  | .min => Nat.rec (f 0) (fun k acc => ExactScalar.min acc (f k)) n

/-- `⟦e⟧ env i j` -- scalar expressions. -/
def FE.eval (env : Env α) (i j : Nat) : FE → α
  | .zeroC => ExactScalar.zero
  | .oneC => ExactScalar.one
  | .ofI e => ExactScalar.ofNat (e.eval env i j)
  | .load b off mask =>
      if mask.eval env i j then env.bufs b (off.eval env i j) else ExactScalar.zero
  | .bin op a b => op.apply (a.eval env i j) (b.eval env i j)
  | .un f a => ExactScalar.fn1 f (a.eval env i j)
  | .recip a => ExactScalar.inv (a.eval env i j)
  | .sel c a b => if c.eval env i j then a.eval env i j else b.eval env i j
  | .selLe a b t e =>
      if ExactScalar.le (a.eval env i j) (b.eval env i j)
      then t.eval env i j else e.eval env i j
  | .acc k => env.accs k i j
  | .dot kdim a b =>
      ExactScalar.sum kdim (fun p =>
        ExactScalar.mul (a.eval env i p) (b.eval env p j))
  | .redCol op n a => op.fold n (fun p => a.eval env i p)
  | .redRow op n a => op.fold n (fun p => a.eval env p j)

/-- Memory: the output buffer. Reducible, and the same type as `Buf`: a kernel's
output is another kernel's input, and keeping the two distinct only obstructs
rewriting across a pipeline stage. -/
abbrev Mem (α : Type) : Type := Nat → α

/-- Point update. -/
def Mem.upd (m : Mem α) (q : Nat) (v : α) : Mem α :=
  fun x => if x = q then v else m x

@[simp] theorem Mem.upd_same (m : Mem α) (q : Nat) (v : α) : m.upd q v q = v := by
  simp [Mem.upd]

@[simp] theorem Mem.upd_other {m : Mem α} {q r : Nat} {v : α} (h : r ≠ q) :
    m.upd q v r = m r := by
  simp [Mem.upd, h]

/-- Write one tile to memory, folding over its coordinates in row-major order.
Later lanes win, mirroring hardware when offsets collide -- which is why
collision-freedom is something the kernel proof must establish. -/
def storeTile (rows cols : Nat) (off : IE) (val : FE) (mask : BE)
    (env : Env α) (m : Mem α) : Mem α :=
  Nat.rec (motive := fun _ => Mem α) m
    (fun i mi =>
      Nat.rec (motive := fun _ => Mem α) mi
        (fun j mj =>
          if mask.eval env i j then
            Mem.upd mj (off.eval env i j) (val.eval env i j)
          else mj)
        cols)
    rows

/-- `⟦s⟧` -- statement semantics as a memory transformer. -/
def Stmt.exec (env : Env α) (m : Mem α) : Stmt → Mem α
  | .skip => m
  | .seq a b => b.exec env (a.exec env m)
  | .store rows cols off val mask => storeTile rows cols off val mask env m
  | .forAcc n init step body =>
      let acc : Nat → Nat → α :=
        Nat.rec (motive := fun _ => Nat → Nat → α)
          (fun i j => init.eval env i j)
          (fun k a => fun i j => step.eval (env.pushStep k a) i j)
          n
      body.exec (env.pushAcc acc) m

/-- Run the whole grid. Program ids are visited in a fixed order; a kernel whose
stores are pairwise disjoint (see `Disjoint.lean`) gives the same memory under
every order, which is the data-race-freedom statement. -/
def Prog.run (p : Prog) (bufs : Nat → Buf α) (m : Mem α) : Mem α :=
  Nat.rec (motive := fun _ => Mem α) m
    (fun b0 m0 =>
      Nat.rec (motive := fun _ => Mem α) m0
        (fun b1 m1 =>
          p.body.exec
            { pid := fun a => if a == 0 then b0 else b1
            , ivs := fun _ => 0
            , accs := fun _ _ _ => ExactScalar.zero
            , bufs := bufs } m1)
        p.grid1)
    p.grid0

/-- What it means for a kernel to implement a spec: every element of the output
agrees, for every input, in exact arithmetic. -/
def Implements (p : Prog) (s : Spec α) : Prop :=
  ∀ (bufs : Nat → Buf α) (m : Mem α) (q : Nat), q < s.outSize →
    p.run bufs m q = s.out bufs q

end VerifiedKernel
