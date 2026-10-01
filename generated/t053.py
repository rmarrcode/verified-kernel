import torch
import triton
import triton.language as tl


@triton.jit
def _mul_combine(a, b):
    return a * b


@triton.jit
def t053_kernel(out_ptr, in0_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (((0.0 * (1.0 / 1.0)) - tl.load(in0_ptr + ((((((tl.program_id(0) // 4095) * 4096) + 0) * 4095) + (tl.program_id(0) % 4095))))))
    for _lv0 in range(0, 4):
        _acc0 = tl.maximum(_acc0, ((0.0 * (1.0 / 1.0)) - tl.load(in0_ptr + ((((((tl.program_id(0) // 4095) * 4096) + tl.maximum(((_lv0 * 1024) + tl.arange(0, 1024)) - tl.maximum(((_lv0 * 1024) + tl.arange(0, 1024)) - 4095, 0), 0)) * 4095) + (tl.program_id(0) % 4095))))))
    _v = ((0.0 * (1.0 / 1.0)) - tl.max(_acc0, axis=0))
    tl.store(out_ptr + tl.program_id(0), _v)


def t053(out, ins):
    grid = (262080,)
    t053_kernel[grid](out, ins[0])
    return out
