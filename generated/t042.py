import torch
import triton
import triton.language as tl


@triton.jit
def _mul_combine(a, b):
    return a * b


@triton.jit
def t042_kernel(out_ptr, in0_ptr):
    _acc0 = tl.zeros([16], dtype=tl.float32) + (tl.load(in0_ptr + ((((((((tl.program_id(0) // 16711744) * 64) + ((tl.program_id(0) // 261121) % 64)) * 512) + tl.maximum((((tl.program_id(0) // 511) % 511) + tl.maximum(((0 // 4) + tl.maximum(tl.maximum(1 - ((tl.program_id(0) // 511) % 511), 0) - (0 // 4), 0)) - tl.maximum(((0 // 4) + tl.maximum(tl.maximum(1 - ((tl.program_id(0) // 511) % 511), 0) - (0 // 4), 0)) - tl.maximum(512 - ((tl.program_id(0) // 511) % 511), 0), 0), 0)) - 1, 0)) * 512) + tl.maximum(((tl.program_id(0) % 511) + tl.maximum(((0 % 4) + tl.maximum(tl.maximum(1 - (tl.program_id(0) % 511), 0) - (0 % 4), 0)) - tl.maximum(((0 % 4) + tl.maximum(tl.maximum(1 - (tl.program_id(0) % 511), 0) - (0 % 4), 0)) - tl.maximum(512 - (tl.program_id(0) % 511), 0), 0), 0)) - 1, 0)))))
    for _lv0 in range(0, 1):
        _acc0 = tl.maximum(_acc0, tl.load(in0_ptr + ((((((((tl.program_id(0) // 16711744) * 64) + ((tl.program_id(0) // 261121) % 64)) * 512) + tl.maximum((((tl.program_id(0) // 511) % 511) + tl.maximum(((tl.maximum(((_lv0 * 16) + tl.arange(0, 16)) - tl.maximum(((_lv0 * 16) + tl.arange(0, 16)) - 15, 0), 0) // 4) + tl.maximum(tl.maximum(1 - ((tl.program_id(0) // 511) % 511), 0) - (tl.maximum(((_lv0 * 16) + tl.arange(0, 16)) - tl.maximum(((_lv0 * 16) + tl.arange(0, 16)) - 15, 0), 0) // 4), 0)) - tl.maximum(((tl.maximum(((_lv0 * 16) + tl.arange(0, 16)) - tl.maximum(((_lv0 * 16) + tl.arange(0, 16)) - 15, 0), 0) // 4) + tl.maximum(tl.maximum(1 - ((tl.program_id(0) // 511) % 511), 0) - (tl.maximum(((_lv0 * 16) + tl.arange(0, 16)) - tl.maximum(((_lv0 * 16) + tl.arange(0, 16)) - 15, 0), 0) // 4), 0)) - tl.maximum(512 - ((tl.program_id(0) // 511) % 511), 0), 0), 0)) - 1, 0)) * 512) + tl.maximum(((tl.program_id(0) % 511) + tl.maximum(((tl.maximum(((_lv0 * 16) + tl.arange(0, 16)) - tl.maximum(((_lv0 * 16) + tl.arange(0, 16)) - 15, 0), 0) % 4) + tl.maximum(tl.maximum(1 - (tl.program_id(0) % 511), 0) - (tl.maximum(((_lv0 * 16) + tl.arange(0, 16)) - tl.maximum(((_lv0 * 16) + tl.arange(0, 16)) - 15, 0), 0) % 4), 0)) - tl.maximum(((tl.maximum(((_lv0 * 16) + tl.arange(0, 16)) - tl.maximum(((_lv0 * 16) + tl.arange(0, 16)) - 15, 0), 0) % 4) + tl.maximum(tl.maximum(1 - (tl.program_id(0) % 511), 0) - (tl.maximum(((_lv0 * 16) + tl.arange(0, 16)) - tl.maximum(((_lv0 * 16) + tl.arange(0, 16)) - 15, 0), 0) % 4), 0)) - tl.maximum(512 - (tl.program_id(0) % 511), 0), 0), 0)) - 1, 0)))))
    _v = tl.max(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t042(out, ins):
    grid = (267387904,)
    t042_kernel[grid](out, ins[0])
    return out
