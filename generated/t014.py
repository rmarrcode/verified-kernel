import torch
import triton
import triton.language as tl


@triton.jit
def _mul_combine(a, b):
    return a * b


@triton.jit
def t014_s0_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 1960) & ((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) < 501760)), tl.load(in0_ptr + (((((((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) // 50176) * 32) + (tl.program_id(0) // 256)) * 50176) + ((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) % 50176)) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 1960) & ((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) < 501760)), other=0.0), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t014_s0(out, ins):
    grid = (8192,)
    t014_s0_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18])
    return out


@triton.jit
def t014_s1_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr):
    _acc0 = tl.zeros([256], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 256) + tl.arange(0, 256)) < 256) & True), tl.load(in19_ptr + (((tl.program_id(0) * 256) + ((_lv0 * 256) + tl.arange(0, 256))) + 0 * tl.arange(0, 256)), mask=((((_lv0 * 256) + tl.arange(0, 256)) < 256) & True), other=0.0), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t014_s1(out, ins):
    grid = (32,)
    t014_s1_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19])
    return out


@triton.jit
def t014_s2_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 1960) & ((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) < 501760)), ((tl.load(in0_ptr + (((((((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) // 50176) * 32) + (tl.program_id(0) // 256)) * 50176) + ((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) % 50176)) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 1960) & ((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) < 501760)), other=0.0) - (tl.load(in20_ptr + (tl.maximum((tl.program_id(0) // 256) - tl.maximum((tl.program_id(0) // 256) - 31, 0), 0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 1960) & ((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) < 501760)), other=0.0) * (1.0 * (1.0 / 501760.0)))) * (tl.load(in0_ptr + (((((((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) // 50176) * 32) + (tl.program_id(0) // 256)) * 50176) + ((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) % 50176)) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 1960) & ((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) < 501760)), other=0.0) - (tl.load(in20_ptr + (tl.maximum((tl.program_id(0) // 256) - tl.maximum((tl.program_id(0) // 256) - 31, 0), 0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 1960) & ((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) < 501760)), other=0.0) * (1.0 * (1.0 / 501760.0))))), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t014_s2(out, ins):
    grid = (8192,)
    t014_s2_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20])
    return out


@triton.jit
def t014_s3_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr):
    _acc0 = tl.zeros([256], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 256) + tl.arange(0, 256)) < 256) & True), tl.load(in21_ptr + (((tl.program_id(0) * 256) + ((_lv0 * 256) + tl.arange(0, 256))) + 0 * tl.arange(0, 256)), mask=((((_lv0 * 256) + tl.arange(0, 256)) < 256) & True), other=0.0), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t014_s3(out, ins):
    grid = (32,)
    t014_s3_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21])
    return out


@triton.jit
def t014_s4_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr):
    _acc0 = tl.zeros([1], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), ((((tl.load(in0_ptr + (tl.program_id(0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) - (tl.load(in20_ptr + (tl.maximum(((tl.program_id(0) // 50176) % 32) - tl.maximum(((tl.program_id(0) // 50176) % 32) - 31, 0), 0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) * (1.0 * (1.0 / 501760.0)))) * (1.0 / tl.sqrt(((tl.load(in22_ptr + (tl.maximum(((tl.program_id(0) // 50176) % 32) - tl.maximum(((tl.program_id(0) // 50176) % 32) - 31, 0), 0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) * (1.0 * (1.0 / 501760.0))) + (1.0 * (1.0 / 100000.0)))))) * tl.load(in1_ptr + (((tl.program_id(0) // 50176) % 32) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)) + tl.load(in2_ptr + (((tl.program_id(0) // 50176) % 32) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)), 0.0))
    _v = tl.maximum(tl.sum(_acc0, axis=0), (0.0 * (1.0 / 1.0)))
    tl.store(out_ptr + tl.program_id(0), _v)


def t014_s4(out, ins):
    grid = (16056320,)
    t014_s4_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22])
    return out


@triton.jit
def t014_s5_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr):
    _acc0 = tl.zeros([256], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 256) + tl.arange(0, 256)) < 288) & ((((1 <= (((tl.program_id(0) // 224) % 224) + ((((_lv0 * 256) + tl.arange(0, 256)) // 3) % 3))) & ((((tl.program_id(0) // 224) % 224) + ((((_lv0 * 256) + tl.arange(0, 256)) // 3) % 3)) < 225)) & (1 <= ((tl.program_id(0) % 224) + (((_lv0 * 256) + tl.arange(0, 256)) % 3)))) & (((tl.program_id(0) % 224) + (((_lv0 * 256) + tl.arange(0, 256)) % 3)) < 225))), (tl.load(in23_ptr + (tl.maximum((((((((tl.program_id(0) // 1605632) * 32) + (((_lv0 * 256) + tl.arange(0, 256)) // 9)) * 224) + tl.maximum((((tl.program_id(0) // 224) % 224) + ((((_lv0 * 256) + tl.arange(0, 256)) // 3) % 3)) - 1, 0)) * 224) + tl.maximum(((tl.program_id(0) % 224) + (((_lv0 * 256) + tl.arange(0, 256)) % 3)) - 1, 0)) - tl.maximum((((((((tl.program_id(0) // 1605632) * 32) + (((_lv0 * 256) + tl.arange(0, 256)) // 9)) * 224) + tl.maximum((((tl.program_id(0) // 224) % 224) + ((((_lv0 * 256) + tl.arange(0, 256)) // 3) % 3)) - 1, 0)) * 224) + tl.maximum(((tl.program_id(0) % 224) + (((_lv0 * 256) + tl.arange(0, 256)) % 3)) - 1, 0)) - 16056319, 0), 0) + 0 * tl.arange(0, 256)), mask=((((_lv0 * 256) + tl.arange(0, 256)) < 288) & ((((1 <= (((tl.program_id(0) // 224) % 224) + ((((_lv0 * 256) + tl.arange(0, 256)) // 3) % 3))) & ((((tl.program_id(0) // 224) % 224) + ((((_lv0 * 256) + tl.arange(0, 256)) // 3) % 3)) < 225)) & (1 <= ((tl.program_id(0) % 224) + (((_lv0 * 256) + tl.arange(0, 256)) % 3)))) & (((tl.program_id(0) % 224) + (((_lv0 * 256) + tl.arange(0, 256)) % 3)) < 225))), other=0.0) * tl.load(in3_ptr + (((((((((tl.program_id(0) // 50176) % 32) * 32) + (((_lv0 * 256) + tl.arange(0, 256)) // 9)) * 3) + ((((_lv0 * 256) + tl.arange(0, 256)) // 3) % 3)) * 3) + (((_lv0 * 256) + tl.arange(0, 256)) % 3)) + 0 * tl.arange(0, 256)), mask=((((_lv0 * 256) + tl.arange(0, 256)) < 288) & ((((1 <= (((tl.program_id(0) // 224) % 224) + ((((_lv0 * 256) + tl.arange(0, 256)) // 3) % 3))) & ((((tl.program_id(0) // 224) % 224) + ((((_lv0 * 256) + tl.arange(0, 256)) // 3) % 3)) < 225)) & (1 <= ((tl.program_id(0) % 224) + (((_lv0 * 256) + tl.arange(0, 256)) % 3)))) & (((tl.program_id(0) % 224) + (((_lv0 * 256) + tl.arange(0, 256)) % 3)) < 225))), other=0.0)), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t014_s5(out, ins):
    grid = (16056320,)
    t014_s5_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23])
    return out


@triton.jit
def t014_s6_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr):
    _acc0 = tl.zeros([2], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 2) + tl.arange(0, 2)) < 2) & ((((((_lv0 * 2) + tl.arange(0, 2)) == 0) & (0 <= ((tl.program_id(0) // 50176) % 64))) & (((tl.program_id(0) // 50176) % 64) < 32)) | (((((_lv0 * 2) + tl.arange(0, 2)) == 1) & (32 <= ((tl.program_id(0) // 50176) % 64))) & (((tl.program_id(0) // 50176) % 64) < 64)))), tl.where((((_lv0 * 2) + tl.arange(0, 2))).to(tl.float32) <= (1.0 * (1.0 / 2.0)), tl.load(in0_ptr + ((((((((tl.program_id(0) // 3211264) * 32) + ((tl.program_id(0) // 50176) % 64)) * 224) + ((tl.program_id(0) // 224) % 224)) * 224) + (tl.program_id(0) % 224)) + 0 * tl.arange(0, 2)), mask=((((_lv0 * 2) + tl.arange(0, 2)) < 2) & ((((((_lv0 * 2) + tl.arange(0, 2)) == 0) & (0 <= ((tl.program_id(0) // 50176) % 64))) & (((tl.program_id(0) // 50176) % 64) < 32)) | (((((_lv0 * 2) + tl.arange(0, 2)) == 1) & (32 <= ((tl.program_id(0) // 50176) % 64))) & (((tl.program_id(0) // 50176) % 64) < 64)))), other=0.0), tl.load(in24_ptr + (tl.maximum((((((((tl.program_id(0) // 3211264) * 32) + tl.maximum(((tl.program_id(0) // 50176) % 64) - 32, 0)) * 224) + ((tl.program_id(0) // 224) % 224)) * 224) + (tl.program_id(0) % 224)) - tl.maximum((((((((tl.program_id(0) // 3211264) * 32) + tl.maximum(((tl.program_id(0) // 50176) % 64) - 32, 0)) * 224) + ((tl.program_id(0) // 224) % 224)) * 224) + (tl.program_id(0) % 224)) - 16056319, 0), 0) + 0 * tl.arange(0, 2)), mask=((((_lv0 * 2) + tl.arange(0, 2)) < 2) & ((((((_lv0 * 2) + tl.arange(0, 2)) == 0) & (0 <= ((tl.program_id(0) // 50176) % 64))) & (((tl.program_id(0) // 50176) % 64) < 32)) | (((((_lv0 * 2) + tl.arange(0, 2)) == 1) & (32 <= ((tl.program_id(0) // 50176) % 64))) & (((tl.program_id(0) // 50176) % 64) < 64)))), other=0.0)), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t014_s6(out, ins):
    grid = (32112640,)
    t014_s6_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24])
    return out


@triton.jit
def t014_s7_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 1960) & ((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) < 501760)), tl.load(in25_ptr + (tl.maximum(((((((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) // 50176) * 64) + (tl.program_id(0) // 256)) * 50176) + ((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) % 50176)) - tl.maximum(((((((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) // 50176) * 64) + (tl.program_id(0) // 256)) * 50176) + ((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) % 50176)) - 32112639, 0), 0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 1960) & ((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) < 501760)), other=0.0), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t014_s7(out, ins):
    grid = (16384,)
    t014_s7_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25])
    return out


@triton.jit
def t014_s8_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr):
    _acc0 = tl.zeros([256], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 256) + tl.arange(0, 256)) < 256) & True), tl.load(in26_ptr + (((tl.program_id(0) * 256) + ((_lv0 * 256) + tl.arange(0, 256))) + 0 * tl.arange(0, 256)), mask=((((_lv0 * 256) + tl.arange(0, 256)) < 256) & True), other=0.0), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t014_s8(out, ins):
    grid = (64,)
    t014_s8_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26])
    return out


@triton.jit
def t014_s9_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 1960) & ((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) < 501760)), ((tl.load(in25_ptr + (tl.maximum(((((((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) // 50176) * 64) + (tl.program_id(0) // 256)) * 50176) + ((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) % 50176)) - tl.maximum(((((((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) // 50176) * 64) + (tl.program_id(0) // 256)) * 50176) + ((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) % 50176)) - 32112639, 0), 0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 1960) & ((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) < 501760)), other=0.0) - (tl.load(in27_ptr + (tl.maximum((tl.program_id(0) // 256) - tl.maximum((tl.program_id(0) // 256) - 63, 0), 0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 1960) & ((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) < 501760)), other=0.0) * (1.0 * (1.0 / 501760.0)))) * (tl.load(in25_ptr + (tl.maximum(((((((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) // 50176) * 64) + (tl.program_id(0) // 256)) * 50176) + ((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) % 50176)) - tl.maximum(((((((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) // 50176) * 64) + (tl.program_id(0) // 256)) * 50176) + ((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) % 50176)) - 32112639, 0), 0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 1960) & ((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) < 501760)), other=0.0) - (tl.load(in27_ptr + (tl.maximum((tl.program_id(0) // 256) - tl.maximum((tl.program_id(0) // 256) - 63, 0), 0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 1960) & ((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) < 501760)), other=0.0) * (1.0 * (1.0 / 501760.0))))), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t014_s9(out, ins):
    grid = (16384,)
    t014_s9_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27])
    return out


@triton.jit
def t014_s10_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr):
    _acc0 = tl.zeros([256], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 256) + tl.arange(0, 256)) < 256) & True), tl.load(in28_ptr + (((tl.program_id(0) * 256) + ((_lv0 * 256) + tl.arange(0, 256))) + 0 * tl.arange(0, 256)), mask=((((_lv0 * 256) + tl.arange(0, 256)) < 256) & True), other=0.0), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t014_s10(out, ins):
    grid = (64,)
    t014_s10_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28])
    return out


@triton.jit
def t014_s11_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr):
    _acc0 = tl.zeros([1], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), ((((tl.load(in25_ptr + (tl.program_id(0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) - (tl.load(in27_ptr + (tl.maximum(((tl.program_id(0) // 50176) % 64) - tl.maximum(((tl.program_id(0) // 50176) % 64) - 63, 0), 0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) * (1.0 * (1.0 / 501760.0)))) * (1.0 / tl.sqrt(((tl.load(in29_ptr + (tl.maximum(((tl.program_id(0) // 50176) % 64) - tl.maximum(((tl.program_id(0) // 50176) % 64) - 63, 0), 0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) * (1.0 * (1.0 / 501760.0))) + (1.0 * (1.0 / 100000.0)))))) * tl.load(in4_ptr + (((tl.program_id(0) // 50176) % 64) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)) + tl.load(in5_ptr + (((tl.program_id(0) // 50176) % 64) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)), 0.0))
    _v = tl.maximum(tl.sum(_acc0, axis=0), (0.0 * (1.0 / 1.0)))
    tl.store(out_ptr + tl.program_id(0), _v)


def t014_s11(out, ins):
    grid = (32112640,)
    t014_s11_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29])
    return out


@triton.jit
def t014_s12_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr):
    _acc0 = tl.zeros([512], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 512) + tl.arange(0, 512)) < 576) & ((((1 <= (((tl.program_id(0) // 224) % 224) + ((((_lv0 * 512) + tl.arange(0, 512)) // 3) % 3))) & ((((tl.program_id(0) // 224) % 224) + ((((_lv0 * 512) + tl.arange(0, 512)) // 3) % 3)) < 225)) & (1 <= ((tl.program_id(0) % 224) + (((_lv0 * 512) + tl.arange(0, 512)) % 3)))) & (((tl.program_id(0) % 224) + (((_lv0 * 512) + tl.arange(0, 512)) % 3)) < 225))), (tl.load(in30_ptr + (tl.maximum((((((((tl.program_id(0) // 1605632) * 64) + (((_lv0 * 512) + tl.arange(0, 512)) // 9)) * 224) + tl.maximum((((tl.program_id(0) // 224) % 224) + ((((_lv0 * 512) + tl.arange(0, 512)) // 3) % 3)) - 1, 0)) * 224) + tl.maximum(((tl.program_id(0) % 224) + (((_lv0 * 512) + tl.arange(0, 512)) % 3)) - 1, 0)) - tl.maximum((((((((tl.program_id(0) // 1605632) * 64) + (((_lv0 * 512) + tl.arange(0, 512)) // 9)) * 224) + tl.maximum((((tl.program_id(0) // 224) % 224) + ((((_lv0 * 512) + tl.arange(0, 512)) // 3) % 3)) - 1, 0)) * 224) + tl.maximum(((tl.program_id(0) % 224) + (((_lv0 * 512) + tl.arange(0, 512)) % 3)) - 1, 0)) - 32112639, 0), 0) + 0 * tl.arange(0, 512)), mask=((((_lv0 * 512) + tl.arange(0, 512)) < 576) & ((((1 <= (((tl.program_id(0) // 224) % 224) + ((((_lv0 * 512) + tl.arange(0, 512)) // 3) % 3))) & ((((tl.program_id(0) // 224) % 224) + ((((_lv0 * 512) + tl.arange(0, 512)) // 3) % 3)) < 225)) & (1 <= ((tl.program_id(0) % 224) + (((_lv0 * 512) + tl.arange(0, 512)) % 3)))) & (((tl.program_id(0) % 224) + (((_lv0 * 512) + tl.arange(0, 512)) % 3)) < 225))), other=0.0) * tl.load(in6_ptr + (((((((((tl.program_id(0) // 50176) % 32) * 64) + (((_lv0 * 512) + tl.arange(0, 512)) // 9)) * 3) + ((((_lv0 * 512) + tl.arange(0, 512)) // 3) % 3)) * 3) + (((_lv0 * 512) + tl.arange(0, 512)) % 3)) + 0 * tl.arange(0, 512)), mask=((((_lv0 * 512) + tl.arange(0, 512)) < 576) & ((((1 <= (((tl.program_id(0) // 224) % 224) + ((((_lv0 * 512) + tl.arange(0, 512)) // 3) % 3))) & ((((tl.program_id(0) // 224) % 224) + ((((_lv0 * 512) + tl.arange(0, 512)) // 3) % 3)) < 225)) & (1 <= ((tl.program_id(0) % 224) + (((_lv0 * 512) + tl.arange(0, 512)) % 3)))) & (((tl.program_id(0) % 224) + (((_lv0 * 512) + tl.arange(0, 512)) % 3)) < 225))), other=0.0)), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t014_s12(out, ins):
    grid = (16056320,)
    t014_s12_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30])
    return out


@triton.jit
def t014_s13_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr):
    _acc0 = tl.zeros([2], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 2) + tl.arange(0, 2)) < 3) & (((((((_lv0 * 2) + tl.arange(0, 2)) == 0) & (0 <= ((tl.program_id(0) // 50176) % 96))) & (((tl.program_id(0) // 50176) % 96) < 32)) | (((((_lv0 * 2) + tl.arange(0, 2)) == 1) & (32 <= ((tl.program_id(0) // 50176) % 96))) & (((tl.program_id(0) // 50176) % 96) < 64))) | (((((_lv0 * 2) + tl.arange(0, 2)) == 2) & (64 <= ((tl.program_id(0) // 50176) % 96))) & (((tl.program_id(0) // 50176) % 96) < 96)))), tl.where((((_lv0 * 2) + tl.arange(0, 2))).to(tl.float32) <= (1.0 * (1.0 / 2.0)), tl.load(in0_ptr + ((((((((tl.program_id(0) // 4816896) * 32) + ((tl.program_id(0) // 50176) % 96)) * 224) + ((tl.program_id(0) // 224) % 224)) * 224) + (tl.program_id(0) % 224)) + 0 * tl.arange(0, 2)), mask=((((_lv0 * 2) + tl.arange(0, 2)) < 3) & (((((((_lv0 * 2) + tl.arange(0, 2)) == 0) & (0 <= ((tl.program_id(0) // 50176) % 96))) & (((tl.program_id(0) // 50176) % 96) < 32)) | (((((_lv0 * 2) + tl.arange(0, 2)) == 1) & (32 <= ((tl.program_id(0) // 50176) % 96))) & (((tl.program_id(0) // 50176) % 96) < 64))) | (((((_lv0 * 2) + tl.arange(0, 2)) == 2) & (64 <= ((tl.program_id(0) // 50176) % 96))) & (((tl.program_id(0) // 50176) % 96) < 96)))), other=0.0), tl.where((((_lv0 * 2) + tl.arange(0, 2))).to(tl.float32) <= (3.0 * (1.0 / 2.0)), tl.load(in24_ptr + (tl.maximum((((((((tl.program_id(0) // 4816896) * 32) + tl.maximum(((tl.program_id(0) // 50176) % 96) - 32, 0)) * 224) + ((tl.program_id(0) // 224) % 224)) * 224) + (tl.program_id(0) % 224)) - tl.maximum((((((((tl.program_id(0) // 4816896) * 32) + tl.maximum(((tl.program_id(0) // 50176) % 96) - 32, 0)) * 224) + ((tl.program_id(0) // 224) % 224)) * 224) + (tl.program_id(0) % 224)) - 16056319, 0), 0) + 0 * tl.arange(0, 2)), mask=((((_lv0 * 2) + tl.arange(0, 2)) < 3) & (((((((_lv0 * 2) + tl.arange(0, 2)) == 0) & (0 <= ((tl.program_id(0) // 50176) % 96))) & (((tl.program_id(0) // 50176) % 96) < 32)) | (((((_lv0 * 2) + tl.arange(0, 2)) == 1) & (32 <= ((tl.program_id(0) // 50176) % 96))) & (((tl.program_id(0) // 50176) % 96) < 64))) | (((((_lv0 * 2) + tl.arange(0, 2)) == 2) & (64 <= ((tl.program_id(0) // 50176) % 96))) & (((tl.program_id(0) // 50176) % 96) < 96)))), other=0.0), tl.load(in31_ptr + (tl.maximum((((((((tl.program_id(0) // 4816896) * 32) + tl.maximum(((tl.program_id(0) // 50176) % 96) - 64, 0)) * 224) + ((tl.program_id(0) // 224) % 224)) * 224) + (tl.program_id(0) % 224)) - tl.maximum((((((((tl.program_id(0) // 4816896) * 32) + tl.maximum(((tl.program_id(0) // 50176) % 96) - 64, 0)) * 224) + ((tl.program_id(0) // 224) % 224)) * 224) + (tl.program_id(0) % 224)) - 16056319, 0), 0) + 0 * tl.arange(0, 2)), mask=((((_lv0 * 2) + tl.arange(0, 2)) < 3) & (((((((_lv0 * 2) + tl.arange(0, 2)) == 0) & (0 <= ((tl.program_id(0) // 50176) % 96))) & (((tl.program_id(0) // 50176) % 96) < 32)) | (((((_lv0 * 2) + tl.arange(0, 2)) == 1) & (32 <= ((tl.program_id(0) // 50176) % 96))) & (((tl.program_id(0) // 50176) % 96) < 64))) | (((((_lv0 * 2) + tl.arange(0, 2)) == 2) & (64 <= ((tl.program_id(0) // 50176) % 96))) & (((tl.program_id(0) // 50176) % 96) < 96)))), other=0.0))), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t014_s13(out, ins):
    grid = (48168960,)
    t014_s13_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31])
    return out


@triton.jit
def t014_s14_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 1960) & ((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) < 501760)), tl.load(in32_ptr + (tl.maximum(((((((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) // 50176) * 96) + (tl.program_id(0) // 256)) * 50176) + ((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) % 50176)) - tl.maximum(((((((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) // 50176) * 96) + (tl.program_id(0) // 256)) * 50176) + ((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) % 50176)) - 48168959, 0), 0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 1960) & ((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) < 501760)), other=0.0), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t014_s14(out, ins):
    grid = (24576,)
    t014_s14_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32])
    return out


@triton.jit
def t014_s15_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr):
    _acc0 = tl.zeros([256], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 256) + tl.arange(0, 256)) < 256) & True), tl.load(in33_ptr + (((tl.program_id(0) * 256) + ((_lv0 * 256) + tl.arange(0, 256))) + 0 * tl.arange(0, 256)), mask=((((_lv0 * 256) + tl.arange(0, 256)) < 256) & True), other=0.0), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t014_s15(out, ins):
    grid = (96,)
    t014_s15_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33])
    return out


@triton.jit
def t014_s16_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 1960) & ((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) < 501760)), ((tl.load(in32_ptr + (tl.maximum(((((((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) // 50176) * 96) + (tl.program_id(0) // 256)) * 50176) + ((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) % 50176)) - tl.maximum(((((((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) // 50176) * 96) + (tl.program_id(0) // 256)) * 50176) + ((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) % 50176)) - 48168959, 0), 0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 1960) & ((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) < 501760)), other=0.0) - (tl.load(in34_ptr + (tl.maximum((tl.program_id(0) // 256) - tl.maximum((tl.program_id(0) // 256) - 95, 0), 0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 1960) & ((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) < 501760)), other=0.0) * (1.0 * (1.0 / 501760.0)))) * (tl.load(in32_ptr + (tl.maximum(((((((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) // 50176) * 96) + (tl.program_id(0) // 256)) * 50176) + ((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) % 50176)) - tl.maximum(((((((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) // 50176) * 96) + (tl.program_id(0) // 256)) * 50176) + ((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) % 50176)) - 48168959, 0), 0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 1960) & ((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) < 501760)), other=0.0) - (tl.load(in34_ptr + (tl.maximum((tl.program_id(0) // 256) - tl.maximum((tl.program_id(0) // 256) - 95, 0), 0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 1960) & ((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) < 501760)), other=0.0) * (1.0 * (1.0 / 501760.0))))), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t014_s16(out, ins):
    grid = (24576,)
    t014_s16_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34])
    return out


@triton.jit
def t014_s17_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr):
    _acc0 = tl.zeros([256], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 256) + tl.arange(0, 256)) < 256) & True), tl.load(in35_ptr + (((tl.program_id(0) * 256) + ((_lv0 * 256) + tl.arange(0, 256))) + 0 * tl.arange(0, 256)), mask=((((_lv0 * 256) + tl.arange(0, 256)) < 256) & True), other=0.0), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t014_s17(out, ins):
    grid = (96,)
    t014_s17_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35])
    return out


@triton.jit
def t014_s18_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr):
    _acc0 = tl.zeros([1], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), ((((tl.load(in32_ptr + (tl.program_id(0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) - (tl.load(in34_ptr + (tl.maximum(((tl.program_id(0) // 50176) % 96) - tl.maximum(((tl.program_id(0) // 50176) % 96) - 95, 0), 0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) * (1.0 * (1.0 / 501760.0)))) * (1.0 / tl.sqrt(((tl.load(in36_ptr + (tl.maximum(((tl.program_id(0) // 50176) % 96) - tl.maximum(((tl.program_id(0) // 50176) % 96) - 95, 0), 0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) * (1.0 * (1.0 / 501760.0))) + (1.0 * (1.0 / 100000.0)))))) * tl.load(in7_ptr + (((tl.program_id(0) // 50176) % 96) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)) + tl.load(in8_ptr + (((tl.program_id(0) // 50176) % 96) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)), 0.0))
    _v = tl.maximum(tl.sum(_acc0, axis=0), (0.0 * (1.0 / 1.0)))
    tl.store(out_ptr + tl.program_id(0), _v)


def t014_s18(out, ins):
    grid = (48168960,)
    t014_s18_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36])
    return out


@triton.jit
def t014_s19_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr):
    _acc0 = tl.zeros([512], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 512) + tl.arange(0, 512)) < 864) & ((((1 <= (((tl.program_id(0) // 224) % 224) + ((((_lv0 * 512) + tl.arange(0, 512)) // 3) % 3))) & ((((tl.program_id(0) // 224) % 224) + ((((_lv0 * 512) + tl.arange(0, 512)) // 3) % 3)) < 225)) & (1 <= ((tl.program_id(0) % 224) + (((_lv0 * 512) + tl.arange(0, 512)) % 3)))) & (((tl.program_id(0) % 224) + (((_lv0 * 512) + tl.arange(0, 512)) % 3)) < 225))), (tl.load(in37_ptr + (tl.maximum((((((((tl.program_id(0) // 1605632) * 96) + (((_lv0 * 512) + tl.arange(0, 512)) // 9)) * 224) + tl.maximum((((tl.program_id(0) // 224) % 224) + ((((_lv0 * 512) + tl.arange(0, 512)) // 3) % 3)) - 1, 0)) * 224) + tl.maximum(((tl.program_id(0) % 224) + (((_lv0 * 512) + tl.arange(0, 512)) % 3)) - 1, 0)) - tl.maximum((((((((tl.program_id(0) // 1605632) * 96) + (((_lv0 * 512) + tl.arange(0, 512)) // 9)) * 224) + tl.maximum((((tl.program_id(0) // 224) % 224) + ((((_lv0 * 512) + tl.arange(0, 512)) // 3) % 3)) - 1, 0)) * 224) + tl.maximum(((tl.program_id(0) % 224) + (((_lv0 * 512) + tl.arange(0, 512)) % 3)) - 1, 0)) - 48168959, 0), 0) + 0 * tl.arange(0, 512)), mask=((((_lv0 * 512) + tl.arange(0, 512)) < 864) & ((((1 <= (((tl.program_id(0) // 224) % 224) + ((((_lv0 * 512) + tl.arange(0, 512)) // 3) % 3))) & ((((tl.program_id(0) // 224) % 224) + ((((_lv0 * 512) + tl.arange(0, 512)) // 3) % 3)) < 225)) & (1 <= ((tl.program_id(0) % 224) + (((_lv0 * 512) + tl.arange(0, 512)) % 3)))) & (((tl.program_id(0) % 224) + (((_lv0 * 512) + tl.arange(0, 512)) % 3)) < 225))), other=0.0) * tl.load(in9_ptr + (((((((((tl.program_id(0) // 50176) % 32) * 96) + (((_lv0 * 512) + tl.arange(0, 512)) // 9)) * 3) + ((((_lv0 * 512) + tl.arange(0, 512)) // 3) % 3)) * 3) + (((_lv0 * 512) + tl.arange(0, 512)) % 3)) + 0 * tl.arange(0, 512)), mask=((((_lv0 * 512) + tl.arange(0, 512)) < 864) & ((((1 <= (((tl.program_id(0) // 224) % 224) + ((((_lv0 * 512) + tl.arange(0, 512)) // 3) % 3))) & ((((tl.program_id(0) // 224) % 224) + ((((_lv0 * 512) + tl.arange(0, 512)) // 3) % 3)) < 225)) & (1 <= ((tl.program_id(0) % 224) + (((_lv0 * 512) + tl.arange(0, 512)) % 3)))) & (((tl.program_id(0) % 224) + (((_lv0 * 512) + tl.arange(0, 512)) % 3)) < 225))), other=0.0)), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t014_s19(out, ins):
    grid = (16056320,)
    t014_s19_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37])
    return out


@triton.jit
def t014_s20_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr, in38_ptr):
    _acc0 = tl.zeros([4], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 4) + tl.arange(0, 4)) < 4) & ((((((((_lv0 * 4) + tl.arange(0, 4)) == 0) & (0 <= ((tl.program_id(0) // 50176) % 128))) & (((tl.program_id(0) // 50176) % 128) < 32)) | (((((_lv0 * 4) + tl.arange(0, 4)) == 1) & (32 <= ((tl.program_id(0) // 50176) % 128))) & (((tl.program_id(0) // 50176) % 128) < 64))) | (((((_lv0 * 4) + tl.arange(0, 4)) == 2) & (64 <= ((tl.program_id(0) // 50176) % 128))) & (((tl.program_id(0) // 50176) % 128) < 96))) | (((((_lv0 * 4) + tl.arange(0, 4)) == 3) & (96 <= ((tl.program_id(0) // 50176) % 128))) & (((tl.program_id(0) // 50176) % 128) < 128)))), tl.where((((_lv0 * 4) + tl.arange(0, 4))).to(tl.float32) <= (1.0 * (1.0 / 2.0)), tl.load(in0_ptr + ((((((((tl.program_id(0) // 6422528) * 32) + ((tl.program_id(0) // 50176) % 128)) * 224) + ((tl.program_id(0) // 224) % 224)) * 224) + (tl.program_id(0) % 224)) + 0 * tl.arange(0, 4)), mask=((((_lv0 * 4) + tl.arange(0, 4)) < 4) & ((((((((_lv0 * 4) + tl.arange(0, 4)) == 0) & (0 <= ((tl.program_id(0) // 50176) % 128))) & (((tl.program_id(0) // 50176) % 128) < 32)) | (((((_lv0 * 4) + tl.arange(0, 4)) == 1) & (32 <= ((tl.program_id(0) // 50176) % 128))) & (((tl.program_id(0) // 50176) % 128) < 64))) | (((((_lv0 * 4) + tl.arange(0, 4)) == 2) & (64 <= ((tl.program_id(0) // 50176) % 128))) & (((tl.program_id(0) // 50176) % 128) < 96))) | (((((_lv0 * 4) + tl.arange(0, 4)) == 3) & (96 <= ((tl.program_id(0) // 50176) % 128))) & (((tl.program_id(0) // 50176) % 128) < 128)))), other=0.0), tl.where((((_lv0 * 4) + tl.arange(0, 4))).to(tl.float32) <= (3.0 * (1.0 / 2.0)), tl.load(in24_ptr + (tl.maximum((((((((tl.program_id(0) // 6422528) * 32) + tl.maximum(((tl.program_id(0) // 50176) % 128) - 32, 0)) * 224) + ((tl.program_id(0) // 224) % 224)) * 224) + (tl.program_id(0) % 224)) - tl.maximum((((((((tl.program_id(0) // 6422528) * 32) + tl.maximum(((tl.program_id(0) // 50176) % 128) - 32, 0)) * 224) + ((tl.program_id(0) // 224) % 224)) * 224) + (tl.program_id(0) % 224)) - 16056319, 0), 0) + 0 * tl.arange(0, 4)), mask=((((_lv0 * 4) + tl.arange(0, 4)) < 4) & ((((((((_lv0 * 4) + tl.arange(0, 4)) == 0) & (0 <= ((tl.program_id(0) // 50176) % 128))) & (((tl.program_id(0) // 50176) % 128) < 32)) | (((((_lv0 * 4) + tl.arange(0, 4)) == 1) & (32 <= ((tl.program_id(0) // 50176) % 128))) & (((tl.program_id(0) // 50176) % 128) < 64))) | (((((_lv0 * 4) + tl.arange(0, 4)) == 2) & (64 <= ((tl.program_id(0) // 50176) % 128))) & (((tl.program_id(0) // 50176) % 128) < 96))) | (((((_lv0 * 4) + tl.arange(0, 4)) == 3) & (96 <= ((tl.program_id(0) // 50176) % 128))) & (((tl.program_id(0) // 50176) % 128) < 128)))), other=0.0), tl.where((((_lv0 * 4) + tl.arange(0, 4))).to(tl.float32) <= (5.0 * (1.0 / 2.0)), tl.load(in31_ptr + (tl.maximum((((((((tl.program_id(0) // 6422528) * 32) + tl.maximum(((tl.program_id(0) // 50176) % 128) - 64, 0)) * 224) + ((tl.program_id(0) // 224) % 224)) * 224) + (tl.program_id(0) % 224)) - tl.maximum((((((((tl.program_id(0) // 6422528) * 32) + tl.maximum(((tl.program_id(0) // 50176) % 128) - 64, 0)) * 224) + ((tl.program_id(0) // 224) % 224)) * 224) + (tl.program_id(0) % 224)) - 16056319, 0), 0) + 0 * tl.arange(0, 4)), mask=((((_lv0 * 4) + tl.arange(0, 4)) < 4) & ((((((((_lv0 * 4) + tl.arange(0, 4)) == 0) & (0 <= ((tl.program_id(0) // 50176) % 128))) & (((tl.program_id(0) // 50176) % 128) < 32)) | (((((_lv0 * 4) + tl.arange(0, 4)) == 1) & (32 <= ((tl.program_id(0) // 50176) % 128))) & (((tl.program_id(0) // 50176) % 128) < 64))) | (((((_lv0 * 4) + tl.arange(0, 4)) == 2) & (64 <= ((tl.program_id(0) // 50176) % 128))) & (((tl.program_id(0) // 50176) % 128) < 96))) | (((((_lv0 * 4) + tl.arange(0, 4)) == 3) & (96 <= ((tl.program_id(0) // 50176) % 128))) & (((tl.program_id(0) // 50176) % 128) < 128)))), other=0.0), tl.load(in38_ptr + (tl.maximum((((((((tl.program_id(0) // 6422528) * 32) + tl.maximum(((tl.program_id(0) // 50176) % 128) - 96, 0)) * 224) + ((tl.program_id(0) // 224) % 224)) * 224) + (tl.program_id(0) % 224)) - tl.maximum((((((((tl.program_id(0) // 6422528) * 32) + tl.maximum(((tl.program_id(0) // 50176) % 128) - 96, 0)) * 224) + ((tl.program_id(0) // 224) % 224)) * 224) + (tl.program_id(0) % 224)) - 16056319, 0), 0) + 0 * tl.arange(0, 4)), mask=((((_lv0 * 4) + tl.arange(0, 4)) < 4) & ((((((((_lv0 * 4) + tl.arange(0, 4)) == 0) & (0 <= ((tl.program_id(0) // 50176) % 128))) & (((tl.program_id(0) // 50176) % 128) < 32)) | (((((_lv0 * 4) + tl.arange(0, 4)) == 1) & (32 <= ((tl.program_id(0) // 50176) % 128))) & (((tl.program_id(0) // 50176) % 128) < 64))) | (((((_lv0 * 4) + tl.arange(0, 4)) == 2) & (64 <= ((tl.program_id(0) // 50176) % 128))) & (((tl.program_id(0) // 50176) % 128) < 96))) | (((((_lv0 * 4) + tl.arange(0, 4)) == 3) & (96 <= ((tl.program_id(0) // 50176) % 128))) & (((tl.program_id(0) // 50176) % 128) < 128)))), other=0.0)))), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t014_s20(out, ins):
    grid = (64225280,)
    t014_s20_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37], ins[38])
    return out


@triton.jit
def t014_s21_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr, in38_ptr, in39_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 1960) & ((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) < 501760)), tl.load(in39_ptr + (tl.maximum(((((((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) // 50176) * 128) + (tl.program_id(0) // 256)) * 50176) + ((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) % 50176)) - tl.maximum(((((((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) // 50176) * 128) + (tl.program_id(0) // 256)) * 50176) + ((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) % 50176)) - 64225279, 0), 0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 1960) & ((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) < 501760)), other=0.0), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t014_s21(out, ins):
    grid = (32768,)
    t014_s21_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37], ins[38], ins[39])
    return out


@triton.jit
def t014_s22_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr, in38_ptr, in39_ptr, in40_ptr):
    _acc0 = tl.zeros([256], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 256) + tl.arange(0, 256)) < 256) & True), tl.load(in40_ptr + (((tl.program_id(0) * 256) + ((_lv0 * 256) + tl.arange(0, 256))) + 0 * tl.arange(0, 256)), mask=((((_lv0 * 256) + tl.arange(0, 256)) < 256) & True), other=0.0), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t014_s22(out, ins):
    grid = (128,)
    t014_s22_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37], ins[38], ins[39], ins[40])
    return out


@triton.jit
def t014_s23_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr, in38_ptr, in39_ptr, in40_ptr, in41_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 1960) & ((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) < 501760)), ((tl.load(in39_ptr + (tl.maximum(((((((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) // 50176) * 128) + (tl.program_id(0) // 256)) * 50176) + ((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) % 50176)) - tl.maximum(((((((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) // 50176) * 128) + (tl.program_id(0) // 256)) * 50176) + ((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) % 50176)) - 64225279, 0), 0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 1960) & ((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) < 501760)), other=0.0) - (tl.load(in41_ptr + (tl.maximum((tl.program_id(0) // 256) - tl.maximum((tl.program_id(0) // 256) - 127, 0), 0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 1960) & ((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) < 501760)), other=0.0) * (1.0 * (1.0 / 501760.0)))) * (tl.load(in39_ptr + (tl.maximum(((((((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) // 50176) * 128) + (tl.program_id(0) // 256)) * 50176) + ((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) % 50176)) - tl.maximum(((((((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) // 50176) * 128) + (tl.program_id(0) // 256)) * 50176) + ((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) % 50176)) - 64225279, 0), 0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 1960) & ((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) < 501760)), other=0.0) - (tl.load(in41_ptr + (tl.maximum((tl.program_id(0) // 256) - tl.maximum((tl.program_id(0) // 256) - 127, 0), 0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 1960) & ((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) < 501760)), other=0.0) * (1.0 * (1.0 / 501760.0))))), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t014_s23(out, ins):
    grid = (32768,)
    t014_s23_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37], ins[38], ins[39], ins[40], ins[41])
    return out


@triton.jit
def t014_s24_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr, in38_ptr, in39_ptr, in40_ptr, in41_ptr, in42_ptr):
    _acc0 = tl.zeros([256], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 256) + tl.arange(0, 256)) < 256) & True), tl.load(in42_ptr + (((tl.program_id(0) * 256) + ((_lv0 * 256) + tl.arange(0, 256))) + 0 * tl.arange(0, 256)), mask=((((_lv0 * 256) + tl.arange(0, 256)) < 256) & True), other=0.0), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t014_s24(out, ins):
    grid = (128,)
    t014_s24_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37], ins[38], ins[39], ins[40], ins[41], ins[42])
    return out


@triton.jit
def t014_s25_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr, in38_ptr, in39_ptr, in40_ptr, in41_ptr, in42_ptr, in43_ptr):
    _acc0 = tl.zeros([1], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), ((((tl.load(in39_ptr + (tl.program_id(0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) - (tl.load(in41_ptr + (tl.maximum(((tl.program_id(0) // 50176) % 128) - tl.maximum(((tl.program_id(0) // 50176) % 128) - 127, 0), 0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) * (1.0 * (1.0 / 501760.0)))) * (1.0 / tl.sqrt(((tl.load(in43_ptr + (tl.maximum(((tl.program_id(0) // 50176) % 128) - tl.maximum(((tl.program_id(0) // 50176) % 128) - 127, 0), 0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) * (1.0 * (1.0 / 501760.0))) + (1.0 * (1.0 / 100000.0)))))) * tl.load(in10_ptr + (((tl.program_id(0) // 50176) % 128) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)) + tl.load(in11_ptr + (((tl.program_id(0) // 50176) % 128) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)), 0.0))
    _v = tl.maximum(tl.sum(_acc0, axis=0), (0.0 * (1.0 / 1.0)))
    tl.store(out_ptr + tl.program_id(0), _v)


def t014_s25(out, ins):
    grid = (64225280,)
    t014_s25_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37], ins[38], ins[39], ins[40], ins[41], ins[42], ins[43])
    return out


@triton.jit
def t014_s26_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr, in38_ptr, in39_ptr, in40_ptr, in41_ptr, in42_ptr, in43_ptr, in44_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 1152) & ((((1 <= (((tl.program_id(0) // 224) % 224) + ((((_lv0 * 1024) + tl.arange(0, 1024)) // 3) % 3))) & ((((tl.program_id(0) // 224) % 224) + ((((_lv0 * 1024) + tl.arange(0, 1024)) // 3) % 3)) < 225)) & (1 <= ((tl.program_id(0) % 224) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 3)))) & (((tl.program_id(0) % 224) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 3)) < 225))), (tl.load(in44_ptr + (tl.maximum((((((((tl.program_id(0) // 1605632) * 128) + (((_lv0 * 1024) + tl.arange(0, 1024)) // 9)) * 224) + tl.maximum((((tl.program_id(0) // 224) % 224) + ((((_lv0 * 1024) + tl.arange(0, 1024)) // 3) % 3)) - 1, 0)) * 224) + tl.maximum(((tl.program_id(0) % 224) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 3)) - 1, 0)) - tl.maximum((((((((tl.program_id(0) // 1605632) * 128) + (((_lv0 * 1024) + tl.arange(0, 1024)) // 9)) * 224) + tl.maximum((((tl.program_id(0) // 224) % 224) + ((((_lv0 * 1024) + tl.arange(0, 1024)) // 3) % 3)) - 1, 0)) * 224) + tl.maximum(((tl.program_id(0) % 224) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 3)) - 1, 0)) - 64225279, 0), 0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 1152) & ((((1 <= (((tl.program_id(0) // 224) % 224) + ((((_lv0 * 1024) + tl.arange(0, 1024)) // 3) % 3))) & ((((tl.program_id(0) // 224) % 224) + ((((_lv0 * 1024) + tl.arange(0, 1024)) // 3) % 3)) < 225)) & (1 <= ((tl.program_id(0) % 224) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 3)))) & (((tl.program_id(0) % 224) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 3)) < 225))), other=0.0) * tl.load(in12_ptr + (((((((((tl.program_id(0) // 50176) % 32) * 128) + (((_lv0 * 1024) + tl.arange(0, 1024)) // 9)) * 3) + ((((_lv0 * 1024) + tl.arange(0, 1024)) // 3) % 3)) * 3) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 3)) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 1152) & ((((1 <= (((tl.program_id(0) // 224) % 224) + ((((_lv0 * 1024) + tl.arange(0, 1024)) // 3) % 3))) & ((((tl.program_id(0) // 224) % 224) + ((((_lv0 * 1024) + tl.arange(0, 1024)) // 3) % 3)) < 225)) & (1 <= ((tl.program_id(0) % 224) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 3)))) & (((tl.program_id(0) % 224) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 3)) < 225))), other=0.0)), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t014_s26(out, ins):
    grid = (16056320,)
    t014_s26_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37], ins[38], ins[39], ins[40], ins[41], ins[42], ins[43], ins[44])
    return out


@triton.jit
def t014_s27_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr, in38_ptr, in39_ptr, in40_ptr, in41_ptr, in42_ptr, in43_ptr, in44_ptr, in45_ptr):
    _acc0 = tl.zeros([4], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 4) + tl.arange(0, 4)) < 5) & (((((((((_lv0 * 4) + tl.arange(0, 4)) == 0) & (0 <= ((tl.program_id(0) // 50176) % 160))) & (((tl.program_id(0) // 50176) % 160) < 32)) | (((((_lv0 * 4) + tl.arange(0, 4)) == 1) & (32 <= ((tl.program_id(0) // 50176) % 160))) & (((tl.program_id(0) // 50176) % 160) < 64))) | (((((_lv0 * 4) + tl.arange(0, 4)) == 2) & (64 <= ((tl.program_id(0) // 50176) % 160))) & (((tl.program_id(0) // 50176) % 160) < 96))) | (((((_lv0 * 4) + tl.arange(0, 4)) == 3) & (96 <= ((tl.program_id(0) // 50176) % 160))) & (((tl.program_id(0) // 50176) % 160) < 128))) | (((((_lv0 * 4) + tl.arange(0, 4)) == 4) & (128 <= ((tl.program_id(0) // 50176) % 160))) & (((tl.program_id(0) // 50176) % 160) < 160)))), tl.where((((_lv0 * 4) + tl.arange(0, 4))).to(tl.float32) <= (1.0 * (1.0 / 2.0)), tl.load(in0_ptr + ((((((((tl.program_id(0) // 8028160) * 32) + ((tl.program_id(0) // 50176) % 160)) * 224) + ((tl.program_id(0) // 224) % 224)) * 224) + (tl.program_id(0) % 224)) + 0 * tl.arange(0, 4)), mask=((((_lv0 * 4) + tl.arange(0, 4)) < 5) & (((((((((_lv0 * 4) + tl.arange(0, 4)) == 0) & (0 <= ((tl.program_id(0) // 50176) % 160))) & (((tl.program_id(0) // 50176) % 160) < 32)) | (((((_lv0 * 4) + tl.arange(0, 4)) == 1) & (32 <= ((tl.program_id(0) // 50176) % 160))) & (((tl.program_id(0) // 50176) % 160) < 64))) | (((((_lv0 * 4) + tl.arange(0, 4)) == 2) & (64 <= ((tl.program_id(0) // 50176) % 160))) & (((tl.program_id(0) // 50176) % 160) < 96))) | (((((_lv0 * 4) + tl.arange(0, 4)) == 3) & (96 <= ((tl.program_id(0) // 50176) % 160))) & (((tl.program_id(0) // 50176) % 160) < 128))) | (((((_lv0 * 4) + tl.arange(0, 4)) == 4) & (128 <= ((tl.program_id(0) // 50176) % 160))) & (((tl.program_id(0) // 50176) % 160) < 160)))), other=0.0), tl.where((((_lv0 * 4) + tl.arange(0, 4))).to(tl.float32) <= (3.0 * (1.0 / 2.0)), tl.load(in24_ptr + (tl.maximum((((((((tl.program_id(0) // 8028160) * 32) + tl.maximum(((tl.program_id(0) // 50176) % 160) - 32, 0)) * 224) + ((tl.program_id(0) // 224) % 224)) * 224) + (tl.program_id(0) % 224)) - tl.maximum((((((((tl.program_id(0) // 8028160) * 32) + tl.maximum(((tl.program_id(0) // 50176) % 160) - 32, 0)) * 224) + ((tl.program_id(0) // 224) % 224)) * 224) + (tl.program_id(0) % 224)) - 16056319, 0), 0) + 0 * tl.arange(0, 4)), mask=((((_lv0 * 4) + tl.arange(0, 4)) < 5) & (((((((((_lv0 * 4) + tl.arange(0, 4)) == 0) & (0 <= ((tl.program_id(0) // 50176) % 160))) & (((tl.program_id(0) // 50176) % 160) < 32)) | (((((_lv0 * 4) + tl.arange(0, 4)) == 1) & (32 <= ((tl.program_id(0) // 50176) % 160))) & (((tl.program_id(0) // 50176) % 160) < 64))) | (((((_lv0 * 4) + tl.arange(0, 4)) == 2) & (64 <= ((tl.program_id(0) // 50176) % 160))) & (((tl.program_id(0) // 50176) % 160) < 96))) | (((((_lv0 * 4) + tl.arange(0, 4)) == 3) & (96 <= ((tl.program_id(0) // 50176) % 160))) & (((tl.program_id(0) // 50176) % 160) < 128))) | (((((_lv0 * 4) + tl.arange(0, 4)) == 4) & (128 <= ((tl.program_id(0) // 50176) % 160))) & (((tl.program_id(0) // 50176) % 160) < 160)))), other=0.0), tl.where((((_lv0 * 4) + tl.arange(0, 4))).to(tl.float32) <= (5.0 * (1.0 / 2.0)), tl.load(in31_ptr + (tl.maximum((((((((tl.program_id(0) // 8028160) * 32) + tl.maximum(((tl.program_id(0) // 50176) % 160) - 64, 0)) * 224) + ((tl.program_id(0) // 224) % 224)) * 224) + (tl.program_id(0) % 224)) - tl.maximum((((((((tl.program_id(0) // 8028160) * 32) + tl.maximum(((tl.program_id(0) // 50176) % 160) - 64, 0)) * 224) + ((tl.program_id(0) // 224) % 224)) * 224) + (tl.program_id(0) % 224)) - 16056319, 0), 0) + 0 * tl.arange(0, 4)), mask=((((_lv0 * 4) + tl.arange(0, 4)) < 5) & (((((((((_lv0 * 4) + tl.arange(0, 4)) == 0) & (0 <= ((tl.program_id(0) // 50176) % 160))) & (((tl.program_id(0) // 50176) % 160) < 32)) | (((((_lv0 * 4) + tl.arange(0, 4)) == 1) & (32 <= ((tl.program_id(0) // 50176) % 160))) & (((tl.program_id(0) // 50176) % 160) < 64))) | (((((_lv0 * 4) + tl.arange(0, 4)) == 2) & (64 <= ((tl.program_id(0) // 50176) % 160))) & (((tl.program_id(0) // 50176) % 160) < 96))) | (((((_lv0 * 4) + tl.arange(0, 4)) == 3) & (96 <= ((tl.program_id(0) // 50176) % 160))) & (((tl.program_id(0) // 50176) % 160) < 128))) | (((((_lv0 * 4) + tl.arange(0, 4)) == 4) & (128 <= ((tl.program_id(0) // 50176) % 160))) & (((tl.program_id(0) // 50176) % 160) < 160)))), other=0.0), tl.where((((_lv0 * 4) + tl.arange(0, 4))).to(tl.float32) <= (7.0 * (1.0 / 2.0)), tl.load(in38_ptr + (tl.maximum((((((((tl.program_id(0) // 8028160) * 32) + tl.maximum(((tl.program_id(0) // 50176) % 160) - 96, 0)) * 224) + ((tl.program_id(0) // 224) % 224)) * 224) + (tl.program_id(0) % 224)) - tl.maximum((((((((tl.program_id(0) // 8028160) * 32) + tl.maximum(((tl.program_id(0) // 50176) % 160) - 96, 0)) * 224) + ((tl.program_id(0) // 224) % 224)) * 224) + (tl.program_id(0) % 224)) - 16056319, 0), 0) + 0 * tl.arange(0, 4)), mask=((((_lv0 * 4) + tl.arange(0, 4)) < 5) & (((((((((_lv0 * 4) + tl.arange(0, 4)) == 0) & (0 <= ((tl.program_id(0) // 50176) % 160))) & (((tl.program_id(0) // 50176) % 160) < 32)) | (((((_lv0 * 4) + tl.arange(0, 4)) == 1) & (32 <= ((tl.program_id(0) // 50176) % 160))) & (((tl.program_id(0) // 50176) % 160) < 64))) | (((((_lv0 * 4) + tl.arange(0, 4)) == 2) & (64 <= ((tl.program_id(0) // 50176) % 160))) & (((tl.program_id(0) // 50176) % 160) < 96))) | (((((_lv0 * 4) + tl.arange(0, 4)) == 3) & (96 <= ((tl.program_id(0) // 50176) % 160))) & (((tl.program_id(0) // 50176) % 160) < 128))) | (((((_lv0 * 4) + tl.arange(0, 4)) == 4) & (128 <= ((tl.program_id(0) // 50176) % 160))) & (((tl.program_id(0) // 50176) % 160) < 160)))), other=0.0), tl.load(in45_ptr + (tl.maximum((((((((tl.program_id(0) // 8028160) * 32) + tl.maximum(((tl.program_id(0) // 50176) % 160) - 128, 0)) * 224) + ((tl.program_id(0) // 224) % 224)) * 224) + (tl.program_id(0) % 224)) - tl.maximum((((((((tl.program_id(0) // 8028160) * 32) + tl.maximum(((tl.program_id(0) // 50176) % 160) - 128, 0)) * 224) + ((tl.program_id(0) // 224) % 224)) * 224) + (tl.program_id(0) % 224)) - 16056319, 0), 0) + 0 * tl.arange(0, 4)), mask=((((_lv0 * 4) + tl.arange(0, 4)) < 5) & (((((((((_lv0 * 4) + tl.arange(0, 4)) == 0) & (0 <= ((tl.program_id(0) // 50176) % 160))) & (((tl.program_id(0) // 50176) % 160) < 32)) | (((((_lv0 * 4) + tl.arange(0, 4)) == 1) & (32 <= ((tl.program_id(0) // 50176) % 160))) & (((tl.program_id(0) // 50176) % 160) < 64))) | (((((_lv0 * 4) + tl.arange(0, 4)) == 2) & (64 <= ((tl.program_id(0) // 50176) % 160))) & (((tl.program_id(0) // 50176) % 160) < 96))) | (((((_lv0 * 4) + tl.arange(0, 4)) == 3) & (96 <= ((tl.program_id(0) // 50176) % 160))) & (((tl.program_id(0) // 50176) % 160) < 128))) | (((((_lv0 * 4) + tl.arange(0, 4)) == 4) & (128 <= ((tl.program_id(0) // 50176) % 160))) & (((tl.program_id(0) // 50176) % 160) < 160)))), other=0.0))))), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t014_s27(out, ins):
    grid = (80281600,)
    t014_s27_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37], ins[38], ins[39], ins[40], ins[41], ins[42], ins[43], ins[44], ins[45])
    return out


@triton.jit
def t014_s28_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr, in38_ptr, in39_ptr, in40_ptr, in41_ptr, in42_ptr, in43_ptr, in44_ptr, in45_ptr, in46_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 1960) & ((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) < 501760)), tl.load(in46_ptr + (tl.maximum(((((((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) // 50176) * 160) + (tl.program_id(0) // 256)) * 50176) + ((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) % 50176)) - tl.maximum(((((((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) // 50176) * 160) + (tl.program_id(0) // 256)) * 50176) + ((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) % 50176)) - 80281599, 0), 0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 1960) & ((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) < 501760)), other=0.0), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t014_s28(out, ins):
    grid = (40960,)
    t014_s28_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37], ins[38], ins[39], ins[40], ins[41], ins[42], ins[43], ins[44], ins[45], ins[46])
    return out


@triton.jit
def t014_s29_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr, in38_ptr, in39_ptr, in40_ptr, in41_ptr, in42_ptr, in43_ptr, in44_ptr, in45_ptr, in46_ptr, in47_ptr):
    _acc0 = tl.zeros([256], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 256) + tl.arange(0, 256)) < 256) & True), tl.load(in47_ptr + (((tl.program_id(0) * 256) + ((_lv0 * 256) + tl.arange(0, 256))) + 0 * tl.arange(0, 256)), mask=((((_lv0 * 256) + tl.arange(0, 256)) < 256) & True), other=0.0), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t014_s29(out, ins):
    grid = (160,)
    t014_s29_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37], ins[38], ins[39], ins[40], ins[41], ins[42], ins[43], ins[44], ins[45], ins[46], ins[47])
    return out


@triton.jit
def t014_s30_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr, in38_ptr, in39_ptr, in40_ptr, in41_ptr, in42_ptr, in43_ptr, in44_ptr, in45_ptr, in46_ptr, in47_ptr, in48_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 1960) & ((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) < 501760)), ((tl.load(in46_ptr + (tl.maximum(((((((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) // 50176) * 160) + (tl.program_id(0) // 256)) * 50176) + ((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) % 50176)) - tl.maximum(((((((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) // 50176) * 160) + (tl.program_id(0) // 256)) * 50176) + ((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) % 50176)) - 80281599, 0), 0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 1960) & ((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) < 501760)), other=0.0) - (tl.load(in48_ptr + (tl.maximum((tl.program_id(0) // 256) - tl.maximum((tl.program_id(0) // 256) - 159, 0), 0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 1960) & ((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) < 501760)), other=0.0) * (1.0 * (1.0 / 501760.0)))) * (tl.load(in46_ptr + (tl.maximum(((((((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) // 50176) * 160) + (tl.program_id(0) // 256)) * 50176) + ((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) % 50176)) - tl.maximum(((((((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) // 50176) * 160) + (tl.program_id(0) // 256)) * 50176) + ((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) % 50176)) - 80281599, 0), 0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 1960) & ((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) < 501760)), other=0.0) - (tl.load(in48_ptr + (tl.maximum((tl.program_id(0) // 256) - tl.maximum((tl.program_id(0) // 256) - 159, 0), 0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 1960) & ((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) < 501760)), other=0.0) * (1.0 * (1.0 / 501760.0))))), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t014_s30(out, ins):
    grid = (40960,)
    t014_s30_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37], ins[38], ins[39], ins[40], ins[41], ins[42], ins[43], ins[44], ins[45], ins[46], ins[47], ins[48])
    return out


@triton.jit
def t014_s31_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr, in38_ptr, in39_ptr, in40_ptr, in41_ptr, in42_ptr, in43_ptr, in44_ptr, in45_ptr, in46_ptr, in47_ptr, in48_ptr, in49_ptr):
    _acc0 = tl.zeros([256], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 256) + tl.arange(0, 256)) < 256) & True), tl.load(in49_ptr + (((tl.program_id(0) * 256) + ((_lv0 * 256) + tl.arange(0, 256))) + 0 * tl.arange(0, 256)), mask=((((_lv0 * 256) + tl.arange(0, 256)) < 256) & True), other=0.0), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t014_s31(out, ins):
    grid = (160,)
    t014_s31_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37], ins[38], ins[39], ins[40], ins[41], ins[42], ins[43], ins[44], ins[45], ins[46], ins[47], ins[48], ins[49])
    return out


@triton.jit
def t014_s32_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr, in38_ptr, in39_ptr, in40_ptr, in41_ptr, in42_ptr, in43_ptr, in44_ptr, in45_ptr, in46_ptr, in47_ptr, in48_ptr, in49_ptr, in50_ptr):
    _acc0 = tl.zeros([1], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), ((((tl.load(in46_ptr + (tl.program_id(0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) - (tl.load(in48_ptr + (tl.maximum(((tl.program_id(0) // 50176) % 160) - tl.maximum(((tl.program_id(0) // 50176) % 160) - 159, 0), 0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) * (1.0 * (1.0 / 501760.0)))) * (1.0 / tl.sqrt(((tl.load(in50_ptr + (tl.maximum(((tl.program_id(0) // 50176) % 160) - tl.maximum(((tl.program_id(0) // 50176) % 160) - 159, 0), 0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) * (1.0 * (1.0 / 501760.0))) + (1.0 * (1.0 / 100000.0)))))) * tl.load(in13_ptr + (((tl.program_id(0) // 50176) % 160) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)) + tl.load(in14_ptr + (((tl.program_id(0) // 50176) % 160) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)), 0.0))
    _v = tl.maximum(tl.sum(_acc0, axis=0), (0.0 * (1.0 / 1.0)))
    tl.store(out_ptr + tl.program_id(0), _v)


def t014_s32(out, ins):
    grid = (80281600,)
    t014_s32_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37], ins[38], ins[39], ins[40], ins[41], ins[42], ins[43], ins[44], ins[45], ins[46], ins[47], ins[48], ins[49], ins[50])
    return out


@triton.jit
def t014_s33_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr, in38_ptr, in39_ptr, in40_ptr, in41_ptr, in42_ptr, in43_ptr, in44_ptr, in45_ptr, in46_ptr, in47_ptr, in48_ptr, in49_ptr, in50_ptr, in51_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 1440) & ((((1 <= (((tl.program_id(0) // 224) % 224) + ((((_lv0 * 1024) + tl.arange(0, 1024)) // 3) % 3))) & ((((tl.program_id(0) // 224) % 224) + ((((_lv0 * 1024) + tl.arange(0, 1024)) // 3) % 3)) < 225)) & (1 <= ((tl.program_id(0) % 224) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 3)))) & (((tl.program_id(0) % 224) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 3)) < 225))), (tl.load(in51_ptr + (tl.maximum((((((((tl.program_id(0) // 1605632) * 160) + (((_lv0 * 1024) + tl.arange(0, 1024)) // 9)) * 224) + tl.maximum((((tl.program_id(0) // 224) % 224) + ((((_lv0 * 1024) + tl.arange(0, 1024)) // 3) % 3)) - 1, 0)) * 224) + tl.maximum(((tl.program_id(0) % 224) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 3)) - 1, 0)) - tl.maximum((((((((tl.program_id(0) // 1605632) * 160) + (((_lv0 * 1024) + tl.arange(0, 1024)) // 9)) * 224) + tl.maximum((((tl.program_id(0) // 224) % 224) + ((((_lv0 * 1024) + tl.arange(0, 1024)) // 3) % 3)) - 1, 0)) * 224) + tl.maximum(((tl.program_id(0) % 224) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 3)) - 1, 0)) - 80281599, 0), 0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 1440) & ((((1 <= (((tl.program_id(0) // 224) % 224) + ((((_lv0 * 1024) + tl.arange(0, 1024)) // 3) % 3))) & ((((tl.program_id(0) // 224) % 224) + ((((_lv0 * 1024) + tl.arange(0, 1024)) // 3) % 3)) < 225)) & (1 <= ((tl.program_id(0) % 224) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 3)))) & (((tl.program_id(0) % 224) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 3)) < 225))), other=0.0) * tl.load(in15_ptr + (((((((((tl.program_id(0) // 50176) % 32) * 160) + (((_lv0 * 1024) + tl.arange(0, 1024)) // 9)) * 3) + ((((_lv0 * 1024) + tl.arange(0, 1024)) // 3) % 3)) * 3) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 3)) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 1440) & ((((1 <= (((tl.program_id(0) // 224) % 224) + ((((_lv0 * 1024) + tl.arange(0, 1024)) // 3) % 3))) & ((((tl.program_id(0) // 224) % 224) + ((((_lv0 * 1024) + tl.arange(0, 1024)) // 3) % 3)) < 225)) & (1 <= ((tl.program_id(0) % 224) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 3)))) & (((tl.program_id(0) % 224) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 3)) < 225))), other=0.0)), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t014_s33(out, ins):
    grid = (16056320,)
    t014_s33_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37], ins[38], ins[39], ins[40], ins[41], ins[42], ins[43], ins[44], ins[45], ins[46], ins[47], ins[48], ins[49], ins[50], ins[51])
    return out


@triton.jit
def t014_s34_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr, in38_ptr, in39_ptr, in40_ptr, in41_ptr, in42_ptr, in43_ptr, in44_ptr, in45_ptr, in46_ptr, in47_ptr, in48_ptr, in49_ptr, in50_ptr, in51_ptr, in52_ptr):
    _acc0 = tl.zeros([4], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 4) + tl.arange(0, 4)) < 6) & ((((((((((_lv0 * 4) + tl.arange(0, 4)) == 0) & (0 <= ((tl.program_id(0) // 50176) % 192))) & (((tl.program_id(0) // 50176) % 192) < 32)) | (((((_lv0 * 4) + tl.arange(0, 4)) == 1) & (32 <= ((tl.program_id(0) // 50176) % 192))) & (((tl.program_id(0) // 50176) % 192) < 64))) | (((((_lv0 * 4) + tl.arange(0, 4)) == 2) & (64 <= ((tl.program_id(0) // 50176) % 192))) & (((tl.program_id(0) // 50176) % 192) < 96))) | (((((_lv0 * 4) + tl.arange(0, 4)) == 3) & (96 <= ((tl.program_id(0) // 50176) % 192))) & (((tl.program_id(0) // 50176) % 192) < 128))) | (((((_lv0 * 4) + tl.arange(0, 4)) == 4) & (128 <= ((tl.program_id(0) // 50176) % 192))) & (((tl.program_id(0) // 50176) % 192) < 160))) | (((((_lv0 * 4) + tl.arange(0, 4)) == 5) & (160 <= ((tl.program_id(0) // 50176) % 192))) & (((tl.program_id(0) // 50176) % 192) < 192)))), tl.where((((_lv0 * 4) + tl.arange(0, 4))).to(tl.float32) <= (1.0 * (1.0 / 2.0)), tl.load(in0_ptr + ((((((((tl.program_id(0) // 9633792) * 32) + ((tl.program_id(0) // 50176) % 192)) * 224) + ((tl.program_id(0) // 224) % 224)) * 224) + (tl.program_id(0) % 224)) + 0 * tl.arange(0, 4)), mask=((((_lv0 * 4) + tl.arange(0, 4)) < 6) & ((((((((((_lv0 * 4) + tl.arange(0, 4)) == 0) & (0 <= ((tl.program_id(0) // 50176) % 192))) & (((tl.program_id(0) // 50176) % 192) < 32)) | (((((_lv0 * 4) + tl.arange(0, 4)) == 1) & (32 <= ((tl.program_id(0) // 50176) % 192))) & (((tl.program_id(0) // 50176) % 192) < 64))) | (((((_lv0 * 4) + tl.arange(0, 4)) == 2) & (64 <= ((tl.program_id(0) // 50176) % 192))) & (((tl.program_id(0) // 50176) % 192) < 96))) | (((((_lv0 * 4) + tl.arange(0, 4)) == 3) & (96 <= ((tl.program_id(0) // 50176) % 192))) & (((tl.program_id(0) // 50176) % 192) < 128))) | (((((_lv0 * 4) + tl.arange(0, 4)) == 4) & (128 <= ((tl.program_id(0) // 50176) % 192))) & (((tl.program_id(0) // 50176) % 192) < 160))) | (((((_lv0 * 4) + tl.arange(0, 4)) == 5) & (160 <= ((tl.program_id(0) // 50176) % 192))) & (((tl.program_id(0) // 50176) % 192) < 192)))), other=0.0), tl.where((((_lv0 * 4) + tl.arange(0, 4))).to(tl.float32) <= (3.0 * (1.0 / 2.0)), tl.load(in24_ptr + (tl.maximum((((((((tl.program_id(0) // 9633792) * 32) + tl.maximum(((tl.program_id(0) // 50176) % 192) - 32, 0)) * 224) + ((tl.program_id(0) // 224) % 224)) * 224) + (tl.program_id(0) % 224)) - tl.maximum((((((((tl.program_id(0) // 9633792) * 32) + tl.maximum(((tl.program_id(0) // 50176) % 192) - 32, 0)) * 224) + ((tl.program_id(0) // 224) % 224)) * 224) + (tl.program_id(0) % 224)) - 16056319, 0), 0) + 0 * tl.arange(0, 4)), mask=((((_lv0 * 4) + tl.arange(0, 4)) < 6) & ((((((((((_lv0 * 4) + tl.arange(0, 4)) == 0) & (0 <= ((tl.program_id(0) // 50176) % 192))) & (((tl.program_id(0) // 50176) % 192) < 32)) | (((((_lv0 * 4) + tl.arange(0, 4)) == 1) & (32 <= ((tl.program_id(0) // 50176) % 192))) & (((tl.program_id(0) // 50176) % 192) < 64))) | (((((_lv0 * 4) + tl.arange(0, 4)) == 2) & (64 <= ((tl.program_id(0) // 50176) % 192))) & (((tl.program_id(0) // 50176) % 192) < 96))) | (((((_lv0 * 4) + tl.arange(0, 4)) == 3) & (96 <= ((tl.program_id(0) // 50176) % 192))) & (((tl.program_id(0) // 50176) % 192) < 128))) | (((((_lv0 * 4) + tl.arange(0, 4)) == 4) & (128 <= ((tl.program_id(0) // 50176) % 192))) & (((tl.program_id(0) // 50176) % 192) < 160))) | (((((_lv0 * 4) + tl.arange(0, 4)) == 5) & (160 <= ((tl.program_id(0) // 50176) % 192))) & (((tl.program_id(0) // 50176) % 192) < 192)))), other=0.0), tl.where((((_lv0 * 4) + tl.arange(0, 4))).to(tl.float32) <= (5.0 * (1.0 / 2.0)), tl.load(in31_ptr + (tl.maximum((((((((tl.program_id(0) // 9633792) * 32) + tl.maximum(((tl.program_id(0) // 50176) % 192) - 64, 0)) * 224) + ((tl.program_id(0) // 224) % 224)) * 224) + (tl.program_id(0) % 224)) - tl.maximum((((((((tl.program_id(0) // 9633792) * 32) + tl.maximum(((tl.program_id(0) // 50176) % 192) - 64, 0)) * 224) + ((tl.program_id(0) // 224) % 224)) * 224) + (tl.program_id(0) % 224)) - 16056319, 0), 0) + 0 * tl.arange(0, 4)), mask=((((_lv0 * 4) + tl.arange(0, 4)) < 6) & ((((((((((_lv0 * 4) + tl.arange(0, 4)) == 0) & (0 <= ((tl.program_id(0) // 50176) % 192))) & (((tl.program_id(0) // 50176) % 192) < 32)) | (((((_lv0 * 4) + tl.arange(0, 4)) == 1) & (32 <= ((tl.program_id(0) // 50176) % 192))) & (((tl.program_id(0) // 50176) % 192) < 64))) | (((((_lv0 * 4) + tl.arange(0, 4)) == 2) & (64 <= ((tl.program_id(0) // 50176) % 192))) & (((tl.program_id(0) // 50176) % 192) < 96))) | (((((_lv0 * 4) + tl.arange(0, 4)) == 3) & (96 <= ((tl.program_id(0) // 50176) % 192))) & (((tl.program_id(0) // 50176) % 192) < 128))) | (((((_lv0 * 4) + tl.arange(0, 4)) == 4) & (128 <= ((tl.program_id(0) // 50176) % 192))) & (((tl.program_id(0) // 50176) % 192) < 160))) | (((((_lv0 * 4) + tl.arange(0, 4)) == 5) & (160 <= ((tl.program_id(0) // 50176) % 192))) & (((tl.program_id(0) // 50176) % 192) < 192)))), other=0.0), tl.where((((_lv0 * 4) + tl.arange(0, 4))).to(tl.float32) <= (7.0 * (1.0 / 2.0)), tl.load(in38_ptr + (tl.maximum((((((((tl.program_id(0) // 9633792) * 32) + tl.maximum(((tl.program_id(0) // 50176) % 192) - 96, 0)) * 224) + ((tl.program_id(0) // 224) % 224)) * 224) + (tl.program_id(0) % 224)) - tl.maximum((((((((tl.program_id(0) // 9633792) * 32) + tl.maximum(((tl.program_id(0) // 50176) % 192) - 96, 0)) * 224) + ((tl.program_id(0) // 224) % 224)) * 224) + (tl.program_id(0) % 224)) - 16056319, 0), 0) + 0 * tl.arange(0, 4)), mask=((((_lv0 * 4) + tl.arange(0, 4)) < 6) & ((((((((((_lv0 * 4) + tl.arange(0, 4)) == 0) & (0 <= ((tl.program_id(0) // 50176) % 192))) & (((tl.program_id(0) // 50176) % 192) < 32)) | (((((_lv0 * 4) + tl.arange(0, 4)) == 1) & (32 <= ((tl.program_id(0) // 50176) % 192))) & (((tl.program_id(0) // 50176) % 192) < 64))) | (((((_lv0 * 4) + tl.arange(0, 4)) == 2) & (64 <= ((tl.program_id(0) // 50176) % 192))) & (((tl.program_id(0) // 50176) % 192) < 96))) | (((((_lv0 * 4) + tl.arange(0, 4)) == 3) & (96 <= ((tl.program_id(0) // 50176) % 192))) & (((tl.program_id(0) // 50176) % 192) < 128))) | (((((_lv0 * 4) + tl.arange(0, 4)) == 4) & (128 <= ((tl.program_id(0) // 50176) % 192))) & (((tl.program_id(0) // 50176) % 192) < 160))) | (((((_lv0 * 4) + tl.arange(0, 4)) == 5) & (160 <= ((tl.program_id(0) // 50176) % 192))) & (((tl.program_id(0) // 50176) % 192) < 192)))), other=0.0), tl.where((((_lv0 * 4) + tl.arange(0, 4))).to(tl.float32) <= (9.0 * (1.0 / 2.0)), tl.load(in45_ptr + (tl.maximum((((((((tl.program_id(0) // 9633792) * 32) + tl.maximum(((tl.program_id(0) // 50176) % 192) - 128, 0)) * 224) + ((tl.program_id(0) // 224) % 224)) * 224) + (tl.program_id(0) % 224)) - tl.maximum((((((((tl.program_id(0) // 9633792) * 32) + tl.maximum(((tl.program_id(0) // 50176) % 192) - 128, 0)) * 224) + ((tl.program_id(0) // 224) % 224)) * 224) + (tl.program_id(0) % 224)) - 16056319, 0), 0) + 0 * tl.arange(0, 4)), mask=((((_lv0 * 4) + tl.arange(0, 4)) < 6) & ((((((((((_lv0 * 4) + tl.arange(0, 4)) == 0) & (0 <= ((tl.program_id(0) // 50176) % 192))) & (((tl.program_id(0) // 50176) % 192) < 32)) | (((((_lv0 * 4) + tl.arange(0, 4)) == 1) & (32 <= ((tl.program_id(0) // 50176) % 192))) & (((tl.program_id(0) // 50176) % 192) < 64))) | (((((_lv0 * 4) + tl.arange(0, 4)) == 2) & (64 <= ((tl.program_id(0) // 50176) % 192))) & (((tl.program_id(0) // 50176) % 192) < 96))) | (((((_lv0 * 4) + tl.arange(0, 4)) == 3) & (96 <= ((tl.program_id(0) // 50176) % 192))) & (((tl.program_id(0) // 50176) % 192) < 128))) | (((((_lv0 * 4) + tl.arange(0, 4)) == 4) & (128 <= ((tl.program_id(0) // 50176) % 192))) & (((tl.program_id(0) // 50176) % 192) < 160))) | (((((_lv0 * 4) + tl.arange(0, 4)) == 5) & (160 <= ((tl.program_id(0) // 50176) % 192))) & (((tl.program_id(0) // 50176) % 192) < 192)))), other=0.0), tl.load(in52_ptr + (tl.maximum((((((((tl.program_id(0) // 9633792) * 32) + tl.maximum(((tl.program_id(0) // 50176) % 192) - 160, 0)) * 224) + ((tl.program_id(0) // 224) % 224)) * 224) + (tl.program_id(0) % 224)) - tl.maximum((((((((tl.program_id(0) // 9633792) * 32) + tl.maximum(((tl.program_id(0) // 50176) % 192) - 160, 0)) * 224) + ((tl.program_id(0) // 224) % 224)) * 224) + (tl.program_id(0) % 224)) - 16056319, 0), 0) + 0 * tl.arange(0, 4)), mask=((((_lv0 * 4) + tl.arange(0, 4)) < 6) & ((((((((((_lv0 * 4) + tl.arange(0, 4)) == 0) & (0 <= ((tl.program_id(0) // 50176) % 192))) & (((tl.program_id(0) // 50176) % 192) < 32)) | (((((_lv0 * 4) + tl.arange(0, 4)) == 1) & (32 <= ((tl.program_id(0) // 50176) % 192))) & (((tl.program_id(0) // 50176) % 192) < 64))) | (((((_lv0 * 4) + tl.arange(0, 4)) == 2) & (64 <= ((tl.program_id(0) // 50176) % 192))) & (((tl.program_id(0) // 50176) % 192) < 96))) | (((((_lv0 * 4) + tl.arange(0, 4)) == 3) & (96 <= ((tl.program_id(0) // 50176) % 192))) & (((tl.program_id(0) // 50176) % 192) < 128))) | (((((_lv0 * 4) + tl.arange(0, 4)) == 4) & (128 <= ((tl.program_id(0) // 50176) % 192))) & (((tl.program_id(0) // 50176) % 192) < 160))) | (((((_lv0 * 4) + tl.arange(0, 4)) == 5) & (160 <= ((tl.program_id(0) // 50176) % 192))) & (((tl.program_id(0) // 50176) % 192) < 192)))), other=0.0)))))), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t014_s34(out, ins):
    grid = (96337920,)
    t014_s34_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37], ins[38], ins[39], ins[40], ins[41], ins[42], ins[43], ins[44], ins[45], ins[46], ins[47], ins[48], ins[49], ins[50], ins[51], ins[52])
    return out


@triton.jit
def t014_s35_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr, in38_ptr, in39_ptr, in40_ptr, in41_ptr, in42_ptr, in43_ptr, in44_ptr, in45_ptr, in46_ptr, in47_ptr, in48_ptr, in49_ptr, in50_ptr, in51_ptr, in52_ptr, in53_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 1960) & ((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) < 501760)), tl.load(in53_ptr + (tl.maximum(((((((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) // 50176) * 192) + (tl.program_id(0) // 256)) * 50176) + ((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) % 50176)) - tl.maximum(((((((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) // 50176) * 192) + (tl.program_id(0) // 256)) * 50176) + ((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) % 50176)) - 96337919, 0), 0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 1960) & ((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) < 501760)), other=0.0), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t014_s35(out, ins):
    grid = (49152,)
    t014_s35_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37], ins[38], ins[39], ins[40], ins[41], ins[42], ins[43], ins[44], ins[45], ins[46], ins[47], ins[48], ins[49], ins[50], ins[51], ins[52], ins[53])
    return out


@triton.jit
def t014_s36_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr, in38_ptr, in39_ptr, in40_ptr, in41_ptr, in42_ptr, in43_ptr, in44_ptr, in45_ptr, in46_ptr, in47_ptr, in48_ptr, in49_ptr, in50_ptr, in51_ptr, in52_ptr, in53_ptr, in54_ptr):
    _acc0 = tl.zeros([256], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 256) + tl.arange(0, 256)) < 256) & True), tl.load(in54_ptr + (((tl.program_id(0) * 256) + ((_lv0 * 256) + tl.arange(0, 256))) + 0 * tl.arange(0, 256)), mask=((((_lv0 * 256) + tl.arange(0, 256)) < 256) & True), other=0.0), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t014_s36(out, ins):
    grid = (192,)
    t014_s36_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37], ins[38], ins[39], ins[40], ins[41], ins[42], ins[43], ins[44], ins[45], ins[46], ins[47], ins[48], ins[49], ins[50], ins[51], ins[52], ins[53], ins[54])
    return out


@triton.jit
def t014_s37_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr, in38_ptr, in39_ptr, in40_ptr, in41_ptr, in42_ptr, in43_ptr, in44_ptr, in45_ptr, in46_ptr, in47_ptr, in48_ptr, in49_ptr, in50_ptr, in51_ptr, in52_ptr, in53_ptr, in54_ptr, in55_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 1960) & ((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) < 501760)), ((tl.load(in53_ptr + (tl.maximum(((((((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) // 50176) * 192) + (tl.program_id(0) // 256)) * 50176) + ((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) % 50176)) - tl.maximum(((((((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) // 50176) * 192) + (tl.program_id(0) // 256)) * 50176) + ((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) % 50176)) - 96337919, 0), 0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 1960) & ((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) < 501760)), other=0.0) - (tl.load(in55_ptr + (tl.maximum((tl.program_id(0) // 256) - tl.maximum((tl.program_id(0) // 256) - 191, 0), 0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 1960) & ((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) < 501760)), other=0.0) * (1.0 * (1.0 / 501760.0)))) * (tl.load(in53_ptr + (tl.maximum(((((((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) // 50176) * 192) + (tl.program_id(0) // 256)) * 50176) + ((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) % 50176)) - tl.maximum(((((((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) // 50176) * 192) + (tl.program_id(0) // 256)) * 50176) + ((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) % 50176)) - 96337919, 0), 0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 1960) & ((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) < 501760)), other=0.0) - (tl.load(in55_ptr + (tl.maximum((tl.program_id(0) // 256) - tl.maximum((tl.program_id(0) // 256) - 191, 0), 0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 1960) & ((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) < 501760)), other=0.0) * (1.0 * (1.0 / 501760.0))))), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t014_s37(out, ins):
    grid = (49152,)
    t014_s37_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37], ins[38], ins[39], ins[40], ins[41], ins[42], ins[43], ins[44], ins[45], ins[46], ins[47], ins[48], ins[49], ins[50], ins[51], ins[52], ins[53], ins[54], ins[55])
    return out


@triton.jit
def t014_s38_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr, in38_ptr, in39_ptr, in40_ptr, in41_ptr, in42_ptr, in43_ptr, in44_ptr, in45_ptr, in46_ptr, in47_ptr, in48_ptr, in49_ptr, in50_ptr, in51_ptr, in52_ptr, in53_ptr, in54_ptr, in55_ptr, in56_ptr):
    _acc0 = tl.zeros([256], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 256) + tl.arange(0, 256)) < 256) & True), tl.load(in56_ptr + (((tl.program_id(0) * 256) + ((_lv0 * 256) + tl.arange(0, 256))) + 0 * tl.arange(0, 256)), mask=((((_lv0 * 256) + tl.arange(0, 256)) < 256) & True), other=0.0), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t014_s38(out, ins):
    grid = (192,)
    t014_s38_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37], ins[38], ins[39], ins[40], ins[41], ins[42], ins[43], ins[44], ins[45], ins[46], ins[47], ins[48], ins[49], ins[50], ins[51], ins[52], ins[53], ins[54], ins[55], ins[56])
    return out


@triton.jit
def t014_s39_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr, in38_ptr, in39_ptr, in40_ptr, in41_ptr, in42_ptr, in43_ptr, in44_ptr, in45_ptr, in46_ptr, in47_ptr, in48_ptr, in49_ptr, in50_ptr, in51_ptr, in52_ptr, in53_ptr, in54_ptr, in55_ptr, in56_ptr, in57_ptr):
    _acc0 = tl.zeros([1], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), ((((tl.load(in53_ptr + (tl.program_id(0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) - (tl.load(in55_ptr + (tl.maximum(((tl.program_id(0) // 50176) % 192) - tl.maximum(((tl.program_id(0) // 50176) % 192) - 191, 0), 0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) * (1.0 * (1.0 / 501760.0)))) * (1.0 / tl.sqrt(((tl.load(in57_ptr + (tl.maximum(((tl.program_id(0) // 50176) % 192) - tl.maximum(((tl.program_id(0) // 50176) % 192) - 191, 0), 0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) * (1.0 * (1.0 / 501760.0))) + (1.0 * (1.0 / 100000.0)))))) * tl.load(in16_ptr + (((tl.program_id(0) // 50176) % 192) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)) + tl.load(in17_ptr + (((tl.program_id(0) // 50176) % 192) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)), 0.0))
    _v = tl.maximum(tl.sum(_acc0, axis=0), (0.0 * (1.0 / 1.0)))
    tl.store(out_ptr + tl.program_id(0), _v)


def t014_s39(out, ins):
    grid = (96337920,)
    t014_s39_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37], ins[38], ins[39], ins[40], ins[41], ins[42], ins[43], ins[44], ins[45], ins[46], ins[47], ins[48], ins[49], ins[50], ins[51], ins[52], ins[53], ins[54], ins[55], ins[56], ins[57])
    return out


@triton.jit
def t014_s40_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr, in38_ptr, in39_ptr, in40_ptr, in41_ptr, in42_ptr, in43_ptr, in44_ptr, in45_ptr, in46_ptr, in47_ptr, in48_ptr, in49_ptr, in50_ptr, in51_ptr, in52_ptr, in53_ptr, in54_ptr, in55_ptr, in56_ptr, in57_ptr, in58_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 1728) & ((((1 <= (((tl.program_id(0) // 224) % 224) + ((((_lv0 * 1024) + tl.arange(0, 1024)) // 3) % 3))) & ((((tl.program_id(0) // 224) % 224) + ((((_lv0 * 1024) + tl.arange(0, 1024)) // 3) % 3)) < 225)) & (1 <= ((tl.program_id(0) % 224) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 3)))) & (((tl.program_id(0) % 224) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 3)) < 225))), (tl.load(in58_ptr + (tl.maximum((((((((tl.program_id(0) // 1605632) * 192) + (((_lv0 * 1024) + tl.arange(0, 1024)) // 9)) * 224) + tl.maximum((((tl.program_id(0) // 224) % 224) + ((((_lv0 * 1024) + tl.arange(0, 1024)) // 3) % 3)) - 1, 0)) * 224) + tl.maximum(((tl.program_id(0) % 224) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 3)) - 1, 0)) - tl.maximum((((((((tl.program_id(0) // 1605632) * 192) + (((_lv0 * 1024) + tl.arange(0, 1024)) // 9)) * 224) + tl.maximum((((tl.program_id(0) // 224) % 224) + ((((_lv0 * 1024) + tl.arange(0, 1024)) // 3) % 3)) - 1, 0)) * 224) + tl.maximum(((tl.program_id(0) % 224) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 3)) - 1, 0)) - 96337919, 0), 0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 1728) & ((((1 <= (((tl.program_id(0) // 224) % 224) + ((((_lv0 * 1024) + tl.arange(0, 1024)) // 3) % 3))) & ((((tl.program_id(0) // 224) % 224) + ((((_lv0 * 1024) + tl.arange(0, 1024)) // 3) % 3)) < 225)) & (1 <= ((tl.program_id(0) % 224) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 3)))) & (((tl.program_id(0) % 224) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 3)) < 225))), other=0.0) * tl.load(in18_ptr + (((((((((tl.program_id(0) // 50176) % 32) * 192) + (((_lv0 * 1024) + tl.arange(0, 1024)) // 9)) * 3) + ((((_lv0 * 1024) + tl.arange(0, 1024)) // 3) % 3)) * 3) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 3)) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 1728) & ((((1 <= (((tl.program_id(0) // 224) % 224) + ((((_lv0 * 1024) + tl.arange(0, 1024)) // 3) % 3))) & ((((tl.program_id(0) // 224) % 224) + ((((_lv0 * 1024) + tl.arange(0, 1024)) // 3) % 3)) < 225)) & (1 <= ((tl.program_id(0) % 224) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 3)))) & (((tl.program_id(0) % 224) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 3)) < 225))), other=0.0)), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t014_s40(out, ins):
    grid = (16056320,)
    t014_s40_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37], ins[38], ins[39], ins[40], ins[41], ins[42], ins[43], ins[44], ins[45], ins[46], ins[47], ins[48], ins[49], ins[50], ins[51], ins[52], ins[53], ins[54], ins[55], ins[56], ins[57], ins[58])
    return out


@triton.jit
def t014_s41_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr, in38_ptr, in39_ptr, in40_ptr, in41_ptr, in42_ptr, in43_ptr, in44_ptr, in45_ptr, in46_ptr, in47_ptr, in48_ptr, in49_ptr, in50_ptr, in51_ptr, in52_ptr, in53_ptr, in54_ptr, in55_ptr, in56_ptr, in57_ptr, in58_ptr, in59_ptr):
    _acc0 = tl.zeros([4], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 4) + tl.arange(0, 4)) < 7) & (((((((((((_lv0 * 4) + tl.arange(0, 4)) == 0) & (0 <= ((tl.program_id(0) // 50176) % 224))) & (((tl.program_id(0) // 50176) % 224) < 32)) | (((((_lv0 * 4) + tl.arange(0, 4)) == 1) & (32 <= ((tl.program_id(0) // 50176) % 224))) & (((tl.program_id(0) // 50176) % 224) < 64))) | (((((_lv0 * 4) + tl.arange(0, 4)) == 2) & (64 <= ((tl.program_id(0) // 50176) % 224))) & (((tl.program_id(0) // 50176) % 224) < 96))) | (((((_lv0 * 4) + tl.arange(0, 4)) == 3) & (96 <= ((tl.program_id(0) // 50176) % 224))) & (((tl.program_id(0) // 50176) % 224) < 128))) | (((((_lv0 * 4) + tl.arange(0, 4)) == 4) & (128 <= ((tl.program_id(0) // 50176) % 224))) & (((tl.program_id(0) // 50176) % 224) < 160))) | (((((_lv0 * 4) + tl.arange(0, 4)) == 5) & (160 <= ((tl.program_id(0) // 50176) % 224))) & (((tl.program_id(0) // 50176) % 224) < 192))) | (((((_lv0 * 4) + tl.arange(0, 4)) == 6) & (192 <= ((tl.program_id(0) // 50176) % 224))) & (((tl.program_id(0) // 50176) % 224) < 224)))), tl.where((((_lv0 * 4) + tl.arange(0, 4))).to(tl.float32) <= (1.0 * (1.0 / 2.0)), tl.load(in0_ptr + ((((((((tl.program_id(0) // 11239424) * 32) + ((tl.program_id(0) // 50176) % 224)) * 224) + ((tl.program_id(0) // 224) % 224)) * 224) + (tl.program_id(0) % 224)) + 0 * tl.arange(0, 4)), mask=((((_lv0 * 4) + tl.arange(0, 4)) < 7) & (((((((((((_lv0 * 4) + tl.arange(0, 4)) == 0) & (0 <= ((tl.program_id(0) // 50176) % 224))) & (((tl.program_id(0) // 50176) % 224) < 32)) | (((((_lv0 * 4) + tl.arange(0, 4)) == 1) & (32 <= ((tl.program_id(0) // 50176) % 224))) & (((tl.program_id(0) // 50176) % 224) < 64))) | (((((_lv0 * 4) + tl.arange(0, 4)) == 2) & (64 <= ((tl.program_id(0) // 50176) % 224))) & (((tl.program_id(0) // 50176) % 224) < 96))) | (((((_lv0 * 4) + tl.arange(0, 4)) == 3) & (96 <= ((tl.program_id(0) // 50176) % 224))) & (((tl.program_id(0) // 50176) % 224) < 128))) | (((((_lv0 * 4) + tl.arange(0, 4)) == 4) & (128 <= ((tl.program_id(0) // 50176) % 224))) & (((tl.program_id(0) // 50176) % 224) < 160))) | (((((_lv0 * 4) + tl.arange(0, 4)) == 5) & (160 <= ((tl.program_id(0) // 50176) % 224))) & (((tl.program_id(0) // 50176) % 224) < 192))) | (((((_lv0 * 4) + tl.arange(0, 4)) == 6) & (192 <= ((tl.program_id(0) // 50176) % 224))) & (((tl.program_id(0) // 50176) % 224) < 224)))), other=0.0), tl.where((((_lv0 * 4) + tl.arange(0, 4))).to(tl.float32) <= (3.0 * (1.0 / 2.0)), tl.load(in24_ptr + (tl.maximum((((((((tl.program_id(0) // 11239424) * 32) + tl.maximum(((tl.program_id(0) // 50176) % 224) - 32, 0)) * 224) + ((tl.program_id(0) // 224) % 224)) * 224) + (tl.program_id(0) % 224)) - tl.maximum((((((((tl.program_id(0) // 11239424) * 32) + tl.maximum(((tl.program_id(0) // 50176) % 224) - 32, 0)) * 224) + ((tl.program_id(0) // 224) % 224)) * 224) + (tl.program_id(0) % 224)) - 16056319, 0), 0) + 0 * tl.arange(0, 4)), mask=((((_lv0 * 4) + tl.arange(0, 4)) < 7) & (((((((((((_lv0 * 4) + tl.arange(0, 4)) == 0) & (0 <= ((tl.program_id(0) // 50176) % 224))) & (((tl.program_id(0) // 50176) % 224) < 32)) | (((((_lv0 * 4) + tl.arange(0, 4)) == 1) & (32 <= ((tl.program_id(0) // 50176) % 224))) & (((tl.program_id(0) // 50176) % 224) < 64))) | (((((_lv0 * 4) + tl.arange(0, 4)) == 2) & (64 <= ((tl.program_id(0) // 50176) % 224))) & (((tl.program_id(0) // 50176) % 224) < 96))) | (((((_lv0 * 4) + tl.arange(0, 4)) == 3) & (96 <= ((tl.program_id(0) // 50176) % 224))) & (((tl.program_id(0) // 50176) % 224) < 128))) | (((((_lv0 * 4) + tl.arange(0, 4)) == 4) & (128 <= ((tl.program_id(0) // 50176) % 224))) & (((tl.program_id(0) // 50176) % 224) < 160))) | (((((_lv0 * 4) + tl.arange(0, 4)) == 5) & (160 <= ((tl.program_id(0) // 50176) % 224))) & (((tl.program_id(0) // 50176) % 224) < 192))) | (((((_lv0 * 4) + tl.arange(0, 4)) == 6) & (192 <= ((tl.program_id(0) // 50176) % 224))) & (((tl.program_id(0) // 50176) % 224) < 224)))), other=0.0), tl.where((((_lv0 * 4) + tl.arange(0, 4))).to(tl.float32) <= (5.0 * (1.0 / 2.0)), tl.load(in31_ptr + (tl.maximum((((((((tl.program_id(0) // 11239424) * 32) + tl.maximum(((tl.program_id(0) // 50176) % 224) - 64, 0)) * 224) + ((tl.program_id(0) // 224) % 224)) * 224) + (tl.program_id(0) % 224)) - tl.maximum((((((((tl.program_id(0) // 11239424) * 32) + tl.maximum(((tl.program_id(0) // 50176) % 224) - 64, 0)) * 224) + ((tl.program_id(0) // 224) % 224)) * 224) + (tl.program_id(0) % 224)) - 16056319, 0), 0) + 0 * tl.arange(0, 4)), mask=((((_lv0 * 4) + tl.arange(0, 4)) < 7) & (((((((((((_lv0 * 4) + tl.arange(0, 4)) == 0) & (0 <= ((tl.program_id(0) // 50176) % 224))) & (((tl.program_id(0) // 50176) % 224) < 32)) | (((((_lv0 * 4) + tl.arange(0, 4)) == 1) & (32 <= ((tl.program_id(0) // 50176) % 224))) & (((tl.program_id(0) // 50176) % 224) < 64))) | (((((_lv0 * 4) + tl.arange(0, 4)) == 2) & (64 <= ((tl.program_id(0) // 50176) % 224))) & (((tl.program_id(0) // 50176) % 224) < 96))) | (((((_lv0 * 4) + tl.arange(0, 4)) == 3) & (96 <= ((tl.program_id(0) // 50176) % 224))) & (((tl.program_id(0) // 50176) % 224) < 128))) | (((((_lv0 * 4) + tl.arange(0, 4)) == 4) & (128 <= ((tl.program_id(0) // 50176) % 224))) & (((tl.program_id(0) // 50176) % 224) < 160))) | (((((_lv0 * 4) + tl.arange(0, 4)) == 5) & (160 <= ((tl.program_id(0) // 50176) % 224))) & (((tl.program_id(0) // 50176) % 224) < 192))) | (((((_lv0 * 4) + tl.arange(0, 4)) == 6) & (192 <= ((tl.program_id(0) // 50176) % 224))) & (((tl.program_id(0) // 50176) % 224) < 224)))), other=0.0), tl.where((((_lv0 * 4) + tl.arange(0, 4))).to(tl.float32) <= (7.0 * (1.0 / 2.0)), tl.load(in38_ptr + (tl.maximum((((((((tl.program_id(0) // 11239424) * 32) + tl.maximum(((tl.program_id(0) // 50176) % 224) - 96, 0)) * 224) + ((tl.program_id(0) // 224) % 224)) * 224) + (tl.program_id(0) % 224)) - tl.maximum((((((((tl.program_id(0) // 11239424) * 32) + tl.maximum(((tl.program_id(0) // 50176) % 224) - 96, 0)) * 224) + ((tl.program_id(0) // 224) % 224)) * 224) + (tl.program_id(0) % 224)) - 16056319, 0), 0) + 0 * tl.arange(0, 4)), mask=((((_lv0 * 4) + tl.arange(0, 4)) < 7) & (((((((((((_lv0 * 4) + tl.arange(0, 4)) == 0) & (0 <= ((tl.program_id(0) // 50176) % 224))) & (((tl.program_id(0) // 50176) % 224) < 32)) | (((((_lv0 * 4) + tl.arange(0, 4)) == 1) & (32 <= ((tl.program_id(0) // 50176) % 224))) & (((tl.program_id(0) // 50176) % 224) < 64))) | (((((_lv0 * 4) + tl.arange(0, 4)) == 2) & (64 <= ((tl.program_id(0) // 50176) % 224))) & (((tl.program_id(0) // 50176) % 224) < 96))) | (((((_lv0 * 4) + tl.arange(0, 4)) == 3) & (96 <= ((tl.program_id(0) // 50176) % 224))) & (((tl.program_id(0) // 50176) % 224) < 128))) | (((((_lv0 * 4) + tl.arange(0, 4)) == 4) & (128 <= ((tl.program_id(0) // 50176) % 224))) & (((tl.program_id(0) // 50176) % 224) < 160))) | (((((_lv0 * 4) + tl.arange(0, 4)) == 5) & (160 <= ((tl.program_id(0) // 50176) % 224))) & (((tl.program_id(0) // 50176) % 224) < 192))) | (((((_lv0 * 4) + tl.arange(0, 4)) == 6) & (192 <= ((tl.program_id(0) // 50176) % 224))) & (((tl.program_id(0) // 50176) % 224) < 224)))), other=0.0), tl.where((((_lv0 * 4) + tl.arange(0, 4))).to(tl.float32) <= (9.0 * (1.0 / 2.0)), tl.load(in45_ptr + (tl.maximum((((((((tl.program_id(0) // 11239424) * 32) + tl.maximum(((tl.program_id(0) // 50176) % 224) - 128, 0)) * 224) + ((tl.program_id(0) // 224) % 224)) * 224) + (tl.program_id(0) % 224)) - tl.maximum((((((((tl.program_id(0) // 11239424) * 32) + tl.maximum(((tl.program_id(0) // 50176) % 224) - 128, 0)) * 224) + ((tl.program_id(0) // 224) % 224)) * 224) + (tl.program_id(0) % 224)) - 16056319, 0), 0) + 0 * tl.arange(0, 4)), mask=((((_lv0 * 4) + tl.arange(0, 4)) < 7) & (((((((((((_lv0 * 4) + tl.arange(0, 4)) == 0) & (0 <= ((tl.program_id(0) // 50176) % 224))) & (((tl.program_id(0) // 50176) % 224) < 32)) | (((((_lv0 * 4) + tl.arange(0, 4)) == 1) & (32 <= ((tl.program_id(0) // 50176) % 224))) & (((tl.program_id(0) // 50176) % 224) < 64))) | (((((_lv0 * 4) + tl.arange(0, 4)) == 2) & (64 <= ((tl.program_id(0) // 50176) % 224))) & (((tl.program_id(0) // 50176) % 224) < 96))) | (((((_lv0 * 4) + tl.arange(0, 4)) == 3) & (96 <= ((tl.program_id(0) // 50176) % 224))) & (((tl.program_id(0) // 50176) % 224) < 128))) | (((((_lv0 * 4) + tl.arange(0, 4)) == 4) & (128 <= ((tl.program_id(0) // 50176) % 224))) & (((tl.program_id(0) // 50176) % 224) < 160))) | (((((_lv0 * 4) + tl.arange(0, 4)) == 5) & (160 <= ((tl.program_id(0) // 50176) % 224))) & (((tl.program_id(0) // 50176) % 224) < 192))) | (((((_lv0 * 4) + tl.arange(0, 4)) == 6) & (192 <= ((tl.program_id(0) // 50176) % 224))) & (((tl.program_id(0) // 50176) % 224) < 224)))), other=0.0), tl.where((((_lv0 * 4) + tl.arange(0, 4))).to(tl.float32) <= (11.0 * (1.0 / 2.0)), tl.load(in52_ptr + (tl.maximum((((((((tl.program_id(0) // 11239424) * 32) + tl.maximum(((tl.program_id(0) // 50176) % 224) - 160, 0)) * 224) + ((tl.program_id(0) // 224) % 224)) * 224) + (tl.program_id(0) % 224)) - tl.maximum((((((((tl.program_id(0) // 11239424) * 32) + tl.maximum(((tl.program_id(0) // 50176) % 224) - 160, 0)) * 224) + ((tl.program_id(0) // 224) % 224)) * 224) + (tl.program_id(0) % 224)) - 16056319, 0), 0) + 0 * tl.arange(0, 4)), mask=((((_lv0 * 4) + tl.arange(0, 4)) < 7) & (((((((((((_lv0 * 4) + tl.arange(0, 4)) == 0) & (0 <= ((tl.program_id(0) // 50176) % 224))) & (((tl.program_id(0) // 50176) % 224) < 32)) | (((((_lv0 * 4) + tl.arange(0, 4)) == 1) & (32 <= ((tl.program_id(0) // 50176) % 224))) & (((tl.program_id(0) // 50176) % 224) < 64))) | (((((_lv0 * 4) + tl.arange(0, 4)) == 2) & (64 <= ((tl.program_id(0) // 50176) % 224))) & (((tl.program_id(0) // 50176) % 224) < 96))) | (((((_lv0 * 4) + tl.arange(0, 4)) == 3) & (96 <= ((tl.program_id(0) // 50176) % 224))) & (((tl.program_id(0) // 50176) % 224) < 128))) | (((((_lv0 * 4) + tl.arange(0, 4)) == 4) & (128 <= ((tl.program_id(0) // 50176) % 224))) & (((tl.program_id(0) // 50176) % 224) < 160))) | (((((_lv0 * 4) + tl.arange(0, 4)) == 5) & (160 <= ((tl.program_id(0) // 50176) % 224))) & (((tl.program_id(0) // 50176) % 224) < 192))) | (((((_lv0 * 4) + tl.arange(0, 4)) == 6) & (192 <= ((tl.program_id(0) // 50176) % 224))) & (((tl.program_id(0) // 50176) % 224) < 224)))), other=0.0), tl.load(in59_ptr + (tl.maximum((((((((tl.program_id(0) // 11239424) * 32) + tl.maximum(((tl.program_id(0) // 50176) % 224) - 192, 0)) * 224) + ((tl.program_id(0) // 224) % 224)) * 224) + (tl.program_id(0) % 224)) - tl.maximum((((((((tl.program_id(0) // 11239424) * 32) + tl.maximum(((tl.program_id(0) // 50176) % 224) - 192, 0)) * 224) + ((tl.program_id(0) // 224) % 224)) * 224) + (tl.program_id(0) % 224)) - 16056319, 0), 0) + 0 * tl.arange(0, 4)), mask=((((_lv0 * 4) + tl.arange(0, 4)) < 7) & (((((((((((_lv0 * 4) + tl.arange(0, 4)) == 0) & (0 <= ((tl.program_id(0) // 50176) % 224))) & (((tl.program_id(0) // 50176) % 224) < 32)) | (((((_lv0 * 4) + tl.arange(0, 4)) == 1) & (32 <= ((tl.program_id(0) // 50176) % 224))) & (((tl.program_id(0) // 50176) % 224) < 64))) | (((((_lv0 * 4) + tl.arange(0, 4)) == 2) & (64 <= ((tl.program_id(0) // 50176) % 224))) & (((tl.program_id(0) // 50176) % 224) < 96))) | (((((_lv0 * 4) + tl.arange(0, 4)) == 3) & (96 <= ((tl.program_id(0) // 50176) % 224))) & (((tl.program_id(0) // 50176) % 224) < 128))) | (((((_lv0 * 4) + tl.arange(0, 4)) == 4) & (128 <= ((tl.program_id(0) // 50176) % 224))) & (((tl.program_id(0) // 50176) % 224) < 160))) | (((((_lv0 * 4) + tl.arange(0, 4)) == 5) & (160 <= ((tl.program_id(0) // 50176) % 224))) & (((tl.program_id(0) // 50176) % 224) < 192))) | (((((_lv0 * 4) + tl.arange(0, 4)) == 6) & (192 <= ((tl.program_id(0) // 50176) % 224))) & (((tl.program_id(0) // 50176) % 224) < 224)))), other=0.0))))))), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t014_s41(out, ins):
    grid = (112394240,)
    t014_s41_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37], ins[38], ins[39], ins[40], ins[41], ins[42], ins[43], ins[44], ins[45], ins[46], ins[47], ins[48], ins[49], ins[50], ins[51], ins[52], ins[53], ins[54], ins[55], ins[56], ins[57], ins[58], ins[59])
    return out


def t014(out, ins):
    _t0 = torch.empty(8192, device=ins[0].device, dtype=torch.float32)
    _t1 = torch.empty(32, device=ins[0].device, dtype=torch.float32)
    _t2 = torch.empty(8192, device=ins[0].device, dtype=torch.float32)
    _t3 = torch.empty(32, device=ins[0].device, dtype=torch.float32)
    _t4 = torch.empty(16056320, device=ins[0].device, dtype=torch.float32)
    _t5 = torch.empty(16056320, device=ins[0].device, dtype=torch.float32)
    _t6 = torch.empty(32112640, device=ins[0].device, dtype=torch.float32)
    _t7 = torch.empty(16384, device=ins[0].device, dtype=torch.float32)
    _t8 = torch.empty(64, device=ins[0].device, dtype=torch.float32)
    _t9 = torch.empty(16384, device=ins[0].device, dtype=torch.float32)
    _t10 = torch.empty(64, device=ins[0].device, dtype=torch.float32)
    _t11 = torch.empty(32112640, device=ins[0].device, dtype=torch.float32)
    _t12 = torch.empty(16056320, device=ins[0].device, dtype=torch.float32)
    _t13 = torch.empty(48168960, device=ins[0].device, dtype=torch.float32)
    _t14 = torch.empty(24576, device=ins[0].device, dtype=torch.float32)
    _t15 = torch.empty(96, device=ins[0].device, dtype=torch.float32)
    _t16 = torch.empty(24576, device=ins[0].device, dtype=torch.float32)
    _t17 = torch.empty(96, device=ins[0].device, dtype=torch.float32)
    _t18 = torch.empty(48168960, device=ins[0].device, dtype=torch.float32)
    _t19 = torch.empty(16056320, device=ins[0].device, dtype=torch.float32)
    _t20 = torch.empty(64225280, device=ins[0].device, dtype=torch.float32)
    _t21 = torch.empty(32768, device=ins[0].device, dtype=torch.float32)
    _t22 = torch.empty(128, device=ins[0].device, dtype=torch.float32)
    _t23 = torch.empty(32768, device=ins[0].device, dtype=torch.float32)
    _t24 = torch.empty(128, device=ins[0].device, dtype=torch.float32)
    _t25 = torch.empty(64225280, device=ins[0].device, dtype=torch.float32)
    _t26 = torch.empty(16056320, device=ins[0].device, dtype=torch.float32)
    _t27 = torch.empty(80281600, device=ins[0].device, dtype=torch.float32)
    _t28 = torch.empty(40960, device=ins[0].device, dtype=torch.float32)
    _t29 = torch.empty(160, device=ins[0].device, dtype=torch.float32)
    _t30 = torch.empty(40960, device=ins[0].device, dtype=torch.float32)
    _t31 = torch.empty(160, device=ins[0].device, dtype=torch.float32)
    _t32 = torch.empty(80281600, device=ins[0].device, dtype=torch.float32)
    _t33 = torch.empty(16056320, device=ins[0].device, dtype=torch.float32)
    _t34 = torch.empty(96337920, device=ins[0].device, dtype=torch.float32)
    _t35 = torch.empty(49152, device=ins[0].device, dtype=torch.float32)
    _t36 = torch.empty(192, device=ins[0].device, dtype=torch.float32)
    _t37 = torch.empty(49152, device=ins[0].device, dtype=torch.float32)
    _t38 = torch.empty(192, device=ins[0].device, dtype=torch.float32)
    _t39 = torch.empty(96337920, device=ins[0].device, dtype=torch.float32)
    _t40 = torch.empty(16056320, device=ins[0].device, dtype=torch.float32)
    t014_s0(_t0, list(ins))
    t014_s1(_t1, list(ins) + [_t0])
    t014_s2(_t2, list(ins) + [_t0, _t1])
    t014_s3(_t3, list(ins) + [_t0, _t1, _t2])
    t014_s4(_t4, list(ins) + [_t0, _t1, _t2, _t3])
    t014_s5(_t5, list(ins) + [_t0, _t1, _t2, _t3, _t4])
    t014_s6(_t6, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5])
    t014_s7(_t7, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6])
    t014_s8(_t8, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7])
    t014_s9(_t9, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8])
    t014_s10(_t10, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9])
    t014_s11(_t11, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10])
    t014_s12(_t12, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11])
    t014_s13(_t13, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12])
    t014_s14(_t14, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13])
    t014_s15(_t15, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13, _t14])
    t014_s16(_t16, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13, _t14, _t15])
    t014_s17(_t17, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13, _t14, _t15, _t16])
    t014_s18(_t18, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13, _t14, _t15, _t16, _t17])
    t014_s19(_t19, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13, _t14, _t15, _t16, _t17, _t18])
    t014_s20(_t20, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13, _t14, _t15, _t16, _t17, _t18, _t19])
    t014_s21(_t21, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13, _t14, _t15, _t16, _t17, _t18, _t19, _t20])
    t014_s22(_t22, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13, _t14, _t15, _t16, _t17, _t18, _t19, _t20, _t21])
    t014_s23(_t23, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13, _t14, _t15, _t16, _t17, _t18, _t19, _t20, _t21, _t22])
    t014_s24(_t24, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13, _t14, _t15, _t16, _t17, _t18, _t19, _t20, _t21, _t22, _t23])
    t014_s25(_t25, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13, _t14, _t15, _t16, _t17, _t18, _t19, _t20, _t21, _t22, _t23, _t24])
    t014_s26(_t26, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13, _t14, _t15, _t16, _t17, _t18, _t19, _t20, _t21, _t22, _t23, _t24, _t25])
    t014_s27(_t27, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13, _t14, _t15, _t16, _t17, _t18, _t19, _t20, _t21, _t22, _t23, _t24, _t25, _t26])
    t014_s28(_t28, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13, _t14, _t15, _t16, _t17, _t18, _t19, _t20, _t21, _t22, _t23, _t24, _t25, _t26, _t27])
    t014_s29(_t29, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13, _t14, _t15, _t16, _t17, _t18, _t19, _t20, _t21, _t22, _t23, _t24, _t25, _t26, _t27, _t28])
    t014_s30(_t30, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13, _t14, _t15, _t16, _t17, _t18, _t19, _t20, _t21, _t22, _t23, _t24, _t25, _t26, _t27, _t28, _t29])
    t014_s31(_t31, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13, _t14, _t15, _t16, _t17, _t18, _t19, _t20, _t21, _t22, _t23, _t24, _t25, _t26, _t27, _t28, _t29, _t30])
    t014_s32(_t32, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13, _t14, _t15, _t16, _t17, _t18, _t19, _t20, _t21, _t22, _t23, _t24, _t25, _t26, _t27, _t28, _t29, _t30, _t31])
    t014_s33(_t33, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13, _t14, _t15, _t16, _t17, _t18, _t19, _t20, _t21, _t22, _t23, _t24, _t25, _t26, _t27, _t28, _t29, _t30, _t31, _t32])
    t014_s34(_t34, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13, _t14, _t15, _t16, _t17, _t18, _t19, _t20, _t21, _t22, _t23, _t24, _t25, _t26, _t27, _t28, _t29, _t30, _t31, _t32, _t33])
    t014_s35(_t35, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13, _t14, _t15, _t16, _t17, _t18, _t19, _t20, _t21, _t22, _t23, _t24, _t25, _t26, _t27, _t28, _t29, _t30, _t31, _t32, _t33, _t34])
    t014_s36(_t36, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13, _t14, _t15, _t16, _t17, _t18, _t19, _t20, _t21, _t22, _t23, _t24, _t25, _t26, _t27, _t28, _t29, _t30, _t31, _t32, _t33, _t34, _t35])
    t014_s37(_t37, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13, _t14, _t15, _t16, _t17, _t18, _t19, _t20, _t21, _t22, _t23, _t24, _t25, _t26, _t27, _t28, _t29, _t30, _t31, _t32, _t33, _t34, _t35, _t36])
    t014_s38(_t38, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13, _t14, _t15, _t16, _t17, _t18, _t19, _t20, _t21, _t22, _t23, _t24, _t25, _t26, _t27, _t28, _t29, _t30, _t31, _t32, _t33, _t34, _t35, _t36, _t37])
    t014_s39(_t39, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13, _t14, _t15, _t16, _t17, _t18, _t19, _t20, _t21, _t22, _t23, _t24, _t25, _t26, _t27, _t28, _t29, _t30, _t31, _t32, _t33, _t34, _t35, _t36, _t37, _t38])
    t014_s40(_t40, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13, _t14, _t15, _t16, _t17, _t18, _t19, _t20, _t21, _t22, _t23, _t24, _t25, _t26, _t27, _t28, _t29, _t30, _t31, _t32, _t33, _t34, _t35, _t36, _t37, _t38, _t39])
    t014_s41(out, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13, _t14, _t15, _t16, _t17, _t18, _t19, _t20, _t21, _t22, _t23, _t24, _t25, _t26, _t27, _t28, _t29, _t30, _t31, _t32, _t33, _t34, _t35, _t36, _t37, _t38, _t39, _t40])
    return out
