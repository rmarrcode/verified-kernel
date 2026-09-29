/-
Rendering the target AST to Triton source text.

This is the last mile and it is *trusted*, deliberately kept as small and
mechanical as possible: every function here is a one-line string template with no
logic. The interesting translation work -- rank reconstruction, mask placement,
offset arithmetic -- already happened in `Emit.lean` and was proved there.

Two places where the rendering encodes a semantic decision, both of which the
axiom test suite (`harness/axiom_tests.py`) checks against real Triton:

  * `IE.sub` is truncating on `Nat`, so it renders as `tl.maximum(a - b, 0)`.
    Rendering it as a bare `-` would be unsound for any index expression that can
    go negative.
  * Triton 3.8 has no `tl.tanh`, so `tanh x` renders as `2*sigmoid(2x) - 1`,
    which is the exact identity.
-/
import VerifiedKernel.Emit

namespace VerifiedKernel

def renderPIE : PIE → String
  | .pid a => s!"tl.program_id({a})"
  | .arangeRows n => s!"tl.arange(0, {n})[:, None]"
  | .arangeCols n => s!"tl.arange(0, {n})[None, :]"
  | .arangeFlat n => s!"tl.arange(0, {n})"
  | .lit n => toString n
  | .loopVar k => s!"_lv{k}"
  | .add a b => s!"({renderPIE a} + {renderPIE b})"
  | .mul a b => s!"({renderPIE a} * {renderPIE b})"
  -- `Nat` subtraction truncates at zero; this is the faithful rendering.
  | .sub a b => s!"tl.maximum({renderPIE a} - {renderPIE b}, 0)"
  | .divi a b => s!"({renderPIE a} // {renderPIE b})"
  | .modi a b => s!"({renderPIE a} % {renderPIE b})"

def renderCmp : Cmp → String
  | .lt => "<" | .le => "<=" | .eq => "==" | .ne => "!="

def renderPBE : PBE → String
  | .tt => "True"   -- only ever reached via a mask the templates omit entirely
  | .cmp c a b => s!"({renderPIE a} {renderCmp c} {renderPIE b})"
  | .and a b => s!"({renderPBE a} & {renderPBE b})"
  | .or a b => s!"({renderPBE a} | {renderPBE b})"
  | .not a => s!"(~{renderPBE a})"

def renderBop (op : Bop) (a b : String) : String :=
  match op with
  | .add => s!"({a} + {b})"
  | .mul => s!"({a} * {b})"
  | .sub => s!"({a} - {b})"
  | .div => s!"({a} / {b})"
  | .max => s!"tl.maximum({a}, {b})"
  | .min => s!"tl.minimum({a}, {b})"

def renderFn1 (f : Fn1) (a : String) : String :=
  match f with
  | .exp => s!"tl.exp({a})"
  | .log => s!"tl.log({a})"
  -- exact identity: tanh x = 2 sigmoid(2x) - 1
  | .tanh => s!"(2.0 * tl.sigmoid(2.0 * ({a})) - 1.0)"
  | .sqrt => s!"tl.sqrt({a})"
  | .erf => s!"tl.erf({a})"
  | .abs => s!"tl.abs({a})"
  | .floorF => s!"tl.floor({a})"

def renderRed (op : RedOp) (a : String) (axis : Nat) : String :=
  match op with
  | .sum => s!"tl.sum({a}, axis={axis})"
  | .prod => s!"tl.reduce({a}, {axis}, _mul_combine)"
  | .max => s!"tl.max({a}, axis={axis})"
  | .min => s!"tl.min({a}, axis={axis})"

