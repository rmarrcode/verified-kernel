import torch
import triton
import triton.language as tl


@triton.jit
def _mul_combine(a, b):
    return a * b


@triton.jit
def t027_s0_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr):
    _acc0 = tl.zeros([128], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 128) + tl.arange(0, 128)) < 192) & ((((((tl.program_id(0) // 841) % 13) + ((((_lv0 * 128) + tl.arange(0, 128)) // 16) % 4)) < 16) & ((((tl.program_id(0) // 29) % 29) + ((((_lv0 * 128) + tl.arange(0, 128)) // 4) % 4)) < 32)) & (((tl.program_id(0) % 29) + (((_lv0 * 128) + tl.arange(0, 128)) % 4)) < 32))), (tl.load(in0_ptr + ((((((((((tl.program_id(0) // 174928) * 3) + (((_lv0 * 128) + tl.arange(0, 128)) // 64)) * 16) + (((tl.program_id(0) // 841) % 13) + ((((_lv0 * 128) + tl.arange(0, 128)) // 16) % 4))) * 32) + (((tl.program_id(0) // 29) % 29) + ((((_lv0 * 128) + tl.arange(0, 128)) // 4) % 4))) * 32) + ((tl.program_id(0) % 29) + (((_lv0 * 128) + tl.arange(0, 128)) % 4))) + 0 * tl.arange(0, 128)), mask=((((_lv0 * 128) + tl.arange(0, 128)) < 192) & ((((((tl.program_id(0) // 841) % 13) + ((((_lv0 * 128) + tl.arange(0, 128)) // 16) % 4)) < 16) & ((((tl.program_id(0) // 29) % 29) + ((((_lv0 * 128) + tl.arange(0, 128)) // 4) % 4)) < 32)) & (((tl.program_id(0) % 29) + (((_lv0 * 128) + tl.arange(0, 128)) % 4)) < 32))), other=0.0) * tl.load(in1_ptr + (((((((((((tl.program_id(0) // 10933) % 16) * 3) + (((_lv0 * 128) + tl.arange(0, 128)) // 64)) * 4) + ((((_lv0 * 128) + tl.arange(0, 128)) // 16) % 4)) * 4) + ((((_lv0 * 128) + tl.arange(0, 128)) // 4) % 4)) * 4) + (((_lv0 * 128) + tl.arange(0, 128)) % 4)) + 0 * tl.arange(0, 128)), mask=((((_lv0 * 128) + tl.arange(0, 128)) < 192) & ((((((tl.program_id(0) // 841) % 13) + ((((_lv0 * 128) + tl.arange(0, 128)) // 16) % 4)) < 16) & ((((tl.program_id(0) // 29) % 29) + ((((_lv0 * 128) + tl.arange(0, 128)) // 4) % 4)) < 32)) & (((tl.program_id(0) % 29) + (((_lv0 * 128) + tl.arange(0, 128)) % 4)) < 32))), other=0.0)), 0.0))
    _v = (((tl.sum(_acc0, axis=0) + tl.load(in2_ptr + (((tl.program_id(0) // 10933) % 16)))) * tl.minimum(tl.maximum(((tl.sum(_acc0, axis=0) + tl.load(in2_ptr + (((tl.program_id(0) // 10933) % 16)))) + (3.0 * (1.0 / 1.0))), (0.0 * (1.0 / 1.0))), (6.0 * (1.0 / 1.0)))) / (6.0 * (1.0 / 1.0)))
    tl.store(out_ptr + tl.program_id(0), _v)


def t027_s0(out, ins):
    grid = (179126272,)
    t027_s0_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4])
    return out


@triton.jit
def t027_s1_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 43):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 43732) & True), tl.load(in5_ptr + (tl.maximum(((((((tl.program_id(0) // 4) * 16) + ((tl.program_id(0) % 4) * 4)) + (((_lv0 * 1024) + tl.arange(0, 1024)) // 10933)) * 10933) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 10933)) - tl.maximum(((((((tl.program_id(0) // 4) * 16) + ((tl.program_id(0) % 4) * 4)) + (((_lv0 * 1024) + tl.arange(0, 1024)) // 10933)) * 10933) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 10933)) - 179126271, 0), 0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 43732) & True), other=0.0), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t027_s1(out, ins):
    grid = (4096,)
    t027_s1_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5])
    return out


@triton.jit
def t027_s2_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 43):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 43732) & True), ((tl.load(in5_ptr + (tl.maximum(((((((tl.program_id(0) // 4) * 16) + ((tl.program_id(0) % 4) * 4)) + (((_lv0 * 1024) + tl.arange(0, 1024)) // 10933)) * 10933) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 10933)) - tl.maximum(((((((tl.program_id(0) // 4) * 16) + ((tl.program_id(0) % 4) * 4)) + (((_lv0 * 1024) + tl.arange(0, 1024)) // 10933)) * 10933) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 10933)) - 179126271, 0), 0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 43732) & True), other=0.0) - (tl.load(in6_ptr + (tl.program_id(0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 43732) & True), other=0.0) * (1.0 * (1.0 / 43732.0)))) * (tl.load(in5_ptr + (tl.maximum(((((((tl.program_id(0) // 4) * 16) + ((tl.program_id(0) % 4) * 4)) + (((_lv0 * 1024) + tl.arange(0, 1024)) // 10933)) * 10933) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 10933)) - tl.maximum(((((((tl.program_id(0) // 4) * 16) + ((tl.program_id(0) % 4) * 4)) + (((_lv0 * 1024) + tl.arange(0, 1024)) // 10933)) * 10933) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 10933)) - 179126271, 0), 0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 43732) & True), other=0.0) - (tl.load(in6_ptr + (tl.program_id(0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 43732) & True), other=0.0) * (1.0 * (1.0 / 43732.0))))), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t027_s2(out, ins):
    grid = (4096,)
    t027_s2_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6])
    return out


@triton.jit
def t027_s3_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr):
    _acc0 = tl.zeros([1], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), ((((tl.load(in5_ptr + (tl.program_id(0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) - (tl.load(in6_ptr + (tl.maximum((((tl.program_id(0) // 174928) * 4) + (((tl.program_id(0) // 10933) % 16) // 4)) - tl.maximum((((tl.program_id(0) // 174928) * 4) + (((tl.program_id(0) // 10933) % 16) // 4)) - 4095, 0), 0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) * (1.0 * (1.0 / 43732.0)))) * (1.0 / tl.sqrt(((tl.load(in7_ptr + (tl.maximum((((tl.program_id(0) // 174928) * 4) + (((tl.program_id(0) // 10933) % 16) // 4)) - tl.maximum((((tl.program_id(0) // 174928) * 4) + (((tl.program_id(0) // 10933) % 16) // 4)) - 4095, 0), 0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) * (1.0 * (1.0 / 43732.0))) + (1.0 * (1.0 / 100000.0)))))) * tl.load(in3_ptr + (((tl.program_id(0) // 10933) % 16) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)) + tl.load(in4_ptr + (((tl.program_id(0) // 10933) % 16) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t027_s3(out, ins):
    grid = (179126272,)
    t027_s3_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7])
    return out


@triton.jit
def t027_s4_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 11):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 10933) & True), tl.load(in8_ptr + (((tl.program_id(0) * 10933) + ((_lv0 * 1024) + tl.arange(0, 1024))) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 10933) & True), other=0.0), 0.0))
    _v = (tl.sum(_acc0, axis=0) * (1.0 * (1.0 / 10933.0)))
    tl.store(out_ptr + tl.program_id(0), _v)


def t027_s4(out, ins):
    grid = (16384,)
    t027_s4_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8])
    return out


def t027(out, ins):
    _t0 = torch.empty(179126272, device=ins[0].device, dtype=torch.float32)
    _t1 = torch.empty(4096, device=ins[0].device, dtype=torch.float32)
    _t2 = torch.empty(4096, device=ins[0].device, dtype=torch.float32)
    _t3 = torch.empty(179126272, device=ins[0].device, dtype=torch.float32)
    t027_s0(_t0, list(ins))
    t027_s1(_t1, list(ins) + [_t0])
    t027_s2(_t2, list(ins) + [_t0, _t1])
    t027_s3(_t3, list(ins) + [_t0, _t1, _t2])
    t027_s4(out, list(ins) + [_t0, _t1, _t2, _t3])
    return out
