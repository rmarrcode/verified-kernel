import torch
import triton
import triton.language as tl


@triton.jit
def t087_kernel(out_ptr, in0_ptr, in1_ptr):
    _acc0 = tl.zeros([64], dtype=tl.float32)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 64) + tl.arange(0, 64)) < 64) & ((((0 <= ((((tl.program_id(0) // 1024) % 1024) * 1) + ((((_lv0 * 64) + tl.arange(0, 64)) % 1) * 1))) & (((((tl.program_id(0) // 1024) % 1024) * 1) + ((((_lv0 * 64) + tl.arange(0, 64)) % 1) * 1)) < 1024)) & (0 <= (((tl.program_id(0) % 1024) * 1) + ((((_lv0 * 64) + tl.arange(0, 64)) % 1) * 1)))) & ((((tl.program_id(0) % 1024) * 1) + ((((_lv0 * 64) + tl.arange(0, 64)) % 1) * 1)) < 1024))), (tl.load(in0_ptr + ((((((((tl.program_id(0) // 134217728) * 64) + (((((tl.program_id(0) // 1048576) % 128) // 128) * 64) + ((_lv0 * 64) + tl.arange(0, 64)))) * 1024) + tl.maximum(((((tl.program_id(0) // 1024) % 1024) * 1) + ((((_lv0 * 64) + tl.arange(0, 64)) % 1) * 1)) - 0, 0)) * 1024) + tl.maximum((((tl.program_id(0) % 1024) * 1) + ((((_lv0 * 64) + tl.arange(0, 64)) % 1) * 1)) - 0, 0)) + 0 * tl.arange(0, 64)), mask=((((_lv0 * 64) + tl.arange(0, 64)) < 64) & ((((0 <= ((((tl.program_id(0) // 1024) % 1024) * 1) + ((((_lv0 * 64) + tl.arange(0, 64)) % 1) * 1))) & (((((tl.program_id(0) // 1024) % 1024) * 1) + ((((_lv0 * 64) + tl.arange(0, 64)) % 1) * 1)) < 1024)) & (0 <= (((tl.program_id(0) % 1024) * 1) + ((((_lv0 * 64) + tl.arange(0, 64)) % 1) * 1)))) & ((((tl.program_id(0) % 1024) * 1) + ((((_lv0 * 64) + tl.arange(0, 64)) % 1) * 1)) < 1024))), other=0.0) * tl.load(in1_ptr + (((((((((tl.program_id(0) // 1048576) % 128) * 64) + ((_lv0 * 64) + tl.arange(0, 64))) * 1) + (((_lv0 * 64) + tl.arange(0, 64)) % 1)) * 1) + (((_lv0 * 64) + tl.arange(0, 64)) % 1)) + 0 * tl.arange(0, 64)), mask=((((_lv0 * 64) + tl.arange(0, 64)) < 64) & ((((0 <= ((((tl.program_id(0) // 1024) % 1024) * 1) + ((((_lv0 * 64) + tl.arange(0, 64)) % 1) * 1))) & (((((tl.program_id(0) // 1024) % 1024) * 1) + ((((_lv0 * 64) + tl.arange(0, 64)) % 1) * 1)) < 1024)) & (0 <= (((tl.program_id(0) % 1024) * 1) + ((((_lv0 * 64) + tl.arange(0, 64)) % 1) * 1)))) & ((((tl.program_id(0) % 1024) * 1) + ((((_lv0 * 64) + tl.arange(0, 64)) % 1) * 1)) < 1024))), other=0.0)), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t087(out, ins):
    grid = (268435456,)
    t087_kernel[grid](out, ins[0], ins[1])
    return out
