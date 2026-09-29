import torch
import triton
import triton.language as tl


@triton.jit
def t083_kernel(out_ptr, in0_ptr, in1_ptr):
    _acc0 = tl.zeros([2], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 2) + tl.arange(0, 2)) < 3) & (((((tl.program_id(0) // 512) % 510) + (((_lv0 * 2) + tl.arange(0, 2)) % 3)) < 512) & ((tl.program_id(0) % 512) < 512))), (tl.load(in0_ptr + ((((((((tl.program_id(0) // 2088960) * 8) + ((tl.program_id(0) // 261120) % 8)) * 512) + (((tl.program_id(0) // 512) % 510) + (((_lv0 * 2) + tl.arange(0, 2)) % 3))) * 512) + (tl.program_id(0) % 512)) + 0 * tl.arange(0, 2)), mask=((((_lv0 * 2) + tl.arange(0, 2)) < 3) & (((((tl.program_id(0) // 512) % 510) + (((_lv0 * 2) + tl.arange(0, 2)) % 3)) < 512) & ((tl.program_id(0) % 512) < 512))), other=0.0) * tl.load(in1_ptr + (((((tl.program_id(0) // 261120) % 8) * 3) + (((_lv0 * 2) + tl.arange(0, 2)) % 3)) + 0 * tl.arange(0, 2)), mask=((((_lv0 * 2) + tl.arange(0, 2)) < 3) & (((((tl.program_id(0) // 512) % 510) + (((_lv0 * 2) + tl.arange(0, 2)) % 3)) < 512) & ((tl.program_id(0) % 512) < 512))), other=0.0)), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t083(out, ins):
    grid = (133693440,)
    t083_kernel[grid](out, ins[0], ins[1])
    return out
