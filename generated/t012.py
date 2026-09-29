import torch
import triton
import triton.language as tl


@triton.jit
def t012_kernel(out_ptr, in0_ptr, in1_ptr):
    _acc0 = tl.zeros([1], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), (tl.load(in0_ptr + ((((tl.program_id(0) // 4096) * 1) + 0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) * tl.load(in1_ptr + ((((tl.program_id(0) // 4096) * 4096) + (tl.program_id(0) % 4096)) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t012(out, ins):
    grid = (16777216,)
    t012_kernel[grid](out, ins[0], ins[1])
    return out
