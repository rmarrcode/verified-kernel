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

/-- `_t0, _t1, ...` for the first `n` intermediates. -/
def tmpNames (n : Nat) : String :=
  String.intercalate ", " ((List.range n).map (fun i => s!"_t{i}"))

def ChainKernel.render (k : ChainKernel) : String :=
  let bodies := String.join (k.stages.map (fun st => st.renderBody ++ "\n\n"))
  let n := k.stages.length
  -- the last stage writes the caller's output, so its buffer is never allocated
  let allocs := String.join ((k.sizes.zipIdx).map (fun p =>
    if p.2 + 1 = n then "" else
      s!"    _t{p.2} = torch.empty({p.1}, device=ins[0].device, dtype=torch.float32)\n"))
  let calls := String.join ((k.stages.zipIdx).map (fun p =>
    let j := p.2
    let args := if j = 0 then "list(ins)"
                else s!"list(ins) + [{tmpNames j}]"
    -- the last stage writes the caller's output rather than an intermediate
    let dst := if j + 1 = n then "out" else s!"_t{j}"
    s!"    {p.1.name}({dst}, {args})\n"))
  preamble ++ bodies ++
  s!"def {k.name}(out, ins):\n" ++
  allocs ++ calls ++ "    return out\n"

end VerifiedKernel
