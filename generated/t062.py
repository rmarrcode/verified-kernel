import torch
import triton
import triton.language as tl


@triton.jit
def t062_kernel(out_ptr, in0_ptr, in1_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 1440) & (((((tl.program_id(0) // 504) % 508) + ((((_lv0 * 1024) + tl.arange(0, 1024)) // 9) % 5)) < 512) & (((tl.program_id(0) % 504) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 9)) < 512))), (tl.load(in0_ptr + ((((((((tl.program_id(0) // 16386048) * 32) + (((_lv0 * 1024) + tl.arange(0, 1024)) // 45)) * 512) + (((tl.program_id(0) // 504) % 508) + ((((_lv0 * 1024) + tl.arange(0, 1024)) // 9) % 5))) * 512) + ((tl.program_id(0) % 504) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 9))) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 1440) & (((((tl.program_id(0) // 504) % 508) + ((((_lv0 * 1024) + tl.arange(0, 1024)) // 9) % 5)) < 512) & (((tl.program_id(0) % 504) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 9)) < 512))), other=0.0) * tl.load(in1_ptr + (((((((((tl.program_id(0) // 256032) % 64) * 32) + (((_lv0 * 1024) + tl.arange(0, 1024)) // 45)) * 5) + ((((_lv0 * 1024) + tl.arange(0, 1024)) // 9) % 5)) * 9) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 9)) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 1440) & (((((tl.program_id(0) // 504) % 508) + ((((_lv0 * 1024) + tl.arange(0, 1024)) // 9) % 5)) < 512) & (((tl.program_id(0) % 504) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 9)) < 512))), other=0.0)), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t062(out, ins):
    grid = (131088384,)
    t062_kernel[grid](out, ins[0], ins[1])
    return out
