import torch
import triton
import triton.language as tl


@triton.jit
def t056_kernel(out_ptr, in0_ptr, in1_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 3):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 2240) & (((((tl.program_id(0) // 250) % 508) + ((((_lv0 * 1024) + tl.arange(0, 1024)) // 7) % 5)) < 512) & (((tl.program_id(0) % 250) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 7)) < 256))), (tl.load(in0_ptr + ((((((((tl.program_id(0) // 16256000) * 64) + (((_lv0 * 1024) + tl.arange(0, 1024)) // 35)) * 512) + (((tl.program_id(0) // 250) % 508) + ((((_lv0 * 1024) + tl.arange(0, 1024)) // 7) % 5))) * 256) + ((tl.program_id(0) % 250) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 7))) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 2240) & (((((tl.program_id(0) // 250) % 508) + ((((_lv0 * 1024) + tl.arange(0, 1024)) // 7) % 5)) < 512) & (((tl.program_id(0) % 250) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 7)) < 256))), other=0.0) * tl.load(in1_ptr + (((((((((tl.program_id(0) // 127000) % 128) * 64) + (((_lv0 * 1024) + tl.arange(0, 1024)) // 35)) * 5) + ((((_lv0 * 1024) + tl.arange(0, 1024)) // 7) % 5)) * 7) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 7)) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 2240) & (((((tl.program_id(0) // 250) % 508) + ((((_lv0 * 1024) + tl.arange(0, 1024)) // 7) % 5)) < 512) & (((tl.program_id(0) % 250) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 7)) < 256))), other=0.0)), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t056(out, ins):
    grid = (130048000,)
    t056_kernel[grid](out, ins[0], ins[1])
    return out
