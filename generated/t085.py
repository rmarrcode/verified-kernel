import torch
import triton
import triton.language as tl


@triton.jit
def t085_kernel(out_ptr, in0_ptr, in1_ptr):
    _acc0 = tl.zeros([16], dtype=tl.float32)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 16) + tl.arange(0, 16)) < 21) & ((((0 <= ((((tl.program_id(0) // 250) % 126) * 1) + (((((_lv0 * 16) + tl.arange(0, 16)) // 7) % 3) * 1))) & (((((tl.program_id(0) // 250) % 126) * 1) + (((((_lv0 * 16) + tl.arange(0, 16)) // 7) % 3) * 1)) < 128)) & (0 <= (((tl.program_id(0) % 250) * 1) + ((((_lv0 * 16) + tl.arange(0, 16)) % 7) * 1)))) & ((((tl.program_id(0) % 250) * 1) + ((((_lv0 * 16) + tl.arange(0, 16)) % 7) * 1)) < 256))), (tl.load(in0_ptr + ((((((((tl.program_id(0) // 4032000) * 128) + (((((tl.program_id(0) // 31500) % 128) // 1) * 1) + (((_lv0 * 16) + tl.arange(0, 16)) // 21))) * 128) + tl.maximum(((((tl.program_id(0) // 250) % 126) * 1) + (((((_lv0 * 16) + tl.arange(0, 16)) // 7) % 3) * 1)) - 0, 0)) * 256) + tl.maximum((((tl.program_id(0) % 250) * 1) + ((((_lv0 * 16) + tl.arange(0, 16)) % 7) * 1)) - 0, 0)) + 0 * tl.arange(0, 16)), mask=((((_lv0 * 16) + tl.arange(0, 16)) < 21) & ((((0 <= ((((tl.program_id(0) // 250) % 126) * 1) + (((((_lv0 * 16) + tl.arange(0, 16)) // 7) % 3) * 1))) & (((((tl.program_id(0) // 250) % 126) * 1) + (((((_lv0 * 16) + tl.arange(0, 16)) // 7) % 3) * 1)) < 128)) & (0 <= (((tl.program_id(0) % 250) * 1) + ((((_lv0 * 16) + tl.arange(0, 16)) % 7) * 1)))) & ((((tl.program_id(0) % 250) * 1) + ((((_lv0 * 16) + tl.arange(0, 16)) % 7) * 1)) < 256))), other=0.0) * tl.load(in1_ptr + (((((((((tl.program_id(0) // 31500) % 128) * 1) + (((_lv0 * 16) + tl.arange(0, 16)) // 21)) * 3) + ((((_lv0 * 16) + tl.arange(0, 16)) // 7) % 3)) * 7) + (((_lv0 * 16) + tl.arange(0, 16)) % 7)) + 0 * tl.arange(0, 16)), mask=((((_lv0 * 16) + tl.arange(0, 16)) < 21) & ((((0 <= ((((tl.program_id(0) // 250) % 126) * 1) + (((((_lv0 * 16) + tl.arange(0, 16)) // 7) % 3) * 1))) & (((((tl.program_id(0) // 250) % 126) * 1) + (((((_lv0 * 16) + tl.arange(0, 16)) // 7) % 3) * 1)) < 128)) & (0 <= (((tl.program_id(0) % 250) * 1) + ((((_lv0 * 16) + tl.arange(0, 16)) % 7) * 1)))) & ((((tl.program_id(0) % 250) * 1) + ((((_lv0 * 16) + tl.arange(0, 16)) % 7) * 1)) < 256))), other=0.0)), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t085(out, ins):
    grid = (129024000,)
    t085_kernel[grid](out, ins[0], ins[1])
    return out
