import torch
import triton
import triton.language as tl


@triton.jit
def _mul_combine(a, b):
    return a * b


@triton.jit
def t024_s0_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr, in38_ptr, in39_ptr, in40_ptr, in41_ptr, in42_ptr, in43_ptr, in44_ptr, in45_ptr, in46_ptr, in47_ptr, in48_ptr, in49_ptr, in50_ptr, in51_ptr, in52_ptr, in53_ptr, in54_ptr, in55_ptr, in56_ptr, in57_ptr, in58_ptr, in59_ptr, in60_ptr, in61_ptr, in62_ptr, in63_ptr):
    _acc0 = tl.zeros([16], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 16) + tl.arange(0, 16)) < 27) & ((((1 <= ((((tl.program_id(0) // 112) % 112) * 2) + ((((_lv0 * 16) + tl.arange(0, 16)) // 3) % 3))) & (((((tl.program_id(0) // 112) % 112) * 2) + ((((_lv0 * 16) + tl.arange(0, 16)) // 3) % 3)) < 225)) & (1 <= (((tl.program_id(0) % 112) * 2) + (((_lv0 * 16) + tl.arange(0, 16)) % 3)))) & ((((tl.program_id(0) % 112) * 2) + (((_lv0 * 16) + tl.arange(0, 16)) % 3)) < 225))), (tl.load(in0_ptr + ((((((((tl.program_id(0) // 401408) * 3) + (((_lv0 * 16) + tl.arange(0, 16)) // 9)) * 224) + tl.maximum(((((tl.program_id(0) // 112) % 112) * 2) + ((((_lv0 * 16) + tl.arange(0, 16)) // 3) % 3)) - 1, 0)) * 224) + tl.maximum((((tl.program_id(0) % 112) * 2) + (((_lv0 * 16) + tl.arange(0, 16)) % 3)) - 1, 0)) + 0 * tl.arange(0, 16)), mask=((((_lv0 * 16) + tl.arange(0, 16)) < 27) & ((((1 <= ((((tl.program_id(0) // 112) % 112) * 2) + ((((_lv0 * 16) + tl.arange(0, 16)) // 3) % 3))) & (((((tl.program_id(0) // 112) % 112) * 2) + ((((_lv0 * 16) + tl.arange(0, 16)) // 3) % 3)) < 225)) & (1 <= (((tl.program_id(0) % 112) * 2) + (((_lv0 * 16) + tl.arange(0, 16)) % 3)))) & ((((tl.program_id(0) % 112) * 2) + (((_lv0 * 16) + tl.arange(0, 16)) % 3)) < 225))), other=0.0) * tl.load(in1_ptr + (((((((((tl.program_id(0) // 12544) % 32) * 3) + (((_lv0 * 16) + tl.arange(0, 16)) // 9)) * 3) + ((((_lv0 * 16) + tl.arange(0, 16)) // 3) % 3)) * 3) + (((_lv0 * 16) + tl.arange(0, 16)) % 3)) + 0 * tl.arange(0, 16)), mask=((((_lv0 * 16) + tl.arange(0, 16)) < 27) & ((((1 <= ((((tl.program_id(0) // 112) % 112) * 2) + ((((_lv0 * 16) + tl.arange(0, 16)) // 3) % 3))) & (((((tl.program_id(0) // 112) % 112) * 2) + ((((_lv0 * 16) + tl.arange(0, 16)) // 3) % 3)) < 225)) & (1 <= (((tl.program_id(0) % 112) * 2) + (((_lv0 * 16) + tl.arange(0, 16)) % 3)))) & ((((tl.program_id(0) % 112) * 2) + (((_lv0 * 16) + tl.arange(0, 16)) % 3)) < 225))), other=0.0)), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t024_s0(out, ins):
    grid = (802816,)
    t024_s0_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37], ins[38], ins[39], ins[40], ins[41], ins[42], ins[43], ins[44], ins[45], ins[46], ins[47], ins[48], ins[49], ins[50], ins[51], ins[52], ins[53], ins[54], ins[55], ins[56], ins[57], ins[58], ins[59], ins[60], ins[61], ins[62], ins[63])
    return out


@triton.jit
def t024_s1_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr, in38_ptr, in39_ptr, in40_ptr, in41_ptr, in42_ptr, in43_ptr, in44_ptr, in45_ptr, in46_ptr, in47_ptr, in48_ptr, in49_ptr, in50_ptr, in51_ptr, in52_ptr, in53_ptr, in54_ptr, in55_ptr, in56_ptr, in57_ptr, in58_ptr, in59_ptr, in60_ptr, in61_ptr, in62_ptr, in63_ptr, in64_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 25):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 25088) & True), tl.load(in64_ptr + (tl.maximum((((((((_lv0 * 1024) + tl.arange(0, 1024)) // 12544) * 32) + tl.program_id(0)) * 12544) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 12544)) - tl.maximum((((((((_lv0 * 1024) + tl.arange(0, 1024)) // 12544) * 32) + tl.program_id(0)) * 12544) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 12544)) - 802815, 0), 0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 25088) & True), other=0.0), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t024_s1(out, ins):
    grid = (32,)
    t024_s1_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37], ins[38], ins[39], ins[40], ins[41], ins[42], ins[43], ins[44], ins[45], ins[46], ins[47], ins[48], ins[49], ins[50], ins[51], ins[52], ins[53], ins[54], ins[55], ins[56], ins[57], ins[58], ins[59], ins[60], ins[61], ins[62], ins[63], ins[64])
    return out


@triton.jit
def t024_s2_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr, in38_ptr, in39_ptr, in40_ptr, in41_ptr, in42_ptr, in43_ptr, in44_ptr, in45_ptr, in46_ptr, in47_ptr, in48_ptr, in49_ptr, in50_ptr, in51_ptr, in52_ptr, in53_ptr, in54_ptr, in55_ptr, in56_ptr, in57_ptr, in58_ptr, in59_ptr, in60_ptr, in61_ptr, in62_ptr, in63_ptr, in64_ptr, in65_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 25):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 25088) & True), ((tl.load(in64_ptr + (tl.maximum((((((((_lv0 * 1024) + tl.arange(0, 1024)) // 12544) * 32) + tl.program_id(0)) * 12544) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 12544)) - tl.maximum((((((((_lv0 * 1024) + tl.arange(0, 1024)) // 12544) * 32) + tl.program_id(0)) * 12544) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 12544)) - 802815, 0), 0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 25088) & True), other=0.0) - (tl.load(in65_ptr + (tl.program_id(0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 25088) & True), other=0.0) * (1.0 * (1.0 / 25088.0)))) * (tl.load(in64_ptr + (tl.maximum((((((((_lv0 * 1024) + tl.arange(0, 1024)) // 12544) * 32) + tl.program_id(0)) * 12544) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 12544)) - tl.maximum((((((((_lv0 * 1024) + tl.arange(0, 1024)) // 12544) * 32) + tl.program_id(0)) * 12544) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 12544)) - 802815, 0), 0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 25088) & True), other=0.0) - (tl.load(in65_ptr + (tl.program_id(0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 25088) & True), other=0.0) * (1.0 * (1.0 / 25088.0))))), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t024_s2(out, ins):
    grid = (32,)
    t024_s2_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37], ins[38], ins[39], ins[40], ins[41], ins[42], ins[43], ins[44], ins[45], ins[46], ins[47], ins[48], ins[49], ins[50], ins[51], ins[52], ins[53], ins[54], ins[55], ins[56], ins[57], ins[58], ins[59], ins[60], ins[61], ins[62], ins[63], ins[64], ins[65])
    return out


@triton.jit
def t024_s3_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr, in38_ptr, in39_ptr, in40_ptr, in41_ptr, in42_ptr, in43_ptr, in44_ptr, in45_ptr, in46_ptr, in47_ptr, in48_ptr, in49_ptr, in50_ptr, in51_ptr, in52_ptr, in53_ptr, in54_ptr, in55_ptr, in56_ptr, in57_ptr, in58_ptr, in59_ptr, in60_ptr, in61_ptr, in62_ptr, in63_ptr, in64_ptr, in65_ptr, in66_ptr):
    _acc0 = tl.zeros([1], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), ((((tl.load(in64_ptr + (tl.program_id(0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) - (tl.load(in65_ptr + (tl.maximum(((tl.program_id(0) // 12544) % 32) - tl.maximum(((tl.program_id(0) // 12544) % 32) - 31, 0), 0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) * (1.0 * (1.0 / 25088.0)))) * (1.0 / tl.sqrt(((tl.load(in66_ptr + (tl.maximum(((tl.program_id(0) // 12544) % 32) - tl.maximum(((tl.program_id(0) // 12544) % 32) - 31, 0), 0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) * (1.0 * (1.0 / 25088.0))) + (1.0 * (1.0 / 100000.0)))))) * tl.load(in2_ptr + (((tl.program_id(0) // 12544) % 32) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)) + tl.load(in3_ptr + (((tl.program_id(0) // 12544) % 32) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)), 0.0))
    _v = tl.maximum(tl.sum(_acc0, axis=0), (0.0 * (1.0 / 1.0)))
    tl.store(out_ptr + tl.program_id(0), _v)


def t024_s3(out, ins):
    grid = (802816,)
    t024_s3_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37], ins[38], ins[39], ins[40], ins[41], ins[42], ins[43], ins[44], ins[45], ins[46], ins[47], ins[48], ins[49], ins[50], ins[51], ins[52], ins[53], ins[54], ins[55], ins[56], ins[57], ins[58], ins[59], ins[60], ins[61], ins[62], ins[63], ins[64], ins[65], ins[66])
    return out


@triton.jit
def t024_s4_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr, in38_ptr, in39_ptr, in40_ptr, in41_ptr, in42_ptr, in43_ptr, in44_ptr, in45_ptr, in46_ptr, in47_ptr, in48_ptr, in49_ptr, in50_ptr, in51_ptr, in52_ptr, in53_ptr, in54_ptr, in55_ptr, in56_ptr, in57_ptr, in58_ptr, in59_ptr, in60_ptr, in61_ptr, in62_ptr, in63_ptr, in64_ptr, in65_ptr, in66_ptr, in67_ptr):
    _acc0 = tl.zeros([32], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 32) + tl.arange(0, 32)) < 32) & ((((tl.program_id(0) // 112) % 112) < 112) & ((tl.program_id(0) % 112) < 112))), (tl.load(in67_ptr + ((((((((tl.program_id(0) // 1204224) * 32) + ((_lv0 * 32) + tl.arange(0, 32))) * 112) + ((tl.program_id(0) // 112) % 112)) * 112) + (tl.program_id(0) % 112)) + 0 * tl.arange(0, 32)), mask=((((_lv0 * 32) + tl.arange(0, 32)) < 32) & ((((tl.program_id(0) // 112) % 112) < 112) & ((tl.program_id(0) % 112) < 112))), other=0.0) * tl.load(in4_ptr + (((((tl.program_id(0) // 12544) % 96) * 32) + ((_lv0 * 32) + tl.arange(0, 32))) + 0 * tl.arange(0, 32)), mask=((((_lv0 * 32) + tl.arange(0, 32)) < 32) & ((((tl.program_id(0) // 112) % 112) < 112) & ((tl.program_id(0) % 112) < 112))), other=0.0)), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t024_s4(out, ins):
    grid = (2408448,)
    t024_s4_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37], ins[38], ins[39], ins[40], ins[41], ins[42], ins[43], ins[44], ins[45], ins[46], ins[47], ins[48], ins[49], ins[50], ins[51], ins[52], ins[53], ins[54], ins[55], ins[56], ins[57], ins[58], ins[59], ins[60], ins[61], ins[62], ins[63], ins[64], ins[65], ins[66], ins[67])
    return out


@triton.jit
def t024_s5_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr, in38_ptr, in39_ptr, in40_ptr, in41_ptr, in42_ptr, in43_ptr, in44_ptr, in45_ptr, in46_ptr, in47_ptr, in48_ptr, in49_ptr, in50_ptr, in51_ptr, in52_ptr, in53_ptr, in54_ptr, in55_ptr, in56_ptr, in57_ptr, in58_ptr, in59_ptr, in60_ptr, in61_ptr, in62_ptr, in63_ptr, in64_ptr, in65_ptr, in66_ptr, in67_ptr, in68_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 25):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 25088) & True), tl.load(in68_ptr + (tl.maximum((((((((_lv0 * 1024) + tl.arange(0, 1024)) // 12544) * 96) + tl.program_id(0)) * 12544) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 12544)) - tl.maximum((((((((_lv0 * 1024) + tl.arange(0, 1024)) // 12544) * 96) + tl.program_id(0)) * 12544) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 12544)) - 2408447, 0), 0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 25088) & True), other=0.0), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t024_s5(out, ins):
    grid = (96,)
    t024_s5_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37], ins[38], ins[39], ins[40], ins[41], ins[42], ins[43], ins[44], ins[45], ins[46], ins[47], ins[48], ins[49], ins[50], ins[51], ins[52], ins[53], ins[54], ins[55], ins[56], ins[57], ins[58], ins[59], ins[60], ins[61], ins[62], ins[63], ins[64], ins[65], ins[66], ins[67], ins[68])
    return out


@triton.jit
def t024_s6_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr, in38_ptr, in39_ptr, in40_ptr, in41_ptr, in42_ptr, in43_ptr, in44_ptr, in45_ptr, in46_ptr, in47_ptr, in48_ptr, in49_ptr, in50_ptr, in51_ptr, in52_ptr, in53_ptr, in54_ptr, in55_ptr, in56_ptr, in57_ptr, in58_ptr, in59_ptr, in60_ptr, in61_ptr, in62_ptr, in63_ptr, in64_ptr, in65_ptr, in66_ptr, in67_ptr, in68_ptr, in69_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 25):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 25088) & True), ((tl.load(in68_ptr + (tl.maximum((((((((_lv0 * 1024) + tl.arange(0, 1024)) // 12544) * 96) + tl.program_id(0)) * 12544) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 12544)) - tl.maximum((((((((_lv0 * 1024) + tl.arange(0, 1024)) // 12544) * 96) + tl.program_id(0)) * 12544) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 12544)) - 2408447, 0), 0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 25088) & True), other=0.0) - (tl.load(in69_ptr + (tl.program_id(0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 25088) & True), other=0.0) * (1.0 * (1.0 / 25088.0)))) * (tl.load(in68_ptr + (tl.maximum((((((((_lv0 * 1024) + tl.arange(0, 1024)) // 12544) * 96) + tl.program_id(0)) * 12544) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 12544)) - tl.maximum((((((((_lv0 * 1024) + tl.arange(0, 1024)) // 12544) * 96) + tl.program_id(0)) * 12544) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 12544)) - 2408447, 0), 0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 25088) & True), other=0.0) - (tl.load(in69_ptr + (tl.program_id(0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 25088) & True), other=0.0) * (1.0 * (1.0 / 25088.0))))), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t024_s6(out, ins):
    grid = (96,)
    t024_s6_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37], ins[38], ins[39], ins[40], ins[41], ins[42], ins[43], ins[44], ins[45], ins[46], ins[47], ins[48], ins[49], ins[50], ins[51], ins[52], ins[53], ins[54], ins[55], ins[56], ins[57], ins[58], ins[59], ins[60], ins[61], ins[62], ins[63], ins[64], ins[65], ins[66], ins[67], ins[68], ins[69])
    return out


@triton.jit
def t024_s7_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr, in38_ptr, in39_ptr, in40_ptr, in41_ptr, in42_ptr, in43_ptr, in44_ptr, in45_ptr, in46_ptr, in47_ptr, in48_ptr, in49_ptr, in50_ptr, in51_ptr, in52_ptr, in53_ptr, in54_ptr, in55_ptr, in56_ptr, in57_ptr, in58_ptr, in59_ptr, in60_ptr, in61_ptr, in62_ptr, in63_ptr, in64_ptr, in65_ptr, in66_ptr, in67_ptr, in68_ptr, in69_ptr, in70_ptr):
    _acc0 = tl.zeros([1], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), ((((tl.load(in68_ptr + (tl.program_id(0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) - (tl.load(in69_ptr + (tl.maximum(((tl.program_id(0) // 12544) % 96) - tl.maximum(((tl.program_id(0) // 12544) % 96) - 95, 0), 0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) * (1.0 * (1.0 / 25088.0)))) * (1.0 / tl.sqrt(((tl.load(in70_ptr + (tl.maximum(((tl.program_id(0) // 12544) % 96) - tl.maximum(((tl.program_id(0) // 12544) % 96) - 95, 0), 0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) * (1.0 * (1.0 / 25088.0))) + (1.0 * (1.0 / 100000.0)))))) * tl.load(in5_ptr + (((tl.program_id(0) // 12544) % 96) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)) + tl.load(in6_ptr + (((tl.program_id(0) // 12544) % 96) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)), 0.0))
    _v = tl.maximum(tl.sum(_acc0, axis=0), (0.0 * (1.0 / 1.0)))
    tl.store(out_ptr + tl.program_id(0), _v)


def t024_s7(out, ins):
    grid = (2408448,)
    t024_s7_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37], ins[38], ins[39], ins[40], ins[41], ins[42], ins[43], ins[44], ins[45], ins[46], ins[47], ins[48], ins[49], ins[50], ins[51], ins[52], ins[53], ins[54], ins[55], ins[56], ins[57], ins[58], ins[59], ins[60], ins[61], ins[62], ins[63], ins[64], ins[65], ins[66], ins[67], ins[68], ins[69], ins[70])
    return out


@triton.jit
def t024_s8_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr, in38_ptr, in39_ptr, in40_ptr, in41_ptr, in42_ptr, in43_ptr, in44_ptr, in45_ptr, in46_ptr, in47_ptr, in48_ptr, in49_ptr, in50_ptr, in51_ptr, in52_ptr, in53_ptr, in54_ptr, in55_ptr, in56_ptr, in57_ptr, in58_ptr, in59_ptr, in60_ptr, in61_ptr, in62_ptr, in63_ptr, in64_ptr, in65_ptr, in66_ptr, in67_ptr, in68_ptr, in69_ptr, in70_ptr, in71_ptr):
    _acc0 = tl.zeros([8], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 8) + tl.arange(0, 8)) < 9) & ((((1 <= (((tl.program_id(0) // 112) % 112) + ((((_lv0 * 8) + tl.arange(0, 8)) // 3) % 3))) & ((((tl.program_id(0) // 112) % 112) + ((((_lv0 * 8) + tl.arange(0, 8)) // 3) % 3)) < 113)) & (1 <= ((tl.program_id(0) % 112) + (((_lv0 * 8) + tl.arange(0, 8)) % 3)))) & (((tl.program_id(0) % 112) + (((_lv0 * 8) + tl.arange(0, 8)) % 3)) < 113))), (tl.load(in71_ptr + (tl.maximum((((((((tl.program_id(0) // 1204224) * 96) + ((tl.program_id(0) // 12544) % 96)) * 112) + tl.maximum((((tl.program_id(0) // 112) % 112) + ((((_lv0 * 8) + tl.arange(0, 8)) // 3) % 3)) - 1, 0)) * 112) + tl.maximum(((tl.program_id(0) % 112) + (((_lv0 * 8) + tl.arange(0, 8)) % 3)) - 1, 0)) - tl.maximum((((((((tl.program_id(0) // 1204224) * 96) + ((tl.program_id(0) // 12544) % 96)) * 112) + tl.maximum((((tl.program_id(0) // 112) % 112) + ((((_lv0 * 8) + tl.arange(0, 8)) // 3) % 3)) - 1, 0)) * 112) + tl.maximum(((tl.program_id(0) % 112) + (((_lv0 * 8) + tl.arange(0, 8)) % 3)) - 1, 0)) - 2408447, 0), 0) + 0 * tl.arange(0, 8)), mask=((((_lv0 * 8) + tl.arange(0, 8)) < 9) & ((((1 <= (((tl.program_id(0) // 112) % 112) + ((((_lv0 * 8) + tl.arange(0, 8)) // 3) % 3))) & ((((tl.program_id(0) // 112) % 112) + ((((_lv0 * 8) + tl.arange(0, 8)) // 3) % 3)) < 113)) & (1 <= ((tl.program_id(0) % 112) + (((_lv0 * 8) + tl.arange(0, 8)) % 3)))) & (((tl.program_id(0) % 112) + (((_lv0 * 8) + tl.arange(0, 8)) % 3)) < 113))), other=0.0) * tl.load(in7_ptr + (((((((tl.program_id(0) // 12544) % 96) * 3) + ((((_lv0 * 8) + tl.arange(0, 8)) // 3) % 3)) * 3) + (((_lv0 * 8) + tl.arange(0, 8)) % 3)) + 0 * tl.arange(0, 8)), mask=((((_lv0 * 8) + tl.arange(0, 8)) < 9) & ((((1 <= (((tl.program_id(0) // 112) % 112) + ((((_lv0 * 8) + tl.arange(0, 8)) // 3) % 3))) & ((((tl.program_id(0) // 112) % 112) + ((((_lv0 * 8) + tl.arange(0, 8)) // 3) % 3)) < 113)) & (1 <= ((tl.program_id(0) % 112) + (((_lv0 * 8) + tl.arange(0, 8)) % 3)))) & (((tl.program_id(0) % 112) + (((_lv0 * 8) + tl.arange(0, 8)) % 3)) < 113))), other=0.0)), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t024_s8(out, ins):
    grid = (2408448,)
    t024_s8_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37], ins[38], ins[39], ins[40], ins[41], ins[42], ins[43], ins[44], ins[45], ins[46], ins[47], ins[48], ins[49], ins[50], ins[51], ins[52], ins[53], ins[54], ins[55], ins[56], ins[57], ins[58], ins[59], ins[60], ins[61], ins[62], ins[63], ins[64], ins[65], ins[66], ins[67], ins[68], ins[69], ins[70], ins[71])
    return out


@triton.jit
def t024_s9_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr, in38_ptr, in39_ptr, in40_ptr, in41_ptr, in42_ptr, in43_ptr, in44_ptr, in45_ptr, in46_ptr, in47_ptr, in48_ptr, in49_ptr, in50_ptr, in51_ptr, in52_ptr, in53_ptr, in54_ptr, in55_ptr, in56_ptr, in57_ptr, in58_ptr, in59_ptr, in60_ptr, in61_ptr, in62_ptr, in63_ptr, in64_ptr, in65_ptr, in66_ptr, in67_ptr, in68_ptr, in69_ptr, in70_ptr, in71_ptr, in72_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 25):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 25088) & True), tl.load(in72_ptr + (tl.maximum((((((((_lv0 * 1024) + tl.arange(0, 1024)) // 12544) * 96) + tl.program_id(0)) * 12544) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 12544)) - tl.maximum((((((((_lv0 * 1024) + tl.arange(0, 1024)) // 12544) * 96) + tl.program_id(0)) * 12544) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 12544)) - 2408447, 0), 0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 25088) & True), other=0.0), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t024_s9(out, ins):
    grid = (96,)
    t024_s9_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37], ins[38], ins[39], ins[40], ins[41], ins[42], ins[43], ins[44], ins[45], ins[46], ins[47], ins[48], ins[49], ins[50], ins[51], ins[52], ins[53], ins[54], ins[55], ins[56], ins[57], ins[58], ins[59], ins[60], ins[61], ins[62], ins[63], ins[64], ins[65], ins[66], ins[67], ins[68], ins[69], ins[70], ins[71], ins[72])
    return out


@triton.jit
def t024_s10_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr, in38_ptr, in39_ptr, in40_ptr, in41_ptr, in42_ptr, in43_ptr, in44_ptr, in45_ptr, in46_ptr, in47_ptr, in48_ptr, in49_ptr, in50_ptr, in51_ptr, in52_ptr, in53_ptr, in54_ptr, in55_ptr, in56_ptr, in57_ptr, in58_ptr, in59_ptr, in60_ptr, in61_ptr, in62_ptr, in63_ptr, in64_ptr, in65_ptr, in66_ptr, in67_ptr, in68_ptr, in69_ptr, in70_ptr, in71_ptr, in72_ptr, in73_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 25):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 25088) & True), ((tl.load(in72_ptr + (tl.maximum((((((((_lv0 * 1024) + tl.arange(0, 1024)) // 12544) * 96) + tl.program_id(0)) * 12544) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 12544)) - tl.maximum((((((((_lv0 * 1024) + tl.arange(0, 1024)) // 12544) * 96) + tl.program_id(0)) * 12544) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 12544)) - 2408447, 0), 0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 25088) & True), other=0.0) - (tl.load(in73_ptr + (tl.program_id(0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 25088) & True), other=0.0) * (1.0 * (1.0 / 25088.0)))) * (tl.load(in72_ptr + (tl.maximum((((((((_lv0 * 1024) + tl.arange(0, 1024)) // 12544) * 96) + tl.program_id(0)) * 12544) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 12544)) - tl.maximum((((((((_lv0 * 1024) + tl.arange(0, 1024)) // 12544) * 96) + tl.program_id(0)) * 12544) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 12544)) - 2408447, 0), 0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 25088) & True), other=0.0) - (tl.load(in73_ptr + (tl.program_id(0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 25088) & True), other=0.0) * (1.0 * (1.0 / 25088.0))))), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t024_s10(out, ins):
    grid = (96,)
    t024_s10_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37], ins[38], ins[39], ins[40], ins[41], ins[42], ins[43], ins[44], ins[45], ins[46], ins[47], ins[48], ins[49], ins[50], ins[51], ins[52], ins[53], ins[54], ins[55], ins[56], ins[57], ins[58], ins[59], ins[60], ins[61], ins[62], ins[63], ins[64], ins[65], ins[66], ins[67], ins[68], ins[69], ins[70], ins[71], ins[72], ins[73])
    return out


@triton.jit
def t024_s11_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr, in38_ptr, in39_ptr, in40_ptr, in41_ptr, in42_ptr, in43_ptr, in44_ptr, in45_ptr, in46_ptr, in47_ptr, in48_ptr, in49_ptr, in50_ptr, in51_ptr, in52_ptr, in53_ptr, in54_ptr, in55_ptr, in56_ptr, in57_ptr, in58_ptr, in59_ptr, in60_ptr, in61_ptr, in62_ptr, in63_ptr, in64_ptr, in65_ptr, in66_ptr, in67_ptr, in68_ptr, in69_ptr, in70_ptr, in71_ptr, in72_ptr, in73_ptr, in74_ptr):
    _acc0 = tl.zeros([1], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), ((((tl.load(in72_ptr + (tl.program_id(0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) - (tl.load(in73_ptr + (tl.maximum(((tl.program_id(0) // 12544) % 96) - tl.maximum(((tl.program_id(0) // 12544) % 96) - 95, 0), 0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) * (1.0 * (1.0 / 25088.0)))) * (1.0 / tl.sqrt(((tl.load(in74_ptr + (tl.maximum(((tl.program_id(0) // 12544) % 96) - tl.maximum(((tl.program_id(0) // 12544) % 96) - 95, 0), 0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) * (1.0 * (1.0 / 25088.0))) + (1.0 * (1.0 / 100000.0)))))) * tl.load(in8_ptr + (((tl.program_id(0) // 12544) % 96) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)) + tl.load(in9_ptr + (((tl.program_id(0) // 12544) % 96) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)), 0.0))
    _v = tl.maximum(tl.sum(_acc0, axis=0), (0.0 * (1.0 / 1.0)))
    tl.store(out_ptr + tl.program_id(0), _v)


def t024_s11(out, ins):
    grid = (2408448,)
    t024_s11_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37], ins[38], ins[39], ins[40], ins[41], ins[42], ins[43], ins[44], ins[45], ins[46], ins[47], ins[48], ins[49], ins[50], ins[51], ins[52], ins[53], ins[54], ins[55], ins[56], ins[57], ins[58], ins[59], ins[60], ins[61], ins[62], ins[63], ins[64], ins[65], ins[66], ins[67], ins[68], ins[69], ins[70], ins[71], ins[72], ins[73], ins[74])
    return out


@triton.jit
def t024_s12_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr, in38_ptr, in39_ptr, in40_ptr, in41_ptr, in42_ptr, in43_ptr, in44_ptr, in45_ptr, in46_ptr, in47_ptr, in48_ptr, in49_ptr, in50_ptr, in51_ptr, in52_ptr, in53_ptr, in54_ptr, in55_ptr, in56_ptr, in57_ptr, in58_ptr, in59_ptr, in60_ptr, in61_ptr, in62_ptr, in63_ptr, in64_ptr, in65_ptr, in66_ptr, in67_ptr, in68_ptr, in69_ptr, in70_ptr, in71_ptr, in72_ptr, in73_ptr, in74_ptr, in75_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 13):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 12544) & True), tl.load(in75_ptr + (((tl.program_id(0) * 12544) + ((_lv0 * 1024) + tl.arange(0, 1024))) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 12544) & True), other=0.0), 0.0))
    _v = (tl.sum(_acc0, axis=0) * (1.0 * (1.0 / 12544.0)))
    tl.store(out_ptr + tl.program_id(0), _v)


def t024_s12(out, ins):
    grid = (192,)
    t024_s12_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37], ins[38], ins[39], ins[40], ins[41], ins[42], ins[43], ins[44], ins[45], ins[46], ins[47], ins[48], ins[49], ins[50], ins[51], ins[52], ins[53], ins[54], ins[55], ins[56], ins[57], ins[58], ins[59], ins[60], ins[61], ins[62], ins[63], ins[64], ins[65], ins[66], ins[67], ins[68], ins[69], ins[70], ins[71], ins[72], ins[73], ins[74], ins[75])
    return out


@triton.jit
def t024_s13_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr, in38_ptr, in39_ptr, in40_ptr, in41_ptr, in42_ptr, in43_ptr, in44_ptr, in45_ptr, in46_ptr, in47_ptr, in48_ptr, in49_ptr, in50_ptr, in51_ptr, in52_ptr, in53_ptr, in54_ptr, in55_ptr, in56_ptr, in57_ptr, in58_ptr, in59_ptr, in60_ptr, in61_ptr, in62_ptr, in63_ptr, in64_ptr, in65_ptr, in66_ptr, in67_ptr, in68_ptr, in69_ptr, in70_ptr, in71_ptr, in72_ptr, in73_ptr, in74_ptr, in75_ptr, in76_ptr):
    _acc0 = tl.zeros([64], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 64) + tl.arange(0, 64)) < 96) & ((0 < 1) & (0 < 1))), (tl.load(in76_ptr + ((((tl.program_id(0) // 24) * 96) + ((_lv0 * 64) + tl.arange(0, 64))) + 0 * tl.arange(0, 64)), mask=((((_lv0 * 64) + tl.arange(0, 64)) < 96) & ((0 < 1) & (0 < 1))), other=0.0) * tl.load(in10_ptr + ((((tl.program_id(0) % 24) * 96) + ((_lv0 * 64) + tl.arange(0, 64))) + 0 * tl.arange(0, 64)), mask=((((_lv0 * 64) + tl.arange(0, 64)) < 96) & ((0 < 1) & (0 < 1))), other=0.0)), 0.0))
    _v = tl.maximum(tl.sum(_acc0, axis=0), (0.0 * (1.0 / 1.0)))
    tl.store(out_ptr + tl.program_id(0), _v)


def t024_s13(out, ins):
    grid = (48,)
    t024_s13_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37], ins[38], ins[39], ins[40], ins[41], ins[42], ins[43], ins[44], ins[45], ins[46], ins[47], ins[48], ins[49], ins[50], ins[51], ins[52], ins[53], ins[54], ins[55], ins[56], ins[57], ins[58], ins[59], ins[60], ins[61], ins[62], ins[63], ins[64], ins[65], ins[66], ins[67], ins[68], ins[69], ins[70], ins[71], ins[72], ins[73], ins[74], ins[75], ins[76])
    return out


@triton.jit
def t024_s14_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr, in38_ptr, in39_ptr, in40_ptr, in41_ptr, in42_ptr, in43_ptr, in44_ptr, in45_ptr, in46_ptr, in47_ptr, in48_ptr, in49_ptr, in50_ptr, in51_ptr, in52_ptr, in53_ptr, in54_ptr, in55_ptr, in56_ptr, in57_ptr, in58_ptr, in59_ptr, in60_ptr, in61_ptr, in62_ptr, in63_ptr, in64_ptr, in65_ptr, in66_ptr, in67_ptr, in68_ptr, in69_ptr, in70_ptr, in71_ptr, in72_ptr, in73_ptr, in74_ptr, in75_ptr, in76_ptr, in77_ptr):
    _acc0 = tl.zeros([16], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 16) + tl.arange(0, 16)) < 24) & ((0 < 1) & (0 < 1))), (tl.load(in77_ptr + ((((tl.program_id(0) // 96) * 24) + ((_lv0 * 16) + tl.arange(0, 16))) + 0 * tl.arange(0, 16)), mask=((((_lv0 * 16) + tl.arange(0, 16)) < 24) & ((0 < 1) & (0 < 1))), other=0.0) * tl.load(in11_ptr + ((((tl.program_id(0) % 96) * 24) + ((_lv0 * 16) + tl.arange(0, 16))) + 0 * tl.arange(0, 16)), mask=((((_lv0 * 16) + tl.arange(0, 16)) < 24) & ((0 < 1) & (0 < 1))), other=0.0)), 0.0))
    _v = (1.0 / ((1.0 * (1.0 / 1.0)) + tl.exp(((0.0 * (1.0 / 1.0)) - tl.sum(_acc0, axis=0)))))
    tl.store(out_ptr + tl.program_id(0), _v)


def t024_s14(out, ins):
    grid = (192,)
    t024_s14_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37], ins[38], ins[39], ins[40], ins[41], ins[42], ins[43], ins[44], ins[45], ins[46], ins[47], ins[48], ins[49], ins[50], ins[51], ins[52], ins[53], ins[54], ins[55], ins[56], ins[57], ins[58], ins[59], ins[60], ins[61], ins[62], ins[63], ins[64], ins[65], ins[66], ins[67], ins[68], ins[69], ins[70], ins[71], ins[72], ins[73], ins[74], ins[75], ins[76], ins[77])
    return out


@triton.jit
def t024_s15_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr, in38_ptr, in39_ptr, in40_ptr, in41_ptr, in42_ptr, in43_ptr, in44_ptr, in45_ptr, in46_ptr, in47_ptr, in48_ptr, in49_ptr, in50_ptr, in51_ptr, in52_ptr, in53_ptr, in54_ptr, in55_ptr, in56_ptr, in57_ptr, in58_ptr, in59_ptr, in60_ptr, in61_ptr, in62_ptr, in63_ptr, in64_ptr, in65_ptr, in66_ptr, in67_ptr, in68_ptr, in69_ptr, in70_ptr, in71_ptr, in72_ptr, in73_ptr, in74_ptr, in75_ptr, in76_ptr, in77_ptr, in78_ptr):
    _acc0 = tl.zeros([64], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 64) + tl.arange(0, 64)) < 96) & ((0 < 1) & (0 < 1))), (tl.load(in78_ptr + ((((tl.program_id(0) // 96) * 96) + ((_lv0 * 64) + tl.arange(0, 64))) + 0 * tl.arange(0, 64)), mask=((((_lv0 * 64) + tl.arange(0, 64)) < 96) & ((0 < 1) & (0 < 1))), other=0.0) * tl.load(in12_ptr + ((((tl.program_id(0) % 96) * 96) + ((_lv0 * 64) + tl.arange(0, 64))) + 0 * tl.arange(0, 64)), mask=((((_lv0 * 64) + tl.arange(0, 64)) < 96) & ((0 < 1) & (0 < 1))), other=0.0)), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t024_s15(out, ins):
    grid = (192,)
    t024_s15_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37], ins[38], ins[39], ins[40], ins[41], ins[42], ins[43], ins[44], ins[45], ins[46], ins[47], ins[48], ins[49], ins[50], ins[51], ins[52], ins[53], ins[54], ins[55], ins[56], ins[57], ins[58], ins[59], ins[60], ins[61], ins[62], ins[63], ins[64], ins[65], ins[66], ins[67], ins[68], ins[69], ins[70], ins[71], ins[72], ins[73], ins[74], ins[75], ins[76], ins[77], ins[78])
    return out


@triton.jit
def t024_s16_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr, in38_ptr, in39_ptr, in40_ptr, in41_ptr, in42_ptr, in43_ptr, in44_ptr, in45_ptr, in46_ptr, in47_ptr, in48_ptr, in49_ptr, in50_ptr, in51_ptr, in52_ptr, in53_ptr, in54_ptr, in55_ptr, in56_ptr, in57_ptr, in58_ptr, in59_ptr, in60_ptr, in61_ptr, in62_ptr, in63_ptr, in64_ptr, in65_ptr, in66_ptr, in67_ptr, in68_ptr, in69_ptr, in70_ptr, in71_ptr, in72_ptr, in73_ptr, in74_ptr, in75_ptr, in76_ptr, in77_ptr, in78_ptr, in79_ptr):
    _acc0 = tl.zeros([2], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 2) + tl.arange(0, 2)) < 2) & True), tl.load(in79_ptr + (((((_lv0 * 2) + tl.arange(0, 2)) * 96) + tl.program_id(0)) + 0 * tl.arange(0, 2)), mask=((((_lv0 * 2) + tl.arange(0, 2)) < 2) & True), other=0.0), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t024_s16(out, ins):
    grid = (96,)
    t024_s16_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37], ins[38], ins[39], ins[40], ins[41], ins[42], ins[43], ins[44], ins[45], ins[46], ins[47], ins[48], ins[49], ins[50], ins[51], ins[52], ins[53], ins[54], ins[55], ins[56], ins[57], ins[58], ins[59], ins[60], ins[61], ins[62], ins[63], ins[64], ins[65], ins[66], ins[67], ins[68], ins[69], ins[70], ins[71], ins[72], ins[73], ins[74], ins[75], ins[76], ins[77], ins[78], ins[79])
    return out


@triton.jit
def t024_s17_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr, in38_ptr, in39_ptr, in40_ptr, in41_ptr, in42_ptr, in43_ptr, in44_ptr, in45_ptr, in46_ptr, in47_ptr, in48_ptr, in49_ptr, in50_ptr, in51_ptr, in52_ptr, in53_ptr, in54_ptr, in55_ptr, in56_ptr, in57_ptr, in58_ptr, in59_ptr, in60_ptr, in61_ptr, in62_ptr, in63_ptr, in64_ptr, in65_ptr, in66_ptr, in67_ptr, in68_ptr, in69_ptr, in70_ptr, in71_ptr, in72_ptr, in73_ptr, in74_ptr, in75_ptr, in76_ptr, in77_ptr, in78_ptr, in79_ptr, in80_ptr):
    _acc0 = tl.zeros([2], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 2) + tl.arange(0, 2)) < 2) & True), ((tl.load(in79_ptr + (((((_lv0 * 2) + tl.arange(0, 2)) * 96) + tl.program_id(0)) + 0 * tl.arange(0, 2)), mask=((((_lv0 * 2) + tl.arange(0, 2)) < 2) & True), other=0.0) - (tl.load(in80_ptr + (tl.program_id(0) + 0 * tl.arange(0, 2)), mask=((((_lv0 * 2) + tl.arange(0, 2)) < 2) & True), other=0.0) * (1.0 * (1.0 / 2.0)))) * (tl.load(in79_ptr + (((((_lv0 * 2) + tl.arange(0, 2)) * 96) + tl.program_id(0)) + 0 * tl.arange(0, 2)), mask=((((_lv0 * 2) + tl.arange(0, 2)) < 2) & True), other=0.0) - (tl.load(in80_ptr + (tl.program_id(0) + 0 * tl.arange(0, 2)), mask=((((_lv0 * 2) + tl.arange(0, 2)) < 2) & True), other=0.0) * (1.0 * (1.0 / 2.0))))), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t024_s17(out, ins):
    grid = (96,)
    t024_s17_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37], ins[38], ins[39], ins[40], ins[41], ins[42], ins[43], ins[44], ins[45], ins[46], ins[47], ins[48], ins[49], ins[50], ins[51], ins[52], ins[53], ins[54], ins[55], ins[56], ins[57], ins[58], ins[59], ins[60], ins[61], ins[62], ins[63], ins[64], ins[65], ins[66], ins[67], ins[68], ins[69], ins[70], ins[71], ins[72], ins[73], ins[74], ins[75], ins[76], ins[77], ins[78], ins[79], ins[80])
    return out


@triton.jit
def t024_s18_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr, in38_ptr, in39_ptr, in40_ptr, in41_ptr, in42_ptr, in43_ptr, in44_ptr, in45_ptr, in46_ptr, in47_ptr, in48_ptr, in49_ptr, in50_ptr, in51_ptr, in52_ptr, in53_ptr, in54_ptr, in55_ptr, in56_ptr, in57_ptr, in58_ptr, in59_ptr, in60_ptr, in61_ptr, in62_ptr, in63_ptr, in64_ptr, in65_ptr, in66_ptr, in67_ptr, in68_ptr, in69_ptr, in70_ptr, in71_ptr, in72_ptr, in73_ptr, in74_ptr, in75_ptr, in76_ptr, in77_ptr, in78_ptr, in79_ptr, in80_ptr, in81_ptr):
    _acc0 = tl.zeros([1], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), ((((tl.load(in79_ptr + (tl.program_id(0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) - (tl.load(in80_ptr + (tl.maximum((tl.program_id(0) % 96) - tl.maximum((tl.program_id(0) % 96) - 95, 0), 0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) * (1.0 * (1.0 / 2.0)))) * (1.0 / tl.sqrt(((tl.load(in81_ptr + (tl.maximum((tl.program_id(0) % 96) - tl.maximum((tl.program_id(0) % 96) - 95, 0), 0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) * (1.0 * (1.0 / 2.0))) + (1.0 * (1.0 / 100000.0)))))) * tl.load(in13_ptr + ((tl.program_id(0) % 96) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)) + tl.load(in14_ptr + ((tl.program_id(0) % 96) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t024_s18(out, ins):
    grid = (192,)
    t024_s18_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37], ins[38], ins[39], ins[40], ins[41], ins[42], ins[43], ins[44], ins[45], ins[46], ins[47], ins[48], ins[49], ins[50], ins[51], ins[52], ins[53], ins[54], ins[55], ins[56], ins[57], ins[58], ins[59], ins[60], ins[61], ins[62], ins[63], ins[64], ins[65], ins[66], ins[67], ins[68], ins[69], ins[70], ins[71], ins[72], ins[73], ins[74], ins[75], ins[76], ins[77], ins[78], ins[79], ins[80], ins[81])
    return out


@triton.jit
def t024_s19_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr, in38_ptr, in39_ptr, in40_ptr, in41_ptr, in42_ptr, in43_ptr, in44_ptr, in45_ptr, in46_ptr, in47_ptr, in48_ptr, in49_ptr, in50_ptr, in51_ptr, in52_ptr, in53_ptr, in54_ptr, in55_ptr, in56_ptr, in57_ptr, in58_ptr, in59_ptr, in60_ptr, in61_ptr, in62_ptr, in63_ptr, in64_ptr, in65_ptr, in66_ptr, in67_ptr, in68_ptr, in69_ptr, in70_ptr, in71_ptr, in72_ptr, in73_ptr, in74_ptr, in75_ptr, in76_ptr, in77_ptr, in78_ptr, in79_ptr, in80_ptr, in81_ptr, in82_ptr):
    _acc0 = tl.zeros([64], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 64) + tl.arange(0, 64)) < 96) & ((0 < 1) & (0 < 1))), (tl.load(in82_ptr + ((((tl.program_id(0) // 576) * 96) + ((_lv0 * 64) + tl.arange(0, 64))) + 0 * tl.arange(0, 64)), mask=((((_lv0 * 64) + tl.arange(0, 64)) < 96) & ((0 < 1) & (0 < 1))), other=0.0) * tl.load(in15_ptr + ((((tl.program_id(0) % 576) * 96) + ((_lv0 * 64) + tl.arange(0, 64))) + 0 * tl.arange(0, 64)), mask=((((_lv0 * 64) + tl.arange(0, 64)) < 96) & ((0 < 1) & (0 < 1))), other=0.0)), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t024_s19(out, ins):
    grid = (1152,)
    t024_s19_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37], ins[38], ins[39], ins[40], ins[41], ins[42], ins[43], ins[44], ins[45], ins[46], ins[47], ins[48], ins[49], ins[50], ins[51], ins[52], ins[53], ins[54], ins[55], ins[56], ins[57], ins[58], ins[59], ins[60], ins[61], ins[62], ins[63], ins[64], ins[65], ins[66], ins[67], ins[68], ins[69], ins[70], ins[71], ins[72], ins[73], ins[74], ins[75], ins[76], ins[77], ins[78], ins[79], ins[80], ins[81], ins[82])
    return out


@triton.jit
def t024_s20_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr, in38_ptr, in39_ptr, in40_ptr, in41_ptr, in42_ptr, in43_ptr, in44_ptr, in45_ptr, in46_ptr, in47_ptr, in48_ptr, in49_ptr, in50_ptr, in51_ptr, in52_ptr, in53_ptr, in54_ptr, in55_ptr, in56_ptr, in57_ptr, in58_ptr, in59_ptr, in60_ptr, in61_ptr, in62_ptr, in63_ptr, in64_ptr, in65_ptr, in66_ptr, in67_ptr, in68_ptr, in69_ptr, in70_ptr, in71_ptr, in72_ptr, in73_ptr, in74_ptr, in75_ptr, in76_ptr, in77_ptr, in78_ptr, in79_ptr, in80_ptr, in81_ptr, in82_ptr, in83_ptr):
    _acc0 = tl.zeros([2], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 2) + tl.arange(0, 2)) < 2) & True), tl.load(in83_ptr + (((((_lv0 * 2) + tl.arange(0, 2)) * 576) + tl.program_id(0)) + 0 * tl.arange(0, 2)), mask=((((_lv0 * 2) + tl.arange(0, 2)) < 2) & True), other=0.0), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t024_s20(out, ins):
    grid = (576,)
    t024_s20_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37], ins[38], ins[39], ins[40], ins[41], ins[42], ins[43], ins[44], ins[45], ins[46], ins[47], ins[48], ins[49], ins[50], ins[51], ins[52], ins[53], ins[54], ins[55], ins[56], ins[57], ins[58], ins[59], ins[60], ins[61], ins[62], ins[63], ins[64], ins[65], ins[66], ins[67], ins[68], ins[69], ins[70], ins[71], ins[72], ins[73], ins[74], ins[75], ins[76], ins[77], ins[78], ins[79], ins[80], ins[81], ins[82], ins[83])
    return out


@triton.jit
def t024_s21_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr, in38_ptr, in39_ptr, in40_ptr, in41_ptr, in42_ptr, in43_ptr, in44_ptr, in45_ptr, in46_ptr, in47_ptr, in48_ptr, in49_ptr, in50_ptr, in51_ptr, in52_ptr, in53_ptr, in54_ptr, in55_ptr, in56_ptr, in57_ptr, in58_ptr, in59_ptr, in60_ptr, in61_ptr, in62_ptr, in63_ptr, in64_ptr, in65_ptr, in66_ptr, in67_ptr, in68_ptr, in69_ptr, in70_ptr, in71_ptr, in72_ptr, in73_ptr, in74_ptr, in75_ptr, in76_ptr, in77_ptr, in78_ptr, in79_ptr, in80_ptr, in81_ptr, in82_ptr, in83_ptr, in84_ptr):
    _acc0 = tl.zeros([2], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 2) + tl.arange(0, 2)) < 2) & True), ((tl.load(in83_ptr + (((((_lv0 * 2) + tl.arange(0, 2)) * 576) + tl.program_id(0)) + 0 * tl.arange(0, 2)), mask=((((_lv0 * 2) + tl.arange(0, 2)) < 2) & True), other=0.0) - (tl.load(in84_ptr + (tl.program_id(0) + 0 * tl.arange(0, 2)), mask=((((_lv0 * 2) + tl.arange(0, 2)) < 2) & True), other=0.0) * (1.0 * (1.0 / 2.0)))) * (tl.load(in83_ptr + (((((_lv0 * 2) + tl.arange(0, 2)) * 576) + tl.program_id(0)) + 0 * tl.arange(0, 2)), mask=((((_lv0 * 2) + tl.arange(0, 2)) < 2) & True), other=0.0) - (tl.load(in84_ptr + (tl.program_id(0) + 0 * tl.arange(0, 2)), mask=((((_lv0 * 2) + tl.arange(0, 2)) < 2) & True), other=0.0) * (1.0 * (1.0 / 2.0))))), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t024_s21(out, ins):
    grid = (576,)
    t024_s21_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37], ins[38], ins[39], ins[40], ins[41], ins[42], ins[43], ins[44], ins[45], ins[46], ins[47], ins[48], ins[49], ins[50], ins[51], ins[52], ins[53], ins[54], ins[55], ins[56], ins[57], ins[58], ins[59], ins[60], ins[61], ins[62], ins[63], ins[64], ins[65], ins[66], ins[67], ins[68], ins[69], ins[70], ins[71], ins[72], ins[73], ins[74], ins[75], ins[76], ins[77], ins[78], ins[79], ins[80], ins[81], ins[82], ins[83], ins[84])
    return out


@triton.jit
def t024_s22_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr, in38_ptr, in39_ptr, in40_ptr, in41_ptr, in42_ptr, in43_ptr, in44_ptr, in45_ptr, in46_ptr, in47_ptr, in48_ptr, in49_ptr, in50_ptr, in51_ptr, in52_ptr, in53_ptr, in54_ptr, in55_ptr, in56_ptr, in57_ptr, in58_ptr, in59_ptr, in60_ptr, in61_ptr, in62_ptr, in63_ptr, in64_ptr, in65_ptr, in66_ptr, in67_ptr, in68_ptr, in69_ptr, in70_ptr, in71_ptr, in72_ptr, in73_ptr, in74_ptr, in75_ptr, in76_ptr, in77_ptr, in78_ptr, in79_ptr, in80_ptr, in81_ptr, in82_ptr, in83_ptr, in84_ptr, in85_ptr):
    _acc0 = tl.zeros([1], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), ((((tl.load(in83_ptr + (tl.program_id(0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) - (tl.load(in84_ptr + (tl.maximum((tl.program_id(0) % 576) - tl.maximum((tl.program_id(0) % 576) - 575, 0), 0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) * (1.0 * (1.0 / 2.0)))) * (1.0 / tl.sqrt(((tl.load(in85_ptr + (tl.maximum((tl.program_id(0) % 576) - tl.maximum((tl.program_id(0) % 576) - 575, 0), 0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) * (1.0 * (1.0 / 2.0))) + (1.0 * (1.0 / 100000.0)))))) * tl.load(in16_ptr + ((tl.program_id(0) % 576) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)) + tl.load(in17_ptr + ((tl.program_id(0) % 576) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)), 0.0))
    _v = tl.maximum(tl.sum(_acc0, axis=0), (0.0 * (1.0 / 1.0)))
    tl.store(out_ptr + tl.program_id(0), _v)


def t024_s22(out, ins):
    grid = (1152,)
    t024_s22_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37], ins[38], ins[39], ins[40], ins[41], ins[42], ins[43], ins[44], ins[45], ins[46], ins[47], ins[48], ins[49], ins[50], ins[51], ins[52], ins[53], ins[54], ins[55], ins[56], ins[57], ins[58], ins[59], ins[60], ins[61], ins[62], ins[63], ins[64], ins[65], ins[66], ins[67], ins[68], ins[69], ins[70], ins[71], ins[72], ins[73], ins[74], ins[75], ins[76], ins[77], ins[78], ins[79], ins[80], ins[81], ins[82], ins[83], ins[84], ins[85])
    return out


@triton.jit
def t024_s23_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr, in38_ptr, in39_ptr, in40_ptr, in41_ptr, in42_ptr, in43_ptr, in44_ptr, in45_ptr, in46_ptr, in47_ptr, in48_ptr, in49_ptr, in50_ptr, in51_ptr, in52_ptr, in53_ptr, in54_ptr, in55_ptr, in56_ptr, in57_ptr, in58_ptr, in59_ptr, in60_ptr, in61_ptr, in62_ptr, in63_ptr, in64_ptr, in65_ptr, in66_ptr, in67_ptr, in68_ptr, in69_ptr, in70_ptr, in71_ptr, in72_ptr, in73_ptr, in74_ptr, in75_ptr, in76_ptr, in77_ptr, in78_ptr, in79_ptr, in80_ptr, in81_ptr, in82_ptr, in83_ptr, in84_ptr, in85_ptr, in86_ptr):
    _acc0 = tl.zeros([8], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 8) + tl.arange(0, 8)) < 9) & ((((1 <= ((((_lv0 * 8) + tl.arange(0, 8)) // 3) % 3)) & (((((_lv0 * 8) + tl.arange(0, 8)) // 3) % 3) < 2)) & (1 <= (((_lv0 * 8) + tl.arange(0, 8)) % 3))) & ((((_lv0 * 8) + tl.arange(0, 8)) % 3) < 2))), (tl.load(in86_ptr + (tl.maximum((((((tl.program_id(0) // 576) * 576) + (tl.program_id(0) % 576)) + tl.maximum(((((_lv0 * 8) + tl.arange(0, 8)) // 3) % 3) - 1, 0)) + tl.maximum((((_lv0 * 8) + tl.arange(0, 8)) % 3) - 1, 0)) - tl.maximum((((((tl.program_id(0) // 576) * 576) + (tl.program_id(0) % 576)) + tl.maximum(((((_lv0 * 8) + tl.arange(0, 8)) // 3) % 3) - 1, 0)) + tl.maximum((((_lv0 * 8) + tl.arange(0, 8)) % 3) - 1, 0)) - 1151, 0), 0) + 0 * tl.arange(0, 8)), mask=((((_lv0 * 8) + tl.arange(0, 8)) < 9) & ((((1 <= ((((_lv0 * 8) + tl.arange(0, 8)) // 3) % 3)) & (((((_lv0 * 8) + tl.arange(0, 8)) // 3) % 3) < 2)) & (1 <= (((_lv0 * 8) + tl.arange(0, 8)) % 3))) & ((((_lv0 * 8) + tl.arange(0, 8)) % 3) < 2))), other=0.0) * tl.load(in18_ptr + ((((((tl.program_id(0) % 576) * 3) + ((((_lv0 * 8) + tl.arange(0, 8)) // 3) % 3)) * 3) + (((_lv0 * 8) + tl.arange(0, 8)) % 3)) + 0 * tl.arange(0, 8)), mask=((((_lv0 * 8) + tl.arange(0, 8)) < 9) & ((((1 <= ((((_lv0 * 8) + tl.arange(0, 8)) // 3) % 3)) & (((((_lv0 * 8) + tl.arange(0, 8)) // 3) % 3) < 2)) & (1 <= (((_lv0 * 8) + tl.arange(0, 8)) % 3))) & ((((_lv0 * 8) + tl.arange(0, 8)) % 3) < 2))), other=0.0)), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t024_s23(out, ins):
    grid = (1152,)
    t024_s23_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37], ins[38], ins[39], ins[40], ins[41], ins[42], ins[43], ins[44], ins[45], ins[46], ins[47], ins[48], ins[49], ins[50], ins[51], ins[52], ins[53], ins[54], ins[55], ins[56], ins[57], ins[58], ins[59], ins[60], ins[61], ins[62], ins[63], ins[64], ins[65], ins[66], ins[67], ins[68], ins[69], ins[70], ins[71], ins[72], ins[73], ins[74], ins[75], ins[76], ins[77], ins[78], ins[79], ins[80], ins[81], ins[82], ins[83], ins[84], ins[85], ins[86])
    return out


@triton.jit
def t024_s24_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr, in38_ptr, in39_ptr, in40_ptr, in41_ptr, in42_ptr, in43_ptr, in44_ptr, in45_ptr, in46_ptr, in47_ptr, in48_ptr, in49_ptr, in50_ptr, in51_ptr, in52_ptr, in53_ptr, in54_ptr, in55_ptr, in56_ptr, in57_ptr, in58_ptr, in59_ptr, in60_ptr, in61_ptr, in62_ptr, in63_ptr, in64_ptr, in65_ptr, in66_ptr, in67_ptr, in68_ptr, in69_ptr, in70_ptr, in71_ptr, in72_ptr, in73_ptr, in74_ptr, in75_ptr, in76_ptr, in77_ptr, in78_ptr, in79_ptr, in80_ptr, in81_ptr, in82_ptr, in83_ptr, in84_ptr, in85_ptr, in86_ptr, in87_ptr):
    _acc0 = tl.zeros([2], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 2) + tl.arange(0, 2)) < 2) & True), tl.load(in87_ptr + (((((_lv0 * 2) + tl.arange(0, 2)) * 576) + tl.program_id(0)) + 0 * tl.arange(0, 2)), mask=((((_lv0 * 2) + tl.arange(0, 2)) < 2) & True), other=0.0), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t024_s24(out, ins):
    grid = (576,)
    t024_s24_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37], ins[38], ins[39], ins[40], ins[41], ins[42], ins[43], ins[44], ins[45], ins[46], ins[47], ins[48], ins[49], ins[50], ins[51], ins[52], ins[53], ins[54], ins[55], ins[56], ins[57], ins[58], ins[59], ins[60], ins[61], ins[62], ins[63], ins[64], ins[65], ins[66], ins[67], ins[68], ins[69], ins[70], ins[71], ins[72], ins[73], ins[74], ins[75], ins[76], ins[77], ins[78], ins[79], ins[80], ins[81], ins[82], ins[83], ins[84], ins[85], ins[86], ins[87])
    return out


@triton.jit
def t024_s25_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr, in38_ptr, in39_ptr, in40_ptr, in41_ptr, in42_ptr, in43_ptr, in44_ptr, in45_ptr, in46_ptr, in47_ptr, in48_ptr, in49_ptr, in50_ptr, in51_ptr, in52_ptr, in53_ptr, in54_ptr, in55_ptr, in56_ptr, in57_ptr, in58_ptr, in59_ptr, in60_ptr, in61_ptr, in62_ptr, in63_ptr, in64_ptr, in65_ptr, in66_ptr, in67_ptr, in68_ptr, in69_ptr, in70_ptr, in71_ptr, in72_ptr, in73_ptr, in74_ptr, in75_ptr, in76_ptr, in77_ptr, in78_ptr, in79_ptr, in80_ptr, in81_ptr, in82_ptr, in83_ptr, in84_ptr, in85_ptr, in86_ptr, in87_ptr, in88_ptr):
    _acc0 = tl.zeros([2], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 2) + tl.arange(0, 2)) < 2) & True), ((tl.load(in87_ptr + (((((_lv0 * 2) + tl.arange(0, 2)) * 576) + tl.program_id(0)) + 0 * tl.arange(0, 2)), mask=((((_lv0 * 2) + tl.arange(0, 2)) < 2) & True), other=0.0) - (tl.load(in88_ptr + (tl.program_id(0) + 0 * tl.arange(0, 2)), mask=((((_lv0 * 2) + tl.arange(0, 2)) < 2) & True), other=0.0) * (1.0 * (1.0 / 2.0)))) * (tl.load(in87_ptr + (((((_lv0 * 2) + tl.arange(0, 2)) * 576) + tl.program_id(0)) + 0 * tl.arange(0, 2)), mask=((((_lv0 * 2) + tl.arange(0, 2)) < 2) & True), other=0.0) - (tl.load(in88_ptr + (tl.program_id(0) + 0 * tl.arange(0, 2)), mask=((((_lv0 * 2) + tl.arange(0, 2)) < 2) & True), other=0.0) * (1.0 * (1.0 / 2.0))))), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t024_s25(out, ins):
    grid = (576,)
    t024_s25_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37], ins[38], ins[39], ins[40], ins[41], ins[42], ins[43], ins[44], ins[45], ins[46], ins[47], ins[48], ins[49], ins[50], ins[51], ins[52], ins[53], ins[54], ins[55], ins[56], ins[57], ins[58], ins[59], ins[60], ins[61], ins[62], ins[63], ins[64], ins[65], ins[66], ins[67], ins[68], ins[69], ins[70], ins[71], ins[72], ins[73], ins[74], ins[75], ins[76], ins[77], ins[78], ins[79], ins[80], ins[81], ins[82], ins[83], ins[84], ins[85], ins[86], ins[87], ins[88])
    return out


@triton.jit
def t024_s26_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr, in38_ptr, in39_ptr, in40_ptr, in41_ptr, in42_ptr, in43_ptr, in44_ptr, in45_ptr, in46_ptr, in47_ptr, in48_ptr, in49_ptr, in50_ptr, in51_ptr, in52_ptr, in53_ptr, in54_ptr, in55_ptr, in56_ptr, in57_ptr, in58_ptr, in59_ptr, in60_ptr, in61_ptr, in62_ptr, in63_ptr, in64_ptr, in65_ptr, in66_ptr, in67_ptr, in68_ptr, in69_ptr, in70_ptr, in71_ptr, in72_ptr, in73_ptr, in74_ptr, in75_ptr, in76_ptr, in77_ptr, in78_ptr, in79_ptr, in80_ptr, in81_ptr, in82_ptr, in83_ptr, in84_ptr, in85_ptr, in86_ptr, in87_ptr, in88_ptr, in89_ptr):
    _acc0 = tl.zeros([1], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), ((((tl.load(in87_ptr + (tl.program_id(0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) - (tl.load(in88_ptr + (tl.maximum((tl.program_id(0) % 576) - tl.maximum((tl.program_id(0) % 576) - 575, 0), 0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) * (1.0 * (1.0 / 2.0)))) * (1.0 / tl.sqrt(((tl.load(in89_ptr + (tl.maximum((tl.program_id(0) % 576) - tl.maximum((tl.program_id(0) % 576) - 575, 0), 0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) * (1.0 * (1.0 / 2.0))) + (1.0 * (1.0 / 100000.0)))))) * tl.load(in19_ptr + ((tl.program_id(0) % 576) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)) + tl.load(in20_ptr + ((tl.program_id(0) % 576) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)), 0.0))
    _v = tl.maximum(tl.sum(_acc0, axis=0), (0.0 * (1.0 / 1.0)))
    tl.store(out_ptr + tl.program_id(0), _v)


def t024_s26(out, ins):
    grid = (1152,)
    t024_s26_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37], ins[38], ins[39], ins[40], ins[41], ins[42], ins[43], ins[44], ins[45], ins[46], ins[47], ins[48], ins[49], ins[50], ins[51], ins[52], ins[53], ins[54], ins[55], ins[56], ins[57], ins[58], ins[59], ins[60], ins[61], ins[62], ins[63], ins[64], ins[65], ins[66], ins[67], ins[68], ins[69], ins[70], ins[71], ins[72], ins[73], ins[74], ins[75], ins[76], ins[77], ins[78], ins[79], ins[80], ins[81], ins[82], ins[83], ins[84], ins[85], ins[86], ins[87], ins[88], ins[89])
    return out


@triton.jit
def t024_s27_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr, in38_ptr, in39_ptr, in40_ptr, in41_ptr, in42_ptr, in43_ptr, in44_ptr, in45_ptr, in46_ptr, in47_ptr, in48_ptr, in49_ptr, in50_ptr, in51_ptr, in52_ptr, in53_ptr, in54_ptr, in55_ptr, in56_ptr, in57_ptr, in58_ptr, in59_ptr, in60_ptr, in61_ptr, in62_ptr, in63_ptr, in64_ptr, in65_ptr, in66_ptr, in67_ptr, in68_ptr, in69_ptr, in70_ptr, in71_ptr, in72_ptr, in73_ptr, in74_ptr, in75_ptr, in76_ptr, in77_ptr, in78_ptr, in79_ptr, in80_ptr, in81_ptr, in82_ptr, in83_ptr, in84_ptr, in85_ptr, in86_ptr, in87_ptr, in88_ptr, in89_ptr, in90_ptr):
    _acc0 = tl.zeros([1], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), tl.load(in90_ptr + (tl.maximum((tl.program_id(0) + ((_lv0 * 1) + tl.arange(0, 1))) - tl.maximum((tl.program_id(0) + ((_lv0 * 1) + tl.arange(0, 1))) - 1151, 0), 0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0), 0.0))
    _v = (tl.sum(_acc0, axis=0) * (1.0 * (1.0 / 1.0)))
    tl.store(out_ptr + tl.program_id(0), _v)


def t024_s27(out, ins):
    grid = (1152,)
    t024_s27_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37], ins[38], ins[39], ins[40], ins[41], ins[42], ins[43], ins[44], ins[45], ins[46], ins[47], ins[48], ins[49], ins[50], ins[51], ins[52], ins[53], ins[54], ins[55], ins[56], ins[57], ins[58], ins[59], ins[60], ins[61], ins[62], ins[63], ins[64], ins[65], ins[66], ins[67], ins[68], ins[69], ins[70], ins[71], ins[72], ins[73], ins[74], ins[75], ins[76], ins[77], ins[78], ins[79], ins[80], ins[81], ins[82], ins[83], ins[84], ins[85], ins[86], ins[87], ins[88], ins[89], ins[90])
    return out


@triton.jit
def t024_s28_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr, in38_ptr, in39_ptr, in40_ptr, in41_ptr, in42_ptr, in43_ptr, in44_ptr, in45_ptr, in46_ptr, in47_ptr, in48_ptr, in49_ptr, in50_ptr, in51_ptr, in52_ptr, in53_ptr, in54_ptr, in55_ptr, in56_ptr, in57_ptr, in58_ptr, in59_ptr, in60_ptr, in61_ptr, in62_ptr, in63_ptr, in64_ptr, in65_ptr, in66_ptr, in67_ptr, in68_ptr, in69_ptr, in70_ptr, in71_ptr, in72_ptr, in73_ptr, in74_ptr, in75_ptr, in76_ptr, in77_ptr, in78_ptr, in79_ptr, in80_ptr, in81_ptr, in82_ptr, in83_ptr, in84_ptr, in85_ptr, in86_ptr, in87_ptr, in88_ptr, in89_ptr, in90_ptr, in91_ptr):
    _acc0 = tl.zeros([512], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 512) + tl.arange(0, 512)) < 576) & ((0 < 1) & (0 < 1))), (tl.load(in91_ptr + ((((tl.program_id(0) // 144) * 576) + ((_lv0 * 512) + tl.arange(0, 512))) + 0 * tl.arange(0, 512)), mask=((((_lv0 * 512) + tl.arange(0, 512)) < 576) & ((0 < 1) & (0 < 1))), other=0.0) * tl.load(in21_ptr + ((((tl.program_id(0) % 144) * 576) + ((_lv0 * 512) + tl.arange(0, 512))) + 0 * tl.arange(0, 512)), mask=((((_lv0 * 512) + tl.arange(0, 512)) < 576) & ((0 < 1) & (0 < 1))), other=0.0)), 0.0))
    _v = tl.maximum(tl.sum(_acc0, axis=0), (0.0 * (1.0 / 1.0)))
    tl.store(out_ptr + tl.program_id(0), _v)


def t024_s28(out, ins):
    grid = (288,)
    t024_s28_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37], ins[38], ins[39], ins[40], ins[41], ins[42], ins[43], ins[44], ins[45], ins[46], ins[47], ins[48], ins[49], ins[50], ins[51], ins[52], ins[53], ins[54], ins[55], ins[56], ins[57], ins[58], ins[59], ins[60], ins[61], ins[62], ins[63], ins[64], ins[65], ins[66], ins[67], ins[68], ins[69], ins[70], ins[71], ins[72], ins[73], ins[74], ins[75], ins[76], ins[77], ins[78], ins[79], ins[80], ins[81], ins[82], ins[83], ins[84], ins[85], ins[86], ins[87], ins[88], ins[89], ins[90], ins[91])
    return out


@triton.jit
def t024_s29_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr, in38_ptr, in39_ptr, in40_ptr, in41_ptr, in42_ptr, in43_ptr, in44_ptr, in45_ptr, in46_ptr, in47_ptr, in48_ptr, in49_ptr, in50_ptr, in51_ptr, in52_ptr, in53_ptr, in54_ptr, in55_ptr, in56_ptr, in57_ptr, in58_ptr, in59_ptr, in60_ptr, in61_ptr, in62_ptr, in63_ptr, in64_ptr, in65_ptr, in66_ptr, in67_ptr, in68_ptr, in69_ptr, in70_ptr, in71_ptr, in72_ptr, in73_ptr, in74_ptr, in75_ptr, in76_ptr, in77_ptr, in78_ptr, in79_ptr, in80_ptr, in81_ptr, in82_ptr, in83_ptr, in84_ptr, in85_ptr, in86_ptr, in87_ptr, in88_ptr, in89_ptr, in90_ptr, in91_ptr, in92_ptr):
    _acc0 = tl.zeros([128], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 128) + tl.arange(0, 128)) < 144) & ((0 < 1) & (0 < 1))), (tl.load(in92_ptr + ((((tl.program_id(0) // 576) * 144) + ((_lv0 * 128) + tl.arange(0, 128))) + 0 * tl.arange(0, 128)), mask=((((_lv0 * 128) + tl.arange(0, 128)) < 144) & ((0 < 1) & (0 < 1))), other=0.0) * tl.load(in22_ptr + ((((tl.program_id(0) % 576) * 144) + ((_lv0 * 128) + tl.arange(0, 128))) + 0 * tl.arange(0, 128)), mask=((((_lv0 * 128) + tl.arange(0, 128)) < 144) & ((0 < 1) & (0 < 1))), other=0.0)), 0.0))
    _v = (1.0 / ((1.0 * (1.0 / 1.0)) + tl.exp(((0.0 * (1.0 / 1.0)) - tl.sum(_acc0, axis=0)))))
    tl.store(out_ptr + tl.program_id(0), _v)


def t024_s29(out, ins):
    grid = (1152,)
    t024_s29_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37], ins[38], ins[39], ins[40], ins[41], ins[42], ins[43], ins[44], ins[45], ins[46], ins[47], ins[48], ins[49], ins[50], ins[51], ins[52], ins[53], ins[54], ins[55], ins[56], ins[57], ins[58], ins[59], ins[60], ins[61], ins[62], ins[63], ins[64], ins[65], ins[66], ins[67], ins[68], ins[69], ins[70], ins[71], ins[72], ins[73], ins[74], ins[75], ins[76], ins[77], ins[78], ins[79], ins[80], ins[81], ins[82], ins[83], ins[84], ins[85], ins[86], ins[87], ins[88], ins[89], ins[90], ins[91], ins[92])
    return out


@triton.jit
def t024_s30_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr, in38_ptr, in39_ptr, in40_ptr, in41_ptr, in42_ptr, in43_ptr, in44_ptr, in45_ptr, in46_ptr, in47_ptr, in48_ptr, in49_ptr, in50_ptr, in51_ptr, in52_ptr, in53_ptr, in54_ptr, in55_ptr, in56_ptr, in57_ptr, in58_ptr, in59_ptr, in60_ptr, in61_ptr, in62_ptr, in63_ptr, in64_ptr, in65_ptr, in66_ptr, in67_ptr, in68_ptr, in69_ptr, in70_ptr, in71_ptr, in72_ptr, in73_ptr, in74_ptr, in75_ptr, in76_ptr, in77_ptr, in78_ptr, in79_ptr, in80_ptr, in81_ptr, in82_ptr, in83_ptr, in84_ptr, in85_ptr, in86_ptr, in87_ptr, in88_ptr, in89_ptr, in90_ptr, in91_ptr, in92_ptr, in93_ptr):
    _acc0 = tl.zeros([512], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 512) + tl.arange(0, 512)) < 576) & ((0 < 1) & (0 < 1))), (tl.load(in93_ptr + ((((tl.program_id(0) // 144) * 576) + ((_lv0 * 512) + tl.arange(0, 512))) + 0 * tl.arange(0, 512)), mask=((((_lv0 * 512) + tl.arange(0, 512)) < 576) & ((0 < 1) & (0 < 1))), other=0.0) * tl.load(in23_ptr + ((((tl.program_id(0) % 144) * 576) + ((_lv0 * 512) + tl.arange(0, 512))) + 0 * tl.arange(0, 512)), mask=((((_lv0 * 512) + tl.arange(0, 512)) < 576) & ((0 < 1) & (0 < 1))), other=0.0)), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t024_s30(out, ins):
    grid = (288,)
    t024_s30_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37], ins[38], ins[39], ins[40], ins[41], ins[42], ins[43], ins[44], ins[45], ins[46], ins[47], ins[48], ins[49], ins[50], ins[51], ins[52], ins[53], ins[54], ins[55], ins[56], ins[57], ins[58], ins[59], ins[60], ins[61], ins[62], ins[63], ins[64], ins[65], ins[66], ins[67], ins[68], ins[69], ins[70], ins[71], ins[72], ins[73], ins[74], ins[75], ins[76], ins[77], ins[78], ins[79], ins[80], ins[81], ins[82], ins[83], ins[84], ins[85], ins[86], ins[87], ins[88], ins[89], ins[90], ins[91], ins[92], ins[93])
    return out


@triton.jit
def t024_s31_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr, in38_ptr, in39_ptr, in40_ptr, in41_ptr, in42_ptr, in43_ptr, in44_ptr, in45_ptr, in46_ptr, in47_ptr, in48_ptr, in49_ptr, in50_ptr, in51_ptr, in52_ptr, in53_ptr, in54_ptr, in55_ptr, in56_ptr, in57_ptr, in58_ptr, in59_ptr, in60_ptr, in61_ptr, in62_ptr, in63_ptr, in64_ptr, in65_ptr, in66_ptr, in67_ptr, in68_ptr, in69_ptr, in70_ptr, in71_ptr, in72_ptr, in73_ptr, in74_ptr, in75_ptr, in76_ptr, in77_ptr, in78_ptr, in79_ptr, in80_ptr, in81_ptr, in82_ptr, in83_ptr, in84_ptr, in85_ptr, in86_ptr, in87_ptr, in88_ptr, in89_ptr, in90_ptr, in91_ptr, in92_ptr, in93_ptr, in94_ptr):
    _acc0 = tl.zeros([2], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 2) + tl.arange(0, 2)) < 2) & True), tl.load(in94_ptr + (((((_lv0 * 2) + tl.arange(0, 2)) * 144) + tl.program_id(0)) + 0 * tl.arange(0, 2)), mask=((((_lv0 * 2) + tl.arange(0, 2)) < 2) & True), other=0.0), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t024_s31(out, ins):
    grid = (144,)
    t024_s31_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37], ins[38], ins[39], ins[40], ins[41], ins[42], ins[43], ins[44], ins[45], ins[46], ins[47], ins[48], ins[49], ins[50], ins[51], ins[52], ins[53], ins[54], ins[55], ins[56], ins[57], ins[58], ins[59], ins[60], ins[61], ins[62], ins[63], ins[64], ins[65], ins[66], ins[67], ins[68], ins[69], ins[70], ins[71], ins[72], ins[73], ins[74], ins[75], ins[76], ins[77], ins[78], ins[79], ins[80], ins[81], ins[82], ins[83], ins[84], ins[85], ins[86], ins[87], ins[88], ins[89], ins[90], ins[91], ins[92], ins[93], ins[94])
    return out


@triton.jit
def t024_s32_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr, in38_ptr, in39_ptr, in40_ptr, in41_ptr, in42_ptr, in43_ptr, in44_ptr, in45_ptr, in46_ptr, in47_ptr, in48_ptr, in49_ptr, in50_ptr, in51_ptr, in52_ptr, in53_ptr, in54_ptr, in55_ptr, in56_ptr, in57_ptr, in58_ptr, in59_ptr, in60_ptr, in61_ptr, in62_ptr, in63_ptr, in64_ptr, in65_ptr, in66_ptr, in67_ptr, in68_ptr, in69_ptr, in70_ptr, in71_ptr, in72_ptr, in73_ptr, in74_ptr, in75_ptr, in76_ptr, in77_ptr, in78_ptr, in79_ptr, in80_ptr, in81_ptr, in82_ptr, in83_ptr, in84_ptr, in85_ptr, in86_ptr, in87_ptr, in88_ptr, in89_ptr, in90_ptr, in91_ptr, in92_ptr, in93_ptr, in94_ptr, in95_ptr):
    _acc0 = tl.zeros([2], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 2) + tl.arange(0, 2)) < 2) & True), ((tl.load(in94_ptr + (((((_lv0 * 2) + tl.arange(0, 2)) * 144) + tl.program_id(0)) + 0 * tl.arange(0, 2)), mask=((((_lv0 * 2) + tl.arange(0, 2)) < 2) & True), other=0.0) - (tl.load(in95_ptr + (tl.program_id(0) + 0 * tl.arange(0, 2)), mask=((((_lv0 * 2) + tl.arange(0, 2)) < 2) & True), other=0.0) * (1.0 * (1.0 / 2.0)))) * (tl.load(in94_ptr + (((((_lv0 * 2) + tl.arange(0, 2)) * 144) + tl.program_id(0)) + 0 * tl.arange(0, 2)), mask=((((_lv0 * 2) + tl.arange(0, 2)) < 2) & True), other=0.0) - (tl.load(in95_ptr + (tl.program_id(0) + 0 * tl.arange(0, 2)), mask=((((_lv0 * 2) + tl.arange(0, 2)) < 2) & True), other=0.0) * (1.0 * (1.0 / 2.0))))), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t024_s32(out, ins):
    grid = (144,)
    t024_s32_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37], ins[38], ins[39], ins[40], ins[41], ins[42], ins[43], ins[44], ins[45], ins[46], ins[47], ins[48], ins[49], ins[50], ins[51], ins[52], ins[53], ins[54], ins[55], ins[56], ins[57], ins[58], ins[59], ins[60], ins[61], ins[62], ins[63], ins[64], ins[65], ins[66], ins[67], ins[68], ins[69], ins[70], ins[71], ins[72], ins[73], ins[74], ins[75], ins[76], ins[77], ins[78], ins[79], ins[80], ins[81], ins[82], ins[83], ins[84], ins[85], ins[86], ins[87], ins[88], ins[89], ins[90], ins[91], ins[92], ins[93], ins[94], ins[95])
    return out


@triton.jit
def t024_s33_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr, in38_ptr, in39_ptr, in40_ptr, in41_ptr, in42_ptr, in43_ptr, in44_ptr, in45_ptr, in46_ptr, in47_ptr, in48_ptr, in49_ptr, in50_ptr, in51_ptr, in52_ptr, in53_ptr, in54_ptr, in55_ptr, in56_ptr, in57_ptr, in58_ptr, in59_ptr, in60_ptr, in61_ptr, in62_ptr, in63_ptr, in64_ptr, in65_ptr, in66_ptr, in67_ptr, in68_ptr, in69_ptr, in70_ptr, in71_ptr, in72_ptr, in73_ptr, in74_ptr, in75_ptr, in76_ptr, in77_ptr, in78_ptr, in79_ptr, in80_ptr, in81_ptr, in82_ptr, in83_ptr, in84_ptr, in85_ptr, in86_ptr, in87_ptr, in88_ptr, in89_ptr, in90_ptr, in91_ptr, in92_ptr, in93_ptr, in94_ptr, in95_ptr, in96_ptr):
    _acc0 = tl.zeros([1], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), ((((tl.load(in94_ptr + (tl.program_id(0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) - (tl.load(in95_ptr + (tl.maximum((tl.program_id(0) % 144) - tl.maximum((tl.program_id(0) % 144) - 143, 0), 0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) * (1.0 * (1.0 / 2.0)))) * (1.0 / tl.sqrt(((tl.load(in96_ptr + (tl.maximum((tl.program_id(0) % 144) - tl.maximum((tl.program_id(0) % 144) - 143, 0), 0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) * (1.0 * (1.0 / 2.0))) + (1.0 * (1.0 / 100000.0)))))) * tl.load(in24_ptr + ((tl.program_id(0) % 144) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)) + tl.load(in25_ptr + ((tl.program_id(0) % 144) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t024_s33(out, ins):
    grid = (288,)
    t024_s33_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37], ins[38], ins[39], ins[40], ins[41], ins[42], ins[43], ins[44], ins[45], ins[46], ins[47], ins[48], ins[49], ins[50], ins[51], ins[52], ins[53], ins[54], ins[55], ins[56], ins[57], ins[58], ins[59], ins[60], ins[61], ins[62], ins[63], ins[64], ins[65], ins[66], ins[67], ins[68], ins[69], ins[70], ins[71], ins[72], ins[73], ins[74], ins[75], ins[76], ins[77], ins[78], ins[79], ins[80], ins[81], ins[82], ins[83], ins[84], ins[85], ins[86], ins[87], ins[88], ins[89], ins[90], ins[91], ins[92], ins[93], ins[94], ins[95], ins[96])
    return out


@triton.jit
def t024_s34_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr, in38_ptr, in39_ptr, in40_ptr, in41_ptr, in42_ptr, in43_ptr, in44_ptr, in45_ptr, in46_ptr, in47_ptr, in48_ptr, in49_ptr, in50_ptr, in51_ptr, in52_ptr, in53_ptr, in54_ptr, in55_ptr, in56_ptr, in57_ptr, in58_ptr, in59_ptr, in60_ptr, in61_ptr, in62_ptr, in63_ptr, in64_ptr, in65_ptr, in66_ptr, in67_ptr, in68_ptr, in69_ptr, in70_ptr, in71_ptr, in72_ptr, in73_ptr, in74_ptr, in75_ptr, in76_ptr, in77_ptr, in78_ptr, in79_ptr, in80_ptr, in81_ptr, in82_ptr, in83_ptr, in84_ptr, in85_ptr, in86_ptr, in87_ptr, in88_ptr, in89_ptr, in90_ptr, in91_ptr, in92_ptr, in93_ptr, in94_ptr, in95_ptr, in96_ptr, in97_ptr):
    _acc0 = tl.zeros([128], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 128) + tl.arange(0, 128)) < 144) & ((0 < 1) & (0 < 1))), (tl.load(in97_ptr + ((((tl.program_id(0) // 864) * 144) + ((_lv0 * 128) + tl.arange(0, 128))) + 0 * tl.arange(0, 128)), mask=((((_lv0 * 128) + tl.arange(0, 128)) < 144) & ((0 < 1) & (0 < 1))), other=0.0) * tl.load(in26_ptr + ((((tl.program_id(0) % 864) * 144) + ((_lv0 * 128) + tl.arange(0, 128))) + 0 * tl.arange(0, 128)), mask=((((_lv0 * 128) + tl.arange(0, 128)) < 144) & ((0 < 1) & (0 < 1))), other=0.0)), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t024_s34(out, ins):
    grid = (1728,)
    t024_s34_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37], ins[38], ins[39], ins[40], ins[41], ins[42], ins[43], ins[44], ins[45], ins[46], ins[47], ins[48], ins[49], ins[50], ins[51], ins[52], ins[53], ins[54], ins[55], ins[56], ins[57], ins[58], ins[59], ins[60], ins[61], ins[62], ins[63], ins[64], ins[65], ins[66], ins[67], ins[68], ins[69], ins[70], ins[71], ins[72], ins[73], ins[74], ins[75], ins[76], ins[77], ins[78], ins[79], ins[80], ins[81], ins[82], ins[83], ins[84], ins[85], ins[86], ins[87], ins[88], ins[89], ins[90], ins[91], ins[92], ins[93], ins[94], ins[95], ins[96], ins[97])
    return out


@triton.jit
def t024_s35_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr, in38_ptr, in39_ptr, in40_ptr, in41_ptr, in42_ptr, in43_ptr, in44_ptr, in45_ptr, in46_ptr, in47_ptr, in48_ptr, in49_ptr, in50_ptr, in51_ptr, in52_ptr, in53_ptr, in54_ptr, in55_ptr, in56_ptr, in57_ptr, in58_ptr, in59_ptr, in60_ptr, in61_ptr, in62_ptr, in63_ptr, in64_ptr, in65_ptr, in66_ptr, in67_ptr, in68_ptr, in69_ptr, in70_ptr, in71_ptr, in72_ptr, in73_ptr, in74_ptr, in75_ptr, in76_ptr, in77_ptr, in78_ptr, in79_ptr, in80_ptr, in81_ptr, in82_ptr, in83_ptr, in84_ptr, in85_ptr, in86_ptr, in87_ptr, in88_ptr, in89_ptr, in90_ptr, in91_ptr, in92_ptr, in93_ptr, in94_ptr, in95_ptr, in96_ptr, in97_ptr, in98_ptr):
    _acc0 = tl.zeros([2], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 2) + tl.arange(0, 2)) < 2) & True), tl.load(in98_ptr + (((((_lv0 * 2) + tl.arange(0, 2)) * 864) + tl.program_id(0)) + 0 * tl.arange(0, 2)), mask=((((_lv0 * 2) + tl.arange(0, 2)) < 2) & True), other=0.0), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t024_s35(out, ins):
    grid = (864,)
    t024_s35_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37], ins[38], ins[39], ins[40], ins[41], ins[42], ins[43], ins[44], ins[45], ins[46], ins[47], ins[48], ins[49], ins[50], ins[51], ins[52], ins[53], ins[54], ins[55], ins[56], ins[57], ins[58], ins[59], ins[60], ins[61], ins[62], ins[63], ins[64], ins[65], ins[66], ins[67], ins[68], ins[69], ins[70], ins[71], ins[72], ins[73], ins[74], ins[75], ins[76], ins[77], ins[78], ins[79], ins[80], ins[81], ins[82], ins[83], ins[84], ins[85], ins[86], ins[87], ins[88], ins[89], ins[90], ins[91], ins[92], ins[93], ins[94], ins[95], ins[96], ins[97], ins[98])
    return out


@triton.jit
def t024_s36_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr, in38_ptr, in39_ptr, in40_ptr, in41_ptr, in42_ptr, in43_ptr, in44_ptr, in45_ptr, in46_ptr, in47_ptr, in48_ptr, in49_ptr, in50_ptr, in51_ptr, in52_ptr, in53_ptr, in54_ptr, in55_ptr, in56_ptr, in57_ptr, in58_ptr, in59_ptr, in60_ptr, in61_ptr, in62_ptr, in63_ptr, in64_ptr, in65_ptr, in66_ptr, in67_ptr, in68_ptr, in69_ptr, in70_ptr, in71_ptr, in72_ptr, in73_ptr, in74_ptr, in75_ptr, in76_ptr, in77_ptr, in78_ptr, in79_ptr, in80_ptr, in81_ptr, in82_ptr, in83_ptr, in84_ptr, in85_ptr, in86_ptr, in87_ptr, in88_ptr, in89_ptr, in90_ptr, in91_ptr, in92_ptr, in93_ptr, in94_ptr, in95_ptr, in96_ptr, in97_ptr, in98_ptr, in99_ptr):
    _acc0 = tl.zeros([2], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 2) + tl.arange(0, 2)) < 2) & True), ((tl.load(in98_ptr + (((((_lv0 * 2) + tl.arange(0, 2)) * 864) + tl.program_id(0)) + 0 * tl.arange(0, 2)), mask=((((_lv0 * 2) + tl.arange(0, 2)) < 2) & True), other=0.0) - (tl.load(in99_ptr + (tl.program_id(0) + 0 * tl.arange(0, 2)), mask=((((_lv0 * 2) + tl.arange(0, 2)) < 2) & True), other=0.0) * (1.0 * (1.0 / 2.0)))) * (tl.load(in98_ptr + (((((_lv0 * 2) + tl.arange(0, 2)) * 864) + tl.program_id(0)) + 0 * tl.arange(0, 2)), mask=((((_lv0 * 2) + tl.arange(0, 2)) < 2) & True), other=0.0) - (tl.load(in99_ptr + (tl.program_id(0) + 0 * tl.arange(0, 2)), mask=((((_lv0 * 2) + tl.arange(0, 2)) < 2) & True), other=0.0) * (1.0 * (1.0 / 2.0))))), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t024_s36(out, ins):
    grid = (864,)
    t024_s36_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37], ins[38], ins[39], ins[40], ins[41], ins[42], ins[43], ins[44], ins[45], ins[46], ins[47], ins[48], ins[49], ins[50], ins[51], ins[52], ins[53], ins[54], ins[55], ins[56], ins[57], ins[58], ins[59], ins[60], ins[61], ins[62], ins[63], ins[64], ins[65], ins[66], ins[67], ins[68], ins[69], ins[70], ins[71], ins[72], ins[73], ins[74], ins[75], ins[76], ins[77], ins[78], ins[79], ins[80], ins[81], ins[82], ins[83], ins[84], ins[85], ins[86], ins[87], ins[88], ins[89], ins[90], ins[91], ins[92], ins[93], ins[94], ins[95], ins[96], ins[97], ins[98], ins[99])
    return out


@triton.jit
def t024_s37_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr, in38_ptr, in39_ptr, in40_ptr, in41_ptr, in42_ptr, in43_ptr, in44_ptr, in45_ptr, in46_ptr, in47_ptr, in48_ptr, in49_ptr, in50_ptr, in51_ptr, in52_ptr, in53_ptr, in54_ptr, in55_ptr, in56_ptr, in57_ptr, in58_ptr, in59_ptr, in60_ptr, in61_ptr, in62_ptr, in63_ptr, in64_ptr, in65_ptr, in66_ptr, in67_ptr, in68_ptr, in69_ptr, in70_ptr, in71_ptr, in72_ptr, in73_ptr, in74_ptr, in75_ptr, in76_ptr, in77_ptr, in78_ptr, in79_ptr, in80_ptr, in81_ptr, in82_ptr, in83_ptr, in84_ptr, in85_ptr, in86_ptr, in87_ptr, in88_ptr, in89_ptr, in90_ptr, in91_ptr, in92_ptr, in93_ptr, in94_ptr, in95_ptr, in96_ptr, in97_ptr, in98_ptr, in99_ptr, in100_ptr):
    _acc0 = tl.zeros([1], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), ((((tl.load(in98_ptr + (tl.program_id(0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) - (tl.load(in99_ptr + (tl.maximum((tl.program_id(0) % 864) - tl.maximum((tl.program_id(0) % 864) - 863, 0), 0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) * (1.0 * (1.0 / 2.0)))) * (1.0 / tl.sqrt(((tl.load(in100_ptr + (tl.maximum((tl.program_id(0) % 864) - tl.maximum((tl.program_id(0) % 864) - 863, 0), 0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) * (1.0 * (1.0 / 2.0))) + (1.0 * (1.0 / 100000.0)))))) * tl.load(in27_ptr + ((tl.program_id(0) % 864) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)) + tl.load(in28_ptr + ((tl.program_id(0) % 864) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)), 0.0))
    _v = tl.maximum(tl.sum(_acc0, axis=0), (0.0 * (1.0 / 1.0)))
    tl.store(out_ptr + tl.program_id(0), _v)


def t024_s37(out, ins):
    grid = (1728,)
    t024_s37_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37], ins[38], ins[39], ins[40], ins[41], ins[42], ins[43], ins[44], ins[45], ins[46], ins[47], ins[48], ins[49], ins[50], ins[51], ins[52], ins[53], ins[54], ins[55], ins[56], ins[57], ins[58], ins[59], ins[60], ins[61], ins[62], ins[63], ins[64], ins[65], ins[66], ins[67], ins[68], ins[69], ins[70], ins[71], ins[72], ins[73], ins[74], ins[75], ins[76], ins[77], ins[78], ins[79], ins[80], ins[81], ins[82], ins[83], ins[84], ins[85], ins[86], ins[87], ins[88], ins[89], ins[90], ins[91], ins[92], ins[93], ins[94], ins[95], ins[96], ins[97], ins[98], ins[99], ins[100])
    return out


@triton.jit
def t024_s38_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr, in38_ptr, in39_ptr, in40_ptr, in41_ptr, in42_ptr, in43_ptr, in44_ptr, in45_ptr, in46_ptr, in47_ptr, in48_ptr, in49_ptr, in50_ptr, in51_ptr, in52_ptr, in53_ptr, in54_ptr, in55_ptr, in56_ptr, in57_ptr, in58_ptr, in59_ptr, in60_ptr, in61_ptr, in62_ptr, in63_ptr, in64_ptr, in65_ptr, in66_ptr, in67_ptr, in68_ptr, in69_ptr, in70_ptr, in71_ptr, in72_ptr, in73_ptr, in74_ptr, in75_ptr, in76_ptr, in77_ptr, in78_ptr, in79_ptr, in80_ptr, in81_ptr, in82_ptr, in83_ptr, in84_ptr, in85_ptr, in86_ptr, in87_ptr, in88_ptr, in89_ptr, in90_ptr, in91_ptr, in92_ptr, in93_ptr, in94_ptr, in95_ptr, in96_ptr, in97_ptr, in98_ptr, in99_ptr, in100_ptr, in101_ptr):
    _acc0 = tl.zeros([8], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 8) + tl.arange(0, 8)) < 9) & ((((1 <= ((((_lv0 * 8) + tl.arange(0, 8)) // 3) % 3)) & (((((_lv0 * 8) + tl.arange(0, 8)) // 3) % 3) < 2)) & (1 <= (((_lv0 * 8) + tl.arange(0, 8)) % 3))) & ((((_lv0 * 8) + tl.arange(0, 8)) % 3) < 2))), (tl.load(in101_ptr + (tl.maximum((((((tl.program_id(0) // 864) * 864) + (tl.program_id(0) % 864)) + tl.maximum(((((_lv0 * 8) + tl.arange(0, 8)) // 3) % 3) - 1, 0)) + tl.maximum((((_lv0 * 8) + tl.arange(0, 8)) % 3) - 1, 0)) - tl.maximum((((((tl.program_id(0) // 864) * 864) + (tl.program_id(0) % 864)) + tl.maximum(((((_lv0 * 8) + tl.arange(0, 8)) // 3) % 3) - 1, 0)) + tl.maximum((((_lv0 * 8) + tl.arange(0, 8)) % 3) - 1, 0)) - 1727, 0), 0) + 0 * tl.arange(0, 8)), mask=((((_lv0 * 8) + tl.arange(0, 8)) < 9) & ((((1 <= ((((_lv0 * 8) + tl.arange(0, 8)) // 3) % 3)) & (((((_lv0 * 8) + tl.arange(0, 8)) // 3) % 3) < 2)) & (1 <= (((_lv0 * 8) + tl.arange(0, 8)) % 3))) & ((((_lv0 * 8) + tl.arange(0, 8)) % 3) < 2))), other=0.0) * tl.load(in29_ptr + ((((((tl.program_id(0) % 864) * 3) + ((((_lv0 * 8) + tl.arange(0, 8)) // 3) % 3)) * 3) + (((_lv0 * 8) + tl.arange(0, 8)) % 3)) + 0 * tl.arange(0, 8)), mask=((((_lv0 * 8) + tl.arange(0, 8)) < 9) & ((((1 <= ((((_lv0 * 8) + tl.arange(0, 8)) // 3) % 3)) & (((((_lv0 * 8) + tl.arange(0, 8)) // 3) % 3) < 2)) & (1 <= (((_lv0 * 8) + tl.arange(0, 8)) % 3))) & ((((_lv0 * 8) + tl.arange(0, 8)) % 3) < 2))), other=0.0)), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t024_s38(out, ins):
    grid = (1728,)
    t024_s38_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37], ins[38], ins[39], ins[40], ins[41], ins[42], ins[43], ins[44], ins[45], ins[46], ins[47], ins[48], ins[49], ins[50], ins[51], ins[52], ins[53], ins[54], ins[55], ins[56], ins[57], ins[58], ins[59], ins[60], ins[61], ins[62], ins[63], ins[64], ins[65], ins[66], ins[67], ins[68], ins[69], ins[70], ins[71], ins[72], ins[73], ins[74], ins[75], ins[76], ins[77], ins[78], ins[79], ins[80], ins[81], ins[82], ins[83], ins[84], ins[85], ins[86], ins[87], ins[88], ins[89], ins[90], ins[91], ins[92], ins[93], ins[94], ins[95], ins[96], ins[97], ins[98], ins[99], ins[100], ins[101])
    return out


@triton.jit
def t024_s39_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr, in38_ptr, in39_ptr, in40_ptr, in41_ptr, in42_ptr, in43_ptr, in44_ptr, in45_ptr, in46_ptr, in47_ptr, in48_ptr, in49_ptr, in50_ptr, in51_ptr, in52_ptr, in53_ptr, in54_ptr, in55_ptr, in56_ptr, in57_ptr, in58_ptr, in59_ptr, in60_ptr, in61_ptr, in62_ptr, in63_ptr, in64_ptr, in65_ptr, in66_ptr, in67_ptr, in68_ptr, in69_ptr, in70_ptr, in71_ptr, in72_ptr, in73_ptr, in74_ptr, in75_ptr, in76_ptr, in77_ptr, in78_ptr, in79_ptr, in80_ptr, in81_ptr, in82_ptr, in83_ptr, in84_ptr, in85_ptr, in86_ptr, in87_ptr, in88_ptr, in89_ptr, in90_ptr, in91_ptr, in92_ptr, in93_ptr, in94_ptr, in95_ptr, in96_ptr, in97_ptr, in98_ptr, in99_ptr, in100_ptr, in101_ptr, in102_ptr):
    _acc0 = tl.zeros([2], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 2) + tl.arange(0, 2)) < 2) & True), tl.load(in102_ptr + (((((_lv0 * 2) + tl.arange(0, 2)) * 864) + tl.program_id(0)) + 0 * tl.arange(0, 2)), mask=((((_lv0 * 2) + tl.arange(0, 2)) < 2) & True), other=0.0), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t024_s39(out, ins):
    grid = (864,)
    t024_s39_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37], ins[38], ins[39], ins[40], ins[41], ins[42], ins[43], ins[44], ins[45], ins[46], ins[47], ins[48], ins[49], ins[50], ins[51], ins[52], ins[53], ins[54], ins[55], ins[56], ins[57], ins[58], ins[59], ins[60], ins[61], ins[62], ins[63], ins[64], ins[65], ins[66], ins[67], ins[68], ins[69], ins[70], ins[71], ins[72], ins[73], ins[74], ins[75], ins[76], ins[77], ins[78], ins[79], ins[80], ins[81], ins[82], ins[83], ins[84], ins[85], ins[86], ins[87], ins[88], ins[89], ins[90], ins[91], ins[92], ins[93], ins[94], ins[95], ins[96], ins[97], ins[98], ins[99], ins[100], ins[101], ins[102])
    return out


@triton.jit
def t024_s40_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr, in38_ptr, in39_ptr, in40_ptr, in41_ptr, in42_ptr, in43_ptr, in44_ptr, in45_ptr, in46_ptr, in47_ptr, in48_ptr, in49_ptr, in50_ptr, in51_ptr, in52_ptr, in53_ptr, in54_ptr, in55_ptr, in56_ptr, in57_ptr, in58_ptr, in59_ptr, in60_ptr, in61_ptr, in62_ptr, in63_ptr, in64_ptr, in65_ptr, in66_ptr, in67_ptr, in68_ptr, in69_ptr, in70_ptr, in71_ptr, in72_ptr, in73_ptr, in74_ptr, in75_ptr, in76_ptr, in77_ptr, in78_ptr, in79_ptr, in80_ptr, in81_ptr, in82_ptr, in83_ptr, in84_ptr, in85_ptr, in86_ptr, in87_ptr, in88_ptr, in89_ptr, in90_ptr, in91_ptr, in92_ptr, in93_ptr, in94_ptr, in95_ptr, in96_ptr, in97_ptr, in98_ptr, in99_ptr, in100_ptr, in101_ptr, in102_ptr, in103_ptr):
    _acc0 = tl.zeros([2], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 2) + tl.arange(0, 2)) < 2) & True), ((tl.load(in102_ptr + (((((_lv0 * 2) + tl.arange(0, 2)) * 864) + tl.program_id(0)) + 0 * tl.arange(0, 2)), mask=((((_lv0 * 2) + tl.arange(0, 2)) < 2) & True), other=0.0) - (tl.load(in103_ptr + (tl.program_id(0) + 0 * tl.arange(0, 2)), mask=((((_lv0 * 2) + tl.arange(0, 2)) < 2) & True), other=0.0) * (1.0 * (1.0 / 2.0)))) * (tl.load(in102_ptr + (((((_lv0 * 2) + tl.arange(0, 2)) * 864) + tl.program_id(0)) + 0 * tl.arange(0, 2)), mask=((((_lv0 * 2) + tl.arange(0, 2)) < 2) & True), other=0.0) - (tl.load(in103_ptr + (tl.program_id(0) + 0 * tl.arange(0, 2)), mask=((((_lv0 * 2) + tl.arange(0, 2)) < 2) & True), other=0.0) * (1.0 * (1.0 / 2.0))))), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t024_s40(out, ins):
    grid = (864,)
    t024_s40_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37], ins[38], ins[39], ins[40], ins[41], ins[42], ins[43], ins[44], ins[45], ins[46], ins[47], ins[48], ins[49], ins[50], ins[51], ins[52], ins[53], ins[54], ins[55], ins[56], ins[57], ins[58], ins[59], ins[60], ins[61], ins[62], ins[63], ins[64], ins[65], ins[66], ins[67], ins[68], ins[69], ins[70], ins[71], ins[72], ins[73], ins[74], ins[75], ins[76], ins[77], ins[78], ins[79], ins[80], ins[81], ins[82], ins[83], ins[84], ins[85], ins[86], ins[87], ins[88], ins[89], ins[90], ins[91], ins[92], ins[93], ins[94], ins[95], ins[96], ins[97], ins[98], ins[99], ins[100], ins[101], ins[102], ins[103])
    return out