/-- Rendering needs the enclosing tile's rank for one reason: reducing the column
axis of a *rank-1* tile is `axis=0`, while on a 2-D tile it is `axis=1`. Emitting
`axis=1` on a flat tile is a shape error at best and a wrong answer at worst. -/
def renderPFE (tk : TileKind) (width : Nat) : PFE → String
  | .zeroC => "0.0"
  | .oneC => "1.0"
  -- A compile-time constant must become a Python float literal: `tl` arithmetic
  -- accepts `5.0`, but a bare Python `int` has no `.to` method.
  | .ofI (.lit n) => s!"{n}.0"
  | .ofI e => s!"({renderPIE e}).to(tl.float32)"
  -- An unconditional mask is omitted rather than rendered: `mask=True` is not a
  -- tile and Triton rejects it.
  | .load b off .tt => s!"tl.load(in{b}_ptr + ({renderPIE off}))"
  -- A masked load needs its offset and mask to agree in rank. The IR is
  -- coordinate-wise, so an offset that happens not to mention the lane
  -- coordinate -- a broadcast read, for instance -- renders as a scalar while the
  -- mask is still a tile, which Triton rejects outright. Adding `0 * arange`
  -- broadcasts the offset to the tile width; it is an arithmetic no-op and
  -- matches the IR, where the offset is evaluated once per lane regardless.
  | .load b off mask =>
      s!"tl.load(in{b}_ptr + ({renderPIE off} + 0 * tl.arange(0, {width})), " ++
      s!"mask={renderPBE mask}, other=0.0)"
  | .bin op a b => renderBop op (renderPFE tk width a) (renderPFE tk width b)
  | .un f a => renderFn1 f (renderPFE tk width a)
  | .recip a => s!"(1.0 / {renderPFE tk width a})"
  -- A trivially-true condition is dropped rather than rendered as `tl.where(True, ..)`.
  | .sel .tt a _ => renderPFE tk width a
  | .sel c a b =>
      s!"tl.where({renderPBE c}, {renderPFE tk width a}, {renderPFE tk width b})"
  | .selLe a b t e =>
      s!"tl.where({renderPFE tk width a} <= {renderPFE tk width b}, " ++
      s!"{renderPFE tk width t}, {renderPFE tk width e})"
  | .acc k => s!"_acc{k}"
  | .dot _ a b =>
      s!"tl.dot({renderPFE tk width a}, {renderPFE tk width b}, input_precision=\"ieee\")"
  | .redCol op n a =>
      renderRed op (renderPFE tk width a) (match tk with | .flat => 0 | .twoD => 1)
  | .redRow op n a => renderRed op (renderPFE tk width a) 0

/-! ## Whole-kernel templates -/

/-- A flat 1-D kernel ready to render: the shape the element-wise family (and
anything else reducible to a pointwise map over the flat output) compiles to. -/
structure FlatKernel where
  name    : String
  arity   : Nat
  block   : Nat
  n       : Nat
  nblocks : Nat
  val     : FE

/-- Comma-separated `in0_ptr, in1_ptr, ...`. -/
def inPtrs (arity : Nat) : String :=
  String.intercalate ", " ((List.range arity).map (fun i => s!"in{i}_ptr"))

/-- `ins[0], ins[1], ...` -/
def inArgs (arity : Nat) : String :=
  String.intercalate ", " ((List.range arity).map (fun i => s!"ins[{i}]"))

def preamble : String :=
  "import torch\nimport triton\nimport triton.language as tl\n\n\n" ++
  -- Triton has no built-in product reduction; `tl.reduce` takes a combine
  -- function, which must itself be a `@triton.jit` definition.
  "@triton.jit\ndef _mul_combine(a, b):\n    return a * b\n\n\n"

def FlatKernel.render (k : FlatKernel) : String :=
  let body := renderPFE .flat k.block (emitFE .flat 1 k.block k.val)
  let off := renderPIE (emitIE .flat 1 k.block (flatOff k.block))
  let msk := renderPBE (emitBE .flat 1 k.block (flatMask k.block k.n))
  let args := inArgs k.arity
  preamble ++
  "@triton.jit\n" ++
  s!"def {k.name}_kernel(out_ptr, {inPtrs k.arity}):\n" ++
  s!"    _off = {off}\n" ++
  s!"    _m = {msk}\n" ++
  s!"    _v = {body}\n" ++
  s!"    tl.store(out_ptr + _off, _v, mask=_m)\n\n\n" ++
  s!"def {k.name}(out, ins):\n" ++
  s!"    grid = ({k.nblocks},)\n" ++
  s!"    {k.name}_kernel[grid](out, {args})\n" ++
  "    return out\n"

