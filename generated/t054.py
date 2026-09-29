import torch
import triton
import triton.language as tl


@triton.jit
def t054_kernel(out_ptr, in0_ptr, in1_ptr):
    _acc0 = tl.zeros([64], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 64) + tl.arange(0, 64)) < 81) & ((((((tl.program_id(0) // 3844) % 62) + ((((_lv0 * 64) + tl.arange(0, 64)) // 9) % 3)) < 64) & ((((tl.program_id(0) // 62) % 62) + ((((_lv0 * 64) + tl.arange(0, 64)) // 3) % 3)) < 64)) & (((tl.program_id(0) % 62) + (((_lv0 * 64) + tl.arange(0, 64)) % 3)) < 64))), (tl.load(in0_ptr + ((((((((((tl.program_id(0) // 15252992) * 3) + (((_lv0 * 64) + tl.arange(0, 64)) // 27)) * 64) + (((tl.program_id(0) // 3844) % 62) + ((((_lv0 * 64) + tl.arange(0, 64)) // 9) % 3))) * 64) + (((tl.program_id(0) // 62) % 62) + ((((_lv0 * 64) + tl.arange(0, 64)) // 3) % 3))) * 64) + ((tl.program_id(0) % 62) + (((_lv0 * 64) + tl.arange(0, 64)) % 3))) + 0 * tl.arange(0, 64)), mask=((((_lv0 * 64) + tl.arange(0, 64)) < 81) & ((((((tl.program_id(0) // 3844) % 62) + ((((_lv0 * 64) + tl.arange(0, 64)) // 9) % 3)) < 64) & ((((tl.program_id(0) // 62) % 62) + ((((_lv0 * 64) + tl.arange(0, 64)) // 3) % 3)) < 64)) & (((tl.program_id(0) % 62) + (((_lv0 * 64) + tl.arange(0, 64)) % 3)) < 64))), other=0.0) * tl.load(in1_ptr + (((((((((((tl.program_id(0) // 238328) % 64) * 3) + (((_lv0 * 64) + tl.arange(0, 64)) // 27)) * 3) + ((((_lv0 * 64) + tl.arange(0, 64)) // 9) % 3)) * 3) + ((((_lv0 * 64) + tl.arange(0, 64)) // 3) % 3)) * 3) + (((_lv0 * 64) + tl.arange(0, 64)) % 3)) + 0 * tl.arange(0, 64)), mask=((((_lv0 * 64) + tl.arange(0, 64)) < 81) & ((((((tl.program_id(0) // 3844) % 62) + ((((_lv0 * 64) + tl.arange(0, 64)) // 9) % 3)) < 64) & ((((tl.program_id(0) // 62) % 62) + ((((_lv0 * 64) + tl.arange(0, 64)) // 3) % 3)) < 64)) & (((tl.program_id(0) % 62) + (((_lv0 * 64) + tl.arange(0, 64)) % 3)) < 64))), other=0.0)), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t054(out, ins):
    grid = (244047872,)
    t054_kernel[grid](out, ins[0], ins[1])
    return out
