import torch
import triton
import triton.language as tl


@triton.jit
def _mul_combine(a, b):
    return a * b


@triton.jit
def t079_kernel(out_ptr, in0_ptr, in1_ptr):
    _acc0 = tl.zeros([64], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 64) + tl.arange(0, 64)) < 96) & (((((((_lv0 * 64) + tl.arange(0, 64)) % 3) * 2) <= ((tl.program_id(0) % 262145) + 1)) & ((tl.maximum(((tl.program_id(0) % 262145) + 1) - ((((_lv0 * 64) + tl.arange(0, 64)) % 3) * 2), 0) % 2) == 0)) & ((tl.maximum(((tl.program_id(0) % 262145) + 1) - ((((_lv0 * 64) + tl.arange(0, 64)) % 3) * 2), 0) // 2) < 131072))), (tl.load(in0_ptr + ((((((tl.program_id(0) // 16777280) * 32) + (((((tl.program_id(0) // 262145) % 64) // 64) * 32) + (((_lv0 * 64) + tl.arange(0, 64)) // 3))) * 131072) + (tl.maximum(((tl.program_id(0) % 262145) + 1) - ((((_lv0 * 64) + tl.arange(0, 64)) % 3) * 2), 0) // 2)) + 0 * tl.arange(0, 64)), mask=((((_lv0 * 64) + tl.arange(0, 64)) < 96) & (((((((_lv0 * 64) + tl.arange(0, 64)) % 3) * 2) <= ((tl.program_id(0) % 262145) + 1)) & ((tl.maximum(((tl.program_id(0) % 262145) + 1) - ((((_lv0 * 64) + tl.arange(0, 64)) % 3) * 2), 0) % 2) == 0)) & ((tl.maximum(((tl.program_id(0) % 262145) + 1) - ((((_lv0 * 64) + tl.arange(0, 64)) % 3) * 2), 0) // 2) < 131072))), other=0.0) * tl.load(in1_ptr + ((((((((((tl.program_id(0) // 262145) % 64) // 64) * 32) + (((_lv0 * 64) + tl.arange(0, 64)) // 3)) * 64) + (((tl.program_id(0) // 262145) % 64) % 64)) * 3) + (((_lv0 * 64) + tl.arange(0, 64)) % 3)) + 0 * tl.arange(0, 64)), mask=((((_lv0 * 64) + tl.arange(0, 64)) < 96) & (((((((_lv0 * 64) + tl.arange(0, 64)) % 3) * 2) <= ((tl.program_id(0) % 262145) + 1)) & ((tl.maximum(((tl.program_id(0) % 262145) + 1) - ((((_lv0 * 64) + tl.arange(0, 64)) % 3) * 2), 0) % 2) == 0)) & ((tl.maximum(((tl.program_id(0) % 262145) + 1) - ((((_lv0 * 64) + tl.arange(0, 64)) % 3) * 2), 0) // 2) < 131072))), other=0.0)), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t079(out, ins):
    grid = (268436480,)
    t079_kernel[grid](out, ins[0], ins[1])
    return out
