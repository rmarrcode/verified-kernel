import torch
import triton
import triton.language as tl


@triton.jit
def _mul_combine(a, b):
    return a * b


@triton.jit
def t015_s0_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr):
    _acc0 = tl.zeros([256], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 256) + tl.arange(0, 256)) < 432) & (((((((((((((_lv0 * 256) + tl.arange(0, 256)) // 9) % 3) <= (((tl.program_id(0) // 3969) % 31) + 1)) & ((tl.maximum((((tl.program_id(0) // 3969) % 31) + 1) - ((((_lv0 * 256) + tl.arange(0, 256)) // 9) % 3), 0) % 2) == 0)) & ((tl.maximum((((tl.program_id(0) // 3969) % 31) + 1) - ((((_lv0 * 256) + tl.arange(0, 256)) // 9) % 3), 0) // 2) < 16)) & (((((_lv0 * 256) + tl.arange(0, 256)) // 3) % 3) <= (((tl.program_id(0) // 63) % 63) + 1))) & ((tl.maximum((((tl.program_id(0) // 63) % 63) + 1) - ((((_lv0 * 256) + tl.arange(0, 256)) // 3) % 3), 0) % 2) == 0)) & ((tl.maximum((((tl.program_id(0) // 63) % 63) + 1) - ((((_lv0 * 256) + tl.arange(0, 256)) // 3) % 3), 0) // 2) < 32)) & ((((_lv0 * 256) + tl.arange(0, 256)) % 3) <= ((tl.program_id(0) % 63) + 1))) & ((tl.maximum(((tl.program_id(0) % 63) + 1) - (((_lv0 * 256) + tl.arange(0, 256)) % 3), 0) % 2) == 0)) & ((tl.maximum(((tl.program_id(0) % 63) + 1) - (((_lv0 * 256) + tl.arange(0, 256)) % 3), 0) // 2) < 32))), (tl.load(in0_ptr + ((((((((((tl.program_id(0) // 3937248) * 16) + (((((tl.program_id(0) // 123039) % 32) // 32) * 16) + (((_lv0 * 256) + tl.arange(0, 256)) // 27))) * 16) + (tl.maximum((((tl.program_id(0) // 3969) % 31) + 1) - ((((_lv0 * 256) + tl.arange(0, 256)) // 9) % 3), 0) // 2)) * 32) + (tl.maximum((((tl.program_id(0) // 63) % 63) + 1) - ((((_lv0 * 256) + tl.arange(0, 256)) // 3) % 3), 0) // 2)) * 32) + (tl.maximum(((tl.program_id(0) % 63) + 1) - (((_lv0 * 256) + tl.arange(0, 256)) % 3), 0) // 2)) + 0 * tl.arange(0, 256)), mask=((((_lv0 * 256) + tl.arange(0, 256)) < 432) & (((((((((((((_lv0 * 256) + tl.arange(0, 256)) // 9) % 3) <= (((tl.program_id(0) // 3969) % 31) + 1)) & ((tl.maximum((((tl.program_id(0) // 3969) % 31) + 1) - ((((_lv0 * 256) + tl.arange(0, 256)) // 9) % 3), 0) % 2) == 0)) & ((tl.maximum((((tl.program_id(0) // 3969) % 31) + 1) - ((((_lv0 * 256) + tl.arange(0, 256)) // 9) % 3), 0) // 2) < 16)) & (((((_lv0 * 256) + tl.arange(0, 256)) // 3) % 3) <= (((tl.program_id(0) // 63) % 63) + 1))) & ((tl.maximum((((tl.program_id(0) // 63) % 63) + 1) - ((((_lv0 * 256) + tl.arange(0, 256)) // 3) % 3), 0) % 2) == 0)) & ((tl.maximum((((tl.program_id(0) // 63) % 63) + 1) - ((((_lv0 * 256) + tl.arange(0, 256)) // 3) % 3), 0) // 2) < 32)) & ((((_lv0 * 256) + tl.arange(0, 256)) % 3) <= ((tl.program_id(0) % 63) + 1))) & ((tl.maximum(((tl.program_id(0) % 63) + 1) - (((_lv0 * 256) + tl.arange(0, 256)) % 3), 0) % 2) == 0)) & ((tl.maximum(((tl.program_id(0) % 63) + 1) - (((_lv0 * 256) + tl.arange(0, 256)) % 3), 0) // 2) < 32))), other=0.0) * tl.load(in1_ptr + ((((((((((((((tl.program_id(0) // 123039) % 32) // 32) * 16) + (((_lv0 * 256) + tl.arange(0, 256)) // 27)) * 32) + (((tl.program_id(0) // 123039) % 32) % 32)) * 3) + ((((_lv0 * 256) + tl.arange(0, 256)) // 9) % 3)) * 3) + ((((_lv0 * 256) + tl.arange(0, 256)) // 3) % 3)) * 3) + (((_lv0 * 256) + tl.arange(0, 256)) % 3)) + 0 * tl.arange(0, 256)), mask=((((_lv0 * 256) + tl.arange(0, 256)) < 432) & (((((((((((((_lv0 * 256) + tl.arange(0, 256)) // 9) % 3) <= (((tl.program_id(0) // 3969) % 31) + 1)) & ((tl.maximum((((tl.program_id(0) // 3969) % 31) + 1) - ((((_lv0 * 256) + tl.arange(0, 256)) // 9) % 3), 0) % 2) == 0)) & ((tl.maximum((((tl.program_id(0) // 3969) % 31) + 1) - ((((_lv0 * 256) + tl.arange(0, 256)) // 9) % 3), 0) // 2) < 16)) & (((((_lv0 * 256) + tl.arange(0, 256)) // 3) % 3) <= (((tl.program_id(0) // 63) % 63) + 1))) & ((tl.maximum((((tl.program_id(0) // 63) % 63) + 1) - ((((_lv0 * 256) + tl.arange(0, 256)) // 3) % 3), 0) % 2) == 0)) & ((tl.maximum((((tl.program_id(0) // 63) % 63) + 1) - ((((_lv0 * 256) + tl.arange(0, 256)) // 3) % 3), 0) // 2) < 32)) & ((((_lv0 * 256) + tl.arange(0, 256)) % 3) <= ((tl.program_id(0) % 63) + 1))) & ((tl.maximum(((tl.program_id(0) % 63) + 1) - (((_lv0 * 256) + tl.arange(0, 256)) % 3), 0) % 2) == 0)) & ((tl.maximum(((tl.program_id(0) % 63) + 1) - (((_lv0 * 256) + tl.arange(0, 256)) % 3), 0) // 2) < 32))), other=0.0)), 0.0))
    _v = (tl.sum(_acc0, axis=0) + tl.load(in2_ptr + (((tl.program_id(0) // 123039) % 32))))
    tl.store(out_ptr + tl.program_id(0), _v)


def t015_s0(out, ins):
    grid = (62995968,)
    t015_s0_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4])
    return out


@triton.jit
def t015_s1_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 8):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 7690) & ((((tl.program_id(0) % 256) * 7690) + ((_lv0 * 1024) + tl.arange(0, 1024))) < 1968624)), tl.load(in5_ptr + (tl.maximum(((((((((tl.program_id(0) % 256) * 7690) + ((_lv0 * 1024) + tl.arange(0, 1024))) // 123039) * 32) + (tl.program_id(0) // 256)) * 123039) + ((((tl.program_id(0) % 256) * 7690) + ((_lv0 * 1024) + tl.arange(0, 1024))) % 123039)) - tl.maximum(((((((((tl.program_id(0) % 256) * 7690) + ((_lv0 * 1024) + tl.arange(0, 1024))) // 123039) * 32) + (tl.program_id(0) // 256)) * 123039) + ((((tl.program_id(0) % 256) * 7690) + ((_lv0 * 1024) + tl.arange(0, 1024))) % 123039)) - 62995967, 0), 0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 7690) & ((((tl.program_id(0) % 256) * 7690) + ((_lv0 * 1024) + tl.arange(0, 1024))) < 1968624)), other=0.0), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t015_s1(out, ins):
    grid = (8192,)
    t015_s1_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5])
    return out


@triton.jit
def t015_s2_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr):
    _acc0 = tl.zeros([256], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 256) + tl.arange(0, 256)) < 256) & True), tl.load(in6_ptr + (((tl.program_id(0) * 256) + ((_lv0 * 256) + tl.arange(0, 256))) + 0 * tl.arange(0, 256)), mask=((((_lv0 * 256) + tl.arange(0, 256)) < 256) & True), other=0.0), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t015_s2(out, ins):
    grid = (32,)
    t015_s2_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6])
    return out


@triton.jit
def t015_s3_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 8):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 7690) & ((((tl.program_id(0) % 256) * 7690) + ((_lv0 * 1024) + tl.arange(0, 1024))) < 1968624)), ((tl.load(in5_ptr + (tl.maximum(((((((((tl.program_id(0) % 256) * 7690) + ((_lv0 * 1024) + tl.arange(0, 1024))) // 123039) * 32) + (tl.program_id(0) // 256)) * 123039) + ((((tl.program_id(0) % 256) * 7690) + ((_lv0 * 1024) + tl.arange(0, 1024))) % 123039)) - tl.maximum(((((((((tl.program_id(0) % 256) * 7690) + ((_lv0 * 1024) + tl.arange(0, 1024))) // 123039) * 32) + (tl.program_id(0) // 256)) * 123039) + ((((tl.program_id(0) % 256) * 7690) + ((_lv0 * 1024) + tl.arange(0, 1024))) % 123039)) - 62995967, 0), 0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 7690) & ((((tl.program_id(0) % 256) * 7690) + ((_lv0 * 1024) + tl.arange(0, 1024))) < 1968624)), other=0.0) - (tl.load(in7_ptr + (tl.maximum((tl.program_id(0) // 256) - tl.maximum((tl.program_id(0) // 256) - 31, 0), 0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 7690) & ((((tl.program_id(0) % 256) * 7690) + ((_lv0 * 1024) + tl.arange(0, 1024))) < 1968624)), other=0.0) * (1.0 * (1.0 / 1968624.0)))) * (tl.load(in5_ptr + (tl.maximum(((((((((tl.program_id(0) % 256) * 7690) + ((_lv0 * 1024) + tl.arange(0, 1024))) // 123039) * 32) + (tl.program_id(0) // 256)) * 123039) + ((((tl.program_id(0) % 256) * 7690) + ((_lv0 * 1024) + tl.arange(0, 1024))) % 123039)) - tl.maximum(((((((((tl.program_id(0) % 256) * 7690) + ((_lv0 * 1024) + tl.arange(0, 1024))) // 123039) * 32) + (tl.program_id(0) // 256)) * 123039) + ((((tl.program_id(0) % 256) * 7690) + ((_lv0 * 1024) + tl.arange(0, 1024))) % 123039)) - 62995967, 0), 0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 7690) & ((((tl.program_id(0) % 256) * 7690) + ((_lv0 * 1024) + tl.arange(0, 1024))) < 1968624)), other=0.0) - (tl.load(in7_ptr + (tl.maximum((tl.program_id(0) // 256) - tl.maximum((tl.program_id(0) // 256) - 31, 0), 0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 7690) & ((((tl.program_id(0) % 256) * 7690) + ((_lv0 * 1024) + tl.arange(0, 1024))) < 1968624)), other=0.0) * (1.0 * (1.0 / 1968624.0))))), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t015_s3(out, ins):
    grid = (8192,)
    t015_s3_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7])
    return out


@triton.jit
def t015_s4_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr):
    _acc0 = tl.zeros([256], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 256) + tl.arange(0, 256)) < 256) & True), tl.load(in8_ptr + (((tl.program_id(0) * 256) + ((_lv0 * 256) + tl.arange(0, 256))) + 0 * tl.arange(0, 256)), mask=((((_lv0 * 256) + tl.arange(0, 256)) < 256) & True), other=0.0), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t015_s4(out, ins):
    grid = (32,)
    t015_s4_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8])
    return out


@triton.jit
def t015_s5_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr):
    _acc0 = tl.zeros([1], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), ((((tl.load(in5_ptr + (tl.program_id(0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) - (tl.load(in7_ptr + (tl.maximum(((tl.program_id(0) // 123039) % 32) - tl.maximum(((tl.program_id(0) // 123039) % 32) - 31, 0), 0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) * (1.0 * (1.0 / 1968624.0)))) * (1.0 / tl.sqrt(((tl.load(in9_ptr + (tl.maximum(((tl.program_id(0) // 123039) % 32) - tl.maximum(((tl.program_id(0) // 123039) % 32) - 31, 0), 0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) * (1.0 * (1.0 / 1968624.0))) + (1.0 * (1.0 / 100000.0)))))) * tl.load(in3_ptr + (((tl.program_id(0) // 123039) % 32) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)) + tl.load(in4_ptr + (((tl.program_id(0) // 123039) % 32) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t015_s5(out, ins):
    grid = (62995968,)
    t015_s5_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9])
    return out


@triton.jit
def t015_s6_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr):
    _acc0 = tl.zeros([256], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 256) + tl.arange(0, 256)) < 481) & ((((tl.program_id(0) % 256) * 481) + ((_lv0 * 256) + tl.arange(0, 256))) < 123039)), tl.load(in10_ptr + (tl.maximum((((tl.program_id(0) // 256) * 123039) + (((tl.program_id(0) % 256) * 481) + ((_lv0 * 256) + tl.arange(0, 256)))) - tl.maximum((((tl.program_id(0) // 256) * 123039) + (((tl.program_id(0) % 256) * 481) + ((_lv0 * 256) + tl.arange(0, 256)))) - 62995967, 0), 0) + 0 * tl.arange(0, 256)), mask=((((_lv0 * 256) + tl.arange(0, 256)) < 481) & ((((tl.program_id(0) % 256) * 481) + ((_lv0 * 256) + tl.arange(0, 256))) < 123039)), other=0.0), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t015_s6(out, ins):
    grid = (131072,)
    t015_s6_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10])
    return out


@triton.jit
def t015_s7_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr):
    _acc0 = tl.zeros([256], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 256) + tl.arange(0, 256)) < 256) & True), tl.load(in11_ptr + (((tl.program_id(0) * 256) + ((_lv0 * 256) + tl.arange(0, 256))) + 0 * tl.arange(0, 256)), mask=((((_lv0 * 256) + tl.arange(0, 256)) < 256) & True), other=0.0), 0.0))
    _v = (tl.sum(_acc0, axis=0) * (1.0 * (1.0 / 123039.0)))
    tl.store(out_ptr + tl.program_id(0), _v)


def t015_s7(out, ins):
    grid = (512,)
    t015_s7_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11])
    return out


@triton.jit
def t015_s8_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr):
    _acc0 = tl.zeros([1], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), (tl.load(in10_ptr + ((((((((((tl.program_id(0) // 3937248) * 32) + ((tl.program_id(0) // 123039) % 32)) * 31) + ((tl.program_id(0) // 3969) % 31)) * 63) + ((tl.program_id(0) // 63) % 63)) * 63) + (tl.program_id(0) % 63)) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) - tl.load(in12_ptr + ((((tl.program_id(0) // 3937248) * 32) + ((tl.program_id(0) // 123039) % 32)) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t015_s8(out, ins):
    grid = (62995968,)
    t015_s8_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12])
    return out


def t015(out, ins):
    _t0 = torch.empty(62995968, device=ins[0].device, dtype=torch.float32)
    _t1 = torch.empty(8192, device=ins[0].device, dtype=torch.float32)
    _t2 = torch.empty(32, device=ins[0].device, dtype=torch.float32)
    _t3 = torch.empty(8192, device=ins[0].device, dtype=torch.float32)
    _t4 = torch.empty(32, device=ins[0].device, dtype=torch.float32)
    _t5 = torch.empty(62995968, device=ins[0].device, dtype=torch.float32)
    _t6 = torch.empty(131072, device=ins[0].device, dtype=torch.float32)
    _t7 = torch.empty(512, device=ins[0].device, dtype=torch.float32)
    t015_s0(_t0, list(ins))
    t015_s1(_t1, list(ins) + [_t0])
    t015_s2(_t2, list(ins) + [_t0, _t1])
    t015_s3(_t3, list(ins) + [_t0, _t1, _t2])
    t015_s4(_t4, list(ins) + [_t0, _t1, _t2, _t3])
    t015_s5(_t5, list(ins) + [_t0, _t1, _t2, _t3, _t4])
    t015_s6(_t6, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5])
    t015_s7(_t7, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6])
    t015_s8(out, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7])
    return out