@triton.jit
def t024_s41_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr, in38_ptr, in39_ptr, in40_ptr, in41_ptr, in42_ptr, in43_ptr, in44_ptr, in45_ptr, in46_ptr, in47_ptr, in48_ptr, in49_ptr, in50_ptr, in51_ptr, in52_ptr, in53_ptr, in54_ptr, in55_ptr, in56_ptr, in57_ptr, in58_ptr, in59_ptr, in60_ptr, in61_ptr, in62_ptr, in63_ptr, in64_ptr, in65_ptr, in66_ptr, in67_ptr, in68_ptr, in69_ptr, in70_ptr, in71_ptr, in72_ptr, in73_ptr, in74_ptr, in75_ptr, in76_ptr, in77_ptr, in78_ptr, in79_ptr, in80_ptr, in81_ptr, in82_ptr, in83_ptr, in84_ptr, in85_ptr, in86_ptr, in87_ptr, in88_ptr, in89_ptr, in90_ptr, in91_ptr, in92_ptr, in93_ptr, in94_ptr, in95_ptr, in96_ptr, in97_ptr, in98_ptr, in99_ptr, in100_ptr, in101_ptr, in102_ptr, in103_ptr, in104_ptr):
    _acc0 = tl.zeros([1], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), ((((tl.load(in102_ptr + (tl.program_id(0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) - (tl.load(in103_ptr + (tl.maximum((tl.program_id(0) % 864) - tl.maximum((tl.program_id(0) % 864) - 863, 0), 0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) * (1.0 * (1.0 / 2.0)))) * (1.0 / tl.sqrt(((tl.load(in104_ptr + (tl.maximum((tl.program_id(0) % 864) - tl.maximum((tl.program_id(0) % 864) - 863, 0), 0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) * (1.0 * (1.0 / 2.0))) + (1.0 * (1.0 / 100000.0)))))) * tl.load(in30_ptr + ((tl.program_id(0) % 864) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)) + tl.load(in31_ptr + ((tl.program_id(0) % 864) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)), 0.0))
    _v = tl.maximum(tl.sum(_acc0, axis=0), (0.0 * (1.0 / 1.0)))
    tl.store(out_ptr + tl.program_id(0), _v)


def t024_s41(out, ins):
    grid = (1728,)
    t024_s41_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37], ins[38], ins[39], ins[40], ins[41], ins[42], ins[43], ins[44], ins[45], ins[46], ins[47], ins[48], ins[49], ins[50], ins[51], ins[52], ins[53], ins[54], ins[55], ins[56], ins[57], ins[58], ins[59], ins[60], ins[61], ins[62], ins[63], ins[64], ins[65], ins[66], ins[67], ins[68], ins[69], ins[70], ins[71], ins[72], ins[73], ins[74], ins[75], ins[76], ins[77], ins[78], ins[79], ins[80], ins[81], ins[82], ins[83], ins[84], ins[85], ins[86], ins[87], ins[88], ins[89], ins[90], ins[91], ins[92], ins[93], ins[94], ins[95], ins[96], ins[97], ins[98], ins[99], ins[100], ins[101], ins[102], ins[103], ins[104])
    return out


@triton.jit
def t024_s42_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr, in38_ptr, in39_ptr, in40_ptr, in41_ptr, in42_ptr, in43_ptr, in44_ptr, in45_ptr, in46_ptr, in47_ptr, in48_ptr, in49_ptr, in50_ptr, in51_ptr, in52_ptr, in53_ptr, in54_ptr, in55_ptr, in56_ptr, in57_ptr, in58_ptr, in59_ptr, in60_ptr, in61_ptr, in62_ptr, in63_ptr, in64_ptr, in65_ptr, in66_ptr, in67_ptr, in68_ptr, in69_ptr, in70_ptr, in71_ptr, in72_ptr, in73_ptr, in74_ptr, in75_ptr, in76_ptr, in77_ptr, in78_ptr, in79_ptr, in80_ptr, in81_ptr, in82_ptr, in83_ptr, in84_ptr, in85_ptr, in86_ptr, in87_ptr, in88_ptr, in89_ptr, in90_ptr, in91_ptr, in92_ptr, in93_ptr, in94_ptr, in95_ptr, in96_ptr, in97_ptr, in98_ptr, in99_ptr, in100_ptr, in101_ptr, in102_ptr, in103_ptr, in104_ptr, in105_ptr):
    _acc0 = tl.zeros([1], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), tl.load(in105_ptr + (tl.maximum((tl.program_id(0) + ((_lv0 * 1) + tl.arange(0, 1))) - tl.maximum((tl.program_id(0) + ((_lv0 * 1) + tl.arange(0, 1))) - 1727, 0), 0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0), 0.0))
    _v = (tl.sum(_acc0, axis=0) * (1.0 * (1.0 / 1.0)))
    tl.store(out_ptr + tl.program_id(0), _v)


def t024_s42(out, ins):
    grid = (1728,)
    t024_s42_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37], ins[38], ins[39], ins[40], ins[41], ins[42], ins[43], ins[44], ins[45], ins[46], ins[47], ins[48], ins[49], ins[50], ins[51], ins[52], ins[53], ins[54], ins[55], ins[56], ins[57], ins[58], ins[59], ins[60], ins[61], ins[62], ins[63], ins[64], ins[65], ins[66], ins[67], ins[68], ins[69], ins[70], ins[71], ins[72], ins[73], ins[74], ins[75], ins[76], ins[77], ins[78], ins[79], ins[80], ins[81], ins[82], ins[83], ins[84], ins[85], ins[86], ins[87], ins[88], ins[89], ins[90], ins[91], ins[92], ins[93], ins[94], ins[95], ins[96], ins[97], ins[98], ins[99], ins[100], ins[101], ins[102], ins[103], ins[104], ins[105])
    return out


@triton.jit
def t024_s43_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr, in38_ptr, in39_ptr, in40_ptr, in41_ptr, in42_ptr, in43_ptr, in44_ptr, in45_ptr, in46_ptr, in47_ptr, in48_ptr, in49_ptr, in50_ptr, in51_ptr, in52_ptr, in53_ptr, in54_ptr, in55_ptr, in56_ptr, in57_ptr, in58_ptr, in59_ptr, in60_ptr, in61_ptr, in62_ptr, in63_ptr, in64_ptr, in65_ptr, in66_ptr, in67_ptr, in68_ptr, in69_ptr, in70_ptr, in71_ptr, in72_ptr, in73_ptr, in74_ptr, in75_ptr, in76_ptr, in77_ptr, in78_ptr, in79_ptr, in80_ptr, in81_ptr, in82_ptr, in83_ptr, in84_ptr, in85_ptr, in86_ptr, in87_ptr, in88_ptr, in89_ptr, in90_ptr, in91_ptr, in92_ptr, in93_ptr, in94_ptr, in95_ptr, in96_ptr, in97_ptr, in98_ptr, in99_ptr, in100_ptr, in101_ptr, in102_ptr, in103_ptr, in104_ptr, in105_ptr, in106_ptr):
    _acc0 = tl.zeros([512], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 512) + tl.arange(0, 512)) < 864) & ((0 < 1) & (0 < 1))), (tl.load(in106_ptr + ((((tl.program_id(0) // 216) * 864) + ((_lv0 * 512) + tl.arange(0, 512))) + 0 * tl.arange(0, 512)), mask=((((_lv0 * 512) + tl.arange(0, 512)) < 864) & ((0 < 1) & (0 < 1))), other=0.0) * tl.load(in32_ptr + ((((tl.program_id(0) % 216) * 864) + ((_lv0 * 512) + tl.arange(0, 512))) + 0 * tl.arange(0, 512)), mask=((((_lv0 * 512) + tl.arange(0, 512)) < 864) & ((0 < 1) & (0 < 1))), other=0.0)), 0.0))
    _v = tl.maximum(tl.sum(_acc0, axis=0), (0.0 * (1.0 / 1.0)))
    tl.store(out_ptr + tl.program_id(0), _v)


def t024_s43(out, ins):
    grid = (432,)
    t024_s43_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37], ins[38], ins[39], ins[40], ins[41], ins[42], ins[43], ins[44], ins[45], ins[46], ins[47], ins[48], ins[49], ins[50], ins[51], ins[52], ins[53], ins[54], ins[55], ins[56], ins[57], ins[58], ins[59], ins[60], ins[61], ins[62], ins[63], ins[64], ins[65], ins[66], ins[67], ins[68], ins[69], ins[70], ins[71], ins[72], ins[73], ins[74], ins[75], ins[76], ins[77], ins[78], ins[79], ins[80], ins[81], ins[82], ins[83], ins[84], ins[85], ins[86], ins[87], ins[88], ins[89], ins[90], ins[91], ins[92], ins[93], ins[94], ins[95], ins[96], ins[97], ins[98], ins[99], ins[100], ins[101], ins[102], ins[103], ins[104], ins[105], ins[106])
    return out


@triton.jit
def t024_s44_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr, in38_ptr, in39_ptr, in40_ptr, in41_ptr, in42_ptr, in43_ptr, in44_ptr, in45_ptr, in46_ptr, in47_ptr, in48_ptr, in49_ptr, in50_ptr, in51_ptr, in52_ptr, in53_ptr, in54_ptr, in55_ptr, in56_ptr, in57_ptr, in58_ptr, in59_ptr, in60_ptr, in61_ptr, in62_ptr, in63_ptr, in64_ptr, in65_ptr, in66_ptr, in67_ptr, in68_ptr, in69_ptr, in70_ptr, in71_ptr, in72_ptr, in73_ptr, in74_ptr, in75_ptr, in76_ptr, in77_ptr, in78_ptr, in79_ptr, in80_ptr, in81_ptr, in82_ptr, in83_ptr, in84_ptr, in85_ptr, in86_ptr, in87_ptr, in88_ptr, in89_ptr, in90_ptr, in91_ptr, in92_ptr, in93_ptr, in94_ptr, in95_ptr, in96_ptr, in97_ptr, in98_ptr, in99_ptr, in100_ptr, in101_ptr, in102_ptr, in103_ptr, in104_ptr, in105_ptr, in106_ptr, in107_ptr):
    _acc0 = tl.zeros([128], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 128) + tl.arange(0, 128)) < 216) & ((0 < 1) & (0 < 1))), (tl.load(in107_ptr + ((((tl.program_id(0) // 864) * 216) + ((_lv0 * 128) + tl.arange(0, 128))) + 0 * tl.arange(0, 128)), mask=((((_lv0 * 128) + tl.arange(0, 128)) < 216) & ((0 < 1) & (0 < 1))), other=0.0) * tl.load(in33_ptr + ((((tl.program_id(0) % 864) * 216) + ((_lv0 * 128) + tl.arange(0, 128))) + 0 * tl.arange(0, 128)), mask=((((_lv0 * 128) + tl.arange(0, 128)) < 216) & ((0 < 1) & (0 < 1))), other=0.0)), 0.0))
    _v = (1.0 / ((1.0 * (1.0 / 1.0)) + tl.exp(((0.0 * (1.0 / 1.0)) - tl.sum(_acc0, axis=0)))))
    tl.store(out_ptr + tl.program_id(0), _v)


def t024_s44(out, ins):
    grid = (1728,)
    t024_s44_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37], ins[38], ins[39], ins[40], ins[41], ins[42], ins[43], ins[44], ins[45], ins[46], ins[47], ins[48], ins[49], ins[50], ins[51], ins[52], ins[53], ins[54], ins[55], ins[56], ins[57], ins[58], ins[59], ins[60], ins[61], ins[62], ins[63], ins[64], ins[65], ins[66], ins[67], ins[68], ins[69], ins[70], ins[71], ins[72], ins[73], ins[74], ins[75], ins[76], ins[77], ins[78], ins[79], ins[80], ins[81], ins[82], ins[83], ins[84], ins[85], ins[86], ins[87], ins[88], ins[89], ins[90], ins[91], ins[92], ins[93], ins[94], ins[95], ins[96], ins[97], ins[98], ins[99], ins[100], ins[101], ins[102], ins[103], ins[104], ins[105], ins[106], ins[107])
    return out


@triton.jit
def t024_s45_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr, in38_ptr, in39_ptr, in40_ptr, in41_ptr, in42_ptr, in43_ptr, in44_ptr, in45_ptr, in46_ptr, in47_ptr, in48_ptr, in49_ptr, in50_ptr, in51_ptr, in52_ptr, in53_ptr, in54_ptr, in55_ptr, in56_ptr, in57_ptr, in58_ptr, in59_ptr, in60_ptr, in61_ptr, in62_ptr, in63_ptr, in64_ptr, in65_ptr, in66_ptr, in67_ptr, in68_ptr, in69_ptr, in70_ptr, in71_ptr, in72_ptr, in73_ptr, in74_ptr, in75_ptr, in76_ptr, in77_ptr, in78_ptr, in79_ptr, in80_ptr, in81_ptr, in82_ptr, in83_ptr, in84_ptr, in85_ptr, in86_ptr, in87_ptr, in88_ptr, in89_ptr, in90_ptr, in91_ptr, in92_ptr, in93_ptr, in94_ptr, in95_ptr, in96_ptr, in97_ptr, in98_ptr, in99_ptr, in100_ptr, in101_ptr, in102_ptr, in103_ptr, in104_ptr, in105_ptr, in106_ptr, in107_ptr, in108_ptr):
    _acc0 = tl.zeros([512], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 512) + tl.arange(0, 512)) < 864) & ((0 < 1) & (0 < 1))), (tl.load(in108_ptr + ((((tl.program_id(0) // 192) * 864) + ((_lv0 * 512) + tl.arange(0, 512))) + 0 * tl.arange(0, 512)), mask=((((_lv0 * 512) + tl.arange(0, 512)) < 864) & ((0 < 1) & (0 < 1))), other=0.0) * tl.load(in34_ptr + ((((tl.program_id(0) % 192) * 864) + ((_lv0 * 512) + tl.arange(0, 512))) + 0 * tl.arange(0, 512)), mask=((((_lv0 * 512) + tl.arange(0, 512)) < 864) & ((0 < 1) & (0 < 1))), other=0.0)), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t024_s45(out, ins):
    grid = (384,)
    t024_s45_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37], ins[38], ins[39], ins[40], ins[41], ins[42], ins[43], ins[44], ins[45], ins[46], ins[47], ins[48], ins[49], ins[50], ins[51], ins[52], ins[53], ins[54], ins[55], ins[56], ins[57], ins[58], ins[59], ins[60], ins[61], ins[62], ins[63], ins[64], ins[65], ins[66], ins[67], ins[68], ins[69], ins[70], ins[71], ins[72], ins[73], ins[74], ins[75], ins[76], ins[77], ins[78], ins[79], ins[80], ins[81], ins[82], ins[83], ins[84], ins[85], ins[86], ins[87], ins[88], ins[89], ins[90], ins[91], ins[92], ins[93], ins[94], ins[95], ins[96], ins[97], ins[98], ins[99], ins[100], ins[101], ins[102], ins[103], ins[104], ins[105], ins[106], ins[107], ins[108])
    return out


@triton.jit
def t024_s46_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr, in38_ptr, in39_ptr, in40_ptr, in41_ptr, in42_ptr, in43_ptr, in44_ptr, in45_ptr, in46_ptr, in47_ptr, in48_ptr, in49_ptr, in50_ptr, in51_ptr, in52_ptr, in53_ptr, in54_ptr, in55_ptr, in56_ptr, in57_ptr, in58_ptr, in59_ptr, in60_ptr, in61_ptr, in62_ptr, in63_ptr, in64_ptr, in65_ptr, in66_ptr, in67_ptr, in68_ptr, in69_ptr, in70_ptr, in71_ptr, in72_ptr, in73_ptr, in74_ptr, in75_ptr, in76_ptr, in77_ptr, in78_ptr, in79_ptr, in80_ptr, in81_ptr, in82_ptr, in83_ptr, in84_ptr, in85_ptr, in86_ptr, in87_ptr, in88_ptr, in89_ptr, in90_ptr, in91_ptr, in92_ptr, in93_ptr, in94_ptr, in95_ptr, in96_ptr, in97_ptr, in98_ptr, in99_ptr, in100_ptr, in101_ptr, in102_ptr, in103_ptr, in104_ptr, in105_ptr, in106_ptr, in107_ptr, in108_ptr, in109_ptr):
    _acc0 = tl.zeros([2], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 2) + tl.arange(0, 2)) < 2) & True), tl.load(in109_ptr + (((((_lv0 * 2) + tl.arange(0, 2)) * 192) + tl.program_id(0)) + 0 * tl.arange(0, 2)), mask=((((_lv0 * 2) + tl.arange(0, 2)) < 2) & True), other=0.0), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t024_s46(out, ins):
    grid = (192,)
    t024_s46_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37], ins[38], ins[39], ins[40], ins[41], ins[42], ins[43], ins[44], ins[45], ins[46], ins[47], ins[48], ins[49], ins[50], ins[51], ins[52], ins[53], ins[54], ins[55], ins[56], ins[57], ins[58], ins[59], ins[60], ins[61], ins[62], ins[63], ins[64], ins[65], ins[66], ins[67], ins[68], ins[69], ins[70], ins[71], ins[72], ins[73], ins[74], ins[75], ins[76], ins[77], ins[78], ins[79], ins[80], ins[81], ins[82], ins[83], ins[84], ins[85], ins[86], ins[87], ins[88], ins[89], ins[90], ins[91], ins[92], ins[93], ins[94], ins[95], ins[96], ins[97], ins[98], ins[99], ins[100], ins[101], ins[102], ins[103], ins[104], ins[105], ins[106], ins[107], ins[108], ins[109])
    return out


