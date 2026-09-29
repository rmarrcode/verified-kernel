import torch
import triton
import triton.language as tl


@triton.jit
def t010_kernel(out_ptr, in0_ptr, in1_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 2048) & True), (tl.load(in0_ptr + ((((((tl.program_id(0) // 786432) * 1024) + ((tl.program_id(0) // 768) % 1024)) * 2048) + ((_lv0 * 1024) + tl.arange(0, 1024)))), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 2048) & True), other=0.0) * tl.load(in1_ptr + (((((0 * 2048) + ((_lv0 * 1024) + tl.arange(0, 1024))) * 768) + (tl.program_id(0) % 768))), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 2048) & True), other=0.0)), 0.0))
    _v = tl.where(True, tl.sum(_acc0, axis=0), 0.0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t010(out, ins):
    grid = (12582912,)
    t010_kernel[grid](out, ins[0], ins[1])
    return out
