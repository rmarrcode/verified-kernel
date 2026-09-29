import torch
import triton
import triton.language as tl


@triton.jit
def t016_kernel(out_ptr, in0_ptr, in1_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32)
    for _lv0 in range(0, 8):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 8192) & True), (tl.load(in0_ptr + (((((_lv0 * 1024) + tl.arange(0, 1024)) * 2048) + ((tl.program_id(0) // 4096) % 2048)) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 8192) & True), other=0.0) * tl.load(in1_ptr + (((((0 * 8192) + ((_lv0 * 1024) + tl.arange(0, 1024))) * 4096) + (tl.program_id(0) % 4096)) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 8192) & True), other=0.0)), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t016(out, ins):
    grid = (8388608,)
    t016_kernel[grid](out, ins[0], ins[1])
    return out
