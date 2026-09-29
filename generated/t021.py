import torch
import triton
import triton.language as tl


@triton.jit
def _mul_combine(a, b):
    return a * b


@triton.jit
def t021_s0_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr):
    _acc0 = tl.zeros([64], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 64) + tl.arange(0, 64)) < 112) & ((((tl.program_id(0) // 224) % 224) < 224) & ((tl.program_id(0) % 224) < 224))), (tl.load(in0_ptr + ((((((((tl.program_id(0) // 33718272) * 112) + ((_lv0 * 64) + tl.arange(0, 64))) * 224) + ((tl.program_id(0) // 224) % 224)) * 224) + (tl.program_id(0) % 224)) + 0 * tl.arange(0, 64)), mask=((((_lv0 * 64) + tl.arange(0, 64)) < 112) & ((((tl.program_id(0) // 224) % 224) < 224) & ((tl.program_id(0) % 224) < 224))), other=0.0) * tl.load(in1_ptr + (((((tl.program_id(0) // 50176) % 672) * 112) + ((_lv0 * 64) + tl.arange(0, 64))) + 0 * tl.arange(0, 64)), mask=((((_lv0 * 64) + tl.arange(0, 64)) < 112) & ((((tl.program_id(0) // 224) % 224) < 224) & ((tl.program_id(0) % 224) < 224))), other=0.0)), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t021_s0(out, ins):
    grid = (337182720,)
    t021_s0_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9])
    return out


@triton.jit
def t021_s1_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 1960) & ((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) < 501760)), tl.load(in10_ptr + (tl.maximum(((((((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) // 50176) * 672) + (tl.program_id(0) // 256)) * 50176) + ((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) % 50176)) - tl.maximum(((((((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) // 50176) * 672) + (tl.program_id(0) // 256)) * 50176) + ((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) % 50176)) - 337182719, 0), 0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 1960) & ((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) < 501760)), other=0.0), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t021_s1(out, ins):
    grid = (172032,)
    t021_s1_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10])
    return out


@triton.jit
def t021_s2_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr):
    _acc0 = tl.zeros([256], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 256) + tl.arange(0, 256)) < 256) & True), tl.load(in11_ptr + (((tl.program_id(0) * 256) + ((_lv0 * 256) + tl.arange(0, 256))) + 0 * tl.arange(0, 256)), mask=((((_lv0 * 256) + tl.arange(0, 256)) < 256) & True), other=0.0), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t021_s2(out, ins):
    grid = (672,)
    t021_s2_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11])
    return out


