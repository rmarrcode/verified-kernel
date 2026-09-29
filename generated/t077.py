import torch
import triton
import triton.language as tl


@triton.jit
def _mul_combine(a, b):
    return a * b


@triton.jit
def t077_s0_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 8):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 8000) & (((((((((((((_lv0 * 1024) + tl.arange(0, 1024)) // 25) % 5) <= ((tl.program_id(0) // 1296) % 20)) & (0 == 0)) & (tl.maximum(((tl.program_id(0) // 1296) % 20) - ((((_lv0 * 1024) + tl.arange(0, 1024)) // 25) % 5), 0) < 16)) & (((((_lv0 * 1024) + tl.arange(0, 1024)) // 5) % 5) <= ((tl.program_id(0) // 36) % 36))) & (0 == 0)) & (tl.maximum(((tl.program_id(0) // 36) % 36) - ((((_lv0 * 1024) + tl.arange(0, 1024)) // 5) % 5), 0) < 32)) & ((((_lv0 * 1024) + tl.arange(0, 1024)) % 5) <= (tl.program_id(0) % 36))) & (0 == 0)) & (tl.maximum((tl.program_id(0) % 36) - (((_lv0 * 1024) + tl.arange(0, 1024)) % 5), 0) < 32))), (tl.load(in0_ptr + ((((((((((tl.program_id(0) // 3317760) * 64) + (((((tl.program_id(0) // 25920) % 128) // 128) * 64) + (((_lv0 * 1024) + tl.arange(0, 1024)) // 125))) * 16) + tl.maximum(((tl.program_id(0) // 1296) % 20) - ((((_lv0 * 1024) + tl.arange(0, 1024)) // 25) % 5), 0)) * 32) + tl.maximum(((tl.program_id(0) // 36) % 36) - ((((_lv0 * 1024) + tl.arange(0, 1024)) // 5) % 5), 0)) * 32) + tl.maximum((tl.program_id(0) % 36) - (((_lv0 * 1024) + tl.arange(0, 1024)) % 5), 0)) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 8000) & (((((((((((((_lv0 * 1024) + tl.arange(0, 1024)) // 25) % 5) <= ((tl.program_id(0) // 1296) % 20)) & (0 == 0)) & (tl.maximum(((tl.program_id(0) // 1296) % 20) - ((((_lv0 * 1024) + tl.arange(0, 1024)) // 25) % 5), 0) < 16)) & (((((_lv0 * 1024) + tl.arange(0, 1024)) // 5) % 5) <= ((tl.program_id(0) // 36) % 36))) & (0 == 0)) & (tl.maximum(((tl.program_id(0) // 36) % 36) - ((((_lv0 * 1024) + tl.arange(0, 1024)) // 5) % 5), 0) < 32)) & ((((_lv0 * 1024) + tl.arange(0, 1024)) % 5) <= (tl.program_id(0) % 36))) & (0 == 0)) & (tl.maximum((tl.program_id(0) % 36) - (((_lv0 * 1024) + tl.arange(0, 1024)) % 5), 0) < 32))), other=0.0) * tl.load(in1_ptr + ((((((((((((((tl.program_id(0) // 25920) % 128) // 128) * 64) + (((_lv0 * 1024) + tl.arange(0, 1024)) // 125)) * 128) + (((tl.program_id(0) // 25920) % 128) % 128)) * 5) + ((((_lv0 * 1024) + tl.arange(0, 1024)) // 25) % 5)) * 5) + ((((_lv0 * 1024) + tl.arange(0, 1024)) // 5) % 5)) * 5) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 5)) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 8000) & (((((((((((((_lv0 * 1024) + tl.arange(0, 1024)) // 25) % 5) <= ((tl.program_id(0) // 1296) % 20)) & (0 == 0)) & (tl.maximum(((tl.program_id(0) // 1296) % 20) - ((((_lv0 * 1024) + tl.arange(0, 1024)) // 25) % 5), 0) < 16)) & (((((_lv0 * 1024) + tl.arange(0, 1024)) // 5) % 5) <= ((tl.program_id(0) // 36) % 36))) & (0 == 0)) & (tl.maximum(((tl.program_id(0) // 36) % 36) - ((((_lv0 * 1024) + tl.arange(0, 1024)) // 5) % 5), 0) < 32)) & ((((_lv0 * 1024) + tl.arange(0, 1024)) % 5) <= (tl.program_id(0) % 36))) & (0 == 0)) & (tl.maximum((tl.program_id(0) % 36) - (((_lv0 * 1024) + tl.arange(0, 1024)) % 5), 0) < 32))), other=0.0)), 0.0))
    _v = ((tl.sum(_acc0, axis=0) + tl.load(in2_ptr + (((tl.program_id(0) // 25920) % 128)))) * (2.0 * (1.0 / 1.0)))
    tl.store(out_ptr + tl.program_id(0), _v)


def t077_s0(out, ins):
    grid = (53084160,)
    t077_s0_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4])
    return out


@triton.jit
def t077_s1_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 405):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 414720) & True), tl.load(in5_ptr + (tl.maximum((((((((_lv0 * 1024) + tl.arange(0, 1024)) // 25920) * 128) + tl.program_id(0)) * 25920) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 25920)) - tl.maximum((((((((_lv0 * 1024) + tl.arange(0, 1024)) // 25920) * 128) + tl.program_id(0)) * 25920) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 25920)) - 53084159, 0), 0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 414720) & True), other=0.0), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t077_s1(out, ins):
    grid = (128,)
    t077_s1_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5])
    return out


@triton.jit
def t077_s2_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 405):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 414720) & True), ((tl.load(in5_ptr + (tl.maximum((((((((_lv0 * 1024) + tl.arange(0, 1024)) // 25920) * 128) + tl.program_id(0)) * 25920) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 25920)) - tl.maximum((((((((_lv0 * 1024) + tl.arange(0, 1024)) // 25920) * 128) + tl.program_id(0)) * 25920) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 25920)) - 53084159, 0), 0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 414720) & True), other=0.0) - (tl.load(in6_ptr + (tl.program_id(0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 414720) & True), other=0.0) * (1.0 * (1.0 / 414720.0)))) * (tl.load(in5_ptr + (tl.maximum((((((((_lv0 * 1024) + tl.arange(0, 1024)) // 25920) * 128) + tl.program_id(0)) * 25920) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 25920)) - tl.maximum((((((((_lv0 * 1024) + tl.arange(0, 1024)) // 25920) * 128) + tl.program_id(0)) * 25920) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 25920)) - 53084159, 0), 0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 414720) & True), other=0.0) - (tl.load(in6_ptr + (tl.program_id(0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 414720) & True), other=0.0) * (1.0 * (1.0 / 414720.0))))), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t077_s2(out, ins):
    grid = (128,)
    t077_s2_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6])
    return out


@triton.jit
def t077_s3_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr):
    _acc0 = tl.zeros([1], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), ((((tl.load(in5_ptr + (tl.program_id(0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) - (tl.load(in6_ptr + (tl.maximum(((tl.program_id(0) // 25920) % 128) - tl.maximum(((tl.program_id(0) // 25920) % 128) - 127, 0), 0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) * (1.0 * (1.0 / 414720.0)))) * (1.0 / tl.sqrt(((tl.load(in7_ptr + (tl.maximum(((tl.program_id(0) // 25920) % 128) - tl.maximum(((tl.program_id(0) // 25920) % 128) - 127, 0), 0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) * (1.0 * (1.0 / 414720.0))) + (1.0 * (1.0 / 100000.0)))))) * tl.load(in3_ptr + (((tl.program_id(0) // 25920) % 128) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)) + tl.load(in4_ptr + (((tl.program_id(0) // 25920) % 128) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t077_s3(out, ins):
    grid = (53084160,)
    t077_s3_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7])
    return out


@triton.jit
def t077_s4_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 26):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 25920) & True), tl.load(in8_ptr + (((tl.program_id(0) * 25920) + ((_lv0 * 1024) + tl.arange(0, 1024))) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 25920) & True), other=0.0), 0.0))
    _v = (tl.sum(_acc0, axis=0) * (1.0 * (1.0 / 25920.0)))
    tl.store(out_ptr + tl.program_id(0), _v)


def t077_s4(out, ins):
    grid = (2048,)
    t077_s4_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8])
    return out


def t077(out, ins):
    _t0 = torch.empty(53084160, device=ins[0].device, dtype=torch.float32)
    _t1 = torch.empty(128, device=ins[0].device, dtype=torch.float32)
    _t2 = torch.empty(128, device=ins[0].device, dtype=torch.float32)
    _t3 = torch.empty(53084160, device=ins[0].device, dtype=torch.float32)
    t077_s0(_t0, list(ins))
    t077_s1(_t1, list(ins) + [_t0])
    t077_s2(_t2, list(ins) + [_t0, _t1])
    t077_s3(_t3, list(ins) + [_t0, _t1, _t2])
    t077_s4(out, list(ins) + [_t0, _t1, _t2, _t3])
    return out
