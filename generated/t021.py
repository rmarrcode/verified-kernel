import torch
import triton
import triton.language as tl


@triton.jit
def _mul_combine(a, b):
    return a * b


@triton.jit
def t021_kernel(out_ptr, in0_ptr):
    _off = ((tl.program_id(0) * 1024) + tl.arange(0, 1024))
    _m = (((tl.program_id(0) * 1024) + tl.arange(0, 1024)) < 402653184)
    _v = (1.0 / ((1.0 * (1.0 / 1.0)) + tl.exp(((0.0 * (1.0 / 1.0)) - tl.load(in0_ptr + (((tl.program_id(0) * 1024) + tl.arange(0, 1024)) + 0 * tl.arange(0, 1024)), mask=(((tl.program_id(0) * 1024) + tl.arange(0, 1024)) < 402653184), other=0.0)))))
    tl.store(out_ptr + _off, _v, mask=_m)


def t021(out, ins):
    grid = (393216,)
    t021_kernel[grid](out, ins[0])
    return out
