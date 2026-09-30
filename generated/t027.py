import torch
import triton
import triton.language as tl


@triton.jit
def _mul_combine(a, b):
    return a * b


@triton.jit
def t027_s0_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr):
    _acc0 = tl.zeros([16], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 16) + tl.arange(0, 16)) < 27) & ((((1 <= (((tl.program_id(0) // 224) % 224) + ((((_lv0 * 16) + tl.arange(0, 16)) // 3) % 3))) & ((((tl.program_id(0) // 224) % 224) + ((((_lv0 * 16) + tl.arange(0, 16)) // 3) % 3)) < 225)) & (1 <= ((tl.program_id(0) % 224) + (((_lv0 * 16) + tl.arange(0, 16)) % 3)))) & (((tl.program_id(0) % 224) + (((_lv0 * 16) + tl.arange(0, 16)) % 3)) < 225))), (tl.load(in0_ptr + ((((((((tl.program_id(0) // 3211264) * 3) + (((_lv0 * 16) + tl.arange(0, 16)) // 9)) * 224) + tl.maximum((((tl.program_id(0) // 224) % 224) + ((((_lv0 * 16) + tl.arange(0, 16)) // 3) % 3)) - 1, 0)) * 224) + tl.maximum(((tl.program_id(0) % 224) + (((_lv0 * 16) + tl.arange(0, 16)) % 3)) - 1, 0)) + 0 * tl.arange(0, 16)), mask=((((_lv0 * 16) + tl.arange(0, 16)) < 27) & ((((1 <= (((tl.program_id(0) // 224) % 224) + ((((_lv0 * 16) + tl.arange(0, 16)) // 3) % 3))) & ((((tl.program_id(0) // 224) % 224) + ((((_lv0 * 16) + tl.arange(0, 16)) // 3) % 3)) < 225)) & (1 <= ((tl.program_id(0) % 224) + (((_lv0 * 16) + tl.arange(0, 16)) % 3)))) & (((tl.program_id(0) % 224) + (((_lv0 * 16) + tl.arange(0, 16)) % 3)) < 225))), other=0.0) * tl.load(in1_ptr + (((((((((tl.program_id(0) // 50176) % 64) * 3) + (((_lv0 * 16) + tl.arange(0, 16)) // 9)) * 3) + ((((_lv0 * 16) + tl.arange(0, 16)) // 3) % 3)) * 3) + (((_lv0 * 16) + tl.arange(0, 16)) % 3)) + 0 * tl.arange(0, 16)), mask=((((_lv0 * 16) + tl.arange(0, 16)) < 27) & ((((1 <= (((tl.program_id(0) // 224) % 224) + ((((_lv0 * 16) + tl.arange(0, 16)) // 3) % 3))) & ((((tl.program_id(0) // 224) % 224) + ((((_lv0 * 16) + tl.arange(0, 16)) // 3) % 3)) < 225)) & (1 <= ((tl.program_id(0) % 224) + (((_lv0 * 16) + tl.arange(0, 16)) % 3)))) & (((tl.program_id(0) % 224) + (((_lv0 * 16) + tl.arange(0, 16)) % 3)) < 225))), other=0.0)), 0.0))
    _v = (tl.sum(_acc0, axis=0) + tl.load(in2_ptr + (((tl.program_id(0) // 50176) % 64))))
    tl.store(out_ptr + tl.program_id(0), _v)


def t027_s0(out, ins):
    grid = (25690112,)
    t027_s0_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26])
    return out


@triton.jit
def t027_s1_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 1568) & ((((tl.program_id(0) % 256) * 1568) + ((_lv0 * 1024) + tl.arange(0, 1024))) < 401408)), tl.load(in27_ptr + (tl.maximum(((((((((tl.program_id(0) % 256) * 1568) + ((_lv0 * 1024) + tl.arange(0, 1024))) // 50176) * 64) + (tl.program_id(0) // 256)) * 50176) + ((((tl.program_id(0) % 256) * 1568) + ((_lv0 * 1024) + tl.arange(0, 1024))) % 50176)) - tl.maximum(((((((((tl.program_id(0) % 256) * 1568) + ((_lv0 * 1024) + tl.arange(0, 1024))) // 50176) * 64) + (tl.program_id(0) // 256)) * 50176) + ((((tl.program_id(0) % 256) * 1568) + ((_lv0 * 1024) + tl.arange(0, 1024))) % 50176)) - 25690111, 0), 0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 1568) & ((((tl.program_id(0) % 256) * 1568) + ((_lv0 * 1024) + tl.arange(0, 1024))) < 401408)), other=0.0), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t027_s1(out, ins):
    grid = (16384,)
    t027_s1_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27])
    return out


@triton.jit
def t027_s2_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr):
    _acc0 = tl.zeros([256], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 256) + tl.arange(0, 256)) < 256) & True), tl.load(in28_ptr + (((tl.program_id(0) * 256) + ((_lv0 * 256) + tl.arange(0, 256))) + 0 * tl.arange(0, 256)), mask=((((_lv0 * 256) + tl.arange(0, 256)) < 256) & True), other=0.0), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t027_s2(out, ins):
    grid = (64,)
    t027_s2_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28])
    return out


@triton.jit
def t027_s3_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 1568) & ((((tl.program_id(0) % 256) * 1568) + ((_lv0 * 1024) + tl.arange(0, 1024))) < 401408)), ((tl.load(in27_ptr + (tl.maximum(((((((((tl.program_id(0) % 256) * 1568) + ((_lv0 * 1024) + tl.arange(0, 1024))) // 50176) * 64) + (tl.program_id(0) // 256)) * 50176) + ((((tl.program_id(0) % 256) * 1568) + ((_lv0 * 1024) + tl.arange(0, 1024))) % 50176)) - tl.maximum(((((((((tl.program_id(0) % 256) * 1568) + ((_lv0 * 1024) + tl.arange(0, 1024))) // 50176) * 64) + (tl.program_id(0) // 256)) * 50176) + ((((tl.program_id(0) % 256) * 1568) + ((_lv0 * 1024) + tl.arange(0, 1024))) % 50176)) - 25690111, 0), 0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 1568) & ((((tl.program_id(0) % 256) * 1568) + ((_lv0 * 1024) + tl.arange(0, 1024))) < 401408)), other=0.0) - (tl.load(in29_ptr + (tl.maximum((tl.program_id(0) // 256) - tl.maximum((tl.program_id(0) // 256) - 63, 0), 0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 1568) & ((((tl.program_id(0) % 256) * 1568) + ((_lv0 * 1024) + tl.arange(0, 1024))) < 401408)), other=0.0) * (1.0 * (1.0 / 401408.0)))) * (tl.load(in27_ptr + (tl.maximum(((((((((tl.program_id(0) % 256) * 1568) + ((_lv0 * 1024) + tl.arange(0, 1024))) // 50176) * 64) + (tl.program_id(0) // 256)) * 50176) + ((((tl.program_id(0) % 256) * 1568) + ((_lv0 * 1024) + tl.arange(0, 1024))) % 50176)) - tl.maximum(((((((((tl.program_id(0) % 256) * 1568) + ((_lv0 * 1024) + tl.arange(0, 1024))) // 50176) * 64) + (tl.program_id(0) // 256)) * 50176) + ((((tl.program_id(0) % 256) * 1568) + ((_lv0 * 1024) + tl.arange(0, 1024))) % 50176)) - 25690111, 0), 0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 1568) & ((((tl.program_id(0) % 256) * 1568) + ((_lv0 * 1024) + tl.arange(0, 1024))) < 401408)), other=0.0) - (tl.load(in29_ptr + (tl.maximum((tl.program_id(0) // 256) - tl.maximum((tl.program_id(0) // 256) - 63, 0), 0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 1568) & ((((tl.program_id(0) % 256) * 1568) + ((_lv0 * 1024) + tl.arange(0, 1024))) < 401408)), other=0.0) * (1.0 * (1.0 / 401408.0))))), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t027_s3(out, ins):
    grid = (16384,)
    t027_s3_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29])
    return out


@triton.jit
def t027_s4_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr):
    _acc0 = tl.zeros([256], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 256) + tl.arange(0, 256)) < 256) & True), tl.load(in30_ptr + (((tl.program_id(0) * 256) + ((_lv0 * 256) + tl.arange(0, 256))) + 0 * tl.arange(0, 256)), mask=((((_lv0 * 256) + tl.arange(0, 256)) < 256) & True), other=0.0), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t027_s4(out, ins):
    grid = (64,)
    t027_s4_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30])
    return out


@triton.jit
def t027_s5_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr):
    _acc0 = tl.zeros([1], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), ((((tl.load(in27_ptr + (tl.program_id(0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) - (tl.load(in29_ptr + (tl.maximum(((tl.program_id(0) // 50176) % 64) - tl.maximum(((tl.program_id(0) // 50176) % 64) - 63, 0), 0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) * (1.0 * (1.0 / 401408.0)))) * (1.0 / tl.sqrt(((tl.load(in31_ptr + (tl.maximum(((tl.program_id(0) // 50176) % 64) - tl.maximum(((tl.program_id(0) // 50176) % 64) - 63, 0), 0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) * (1.0 * (1.0 / 401408.0))) + (1.0 * (1.0 / 100000.0)))))) * tl.load(in3_ptr + (((tl.program_id(0) // 50176) % 64) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)) + tl.load(in4_ptr + (((tl.program_id(0) // 50176) % 64) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)), 0.0))
    _v = tl.maximum(tl.sum(_acc0, axis=0), (0.0 * (1.0 / 1.0)))
    tl.store(out_ptr + tl.program_id(0), _v)


def t027_s5(out, ins):
    grid = (25690112,)
    t027_s5_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31])
    return out


@triton.jit
def t027_s6_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr):
    _acc0 = tl.zeros([512], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 512) + tl.arange(0, 512)) < 576) & ((((1 <= (((tl.program_id(0) // 224) % 224) + ((((_lv0 * 512) + tl.arange(0, 512)) // 3) % 3))) & ((((tl.program_id(0) // 224) % 224) + ((((_lv0 * 512) + tl.arange(0, 512)) // 3) % 3)) < 225)) & (1 <= ((tl.program_id(0) % 224) + (((_lv0 * 512) + tl.arange(0, 512)) % 3)))) & (((tl.program_id(0) % 224) + (((_lv0 * 512) + tl.arange(0, 512)) % 3)) < 225))), (tl.load(in32_ptr + (tl.maximum((((((((tl.program_id(0) // 3211264) * 64) + (((_lv0 * 512) + tl.arange(0, 512)) // 9)) * 224) + tl.maximum((((tl.program_id(0) // 224) % 224) + ((((_lv0 * 512) + tl.arange(0, 512)) // 3) % 3)) - 1, 0)) * 224) + tl.maximum(((tl.program_id(0) % 224) + (((_lv0 * 512) + tl.arange(0, 512)) % 3)) - 1, 0)) - tl.maximum((((((((tl.program_id(0) // 3211264) * 64) + (((_lv0 * 512) + tl.arange(0, 512)) // 9)) * 224) + tl.maximum((((tl.program_id(0) // 224) % 224) + ((((_lv0 * 512) + tl.arange(0, 512)) // 3) % 3)) - 1, 0)) * 224) + tl.maximum(((tl.program_id(0) % 224) + (((_lv0 * 512) + tl.arange(0, 512)) % 3)) - 1, 0)) - 25690111, 0), 0) + 0 * tl.arange(0, 512)), mask=((((_lv0 * 512) + tl.arange(0, 512)) < 576) & ((((1 <= (((tl.program_id(0) // 224) % 224) + ((((_lv0 * 512) + tl.arange(0, 512)) // 3) % 3))) & ((((tl.program_id(0) // 224) % 224) + ((((_lv0 * 512) + tl.arange(0, 512)) // 3) % 3)) < 225)) & (1 <= ((tl.program_id(0) % 224) + (((_lv0 * 512) + tl.arange(0, 512)) % 3)))) & (((tl.program_id(0) % 224) + (((_lv0 * 512) + tl.arange(0, 512)) % 3)) < 225))), other=0.0) * tl.load(in5_ptr + (((((((((tl.program_id(0) // 50176) % 64) * 64) + (((_lv0 * 512) + tl.arange(0, 512)) // 9)) * 3) + ((((_lv0 * 512) + tl.arange(0, 512)) // 3) % 3)) * 3) + (((_lv0 * 512) + tl.arange(0, 512)) % 3)) + 0 * tl.arange(0, 512)), mask=((((_lv0 * 512) + tl.arange(0, 512)) < 576) & ((((1 <= (((tl.program_id(0) // 224) % 224) + ((((_lv0 * 512) + tl.arange(0, 512)) // 3) % 3))) & ((((tl.program_id(0) // 224) % 224) + ((((_lv0 * 512) + tl.arange(0, 512)) // 3) % 3)) < 225)) & (1 <= ((tl.program_id(0) % 224) + (((_lv0 * 512) + tl.arange(0, 512)) % 3)))) & (((tl.program_id(0) % 224) + (((_lv0 * 512) + tl.arange(0, 512)) % 3)) < 225))), other=0.0)), 0.0))
    _v = (tl.sum(_acc0, axis=0) + tl.load(in6_ptr + (((tl.program_id(0) // 50176) % 64))))
    tl.store(out_ptr + tl.program_id(0), _v)


def t027_s6(out, ins):
    grid = (25690112,)
    t027_s6_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32])
    return out


@triton.jit
def t027_s7_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 1568) & ((((tl.program_id(0) % 256) * 1568) + ((_lv0 * 1024) + tl.arange(0, 1024))) < 401408)), tl.load(in33_ptr + (tl.maximum(((((((((tl.program_id(0) % 256) * 1568) + ((_lv0 * 1024) + tl.arange(0, 1024))) // 50176) * 64) + (tl.program_id(0) // 256)) * 50176) + ((((tl.program_id(0) % 256) * 1568) + ((_lv0 * 1024) + tl.arange(0, 1024))) % 50176)) - tl.maximum(((((((((tl.program_id(0) % 256) * 1568) + ((_lv0 * 1024) + tl.arange(0, 1024))) // 50176) * 64) + (tl.program_id(0) // 256)) * 50176) + ((((tl.program_id(0) % 256) * 1568) + ((_lv0 * 1024) + tl.arange(0, 1024))) % 50176)) - 25690111, 0), 0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 1568) & ((((tl.program_id(0) % 256) * 1568) + ((_lv0 * 1024) + tl.arange(0, 1024))) < 401408)), other=0.0), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t027_s7(out, ins):
    grid = (16384,)
    t027_s7_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33])
    return out


@triton.jit
def t027_s8_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr):
    _acc0 = tl.zeros([256], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 256) + tl.arange(0, 256)) < 256) & True), tl.load(in34_ptr + (((tl.program_id(0) * 256) + ((_lv0 * 256) + tl.arange(0, 256))) + 0 * tl.arange(0, 256)), mask=((((_lv0 * 256) + tl.arange(0, 256)) < 256) & True), other=0.0), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t027_s8(out, ins):
    grid = (64,)
    t027_s8_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34])
    return out


@triton.jit
def t027_s9_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 1568) & ((((tl.program_id(0) % 256) * 1568) + ((_lv0 * 1024) + tl.arange(0, 1024))) < 401408)), ((tl.load(in33_ptr + (tl.maximum(((((((((tl.program_id(0) % 256) * 1568) + ((_lv0 * 1024) + tl.arange(0, 1024))) // 50176) * 64) + (tl.program_id(0) // 256)) * 50176) + ((((tl.program_id(0) % 256) * 1568) + ((_lv0 * 1024) + tl.arange(0, 1024))) % 50176)) - tl.maximum(((((((((tl.program_id(0) % 256) * 1568) + ((_lv0 * 1024) + tl.arange(0, 1024))) // 50176) * 64) + (tl.program_id(0) // 256)) * 50176) + ((((tl.program_id(0) % 256) * 1568) + ((_lv0 * 1024) + tl.arange(0, 1024))) % 50176)) - 25690111, 0), 0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 1568) & ((((tl.program_id(0) % 256) * 1568) + ((_lv0 * 1024) + tl.arange(0, 1024))) < 401408)), other=0.0) - (tl.load(in35_ptr + (tl.maximum((tl.program_id(0) // 256) - tl.maximum((tl.program_id(0) // 256) - 63, 0), 0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 1568) & ((((tl.program_id(0) % 256) * 1568) + ((_lv0 * 1024) + tl.arange(0, 1024))) < 401408)), other=0.0) * (1.0 * (1.0 / 401408.0)))) * (tl.load(in33_ptr + (tl.maximum(((((((((tl.program_id(0) % 256) * 1568) + ((_lv0 * 1024) + tl.arange(0, 1024))) // 50176) * 64) + (tl.program_id(0) // 256)) * 50176) + ((((tl.program_id(0) % 256) * 1568) + ((_lv0 * 1024) + tl.arange(0, 1024))) % 50176)) - tl.maximum(((((((((tl.program_id(0) % 256) * 1568) + ((_lv0 * 1024) + tl.arange(0, 1024))) // 50176) * 64) + (tl.program_id(0) // 256)) * 50176) + ((((tl.program_id(0) % 256) * 1568) + ((_lv0 * 1024) + tl.arange(0, 1024))) % 50176)) - 25690111, 0), 0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 1568) & ((((tl.program_id(0) % 256) * 1568) + ((_lv0 * 1024) + tl.arange(0, 1024))) < 401408)), other=0.0) - (tl.load(in35_ptr + (tl.maximum((tl.program_id(0) // 256) - tl.maximum((tl.program_id(0) // 256) - 63, 0), 0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 1568) & ((((tl.program_id(0) % 256) * 1568) + ((_lv0 * 1024) + tl.arange(0, 1024))) < 401408)), other=0.0) * (1.0 * (1.0 / 401408.0))))), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t027_s9(out, ins):
    grid = (16384,)
    t027_s9_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35])
    return out


@triton.jit
def t027_s10_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr):
    _acc0 = tl.zeros([256], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 256) + tl.arange(0, 256)) < 256) & True), tl.load(in36_ptr + (((tl.program_id(0) * 256) + ((_lv0 * 256) + tl.arange(0, 256))) + 0 * tl.arange(0, 256)), mask=((((_lv0 * 256) + tl.arange(0, 256)) < 256) & True), other=0.0), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t027_s10(out, ins):
    grid = (64,)
    t027_s10_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36])
    return out


@triton.jit
def t027_s11_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr):
    _acc0 = tl.zeros([1], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), ((((tl.load(in33_ptr + (tl.program_id(0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) - (tl.load(in35_ptr + (tl.maximum(((tl.program_id(0) // 50176) % 64) - tl.maximum(((tl.program_id(0) // 50176) % 64) - 63, 0), 0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) * (1.0 * (1.0 / 401408.0)))) * (1.0 / tl.sqrt(((tl.load(in37_ptr + (tl.maximum(((tl.program_id(0) // 50176) % 64) - tl.maximum(((tl.program_id(0) // 50176) % 64) - 63, 0), 0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) * (1.0 * (1.0 / 401408.0))) + (1.0 * (1.0 / 100000.0)))))) * tl.load(in7_ptr + (((tl.program_id(0) // 50176) % 64) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)) + tl.load(in8_ptr + (((tl.program_id(0) // 50176) % 64) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)), 0.0))
    _v = tl.maximum(tl.sum(_acc0, axis=0), (0.0 * (1.0 / 1.0)))
    tl.store(out_ptr + tl.program_id(0), _v)


def t027_s11(out, ins):
    grid = (25690112,)
    t027_s11_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37])
    return out


@triton.jit
def t027_s12_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr, in38_ptr):
    _acc0 = tl.zeros([4], dtype=tl.float32) + (tl.load(in38_ptr + ((((((((tl.program_id(0) // 802816) * 64) + ((tl.program_id(0) // 12544) % 64)) * 224) + tl.maximum(((((tl.program_id(0) // 112) % 112) * 2) + tl.maximum(((0 // 2) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 112) % 112) * 2), 0) - (0 // 2), 0)) - tl.maximum(((0 // 2) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 112) % 112) * 2), 0) - (0 // 2), 0)) - tl.maximum(223 - (((tl.program_id(0) // 112) % 112) * 2), 0), 0), 0)) - tl.maximum(((((tl.program_id(0) // 112) % 112) * 2) + tl.maximum(((0 // 2) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 112) % 112) * 2), 0) - (0 // 2), 0)) - tl.maximum(((0 // 2) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 112) % 112) * 2), 0) - (0 // 2), 0)) - tl.maximum(223 - (((tl.program_id(0) // 112) % 112) * 2), 0), 0), 0)) - 223, 0), 0)) * 224) + tl.maximum((((tl.program_id(0) % 112) * 2) + tl.maximum(((0 % 2) + tl.maximum(tl.maximum(0 - ((tl.program_id(0) % 112) * 2), 0) - (0 % 2), 0)) - tl.maximum(((0 % 2) + tl.maximum(tl.maximum(0 - ((tl.program_id(0) % 112) * 2), 0) - (0 % 2), 0)) - tl.maximum(223 - ((tl.program_id(0) % 112) * 2), 0), 0), 0)) - tl.maximum((((tl.program_id(0) % 112) * 2) + tl.maximum(((0 % 2) + tl.maximum(tl.maximum(0 - ((tl.program_id(0) % 112) * 2), 0) - (0 % 2), 0)) - tl.maximum(((0 % 2) + tl.maximum(tl.maximum(0 - ((tl.program_id(0) % 112) * 2), 0) - (0 % 2), 0)) - tl.maximum(223 - ((tl.program_id(0) % 112) * 2), 0), 0), 0)) - 223, 0), 0)))))
    for _lv0 in range(0, 1):
        _acc0 = tl.maximum(_acc0, tl.load(in38_ptr + ((((((((tl.program_id(0) // 802816) * 64) + ((tl.program_id(0) // 12544) % 64)) * 224) + tl.maximum(((((tl.program_id(0) // 112) % 112) * 2) + tl.maximum(((tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - 3, 0), 0) // 2) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 112) % 112) * 2), 0) - (tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - 3, 0), 0) // 2), 0)) - tl.maximum(((tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - 3, 0), 0) // 2) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 112) % 112) * 2), 0) - (tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - 3, 0), 0) // 2), 0)) - tl.maximum(223 - (((tl.program_id(0) // 112) % 112) * 2), 0), 0), 0)) - tl.maximum(((((tl.program_id(0) // 112) % 112) * 2) + tl.maximum(((tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - 3, 0), 0) // 2) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 112) % 112) * 2), 0) - (tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - 3, 0), 0) // 2), 0)) - tl.maximum(((tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - 3, 0), 0) // 2) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 112) % 112) * 2), 0) - (tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - 3, 0), 0) // 2), 0)) - tl.maximum(223 - (((tl.program_id(0) // 112) % 112) * 2), 0), 0), 0)) - 223, 0), 0)) * 224) + tl.maximum((((tl.program_id(0) % 112) * 2) + tl.maximum(((tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - 3, 0), 0) % 2) + tl.maximum(tl.maximum(0 - ((tl.program_id(0) % 112) * 2), 0) - (tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - 3, 0), 0) % 2), 0)) - tl.maximum(((tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - 3, 0), 0) % 2) + tl.maximum(tl.maximum(0 - ((tl.program_id(0) % 112) * 2), 0) - (tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - 3, 0), 0) % 2), 0)) - tl.maximum(223 - ((tl.program_id(0) % 112) * 2), 0), 0), 0)) - tl.maximum((((tl.program_id(0) % 112) * 2) + tl.maximum(((tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - 3, 0), 0) % 2) + tl.maximum(tl.maximum(0 - ((tl.program_id(0) % 112) * 2), 0) - (tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - 3, 0), 0) % 2), 0)) - tl.maximum(((tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - 3, 0), 0) % 2) + tl.maximum(tl.maximum(0 - ((tl.program_id(0) % 112) * 2), 0) - (tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - 3, 0), 0) % 2), 0)) - tl.maximum(223 - ((tl.program_id(0) % 112) * 2), 0), 0), 0)) - 223, 0), 0)))))
    _v = tl.max(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t027_s12(out, ins):
    grid = (6422528,)
    t027_s12_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37], ins[38])
    return out


@triton.jit
def t027_s13_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr, in38_ptr, in39_ptr):
    _acc0 = tl.zeros([512], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 512) + tl.arange(0, 512)) < 576) & ((((1 <= (((tl.program_id(0) // 112) % 112) + ((((_lv0 * 512) + tl.arange(0, 512)) // 3) % 3))) & ((((tl.program_id(0) // 112) % 112) + ((((_lv0 * 512) + tl.arange(0, 512)) // 3) % 3)) < 113)) & (1 <= ((tl.program_id(0) % 112) + (((_lv0 * 512) + tl.arange(0, 512)) % 3)))) & (((tl.program_id(0) % 112) + (((_lv0 * 512) + tl.arange(0, 512)) % 3)) < 113))), (tl.load(in39_ptr + (tl.maximum((((((((tl.program_id(0) // 1605632) * 64) + (((_lv0 * 512) + tl.arange(0, 512)) // 9)) * 112) + tl.maximum((((tl.program_id(0) // 112) % 112) + ((((_lv0 * 512) + tl.arange(0, 512)) // 3) % 3)) - 1, 0)) * 112) + tl.maximum(((tl.program_id(0) % 112) + (((_lv0 * 512) + tl.arange(0, 512)) % 3)) - 1, 0)) - tl.maximum((((((((tl.program_id(0) // 1605632) * 64) + (((_lv0 * 512) + tl.arange(0, 512)) // 9)) * 112) + tl.maximum((((tl.program_id(0) // 112) % 112) + ((((_lv0 * 512) + tl.arange(0, 512)) // 3) % 3)) - 1, 0)) * 112) + tl.maximum(((tl.program_id(0) % 112) + (((_lv0 * 512) + tl.arange(0, 512)) % 3)) - 1, 0)) - 6422527, 0), 0) + 0 * tl.arange(0, 512)), mask=((((_lv0 * 512) + tl.arange(0, 512)) < 576) & ((((1 <= (((tl.program_id(0) // 112) % 112) + ((((_lv0 * 512) + tl.arange(0, 512)) // 3) % 3))) & ((((tl.program_id(0) // 112) % 112) + ((((_lv0 * 512) + tl.arange(0, 512)) // 3) % 3)) < 113)) & (1 <= ((tl.program_id(0) % 112) + (((_lv0 * 512) + tl.arange(0, 512)) % 3)))) & (((tl.program_id(0) % 112) + (((_lv0 * 512) + tl.arange(0, 512)) % 3)) < 113))), other=0.0) * tl.load(in9_ptr + (((((((((tl.program_id(0) // 12544) % 128) * 64) + (((_lv0 * 512) + tl.arange(0, 512)) // 9)) * 3) + ((((_lv0 * 512) + tl.arange(0, 512)) // 3) % 3)) * 3) + (((_lv0 * 512) + tl.arange(0, 512)) % 3)) + 0 * tl.arange(0, 512)), mask=((((_lv0 * 512) + tl.arange(0, 512)) < 576) & ((((1 <= (((tl.program_id(0) // 112) % 112) + ((((_lv0 * 512) + tl.arange(0, 512)) // 3) % 3))) & ((((tl.program_id(0) // 112) % 112) + ((((_lv0 * 512) + tl.arange(0, 512)) // 3) % 3)) < 113)) & (1 <= ((tl.program_id(0) % 112) + (((_lv0 * 512) + tl.arange(0, 512)) % 3)))) & (((tl.program_id(0) % 112) + (((_lv0 * 512) + tl.arange(0, 512)) % 3)) < 113))), other=0.0)), 0.0))
    _v = (tl.sum(_acc0, axis=0) + tl.load(in10_ptr + (((tl.program_id(0) // 12544) % 128))))
    tl.store(out_ptr + tl.program_id(0), _v)


def t027_s13(out, ins):
    grid = (12845056,)
    t027_s13_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37], ins[38], ins[39])
    return out


@triton.jit
def t027_s14_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr, in38_ptr, in39_ptr, in40_ptr):
    _acc0 = tl.zeros([256], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 256) + tl.arange(0, 256)) < 392) & ((((tl.program_id(0) % 256) * 392) + ((_lv0 * 256) + tl.arange(0, 256))) < 100352)), tl.load(in40_ptr + (tl.maximum(((((((((tl.program_id(0) % 256) * 392) + ((_lv0 * 256) + tl.arange(0, 256))) // 12544) * 128) + (tl.program_id(0) // 256)) * 12544) + ((((tl.program_id(0) % 256) * 392) + ((_lv0 * 256) + tl.arange(0, 256))) % 12544)) - tl.maximum(((((((((tl.program_id(0) % 256) * 392) + ((_lv0 * 256) + tl.arange(0, 256))) // 12544) * 128) + (tl.program_id(0) // 256)) * 12544) + ((((tl.program_id(0) % 256) * 392) + ((_lv0 * 256) + tl.arange(0, 256))) % 12544)) - 12845055, 0), 0) + 0 * tl.arange(0, 256)), mask=((((_lv0 * 256) + tl.arange(0, 256)) < 392) & ((((tl.program_id(0) % 256) * 392) + ((_lv0 * 256) + tl.arange(0, 256))) < 100352)), other=0.0), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t027_s14(out, ins):
    grid = (32768,)
    t027_s14_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37], ins[38], ins[39], ins[40])
    return out


@triton.jit
def t027_s15_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr, in38_ptr, in39_ptr, in40_ptr, in41_ptr):
    _acc0 = tl.zeros([256], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 256) + tl.arange(0, 256)) < 256) & True), tl.load(in41_ptr + (((tl.program_id(0) * 256) + ((_lv0 * 256) + tl.arange(0, 256))) + 0 * tl.arange(0, 256)), mask=((((_lv0 * 256) + tl.arange(0, 256)) < 256) & True), other=0.0), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t027_s15(out, ins):
    grid = (128,)
    t027_s15_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37], ins[38], ins[39], ins[40], ins[41])
    return out


@triton.jit
def t027_s16_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr, in38_ptr, in39_ptr, in40_ptr, in41_ptr, in42_ptr):
    _acc0 = tl.zeros([256], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 256) + tl.arange(0, 256)) < 392) & ((((tl.program_id(0) % 256) * 392) + ((_lv0 * 256) + tl.arange(0, 256))) < 100352)), ((tl.load(in40_ptr + (tl.maximum(((((((((tl.program_id(0) % 256) * 392) + ((_lv0 * 256) + tl.arange(0, 256))) // 12544) * 128) + (tl.program_id(0) // 256)) * 12544) + ((((tl.program_id(0) % 256) * 392) + ((_lv0 * 256) + tl.arange(0, 256))) % 12544)) - tl.maximum(((((((((tl.program_id(0) % 256) * 392) + ((_lv0 * 256) + tl.arange(0, 256))) // 12544) * 128) + (tl.program_id(0) // 256)) * 12544) + ((((tl.program_id(0) % 256) * 392) + ((_lv0 * 256) + tl.arange(0, 256))) % 12544)) - 12845055, 0), 0) + 0 * tl.arange(0, 256)), mask=((((_lv0 * 256) + tl.arange(0, 256)) < 392) & ((((tl.program_id(0) % 256) * 392) + ((_lv0 * 256) + tl.arange(0, 256))) < 100352)), other=0.0) - (tl.load(in42_ptr + (tl.maximum((tl.program_id(0) // 256) - tl.maximum((tl.program_id(0) // 256) - 127, 0), 0) + 0 * tl.arange(0, 256)), mask=((((_lv0 * 256) + tl.arange(0, 256)) < 392) & ((((tl.program_id(0) % 256) * 392) + ((_lv0 * 256) + tl.arange(0, 256))) < 100352)), other=0.0) * (1.0 * (1.0 / 100352.0)))) * (tl.load(in40_ptr + (tl.maximum(((((((((tl.program_id(0) % 256) * 392) + ((_lv0 * 256) + tl.arange(0, 256))) // 12544) * 128) + (tl.program_id(0) // 256)) * 12544) + ((((tl.program_id(0) % 256) * 392) + ((_lv0 * 256) + tl.arange(0, 256))) % 12544)) - tl.maximum(((((((((tl.program_id(0) % 256) * 392) + ((_lv0 * 256) + tl.arange(0, 256))) // 12544) * 128) + (tl.program_id(0) // 256)) * 12544) + ((((tl.program_id(0) % 256) * 392) + ((_lv0 * 256) + tl.arange(0, 256))) % 12544)) - 12845055, 0), 0) + 0 * tl.arange(0, 256)), mask=((((_lv0 * 256) + tl.arange(0, 256)) < 392) & ((((tl.program_id(0) % 256) * 392) + ((_lv0 * 256) + tl.arange(0, 256))) < 100352)), other=0.0) - (tl.load(in42_ptr + (tl.maximum((tl.program_id(0) // 256) - tl.maximum((tl.program_id(0) // 256) - 127, 0), 0) + 0 * tl.arange(0, 256)), mask=((((_lv0 * 256) + tl.arange(0, 256)) < 392) & ((((tl.program_id(0) % 256) * 392) + ((_lv0 * 256) + tl.arange(0, 256))) < 100352)), other=0.0) * (1.0 * (1.0 / 100352.0))))), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t027_s16(out, ins):
    grid = (32768,)
    t027_s16_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37], ins[38], ins[39], ins[40], ins[41], ins[42])
    return out


@triton.jit
def t027_s17_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr, in38_ptr, in39_ptr, in40_ptr, in41_ptr, in42_ptr, in43_ptr):
    _acc0 = tl.zeros([256], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 256) + tl.arange(0, 256)) < 256) & True), tl.load(in43_ptr + (((tl.program_id(0) * 256) + ((_lv0 * 256) + tl.arange(0, 256))) + 0 * tl.arange(0, 256)), mask=((((_lv0 * 256) + tl.arange(0, 256)) < 256) & True), other=0.0), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t027_s17(out, ins):
    grid = (128,)
    t027_s17_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37], ins[38], ins[39], ins[40], ins[41], ins[42], ins[43])
    return out


@triton.jit
def t027_s18_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr, in38_ptr, in39_ptr, in40_ptr, in41_ptr, in42_ptr, in43_ptr, in44_ptr):
    _acc0 = tl.zeros([1], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), ((((tl.load(in40_ptr + (tl.program_id(0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) - (tl.load(in42_ptr + (tl.maximum(((tl.program_id(0) // 12544) % 128) - tl.maximum(((tl.program_id(0) // 12544) % 128) - 127, 0), 0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) * (1.0 * (1.0 / 100352.0)))) * (1.0 / tl.sqrt(((tl.load(in44_ptr + (tl.maximum(((tl.program_id(0) // 12544) % 128) - tl.maximum(((tl.program_id(0) // 12544) % 128) - 127, 0), 0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) * (1.0 * (1.0 / 100352.0))) + (1.0 * (1.0 / 100000.0)))))) * tl.load(in11_ptr + (((tl.program_id(0) // 12544) % 128) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)) + tl.load(in12_ptr + (((tl.program_id(0) // 12544) % 128) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)), 0.0))
    _v = tl.maximum(tl.sum(_acc0, axis=0), (0.0 * (1.0 / 1.0)))
    tl.store(out_ptr + tl.program_id(0), _v)


def t027_s18(out, ins):
    grid = (12845056,)
    t027_s18_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37], ins[38], ins[39], ins[40], ins[41], ins[42], ins[43], ins[44])
    return out


@triton.jit
def t027_s19_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr, in38_ptr, in39_ptr, in40_ptr, in41_ptr, in42_ptr, in43_ptr, in44_ptr, in45_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 1152) & ((((1 <= (((tl.program_id(0) // 112) % 112) + ((((_lv0 * 1024) + tl.arange(0, 1024)) // 3) % 3))) & ((((tl.program_id(0) // 112) % 112) + ((((_lv0 * 1024) + tl.arange(0, 1024)) // 3) % 3)) < 113)) & (1 <= ((tl.program_id(0) % 112) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 3)))) & (((tl.program_id(0) % 112) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 3)) < 113))), (tl.load(in45_ptr + (tl.maximum((((((((tl.program_id(0) // 1605632) * 128) + (((_lv0 * 1024) + tl.arange(0, 1024)) // 9)) * 112) + tl.maximum((((tl.program_id(0) // 112) % 112) + ((((_lv0 * 1024) + tl.arange(0, 1024)) // 3) % 3)) - 1, 0)) * 112) + tl.maximum(((tl.program_id(0) % 112) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 3)) - 1, 0)) - tl.maximum((((((((tl.program_id(0) // 1605632) * 128) + (((_lv0 * 1024) + tl.arange(0, 1024)) // 9)) * 112) + tl.maximum((((tl.program_id(0) // 112) % 112) + ((((_lv0 * 1024) + tl.arange(0, 1024)) // 3) % 3)) - 1, 0)) * 112) + tl.maximum(((tl.program_id(0) % 112) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 3)) - 1, 0)) - 12845055, 0), 0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 1152) & ((((1 <= (((tl.program_id(0) // 112) % 112) + ((((_lv0 * 1024) + tl.arange(0, 1024)) // 3) % 3))) & ((((tl.program_id(0) // 112) % 112) + ((((_lv0 * 1024) + tl.arange(0, 1024)) // 3) % 3)) < 113)) & (1 <= ((tl.program_id(0) % 112) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 3)))) & (((tl.program_id(0) % 112) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 3)) < 113))), other=0.0) * tl.load(in13_ptr + (((((((((tl.program_id(0) // 12544) % 128) * 128) + (((_lv0 * 1024) + tl.arange(0, 1024)) // 9)) * 3) + ((((_lv0 * 1024) + tl.arange(0, 1024)) // 3) % 3)) * 3) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 3)) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 1152) & ((((1 <= (((tl.program_id(0) // 112) % 112) + ((((_lv0 * 1024) + tl.arange(0, 1024)) // 3) % 3))) & ((((tl.program_id(0) // 112) % 112) + ((((_lv0 * 1024) + tl.arange(0, 1024)) // 3) % 3)) < 113)) & (1 <= ((tl.program_id(0) % 112) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 3)))) & (((tl.program_id(0) % 112) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 3)) < 113))), other=0.0)), 0.0))
    _v = (tl.sum(_acc0, axis=0) + tl.load(in14_ptr + (((tl.program_id(0) // 12544) % 128))))
    tl.store(out_ptr + tl.program_id(0), _v)


def t027_s19(out, ins):
    grid = (12845056,)
    t027_s19_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37], ins[38], ins[39], ins[40], ins[41], ins[42], ins[43], ins[44], ins[45])
    return out


@triton.jit
def t027_s20_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr, in38_ptr, in39_ptr, in40_ptr, in41_ptr, in42_ptr, in43_ptr, in44_ptr, in45_ptr, in46_ptr):
    _acc0 = tl.zeros([256], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 256) + tl.arange(0, 256)) < 392) & ((((tl.program_id(0) % 256) * 392) + ((_lv0 * 256) + tl.arange(0, 256))) < 100352)), tl.load(in46_ptr + (tl.maximum(((((((((tl.program_id(0) % 256) * 392) + ((_lv0 * 256) + tl.arange(0, 256))) // 12544) * 128) + (tl.program_id(0) // 256)) * 12544) + ((((tl.program_id(0) % 256) * 392) + ((_lv0 * 256) + tl.arange(0, 256))) % 12544)) - tl.maximum(((((((((tl.program_id(0) % 256) * 392) + ((_lv0 * 256) + tl.arange(0, 256))) // 12544) * 128) + (tl.program_id(0) // 256)) * 12544) + ((((tl.program_id(0) % 256) * 392) + ((_lv0 * 256) + tl.arange(0, 256))) % 12544)) - 12845055, 0), 0) + 0 * tl.arange(0, 256)), mask=((((_lv0 * 256) + tl.arange(0, 256)) < 392) & ((((tl.program_id(0) % 256) * 392) + ((_lv0 * 256) + tl.arange(0, 256))) < 100352)), other=0.0), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t027_s20(out, ins):
    grid = (32768,)
    t027_s20_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37], ins[38], ins[39], ins[40], ins[41], ins[42], ins[43], ins[44], ins[45], ins[46])
    return out


@triton.jit
def t027_s21_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr, in38_ptr, in39_ptr, in40_ptr, in41_ptr, in42_ptr, in43_ptr, in44_ptr, in45_ptr, in46_ptr, in47_ptr):
    _acc0 = tl.zeros([256], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 256) + tl.arange(0, 256)) < 256) & True), tl.load(in47_ptr + (((tl.program_id(0) * 256) + ((_lv0 * 256) + tl.arange(0, 256))) + 0 * tl.arange(0, 256)), mask=((((_lv0 * 256) + tl.arange(0, 256)) < 256) & True), other=0.0), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t027_s21(out, ins):
    grid = (128,)
    t027_s21_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37], ins[38], ins[39], ins[40], ins[41], ins[42], ins[43], ins[44], ins[45], ins[46], ins[47])
    return out


@triton.jit
def t027_s22_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr, in38_ptr, in39_ptr, in40_ptr, in41_ptr, in42_ptr, in43_ptr, in44_ptr, in45_ptr, in46_ptr, in47_ptr, in48_ptr):
    _acc0 = tl.zeros([256], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 256) + tl.arange(0, 256)) < 392) & ((((tl.program_id(0) % 256) * 392) + ((_lv0 * 256) + tl.arange(0, 256))) < 100352)), ((tl.load(in46_ptr + (tl.maximum(((((((((tl.program_id(0) % 256) * 392) + ((_lv0 * 256) + tl.arange(0, 256))) // 12544) * 128) + (tl.program_id(0) // 256)) * 12544) + ((((tl.program_id(0) % 256) * 392) + ((_lv0 * 256) + tl.arange(0, 256))) % 12544)) - tl.maximum(((((((((tl.program_id(0) % 256) * 392) + ((_lv0 * 256) + tl.arange(0, 256))) // 12544) * 128) + (tl.program_id(0) // 256)) * 12544) + ((((tl.program_id(0) % 256) * 392) + ((_lv0 * 256) + tl.arange(0, 256))) % 12544)) - 12845055, 0), 0) + 0 * tl.arange(0, 256)), mask=((((_lv0 * 256) + tl.arange(0, 256)) < 392) & ((((tl.program_id(0) % 256) * 392) + ((_lv0 * 256) + tl.arange(0, 256))) < 100352)), other=0.0) - (tl.load(in48_ptr + (tl.maximum((tl.program_id(0) // 256) - tl.maximum((tl.program_id(0) // 256) - 127, 0), 0) + 0 * tl.arange(0, 256)), mask=((((_lv0 * 256) + tl.arange(0, 256)) < 392) & ((((tl.program_id(0) % 256) * 392) + ((_lv0 * 256) + tl.arange(0, 256))) < 100352)), other=0.0) * (1.0 * (1.0 / 100352.0)))) * (tl.load(in46_ptr + (tl.maximum(((((((((tl.program_id(0) % 256) * 392) + ((_lv0 * 256) + tl.arange(0, 256))) // 12544) * 128) + (tl.program_id(0) // 256)) * 12544) + ((((tl.program_id(0) % 256) * 392) + ((_lv0 * 256) + tl.arange(0, 256))) % 12544)) - tl.maximum(((((((((tl.program_id(0) % 256) * 392) + ((_lv0 * 256) + tl.arange(0, 256))) // 12544) * 128) + (tl.program_id(0) // 256)) * 12544) + ((((tl.program_id(0) % 256) * 392) + ((_lv0 * 256) + tl.arange(0, 256))) % 12544)) - 12845055, 0), 0) + 0 * tl.arange(0, 256)), mask=((((_lv0 * 256) + tl.arange(0, 256)) < 392) & ((((tl.program_id(0) % 256) * 392) + ((_lv0 * 256) + tl.arange(0, 256))) < 100352)), other=0.0) - (tl.load(in48_ptr + (tl.maximum((tl.program_id(0) // 256) - tl.maximum((tl.program_id(0) // 256) - 127, 0), 0) + 0 * tl.arange(0, 256)), mask=((((_lv0 * 256) + tl.arange(0, 256)) < 392) & ((((tl.program_id(0) % 256) * 392) + ((_lv0 * 256) + tl.arange(0, 256))) < 100352)), other=0.0) * (1.0 * (1.0 / 100352.0))))), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t027_s22(out, ins):
    grid = (32768,)
    t027_s22_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37], ins[38], ins[39], ins[40], ins[41], ins[42], ins[43], ins[44], ins[45], ins[46], ins[47], ins[48])
    return out


@triton.jit
def t027_s23_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr, in38_ptr, in39_ptr, in40_ptr, in41_ptr, in42_ptr, in43_ptr, in44_ptr, in45_ptr, in46_ptr, in47_ptr, in48_ptr, in49_ptr):
    _acc0 = tl.zeros([256], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 256) + tl.arange(0, 256)) < 256) & True), tl.load(in49_ptr + (((tl.program_id(0) * 256) + ((_lv0 * 256) + tl.arange(0, 256))) + 0 * tl.arange(0, 256)), mask=((((_lv0 * 256) + tl.arange(0, 256)) < 256) & True), other=0.0), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t027_s23(out, ins):
    grid = (128,)
    t027_s23_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37], ins[38], ins[39], ins[40], ins[41], ins[42], ins[43], ins[44], ins[45], ins[46], ins[47], ins[48], ins[49])
    return out


@triton.jit
def t027_s24_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr, in38_ptr, in39_ptr, in40_ptr, in41_ptr, in42_ptr, in43_ptr, in44_ptr, in45_ptr, in46_ptr, in47_ptr, in48_ptr, in49_ptr, in50_ptr):
    _acc0 = tl.zeros([1], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), ((((tl.load(in46_ptr + (tl.program_id(0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) - (tl.load(in48_ptr + (tl.maximum(((tl.program_id(0) // 12544) % 128) - tl.maximum(((tl.program_id(0) // 12544) % 128) - 127, 0), 0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) * (1.0 * (1.0 / 100352.0)))) * (1.0 / tl.sqrt(((tl.load(in50_ptr + (tl.maximum(((tl.program_id(0) // 12544) % 128) - tl.maximum(((tl.program_id(0) // 12544) % 128) - 127, 0), 0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) * (1.0 * (1.0 / 100352.0))) + (1.0 * (1.0 / 100000.0)))))) * tl.load(in15_ptr + (((tl.program_id(0) // 12544) % 128) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)) + tl.load(in16_ptr + (((tl.program_id(0) // 12544) % 128) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)), 0.0))
    _v = tl.maximum(tl.sum(_acc0, axis=0), (0.0 * (1.0 / 1.0)))
    tl.store(out_ptr + tl.program_id(0), _v)


def t027_s24(out, ins):
    grid = (12845056,)
    t027_s24_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37], ins[38], ins[39], ins[40], ins[41], ins[42], ins[43], ins[44], ins[45], ins[46], ins[47], ins[48], ins[49], ins[50])
    return out


@triton.jit
def t027_s25_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr, in38_ptr, in39_ptr, in40_ptr, in41_ptr, in42_ptr, in43_ptr, in44_ptr, in45_ptr, in46_ptr, in47_ptr, in48_ptr, in49_ptr, in50_ptr, in51_ptr):
    _acc0 = tl.zeros([4], dtype=tl.float32) + (tl.load(in51_ptr + ((((((((tl.program_id(0) // 401408) * 128) + ((tl.program_id(0) // 3136) % 128)) * 112) + tl.maximum(((((tl.program_id(0) // 56) % 56) * 2) + tl.maximum(((0 // 2) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 56) % 56) * 2), 0) - (0 // 2), 0)) - tl.maximum(((0 // 2) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 56) % 56) * 2), 0) - (0 // 2), 0)) - tl.maximum(111 - (((tl.program_id(0) // 56) % 56) * 2), 0), 0), 0)) - tl.maximum(((((tl.program_id(0) // 56) % 56) * 2) + tl.maximum(((0 // 2) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 56) % 56) * 2), 0) - (0 // 2), 0)) - tl.maximum(((0 // 2) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 56) % 56) * 2), 0) - (0 // 2), 0)) - tl.maximum(111 - (((tl.program_id(0) // 56) % 56) * 2), 0), 0), 0)) - 111, 0), 0)) * 112) + tl.maximum((((tl.program_id(0) % 56) * 2) + tl.maximum(((0 % 2) + tl.maximum(tl.maximum(0 - ((tl.program_id(0) % 56) * 2), 0) - (0 % 2), 0)) - tl.maximum(((0 % 2) + tl.maximum(tl.maximum(0 - ((tl.program_id(0) % 56) * 2), 0) - (0 % 2), 0)) - tl.maximum(111 - ((tl.program_id(0) % 56) * 2), 0), 0), 0)) - tl.maximum((((tl.program_id(0) % 56) * 2) + tl.maximum(((0 % 2) + tl.maximum(tl.maximum(0 - ((tl.program_id(0) % 56) * 2), 0) - (0 % 2), 0)) - tl.maximum(((0 % 2) + tl.maximum(tl.maximum(0 - ((tl.program_id(0) % 56) * 2), 0) - (0 % 2), 0)) - tl.maximum(111 - ((tl.program_id(0) % 56) * 2), 0), 0), 0)) - 111, 0), 0)))))
    for _lv0 in range(0, 1):
        _acc0 = tl.maximum(_acc0, tl.load(in51_ptr + ((((((((tl.program_id(0) // 401408) * 128) + ((tl.program_id(0) // 3136) % 128)) * 112) + tl.maximum(((((tl.program_id(0) // 56) % 56) * 2) + tl.maximum(((tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - 3, 0), 0) // 2) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 56) % 56) * 2), 0) - (tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - 3, 0), 0) // 2), 0)) - tl.maximum(((tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - 3, 0), 0) // 2) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 56) % 56) * 2), 0) - (tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - 3, 0), 0) // 2), 0)) - tl.maximum(111 - (((tl.program_id(0) // 56) % 56) * 2), 0), 0), 0)) - tl.maximum(((((tl.program_id(0) // 56) % 56) * 2) + tl.maximum(((tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - 3, 0), 0) // 2) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 56) % 56) * 2), 0) - (tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - 3, 0), 0) // 2), 0)) - tl.maximum(((tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - 3, 0), 0) // 2) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 56) % 56) * 2), 0) - (tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - 3, 0), 0) // 2), 0)) - tl.maximum(111 - (((tl.program_id(0) // 56) % 56) * 2), 0), 0), 0)) - 111, 0), 0)) * 112) + tl.maximum((((tl.program_id(0) % 56) * 2) + tl.maximum(((tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - 3, 0), 0) % 2) + tl.maximum(tl.maximum(0 - ((tl.program_id(0) % 56) * 2), 0) - (tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - 3, 0), 0) % 2), 0)) - tl.maximum(((tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - 3, 0), 0) % 2) + tl.maximum(tl.maximum(0 - ((tl.program_id(0) % 56) * 2), 0) - (tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - 3, 0), 0) % 2), 0)) - tl.maximum(111 - ((tl.program_id(0) % 56) * 2), 0), 0), 0)) - tl.maximum((((tl.program_id(0) % 56) * 2) + tl.maximum(((tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - 3, 0), 0) % 2) + tl.maximum(tl.maximum(0 - ((tl.program_id(0) % 56) * 2), 0) - (tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - 3, 0), 0) % 2), 0)) - tl.maximum(((tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - 3, 0), 0) % 2) + tl.maximum(tl.maximum(0 - ((tl.program_id(0) % 56) * 2), 0) - (tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - 3, 0), 0) % 2), 0)) - tl.maximum(111 - ((tl.program_id(0) % 56) * 2), 0), 0), 0)) - 111, 0), 0)))))
    _v = tl.max(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t027_s25(out, ins):
    grid = (3211264,)
    t027_s25_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37], ins[38], ins[39], ins[40], ins[41], ins[42], ins[43], ins[44], ins[45], ins[46], ins[47], ins[48], ins[49], ins[50], ins[51])
    return out


@triton.jit
def t027_s26_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr, in38_ptr, in39_ptr, in40_ptr, in41_ptr, in42_ptr, in43_ptr, in44_ptr, in45_ptr, in46_ptr, in47_ptr, in48_ptr, in49_ptr, in50_ptr, in51_ptr, in52_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 1152) & ((((1 <= (((tl.program_id(0) // 56) % 56) + ((((_lv0 * 1024) + tl.arange(0, 1024)) // 3) % 3))) & ((((tl.program_id(0) // 56) % 56) + ((((_lv0 * 1024) + tl.arange(0, 1024)) // 3) % 3)) < 57)) & (1 <= ((tl.program_id(0) % 56) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 3)))) & (((tl.program_id(0) % 56) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 3)) < 57))), (tl.load(in52_ptr + (tl.maximum((((((((tl.program_id(0) // 802816) * 128) + (((_lv0 * 1024) + tl.arange(0, 1024)) // 9)) * 56) + tl.maximum((((tl.program_id(0) // 56) % 56) + ((((_lv0 * 1024) + tl.arange(0, 1024)) // 3) % 3)) - 1, 0)) * 56) + tl.maximum(((tl.program_id(0) % 56) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 3)) - 1, 0)) - tl.maximum((((((((tl.program_id(0) // 802816) * 128) + (((_lv0 * 1024) + tl.arange(0, 1024)) // 9)) * 56) + tl.maximum((((tl.program_id(0) // 56) % 56) + ((((_lv0 * 1024) + tl.arange(0, 1024)) // 3) % 3)) - 1, 0)) * 56) + tl.maximum(((tl.program_id(0) % 56) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 3)) - 1, 0)) - 3211263, 0), 0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 1152) & ((((1 <= (((tl.program_id(0) // 56) % 56) + ((((_lv0 * 1024) + tl.arange(0, 1024)) // 3) % 3))) & ((((tl.program_id(0) // 56) % 56) + ((((_lv0 * 1024) + tl.arange(0, 1024)) // 3) % 3)) < 57)) & (1 <= ((tl.program_id(0) % 56) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 3)))) & (((tl.program_id(0) % 56) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 3)) < 57))), other=0.0) * tl.load(in17_ptr + (((((((((tl.program_id(0) // 3136) % 256) * 128) + (((_lv0 * 1024) + tl.arange(0, 1024)) // 9)) * 3) + ((((_lv0 * 1024) + tl.arange(0, 1024)) // 3) % 3)) * 3) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 3)) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 1152) & ((((1 <= (((tl.program_id(0) // 56) % 56) + ((((_lv0 * 1024) + tl.arange(0, 1024)) // 3) % 3))) & ((((tl.program_id(0) // 56) % 56) + ((((_lv0 * 1024) + tl.arange(0, 1024)) // 3) % 3)) < 57)) & (1 <= ((tl.program_id(0) % 56) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 3)))) & (((tl.program_id(0) % 56) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 3)) < 57))), other=0.0)), 0.0))
    _v = (tl.sum(_acc0, axis=0) + tl.load(in18_ptr + (((tl.program_id(0) // 3136) % 256))))
    tl.store(out_ptr + tl.program_id(0), _v)


def t027_s26(out, ins):
    grid = (6422528,)
    t027_s26_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37], ins[38], ins[39], ins[40], ins[41], ins[42], ins[43], ins[44], ins[45], ins[46], ins[47], ins[48], ins[49], ins[50], ins[51], ins[52])
    return out


@triton.jit
def t027_s27_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr, in38_ptr, in39_ptr, in40_ptr, in41_ptr, in42_ptr, in43_ptr, in44_ptr, in45_ptr, in46_ptr, in47_ptr, in48_ptr, in49_ptr, in50_ptr, in51_ptr, in52_ptr, in53_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 25):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 25088) & True), tl.load(in53_ptr + (tl.maximum((((((((_lv0 * 1024) + tl.arange(0, 1024)) // 3136) * 256) + tl.program_id(0)) * 3136) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 3136)) - tl.maximum((((((((_lv0 * 1024) + tl.arange(0, 1024)) // 3136) * 256) + tl.program_id(0)) * 3136) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 3136)) - 6422527, 0), 0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 25088) & True), other=0.0), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t027_s27(out, ins):
    grid = (256,)
    t027_s27_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37], ins[38], ins[39], ins[40], ins[41], ins[42], ins[43], ins[44], ins[45], ins[46], ins[47], ins[48], ins[49], ins[50], ins[51], ins[52], ins[53])
    return out


@triton.jit
def t027_s28_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr, in38_ptr, in39_ptr, in40_ptr, in41_ptr, in42_ptr, in43_ptr, in44_ptr, in45_ptr, in46_ptr, in47_ptr, in48_ptr, in49_ptr, in50_ptr, in51_ptr, in52_ptr, in53_ptr, in54_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 25):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 25088) & True), ((tl.load(in53_ptr + (tl.maximum((((((((_lv0 * 1024) + tl.arange(0, 1024)) // 3136) * 256) + tl.program_id(0)) * 3136) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 3136)) - tl.maximum((((((((_lv0 * 1024) + tl.arange(0, 1024)) // 3136) * 256) + tl.program_id(0)) * 3136) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 3136)) - 6422527, 0), 0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 25088) & True), other=0.0) - (tl.load(in54_ptr + (tl.program_id(0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 25088) & True), other=0.0) * (1.0 * (1.0 / 25088.0)))) * (tl.load(in53_ptr + (tl.maximum((((((((_lv0 * 1024) + tl.arange(0, 1024)) // 3136) * 256) + tl.program_id(0)) * 3136) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 3136)) - tl.maximum((((((((_lv0 * 1024) + tl.arange(0, 1024)) // 3136) * 256) + tl.program_id(0)) * 3136) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 3136)) - 6422527, 0), 0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 25088) & True), other=0.0) - (tl.load(in54_ptr + (tl.program_id(0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 25088) & True), other=0.0) * (1.0 * (1.0 / 25088.0))))), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t027_s28(out, ins):
    grid = (256,)
    t027_s28_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37], ins[38], ins[39], ins[40], ins[41], ins[42], ins[43], ins[44], ins[45], ins[46], ins[47], ins[48], ins[49], ins[50], ins[51], ins[52], ins[53], ins[54])
    return out


@triton.jit
def t027_s29_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr, in38_ptr, in39_ptr, in40_ptr, in41_ptr, in42_ptr, in43_ptr, in44_ptr, in45_ptr, in46_ptr, in47_ptr, in48_ptr, in49_ptr, in50_ptr, in51_ptr, in52_ptr, in53_ptr, in54_ptr, in55_ptr):
    _acc0 = tl.zeros([1], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), ((((tl.load(in53_ptr + (tl.program_id(0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) - (tl.load(in54_ptr + (tl.maximum(((tl.program_id(0) // 3136) % 256) - tl.maximum(((tl.program_id(0) // 3136) % 256) - 255, 0), 0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) * (1.0 * (1.0 / 25088.0)))) * (1.0 / tl.sqrt(((tl.load(in55_ptr + (tl.maximum(((tl.program_id(0) // 3136) % 256) - tl.maximum(((tl.program_id(0) // 3136) % 256) - 255, 0), 0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) * (1.0 * (1.0 / 25088.0))) + (1.0 * (1.0 / 100000.0)))))) * tl.load(in19_ptr + (((tl.program_id(0) // 3136) % 256) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)) + tl.load(in20_ptr + (((tl.program_id(0) // 3136) % 256) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)), 0.0))
    _v = tl.maximum(tl.sum(_acc0, axis=0), (0.0 * (1.0 / 1.0)))
    tl.store(out_ptr + tl.program_id(0), _v)


def t027_s29(out, ins):
    grid = (6422528,)
    t027_s29_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37], ins[38], ins[39], ins[40], ins[41], ins[42], ins[43], ins[44], ins[45], ins[46], ins[47], ins[48], ins[49], ins[50], ins[51], ins[52], ins[53], ins[54], ins[55])
    return out


@triton.jit
def t027_s30_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr, in38_ptr, in39_ptr, in40_ptr, in41_ptr, in42_ptr, in43_ptr, in44_ptr, in45_ptr, in46_ptr, in47_ptr, in48_ptr, in49_ptr, in50_ptr, in51_ptr, in52_ptr, in53_ptr, in54_ptr, in55_ptr, in56_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 3):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 2304) & ((((1 <= (((tl.program_id(0) // 56) % 56) + ((((_lv0 * 1024) + tl.arange(0, 1024)) // 3) % 3))) & ((((tl.program_id(0) // 56) % 56) + ((((_lv0 * 1024) + tl.arange(0, 1024)) // 3) % 3)) < 57)) & (1 <= ((tl.program_id(0) % 56) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 3)))) & (((tl.program_id(0) % 56) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 3)) < 57))), (tl.load(in56_ptr + (tl.maximum((((((((tl.program_id(0) // 802816) * 256) + (((_lv0 * 1024) + tl.arange(0, 1024)) // 9)) * 56) + tl.maximum((((tl.program_id(0) // 56) % 56) + ((((_lv0 * 1024) + tl.arange(0, 1024)) // 3) % 3)) - 1, 0)) * 56) + tl.maximum(((tl.program_id(0) % 56) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 3)) - 1, 0)) - tl.maximum((((((((tl.program_id(0) // 802816) * 256) + (((_lv0 * 1024) + tl.arange(0, 1024)) // 9)) * 56) + tl.maximum((((tl.program_id(0) // 56) % 56) + ((((_lv0 * 1024) + tl.arange(0, 1024)) // 3) % 3)) - 1, 0)) * 56) + tl.maximum(((tl.program_id(0) % 56) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 3)) - 1, 0)) - 6422527, 0), 0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 2304) & ((((1 <= (((tl.program_id(0) // 56) % 56) + ((((_lv0 * 1024) + tl.arange(0, 1024)) // 3) % 3))) & ((((tl.program_id(0) // 56) % 56) + ((((_lv0 * 1024) + tl.arange(0, 1024)) // 3) % 3)) < 57)) & (1 <= ((tl.program_id(0) % 56) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 3)))) & (((tl.program_id(0) % 56) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 3)) < 57))), other=0.0) * tl.load(in21_ptr + (((((((((tl.program_id(0) // 3136) % 256) * 256) + (((_lv0 * 1024) + tl.arange(0, 1024)) // 9)) * 3) + ((((_lv0 * 1024) + tl.arange(0, 1024)) // 3) % 3)) * 3) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 3)) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 2304) & ((((1 <= (((tl.program_id(0) // 56) % 56) + ((((_lv0 * 1024) + tl.arange(0, 1024)) // 3) % 3))) & ((((tl.program_id(0) // 56) % 56) + ((((_lv0 * 1024) + tl.arange(0, 1024)) // 3) % 3)) < 57)) & (1 <= ((tl.program_id(0) % 56) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 3)))) & (((tl.program_id(0) % 56) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 3)) < 57))), other=0.0)), 0.0))
    _v = (tl.sum(_acc0, axis=0) + tl.load(in22_ptr + (((tl.program_id(0) // 3136) % 256))))
    tl.store(out_ptr + tl.program_id(0), _v)


def t027_s30(out, ins):
    grid = (6422528,)
    t027_s30_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37], ins[38], ins[39], ins[40], ins[41], ins[42], ins[43], ins[44], ins[45], ins[46], ins[47], ins[48], ins[49], ins[50], ins[51], ins[52], ins[53], ins[54], ins[55], ins[56])
    return out


@triton.jit
def t027_s31_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr, in38_ptr, in39_ptr, in40_ptr, in41_ptr, in42_ptr, in43_ptr, in44_ptr, in45_ptr, in46_ptr, in47_ptr, in48_ptr, in49_ptr, in50_ptr, in51_ptr, in52_ptr, in53_ptr, in54_ptr, in55_ptr, in56_ptr, in57_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 25):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 25088) & True), tl.load(in57_ptr + (tl.maximum((((((((_lv0 * 1024) + tl.arange(0, 1024)) // 3136) * 256) + tl.program_id(0)) * 3136) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 3136)) - tl.maximum((((((((_lv0 * 1024) + tl.arange(0, 1024)) // 3136) * 256) + tl.program_id(0)) * 3136) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 3136)) - 6422527, 0), 0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 25088) & True), other=0.0), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t027_s31(out, ins):
    grid = (256,)
    t027_s31_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37], ins[38], ins[39], ins[40], ins[41], ins[42], ins[43], ins[44], ins[45], ins[46], ins[47], ins[48], ins[49], ins[50], ins[51], ins[52], ins[53], ins[54], ins[55], ins[56], ins[57])
    return out


@triton.jit
def t027_s32_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr, in38_ptr, in39_ptr, in40_ptr, in41_ptr, in42_ptr, in43_ptr, in44_ptr, in45_ptr, in46_ptr, in47_ptr, in48_ptr, in49_ptr, in50_ptr, in51_ptr, in52_ptr, in53_ptr, in54_ptr, in55_ptr, in56_ptr, in57_ptr, in58_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 25):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 25088) & True), ((tl.load(in57_ptr + (tl.maximum((((((((_lv0 * 1024) + tl.arange(0, 1024)) // 3136) * 256) + tl.program_id(0)) * 3136) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 3136)) - tl.maximum((((((((_lv0 * 1024) + tl.arange(0, 1024)) // 3136) * 256) + tl.program_id(0)) * 3136) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 3136)) - 6422527, 0), 0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 25088) & True), other=0.0) - (tl.load(in58_ptr + (tl.program_id(0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 25088) & True), other=0.0) * (1.0 * (1.0 / 25088.0)))) * (tl.load(in57_ptr + (tl.maximum((((((((_lv0 * 1024) + tl.arange(0, 1024)) // 3136) * 256) + tl.program_id(0)) * 3136) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 3136)) - tl.maximum((((((((_lv0 * 1024) + tl.arange(0, 1024)) // 3136) * 256) + tl.program_id(0)) * 3136) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 3136)) - 6422527, 0), 0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 25088) & True), other=0.0) - (tl.load(in58_ptr + (tl.program_id(0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 25088) & True), other=0.0) * (1.0 * (1.0 / 25088.0))))), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t027_s32(out, ins):
    grid = (256,)
    t027_s32_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37], ins[38], ins[39], ins[40], ins[41], ins[42], ins[43], ins[44], ins[45], ins[46], ins[47], ins[48], ins[49], ins[50], ins[51], ins[52], ins[53], ins[54], ins[55], ins[56], ins[57], ins[58])
    return out


@triton.jit
def t027_s33_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr, in38_ptr, in39_ptr, in40_ptr, in41_ptr, in42_ptr, in43_ptr, in44_ptr, in45_ptr, in46_ptr, in47_ptr, in48_ptr, in49_ptr, in50_ptr, in51_ptr, in52_ptr, in53_ptr, in54_ptr, in55_ptr, in56_ptr, in57_ptr, in58_ptr, in59_ptr):
    _acc0 = tl.zeros([1], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), ((((tl.load(in57_ptr + (tl.program_id(0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) - (tl.load(in58_ptr + (tl.maximum(((tl.program_id(0) // 3136) % 256) - tl.maximum(((tl.program_id(0) // 3136) % 256) - 255, 0), 0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) * (1.0 * (1.0 / 25088.0)))) * (1.0 / tl.sqrt(((tl.load(in59_ptr + (tl.maximum(((tl.program_id(0) // 3136) % 256) - tl.maximum(((tl.program_id(0) // 3136) % 256) - 255, 0), 0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) * (1.0 * (1.0 / 25088.0))) + (1.0 * (1.0 / 100000.0)))))) * tl.load(in23_ptr + (((tl.program_id(0) // 3136) % 256) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)) + tl.load(in24_ptr + (((tl.program_id(0) // 3136) % 256) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)), 0.0))
    _v = tl.maximum(tl.sum(_acc0, axis=0), (0.0 * (1.0 / 1.0)))
    tl.store(out_ptr + tl.program_id(0), _v)


def t027_s33(out, ins):
    grid = (6422528,)
    t027_s33_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37], ins[38], ins[39], ins[40], ins[41], ins[42], ins[43], ins[44], ins[45], ins[46], ins[47], ins[48], ins[49], ins[50], ins[51], ins[52], ins[53], ins[54], ins[55], ins[56], ins[57], ins[58], ins[59])
    return out


@triton.jit
def t027_s34_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr, in38_ptr, in39_ptr, in40_ptr, in41_ptr, in42_ptr, in43_ptr, in44_ptr, in45_ptr, in46_ptr, in47_ptr, in48_ptr, in49_ptr, in50_ptr, in51_ptr, in52_ptr, in53_ptr, in54_ptr, in55_ptr, in56_ptr, in57_ptr, in58_ptr, in59_ptr, in60_ptr):
    _acc0 = tl.zeros([4], dtype=tl.float32) + (tl.load(in60_ptr + ((((((((tl.program_id(0) // 200704) * 256) + ((tl.program_id(0) // 784) % 256)) * 56) + tl.maximum(((((tl.program_id(0) // 28) % 28) * 2) + tl.maximum(((0 // 2) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 28) % 28) * 2), 0) - (0 // 2), 0)) - tl.maximum(((0 // 2) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 28) % 28) * 2), 0) - (0 // 2), 0)) - tl.maximum(55 - (((tl.program_id(0) // 28) % 28) * 2), 0), 0), 0)) - tl.maximum(((((tl.program_id(0) // 28) % 28) * 2) + tl.maximum(((0 // 2) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 28) % 28) * 2), 0) - (0 // 2), 0)) - tl.maximum(((0 // 2) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 28) % 28) * 2), 0) - (0 // 2), 0)) - tl.maximum(55 - (((tl.program_id(0) // 28) % 28) * 2), 0), 0), 0)) - 55, 0), 0)) * 56) + tl.maximum((((tl.program_id(0) % 28) * 2) + tl.maximum(((0 % 2) + tl.maximum(tl.maximum(0 - ((tl.program_id(0) % 28) * 2), 0) - (0 % 2), 0)) - tl.maximum(((0 % 2) + tl.maximum(tl.maximum(0 - ((tl.program_id(0) % 28) * 2), 0) - (0 % 2), 0)) - tl.maximum(55 - ((tl.program_id(0) % 28) * 2), 0), 0), 0)) - tl.maximum((((tl.program_id(0) % 28) * 2) + tl.maximum(((0 % 2) + tl.maximum(tl.maximum(0 - ((tl.program_id(0) % 28) * 2), 0) - (0 % 2), 0)) - tl.maximum(((0 % 2) + tl.maximum(tl.maximum(0 - ((tl.program_id(0) % 28) * 2), 0) - (0 % 2), 0)) - tl.maximum(55 - ((tl.program_id(0) % 28) * 2), 0), 0), 0)) - 55, 0), 0)))))
    for _lv0 in range(0, 1):
        _acc0 = tl.maximum(_acc0, tl.load(in60_ptr + ((((((((tl.program_id(0) // 200704) * 256) + ((tl.program_id(0) // 784) % 256)) * 56) + tl.maximum(((((tl.program_id(0) // 28) % 28) * 2) + tl.maximum(((tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - 3, 0), 0) // 2) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 28) % 28) * 2), 0) - (tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - 3, 0), 0) // 2), 0)) - tl.maximum(((tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - 3, 0), 0) // 2) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 28) % 28) * 2), 0) - (tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - 3, 0), 0) // 2), 0)) - tl.maximum(55 - (((tl.program_id(0) // 28) % 28) * 2), 0), 0), 0)) - tl.maximum(((((tl.program_id(0) // 28) % 28) * 2) + tl.maximum(((tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - 3, 0), 0) // 2) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 28) % 28) * 2), 0) - (tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - 3, 0), 0) // 2), 0)) - tl.maximum(((tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - 3, 0), 0) // 2) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 28) % 28) * 2), 0) - (tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - 3, 0), 0) // 2), 0)) - tl.maximum(55 - (((tl.program_id(0) // 28) % 28) * 2), 0), 0), 0)) - 55, 0), 0)) * 56) + tl.maximum((((tl.program_id(0) % 28) * 2) + tl.maximum(((tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - 3, 0), 0) % 2) + tl.maximum(tl.maximum(0 - ((tl.program_id(0) % 28) * 2), 0) - (tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - 3, 0), 0) % 2), 0)) - tl.maximum(((tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - 3, 0), 0) % 2) + tl.maximum(tl.maximum(0 - ((tl.program_id(0) % 28) * 2), 0) - (tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - 3, 0), 0) % 2), 0)) - tl.maximum(55 - ((tl.program_id(0) % 28) * 2), 0), 0), 0)) - tl.maximum((((tl.program_id(0) % 28) * 2) + tl.maximum(((tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - 3, 0), 0) % 2) + tl.maximum(tl.maximum(0 - ((tl.program_id(0) % 28) * 2), 0) - (tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - 3, 0), 0) % 2), 0)) - tl.maximum(((tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - 3, 0), 0) % 2) + tl.maximum(tl.maximum(0 - ((tl.program_id(0) % 28) * 2), 0) - (tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - 3, 0), 0) % 2), 0)) - tl.maximum(55 - ((tl.program_id(0) % 28) * 2), 0), 0), 0)) - 55, 0), 0)))))
    _v = tl.max(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t027_s34(out, ins):
    grid = (1605632,)
    t027_s34_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37], ins[38], ins[39], ins[40], ins[41], ins[42], ins[43], ins[44], ins[45], ins[46], ins[47], ins[48], ins[49], ins[50], ins[51], ins[52], ins[53], ins[54], ins[55], ins[56], ins[57], ins[58], ins[59], ins[60])
    return out


@triton.jit
def t027_s35_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr, in38_ptr, in39_ptr, in40_ptr, in41_ptr, in42_ptr, in43_ptr, in44_ptr, in45_ptr, in46_ptr, in47_ptr, in48_ptr, in49_ptr, in50_ptr, in51_ptr, in52_ptr, in53_ptr, in54_ptr, in55_ptr, in56_ptr, in57_ptr, in58_ptr, in59_ptr, in60_ptr, in61_ptr):
    _acc0 = tl.zeros([512], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 512) + tl.arange(0, 512)) < 784) & True), tl.load(in61_ptr + (((tl.program_id(0) * 784) + ((_lv0 * 512) + tl.arange(0, 512))) + 0 * tl.arange(0, 512)), mask=((((_lv0 * 512) + tl.arange(0, 512)) < 784) & True), other=0.0), 0.0))
    _v = (tl.sum(_acc0, axis=0) * (1.0 * (1.0 / 784.0)))
    tl.store(out_ptr + tl.program_id(0), _v)


def t027_s35(out, ins):
    grid = (2048,)
    t027_s35_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37], ins[38], ins[39], ins[40], ins[41], ins[42], ins[43], ins[44], ins[45], ins[46], ins[47], ins[48], ins[49], ins[50], ins[51], ins[52], ins[53], ins[54], ins[55], ins[56], ins[57], ins[58], ins[59], ins[60], ins[61])
    return out


@triton.jit
def t027_s36_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr, in38_ptr, in39_ptr, in40_ptr, in41_ptr, in42_ptr, in43_ptr, in44_ptr, in45_ptr, in46_ptr, in47_ptr, in48_ptr, in49_ptr, in50_ptr, in51_ptr, in52_ptr, in53_ptr, in54_ptr, in55_ptr, in56_ptr, in57_ptr, in58_ptr, in59_ptr, in60_ptr, in61_ptr, in62_ptr):
    _acc0 = tl.zeros([256], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 256) + tl.arange(0, 256)) < 256) & True), (tl.load(in62_ptr + ((((tl.program_id(0) // 10) * 256) + ((_lv0 * 256) + tl.arange(0, 256))) + 0 * tl.arange(0, 256)), mask=((((_lv0 * 256) + tl.arange(0, 256)) < 256) & True), other=0.0) * tl.load(in25_ptr + ((((tl.program_id(0) % 10) * 256) + ((_lv0 * 256) + tl.arange(0, 256))) + 0 * tl.arange(0, 256)), mask=((((_lv0 * 256) + tl.arange(0, 256)) < 256) & True), other=0.0)), 0.0))
    _v = (tl.sum(_acc0, axis=0) + tl.load(in26_ptr + ((tl.program_id(0) % 10))))
    tl.store(out_ptr + tl.program_id(0), _v)


def t027_s36(out, ins):
    grid = (80,)
    t027_s36_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37], ins[38], ins[39], ins[40], ins[41], ins[42], ins[43], ins[44], ins[45], ins[46], ins[47], ins[48], ins[49], ins[50], ins[51], ins[52], ins[53], ins[54], ins[55], ins[56], ins[57], ins[58], ins[59], ins[60], ins[61], ins[62])
    return out


def t027(out, ins):
    _t0 = torch.empty(25690112, device=ins[0].device, dtype=torch.float32)
    _t1 = torch.empty(16384, device=ins[0].device, dtype=torch.float32)
    _t2 = torch.empty(64, device=ins[0].device, dtype=torch.float32)
    _t3 = torch.empty(16384, device=ins[0].device, dtype=torch.float32)
    _t4 = torch.empty(64, device=ins[0].device, dtype=torch.float32)
    _t5 = torch.empty(25690112, device=ins[0].device, dtype=torch.float32)
    _t6 = torch.empty(25690112, device=ins[0].device, dtype=torch.float32)
    _t7 = torch.empty(16384, device=ins[0].device, dtype=torch.float32)
    _t8 = torch.empty(64, device=ins[0].device, dtype=torch.float32)
    _t9 = torch.empty(16384, device=ins[0].device, dtype=torch.float32)
    _t10 = torch.empty(64, device=ins[0].device, dtype=torch.float32)
    _t11 = torch.empty(25690112, device=ins[0].device, dtype=torch.float32)
    _t12 = torch.empty(6422528, device=ins[0].device, dtype=torch.float32)
    _t13 = torch.empty(12845056, device=ins[0].device, dtype=torch.float32)
    _t14 = torch.empty(32768, device=ins[0].device, dtype=torch.float32)
    _t15 = torch.empty(128, device=ins[0].device, dtype=torch.float32)
    _t16 = torch.empty(32768, device=ins[0].device, dtype=torch.float32)
    _t17 = torch.empty(128, device=ins[0].device, dtype=torch.float32)
    _t18 = torch.empty(12845056, device=ins[0].device, dtype=torch.float32)
    _t19 = torch.empty(12845056, device=ins[0].device, dtype=torch.float32)
    _t20 = torch.empty(32768, device=ins[0].device, dtype=torch.float32)
    _t21 = torch.empty(128, device=ins[0].device, dtype=torch.float32)
    _t22 = torch.empty(32768, device=ins[0].device, dtype=torch.float32)
    _t23 = torch.empty(128, device=ins[0].device, dtype=torch.float32)
    _t24 = torch.empty(12845056, device=ins[0].device, dtype=torch.float32)
    _t25 = torch.empty(3211264, device=ins[0].device, dtype=torch.float32)
    _t26 = torch.empty(6422528, device=ins[0].device, dtype=torch.float32)
    _t27 = torch.empty(256, device=ins[0].device, dtype=torch.float32)
    _t28 = torch.empty(256, device=ins[0].device, dtype=torch.float32)
    _t29 = torch.empty(6422528, device=ins[0].device, dtype=torch.float32)
    _t30 = torch.empty(6422528, device=ins[0].device, dtype=torch.float32)
    _t31 = torch.empty(256, device=ins[0].device, dtype=torch.float32)
    _t32 = torch.empty(256, device=ins[0].device, dtype=torch.float32)
    _t33 = torch.empty(6422528, device=ins[0].device, dtype=torch.float32)
    _t34 = torch.empty(1605632, device=ins[0].device, dtype=torch.float32)
    _t35 = torch.empty(2048, device=ins[0].device, dtype=torch.float32)
    t027_s0(_t0, list(ins))
    t027_s1(_t1, list(ins) + [_t0])
    t027_s2(_t2, list(ins) + [_t0, _t1])
    t027_s3(_t3, list(ins) + [_t0, _t1, _t2])
    t027_s4(_t4, list(ins) + [_t0, _t1, _t2, _t3])
    t027_s5(_t5, list(ins) + [_t0, _t1, _t2, _t3, _t4])
    t027_s6(_t6, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5])
    t027_s7(_t7, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6])
    t027_s8(_t8, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7])
    t027_s9(_t9, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8])
    t027_s10(_t10, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9])
    t027_s11(_t11, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10])
    t027_s12(_t12, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11])
    t027_s13(_t13, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12])
    t027_s14(_t14, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13])
    t027_s15(_t15, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13, _t14])
    t027_s16(_t16, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13, _t14, _t15])
    t027_s17(_t17, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13, _t14, _t15, _t16])
    t027_s18(_t18, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13, _t14, _t15, _t16, _t17])
    t027_s19(_t19, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13, _t14, _t15, _t16, _t17, _t18])
    t027_s20(_t20, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13, _t14, _t15, _t16, _t17, _t18, _t19])
    t027_s21(_t21, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13, _t14, _t15, _t16, _t17, _t18, _t19, _t20])
    t027_s22(_t22, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13, _t14, _t15, _t16, _t17, _t18, _t19, _t20, _t21])
    t027_s23(_t23, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13, _t14, _t15, _t16, _t17, _t18, _t19, _t20, _t21, _t22])
    t027_s24(_t24, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13, _t14, _t15, _t16, _t17, _t18, _t19, _t20, _t21, _t22, _t23])
    t027_s25(_t25, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13, _t14, _t15, _t16, _t17, _t18, _t19, _t20, _t21, _t22, _t23, _t24])
    t027_s26(_t26, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13, _t14, _t15, _t16, _t17, _t18, _t19, _t20, _t21, _t22, _t23, _t24, _t25])
    t027_s27(_t27, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13, _t14, _t15, _t16, _t17, _t18, _t19, _t20, _t21, _t22, _t23, _t24, _t25, _t26])
    t027_s28(_t28, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13, _t14, _t15, _t16, _t17, _t18, _t19, _t20, _t21, _t22, _t23, _t24, _t25, _t26, _t27])
    t027_s29(_t29, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13, _t14, _t15, _t16, _t17, _t18, _t19, _t20, _t21, _t22, _t23, _t24, _t25, _t26, _t27, _t28])
    t027_s30(_t30, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13, _t14, _t15, _t16, _t17, _t18, _t19, _t20, _t21, _t22, _t23, _t24, _t25, _t26, _t27, _t28, _t29])
    t027_s31(_t31, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13, _t14, _t15, _t16, _t17, _t18, _t19, _t20, _t21, _t22, _t23, _t24, _t25, _t26, _t27, _t28, _t29, _t30])
    t027_s32(_t32, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13, _t14, _t15, _t16, _t17, _t18, _t19, _t20, _t21, _t22, _t23, _t24, _t25, _t26, _t27, _t28, _t29, _t30, _t31])
    t027_s33(_t33, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13, _t14, _t15, _t16, _t17, _t18, _t19, _t20, _t21, _t22, _t23, _t24, _t25, _t26, _t27, _t28, _t29, _t30, _t31, _t32])
    t027_s34(_t34, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13, _t14, _t15, _t16, _t17, _t18, _t19, _t20, _t21, _t22, _t23, _t24, _t25, _t26, _t27, _t28, _t29, _t30, _t31, _t32, _t33])
    t027_s35(_t35, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13, _t14, _t15, _t16, _t17, _t18, _t19, _t20, _t21, _t22, _t23, _t24, _t25, _t26, _t27, _t28, _t29, _t30, _t31, _t32, _t33, _t34])
    t027_s36(out, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13, _t14, _t15, _t16, _t17, _t18, _t19, _t20, _t21, _t22, _t23, _t24, _t25, _t26, _t27, _t28, _t29, _t30, _t31, _t32, _t33, _t34, _t35])
    return out
