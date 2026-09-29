import torch
import triton
import triton.language as tl


@triton.jit
def t094_kernel(out_ptr, in0_ptr, in1_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 524288):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 536870912) & True), ((tl.load(in0_ptr + ((((((_lv0 * 1024) + tl.arange(0, 1024)) // 32768) * 32768) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 32768)) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 536870912) & True), other=0.0) - tl.load(in1_ptr + ((((((_lv0 * 1024) + tl.arange(0, 1024)) // 32768) * 32768) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 32768)) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 536870912) & True), other=0.0)) * (tl.load(in0_ptr + ((((((_lv0 * 1024) + tl.arange(0, 1024)) // 32768) * 32768) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 32768)) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 536870912) & True), other=0.0) - tl.load(in1_ptr + ((((((_lv0 * 1024) + tl.arange(0, 1024)) // 32768) * 32768) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 32768)) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 536870912) & True), other=0.0))), 0.0))
    _v = (tl.sum(_acc0, axis=0) * (1.0 * (1.0 / 536870912.0)))
    tl.store(out_ptr + tl.program_id(0), _v)


def t094(out, ins):
    grid = (1,)
    t094_kernel[grid](out, ins[0], ins[1])
    return out
