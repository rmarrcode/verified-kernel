import torch
import triton
import triton.language as tl


@triton.jit
def _mul_combine(a, b):
    return a * b


@triton.jit
def iso7_kernel(out_ptr, in0_ptr, in1_ptr):
    _acc0 = tl.zeros([8], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 8) + tl.arange(0, 8)) < 8) & ((0 < 1) & (0 < 1))), (tl.load(in0_ptr + ((((tl.program_id(0) // 32) * 8) + ((_lv0 * 8) + tl.arange(0, 8))) + 0 * tl.arange(0, 8)), mask=((((_lv0 * 8) + tl.arange(0, 8)) < 8) & ((0 < 1) & (0 < 1))), other=0.0) * tl.load(in1_ptr + ((((tl.program_id(0) % 32) * 8) + ((_lv0 * 8) + tl.arange(0, 8))) + 0 * tl.arange(0, 8)), mask=((((_lv0 * 8) + tl.arange(0, 8)) < 8) & ((0 < 1) & (0 < 1))), other=0.0)), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def iso7(out, ins):
    grid = (64,)
    iso7_kernel[grid](out, ins[0], ins[1])
    return out
