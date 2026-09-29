import torch
import triton
import triton.language as tl


@triton.jit
def t074_kernel(out_ptr, in0_ptr, in1_ptr):
    _acc0 = tl.zeros([128], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 128) + tl.arange(0, 128)) < 160) & (((((((_lv0 * 128) + tl.arange(0, 128)) % 5) * 3) <= ((tl.program_id(0) % 131084) + 0)) & ((tl.maximum(((tl.program_id(0) % 131084) + 0) - ((((_lv0 * 128) + tl.arange(0, 128)) % 5) * 3), 0) % 1) == 0)) & ((tl.maximum(((tl.program_id(0) % 131084) + 0) - ((((_lv0 * 128) + tl.arange(0, 128)) % 5) * 3), 0) // 1) < 131072))), (tl.load(in0_ptr + ((((((tl.program_id(0) // 8389376) * 32) + (((((tl.program_id(0) // 131084) % 64) // 64) * 32) + (((_lv0 * 128) + tl.arange(0, 128)) // 5))) * 131072) + (tl.maximum(((tl.program_id(0) % 131084) + 0) - ((((_lv0 * 128) + tl.arange(0, 128)) % 5) * 3), 0) // 1)) + 0 * tl.arange(0, 128)), mask=((((_lv0 * 128) + tl.arange(0, 128)) < 160) & (((((((_lv0 * 128) + tl.arange(0, 128)) % 5) * 3) <= ((tl.program_id(0) % 131084) + 0)) & ((tl.maximum(((tl.program_id(0) % 131084) + 0) - ((((_lv0 * 128) + tl.arange(0, 128)) % 5) * 3), 0) % 1) == 0)) & ((tl.maximum(((tl.program_id(0) % 131084) + 0) - ((((_lv0 * 128) + tl.arange(0, 128)) % 5) * 3), 0) // 1) < 131072))), other=0.0) * tl.load(in1_ptr + ((((((((((tl.program_id(0) // 131084) % 64) // 64) * 32) + (((_lv0 * 128) + tl.arange(0, 128)) // 5)) * 64) + (((tl.program_id(0) // 131084) % 64) % 64)) * 5) + (((_lv0 * 128) + tl.arange(0, 128)) % 5)) + 0 * tl.arange(0, 128)), mask=((((_lv0 * 128) + tl.arange(0, 128)) < 160) & (((((((_lv0 * 128) + tl.arange(0, 128)) % 5) * 3) <= ((tl.program_id(0) % 131084) + 0)) & ((tl.maximum(((tl.program_id(0) % 131084) + 0) - ((((_lv0 * 128) + tl.arange(0, 128)) % 5) * 3), 0) % 1) == 0)) & ((tl.maximum(((tl.program_id(0) % 131084) + 0) - ((((_lv0 * 128) + tl.arange(0, 128)) % 5) * 3), 0) // 1) < 131072))), other=0.0)), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t074(out, ins):
    grid = (268460032,)
    t074_kernel[grid](out, ins[0], ins[1])
    return out
