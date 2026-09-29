import torch
import triton
import triton.language as tl


@triton.jit
def t045_kernel(out_ptr, in0_ptr):
    _acc0 = tl.zeros([64], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 64) + tl.arange(0, 64)) < 121) & ((((0 <= ((((tl.program_id(0) // 186) % 186) * 11) + (((_lv0 * 64) + tl.arange(0, 64)) // 11))) & (((((tl.program_id(0) // 186) % 186) * 11) + (((_lv0 * 64) + tl.arange(0, 64)) // 11)) < 2048)) & (0 <= (((tl.program_id(0) % 186) * 11) + (((_lv0 * 64) + tl.arange(0, 64)) % 11)))) & ((((tl.program_id(0) % 186) * 11) + (((_lv0 * 64) + tl.arange(0, 64)) % 11)) < 2048))), tl.load(in0_ptr + ((((((((tl.program_id(0) // 2214144) * 64) + ((tl.program_id(0) // 34596) % 64)) * 2048) + ((((tl.program_id(0) // 186) % 186) * 11) + (((_lv0 * 64) + tl.arange(0, 64)) // 11))) * 2048) + (((tl.program_id(0) % 186) * 11) + (((_lv0 * 64) + tl.arange(0, 64)) % 11))) + 0 * tl.arange(0, 64)), mask=((((_lv0 * 64) + tl.arange(0, 64)) < 121) & ((((0 <= ((((tl.program_id(0) // 186) % 186) * 11) + (((_lv0 * 64) + tl.arange(0, 64)) // 11))) & (((((tl.program_id(0) // 186) % 186) * 11) + (((_lv0 * 64) + tl.arange(0, 64)) // 11)) < 2048)) & (0 <= (((tl.program_id(0) % 186) * 11) + (((_lv0 * 64) + tl.arange(0, 64)) % 11)))) & ((((tl.program_id(0) % 186) * 11) + (((_lv0 * 64) + tl.arange(0, 64)) % 11)) < 2048))), other=0.0), 0.0))
    _v = (tl.sum(_acc0, axis=0) * (1.0 * (1.0 / 121.0)))
    tl.store(out_ptr + tl.program_id(0), _v)


def t045(out, ins):
    grid = (8856576,)
    t045_kernel[grid](out, ins[0])
    return out
