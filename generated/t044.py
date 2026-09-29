import torch
import triton
import triton.language as tl


@triton.jit
def t044_kernel(out_ptr, in0_ptr):
    _acc0 = tl.zeros([8], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 8) + tl.arange(0, 8)) < 8) & ((4 <= (((tl.program_id(0) % 65537) * 1) + ((_lv0 * 8) + tl.arange(0, 8)))) & ((((tl.program_id(0) % 65537) * 1) + ((_lv0 * 8) + tl.arange(0, 8))) < 65540))), tl.load(in0_ptr + ((((((tl.program_id(0) // 8388736) * 128) + ((tl.program_id(0) // 65537) % 128)) * 65536) + tl.maximum((((tl.program_id(0) % 65537) * 1) + ((_lv0 * 8) + tl.arange(0, 8))) - 4, 0)) + 0 * tl.arange(0, 8)), mask=((((_lv0 * 8) + tl.arange(0, 8)) < 8) & ((4 <= (((tl.program_id(0) % 65537) * 1) + ((_lv0 * 8) + tl.arange(0, 8)))) & ((((tl.program_id(0) % 65537) * 1) + ((_lv0 * 8) + tl.arange(0, 8))) < 65540))), other=0.0), 0.0))
    _v = (tl.sum(_acc0, axis=0) * (1.0 * (1.0 / 8.0)))
    tl.store(out_ptr + tl.program_id(0), _v)


def t044(out, ins):
    grid = (268439552,)
    t044_kernel[grid](out, ins[0])
    return out
