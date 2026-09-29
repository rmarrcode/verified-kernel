import torch
import triton
import triton.language as tl


@triton.jit
def _mul_combine(a, b):
    return a * b


@triton.jit
def t025_s0_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr):
    _acc0 = tl.zeros([64], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 64) + tl.arange(0, 64)) < 80) & ((((tl.program_id(0) // 224) % 224) < 224) & ((tl.program_id(0) % 224) < 224))), (tl.load(in0_ptr + ((((((((tl.program_id(0) // 6021120) * 240) + (((((tl.program_id(0) // 50176) % 120) // 40) * 80) + ((_lv0 * 64) + tl.arange(0, 64)))) * 224) + ((tl.program_id(0) // 224) % 224)) * 224) + (tl.program_id(0) % 224)) + 0 * tl.arange(0, 64)), mask=((((_lv0 * 64) + tl.arange(0, 64)) < 80) & ((((tl.program_id(0) // 224) % 224) < 224) & ((tl.program_id(0) % 224) < 224))), other=0.0) * tl.load(in1_ptr + (((((tl.program_id(0) // 50176) % 120) * 80) + ((_lv0 * 64) + tl.arange(0, 64))) + 0 * tl.arange(0, 64)), mask=((((_lv0 * 64) + tl.arange(0, 64)) < 80) & ((((tl.program_id(0) // 224) % 224) < 224) & ((tl.program_id(0) % 224) < 224))), other=0.0)), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t025_s0(out, ins):
    grid = (60211200,)
    t025_s0_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12])
    return out


@triton.jit
def t025_s1_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 1960) & ((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) < 501760)), tl.load(in13_ptr + (tl.maximum(((((((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) // 50176) * 120) + (tl.program_id(0) // 256)) * 50176) + ((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) % 50176)) - tl.maximum(((((((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) // 50176) * 120) + (tl.program_id(0) // 256)) * 50176) + ((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) % 50176)) - 60211199, 0), 0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 1960) & ((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) < 501760)), other=0.0), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t025_s1(out, ins):
    grid = (30720,)
    t025_s1_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13])
    return out


@triton.jit
def t025_s2_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr):
    _acc0 = tl.zeros([256], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 256) + tl.arange(0, 256)) < 256) & True), tl.load(in14_ptr + (((tl.program_id(0) * 256) + ((_lv0 * 256) + tl.arange(0, 256))) + 0 * tl.arange(0, 256)), mask=((((_lv0 * 256) + tl.arange(0, 256)) < 256) & True), other=0.0), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t025_s2(out, ins):
    grid = (120,)
    t025_s2_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14])
    return out


