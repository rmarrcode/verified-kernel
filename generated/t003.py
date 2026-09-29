import torch
import triton
import triton.language as tl


@triton.jit
def t003_kernel(out_ptr, in0_ptr, in1_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 1024) & True), (tl.load(in0_ptr + ((((((tl.program_id(0) // 1048576) * 512) + ((tl.program_id(0) // 2048) % 512)) * 1024) + ((_lv0 * 1024) + tl.arange(0, 1024))) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 1024) & True), other=0.0) * tl.load(in1_ptr + ((((((tl.program_id(0) // 1048576) * 1024) + ((_lv0 * 1024) + tl.arange(0, 1024))) * 2048) + (tl.program_id(0) % 2048)) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 1024) & True), other=0.0)), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t003(out, ins):
    grid = (134217728,)
    t003_kernel[grid](out, ins[0], ins[1])
    return out