/-- Metadata the Python runtime needs. -/
def FlatKernel.manifest (k : FlatKernel) : String :=
  let q : String := "\""
  "{" ++ q ++ "name" ++ q ++ ": " ++ q ++ k.name ++ q ++
  ", " ++ q ++ "arity" ++ q ++ ": " ++ toString k.arity ++
  ", " ++ q ++ "out_size" ++ q ++ ": " ++ toString k.n ++
  ", " ++ q ++ "nblocks" ++ q ++ ": " ++ toString k.nblocks ++
  ", " ++ q ++ "block" ++ q ++ ": " ++ toString k.block ++
  ", " ++ q ++ "kind" ++ q ++ ": " ++ q ++ "flat1d" ++ q ++ "}"

/-! ### The reduction template -/

/-- A reduction kernel ready to render: one program per output element, tiling the
reduced axis with a `block`-lane accumulator. -/
structure ReduceKernel where
  name   : String
  arity  : Nat
  block  : Nat
  nkb    : Nat
  nout   : Nat
  /-- the accumulator's starting value. Zero for a sum; for a max it is the element
  at reduction index 0 -- a genuine element, since a max has no identity to start
  from. -/
  init   : FE
  step   : FE
  stored : FE

/-- Just the kernel and its launcher, without the module preamble, so a pipeline
can concatenate two of them. -/
def ReduceKernel.renderBody (k : ReduceKernel) : String :=
  let stepS := renderPFE .flat k.block (emitFE .flat 1 k.block k.step)
  let storedS := renderPFE .flat k.block (emitFE .flat 1 k.block k.stored)
  let args := inArgs k.arity
  "@triton.jit\n" ++
  s!"def {k.name}_kernel(out_ptr, {inPtrs k.arity}):\n" ++
  -- The accumulator must start as a *tile*: a loop-carried value in Triton keeps
  -- one type across iterations, so seeding it with a scalar would not compile.
  -- Adding `tl.zeros` broadcasts a scalar seed to the tile width.
  s!"    _acc0 = tl.zeros([{k.block}], dtype=tl.float32) + (" ++
    renderPFE .flat k.block (emitFE .flat 1 k.block k.init) ++ ")\n" ++
  s!"    for _lv0 in range(0, {k.nkb}):\n" ++
  s!"        _acc0 = {stepS}\n" ++
  s!"    _v = {storedS}\n" ++
  "    tl.store(out_ptr + tl.program_id(0), _v)\n\n\n" ++
  s!"def {k.name}(out, ins):\n" ++
  s!"    grid = ({k.nout},)\n" ++
  s!"    {k.name}_kernel[grid](out, {args})\n" ++
  "    return out\n"

def ReduceKernel.render (k : ReduceKernel) : String :=
  preamble ++ k.renderBody

/-! ### Two-stage pipelines

Stage 1 writes an intermediate buffer; stage 2 reads it as its *last* input, so the
intermediate simply appends to the input list and no renumbering is needed. The
launcher allocates it, which is the only place the runtime touches memory the
proofs reason about -- hence `n1` comes from the certificate, not from a guess. -/

structure PipelineKernel where
  name   : String
  /-- number of real inputs (the intermediate is buffer index `arity`) -/
  arity  : Nat
  /-- element count of the intermediate buffer -/
  n1     : Nat
  stage1 : ReduceKernel
  stage2 : ReduceKernel

def PipelineKernel.render (k : PipelineKernel) : String :=
  preamble ++ k.stage1.renderBody ++ "\n\n" ++ k.stage2.renderBody ++ "\n\n" ++
  s!"def {k.name}(out, ins):\n" ++
  s!"    _tmp = torch.empty({k.n1}, device=ins[0].device, dtype=torch.float32)\n" ++
  s!"    {k.stage1.name}(_tmp, ins)\n" ++
  s!"    {k.stage2.name}(out, list(ins) + [_tmp])\n" ++
  "    return out\n"


end VerifiedKernel