@triton.jit
def t025_s3_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 1960) & ((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) < 501760)), ((tl.load(in13_ptr + (tl.maximum(((((((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) // 50176) * 120) + (tl.program_id(0) // 256)) * 50176) + ((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) % 50176)) - tl.maximum(((((((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) // 50176) * 120) + (tl.program_id(0) // 256)) * 50176) + ((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) % 50176)) - 60211199, 0), 0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 1960) & ((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) < 501760)), other=0.0) - (tl.load(in15_ptr + (tl.maximum((tl.program_id(0) // 256) - tl.maximum((tl.program_id(0) // 256) - 119, 0), 0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 1960) & ((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) < 501760)), other=0.0) * (1.0 * (1.0 / 501760.0)))) * (tl.load(in13_ptr + (tl.maximum(((((((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) // 50176) * 120) + (tl.program_id(0) // 256)) * 50176) + ((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) % 50176)) - tl.maximum(((((((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) // 50176) * 120) + (tl.program_id(0) // 256)) * 50176) + ((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) % 50176)) - 60211199, 0), 0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 1960) & ((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) < 501760)), other=0.0) - (tl.load(in15_ptr + (tl.maximum((tl.program_id(0) // 256) - tl.maximum((tl.program_id(0) // 256) - 119, 0), 0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 1960) & ((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) < 501760)), other=0.0) * (1.0 * (1.0 / 501760.0))))), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t025_s3(out, ins):
    grid = (30720,)
    t025_s3_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15])
    return out


@triton.jit
def t025_s4_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr):
    _acc0 = tl.zeros([256], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 256) + tl.arange(0, 256)) < 256) & True), tl.load(in16_ptr + (((tl.program_id(0) * 256) + ((_lv0 * 256) + tl.arange(0, 256))) + 0 * tl.arange(0, 256)), mask=((((_lv0 * 256) + tl.arange(0, 256)) < 256) & True), other=0.0), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t025_s4(out, ins):
    grid = (120,)
    t025_s4_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16])
    return out


@triton.jit
def t025_s5_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr):
    _acc0 = tl.zeros([1], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), ((((tl.load(in13_ptr + (tl.program_id(0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) - (tl.load(in15_ptr + (tl.maximum(((tl.program_id(0) // 50176) % 120) - tl.maximum(((tl.program_id(0) // 50176) % 120) - 119, 0), 0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) * (1.0 * (1.0 / 501760.0)))) * (1.0 / tl.sqrt(((tl.load(in17_ptr + (tl.maximum(((tl.program_id(0) // 50176) % 120) - tl.maximum(((tl.program_id(0) // 50176) % 120) - 119, 0), 0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) * (1.0 * (1.0 / 501760.0))) + (1.0 * (1.0 / 100000.0)))))) * tl.load(in2_ptr + (((tl.program_id(0) // 50176) % 120) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)) + tl.load(in3_ptr + (((tl.program_id(0) // 50176) % 120) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)), 0.0))
    _v = tl.maximum(tl.sum(_acc0, axis=0), (0.0 * (1.0 / 1.0)))
    tl.store(out_ptr + tl.program_id(0), _v)


def t025_s5(out, ins):
    grid = (60211200,)
    t025_s5_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17])
    return out


@triton.jit
def t025_s6_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr):
    _acc0 = tl.zeros([8], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 8) + tl.arange(0, 8)) < 9) & ((((1 <= (((tl.program_id(0) // 224) % 224) + ((((_lv0 * 8) + tl.arange(0, 8)) // 3) % 3))) & ((((tl.program_id(0) // 224) % 224) + ((((_lv0 * 8) + tl.arange(0, 8)) // 3) % 3)) < 225)) & (1 <= ((tl.program_id(0) % 224) + (((_lv0 * 8) + tl.arange(0, 8)) % 3)))) & (((tl.program_id(0) % 224) + (((_lv0 * 8) + tl.arange(0, 8)) % 3)) < 225))), (tl.load(in18_ptr + (tl.maximum((((((((tl.program_id(0) // 6021120) * 120) + ((tl.program_id(0) // 50176) % 120)) * 224) + tl.maximum((((tl.program_id(0) // 224) % 224) + ((((_lv0 * 8) + tl.arange(0, 8)) // 3) % 3)) - 1, 0)) * 224) + tl.maximum(((tl.program_id(0) % 224) + (((_lv0 * 8) + tl.arange(0, 8)) % 3)) - 1, 0)) - tl.maximum((((((((tl.program_id(0) // 6021120) * 120) + ((tl.program_id(0) // 50176) % 120)) * 224) + tl.maximum((((tl.program_id(0) // 224) % 224) + ((((_lv0 * 8) + tl.arange(0, 8)) // 3) % 3)) - 1, 0)) * 224) + tl.maximum(((tl.program_id(0) % 224) + (((_lv0 * 8) + tl.arange(0, 8)) % 3)) - 1, 0)) - 60211199, 0), 0) + 0 * tl.arange(0, 8)), mask=((((_lv0 * 8) + tl.arange(0, 8)) < 9) & ((((1 <= (((tl.program_id(0) // 224) % 224) + ((((_lv0 * 8) + tl.arange(0, 8)) // 3) % 3))) & ((((tl.program_id(0) // 224) % 224) + ((((_lv0 * 8) + tl.arange(0, 8)) // 3) % 3)) < 225)) & (1 <= ((tl.program_id(0) % 224) + (((_lv0 * 8) + tl.arange(0, 8)) % 3)))) & (((tl.program_id(0) % 224) + (((_lv0 * 8) + tl.arange(0, 8)) % 3)) < 225))), other=0.0) * tl.load(in4_ptr + (((((((tl.program_id(0) // 50176) % 120) * 3) + ((((_lv0 * 8) + tl.arange(0, 8)) // 3) % 3)) * 3) + (((_lv0 * 8) + tl.arange(0, 8)) % 3)) + 0 * tl.arange(0, 8)), mask=((((_lv0 * 8) + tl.arange(0, 8)) < 9) & ((((1 <= (((tl.program_id(0) // 224) % 224) + ((((_lv0 * 8) + tl.arange(0, 8)) // 3) % 3))) & ((((tl.program_id(0) // 224) % 224) + ((((_lv0 * 8) + tl.arange(0, 8)) // 3) % 3)) < 225)) & (1 <= ((tl.program_id(0) % 224) + (((_lv0 * 8) + tl.arange(0, 8)) % 3)))) & (((tl.program_id(0) % 224) + (((_lv0 * 8) + tl.arange(0, 8)) % 3)) < 225))), other=0.0)), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t025_s6(out, ins):
    grid = (60211200,)
    t025_s6_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18])
    return out


@triton.jit
def t025_s7_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 1960) & ((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) < 501760)), tl.load(in19_ptr + (tl.maximum(((((((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) // 50176) * 120) + (tl.program_id(0) // 256)) * 50176) + ((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) % 50176)) - tl.maximum(((((((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) // 50176) * 120) + (tl.program_id(0) // 256)) * 50176) + ((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) % 50176)) - 60211199, 0), 0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 1960) & ((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) < 501760)), other=0.0), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t025_s7(out, ins):
    grid = (30720,)
    t025_s7_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19])
    return out


@triton.jit
def t025_s8_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr):
    _acc0 = tl.zeros([256], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 256) + tl.arange(0, 256)) < 256) & True), tl.load(in20_ptr + (((tl.program_id(0) * 256) + ((_lv0 * 256) + tl.arange(0, 256))) + 0 * tl.arange(0, 256)), mask=((((_lv0 * 256) + tl.arange(0, 256)) < 256) & True), other=0.0), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t025_s8(out, ins):
    grid = (120,)
    t025_s8_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20])
    return out


@triton.jit
def t025_s9_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 1960) & ((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) < 501760)), ((tl.load(in19_ptr + (tl.maximum(((((((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) // 50176) * 120) + (tl.program_id(0) // 256)) * 50176) + ((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) % 50176)) - tl.maximum(((((((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) // 50176) * 120) + (tl.program_id(0) // 256)) * 50176) + ((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) % 50176)) - 60211199, 0), 0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 1960) & ((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) < 501760)), other=0.0) - (tl.load(in21_ptr + (tl.maximum((tl.program_id(0) // 256) - tl.maximum((tl.program_id(0) // 256) - 119, 0), 0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 1960) & ((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) < 501760)), other=0.0) * (1.0 * (1.0 / 501760.0)))) * (tl.load(in19_ptr + (tl.maximum(((((((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) // 50176) * 120) + (tl.program_id(0) // 256)) * 50176) + ((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) % 50176)) - tl.maximum(((((((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) // 50176) * 120) + (tl.program_id(0) // 256)) * 50176) + ((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) % 50176)) - 60211199, 0), 0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 1960) & ((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) < 501760)), other=0.0) - (tl.load(in21_ptr + (tl.maximum((tl.program_id(0) // 256) - tl.maximum((tl.program_id(0) // 256) - 119, 0), 0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 1960) & ((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) < 501760)), other=0.0) * (1.0 * (1.0 / 501760.0))))), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t025_s9(out, ins):
    grid = (30720,)
    t025_s9_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21])
    return out


@triton.jit
def t025_s10_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr):
    _acc0 = tl.zeros([256], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 256) + tl.arange(0, 256)) < 256) & True), tl.load(in22_ptr + (((tl.program_id(0) * 256) + ((_lv0 * 256) + tl.arange(0, 256))) + 0 * tl.arange(0, 256)), mask=((((_lv0 * 256) + tl.arange(0, 256)) < 256) & True), other=0.0), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t025_s10(out, ins):
    grid = (120,)
    t025_s10_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22])
    return out


@triton.jit
def t025_s11_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr):
    _acc0 = tl.zeros([1], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), ((((tl.load(in19_ptr + (tl.program_id(0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) - (tl.load(in21_ptr + (tl.maximum(((tl.program_id(0) // 50176) % 120) - tl.maximum(((tl.program_id(0) // 50176) % 120) - 119, 0), 0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) * (1.0 * (1.0 / 501760.0)))) * (1.0 / tl.sqrt(((tl.load(in23_ptr + (tl.maximum(((tl.program_id(0) // 50176) % 120) - tl.maximum(((tl.program_id(0) // 50176) % 120) - 119, 0), 0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) * (1.0 * (1.0 / 501760.0))) + (1.0 * (1.0 / 100000.0)))))) * tl.load(in5_ptr + (((tl.program_id(0) // 50176) % 120) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)) + tl.load(in6_ptr + (((tl.program_id(0) // 50176) % 120) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t025_s11(out, ins):
    grid = (60211200,)
    t025_s11_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23])
    return out


@triton.jit
def t025_s12_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr):
    _acc0 = tl.zeros([1], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), tl.load(in24_ptr + (tl.maximum((((((((((tl.program_id(0) // 6021120) * 3) + ((tl.program_id(0) // 50176) % 3)) * 40) + ((tl.program_id(0) // 150528) % 40)) * 224) + ((tl.program_id(0) // 224) % 224)) * 224) + (tl.program_id(0) % 224)) - tl.maximum((((((((((tl.program_id(0) // 6021120) * 3) + ((tl.program_id(0) // 50176) % 3)) * 40) + ((tl.program_id(0) // 150528) % 40)) * 224) + ((tl.program_id(0) // 224) % 224)) * 224) + (tl.program_id(0) % 224)) - 60211199, 0), 0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t025_s12(out, ins):
    grid = (60211200,)
    t025_s12_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24])
    return out


@triton.jit
def t025_s13_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr):
    _acc0 = tl.zeros([32], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 32) + tl.arange(0, 32)) < 40) & ((((tl.program_id(0) // 224) % 224) < 224) & ((tl.program_id(0) % 224) < 224))), (tl.load(in25_ptr + (tl.maximum((((((((tl.program_id(0) // 24084480) * 120) + (((((tl.program_id(0) // 50176) % 480) // 160) * 40) + ((_lv0 * 32) + tl.arange(0, 32)))) * 224) + ((tl.program_id(0) // 224) % 224)) * 224) + (tl.program_id(0) % 224)) - tl.maximum((((((((tl.program_id(0) // 24084480) * 120) + (((((tl.program_id(0) // 50176) % 480) // 160) * 40) + ((_lv0 * 32) + tl.arange(0, 32)))) * 224) + ((tl.program_id(0) // 224) % 224)) * 224) + (tl.program_id(0) % 224)) - 60211199, 0), 0) + 0 * tl.arange(0, 32)), mask=((((_lv0 * 32) + tl.arange(0, 32)) < 40) & ((((tl.program_id(0) // 224) % 224) < 224) & ((tl.program_id(0) % 224) < 224))), other=0.0) * tl.load(in7_ptr + (((((tl.program_id(0) // 50176) % 480) * 40) + ((_lv0 * 32) + tl.arange(0, 32))) + 0 * tl.arange(0, 32)), mask=((((_lv0 * 32) + tl.arange(0, 32)) < 40) & ((((tl.program_id(0) // 224) % 224) < 224) & ((tl.program_id(0) % 224) < 224))), other=0.0)), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t025_s13(out, ins):
    grid = (240844800,)
    t025_s13_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25])
    return out


@triton.jit
def t025_s14_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 1960) & ((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) < 501760)), tl.load(in26_ptr + (tl.maximum(((((((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) // 50176) * 480) + (tl.program_id(0) // 256)) * 50176) + ((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) % 50176)) - tl.maximum(((((((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) // 50176) * 480) + (tl.program_id(0) // 256)) * 50176) + ((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) % 50176)) - 240844799, 0), 0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 1960) & ((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) < 501760)), other=0.0), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t025_s14(out, ins):
    grid = (122880,)
    t025_s14_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26])
    return out


@triton.jit
def t025_s15_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr):
    _acc0 = tl.zeros([256], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 256) + tl.arange(0, 256)) < 256) & True), tl.load(in27_ptr + (((tl.program_id(0) * 256) + ((_lv0 * 256) + tl.arange(0, 256))) + 0 * tl.arange(0, 256)), mask=((((_lv0 * 256) + tl.arange(0, 256)) < 256) & True), other=0.0), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t025_s15(out, ins):
    grid = (480,)
    t025_s15_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27])
    return out


@triton.jit
def t025_s16_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 1960) & ((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) < 501760)), ((tl.load(in26_ptr + (tl.maximum(((((((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) // 50176) * 480) + (tl.program_id(0) // 256)) * 50176) + ((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) % 50176)) - tl.maximum(((((((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) // 50176) * 480) + (tl.program_id(0) // 256)) * 50176) + ((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) % 50176)) - 240844799, 0), 0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 1960) & ((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) < 501760)), other=0.0) - (tl.load(in28_ptr + (tl.maximum((tl.program_id(0) // 256) - tl.maximum((tl.program_id(0) // 256) - 479, 0), 0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 1960) & ((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) < 501760)), other=0.0) * (1.0 * (1.0 / 501760.0)))) * (tl.load(in26_ptr + (tl.maximum(((((((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) // 50176) * 480) + (tl.program_id(0) // 256)) * 50176) + ((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) % 50176)) - tl.maximum(((((((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) // 50176) * 480) + (tl.program_id(0) // 256)) * 50176) + ((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) % 50176)) - 240844799, 0), 0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 1960) & ((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) < 501760)), other=0.0) - (tl.load(in28_ptr + (tl.maximum((tl.program_id(0) // 256) - tl.maximum((tl.program_id(0) // 256) - 479, 0), 0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 1960) & ((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) < 501760)), other=0.0) * (1.0 * (1.0 / 501760.0))))), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t025_s16(out, ins):
    grid = (122880,)
    t025_s16_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28])
    return out


@triton.jit
def t025_s17_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr):
    _acc0 = tl.zeros([256], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 256) + tl.arange(0, 256)) < 256) & True), tl.load(in29_ptr + (((tl.program_id(0) * 256) + ((_lv0 * 256) + tl.arange(0, 256))) + 0 * tl.arange(0, 256)), mask=((((_lv0 * 256) + tl.arange(0, 256)) < 256) & True), other=0.0), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t025_s17(out, ins):
    grid = (480,)
    t025_s17_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29])
    return out


@triton.jit
def t025_s18_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr):
    _acc0 = tl.zeros([1], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), ((((tl.load(in26_ptr + (tl.program_id(0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) - (tl.load(in28_ptr + (tl.maximum(((tl.program_id(0) // 50176) % 480) - tl.maximum(((tl.program_id(0) // 50176) % 480) - 479, 0), 0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) * (1.0 * (1.0 / 501760.0)))) * (1.0 / tl.sqrt(((tl.load(in30_ptr + (tl.maximum(((tl.program_id(0) // 50176) % 480) - tl.maximum(((tl.program_id(0) // 50176) % 480) - 479, 0), 0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) * (1.0 * (1.0 / 501760.0))) + (1.0 * (1.0 / 100000.0)))))) * tl.load(in8_ptr + (((tl.program_id(0) // 50176) % 480) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)) + tl.load(in9_ptr + (((tl.program_id(0) // 50176) % 480) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)), 0.0))
    _v = tl.maximum(tl.sum(_acc0, axis=0), (0.0 * (1.0 / 1.0)))
    tl.store(out_ptr + tl.program_id(0), _v)


def t025_s18(out, ins):
    grid = (240844800,)
    t025_s18_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30])
    return out


@triton.jit
def t025_s19_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr):
    _acc0 = tl.zeros([128], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 128) + tl.arange(0, 128)) < 240) & ((((tl.program_id(0) // 224) % 224) < 224) & ((tl.program_id(0) % 224) < 224))), (tl.load(in0_ptr + ((((((((tl.program_id(0) // 24084480) * 240) + ((_lv0 * 128) + tl.arange(0, 128))) * 224) + ((tl.program_id(0) // 224) % 224)) * 224) + (tl.program_id(0) % 224)) + 0 * tl.arange(0, 128)), mask=((((_lv0 * 128) + tl.arange(0, 128)) < 240) & ((((tl.program_id(0) // 224) % 224) < 224) & ((tl.program_id(0) % 224) < 224))), other=0.0) * tl.load(in10_ptr + (((((tl.program_id(0) // 50176) % 480) * 240) + ((_lv0 * 128) + tl.arange(0, 128))) + 0 * tl.arange(0, 128)), mask=((((_lv0 * 128) + tl.arange(0, 128)) < 240) & ((((tl.program_id(0) // 224) % 224) < 224) & ((tl.program_id(0) % 224) < 224))), other=0.0)), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t025_s19(out, ins):
    grid = (240844800,)
    t025_s19_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31])
    return out


@triton.jit
def t025_s20_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 1960) & ((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) < 501760)), tl.load(in32_ptr + (tl.maximum(((((((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) // 50176) * 480) + (tl.program_id(0) // 256)) * 50176) + ((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) % 50176)) - tl.maximum(((((((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) // 50176) * 480) + (tl.program_id(0) // 256)) * 50176) + ((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) % 50176)) - 240844799, 0), 0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 1960) & ((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) < 501760)), other=0.0), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t025_s20(out, ins):
    grid = (122880,)
    t025_s20_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32])
    return out


@triton.jit
def t025_s21_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr):
    _acc0 = tl.zeros([256], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 256) + tl.arange(0, 256)) < 256) & True), tl.load(in33_ptr + (((tl.program_id(0) * 256) + ((_lv0 * 256) + tl.arange(0, 256))) + 0 * tl.arange(0, 256)), mask=((((_lv0 * 256) + tl.arange(0, 256)) < 256) & True), other=0.0), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t025_s21(out, ins):
    grid = (480,)
    t025_s21_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33])
    return out


@triton.jit
def t025_s22_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 1960) & ((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) < 501760)), ((tl.load(in32_ptr + (tl.maximum(((((((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) // 50176) * 480) + (tl.program_id(0) // 256)) * 50176) + ((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) % 50176)) - tl.maximum(((((((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) // 50176) * 480) + (tl.program_id(0) // 256)) * 50176) + ((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) % 50176)) - 240844799, 0), 0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 1960) & ((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) < 501760)), other=0.0) - (tl.load(in34_ptr + (tl.maximum((tl.program_id(0) // 256) - tl.maximum((tl.program_id(0) // 256) - 479, 0), 0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 1960) & ((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) < 501760)), other=0.0) * (1.0 * (1.0 / 501760.0)))) * (tl.load(in32_ptr + (tl.maximum(((((((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) // 50176) * 480) + (tl.program_id(0) // 256)) * 50176) + ((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) % 50176)) - tl.maximum(((((((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) // 50176) * 480) + (tl.program_id(0) // 256)) * 50176) + ((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) % 50176)) - 240844799, 0), 0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 1960) & ((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) < 501760)), other=0.0) - (tl.load(in34_ptr + (tl.maximum((tl.program_id(0) // 256) - tl.maximum((tl.program_id(0) // 256) - 479, 0), 0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 1960) & ((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) < 501760)), other=0.0) * (1.0 * (1.0 / 501760.0))))), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t025_s22(out, ins):
    grid = (122880,)
    t025_s22_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34])
    return out


@triton.jit
def t025_s23_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr):
    _acc0 = tl.zeros([256], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 256) + tl.arange(0, 256)) < 256) & True), tl.load(in35_ptr + (((tl.program_id(0) * 256) + ((_lv0 * 256) + tl.arange(0, 256))) + 0 * tl.arange(0, 256)), mask=((((_lv0 * 256) + tl.arange(0, 256)) < 256) & True), other=0.0), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t025_s23(out, ins):
    grid = (480,)
    t025_s23_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35])
    return out


@triton.jit
def t025_s24_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr):
    _acc0 = tl.zeros([1], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), ((((tl.load(in32_ptr + (tl.program_id(0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) - (tl.load(in34_ptr + (tl.maximum(((tl.program_id(0) // 50176) % 480) - tl.maximum(((tl.program_id(0) // 50176) % 480) - 479, 0), 0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) * (1.0 * (1.0 / 501760.0)))) * (1.0 / tl.sqrt(((tl.load(in36_ptr + (tl.maximum(((tl.program_id(0) // 50176) % 480) - tl.maximum(((tl.program_id(0) // 50176) % 480) - 479, 0), 0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) * (1.0 * (1.0 / 501760.0))) + (1.0 * (1.0 / 100000.0)))))) * tl.load(in11_ptr + (((tl.program_id(0) // 50176) % 480) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)) + tl.load(in12_ptr + (((tl.program_id(0) // 50176) % 480) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t025_s24(out, ins):
    grid = (240844800,)
    t025_s24_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36])
    return out


@triton.jit
def t025_s25_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr):
    _acc0 = tl.zeros([1], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), (tl.load(in31_ptr + ((((((((tl.program_id(0) // 24084480) * 480) + ((tl.program_id(0) // 50176) % 480)) * 224) + ((tl.program_id(0) // 224) % 224)) * 224) + (tl.program_id(0) % 224)) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) + tl.load(in37_ptr + ((((((((tl.program_id(0) // 24084480) * 480) + ((tl.program_id(0) // 50176) % 480)) * 224) + ((tl.program_id(0) // 224) % 224)) * 224) + (tl.program_id(0) % 224)) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t025_s25(out, ins):
    grid = (240844800,)
    t025_s25_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37])
    return out


def t025(out, ins):
    _t0 = torch.empty(60211200, device=ins[0].device, dtype=torch.float32)
    _t1 = torch.empty(30720, device=ins[0].device, dtype=torch.float32)
    _t2 = torch.empty(120, device=ins[0].device, dtype=torch.float32)
    _t3 = torch.empty(30720, device=ins[0].device, dtype=torch.float32)
    _t4 = torch.empty(120, device=ins[0].device, dtype=torch.float32)
    _t5 = torch.empty(60211200, device=ins[0].device, dtype=torch.float32)
    _t6 = torch.empty(60211200, device=ins[0].device, dtype=torch.float32)
    _t7 = torch.empty(30720, device=ins[0].device, dtype=torch.float32)
    _t8 = torch.empty(120, device=ins[0].device, dtype=torch.float32)
    _t9 = torch.empty(30720, device=ins[0].device, dtype=torch.float32)
    _t10 = torch.empty(120, device=ins[0].device, dtype=torch.float32)
    _t11 = torch.empty(60211200, device=ins[0].device, dtype=torch.float32)
    _t12 = torch.empty(60211200, device=ins[0].device, dtype=torch.float32)
    _t13 = torch.empty(240844800, device=ins[0].device, dtype=torch.float32)
    _t14 = torch.empty(122880, device=ins[0].device, dtype=torch.float32)
    _t15 = torch.empty(480, device=ins[0].device, dtype=torch.float32)
    _t16 = torch.empty(122880, device=ins[0].device, dtype=torch.float32)
    _t17 = torch.empty(480, device=ins[0].device, dtype=torch.float32)
    _t18 = torch.empty(240844800, device=ins[0].device, dtype=torch.float32)
    _t19 = torch.empty(240844800, device=ins[0].device, dtype=torch.float32)
    _t20 = torch.empty(122880, device=ins[0].device, dtype=torch.float32)
    _t21 = torch.empty(480, device=ins[0].device, dtype=torch.float32)
    _t22 = torch.empty(122880, device=ins[0].device, dtype=torch.float32)
    _t23 = torch.empty(480, device=ins[0].device, dtype=torch.float32)
    _t24 = torch.empty(240844800, device=ins[0].device, dtype=torch.float32)
    t025_s0(_t0, list(ins))
    t025_s1(_t1, list(ins) + [_t0])
    t025_s2(_t2, list(ins) + [_t0, _t1])
    t025_s3(_t3, list(ins) + [_t0, _t1, _t2])
    t025_s4(_t4, list(ins) + [_t0, _t1, _t2, _t3])
    t025_s5(_t5, list(ins) + [_t0, _t1, _t2, _t3, _t4])
    t025_s6(_t6, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5])
    t025_s7(_t7, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6])
    t025_s8(_t8, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7])
    t025_s9(_t9, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8])
    t025_s10(_t10, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9])
    t025_s11(_t11, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10])
    t025_s12(_t12, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11])
    t025_s13(_t13, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12])
    t025_s14(_t14, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13])
    t025_s15(_t15, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13, _t14])
    t025_s16(_t16, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13, _t14, _t15])
    t025_s17(_t17, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13, _t14, _t15, _t16])
    t025_s18(_t18, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13, _t14, _t15, _t16, _t17])
    t025_s19(_t19, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13, _t14, _t15, _t16, _t17, _t18])
    t025_s20(_t20, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13, _t14, _t15, _t16, _t17, _t18, _t19])
    t025_s21(_t21, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13, _t14, _t15, _t16, _t17, _t18, _t19, _t20])
    t025_s22(_t22, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13, _t14, _t15, _t16, _t17, _t18, _t19, _t20, _t21])
    t025_s23(_t23, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13, _t14, _t15, _t16, _t17, _t18, _t19, _t20, _t21, _t22])
    t025_s24(_t24, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13, _t14, _t15, _t16, _t17, _t18, _t19, _t20, _t21, _t22, _t23])
    t025_s25(out, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13, _t14, _t15, _t16, _t17, _t18, _t19, _t20, _t21, _t22, _t23, _t24])
    return out
