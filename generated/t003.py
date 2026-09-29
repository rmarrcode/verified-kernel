import torch
import triton
import triton.language as tl


@triton.jit
def _mul_combine(a, b):
    return a * b


@triton.jit
def t003_s0_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 8):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 8192) & True), (tl.load(in0_ptr + ((((tl.program_id(0) // 1024) * 8192) + ((_lv0 * 1024) + tl.arange(0, 1024))) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 8192) & True), other=0.0) * tl.load(in1_ptr + ((((tl.program_id(0) % 1024) * 8192) + ((_lv0 * 1024) + tl.arange(0, 1024))) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 8192) & True), other=0.0)), 0.0))
    _v = tl.maximum((tl.sum(_acc0, axis=0) + tl.load(in2_ptr + ((tl.program_id(0) % 1024)))), (0.0 * (1.0 / 1.0)))
    tl.store(out_ptr + tl.program_id(0), _v)


def t003_s0(out, ins):
    grid = (1048576,)
    t003_s0_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34])
    return out


@triton.jit
def t003_s1_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 1024) & True), (tl.load(in35_ptr + ((((tl.program_id(0) // 1024) * 1024) + ((_lv0 * 1024) + tl.arange(0, 1024))) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 1024) & True), other=0.0) * tl.load(in3_ptr + ((((tl.program_id(0) % 1024) * 1024) + ((_lv0 * 1024) + tl.arange(0, 1024))) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 1024) & True), other=0.0)), 0.0))
    _v = tl.maximum((tl.sum(_acc0, axis=0) + tl.load(in4_ptr + ((tl.program_id(0) % 1024)))), (0.0 * (1.0 / 1.0)))
    tl.store(out_ptr + tl.program_id(0), _v)


def t003_s1(out, ins):
    grid = (1048576,)
    t003_s1_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35])
    return out


@triton.jit
def t003_s2_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 1024) & True), (tl.load(in36_ptr + ((((tl.program_id(0) // 1024) * 1024) + ((_lv0 * 1024) + tl.arange(0, 1024))) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 1024) & True), other=0.0) * tl.load(in5_ptr + ((((tl.program_id(0) % 1024) * 1024) + ((_lv0 * 1024) + tl.arange(0, 1024))) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 1024) & True), other=0.0)), 0.0))
    _v = tl.maximum((tl.sum(_acc0, axis=0) + tl.load(in6_ptr + ((tl.program_id(0) % 1024)))), (0.0 * (1.0 / 1.0)))
    tl.store(out_ptr + tl.program_id(0), _v)


def t003_s2(out, ins):
    grid = (1048576,)
    t003_s2_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36])
    return out


@triton.jit
def t003_s3_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 1024) & True), (tl.load(in37_ptr + ((((tl.program_id(0) // 1024) * 1024) + ((_lv0 * 1024) + tl.arange(0, 1024))) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 1024) & True), other=0.0) * tl.load(in7_ptr + ((((tl.program_id(0) % 1024) * 1024) + ((_lv0 * 1024) + tl.arange(0, 1024))) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 1024) & True), other=0.0)), 0.0))
    _v = tl.maximum((tl.sum(_acc0, axis=0) + tl.load(in8_ptr + ((tl.program_id(0) % 1024)))), (0.0 * (1.0 / 1.0)))
    tl.store(out_ptr + tl.program_id(0), _v)


def t003_s3(out, ins):
    grid = (1048576,)
    t003_s3_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37])
    return out


@triton.jit
def t003_s4_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr, in38_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 1024) & True), (tl.load(in38_ptr + ((((tl.program_id(0) // 1024) * 1024) + ((_lv0 * 1024) + tl.arange(0, 1024))) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 1024) & True), other=0.0) * tl.load(in9_ptr + ((((tl.program_id(0) % 1024) * 1024) + ((_lv0 * 1024) + tl.arange(0, 1024))) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 1024) & True), other=0.0)), 0.0))
    _v = tl.maximum((tl.sum(_acc0, axis=0) + tl.load(in10_ptr + ((tl.program_id(0) % 1024)))), (0.0 * (1.0 / 1.0)))
    tl.store(out_ptr + tl.program_id(0), _v)


def t003_s4(out, ins):
    grid = (1048576,)
    t003_s4_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37], ins[38])
    return out


@triton.jit
def t003_s5_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr, in38_ptr, in39_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 1024) & True), (tl.load(in39_ptr + ((((tl.program_id(0) // 1024) * 1024) + ((_lv0 * 1024) + tl.arange(0, 1024))) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 1024) & True), other=0.0) * tl.load(in11_ptr + ((((tl.program_id(0) % 1024) * 1024) + ((_lv0 * 1024) + tl.arange(0, 1024))) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 1024) & True), other=0.0)), 0.0))
    _v = tl.maximum((tl.sum(_acc0, axis=0) + tl.load(in12_ptr + ((tl.program_id(0) % 1024)))), (0.0 * (1.0 / 1.0)))
    tl.store(out_ptr + tl.program_id(0), _v)


def t003_s5(out, ins):
    grid = (1048576,)
    t003_s5_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37], ins[38], ins[39])
    return out


@triton.jit
def t003_s6_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr, in38_ptr, in39_ptr, in40_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 1024) & True), (tl.load(in40_ptr + ((((tl.program_id(0) // 1024) * 1024) + ((_lv0 * 1024) + tl.arange(0, 1024))) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 1024) & True), other=0.0) * tl.load(in13_ptr + ((((tl.program_id(0) % 1024) * 1024) + ((_lv0 * 1024) + tl.arange(0, 1024))) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 1024) & True), other=0.0)), 0.0))
    _v = tl.maximum((tl.sum(_acc0, axis=0) + tl.load(in14_ptr + ((tl.program_id(0) % 1024)))), (0.0 * (1.0 / 1.0)))
    tl.store(out_ptr + tl.program_id(0), _v)


def t003_s6(out, ins):
    grid = (1048576,)
    t003_s6_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37], ins[38], ins[39], ins[40])
    return out


@triton.jit
def t003_s7_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr, in38_ptr, in39_ptr, in40_ptr, in41_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 1024) & True), (tl.load(in41_ptr + ((((tl.program_id(0) // 1024) * 1024) + ((_lv0 * 1024) + tl.arange(0, 1024))) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 1024) & True), other=0.0) * tl.load(in15_ptr + ((((tl.program_id(0) % 1024) * 1024) + ((_lv0 * 1024) + tl.arange(0, 1024))) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 1024) & True), other=0.0)), 0.0))
    _v = tl.maximum((tl.sum(_acc0, axis=0) + tl.load(in16_ptr + ((tl.program_id(0) % 1024)))), (0.0 * (1.0 / 1.0)))
    tl.store(out_ptr + tl.program_id(0), _v)


def t003_s7(out, ins):
    grid = (1048576,)
    t003_s7_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37], ins[38], ins[39], ins[40], ins[41])
    return out


@triton.jit
def t003_s8_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr, in38_ptr, in39_ptr, in40_ptr, in41_ptr, in42_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 1024) & True), (tl.load(in42_ptr + ((((tl.program_id(0) // 1024) * 1024) + ((_lv0 * 1024) + tl.arange(0, 1024))) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 1024) & True), other=0.0) * tl.load(in17_ptr + ((((tl.program_id(0) % 1024) * 1024) + ((_lv0 * 1024) + tl.arange(0, 1024))) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 1024) & True), other=0.0)), 0.0))
    _v = tl.maximum((tl.sum(_acc0, axis=0) + tl.load(in18_ptr + ((tl.program_id(0) % 1024)))), (0.0 * (1.0 / 1.0)))
    tl.store(out_ptr + tl.program_id(0), _v)


def t003_s8(out, ins):
    grid = (1048576,)
    t003_s8_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37], ins[38], ins[39], ins[40], ins[41], ins[42])
    return out


@triton.jit
def t003_s9_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr, in38_ptr, in39_ptr, in40_ptr, in41_ptr, in42_ptr, in43_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 1024) & True), (tl.load(in43_ptr + ((((tl.program_id(0) // 1024) * 1024) + ((_lv0 * 1024) + tl.arange(0, 1024))) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 1024) & True), other=0.0) * tl.load(in19_ptr + ((((tl.program_id(0) % 1024) * 1024) + ((_lv0 * 1024) + tl.arange(0, 1024))) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 1024) & True), other=0.0)), 0.0))
    _v = tl.maximum((tl.sum(_acc0, axis=0) + tl.load(in20_ptr + ((tl.program_id(0) % 1024)))), (0.0 * (1.0 / 1.0)))
    tl.store(out_ptr + tl.program_id(0), _v)


def t003_s9(out, ins):
    grid = (1048576,)
    t003_s9_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37], ins[38], ins[39], ins[40], ins[41], ins[42], ins[43])
    return out


@triton.jit
def t003_s10_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr, in38_ptr, in39_ptr, in40_ptr, in41_ptr, in42_ptr, in43_ptr, in44_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 1024) & True), (tl.load(in44_ptr + ((((tl.program_id(0) // 1024) * 1024) + ((_lv0 * 1024) + tl.arange(0, 1024))) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 1024) & True), other=0.0) * tl.load(in21_ptr + ((((tl.program_id(0) % 1024) * 1024) + ((_lv0 * 1024) + tl.arange(0, 1024))) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 1024) & True), other=0.0)), 0.0))
    _v = tl.maximum((tl.sum(_acc0, axis=0) + tl.load(in22_ptr + ((tl.program_id(0) % 1024)))), (0.0 * (1.0 / 1.0)))
    tl.store(out_ptr + tl.program_id(0), _v)


def t003_s10(out, ins):
    grid = (1048576,)
    t003_s10_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37], ins[38], ins[39], ins[40], ins[41], ins[42], ins[43], ins[44])
    return out


@triton.jit
def t003_s11_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr, in38_ptr, in39_ptr, in40_ptr, in41_ptr, in42_ptr, in43_ptr, in44_ptr, in45_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 1024) & True), (tl.load(in45_ptr + ((((tl.program_id(0) // 1024) * 1024) + ((_lv0 * 1024) + tl.arange(0, 1024))) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 1024) & True), other=0.0) * tl.load(in23_ptr + ((((tl.program_id(0) % 1024) * 1024) + ((_lv0 * 1024) + tl.arange(0, 1024))) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 1024) & True), other=0.0)), 0.0))
    _v = tl.maximum((tl.sum(_acc0, axis=0) + tl.load(in24_ptr + ((tl.program_id(0) % 1024)))), (0.0 * (1.0 / 1.0)))
    tl.store(out_ptr + tl.program_id(0), _v)


def t003_s11(out, ins):
    grid = (1048576,)
    t003_s11_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37], ins[38], ins[39], ins[40], ins[41], ins[42], ins[43], ins[44], ins[45])
    return out


@triton.jit
def t003_s12_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr, in38_ptr, in39_ptr, in40_ptr, in41_ptr, in42_ptr, in43_ptr, in44_ptr, in45_ptr, in46_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 1024) & True), (tl.load(in46_ptr + ((((tl.program_id(0) // 1024) * 1024) + ((_lv0 * 1024) + tl.arange(0, 1024))) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 1024) & True), other=0.0) * tl.load(in25_ptr + ((((tl.program_id(0) % 1024) * 1024) + ((_lv0 * 1024) + tl.arange(0, 1024))) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 1024) & True), other=0.0)), 0.0))
    _v = tl.maximum((tl.sum(_acc0, axis=0) + tl.load(in26_ptr + ((tl.program_id(0) % 1024)))), (0.0 * (1.0 / 1.0)))
    tl.store(out_ptr + tl.program_id(0), _v)


def t003_s12(out, ins):
    grid = (1048576,)
    t003_s12_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37], ins[38], ins[39], ins[40], ins[41], ins[42], ins[43], ins[44], ins[45], ins[46])
    return out


@triton.jit
def t003_s13_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr, in38_ptr, in39_ptr, in40_ptr, in41_ptr, in42_ptr, in43_ptr, in44_ptr, in45_ptr, in46_ptr, in47_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 1024) & True), (tl.load(in47_ptr + ((((tl.program_id(0) // 1024) * 1024) + ((_lv0 * 1024) + tl.arange(0, 1024))) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 1024) & True), other=0.0) * tl.load(in27_ptr + ((((tl.program_id(0) % 1024) * 1024) + ((_lv0 * 1024) + tl.arange(0, 1024))) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 1024) & True), other=0.0)), 0.0))
    _v = tl.maximum((tl.sum(_acc0, axis=0) + tl.load(in28_ptr + ((tl.program_id(0) % 1024)))), (0.0 * (1.0 / 1.0)))
    tl.store(out_ptr + tl.program_id(0), _v)


def t003_s13(out, ins):
    grid = (1048576,)
    t003_s13_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37], ins[38], ins[39], ins[40], ins[41], ins[42], ins[43], ins[44], ins[45], ins[46], ins[47])
    return out


@triton.jit
def t003_s14_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr, in38_ptr, in39_ptr, in40_ptr, in41_ptr, in42_ptr, in43_ptr, in44_ptr, in45_ptr, in46_ptr, in47_ptr, in48_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 1024) & True), (tl.load(in48_ptr + ((((tl.program_id(0) // 1024) * 1024) + ((_lv0 * 1024) + tl.arange(0, 1024))) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 1024) & True), other=0.0) * tl.load(in29_ptr + ((((tl.program_id(0) % 1024) * 1024) + ((_lv0 * 1024) + tl.arange(0, 1024))) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 1024) & True), other=0.0)), 0.0))
    _v = tl.maximum((tl.sum(_acc0, axis=0) + tl.load(in30_ptr + ((tl.program_id(0) % 1024)))), (0.0 * (1.0 / 1.0)))
    tl.store(out_ptr + tl.program_id(0), _v)


def t003_s14(out, ins):
    grid = (1048576,)
    t003_s14_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37], ins[38], ins[39], ins[40], ins[41], ins[42], ins[43], ins[44], ins[45], ins[46], ins[47], ins[48])
    return out


@triton.jit
def t003_s15_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr, in38_ptr, in39_ptr, in40_ptr, in41_ptr, in42_ptr, in43_ptr, in44_ptr, in45_ptr, in46_ptr, in47_ptr, in48_ptr, in49_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 1024) & True), (tl.load(in49_ptr + ((((tl.program_id(0) // 1024) * 1024) + ((_lv0 * 1024) + tl.arange(0, 1024))) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 1024) & True), other=0.0) * tl.load(in31_ptr + ((((tl.program_id(0) % 1024) * 1024) + ((_lv0 * 1024) + tl.arange(0, 1024))) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 1024) & True), other=0.0)), 0.0))
    _v = tl.maximum((tl.sum(_acc0, axis=0) + tl.load(in32_ptr + ((tl.program_id(0) % 1024)))), (0.0 * (1.0 / 1.0)))
    tl.store(out_ptr + tl.program_id(0), _v)


def t003_s15(out, ins):
    grid = (1048576,)
    t003_s15_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37], ins[38], ins[39], ins[40], ins[41], ins[42], ins[43], ins[44], ins[45], ins[46], ins[47], ins[48], ins[49])
    return out


@triton.jit
def t003_s16_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr, in27_ptr, in28_ptr, in29_ptr, in30_ptr, in31_ptr, in32_ptr, in33_ptr, in34_ptr, in35_ptr, in36_ptr, in37_ptr, in38_ptr, in39_ptr, in40_ptr, in41_ptr, in42_ptr, in43_ptr, in44_ptr, in45_ptr, in46_ptr, in47_ptr, in48_ptr, in49_ptr, in50_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 1024) & True), (tl.load(in50_ptr + ((((tl.program_id(0) // 8192) * 1024) + ((_lv0 * 1024) + tl.arange(0, 1024))) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 1024) & True), other=0.0) * tl.load(in33_ptr + ((((tl.program_id(0) % 8192) * 1024) + ((_lv0 * 1024) + tl.arange(0, 1024))) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 1024) & True), other=0.0)), 0.0))
    _v = (tl.sum(_acc0, axis=0) + tl.load(in34_ptr + ((tl.program_id(0) % 8192))))
    tl.store(out_ptr + tl.program_id(0), _v)


def t003_s16(out, ins):
    grid = (8388608,)
    t003_s16_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26], ins[27], ins[28], ins[29], ins[30], ins[31], ins[32], ins[33], ins[34], ins[35], ins[36], ins[37], ins[38], ins[39], ins[40], ins[41], ins[42], ins[43], ins[44], ins[45], ins[46], ins[47], ins[48], ins[49], ins[50])
    return out


def t003(out, ins):
    _t0 = torch.empty(1048576, device=ins[0].device, dtype=torch.float32)
    _t1 = torch.empty(1048576, device=ins[0].device, dtype=torch.float32)
    _t2 = torch.empty(1048576, device=ins[0].device, dtype=torch.float32)
    _t3 = torch.empty(1048576, device=ins[0].device, dtype=torch.float32)
    _t4 = torch.empty(1048576, device=ins[0].device, dtype=torch.float32)
    _t5 = torch.empty(1048576, device=ins[0].device, dtype=torch.float32)
    _t6 = torch.empty(1048576, device=ins[0].device, dtype=torch.float32)
    _t7 = torch.empty(1048576, device=ins[0].device, dtype=torch.float32)
    _t8 = torch.empty(1048576, device=ins[0].device, dtype=torch.float32)
    _t9 = torch.empty(1048576, device=ins[0].device, dtype=torch.float32)
    _t10 = torch.empty(1048576, device=ins[0].device, dtype=torch.float32)
    _t11 = torch.empty(1048576, device=ins[0].device, dtype=torch.float32)
    _t12 = torch.empty(1048576, device=ins[0].device, dtype=torch.float32)
    _t13 = torch.empty(1048576, device=ins[0].device, dtype=torch.float32)
    _t14 = torch.empty(1048576, device=ins[0].device, dtype=torch.float32)
    _t15 = torch.empty(1048576, device=ins[0].device, dtype=torch.float32)
    t003_s0(_t0, list(ins))
    t003_s1(_t1, list(ins) + [_t0])
    t003_s2(_t2, list(ins) + [_t0, _t1])
    t003_s3(_t3, list(ins) + [_t0, _t1, _t2])
    t003_s4(_t4, list(ins) + [_t0, _t1, _t2, _t3])
    t003_s5(_t5, list(ins) + [_t0, _t1, _t2, _t3, _t4])
    t003_s6(_t6, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5])
    t003_s7(_t7, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6])
    t003_s8(_t8, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7])
    t003_s9(_t9, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8])
    t003_s10(_t10, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9])
    t003_s11(_t11, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10])
    t003_s12(_t12, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11])
    t003_s13(_t13, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12])
    t003_s14(_t14, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13])
    t003_s15(_t15, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13, _t14])
    t003_s16(out, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13, _t14, _t15])
    return out
