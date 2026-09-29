import torch
import triton
import triton.language as tl


@triton.jit
def t063_kernel(out_ptr, in0_ptr, in1_ptr):
    _acc0 = tl.zeros([128], dtype=tl.float32)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 128) + tl.arange(0, 128)) < 144) & ((((0 <= ((((tl.program_id(0) // 1022) % 1022) * 1) + (((((_lv0 * 128) + tl.arange(0, 128)) // 3) % 3) * 1))) & (((((tl.program_id(0) // 1022) % 1022) * 1) + (((((_lv0 * 128) + tl.arange(0, 128)) // 3) % 3) * 1)) < 1024)) & (0 <= (((tl.program_id(0) % 1022) * 1) + ((((_lv0 * 128) + tl.arange(0, 128)) % 3) * 1)))) & ((((tl.program_id(0) % 1022) * 1) + ((((_lv0 * 128) + tl.arange(0, 128)) % 3) * 1)) < 1024))), (tl.load(in0_ptr + ((((((((tl.program_id(0) // 133693952) * 16) + (((((tl.program_id(0) // 1044484) % 128) // 128) * 16) + (((_lv0 * 128) + tl.arange(0, 128)) // 9))) * 1024) + tl.maximum(((((tl.program_id(0) // 1022) % 1022) * 1) + (((((_lv0 * 128) + tl.arange(0, 128)) // 3) % 3) * 1)) - 0, 0)) * 1024) + tl.maximum((((tl.program_id(0) % 1022) * 1) + ((((_lv0 * 128) + tl.arange(0, 128)) % 3) * 1)) - 0, 0))), mask=((((_lv0 * 128) + tl.arange(0, 128)) < 144) & ((((0 <= ((((tl.program_id(0) // 1022) % 1022) * 1) + (((((_lv0 * 128) + tl.arange(0, 128)) // 3) % 3) * 1))) & (((((tl.program_id(0) // 1022) % 1022) * 1) + (((((_lv0 * 128) + tl.arange(0, 128)) // 3) % 3) * 1)) < 1024)) & (0 <= (((tl.program_id(0) % 1022) * 1) + ((((_lv0 * 128) + tl.arange(0, 128)) % 3) * 1)))) & ((((tl.program_id(0) % 1022) * 1) + ((((_lv0 * 128) + tl.arange(0, 128)) % 3) * 1)) < 1024))), other=0.0) * tl.load(in1_ptr + (((((((((tl.program_id(0) // 1044484) % 128) * 16) + (((_lv0 * 128) + tl.arange(0, 128)) // 9)) * 3) + ((((_lv0 * 128) + tl.arange(0, 128)) // 3) % 3)) * 3) + (((_lv0 * 128) + tl.arange(0, 128)) % 3))), mask=((((_lv0 * 128) + tl.arange(0, 128)) < 144) & ((((0 <= ((((tl.program_id(0) // 1022) % 1022) * 1) + (((((_lv0 * 128) + tl.arange(0, 128)) // 3) % 3) * 1))) & (((((tl.program_id(0) // 1022) % 1022) * 1) + (((((_lv0 * 128) + tl.arange(0, 128)) // 3) % 3) * 1)) < 1024)) & (0 <= (((tl.program_id(0) % 1022) * 1) + ((((_lv0 * 128) + tl.arange(0, 128)) % 3) * 1)))) & ((((tl.program_id(0) % 1022) * 1) + ((((_lv0 * 128) + tl.arange(0, 128)) % 3) * 1)) < 1024))), other=0.0)), 0.0))
    _v = tl.where(True, tl.sum(_acc0, axis=0), 0.0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t063(out, ins):
    grid = (534775808,)
    t063_kernel[grid](out, ins[0], ins[1])
    return out
