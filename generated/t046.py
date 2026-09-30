import torch
import triton
import triton.language as tl


@triton.jit
def _mul_combine(a, b):
    return a * b


@triton.jit
def t046_s0_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr):
    _acc0 = tl.zeros([512], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 512) + tl.arange(0, 512)) < 512) & True), (tl.load(in0_ptr + (((((tl.program_id(0) // 48) % 204800) * 512) + ((_lv0 * 512) + tl.arange(0, 512))) + 0 * tl.arange(0, 512)), mask=((((_lv0 * 512) + tl.arange(0, 512)) < 512) & True), other=0.0) * tl.load(in1_ptr + (((((_lv0 * 512) + tl.arange(0, 512)) * 48) + (tl.program_id(0) % 48)) + 0 * tl.arange(0, 512)), mask=((((_lv0 * 512) + tl.arange(0, 512)) < 512) & True), other=0.0)), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t046_s0(out, ins):
    grid = (9830400,)
    t046_s0_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4])
    return out


@triton.jit
def t046_s1_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr):
    _acc0 = tl.zeros([512], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 512) + tl.arange(0, 512)) < 800) & ((((tl.program_id(0) % 256) * 800) + ((_lv0 * 512) + tl.arange(0, 512))) < 204800)), tl.load(in5_ptr + ((((((tl.program_id(0) % 256) * 800) + ((_lv0 * 512) + tl.arange(0, 512))) * 48) + (tl.program_id(0) // 256)) + 0 * tl.arange(0, 512)), mask=((((_lv0 * 512) + tl.arange(0, 512)) < 800) & ((((tl.program_id(0) % 256) * 800) + ((_lv0 * 512) + tl.arange(0, 512))) < 204800)), other=0.0), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t046_s1(out, ins):
    grid = (12288,)
    t046_s1_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5])
    return out


@triton.jit
def t046_s2_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr):
    _acc0 = tl.zeros([256], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 256) + tl.arange(0, 256)) < 256) & True), tl.load(in6_ptr + (((tl.program_id(0) * 256) + ((_lv0 * 256) + tl.arange(0, 256))) + 0 * tl.arange(0, 256)), mask=((((_lv0 * 256) + tl.arange(0, 256)) < 256) & True), other=0.0), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t046_s2(out, ins):
    grid = (48,)
    t046_s2_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6])
    return out


@triton.jit
def t046_s3_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr):
    _acc0 = tl.zeros([512], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 512) + tl.arange(0, 512)) < 800) & ((((tl.program_id(0) % 256) * 800) + ((_lv0 * 512) + tl.arange(0, 512))) < 204800)), ((tl.load(in5_ptr + ((((((tl.program_id(0) % 256) * 800) + ((_lv0 * 512) + tl.arange(0, 512))) * 48) + (tl.program_id(0) // 256)) + 0 * tl.arange(0, 512)), mask=((((_lv0 * 512) + tl.arange(0, 512)) < 800) & ((((tl.program_id(0) % 256) * 800) + ((_lv0 * 512) + tl.arange(0, 512))) < 204800)), other=0.0) - (tl.load(in7_ptr + (tl.maximum((tl.program_id(0) // 256) - tl.maximum((tl.program_id(0) // 256) - 47, 0), 0) + 0 * tl.arange(0, 512)), mask=((((_lv0 * 512) + tl.arange(0, 512)) < 800) & ((((tl.program_id(0) % 256) * 800) + ((_lv0 * 512) + tl.arange(0, 512))) < 204800)), other=0.0) * (1.0 * (1.0 / 204800.0)))) * (tl.load(in5_ptr + ((((((tl.program_id(0) % 256) * 800) + ((_lv0 * 512) + tl.arange(0, 512))) * 48) + (tl.program_id(0) // 256)) + 0 * tl.arange(0, 512)), mask=((((_lv0 * 512) + tl.arange(0, 512)) < 800) & ((((tl.program_id(0) % 256) * 800) + ((_lv0 * 512) + tl.arange(0, 512))) < 204800)), other=0.0) - (tl.load(in7_ptr + (tl.maximum((tl.program_id(0) // 256) - tl.maximum((tl.program_id(0) // 256) - 47, 0), 0) + 0 * tl.arange(0, 512)), mask=((((_lv0 * 512) + tl.arange(0, 512)) < 800) & ((((tl.program_id(0) % 256) * 800) + ((_lv0 * 512) + tl.arange(0, 512))) < 204800)), other=0.0) * (1.0 * (1.0 / 204800.0))))), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t046_s3(out, ins):
    grid = (12288,)
    t046_s3_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7])
    return out


@triton.jit
def t046_s4_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr):
    _acc0 = tl.zeros([256], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 256) + tl.arange(0, 256)) < 256) & True), tl.load(in8_ptr + (((tl.program_id(0) * 256) + ((_lv0 * 256) + tl.arange(0, 256))) + 0 * tl.arange(0, 256)), mask=((((_lv0 * 256) + tl.arange(0, 256)) < 256) & True), other=0.0), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t046_s4(out, ins):
    grid = (48,)
    t046_s4_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8])
    return out


