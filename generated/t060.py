import torch
import triton
import triton.language as tl


@triton.jit
def _mul_combine(a, b):
    return a * b


@triton.jit
def t060_s0_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr):
    _acc0 = tl.zeros([64], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 64) + tl.arange(0, 64)) < 81) & (((((((((((((_lv0 * 64) + tl.arange(0, 64)) // 9) % 3) <= (((tl.program_id(0) // 3969) % 31) + 1)) & ((tl.maximum((((tl.program_id(0) // 3969) % 31) + 1) - ((((_lv0 * 64) + tl.arange(0, 64)) // 9) % 3), 0) % 2) == 0)) & ((tl.maximum((((tl.program_id(0) // 3969) % 31) + 1) - ((((_lv0 * 64) + tl.arange(0, 64)) // 9) % 3), 0) // 2) < 16)) & (((((_lv0 * 64) + tl.arange(0, 64)) // 3) % 3) <= (((tl.program_id(0) // 63) % 63) + 1))) & ((tl.maximum((((tl.program_id(0) // 63) % 63) + 1) - ((((_lv0 * 64) + tl.arange(0, 64)) // 3) % 3), 0) % 2) == 0)) & ((tl.maximum((((tl.program_id(0) // 63) % 63) + 1) - ((((_lv0 * 64) + tl.arange(0, 64)) // 3) % 3), 0) // 2) < 32)) & ((((_lv0 * 64) + tl.arange(0, 64)) % 3) <= ((tl.program_id(0) % 63) + 1))) & ((tl.maximum(((tl.program_id(0) % 63) + 1) - (((_lv0 * 64) + tl.arange(0, 64)) % 3), 0) % 2) == 0)) & ((tl.maximum(((tl.program_id(0) % 63) + 1) - (((_lv0 * 64) + tl.arange(0, 64)) % 3), 0) // 2) < 32))), (tl.load(in0_ptr + ((((((((((tl.program_id(0) // 1968624) * 3) + (((((tl.program_id(0) // 123039) % 16) // 16) * 3) + (((_lv0 * 64) + tl.arange(0, 64)) // 27))) * 16) + (tl.maximum((((tl.program_id(0) // 3969) % 31) + 1) - ((((_lv0 * 64) + tl.arange(0, 64)) // 9) % 3), 0) // 2)) * 32) + (tl.maximum((((tl.program_id(0) // 63) % 63) + 1) - ((((_lv0 * 64) + tl.arange(0, 64)) // 3) % 3), 0) // 2)) * 32) + (tl.maximum(((tl.program_id(0) % 63) + 1) - (((_lv0 * 64) + tl.arange(0, 64)) % 3), 0) // 2)) + 0 * tl.arange(0, 64)), mask=((((_lv0 * 64) + tl.arange(0, 64)) < 81) & (((((((((((((_lv0 * 64) + tl.arange(0, 64)) // 9) % 3) <= (((tl.program_id(0) // 3969) % 31) + 1)) & ((tl.maximum((((tl.program_id(0) // 3969) % 31) + 1) - ((((_lv0 * 64) + tl.arange(0, 64)) // 9) % 3), 0) % 2) == 0)) & ((tl.maximum((((tl.program_id(0) // 3969) % 31) + 1) - ((((_lv0 * 64) + tl.arange(0, 64)) // 9) % 3), 0) // 2) < 16)) & (((((_lv0 * 64) + tl.arange(0, 64)) // 3) % 3) <= (((tl.program_id(0) // 63) % 63) + 1))) & ((tl.maximum((((tl.program_id(0) // 63) % 63) + 1) - ((((_lv0 * 64) + tl.arange(0, 64)) // 3) % 3), 0) % 2) == 0)) & ((tl.maximum((((tl.program_id(0) // 63) % 63) + 1) - ((((_lv0 * 64) + tl.arange(0, 64)) // 3) % 3), 0) // 2) < 32)) & ((((_lv0 * 64) + tl.arange(0, 64)) % 3) <= ((tl.program_id(0) % 63) + 1))) & ((tl.maximum(((tl.program_id(0) % 63) + 1) - (((_lv0 * 64) + tl.arange(0, 64)) % 3), 0) % 2) == 0)) & ((tl.maximum(((tl.program_id(0) % 63) + 1) - (((_lv0 * 64) + tl.arange(0, 64)) % 3), 0) // 2) < 32))), other=0.0) * tl.load(in1_ptr + ((((((((((((((tl.program_id(0) // 123039) % 16) // 16) * 3) + (((_lv0 * 64) + tl.arange(0, 64)) // 27)) * 16) + (((tl.program_id(0) // 123039) % 16) % 16)) * 3) + ((((_lv0 * 64) + tl.arange(0, 64)) // 9) % 3)) * 3) + ((((_lv0 * 64) + tl.arange(0, 64)) // 3) % 3)) * 3) + (((_lv0 * 64) + tl.arange(0, 64)) % 3)) + 0 * tl.arange(0, 64)), mask=((((_lv0 * 64) + tl.arange(0, 64)) < 81) & (((((((((((((_lv0 * 64) + tl.arange(0, 64)) // 9) % 3) <= (((tl.program_id(0) // 3969) % 31) + 1)) & ((tl.maximum((((tl.program_id(0) // 3969) % 31) + 1) - ((((_lv0 * 64) + tl.arange(0, 64)) // 9) % 3), 0) % 2) == 0)) & ((tl.maximum((((tl.program_id(0) // 3969) % 31) + 1) - ((((_lv0 * 64) + tl.arange(0, 64)) // 9) % 3), 0) // 2) < 16)) & (((((_lv0 * 64) + tl.arange(0, 64)) // 3) % 3) <= (((tl.program_id(0) // 63) % 63) + 1))) & ((tl.maximum((((tl.program_id(0) // 63) % 63) + 1) - ((((_lv0 * 64) + tl.arange(0, 64)) // 3) % 3), 0) % 2) == 0)) & ((tl.maximum((((tl.program_id(0) // 63) % 63) + 1) - ((((_lv0 * 64) + tl.arange(0, 64)) // 3) % 3), 0) // 2) < 32)) & ((((_lv0 * 64) + tl.arange(0, 64)) % 3) <= ((tl.program_id(0) % 63) + 1))) & ((tl.maximum(((tl.program_id(0) % 63) + 1) - (((_lv0 * 64) + tl.arange(0, 64)) % 3), 0) % 2) == 0)) & ((tl.maximum(((tl.program_id(0) % 63) + 1) - (((_lv0 * 64) + tl.arange(0, 64)) % 3), 0) // 2) < 32))), other=0.0)), 0.0))
    _v = (tl.sum(_acc0, axis=0) + tl.load(in2_ptr + (((tl.program_id(0) // 123039) % 16))))
    tl.store(out_ptr + tl.program_id(0), _v)


def t060_s0(out, ins):
    grid = (251983872,)
    t060_s0_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4])
    return out


@triton.jit
def t060_s1_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr):
    _acc0 = tl.zeros([1], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), (1.0 / ((1.0 * (1.0 / 1.0)) + tl.exp(((0.0 * (1.0 / 1.0)) - tl.load(in5_ptr + ((((((((((tl.program_id(0) // 1968624) * 16) + ((tl.program_id(0) // 123039) % 16)) * 31) + ((tl.program_id(0) // 3969) % 31)) * 63) + ((tl.program_id(0) // 63) % 63)) * 63) + (tl.program_id(0) % 63)) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0))))), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t060_s1(out, ins):
    grid = (251983872,)
    t060_s1_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5])
    return out


@triton.jit
def t060_s2_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr):
    _acc0 = tl.zeros([1], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), (tl.load(in6_ptr + ((((((((((tl.program_id(0) // 1968624) * 16) + ((tl.program_id(0) // 123039) % 16)) * 31) + ((tl.program_id(0) // 3969) % 31)) * 63) + ((tl.program_id(0) // 63) % 63)) * 63) + (tl.program_id(0) % 63)) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) * tl.load(in5_ptr + ((((((((((tl.program_id(0) // 1968624) * 16) + ((tl.program_id(0) // 123039) % 16)) * 31) + ((tl.program_id(0) // 3969) % 31)) * 63) + ((tl.program_id(0) // 63) % 63)) * 63) + (tl.program_id(0) % 63)) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t060_s2(out, ins):
    grid = (251983872,)
    t060_s2_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6])
    return out


@triton.jit
def t060_s3_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 481):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 492156) & True), tl.load(in7_ptr + (tl.maximum(((((((tl.program_id(0) // 4) * 16) + ((tl.program_id(0) % 4) * 4)) + (((_lv0 * 1024) + tl.arange(0, 1024)) // 123039)) * 123039) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 123039)) - tl.maximum(((((((tl.program_id(0) // 4) * 16) + ((tl.program_id(0) % 4) * 4)) + (((_lv0 * 1024) + tl.arange(0, 1024)) // 123039)) * 123039) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 123039)) - 251983871, 0), 0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 492156) & True), other=0.0), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t060_s3(out, ins):
    grid = (512,)
    t060_s3_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7])
    return out


@triton.jit
def t060_s4_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 481):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 492156) & True), ((tl.load(in7_ptr + (tl.maximum(((((((tl.program_id(0) // 4) * 16) + ((tl.program_id(0) % 4) * 4)) + (((_lv0 * 1024) + tl.arange(0, 1024)) // 123039)) * 123039) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 123039)) - tl.maximum(((((((tl.program_id(0) // 4) * 16) + ((tl.program_id(0) % 4) * 4)) + (((_lv0 * 1024) + tl.arange(0, 1024)) // 123039)) * 123039) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 123039)) - 251983871, 0), 0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 492156) & True), other=0.0) - (tl.load(in8_ptr + (tl.program_id(0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 492156) & True), other=0.0) * (1.0 * (1.0 / 492156.0)))) * (tl.load(in7_ptr + (tl.maximum(((((((tl.program_id(0) // 4) * 16) + ((tl.program_id(0) % 4) * 4)) + (((_lv0 * 1024) + tl.arange(0, 1024)) // 123039)) * 123039) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 123039)) - tl.maximum(((((((tl.program_id(0) // 4) * 16) + ((tl.program_id(0) % 4) * 4)) + (((_lv0 * 1024) + tl.arange(0, 1024)) // 123039)) * 123039) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 123039)) - 251983871, 0), 0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 492156) & True), other=0.0) - (tl.load(in8_ptr + (tl.program_id(0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 492156) & True), other=0.0) * (1.0 * (1.0 / 492156.0))))), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t060_s4(out, ins):
    grid = (512,)
    t060_s4_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8])
    return out


@triton.jit
def t060_s5_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr):
    _acc0 = tl.zeros([1], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), ((((tl.load(in7_ptr + (tl.program_id(0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) - (tl.load(in8_ptr + (tl.maximum((((tl.program_id(0) // 1968624) * 4) + (((tl.program_id(0) // 123039) % 16) // 4)) - tl.maximum((((tl.program_id(0) // 1968624) * 4) + (((tl.program_id(0) // 123039) % 16) // 4)) - 511, 0), 0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) * (1.0 * (1.0 / 492156.0)))) * (1.0 / tl.sqrt(((tl.load(in9_ptr + (tl.maximum((((tl.program_id(0) // 1968624) * 4) + (((tl.program_id(0) // 123039) % 16) // 4)) - tl.maximum((((tl.program_id(0) // 1968624) * 4) + (((tl.program_id(0) // 123039) % 16) // 4)) - 511, 0), 0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) * (1.0 * (1.0 / 492156.0))) + (1.0 * (1.0 / 100000.0)))))) * tl.load(in3_ptr + (((tl.program_id(0) // 123039) % 16) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)) + tl.load(in4_ptr + (((tl.program_id(0) // 123039) % 16) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)), 0.0))
    _v = ((tl.sum(_acc0, axis=0) * tl.minimum(tl.maximum((tl.sum(_acc0, axis=0) + (3.0 * (1.0 / 1.0))), (0.0 * (1.0 / 1.0))), (6.0 * (1.0 / 1.0)))) / (6.0 * (1.0 / 1.0)))
    tl.store(out_ptr + tl.program_id(0), _v)


def t060_s5(out, ins):
    grid = (251983872,)
    t060_s5_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9])
    return out


def t060(out, ins):
    _t0 = torch.empty(251983872, device=ins[0].device, dtype=torch.float32)
    _t1 = torch.empty(251983872, device=ins[0].device, dtype=torch.float32)
    _t2 = torch.empty(251983872, device=ins[0].device, dtype=torch.float32)
    _t3 = torch.empty(512, device=ins[0].device, dtype=torch.float32)
    _t4 = torch.empty(512, device=ins[0].device, dtype=torch.float32)
    t060_s0(_t0, list(ins))
    t060_s1(_t1, list(ins) + [_t0])
    t060_s2(_t2, list(ins) + [_t0, _t1])
    t060_s3(_t3, list(ins) + [_t0, _t1, _t2])
    t060_s4(_t4, list(ins) + [_t0, _t1, _t2, _t3])
    t060_s5(out, list(ins) + [_t0, _t1, _t2, _t3, _t4])
    return out
