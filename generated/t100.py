import torch
import triton
import triton.language as tl


@triton.jit
def _mul_combine(a, b):
    return a * b


@triton.jit
def t100_s0_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 1728) & (((((((((((((_lv0 * 1024) + tl.arange(0, 1024)) // 9) % 3) <= (((tl.program_id(0) // 9025) % 47) + 1)) & ((tl.maximum((((tl.program_id(0) // 9025) % 47) + 1) - ((((_lv0 * 1024) + tl.arange(0, 1024)) // 9) % 3), 0) % 2) == 0)) & ((tl.maximum((((tl.program_id(0) // 9025) % 47) + 1) - ((((_lv0 * 1024) + tl.arange(0, 1024)) // 9) % 3), 0) // 2) < 24)) & (((((_lv0 * 1024) + tl.arange(0, 1024)) // 3) % 3) <= (((tl.program_id(0) // 95) % 95) + 1))) & ((tl.maximum((((tl.program_id(0) // 95) % 95) + 1) - ((((_lv0 * 1024) + tl.arange(0, 1024)) // 3) % 3), 0) % 2) == 0)) & ((tl.maximum((((tl.program_id(0) // 95) % 95) + 1) - ((((_lv0 * 1024) + tl.arange(0, 1024)) // 3) % 3), 0) // 2) < 48)) & ((((_lv0 * 1024) + tl.arange(0, 1024)) % 3) <= ((tl.program_id(0) % 95) + 1))) & ((tl.maximum(((tl.program_id(0) % 95) + 1) - (((_lv0 * 1024) + tl.arange(0, 1024)) % 3), 0) % 2) == 0)) & ((tl.maximum(((tl.program_id(0) % 95) + 1) - (((_lv0 * 1024) + tl.arange(0, 1024)) % 3), 0) // 2) < 48))), (tl.load(in0_ptr + ((((((((((tl.program_id(0) // 54294400) * 64) + (((((tl.program_id(0) // 424175) % 128) // 128) * 64) + (((_lv0 * 1024) + tl.arange(0, 1024)) // 27))) * 24) + (tl.maximum((((tl.program_id(0) // 9025) % 47) + 1) - ((((_lv0 * 1024) + tl.arange(0, 1024)) // 9) % 3), 0) // 2)) * 48) + (tl.maximum((((tl.program_id(0) // 95) % 95) + 1) - ((((_lv0 * 1024) + tl.arange(0, 1024)) // 3) % 3), 0) // 2)) * 48) + (tl.maximum(((tl.program_id(0) % 95) + 1) - (((_lv0 * 1024) + tl.arange(0, 1024)) % 3), 0) // 2)) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 1728) & (((((((((((((_lv0 * 1024) + tl.arange(0, 1024)) // 9) % 3) <= (((tl.program_id(0) // 9025) % 47) + 1)) & ((tl.maximum((((tl.program_id(0) // 9025) % 47) + 1) - ((((_lv0 * 1024) + tl.arange(0, 1024)) // 9) % 3), 0) % 2) == 0)) & ((tl.maximum((((tl.program_id(0) // 9025) % 47) + 1) - ((((_lv0 * 1024) + tl.arange(0, 1024)) // 9) % 3), 0) // 2) < 24)) & (((((_lv0 * 1024) + tl.arange(0, 1024)) // 3) % 3) <= (((tl.program_id(0) // 95) % 95) + 1))) & ((tl.maximum((((tl.program_id(0) // 95) % 95) + 1) - ((((_lv0 * 1024) + tl.arange(0, 1024)) // 3) % 3), 0) % 2) == 0)) & ((tl.maximum((((tl.program_id(0) // 95) % 95) + 1) - ((((_lv0 * 1024) + tl.arange(0, 1024)) // 3) % 3), 0) // 2) < 48)) & ((((_lv0 * 1024) + tl.arange(0, 1024)) % 3) <= ((tl.program_id(0) % 95) + 1))) & ((tl.maximum(((tl.program_id(0) % 95) + 1) - (((_lv0 * 1024) + tl.arange(0, 1024)) % 3), 0) % 2) == 0)) & ((tl.maximum(((tl.program_id(0) % 95) + 1) - (((_lv0 * 1024) + tl.arange(0, 1024)) % 3), 0) // 2) < 48))), other=0.0) * tl.load(in1_ptr + ((((((((((((((tl.program_id(0) // 424175) % 128) // 128) * 64) + (((_lv0 * 1024) + tl.arange(0, 1024)) // 27)) * 128) + (((tl.program_id(0) // 424175) % 128) % 128)) * 3) + ((((_lv0 * 1024) + tl.arange(0, 1024)) // 9) % 3)) * 3) + ((((_lv0 * 1024) + tl.arange(0, 1024)) // 3) % 3)) * 3) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 3)) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 1728) & (((((((((((((_lv0 * 1024) + tl.arange(0, 1024)) // 9) % 3) <= (((tl.program_id(0) // 9025) % 47) + 1)) & ((tl.maximum((((tl.program_id(0) // 9025) % 47) + 1) - ((((_lv0 * 1024) + tl.arange(0, 1024)) // 9) % 3), 0) % 2) == 0)) & ((tl.maximum((((tl.program_id(0) // 9025) % 47) + 1) - ((((_lv0 * 1024) + tl.arange(0, 1024)) // 9) % 3), 0) // 2) < 24)) & (((((_lv0 * 1024) + tl.arange(0, 1024)) // 3) % 3) <= (((tl.program_id(0) // 95) % 95) + 1))) & ((tl.maximum((((tl.program_id(0) // 95) % 95) + 1) - ((((_lv0 * 1024) + tl.arange(0, 1024)) // 3) % 3), 0) % 2) == 0)) & ((tl.maximum((((tl.program_id(0) // 95) % 95) + 1) - ((((_lv0 * 1024) + tl.arange(0, 1024)) // 3) % 3), 0) // 2) < 48)) & ((((_lv0 * 1024) + tl.arange(0, 1024)) % 3) <= ((tl.program_id(0) % 95) + 1))) & ((tl.maximum(((tl.program_id(0) % 95) + 1) - (((_lv0 * 1024) + tl.arange(0, 1024)) % 3), 0) % 2) == 0)) & ((tl.maximum(((tl.program_id(0) % 95) + 1) - (((_lv0 * 1024) + tl.arange(0, 1024)) % 3), 0) // 2) < 48))), other=0.0)), 0.0))
    _v = (tl.maximum((tl.sum(_acc0, axis=0) + tl.load(in2_ptr + (((tl.program_id(0) // 424175) % 128)))), (0.0 - (1.0 * (1.0 / 1.0)))) / (2.0 * (1.0 / 1.0)))
    tl.store(out_ptr + tl.program_id(0), _v)


def t100_s0(out, ins):
    grid = (434355200,)
    t100_s0_kernel[grid](out, ins[0], ins[1], ins[2])
    return out


def t100(out, ins):
    t100_s0(out, list(ins))
    return out
