import torch
import triton
import triton.language as tl


@triton.jit
def t059_kernel(out_ptr, in0_ptr, in1_ptr):
    _acc0 = tl.zeros([16], dtype=tl.float32)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 16) + tl.arange(0, 16)) < 27) & ((((((0 <= ((((tl.program_id(0) // 2540) % 254) * 1) + (((((_lv0 * 16) + tl.arange(0, 16)) // 3) % 3) * 1))) & (((((tl.program_id(0) // 2540) % 254) * 1) + (((((_lv0 * 16) + tl.arange(0, 16)) // 3) % 3) * 1)) < 256)) & (0 <= ((((tl.program_id(0) // 10) % 254) * 1) + ((((_lv0 * 16) + tl.arange(0, 16)) % 3) * 1)))) & (((((tl.program_id(0) // 10) % 254) * 1) + ((((_lv0 * 16) + tl.arange(0, 16)) % 3) * 1)) < 256)) & (0 <= (((tl.program_id(0) % 10) * 1) + ((((_lv0 * 16) + tl.arange(0, 16)) % 1) * 1)))) & ((((tl.program_id(0) % 10) * 1) + ((((_lv0 * 16) + tl.arange(0, 16)) % 1) * 1)) < 10))), (tl.load(in0_ptr + ((((((((((tl.program_id(0) // 41290240) * 3) + (((((tl.program_id(0) // 645160) % 64) // 64) * 3) + (((_lv0 * 16) + tl.arange(0, 16)) // 9))) * 256) + tl.maximum(((((tl.program_id(0) // 2540) % 254) * 1) + (((((_lv0 * 16) + tl.arange(0, 16)) // 3) % 3) * 1)) - 0, 0)) * 256) + tl.maximum(((((tl.program_id(0) // 10) % 254) * 1) + ((((_lv0 * 16) + tl.arange(0, 16)) % 3) * 1)) - 0, 0)) * 10) + tl.maximum((((tl.program_id(0) % 10) * 1) + ((((_lv0 * 16) + tl.arange(0, 16)) % 1) * 1)) - 0, 0)) + 0 * tl.arange(0, 16)), mask=((((_lv0 * 16) + tl.arange(0, 16)) < 27) & ((((((0 <= ((((tl.program_id(0) // 2540) % 254) * 1) + (((((_lv0 * 16) + tl.arange(0, 16)) // 3) % 3) * 1))) & (((((tl.program_id(0) // 2540) % 254) * 1) + (((((_lv0 * 16) + tl.arange(0, 16)) // 3) % 3) * 1)) < 256)) & (0 <= ((((tl.program_id(0) // 10) % 254) * 1) + ((((_lv0 * 16) + tl.arange(0, 16)) % 3) * 1)))) & (((((tl.program_id(0) // 10) % 254) * 1) + ((((_lv0 * 16) + tl.arange(0, 16)) % 3) * 1)) < 256)) & (0 <= (((tl.program_id(0) % 10) * 1) + ((((_lv0 * 16) + tl.arange(0, 16)) % 1) * 1)))) & ((((tl.program_id(0) % 10) * 1) + ((((_lv0 * 16) + tl.arange(0, 16)) % 1) * 1)) < 10))), other=0.0) * tl.load(in1_ptr + (((((((((((tl.program_id(0) // 645160) % 64) * 3) + (((_lv0 * 16) + tl.arange(0, 16)) // 9)) * 3) + ((((_lv0 * 16) + tl.arange(0, 16)) // 3) % 3)) * 3) + (((_lv0 * 16) + tl.arange(0, 16)) % 3)) * 1) + (((_lv0 * 16) + tl.arange(0, 16)) % 1)) + 0 * tl.arange(0, 16)), mask=((((_lv0 * 16) + tl.arange(0, 16)) < 27) & ((((((0 <= ((((tl.program_id(0) // 2540) % 254) * 1) + (((((_lv0 * 16) + tl.arange(0, 16)) // 3) % 3) * 1))) & (((((tl.program_id(0) // 2540) % 254) * 1) + (((((_lv0 * 16) + tl.arange(0, 16)) // 3) % 3) * 1)) < 256)) & (0 <= ((((tl.program_id(0) // 10) % 254) * 1) + ((((_lv0 * 16) + tl.arange(0, 16)) % 3) * 1)))) & (((((tl.program_id(0) // 10) % 254) * 1) + ((((_lv0 * 16) + tl.arange(0, 16)) % 3) * 1)) < 256)) & (0 <= (((tl.program_id(0) % 10) * 1) + ((((_lv0 * 16) + tl.arange(0, 16)) % 1) * 1)))) & ((((tl.program_id(0) % 10) * 1) + ((((_lv0 * 16) + tl.arange(0, 16)) % 1) * 1)) < 10))), other=0.0)), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t059(out, ins):
    grid = (330321920,)
    t059_kernel[grid](out, ins[0], ins[1])
    return out
