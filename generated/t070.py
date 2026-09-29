import torch
import triton
import triton.language as tl


@triton.jit
def t070_kernel(out_ptr, in0_ptr, in1_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 1296) & (((((((((((((_lv0 * 1024) + tl.arange(0, 1024)) // 9) % 3) <= ((tl.program_id(0) // 9604) % 98)) & (0 == 0)) & (tl.maximum(((tl.program_id(0) // 9604) % 98) - ((((_lv0 * 1024) + tl.arange(0, 1024)) // 9) % 3), 0) < 96)) & (((((_lv0 * 1024) + tl.arange(0, 1024)) // 3) % 3) <= ((tl.program_id(0) // 98) % 98))) & (0 == 0)) & (tl.maximum(((tl.program_id(0) // 98) % 98) - ((((_lv0 * 1024) + tl.arange(0, 1024)) // 3) % 3), 0) < 96)) & ((((_lv0 * 1024) + tl.arange(0, 1024)) % 3) <= (tl.program_id(0) % 98))) & (0 == 0)) & (tl.maximum((tl.program_id(0) % 98) - (((_lv0 * 1024) + tl.arange(0, 1024)) % 3), 0) < 96))), (tl.load(in0_ptr + ((((((((((tl.program_id(0) // 22588608) * 48) + (((((tl.program_id(0) // 941192) % 24) // 24) * 48) + (((_lv0 * 1024) + tl.arange(0, 1024)) // 27))) * 96) + tl.maximum(((tl.program_id(0) // 9604) % 98) - ((((_lv0 * 1024) + tl.arange(0, 1024)) // 9) % 3), 0)) * 96) + tl.maximum(((tl.program_id(0) // 98) % 98) - ((((_lv0 * 1024) + tl.arange(0, 1024)) // 3) % 3), 0)) * 96) + tl.maximum((tl.program_id(0) % 98) - (((_lv0 * 1024) + tl.arange(0, 1024)) % 3), 0)) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 1296) & (((((((((((((_lv0 * 1024) + tl.arange(0, 1024)) // 9) % 3) <= ((tl.program_id(0) // 9604) % 98)) & (0 == 0)) & (tl.maximum(((tl.program_id(0) // 9604) % 98) - ((((_lv0 * 1024) + tl.arange(0, 1024)) // 9) % 3), 0) < 96)) & (((((_lv0 * 1024) + tl.arange(0, 1024)) // 3) % 3) <= ((tl.program_id(0) // 98) % 98))) & (0 == 0)) & (tl.maximum(((tl.program_id(0) // 98) % 98) - ((((_lv0 * 1024) + tl.arange(0, 1024)) // 3) % 3), 0) < 96)) & ((((_lv0 * 1024) + tl.arange(0, 1024)) % 3) <= (tl.program_id(0) % 98))) & (0 == 0)) & (tl.maximum((tl.program_id(0) % 98) - (((_lv0 * 1024) + tl.arange(0, 1024)) % 3), 0) < 96))), other=0.0) * tl.load(in1_ptr + ((((((((((((((tl.program_id(0) // 941192) % 24) // 24) * 48) + (((_lv0 * 1024) + tl.arange(0, 1024)) // 27)) * 24) + (((tl.program_id(0) // 941192) % 24) % 24)) * 3) + ((((_lv0 * 1024) + tl.arange(0, 1024)) // 9) % 3)) * 3) + ((((_lv0 * 1024) + tl.arange(0, 1024)) // 3) % 3)) * 3) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 3)) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 1296) & (((((((((((((_lv0 * 1024) + tl.arange(0, 1024)) // 9) % 3) <= ((tl.program_id(0) // 9604) % 98)) & (0 == 0)) & (tl.maximum(((tl.program_id(0) // 9604) % 98) - ((((_lv0 * 1024) + tl.arange(0, 1024)) // 9) % 3), 0) < 96)) & (((((_lv0 * 1024) + tl.arange(0, 1024)) // 3) % 3) <= ((tl.program_id(0) // 98) % 98))) & (0 == 0)) & (tl.maximum(((tl.program_id(0) // 98) % 98) - ((((_lv0 * 1024) + tl.arange(0, 1024)) // 3) % 3), 0) < 96)) & ((((_lv0 * 1024) + tl.arange(0, 1024)) % 3) <= (tl.program_id(0) % 98))) & (0 == 0)) & (tl.maximum((tl.program_id(0) % 98) - (((_lv0 * 1024) + tl.arange(0, 1024)) % 3), 0) < 96))), other=0.0)), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t070(out, ins):
    grid = (180708864,)
    t070_kernel[grid](out, ins[0], ins[1])
    return out
