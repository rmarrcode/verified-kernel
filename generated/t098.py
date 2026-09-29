import torch
import triton
import triton.language as tl


@triton.jit
def t098_kernel(out_ptr, in0_ptr, in1_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32)
    for _lv0 in range(0, 262144):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 268435456) & True), (tl.load(in1_ptr + ((((((tl.program_id(0) // 1) * 268435456) + ((_lv0 * 1024) + tl.arange(0, 1024))) * 1) + (tl.program_id(0) % 1))), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 268435456) & True), other=0.0) * (tl.log(tl.load(in1_ptr + ((((((tl.program_id(0) // 1) * 268435456) + ((_lv0 * 1024) + tl.arange(0, 1024))) * 1) + (tl.program_id(0) % 1))), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 268435456) & True), other=0.0)) - tl.log(tl.load(in0_ptr + ((((((tl.program_id(0) // 1) * 268435456) + ((_lv0 * 1024) + tl.arange(0, 1024))) * 1) + (tl.program_id(0) % 1))), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 268435456) & True), other=0.0)))), 0.0))
    _v = tl.where(True, (tl.sum(_acc0, axis=0) * (1.0 * (1.0 / 16384.0))), 0.0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t098(out, ins):
    grid = (1,)
    t098_kernel[grid](out, ins[0], ins[1])
    return out
