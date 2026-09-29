import torch
import triton
import triton.language as tl


@triton.jit
def _mul_combine(a, b):
    return a * b


@triton.jit
def t011_s0_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 1600) & ((((((((((_lv0 * 1024) + tl.arange(0, 1024)) // 5) % 5) <= (((tl.program_id(0) // 34) % 34) + 1)) & (0 == 0)) & (tl.maximum((((tl.program_id(0) // 34) % 34) + 1) - ((((_lv0 * 1024) + tl.arange(0, 1024)) // 5) % 5), 0) < 32)) & ((((_lv0 * 1024) + tl.arange(0, 1024)) % 5) <= ((tl.program_id(0) % 34) + 1))) & (0 == 0)) & (tl.maximum(((tl.program_id(0) % 34) + 1) - (((_lv0 * 1024) + tl.arange(0, 1024)) % 5), 0) < 32))), (tl.load(in0_ptr + ((((((((tl.program_id(0) // 147968) * 64) + (((((tl.program_id(0) // 1156) % 128) // 128) * 64) + (((_lv0 * 1024) + tl.arange(0, 1024)) // 25))) * 32) + tl.maximum((((tl.program_id(0) // 34) % 34) + 1) - ((((_lv0 * 1024) + tl.arange(0, 1024)) // 5) % 5), 0)) * 32) + tl.maximum(((tl.program_id(0) % 34) + 1) - (((_lv0 * 1024) + tl.arange(0, 1024)) % 5), 0)) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 1600) & ((((((((((_lv0 * 1024) + tl.arange(0, 1024)) // 5) % 5) <= (((tl.program_id(0) // 34) % 34) + 1)) & (0 == 0)) & (tl.maximum((((tl.program_id(0) // 34) % 34) + 1) - ((((_lv0 * 1024) + tl.arange(0, 1024)) // 5) % 5), 0) < 32)) & ((((_lv0 * 1024) + tl.arange(0, 1024)) % 5) <= ((tl.program_id(0) % 34) + 1))) & (0 == 0)) & (tl.maximum(((tl.program_id(0) % 34) + 1) - (((_lv0 * 1024) + tl.arange(0, 1024)) % 5), 0) < 32))), other=0.0) * tl.load(in1_ptr + ((((((((((((tl.program_id(0) // 1156) % 128) // 128) * 64) + (((_lv0 * 1024) + tl.arange(0, 1024)) // 25)) * 128) + (((tl.program_id(0) // 1156) % 128) % 128)) * 5) + ((((_lv0 * 1024) + tl.arange(0, 1024)) // 5) % 5)) * 5) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 5)) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 1600) & ((((((((((_lv0 * 1024) + tl.arange(0, 1024)) // 5) % 5) <= (((tl.program_id(0) // 34) % 34) + 1)) & (0 == 0)) & (tl.maximum((((tl.program_id(0) // 34) % 34) + 1) - ((((_lv0 * 1024) + tl.arange(0, 1024)) // 5) % 5), 0) < 32)) & ((((_lv0 * 1024) + tl.arange(0, 1024)) % 5) <= ((tl.program_id(0) % 34) + 1))) & (0 == 0)) & (tl.maximum(((tl.program_id(0) % 34) + 1) - (((_lv0 * 1024) + tl.arange(0, 1024)) % 5), 0) < 32))), other=0.0)), 0.0))
    _v = (tl.sum(_acc0, axis=0) + tl.load(in2_ptr + (((tl.program_id(0) // 1156) % 128))))
    tl.store(out_ptr + tl.program_id(0), _v)


def t011_s0(out, ins):
    grid = (75759616,)
    t011_s0_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6])
    return out


@triton.jit
def t011_s1_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 578):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 591872) & True), tl.load(in7_ptr + (tl.maximum((((((((_lv0 * 1024) + tl.arange(0, 1024)) // 1156) * 128) + tl.program_id(0)) * 1156) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 1156)) - tl.maximum((((((((_lv0 * 1024) + tl.arange(0, 1024)) // 1156) * 128) + tl.program_id(0)) * 1156) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 1156)) - 75759615, 0), 0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 591872) & True), other=0.0), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t011_s1(out, ins):
    grid = (128,)
    t011_s1_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7])
    return out


@triton.jit
def t011_s2_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 578):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 591872) & True), ((tl.load(in7_ptr + (tl.maximum((((((((_lv0 * 1024) + tl.arange(0, 1024)) // 1156) * 128) + tl.program_id(0)) * 1156) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 1156)) - tl.maximum((((((((_lv0 * 1024) + tl.arange(0, 1024)) // 1156) * 128) + tl.program_id(0)) * 1156) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 1156)) - 75759615, 0), 0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 591872) & True), other=0.0) - (tl.load(in8_ptr + (tl.program_id(0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 591872) & True), other=0.0) * (1.0 * (1.0 / 591872.0)))) * (tl.load(in7_ptr + (tl.maximum((((((((_lv0 * 1024) + tl.arange(0, 1024)) // 1156) * 128) + tl.program_id(0)) * 1156) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 1156)) - tl.maximum((((((((_lv0 * 1024) + tl.arange(0, 1024)) // 1156) * 128) + tl.program_id(0)) * 1156) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 1156)) - 75759615, 0), 0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 591872) & True), other=0.0) - (tl.load(in8_ptr + (tl.program_id(0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 591872) & True), other=0.0) * (1.0 * (1.0 / 591872.0))))), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t011_s2(out, ins):
    grid = (128,)
    t011_s2_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8])
    return out


@triton.jit
def t011_s3_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr):
    _acc0 = tl.zeros([1], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), ((((tl.load(in7_ptr + (tl.program_id(0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) - (tl.load(in8_ptr + (tl.maximum(((tl.program_id(0) // 1156) % 128) - tl.maximum(((tl.program_id(0) // 1156) % 128) - 127, 0), 0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) * (1.0 * (1.0 / 591872.0)))) * (1.0 / tl.sqrt(((tl.load(in9_ptr + (tl.maximum(((tl.program_id(0) // 1156) % 128) - tl.maximum(((tl.program_id(0) // 1156) % 128) - 127, 0), 0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) * (1.0 * (1.0 / 591872.0))) + (1.0 * (1.0 / 100000.0)))))) * tl.load(in3_ptr + (((tl.program_id(0) // 1156) % 128) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)) + tl.load(in4_ptr + (((tl.program_id(0) // 1156) % 128) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)), 0.0))
    _v = (2.0 * tl.sigmoid(2.0 * (tl.sum(_acc0, axis=0))) - 1.0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t011_s3(out, ins):
    grid = (75759616,)
    t011_s3_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9])
    return out


@triton.jit
def t011_s4_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr):
    _acc0 = tl.zeros([4], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = tl.maximum(_acc0, tl.load(in10_ptr + ((((((((tl.program_id(0) // 36992) * 128) + ((tl.program_id(0) // 289) % 128)) * 34) + tl.maximum(((((tl.program_id(0) // 17) % 17) * 2) + tl.maximum(((tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - 3, 0), 0) // 2) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 17) % 17) * 2), 0) - (tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - 3, 0), 0) // 2), 0)) - tl.maximum(((tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - 3, 0), 0) // 2) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 17) % 17) * 2), 0) - (tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - 3, 0), 0) // 2), 0)) - tl.maximum(33 - (((tl.program_id(0) // 17) % 17) * 2), 0), 0), 0)) - tl.maximum(((((tl.program_id(0) // 17) % 17) * 2) + tl.maximum(((tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - 3, 0), 0) // 2) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 17) % 17) * 2), 0) - (tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - 3, 0), 0) // 2), 0)) - tl.maximum(((tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - 3, 0), 0) // 2) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 17) % 17) * 2), 0) - (tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - 3, 0), 0) // 2), 0)) - tl.maximum(33 - (((tl.program_id(0) // 17) % 17) * 2), 0), 0), 0)) - 33, 0), 0)) * 34) + tl.maximum((((tl.program_id(0) % 17) * 2) + tl.maximum(((tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - 3, 0), 0) % 2) + tl.maximum(tl.maximum(0 - ((tl.program_id(0) % 17) * 2), 0) - (tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - 3, 0), 0) % 2), 0)) - tl.maximum(((tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - 3, 0), 0) % 2) + tl.maximum(tl.maximum(0 - ((tl.program_id(0) % 17) * 2), 0) - (tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - 3, 0), 0) % 2), 0)) - tl.maximum(33 - ((tl.program_id(0) % 17) * 2), 0), 0), 0)) - tl.maximum((((tl.program_id(0) % 17) * 2) + tl.maximum(((tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - 3, 0), 0) % 2) + tl.maximum(tl.maximum(0 - ((tl.program_id(0) % 17) * 2), 0) - (tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - 3, 0), 0) % 2), 0)) - tl.maximum(((tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - 3, 0), 0) % 2) + tl.maximum(tl.maximum(0 - ((tl.program_id(0) % 17) * 2), 0) - (tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - 3, 0), 0) % 2), 0)) - tl.maximum(33 - ((tl.program_id(0) % 17) * 2), 0), 0), 0)) - 33, 0), 0)))))
    _v = tl.max(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t011_s4(out, ins):
    grid = (18939904,)
    t011_s4_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10])
    return out


@triton.jit
def t011_s5_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 5):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 4624) & True), tl.load(in11_ptr + (tl.maximum(((((((tl.program_id(0) // 8) * 128) + ((tl.program_id(0) % 8) * 16)) + (((_lv0 * 1024) + tl.arange(0, 1024)) // 289)) * 289) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 289)) - tl.maximum(((((((tl.program_id(0) // 8) * 128) + ((tl.program_id(0) % 8) * 16)) + (((_lv0 * 1024) + tl.arange(0, 1024)) // 289)) * 289) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 289)) - 18939903, 0), 0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 4624) & True), other=0.0), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t011_s5(out, ins):
    grid = (4096,)
    t011_s5_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11])
    return out


@triton.jit
def t011_s6_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 5):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 4624) & True), ((tl.load(in11_ptr + (tl.maximum(((((((tl.program_id(0) // 8) * 128) + ((tl.program_id(0) % 8) * 16)) + (((_lv0 * 1024) + tl.arange(0, 1024)) // 289)) * 289) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 289)) - tl.maximum(((((((tl.program_id(0) // 8) * 128) + ((tl.program_id(0) % 8) * 16)) + (((_lv0 * 1024) + tl.arange(0, 1024)) // 289)) * 289) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 289)) - 18939903, 0), 0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 4624) & True), other=0.0) - (tl.load(in12_ptr + (tl.program_id(0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 4624) & True), other=0.0) * (1.0 * (1.0 / 4624.0)))) * (tl.load(in11_ptr + (tl.maximum(((((((tl.program_id(0) // 8) * 128) + ((tl.program_id(0) % 8) * 16)) + (((_lv0 * 1024) + tl.arange(0, 1024)) // 289)) * 289) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 289)) - tl.maximum(((((((tl.program_id(0) // 8) * 128) + ((tl.program_id(0) % 8) * 16)) + (((_lv0 * 1024) + tl.arange(0, 1024)) // 289)) * 289) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 289)) - 18939903, 0), 0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 4624) & True), other=0.0) - (tl.load(in12_ptr + (tl.program_id(0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 4624) & True), other=0.0) * (1.0 * (1.0 / 4624.0))))), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t011_s6(out, ins):
    grid = (4096,)
    t011_s6_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12])
    return out


@triton.jit
def t011_s7_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr):
    _acc0 = tl.zeros([1], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), ((((tl.load(in11_ptr + (tl.program_id(0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) - (tl.load(in12_ptr + (tl.maximum((((tl.program_id(0) // 36992) * 8) + (((tl.program_id(0) // 289) % 128) // 16)) - tl.maximum((((tl.program_id(0) // 36992) * 8) + (((tl.program_id(0) // 289) % 128) // 16)) - 4095, 0), 0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) * (1.0 * (1.0 / 4624.0)))) * (1.0 / tl.sqrt(((tl.load(in13_ptr + (tl.maximum((((tl.program_id(0) // 36992) * 8) + (((tl.program_id(0) // 289) % 128) // 16)) - tl.maximum((((tl.program_id(0) // 36992) * 8) + (((tl.program_id(0) // 289) % 128) // 16)) - 4095, 0), 0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) * (1.0 * (1.0 / 4624.0))) + (1.0 * (1.0 / 100000.0)))))) * tl.load(in5_ptr + (((tl.program_id(0) // 289) % 128) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)) + tl.load(in6_ptr + (((tl.program_id(0) // 289) % 128) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t011_s7(out, ins):
    grid = (18939904,)
    t011_s7_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13])
    return out


def t011(out, ins):
    _t0 = torch.empty(75759616, device=ins[0].device, dtype=torch.float32)
    _t1 = torch.empty(128, device=ins[0].device, dtype=torch.float32)
    _t2 = torch.empty(128, device=ins[0].device, dtype=torch.float32)
    _t3 = torch.empty(75759616, device=ins[0].device, dtype=torch.float32)
    _t4 = torch.empty(18939904, device=ins[0].device, dtype=torch.float32)
    _t5 = torch.empty(4096, device=ins[0].device, dtype=torch.float32)
    _t6 = torch.empty(4096, device=ins[0].device, dtype=torch.float32)
    t011_s0(_t0, list(ins))
    t011_s1(_t1, list(ins) + [_t0])
    t011_s2(_t2, list(ins) + [_t0, _t1])
    t011_s3(_t3, list(ins) + [_t0, _t1, _t2])
    t011_s4(_t4, list(ins) + [_t0, _t1, _t2, _t3])
    t011_s5(_t5, list(ins) + [_t0, _t1, _t2, _t3, _t4])
    t011_s6(_t6, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5])
    t011_s7(out, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6])
    return out