@triton.jit
def t024_s47_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr, in38_ptr, in39_ptr, in40_ptr, in41_ptr, in42_ptr, in43_ptr, in44_ptr, in45_ptr, in46_ptr, in47_ptr, in48_ptr, in49_ptr, in50_ptr, in51_ptr, in52_ptr, in53_ptr, in54_ptr, in55_ptr, in56_ptr, in57_ptr, in58_ptr, in59_ptr, in60_ptr, in61_ptr, in62_ptr, in63_ptr, in64_ptr, in65_ptr, in66_ptr, in67_ptr, in68_ptr, in69_ptr, in70_ptr, in71_ptr, in72_ptr, in73_ptr, in74_ptr, in75_ptr, in76_ptr, in77_ptr, in78_ptr, in79_ptr, in80_ptr, in81_ptr, in82_ptr, in83_ptr, in84_ptr, in85_ptr, in86_ptr, in87_ptr, in88_ptr, in89_ptr, in90_ptr, in91_ptr, in92_ptr, in93_ptr, in94_ptr, in95_ptr, in96_ptr, in97_ptr, in98_ptr, in99_ptr, in100_ptr, in101_ptr, in102_ptr, in103_ptr, in104_ptr, in105_ptr, in106_ptr, in107_ptr, in108_ptr, in109_ptr, in110_ptr):
    _acc0 = tl.zeros([2], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 2) + tl.arange(0, 2)) < 2) & True), ((tl.load(in109_ptr + (((((_lv0 * 2) + tl.arange(0, 2)) * 192) + tl.program_id(0)) + 0 * tl.arange(0, 2)), mask=((((_lv0 * 2) + tl.arange(0, 2)) < 2) & True), other=0.0) - (tl.load(in110_ptr + (tl.program_id(0) + 0 * tl.arange(0, 2)), mask=((((_lv0 * 2) + tl.arange(0, 2)) < 2) & True), other=0.0) * (1.0 * (1.0 / 2.0)))) * (tl.load(in109_ptr + (((((_lv0 * 2) + tl.arange(0, 2)) * 192) + tl.program_id(0)) + 0 * tl.arange(0, 2)), mask=((((_lv0 * 2) + tl.arange(0, 2)) < 2) & True), other=0.0) - (tl.load(in110_ptr + (tl.program_id(0) + 0 * tl.arange(0, 2)), mask=((((_lv0 * 2) + tl.arange(0, 2)) < 2) & True), other=0.0) * (1.0 * (1.0 / 2.0))))), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t024_s47(out, ins):
    grid = (192,)
    t024_s47_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37], ins[38], ins[39], ins[40], ins[41], ins[42], ins[43], ins[44], ins[45], ins[46], ins[47], ins[48], ins[49], ins[50], ins[51], ins[52], ins[53], ins[54], ins[55], ins[56], ins[57], ins[58], ins[59], ins[60], ins[61], ins[62], ins[63], ins[64], ins[65], ins[66], ins[67], ins[68], ins[69], ins[70], ins[71], ins[72], ins[73], ins[74], ins[75], ins[76], ins[77], ins[78], ins[79], ins[80], ins[81], ins[82], ins[83], ins[84], ins[85], ins[86], ins[87], ins[88], ins[89], ins[90], ins[91], ins[92], ins[93], ins[94], ins[95], ins[96], ins[97], ins[98], ins[99], ins[100], ins[101], ins[102], ins[103], ins[104], ins[105], ins[106], ins[107], ins[108], ins[109], ins[110])
    return out


