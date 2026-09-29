import torch
import triton
import triton.language as tl


@triton.jit
def t054_kernel(out_ptr, in0_ptr, in1_ptr):
    _acc0 = tl.zeros([64], dtype=tl.float32)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 64) + tl.arange(0, 64)) < 81) & ((((((0 <= ((((tl.program_id(0) // 3844) % 62) * 1) + (((((_lv0 * 64) + tl.arange(0, 64)) // 9) % 3) * 1))) & (((((tl.program_id(0) // 3844) % 62) * 1) + (((((_lv0 * 64) + tl.arange(0, 64)) // 9) % 3) * 1)) < 64)) & (0 <= ((((tl.program_id(0) // 62) % 62) * 1) + (((((_lv0 * 64) + tl.arange(0, 64)) // 3) % 3) * 1)))) & (((((tl.program_id(0) // 62) % 62) * 1) + (((((_lv0 * 64) + tl.arange(0, 64)) // 3) % 3) * 1)) < 64)) & (0 <= (((tl.program_id(0) % 62) * 1) + ((((_lv0 * 64) + tl.arange(0, 64)) % 3) * 1)))) & ((((tl.program_id(0) % 62) * 1) + ((((_lv0 * 64) + tl.arange(0, 64)) % 3) * 1)) < 64))), (tl.load(in0_ptr + ((((((((((tl.program_id(0) // 15252992) * 3) + (((((tl.program_id(0) // 238328) % 64) // 64) * 3) + (((_lv0 * 64) + tl.arange(0, 64)) // 27))) * 64) + tl.maximum(((((tl.program_id(0) // 3844) % 62) * 1) + (((((_lv0 * 64) + tl.arange(0, 64)) // 9) % 3) * 1)) - 0, 0)) * 64) + tl.maximum(((((tl.program_id(0) // 62) % 62) * 1) + (((((_lv0 * 64) + tl.arange(0, 64)) // 3) % 3) * 1)) - 0, 0)) * 64) + tl.maximum((((tl.program_id(0) % 62) * 1) + ((((_lv0 * 64) + tl.arange(0, 64)) % 3) * 1)) - 0, 0)) + 0 * tl.arange(0, 64)), mask=((((_lv0 * 64) + tl.arange(0, 64)) < 81) & ((((((0 <= ((((tl.program_id(0) // 3844) % 62) * 1) + (((((_lv0 * 64) + tl.arange(0, 64)) // 9) % 3) * 1))) & (((((tl.program_id(0) // 3844) % 62) * 1) + (((((_lv0 * 64) + tl.arange(0, 64)) // 9) % 3) * 1)) < 64)) & (0 <= ((((tl.program_id(0) // 62) % 62) * 1) + (((((_lv0 * 64) + tl.arange(0, 64)) // 3) % 3) * 1)))) & (((((tl.program_id(0) // 62) % 62) * 1) + (((((_lv0 * 64) + tl.arange(0, 64)) // 3) % 3) * 1)) < 64)) & (0 <= (((tl.program_id(0) % 62) * 1) + ((((_lv0 * 64) + tl.arange(0, 64)) % 3) * 1)))) & ((((tl.program_id(0) % 62) * 1) + ((((_lv0 * 64) + tl.arange(0, 64)) % 3) * 1)) < 64))), other=0.0) * tl.load(in1_ptr + (((((((((((tl.program_id(0) // 238328) % 64) * 3) + (((_lv0 * 64) + tl.arange(0, 64)) // 27)) * 3) + ((((_lv0 * 64) + tl.arange(0, 64)) // 9) % 3)) * 3) + ((((_lv0 * 64) + tl.arange(0, 64)) // 3) % 3)) * 3) + (((_lv0 * 64) + tl.arange(0, 64)) % 3)) + 0 * tl.arange(0, 64)), mask=((((_lv0 * 64) + tl.arange(0, 64)) < 81) & ((((((0 <= ((((tl.program_id(0) // 3844) % 62) * 1) + (((((_lv0 * 64) + tl.arange(0, 64)) // 9) % 3) * 1))) & (((((tl.program_id(0) // 3844) % 62) * 1) + (((((_lv0 * 64) + tl.arange(0, 64)) // 9) % 3) * 1)) < 64)) & (0 <= ((((tl.program_id(0) // 62) % 62) * 1) + (((((_lv0 * 64) + tl.arange(0, 64)) // 3) % 3) * 1)))) & (((((tl.program_id(0) // 62) % 62) * 1) + (((((_lv0 * 64) + tl.arange(0, 64)) // 3) % 3) * 1)) < 64)) & (0 <= (((tl.program_id(0) % 62) * 1) + ((((_lv0 * 64) + tl.arange(0, 64)) % 3) * 1)))) & ((((tl.program_id(0) % 62) * 1) + ((((_lv0 * 64) + tl.arange(0, 64)) % 3) * 1)) < 64))), other=0.0)), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t054(out, ins):
    grid = (244047872,)
    t054_kernel[grid](out, ins[0], ins[1])
    return out
