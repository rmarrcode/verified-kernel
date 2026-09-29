import torch
import triton
import triton.language as tl


@triton.jit
def _mul_combine(a, b):
    return a * b


@triton.jit
def t006_s0_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr):
    _acc0 = tl.zeros([256], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 256) + tl.arange(0, 256)) < 480) & ((((tl.program_id(0) // 224) % 224) < 224) & ((tl.program_id(0) % 224) < 224))), (tl.load(in0_ptr + ((((((((tl.program_id(0) // 9633792) * 480) + ((_lv0 * 256) + tl.arange(0, 256))) * 224) + ((tl.program_id(0) // 224) % 224)) * 224) + (tl.program_id(0) % 224)) + 0 * tl.arange(0, 256)), mask=((((_lv0 * 256) + tl.arange(0, 256)) < 480) & ((((tl.program_id(0) // 224) % 224) < 224) & ((tl.program_id(0) % 224) < 224))), other=0.0) * tl.load(in1_ptr + (((((tl.program_id(0) // 50176) % 192) * 480) + ((_lv0 * 256) + tl.arange(0, 256))) + 0 * tl.arange(0, 256)), mask=((((_lv0 * 256) + tl.arange(0, 256)) < 480) & ((((tl.program_id(0) // 224) % 224) < 224) & ((tl.program_id(0) % 224) < 224))), other=0.0)), 0.0))
    _v = (tl.sum(_acc0, axis=0) + tl.load(in2_ptr + (((tl.program_id(0) // 50176) % 192))))
    tl.store(out_ptr + tl.program_id(0), _v)


def t006_s0(out, ins):
    grid = (96337920,)
    t006_s0_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12])
    return out


@triton.jit
def t006_s1_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr):
    _acc0 = tl.zeros([256], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 256) + tl.arange(0, 256)) < 480) & ((((tl.program_id(0) // 224) % 224) < 224) & ((tl.program_id(0) % 224) < 224))), (tl.load(in0_ptr + ((((((((tl.program_id(0) // 4816896) * 480) + ((_lv0 * 256) + tl.arange(0, 256))) * 224) + ((tl.program_id(0) // 224) % 224)) * 224) + (tl.program_id(0) % 224)) + 0 * tl.arange(0, 256)), mask=((((_lv0 * 256) + tl.arange(0, 256)) < 480) & ((((tl.program_id(0) // 224) % 224) < 224) & ((tl.program_id(0) % 224) < 224))), other=0.0) * tl.load(in3_ptr + (((((tl.program_id(0) // 50176) % 96) * 480) + ((_lv0 * 256) + tl.arange(0, 256))) + 0 * tl.arange(0, 256)), mask=((((_lv0 * 256) + tl.arange(0, 256)) < 480) & ((((tl.program_id(0) // 224) % 224) < 224) & ((tl.program_id(0) % 224) < 224))), other=0.0)), 0.0))
    _v = (tl.sum(_acc0, axis=0) + tl.load(in4_ptr + (((tl.program_id(0) // 50176) % 96))))
    tl.store(out_ptr + tl.program_id(0), _v)


def t006_s1(out, ins):
    grid = (48168960,)
    t006_s1_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13])
    return out


@triton.jit
def t006_s2_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr):
    _acc0 = tl.zeros([512], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 512) + tl.arange(0, 512)) < 864) & ((((1 <= (((tl.program_id(0) // 224) % 224) + ((((_lv0 * 512) + tl.arange(0, 512)) // 3) % 3))) & ((((tl.program_id(0) // 224) % 224) + ((((_lv0 * 512) + tl.arange(0, 512)) // 3) % 3)) < 225)) & (1 <= ((tl.program_id(0) % 224) + (((_lv0 * 512) + tl.arange(0, 512)) % 3)))) & (((tl.program_id(0) % 224) + (((_lv0 * 512) + tl.arange(0, 512)) % 3)) < 225))), (tl.load(in14_ptr + (tl.maximum((((((((tl.program_id(0) // 10436608) * 96) + (((_lv0 * 512) + tl.arange(0, 512)) // 9)) * 224) + tl.maximum((((tl.program_id(0) // 224) % 224) + ((((_lv0 * 512) + tl.arange(0, 512)) // 3) % 3)) - 1, 0)) * 224) + tl.maximum(((tl.program_id(0) % 224) + (((_lv0 * 512) + tl.arange(0, 512)) % 3)) - 1, 0)) - tl.maximum((((((((tl.program_id(0) // 10436608) * 96) + (((_lv0 * 512) + tl.arange(0, 512)) // 9)) * 224) + tl.maximum((((tl.program_id(0) // 224) % 224) + ((((_lv0 * 512) + tl.arange(0, 512)) // 3) % 3)) - 1, 0)) * 224) + tl.maximum(((tl.program_id(0) % 224) + (((_lv0 * 512) + tl.arange(0, 512)) % 3)) - 1, 0)) - 48168959, 0), 0) + 0 * tl.arange(0, 512)), mask=((((_lv0 * 512) + tl.arange(0, 512)) < 864) & ((((1 <= (((tl.program_id(0) // 224) % 224) + ((((_lv0 * 512) + tl.arange(0, 512)) // 3) % 3))) & ((((tl.program_id(0) // 224) % 224) + ((((_lv0 * 512) + tl.arange(0, 512)) // 3) % 3)) < 225)) & (1 <= ((tl.program_id(0) % 224) + (((_lv0 * 512) + tl.arange(0, 512)) % 3)))) & (((tl.program_id(0) % 224) + (((_lv0 * 512) + tl.arange(0, 512)) % 3)) < 225))), other=0.0) * tl.load(in5_ptr + (((((((((tl.program_id(0) // 50176) % 208) * 96) + (((_lv0 * 512) + tl.arange(0, 512)) // 9)) * 3) + ((((_lv0 * 512) + tl.arange(0, 512)) // 3) % 3)) * 3) + (((_lv0 * 512) + tl.arange(0, 512)) % 3)) + 0 * tl.arange(0, 512)), mask=((((_lv0 * 512) + tl.arange(0, 512)) < 864) & ((((1 <= (((tl.program_id(0) // 224) % 224) + ((((_lv0 * 512) + tl.arange(0, 512)) // 3) % 3))) & ((((tl.program_id(0) // 224) % 224) + ((((_lv0 * 512) + tl.arange(0, 512)) // 3) % 3)) < 225)) & (1 <= ((tl.program_id(0) % 224) + (((_lv0 * 512) + tl.arange(0, 512)) % 3)))) & (((tl.program_id(0) % 224) + (((_lv0 * 512) + tl.arange(0, 512)) % 3)) < 225))), other=0.0)), 0.0))
    _v = (tl.sum(_acc0, axis=0) + tl.load(in6_ptr + (((tl.program_id(0) // 50176) % 208))))
    tl.store(out_ptr + tl.program_id(0), _v)


def t006_s2(out, ins):
    grid = (104366080,)
    t006_s2_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14])
    return out


@triton.jit
def t006_s3_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr):
    _acc0 = tl.zeros([256], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 256) + tl.arange(0, 256)) < 480) & ((((tl.program_id(0) // 224) % 224) < 224) & ((tl.program_id(0) % 224) < 224))), (tl.load(in0_ptr + ((((((((tl.program_id(0) // 802816) * 480) + ((_lv0 * 256) + tl.arange(0, 256))) * 224) + ((tl.program_id(0) // 224) % 224)) * 224) + (tl.program_id(0) % 224)) + 0 * tl.arange(0, 256)), mask=((((_lv0 * 256) + tl.arange(0, 256)) < 480) & ((((tl.program_id(0) // 224) % 224) < 224) & ((tl.program_id(0) % 224) < 224))), other=0.0) * tl.load(in7_ptr + (((((tl.program_id(0) // 50176) % 16) * 480) + ((_lv0 * 256) + tl.arange(0, 256))) + 0 * tl.arange(0, 256)), mask=((((_lv0 * 256) + tl.arange(0, 256)) < 480) & ((((tl.program_id(0) // 224) % 224) < 224) & ((tl.program_id(0) % 224) < 224))), other=0.0)), 0.0))
    _v = (tl.sum(_acc0, axis=0) + tl.load(in8_ptr + (((tl.program_id(0) // 50176) % 16))))
    tl.store(out_ptr + tl.program_id(0), _v)


def t006_s3(out, ins):
    grid = (8028160,)
    t006_s3_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15])
    return out


@triton.jit
def t006_s4_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr):
    _acc0 = tl.zeros([256], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 256) + tl.arange(0, 256)) < 400) & ((((2 <= (((tl.program_id(0) // 224) % 224) + ((((_lv0 * 256) + tl.arange(0, 256)) // 5) % 5))) & ((((tl.program_id(0) // 224) % 224) + ((((_lv0 * 256) + tl.arange(0, 256)) // 5) % 5)) < 226)) & (2 <= ((tl.program_id(0) % 224) + (((_lv0 * 256) + tl.arange(0, 256)) % 5)))) & (((tl.program_id(0) % 224) + (((_lv0 * 256) + tl.arange(0, 256)) % 5)) < 226))), (tl.load(in16_ptr + (tl.maximum((((((((tl.program_id(0) // 2408448) * 16) + (((_lv0 * 256) + tl.arange(0, 256)) // 25)) * 224) + tl.maximum((((tl.program_id(0) // 224) % 224) + ((((_lv0 * 256) + tl.arange(0, 256)) // 5) % 5)) - 2, 0)) * 224) + tl.maximum(((tl.program_id(0) % 224) + (((_lv0 * 256) + tl.arange(0, 256)) % 5)) - 2, 0)) - tl.maximum((((((((tl.program_id(0) // 2408448) * 16) + (((_lv0 * 256) + tl.arange(0, 256)) // 25)) * 224) + tl.maximum((((tl.program_id(0) // 224) % 224) + ((((_lv0 * 256) + tl.arange(0, 256)) // 5) % 5)) - 2, 0)) * 224) + tl.maximum(((tl.program_id(0) % 224) + (((_lv0 * 256) + tl.arange(0, 256)) % 5)) - 2, 0)) - 8028159, 0), 0) + 0 * tl.arange(0, 256)), mask=((((_lv0 * 256) + tl.arange(0, 256)) < 400) & ((((2 <= (((tl.program_id(0) // 224) % 224) + ((((_lv0 * 256) + tl.arange(0, 256)) // 5) % 5))) & ((((tl.program_id(0) // 224) % 224) + ((((_lv0 * 256) + tl.arange(0, 256)) // 5) % 5)) < 226)) & (2 <= ((tl.program_id(0) % 224) + (((_lv0 * 256) + tl.arange(0, 256)) % 5)))) & (((tl.program_id(0) % 224) + (((_lv0 * 256) + tl.arange(0, 256)) % 5)) < 226))), other=0.0) * tl.load(in9_ptr + (((((((((tl.program_id(0) // 50176) % 48) * 16) + (((_lv0 * 256) + tl.arange(0, 256)) // 25)) * 5) + ((((_lv0 * 256) + tl.arange(0, 256)) // 5) % 5)) * 5) + (((_lv0 * 256) + tl.arange(0, 256)) % 5)) + 0 * tl.arange(0, 256)), mask=((((_lv0 * 256) + tl.arange(0, 256)) < 400) & ((((2 <= (((tl.program_id(0) // 224) % 224) + ((((_lv0 * 256) + tl.arange(0, 256)) // 5) % 5))) & ((((tl.program_id(0) // 224) % 224) + ((((_lv0 * 256) + tl.arange(0, 256)) // 5) % 5)) < 226)) & (2 <= ((tl.program_id(0) % 224) + (((_lv0 * 256) + tl.arange(0, 256)) % 5)))) & (((tl.program_id(0) % 224) + (((_lv0 * 256) + tl.arange(0, 256)) % 5)) < 226))), other=0.0)), 0.0))
    _v = (tl.sum(_acc0, axis=0) + tl.load(in10_ptr + (((tl.program_id(0) // 50176) % 48))))
    tl.store(out_ptr + tl.program_id(0), _v)


def t006_s4(out, ins):
    grid = (24084480,)
    t006_s4_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16])
    return out


@triton.jit
def t006_s5_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr):
    _acc0 = tl.zeros([8], dtype=tl.float32) + (tl.load(in0_ptr + ((((((((tl.program_id(0) // 24084480) * 480) + ((tl.program_id(0) // 50176) % 480)) * 224) + tl.maximum(tl.maximum((((tl.program_id(0) // 224) % 224) + tl.maximum(((0 // 3) + tl.maximum(tl.maximum(1 - ((tl.program_id(0) // 224) % 224), 0) - (0 // 3), 0)) - tl.maximum(((0 // 3) + tl.maximum(tl.maximum(1 - ((tl.program_id(0) // 224) % 224), 0) - (0 // 3), 0)) - tl.maximum(224 - ((tl.program_id(0) // 224) % 224), 0), 0), 0)) - 1, 0) - tl.maximum(tl.maximum((((tl.program_id(0) // 224) % 224) + tl.maximum(((0 // 3) + tl.maximum(tl.maximum(1 - ((tl.program_id(0) // 224) % 224), 0) - (0 // 3), 0)) - tl.maximum(((0 // 3) + tl.maximum(tl.maximum(1 - ((tl.program_id(0) // 224) % 224), 0) - (0 // 3), 0)) - tl.maximum(224 - ((tl.program_id(0) // 224) % 224), 0), 0), 0)) - 1, 0) - 223, 0), 0)) * 224) + tl.maximum(tl.maximum(((tl.program_id(0) % 224) + tl.maximum(((0 % 3) + tl.maximum(tl.maximum(1 - (tl.program_id(0) % 224), 0) - (0 % 3), 0)) - tl.maximum(((0 % 3) + tl.maximum(tl.maximum(1 - (tl.program_id(0) % 224), 0) - (0 % 3), 0)) - tl.maximum(224 - (tl.program_id(0) % 224), 0), 0), 0)) - 1, 0) - tl.maximum(tl.maximum(((tl.program_id(0) % 224) + tl.maximum(((0 % 3) + tl.maximum(tl.maximum(1 - (tl.program_id(0) % 224), 0) - (0 % 3), 0)) - tl.maximum(((0 % 3) + tl.maximum(tl.maximum(1 - (tl.program_id(0) % 224), 0) - (0 % 3), 0)) - tl.maximum(224 - (tl.program_id(0) % 224), 0), 0), 0)) - 1, 0) - 223, 0), 0)))))
    for _lv0 in range(0, 2):
        _acc0 = tl.maximum(_acc0, tl.load(in0_ptr + ((((((((tl.program_id(0) // 24084480) * 480) + ((tl.program_id(0) // 50176) % 480)) * 224) + tl.maximum(tl.maximum((((tl.program_id(0) // 224) % 224) + tl.maximum(((tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 8, 0), 0) // 3) + tl.maximum(tl.maximum(1 - ((tl.program_id(0) // 224) % 224), 0) - (tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 8, 0), 0) // 3), 0)) - tl.maximum(((tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 8, 0), 0) // 3) + tl.maximum(tl.maximum(1 - ((tl.program_id(0) // 224) % 224), 0) - (tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 8, 0), 0) // 3), 0)) - tl.maximum(224 - ((tl.program_id(0) // 224) % 224), 0), 0), 0)) - 1, 0) - tl.maximum(tl.maximum((((tl.program_id(0) // 224) % 224) + tl.maximum(((tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 8, 0), 0) // 3) + tl.maximum(tl.maximum(1 - ((tl.program_id(0) // 224) % 224), 0) - (tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 8, 0), 0) // 3), 0)) - tl.maximum(((tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 8, 0), 0) // 3) + tl.maximum(tl.maximum(1 - ((tl.program_id(0) // 224) % 224), 0) - (tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 8, 0), 0) // 3), 0)) - tl.maximum(224 - ((tl.program_id(0) // 224) % 224), 0), 0), 0)) - 1, 0) - 223, 0), 0)) * 224) + tl.maximum(tl.maximum(((tl.program_id(0) % 224) + tl.maximum(((tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 8, 0), 0) % 3) + tl.maximum(tl.maximum(1 - (tl.program_id(0) % 224), 0) - (tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 8, 0), 0) % 3), 0)) - tl.maximum(((tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 8, 0), 0) % 3) + tl.maximum(tl.maximum(1 - (tl.program_id(0) % 224), 0) - (tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 8, 0), 0) % 3), 0)) - tl.maximum(224 - (tl.program_id(0) % 224), 0), 0), 0)) - 1, 0) - tl.maximum(tl.maximum(((tl.program_id(0) % 224) + tl.maximum(((tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 8, 0), 0) % 3) + tl.maximum(tl.maximum(1 - (tl.program_id(0) % 224), 0) - (tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 8, 0), 0) % 3), 0)) - tl.maximum(((tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 8, 0), 0) % 3) + tl.maximum(tl.maximum(1 - (tl.program_id(0) % 224), 0) - (tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 8, 0), 0) % 3), 0)) - tl.maximum(224 - (tl.program_id(0) % 224), 0), 0), 0)) - 1, 0) - 223, 0), 0)))))
    _v = tl.max(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t006_s5(out, ins):
    grid = (240844800,)
    t006_s5_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17])
    return out


@triton.jit
def t006_s6_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr):
    _acc0 = tl.zeros([256], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 256) + tl.arange(0, 256)) < 480) & ((((tl.program_id(0) // 224) % 224) < 224) & ((tl.program_id(0) % 224) < 224))), (tl.load(in18_ptr + ((((((((tl.program_id(0) // 3211264) * 480) + ((_lv0 * 256) + tl.arange(0, 256))) * 224) + ((tl.program_id(0) // 224) % 224)) * 224) + (tl.program_id(0) % 224)) + 0 * tl.arange(0, 256)), mask=((((_lv0 * 256) + tl.arange(0, 256)) < 480) & ((((tl.program_id(0) // 224) % 224) < 224) & ((tl.program_id(0) % 224) < 224))), other=0.0) * tl.load(in11_ptr + (((((tl.program_id(0) // 50176) % 64) * 480) + ((_lv0 * 256) + tl.arange(0, 256))) + 0 * tl.arange(0, 256)), mask=((((_lv0 * 256) + tl.arange(0, 256)) < 480) & ((((tl.program_id(0) // 224) % 224) < 224) & ((tl.program_id(0) % 224) < 224))), other=0.0)), 0.0))
    _v = (tl.sum(_acc0, axis=0) + tl.load(in12_ptr + (((tl.program_id(0) // 50176) % 64))))
    tl.store(out_ptr + tl.program_id(0), _v)


def t006_s6(out, ins):
    grid = (32112640,)
    t006_s6_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18])
    return out


@triton.jit
def t006_s7_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr, in14_ptr, in15_ptr, in16_ptr, in17_ptr, in18_ptr, in19_ptr):
    _acc0 = tl.zeros([4], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 4) + tl.arange(0, 4)) < 4) & ((((((((_lv0 * 4) + tl.arange(0, 4)) == 0) & (0 <= ((tl.program_id(0) // 50176) % 512))) & (((tl.program_id(0) // 50176) % 512) < 192)) | (((((_lv0 * 4) + tl.arange(0, 4)) == 1) & (192 <= ((tl.program_id(0) // 50176) % 512))) & (((tl.program_id(0) // 50176) % 512) < 400))) | (((((_lv0 * 4) + tl.arange(0, 4)) == 2) & (400 <= ((tl.program_id(0) // 50176) % 512))) & (((tl.program_id(0) // 50176) % 512) < 448))) | (((((_lv0 * 4) + tl.arange(0, 4)) == 3) & (448 <= ((tl.program_id(0) // 50176) % 512))) & (((tl.program_id(0) // 50176) % 512) < 512)))), tl.where((((_lv0 * 4) + tl.arange(0, 4))).to(tl.float32) <= (1.0 * (1.0 / 2.0)), tl.load(in13_ptr + (tl.maximum((((((((tl.program_id(0) // 25690112) * 192) + ((tl.program_id(0) // 50176) % 512)) * 224) + ((tl.program_id(0) // 224) % 224)) * 224) + (tl.program_id(0) % 224)) - tl.maximum((((((((tl.program_id(0) // 25690112) * 192) + ((tl.program_id(0) // 50176) % 512)) * 224) + ((tl.program_id(0) // 224) % 224)) * 224) + (tl.program_id(0) % 224)) - 96337919, 0), 0) + 0 * tl.arange(0, 4)), mask=((((_lv0 * 4) + tl.arange(0, 4)) < 4) & ((((((((_lv0 * 4) + tl.arange(0, 4)) == 0) & (0 <= ((tl.program_id(0) // 50176) % 512))) & (((tl.program_id(0) // 50176) % 512) < 192)) | (((((_lv0 * 4) + tl.arange(0, 4)) == 1) & (192 <= ((tl.program_id(0) // 50176) % 512))) & (((tl.program_id(0) // 50176) % 512) < 400))) | (((((_lv0 * 4) + tl.arange(0, 4)) == 2) & (400 <= ((tl.program_id(0) // 50176) % 512))) & (((tl.program_id(0) // 50176) % 512) < 448))) | (((((_lv0 * 4) + tl.arange(0, 4)) == 3) & (448 <= ((tl.program_id(0) // 50176) % 512))) & (((tl.program_id(0) // 50176) % 512) < 512)))), other=0.0), tl.where((((_lv0 * 4) + tl.arange(0, 4))).to(tl.float32) <= (3.0 * (1.0 / 2.0)), tl.load(in15_ptr + (tl.maximum((((((((tl.program_id(0) // 25690112) * 208) + tl.maximum(((tl.program_id(0) // 50176) % 512) - 192, 0)) * 224) + ((tl.program_id(0) // 224) % 224)) * 224) + (tl.program_id(0) % 224)) - tl.maximum((((((((tl.program_id(0) // 25690112) * 208) + tl.maximum(((tl.program_id(0) // 50176) % 512) - 192, 0)) * 224) + ((tl.program_id(0) // 224) % 224)) * 224) + (tl.program_id(0) % 224)) - 104366079, 0), 0) + 0 * tl.arange(0, 4)), mask=((((_lv0 * 4) + tl.arange(0, 4)) < 4) & ((((((((_lv0 * 4) + tl.arange(0, 4)) == 0) & (0 <= ((tl.program_id(0) // 50176) % 512))) & (((tl.program_id(0) // 50176) % 512) < 192)) | (((((_lv0 * 4) + tl.arange(0, 4)) == 1) & (192 <= ((tl.program_id(0) // 50176) % 512))) & (((tl.program_id(0) // 50176) % 512) < 400))) | (((((_lv0 * 4) + tl.arange(0, 4)) == 2) & (400 <= ((tl.program_id(0) // 50176) % 512))) & (((tl.program_id(0) // 50176) % 512) < 448))) | (((((_lv0 * 4) + tl.arange(0, 4)) == 3) & (448 <= ((tl.program_id(0) // 50176) % 512))) & (((tl.program_id(0) // 50176) % 512) < 512)))), other=0.0), tl.where((((_lv0 * 4) + tl.arange(0, 4))).to(tl.float32) <= (5.0 * (1.0 / 2.0)), tl.load(in17_ptr + (tl.maximum((((((((tl.program_id(0) // 25690112) * 48) + tl.maximum(((tl.program_id(0) // 50176) % 512) - 400, 0)) * 224) + ((tl.program_id(0) // 224) % 224)) * 224) + (tl.program_id(0) % 224)) - tl.maximum((((((((tl.program_id(0) // 25690112) * 48) + tl.maximum(((tl.program_id(0) // 50176) % 512) - 400, 0)) * 224) + ((tl.program_id(0) // 224) % 224)) * 224) + (tl.program_id(0) % 224)) - 24084479, 0), 0) + 0 * tl.arange(0, 4)), mask=((((_lv0 * 4) + tl.arange(0, 4)) < 4) & ((((((((_lv0 * 4) + tl.arange(0, 4)) == 0) & (0 <= ((tl.program_id(0) // 50176) % 512))) & (((tl.program_id(0) // 50176) % 512) < 192)) | (((((_lv0 * 4) + tl.arange(0, 4)) == 1) & (192 <= ((tl.program_id(0) // 50176) % 512))) & (((tl.program_id(0) // 50176) % 512) < 400))) | (((((_lv0 * 4) + tl.arange(0, 4)) == 2) & (400 <= ((tl.program_id(0) // 50176) % 512))) & (((tl.program_id(0) // 50176) % 512) < 448))) | (((((_lv0 * 4) + tl.arange(0, 4)) == 3) & (448 <= ((tl.program_id(0) // 50176) % 512))) & (((tl.program_id(0) // 50176) % 512) < 512)))), other=0.0), tl.load(in19_ptr + (tl.maximum((((((((tl.program_id(0) // 25690112) * 64) + tl.maximum(((tl.program_id(0) // 50176) % 512) - 448, 0)) * 224) + ((tl.program_id(0) // 224) % 224)) * 224) + (tl.program_id(0) % 224)) - tl.maximum((((((((tl.program_id(0) // 25690112) * 64) + tl.maximum(((tl.program_id(0) // 50176) % 512) - 448, 0)) * 224) + ((tl.program_id(0) // 224) % 224)) * 224) + (tl.program_id(0) % 224)) - 32112639, 0), 0) + 0 * tl.arange(0, 4)), mask=((((_lv0 * 4) + tl.arange(0, 4)) < 4) & ((((((((_lv0 * 4) + tl.arange(0, 4)) == 0) & (0 <= ((tl.program_id(0) // 50176) % 512))) & (((tl.program_id(0) // 50176) % 512) < 192)) | (((((_lv0 * 4) + tl.arange(0, 4)) == 1) & (192 <= ((tl.program_id(0) // 50176) % 512))) & (((tl.program_id(0) // 50176) % 512) < 400))) | (((((_lv0 * 4) + tl.arange(0, 4)) == 2) & (400 <= ((tl.program_id(0) // 50176) % 512))) & (((tl.program_id(0) // 50176) % 512) < 448))) | (((((_lv0 * 4) + tl.arange(0, 4)) == 3) & (448 <= ((tl.program_id(0) // 50176) % 512))) & (((tl.program_id(0) // 50176) % 512) < 512)))), other=0.0)))), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t006_s7(out, ins):
    grid = (256901120,)
    t006_s7_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13], ins[14], ins[15], ins[16], ins[17], ins[18], ins[19])
    return out


def t006(out, ins):
    _t0 = torch.empty(96337920, device=ins[0].device, dtype=torch.float32)
    _t1 = torch.empty(48168960, device=ins[0].device, dtype=torch.float32)
    _t2 = torch.empty(104366080, device=ins[0].device, dtype=torch.float32)
    _t3 = torch.empty(8028160, device=ins[0].device, dtype=torch.float32)
    _t4 = torch.empty(24084480, device=ins[0].device, dtype=torch.float32)
    _t5 = torch.empty(240844800, device=ins[0].device, dtype=torch.float32)
    _t6 = torch.empty(32112640, device=ins[0].device, dtype=torch.float32)
    t006_s0(_t0, list(ins))
    t006_s1(_t1, list(ins) + [_t0])
    t006_s2(_t2, list(ins) + [_t0, _t1])
    t006_s3(_t3, list(ins) + [_t0, _t1, _t2])
    t006_s4(_t4, list(ins) + [_t0, _t1, _t2, _t3])
    t006_s5(_t5, list(ins) + [_t0, _t1, _t2, _t3, _t4])
    t006_s6(_t6, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5])
    t006_s7(out, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6])
    return out