@triton.jit
def t024_s48_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr, in38_ptr, in39_ptr, in40_ptr, in41_ptr, in42_ptr, in43_ptr, in44_ptr, in45_ptr, in46_ptr, in47_ptr, in48_ptr, in49_ptr, in50_ptr, in51_ptr, in52_ptr, in53_ptr, in54_ptr, in55_ptr, in56_ptr, in57_ptr, in58_ptr, in59_ptr, in60_ptr, in61_ptr, in62_ptr, in63_ptr, in64_ptr, in65_ptr, in66_ptr, in67_ptr, in68_ptr, in69_ptr, in70_ptr, in71_ptr, in72_ptr, in73_ptr, in74_ptr, in75_ptr, in76_ptr, in77_ptr, in78_ptr, in79_ptr, in80_ptr, in81_ptr, in82_ptr, in83_ptr, in84_ptr, in85_ptr, in86_ptr, in87_ptr, in88_ptr, in89_ptr, in90_ptr, in91_ptr, in92_ptr, in93_ptr, in94_ptr, in95_ptr, in96_ptr, in97_ptr, in98_ptr, in99_ptr, in100_ptr, in101_ptr, in102_ptr, in103_ptr, in104_ptr, in105_ptr, in106_ptr, in107_ptr, in108_ptr, in109_ptr, in110_ptr, in111_ptr):
    _acc0 = tl.zeros([1], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), ((((tl.load(in109_ptr + (tl.program_id(0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) - (tl.load(in110_ptr + (tl.maximum((tl.program_id(0) % 192) - tl.maximum((tl.program_id(0) % 192) - 191, 0), 0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) * (1.0 * (1.0 / 2.0)))) * (1.0 / tl.sqrt(((tl.load(in111_ptr + (tl.maximum((tl.program_id(0) % 192) - tl.maximum((tl.program_id(0) % 192) - 191, 0), 0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) * (1.0 * (1.0 / 2.0))) + (1.0 * (1.0 / 100000.0)))))) * tl.load(in35_ptr + ((tl.program_id(0) % 192) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)) + tl.load(in36_ptr + ((tl.program_id(0) % 192) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t024_s48(out, ins):
    grid = (384,)
    t024_s48_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37], ins[38], ins[39], ins[40], ins[41], ins[42], ins[43], ins[44], ins[45], ins[46], ins[47], ins[48], ins[49], ins[50], ins[51], ins[52], ins[53], ins[54], ins[55], ins[56], ins[57], ins[58], ins[59], ins[60], ins[61], ins[62], ins[63], ins[64], ins[65], ins[66], ins[67], ins[68], ins[69], ins[70], ins[71], ins[72], ins[73], ins[74], ins[75], ins[76], ins[77], ins[78], ins[79], ins[80], ins[81], ins[82], ins[83], ins[84], ins[85], ins[86], ins[87], ins[88], ins[89], ins[90], ins[91], ins[92], ins[93], ins[94], ins[95], ins[96], ins[97], ins[98], ins[99], ins[100], ins[101], ins[102], ins[103], ins[104], ins[105], ins[106], ins[107], ins[108], ins[109], ins[110], ins[111])
    return out


@triton.jit
def t024_s49_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr, in38_ptr, in39_ptr, in40_ptr, in41_ptr, in42_ptr, in43_ptr, in44_ptr, in45_ptr, in46_ptr, in47_ptr, in48_ptr, in49_ptr, in50_ptr, in51_ptr, in52_ptr, in53_ptr, in54_ptr, in55_ptr, in56_ptr, in57_ptr, in58_ptr, in59_ptr, in60_ptr, in61_ptr, in62_ptr, in63_ptr, in64_ptr, in65_ptr, in66_ptr, in67_ptr, in68_ptr, in69_ptr, in70_ptr, in71_ptr, in72_ptr, in73_ptr, in74_ptr, in75_ptr, in76_ptr, in77_ptr, in78_ptr, in79_ptr, in80_ptr, in81_ptr, in82_ptr, in83_ptr, in84_ptr, in85_ptr, in86_ptr, in87_ptr, in88_ptr, in89_ptr, in90_ptr, in91_ptr, in92_ptr, in93_ptr, in94_ptr, in95_ptr, in96_ptr, in97_ptr, in98_ptr, in99_ptr, in100_ptr, in101_ptr, in102_ptr, in103_ptr, in104_ptr, in105_ptr, in106_ptr, in107_ptr, in108_ptr, in109_ptr, in110_ptr, in111_ptr, in112_ptr):
    _acc0 = tl.zeros([128], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 128) + tl.arange(0, 128)) < 192) & ((0 < 1) & (0 < 1))), (tl.load(in112_ptr + ((((tl.program_id(0) // 1152) * 192) + ((_lv0 * 128) + tl.arange(0, 128))) + 0 * tl.arange(0, 128)), mask=((((_lv0 * 128) + tl.arange(0, 128)) < 192) & ((0 < 1) & (0 < 1))), other=0.0) * tl.load(in37_ptr + ((((tl.program_id(0) % 1152) * 192) + ((_lv0 * 128) + tl.arange(0, 128))) + 0 * tl.arange(0, 128)), mask=((((_lv0 * 128) + tl.arange(0, 128)) < 192) & ((0 < 1) & (0 < 1))), other=0.0)), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t024_s49(out, ins):
    grid = (2304,)
    t024_s49_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37], ins[38], ins[39], ins[40], ins[41], ins[42], ins[43], ins[44], ins[45], ins[46], ins[47], ins[48], ins[49], ins[50], ins[51], ins[52], ins[53], ins[54], ins[55], ins[56], ins[57], ins[58], ins[59], ins[60], ins[61], ins[62], ins[63], ins[64], ins[65], ins[66], ins[67], ins[68], ins[69], ins[70], ins[71], ins[72], ins[73], ins[74], ins[75], ins[76], ins[77], ins[78], ins[79], ins[80], ins[81], ins[82], ins[83], ins[84], ins[85], ins[86], ins[87], ins[88], ins[89], ins[90], ins[91], ins[92], ins[93], ins[94], ins[95], ins[96], ins[97], ins[98], ins[99], ins[100], ins[101], ins[102], ins[103], ins[104], ins[105], ins[106], ins[107], ins[108], ins[109], ins[110], ins[111], ins[112])
    return out


@triton.jit
def t024_s50_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr, in38_ptr, in39_ptr, in40_ptr, in41_ptr, in42_ptr, in43_ptr, in44_ptr, in45_ptr, in46_ptr, in47_ptr, in48_ptr, in49_ptr, in50_ptr, in51_ptr, in52_ptr, in53_ptr, in54_ptr, in55_ptr, in56_ptr, in57_ptr, in58_ptr, in59_ptr, in60_ptr, in61_ptr, in62_ptr, in63_ptr, in64_ptr, in65_ptr, in66_ptr, in67_ptr, in68_ptr, in69_ptr, in70_ptr, in71_ptr, in72_ptr, in73_ptr, in74_ptr, in75_ptr, in76_ptr, in77_ptr, in78_ptr, in79_ptr, in80_ptr, in81_ptr, in82_ptr, in83_ptr, in84_ptr, in85_ptr, in86_ptr, in87_ptr, in88_ptr, in89_ptr, in90_ptr, in91_ptr, in92_ptr, in93_ptr, in94_ptr, in95_ptr, in96_ptr, in97_ptr, in98_ptr, in99_ptr, in100_ptr, in101_ptr, in102_ptr, in103_ptr, in104_ptr, in105_ptr, in106_ptr, in107_ptr, in108_ptr, in109_ptr, in110_ptr, in111_ptr, in112_ptr, in113_ptr):
    _acc0 = tl.zeros([2], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 2) + tl.arange(0, 2)) < 2) & True), tl.load(in113_ptr + (((((_lv0 * 2) + tl.arange(0, 2)) * 1152) + tl.program_id(0)) + 0 * tl.arange(0, 2)), mask=((((_lv0 * 2) + tl.arange(0, 2)) < 2) & True), other=0.0), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t024_s50(out, ins):
    grid = (1152,)
    t024_s50_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37], ins[38], ins[39], ins[40], ins[41], ins[42], ins[43], ins[44], ins[45], ins[46], ins[47], ins[48], ins[49], ins[50], ins[51], ins[52], ins[53], ins[54], ins[55], ins[56], ins[57], ins[58], ins[59], ins[60], ins[61], ins[62], ins[63], ins[64], ins[65], ins[66], ins[67], ins[68], ins[69], ins[70], ins[71], ins[72], ins[73], ins[74], ins[75], ins[76], ins[77], ins[78], ins[79], ins[80], ins[81], ins[82], ins[83], ins[84], ins[85], ins[86], ins[87], ins[88], ins[89], ins[90], ins[91], ins[92], ins[93], ins[94], ins[95], ins[96], ins[97], ins[98], ins[99], ins[100], ins[101], ins[102], ins[103], ins[104], ins[105], ins[106], ins[107], ins[108], ins[109], ins[110], ins[111], ins[112], ins[113])
    return out


@triton.jit
def t024_s51_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr, in38_ptr, in39_ptr, in40_ptr, in41_ptr, in42_ptr, in43_ptr, in44_ptr, in45_ptr, in46_ptr, in47_ptr, in48_ptr, in49_ptr, in50_ptr, in51_ptr, in52_ptr, in53_ptr, in54_ptr, in55_ptr, in56_ptr, in57_ptr, in58_ptr, in59_ptr, in60_ptr, in61_ptr, in62_ptr, in63_ptr, in64_ptr, in65_ptr, in66_ptr, in67_ptr, in68_ptr, in69_ptr, in70_ptr, in71_ptr, in72_ptr, in73_ptr, in74_ptr, in75_ptr, in76_ptr, in77_ptr, in78_ptr, in79_ptr, in80_ptr, in81_ptr, in82_ptr, in83_ptr, in84_ptr, in85_ptr, in86_ptr, in87_ptr, in88_ptr, in89_ptr, in90_ptr, in91_ptr, in92_ptr, in93_ptr, in94_ptr, in95_ptr, in96_ptr, in97_ptr, in98_ptr, in99_ptr, in100_ptr, in101_ptr, in102_ptr, in103_ptr, in104_ptr, in105_ptr, in106_ptr, in107_ptr, in108_ptr, in109_ptr, in110_ptr, in111_ptr, in112_ptr, in113_ptr, in114_ptr):
    _acc0 = tl.zeros([2], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 2) + tl.arange(0, 2)) < 2) & True), ((tl.load(in113_ptr + (((((_lv0 * 2) + tl.arange(0, 2)) * 1152) + tl.program_id(0)) + 0 * tl.arange(0, 2)), mask=((((_lv0 * 2) + tl.arange(0, 2)) < 2) & True), other=0.0) - (tl.load(in114_ptr + (tl.program_id(0) + 0 * tl.arange(0, 2)), mask=((((_lv0 * 2) + tl.arange(0, 2)) < 2) & True), other=0.0) * (1.0 * (1.0 / 2.0)))) * (tl.load(in113_ptr + (((((_lv0 * 2) + tl.arange(0, 2)) * 1152) + tl.program_id(0)) + 0 * tl.arange(0, 2)), mask=((((_lv0 * 2) + tl.arange(0, 2)) < 2) & True), other=0.0) - (tl.load(in114_ptr + (tl.program_id(0) + 0 * tl.arange(0, 2)), mask=((((_lv0 * 2) + tl.arange(0, 2)) < 2) & True), other=0.0) * (1.0 * (1.0 / 2.0))))), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t024_s51(out, ins):
    grid = (1152,)
    t024_s51_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37], ins[38], ins[39], ins[40], ins[41], ins[42], ins[43], ins[44], ins[45], ins[46], ins[47], ins[48], ins[49], ins[50], ins[51], ins[52], ins[53], ins[54], ins[55], ins[56], ins[57], ins[58], ins[59], ins[60], ins[61], ins[62], ins[63], ins[64], ins[65], ins[66], ins[67], ins[68], ins[69], ins[70], ins[71], ins[72], ins[73], ins[74], ins[75], ins[76], ins[77], ins[78], ins[79], ins[80], ins[81], ins[82], ins[83], ins[84], ins[85], ins[86], ins[87], ins[88], ins[89], ins[90], ins[91], ins[92], ins[93], ins[94], ins[95], ins[96], ins[97], ins[98], ins[99], ins[100], ins[101], ins[102], ins[103], ins[104], ins[105], ins[106], ins[107], ins[108], ins[109], ins[110], ins[111], ins[112], ins[113], ins[114])
    return out


@triton.jit
def t024_s52_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr, in38_ptr, in39_ptr, in40_ptr, in41_ptr, in42_ptr, in43_ptr, in44_ptr, in45_ptr, in46_ptr, in47_ptr, in48_ptr, in49_ptr, in50_ptr, in51_ptr, in52_ptr, in53_ptr, in54_ptr, in55_ptr, in56_ptr, in57_ptr, in58_ptr, in59_ptr, in60_ptr, in61_ptr, in62_ptr, in63_ptr, in64_ptr, in65_ptr, in66_ptr, in67_ptr, in68_ptr, in69_ptr, in70_ptr, in71_ptr, in72_ptr, in73_ptr, in74_ptr, in75_ptr, in76_ptr, in77_ptr, in78_ptr, in79_ptr, in80_ptr, in81_ptr, in82_ptr, in83_ptr, in84_ptr, in85_ptr, in86_ptr, in87_ptr, in88_ptr, in89_ptr, in90_ptr, in91_ptr, in92_ptr, in93_ptr, in94_ptr, in95_ptr, in96_ptr, in97_ptr, in98_ptr, in99_ptr, in100_ptr, in101_ptr, in102_ptr, in103_ptr, in104_ptr, in105_ptr, in106_ptr, in107_ptr, in108_ptr, in109_ptr, in110_ptr, in111_ptr, in112_ptr, in113_ptr, in114_ptr, in115_ptr):
    _acc0 = tl.zeros([1], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), ((((tl.load(in113_ptr + (tl.program_id(0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) - (tl.load(in114_ptr + (tl.maximum((tl.program_id(0) % 1152) - tl.maximum((tl.program_id(0) % 1152) - 1151, 0), 0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) * (1.0 * (1.0 / 2.0)))) * (1.0 / tl.sqrt(((tl.load(in115_ptr + (tl.maximum((tl.program_id(0) % 1152) - tl.maximum((tl.program_id(0) % 1152) - 1151, 0), 0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) * (1.0 * (1.0 / 2.0))) + (1.0 * (1.0 / 100000.0)))))) * tl.load(in38_ptr + ((tl.program_id(0) % 1152) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)) + tl.load(in39_ptr + ((tl.program_id(0) % 1152) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)), 0.0))
    _v = tl.maximum(tl.sum(_acc0, axis=0), (0.0 * (1.0 / 1.0)))
    tl.store(out_ptr + tl.program_id(0), _v)


def t024_s52(out, ins):
    grid = (2304,)
    t024_s52_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37], ins[38], ins[39], ins[40], ins[41], ins[42], ins[43], ins[44], ins[45], ins[46], ins[47], ins[48], ins[49], ins[50], ins[51], ins[52], ins[53], ins[54], ins[55], ins[56], ins[57], ins[58], ins[59], ins[60], ins[61], ins[62], ins[63], ins[64], ins[65], ins[66], ins[67], ins[68], ins[69], ins[70], ins[71], ins[72], ins[73], ins[74], ins[75], ins[76], ins[77], ins[78], ins[79], ins[80], ins[81], ins[82], ins[83], ins[84], ins[85], ins[86], ins[87], ins[88], ins[89], ins[90], ins[91], ins[92], ins[93], ins[94], ins[95], ins[96], ins[97], ins[98], ins[99], ins[100], ins[101], ins[102], ins[103], ins[104], ins[105], ins[106], ins[107], ins[108], ins[109], ins[110], ins[111], ins[112], ins[113], ins[114], ins[115])
    return out


@triton.jit
def t024_s53_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr, in38_ptr, in39_ptr, in40_ptr, in41_ptr, in42_ptr, in43_ptr, in44_ptr, in45_ptr, in46_ptr, in47_ptr, in48_ptr, in49_ptr, in50_ptr, in51_ptr, in52_ptr, in53_ptr, in54_ptr, in55_ptr, in56_ptr, in57_ptr, in58_ptr, in59_ptr, in60_ptr, in61_ptr, in62_ptr, in63_ptr, in64_ptr, in65_ptr, in66_ptr, in67_ptr, in68_ptr, in69_ptr, in70_ptr, in71_ptr, in72_ptr, in73_ptr, in74_ptr, in75_ptr, in76_ptr, in77_ptr, in78_ptr, in79_ptr, in80_ptr, in81_ptr, in82_ptr, in83_ptr, in84_ptr, in85_ptr, in86_ptr, in87_ptr, in88_ptr, in89_ptr, in90_ptr, in91_ptr, in92_ptr, in93_ptr, in94_ptr, in95_ptr, in96_ptr, in97_ptr, in98_ptr, in99_ptr, in100_ptr, in101_ptr, in102_ptr, in103_ptr, in104_ptr, in105_ptr, in106_ptr, in107_ptr, in108_ptr, in109_ptr, in110_ptr, in111_ptr, in112_ptr, in113_ptr, in114_ptr, in115_ptr, in116_ptr):
    _acc0 = tl.zeros([8], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 8) + tl.arange(0, 8)) < 9) & ((((1 <= ((((_lv0 * 8) + tl.arange(0, 8)) // 3) % 3)) & (((((_lv0 * 8) + tl.arange(0, 8)) // 3) % 3) < 2)) & (1 <= (((_lv0 * 8) + tl.arange(0, 8)) % 3))) & ((((_lv0 * 8) + tl.arange(0, 8)) % 3) < 2))), (tl.load(in116_ptr + (tl.maximum((((((tl.program_id(0) // 1152) * 1152) + (tl.program_id(0) % 1152)) + tl.maximum(((((_lv0 * 8) + tl.arange(0, 8)) // 3) % 3) - 1, 0)) + tl.maximum((((_lv0 * 8) + tl.arange(0, 8)) % 3) - 1, 0)) - tl.maximum((((((tl.program_id(0) // 1152) * 1152) + (tl.program_id(0) % 1152)) + tl.maximum(((((_lv0 * 8) + tl.arange(0, 8)) // 3) % 3) - 1, 0)) + tl.maximum((((_lv0 * 8) + tl.arange(0, 8)) % 3) - 1, 0)) - 2303, 0), 0) + 0 * tl.arange(0, 8)), mask=((((_lv0 * 8) + tl.arange(0, 8)) < 9) & ((((1 <= ((((_lv0 * 8) + tl.arange(0, 8)) // 3) % 3)) & (((((_lv0 * 8) + tl.arange(0, 8)) // 3) % 3) < 2)) & (1 <= (((_lv0 * 8) + tl.arange(0, 8)) % 3))) & ((((_lv0 * 8) + tl.arange(0, 8)) % 3) < 2))), other=0.0) * tl.load(in40_ptr + ((((((tl.program_id(0) % 1152) * 3) + ((((_lv0 * 8) + tl.arange(0, 8)) // 3) % 3)) * 3) + (((_lv0 * 8) + tl.arange(0, 8)) % 3)) + 0 * tl.arange(0, 8)), mask=((((_lv0 * 8) + tl.arange(0, 8)) < 9) & ((((1 <= ((((_lv0 * 8) + tl.arange(0, 8)) // 3) % 3)) & (((((_lv0 * 8) + tl.arange(0, 8)) // 3) % 3) < 2)) & (1 <= (((_lv0 * 8) + tl.arange(0, 8)) % 3))) & ((((_lv0 * 8) + tl.arange(0, 8)) % 3) < 2))), other=0.0)), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t024_s53(out, ins):
    grid = (2304,)
    t024_s53_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37], ins[38], ins[39], ins[40], ins[41], ins[42], ins[43], ins[44], ins[45], ins[46], ins[47], ins[48], ins[49], ins[50], ins[51], ins[52], ins[53], ins[54], ins[55], ins[56], ins[57], ins[58], ins[59], ins[60], ins[61], ins[62], ins[63], ins[64], ins[65], ins[66], ins[67], ins[68], ins[69], ins[70], ins[71], ins[72], ins[73], ins[74], ins[75], ins[76], ins[77], ins[78], ins[79], ins[80], ins[81], ins[82], ins[83], ins[84], ins[85], ins[86], ins[87], ins[88], ins[89], ins[90], ins[91], ins[92], ins[93], ins[94], ins[95], ins[96], ins[97], ins[98], ins[99], ins[100], ins[101], ins[102], ins[103], ins[104], ins[105], ins[106], ins[107], ins[108], ins[109], ins[110], ins[111], ins[112], ins[113], ins[114], ins[115], ins[116])
    return out


@triton.jit
def t024_s54_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr, in38_ptr, in39_ptr, in40_ptr, in41_ptr, in42_ptr, in43_ptr, in44_ptr, in45_ptr, in46_ptr, in47_ptr, in48_ptr, in49_ptr, in50_ptr, in51_ptr, in52_ptr, in53_ptr, in54_ptr, in55_ptr, in56_ptr, in57_ptr, in58_ptr, in59_ptr, in60_ptr, in61_ptr, in62_ptr, in63_ptr, in64_ptr, in65_ptr, in66_ptr, in67_ptr, in68_ptr, in69_ptr, in70_ptr, in71_ptr, in72_ptr, in73_ptr, in74_ptr, in75_ptr, in76_ptr, in77_ptr, in78_ptr, in79_ptr, in80_ptr, in81_ptr, in82_ptr, in83_ptr, in84_ptr, in85_ptr, in86_ptr, in87_ptr, in88_ptr, in89_ptr, in90_ptr, in91_ptr, in92_ptr, in93_ptr, in94_ptr, in95_ptr, in96_ptr, in97_ptr, in98_ptr, in99_ptr, in100_ptr, in101_ptr, in102_ptr, in103_ptr, in104_ptr, in105_ptr, in106_ptr, in107_ptr, in108_ptr, in109_ptr, in110_ptr, in111_ptr, in112_ptr, in113_ptr, in114_ptr, in115_ptr, in116_ptr, in117_ptr):
    _acc0 = tl.zeros([2], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 2) + tl.arange(0, 2)) < 2) & True), tl.load(in117_ptr + (((((_lv0 * 2) + tl.arange(0, 2)) * 1152) + tl.program_id(0)) + 0 * tl.arange(0, 2)), mask=((((_lv0 * 2) + tl.arange(0, 2)) < 2) & True), other=0.0), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t024_s54(out, ins):
    grid = (1152,)
    t024_s54_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37], ins[38], ins[39], ins[40], ins[41], ins[42], ins[43], ins[44], ins[45], ins[46], ins[47], ins[48], ins[49], ins[50], ins[51], ins[52], ins[53], ins[54], ins[55], ins[56], ins[57], ins[58], ins[59], ins[60], ins[61], ins[62], ins[63], ins[64], ins[65], ins[66], ins[67], ins[68], ins[69], ins[70], ins[71], ins[72], ins[73], ins[74], ins[75], ins[76], ins[77], ins[78], ins[79], ins[80], ins[81], ins[82], ins[83], ins[84], ins[85], ins[86], ins[87], ins[88], ins[89], ins[90], ins[91], ins[92], ins[93], ins[94], ins[95], ins[96], ins[97], ins[98], ins[99], ins[100], ins[101], ins[102], ins[103], ins[104], ins[105], ins[106], ins[107], ins[108], ins[109], ins[110], ins[111], ins[112], ins[113], ins[114], ins[115], ins[116], ins[117])
    return out


