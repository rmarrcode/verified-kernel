import torch
import triton
import triton.language as tl


@triton.jit
def _mul_combine(a, b):
    return a * b


@triton.jit
def t066_kernel(out_ptr, in0_ptr, in1_ptr):
    _acc0 = tl.zeros([256], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 256) + tl.arange(0, 256)) < 315) & ((((((tl.program_id(0) // 15128) % 14) + ((((_lv0 * 256) + tl.arange(0, 256)) // 35) % 3)) < 16) & ((((tl.program_id(0) // 122) % 124) + ((((_lv0 * 256) + tl.arange(0, 256)) // 7) % 5)) < 128)) & (((tl.program_id(0) % 122) + (((_lv0 * 256) + tl.arange(0, 256)) % 7)) < 128))), (tl.load(in0_ptr + ((((((((((tl.program_id(0) // 13554688) * 3) + (((_lv0 * 256) + tl.arange(0, 256)) // 105)) * 16) + (((tl.program_id(0) // 15128) % 14) + ((((_lv0 * 256) + tl.arange(0, 256)) // 35) % 3))) * 128) + (((tl.program_id(0) // 122) % 124) + ((((_lv0 * 256) + tl.arange(0, 256)) // 7) % 5))) * 128) + ((tl.program_id(0) % 122) + (((_lv0 * 256) + tl.arange(0, 256)) % 7))) + 0 * tl.arange(0, 256)), mask=((((_lv0 * 256) + tl.arange(0, 256)) < 315) & ((((((tl.program_id(0) // 15128) % 14) + ((((_lv0 * 256) + tl.arange(0, 256)) // 35) % 3)) < 16) & ((((tl.program_id(0) // 122) % 124) + ((((_lv0 * 256) + tl.arange(0, 256)) // 7) % 5)) < 128)) & (((tl.program_id(0) % 122) + (((_lv0 * 256) + tl.arange(0, 256)) % 7)) < 128))), other=0.0) * tl.load(in1_ptr + (((((((((((tl.program_id(0) // 211792) % 64) * 3) + (((_lv0 * 256) + tl.arange(0, 256)) // 105)) * 3) + ((((_lv0 * 256) + tl.arange(0, 256)) // 35) % 3)) * 5) + ((((_lv0 * 256) + tl.arange(0, 256)) // 7) % 5)) * 7) + (((_lv0 * 256) + tl.arange(0, 256)) % 7)) + 0 * tl.arange(0, 256)), mask=((((_lv0 * 256) + tl.arange(0, 256)) < 315) & ((((((tl.program_id(0) // 15128) % 14) + ((((_lv0 * 256) + tl.arange(0, 256)) // 35) % 3)) < 16) & ((((tl.program_id(0) // 122) % 124) + ((((_lv0 * 256) + tl.arange(0, 256)) // 7) % 5)) < 128)) & (((tl.program_id(0) % 122) + (((_lv0 * 256) + tl.arange(0, 256)) % 7)) < 128))), other=0.0)), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t066(out, ins):
    grid = (108437504,)
    t066_kernel[grid](out, ins[0], ins[1])
    return out
