import torch
import triton
import triton.language as tl


@triton.jit
def t060_kernel(out_ptr, in0_ptr, in1_ptr):
    _acc0 = tl.zeros([256], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 256) + tl.arange(0, 256)) < 315) & ((((((0 <= ((((tl.program_id(0) // 3480) % 62) * 1) + (((((_lv0 * 256) + tl.arange(0, 256)) // 35) % 3) * 1))) & (((((tl.program_id(0) // 3480) % 62) * 1) + (((((_lv0 * 256) + tl.arange(0, 256)) // 35) % 3) * 1)) < 64)) & (0 <= ((((tl.program_id(0) // 58) % 60) * 1) + (((((_lv0 * 256) + tl.arange(0, 256)) // 7) % 5) * 1)))) & (((((tl.program_id(0) // 58) % 60) * 1) + (((((_lv0 * 256) + tl.arange(0, 256)) // 7) % 5) * 1)) < 64)) & (0 <= (((tl.program_id(0) % 58) * 1) + ((((_lv0 * 256) + tl.arange(0, 256)) % 7) * 1)))) & ((((tl.program_id(0) % 58) * 1) + ((((_lv0 * 256) + tl.arange(0, 256)) % 7) * 1)) < 64))), (tl.load(in0_ptr + ((((((((((tl.program_id(0) // 13808640) * 3) + (((((tl.program_id(0) // 215760) % 64) // 64) * 3) + (((_lv0 * 256) + tl.arange(0, 256)) // 105))) * 64) + tl.maximum(((((tl.program_id(0) // 3480) % 62) * 1) + (((((_lv0 * 256) + tl.arange(0, 256)) // 35) % 3) * 1)) - 0, 0)) * 64) + tl.maximum(((((tl.program_id(0) // 58) % 60) * 1) + (((((_lv0 * 256) + tl.arange(0, 256)) // 7) % 5) * 1)) - 0, 0)) * 64) + tl.maximum((((tl.program_id(0) % 58) * 1) + ((((_lv0 * 256) + tl.arange(0, 256)) % 7) * 1)) - 0, 0)) + 0 * tl.arange(0, 256)), mask=((((_lv0 * 256) + tl.arange(0, 256)) < 315) & ((((((0 <= ((((tl.program_id(0) // 3480) % 62) * 1) + (((((_lv0 * 256) + tl.arange(0, 256)) // 35) % 3) * 1))) & (((((tl.program_id(0) // 3480) % 62) * 1) + (((((_lv0 * 256) + tl.arange(0, 256)) // 35) % 3) * 1)) < 64)) & (0 <= ((((tl.program_id(0) // 58) % 60) * 1) + (((((_lv0 * 256) + tl.arange(0, 256)) // 7) % 5) * 1)))) & (((((tl.program_id(0) // 58) % 60) * 1) + (((((_lv0 * 256) + tl.arange(0, 256)) // 7) % 5) * 1)) < 64)) & (0 <= (((tl.program_id(0) % 58) * 1) + ((((_lv0 * 256) + tl.arange(0, 256)) % 7) * 1)))) & ((((tl.program_id(0) % 58) * 1) + ((((_lv0 * 256) + tl.arange(0, 256)) % 7) * 1)) < 64))), other=0.0) * tl.load(in1_ptr + (((((((((((tl.program_id(0) // 215760) % 64) * 3) + (((_lv0 * 256) + tl.arange(0, 256)) // 105)) * 3) + ((((_lv0 * 256) + tl.arange(0, 256)) // 35) % 3)) * 5) + ((((_lv0 * 256) + tl.arange(0, 256)) // 7) % 5)) * 7) + (((_lv0 * 256) + tl.arange(0, 256)) % 7)) + 0 * tl.arange(0, 256)), mask=((((_lv0 * 256) + tl.arange(0, 256)) < 315) & ((((((0 <= ((((tl.program_id(0) // 3480) % 62) * 1) + (((((_lv0 * 256) + tl.arange(0, 256)) // 35) % 3) * 1))) & (((((tl.program_id(0) // 3480) % 62) * 1) + (((((_lv0 * 256) + tl.arange(0, 256)) // 35) % 3) * 1)) < 64)) & (0 <= ((((tl.program_id(0) // 58) % 60) * 1) + (((((_lv0 * 256) + tl.arange(0, 256)) // 7) % 5) * 1)))) & (((((tl.program_id(0) // 58) % 60) * 1) + (((((_lv0 * 256) + tl.arange(0, 256)) // 7) % 5) * 1)) < 64)) & (0 <= (((tl.program_id(0) % 58) * 1) + ((((_lv0 * 256) + tl.arange(0, 256)) % 7) * 1)))) & ((((tl.program_id(0) % 58) * 1) + ((((_lv0 * 256) + tl.arange(0, 256)) % 7) * 1)) < 64))), other=0.0)), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t060(out, ins):
    grid = (220938240,)
    t060_kernel[grid](out, ins[0], ins[1])
    return out