@triton.jit
def t024_s55_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr, in38_ptr, in39_ptr, in40_ptr, in41_ptr, in42_ptr, in43_ptr, in44_ptr, in45_ptr, in46_ptr, in47_ptr, in48_ptr, in49_ptr, in50_ptr, in51_ptr, in52_ptr, in53_ptr, in54_ptr, in55_ptr, in56_ptr, in57_ptr, in58_ptr, in59_ptr, in60_ptr, in61_ptr, in62_ptr, in63_ptr, in64_ptr, in65_ptr, in66_ptr, in67_ptr, in68_ptr, in69_ptr, in70_ptr, in71_ptr, in72_ptr, in73_ptr, in74_ptr, in75_ptr, in76_ptr, in77_ptr, in78_ptr, in79_ptr, in80_ptr, in81_ptr, in82_ptr, in83_ptr, in84_ptr, in85_ptr, in86_ptr, in87_ptr, in88_ptr, in89_ptr, in90_ptr, in91_ptr, in92_ptr, in93_ptr, in94_ptr, in95_ptr, in96_ptr, in97_ptr, in98_ptr, in99_ptr, in100_ptr, in101_ptr, in102_ptr, in103_ptr, in104_ptr, in105_ptr, in106_ptr, in107_ptr, in108_ptr, in109_ptr, in110_ptr, in111_ptr, in112_ptr, in113_ptr, in114_ptr, in115_ptr, in116_ptr, in117_ptr, in118_ptr):
    _acc0 = tl.zeros([2], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 2) + tl.arange(0, 2)) < 2) & True), ((tl.load(in117_ptr + (((((_lv0 * 2) + tl.arange(0, 2)) * 1152) + tl.program_id(0)) + 0 * tl.arange(0, 2)), mask=((((_lv0 * 2) + tl.arange(0, 2)) < 2) & True), other=0.0) - (tl.load(in118_ptr + (tl.program_id(0) + 0 * tl.arange(0, 2)), mask=((((_lv0 * 2) + tl.arange(0, 2)) < 2) & True), other=0.0) * (1.0 * (1.0 / 2.0)))) * (tl.load(in117_ptr + (((((_lv0 * 2) + tl.arange(0, 2)) * 1152) + tl.program_id(0)) + 0 * tl.arange(0, 2)), mask=((((_lv0 * 2) + tl.arange(0, 2)) < 2) & True), other=0.0) - (tl.load(in118_ptr + (tl.program_id(0) + 0 * tl.arange(0, 2)), mask=((((_lv0 * 2) + tl.arange(0, 2)) < 2) & True), other=0.0) * (1.0 * (1.0 / 2.0))))), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t024_s55(out, ins):
    grid = (1152,)
    t024_s55_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37], ins[38], ins[39], ins[40], ins[41], ins[42], ins[43], ins[44], ins[45], ins[46], ins[47], ins[48], ins[49], ins[50], ins[51], ins[52], ins[53], ins[54], ins[55], ins[56], ins[57], ins[58], ins[59], ins[60], ins[61], ins[62], ins[63], ins[64], ins[65], ins[66], ins[67], ins[68], ins[69], ins[70], ins[71], ins[72], ins[73], ins[74], ins[75], ins[76], ins[77], ins[78], ins[79], ins[80], ins[81], ins[82], ins[83], ins[84], ins[85], ins[86], ins[87], ins[88], ins[89], ins[90], ins[91], ins[92], ins[93], ins[94], ins[95], ins[96], ins[97], ins[98], ins[99], ins[100], ins[101], ins[102], ins[103], ins[104], ins[105], ins[106], ins[107], ins[108], ins[109], ins[110], ins[111], ins[112], ins[113], ins[114], ins[115], ins[116], ins[117], ins[118])
    return out


@triton.jit
def t024_s56_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr, in38_ptr, in39_ptr, in40_ptr, in41_ptr, in42_ptr, in43_ptr, in44_ptr, in45_ptr, in46_ptr, in47_ptr, in48_ptr, in49_ptr, in50_ptr, in51_ptr, in52_ptr, in53_ptr, in54_ptr, in55_ptr, in56_ptr, in57_ptr, in58_ptr, in59_ptr, in60_ptr, in61_ptr, in62_ptr, in63_ptr, in64_ptr, in65_ptr, in66_ptr, in67_ptr, in68_ptr, in69_ptr, in70_ptr, in71_ptr, in72_ptr, in73_ptr, in74_ptr, in75_ptr, in76_ptr, in77_ptr, in78_ptr, in79_ptr, in80_ptr, in81_ptr, in82_ptr, in83_ptr, in84_ptr, in85_ptr, in86_ptr, in87_ptr, in88_ptr, in89_ptr, in90_ptr, in91_ptr, in92_ptr, in93_ptr, in94_ptr, in95_ptr, in96_ptr, in97_ptr, in98_ptr, in99_ptr, in100_ptr, in101_ptr, in102_ptr, in103_ptr, in104_ptr, in105_ptr, in106_ptr, in107_ptr, in108_ptr, in109_ptr, in110_ptr, in111_ptr, in112_ptr, in113_ptr, in114_ptr, in115_ptr, in116_ptr, in117_ptr, in118_ptr, in119_ptr):
    _acc0 = tl.zeros([1], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), ((((tl.load(in117_ptr + (tl.program_id(0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) - (tl.load(in118_ptr + (tl.maximum((tl.program_id(0) % 1152) - tl.maximum((tl.program_id(0) % 1152) - 1151, 0), 0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) * (1.0 * (1.0 / 2.0)))) * (1.0 / tl.sqrt(((tl.load(in119_ptr + (tl.maximum((tl.program_id(0) % 1152) - tl.maximum((tl.program_id(0) % 1152) - 1151, 0), 0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) * (1.0 * (1.0 / 2.0))) + (1.0 * (1.0 / 100000.0)))))) * tl.load(in41_ptr + ((tl.program_id(0) % 1152) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)) + tl.load(in42_ptr + ((tl.program_id(0) % 1152) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)), 0.0))
    _v = tl.maximum(tl.sum(_acc0, axis=0), (0.0 * (1.0 / 1.0)))
    tl.store(out_ptr + tl.program_id(0), _v)


def t024_s56(out, ins):
    grid = (2304,)
    t024_s56_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37], ins[38], ins[39], ins[40], ins[41], ins[42], ins[43], ins[44], ins[45], ins[46], ins[47], ins[48], ins[49], ins[50], ins[51], ins[52], ins[53], ins[54], ins[55], ins[56], ins[57], ins[58], ins[59], ins[60], ins[61], ins[62], ins[63], ins[64], ins[65], ins[66], ins[67], ins[68], ins[69], ins[70], ins[71], ins[72], ins[73], ins[74], ins[75], ins[76], ins[77], ins[78], ins[79], ins[80], ins[81], ins[82], ins[83], ins[84], ins[85], ins[86], ins[87], ins[88], ins[89], ins[90], ins[91], ins[92], ins[93], ins[94], ins[95], ins[96], ins[97], ins[98], ins[99], ins[100], ins[101], ins[102], ins[103], ins[104], ins[105], ins[106], ins[107], ins[108], ins[109], ins[110], ins[111], ins[112], ins[113], ins[114], ins[115], ins[116], ins[117], ins[118], ins[119])
    return out


@triton.jit
def t024_s57_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr, in38_ptr, in39_ptr, in40_ptr, in41_ptr, in42_ptr, in43_ptr, in44_ptr, in45_ptr, in46_ptr, in47_ptr, in48_ptr, in49_ptr, in50_ptr, in51_ptr, in52_ptr, in53_ptr, in54_ptr, in55_ptr, in56_ptr, in57_ptr, in58_ptr, in59_ptr, in60_ptr, in61_ptr, in62_ptr, in63_ptr, in64_ptr, in65_ptr, in66_ptr, in67_ptr, in68_ptr, in69_ptr, in70_ptr, in71_ptr, in72_ptr, in73_ptr, in74_ptr, in75_ptr, in76_ptr, in77_ptr, in78_ptr, in79_ptr, in80_ptr, in81_ptr, in82_ptr, in83_ptr, in84_ptr, in85_ptr, in86_ptr, in87_ptr, in88_ptr, in89_ptr, in90_ptr, in91_ptr, in92_ptr, in93_ptr, in94_ptr, in95_ptr, in96_ptr, in97_ptr, in98_ptr, in99_ptr, in100_ptr, in101_ptr, in102_ptr, in103_ptr, in104_ptr, in105_ptr, in106_ptr, in107_ptr, in108_ptr, in109_ptr, in110_ptr, in111_ptr, in112_ptr, in113_ptr, in114_ptr, in115_ptr, in116_ptr, in117_ptr, in118_ptr, in119_ptr, in120_ptr):
    _acc0 = tl.zeros([1], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), tl.load(in120_ptr + (tl.maximum((tl.program_id(0) + ((_lv0 * 1) + tl.arange(0, 1))) - tl.maximum((tl.program_id(0) + ((_lv0 * 1) + tl.arange(0, 1))) - 2303, 0), 0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0), 0.0))
    _v = (tl.sum(_acc0, axis=0) * (1.0 * (1.0 / 1.0)))
    tl.store(out_ptr + tl.program_id(0), _v)


def t024_s57(out, ins):
    grid = (2304,)
    t024_s57_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37], ins[38], ins[39], ins[40], ins[41], ins[42], ins[43], ins[44], ins[45], ins[46], ins[47], ins[48], ins[49], ins[50], ins[51], ins[52], ins[53], ins[54], ins[55], ins[56], ins[57], ins[58], ins[59], ins[60], ins[61], ins[62], ins[63], ins[64], ins[65], ins[66], ins[67], ins[68], ins[69], ins[70], ins[71], ins[72], ins[73], ins[74], ins[75], ins[76], ins[77], ins[78], ins[79], ins[80], ins[81], ins[82], ins[83], ins[84], ins[85], ins[86], ins[87], ins[88], ins[89], ins[90], ins[91], ins[92], ins[93], ins[94], ins[95], ins[96], ins[97], ins[98], ins[99], ins[100], ins[101], ins[102], ins[103], ins[104], ins[105], ins[106], ins[107], ins[108], ins[109], ins[110], ins[111], ins[112], ins[113], ins[114], ins[115], ins[116], ins[117], ins[118], ins[119], ins[120])
    return out


@triton.jit
def t024_s58_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr, in38_ptr, in39_ptr, in40_ptr, in41_ptr, in42_ptr, in43_ptr, in44_ptr, in45_ptr, in46_ptr, in47_ptr, in48_ptr, in49_ptr, in50_ptr, in51_ptr, in52_ptr, in53_ptr, in54_ptr, in55_ptr, in56_ptr, in57_ptr, in58_ptr, in59_ptr, in60_ptr, in61_ptr, in62_ptr, in63_ptr, in64_ptr, in65_ptr, in66_ptr, in67_ptr, in68_ptr, in69_ptr, in70_ptr, in71_ptr, in72_ptr, in73_ptr, in74_ptr, in75_ptr, in76_ptr, in77_ptr, in78_ptr, in79_ptr, in80_ptr, in81_ptr, in82_ptr, in83_ptr, in84_ptr, in85_ptr, in86_ptr, in87_ptr, in88_ptr, in89_ptr, in90_ptr, in91_ptr, in92_ptr, in93_ptr, in94_ptr, in95_ptr, in96_ptr, in97_ptr, in98_ptr, in99_ptr, in100_ptr, in101_ptr, in102_ptr, in103_ptr, in104_ptr, in105_ptr, in106_ptr, in107_ptr, in108_ptr, in109_ptr, in110_ptr, in111_ptr, in112_ptr, in113_ptr, in114_ptr, in115_ptr, in116_ptr, in117_ptr, in118_ptr, in119_ptr, in120_ptr, in121_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 1152) & ((0 < 1) & (0 < 1))), (tl.load(in121_ptr + ((((tl.program_id(0) // 288) * 1152) + ((_lv0 * 1024) + tl.arange(0, 1024))) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 1152) & ((0 < 1) & (0 < 1))), other=0.0) * tl.load(in43_ptr + ((((tl.program_id(0) % 288) * 1152) + ((_lv0 * 1024) + tl.arange(0, 1024))) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 1152) & ((0 < 1) & (0 < 1))), other=0.0)), 0.0))
    _v = tl.maximum(tl.sum(_acc0, axis=0), (0.0 * (1.0 / 1.0)))
    tl.store(out_ptr + tl.program_id(0), _v)


def t024_s58(out, ins):
    grid = (576,)
    t024_s58_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37], ins[38], ins[39], ins[40], ins[41], ins[42], ins[43], ins[44], ins[45], ins[46], ins[47], ins[48], ins[49], ins[50], ins[51], ins[52], ins[53], ins[54], ins[55], ins[56], ins[57], ins[58], ins[59], ins[60], ins[61], ins[62], ins[63], ins[64], ins[65], ins[66], ins[67], ins[68], ins[69], ins[70], ins[71], ins[72], ins[73], ins[74], ins[75], ins[76], ins[77], ins[78], ins[79], ins[80], ins[81], ins[82], ins[83], ins[84], ins[85], ins[86], ins[87], ins[88], ins[89], ins[90], ins[91], ins[92], ins[93], ins[94], ins[95], ins[96], ins[97], ins[98], ins[99], ins[100], ins[101], ins[102], ins[103], ins[104], ins[105], ins[106], ins[107], ins[108], ins[109], ins[110], ins[111], ins[112], ins[113], ins[114], ins[115], ins[116], ins[117], ins[118], ins[119], ins[120], ins[121])
    return out


@triton.jit
def t024_s59_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr, in38_ptr, in39_ptr, in40_ptr, in41_ptr, in42_ptr, in43_ptr, in44_ptr, in45_ptr, in46_ptr, in47_ptr, in48_ptr, in49_ptr, in50_ptr, in51_ptr, in52_ptr, in53_ptr, in54_ptr, in55_ptr, in56_ptr, in57_ptr, in58_ptr, in59_ptr, in60_ptr, in61_ptr, in62_ptr, in63_ptr, in64_ptr, in65_ptr, in66_ptr, in67_ptr, in68_ptr, in69_ptr, in70_ptr, in71_ptr, in72_ptr, in73_ptr, in74_ptr, in75_ptr, in76_ptr, in77_ptr, in78_ptr, in79_ptr, in80_ptr, in81_ptr, in82_ptr, in83_ptr, in84_ptr, in85_ptr, in86_ptr, in87_ptr, in88_ptr, in89_ptr, in90_ptr, in91_ptr, in92_ptr, in93_ptr, in94_ptr, in95_ptr, in96_ptr, in97_ptr, in98_ptr, in99_ptr, in100_ptr, in101_ptr, in102_ptr, in103_ptr, in104_ptr, in105_ptr, in106_ptr, in107_ptr, in108_ptr, in109_ptr, in110_ptr, in111_ptr, in112_ptr, in113_ptr, in114_ptr, in115_ptr, in116_ptr, in117_ptr, in118_ptr, in119_ptr, in120_ptr, in121_ptr, in122_ptr):
    _acc0 = tl.zeros([256], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 256) + tl.arange(0, 256)) < 288) & ((0 < 1) & (0 < 1))), (tl.load(in122_ptr + ((((tl.program_id(0) // 1152) * 288) + ((_lv0 * 256) + tl.arange(0, 256))) + 0 * tl.arange(0, 256)), mask=((((_lv0 * 256) + tl.arange(0, 256)) < 288) & ((0 < 1) & (0 < 1))), other=0.0) * tl.load(in44_ptr + ((((tl.program_id(0) % 1152) * 288) + ((_lv0 * 256) + tl.arange(0, 256))) + 0 * tl.arange(0, 256)), mask=((((_lv0 * 256) + tl.arange(0, 256)) < 288) & ((0 < 1) & (0 < 1))), other=0.0)), 0.0))
    _v = (1.0 / ((1.0 * (1.0 / 1.0)) + tl.exp(((0.0 * (1.0 / 1.0)) - tl.sum(_acc0, axis=0)))))
    tl.store(out_ptr + tl.program_id(0), _v)


def t024_s59(out, ins):
    grid = (2304,)
    t024_s59_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37], ins[38], ins[39], ins[40], ins[41], ins[42], ins[43], ins[44], ins[45], ins[46], ins[47], ins[48], ins[49], ins[50], ins[51], ins[52], ins[53], ins[54], ins[55], ins[56], ins[57], ins[58], ins[59], ins[60], ins[61], ins[62], ins[63], ins[64], ins[65], ins[66], ins[67], ins[68], ins[69], ins[70], ins[71], ins[72], ins[73], ins[74], ins[75], ins[76], ins[77], ins[78], ins[79], ins[80], ins[81], ins[82], ins[83], ins[84], ins[85], ins[86], ins[87], ins[88], ins[89], ins[90], ins[91], ins[92], ins[93], ins[94], ins[95], ins[96], ins[97], ins[98], ins[99], ins[100], ins[101], ins[102], ins[103], ins[104], ins[105], ins[106], ins[107], ins[108], ins[109], ins[110], ins[111], ins[112], ins[113], ins[114], ins[115], ins[116], ins[117], ins[118], ins[119], ins[120], ins[121], ins[122])
    return out


@triton.jit
def t024_s60_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr, in38_ptr, in39_ptr, in40_ptr, in41_ptr, in42_ptr, in43_ptr, in44_ptr, in45_ptr, in46_ptr, in47_ptr, in48_ptr, in49_ptr, in50_ptr, in51_ptr, in52_ptr, in53_ptr, in54_ptr, in55_ptr, in56_ptr, in57_ptr, in58_ptr, in59_ptr, in60_ptr, in61_ptr, in62_ptr, in63_ptr, in64_ptr, in65_ptr, in66_ptr, in67_ptr, in68_ptr, in69_ptr, in70_ptr, in71_ptr, in72_ptr, in73_ptr, in74_ptr, in75_ptr, in76_ptr, in77_ptr, in78_ptr, in79_ptr, in80_ptr, in81_ptr, in82_ptr, in83_ptr, in84_ptr, in85_ptr, in86_ptr, in87_ptr, in88_ptr, in89_ptr, in90_ptr, in91_ptr, in92_ptr, in93_ptr, in94_ptr, in95_ptr, in96_ptr, in97_ptr, in98_ptr, in99_ptr, in100_ptr, in101_ptr, in102_ptr, in103_ptr, in104_ptr, in105_ptr, in106_ptr, in107_ptr, in108_ptr, in109_ptr, in110_ptr, in111_ptr, in112_ptr, in113_ptr, in114_ptr, in115_ptr, in116_ptr, in117_ptr, in118_ptr, in119_ptr, in120_ptr, in121_ptr, in122_ptr, in123_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 1152) & ((0 < 1) & (0 < 1))), (tl.load(in123_ptr + ((((tl.program_id(0) // 288) * 1152) + ((_lv0 * 1024) + tl.arange(0, 1024))) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 1152) & ((0 < 1) & (0 < 1))), other=0.0) * tl.load(in45_ptr + ((((tl.program_id(0) % 288) * 1152) + ((_lv0 * 1024) + tl.arange(0, 1024))) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 1152) & ((0 < 1) & (0 < 1))), other=0.0)), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t024_s60(out, ins):
    grid = (576,)
    t024_s60_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37], ins[38], ins[39], ins[40], ins[41], ins[42], ins[43], ins[44], ins[45], ins[46], ins[47], ins[48], ins[49], ins[50], ins[51], ins[52], ins[53], ins[54], ins[55], ins[56], ins[57], ins[58], ins[59], ins[60], ins[61], ins[62], ins[63], ins[64], ins[65], ins[66], ins[67], ins[68], ins[69], ins[70], ins[71], ins[72], ins[73], ins[74], ins[75], ins[76], ins[77], ins[78], ins[79], ins[80], ins[81], ins[82], ins[83], ins[84], ins[85], ins[86], ins[87], ins[88], ins[89], ins[90], ins[91], ins[92], ins[93], ins[94], ins[95], ins[96], ins[97], ins[98], ins[99], ins[100], ins[101], ins[102], ins[103], ins[104], ins[105], ins[106], ins[107], ins[108], ins[109], ins[110], ins[111], ins[112], ins[113], ins[114], ins[115], ins[116], ins[117], ins[118], ins[119], ins[120], ins[121], ins[122], ins[123])
    return out


@triton.jit
def t024_s61_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr, in38_ptr, in39_ptr, in40_ptr, in41_ptr, in42_ptr, in43_ptr, in44_ptr, in45_ptr, in46_ptr, in47_ptr, in48_ptr, in49_ptr, in50_ptr, in51_ptr, in52_ptr, in53_ptr, in54_ptr, in55_ptr, in56_ptr, in57_ptr, in58_ptr, in59_ptr, in60_ptr, in61_ptr, in62_ptr, in63_ptr, in64_ptr, in65_ptr, in66_ptr, in67_ptr, in68_ptr, in69_ptr, in70_ptr, in71_ptr, in72_ptr, in73_ptr, in74_ptr, in75_ptr, in76_ptr, in77_ptr, in78_ptr, in79_ptr, in80_ptr, in81_ptr, in82_ptr, in83_ptr, in84_ptr, in85_ptr, in86_ptr, in87_ptr, in88_ptr, in89_ptr, in90_ptr, in91_ptr, in92_ptr, in93_ptr, in94_ptr, in95_ptr, in96_ptr, in97_ptr, in98_ptr, in99_ptr, in100_ptr, in101_ptr, in102_ptr, in103_ptr, in104_ptr, in105_ptr, in106_ptr, in107_ptr, in108_ptr, in109_ptr, in110_ptr, in111_ptr, in112_ptr, in113_ptr, in114_ptr, in115_ptr, in116_ptr, in117_ptr, in118_ptr, in119_ptr, in120_ptr, in121_ptr, in122_ptr, in123_ptr, in124_ptr):
    _acc0 = tl.zeros([2], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 2) + tl.arange(0, 2)) < 2) & True), tl.load(in124_ptr + (((((_lv0 * 2) + tl.arange(0, 2)) * 288) + tl.program_id(0)) + 0 * tl.arange(0, 2)), mask=((((_lv0 * 2) + tl.arange(0, 2)) < 2) & True), other=0.0), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t024_s61(out, ins):
    grid = (288,)
    t024_s61_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37], ins[38], ins[39], ins[40], ins[41], ins[42], ins[43], ins[44], ins[45], ins[46], ins[47], ins[48], ins[49], ins[50], ins[51], ins[52], ins[53], ins[54], ins[55], ins[56], ins[57], ins[58], ins[59], ins[60], ins[61], ins[62], ins[63], ins[64], ins[65], ins[66], ins[67], ins[68], ins[69], ins[70], ins[71], ins[72], ins[73], ins[74], ins[75], ins[76], ins[77], ins[78], ins[79], ins[80], ins[81], ins[82], ins[83], ins[84], ins[85], ins[86], ins[87], ins[88], ins[89], ins[90], ins[91], ins[92], ins[93], ins[94], ins[95], ins[96], ins[97], ins[98], ins[99], ins[100], ins[101], ins[102], ins[103], ins[104], ins[105], ins[106], ins[107], ins[108], ins[109], ins[110], ins[111], ins[112], ins[113], ins[114], ins[115], ins[116], ins[117], ins[118], ins[119], ins[120], ins[121], ins[122], ins[123], ins[124])
    return out


@triton.jit
def t024_s62_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr, in38_ptr, in39_ptr, in40_ptr, in41_ptr, in42_ptr, in43_ptr, in44_ptr, in45_ptr, in46_ptr, in47_ptr, in48_ptr, in49_ptr, in50_ptr, in51_ptr, in52_ptr, in53_ptr, in54_ptr, in55_ptr, in56_ptr, in57_ptr, in58_ptr, in59_ptr, in60_ptr, in61_ptr, in62_ptr, in63_ptr, in64_ptr, in65_ptr, in66_ptr, in67_ptr, in68_ptr, in69_ptr, in70_ptr, in71_ptr, in72_ptr, in73_ptr, in74_ptr, in75_ptr, in76_ptr, in77_ptr, in78_ptr, in79_ptr, in80_ptr, in81_ptr, in82_ptr, in83_ptr, in84_ptr, in85_ptr, in86_ptr, in87_ptr, in88_ptr, in89_ptr, in90_ptr, in91_ptr, in92_ptr, in93_ptr, in94_ptr, in95_ptr, in96_ptr, in97_ptr, in98_ptr, in99_ptr, in100_ptr, in101_ptr, in102_ptr, in103_ptr, in104_ptr, in105_ptr, in106_ptr, in107_ptr, in108_ptr, in109_ptr, in110_ptr, in111_ptr, in112_ptr, in113_ptr, in114_ptr, in115_ptr, in116_ptr, in117_ptr, in118_ptr, in119_ptr, in120_ptr, in121_ptr, in122_ptr, in123_ptr, in124_ptr, in125_ptr):
    _acc0 = tl.zeros([2], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 2) + tl.arange(0, 2)) < 2) & True), ((tl.load(in124_ptr + (((((_lv0 * 2) + tl.arange(0, 2)) * 288) + tl.program_id(0)) + 0 * tl.arange(0, 2)), mask=((((_lv0 * 2) + tl.arange(0, 2)) < 2) & True), other=0.0) - (tl.load(in125_ptr + (tl.program_id(0) + 0 * tl.arange(0, 2)), mask=((((_lv0 * 2) + tl.arange(0, 2)) < 2) & True), other=0.0) * (1.0 * (1.0 / 2.0)))) * (tl.load(in124_ptr + (((((_lv0 * 2) + tl.arange(0, 2)) * 288) + tl.program_id(0)) + 0 * tl.arange(0, 2)), mask=((((_lv0 * 2) + tl.arange(0, 2)) < 2) & True), other=0.0) - (tl.load(in125_ptr + (tl.program_id(0) + 0 * tl.arange(0, 2)), mask=((((_lv0 * 2) + tl.arange(0, 2)) < 2) & True), other=0.0) * (1.0 * (1.0 / 2.0))))), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t024_s62(out, ins):
    grid = (288,)
    t024_s62_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37], ins[38], ins[39], ins[40], ins[41], ins[42], ins[43], ins[44], ins[45], ins[46], ins[47], ins[48], ins[49], ins[50], ins[51], ins[52], ins[53], ins[54], ins[55], ins[56], ins[57], ins[58], ins[59], ins[60], ins[61], ins[62], ins[63], ins[64], ins[65], ins[66], ins[67], ins[68], ins[69], ins[70], ins[71], ins[72], ins[73], ins[74], ins[75], ins[76], ins[77], ins[78], ins[79], ins[80], ins[81], ins[82], ins[83], ins[84], ins[85], ins[86], ins[87], ins[88], ins[89], ins[90], ins[91], ins[92], ins[93], ins[94], ins[95], ins[96], ins[97], ins[98], ins[99], ins[100], ins[101], ins[102], ins[103], ins[104], ins[105], ins[106], ins[107], ins[108], ins[109], ins[110], ins[111], ins[112], ins[113], ins[114], ins[115], ins[116], ins[117], ins[118], ins[119], ins[120], ins[121], ins[122], ins[123], ins[124], ins[125])
    return out


@triton.jit
def t024_s63_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr, in38_ptr, in39_ptr, in40_ptr, in41_ptr, in42_ptr, in43_ptr, in44_ptr, in45_ptr, in46_ptr, in47_ptr, in48_ptr, in49_ptr, in50_ptr, in51_ptr, in52_ptr, in53_ptr, in54_ptr, in55_ptr, in56_ptr, in57_ptr, in58_ptr, in59_ptr, in60_ptr, in61_ptr, in62_ptr, in63_ptr, in64_ptr, in65_ptr, in66_ptr, in67_ptr, in68_ptr, in69_ptr, in70_ptr, in71_ptr, in72_ptr, in73_ptr, in74_ptr, in75_ptr, in76_ptr, in77_ptr, in78_ptr, in79_ptr, in80_ptr, in81_ptr, in82_ptr, in83_ptr, in84_ptr, in85_ptr, in86_ptr, in87_ptr, in88_ptr, in89_ptr, in90_ptr, in91_ptr, in92_ptr, in93_ptr, in94_ptr, in95_ptr, in96_ptr, in97_ptr, in98_ptr, in99_ptr, in100_ptr, in101_ptr, in102_ptr, in103_ptr, in104_ptr, in105_ptr, in106_ptr, in107_ptr, in108_ptr, in109_ptr, in110_ptr, in111_ptr, in112_ptr, in113_ptr, in114_ptr, in115_ptr, in116_ptr, in117_ptr, in118_ptr, in119_ptr, in120_ptr, in121_ptr, in122_ptr, in123_ptr, in124_ptr, in125_ptr, in126_ptr):
    _acc0 = tl.zeros([1], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), ((((tl.load(in124_ptr + (tl.program_id(0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) - (tl.load(in125_ptr + (tl.maximum((tl.program_id(0) % 288) - tl.maximum((tl.program_id(0) % 288) - 287, 0), 0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) * (1.0 * (1.0 / 2.0)))) * (1.0 / tl.sqrt(((tl.load(in126_ptr + (tl.maximum((tl.program_id(0) % 288) - tl.maximum((tl.program_id(0) % 288) - 287, 0), 0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) * (1.0 * (1.0 / 2.0))) + (1.0 * (1.0 / 100000.0)))))) * tl.load(in46_ptr + ((tl.program_id(0) % 288) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)) + tl.load(in47_ptr + ((tl.program_id(0) % 288) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t024_s63(out, ins):
    grid = (576,)
    t024_s63_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37], ins[38], ins[39], ins[40], ins[41], ins[42], ins[43], ins[44], ins[45], ins[46], ins[47], ins[48], ins[49], ins[50], ins[51], ins[52], ins[53], ins[54], ins[55], ins[56], ins[57], ins[58], ins[59], ins[60], ins[61], ins[62], ins[63], ins[64], ins[65], ins[66], ins[67], ins[68], ins[69], ins[70], ins[71], ins[72], ins[73], ins[74], ins[75], ins[76], ins[77], ins[78], ins[79], ins[80], ins[81], ins[82], ins[83], ins[84], ins[85], ins[86], ins[87], ins[88], ins[89], ins[90], ins[91], ins[92], ins[93], ins[94], ins[95], ins[96], ins[97], ins[98], ins[99], ins[100], ins[101], ins[102], ins[103], ins[104], ins[105], ins[106], ins[107], ins[108], ins[109], ins[110], ins[111], ins[112], ins[113], ins[114], ins[115], ins[116], ins[117], ins[118], ins[119], ins[120], ins[121], ins[122], ins[123], ins[124], ins[125], ins[126])
    return out


@triton.jit
def t024_s64_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr, in38_ptr, in39_ptr, in40_ptr, in41_ptr, in42_ptr, in43_ptr, in44_ptr, in45_ptr, in46_ptr, in47_ptr, in48_ptr, in49_ptr, in50_ptr, in51_ptr, in52_ptr, in53_ptr, in54_ptr, in55_ptr, in56_ptr, in57_ptr, in58_ptr, in59_ptr, in60_ptr, in61_ptr, in62_ptr, in63_ptr, in64_ptr, in65_ptr, in66_ptr, in67_ptr, in68_ptr, in69_ptr, in70_ptr, in71_ptr, in72_ptr, in73_ptr, in74_ptr, in75_ptr, in76_ptr, in77_ptr, in78_ptr, in79_ptr, in80_ptr, in81_ptr, in82_ptr, in83_ptr, in84_ptr, in85_ptr, in86_ptr, in87_ptr, in88_ptr, in89_ptr, in90_ptr, in91_ptr, in92_ptr, in93_ptr, in94_ptr, in95_ptr, in96_ptr, in97_ptr, in98_ptr, in99_ptr, in100_ptr, in101_ptr, in102_ptr, in103_ptr, in104_ptr, in105_ptr, in106_ptr, in107_ptr, in108_ptr, in109_ptr, in110_ptr, in111_ptr, in112_ptr, in113_ptr, in114_ptr, in115_ptr, in116_ptr, in117_ptr, in118_ptr, in119_ptr, in120_ptr, in121_ptr, in122_ptr, in123_ptr, in124_ptr, in125_ptr, in126_ptr, in127_ptr):
    _acc0 = tl.zeros([256], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 256) + tl.arange(0, 256)) < 288) & ((0 < 1) & (0 < 1))), (tl.load(in127_ptr + ((((tl.program_id(0) // 1728) * 288) + ((_lv0 * 256) + tl.arange(0, 256))) + 0 * tl.arange(0, 256)), mask=((((_lv0 * 256) + tl.arange(0, 256)) < 288) & ((0 < 1) & (0 < 1))), other=0.0) * tl.load(in48_ptr + ((((tl.program_id(0) % 1728) * 288) + ((_lv0 * 256) + tl.arange(0, 256))) + 0 * tl.arange(0, 256)), mask=((((_lv0 * 256) + tl.arange(0, 256)) < 288) & ((0 < 1) & (0 < 1))), other=0.0)), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t024_s64(out, ins):
    grid = (3456,)
    t024_s64_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37], ins[38], ins[39], ins[40], ins[41], ins[42], ins[43], ins[44], ins[45], ins[46], ins[47], ins[48], ins[49], ins[50], ins[51], ins[52], ins[53], ins[54], ins[55], ins[56], ins[57], ins[58], ins[59], ins[60], ins[61], ins[62], ins[63], ins[64], ins[65], ins[66], ins[67], ins[68], ins[69], ins[70], ins[71], ins[72], ins[73], ins[74], ins[75], ins[76], ins[77], ins[78], ins[79], ins[80], ins[81], ins[82], ins[83], ins[84], ins[85], ins[86], ins[87], ins[88], ins[89], ins[90], ins[91], ins[92], ins[93], ins[94], ins[95], ins[96], ins[97], ins[98], ins[99], ins[100], ins[101], ins[102], ins[103], ins[104], ins[105], ins[106], ins[107], ins[108], ins[109], ins[110], ins[111], ins[112], ins[113], ins[114], ins[115], ins[116], ins[117], ins[118], ins[119], ins[120], ins[121], ins[122], ins[123], ins[124], ins[125], ins[126], ins[127])
    return out


@triton.jit
def t024_s65_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr, in38_ptr, in39_ptr, in40_ptr, in41_ptr, in42_ptr, in43_ptr, in44_ptr, in45_ptr, in46_ptr, in47_ptr, in48_ptr, in49_ptr, in50_ptr, in51_ptr, in52_ptr, in53_ptr, in54_ptr, in55_ptr, in56_ptr, in57_ptr, in58_ptr, in59_ptr, in60_ptr, in61_ptr, in62_ptr, in63_ptr, in64_ptr, in65_ptr, in66_ptr, in67_ptr, in68_ptr, in69_ptr, in70_ptr, in71_ptr, in72_ptr, in73_ptr, in74_ptr, in75_ptr, in76_ptr, in77_ptr, in78_ptr, in79_ptr, in80_ptr, in81_ptr, in82_ptr, in83_ptr, in84_ptr, in85_ptr, in86_ptr, in87_ptr, in88_ptr, in89_ptr, in90_ptr, in91_ptr, in92_ptr, in93_ptr, in94_ptr, in95_ptr, in96_ptr, in97_ptr, in98_ptr, in99_ptr, in100_ptr, in101_ptr, in102_ptr, in103_ptr, in104_ptr, in105_ptr, in106_ptr, in107_ptr, in108_ptr, in109_ptr, in110_ptr, in111_ptr, in112_ptr, in113_ptr, in114_ptr, in115_ptr, in116_ptr, in117_ptr, in118_ptr, in119_ptr, in120_ptr, in121_ptr, in122_ptr, in123_ptr, in124_ptr, in125_ptr, in126_ptr, in127_ptr, in128_ptr):
    _acc0 = tl.zeros([2], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 2) + tl.arange(0, 2)) < 2) & True), tl.load(in128_ptr + (((((_lv0 * 2) + tl.arange(0, 2)) * 1728) + tl.program_id(0)) + 0 * tl.arange(0, 2)), mask=((((_lv0 * 2) + tl.arange(0, 2)) < 2) & True), other=0.0), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t024_s65(out, ins):
    grid = (1728,)
    t024_s65_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37], ins[38], ins[39], ins[40], ins[41], ins[42], ins[43], ins[44], ins[45], ins[46], ins[47], ins[48], ins[49], ins[50], ins[51], ins[52], ins[53], ins[54], ins[55], ins[56], ins[57], ins[58], ins[59], ins[60], ins[61], ins[62], ins[63], ins[64], ins[65], ins[66], ins[67], ins[68], ins[69], ins[70], ins[71], ins[72], ins[73], ins[74], ins[75], ins[76], ins[77], ins[78], ins[79], ins[80], ins[81], ins[82], ins[83], ins[84], ins[85], ins[86], ins[87], ins[88], ins[89], ins[90], ins[91], ins[92], ins[93], ins[94], ins[95], ins[96], ins[97], ins[98], ins[99], ins[100], ins[101], ins[102], ins[103], ins[104], ins[105], ins[106], ins[107], ins[108], ins[109], ins[110], ins[111], ins[112], ins[113], ins[114], ins[115], ins[116], ins[117], ins[118], ins[119], ins[120], ins[121], ins[122], ins[123], ins[124], ins[125], ins[126], ins[127], ins[128])
    return out


@triton.jit
def t024_s66_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr, in38_ptr, in39_ptr, in40_ptr, in41_ptr, in42_ptr, in43_ptr, in44_ptr, in45_ptr, in46_ptr, in47_ptr, in48_ptr, in49_ptr, in50_ptr, in51_ptr, in52_ptr, in53_ptr, in54_ptr, in55_ptr, in56_ptr, in57_ptr, in58_ptr, in59_ptr, in60_ptr, in61_ptr, in62_ptr, in63_ptr, in64_ptr, in65_ptr, in66_ptr, in67_ptr, in68_ptr, in69_ptr, in70_ptr, in71_ptr, in72_ptr, in73_ptr, in74_ptr, in75_ptr, in76_ptr, in77_ptr, in78_ptr, in79_ptr, in80_ptr, in81_ptr, in82_ptr, in83_ptr, in84_ptr, in85_ptr, in86_ptr, in87_ptr, in88_ptr, in89_ptr, in90_ptr, in91_ptr, in92_ptr, in93_ptr, in94_ptr, in95_ptr, in96_ptr, in97_ptr, in98_ptr, in99_ptr, in100_ptr, in101_ptr, in102_ptr, in103_ptr, in104_ptr, in105_ptr, in106_ptr, in107_ptr, in108_ptr, in109_ptr, in110_ptr, in111_ptr, in112_ptr, in113_ptr, in114_ptr, in115_ptr, in116_ptr, in117_ptr, in118_ptr, in119_ptr, in120_ptr, in121_ptr, in122_ptr, in123_ptr, in124_ptr, in125_ptr, in126_ptr, in127_ptr, in128_ptr, in129_ptr):
    _acc0 = tl.zeros([2], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 2) + tl.arange(0, 2)) < 2) & True), ((tl.load(in128_ptr + (((((_lv0 * 2) + tl.arange(0, 2)) * 1728) + tl.program_id(0)) + 0 * tl.arange(0, 2)), mask=((((_lv0 * 2) + tl.arange(0, 2)) < 2) & True), other=0.0) - (tl.load(in129_ptr + (tl.program_id(0) + 0 * tl.arange(0, 2)), mask=((((_lv0 * 2) + tl.arange(0, 2)) < 2) & True), other=0.0) * (1.0 * (1.0 / 2.0)))) * (tl.load(in128_ptr + (((((_lv0 * 2) + tl.arange(0, 2)) * 1728) + tl.program_id(0)) + 0 * tl.arange(0, 2)), mask=((((_lv0 * 2) + tl.arange(0, 2)) < 2) & True), other=0.0) - (tl.load(in129_ptr + (tl.program_id(0) + 0 * tl.arange(0, 2)), mask=((((_lv0 * 2) + tl.arange(0, 2)) < 2) & True), other=0.0) * (1.0 * (1.0 / 2.0))))), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t024_s66(out, ins):
    grid = (1728,)
    t024_s66_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37], ins[38], ins[39], ins[40], ins[41], ins[42], ins[43], ins[44], ins[45], ins[46], ins[47], ins[48], ins[49], ins[50], ins[51], ins[52], ins[53], ins[54], ins[55], ins[56], ins[57], ins[58], ins[59], ins[60], ins[61], ins[62], ins[63], ins[64], ins[65], ins[66], ins[67], ins[68], ins[69], ins[70], ins[71], ins[72], ins[73], ins[74], ins[75], ins[76], ins[77], ins[78], ins[79], ins[80], ins[81], ins[82], ins[83], ins[84], ins[85], ins[86], ins[87], ins[88], ins[89], ins[90], ins[91], ins[92], ins[93], ins[94], ins[95], ins[96], ins[97], ins[98], ins[99], ins[100], ins[101], ins[102], ins[103], ins[104], ins[105], ins[106], ins[107], ins[108], ins[109], ins[110], ins[111], ins[112], ins[113], ins[114], ins[115], ins[116], ins[117], ins[118], ins[119], ins[120], ins[121], ins[122], ins[123], ins[124], ins[125], ins[126], ins[127], ins[128], ins[129])
    return out


