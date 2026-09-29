import torch
import triton
import triton.language as tl


@triton.jit
def _mul_combine(a, b):
    return a * b


@triton.jit
def iso3_kernel(out_ptr, in0_ptr, in1_ptr):
    _acc0 = tl.zeros([64], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 64) + tl.arange(0, 64)) < 72) & ((((1 <= ((((_lv0 * 64) + tl.arange(0, 64)) // 3) % 3)) & (((((_lv0 * 64) + tl.arange(0, 64)) // 3) % 3) < 2)) & (1 <= (((_lv0 * 64) + tl.arange(0, 64)) % 3))) & ((((_lv0 * 64) + tl.arange(0, 64)) % 3) < 2))), (tl.load(in0_ptr + ((((((tl.program_id(0) // 16) * 8) + (((_lv0 * 64) + tl.arange(0, 64)) // 9)) + tl.maximum(((((_lv0 * 64) + tl.arange(0, 64)) // 3) % 3) - 1, 0)) + tl.maximum((((_lv0 * 64) + tl.arange(0, 64)) % 3) - 1, 0)) + 0 * tl.arange(0, 64)), mask=((((_lv0 * 64) + tl.arange(0, 64)) < 72) & ((((1 <= ((((_lv0 * 64) + tl.arange(0, 64)) // 3) % 3)) & (((((_lv0 * 64) + tl.arange(0, 64)) // 3) % 3) < 2)) & (1 <= (((_lv0 * 64) + tl.arange(0, 64)) % 3))) & ((((_lv0 * 64) + tl.arange(0, 64)) % 3) < 2))), other=0.0) * tl.load(in1_ptr + ((((((((tl.program_id(0) % 16) * 8) + (((_lv0 * 64) + tl.arange(0, 64)) // 9)) * 3) + ((((_lv0 * 64) + tl.arange(0, 64)) // 3) % 3)) * 3) + (((_lv0 * 64) + tl.arange(0, 64)) % 3)) + 0 * tl.arange(0, 64)), mask=((((_lv0 * 64) + tl.arange(0, 64)) < 72) & ((((1 <= ((((_lv0 * 64) + tl.arange(0, 64)) // 3) % 3)) & (((((_lv0 * 64) + tl.arange(0, 64)) // 3) % 3) < 2)) & (1 <= (((_lv0 * 64) + tl.arange(0, 64)) % 3))) & ((((_lv0 * 64) + tl.arange(0, 64)) % 3) < 2))), other=0.0)), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def iso3(out, ins):
    grid = (32,)
    iso3_kernel[grid](out, ins[0], ins[1])
    return out
