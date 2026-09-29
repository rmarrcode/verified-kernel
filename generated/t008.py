import torch
import triton
import triton.language as tl


@triton.jit
def t008_kernel(out_ptr, in0_ptr, in1_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32)
    for _lv0 in range(0, 3):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 2949) & True), (tl.load(in0_ptr + (((((0 * 8205) + ((tl.program_id(0) // 5921) % 8205)) * 2949) + ((_lv0 * 1024) + tl.arange(0, 1024))) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 2949) & True), other=0.0) * tl.load(in1_ptr + (((((0 * 2949) + ((_lv0 * 1024) + tl.arange(0, 1024))) * 5921) + (tl.program_id(0) % 5921)) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 2949) & True), other=0.0)), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t008(out, ins):
    grid = (48581805,)
    t008_kernel[grid](out, ins[0], ins[1])
    return out
