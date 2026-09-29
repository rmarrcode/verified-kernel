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

end VerifiedKernel
