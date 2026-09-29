import torch
import triton
import triton.language as tl


@triton.jit
def _mul_combine(a, b):
    return a * b


@triton.jit
def iso6_kernel(out_ptr, in0_ptr, in1_ptr):
    _acc0 = tl.zeros([16], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 16) + tl.arange(0, 16)) < 24) & ((((tl.program_id(0) // 4) % 4) < 4) & ((tl.program_id(0) % 4) < 4))), (tl.load(in0_ptr + ((((((((tl.program_id(0) // 1536) * 24) + ((_lv0 * 16) + tl.arange(0, 16))) * 4) + ((tl.program_id(0) // 4) % 4)) * 4) + (tl.program_id(0) % 4)) + 0 * tl.arange(0, 16)), mask=((((_lv0 * 16) + tl.arange(0, 16)) < 24) & ((((tl.program_id(0) // 4) % 4) < 4) & ((tl.program_id(0) % 4) < 4))), other=0.0) * tl.load(in1_ptr + (((((tl.program_id(0) // 16) % 96) * 24) + ((_lv0 * 16) + tl.arange(0, 16))) + 0 * tl.arange(0, 16)), mask=((((_lv0 * 16) + tl.arange(0, 16)) < 24) & ((((tl.program_id(0) // 4) % 4) < 4) & ((tl.program_id(0) % 4) < 4))), other=0.0)), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def iso6(out, ins):
    grid = (3072,)
    iso6_kernel[grid](out, ins[0], ins[1])
    return out
