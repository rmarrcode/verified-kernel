import torch
import triton
import triton.language as tl


@triton.jit
def _mul_combine(a, b):
    return a * b


@triton.jit
def t046_kernel(out_ptr, in0_ptr):
    _acc0 = tl.zeros([16], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 16) + tl.arange(0, 16)) < 27) & ((((((1 <= ((((tl.program_id(0) // 8192) % 64) * 2) + (((_lv0 * 16) + tl.arange(0, 16)) // 9))) & (((((tl.program_id(0) // 8192) % 64) * 2) + (((_lv0 * 16) + tl.arange(0, 16)) // 9)) < 129)) & (1 <= ((((tl.program_id(0) // 128) % 64) * 2) + ((((_lv0 * 16) + tl.arange(0, 16)) // 3) % 3)))) & (((((tl.program_id(0) // 128) % 64) * 2) + ((((_lv0 * 16) + tl.arange(0, 16)) // 3) % 3)) < 129)) & (1 <= (((tl.program_id(0) % 128) * 2) + (((_lv0 * 16) + tl.arange(0, 16)) % 3)))) & ((((tl.program_id(0) % 128) * 2) + (((_lv0 * 16) + tl.arange(0, 16)) % 3)) < 257))), tl.load(in0_ptr + ((((((((((tl.program_id(0) // 16777216) * 32) + ((tl.program_id(0) // 524288) % 32)) * 128) + tl.maximum(((((tl.program_id(0) // 8192) % 64) * 2) + (((_lv0 * 16) + tl.arange(0, 16)) // 9)) - 1, 0)) * 128) + tl.maximum(((((tl.program_id(0) // 128) % 64) * 2) + ((((_lv0 * 16) + tl.arange(0, 16)) // 3) % 3)) - 1, 0)) * 256) + tl.maximum((((tl.program_id(0) % 128) * 2) + (((_lv0 * 16) + tl.arange(0, 16)) % 3)) - 1, 0)) + 0 * tl.arange(0, 16)), mask=((((_lv0 * 16) + tl.arange(0, 16)) < 27) & ((((((1 <= ((((tl.program_id(0) // 8192) % 64) * 2) + (((_lv0 * 16) + tl.arange(0, 16)) // 9))) & (((((tl.program_id(0) // 8192) % 64) * 2) + (((_lv0 * 16) + tl.arange(0, 16)) // 9)) < 129)) & (1 <= ((((tl.program_id(0) // 128) % 64) * 2) + ((((_lv0 * 16) + tl.arange(0, 16)) // 3) % 3)))) & (((((tl.program_id(0) // 128) % 64) * 2) + ((((_lv0 * 16) + tl.arange(0, 16)) // 3) % 3)) < 129)) & (1 <= (((tl.program_id(0) % 128) * 2) + (((_lv0 * 16) + tl.arange(0, 16)) % 3)))) & ((((tl.program_id(0) % 128) * 2) + (((_lv0 * 16) + tl.arange(0, 16)) % 3)) < 257))), other=0.0), 0.0))
    _v = (tl.sum(_acc0, axis=0) * (1.0 * (1.0 / 27.0)))
    tl.store(out_ptr + tl.program_id(0), _v)


def t046(out, ins):
    grid = (134217728,)
    t046_kernel[grid](out, ins[0])
    return out
