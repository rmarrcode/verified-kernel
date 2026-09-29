import torch
import triton
import triton.language as tl


@triton.jit
def t014_kernel(out_ptr, in0_ptr, in1_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32)
    for _lv0 in range(0, 4):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 4096) & True), (tl.load(in0_ptr + (((((0 * 4096) + ((tl.program_id(0) // 4096) % 4096)) * 4096) + ((_lv0 * 1024) + tl.arange(0, 1024)))), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 4096) & True), other=0.0) * tl.load(in1_ptr + (((((0 * 4096) + ((_lv0 * 1024) + tl.arange(0, 1024))) * 4096) + (tl.program_id(0) % 4096))), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 4096) & True), other=0.0)), 0.0))
    _v = tl.where((((tl.program_id(0) // 4096) % 4096) <= (tl.program_id(0) % 4096)), tl.sum(_acc0, axis=0), 0.0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t014(out, ins):
    grid = (16777216,)
    t014_kernel[grid](out, ins[0], ins[1])
    return out