@triton.jit
def t024_s67_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr, in38_ptr, in39_ptr, in40_ptr, in41_ptr, in42_ptr, in43_ptr, in44_ptr, in45_ptr, in46_ptr, in47_ptr, in48_ptr, in49_ptr, in50_ptr, in51_ptr, in52_ptr, in53_ptr, in54_ptr, in55_ptr, in56_ptr, in57_ptr, in58_ptr, in59_ptr, in60_ptr, in61_ptr, in62_ptr, in63_ptr, in64_ptr, in65_ptr, in66_ptr, in67_ptr, in68_ptr, in69_ptr, in70_ptr, in71_ptr, in72_ptr, in73_ptr, in74_ptr, in75_ptr, in76_ptr, in77_ptr, in78_ptr, in79_ptr, in80_ptr, in81_ptr, in82_ptr, in83_ptr, in84_ptr, in85_ptr, in86_ptr, in87_ptr, in88_ptr, in89_ptr, in90_ptr, in91_ptr, in92_ptr, in93_ptr, in94_ptr, in95_ptr, in96_ptr, in97_ptr, in98_ptr, in99_ptr, in100_ptr, in101_ptr, in102_ptr, in103_ptr, in104_ptr, in105_ptr, in106_ptr, in107_ptr, in108_ptr, in109_ptr, in110_ptr, in111_ptr, in112_ptr, in113_ptr, in114_ptr, in115_ptr, in116_ptr, in117_ptr, in118_ptr, in119_ptr, in120_ptr, in121_ptr, in122_ptr, in123_ptr, in124_ptr, in125_ptr, in126_ptr, in127_ptr, in128_ptr, in129_ptr, in130_ptr):
    _acc0 = tl.zeros([1], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), ((((tl.load(in128_ptr + (tl.program_id(0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) - (tl.load(in129_ptr + (tl.maximum((tl.program_id(0) % 1728) - tl.maximum((tl.program_id(0) % 1728) - 1727, 0), 0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) * (1.0 * (1.0 / 2.0)))) * (1.0 / tl.sqrt(((tl.load(in130_ptr + (tl.maximum((tl.program_id(0) % 1728) - tl.maximum((tl.program_id(0) % 1728) - 1727, 0), 0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) * (1.0 * (1.0 / 2.0))) + (1.0 * (1.0 / 100000.0)))))) * tl.load(in49_ptr + ((tl.program_id(0) % 1728) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)) + tl.load(in50_ptr + ((tl.program_id(0) % 1728) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)), 0.0))
    _v = tl.maximum(tl.sum(_acc0, axis=0), (0.0 * (1.0 / 1.0)))
    tl.store(out_ptr + tl.program_id(0), _v)


def t024_s67(out, ins):
    grid = (3456,)
    t024_s67_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37], ins[38], ins[39], ins[40], ins[41], ins[42], ins[43], ins[44], ins[45], ins[46], ins[47], ins[48], ins[49], ins[50], ins[51], ins[52], ins[53], ins[54], ins[55], ins[56], ins[57], ins[58], ins[59], ins[60], ins[61], ins[62], ins[63], ins[64], ins[65], ins[66], ins[67], ins[68], ins[69], ins[70], ins[71], ins[72], ins[73], ins[74], ins[75], ins[76], ins[77], ins[78], ins[79], ins[80], ins[81], ins[82], ins[83], ins[84], ins[85], ins[86], ins[87], ins[88], ins[89], ins[90], ins[91], ins[92], ins[93], ins[94], ins[95], ins[96], ins[97], ins[98], ins[99], ins[100], ins[101], ins[102], ins[103], ins[104], ins[105], ins[106], ins[107], ins[108], ins[109], ins[110], ins[111], ins[112], ins[113], ins[114], ins[115], ins[116], ins[117], ins[118], ins[119], ins[120], ins[121], ins[122], ins[123], ins[124], ins[125], ins[126], ins[127], ins[128], ins[129], ins[130])
    return out


@triton.jit
def t024_s68_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr, in38_ptr, in39_ptr, in40_ptr, in41_ptr, in42_ptr, in43_ptr, in44_ptr, in45_ptr, in46_ptr, in47_ptr, in48_ptr, in49_ptr, in50_ptr, in51_ptr, in52_ptr, in53_ptr, in54_ptr, in55_ptr, in56_ptr, in57_ptr, in58_ptr, in59_ptr, in60_ptr, in61_ptr, in62_ptr, in63_ptr, in64_ptr, in65_ptr, in66_ptr, in67_ptr, in68_ptr, in69_ptr, in70_ptr, in71_ptr, in72_ptr, in73_ptr, in74_ptr, in75_ptr, in76_ptr, in77_ptr, in78_ptr, in79_ptr, in80_ptr, in81_ptr, in82_ptr, in83_ptr, in84_ptr, in85_ptr, in86_ptr, in87_ptr, in88_ptr, in89_ptr, in90_ptr, in91_ptr, in92_ptr, in93_ptr, in94_ptr, in95_ptr, in96_ptr, in97_ptr, in98_ptr, in99_ptr, in100_ptr, in101_ptr, in102_ptr, in103_ptr, in104_ptr, in105_ptr, in106_ptr, in107_ptr, in108_ptr, in109_ptr, in110_ptr, in111_ptr, in112_ptr, in113_ptr, in114_ptr, in115_ptr, in116_ptr, in117_ptr, in118_ptr, in119_ptr, in120_ptr, in121_ptr, in122_ptr, in123_ptr, in124_ptr, in125_ptr, in126_ptr, in127_ptr, in128_ptr, in129_ptr, in130_ptr, in131_ptr):
    _acc0 = tl.zeros([8], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 8) + tl.arange(0, 8)) < 9) & ((((1 <= ((((_lv0 * 8) + tl.arange(0, 8)) // 3) % 3)) & (((((_lv0 * 8) + tl.arange(0, 8)) // 3) % 3) < 2)) & (1 <= (((_lv0 * 8) + tl.arange(0, 8)) % 3))) & ((((_lv0 * 8) + tl.arange(0, 8)) % 3) < 2))), (tl.load(in131_ptr + (tl.maximum((((((tl.program_id(0) // 1728) * 1728) + (tl.program_id(0) % 1728)) + tl.maximum(((((_lv0 * 8) + tl.arange(0, 8)) // 3) % 3) - 1, 0)) + tl.maximum((((_lv0 * 8) + tl.arange(0, 8)) % 3) - 1, 0)) - tl.maximum((((((tl.program_id(0) // 1728) * 1728) + (tl.program_id(0) % 1728)) + tl.maximum(((((_lv0 * 8) + tl.arange(0, 8)) // 3) % 3) - 1, 0)) + tl.maximum((((_lv0 * 8) + tl.arange(0, 8)) % 3) - 1, 0)) - 3455, 0), 0) + 0 * tl.arange(0, 8)), mask=((((_lv0 * 8) + tl.arange(0, 8)) < 9) & ((((1 <= ((((_lv0 * 8) + tl.arange(0, 8)) // 3) % 3)) & (((((_lv0 * 8) + tl.arange(0, 8)) // 3) % 3) < 2)) & (1 <= (((_lv0 * 8) + tl.arange(0, 8)) % 3))) & ((((_lv0 * 8) + tl.arange(0, 8)) % 3) < 2))), other=0.0) * tl.load(in51_ptr + ((((((tl.program_id(0) % 1728) * 3) + ((((_lv0 * 8) + tl.arange(0, 8)) // 3) % 3)) * 3) + (((_lv0 * 8) + tl.arange(0, 8)) % 3)) + 0 * tl.arange(0, 8)), mask=((((_lv0 * 8) + tl.arange(0, 8)) < 9) & ((((1 <= ((((_lv0 * 8) + tl.arange(0, 8)) // 3) % 3)) & (((((_lv0 * 8) + tl.arange(0, 8)) // 3) % 3) < 2)) & (1 <= (((_lv0 * 8) + tl.arange(0, 8)) % 3))) & ((((_lv0 * 8) + tl.arange(0, 8)) % 3) < 2))), other=0.0)), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t024_s68(out, ins):
    grid = (3456,)
    t024_s68_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37], ins[38], ins[39], ins[40], ins[41], ins[42], ins[43], ins[44], ins[45], ins[46], ins[47], ins[48], ins[49], ins[50], ins[51], ins[52], ins[53], ins[54], ins[55], ins[56], ins[57], ins[58], ins[59], ins[60], ins[61], ins[62], ins[63], ins[64], ins[65], ins[66], ins[67], ins[68], ins[69], ins[70], ins[71], ins[72], ins[73], ins[74], ins[75], ins[76], ins[77], ins[78], ins[79], ins[80], ins[81], ins[82], ins[83], ins[84], ins[85], ins[86], ins[87], ins[88], ins[89], ins[90], ins[91], ins[92], ins[93], ins[94], ins[95], ins[96], ins[97], ins[98], ins[99], ins[100], ins[101], ins[102], ins[103], ins[104], ins[105], ins[106], ins[107], ins[108], ins[109], ins[110], ins[111], ins[112], ins[113], ins[114], ins[115], ins[116], ins[117], ins[118], ins[119], ins[120], ins[121], ins[122], ins[123], ins[124], ins[125], ins[126], ins[127], ins[128], ins[129], ins[130], ins[131])
    return out


@triton.jit
def t024_s69_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr, in38_ptr, in39_ptr, in40_ptr, in41_ptr, in42_ptr, in43_ptr, in44_ptr, in45_ptr, in46_ptr, in47_ptr, in48_ptr, in49_ptr, in50_ptr, in51_ptr, in52_ptr, in53_ptr, in54_ptr, in55_ptr, in56_ptr, in57_ptr, in58_ptr, in59_ptr, in60_ptr, in61_ptr, in62_ptr, in63_ptr, in64_ptr, in65_ptr, in66_ptr, in67_ptr, in68_ptr, in69_ptr, in70_ptr, in71_ptr, in72_ptr, in73_ptr, in74_ptr, in75_ptr, in76_ptr, in77_ptr, in78_ptr, in79_ptr, in80_ptr, in81_ptr, in82_ptr, in83_ptr, in84_ptr, in85_ptr, in86_ptr, in87_ptr, in88_ptr, in89_ptr, in90_ptr, in91_ptr, in92_ptr, in93_ptr, in94_ptr, in95_ptr, in96_ptr, in97_ptr, in98_ptr, in99_ptr, in100_ptr, in101_ptr, in102_ptr, in103_ptr, in104_ptr, in105_ptr, in106_ptr, in107_ptr, in108_ptr, in109_ptr, in110_ptr, in111_ptr, in112_ptr, in113_ptr, in114_ptr, in115_ptr, in116_ptr, in117_ptr, in118_ptr, in119_ptr, in120_ptr, in121_ptr, in122_ptr, in123_ptr, in124_ptr, in125_ptr, in126_ptr, in127_ptr, in128_ptr, in129_ptr, in130_ptr, in131_ptr, in132_ptr):
    _acc0 = tl.zeros([2], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 2) + tl.arange(0, 2)) < 2) & True), tl.load(in132_ptr + (((((_lv0 * 2) + tl.arange(0, 2)) * 1728) + tl.program_id(0)) + 0 * tl.arange(0, 2)), mask=((((_lv0 * 2) + tl.arange(0, 2)) < 2) & True), other=0.0), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t024_s69(out, ins):
    grid = (1728,)
    t024_s69_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37], ins[38], ins[39], ins[40], ins[41], ins[42], ins[43], ins[44], ins[45], ins[46], ins[47], ins[48], ins[49], ins[50], ins[51], ins[52], ins[53], ins[54], ins[55], ins[56], ins[57], ins[58], ins[59], ins[60], ins[61], ins[62], ins[63], ins[64], ins[65], ins[66], ins[67], ins[68], ins[69], ins[70], ins[71], ins[72], ins[73], ins[74], ins[75], ins[76], ins[77], ins[78], ins[79], ins[80], ins[81], ins[82], ins[83], ins[84], ins[85], ins[86], ins[87], ins[88], ins[89], ins[90], ins[91], ins[92], ins[93], ins[94], ins[95], ins[96], ins[97], ins[98], ins[99], ins[100], ins[101], ins[102], ins[103], ins[104], ins[105], ins[106], ins[107], ins[108], ins[109], ins[110], ins[111], ins[112], ins[113], ins[114], ins[115], ins[116], ins[117], ins[118], ins[119], ins[120], ins[121], ins[122], ins[123], ins[124], ins[125], ins[126], ins[127], ins[128], ins[129], ins[130], ins[131], ins[132])
    return out


@triton.jit
def t024_s70_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr, in38_ptr, in39_ptr, in40_ptr, in41_ptr, in42_ptr, in43_ptr, in44_ptr, in45_ptr, in46_ptr, in47_ptr, in48_ptr, in49_ptr, in50_ptr, in51_ptr, in52_ptr, in53_ptr, in54_ptr, in55_ptr, in56_ptr, in57_ptr, in58_ptr, in59_ptr, in60_ptr, in61_ptr, in62_ptr, in63_ptr, in64_ptr, in65_ptr, in66_ptr, in67_ptr, in68_ptr, in69_ptr, in70_ptr, in71_ptr, in72_ptr, in73_ptr, in74_ptr, in75_ptr, in76_ptr, in77_ptr, in78_ptr, in79_ptr, in80_ptr, in81_ptr, in82_ptr, in83_ptr, in84_ptr, in85_ptr, in86_ptr, in87_ptr, in88_ptr, in89_ptr, in90_ptr, in91_ptr, in92_ptr, in93_ptr, in94_ptr, in95_ptr, in96_ptr, in97_ptr, in98_ptr, in99_ptr, in100_ptr, in101_ptr, in102_ptr, in103_ptr, in104_ptr, in105_ptr, in106_ptr, in107_ptr, in108_ptr, in109_ptr, in110_ptr, in111_ptr, in112_ptr, in113_ptr, in114_ptr, in115_ptr, in116_ptr, in117_ptr, in118_ptr, in119_ptr, in120_ptr, in121_ptr, in122_ptr, in123_ptr, in124_ptr, in125_ptr, in126_ptr, in127_ptr, in128_ptr, in129_ptr, in130_ptr, in131_ptr, in132_ptr, in133_ptr):
    _acc0 = tl.zeros([2], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 2) + tl.arange(0, 2)) < 2) & True), ((tl.load(in132_ptr + (((((_lv0 * 2) + tl.arange(0, 2)) * 1728) + tl.program_id(0)) + 0 * tl.arange(0, 2)), mask=((((_lv0 * 2) + tl.arange(0, 2)) < 2) & True), other=0.0) - (tl.load(in133_ptr + (tl.program_id(0) + 0 * tl.arange(0, 2)), mask=((((_lv0 * 2) + tl.arange(0, 2)) < 2) & True), other=0.0) * (1.0 * (1.0 / 2.0)))) * (tl.load(in132_ptr + (((((_lv0 * 2) + tl.arange(0, 2)) * 1728) + tl.program_id(0)) + 0 * tl.arange(0, 2)), mask=((((_lv0 * 2) + tl.arange(0, 2)) < 2) & True), other=0.0) - (tl.load(in133_ptr + (tl.program_id(0) + 0 * tl.arange(0, 2)), mask=((((_lv0 * 2) + tl.arange(0, 2)) < 2) & True), other=0.0) * (1.0 * (1.0 / 2.0))))), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t024_s70(out, ins):
    grid = (1728,)
    t024_s70_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37], ins[38], ins[39], ins[40], ins[41], ins[42], ins[43], ins[44], ins[45], ins[46], ins[47], ins[48], ins[49], ins[50], ins[51], ins[52], ins[53], ins[54], ins[55], ins[56], ins[57], ins[58], ins[59], ins[60], ins[61], ins[62], ins[63], ins[64], ins[65], ins[66], ins[67], ins[68], ins[69], ins[70], ins[71], ins[72], ins[73], ins[74], ins[75], ins[76], ins[77], ins[78], ins[79], ins[80], ins[81], ins[82], ins[83], ins[84], ins[85], ins[86], ins[87], ins[88], ins[89], ins[90], ins[91], ins[92], ins[93], ins[94], ins[95], ins[96], ins[97], ins[98], ins[99], ins[100], ins[101], ins[102], ins[103], ins[104], ins[105], ins[106], ins[107], ins[108], ins[109], ins[110], ins[111], ins[112], ins[113], ins[114], ins[115], ins[116], ins[117], ins[118], ins[119], ins[120], ins[121], ins[122], ins[123], ins[124], ins[125], ins[126], ins[127], ins[128], ins[129], ins[130], ins[131], ins[132], ins[133])
    return out


@triton.jit
def t024_s71_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr, in38_ptr, in39_ptr, in40_ptr, in41_ptr, in42_ptr, in43_ptr, in44_ptr, in45_ptr, in46_ptr, in47_ptr, in48_ptr, in49_ptr, in50_ptr, in51_ptr, in52_ptr, in53_ptr, in54_ptr, in55_ptr, in56_ptr, in57_ptr, in58_ptr, in59_ptr, in60_ptr, in61_ptr, in62_ptr, in63_ptr, in64_ptr, in65_ptr, in66_ptr, in67_ptr, in68_ptr, in69_ptr, in70_ptr, in71_ptr, in72_ptr, in73_ptr, in74_ptr, in75_ptr, in76_ptr, in77_ptr, in78_ptr, in79_ptr, in80_ptr, in81_ptr, in82_ptr, in83_ptr, in84_ptr, in85_ptr, in86_ptr, in87_ptr, in88_ptr, in89_ptr, in90_ptr, in91_ptr, in92_ptr, in93_ptr, in94_ptr, in95_ptr, in96_ptr, in97_ptr, in98_ptr, in99_ptr, in100_ptr, in101_ptr, in102_ptr, in103_ptr, in104_ptr, in105_ptr, in106_ptr, in107_ptr, in108_ptr, in109_ptr, in110_ptr, in111_ptr, in112_ptr, in113_ptr, in114_ptr, in115_ptr, in116_ptr, in117_ptr, in118_ptr, in119_ptr, in120_ptr, in121_ptr, in122_ptr, in123_ptr, in124_ptr, in125_ptr, in126_ptr, in127_ptr, in128_ptr, in129_ptr, in130_ptr, in131_ptr, in132_ptr, in133_ptr, in134_ptr):
    _acc0 = tl.zeros([1], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), ((((tl.load(in132_ptr + (tl.program_id(0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) - (tl.load(in133_ptr + (tl.maximum((tl.program_id(0) % 1728) - tl.maximum((tl.program_id(0) % 1728) - 1727, 0), 0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) * (1.0 * (1.0 / 2.0)))) * (1.0 / tl.sqrt(((tl.load(in134_ptr + (tl.maximum((tl.program_id(0) % 1728) - tl.maximum((tl.program_id(0) % 1728) - 1727, 0), 0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) * (1.0 * (1.0 / 2.0))) + (1.0 * (1.0 / 100000.0)))))) * tl.load(in52_ptr + ((tl.program_id(0) % 1728) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)) + tl.load(in53_ptr + ((tl.program_id(0) % 1728) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)), 0.0))
    _v = tl.maximum(tl.sum(_acc0, axis=0), (0.0 * (1.0 / 1.0)))
    tl.store(out_ptr + tl.program_id(0), _v)


def t024_s71(out, ins):
    grid = (3456,)
    t024_s71_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37], ins[38], ins[39], ins[40], ins[41], ins[42], ins[43], ins[44], ins[45], ins[46], ins[47], ins[48], ins[49], ins[50], ins[51], ins[52], ins[53], ins[54], ins[55], ins[56], ins[57], ins[58], ins[59], ins[60], ins[61], ins[62], ins[63], ins[64], ins[65], ins[66], ins[67], ins[68], ins[69], ins[70], ins[71], ins[72], ins[73], ins[74], ins[75], ins[76], ins[77], ins[78], ins[79], ins[80], ins[81], ins[82], ins[83], ins[84], ins[85], ins[86], ins[87], ins[88], ins[89], ins[90], ins[91], ins[92], ins[93], ins[94], ins[95], ins[96], ins[97], ins[98], ins[99], ins[100], ins[101], ins[102], ins[103], ins[104], ins[105], ins[106], ins[107], ins[108], ins[109], ins[110], ins[111], ins[112], ins[113], ins[114], ins[115], ins[116], ins[117], ins[118], ins[119], ins[120], ins[121], ins[122], ins[123], ins[124], ins[125], ins[126], ins[127], ins[128], ins[129], ins[130], ins[131], ins[132], ins[133], ins[134])
    return out


@triton.jit
def t024_s72_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr, in38_ptr, in39_ptr, in40_ptr, in41_ptr, in42_ptr, in43_ptr, in44_ptr, in45_ptr, in46_ptr, in47_ptr, in48_ptr, in49_ptr, in50_ptr, in51_ptr, in52_ptr, in53_ptr, in54_ptr, in55_ptr, in56_ptr, in57_ptr, in58_ptr, in59_ptr, in60_ptr, in61_ptr, in62_ptr, in63_ptr, in64_ptr, in65_ptr, in66_ptr, in67_ptr, in68_ptr, in69_ptr, in70_ptr, in71_ptr, in72_ptr, in73_ptr, in74_ptr, in75_ptr, in76_ptr, in77_ptr, in78_ptr, in79_ptr, in80_ptr, in81_ptr, in82_ptr, in83_ptr, in84_ptr, in85_ptr, in86_ptr, in87_ptr, in88_ptr, in89_ptr, in90_ptr, in91_ptr, in92_ptr, in93_ptr, in94_ptr, in95_ptr, in96_ptr, in97_ptr, in98_ptr, in99_ptr, in100_ptr, in101_ptr, in102_ptr, in103_ptr, in104_ptr, in105_ptr, in106_ptr, in107_ptr, in108_ptr, in109_ptr, in110_ptr, in111_ptr, in112_ptr, in113_ptr, in114_ptr, in115_ptr, in116_ptr, in117_ptr, in118_ptr, in119_ptr, in120_ptr, in121_ptr, in122_ptr, in123_ptr, in124_ptr, in125_ptr, in126_ptr, in127_ptr, in128_ptr, in129_ptr, in130_ptr, in131_ptr, in132_ptr, in133_ptr, in134_ptr, in135_ptr):
    _acc0 = tl.zeros([1], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), tl.load(in135_ptr + (tl.maximum((tl.program_id(0) + ((_lv0 * 1) + tl.arange(0, 1))) - tl.maximum((tl.program_id(0) + ((_lv0 * 1) + tl.arange(0, 1))) - 3455, 0), 0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0), 0.0))
    _v = (tl.sum(_acc0, axis=0) * (1.0 * (1.0 / 1.0)))
    tl.store(out_ptr + tl.program_id(0), _v)


def t024_s72(out, ins):
    grid = (3456,)
    t024_s72_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37], ins[38], ins[39], ins[40], ins[41], ins[42], ins[43], ins[44], ins[45], ins[46], ins[47], ins[48], ins[49], ins[50], ins[51], ins[52], ins[53], ins[54], ins[55], ins[56], ins[57], ins[58], ins[59], ins[60], ins[61], ins[62], ins[63], ins[64], ins[65], ins[66], ins[67], ins[68], ins[69], ins[70], ins[71], ins[72], ins[73], ins[74], ins[75], ins[76], ins[77], ins[78], ins[79], ins[80], ins[81], ins[82], ins[83], ins[84], ins[85], ins[86], ins[87], ins[88], ins[89], ins[90], ins[91], ins[92], ins[93], ins[94], ins[95], ins[96], ins[97], ins[98], ins[99], ins[100], ins[101], ins[102], ins[103], ins[104], ins[105], ins[106], ins[107], ins[108], ins[109], ins[110], ins[111], ins[112], ins[113], ins[114], ins[115], ins[116], ins[117], ins[118], ins[119], ins[120], ins[121], ins[122], ins[123], ins[124], ins[125], ins[126], ins[127], ins[128], ins[129], ins[130], ins[131], ins[132], ins[133], ins[134], ins[135])
    return out


@triton.jit
def t024_s73_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr, in38_ptr, in39_ptr, in40_ptr, in41_ptr, in42_ptr, in43_ptr, in44_ptr, in45_ptr, in46_ptr, in47_ptr, in48_ptr, in49_ptr, in50_ptr, in51_ptr, in52_ptr, in53_ptr, in54_ptr, in55_ptr, in56_ptr, in57_ptr, in58_ptr, in59_ptr, in60_ptr, in61_ptr, in62_ptr, in63_ptr, in64_ptr, in65_ptr, in66_ptr, in67_ptr, in68_ptr, in69_ptr, in70_ptr, in71_ptr, in72_ptr, in73_ptr, in74_ptr, in75_ptr, in76_ptr, in77_ptr, in78_ptr, in79_ptr, in80_ptr, in81_ptr, in82_ptr, in83_ptr, in84_ptr, in85_ptr, in86_ptr, in87_ptr, in88_ptr, in89_ptr, in90_ptr, in91_ptr, in92_ptr, in93_ptr, in94_ptr, in95_ptr, in96_ptr, in97_ptr, in98_ptr, in99_ptr, in100_ptr, in101_ptr, in102_ptr, in103_ptr, in104_ptr, in105_ptr, in106_ptr, in107_ptr, in108_ptr, in109_ptr, in110_ptr, in111_ptr, in112_ptr, in113_ptr, in114_ptr, in115_ptr, in116_ptr, in117_ptr, in118_ptr, in119_ptr, in120_ptr, in121_ptr, in122_ptr, in123_ptr, in124_ptr, in125_ptr, in126_ptr, in127_ptr, in128_ptr, in129_ptr, in130_ptr, in131_ptr, in132_ptr, in133_ptr, in134_ptr, in135_ptr, in136_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 1728) & ((0 < 1) & (0 < 1))), (tl.load(in136_ptr + ((((tl.program_id(0) // 432) * 1728) + ((_lv0 * 1024) + tl.arange(0, 1024))) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 1728) & ((0 < 1) & (0 < 1))), other=0.0) * tl.load(in54_ptr + ((((tl.program_id(0) % 432) * 1728) + ((_lv0 * 1024) + tl.arange(0, 1024))) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 1728) & ((0 < 1) & (0 < 1))), other=0.0)), 0.0))
    _v = tl.maximum(tl.sum(_acc0, axis=0), (0.0 * (1.0 / 1.0)))
    tl.store(out_ptr + tl.program_id(0), _v)


def t024_s73(out, ins):
    grid = (864,)
    t024_s73_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37], ins[38], ins[39], ins[40], ins[41], ins[42], ins[43], ins[44], ins[45], ins[46], ins[47], ins[48], ins[49], ins[50], ins[51], ins[52], ins[53], ins[54], ins[55], ins[56], ins[57], ins[58], ins[59], ins[60], ins[61], ins[62], ins[63], ins[64], ins[65], ins[66], ins[67], ins[68], ins[69], ins[70], ins[71], ins[72], ins[73], ins[74], ins[75], ins[76], ins[77], ins[78], ins[79], ins[80], ins[81], ins[82], ins[83], ins[84], ins[85], ins[86], ins[87], ins[88], ins[89], ins[90], ins[91], ins[92], ins[93], ins[94], ins[95], ins[96], ins[97], ins[98], ins[99], ins[100], ins[101], ins[102], ins[103], ins[104], ins[105], ins[106], ins[107], ins[108], ins[109], ins[110], ins[111], ins[112], ins[113], ins[114], ins[115], ins[116], ins[117], ins[118], ins[119], ins[120], ins[121], ins[122], ins[123], ins[124], ins[125], ins[126], ins[127], ins[128], ins[129], ins[130], ins[131], ins[132], ins[133], ins[134], ins[135], ins[136])
    return out


@triton.jit
def t024_s74_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr, in38_ptr, in39_ptr, in40_ptr, in41_ptr, in42_ptr, in43_ptr, in44_ptr, in45_ptr, in46_ptr, in47_ptr, in48_ptr, in49_ptr, in50_ptr, in51_ptr, in52_ptr, in53_ptr, in54_ptr, in55_ptr, in56_ptr, in57_ptr, in58_ptr, in59_ptr, in60_ptr, in61_ptr, in62_ptr, in63_ptr, in64_ptr, in65_ptr, in66_ptr, in67_ptr, in68_ptr, in69_ptr, in70_ptr, in71_ptr, in72_ptr, in73_ptr, in74_ptr, in75_ptr, in76_ptr, in77_ptr, in78_ptr, in79_ptr, in80_ptr, in81_ptr, in82_ptr, in83_ptr, in84_ptr, in85_ptr, in86_ptr, in87_ptr, in88_ptr, in89_ptr, in90_ptr, in91_ptr, in92_ptr, in93_ptr, in94_ptr, in95_ptr, in96_ptr, in97_ptr, in98_ptr, in99_ptr, in100_ptr, in101_ptr, in102_ptr, in103_ptr, in104_ptr, in105_ptr, in106_ptr, in107_ptr, in108_ptr, in109_ptr, in110_ptr, in111_ptr, in112_ptr, in113_ptr, in114_ptr, in115_ptr, in116_ptr, in117_ptr, in118_ptr, in119_ptr, in120_ptr, in121_ptr, in122_ptr, in123_ptr, in124_ptr, in125_ptr, in126_ptr, in127_ptr, in128_ptr, in129_ptr, in130_ptr, in131_ptr, in132_ptr, in133_ptr, in134_ptr, in135_ptr, in136_ptr, in137_ptr):
    _acc0 = tl.zeros([256], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 256) + tl.arange(0, 256)) < 432) & ((0 < 1) & (0 < 1))), (tl.load(in137_ptr + ((((tl.program_id(0) // 1728) * 432) + ((_lv0 * 256) + tl.arange(0, 256))) + 0 * tl.arange(0, 256)), mask=((((_lv0 * 256) + tl.arange(0, 256)) < 432) & ((0 < 1) & (0 < 1))), other=0.0) * tl.load(in55_ptr + ((((tl.program_id(0) % 1728) * 432) + ((_lv0 * 256) + tl.arange(0, 256))) + 0 * tl.arange(0, 256)), mask=((((_lv0 * 256) + tl.arange(0, 256)) < 432) & ((0 < 1) & (0 < 1))), other=0.0)), 0.0))
    _v = (1.0 / ((1.0 * (1.0 / 1.0)) + tl.exp(((0.0 * (1.0 / 1.0)) - tl.sum(_acc0, axis=0)))))
    tl.store(out_ptr + tl.program_id(0), _v)


def t024_s74(out, ins):
    grid = (3456,)
    t024_s74_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37], ins[38], ins[39], ins[40], ins[41], ins[42], ins[43], ins[44], ins[45], ins[46], ins[47], ins[48], ins[49], ins[50], ins[51], ins[52], ins[53], ins[54], ins[55], ins[56], ins[57], ins[58], ins[59], ins[60], ins[61], ins[62], ins[63], ins[64], ins[65], ins[66], ins[67], ins[68], ins[69], ins[70], ins[71], ins[72], ins[73], ins[74], ins[75], ins[76], ins[77], ins[78], ins[79], ins[80], ins[81], ins[82], ins[83], ins[84], ins[85], ins[86], ins[87], ins[88], ins[89], ins[90], ins[91], ins[92], ins[93], ins[94], ins[95], ins[96], ins[97], ins[98], ins[99], ins[100], ins[101], ins[102], ins[103], ins[104], ins[105], ins[106], ins[107], ins[108], ins[109], ins[110], ins[111], ins[112], ins[113], ins[114], ins[115], ins[116], ins[117], ins[118], ins[119], ins[120], ins[121], ins[122], ins[123], ins[124], ins[125], ins[126], ins[127], ins[128], ins[129], ins[130], ins[131], ins[132], ins[133], ins[134], ins[135], ins[136], ins[137])
    return out


@triton.jit
def t024_s75_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr, in38_ptr, in39_ptr, in40_ptr, in41_ptr, in42_ptr, in43_ptr, in44_ptr, in45_ptr, in46_ptr, in47_ptr, in48_ptr, in49_ptr, in50_ptr, in51_ptr, in52_ptr, in53_ptr, in54_ptr, in55_ptr, in56_ptr, in57_ptr, in58_ptr, in59_ptr, in60_ptr, in61_ptr, in62_ptr, in63_ptr, in64_ptr, in65_ptr, in66_ptr, in67_ptr, in68_ptr, in69_ptr, in70_ptr, in71_ptr, in72_ptr, in73_ptr, in74_ptr, in75_ptr, in76_ptr, in77_ptr, in78_ptr, in79_ptr, in80_ptr, in81_ptr, in82_ptr, in83_ptr, in84_ptr, in85_ptr, in86_ptr, in87_ptr, in88_ptr, in89_ptr, in90_ptr, in91_ptr, in92_ptr, in93_ptr, in94_ptr, in95_ptr, in96_ptr, in97_ptr, in98_ptr, in99_ptr, in100_ptr, in101_ptr, in102_ptr, in103_ptr, in104_ptr, in105_ptr, in106_ptr, in107_ptr, in108_ptr, in109_ptr, in110_ptr, in111_ptr, in112_ptr, in113_ptr, in114_ptr, in115_ptr, in116_ptr, in117_ptr, in118_ptr, in119_ptr, in120_ptr, in121_ptr, in122_ptr, in123_ptr, in124_ptr, in125_ptr, in126_ptr, in127_ptr, in128_ptr, in129_ptr, in130_ptr, in131_ptr, in132_ptr, in133_ptr, in134_ptr, in135_ptr, in136_ptr, in137_ptr, in138_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 1728) & ((0 < 1) & (0 < 1))), (tl.load(in138_ptr + ((((tl.program_id(0) // 384) * 1728) + ((_lv0 * 1024) + tl.arange(0, 1024))) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 1728) & ((0 < 1) & (0 < 1))), other=0.0) * tl.load(in56_ptr + ((((tl.program_id(0) % 384) * 1728) + ((_lv0 * 1024) + tl.arange(0, 1024))) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 1728) & ((0 < 1) & (0 < 1))), other=0.0)), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t024_s75(out, ins):
    grid = (768,)
    t024_s75_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37], ins[38], ins[39], ins[40], ins[41], ins[42], ins[43], ins[44], ins[45], ins[46], ins[47], ins[48], ins[49], ins[50], ins[51], ins[52], ins[53], ins[54], ins[55], ins[56], ins[57], ins[58], ins[59], ins[60], ins[61], ins[62], ins[63], ins[64], ins[65], ins[66], ins[67], ins[68], ins[69], ins[70], ins[71], ins[72], ins[73], ins[74], ins[75], ins[76], ins[77], ins[78], ins[79], ins[80], ins[81], ins[82], ins[83], ins[84], ins[85], ins[86], ins[87], ins[88], ins[89], ins[90], ins[91], ins[92], ins[93], ins[94], ins[95], ins[96], ins[97], ins[98], ins[99], ins[100], ins[101], ins[102], ins[103], ins[104], ins[105], ins[106], ins[107], ins[108], ins[109], ins[110], ins[111], ins[112], ins[113], ins[114], ins[115], ins[116], ins[117], ins[118], ins[119], ins[120], ins[121], ins[122], ins[123], ins[124], ins[125], ins[126], ins[127], ins[128], ins[129], ins[130], ins[131], ins[132], ins[133], ins[134], ins[135], ins[136], ins[137], ins[138])
    return out


@triton.jit
def t024_s76_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr, in38_ptr, in39_ptr, in40_ptr, in41_ptr, in42_ptr, in43_ptr, in44_ptr, in45_ptr, in46_ptr, in47_ptr, in48_ptr, in49_ptr, in50_ptr, in51_ptr, in52_ptr, in53_ptr, in54_ptr, in55_ptr, in56_ptr, in57_ptr, in58_ptr, in59_ptr, in60_ptr, in61_ptr, in62_ptr, in63_ptr, in64_ptr, in65_ptr, in66_ptr, in67_ptr, in68_ptr, in69_ptr, in70_ptr, in71_ptr, in72_ptr, in73_ptr, in74_ptr, in75_ptr, in76_ptr, in77_ptr, in78_ptr, in79_ptr, in80_ptr, in81_ptr, in82_ptr, in83_ptr, in84_ptr, in85_ptr, in86_ptr, in87_ptr, in88_ptr, in89_ptr, in90_ptr, in91_ptr, in92_ptr, in93_ptr, in94_ptr, in95_ptr, in96_ptr, in97_ptr, in98_ptr, in99_ptr, in100_ptr, in101_ptr, in102_ptr, in103_ptr, in104_ptr, in105_ptr, in106_ptr, in107_ptr, in108_ptr, in109_ptr, in110_ptr, in111_ptr, in112_ptr, in113_ptr, in114_ptr, in115_ptr, in116_ptr, in117_ptr, in118_ptr, in119_ptr, in120_ptr, in121_ptr, in122_ptr, in123_ptr, in124_ptr, in125_ptr, in126_ptr, in127_ptr, in128_ptr, in129_ptr, in130_ptr, in131_ptr, in132_ptr, in133_ptr, in134_ptr, in135_ptr, in136_ptr, in137_ptr, in138_ptr, in139_ptr):
    _acc0 = tl.zeros([2], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 2) + tl.arange(0, 2)) < 2) & True), tl.load(in139_ptr + (((((_lv0 * 2) + tl.arange(0, 2)) * 384) + tl.program_id(0)) + 0 * tl.arange(0, 2)), mask=((((_lv0 * 2) + tl.arange(0, 2)) < 2) & True), other=0.0), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t024_s76(out, ins):
    grid = (384,)
    t024_s76_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37], ins[38], ins[39], ins[40], ins[41], ins[42], ins[43], ins[44], ins[45], ins[46], ins[47], ins[48], ins[49], ins[50], ins[51], ins[52], ins[53], ins[54], ins[55], ins[56], ins[57], ins[58], ins[59], ins[60], ins[61], ins[62], ins[63], ins[64], ins[65], ins[66], ins[67], ins[68], ins[69], ins[70], ins[71], ins[72], ins[73], ins[74], ins[75], ins[76], ins[77], ins[78], ins[79], ins[80], ins[81], ins[82], ins[83], ins[84], ins[85], ins[86], ins[87], ins[88], ins[89], ins[90], ins[91], ins[92], ins[93], ins[94], ins[95], ins[96], ins[97], ins[98], ins[99], ins[100], ins[101], ins[102], ins[103], ins[104], ins[105], ins[106], ins[107], ins[108], ins[109], ins[110], ins[111], ins[112], ins[113], ins[114], ins[115], ins[116], ins[117], ins[118], ins[119], ins[120], ins[121], ins[122], ins[123], ins[124], ins[125], ins[126], ins[127], ins[128], ins[129], ins[130], ins[131], ins[132], ins[133], ins[134], ins[135], ins[136], ins[137], ins[138], ins[139])
    return out


