import torch
import triton
import triton.language as tl


@triton.jit
def _mul_combine(a, b):
    return a * b


@triton.jit
def t005_s0_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr):
    _acc0 = tl.zeros([256], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 256) + tl.arange(0, 256)) < 363) & ((((2 <= ((((tl.program_id(0) // 55) % 55) * 4) + ((((_lv0 * 256) + tl.arange(0, 256)) // 11) % 11))) & (((((tl.program_id(0) // 55) % 55) * 4) + ((((_lv0 * 256) + tl.arange(0, 256)) // 11) % 11)) < 226)) & (2 <= (((tl.program_id(0) % 55) * 4) + (((_lv0 * 256) + tl.arange(0, 256)) % 11)))) & ((((tl.program_id(0) % 55) * 4) + (((_lv0 * 256) + tl.arange(0, 256)) % 11)) < 226))), (tl.load(in0_ptr + ((((((((tl.program_id(0) // 290400) * 3) + (((_lv0 * 256) + tl.arange(0, 256)) // 121)) * 224) + tl.maximum(((((tl.program_id(0) // 55) % 55) * 4) + ((((_lv0 * 256) + tl.arange(0, 256)) // 11) % 11)) - 2, 0)) * 224) + tl.maximum((((tl.program_id(0) % 55) * 4) + (((_lv0 * 256) + tl.arange(0, 256)) % 11)) - 2, 0)) + 0 * tl.arange(0, 256)), mask=((((_lv0 * 256) + tl.arange(0, 256)) < 363) & ((((2 <= ((((tl.program_id(0) // 55) % 55) * 4) + ((((_lv0 * 256) + tl.arange(0, 256)) // 11) % 11))) & (((((tl.program_id(0) // 55) % 55) * 4) + ((((_lv0 * 256) + tl.arange(0, 256)) // 11) % 11)) < 226)) & (2 <= (((tl.program_id(0) % 55) * 4) + (((_lv0 * 256) + tl.arange(0, 256)) % 11)))) & ((((tl.program_id(0) % 55) * 4) + (((_lv0 * 256) + tl.arange(0, 256)) % 11)) < 226))), other=0.0) * tl.load(in1_ptr + (((((((((tl.program_id(0) // 3025) % 96) * 3) + (((_lv0 * 256) + tl.arange(0, 256)) // 121)) * 11) + ((((_lv0 * 256) + tl.arange(0, 256)) // 11) % 11)) * 11) + (((_lv0 * 256) + tl.arange(0, 256)) % 11)) + 0 * tl.arange(0, 256)), mask=((((_lv0 * 256) + tl.arange(0, 256)) < 363) & ((((2 <= ((((tl.program_id(0) // 55) % 55) * 4) + ((((_lv0 * 256) + tl.arange(0, 256)) // 11) % 11))) & (((((tl.program_id(0) // 55) % 55) * 4) + ((((_lv0 * 256) + tl.arange(0, 256)) // 11) % 11)) < 226)) & (2 <= (((tl.program_id(0) % 55) * 4) + (((_lv0 * 256) + tl.arange(0, 256)) % 11)))) & ((((tl.program_id(0) % 55) * 4) + (((_lv0 * 256) + tl.arange(0, 256)) % 11)) < 226))), other=0.0)), 0.0))
    _v = tl.maximum((tl.sum(_acc0, axis=0) + tl.load(in2_ptr + (((tl.program_id(0) // 3025) % 96)))), (0.0 * (1.0 / 1.0)))
    tl.store(out_ptr + tl.program_id(0), _v)


def t005_s0(out, ins):
    grid = (297369600,)
    t005_s0_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16])
    return out


@triton.jit
def t005_s1_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr):
    _acc0 = tl.zeros([8], dtype=tl.float32) + (tl.load(in17_ptr + ((((((((tl.program_id(0) // 69984) * 96) + ((tl.program_id(0) // 729) % 96)) * 55) + tl.maximum(((((tl.program_id(0) // 27) % 27) * 2) + tl.maximum(((0 // 3) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 27) % 27) * 2), 0) - (0 // 3), 0)) - tl.maximum(((0 // 3) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 27) % 27) * 2), 0) - (0 // 3), 0)) - tl.maximum(54 - (((tl.program_id(0) // 27) % 27) * 2), 0), 0), 0)) - tl.maximum(((((tl.program_id(0) // 27) % 27) * 2) + tl.maximum(((0 // 3) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 27) % 27) * 2), 0) - (0 // 3), 0)) - tl.maximum(((0 // 3) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 27) % 27) * 2), 0) - (0 // 3), 0)) - tl.maximum(54 - (((tl.program_id(0) // 27) % 27) * 2), 0), 0), 0)) - 54, 0), 0)) * 55) + tl.maximum((((tl.program_id(0) % 27) * 2) + tl.maximum(((0 % 3) + tl.maximum(tl.maximum(0 - ((tl.program_id(0) % 27) * 2), 0) - (0 % 3), 0)) - tl.maximum(((0 % 3) + tl.maximum(tl.maximum(0 - ((tl.program_id(0) % 27) * 2), 0) - (0 % 3), 0)) - tl.maximum(54 - ((tl.program_id(0) % 27) * 2), 0), 0), 0)) - tl.maximum((((tl.program_id(0) % 27) * 2) + tl.maximum(((0 % 3) + tl.maximum(tl.maximum(0 - ((tl.program_id(0) % 27) * 2), 0) - (0 % 3), 0)) - tl.maximum(((0 % 3) + tl.maximum(tl.maximum(0 - ((tl.program_id(0) % 27) * 2), 0) - (0 % 3), 0)) - tl.maximum(54 - ((tl.program_id(0) % 27) * 2), 0), 0), 0)) - 54, 0), 0)))))
    for _lv0 in range(0, 2):
        _acc0 = tl.maximum(_acc0, tl.load(in17_ptr + ((((((((tl.program_id(0) // 69984) * 96) + ((tl.program_id(0) // 729) % 96)) * 55) + tl.maximum(((((tl.program_id(0) // 27) % 27) * 2) + tl.maximum(((tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 8, 0), 0) // 3) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 27) % 27) * 2), 0) - (tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 8, 0), 0) // 3), 0)) - tl.maximum(((tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 8, 0), 0) // 3) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 27) % 27) * 2), 0) - (tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 8, 0), 0) // 3), 0)) - tl.maximum(54 - (((tl.program_id(0) // 27) % 27) * 2), 0), 0), 0)) - tl.maximum(((((tl.program_id(0) // 27) % 27) * 2) + tl.maximum(((tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 8, 0), 0) // 3) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 27) % 27) * 2), 0) - (tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 8, 0), 0) // 3), 0)) - tl.maximum(((tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 8, 0), 0) // 3) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 27) % 27) * 2), 0) - (tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 8, 0), 0) // 3), 0)) - tl.maximum(54 - (((tl.program_id(0) // 27) % 27) * 2), 0), 0), 0)) - 54, 0), 0)) * 55) + tl.maximum((((tl.program_id(0) % 27) * 2) + tl.maximum(((tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 8, 0), 0) % 3) + tl.maximum(tl.maximum(0 - ((tl.program_id(0) % 27) * 2), 0) - (tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 8, 0), 0) % 3), 0)) - tl.maximum(((tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 8, 0), 0) % 3) + tl.maximum(tl.maximum(0 - ((tl.program_id(0) % 27) * 2), 0) - (tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 8, 0), 0) % 3), 0)) - tl.maximum(54 - ((tl.program_id(0) % 27) * 2), 0), 0), 0)) - tl.maximum((((tl.program_id(0) % 27) * 2) + tl.maximum(((tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 8, 0), 0) % 3) + tl.maximum(tl.maximum(0 - ((tl.program_id(0) % 27) * 2), 0) - (tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 8, 0), 0) % 3), 0)) - tl.maximum(((tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 8, 0), 0) % 3) + tl.maximum(tl.maximum(0 - ((tl.program_id(0) % 27) * 2), 0) - (tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 8, 0), 0) % 3), 0)) - tl.maximum(54 - ((tl.program_id(0) % 27) * 2), 0), 0), 0)) - 54, 0), 0)))))
    _v = tl.max(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t005_s1(out, ins):
    grid = (71663616,)
    t005_s1_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17])
    return out


@triton.jit
def t005_s2_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 3):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 2400) & ((((2 <= (((tl.program_id(0) // 27) % 27) + ((((_lv0 * 1024) + tl.arange(0, 1024)) // 5) % 5))) & ((((tl.program_id(0) // 27) % 27) + ((((_lv0 * 1024) + tl.arange(0, 1024)) // 5) % 5)) < 29)) & (2 <= ((tl.program_id(0) % 27) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 5)))) & (((tl.program_id(0) % 27) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 5)) < 29))), (tl.load(in18_ptr + (tl.maximum((((((((tl.program_id(0) // 186624) * 96) + (((_lv0 * 1024) + tl.arange(0, 1024)) // 25)) * 27) + tl.maximum((((tl.program_id(0) // 27) % 27) + ((((_lv0 * 1024) + tl.arange(0, 1024)) // 5) % 5)) - 2, 0)) * 27) + tl.maximum(((tl.program_id(0) % 27) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 5)) - 2, 0)) - tl.maximum((((((((tl.program_id(0) // 186624) * 96) + (((_lv0 * 1024) + tl.arange(0, 1024)) // 25)) * 27) + tl.maximum((((tl.program_id(0) // 27) % 27) + ((((_lv0 * 1024) + tl.arange(0, 1024)) // 5) % 5)) - 2, 0)) * 27) + tl.maximum(((tl.program_id(0) % 27) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 5)) - 2, 0)) - 71663615, 0), 0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 2400) & ((((2 <= (((tl.program_id(0) // 27) % 27) + ((((_lv0 * 1024) + tl.arange(0, 1024)) // 5) % 5))) & ((((tl.program_id(0) // 27) % 27) + ((((_lv0 * 1024) + tl.arange(0, 1024)) // 5) % 5)) < 29)) & (2 <= ((tl.program_id(0) % 27) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 5)))) & (((tl.program_id(0) % 27) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 5)) < 29))), other=0.0) * tl.load(in3_ptr + (((((((((tl.program_id(0) // 729) % 256) * 96) + (((_lv0 * 1024) + tl.arange(0, 1024)) // 25)) * 5) + ((((_lv0 * 1024) + tl.arange(0, 1024)) // 5) % 5)) * 5) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 5)) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 2400) & ((((2 <= (((tl.program_id(0) // 27) % 27) + ((((_lv0 * 1024) + tl.arange(0, 1024)) // 5) % 5))) & ((((tl.program_id(0) // 27) % 27) + ((((_lv0 * 1024) + tl.arange(0, 1024)) // 5) % 5)) < 29)) & (2 <= ((tl.program_id(0) % 27) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 5)))) & (((tl.program_id(0) % 27) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 5)) < 29))), other=0.0)), 0.0))
    _v = tl.maximum((tl.sum(_acc0, axis=0) + tl.load(in4_ptr + (((tl.program_id(0) // 729) % 256)))), (0.0 * (1.0 / 1.0)))
    tl.store(out_ptr + tl.program_id(0), _v)


def t005_s2(out, ins):
    grid = (191102976,)
    t005_s2_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18])
    return out


@triton.jit
def t005_s3_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr):
    _acc0 = tl.zeros([8], dtype=tl.float32) + (tl.load(in19_ptr + ((((((((tl.program_id(0) // 43264) * 256) + ((tl.program_id(0) // 169) % 256)) * 27) + tl.maximum(((((tl.program_id(0) // 13) % 13) * 2) + tl.maximum(((0 // 3) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 13) % 13) * 2), 0) - (0 // 3), 0)) - tl.maximum(((0 // 3) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 13) % 13) * 2), 0) - (0 // 3), 0)) - tl.maximum(26 - (((tl.program_id(0) // 13) % 13) * 2), 0), 0), 0)) - tl.maximum(((((tl.program_id(0) // 13) % 13) * 2) + tl.maximum(((0 // 3) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 13) % 13) * 2), 0) - (0 // 3), 0)) - tl.maximum(((0 // 3) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 13) % 13) * 2), 0) - (0 // 3), 0)) - tl.maximum(26 - (((tl.program_id(0) // 13) % 13) * 2), 0), 0), 0)) - 26, 0), 0)) * 27) + tl.maximum((((tl.program_id(0) % 13) * 2) + tl.maximum(((0 % 3) + tl.maximum(tl.maximum(0 - ((tl.program_id(0) % 13) * 2), 0) - (0 % 3), 0)) - tl.maximum(((0 % 3) + tl.maximum(tl.maximum(0 - ((tl.program_id(0) % 13) * 2), 0) - (0 % 3), 0)) - tl.maximum(26 - ((tl.program_id(0) % 13) * 2), 0), 0), 0)) - tl.maximum((((tl.program_id(0) % 13) * 2) + tl.maximum(((0 % 3) + tl.maximum(tl.maximum(0 - ((tl.program_id(0) % 13) * 2), 0) - (0 % 3), 0)) - tl.maximum(((0 % 3) + tl.maximum(tl.maximum(0 - ((tl.program_id(0) % 13) * 2), 0) - (0 % 3), 0)) - tl.maximum(26 - ((tl.program_id(0) % 13) * 2), 0), 0), 0)) - 26, 0), 0)))))
    for _lv0 in range(0, 2):
        _acc0 = tl.maximum(_acc0, tl.load(in19_ptr + ((((((((tl.program_id(0) // 43264) * 256) + ((tl.program_id(0) // 169) % 256)) * 27) + tl.maximum(((((tl.program_id(0) // 13) % 13) * 2) + tl.maximum(((tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 8, 0), 0) // 3) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 13) % 13) * 2), 0) - (tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 8, 0), 0) // 3), 0)) - tl.maximum(((tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 8, 0), 0) // 3) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 13) % 13) * 2), 0) - (tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 8, 0), 0) // 3), 0)) - tl.maximum(26 - (((tl.program_id(0) // 13) % 13) * 2), 0), 0), 0)) - tl.maximum(((((tl.program_id(0) // 13) % 13) * 2) + tl.maximum(((tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 8, 0), 0) // 3) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 13) % 13) * 2), 0) - (tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 8, 0), 0) // 3), 0)) - tl.maximum(((tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 8, 0), 0) // 3) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 13) % 13) * 2), 0) - (tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 8, 0), 0) // 3), 0)) - tl.maximum(26 - (((tl.program_id(0) // 13) % 13) * 2), 0), 0), 0)) - 26, 0), 0)) * 27) + tl.maximum((((tl.program_id(0) % 13) * 2) + tl.maximum(((tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 8, 0), 0) % 3) + tl.maximum(tl.maximum(0 - ((tl.program_id(0) % 13) * 2), 0) - (tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 8, 0), 0) % 3), 0)) - tl.maximum(((tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 8, 0), 0) % 3) + tl.maximum(tl.maximum(0 - ((tl.program_id(0) % 13) * 2), 0) - (tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 8, 0), 0) % 3), 0)) - tl.maximum(26 - ((tl.program_id(0) % 13) * 2), 0), 0), 0)) - tl.maximum((((tl.program_id(0) % 13) * 2) + tl.maximum(((tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 8, 0), 0) % 3) + tl.maximum(tl.maximum(0 - ((tl.program_id(0) % 13) * 2), 0) - (tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 8, 0), 0) % 3), 0)) - tl.maximum(((tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 8, 0), 0) % 3) + tl.maximum(tl.maximum(0 - ((tl.program_id(0) % 13) * 2), 0) - (tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 8, 0), 0) % 3), 0)) - tl.maximum(26 - ((tl.program_id(0) % 13) * 2), 0), 0), 0)) - 26, 0), 0)))))
    _v = tl.max(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t005_s3(out, ins):
    grid = (44302336,)
    t005_s3_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19])
    return out


@triton.jit
def t005_s4_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 3):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 2304) & ((((1 <= (((tl.program_id(0) // 13) % 13) + ((((_lv0 * 1024) + tl.arange(0, 1024)) // 3) % 3))) & ((((tl.program_id(0) // 13) % 13) + ((((_lv0 * 1024) + tl.arange(0, 1024)) // 3) % 3)) < 14)) & (1 <= ((tl.program_id(0) % 13) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 3)))) & (((tl.program_id(0) % 13) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 3)) < 14))), (tl.load(in20_ptr + (tl.maximum((((((((tl.program_id(0) // 64896) * 256) + (((_lv0 * 1024) + tl.arange(0, 1024)) // 9)) * 13) + tl.maximum((((tl.program_id(0) // 13) % 13) + ((((_lv0 * 1024) + tl.arange(0, 1024)) // 3) % 3)) - 1, 0)) * 13) + tl.maximum(((tl.program_id(0) % 13) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 3)) - 1, 0)) - tl.maximum((((((((tl.program_id(0) // 64896) * 256) + (((_lv0 * 1024) + tl.arange(0, 1024)) // 9)) * 13) + tl.maximum((((tl.program_id(0) // 13) % 13) + ((((_lv0 * 1024) + tl.arange(0, 1024)) // 3) % 3)) - 1, 0)) * 13) + tl.maximum(((tl.program_id(0) % 13) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 3)) - 1, 0)) - 44302335, 0), 0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 2304) & ((((1 <= (((tl.program_id(0) // 13) % 13) + ((((_lv0 * 1024) + tl.arange(0, 1024)) // 3) % 3))) & ((((tl.program_id(0) // 13) % 13) + ((((_lv0 * 1024) + tl.arange(0, 1024)) // 3) % 3)) < 14)) & (1 <= ((tl.program_id(0) % 13) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 3)))) & (((tl.program_id(0) % 13) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 3)) < 14))), other=0.0) * tl.load(in5_ptr + (((((((((tl.program_id(0) // 169) % 384) * 256) + (((_lv0 * 1024) + tl.arange(0, 1024)) // 9)) * 3) + ((((_lv0 * 1024) + tl.arange(0, 1024)) // 3) % 3)) * 3) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 3)) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 2304) & ((((1 <= (((tl.program_id(0) // 13) % 13) + ((((_lv0 * 1024) + tl.arange(0, 1024)) // 3) % 3))) & ((((tl.program_id(0) // 13) % 13) + ((((_lv0 * 1024) + tl.arange(0, 1024)) // 3) % 3)) < 14)) & (1 <= ((tl.program_id(0) % 13) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 3)))) & (((tl.program_id(0) % 13) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 3)) < 14))), other=0.0)), 0.0))
    _v = tl.maximum((tl.sum(_acc0, axis=0) + tl.load(in6_ptr + (((tl.program_id(0) // 169) % 384)))), (0.0 * (1.0 / 1.0)))
    tl.store(out_ptr + tl.program_id(0), _v)


def t005_s4(out, ins):
    grid = (66453504,)
    t005_s4_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20])
    return out


@triton.jit
def t005_s5_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 4):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 3456) & ((((1 <= (((tl.program_id(0) // 13) % 13) + ((((_lv0 * 1024) + tl.arange(0, 1024)) // 3) % 3))) & ((((tl.program_id(0) // 13) % 13) + ((((_lv0 * 1024) + tl.arange(0, 1024)) // 3) % 3)) < 14)) & (1 <= ((tl.program_id(0) % 13) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 3)))) & (((tl.program_id(0) % 13) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 3)) < 14))), (tl.load(in21_ptr + (tl.maximum((((((((tl.program_id(0) // 64896) * 384) + (((_lv0 * 1024) + tl.arange(0, 1024)) // 9)) * 13) + tl.maximum((((tl.program_id(0) // 13) % 13) + ((((_lv0 * 1024) + tl.arange(0, 1024)) // 3) % 3)) - 1, 0)) * 13) + tl.maximum(((tl.program_id(0) % 13) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 3)) - 1, 0)) - tl.maximum((((((((tl.program_id(0) // 64896) * 384) + (((_lv0 * 1024) + tl.arange(0, 1024)) // 9)) * 13) + tl.maximum((((tl.program_id(0) // 13) % 13) + ((((_lv0 * 1024) + tl.arange(0, 1024)) // 3) % 3)) - 1, 0)) * 13) + tl.maximum(((tl.program_id(0) % 13) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 3)) - 1, 0)) - 66453503, 0), 0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 3456) & ((((1 <= (((tl.program_id(0) // 13) % 13) + ((((_lv0 * 1024) + tl.arange(0, 1024)) // 3) % 3))) & ((((tl.program_id(0) // 13) % 13) + ((((_lv0 * 1024) + tl.arange(0, 1024)) // 3) % 3)) < 14)) & (1 <= ((tl.program_id(0) % 13) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 3)))) & (((tl.program_id(0) % 13) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 3)) < 14))), other=0.0) * tl.load(in7_ptr + (((((((((tl.program_id(0) // 169) % 384) * 384) + (((_lv0 * 1024) + tl.arange(0, 1024)) // 9)) * 3) + ((((_lv0 * 1024) + tl.arange(0, 1024)) // 3) % 3)) * 3) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 3)) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 3456) & ((((1 <= (((tl.program_id(0) // 13) % 13) + ((((_lv0 * 1024) + tl.arange(0, 1024)) // 3) % 3))) & ((((tl.program_id(0) // 13) % 13) + ((((_lv0 * 1024) + tl.arange(0, 1024)) // 3) % 3)) < 14)) & (1 <= ((tl.program_id(0) % 13) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 3)))) & (((tl.program_id(0) % 13) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 3)) < 14))), other=0.0)), 0.0))
    _v = tl.maximum((tl.sum(_acc0, axis=0) + tl.load(in8_ptr + (((tl.program_id(0) // 169) % 384)))), (0.0 * (1.0 / 1.0)))
    tl.store(out_ptr + tl.program_id(0), _v)


def t005_s5(out, ins):
    grid = (66453504,)
    t005_s5_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21])
    return out


@triton.jit
def t005_s6_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 4):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 3456) & ((((1 <= (((tl.program_id(0) // 13) % 13) + ((((_lv0 * 1024) + tl.arange(0, 1024)) // 3) % 3))) & ((((tl.program_id(0) // 13) % 13) + ((((_lv0 * 1024) + tl.arange(0, 1024)) // 3) % 3)) < 14)) & (1 <= ((tl.program_id(0) % 13) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 3)))) & (((tl.program_id(0) % 13) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 3)) < 14))), (tl.load(in22_ptr + (tl.maximum((((((((tl.program_id(0) // 43264) * 384) + (((_lv0 * 1024) + tl.arange(0, 1024)) // 9)) * 13) + tl.maximum((((tl.program_id(0) // 13) % 13) + ((((_lv0 * 1024) + tl.arange(0, 1024)) // 3) % 3)) - 1, 0)) * 13) + tl.maximum(((tl.program_id(0) % 13) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 3)) - 1, 0)) - tl.maximum((((((((tl.program_id(0) // 43264) * 384) + (((_lv0 * 1024) + tl.arange(0, 1024)) // 9)) * 13) + tl.maximum((((tl.program_id(0) // 13) % 13) + ((((_lv0 * 1024) + tl.arange(0, 1024)) // 3) % 3)) - 1, 0)) * 13) + tl.maximum(((tl.program_id(0) % 13) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 3)) - 1, 0)) - 66453503, 0), 0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 3456) & ((((1 <= (((tl.program_id(0) // 13) % 13) + ((((_lv0 * 1024) + tl.arange(0, 1024)) // 3) % 3))) & ((((tl.program_id(0) // 13) % 13) + ((((_lv0 * 1024) + tl.arange(0, 1024)) // 3) % 3)) < 14)) & (1 <= ((tl.program_id(0) % 13) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 3)))) & (((tl.program_id(0) % 13) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 3)) < 14))), other=0.0) * tl.load(in9_ptr + (((((((((tl.program_id(0) // 169) % 256) * 384) + (((_lv0 * 1024) + tl.arange(0, 1024)) // 9)) * 3) + ((((_lv0 * 1024) + tl.arange(0, 1024)) // 3) % 3)) * 3) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 3)) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 3456) & ((((1 <= (((tl.program_id(0) // 13) % 13) + ((((_lv0 * 1024) + tl.arange(0, 1024)) // 3) % 3))) & ((((tl.program_id(0) // 13) % 13) + ((((_lv0 * 1024) + tl.arange(0, 1024)) // 3) % 3)) < 14)) & (1 <= ((tl.program_id(0) % 13) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 3)))) & (((tl.program_id(0) % 13) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 3)) < 14))), other=0.0)), 0.0))
    _v = tl.maximum((tl.sum(_acc0, axis=0) + tl.load(in10_ptr + (((tl.program_id(0) // 169) % 256)))), (0.0 * (1.0 / 1.0)))
    tl.store(out_ptr + tl.program_id(0), _v)


def t005_s6(out, ins):
    grid = (44302336,)
    t005_s6_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22])
    return out


@triton.jit
def t005_s7_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr):
    _acc0 = tl.zeros([8], dtype=tl.float32) + (tl.load(in23_ptr + ((((((((tl.program_id(0) // 9216) * 256) + ((tl.program_id(0) // 36) % 256)) * 13) + tl.maximum(((((tl.program_id(0) // 6) % 6) * 2) + tl.maximum(((0 // 3) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 6) % 6) * 2), 0) - (0 // 3), 0)) - tl.maximum(((0 // 3) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 6) % 6) * 2), 0) - (0 // 3), 0)) - tl.maximum(12 - (((tl.program_id(0) // 6) % 6) * 2), 0), 0), 0)) - tl.maximum(((((tl.program_id(0) // 6) % 6) * 2) + tl.maximum(((0 // 3) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 6) % 6) * 2), 0) - (0 // 3), 0)) - tl.maximum(((0 // 3) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 6) % 6) * 2), 0) - (0 // 3), 0)) - tl.maximum(12 - (((tl.program_id(0) // 6) % 6) * 2), 0), 0), 0)) - 12, 0), 0)) * 13) + tl.maximum((((tl.program_id(0) % 6) * 2) + tl.maximum(((0 % 3) + tl.maximum(tl.maximum(0 - ((tl.program_id(0) % 6) * 2), 0) - (0 % 3), 0)) - tl.maximum(((0 % 3) + tl.maximum(tl.maximum(0 - ((tl.program_id(0) % 6) * 2), 0) - (0 % 3), 0)) - tl.maximum(12 - ((tl.program_id(0) % 6) * 2), 0), 0), 0)) - tl.maximum((((tl.program_id(0) % 6) * 2) + tl.maximum(((0 % 3) + tl.maximum(tl.maximum(0 - ((tl.program_id(0) % 6) * 2), 0) - (0 % 3), 0)) - tl.maximum(((0 % 3) + tl.maximum(tl.maximum(0 - ((tl.program_id(0) % 6) * 2), 0) - (0 % 3), 0)) - tl.maximum(12 - ((tl.program_id(0) % 6) * 2), 0), 0), 0)) - 12, 0), 0)))))
    for _lv0 in range(0, 2):
        _acc0 = tl.maximum(_acc0, tl.load(in23_ptr + ((((((((tl.program_id(0) // 9216) * 256) + ((tl.program_id(0) // 36) % 256)) * 13) + tl.maximum(((((tl.program_id(0) // 6) % 6) * 2) + tl.maximum(((tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 8, 0), 0) // 3) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 6) % 6) * 2), 0) - (tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 8, 0), 0) // 3), 0)) - tl.maximum(((tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 8, 0), 0) // 3) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 6) % 6) * 2), 0) - (tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 8, 0), 0) // 3), 0)) - tl.maximum(12 - (((tl.program_id(0) // 6) % 6) * 2), 0), 0), 0)) - tl.maximum(((((tl.program_id(0) // 6) % 6) * 2) + tl.maximum(((tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 8, 0), 0) // 3) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 6) % 6) * 2), 0) - (tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 8, 0), 0) // 3), 0)) - tl.maximum(((tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 8, 0), 0) // 3) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 6) % 6) * 2), 0) - (tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 8, 0), 0) // 3), 0)) - tl.maximum(12 - (((tl.program_id(0) // 6) % 6) * 2), 0), 0), 0)) - 12, 0), 0)) * 13) + tl.maximum((((tl.program_id(0) % 6) * 2) + tl.maximum(((tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 8, 0), 0) % 3) + tl.maximum(tl.maximum(0 - ((tl.program_id(0) % 6) * 2), 0) - (tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 8, 0), 0) % 3), 0)) - tl.maximum(((tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 8, 0), 0) % 3) + tl.maximum(tl.maximum(0 - ((tl.program_id(0) % 6) * 2), 0) - (tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 8, 0), 0) % 3), 0)) - tl.maximum(12 - ((tl.program_id(0) % 6) * 2), 0), 0), 0)) - tl.maximum((((tl.program_id(0) % 6) * 2) + tl.maximum(((tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 8, 0), 0) % 3) + tl.maximum(tl.maximum(0 - ((tl.program_id(0) % 6) * 2), 0) - (tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 8, 0), 0) % 3), 0)) - tl.maximum(((tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 8, 0), 0) % 3) + tl.maximum(tl.maximum(0 - ((tl.program_id(0) % 6) * 2), 0) - (tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 8, 0), 0) % 3), 0)) - tl.maximum(12 - ((tl.program_id(0) % 6) * 2), 0), 0), 0)) - 12, 0), 0)))))
    _v = tl.max(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t005_s7(out, ins):
    grid = (9437184,)
    t005_s7_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23])
    return out


@triton.jit
def t005_s8_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 9):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 9216) & True), (tl.load(in24_ptr + (tl.maximum((((tl.program_id(0) // 4096) * 9216) + ((_lv0 * 1024) + tl.arange(0, 1024))) - tl.maximum((((tl.program_id(0) // 4096) * 9216) + ((_lv0 * 1024) + tl.arange(0, 1024))) - 9437183, 0), 0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 9216) & True), other=0.0) * tl.load(in11_ptr + ((((tl.program_id(0) % 4096) * 9216) + ((_lv0 * 1024) + tl.arange(0, 1024))) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 9216) & True), other=0.0)), 0.0))
    _v = tl.maximum((tl.sum(_acc0, axis=0) + tl.load(in12_ptr + ((tl.program_id(0) % 4096)))), (0.0 * (1.0 / 1.0)))
    tl.store(out_ptr + tl.program_id(0), _v)


def t005_s8(out, ins):
    grid = (4194304,)
    t005_s8_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24])
    return out


@triton.jit
def t005_s9_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 4):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 4096) & True), (tl.load(in25_ptr + ((((tl.program_id(0) // 4096) * 4096) + ((_lv0 * 1024) + tl.arange(0, 1024))) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 4096) & True), other=0.0) * tl.load(in13_ptr + ((((tl.program_id(0) % 4096) * 4096) + ((_lv0 * 1024) + tl.arange(0, 1024))) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 4096) & True), other=0.0)), 0.0))
    _v = tl.maximum((tl.sum(_acc0, axis=0) + tl.load(in14_ptr + ((tl.program_id(0) % 4096)))), (0.0 * (1.0 / 1.0)))
    tl.store(out_ptr + tl.program_id(0), _v)


def t005_s9(out, ins):
    grid = (4194304,)
    t005_s9_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25])
    return out


@triton.jit
def t005_s10_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr, in20_ptr, in21_ptr, in22_ptr, in23_ptr, in24_ptr, in25_ptr, in26_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 4):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 4096) & True), (tl.load(in26_ptr + ((((tl.program_id(0) // 1000) * 4096) + ((_lv0 * 1024) + tl.arange(0, 1024))) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 4096) & True), other=0.0) * tl.load(in15_ptr + ((((tl.program_id(0) % 1000) * 4096) + ((_lv0 * 1024) + tl.arange(0, 1024))) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 4096) & True), other=0.0)), 0.0))
    _v = (tl.sum(_acc0, axis=0) + tl.load(in16_ptr + ((tl.program_id(0) % 1000))))
    tl.store(out_ptr + tl.program_id(0), _v)


def t005_s10(out, ins):
    grid = (1024000,)
    t005_s10_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19], ins[20], ins[21], ins[22], ins[23], ins[24], ins[25], ins[26])
    return out


def t005(out, ins):
    _t0 = torch.empty(297369600, device=ins[0].device, dtype=torch.float32)
    _t1 = torch.empty(71663616, device=ins[0].device, dtype=torch.float32)
    _t2 = torch.empty(191102976, device=ins[0].device, dtype=torch.float32)
    _t3 = torch.empty(44302336, device=ins[0].device, dtype=torch.float32)
    _t4 = torch.empty(66453504, device=ins[0].device, dtype=torch.float32)
    _t5 = torch.empty(66453504, device=ins[0].device, dtype=torch.float32)
    _t6 = torch.empty(44302336, device=ins[0].device, dtype=torch.float32)
    _t7 = torch.empty(9437184, device=ins[0].device, dtype=torch.float32)
    _t8 = torch.empty(4194304, device=ins[0].device, dtype=torch.float32)
    _t9 = torch.empty(4194304, device=ins[0].device, dtype=torch.float32)
    t005_s0(_t0, list(ins))
    t005_s1(_t1, list(ins) + [_t0])
    t005_s2(_t2, list(ins) + [_t0, _t1])
    t005_s3(_t3, list(ins) + [_t0, _t1, _t2])
    t005_s4(_t4, list(ins) + [_t0, _t1, _t2, _t3])
    t005_s5(_t5, list(ins) + [_t0, _t1, _t2, _t3, _t4])
    t005_s6(_t6, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5])
    t005_s7(_t7, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6])
    t005_s8(_t8, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7])
    t005_s9(_t9, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8])
    t005_s10(out, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7, _t8, _t9])
    return out
