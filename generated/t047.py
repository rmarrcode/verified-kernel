import torch
import triton
import triton.language as tl


@triton.jit
def _mul_combine(a, b):
    return a * b


@triton.jit
def t047_s0_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr):
    _acc0 = tl.zeros([512], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 512) + tl.arange(0, 512)) < 864) & ((((((tl.program_id(0) // 3844) % 30) + ((((_lv0 * 512) + tl.arange(0, 512)) // 9) % 3)) < 32) & ((((tl.program_id(0) // 62) % 62) + ((((_lv0 * 512) + tl.arange(0, 512)) // 3) % 3)) < 64)) & (((tl.program_id(0) % 62) + (((_lv0 * 512) + tl.arange(0, 512)) % 3)) < 64))), (tl.load(in0_ptr + ((((((((((tl.program_id(0) // 7380480) * 32) + (((_lv0 * 512) + tl.arange(0, 512)) // 27)) * 32) + (((tl.program_id(0) // 3844) % 30) + ((((_lv0 * 512) + tl.arange(0, 512)) // 9) % 3))) * 64) + (((tl.program_id(0) // 62) % 62) + ((((_lv0 * 512) + tl.arange(0, 512)) // 3) % 3))) * 64) + ((tl.program_id(0) % 62) + (((_lv0 * 512) + tl.arange(0, 512)) % 3))) + 0 * tl.arange(0, 512)), mask=((((_lv0 * 512) + tl.arange(0, 512)) < 864) & ((((((tl.program_id(0) // 3844) % 30) + ((((_lv0 * 512) + tl.arange(0, 512)) // 9) % 3)) < 32) & ((((tl.program_id(0) // 62) % 62) + ((((_lv0 * 512) + tl.arange(0, 512)) // 3) % 3)) < 64)) & (((tl.program_id(0) % 62) + (((_lv0 * 512) + tl.arange(0, 512)) % 3)) < 64))), other=0.0) * tl.load(in1_ptr + (((((((((((tl.program_id(0) // 115320) % 64) * 32) + (((_lv0 * 512) + tl.arange(0, 512)) // 27)) * 3) + ((((_lv0 * 512) + tl.arange(0, 512)) // 9) % 3)) * 3) + ((((_lv0 * 512) + tl.arange(0, 512)) // 3) % 3)) * 3) + (((_lv0 * 512) + tl.arange(0, 512)) % 3)) + 0 * tl.arange(0, 512)), mask=((((_lv0 * 512) + tl.arange(0, 512)) < 864) & ((((((tl.program_id(0) // 3844) % 30) + ((((_lv0 * 512) + tl.arange(0, 512)) // 9) % 3)) < 32) & ((((tl.program_id(0) // 62) % 62) + ((((_lv0 * 512) + tl.arange(0, 512)) // 3) % 3)) < 64)) & (((tl.program_id(0) % 62) + (((_lv0 * 512) + tl.arange(0, 512)) % 3)) < 64))), other=0.0)), 0.0))
    _v = (2.0 * tl.sigmoid(2.0 * (((tl.sum(_acc0, axis=0) + tl.load(in2_ptr + (((tl.program_id(0) // 115320) % 64)))) * (2.0 * tl.sigmoid(2.0 * (tl.log(((1.0 * (1.0 / 1.0)) + tl.exp((tl.sum(_acc0, axis=0) + tl.load(in2_ptr + (((tl.program_id(0) // 115320) % 64))))))))) - 1.0)))) - 1.0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t047_s0(out, ins):
    grid = (118087680,)
    t047_s0_kernel[grid](out, ins[0], ins[1], ins[2])
    return out


def t047(out, ins):
    t047_s0(out, list(ins))
    return out
