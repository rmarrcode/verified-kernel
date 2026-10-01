/-
Rendering a three-stage pipeline.

Kept in its own file so the two-stage template stays untouched. The launcher
allocates both intermediates and appends them to the input list, so stage `n` reads
them as its last buffers and no renumbering is needed anywhere.
-/
import VerifiedKernel.Render

namespace VerifiedKernel

/-- A three-stage pipeline: two intermediate buffers, `n1` and `n2` elements. -/
structure PipelineKernel3 where
  name   : String
  /-- number of real inputs; the intermediates are buffers `arity` and `arity+1` -/
  arity  : Nat
  n1     : Nat
  n2     : Nat
  stage1 : ReduceKernel
  stage2 : ReduceKernel
  stage3 : ReduceKernel

def PipelineKernel3.render (k : PipelineKernel3) : String :=
  preamble ++ k.stage1.renderBody ++ "\n\n" ++ k.stage2.renderBody ++ "\n\n" ++
  k.stage3.renderBody ++ "\n\n" ++
  s!"def {k.name}(out, ins):\n" ++
  s!"    _t1 = torch.empty({k.n1}, device=ins[0].device, dtype=torch.float32)\n" ++
  s!"    _t2 = torch.empty({k.n2}, device=ins[0].device, dtype=torch.float32)\n" ++
  s!"    {k.stage1.name}(_t1, ins)\n" ++
  s!"    {k.stage2.name}(_t2, list(ins) + [_t1])\n" ++
  s!"    {k.stage3.name}(out, list(ins) + [_t1, _t2])\n" ++
  "    return out\n"

/-! ### Chains of arbitrary length

A fused operator is a handful of stages; a convolutional network is a hundred. The
launcher allocates one intermediate per stage and appends it to the input list, so
stage `j` reads buffers `0 .. arity+j-1` and writes `arity+j` -- no renumbering
anywhere, and the buffer a stage writes is fixed by its position. -/

structure ChainKernel where
  name   : String
  /-- number of real inputs; stage `j` writes buffer `arity + j` -/
  arity  : Nat
  /-- element count of each stage's output buffer, in order -/
  sizes  : List Nat
  stages : List ReduceKernel
  /-- the intermediates (by index) to release after each stage: those it was the
  last to read -/
  frees  : List (List Nat) := []

/-- Lines run after stage `j`: replace each intermediate it was the last reader of
by a one-element placeholder, so its memory can be reused.

The semantics (`runStages`) keeps every buffer for the whole chain. Releasing one
early agrees with that exactly when no later stage reads it, and a stage reads a
buffer only if its body or `post` names it -- otherwise its kernel issues no load
from that pointer, so the placeholder is passed but never dereferenced. `frees` is
computed from that fact by the generator (`compile.chain_lifetimes`). -/
def releaseLines (arity : Nat) (frees : List (List Nat)) (j : Nat) : String :=
  String.join ((frees.getD j []).map (fun i => s!"    _b[{arity + i}] = _dead\n"))

/-- The launcher's opening lines: every buffer, by number, in one flat list. An
intermediate is allocated only when its stage runs; until then, and after its last
reader, its slot holds the placeholder -- a loop's body is passed every outer buffer,
and none of those it does not read is ever dereferenced. -/
def bufList (n : Nat) : String :=
  "    _dead = torch.empty(1, device=ins[0].device, dtype=torch.float32)\n" ++
  s!"    _b = [x.reshape(-1) for x in ins] + [_dead] * {n}\n"

/-- Allocate item `j`'s output: an intermediate, or the caller's output if last. -/
def allocLine (arity n j size : Nat) : String :=
  if j + 1 = n then s!"    _b[{arity + j}] = out.reshape(-1)\n"
  else s!"    _b[{arity + j}] = torch.empty({size}, device=ins[0].device, dtype=torch.float32)\n"

