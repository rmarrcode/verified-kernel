import torch
import triton
import triton.language as tl


@triton.jit
def _mul_combine(a, b):
    return a * b


@triton.jit
def t050_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr):
    _acc0 = tl.zeros([256], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 256) + tl.arange(0, 256)) < 363) & ((((2 <= ((((tl.program_id(0) // 55) % 55) * 4) + ((((_lv0 * 256) + tl.arange(0, 256)) // 11) % 11))) & (((((tl.program_id(0) // 55) % 55) * 4) + ((((_lv0 * 256) + tl.arange(0, 256)) // 11) % 11)) < 226)) & (2 <= (((tl.program_id(0) % 55) * 4) + (((_lv0 * 256) + tl.arange(0, 256)) % 11)))) & ((((tl.program_id(0) % 55) * 4) + (((_lv0 * 256) + tl.arange(0, 256)) % 11)) < 226))), (tl.load(in0_ptr + ((((((((tl.program_id(0) // 290400) * 3) + (((_lv0 * 256) + tl.arange(0, 256)) // 121)) * 224) + tl.maximum(((((tl.program_id(0) // 55) % 55) * 4) + ((((_lv0 * 256) + tl.arange(0, 256)) // 11) % 11)) - 2, 0)) * 224) + tl.maximum((((tl.program_id(0) % 55) * 4) + (((_lv0 * 256) + tl.arange(0, 256)) % 11)) - 2, 0)) + 0 * tl.arange(0, 256)), mask=((((_lv0 * 256) + tl.arange(0, 256)) < 363) & ((((2 <= ((((tl.program_id(0) // 55) % 55) * 4) + ((((_lv0 * 256) + tl.arange(0, 256)) // 11) % 11))) & (((((tl.program_id(0) // 55) % 55) * 4) + ((((_lv0 * 256) + tl.arange(0, 256)) // 11) % 11)) < 226)) & (2 <= (((tl.program_id(0) % 55) * 4) + (((_lv0 * 256) + tl.arange(0, 256)) % 11)))) & ((((tl.program_id(0) % 55) * 4) + (((_lv0 * 256) + tl.arange(0, 256)) % 11)) < 226))), other=0.0) * tl.load(in1_ptr + (((((((((tl.program_id(0) // 3025) % 96) * 3) + (((_lv0 * 256) + tl.arange(0, 256)) // 121)) * 11) + ((((_lv0 * 256) + tl.arange(0, 256)) // 11) % 11)) * 11) + (((_lv0 * 256) + tl.arange(0, 256)) % 11)) + 0 * tl.arange(0, 256)), mask=((((_lv0 * 256) + tl.arange(0, 256)) < 363) & ((((2 <= ((((tl.program_id(0) // 55) % 55) * 4) + ((((_lv0 * 256) + tl.arange(0, 256)) // 11) % 11))) & (((((tl.program_id(0) // 55) % 55) * 4) + ((((_lv0 * 256) + tl.arange(0, 256)) // 11) % 11)) < 226)) & (2 <= (((tl.program_id(0) % 55) * 4) + (((_lv0 * 256) + tl.arange(0, 256)) % 11)))) & ((((tl.program_id(0) % 55) * 4) + (((_lv0 * 256) + tl.arange(0, 256)) % 11)) < 226))), other=0.0)), 0.0))
    _v = (tl.sum(_acc0, axis=0) + tl.load(in2_ptr + (((tl.program_id(0) // 3025) % 96))))
    tl.store(out_ptr + tl.program_id(0), _v)


def t050(out, ins):
    grid = (74342400,)
    t050_kernel[grid](out, ins[0], ins[1], ins[2])
    return out