@triton.jit
def t024_s77_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr, in38_ptr, in39_ptr, in40_ptr, in41_ptr, in42_ptr, in43_ptr, in44_ptr, in45_ptr, in46_ptr, in47_ptr, in48_ptr, in49_ptr, in50_ptr, in51_ptr, in52_ptr, in53_ptr, in54_ptr, in55_ptr, in56_ptr, in57_ptr, in58_ptr, in59_ptr, in60_ptr, in61_ptr, in62_ptr, in63_ptr, in64_ptr, in65_ptr, in66_ptr, in67_ptr, in68_ptr, in69_ptr, in70_ptr, in71_ptr, in72_ptr, in73_ptr, in74_ptr, in75_ptr, in76_ptr, in77_ptr, in78_ptr, in79_ptr, in80_ptr, in81_ptr, in82_ptr, in83_ptr, in84_ptr, in85_ptr, in86_ptr, in87_ptr, in88_ptr, in89_ptr, in90_ptr, in91_ptr, in92_ptr, in93_ptr, in94_ptr, in95_ptr, in96_ptr, in97_ptr, in98_ptr, in99_ptr, in100_ptr, in101_ptr, in102_ptr, in103_ptr, in104_ptr, in105_ptr, in106_ptr, in107_ptr, in108_ptr, in109_ptr, in110_ptr, in111_ptr, in112_ptr, in113_ptr, in114_ptr, in115_ptr, in116_ptr, in117_ptr, in118_ptr, in119_ptr, in120_ptr, in121_ptr, in122_ptr, in123_ptr, in124_ptr, in125_ptr, in126_ptr, in127_ptr, in128_ptr, in129_ptr, in130_ptr, in131_ptr, in132_ptr, in133_ptr, in134_ptr, in135_ptr, in136_ptr, in137_ptr, in138_ptr, in139_ptr, in140_ptr):
    _acc0 = tl.zeros([2], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 2) + tl.arange(0, 2)) < 2) & True), ((tl.load(in139_ptr + (((((_lv0 * 2) + tl.arange(0, 2)) * 384) + tl.program_id(0)) + 0 * tl.arange(0, 2)), mask=((((_lv0 * 2) + tl.arange(0, 2)) < 2) & True), other=0.0) - (tl.load(in140_ptr + (tl.program_id(0) + 0 * tl.arange(0, 2)), mask=((((_lv0 * 2) + tl.arange(0, 2)) < 2) & True), other=0.0) * (1.0 * (1.0 / 2.0)))) * (tl.load(in139_ptr + (((((_lv0 * 2) + tl.arange(0, 2)) * 384) + tl.program_id(0)) + 0 * tl.arange(0, 2)), mask=((((_lv0 * 2) + tl.arange(0, 2)) < 2) & True), other=0.0) - (tl.load(in140_ptr + (tl.program_id(0) + 0 * tl.arange(0, 2)), mask=((((_lv0 * 2) + tl.arange(0, 2)) < 2) & True), other=0.0) * (1.0 * (1.0 / 2.0))))), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t024_s77(out, ins):
    grid = (384,)
    t024_s77_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37], ins[38], ins[39], ins[40], ins[41], ins[42], ins[43], ins[44], ins[45], ins[46], ins[47], ins[48], ins[49], ins[50], ins[51], ins[52], ins[53], ins[54], ins[55], ins[56], ins[57], ins[58], ins[59], ins[60], ins[61], ins[62], ins[63], ins[64], ins[65], ins[66], ins[67], ins[68], ins[69], ins[70], ins[71], ins[72], ins[73], ins[74], ins[75], ins[76], ins[77], ins[78], ins[79], ins[80], ins[81], ins[82], ins[83], ins[84], ins[85], ins[86], ins[87], ins[88], ins[89], ins[90], ins[91], ins[92], ins[93], ins[94], ins[95], ins[96], ins[97], ins[98], ins[99], ins[100], ins[101], ins[102], ins[103], ins[104], ins[105], ins[106], ins[107], ins[108], ins[109], ins[110], ins[111], ins[112], ins[113], ins[114], ins[115], ins[116], ins[117], ins[118], ins[119], ins[120], ins[121], ins[122], ins[123], ins[124], ins[125], ins[126], ins[127], ins[128], ins[129], ins[130], ins[131], ins[132], ins[133], ins[134], ins[135], ins[136], ins[137], ins[138], ins[139], ins[140])
    return out


@triton.jit
def t024_s78_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr, in38_ptr, in39_ptr, in40_ptr, in41_ptr, in42_ptr, in43_ptr, in44_ptr, in45_ptr, in46_ptr, in47_ptr, in48_ptr, in49_ptr, in50_ptr, in51_ptr, in52_ptr, in53_ptr, in54_ptr, in55_ptr, in56_ptr, in57_ptr, in58_ptr, in59_ptr, in60_ptr, in61_ptr, in62_ptr, in63_ptr, in64_ptr, in65_ptr, in66_ptr, in67_ptr, in68_ptr, in69_ptr, in70_ptr, in71_ptr, in72_ptr, in73_ptr, in74_ptr, in75_ptr, in76_ptr, in77_ptr, in78_ptr, in79_ptr, in80_ptr, in81_ptr, in82_ptr, in83_ptr, in84_ptr, in85_ptr, in86_ptr, in87_ptr, in88_ptr, in89_ptr, in90_ptr, in91_ptr, in92_ptr, in93_ptr, in94_ptr, in95_ptr, in96_ptr, in97_ptr, in98_ptr, in99_ptr, in100_ptr, in101_ptr, in102_ptr, in103_ptr, in104_ptr, in105_ptr, in106_ptr, in107_ptr, in108_ptr, in109_ptr, in110_ptr, in111_ptr, in112_ptr, in113_ptr, in114_ptr, in115_ptr, in116_ptr, in117_ptr, in118_ptr, in119_ptr, in120_ptr, in121_ptr, in122_ptr, in123_ptr, in124_ptr, in125_ptr, in126_ptr, in127_ptr, in128_ptr, in129_ptr, in130_ptr, in131_ptr, in132_ptr, in133_ptr, in134_ptr, in135_ptr, in136_ptr, in137_ptr, in138_ptr, in139_ptr, in140_ptr, in141_ptr):
    _acc0 = tl.zeros([1], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), ((((tl.load(in139_ptr + (tl.program_id(0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) - (tl.load(in140_ptr + (tl.maximum((tl.program_id(0) % 384) - tl.maximum((tl.program_id(0) % 384) - 383, 0), 0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) * (1.0 * (1.0 / 2.0)))) * (1.0 / tl.sqrt(((tl.load(in141_ptr + (tl.maximum((tl.program_id(0) % 384) - tl.maximum((tl.program_id(0) % 384) - 383, 0), 0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) * (1.0 * (1.0 / 2.0))) + (1.0 * (1.0 / 100000.0)))))) * tl.load(in57_ptr + ((tl.program_id(0) % 384) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)) + tl.load(in58_ptr + ((tl.program_id(0) % 384) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t024_s78(out, ins):
    grid = (768,)
    t024_s78_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37], ins[38], ins[39], ins[40], ins[41], ins[42], ins[43], ins[44], ins[45], ins[46], ins[47], ins[48], ins[49], ins[50], ins[51], ins[52], ins[53], ins[54], ins[55], ins[56], ins[57], ins[58], ins[59], ins[60], ins[61], ins[62], ins[63], ins[64], ins[65], ins[66], ins[67], ins[68], ins[69], ins[70], ins[71], ins[72], ins[73], ins[74], ins[75], ins[76], ins[77], ins[78], ins[79], ins[80], ins[81], ins[82], ins[83], ins[84], ins[85], ins[86], ins[87], ins[88], ins[89], ins[90], ins[91], ins[92], ins[93], ins[94], ins[95], ins[96], ins[97], ins[98], ins[99], ins[100], ins[101], ins[102], ins[103], ins[104], ins[105], ins[106], ins[107], ins[108], ins[109], ins[110], ins[111], ins[112], ins[113], ins[114], ins[115], ins[116], ins[117], ins[118], ins[119], ins[120], ins[121], ins[122], ins[123], ins[124], ins[125], ins[126], ins[127], ins[128], ins[129], ins[130], ins[131], ins[132], ins[133], ins[134], ins[135], ins[136], ins[137], ins[138], ins[139], ins[140], ins[141])
    return out


@triton.jit
def t024_s79_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr, in38_ptr, in39_ptr, in40_ptr, in41_ptr, in42_ptr, in43_ptr, in44_ptr, in45_ptr, in46_ptr, in47_ptr, in48_ptr, in49_ptr, in50_ptr, in51_ptr, in52_ptr, in53_ptr, in54_ptr, in55_ptr, in56_ptr, in57_ptr, in58_ptr, in59_ptr, in60_ptr, in61_ptr, in62_ptr, in63_ptr, in64_ptr, in65_ptr, in66_ptr, in67_ptr, in68_ptr, in69_ptr, in70_ptr, in71_ptr, in72_ptr, in73_ptr, in74_ptr, in75_ptr, in76_ptr, in77_ptr, in78_ptr, in79_ptr, in80_ptr, in81_ptr, in82_ptr, in83_ptr, in84_ptr, in85_ptr, in86_ptr, in87_ptr, in88_ptr, in89_ptr, in90_ptr, in91_ptr, in92_ptr, in93_ptr, in94_ptr, in95_ptr, in96_ptr, in97_ptr, in98_ptr, in99_ptr, in100_ptr, in101_ptr, in102_ptr, in103_ptr, in104_ptr, in105_ptr, in106_ptr, in107_ptr, in108_ptr, in109_ptr, in110_ptr, in111_ptr, in112_ptr, in113_ptr, in114_ptr, in115_ptr, in116_ptr, in117_ptr, in118_ptr, in119_ptr, in120_ptr, in121_ptr, in122_ptr, in123_ptr, in124_ptr, in125_ptr, in126_ptr, in127_ptr, in128_ptr, in129_ptr, in130_ptr, in131_ptr, in132_ptr, in133_ptr, in134_ptr, in135_ptr, in136_ptr, in137_ptr, in138_ptr, in139_ptr, in140_ptr, in141_ptr, in142_ptr):
    _acc0 = tl.zeros([256], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 256) + tl.arange(0, 256)) < 384) & ((0 < 1) & (0 < 1))), (tl.load(in142_ptr + ((((tl.program_id(0) // 1408) * 384) + ((_lv0 * 256) + tl.arange(0, 256))) + 0 * tl.arange(0, 256)), mask=((((_lv0 * 256) + tl.arange(0, 256)) < 384) & ((0 < 1) & (0 < 1))), other=0.0) * tl.load(in59_ptr + ((((tl.program_id(0) % 1408) * 384) + ((_lv0 * 256) + tl.arange(0, 256))) + 0 * tl.arange(0, 256)), mask=((((_lv0 * 256) + tl.arange(0, 256)) < 384) & ((0 < 1) & (0 < 1))), other=0.0)), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t024_s79(out, ins):
    grid = (2816,)
    t024_s79_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37], ins[38], ins[39], ins[40], ins[41], ins[42], ins[43], ins[44], ins[45], ins[46], ins[47], ins[48], ins[49], ins[50], ins[51], ins[52], ins[53], ins[54], ins[55], ins[56], ins[57], ins[58], ins[59], ins[60], ins[61], ins[62], ins[63], ins[64], ins[65], ins[66], ins[67], ins[68], ins[69], ins[70], ins[71], ins[72], ins[73], ins[74], ins[75], ins[76], ins[77], ins[78], ins[79], ins[80], ins[81], ins[82], ins[83], ins[84], ins[85], ins[86], ins[87], ins[88], ins[89], ins[90], ins[91], ins[92], ins[93], ins[94], ins[95], ins[96], ins[97], ins[98], ins[99], ins[100], ins[101], ins[102], ins[103], ins[104], ins[105], ins[106], ins[107], ins[108], ins[109], ins[110], ins[111], ins[112], ins[113], ins[114], ins[115], ins[116], ins[117], ins[118], ins[119], ins[120], ins[121], ins[122], ins[123], ins[124], ins[125], ins[126], ins[127], ins[128], ins[129], ins[130], ins[131], ins[132], ins[133], ins[134], ins[135], ins[136], ins[137], ins[138], ins[139], ins[140], ins[141], ins[142])
    return out


@triton.jit
def t024_s80_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr, in38_ptr, in39_ptr, in40_ptr, in41_ptr, in42_ptr, in43_ptr, in44_ptr, in45_ptr, in46_ptr, in47_ptr, in48_ptr, in49_ptr, in50_ptr, in51_ptr, in52_ptr, in53_ptr, in54_ptr, in55_ptr, in56_ptr, in57_ptr, in58_ptr, in59_ptr, in60_ptr, in61_ptr, in62_ptr, in63_ptr, in64_ptr, in65_ptr, in66_ptr, in67_ptr, in68_ptr, in69_ptr, in70_ptr, in71_ptr, in72_ptr, in73_ptr, in74_ptr, in75_ptr, in76_ptr, in77_ptr, in78_ptr, in79_ptr, in80_ptr, in81_ptr, in82_ptr, in83_ptr, in84_ptr, in85_ptr, in86_ptr, in87_ptr, in88_ptr, in89_ptr, in90_ptr, in91_ptr, in92_ptr, in93_ptr, in94_ptr, in95_ptr, in96_ptr, in97_ptr, in98_ptr, in99_ptr, in100_ptr, in101_ptr, in102_ptr, in103_ptr, in104_ptr, in105_ptr, in106_ptr, in107_ptr, in108_ptr, in109_ptr, in110_ptr, in111_ptr, in112_ptr, in113_ptr, in114_ptr, in115_ptr, in116_ptr, in117_ptr, in118_ptr, in119_ptr, in120_ptr, in121_ptr, in122_ptr, in123_ptr, in124_ptr, in125_ptr, in126_ptr, in127_ptr, in128_ptr, in129_ptr, in130_ptr, in131_ptr, in132_ptr, in133_ptr, in134_ptr, in135_ptr, in136_ptr, in137_ptr, in138_ptr, in139_ptr, in140_ptr, in141_ptr, in142_ptr, in143_ptr):
    _acc0 = tl.zeros([2], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 2) + tl.arange(0, 2)) < 2) & True), tl.load(in143_ptr + (((((_lv0 * 2) + tl.arange(0, 2)) * 1408) + tl.program_id(0)) + 0 * tl.arange(0, 2)), mask=((((_lv0 * 2) + tl.arange(0, 2)) < 2) & True), other=0.0), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t024_s80(out, ins):
    grid = (1408,)
    t024_s80_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37], ins[38], ins[39], ins[40], ins[41], ins[42], ins[43], ins[44], ins[45], ins[46], ins[47], ins[48], ins[49], ins[50], ins[51], ins[52], ins[53], ins[54], ins[55], ins[56], ins[57], ins[58], ins[59], ins[60], ins[61], ins[62], ins[63], ins[64], ins[65], ins[66], ins[67], ins[68], ins[69], ins[70], ins[71], ins[72], ins[73], ins[74], ins[75], ins[76], ins[77], ins[78], ins[79], ins[80], ins[81], ins[82], ins[83], ins[84], ins[85], ins[86], ins[87], ins[88], ins[89], ins[90], ins[91], ins[92], ins[93], ins[94], ins[95], ins[96], ins[97], ins[98], ins[99], ins[100], ins[101], ins[102], ins[103], ins[104], ins[105], ins[106], ins[107], ins[108], ins[109], ins[110], ins[111], ins[112], ins[113], ins[114], ins[115], ins[116], ins[117], ins[118], ins[119], ins[120], ins[121], ins[122], ins[123], ins[124], ins[125], ins[126], ins[127], ins[128], ins[129], ins[130], ins[131], ins[132], ins[133], ins[134], ins[135], ins[136], ins[137], ins[138], ins[139], ins[140], ins[141], ins[142], ins[143])
    return out


@triton.jit
def t024_s81_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr, in38_ptr, in39_ptr, in40_ptr, in41_ptr, in42_ptr, in43_ptr, in44_ptr, in45_ptr, in46_ptr, in47_ptr, in48_ptr, in49_ptr, in50_ptr, in51_ptr, in52_ptr, in53_ptr, in54_ptr, in55_ptr, in56_ptr, in57_ptr, in58_ptr, in59_ptr, in60_ptr, in61_ptr, in62_ptr, in63_ptr, in64_ptr, in65_ptr, in66_ptr, in67_ptr, in68_ptr, in69_ptr, in70_ptr, in71_ptr, in72_ptr, in73_ptr, in74_ptr, in75_ptr, in76_ptr, in77_ptr, in78_ptr, in79_ptr, in80_ptr, in81_ptr, in82_ptr, in83_ptr, in84_ptr, in85_ptr, in86_ptr, in87_ptr, in88_ptr, in89_ptr, in90_ptr, in91_ptr, in92_ptr, in93_ptr, in94_ptr, in95_ptr, in96_ptr, in97_ptr, in98_ptr, in99_ptr, in100_ptr, in101_ptr, in102_ptr, in103_ptr, in104_ptr, in105_ptr, in106_ptr, in107_ptr, in108_ptr, in109_ptr, in110_ptr, in111_ptr, in112_ptr, in113_ptr, in114_ptr, in115_ptr, in116_ptr, in117_ptr, in118_ptr, in119_ptr, in120_ptr, in121_ptr, in122_ptr, in123_ptr, in124_ptr, in125_ptr, in126_ptr, in127_ptr, in128_ptr, in129_ptr, in130_ptr, in131_ptr, in132_ptr, in133_ptr, in134_ptr, in135_ptr, in136_ptr, in137_ptr, in138_ptr, in139_ptr, in140_ptr, in141_ptr, in142_ptr, in143_ptr, in144_ptr):
    _acc0 = tl.zeros([2], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 2) + tl.arange(0, 2)) < 2) & True), ((tl.load(in143_ptr + (((((_lv0 * 2) + tl.arange(0, 2)) * 1408) + tl.program_id(0)) + 0 * tl.arange(0, 2)), mask=((((_lv0 * 2) + tl.arange(0, 2)) < 2) & True), other=0.0) - (tl.load(in144_ptr + (tl.program_id(0) + 0 * tl.arange(0, 2)), mask=((((_lv0 * 2) + tl.arange(0, 2)) < 2) & True), other=0.0) * (1.0 * (1.0 / 2.0)))) * (tl.load(in143_ptr + (((((_lv0 * 2) + tl.arange(0, 2)) * 1408) + tl.program_id(0)) + 0 * tl.arange(0, 2)), mask=((((_lv0 * 2) + tl.arange(0, 2)) < 2) & True), other=0.0) - (tl.load(in144_ptr + (tl.program_id(0) + 0 * tl.arange(0, 2)), mask=((((_lv0 * 2) + tl.arange(0, 2)) < 2) & True), other=0.0) * (1.0 * (1.0 / 2.0))))), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t024_s81(out, ins):
    grid = (1408,)
    t024_s81_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37], ins[38], ins[39], ins[40], ins[41], ins[42], ins[43], ins[44], ins[45], ins[46], ins[47], ins[48], ins[49], ins[50], ins[51], ins[52], ins[53], ins[54], ins[55], ins[56], ins[57], ins[58], ins[59], ins[60], ins[61], ins[62], ins[63], ins[64], ins[65], ins[66], ins[67], ins[68], ins[69], ins[70], ins[71], ins[72], ins[73], ins[74], ins[75], ins[76], ins[77], ins[78], ins[79], ins[80], ins[81], ins[82], ins[83], ins[84], ins[85], ins[86], ins[87], ins[88], ins[89], ins[90], ins[91], ins[92], ins[93], ins[94], ins[95], ins[96], ins[97], ins[98], ins[99], ins[100], ins[101], ins[102], ins[103], ins[104], ins[105], ins[106], ins[107], ins[108], ins[109], ins[110], ins[111], ins[112], ins[113], ins[114], ins[115], ins[116], ins[117], ins[118], ins[119], ins[120], ins[121], ins[122], ins[123], ins[124], ins[125], ins[126], ins[127], ins[128], ins[129], ins[130], ins[131], ins[132], ins[133], ins[134], ins[135], ins[136], ins[137], ins[138], ins[139], ins[140], ins[141], ins[142], ins[143], ins[144])
    return out