@triton.jit
def t046_s5_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr):
    _acc0 = tl.zeros([1], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), ((((tl.load(in5_ptr + (tl.program_id(0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) - (tl.load(in7_ptr + (tl.maximum((tl.program_id(0) % 48) - tl.maximum((tl.program_id(0) % 48) - 47, 0), 0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) * (1.0 * (1.0 / 204800.0)))) * (1.0 / tl.sqrt(((tl.load(in9_ptr + (tl.maximum((tl.program_id(0) % 48) - tl.maximum((tl.program_id(0) % 48) - 47, 0), 0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) * (1.0 * (1.0 / 204800.0))) + (1.0 * (1.0 / 100000.0)))))) * tl.load(in2_ptr + ((tl.program_id(0) % 48) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)) + tl.load(in3_ptr + ((tl.program_id(0) % 48) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t046_s5(out, ins):
    grid = (9830400,)
    t046_s5_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9])
    return out


@triton.jit
def t046_s6_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr):
    _acc0 = tl.zeros([32], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 32) + tl.arange(0, 32)) < 48) & True), tl.exp(tl.load(in10_ptr + (((tl.program_id(0) * 48) + ((_lv0 * 32) + tl.arange(0, 32))) + 0 * tl.arange(0, 32)), mask=((((_lv0 * 32) + tl.arange(0, 32)) < 48) & True), other=0.0)), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t046_s6(out, ins):
    grid = (204800,)
    t046_s6_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10])
    return out


@triton.jit
def t046_s7_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr):
    _acc0 = tl.zeros([1], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), (tl.exp(tl.load(in10_ptr + (tl.program_id(0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)) * (1.0 / tl.load(in11_ptr + (tl.maximum((tl.program_id(0) // 48) - tl.maximum((tl.program_id(0) // 48) - 204799, 0), 0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0))), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t046_s7(out, ins):
    grid = (9830400,)
    t046_s7_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11])
    return out


@triton.jit
def t046_s8_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr):
    _acc0 = tl.zeros([1], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), tl.load(in12_ptr + (tl.maximum((((tl.program_id(0) // 32) * 48) + (tl.program_id(0) % 32)) - tl.maximum((((tl.program_id(0) // 32) * 48) + (tl.program_id(0) % 32)) - 9830399, 0), 0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t046_s8(out, ins):
    grid = (6553600,)
    t046_s8_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12])
    return out


@triton.jit
def t046_s9_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr):
    _acc0 = tl.zeros([64], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 64) + tl.arange(0, 64)) < 100) & True), tl.load(in13_ptr + ((((((tl.program_id(0) // 32) * 100) + ((_lv0 * 64) + tl.arange(0, 64))) * 32) + (tl.program_id(0) % 32)) + 0 * tl.arange(0, 64)), mask=((((_lv0 * 64) + tl.arange(0, 64)) < 100) & True), other=0.0), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t046_s9(out, ins):
    grid = (65536,)
    t046_s9_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13])
    return out


@triton.jit
def t046_s10_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr):
    _acc0 = tl.zeros([1], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), (tl.load(in14_ptr + ((((tl.program_id(0) // 16384) * 32) + (tl.program_id(0) % 32)) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) * tl.load(in4_ptr + (((((tl.program_id(0) // 32) % 512) * 32) + (tl.program_id(0) % 32)) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t046_s10(out, ins):
    grid = (33554432,)
    t046_s10_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14])
    return out


@triton.jit
def t046_s11_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr):
    _acc0 = tl.zeros([1], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), tl.load(in13_ptr + (tl.maximum((((((tl.program_id(0) // 3200) * 100) + (tl.program_id(0) % 100)) * 32) + ((tl.program_id(0) // 100) % 32)) - tl.maximum((((((tl.program_id(0) // 3200) * 100) + (tl.program_id(0) % 100)) * 32) + ((tl.program_id(0) // 100) % 32)) - 6553599, 0), 0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t046_s11(out, ins):
    grid = (6553600,)
    t046_s11_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15])
    return out


@triton.jit
def t046_s12_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr):
    _acc0 = tl.zeros([64], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 64) + tl.arange(0, 64)) < 100) & True), (tl.load(in16_ptr + ((((((tl.program_id(0) // 16384) * 32) + ((tl.program_id(0) // 512) % 32)) * 100) + ((_lv0 * 64) + tl.arange(0, 64))) + 0 * tl.arange(0, 64)), mask=((((_lv0 * 64) + tl.arange(0, 64)) < 100) & True), other=0.0) * tl.load(in0_ptr + ((((((tl.program_id(0) // 16384) * 100) + ((_lv0 * 64) + tl.arange(0, 64))) * 512) + (tl.program_id(0) % 512)) + 0 * tl.arange(0, 64)), mask=((((_lv0 * 64) + tl.arange(0, 64)) < 100) & True), other=0.0)), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t046_s12(out, ins):
    grid = (33554432,)
    t046_s12_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16])
    return out


@triton.jit
def t046_s13_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr):
    _acc0 = tl.zeros([1], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), tl.load(in17_ptr + ((((((tl.program_id(0) // 16384) * 32) + (tl.program_id(0) % 32)) * 512) + ((tl.program_id(0) // 32) % 512)) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t046_s13(out, ins):
    grid = (33554432,)
    t046_s13_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17])
    return out


@triton.jit
def t046_s14_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr):
    _acc0 = tl.zeros([1], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), (tl.load(in18_ptr + ((((((tl.program_id(0) // 16384) * 512) + ((tl.program_id(0) // 32) % 512)) * 32) + (tl.program_id(0) % 32)) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) - tl.load(in15_ptr + ((((((tl.program_id(0) // 16384) * 512) + ((tl.program_id(0) // 32) % 512)) * 32) + (tl.program_id(0) % 32)) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t046_s14(out, ins):
    grid = (33554432,)
    t046_s14_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18])
    return out


@triton.jit
def t046_s15_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr):
    _acc0 = tl.zeros([512], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 512) + tl.arange(0, 512)) < 512) & True), (tl.load(in19_ptr + ((((((tl.program_id(0) // 32) * 512) + ((_lv0 * 512) + tl.arange(0, 512))) * 32) + (tl.program_id(0) % 32)) + 0 * tl.arange(0, 512)), mask=((((_lv0 * 512) + tl.arange(0, 512)) < 512) & True), other=0.0) * tl.load(in19_ptr + ((((((tl.program_id(0) // 32) * 512) + ((_lv0 * 512) + tl.arange(0, 512))) * 32) + (tl.program_id(0) % 32)) + 0 * tl.arange(0, 512)), mask=((((_lv0 * 512) + tl.arange(0, 512)) < 512) & True), other=0.0)), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t046_s15(out, ins):
    grid = (65536,)
    t046_s15_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19])
    return out


@triton.jit
def t046_s16_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr):
    _acc0 = tl.zeros([1], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), (tl.load(in19_ptr + (tl.program_id(0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) * (1.0 / tl.maximum(tl.sqrt(tl.load(in20_ptr + (tl.maximum((((tl.program_id(0) // (512 * 32)) * 32) + (tl.program_id(0) % 32)) - tl.maximum((((tl.program_id(0) // (512 * 32)) * 32) + (tl.program_id(0) % 32)) - 65535, 0), 0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)), (1.0 * (1.0 / 1000000000000.0))))), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t046_s16(out, ins):
    grid = (33554432,)
    t046_s16_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20])
    return out


@triton.jit
def t046_s17_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 16):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 16384) & True), (tl.load(in21_ptr + (((tl.program_id(0) * 16384) + ((_lv0 * 1024) + tl.arange(0, 1024))) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 16384) & True), other=0.0) * tl.load(in21_ptr + (((tl.program_id(0) * 16384) + ((_lv0 * 1024) + tl.arange(0, 1024))) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 16384) & True), other=0.0)), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t046_s17(out, ins):
    grid = (2048,)
    t046_s17_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21])
    return out


@triton.jit
def t046_s18_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr):
    _acc0 = tl.zeros([1], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), (tl.load(in21_ptr + (tl.program_id(0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) * (1.0 / tl.maximum(tl.sqrt(tl.load(in22_ptr + (tl.maximum((tl.program_id(0) // 16384) - tl.maximum((tl.program_id(0) // 16384) - 2047, 0), 0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)), (1.0 * (1.0 / 1000000000000.0))))), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t046_s18(out, ins):
    grid = (33554432,)
    t046_s18_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22])
    return out


def t046(out, ins):
    _t0 = torch.empty(9830400, device=ins[0].device, dtype=torch.float32)
    _t1 = torch.empty(12288, device=ins[0].device, dtype=torch.float32)
    _t2 = torch.empty(48, device=ins[0].device, dtype=torch.float32)
    _t3 = torch.empty(12288, device=ins[0].device, dtype=torch.float32)
    _t4 = torch.empty(48, device=ins[0].device, dtype=torch.float32)
    _t5 = torch.empty(9830400, device=ins[0].device, dtype=torch.float32)
    _t6 = torch.empty(204800, device=ins[0].device, dtype=torch.float32)
    _t7 = torch.empty(9830400, device=ins[0].device, dtype=torch.float32)
    _t8 = torch.empty(6553600, device=ins[0].device, dtype=torch.float32)
    _t9 = torch.empty(65536, device=ins[0].device, dtype=torch.float32)
    _t10 = torch.empty(33554432, device=ins[0].device, dtype=torch.float32)
    _t11 = torch.empty(6553600, device=ins[0].device, dtype=torch.float32)
    _t12 = torch.empty(33554432, device=ins[0].device, dtype=torch.float32)
    _t13 = torch.empty(33554432, device=ins[0].device, dtype=torch.float32)
    _t14 = torch.empty(33554432, device=ins[0].device, dtype=torch.float32)
    _t15 = torch.empty(65536, device=ins[0].device, dtype=torch.float32)
    _t16 = torch.empty(33554432, device=ins[0].device, dtype=torch.float32)
    _t17 = torch.empty(2048, device=ins[0].device, dtype=torch.float32)
    t046_s0(_t0, list(ins))
    t046_s1(_t1, list(ins) + [_t0])
    t046_s2(_t2, list(ins) + [_t0, _t1])
    t046_s3(_t3, list(ins) + [_t0, _t1, _t2])
    t046_s4(_t4, list(ins) + [_t0, _t1, _t2, _t3])
    t046_s5(_t5, list(ins) + [_t0, _t1, _t2, _t3, _t4])
    t046_s6(_t6, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5])
    t046_s7(_t7, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6])
    t046_s8(_t8, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7])
    t046_s9(_t9, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8])
    t046_s10(_t10, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9])
    t046_s11(_t11, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10])
    t046_s12(_t12, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11])
    t046_s13(_t13, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12])
    t046_s14(_t14, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13])
    t046_s15(_t15, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13, _t14])
    t046_s16(_t16, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13, _t14, _t15])
    t046_s17(_t17, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13, _t14, _t15, _t16])
    t046_s18(out, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13, _t14, _t15, _t16, _t17])
    return out
