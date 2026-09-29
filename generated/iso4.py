import torch
import triton
import triton.language as tl


@triton.jit
def _mul_combine(a, b):
    return a * b


@triton.jit
def iso4_kernel(out_ptr, in0_ptr, in1_ptr):
    _acc0 = tl.zeros([16], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 16) + tl.arange(0, 16)) < 24) & ((0 < 1) & (0 < 1))), (tl.load(in0_ptr + ((((tl.program_id(0) // 96) * 24) + ((_lv0 * 16) + tl.arange(0, 16))) + 0 * tl.arange(0, 16)), mask=((((_lv0 * 16) + tl.arange(0, 16)) < 24) & ((0 < 1) & (0 < 1))), other=0.0) * tl.load(in1_ptr + ((((tl.program_id(0) % 96) * 24) + ((_lv0 * 16) + tl.arange(0, 16))) + 0 * tl.arange(0, 16)), mask=((((_lv0 * 16) + tl.arange(0, 16)) < 24) & ((0 < 1) & (0 < 1))), other=0.0)), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def iso4(out, ins):
    grid = (192,)
    iso4_kernel[grid](out, ins[0], ins[1])
    return out
