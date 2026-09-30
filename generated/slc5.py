import torch
import triton
import triton.language as tl


@triton.jit
def _mul_combine(a, b):
    return a * b


@triton.jit
def slc5_s0_kernel(out_ptr, in0_ptr):
    _acc0 = tl.zeros([1], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), tl.load(in0_ptr + ((((((tl.program_id(0) // 48) * 9) + (((tl.program_id(0) // 12) % 4) + 5)) * 12) + (tl.program_id(0) % 12)) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0), 0.0))
    _v = (tl.sum(_acc0, axis=0) * (3.0 * (1.0 / 1.0)))
    tl.store(out_ptr + tl.program_id(0), _v)


def slc5_s0(out, ins):
    grid = (96,)
    slc5_s0_kernel[grid](out, ins[0])
    return out


def slc5(out, ins):
    slc5_s0(out, list(ins))
    return out