@triton.jit
def t021_s3_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 1960) & ((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) < 501760)), ((tl.load(in10_ptr + (tl.maximum(((((((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) // 50176) * 672) + (tl.program_id(0) // 256)) * 50176) + ((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) % 50176)) - tl.maximum(((((((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) // 50176) * 672) + (tl.program_id(0) // 256)) * 50176) + ((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) % 50176)) - 337182719, 0), 0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 1960) & ((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) < 501760)), other=0.0) - (tl.load(in12_ptr + (tl.maximum((tl.program_id(0) // 256) - tl.maximum((tl.program_id(0) // 256) - 671, 0), 0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 1960) & ((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) < 501760)), other=0.0) * (1.0 * (1.0 / 501760.0)))) * (tl.load(in10_ptr + (tl.maximum(((((((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) // 50176) * 672) + (tl.program_id(0) // 256)) * 50176) + ((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) % 50176)) - tl.maximum(((((((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) // 50176) * 672) + (tl.program_id(0) // 256)) * 50176) + ((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) % 50176)) - 337182719, 0), 0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 1960) & ((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) < 501760)), other=0.0) - (tl.load(in12_ptr + (tl.maximum((tl.program_id(0) // 256) - tl.maximum((tl.program_id(0) // 256) - 671, 0), 0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 1960) & ((((tl.program_id(0) % 256) * 1960) + ((_lv0 * 1024) + tl.arange(0, 1024))) < 501760)), other=0.0) * (1.0 * (1.0 / 501760.0))))), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t021_s3(out, ins):
    grid = (172032,)
    t021_s3_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12])
    return out


@triton.jit
def t021_s4_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr):
    _acc0 = tl.zeros([256], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 256) + tl.arange(0, 256)) < 256) & True), tl.load(in13_ptr + (((tl.program_id(0) * 256) + ((_lv0 * 256) + tl.arange(0, 256))) + 0 * tl.arange(0, 256)), mask=((((_lv0 * 256) + tl.arange(0, 256)) < 256) & True), other=0.0), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t021_s4(out, ins):
    grid = (672,)
    t021_s4_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13])
    return out


@triton.jit
def t021_s5_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr):
    _acc0 = tl.zeros([1], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), ((((tl.load(in10_ptr + (tl.program_id(0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) - (tl.load(in12_ptr + (tl.maximum(((tl.program_id(0) // 50176) % 672) - tl.maximum(((tl.program_id(0) // 50176) % 672) - 671, 0), 0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) * (1.0 * (1.0 / 501760.0)))) * (1.0 / tl.sqrt(((tl.load(in14_ptr + (tl.maximum(((tl.program_id(0) // 50176) % 672) - tl.maximum(((tl.program_id(0) // 50176) % 672) - 671, 0), 0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) * (1.0 * (1.0 / 501760.0))) + (1.0 * (1.0 / 100000.0)))))) * tl.load(in2_ptr + (((tl.program_id(0) // 50176) % 672) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)) + tl.load(in3_ptr + (((tl.program_id(0) // 50176) % 672) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)), 0.0))
    _v = tl.minimum(tl.maximum(tl.sum(_acc0, axis=0), (0.0 * (1.0 / 1.0))), (6.0 * (1.0 / 1.0)))
    tl.store(out_ptr + tl.program_id(0), _v)


def t021_s5(out, ins):
    grid = (337182720,)
    t021_s5_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14])
    return out


@triton.jit
def t021_s6_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr):
    _acc0 = tl.zeros([16], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 16) + tl.arange(0, 16)) < 25) & ((((2 <= ((((tl.program_id(0) // 112) % 112) * 2) + ((((_lv0 * 16) + tl.arange(0, 16)) // 5) % 5))) & (((((tl.program_id(0) // 112) % 112) * 2) + ((((_lv0 * 16) + tl.arange(0, 16)) // 5) % 5)) < 226)) & (2 <= (((tl.program_id(0) % 112) * 2) + (((_lv0 * 16) + tl.arange(0, 16)) % 5)))) & ((((tl.program_id(0) % 112) * 2) + (((_lv0 * 16) + tl.arange(0, 16)) % 5)) < 226))), (tl.load(in15_ptr + (tl.maximum((((((((tl.program_id(0) // 8429568) * 672) + ((tl.program_id(0) // 12544) % 672)) * 224) + tl.maximum(((((tl.program_id(0) // 112) % 112) * 2) + ((((_lv0 * 16) + tl.arange(0, 16)) // 5) % 5)) - 2, 0)) * 224) + tl.maximum((((tl.program_id(0) % 112) * 2) + (((_lv0 * 16) + tl.arange(0, 16)) % 5)) - 2, 0)) - tl.maximum((((((((tl.program_id(0) // 8429568) * 672) + ((tl.program_id(0) // 12544) % 672)) * 224) + tl.maximum(((((tl.program_id(0) // 112) % 112) * 2) + ((((_lv0 * 16) + tl.arange(0, 16)) // 5) % 5)) - 2, 0)) * 224) + tl.maximum((((tl.program_id(0) % 112) * 2) + (((_lv0 * 16) + tl.arange(0, 16)) % 5)) - 2, 0)) - 337182719, 0), 0) + 0 * tl.arange(0, 16)), mask=((((_lv0 * 16) + tl.arange(0, 16)) < 25) & ((((2 <= ((((tl.program_id(0) // 112) % 112) * 2) + ((((_lv0 * 16) + tl.arange(0, 16)) // 5) % 5))) & (((((tl.program_id(0) // 112) % 112) * 2) + ((((_lv0 * 16) + tl.arange(0, 16)) // 5) % 5)) < 226)) & (2 <= (((tl.program_id(0) % 112) * 2) + (((_lv0 * 16) + tl.arange(0, 16)) % 5)))) & ((((tl.program_id(0) % 112) * 2) + (((_lv0 * 16) + tl.arange(0, 16)) % 5)) < 226))), other=0.0) * tl.load(in4_ptr + (((((((tl.program_id(0) // 12544) % 672) * 5) + ((((_lv0 * 16) + tl.arange(0, 16)) // 5) % 5)) * 5) + (((_lv0 * 16) + tl.arange(0, 16)) % 5)) + 0 * tl.arange(0, 16)), mask=((((_lv0 * 16) + tl.arange(0, 16)) < 25) & ((((2 <= ((((tl.program_id(0) // 112) % 112) * 2) + ((((_lv0 * 16) + tl.arange(0, 16)) // 5) % 5))) & (((((tl.program_id(0) // 112) % 112) * 2) + ((((_lv0 * 16) + tl.arange(0, 16)) // 5) % 5)) < 226)) & (2 <= (((tl.program_id(0) % 112) * 2) + (((_lv0 * 16) + tl.arange(0, 16)) % 5)))) & ((((tl.program_id(0) % 112) * 2) + (((_lv0 * 16) + tl.arange(0, 16)) % 5)) < 226))), other=0.0)), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t021_s6(out, ins):
    grid = (84295680,)
    t021_s6_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15])
    return out


@triton.jit
def t021_s7_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr):
    _acc0 = tl.zeros([256], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 256) + tl.arange(0, 256)) < 490) & ((((tl.program_id(0) % 256) * 490) + ((_lv0 * 256) + tl.arange(0, 256))) < 125440)), tl.load(in16_ptr + (tl.maximum(((((((((tl.program_id(0) % 256) * 490) + ((_lv0 * 256) + tl.arange(0, 256))) // 12544) * 672) + (tl.program_id(0) // 256)) * 12544) + ((((tl.program_id(0) % 256) * 490) + ((_lv0 * 256) + tl.arange(0, 256))) % 12544)) - tl.maximum(((((((((tl.program_id(0) % 256) * 490) + ((_lv0 * 256) + tl.arange(0, 256))) // 12544) * 672) + (tl.program_id(0) // 256)) * 12544) + ((((tl.program_id(0) % 256) * 490) + ((_lv0 * 256) + tl.arange(0, 256))) % 12544)) - 84295679, 0), 0) + 0 * tl.arange(0, 256)), mask=((((_lv0 * 256) + tl.arange(0, 256)) < 490) & ((((tl.program_id(0) % 256) * 490) + ((_lv0 * 256) + tl.arange(0, 256))) < 125440)), other=0.0), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t021_s7(out, ins):
    grid = (172032,)
    t021_s7_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16])
    return out


@triton.jit
def t021_s8_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr):
    _acc0 = tl.zeros([256], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 256) + tl.arange(0, 256)) < 256) & True), tl.load(in17_ptr + (((tl.program_id(0) * 256) + ((_lv0 * 256) + tl.arange(0, 256))) + 0 * tl.arange(0, 256)), mask=((((_lv0 * 256) + tl.arange(0, 256)) < 256) & True), other=0.0), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t021_s8(out, ins):
    grid = (672,)
    t021_s8_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17])
    return out


@triton.jit
def t021_s9_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr):
    _acc0 = tl.zeros([256], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 256) + tl.arange(0, 256)) < 490) & ((((tl.program_id(0) % 256) * 490) + ((_lv0 * 256) + tl.arange(0, 256))) < 125440)), ((tl.load(in16_ptr + (tl.maximum(((((((((tl.program_id(0) % 256) * 490) + ((_lv0 * 256) + tl.arange(0, 256))) // 12544) * 672) + (tl.program_id(0) // 256)) * 12544) + ((((tl.program_id(0) % 256) * 490) + ((_lv0 * 256) + tl.arange(0, 256))) % 12544)) - tl.maximum(((((((((tl.program_id(0) % 256) * 490) + ((_lv0 * 256) + tl.arange(0, 256))) // 12544) * 672) + (tl.program_id(0) // 256)) * 12544) + ((((tl.program_id(0) % 256) * 490) + ((_lv0 * 256) + tl.arange(0, 256))) % 12544)) - 84295679, 0), 0) + 0 * tl.arange(0, 256)), mask=((((_lv0 * 256) + tl.arange(0, 256)) < 490) & ((((tl.program_id(0) % 256) * 490) + ((_lv0 * 256) + tl.arange(0, 256))) < 125440)), other=0.0) - (tl.load(in18_ptr + (tl.maximum((tl.program_id(0) // 256) - tl.maximum((tl.program_id(0) // 256) - 671, 0), 0) + 0 * tl.arange(0, 256)), mask=((((_lv0 * 256) + tl.arange(0, 256)) < 490) & ((((tl.program_id(0) % 256) * 490) + ((_lv0 * 256) + tl.arange(0, 256))) < 125440)), other=0.0) * (1.0 * (1.0 / 125440.0)))) * (tl.load(in16_ptr + (tl.maximum(((((((((tl.program_id(0) % 256) * 490) + ((_lv0 * 256) + tl.arange(0, 256))) // 12544) * 672) + (tl.program_id(0) // 256)) * 12544) + ((((tl.program_id(0) % 256) * 490) + ((_lv0 * 256) + tl.arange(0, 256))) % 12544)) - tl.maximum(((((((((tl.program_id(0) % 256) * 490) + ((_lv0 * 256) + tl.arange(0, 256))) // 12544) * 672) + (tl.program_id(0) // 256)) * 12544) + ((((tl.program_id(0) % 256) * 490) + ((_lv0 * 256) + tl.arange(0, 256))) % 12544)) - 84295679, 0), 0) + 0 * tl.arange(0, 256)), mask=((((_lv0 * 256) + tl.arange(0, 256)) < 490) & ((((tl.program_id(0) % 256) * 490) + ((_lv0 * 256) + tl.arange(0, 256))) < 125440)), other=0.0) - (tl.load(in18_ptr + (tl.maximum((tl.program_id(0) // 256) - tl.maximum((tl.program_id(0) // 256) - 671, 0), 0) + 0 * tl.arange(0, 256)), mask=((((_lv0 * 256) + tl.arange(0, 256)) < 490) & ((((tl.program_id(0) % 256) * 490) + ((_lv0 * 256) + tl.arange(0, 256))) < 125440)), other=0.0) * (1.0 * (1.0 / 125440.0))))), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t021_s9(out, ins):
    grid = (172032,)
    t021_s9_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18])
    return out


@triton.jit
def t021_s10_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr):
    _acc0 = tl.zeros([256], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 256) + tl.arange(0, 256)) < 256) & True), tl.load(in19_ptr + (((tl.program_id(0) * 256) + ((_lv0 * 256) + tl.arange(0, 256))) + 0 * tl.arange(0, 256)), mask=((((_lv0 * 256) + tl.arange(0, 256)) < 256) & True), other=0.0), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t021_s10(out, ins):
    grid = (672,)
    t021_s10_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19])
    return out


@triton.jit
def t021_s11_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr):
    _acc0 = tl.zeros([1], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), ((((tl.load(in16_ptr + (tl.program_id(0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) - (tl.load(in18_ptr + (tl.maximum(((tl.program_id(0) // 12544) % 672) - tl.maximum(((tl.program_id(0) // 12544) % 672) - 671, 0), 0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) * (1.0 * (1.0 / 125440.0)))) * (1.0 / tl.sqrt(((tl.load(in20_ptr + (tl.maximum(((tl.program_id(0) // 12544) % 672) - tl.maximum(((tl.program_id(0) // 12544) % 672) - 671, 0), 0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) * (1.0 * (1.0 / 125440.0))) + (1.0 * (1.0 / 100000.0)))))) * tl.load(in5_ptr + (((tl.program_id(0) // 12544) % 672) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)) + tl.load(in6_ptr + (((tl.program_id(0) // 12544) % 672) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)), 0.0))
    _v = tl.minimum(tl.maximum(tl.sum(_acc0, axis=0), (0.0 * (1.0 / 1.0))), (6.0 * (1.0 / 1.0)))
    tl.store(out_ptr + tl.program_id(0), _v)


def t021_s11(out, ins):
    grid = (84295680,)
    t021_s11_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20])
    return out


@triton.jit
def t021_s12_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr):
    _acc0 = tl.zeros([512], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 512) + tl.arange(0, 512)) < 672) & ((((tl.program_id(0) // 112) % 112) < 112) & ((tl.program_id(0) % 112) < 112))), (tl.load(in21_ptr + ((((((((tl.program_id(0) // 2408448) * 672) + ((_lv0 * 512) + tl.arange(0, 512))) * 112) + ((tl.program_id(0) // 112) % 112)) * 112) + (tl.program_id(0) % 112)) + 0 * tl.arange(0, 512)), mask=((((_lv0 * 512) + tl.arange(0, 512)) < 672) & ((((tl.program_id(0) // 112) % 112) < 112) & ((tl.program_id(0) % 112) < 112))), other=0.0) * tl.load(in7_ptr + (((((tl.program_id(0) // 12544) % 192) * 672) + ((_lv0 * 512) + tl.arange(0, 512))) + 0 * tl.arange(0, 512)), mask=((((_lv0 * 512) + tl.arange(0, 512)) < 672) & ((((tl.program_id(0) // 112) % 112) < 112) & ((tl.program_id(0) % 112) < 112))), other=0.0)), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t021_s12(out, ins):
    grid = (24084480,)
    t021_s12_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21])
    return out


@triton.jit
def t021_s13_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr):
    _acc0 = tl.zeros([256], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 256) + tl.arange(0, 256)) < 490) & ((((tl.program_id(0) % 256) * 490) + ((_lv0 * 256) + tl.arange(0, 256))) < 125440)), tl.load(in22_ptr + (tl.maximum(((((((((tl.program_id(0) % 256) * 490) + ((_lv0 * 256) + tl.arange(0, 256))) // 12544) * 192) + (tl.program_id(0) // 256)) * 12544) + ((((tl.program_id(0) % 256) * 490) + ((_lv0 * 256) + tl.arange(0, 256))) % 12544)) - tl.maximum(((((((((tl.program_id(0) % 256) * 490) + ((_lv0 * 256) + tl.arange(0, 256))) // 12544) * 192) + (tl.program_id(0) // 256)) * 12544) + ((((tl.program_id(0) % 256) * 490) + ((_lv0 * 256) + tl.arange(0, 256))) % 12544)) - 24084479, 0), 0) + 0 * tl.arange(0, 256)), mask=((((_lv0 * 256) + tl.arange(0, 256)) < 490) & ((((tl.program_id(0) % 256) * 490) + ((_lv0 * 256) + tl.arange(0, 256))) < 125440)), other=0.0), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t021_s13(out, ins):
    grid = (49152,)
    t021_s13_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22])
    return out


@triton.jit
def t021_s14_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr):
    _acc0 = tl.zeros([256], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 256) + tl.arange(0, 256)) < 256) & True), tl.load(in23_ptr + (((tl.program_id(0) * 256) + ((_lv0 * 256) + tl.arange(0, 256))) + 0 * tl.arange(0, 256)), mask=((((_lv0 * 256) + tl.arange(0, 256)) < 256) & True), other=0.0), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t021_s14(out, ins):
    grid = (192,)
    t021_s14_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23])
    return out


@triton.jit
def t021_s15_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr):
    _acc0 = tl.zeros([256], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 256) + tl.arange(0, 256)) < 490) & ((((tl.program_id(0) % 256) * 490) + ((_lv0 * 256) + tl.arange(0, 256))) < 125440)), ((tl.load(in22_ptr + (tl.maximum(((((((((tl.program_id(0) % 256) * 490) + ((_lv0 * 256) + tl.arange(0, 256))) // 12544) * 192) + (tl.program_id(0) // 256)) * 12544) + ((((tl.program_id(0) % 256) * 490) + ((_lv0 * 256) + tl.arange(0, 256))) % 12544)) - tl.maximum(((((((((tl.program_id(0) % 256) * 490) + ((_lv0 * 256) + tl.arange(0, 256))) // 12544) * 192) + (tl.program_id(0) // 256)) * 12544) + ((((tl.program_id(0) % 256) * 490) + ((_lv0 * 256) + tl.arange(0, 256))) % 12544)) - 24084479, 0), 0) + 0 * tl.arange(0, 256)), mask=((((_lv0 * 256) + tl.arange(0, 256)) < 490) & ((((tl.program_id(0) % 256) * 490) + ((_lv0 * 256) + tl.arange(0, 256))) < 125440)), other=0.0) - (tl.load(in24_ptr + (tl.maximum((tl.program_id(0) // 256) - tl.maximum((tl.program_id(0) // 256) - 191, 0), 0) + 0 * tl.arange(0, 256)), mask=((((_lv0 * 256) + tl.arange(0, 256)) < 490) & ((((tl.program_id(0) % 256) * 490) + ((_lv0 * 256) + tl.arange(0, 256))) < 125440)), other=0.0) * (1.0 * (1.0 / 125440.0)))) * (tl.load(in22_ptr + (tl.maximum(((((((((tl.program_id(0) % 256) * 490) + ((_lv0 * 256) + tl.arange(0, 256))) // 12544) * 192) + (tl.program_id(0) // 256)) * 12544) + ((((tl.program_id(0) % 256) * 490) + ((_lv0 * 256) + tl.arange(0, 256))) % 12544)) - tl.maximum(((((((((tl.program_id(0) % 256) * 490) + ((_lv0 * 256) + tl.arange(0, 256))) // 12544) * 192) + (tl.program_id(0) // 256)) * 12544) + ((((tl.program_id(0) % 256) * 490) + ((_lv0 * 256) + tl.arange(0, 256))) % 12544)) - 24084479, 0), 0) + 0 * tl.arange(0, 256)), mask=((((_lv0 * 256) + tl.arange(0, 256)) < 490) & ((((tl.program_id(0) % 256) * 490) + ((_lv0 * 256) + tl.arange(0, 256))) < 125440)), other=0.0) - (tl.load(in24_ptr + (tl.maximum((tl.program_id(0) // 256) - tl.maximum((tl.program_id(0) // 256) - 191, 0), 0) + 0 * tl.arange(0, 256)), mask=((((_lv0 * 256) + tl.arange(0, 256)) < 490) & ((((tl.program_id(0) % 256) * 490) + ((_lv0 * 256) + tl.arange(0, 256))) < 125440)), other=0.0) * (1.0 * (1.0 / 125440.0))))), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t021_s15(out, ins):
    grid = (49152,)
    t021_s15_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24])
    return out


@triton.jit
def t021_s16_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr):
    _acc0 = tl.zeros([256], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 256) + tl.arange(0, 256)) < 256) & True), tl.load(in25_ptr + (((tl.program_id(0) * 256) + ((_lv0 * 256) + tl.arange(0, 256))) + 0 * tl.arange(0, 256)), mask=((((_lv0 * 256) + tl.arange(0, 256)) < 256) & True), other=0.0), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t021_s16(out, ins):
    grid = (192,)
    t021_s16_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25])
    return out


@triton.jit
def t021_s17_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr):
    _acc0 = tl.zeros([1], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), ((((tl.load(in22_ptr + (tl.program_id(0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) - (tl.load(in24_ptr + (tl.maximum(((tl.program_id(0) // 12544) % 192) - tl.maximum(((tl.program_id(0) // 12544) % 192) - 191, 0), 0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) * (1.0 * (1.0 / 125440.0)))) * (1.0 / tl.sqrt(((tl.load(in26_ptr + (tl.maximum(((tl.program_id(0) // 12544) % 192) - tl.maximum(((tl.program_id(0) // 12544) % 192) - 191, 0), 0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) * (1.0 * (1.0 / 125440.0))) + (1.0 * (1.0 / 100000.0)))))) * tl.load(in8_ptr + (((tl.program_id(0) // 12544) % 192) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)) + tl.load(in9_ptr + (((tl.program_id(0) // 12544) % 192) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t021_s17(out, ins):
    grid = (24084480,)
    t021_s17_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26])
    return out


def t021(out, ins):
    _t0 = torch.empty(337182720, device=ins[0].device, dtype=torch.float32)
    _t1 = torch.empty(172032, device=ins[0].device, dtype=torch.float32)
    _t2 = torch.empty(672, device=ins[0].device, dtype=torch.float32)
    _t3 = torch.empty(172032, device=ins[0].device, dtype=torch.float32)
    _t4 = torch.empty(672, device=ins[0].device, dtype=torch.float32)
    _t5 = torch.empty(337182720, device=ins[0].device, dtype=torch.float32)
    _t6 = torch.empty(84295680, device=ins[0].device, dtype=torch.float32)
    _t7 = torch.empty(172032, device=ins[0].device, dtype=torch.float32)
    _t8 = torch.empty(672, device=ins[0].device, dtype=torch.float32)
    _t9 = torch.empty(172032, device=ins[0].device, dtype=torch.float32)
    _t10 = torch.empty(672, device=ins[0].device, dtype=torch.float32)
    _t11 = torch.empty(84295680, device=ins[0].device, dtype=torch.float32)
    _t12 = torch.empty(24084480, device=ins[0].device, dtype=torch.float32)
    _t13 = torch.empty(49152, device=ins[0].device, dtype=torch.float32)
    _t14 = torch.empty(192, device=ins[0].device, dtype=torch.float32)
    _t15 = torch.empty(49152, device=ins[0].device, dtype=torch.float32)
    _t16 = torch.empty(192, device=ins[0].device, dtype=torch.float32)
    t021_s0(_t0, list(ins))
    t021_s1(_t1, list(ins) + [_t0])
    t021_s2(_t2, list(ins) + [_t0, _t1])
    t021_s3(_t3, list(ins) + [_t0, _t1, _t2])
    t021_s4(_t4, list(ins) + [_t0, _t1, _t2, _t3])
    t021_s5(_t5, list(ins) + [_t0, _t1, _t2, _t3, _t4])
    t021_s6(_t6, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5])
    t021_s7(_t7, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6])
    t021_s8(_t8, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7])
    t021_s9(_t9, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8])
    t021_s10(_t10, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9])
    t021_s11(_t11, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10])
    t021_s12(_t12, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11])
    t021_s13(_t13, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12])
    t021_s14(_t14, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13])
    t021_s15(_t15, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13, _t14])
    t021_s16(_t16, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13, _t14, _t15])
    t021_s17(out, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9, _t10, _t11, _t12, _t13, _t14, _t15, _t16])
    return out
