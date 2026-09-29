import torch
import triton
import triton.language as tl


@triton.jit
def _mul_combine(a, b):
    return a * b


@triton.jit
def t027_kernel(out_ptr, in0_ptr):
    _off = ((tl.program_id(0) * 1024) + tl.arange(0, 1024))
    _m = (((tl.program_id(0) * 1024) + tl.arange(0, 1024)) < 402653184)
    _v = ((955375017913994.0 * (1.0 / 909273931795369.0)) * tl.where(tl.load(in0_ptr + (((tl.program_id(0) * 1024) + tl.arange(0, 1024)) + 0 * tl.arange(0, 1024)), mask=(((tl.program_id(0) * 1024) + tl.arange(0, 1024)) < 402653184), other=0.0) <= (0.0 * (1.0 / 1.0)), ((1432529283788243.0 * (1.0 / 856129058194449.0)) * (tl.exp(tl.load(in0_ptr + (((tl.program_id(0) * 1024) + tl.arange(0, 1024)) + 0 * tl.arange(0, 1024)), mask=(((tl.program_id(0) * 1024) + tl.arange(0, 1024)) < 402653184), other=0.0)) - (1.0 * (1.0 / 1.0)))), tl.load(in0_ptr + (((tl.program_id(0) * 1024) + tl.arange(0, 1024)) + 0 * tl.arange(0, 1024)), mask=(((tl.program_id(0) * 1024) + tl.arange(0, 1024)) < 402653184), other=0.0)))
    tl.store(out_ptr + _off, _v, mask=_m)


def t027(out, ins):
    grid = (393216,)
    t027_kernel[grid](out, ins[0])
    return out
