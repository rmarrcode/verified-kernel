import torch
import triton
import triton.language as tl


@triton.jit
def _mul_combine(a, b):
    return a * b


@triton.jit
def iso2_kernel(out_ptr, in0_ptr, in1_ptr):
    _acc0 = tl.zeros([8], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 8) + tl.arange(0, 8)) < 9) & ((((1 <= ((((_lv0 * 8) + tl.arange(0, 8)) // 3) % 3)) & (((((_lv0 * 8) + tl.arange(0, 8)) // 3) % 3) < 3)) & (1 <= (((_lv0 * 8) + tl.arange(0, 8)) % 3))) & ((((_lv0 * 8) + tl.arange(0, 8)) % 3) < 3))), (tl.load(in0_ptr + ((((((((tl.program_id(0) // 8) * 8) + (tl.program_id(0) % 8)) * 2) + tl.maximum(((((_lv0 * 8) + tl.arange(0, 8)) // 3) % 3) - 1, 0)) * 2) + tl.maximum((((_lv0 * 8) + tl.arange(0, 8)) % 3) - 1, 0)) + 0 * tl.arange(0, 8)), mask=((((_lv0 * 8) + tl.arange(0, 8)) < 9) & ((((1 <= ((((_lv0 * 8) + tl.arange(0, 8)) // 3) % 3)) & (((((_lv0 * 8) + tl.arange(0, 8)) // 3) % 3) < 3)) & (1 <= (((_lv0 * 8) + tl.arange(0, 8)) % 3))) & ((((_lv0 * 8) + tl.arange(0, 8)) % 3) < 3))), other=0.0) * tl.load(in1_ptr + ((((((tl.program_id(0) % 8) * 3) + ((((_lv0 * 8) + tl.arange(0, 8)) // 3) % 3)) * 3) + (((_lv0 * 8) + tl.arange(0, 8)) % 3)) + 0 * tl.arange(0, 8)), mask=((((_lv0 * 8) + tl.arange(0, 8)) < 9) & ((((1 <= ((((_lv0 * 8) + tl.arange(0, 8)) // 3) % 3)) & (((((_lv0 * 8) + tl.arange(0, 8)) // 3) % 3) < 3)) & (1 <= (((_lv0 * 8) + tl.arange(0, 8)) % 3))) & ((((_lv0 * 8) + tl.arange(0, 8)) % 3) < 3))), other=0.0)), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def iso2(out, ins):
    grid = (16,)
    iso2_kernel[grid](out, ins[0], ins[1])
    return out
