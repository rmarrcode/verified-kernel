import torch
import triton
import triton.language as tl


@triton.jit
def _mul_combine(a, b):
    return a * b


@triton.jit
def t076_kernel(out_ptr, in0_ptr, in1_ptr):
    _acc0 = tl.zeros([128], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 128) + tl.arange(0, 128)) < 192) & ((((tl.program_id(0) % 174758) * 3) + ((((_lv0 * 128) + tl.arange(0, 128)) % 3) * 4)) < 524280)), (tl.load(in0_ptr + ((((((tl.program_id(0) // 22369024) * 64) + (((_lv0 * 128) + tl.arange(0, 128)) // 3)) * 524280) + (((tl.program_id(0) % 174758) * 3) + ((((_lv0 * 128) + tl.arange(0, 128)) % 3) * 4))) + 0 * tl.arange(0, 128)), mask=((((_lv0 * 128) + tl.arange(0, 128)) < 192) & ((((tl.program_id(0) % 174758) * 3) + ((((_lv0 * 128) + tl.arange(0, 128)) % 3) * 4)) < 524280)), other=0.0) * tl.load(in1_ptr + (((((((tl.program_id(0) // 174758) % 128) * 64) + (((_lv0 * 128) + tl.arange(0, 128)) // 3)) * 3) + (((_lv0 * 128) + tl.arange(0, 128)) % 3)) + 0 * tl.arange(0, 128)), mask=((((_lv0 * 128) + tl.arange(0, 128)) < 192) & ((((tl.program_id(0) % 174758) * 3) + ((((_lv0 * 128) + tl.arange(0, 128)) % 3) * 4)) < 524280)), other=0.0)), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t076(out, ins):
    grid = (178952192,)
    t076_kernel[grid](out, ins[0], ins[1])
    return out
