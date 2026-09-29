import torch
import triton
import triton.language as tl


@triton.jit
def t007_kernel(out_ptr, in0_ptr, in1_ptr):
    _acc0 = tl.zeros([64], dtype=tl.float32)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 64) + tl.arange(0, 64)) < 64) & True), (tl.load(in0_ptr + (((((0 * 16384) + ((tl.program_id(0) // 32768) % 16384)) * 64) + ((_lv0 * 64) + tl.arange(0, 64)))), mask=((((_lv0 * 64) + tl.arange(0, 64)) < 64) & True), other=0.0) * tl.load(in1_ptr + (((((0 * 64) + ((_lv0 * 64) + tl.arange(0, 64))) * 32768) + (tl.program_id(0) % 32768))), mask=((((_lv0 * 64) + tl.arange(0, 64)) < 64) & True), other=0.0)), 0.0))
    _v = tl.where(True, tl.sum(_acc0, axis=0), 0.0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t007(out, ins):
    grid = (536870912,)
    t007_kernel[grid](out, ins[0], ins[1])
    return out
