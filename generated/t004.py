import torch
import triton
import triton.language as tl


@triton.jit
def _mul_combine(a, b):
    return a * b


@triton.jit
def t004_s0_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr):
    _acc0 = tl.zeros([16], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 16) + tl.arange(0, 16)) < 25) & (((((tl.program_id(0) // 28) % 28) + ((((_lv0 * 16) + tl.arange(0, 16)) // 5) % 5)) < 32) & (((tl.program_id(0) % 28) + (((_lv0 * 16) + tl.arange(0, 16)) % 5)) < 32))), (tl.load(in0_ptr + ((((((tl.program_id(0) // 4704) * 32) + (((tl.program_id(0) // 28) % 28) + ((((_lv0 * 16) + tl.arange(0, 16)) // 5) % 5))) * 32) + ((tl.program_id(0) % 28) + (((_lv0 * 16) + tl.arange(0, 16)) % 5))) + 0 * tl.arange(0, 16)), mask=((((_lv0 * 16) + tl.arange(0, 16)) < 25) & (((((tl.program_id(0) // 28) % 28) + ((((_lv0 * 16) + tl.arange(0, 16)) // 5) % 5)) < 32) & (((tl.program_id(0) % 28) + (((_lv0 * 16) + tl.arange(0, 16)) % 5)) < 32))), other=0.0) * tl.load(in1_ptr + (((((((tl.program_id(0) // 784) % 6) * 5) + ((((_lv0 * 16) + tl.arange(0, 16)) // 5) % 5)) * 5) + (((_lv0 * 16) + tl.arange(0, 16)) % 5)) + 0 * tl.arange(0, 16)), mask=((((_lv0 * 16) + tl.arange(0, 16)) < 25) & (((((tl.program_id(0) // 28) % 28) + ((((_lv0 * 16) + tl.arange(0, 16)) // 5) % 5)) < 32) & (((tl.program_id(0) % 28) + (((_lv0 * 16) + tl.arange(0, 16)) % 5)) < 32))), other=0.0)), 0.0))
    _v = tl.maximum((tl.sum(_acc0, axis=0) + tl.load(in2_ptr + (((tl.program_id(0) // 784) % 6)))), (0.0 * (1.0 / 1.0)))
    tl.store(out_ptr + tl.program_id(0), _v)


def t004_s0(out, ins):
    grid = (19267584,)
    t004_s0_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10])
    return out


@triton.jit
def t004_s1_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr):
    _acc0 = tl.zeros([4], dtype=tl.float32) + (tl.load(in11_ptr + ((((((((tl.program_id(0) // 1176) * 6) + ((tl.program_id(0) // 196) % 6)) * 28) + tl.maximum(((((tl.program_id(0) // 14) % 14) * 2) + tl.maximum(((0 // 2) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 14) % 14) * 2), 0) - (0 // 2), 0)) - tl.maximum(((0 // 2) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 14) % 14) * 2), 0) - (0 // 2), 0)) - tl.maximum(27 - (((tl.program_id(0) // 14) % 14) * 2), 0), 0), 0)) - tl.maximum(((((tl.program_id(0) // 14) % 14) * 2) + tl.maximum(((0 // 2) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 14) % 14) * 2), 0) - (0 // 2), 0)) - tl.maximum(((0 // 2) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 14) % 14) * 2), 0) - (0 // 2), 0)) - tl.maximum(27 - (((tl.program_id(0) // 14) % 14) * 2), 0), 0), 0)) - 27, 0), 0)) * 28) + tl.maximum((((tl.program_id(0) % 14) * 2) + tl.maximum(((0 % 2) + tl.maximum(tl.maximum(0 - ((tl.program_id(0) % 14) * 2), 0) - (0 % 2), 0)) - tl.maximum(((0 % 2) + tl.maximum(tl.maximum(0 - ((tl.program_id(0) % 14) * 2), 0) - (0 % 2), 0)) - tl.maximum(27 - ((tl.program_id(0) % 14) * 2), 0), 0), 0)) - tl.maximum((((tl.program_id(0) % 14) * 2) + tl.maximum(((0 % 2) + tl.maximum(tl.maximum(0 - ((tl.program_id(0) % 14) * 2), 0) - (0 % 2), 0)) - tl.maximum(((0 % 2) + tl.maximum(tl.maximum(0 - ((tl.program_id(0) % 14) * 2), 0) - (0 % 2), 0)) - tl.maximum(27 - ((tl.program_id(0) % 14) * 2), 0), 0), 0)) - 27, 0), 0)))))
    for _lv0 in range(0, 1):
        _acc0 = tl.maximum(_acc0, tl.load(in11_ptr + ((((((((tl.program_id(0) // 1176) * 6) + ((tl.program_id(0) // 196) % 6)) * 28) + tl.maximum(((((tl.program_id(0) // 14) % 14) * 2) + tl.maximum(((tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - 3, 0), 0) // 2) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 14) % 14) * 2), 0) - (tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - 3, 0), 0) // 2), 0)) - tl.maximum(((tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - 3, 0), 0) // 2) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 14) % 14) * 2), 0) - (tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - 3, 0), 0) // 2), 0)) - tl.maximum(27 - (((tl.program_id(0) // 14) % 14) * 2), 0), 0), 0)) - tl.maximum(((((tl.program_id(0) // 14) % 14) * 2) + tl.maximum(((tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - 3, 0), 0) // 2) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 14) % 14) * 2), 0) - (tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - 3, 0), 0) // 2), 0)) - tl.maximum(((tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - 3, 0), 0) // 2) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 14) % 14) * 2), 0) - (tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - 3, 0), 0) // 2), 0)) - tl.maximum(27 - (((tl.program_id(0) // 14) % 14) * 2), 0), 0), 0)) - 27, 0), 0)) * 28) + tl.maximum((((tl.program_id(0) % 14) * 2) + tl.maximum(((tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - 3, 0), 0) % 2) + tl.maximum(tl.maximum(0 - ((tl.program_id(0) % 14) * 2), 0) - (tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - 3, 0), 0) % 2), 0)) - tl.maximum(((tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - 3, 0), 0) % 2) + tl.maximum(tl.maximum(0 - ((tl.program_id(0) % 14) * 2), 0) - (tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - 3, 0), 0) % 2), 0)) - tl.maximum(27 - ((tl.program_id(0) % 14) * 2), 0), 0), 0)) - tl.maximum((((tl.program_id(0) % 14) * 2) + tl.maximum(((tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - 3, 0), 0) % 2) + tl.maximum(tl.maximum(0 - ((tl.program_id(0) % 14) * 2), 0) - (tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - 3, 0), 0) % 2), 0)) - tl.maximum(((tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - 3, 0), 0) % 2) + tl.maximum(tl.maximum(0 - ((tl.program_id(0) % 14) * 2), 0) - (tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - 3, 0), 0) % 2), 0)) - tl.maximum(27 - ((tl.program_id(0) % 14) * 2), 0), 0), 0)) - 27, 0), 0)))))
    _v = tl.max(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t004_s1(out, ins):
    grid = (4816896,)
    t004_s1_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11])
    return out


@triton.jit
def t004_s2_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr):
    _acc0 = tl.zeros([128], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 128) + tl.arange(0, 128)) < 150) & (((((tl.program_id(0) // 10) % 10) + ((((_lv0 * 128) + tl.arange(0, 128)) // 5) % 5)) < 14) & (((tl.program_id(0) % 10) + (((_lv0 * 128) + tl.arange(0, 128)) % 5)) < 14))), (tl.load(in12_ptr + (tl.maximum((((((((tl.program_id(0) // 1600) * 6) + (((_lv0 * 128) + tl.arange(0, 128)) // 25)) * 14) + (((tl.program_id(0) // 10) % 10) + ((((_lv0 * 128) + tl.arange(0, 128)) // 5) % 5))) * 14) + ((tl.program_id(0) % 10) + (((_lv0 * 128) + tl.arange(0, 128)) % 5))) - tl.maximum((((((((tl.program_id(0) // 1600) * 6) + (((_lv0 * 128) + tl.arange(0, 128)) // 25)) * 14) + (((tl.program_id(0) // 10) % 10) + ((((_lv0 * 128) + tl.arange(0, 128)) // 5) % 5))) * 14) + ((tl.program_id(0) % 10) + (((_lv0 * 128) + tl.arange(0, 128)) % 5))) - 4816895, 0), 0) + 0 * tl.arange(0, 128)), mask=((((_lv0 * 128) + tl.arange(0, 128)) < 150) & (((((tl.program_id(0) // 10) % 10) + ((((_lv0 * 128) + tl.arange(0, 128)) // 5) % 5)) < 14) & (((tl.program_id(0) % 10) + (((_lv0 * 128) + tl.arange(0, 128)) % 5)) < 14))), other=0.0) * tl.load(in3_ptr + (((((((((tl.program_id(0) // 100) % 16) * 6) + (((_lv0 * 128) + tl.arange(0, 128)) // 25)) * 5) + ((((_lv0 * 128) + tl.arange(0, 128)) // 5) % 5)) * 5) + (((_lv0 * 128) + tl.arange(0, 128)) % 5)) + 0 * tl.arange(0, 128)), mask=((((_lv0 * 128) + tl.arange(0, 128)) < 150) & (((((tl.program_id(0) // 10) % 10) + ((((_lv0 * 128) + tl.arange(0, 128)) // 5) % 5)) < 14) & (((tl.program_id(0) % 10) + (((_lv0 * 128) + tl.arange(0, 128)) % 5)) < 14))), other=0.0)), 0.0))
    _v = tl.maximum((tl.sum(_acc0, axis=0) + tl.load(in4_ptr + (((tl.program_id(0) // 100) % 16)))), (0.0 * (1.0 / 1.0)))
    tl.store(out_ptr + tl.program_id(0), _v)


def t004_s2(out, ins):
    grid = (6553600,)
    t004_s2_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12])
    return out


@triton.jit
def t004_s3_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr):
    _acc0 = tl.zeros([4], dtype=tl.float32) + (tl.load(in13_ptr + ((((((((tl.program_id(0) // 400) * 16) + ((tl.program_id(0) // 25) % 16)) * 10) + tl.maximum(((((tl.program_id(0) // 5) % 5) * 2) + tl.maximum(((0 // 2) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 5) % 5) * 2), 0) - (0 // 2), 0)) - tl.maximum(((0 // 2) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 5) % 5) * 2), 0) - (0 // 2), 0)) - tl.maximum(9 - (((tl.program_id(0) // 5) % 5) * 2), 0), 0), 0)) - tl.maximum(((((tl.program_id(0) // 5) % 5) * 2) + tl.maximum(((0 // 2) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 5) % 5) * 2), 0) - (0 // 2), 0)) - tl.maximum(((0 // 2) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 5) % 5) * 2), 0) - (0 // 2), 0)) - tl.maximum(9 - (((tl.program_id(0) // 5) % 5) * 2), 0), 0), 0)) - 9, 0), 0)) * 10) + tl.maximum((((tl.program_id(0) % 5) * 2) + tl.maximum(((0 % 2) + tl.maximum(tl.maximum(0 - ((tl.program_id(0) % 5) * 2), 0) - (0 % 2), 0)) - tl.maximum(((0 % 2) + tl.maximum(tl.maximum(0 - ((tl.program_id(0) % 5) * 2), 0) - (0 % 2), 0)) - tl.maximum(9 - ((tl.program_id(0) % 5) * 2), 0), 0), 0)) - tl.maximum((((tl.program_id(0) % 5) * 2) + tl.maximum(((0 % 2) + tl.maximum(tl.maximum(0 - ((tl.program_id(0) % 5) * 2), 0) - (0 % 2), 0)) - tl.maximum(((0 % 2) + tl.maximum(tl.maximum(0 - ((tl.program_id(0) % 5) * 2), 0) - (0 % 2), 0)) - tl.maximum(9 - ((tl.program_id(0) % 5) * 2), 0), 0), 0)) - 9, 0), 0)))))
    for _lv0 in range(0, 1):
        _acc0 = tl.maximum(_acc0, tl.load(in13_ptr + ((((((((tl.program_id(0) // 400) * 16) + ((tl.program_id(0) // 25) % 16)) * 10) + tl.maximum(((((tl.program_id(0) // 5) % 5) * 2) + tl.maximum(((tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - 3, 0), 0) // 2) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 5) % 5) * 2), 0) - (tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - 3, 0), 0) // 2), 0)) - tl.maximum(((tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - 3, 0), 0) // 2) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 5) % 5) * 2), 0) - (tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - 3, 0), 0) // 2), 0)) - tl.maximum(9 - (((tl.program_id(0) // 5) % 5) * 2), 0), 0), 0)) - tl.maximum(((((tl.program_id(0) // 5) % 5) * 2) + tl.maximum(((tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - 3, 0), 0) // 2) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 5) % 5) * 2), 0) - (tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - 3, 0), 0) // 2), 0)) - tl.maximum(((tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - 3, 0), 0) // 2) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 5) % 5) * 2), 0) - (tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - 3, 0), 0) // 2), 0)) - tl.maximum(9 - (((tl.program_id(0) // 5) % 5) * 2), 0), 0), 0)) - 9, 0), 0)) * 10) + tl.maximum((((tl.program_id(0) % 5) * 2) + tl.maximum(((tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - 3, 0), 0) % 2) + tl.maximum(tl.maximum(0 - ((tl.program_id(0) % 5) * 2), 0) - (tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - 3, 0), 0) % 2), 0)) - tl.maximum(((tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - 3, 0), 0) % 2) + tl.maximum(tl.maximum(0 - ((tl.program_id(0) % 5) * 2), 0) - (tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - 3, 0), 0) % 2), 0)) - tl.maximum(9 - ((tl.program_id(0) % 5) * 2), 0), 0), 0)) - tl.maximum((((tl.program_id(0) % 5) * 2) + tl.maximum(((tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - 3, 0), 0) % 2) + tl.maximum(tl.maximum(0 - ((tl.program_id(0) % 5) * 2), 0) - (tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - 3, 0), 0) % 2), 0)) - tl.maximum(((tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - 3, 0), 0) % 2) + tl.maximum(tl.maximum(0 - ((tl.program_id(0) % 5) * 2), 0) - (tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - 3, 0), 0) % 2), 0)) - tl.maximum(9 - ((tl.program_id(0) % 5) * 2), 0), 0), 0)) - 9, 0), 0)))))
    _v = tl.max(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t004_s3(out, ins):
    grid = (1638400,)
    t004_s3_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13])
    return out


@triton.jit
def t004_s4_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr):
    _acc0 = tl.zeros([256], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 256) + tl.arange(0, 256)) < 400) & True), (tl.load(in14_ptr + (tl.maximum((((tl.program_id(0) // 120) * 400) + ((_lv0 * 256) + tl.arange(0, 256))) - tl.maximum((((tl.program_id(0) // 120) * 400) + ((_lv0 * 256) + tl.arange(0, 256))) - 1638399, 0), 0) + 0 * tl.arange(0, 256)), mask=((((_lv0 * 256) + tl.arange(0, 256)) < 400) & True), other=0.0) * tl.load(in5_ptr + ((((tl.program_id(0) % 120) * 400) + ((_lv0 * 256) + tl.arange(0, 256))) + 0 * tl.arange(0, 256)), mask=((((_lv0 * 256) + tl.arange(0, 256)) < 400) & True), other=0.0)), 0.0))
    _v = tl.maximum((tl.sum(_acc0, axis=0) + tl.load(in6_ptr + ((tl.program_id(0) % 120)))), (0.0 * (1.0 / 1.0)))
    tl.store(out_ptr + tl.program_id(0), _v)


def t004_s4(out, ins):
    grid = (491520,)
    t004_s4_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14])
    return out


@triton.jit
def t004_s5_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr):
    _acc0 = tl.zeros([64], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 64) + tl.arange(0, 64)) < 120) & True), (tl.load(in15_ptr + ((((tl.program_id(0) // 84) * 120) + ((_lv0 * 64) + tl.arange(0, 64))) + 0 * tl.arange(0, 64)), mask=((((_lv0 * 64) + tl.arange(0, 64)) < 120) & True), other=0.0) * tl.load(in7_ptr + ((((tl.program_id(0) % 84) * 120) + ((_lv0 * 64) + tl.arange(0, 64))) + 0 * tl.arange(0, 64)), mask=((((_lv0 * 64) + tl.arange(0, 64)) < 120) & True), other=0.0)), 0.0))
    _v = tl.maximum((tl.sum(_acc0, axis=0) + tl.load(in8_ptr + ((tl.program_id(0) % 84)))), (0.0 * (1.0 / 1.0)))
    tl.store(out_ptr + tl.program_id(0), _v)


def t004_s5(out, ins):
    grid = (344064,)
    t004_s5_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15])
    return out


@triton.jit
def t004_s6_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr):
    _acc0 = tl.zeros([64], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 64) + tl.arange(0, 64)) < 84) & True), (tl.load(in16_ptr + ((((tl.program_id(0) // 20) * 84) + ((_lv0 * 64) + tl.arange(0, 64))) + 0 * tl.arange(0, 64)), mask=((((_lv0 * 64) + tl.arange(0, 64)) < 84) & True), other=0.0) * tl.load(in9_ptr + ((((tl.program_id(0) % 20) * 84) + ((_lv0 * 64) + tl.arange(0, 64))) + 0 * tl.arange(0, 64)), mask=((((_lv0 * 64) + tl.arange(0, 64)) < 84) & True), other=0.0)), 0.0))
    _v = (tl.sum(_acc0, axis=0) + tl.load(in10_ptr + ((tl.program_id(0) % 20))))
    tl.store(out_ptr + tl.program_id(0), _v)


def t004_s6(out, ins):
    grid = (81920,)
    t004_s6_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16])
    return out


def t004(out, ins):
    _t0 = torch.empty(19267584, device=ins[0].device, dtype=torch.float32)
    _t1 = torch.empty(4816896, device=ins[0].device, dtype=torch.float32)
    _t2 = torch.empty(6553600, device=ins[0].device, dtype=torch.float32)
    _t3 = torch.empty(1638400, device=ins[0].device, dtype=torch.float32)
    _t4 = torch.empty(491520, device=ins[0].device, dtype=torch.float32)
    _t5 = torch.empty(344064, device=ins[0].device, dtype=torch.float32)
    t004_s0(_t0, list(ins))
    t004_s1(_t1, list(ins) + [_t0])
    t004_s2(_t2, list(ins) + [_t0, _t1])
    t004_s3(_t3, list(ins) + [_t0, _t1, _t2])
    t004_s4(_t4, list(ins) + [_t0, _t1, _t2, _t3])
    t004_s5(_t5, list(ins) + [_t0, _t1, _t2, _t3, _t4])
    t004_s6(out, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5])
    return out
