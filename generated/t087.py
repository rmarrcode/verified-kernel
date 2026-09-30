import torch
import triton
import triton.language as tl


@triton.jit
def _mul_combine(a, b):
    return a * b


@triton.jit
def t087_s0_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr):
    _acc0 = tl.zeros([64], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 64) + tl.arange(0, 64)) < 72) & (((((tl.program_id(0) // 254) % 254) + ((((_lv0 * 64) + tl.arange(0, 64)) // 3) % 3)) < 256) & (((tl.program_id(0) % 254) + (((_lv0 * 64) + tl.arange(0, 64)) % 3)) < 256))), (tl.load(in0_ptr + ((((((((tl.program_id(0) // 4129024) * 8) + (((_lv0 * 64) + tl.arange(0, 64)) // 9)) * 256) + (((tl.program_id(0) // 254) % 254) + ((((_lv0 * 64) + tl.arange(0, 64)) // 3) % 3))) * 256) + ((tl.program_id(0) % 254) + (((_lv0 * 64) + tl.arange(0, 64)) % 3))) + 0 * tl.arange(0, 64)), mask=((((_lv0 * 64) + tl.arange(0, 64)) < 72) & (((((tl.program_id(0) // 254) % 254) + ((((_lv0 * 64) + tl.arange(0, 64)) // 3) % 3)) < 256) & (((tl.program_id(0) % 254) + (((_lv0 * 64) + tl.arange(0, 64)) % 3)) < 256))), other=0.0) * tl.load(in1_ptr + (((((((((tl.program_id(0) // 64516) % 64) * 8) + (((_lv0 * 64) + tl.arange(0, 64)) // 9)) * 3) + ((((_lv0 * 64) + tl.arange(0, 64)) // 3) % 3)) * 3) + (((_lv0 * 64) + tl.arange(0, 64)) % 3)) + 0 * tl.arange(0, 64)), mask=((((_lv0 * 64) + tl.arange(0, 64)) < 72) & (((((tl.program_id(0) // 254) % 254) + ((((_lv0 * 64) + tl.arange(0, 64)) // 3) % 3)) < 256) & (((tl.program_id(0) % 254) + (((_lv0 * 64) + tl.arange(0, 64)) % 3)) < 256))), other=0.0)), 0.0))
    _v = ((((tl.sum(_acc0, axis=0) + tl.load(in2_ptr + (((tl.program_id(0) // 64516) % 64)))) - (1.0 * (1.0 / 2.0))) - (1.0 * (1.0 / 5.0))) * (2.0 * tl.sigmoid(2.0 * (tl.log(((1.0 * (1.0 / 1.0)) + tl.exp((((tl.sum(_acc0, axis=0) + tl.load(in2_ptr + (((tl.program_id(0) // 64516) % 64)))) - (1.0 * (1.0 / 2.0))) - (1.0 * (1.0 / 5.0)))))))) - 1.0))
    tl.store(out_ptr + tl.program_id(0), _v)


def t087_s0(out, ins):
    grid = (264257536,)
    t087_s0_kernel[grid](out, ins[0], ins[1], ins[2])
    return out


def t087(out, ins):
    t087_s0(out, list(ins))
    return out
