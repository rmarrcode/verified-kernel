import torch
import triton
import triton.language as tl


@triton.jit
def _mul_combine(a, b):
    return a * b


@triton.jit
def t023_s0_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr):
    _acc0 = tl.zeros([64], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 64) + tl.arange(0, 64)) < 81) & ((((((tl.program_id(0) // 900) % 22) + ((((_lv0 * 64) + tl.arange(0, 64)) // 9) % 3)) < 24) & ((((tl.program_id(0) // 30) % 30) + ((((_lv0 * 64) + tl.arange(0, 64)) // 3) % 3)) < 32)) & (((tl.program_id(0) % 30) + (((_lv0 * 64) + tl.arange(0, 64)) % 3)) < 32))), (tl.load(in0_ptr + ((((((((((tl.program_id(0) // 475200) * 3) + (((_lv0 * 64) + tl.arange(0, 64)) // 27)) * 24) + (((tl.program_id(0) // 900) % 22) + ((((_lv0 * 64) + tl.arange(0, 64)) // 9) % 3))) * 32) + (((tl.program_id(0) // 30) % 30) + ((((_lv0 * 64) + tl.arange(0, 64)) // 3) % 3))) * 32) + ((tl.program_id(0) % 30) + (((_lv0 * 64) + tl.arange(0, 64)) % 3))) + 0 * tl.arange(0, 64)), mask=((((_lv0 * 64) + tl.arange(0, 64)) < 81) & ((((((tl.program_id(0) // 900) % 22) + ((((_lv0 * 64) + tl.arange(0, 64)) // 9) % 3)) < 24) & ((((tl.program_id(0) // 30) % 30) + ((((_lv0 * 64) + tl.arange(0, 64)) // 3) % 3)) < 32)) & (((tl.program_id(0) % 30) + (((_lv0 * 64) + tl.arange(0, 64)) % 3)) < 32))), other=0.0) * tl.load(in1_ptr + (((((((((((tl.program_id(0) // 19800) % 24) * 3) + (((_lv0 * 64) + tl.arange(0, 64)) // 27)) * 3) + ((((_lv0 * 64) + tl.arange(0, 64)) // 9) % 3)) * 3) + ((((_lv0 * 64) + tl.arange(0, 64)) // 3) % 3)) * 3) + (((_lv0 * 64) + tl.arange(0, 64)) % 3)) + 0 * tl.arange(0, 64)), mask=((((_lv0 * 64) + tl.arange(0, 64)) < 81) & ((((((tl.program_id(0) // 900) % 22) + ((((_lv0 * 64) + tl.arange(0, 64)) // 9) % 3)) < 24) & ((((tl.program_id(0) // 30) % 30) + ((((_lv0 * 64) + tl.arange(0, 64)) // 3) % 3)) < 32)) & (((tl.program_id(0) % 30) + (((_lv0 * 64) + tl.arange(0, 64)) % 3)) < 32))), other=0.0)), 0.0))
    _v = (tl.sum(_acc0, axis=0) + tl.load(in2_ptr + (((tl.program_id(0) // 19800) % 24))))
    tl.store(out_ptr + tl.program_id(0), _v)


def t023_s0(out, ins):
    grid = (60825600,)
    t023_s0_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4])
    return out


@triton.jit
def t023_s1_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 59):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 59400) & True), tl.load(in5_ptr + (tl.maximum(((((((tl.program_id(0) // 8) * 24) + ((tl.program_id(0) % 8) * 3)) + (((_lv0 * 1024) + tl.arange(0, 1024)) // 19800)) * 19800) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 19800)) - tl.maximum(((((((tl.program_id(0) // 8) * 24) + ((tl.program_id(0) % 8) * 3)) + (((_lv0 * 1024) + tl.arange(0, 1024)) // 19800)) * 19800) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 19800)) - 60825599, 0), 0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 59400) & True), other=0.0), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t023_s1(out, ins):
    grid = (1024,)
    t023_s1_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5])
    return out


@triton.jit
def t023_s2_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 59):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 59400) & True), ((tl.load(in5_ptr + (tl.maximum(((((((tl.program_id(0) // 8) * 24) + ((tl.program_id(0) % 8) * 3)) + (((_lv0 * 1024) + tl.arange(0, 1024)) // 19800)) * 19800) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 19800)) - tl.maximum(((((((tl.program_id(0) // 8) * 24) + ((tl.program_id(0) % 8) * 3)) + (((_lv0 * 1024) + tl.arange(0, 1024)) // 19800)) * 19800) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 19800)) - 60825599, 0), 0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 59400) & True), other=0.0) - (tl.load(in6_ptr + (tl.program_id(0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 59400) & True), other=0.0) * (1.0 * (1.0 / 59400.0)))) * (tl.load(in5_ptr + (tl.maximum(((((((tl.program_id(0) // 8) * 24) + ((tl.program_id(0) % 8) * 3)) + (((_lv0 * 1024) + tl.arange(0, 1024)) // 19800)) * 19800) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 19800)) - tl.maximum(((((((tl.program_id(0) // 8) * 24) + ((tl.program_id(0) % 8) * 3)) + (((_lv0 * 1024) + tl.arange(0, 1024)) // 19800)) * 19800) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 19800)) - 60825599, 0), 0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 59400) & True), other=0.0) - (tl.load(in6_ptr + (tl.program_id(0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 59400) & True), other=0.0) * (1.0 * (1.0 / 59400.0))))), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t023_s2(out, ins):
    grid = (1024,)
    t023_s2_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6])
    return out


@triton.jit
def t023_s3_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr):
    _acc0 = tl.zeros([1], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), ((((tl.load(in5_ptr + (tl.program_id(0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) - (tl.load(in6_ptr + (tl.maximum((((tl.program_id(0) // 475200) * 8) + (((tl.program_id(0) // 19800) % 24) // 3)) - tl.maximum((((tl.program_id(0) // 475200) * 8) + (((tl.program_id(0) // 19800) % 24) // 3)) - 1023, 0), 0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) * (1.0 * (1.0 / 59400.0)))) * (1.0 / tl.sqrt(((tl.load(in7_ptr + (tl.maximum((((tl.program_id(0) // 475200) * 8) + (((tl.program_id(0) // 19800) % 24) // 3)) - tl.maximum((((tl.program_id(0) // 475200) * 8) + (((tl.program_id(0) // 19800) % 24) // 3)) - 1023, 0), 0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) * (1.0 * (1.0 / 59400.0))) + (1.0 * (1.0 / 100000.0)))))) * tl.load(in3_ptr + (((tl.program_id(0) // 19800) % 24) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)) + tl.load(in4_ptr + (((tl.program_id(0) // 19800) % 24) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t023_s3(out, ins):
    grid = (60825600,)
    t023_s3_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7])
    return out


@triton.jit
def t023_s4_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 465):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 475200) & True), tl.load(in8_ptr + (((tl.program_id(0) * 475200) + ((_lv0 * 1024) + tl.arange(0, 1024))) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 475200) & True), other=0.0), 0.0))
    _v = (tl.sum(_acc0, axis=0) * (1.0 * (1.0 / 475200.0)))
    tl.store(out_ptr + tl.program_id(0), _v)


def t023_s4(out, ins):
    grid = (128,)
    t023_s4_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8])
    return out


def t023(out, ins):
    _t0 = torch.empty(60825600, device=ins[0].device, dtype=torch.float32)
    _t1 = torch.empty(1024, device=ins[0].device, dtype=torch.float32)
    _t2 = torch.empty(1024, device=ins[0].device, dtype=torch.float32)
    _t3 = torch.empty(60825600, device=ins[0].device, dtype=torch.float32)
    t023_s0(_t0, list(ins))
    t023_s1(_t1, list(ins) + [_t0])
    t023_s2(_t2, list(ins) + [_t0, _t1])
    t023_s3(_t3, list(ins) + [_t0, _t1, _t2])
    t023_s4(out, list(ins) + [_t0, _t1, _t2, _t3])
    return out
