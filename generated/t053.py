import torch
import triton
import triton.language as tl


@triton.jit
def _mul_combine(a, b):
    return a * b


@triton.jit
def t053_s0_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 8):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 8192) & True), (tl.load(in0_ptr + ((((tl.program_id(0) // 8192) * 8192) + ((_lv0 * 1024) + tl.arange(0, 1024))) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 8192) & True), other=0.0) * tl.load(in1_ptr + ((((tl.program_id(0) % 8192) * 8192) + ((_lv0 * 1024) + tl.arange(0, 1024))) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 8192) & True), other=0.0)), 0.0))
    _v = (((1.0 * (1.0 / 2.0)) * tl.minimum(tl.maximum(((tl.sum(_acc0, axis=0) + tl.load(in2_ptr + ((tl.program_id(0) % 8192)))) * (1.0 * (1.0 / 2.0))), (0.0 - (2.0 * (1.0 / 1.0)))), (2.0 * (1.0 / 1.0)))) * ((1.0 * (1.0 / 1.0)) + tl.erf((tl.minimum(tl.maximum(((tl.sum(_acc0, axis=0) + tl.load(in2_ptr + ((tl.program_id(0) % 8192)))) * (1.0 * (1.0 / 2.0))), (0.0 - (2.0 * (1.0 / 1.0)))), (2.0 * (1.0 / 1.0))) * (1.0 / tl.sqrt((2.0 * (1.0 / 1.0))))))))
    tl.store(out_ptr + tl.program_id(0), _v)


def t053_s0(out, ins):
    grid = (16777216,)
    t053_s0_kernel[grid](out, ins[0], ins[1], ins[2])
    return out


def t053(out, ins):
    t053_s0(out, list(ins))
    return out
