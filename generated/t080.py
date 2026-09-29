import torch
import triton
import triton.language as tl


@triton.jit
def t080_kernel(out_ptr, in0_ptr, in1_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 1440) & ((((2 <= ((((tl.program_id(0) // 496) % 508) * 1) + (((((_lv0 * 1024) + tl.arange(0, 1024)) // 9) % 5) * 2))) & (((((tl.program_id(0) // 496) % 508) * 1) + (((((_lv0 * 1024) + tl.arange(0, 1024)) // 9) % 5) * 2)) < 514)) & (4 <= (((tl.program_id(0) % 496) * 1) + ((((_lv0 * 1024) + tl.arange(0, 1024)) % 9) * 3)))) & ((((tl.program_id(0) % 496) * 1) + ((((_lv0 * 1024) + tl.arange(0, 1024)) % 9) * 3)) < 516))), (tl.load(in0_ptr + ((((((((tl.program_id(0) // 16125952) * 32) + (((((tl.program_id(0) // 251968) % 64) // 64) * 32) + (((_lv0 * 1024) + tl.arange(0, 1024)) // 45))) * 512) + tl.maximum(((((tl.program_id(0) // 496) % 508) * 1) + (((((_lv0 * 1024) + tl.arange(0, 1024)) // 9) % 5) * 2)) - 2, 0)) * 512) + tl.maximum((((tl.program_id(0) % 496) * 1) + ((((_lv0 * 1024) + tl.arange(0, 1024)) % 9) * 3)) - 4, 0)) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 1440) & ((((2 <= ((((tl.program_id(0) // 496) % 508) * 1) + (((((_lv0 * 1024) + tl.arange(0, 1024)) // 9) % 5) * 2))) & (((((tl.program_id(0) // 496) % 508) * 1) + (((((_lv0 * 1024) + tl.arange(0, 1024)) // 9) % 5) * 2)) < 514)) & (4 <= (((tl.program_id(0) % 496) * 1) + ((((_lv0 * 1024) + tl.arange(0, 1024)) % 9) * 3)))) & ((((tl.program_id(0) % 496) * 1) + ((((_lv0 * 1024) + tl.arange(0, 1024)) % 9) * 3)) < 516))), other=0.0) * tl.load(in1_ptr + (((((((((tl.program_id(0) // 251968) % 64) * 32) + (((_lv0 * 1024) + tl.arange(0, 1024)) // 45)) * 5) + ((((_lv0 * 1024) + tl.arange(0, 1024)) // 9) % 5)) * 9) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 9)) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 1440) & ((((2 <= ((((tl.program_id(0) // 496) % 508) * 1) + (((((_lv0 * 1024) + tl.arange(0, 1024)) // 9) % 5) * 2))) & (((((tl.program_id(0) // 496) % 508) * 1) + (((((_lv0 * 1024) + tl.arange(0, 1024)) // 9) % 5) * 2)) < 514)) & (4 <= (((tl.program_id(0) % 496) * 1) + ((((_lv0 * 1024) + tl.arange(0, 1024)) % 9) * 3)))) & ((((tl.program_id(0) % 496) * 1) + ((((_lv0 * 1024) + tl.arange(0, 1024)) % 9) * 3)) < 516))), other=0.0)), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t080(out, ins):
    grid = (129007616,)
    t080_kernel[grid](out, ins[0], ins[1])
    return out
