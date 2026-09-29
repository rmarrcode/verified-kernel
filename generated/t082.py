import torch
import triton
import triton.language as tl


@triton.jit
def t082_kernel(out_ptr, in0_ptr, in1_ptr):
    _acc0 = tl.zeros([8], dtype=tl.float32)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 8) + tl.arange(0, 8)) < 9) & ((((0 <= ((((tl.program_id(0) // 510) % 510) * 1) + (((((_lv0 * 8) + tl.arange(0, 8)) // 3) % 3) * 1))) & (((((tl.program_id(0) // 510) % 510) * 1) + (((((_lv0 * 8) + tl.arange(0, 8)) // 3) % 3) * 1)) < 512)) & (0 <= (((tl.program_id(0) % 510) * 1) + ((((_lv0 * 8) + tl.arange(0, 8)) % 3) * 1)))) & ((((tl.program_id(0) % 510) * 1) + ((((_lv0 * 8) + tl.arange(0, 8)) % 3) * 1)) < 512))), (tl.load(in0_ptr + ((((((((tl.program_id(0) // 16646400) * 64) + (((((tl.program_id(0) // 260100) % 64) // 1) * 1) + (((_lv0 * 8) + tl.arange(0, 8)) // 9))) * 512) + tl.maximum(((((tl.program_id(0) // 510) % 510) * 1) + (((((_lv0 * 8) + tl.arange(0, 8)) // 3) % 3) * 1)) - 0, 0)) * 512) + tl.maximum((((tl.program_id(0) % 510) * 1) + ((((_lv0 * 8) + tl.arange(0, 8)) % 3) * 1)) - 0, 0)) + 0 * tl.arange(0, 8)), mask=((((_lv0 * 8) + tl.arange(0, 8)) < 9) & ((((0 <= ((((tl.program_id(0) // 510) % 510) * 1) + (((((_lv0 * 8) + tl.arange(0, 8)) // 3) % 3) * 1))) & (((((tl.program_id(0) // 510) % 510) * 1) + (((((_lv0 * 8) + tl.arange(0, 8)) // 3) % 3) * 1)) < 512)) & (0 <= (((tl.program_id(0) % 510) * 1) + ((((_lv0 * 8) + tl.arange(0, 8)) % 3) * 1)))) & ((((tl.program_id(0) % 510) * 1) + ((((_lv0 * 8) + tl.arange(0, 8)) % 3) * 1)) < 512))), other=0.0) * tl.load(in1_ptr + (((((((((tl.program_id(0) // 260100) % 64) * 1) + (((_lv0 * 8) + tl.arange(0, 8)) // 9)) * 3) + ((((_lv0 * 8) + tl.arange(0, 8)) // 3) % 3)) * 3) + (((_lv0 * 8) + tl.arange(0, 8)) % 3)) + 0 * tl.arange(0, 8)), mask=((((_lv0 * 8) + tl.arange(0, 8)) < 9) & ((((0 <= ((((tl.program_id(0) // 510) % 510) * 1) + (((((_lv0 * 8) + tl.arange(0, 8)) // 3) % 3) * 1))) & (((((tl.program_id(0) // 510) % 510) * 1) + (((((_lv0 * 8) + tl.arange(0, 8)) // 3) % 3) * 1)) < 512)) & (0 <= (((tl.program_id(0) % 510) * 1) + ((((_lv0 * 8) + tl.arange(0, 8)) % 3) * 1)))) & ((((tl.program_id(0) % 510) * 1) + ((((_lv0 * 8) + tl.arange(0, 8)) % 3) * 1)) < 512))), other=0.0)), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t082(out, ins):
    grid = (266342400,)
    t082_kernel[grid](out, ins[0], ins[1])
    return out
