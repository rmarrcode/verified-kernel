import torch
import triton
import triton.language as tl


@triton.jit
def t088_kernel(out_ptr, in0_ptr):
    _off = ((tl.program_id(0) * 1024) + tl.arange(0, 1024))
    _m = (((tl.program_id(0) * 1024) + tl.arange(0, 1024)) < 67108864)
    _v = (((1.0 * (1.0 / 2.0)) * tl.load(in0_ptr + (((tl.program_id(0) * 1024) + tl.arange(0, 1024)) + 0 * tl.arange(0, 1024)), mask=(((tl.program_id(0) * 1024) + tl.arange(0, 1024)) < 67108864), other=0.0)) * ((1.0 * (1.0 / 1.0)) + (2.0 * tl.sigmoid(2.0 * (((354576841927535.0 * (1.0 / 444396168752463.0)) * (tl.load(in0_ptr + (((tl.program_id(0) * 1024) + tl.arange(0, 1024)) + 0 * tl.arange(0, 1024)), mask=(((tl.program_id(0) * 1024) + tl.arange(0, 1024)) < 67108864), other=0.0) + ((8943.0 * (1.0 / 200000.0)) * ((tl.load(in0_ptr + (((tl.program_id(0) * 1024) + tl.arange(0, 1024)) + 0 * tl.arange(0, 1024)), mask=(((tl.program_id(0) * 1024) + tl.arange(0, 1024)) < 67108864), other=0.0) * tl.load(in0_ptr + (((tl.program_id(0) * 1024) + tl.arange(0, 1024)) + 0 * tl.arange(0, 1024)), mask=(((tl.program_id(0) * 1024) + tl.arange(0, 1024)) < 67108864), other=0.0)) * tl.load(in0_ptr + (((tl.program_id(0) * 1024) + tl.arange(0, 1024)) + 0 * tl.arange(0, 1024)), mask=(((tl.program_id(0) * 1024) + tl.arange(0, 1024)) < 67108864), other=0.0))))))) - 1.0)))
    tl.store(out_ptr + _off, _v, mask=_m)


def t088(out, ins):
    grid = (65536,)
    t088_kernel[grid](out, ins[0])
    return out
