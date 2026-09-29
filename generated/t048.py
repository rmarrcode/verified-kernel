import torch
import triton
import triton.language as tl


@triton.jit
def t048_kernel(out_ptr, in0_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32)
    for _lv0 in range(0, 4):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 4096) & True), tl.load(in0_ptr + ((((((tl.program_id(0) // 4095) * 4096) + ((_lv0 * 1024) + tl.arange(0, 1024))) * 4095) + (tl.program_id(0) % 4095)) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 4096) & True), other=0.0), 0.0))
    _v = (tl.sum(_acc0, axis=0) * (1.0 * (1.0 / 4096.0)))
    tl.store(out_ptr + tl.program_id(0), _v)


def t048(out, ins):
    grid = (262080,)
    t048_kernel[grid](out, ins[0])
    return out
