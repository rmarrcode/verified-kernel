import torch
import triton
import triton.language as tl


@triton.jit
def t022_kernel(out_ptr, in0_ptr):
    _off = ((tl.program_id(0) * 1024) + tl.arange(0, 1024))
    _m = (((tl.program_id(0) * 1024) + tl.arange(0, 1024)) < 402653184)
    _v = (2.0 * tl.sigmoid(2.0 * (tl.load(in0_ptr + (((tl.program_id(0) * 1024) + tl.arange(0, 1024))), mask=(((tl.program_id(0) * 1024) + tl.arange(0, 1024)) < 402653184), other=0.0))) - 1.0)
    tl.store(out_ptr + _off, _v, mask=_m)


def t022(out, ins):
    grid = (393216,)
    t022_kernel[grid](out, ins[0])
    return out