@triton.jit
def t024_s82_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr, in38_ptr, in39_ptr, in40_ptr, in41_ptr, in42_ptr, in43_ptr, in44_ptr, in45_ptr, in46_ptr, in47_ptr, in48_ptr, in49_ptr, in50_ptr, in51_ptr, in52_ptr, in53_ptr, in54_ptr, in55_ptr, in56_ptr, in57_ptr, in58_ptr, in59_ptr, in60_ptr, in61_ptr, in62_ptr, in63_ptr, in64_ptr, in65_ptr, in66_ptr, in67_ptr, in68_ptr, in69_ptr, in70_ptr, in71_ptr, in72_ptr, in73_ptr, in74_ptr, in75_ptr, in76_ptr, in77_ptr, in78_ptr, in79_ptr, in80_ptr, in81_ptr, in82_ptr, in83_ptr, in84_ptr, in85_ptr, in86_ptr, in87_ptr, in88_ptr, in89_ptr, in90_ptr, in91_ptr, in92_ptr, in93_ptr, in94_ptr, in95_ptr, in96_ptr, in97_ptr, in98_ptr, in99_ptr, in100_ptr, in101_ptr, in102_ptr, in103_ptr, in104_ptr, in105_ptr, in106_ptr, in107_ptr, in108_ptr, in109_ptr, in110_ptr, in111_ptr, in112_ptr, in113_ptr, in114_ptr, in115_ptr, in116_ptr, in117_ptr, in118_ptr, in119_ptr, in120_ptr, in121_ptr, in122_ptr, in123_ptr, in124_ptr, in125_ptr, in126_ptr, in127_ptr, in128_ptr, in129_ptr, in130_ptr, in131_ptr, in132_ptr, in133_ptr, in134_ptr, in135_ptr, in136_ptr, in137_ptr, in138_ptr, in139_ptr, in140_ptr, in141_ptr, in142_ptr, in143_ptr, in144_ptr, in145_ptr):
    _acc0 = tl.zeros([1], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), ((((tl.load(in143_ptr + (tl.program_id(0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) - (tl.load(in144_ptr + (tl.maximum((tl.program_id(0) % 1408) - tl.maximum((tl.program_id(0) % 1408) - 1407, 0), 0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) * (1.0 * (1.0 / 2.0)))) * (1.0 / tl.sqrt(((tl.load(in145_ptr + (tl.maximum((tl.program_id(0) % 1408) - tl.maximum((tl.program_id(0) % 1408) - 1407, 0), 0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) * (1.0 * (1.0 / 2.0))) + (1.0 * (1.0 / 100000.0)))))) * tl.load(in60_ptr + ((tl.program_id(0) % 1408) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)) + tl.load(in61_ptr + ((tl.program_id(0) % 1408) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)), 0.0))
    _v = tl.maximum(tl.sum(_acc0, axis=0), (0.0 * (1.0 / 1.0)))
    tl.store(out_ptr + tl.program_id(0), _v)


def t024_s82(out, ins):
    grid = (2816,)
    t024_s82_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37], ins[38], ins[39], ins[40], ins[41], ins[42], ins[43], ins[44], ins[45], ins[46], ins[47], ins[48], ins[49], ins[50], ins[51], ins[52], ins[53], ins[54], ins[55], ins[56], ins[57], ins[58], ins[59], ins[60], ins[61], ins[62], ins[63], ins[64], ins[65], ins[66], ins[67], ins[68], ins[69], ins[70], ins[71], ins[72], ins[73], ins[74], ins[75], ins[76], ins[77], ins[78], ins[79], ins[80], ins[81], ins[82], ins[83], ins[84], ins[85], ins[86], ins[87], ins[88], ins[89], ins[90], ins[91], ins[92], ins[93], ins[94], ins[95], ins[96], ins[97], ins[98], ins[99], ins[100], ins[101], ins[102], ins[103], ins[104], ins[105], ins[106], ins[107], ins[108], ins[109], ins[110], ins[111], ins[112], ins[113], ins[114], ins[115], ins[116], ins[117], ins[118], ins[119], ins[120], ins[121], ins[122], ins[123], ins[124], ins[125], ins[126], ins[127], ins[128], ins[129], ins[130], ins[131], ins[132], ins[133], ins[134], ins[135], ins[136], ins[137], ins[138], ins[139], ins[140], ins[141], ins[142], ins[143], ins[144], ins[145])
    return out


@triton.jit
def t024_s83_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr, in38_ptr, in39_ptr, in40_ptr, in41_ptr, in42_ptr, in43_ptr, in44_ptr, in45_ptr, in46_ptr, in47_ptr, in48_ptr, in49_ptr, in50_ptr, in51_ptr, in52_ptr, in53_ptr, in54_ptr, in55_ptr, in56_ptr, in57_ptr, in58_ptr, in59_ptr, in60_ptr, in61_ptr, in62_ptr, in63_ptr, in64_ptr, in65_ptr, in66_ptr, in67_ptr, in68_ptr, in69_ptr, in70_ptr, in71_ptr, in72_ptr, in73_ptr, in74_ptr, in75_ptr, in76_ptr, in77_ptr, in78_ptr, in79_ptr, in80_ptr, in81_ptr, in82_ptr, in83_ptr, in84_ptr, in85_ptr, in86_ptr, in87_ptr, in88_ptr, in89_ptr, in90_ptr, in91_ptr, in92_ptr, in93_ptr, in94_ptr, in95_ptr, in96_ptr, in97_ptr, in98_ptr, in99_ptr, in100_ptr, in101_ptr, in102_ptr, in103_ptr, in104_ptr, in105_ptr, in106_ptr, in107_ptr, in108_ptr, in109_ptr, in110_ptr, in111_ptr, in112_ptr, in113_ptr, in114_ptr, in115_ptr, in116_ptr, in117_ptr, in118_ptr, in119_ptr, in120_ptr, in121_ptr, in122_ptr, in123_ptr, in124_ptr, in125_ptr, in126_ptr, in127_ptr, in128_ptr, in129_ptr, in130_ptr, in131_ptr, in132_ptr, in133_ptr, in134_ptr, in135_ptr, in136_ptr, in137_ptr, in138_ptr, in139_ptr, in140_ptr, in141_ptr, in142_ptr, in143_ptr, in144_ptr, in145_ptr, in146_ptr):
    _acc0 = tl.zeros([1], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), tl.load(in146_ptr + (tl.maximum((tl.program_id(0) + ((_lv0 * 1) + tl.arange(0, 1))) - tl.maximum((tl.program_id(0) + ((_lv0 * 1) + tl.arange(0, 1))) - 2815, 0), 0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0), 0.0))
    _v = (tl.sum(_acc0, axis=0) * (1.0 * (1.0 / 1.0)))
    tl.store(out_ptr + tl.program_id(0), _v)


def t024_s83(out, ins):
    grid = (2816,)
    t024_s83_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37], ins[38], ins[39], ins[40], ins[41], ins[42], ins[43], ins[44], ins[45], ins[46], ins[47], ins[48], ins[49], ins[50], ins[51], ins[52], ins[53], ins[54], ins[55], ins[56], ins[57], ins[58], ins[59], ins[60], ins[61], ins[62], ins[63], ins[64], ins[65], ins[66], ins[67], ins[68], ins[69], ins[70], ins[71], ins[72], ins[73], ins[74], ins[75], ins[76], ins[77], ins[78], ins[79], ins[80], ins[81], ins[82], ins[83], ins[84], ins[85], ins[86], ins[87], ins[88], ins[89], ins[90], ins[91], ins[92], ins[93], ins[94], ins[95], ins[96], ins[97], ins[98], ins[99], ins[100], ins[101], ins[102], ins[103], ins[104], ins[105], ins[106], ins[107], ins[108], ins[109], ins[110], ins[111], ins[112], ins[113], ins[114], ins[115], ins[116], ins[117], ins[118], ins[119], ins[120], ins[121], ins[122], ins[123], ins[124], ins[125], ins[126], ins[127], ins[128], ins[129], ins[130], ins[131], ins[132], ins[133], ins[134], ins[135], ins[136], ins[137], ins[138], ins[139], ins[140], ins[141], ins[142], ins[143], ins[144], ins[145], ins[146])
    return out


@triton.jit
def t024_s84_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr, in38_ptr, in39_ptr, in40_ptr, in41_ptr, in42_ptr, in43_ptr, in44_ptr, in45_ptr, in46_ptr, in47_ptr, in48_ptr, in49_ptr, in50_ptr, in51_ptr, in52_ptr, in53_ptr, in54_ptr, in55_ptr, in56_ptr, in57_ptr, in58_ptr, in59_ptr, in60_ptr, in61_ptr, in62_ptr, in63_ptr, in64_ptr, in65_ptr, in66_ptr, in67_ptr, in68_ptr, in69_ptr, in70_ptr, in71_ptr, in72_ptr, in73_ptr, in74_ptr, in75_ptr, in76_ptr, in77_ptr, in78_ptr, in79_ptr, in80_ptr, in81_ptr, in82_ptr, in83_ptr, in84_ptr, in85_ptr, in86_ptr, in87_ptr, in88_ptr, in89_ptr, in90_ptr, in91_ptr, in92_ptr, in93_ptr, in94_ptr, in95_ptr, in96_ptr, in97_ptr, in98_ptr, in99_ptr, in100_ptr, in101_ptr, in102_ptr, in103_ptr, in104_ptr, in105_ptr, in106_ptr, in107_ptr, in108_ptr, in109_ptr, in110_ptr, in111_ptr, in112_ptr, in113_ptr, in114_ptr, in115_ptr, in116_ptr, in117_ptr, in118_ptr, in119_ptr, in120_ptr, in121_ptr, in122_ptr, in123_ptr, in124_ptr, in125_ptr, in126_ptr, in127_ptr, in128_ptr, in129_ptr, in130_ptr, in131_ptr, in132_ptr, in133_ptr, in134_ptr, in135_ptr, in136_ptr, in137_ptr, in138_ptr, in139_ptr, in140_ptr, in141_ptr, in142_ptr, in143_ptr, in144_ptr, in145_ptr, in146_ptr, in147_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 1408) & True), (tl.load(in147_ptr + ((((tl.program_id(0) // 1000) * 1408) + ((_lv0 * 1024) + tl.arange(0, 1024))) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 1408) & True), other=0.0) * tl.load(in62_ptr + ((((tl.program_id(0) % 1000) * 1408) + ((_lv0 * 1024) + tl.arange(0, 1024))) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 1408) & True), other=0.0)), 0.0))
    _v = (tl.sum(_acc0, axis=0) + tl.load(in63_ptr + ((tl.program_id(0) % 1000))))
    tl.store(out_ptr + tl.program_id(0), _v)


def t024_s84(out, ins):
    grid = (2000,)
    t024_s84_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37], ins[38], ins[39], ins[40], ins[41], ins[42], ins[43], ins[44], ins[45], ins[46], ins[47], ins[48], ins[49], ins[50], ins[51], ins[52], ins[53], ins[54], ins[55], ins[56], ins[57], ins[58], ins[59], ins[60], ins[61], ins[62], ins[63], ins[64], ins[65], ins[66], ins[67], ins[68], ins[69], ins[70], ins[71], ins[72], ins[73], ins[74], ins[75], ins[76], ins[77], ins[78], ins[79], ins[80], ins[81], ins[82], ins[83], ins[84], ins[85], ins[86], ins[87], ins[88], ins[89], ins[90], ins[91], ins[92], ins[93], ins[94], ins[95], ins[96], ins[97], ins[98], ins[99], ins[100], ins[101], ins[102], ins[103], ins[104], ins[105], ins[106], ins[107], ins[108], ins[109], ins[110], ins[111], ins[112], ins[113], ins[114], ins[115], ins[116], ins[117], ins[118], ins[119], ins[120], ins[121], ins[122], ins[123], ins[124], ins[125], ins[126], ins[127], ins[128], ins[129], ins[130], ins[131], ins[132], ins[133], ins[134], ins[135], ins[136], ins[137], ins[138], ins[139], ins[140], ins[141], ins[142], ins[143], ins[144], ins[145], ins[146], ins[147])
    return out


def t024(out, ins):
    _t0 = torch.empty(802816, device=ins[0].device, dtype=torch.float32)
    _t1 = torch.empty(32, device=ins[0].device, dtype=torch.float32)
    _t2 = torch.empty(32, device=ins[0].device, dtype=torch.float32)
    _t3 = torch.empty(802816, device=ins[0].device, dtype=torch.float32)
    _t4 = torch.empty(2408448, device=ins[0].device, dtype=torch.float32)
    _t5 = torch.empty(96, device=ins[0].device, dtype=torch.float32)
    _t6 = torch.empty(96, device=ins[0].device, dtype=torch.float32)
    _t7 = torch.empty(2408448, device=ins[0].device, dtype=torch.float32)
    _t8 = torch.empty(2408448, device=ins[0].device, dtype=torch.float32)
    _t9 = torch.empty(96, device=ins[0].device, dtype=torch.float32)
    _t10 = torch.empty(96, device=ins[0].device, dtype=torch.float32)
    _t11 = torch.empty(2408448, device=ins[0].device, dtype=torch.float32)
    _t12 = torch.empty(192, device=ins[0].device, dtype=torch.float32)
    _t13 = torch.empty(48, device=ins[0].device, dtype=torch.float32)
    _t14 = torch.empty(192, device=ins[0].device, dtype=torch.float32)
    _t15 = torch.empty(192, device=ins[0].device, dtype=torch.float32)
    _t16 = torch.empty(96, device=ins[0].device, dtype=torch.float32)
    _t17 = torch.empty(96, device=ins[0].device, dtype=torch.float32)
    _t18 = torch.empty(192, device=ins[0].device, dtype=torch.float32)
    _t19 = torch.empty(1152, device=ins[0].device, dtype=torch.float32)
    _t20 = torch.empty(576, device=ins[0].device, dtype=torch.float32)
    _t21 = torch.empty(576, device=ins[0].device, dtype=torch.float32)
    _t22 = torch.empty(1152, device=ins[0].device, dtype=torch.float32)
    _t23 = torch.empty(1152, device=ins[0].device, dtype=torch.float32)
    _t24 = torch.empty(576, device=ins[0].device, dtype=torch.float32)
    _t25 = torch.empty(576, device=ins[0].device, dtype=torch.float32)
    _t26 = torch.empty(1152, device=ins[0].device, dtype=torch.float32)
    _t27 = torch.empty(1152, device=ins[0].device, dtype=torch.float32)
    _t28 = torch.empty(288, device=ins[0].device, dtype=torch.float32)
    _t29 = torch.empty(1152, device=ins[0].device, dtype=torch.float32)
    _t30 = torch.empty(288, device=ins[0].device, dtype=torch.float32)
    _t31 = torch.empty(144, device=ins[0].device, dtype=torch.float32)
    _t32 = torch.empty(144, device=ins[0].device, dtype=torch.float32)
    _t33 = torch.empty(288, device=ins[0].device, dtype=torch.float32)
    _t34 = torch.empty(1728, device=ins[0].device, dtype=torch.float32)
    _t35 = torch.empty(864, device=ins[0].device, dtype=torch.float32)
    _t36 = torch.empty(864, device=ins[0].device, dtype=torch.float32)
    _t37 = torch.empty(1728, device=ins[0].device, dtype=torch.float32)
    _t38 = torch.empty(1728, device=ins[0].device, dtype=torch.float32)
    _t39 = torch.empty(864, device=ins[0].device, dtype=torch.float32)
    _t40 = torch.empty(864, device=ins[0].device, dtype=torch.float32)
    _t41 = torch.empty(1728, device=ins[0].device, dtype=torch.float32)
    _t42 = torch.empty(1728, device=ins[0].device, dtype=torch.float32)
    _t43 = torch.empty(432, device=ins[0].device, dtype=torch.float32)
    _t44 = torch.empty(1728, device=ins[0].device, dtype=torch.float32)
    _t45 = torch.empty(384, device=ins[0].device, dtype=torch.float32)
    _t46 = torch.empty(192, device=ins[0].device, dtype=torch.float32)
    _t47 = torch.empty(192, device=ins[0].device, dtype=torch.float32)
    _t48 = torch.empty(384, device=ins[0].device, dtype=torch.float32)
    _t49 = torch.empty(2304, device=ins[0].device, dtype=torch.float32)
    _t50 = torch.empty(1152, device=ins[0].device, dtype=torch.float32)
    _t51 = torch.empty(1152, device=ins[0].device, dtype=torch.float32)
    _t52 = torch.empty(2304, device=ins[0].device, dtype=torch.float32)
    _t53 = torch.empty(2304, device=ins[0].device, dtype=torch.float32)
    _t54 = torch.empty(1152, device=ins[0].device, dtype=torch.float32)
    _t55 = torch.empty(1152, device=ins[0].device, dtype=torch.float32)
    _t56 = torch.empty(2304, device=ins[0].device, dtype=torch.float32)
    _t57 = torch.empty(2304, device=ins[0].device, dtype=torch.float32)
    _t58 = torch.empty(576, device=ins[0].device, dtype=torch.float32)
    _t59 = torch.empty(2304, device=ins[0].device, dtype=torch.float32)
    _t60 = torch.empty(576, device=ins[0].device, dtype=torch.float32)
    _t61 = torch.empty(288, device=ins[0].device, dtype=torch.float32)
    _t62 = torch.empty(288, device=ins[0].device, dtype=torch.float32)
    _t63 = torch.empty(576, device=ins[0].device, dtype=torch.float32)
    _t64 = torch.empty(3456, device=ins[0].device, dtype=torch.float32)
    _t65 = torch.empty(1728, device=ins[0].device, dtype=torch.float32)
    _t66 = torch.empty(1728, device=ins[0].device, dtype=torch.float32)
    _t67 = torch.empty(3456, device=ins[0].device, dtype=torch.float32)
    _t68 = torch.empty(3456, device=ins[0].device, dtype=torch.float32)
    _t69 = torch.empty(1728, device=ins[0].device, dtype=torch.float32)
    _t70 = torch.empty(1728, device=ins[0].device, dtype=torch.float32)
    _t71 = torch.empty(3456, device=ins[0].device, dtype=torch.float32)
    _t72 = torch.empty(3456, device=ins[0].device, dtype=torch.float32)
    _t73 = torch.empty(864, device=ins[0].device, dtype=torch.float32)
    _t74 = torch.empty(3456, device=ins[0].device, dtype=torch.float32)
    _t75 = torch.empty(768, device=ins[0].device, dtype=torch.float32)
    _t76 = torch.empty(384, device=ins[0].device, dtype=torch.float32)
    _t77 = torch.empty(384, device=ins[0].device, dtype=torch.float32)
    _t78 = torch.empty(768, device=ins[0].device, dtype=torch.float32)
    _t79 = torch.empty(2816, device=ins[0].device, dtype=torch.float32)
    _t80 = torch.empty(1408, device=ins[0].device, dtype=torch.float32)
    _t81 = torch.empty(1408, device=ins[0].device, dtype=torch.float32)
    _t82 = torch.empty(2816, device=ins[0].device, dtype=torch.float32)
    _t83 = torch.empty(2816, device=ins[0].device, dtype=torch.float32)
    t024_s0(_t0, list(ins))
    t024_s1(_t1, list(ins) + [_t0])
    t024_s2(_t2, list(ins) + [_t0, _t1])
    t024_s3(_t3, list(ins) + [_t0, _t1, _t2])
    t024_s4(_t4, list(ins) + [_t0, _t1, _t2, _t3])
    t024_s5(_t5, list(ins) + [_t0, _t1, _t2, _t3, _t4])
    t024_s6(_t6, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5])
    t024_s7(_t7, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6])
    t024_s8(_t8, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7])
    t024_s9(_t9, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8])
    t024_s10(_t10, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9])
    t024_s11(_t11, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10])
    t024_s12(_t12, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11])
    t024_s13(_t13, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12])
    t024_s14(_t14, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13])
    t024_s15(_t15, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13, _t14])
    t024_s16(_t16, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13, _t14, _t15])
    t024_s17(_t17, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13, _t14, _t15, _t16])
    t024_s18(_t18, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13, _t14, _t15, _t16, _t17])
    t024_s19(_t19, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13, _t14, _t15, _t16, _t17, _t18])
    t024_s20(_t20, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13, _t14, _t15, _t16, _t17, _t18, _t19])
    t024_s21(_t21, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13, _t14, _t15, _t16, _t17, _t18, _t19, _t20])
    t024_s22(_t22, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13, _t14, _t15, _t16, _t17, _t18, _t19, _t20, _t21])
    t024_s23(_t23, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13, _t14, _t15, _t16, _t17, _t18, _t19, _t20, _t21, _t22])
    t024_s24(_t24, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13, _t14, _t15, _t16, _t17, _t18, _t19, _t20, _t21, _t22, _t23])
    t024_s25(_t25, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13, _t14, _t15, _t16, _t17, _t18, _t19, _t20, _t21, _t22, _t23, _t24])
    t024_s26(_t26, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13, _t14, _t15, _t16, _t17, _t18, _t19, _t20, _t21, _t22, _t23, _t24, _t25])
    t024_s27(_t27, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13, _t14, _t15, _t16, _t17, _t18, _t19, _t20, _t21, _t22, _t23, _t24, _t25, _t26])
    t024_s28(_t28, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13, _t14, _t15, _t16, _t17, _t18, _t19, _t20, _t21, _t22, _t23, _t24, _t25, _t26, _t27])
    t024_s29(_t29, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13, _t14, _t15, _t16, _t17, _t18, _t19, _t20, _t21, _t22, _t23, _t24, _t25, _t26, _t27, _t28])
    t024_s30(_t30, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13, _t14, _t15, _t16, _t17, _t18, _t19, _t20, _t21, _t22, _t23, _t24, _t25, _t26, _t27, _t28, _t29])
    t024_s31(_t31, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13, _t14, _t15, _t16, _t17, _t18, _t19, _t20, _t21, _t22, _t23, _t24, _t25, _t26, _t27, _t28, _t29, _t30])
    t024_s32(_t32, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13, _t14, _t15, _t16, _t17, _t18, _t19, _t20, _t21, _t22, _t23, _t24, _t25, _t26, _t27, _t28, _t29, _t30, _t31])
    t024_s33(_t33, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13, _t14, _t15, _t16, _t17, _t18, _t19, _t20, _t21, _t22, _t23, _t24, _t25, _t26, _t27, _t28, _t29, _t30, _t31, _t32])
    t024_s34(_t34, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13, _t14, _t15, _t16, _t17, _t18, _t19, _t20, _t21, _t22, _t23, _t24, _t25, _t26, _t27, _t28, _t29, _t30, _t31, _t32, _t33])
    t024_s35(_t35, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13, _t14, _t15, _t16, _t17, _t18, _t19, _t20, _t21, _t22, _t23, _t24, _t25, _t26, _t27, _t28, _t29, _t30, _t31, _t32, _t33, _t34])
    t024_s36(_t36, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13, _t14, _t15, _t16, _t17, _t18, _t19, _t20, _t21, _t22, _t23, _t24, _t25, _t26, _t27, _t28, _t29, _t30, _t31, _t32, _t33, _t34, _t35])
    t024_s37(_t37, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13, _t14, _t15, _t16, _t17, _t18, _t19, _t20, _t21, _t22, _t23, _t24, _t25, _t26, _t27, _t28, _t29, _t30, _t31, _t32, _t33, _t34, _t35, _t36])
    t024_s38(_t38, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13, _t14, _t15, _t16, _t17, _t18, _t19, _t20, _t21, _t22, _t23, _t24, _t25, _t26, _t27, _t28, _t29, _t30, _t31, _t32, _t33, _t34, _t35, _t36, _t37])
    t024_s39(_t39, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13, _t14, _t15, _t16, _t17, _t18, _t19, _t20, _t21, _t22, _t23, _t24, _t25, _t26, _t27, _t28, _t29, _t30, _t31, _t32, _t33, _t34, _t35, _t36, _t37, _t38])
    t024_s40(_t40, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13, _t14, _t15, _t16, _t17, _t18, _t19, _t20, _t21, _t22, _t23, _t24, _t25, _t26, _t27, _t28, _t29, _t30, _t31, _t32, _t33, _t34, _t35, _t36, _t37, _t38, _t39])
    t024_s41(_t41, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13, _t14, _t15, _t16, _t17, _t18, _t19, _t20, _t21, _t22, _t23, _t24, _t25, _t26, _t27, _t28, _t29, _t30, _t31, _t32, _t33, _t34, _t35, _t36, _t37, _t38, _t39, _t40])
    t024_s42(_t42, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13, _t14, _t15, _t16, _t17, _t18, _t19, _t20, _t21, _t22, _t23, _t24, _t25, _t26, _t27, _t28, _t29, _t30, _t31, _t32, _t33, _t34, _t35, _t36, _t37, _t38, _t39, _t40, _t41])
    t024_s43(_t43, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13, _t14, _t15, _t16, _t17, _t18, _t19, _t20, _t21, _t22, _t23, _t24, _t25, _t26, _t27, _t28, _t29, _t30, _t31, _t32, _t33, _t34, _t35, _t36, _t37, _t38, _t39, _t40, _t41, _t42])
    t024_s44(_t44, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13, _t14, _t15, _t16, _t17, _t18, _t19, _t20, _t21, _t22, _t23, _t24, _t25, _t26, _t27, _t28, _t29, _t30, _t31, _t32, _t33, _t34, _t35, _t36, _t37, _t38, _t39, _t40, _t41, _t42, _t43])
    t024_s45(_t45, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13, _t14, _t15, _t16, _t17, _t18, _t19, _t20, _t21, _t22, _t23, _t24, _t25, _t26, _t27, _t28, _t29, _t30, _t31, _t32, _t33, _t34, _t35, _t36, _t37, _t38, _t39, _t40, _t41, _t42, _t43, _t44])
    t024_s46(_t46, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13, _t14, _t15, _t16, _t17, _t18, _t19, _t20, _t21, _t22, _t23, _t24, _t25, _t26, _t27, _t28, _t29, _t30, _t31, _t32, _t33, _t34, _t35, _t36, _t37, _t38, _t39, _t40, _t41, _t42, _t43, _t44, _t45])
    t024_s47(_t47, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13, _t14, _t15, _t16, _t17, _t18, _t19, _t20, _t21, _t22, _t23, _t24, _t25, _t26, _t27, _t28, _t29, _t30, _t31, _t32, _t33, _t34, _t35, _t36, _t37, _t38, _t39, _t40, _t41, _t42, _t43, _t44, _t45, _t46])
    t024_s48(_t48, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13, _t14, _t15, _t16, _t17, _t18, _t19, _t20, _t21, _t22, _t23, _t24, _t25, _t26, _t27, _t28, _t29, _t30, _t31, _t32, _t33, _t34, _t35, _t36, _t37, _t38, _t39, _t40, _t41, _t42, _t43, _t44, _t45, _t46, _t47])
    t024_s49(_t49, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13, _t14, _t15, _t16, _t17, _t18, _t19, _t20, _t21, _t22, _t23, _t24, _t25, _t26, _t27, _t28, _t29, _t30, _t31, _t32, _t33, _t34, _t35, _t36, _t37, _t38, _t39, _t40, _t41, _t42, _t43, _t44, _t45, _t46, _t47, _t48])
    t024_s50(_t50, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13, _t14, _t15, _t16, _t17, _t18, _t19, _t20, _t21, _t22, _t23, _t24, _t25, _t26, _t27, _t28, _t29, _t30, _t31, _t32, _t33, _t34, _t35, _t36, _t37, _t38, _t39, _t40, _t41, _t42, _t43, _t44, _t45, _t46, _t47, _t48, _t49])
    t024_s51(_t51, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13, _t14, _t15, _t16, _t17, _t18, _t19, _t20, _t21, _t22, _t23, _t24, _t25, _t26, _t27, _t28, _t29, _t30, _t31, _t32, _t33, _t34, _t35, _t36, _t37, _t38, _t39, _t40, _t41, _t42, _t43, _t44, _t45, _t46, _t47, _t48, _t49, _t50])
    t024_s52(_t52, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13, _t14, _t15, _t16, _t17, _t18, _t19, _t20, _t21, _t22, _t23, _t24, _t25, _t26, _t27, _t28, _t29, _t30, _t31, _t32, _t33, _t34, _t35, _t36, _t37, _t38, _t39, _t40, _t41, _t42, _t43, _t44, _t45, _t46, _t47, _t48, _t49, _t50, _t51])
    t024_s53(_t53, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13, _t14, _t15, _t16, _t17, _t18, _t19, _t20, _t21, _t22, _t23, _t24, _t25, _t26, _t27, _t28, _t29, _t30, _t31, _t32, _t33, _t34, _t35, _t36, _t37, _t38, _t39, _t40, _t41, _t42, _t43, _t44, _t45, _t46, _t47, _t48, _t49, _t50, _t51, _t52])
    t024_s54(_t54, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13, _t14, _t15, _t16, _t17, _t18, _t19, _t20, _t21, _t22, _t23, _t24, _t25, _t26, _t27, _t28, _t29, _t30, _t31, _t32, _t33, _t34, _t35, _t36, _t37, _t38, _t39, _t40, _t41, _t42, _t43, _t44, _t45, _t46, _t47, _t48, _t49, _t50, _t51, _t52, _t53])
    t024_s55(_t55, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13, _t14, _t15, _t16, _t17, _t18, _t19, _t20, _t21, _t22, _t23, _t24, _t25, _t26, _t27, _t28, _t29, _t30, _t31, _t32, _t33, _t34, _t35, _t36, _t37, _t38, _t39, _t40, _t41, _t42, _t43, _t44, _t45, _t46, _t47, _t48, _t49, _t50, _t51, _t52, _t53, _t54])
    t024_s56(_t56, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13, _t14, _t15, _t16, _t17, _t18, _t19, _t20, _t21, _t22, _t23, _t24, _t25, _t26, _t27, _t28, _t29, _t30, _t31, _t32, _t33, _t34, _t35, _t36, _t37, _t38, _t39, _t40, _t41, _t42, _t43, _t44, _t45, _t46, _t47, _t48, _t49, _t50, _t51, _t52, _t53, _t54, _t55])
    t024_s57(_t57, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13, _t14, _t15, _t16, _t17, _t18, _t19, _t20, _t21, _t22, _t23, _t24, _t25, _t26, _t27, _t28, _t29, _t30, _t31, _t32, _t33, _t34, _t35, _t36, _t37, _t38, _t39, _t40, _t41, _t42, _t43, _t44, _t45, _t46, _t47, _t48, _t49, _t50, _t51, _t52, _t53, _t54, _t55, _t56])
    t024_s58(_t58, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13, _t14, _t15, _t16, _t17, _t18, _t19, _t20, _t21, _t22, _t23, _t24, _t25, _t26, _t27, _t28, _t29, _t30, _t31, _t32, _t33, _t34, _t35, _t36, _t37, _t38, _t39, _t40, _t41, _t42, _t43, _t44, _t45, _t46, _t47, _t48, _t49, _t50, _t51, _t52, _t53, _t54, _t55, _t56, _t57])
    t024_s59(_t59, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13, _t14, _t15, _t16, _t17, _t18, _t19, _t20, _t21, _t22, _t23, _t24, _t25, _t26, _t27, _t28, _t29, _t30, _t31, _t32, _t33, _t34, _t35, _t36, _t37, _t38, _t39, _t40, _t41, _t42, _t43, _t44, _t45, _t46, _t47, _t48, _t49, _t50, _t51, _t52, _t53, _t54, _t55, _t56, _t57, _t58])
    t024_s60(_t60, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13, _t14, _t15, _t16, _t17, _t18, _t19, _t20, _t21, _t22, _t23, _t24, _t25, _t26, _t27, _t28, _t29, _t30, _t31, _t32, _t33, _t34, _t35, _t36, _t37, _t38, _t39, _t40, _t41, _t42, _t43, _t44, _t45, _t46, _t47, _t48, _t49, _t50, _t51, _t52, _t53, _t54, _t55, _t56, _t57, _t58, _t59])
    t024_s61(_t61, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13, _t14, _t15, _t16, _t17, _t18, _t19, _t20, _t21, _t22, _t23, _t24, _t25, _t26, _t27, _t28, _t29, _t30, _t31, _t32, _t33, _t34, _t35, _t36, _t37, _t38, _t39, _t40, _t41, _t42, _t43, _t44, _t45, _t46, _t47, _t48, _t49, _t50, _t51, _t52, _t53, _t54, _t55, _t56, _t57, _t58, _t59, _t60])
    t024_s62(_t62, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13, _t14, _t15, _t16, _t17, _t18, _t19, _t20, _t21, _t22, _t23, _t24, _t25, _t26, _t27, _t28, _t29, _t30, _t31, _t32, _t33, _t34, _t35, _t36, _t37, _t38, _t39, _t40, _t41, _t42, _t43, _t44, _t45, _t46, _t47, _t48, _t49, _t50, _t51, _t52, _t53, _t54, _t55, _t56, _t57, _t58, _t59, _t60, _t61])
    t024_s63(_t63, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13, _t14, _t15, _t16, _t17, _t18, _t19, _t20, _t21, _t22, _t23, _t24, _t25, _t26, _t27, _t28, _t29, _t30, _t31, _t32, _t33, _t34, _t35, _t36, _t37, _t38, _t39, _t40, _t41, _t42, _t43, _t44, _t45, _t46, _t47, _t48, _t49, _t50, _t51, _t52, _t53, _t54, _t55, _t56, _t57, _t58, _t59, _t60, _t61, _t62])
    t024_s64(_t64, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13, _t14, _t15, _t16, _t17, _t18, _t19, _t20, _t21, _t22, _t23, _t24, _t25, _t26, _t27, _t28, _t29, _t30, _t31, _t32, _t33, _t34, _t35, _t36, _t37, _t38, _t39, _t40, _t41, _t42, _t43, _t44, _t45, _t46, _t47, _t48, _t49, _t50, _t51, _t52, _t53, _t54, _t55, _t56, _t57, _t58, _t59, _t60, _t61, _t62, _t63])
    t024_s65(_t65, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13, _t14, _t15, _t16, _t17, _t18, _t19, _t20, _t21, _t22, _t23, _t24, _t25, _t26, _t27, _t28, _t29, _t30, _t31, _t32, _t33, _t34, _t35, _t36, _t37, _t38, _t39, _t40, _t41, _t42, _t43, _t44, _t45, _t46, _t47, _t48, _t49, _t50, _t51, _t52, _t53, _t54, _t55, _t56, _t57, _t58, _t59, _t60, _t61, _t62, _t63, _t64])
    t024_s66(_t66, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13, _t14, _t15, _t16, _t17, _t18, _t19, _t20, _t21, _t22, _t23, _t24, _t25, _t26, _t27, _t28, _t29, _t30, _t31, _t32, _t33, _t34, _t35, _t36, _t37, _t38, _t39, _t40, _t41, _t42, _t43, _t44, _t45, _t46, _t47, _t48, _t49, _t50, _t51, _t52, _t53, _t54, _t55, _t56, _t57, _t58, _t59, _t60, _t61, _t62, _t63, _t64, _t65])
    t024_s67(_t67, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13, _t14, _t15, _t16, _t17, _t18, _t19, _t20, _t21, _t22, _t23, _t24, _t25, _t26, _t27, _t28, _t29, _t30, _t31, _t32, _t33, _t34, _t35, _t36, _t37, _t38, _t39, _t40, _t41, _t42, _t43, _t44, _t45, _t46, _t47, _t48, _t49, _t50, _t51, _t52, _t53, _t54, _t55, _t56, _t57, _t58, _t59, _t60, _t61, _t62, _t63, _t64, _t65, _t66])
    t024_s68(_t68, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13, _t14, _t15, _t16, _t17, _t18, _t19, _t20, _t21, _t22, _t23, _t24, _t25, _t26, _t27, _t28, _t29, _t30, _t31, _t32, _t33, _t34, _t35, _t36, _t37, _t38, _t39, _t40, _t41, _t42, _t43, _t44, _t45, _t46, _t47, _t48, _t49, _t50, _t51, _t52, _t53, _t54, _t55, _t56, _t57, _t58, _t59, _t60, _t61, _t62, _t63, _t64, _t65, _t66, _t67])
    t024_s69(_t69, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13, _t14, _t15, _t16, _t17, _t18, _t19, _t20, _t21, _t22, _t23, _t24, _t25, _t26, _t27, _t28, _t29, _t30, _t31, _t32, _t33, _t34, _t35, _t36, _t37, _t38, _t39, _t40, _t41, _t42, _t43, _t44, _t45, _t46, _t47, _t48, _t49, _t50, _t51, _t52, _t53, _t54, _t55, _t56, _t57, _t58, _t59, _t60, _t61, _t62, _t63, _t64, _t65, _t66, _t67, _t68])
    t024_s70(_t70, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13, _t14, _t15, _t16, _t17, _t18, _t19, _t20, _t21, _t22, _t23, _t24, _t25, _t26, _t27, _t28, _t29, _t30, _t31, _t32, _t33, _t34, _t35, _t36, _t37, _t38, _t39, _t40, _t41, _t42, _t43, _t44, _t45, _t46, _t47, _t48, _t49, _t50, _t51, _t52, _t53, _t54, _t55, _t56, _t57, _t58, _t59, _t60, _t61, _t62, _t63, _t64, _t65, _t66, _t67, _t68, _t69])
    t024_s71(_t71, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13, _t14, _t15, _t16, _t17, _t18, _t19, _t20, _t21, _t22, _t23, _t24, _t25, _t26, _t27, _t28, _t29, _t30, _t31, _t32, _t33, _t34, _t35, _t36, _t37, _t38, _t39, _t40, _t41, _t42, _t43, _t44, _t45, _t46, _t47, _t48, _t49, _t50, _t51, _t52, _t53, _t54, _t55, _t56, _t57, _t58, _t59, _t60, _t61, _t62, _t63, _t64, _t65, _t66, _t67, _t68, _t69, _t70])
    t024_s72(_t72, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13, _t14, _t15, _t16, _t17, _t18, _t19, _t20, _t21, _t22, _t23, _t24, _t25, _t26, _t27, _t28, _t29, _t30, _t31, _t32, _t33, _t34, _t35, _t36, _t37, _t38, _t39, _t40, _t41, _t42, _t43, _t44, _t45, _t46, _t47, _t48, _t49, _t50, _t51, _t52, _t53, _t54, _t55, _t56, _t57, _t58, _t59, _t60, _t61, _t62, _t63, _t64, _t65, _t66, _t67, _t68, _t69, _t70, _t71])
    t024_s73(_t73, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13, _t14, _t15, _t16, _t17, _t18, _t19, _t20, _t21, _t22, _t23, _t24, _t25, _t26, _t27, _t28, _t29, _t30, _t31, _t32, _t33, _t34, _t35, _t36, _t37, _t38, _t39, _t40, _t41, _t42, _t43, _t44, _t45, _t46, _t47, _t48, _t49, _t50, _t51, _t52, _t53, _t54, _t55, _t56, _t57, _t58, _t59, _t60, _t61, _t62, _t63, _t64, _t65, _t66, _t67, _t68, _t69, _t70, _t71, _t72])
    t024_s74(_t74, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13, _t14, _t15, _t16, _t17, _t18, _t19, _t20, _t21, _t22, _t23, _t24, _t25, _t26, _t27, _t28, _t29, _t30, _t31, _t32, _t33, _t34, _t35, _t36, _t37, _t38, _t39, _t40, _t41, _t42, _t43, _t44, _t45, _t46, _t47, _t48, _t49, _t50, _t51, _t52, _t53, _t54, _t55, _t56, _t57, _t58, _t59, _t60, _t61, _t62, _t63, _t64, _t65, _t66, _t67, _t68, _t69, _t70, _t71, _t72, _t73])
    t024_s75(_t75, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13, _t14, _t15, _t16, _t17, _t18, _t19, _t20, _t21, _t22, _t23, _t24, _t25, _t26, _t27, _t28, _t29, _t30, _t31, _t32, _t33, _t34, _t35, _t36, _t37, _t38, _t39, _t40, _t41, _t42, _t43, _t44, _t45, _t46, _t47, _t48, _t49, _t50, _t51, _t52, _t53, _t54, _t55, _t56, _t57, _t58, _t59, _t60, _t61, _t62, _t63, _t64, _t65, _t66, _t67, _t68, _t69, _t70, _t71, _t72, _t73, _t74])
    t024_s76(_t76, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13, _t14, _t15, _t16, _t17, _t18, _t19, _t20, _t21, _t22, _t23, _t24, _t25, _t26, _t27, _t28, _t29, _t30, _t31, _t32, _t33, _t34, _t35, _t36, _t37, _t38, _t39, _t40, _t41, _t42, _t43, _t44, _t45, _t46, _t47, _t48, _t49, _t50, _t51, _t52, _t53, _t54, _t55, _t56, _t57, _t58, _t59, _t60, _t61, _t62, _t63, _t64, _t65, _t66, _t67, _t68, _t69, _t70, _t71, _t72, _t73, _t74, _t75])
    t024_s77(_t77, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13, _t14, _t15, _t16, _t17, _t18, _t19, _t20, _t21, _t22, _t23, _t24, _t25, _t26, _t27, _t28, _t29, _t30, _t31, _t32, _t33, _t34, _t35, _t36, _t37, _t38, _t39, _t40, _t41, _t42, _t43, _t44, _t45, _t46, _t47, _t48, _t49, _t50, _t51, _t52, _t53, _t54, _t55, _t56, _t57, _t58, _t59, _t60, _t61, _t62, _t63, _t64, _t65, _t66, _t67, _t68, _t69, _t70, _t71, _t72, _t73, _t74, _t75, _t76])
    t024_s78(_t78, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13, _t14, _t15, _t16, _t17, _t18, _t19, _t20, _t21, _t22, _t23, _t24, _t25, _t26, _t27, _t28, _t29, _t30, _t31, _t32, _t33, _t34, _t35, _t36, _t37, _t38, _t39, _t40, _t41, _t42, _t43, _t44, _t45, _t46, _t47, _t48, _t49, _t50, _t51, _t52, _t53, _t54, _t55, _t56, _t57, _t58, _t59, _t60, _t61, _t62, _t63, _t64, _t65, _t66, _t67, _t68, _t69, _t70, _t71, _t72, _t73, _t74, _t75, _t76, _t77])
    t024_s79(_t79, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13, _t14, _t15, _t16, _t17, _t18, _t19, _t20, _t21, _t22, _t23, _t24, _t25, _t26, _t27, _t28, _t29, _t30, _t31, _t32, _t33, _t34, _t35, _t36, _t37, _t38, _t39, _t40, _t41, _t42, _t43, _t44, _t45, _t46, _t47, _t48, _t49, _t50, _t51, _t52, _t53, _t54, _t55, _t56, _t57, _t58, _t59, _t60, _t61, _t62, _t63, _t64, _t65, _t66, _t67, _t68, _t69, _t70, _t71, _t72, _t73, _t74, _t75, _t76, _t77, _t78])
    t024_s80(_t80, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13, _t14, _t15, _t16, _t17, _t18, _t19, _t20, _t21, _t22, _t23, _t24, _t25, _t26, _t27, _t28, _t29, _t30, _t31, _t32, _t33, _t34, _t35, _t36, _t37, _t38, _t39, _t40, _t41, _t42, _t43, _t44, _t45, _t46, _t47, _t48, _t49, _t50, _t51, _t52, _t53, _t54, _t55, _t56, _t57, _t58, _t59, _t60, _t61, _t62, _t63, _t64, _t65, _t66, _t67, _t68, _t69, _t70, _t71, _t72, _t73, _t74, _t75, _t76, _t77, _t78, _t79])
    t024_s81(_t81, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13, _t14, _t15, _t16, _t17, _t18, _t19, _t20, _t21, _t22, _t23, _t24, _t25, _t26, _t27, _t28, _t29, _t30, _t31, _t32, _t33, _t34, _t35, _t36, _t37, _t38, _t39, _t40, _t41, _t42, _t43, _t44, _t45, _t46, _t47, _t48, _t49, _t50, _t51, _t52, _t53, _t54, _t55, _t56, _t57, _t58, _t59, _t60, _t61, _t62, _t63, _t64, _t65, _t66, _t67, _t68, _t69, _t70, _t71, _t72, _t73, _t74, _t75, _t76, _t77, _t78, _t79, _t80])
    t024_s82(_t82, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13, _t14, _t15, _t16, _t17, _t18, _t19, _t20, _t21, _t22, _t23, _t24, _t25, _t26, _t27, _t28, _t29, _t30, _t31, _t32, _t33, _t34, _t35, _t36, _t37, _t38, _t39, _t40, _t41, _t42, _t43, _t44, _t45, _t46, _t47, _t48, _t49, _t50, _t51, _t52, _t53, _t54, _t55, _t56, _t57, _t58, _t59, _t60, _t61, _t62, _t63, _t64, _t65, _t66, _t67, _t68, _t69, _t70, _t71, _t72, _t73, _t74, _t75, _t76, _t77, _t78, _t79, _t80, _t81])
    t024_s83(_t83, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13, _t14, _t15, _t16, _t17, _t18, _t19, _t20, _t21, _t22, _t23, _t24, _t25, _t26, _t27, _t28, _t29, _t30, _t31, _t32, _t33, _t34, _t35, _t36, _t37, _t38, _t39, _t40, _t41, _t42, _t43, _t44, _t45, _t46, _t47, _t48, _t49, _t50, _t51, _t52, _t53, _t54, _t55, _t56, _t57, _t58, _t59, _t60, _t61, _t62, _t63, _t64, _t65, _t66, _t67, _t68, _t69, _t70, _t71, _t72, _t73, _t74, _t75, _t76, _t77, _t78, _t79, _t80, _t81, _t82])
    t024_s84(out, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13, _t14, _t15, _t16, _t17, _t18, _t19, _t20, _t21, _t22, _t23, _t24, _t25, _t26, _t27, _t28, _t29, _t30, _t31, _t32, _t33, _t34, _t35, _t36, _t37, _t38, _t39, _t40, _t41, _t42, _t43, _t44, _t45, _t46, _t47, _t48, _t49, _t50, _t51, _t52, _t53, _t54, _t55, _t56, _t57, _t58, _t59, _t60, _t61, _t62, _t63, _t64, _t65, _t66, _t67, _t68, _t69, _t70, _t71, _t72, _t73, _t74, _t75, _t76, _t77, _t78, _t79, _t80, _t81, _t82, _t83])
    return out
