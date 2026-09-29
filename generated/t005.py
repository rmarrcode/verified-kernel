import torch
import triton
import triton.language as tl


@triton.jit
def t005_kernel(out_ptr, in0_ptr):
    _off = ((tl.program_id(0) * 1024) + tl.arange(0, 1024))
    _m = (((tl.program_id(0) * 1024) + tl.arange(0, 1024)) < 268435456)
    _v = (tl.load(in0_ptr + (((tl.program_id(0) * 1024) + tl.arange(0, 1024)) + 0 * tl.arange(0, 1024)), mask=(((tl.program_id(0) * 1024) + tl.arange(0, 1024)) < 268435456), other=0.0) * (157.0 * (1.0 / 50.0)))
    tl.store(out_ptr + _off, _v, mask=_m)


def t005(out, ins):
    grid = (262144,)
    t005_kernel[grid](out, ins[0])
    return out
