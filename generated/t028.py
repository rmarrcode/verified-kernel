import torch
import triton
import triton.language as tl


@triton.jit
def t028_kernel(out_ptr, in0_ptr):
    _off = ((tl.program_id(0) * 1024) + tl.arange(0, 1024))
    _m = (((tl.program_id(0) * 1024) + tl.arange(0, 1024)) < 201326592)
    _v = tl.minimum(tl.maximum(((tl.load(in0_ptr + (((tl.program_id(0) * 1024) + tl.arange(0, 1024)) + 0 * tl.arange(0, 1024)), mask=(((tl.program_id(0) * 1024) + tl.arange(0, 1024)) < 201326592), other=0.0) / (6.0 * (1.0 / 1.0))) + (1.0 * (1.0 / 2.0))), (0.0 * (1.0 / 1.0))), (1.0 * (1.0 / 1.0)))
    tl.store(out_ptr + _off, _v, mask=_m)


def t028(out, ins):
    grid = (196608,)
    t028_kernel[grid](out, ins[0])
    return out
