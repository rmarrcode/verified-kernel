import torch
import triton
import triton.language as tl


@triton.jit
def t026_kernel(out_ptr, in0_ptr):
    _off = ((tl.program_id(0) * 1024) + tl.arange(0, 1024))
    _m = (((tl.program_id(0) * 1024) + tl.arange(0, 1024)) < 402653184)
    _v = (((1.0 * (1.0 / 2.0)) * tl.load(in0_ptr + (((tl.program_id(0) * 1024) + tl.arange(0, 1024)) + 0 * tl.arange(0, 1024)), mask=(((tl.program_id(0) * 1024) + tl.arange(0, 1024)) < 402653184), other=0.0)) * ((1.0 * (1.0 / 1.0)) + tl.erf((tl.load(in0_ptr + (((tl.program_id(0) * 1024) + tl.arange(0, 1024)) + 0 * tl.arange(0, 1024)), mask=(((tl.program_id(0) * 1024) + tl.arange(0, 1024)) < 402653184), other=0.0) * (1.0 / tl.sqrt((2.0 * (1.0 / 1.0))))))))
    tl.store(out_ptr + _off, _v, mask=_m)


def t026(out, ins):
    grid = (393216,)
    t026_kernel[grid](out, ins[0])
    return out
