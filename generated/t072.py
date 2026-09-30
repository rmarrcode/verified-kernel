import torch
import triton
import triton.language as tl


@triton.jit
def _mul_combine(a, b):
    return a * b


@triton.jit
def t072_kernel(out_ptr, in0_ptr, in1_ptr):
    _acc0 = tl.zeros([512], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 512) + tl.arange(0, 512)) < 840) & (((((((((((((_lv0 * 512) + tl.arange(0, 512)) // 35) % 3) <= (((tl.program_id(0) // 4608) % 24) + 1)) & ((tl.maximum((((tl.program_id(0) // 4608) % 24) + 1) - ((((_lv0 * 512) + tl.arange(0, 512)) // 35) % 3), 0) % 2) == 0)) & ((tl.maximum((((tl.program_id(0) // 4608) % 24) + 1) - ((((_lv0 * 512) + tl.arange(0, 512)) // 35) % 3), 0) // 2) < 12)) & (((((_lv0 * 512) + tl.arange(0, 512)) // 7) % 5) <= (((tl.program_id(0) // 96) % 48) + 2))) & ((tl.maximum((((tl.program_id(0) // 96) % 48) + 2) - ((((_lv0 * 512) + tl.arange(0, 512)) // 7) % 5), 0) % 2) == 0)) & ((tl.maximum((((tl.program_id(0) // 96) % 48) + 2) - ((((_lv0 * 512) + tl.arange(0, 512)) // 7) % 5), 0) // 2) < 24)) & ((((_lv0 * 512) + tl.arange(0, 512)) % 7) <= ((tl.program_id(0) % 96) + 3))) & ((tl.maximum(((tl.program_id(0) % 96) + 3) - (((_lv0 * 512) + tl.arange(0, 512)) % 7), 0) % 2) == 0)) & ((tl.maximum(((tl.program_id(0) % 96) + 3) - (((_lv0 * 512) + tl.arange(0, 512)) % 7), 0) // 2) < 48))), (tl.load(in0_ptr + ((((((((((tl.program_id(0) // 3538944) * 32) + (((((tl.program_id(0) // 110592) % 32) // 8) * 8) + (((_lv0 * 512) + tl.arange(0, 512)) // 105))) * 12) + (tl.maximum((((tl.program_id(0) // 4608) % 24) + 1) - ((((_lv0 * 512) + tl.arange(0, 512)) // 35) % 3), 0) // 2)) * 24) + (tl.maximum((((tl.program_id(0) // 96) % 48) + 2) - ((((_lv0 * 512) + tl.arange(0, 512)) // 7) % 5), 0) // 2)) * 48) + (tl.maximum(((tl.program_id(0) % 96) + 3) - (((_lv0 * 512) + tl.arange(0, 512)) % 7), 0) // 2)) + 0 * tl.arange(0, 512)), mask=((((_lv0 * 512) + tl.arange(0, 512)) < 840) & (((((((((((((_lv0 * 512) + tl.arange(0, 512)) // 35) % 3) <= (((tl.program_id(0) // 4608) % 24) + 1)) & ((tl.maximum((((tl.program_id(0) // 4608) % 24) + 1) - ((((_lv0 * 512) + tl.arange(0, 512)) // 35) % 3), 0) % 2) == 0)) & ((tl.maximum((((tl.program_id(0) // 4608) % 24) + 1) - ((((_lv0 * 512) + tl.arange(0, 512)) // 35) % 3), 0) // 2) < 12)) & (((((_lv0 * 512) + tl.arange(0, 512)) // 7) % 5) <= (((tl.program_id(0) // 96) % 48) + 2))) & ((tl.maximum((((tl.program_id(0) // 96) % 48) + 2) - ((((_lv0 * 512) + tl.arange(0, 512)) // 7) % 5), 0) % 2) == 0)) & ((tl.maximum((((tl.program_id(0) // 96) % 48) + 2) - ((((_lv0 * 512) + tl.arange(0, 512)) // 7) % 5), 0) // 2) < 24)) & ((((_lv0 * 512) + tl.arange(0, 512)) % 7) <= ((tl.program_id(0) % 96) + 3))) & ((tl.maximum(((tl.program_id(0) % 96) + 3) - (((_lv0 * 512) + tl.arange(0, 512)) % 7), 0) % 2) == 0)) & ((tl.maximum(((tl.program_id(0) % 96) + 3) - (((_lv0 * 512) + tl.arange(0, 512)) % 7), 0) // 2) < 48))), other=0.0) * tl.load(in1_ptr + ((((((((((((((tl.program_id(0) // 110592) % 32) // 8) * 8) + (((_lv0 * 512) + tl.arange(0, 512)) // 105)) * 8) + (((tl.program_id(0) // 110592) % 32) % 8)) * 3) + ((((_lv0 * 512) + tl.arange(0, 512)) // 35) % 3)) * 5) + ((((_lv0 * 512) + tl.arange(0, 512)) // 7) % 5)) * 7) + (((_lv0 * 512) + tl.arange(0, 512)) % 7)) + 0 * tl.arange(0, 512)), mask=((((_lv0 * 512) + tl.arange(0, 512)) < 840) & (((((((((((((_lv0 * 512) + tl.arange(0, 512)) // 35) % 3) <= (((tl.program_id(0) // 4608) % 24) + 1)) & ((tl.maximum((((tl.program_id(0) // 4608) % 24) + 1) - ((((_lv0 * 512) + tl.arange(0, 512)) // 35) % 3), 0) % 2) == 0)) & ((tl.maximum((((tl.program_id(0) // 4608) % 24) + 1) - ((((_lv0 * 512) + tl.arange(0, 512)) // 35) % 3), 0) // 2) < 12)) & (((((_lv0 * 512) + tl.arange(0, 512)) // 7) % 5) <= (((tl.program_id(0) // 96) % 48) + 2))) & ((tl.maximum((((tl.program_id(0) // 96) % 48) + 2) - ((((_lv0 * 512) + tl.arange(0, 512)) // 7) % 5), 0) % 2) == 0)) & ((tl.maximum((((tl.program_id(0) // 96) % 48) + 2) - ((((_lv0 * 512) + tl.arange(0, 512)) // 7) % 5), 0) // 2) < 24)) & ((((_lv0 * 512) + tl.arange(0, 512)) % 7) <= ((tl.program_id(0) % 96) + 3))) & ((tl.maximum(((tl.program_id(0) % 96) + 3) - (((_lv0 * 512) + tl.arange(0, 512)) % 7), 0) % 2) == 0)) & ((tl.maximum(((tl.program_id(0) % 96) + 3) - (((_lv0 * 512) + tl.arange(0, 512)) % 7), 0) // 2) < 48))), other=0.0)), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t072(out, ins):
    grid = (28311552,)
    t072_kernel[grid](out, ins[0], ins[1])
    return out
