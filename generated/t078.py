import torch
import triton
import triton.language as tl


@triton.jit
def t078_kernel(out_ptr, in0_ptr, in1_ptr):
    _acc0 = tl.zeros([512], dtype=tl.float32)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 512) + tl.arange(0, 512)) < 672) & (((((((((((_lv0 * 512) + tl.arange(0, 512)) // 7) % 3) * 1) <= (((tl.program_id(0) // 1024) % 512) + 1)) & ((tl.maximum((((tl.program_id(0) // 1024) % 512) + 1) - (((((_lv0 * 512) + tl.arange(0, 512)) // 7) % 3) * 1), 0) % 1) == 0)) & ((tl.maximum((((tl.program_id(0) // 1024) % 512) + 1) - (((((_lv0 * 512) + tl.arange(0, 512)) // 7) % 3) * 1), 0) // 1) < 512)) & (((((_lv0 * 512) + tl.arange(0, 512)) % 7) * 1) <= ((tl.program_id(0) % 1024) + 3))) & ((tl.maximum(((tl.program_id(0) % 1024) + 3) - ((((_lv0 * 512) + tl.arange(0, 512)) % 7) * 1), 0) % 1) == 0)) & ((tl.maximum(((tl.program_id(0) % 1024) + 3) - ((((_lv0 * 512) + tl.arange(0, 512)) % 7) * 1), 0) // 1) < 1024))), (tl.load(in0_ptr + ((((((((tl.program_id(0) // 16777216) * 32) + (((((tl.program_id(0) // 524288) % 32) // 32) * 32) + (((_lv0 * 512) + tl.arange(0, 512)) // 21))) * 512) + (tl.maximum((((tl.program_id(0) // 1024) % 512) + 1) - (((((_lv0 * 512) + tl.arange(0, 512)) // 7) % 3) * 1), 0) // 1)) * 1024) + (tl.maximum(((tl.program_id(0) % 1024) + 3) - ((((_lv0 * 512) + tl.arange(0, 512)) % 7) * 1), 0) // 1)) + 0 * tl.arange(0, 512)), mask=((((_lv0 * 512) + tl.arange(0, 512)) < 672) & (((((((((((_lv0 * 512) + tl.arange(0, 512)) // 7) % 3) * 1) <= (((tl.program_id(0) // 1024) % 512) + 1)) & ((tl.maximum((((tl.program_id(0) // 1024) % 512) + 1) - (((((_lv0 * 512) + tl.arange(0, 512)) // 7) % 3) * 1), 0) % 1) == 0)) & ((tl.maximum((((tl.program_id(0) // 1024) % 512) + 1) - (((((_lv0 * 512) + tl.arange(0, 512)) // 7) % 3) * 1), 0) // 1) < 512)) & (((((_lv0 * 512) + tl.arange(0, 512)) % 7) * 1) <= ((tl.program_id(0) % 1024) + 3))) & ((tl.maximum(((tl.program_id(0) % 1024) + 3) - ((((_lv0 * 512) + tl.arange(0, 512)) % 7) * 1), 0) % 1) == 0)) & ((tl.maximum(((tl.program_id(0) % 1024) + 3) - ((((_lv0 * 512) + tl.arange(0, 512)) % 7) * 1), 0) // 1) < 1024))), other=0.0) * tl.load(in1_ptr + ((((((((((((tl.program_id(0) // 524288) % 32) // 32) * 32) + (((_lv0 * 512) + tl.arange(0, 512)) // 21)) * 32) + (((tl.program_id(0) // 524288) % 32) % 32)) * 3) + ((((_lv0 * 512) + tl.arange(0, 512)) // 7) % 3)) * 7) + (((_lv0 * 512) + tl.arange(0, 512)) % 7)) + 0 * tl.arange(0, 512)), mask=((((_lv0 * 512) + tl.arange(0, 512)) < 672) & (((((((((((_lv0 * 512) + tl.arange(0, 512)) // 7) % 3) * 1) <= (((tl.program_id(0) // 1024) % 512) + 1)) & ((tl.maximum((((tl.program_id(0) // 1024) % 512) + 1) - (((((_lv0 * 512) + tl.arange(0, 512)) // 7) % 3) * 1), 0) % 1) == 0)) & ((tl.maximum((((tl.program_id(0) // 1024) % 512) + 1) - (((((_lv0 * 512) + tl.arange(0, 512)) // 7) % 3) * 1), 0) // 1) < 512)) & (((((_lv0 * 512) + tl.arange(0, 512)) % 7) * 1) <= ((tl.program_id(0) % 1024) + 3))) & ((tl.maximum(((tl.program_id(0) % 1024) + 3) - ((((_lv0 * 512) + tl.arange(0, 512)) % 7) * 1), 0) % 1) == 0)) & ((tl.maximum(((tl.program_id(0) % 1024) + 3) - ((((_lv0 * 512) + tl.arange(0, 512)) % 7) * 1), 0) // 1) < 1024))), other=0.0)), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t078(out, ins):
    grid = (134217728,)
    t078_kernel[grid](out, ins[0], ins[1])
    return out
