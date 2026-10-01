import torch
import triton
import triton.language as tl


@triton.jit
def _mul_combine(a, b):
    return a * b


@triton.jit
def t059_kernel(out_ptr, in0_ptr, in1_ptr):
    _acc0 = tl.zeros([16], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 16) + tl.arange(0, 16)) < 27) & ((((((tl.program_id(0) // 2540) % 254) + ((((_lv0 * 16) + tl.arange(0, 16)) // 3) % 3)) < 256) & ((((tl.program_id(0) // 10) % 254) + (((_lv0 * 16) + tl.arange(0, 16)) % 3)) < 256)) & ((tl.program_id(0) % 10) < 10))), (tl.load(in0_ptr + ((((((((((tl.program_id(0) // 41290240) * 3) + (((_lv0 * 16) + tl.arange(0, 16)) // 9)) * 256) + (((tl.program_id(0) // 2540) % 254) + ((((_lv0 * 16) + tl.arange(0, 16)) // 3) % 3))) * 256) + (((tl.program_id(0) // 10) % 254) + (((_lv0 * 16) + tl.arange(0, 16)) % 3))) * 10) + (tl.program_id(0) % 10)) + 0 * tl.arange(0, 16)), mask=((((_lv0 * 16) + tl.arange(0, 16)) < 27) & ((((((tl.program_id(0) // 2540) % 254) + ((((_lv0 * 16) + tl.arange(0, 16)) // 3) % 3)) < 256) & ((((tl.program_id(0) // 10) % 254) + (((_lv0 * 16) + tl.arange(0, 16)) % 3)) < 256)) & ((tl.program_id(0) % 10) < 10))), other=0.0) * tl.load(in1_ptr + (((((((((tl.program_id(0) // 645160) % 64) * 3) + (((_lv0 * 16) + tl.arange(0, 16)) // 9)) * 3) + ((((_lv0 * 16) + tl.arange(0, 16)) // 3) % 3)) * 3) + (((_lv0 * 16) + tl.arange(0, 16)) % 3)) + 0 * tl.arange(0, 16)), mask=((((_lv0 * 16) + tl.arange(0, 16)) < 27) & ((((((tl.program_id(0) // 2540) % 254) + ((((_lv0 * 16) + tl.arange(0, 16)) // 3) % 3)) < 256) & ((((tl.program_id(0) // 10) % 254) + (((_lv0 * 16) + tl.arange(0, 16)) % 3)) < 256)) & ((tl.program_id(0) % 10) < 10))), other=0.0)), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t059(out, ins):
    grid = (330321920,)
    t059_kernel[grid](out, ins[0], ins[1])
    return out
