import torch
import triton
import triton.language as tl


@triton.jit
def _mul_combine(a, b):
    return a * b


@triton.jit
def t009_kernel(out_ptr, in0_ptr, in1_ptr):
    _acc0 = tl.zeros([32], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 32) + tl.arange(0, 32)) < 32) & True), (tl.load(in0_ptr + (((((tl.program_id(0) // 32768) % 8192) * 32) + ((_lv0 * 32) + tl.arange(0, 32))) + 0 * tl.arange(0, 32)), mask=((((_lv0 * 32) + tl.arange(0, 32)) < 32) & True), other=0.0) * tl.load(in1_ptr + (((((_lv0 * 32) + tl.arange(0, 32)) * 32768) + (tl.program_id(0) % 32768)) + 0 * tl.arange(0, 32)), mask=((((_lv0 * 32) + tl.arange(0, 32)) < 32) & True), other=0.0)), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t009(out, ins):
    grid = (268435456,)
    t009_kernel[grid](out, ins[0], ins[1])
    return out
