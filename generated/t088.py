import torch
import triton
import triton.language as tl


@triton.jit
def _mul_combine(a, b):
    return a * b


@triton.jit
def t088_s0_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 8):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 8192) & True), (tl.load(in0_ptr + ((((tl.program_id(0) // 8192) * 8192) + ((_lv0 * 1024) + tl.arange(0, 1024))) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 8192) & True), other=0.0) * tl.load(in1_ptr + ((((tl.program_id(0) % 8192) * 8192) + ((_lv0 * 1024) + tl.arange(0, 1024))) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 8192) & True), other=0.0)), 0.0))
    _v = (tl.sum(_acc0, axis=0) + tl.load(in2_ptr + ((tl.program_id(0) % 8192))))
    tl.store(out_ptr + tl.program_id(0), _v)


def t088_s0(out, ins):
    grid = (8388608,)
    t088_s0_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5])
    return out


@triton.jit
def t088_s1_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr):
    _acc0 = tl.zeros([32], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 32) + tl.arange(0, 32)) < 32) & True), tl.load(in6_ptr + (tl.maximum(((((tl.program_id(0) // 256) * 8192) + ((tl.program_id(0) % 256) * 32)) + ((_lv0 * 32) + tl.arange(0, 32))) - tl.maximum(((((tl.program_id(0) // 256) * 8192) + ((tl.program_id(0) % 256) * 32)) + ((_lv0 * 32) + tl.arange(0, 32))) - 8388607, 0), 0) + 0 * tl.arange(0, 32)), mask=((((_lv0 * 32) + tl.arange(0, 32)) < 32) & True), other=0.0), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t088_s1(out, ins):
    grid = (262144,)
    t088_s1_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6])
    return out


@triton.jit
def t088_s2_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr):
    _acc0 = tl.zeros([32], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 32) + tl.arange(0, 32)) < 32) & True), ((tl.load(in6_ptr + (tl.maximum(((((tl.program_id(0) // 256) * 8192) + ((tl.program_id(0) % 256) * 32)) + ((_lv0 * 32) + tl.arange(0, 32))) - tl.maximum(((((tl.program_id(0) // 256) * 8192) + ((tl.program_id(0) % 256) * 32)) + ((_lv0 * 32) + tl.arange(0, 32))) - 8388607, 0), 0) + 0 * tl.arange(0, 32)), mask=((((_lv0 * 32) + tl.arange(0, 32)) < 32) & True), other=0.0) - (tl.load(in7_ptr + (tl.program_id(0) + 0 * tl.arange(0, 32)), mask=((((_lv0 * 32) + tl.arange(0, 32)) < 32) & True), other=0.0) * (1.0 * (1.0 / 32.0)))) * (tl.load(in6_ptr + (tl.maximum(((((tl.program_id(0) // 256) * 8192) + ((tl.program_id(0) % 256) * 32)) + ((_lv0 * 32) + tl.arange(0, 32))) - tl.maximum(((((tl.program_id(0) // 256) * 8192) + ((tl.program_id(0) % 256) * 32)) + ((_lv0 * 32) + tl.arange(0, 32))) - 8388607, 0), 0) + 0 * tl.arange(0, 32)), mask=((((_lv0 * 32) + tl.arange(0, 32)) < 32) & True), other=0.0) - (tl.load(in7_ptr + (tl.program_id(0) + 0 * tl.arange(0, 32)), mask=((((_lv0 * 32) + tl.arange(0, 32)) < 32) & True), other=0.0) * (1.0 * (1.0 / 32.0))))), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t088_s2(out, ins):
    grid = (262144,)
    t088_s2_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7])
    return out


@triton.jit
def t088_s3_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr):
    _acc0 = tl.zeros([1], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), ((((tl.load(in6_ptr + (tl.program_id(0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) - (tl.load(in7_ptr + (tl.maximum((((tl.program_id(0) // 8192) * 256) + ((tl.program_id(0) % 8192) // 32)) - tl.maximum((((tl.program_id(0) // 8192) * 256) + ((tl.program_id(0) % 8192) // 32)) - 262143, 0), 0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) * (1.0 * (1.0 / 32.0)))) * (1.0 / tl.sqrt(((tl.load(in8_ptr + (tl.maximum((((tl.program_id(0) // 8192) * 256) + ((tl.program_id(0) % 8192) // 32)) - tl.maximum((((tl.program_id(0) // 8192) * 256) + ((tl.program_id(0) % 8192) // 32)) - 262143, 0), 0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) * (1.0 * (1.0 / 32.0))) + (1.0 * (1.0 / 100000.0)))))) * tl.load(in3_ptr + ((tl.program_id(0) % 8192) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)) + tl.load(in4_ptr + ((tl.program_id(0) % 8192) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t088_s3(out, ins):
    grid = (8388608,)
    t088_s3_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8])
    return out


@triton.jit
def t088_s4_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr):
    _acc0 = tl.zeros([1], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), (1.0 / ((1.0 * (1.0 / 1.0)) + tl.exp(((0.0 * (1.0 / 1.0)) - tl.load(in9_ptr + ((((tl.program_id(0) // 8192) * 8192) + (tl.program_id(0) % 8192)) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0))))), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t088_s4(out, ins):
    grid = (8388608,)
    t088_s4_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9])
    return out


@triton.jit
def t088_s5_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr):
    _acc0 = tl.zeros([1], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), (tl.load(in9_ptr + ((((tl.program_id(0) // 8192) * 8192) + (tl.program_id(0) % 8192)) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) * tl.load(in10_ptr + ((((tl.program_id(0) // 8192) * 8192) + (tl.program_id(0) % 8192)) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t088_s5(out, ins):
    grid = (8388608,)
    t088_s5_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10])
    return out


@triton.jit
def t088_s6_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr):
    _acc0 = tl.zeros([1], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), (tl.load(in11_ptr + ((((tl.program_id(0) // 8192) * 8192) + (tl.program_id(0) % 8192)) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) * tl.load(in5_ptr + ((tl.program_id(0) % 8192) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t088_s6(out, ins):
    grid = (8388608,)
    t088_s6_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11])
    return out


@triton.jit
def t088_s7_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr):
    _acc0 = tl.zeros([1], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), (1.0 / ((1.0 * (1.0 / 1.0)) + tl.exp(((0.0 * (1.0 / 1.0)) - tl.load(in12_ptr + ((((tl.program_id(0) // 8192) * 8192) + (tl.program_id(0) % 8192)) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0))))), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t088_s7(out, ins):
    grid = (8388608,)
    t088_s7_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12])
    return out


@triton.jit
def t088_s8_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr, in12_ptr, in13_ptr):
    _acc0 = tl.zeros([1], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), (tl.load(in12_ptr + ((((tl.program_id(0) // 8192) * 8192) + (tl.program_id(0) % 8192)) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) * tl.load(in13_ptr + ((((tl.program_id(0) // 8192) * 8192) + (tl.program_id(0) % 8192)) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t088_s8(out, ins):
    grid = (8388608,)
    t088_s8_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11], ins[12], ins[13])
    return out


def t088(out, ins):
    _t0 = torch.empty(8388608, device=ins[0].device, dtype=torch.float32)
    _t1 = torch.empty(262144, device=ins[0].device, dtype=torch.float32)
    _t2 = torch.empty(262144, device=ins[0].device, dtype=torch.float32)
    _t3 = torch.empty(8388608, device=ins[0].device, dtype=torch.float32)
    _t4 = torch.empty(8388608, device=ins[0].device, dtype=torch.float32)
    _t5 = torch.empty(8388608, device=ins[0].device, dtype=torch.float32)
    _t6 = torch.empty(8388608, device=ins[0].device, dtype=torch.float32)
    _t7 = torch.empty(8388608, device=ins[0].device, dtype=torch.float32)
    t088_s0(_t0, list(ins))
    t088_s1(_t1, list(ins) + [_t0])
    t088_s2(_t2, list(ins) + [_t0, _t1])
    t088_s3(_t3, list(ins) + [_t0, _t1, _t2])
    t088_s4(_t4, list(ins) + [_t0, _t1, _t2, _t3])
    t088_s5(_t5, list(ins) + [_t0, _t1, _t2, _t3, _t4])
    t088_s6(_t6, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5])
    t088_s7(_t7, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6])
    t088_s8(out, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6, _t7])
    return out
