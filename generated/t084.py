import torch
import triton
import triton.language as tl


@triton.jit
def t084_kernel(out_ptr, in0_ptr, in1_ptr):
    _acc0 = tl.zeros([8], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 8) + tl.arange(0, 8)) < 9) & (((((tl.program_id(0) // 510) % 254) + ((((_lv0 * 8) + tl.arange(0, 8)) // 3) % 3)) < 256) & (((tl.program_id(0) % 510) + (((_lv0 * 8) + tl.arange(0, 8)) % 3)) < 512))), (tl.load(in0_ptr + ((((((((tl.program_id(0) // 16581120) * 128) + ((tl.program_id(0) // 129540) % 128)) * 256) + (((tl.program_id(0) // 510) % 254) + ((((_lv0 * 8) + tl.arange(0, 8)) // 3) % 3))) * 512) + ((tl.program_id(0) % 510) + (((_lv0 * 8) + tl.arange(0, 8)) % 3))) + 0 * tl.arange(0, 8)), mask=((((_lv0 * 8) + tl.arange(0, 8)) < 9) & (((((tl.program_id(0) // 510) % 254) + ((((_lv0 * 8) + tl.arange(0, 8)) // 3) % 3)) < 256) & (((tl.program_id(0) % 510) + (((_lv0 * 8) + tl.arange(0, 8)) % 3)) < 512))), other=0.0) * tl.load(in1_ptr + (((((((tl.program_id(0) // 129540) % 128) * 3) + ((((_lv0 * 8) + tl.arange(0, 8)) // 3) % 3)) * 3) + (((_lv0 * 8) + tl.arange(0, 8)) % 3)) + 0 * tl.arange(0, 8)), mask=((((_lv0 * 8) + tl.arange(0, 8)) < 9) & (((((tl.program_id(0) // 510) % 254) + ((((_lv0 * 8) + tl.arange(0, 8)) // 3) % 3)) < 256) & (((tl.program_id(0) % 510) + (((_lv0 * 8) + tl.arange(0, 8)) % 3)) < 512))), other=0.0)), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t084(out, ins):
    grid = (265297920,)
    t084_kernel[grid](out, ins[0], ins[1])
    return out