def ChainKernel.render (k : ChainKernel) : String :=
  let bodies := String.join (k.stages.map (fun st => st.renderBody ++ "\n\n"))
  let n := k.stages.length
  let calls := String.join ((k.stages.zipIdx).map (fun p =>
    let j := p.2
    allocLine k.arity n j (k.sizes.getD j 0) ++
    s!"    {p.1.name}(_b[{k.arity + j}], _b[:{k.arity + j}])\n" ++
    releaseLines k.arity k.frees j))
  preamble ++ bodies ++
  s!"def {k.name}(out, ins):\n" ++ bufList n ++
  calls ++ "    return out\n"

/-! ### Chains containing recurrences

A `Recur` stage (see `Recur.lean`) is run by the launcher as a Python loop over the
body's kernels. Its semantics there fixes what the loop must do:

  * state `0` is the initial-state buffer's first `S` elements, copied to the
    history's first `S` slots;
  * at step `s` the body sees every outer buffer by number, then the state -- the
    history's window `s*S ..` -- then each view, the window `s*stride ..` of its
    source, then its own intermediates;
  * the body's last kernel writes the history's window `(s+1)*S ..`, which is the
    next state.

A window of a contiguous flat tensor reads its element `i` from `offset + i`, which
is exactly `Recur.envAt`'s view. That is the one assumption about the runtime this
adds, and it is PyTorch's slicing of a 1-D tensor. -/

structure RecurKernel where
  T      : Nat
  S      : Nat
  init   : Nat
  /-- `(source buffer, stride)` per view, in buffer order after the state -/
  views  : List (Nat × Nat)
  /-- sizes of the body's intermediates other than the last, which is the state -/
  sizes  : List Nat
  body   : List ReduceKernel

inductive ChainItem where
  | red (k : ReduceKernel)
  | loop (k : RecurKernel)

def ChainItem.defs : ChainItem → String
  | .red k => k.renderBody ++ "\n\n"
  | .loop r => String.join (r.body.map (fun b => b.renderBody ++ "\n\n"))

structure GChainKernel where
  name  : String
  arity : Nat
  sizes : List Nat
  items : List ChainItem
  frees : List (List Nat) := []

/-- The launcher lines for item `j`, whose output is outer buffer `arity + j`, in a
chain of `n` items. A body's own buffers are numbered above every outer one. -/
def ChainItem.call (arity n j : Nat) : ChainItem → String
  | .red k => s!"    {k.name}(_b[{arity + j}], _b[:{arity + j}])\n"
  | .loop r =>
    let base := arity + n
    let nb := r.body.length
    let allocs := String.join (r.sizes.map (fun n =>
      s!"torch.empty({n}, device=_h.device, dtype=torch.float32), "))
    let views := String.join (r.views.map (fun p =>
      s!"_b[{p.1}][_s * {p.2}:(_s + 1) * {p.2}], "))
    let calls := String.join ((r.body.zipIdx).map (fun p =>
      let i := p.2
      let dst := if i + 1 = nb then s!"_h[(_s + 1) * {r.S}:(_s + 2) * {r.S}]"
                 else s!"_l[{i}]"
      s!"        {p.1.name}({dst}, _e[:{base + 1 + r.views.length + i}])\n"))
    s!"    _h = _b[{arity + j}]\n" ++
    s!"    _h[0:{r.S}].copy_(_b[{r.init}][0:{r.S}])\n" ++
    s!"    _l = [{allocs}]\n" ++
    s!"    for _s in range({r.T}):\n" ++
    -- every outer buffer, then the state, the views and the intermediates
    s!"        _e = _b + [_h[_s * {r.S}:(_s + 1) * {r.S}], {views}] + _l\n" ++
    calls

def GChainKernel.render (k : GChainKernel) : String :=
  let bodies := String.join (k.items.map ChainItem.defs)
  let n := k.items.length
  let calls := String.join ((k.items.zipIdx).map (fun p =>
    allocLine k.arity n p.2 (k.sizes.getD p.2 0) ++ p.1.call k.arity n p.2 ++
    releaseLines k.arity k.frees p.2))
  preamble ++ bodies ++
  s!"def {k.name}(out, ins):\n" ++ bufList n ++
  calls ++ "    return out\n"

end VerifiedKernel
