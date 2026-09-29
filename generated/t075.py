import torch
import triton
import triton.language as tl


@triton.jit
def t075_kernel(out_ptr, in0_ptr, in1_ptr):
    _acc0 = tl.zeros([64], dtype=tl.float32)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 64) + tl.arange(0, 64)) < 120) & (((((((((((_lv0 * 64) + tl.arange(0, 64)) // 5) % 3) * 2) <= (((tl.program_id(0) // 766) % 257) + 1)) & ((tl.maximum((((tl.program_id(0) // 766) % 257) + 1) - (((((_lv0 * 64) + tl.arange(0, 64)) // 5) % 3) * 2), 0) % 2) == 0)) & ((tl.maximum((((tl.program_id(0) // 766) % 257) + 1) - (((((_lv0 * 64) + tl.arange(0, 64)) // 5) % 3) * 2), 0) // 2) < 128)) & (((((_lv0 * 64) + tl.arange(0, 64)) % 5) * 1) <= ((tl.program_id(0) % 766) + 2))) & ((tl.maximum(((tl.program_id(0) % 766) + 2) - ((((_lv0 * 64) + tl.arange(0, 64)) % 5) * 1), 0) % 3) == 0)) & ((tl.maximum(((tl.program_id(0) % 766) + 2) - ((((_lv0 * 64) + tl.arange(0, 64)) % 5) * 1), 0) // 3) < 256))), (tl.load(in0_ptr + ((((((((tl.program_id(0) // 12599168) * 32) + (((((tl.program_id(0) // 196862) % 64) // 16) * 8) + (((_lv0 * 64) + tl.arange(0, 64)) // 15))) * 128) + (tl.maximum((((tl.program_id(0) // 766) % 257) + 1) - (((((_lv0 * 64) + tl.arange(0, 64)) // 5) % 3) * 2), 0) // 2)) * 256) + (tl.maximum(((tl.program_id(0) % 766) + 2) - ((((_lv0 * 64) + tl.arange(0, 64)) % 5) * 1), 0) // 3))), mask=((((_lv0 * 64) + tl.arange(0, 64)) < 120) & (((((((((((_lv0 * 64) + tl.arange(0, 64)) // 5) % 3) * 2) <= (((tl.program_id(0) // 766) % 257) + 1)) & ((tl.maximum((((tl.program_id(0) // 766) % 257) + 1) - (((((_lv0 * 64) + tl.arange(0, 64)) // 5) % 3) * 2), 0) % 2) == 0)) & ((tl.maximum((((tl.program_id(0) // 766) % 257) + 1) - (((((_lv0 * 64) + tl.arange(0, 64)) // 5) % 3) * 2), 0) // 2) < 128)) & (((((_lv0 * 64) + tl.arange(0, 64)) % 5) * 1) <= ((tl.program_id(0) % 766) + 2))) & ((tl.maximum(((tl.program_id(0) % 766) + 2) - ((((_lv0 * 64) + tl.arange(0, 64)) % 5) * 1), 0) % 3) == 0)) & ((tl.maximum(((tl.program_id(0) % 766) + 2) - ((((_lv0 * 64) + tl.arange(0, 64)) % 5) * 1), 0) // 3) < 256))), other=0.0) * tl.load(in1_ptr + ((((((((((((tl.program_id(0) // 196862) % 64) // 16) * 8) + (((_lv0 * 64) + tl.arange(0, 64)) // 15)) * 16) + (((tl.program_id(0) // 196862) % 64) % 16)) * 3) + ((((_lv0 * 64) + tl.arange(0, 64)) // 5) % 3)) * 5) + (((_lv0 * 64) + tl.arange(0, 64)) % 5))), mask=((((_lv0 * 64) + tl.arange(0, 64)) < 120) & (((((((((((_lv0 * 64) + tl.arange(0, 64)) // 5) % 3) * 2) <= (((tl.program_id(0) // 766) % 257) + 1)) & ((tl.maximum((((tl.program_id(0) // 766) % 257) + 1) - (((((_lv0 * 64) + tl.arange(0, 64)) // 5) % 3) * 2), 0) % 2) == 0)) & ((tl.maximum((((tl.program_id(0) // 766) % 257) + 1) - (((((_lv0 * 64) + tl.arange(0, 64)) // 5) % 3) * 2), 0) // 2) < 128)) & (((((_lv0 * 64) + tl.arange(0, 64)) % 5) * 1) <= ((tl.program_id(0) % 766) + 2))) & ((tl.maximum(((tl.program_id(0) % 766) + 2) - ((((_lv0 * 64) + tl.arange(0, 64)) % 5) * 1), 0) % 3) == 0)) & ((tl.maximum(((tl.program_id(0) % 766) + 2) - ((((_lv0 * 64) + tl.arange(0, 64)) % 5) * 1), 0) // 3) < 256))), other=0.0)), 0.0))
    _v = tl.where(True, tl.sum(_acc0, axis=0), 0.0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t075(out, ins):
    grid = (201586688,)
    t075_kernel[grid](out, ins[0], ins[1])
    return out
