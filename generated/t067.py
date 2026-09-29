import torch
import triton
import triton.language as tl


@triton.jit
def t067_kernel(out_ptr, in0_ptr, in1_ptr):
    _acc0 = tl.zeros([128], dtype=tl.float32)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 128) + tl.arange(0, 128)) < 192) & ((0 <= (((tl.program_id(0) % 131070) * 1) + ((((_lv0 * 128) + tl.arange(0, 128)) % 3) * 1))) & ((((tl.program_id(0) % 131070) * 1) + ((((_lv0 * 128) + tl.arange(0, 128)) % 3) * 1)) < 131072))), (tl.load(in0_ptr + ((((((tl.program_id(0) // 16776960) * 64) + (((((tl.program_id(0) // 131070) % 128) // 128) * 64) + (((_lv0 * 128) + tl.arange(0, 128)) // 3))) * 131072) + tl.maximum((((tl.program_id(0) % 131070) * 1) + ((((_lv0 * 128) + tl.arange(0, 128)) % 3) * 1)) - 0, 0)) + 0 * tl.arange(0, 128)), mask=((((_lv0 * 128) + tl.arange(0, 128)) < 192) & ((0 <= (((tl.program_id(0) % 131070) * 1) + ((((_lv0 * 128) + tl.arange(0, 128)) % 3) * 1))) & ((((tl.program_id(0) % 131070) * 1) + ((((_lv0 * 128) + tl.arange(0, 128)) % 3) * 1)) < 131072))), other=0.0) * tl.load(in1_ptr + (((((((tl.program_id(0) // 131070) % 128) * 64) + (((_lv0 * 128) + tl.arange(0, 128)) // 3)) * 3) + (((_lv0 * 128) + tl.arange(0, 128)) % 3)) + 0 * tl.arange(0, 128)), mask=((((_lv0 * 128) + tl.arange(0, 128)) < 192) & ((0 <= (((tl.program_id(0) % 131070) * 1) + ((((_lv0 * 128) + tl.arange(0, 128)) % 3) * 1))) & ((((tl.program_id(0) % 131070) * 1) + ((((_lv0 * 128) + tl.arange(0, 128)) % 3) * 1)) < 131072))), other=0.0)), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t067(out, ins):
    grid = (268431360,)
    t067_kernel[grid](out, ins[0], ins[1])
    return out
