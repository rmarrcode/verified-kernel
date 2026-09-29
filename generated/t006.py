import torch
import triton
import triton.language as tl


@triton.jit
def _mul_combine(a, b):
    return a * b


@triton.jit
def t006_s0_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr):
    _acc0 = tl.zeros([64], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 64) + tl.arange(0, 64)) < 81) & ((((((tl.program_id(0) // 900) % 14) + ((((_lv0 * 64) + tl.arange(0, 64)) // 9) % 3)) < 16) & ((((tl.program_id(0) // 30) % 30) + ((((_lv0 * 64) + tl.arange(0, 64)) // 3) % 3)) < 32)) & (((tl.program_id(0) % 30) + (((_lv0 * 64) + tl.arange(0, 64)) % 3)) < 32))), (tl.load(in0_ptr + ((((((((((tl.program_id(0) // 201600) * 3) + (((_lv0 * 64) + tl.arange(0, 64)) // 27)) * 16) + (((tl.program_id(0) // 900) % 14) + ((((_lv0 * 64) + tl.arange(0, 64)) // 9) % 3))) * 32) + (((tl.program_id(0) // 30) % 30) + ((((_lv0 * 64) + tl.arange(0, 64)) // 3) % 3))) * 32) + ((tl.program_id(0) % 30) + (((_lv0 * 64) + tl.arange(0, 64)) % 3))) + 0 * tl.arange(0, 64)), mask=((((_lv0 * 64) + tl.arange(0, 64)) < 81) & ((((((tl.program_id(0) // 900) % 14) + ((((_lv0 * 64) + tl.arange(0, 64)) // 9) % 3)) < 16) & ((((tl.program_id(0) // 30) % 30) + ((((_lv0 * 64) + tl.arange(0, 64)) // 3) % 3)) < 32)) & (((tl.program_id(0) % 30) + (((_lv0 * 64) + tl.arange(0, 64)) % 3)) < 32))), other=0.0) * tl.load(in1_ptr + (((((((((((tl.program_id(0) // 12600) % 16) * 3) + (((_lv0 * 64) + tl.arange(0, 64)) // 27)) * 3) + ((((_lv0 * 64) + tl.arange(0, 64)) // 9) % 3)) * 3) + ((((_lv0 * 64) + tl.arange(0, 64)) // 3) % 3)) * 3) + (((_lv0 * 64) + tl.arange(0, 64)) % 3)) + 0 * tl.arange(0, 64)), mask=((((_lv0 * 64) + tl.arange(0, 64)) < 81) & ((((((tl.program_id(0) // 900) % 14) + ((((_lv0 * 64) + tl.arange(0, 64)) // 9) % 3)) < 16) & ((((tl.program_id(0) // 30) % 30) + ((((_lv0 * 64) + tl.arange(0, 64)) // 3) % 3)) < 32)) & (((tl.program_id(0) % 30) + (((_lv0 * 64) + tl.arange(0, 64)) % 3)) < 32))), other=0.0)), 0.0))
    _v = (tl.sum(_acc0, axis=0) + tl.load(in2_ptr + (((tl.program_id(0) // 12600) % 16))))
    tl.store(out_ptr + tl.program_id(0), _v)


def t006_s0(out, ins):
    grid = (25804800,)
    t006_s0_kernel[grid](out, ins[0], ins[1], ins[2])
    return out


@triton.jit
def t006_s1_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr):
    _acc0 = tl.zeros([16], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 16) + tl.arange(0, 16)) < 16) & True), tl.exp(tl.load(in3_ptr + ((((((tl.program_id(0) // 12600) * 16) + ((_lv0 * 16) + tl.arange(0, 16))) * 12600) + (tl.program_id(0) % 12600)) + 0 * tl.arange(0, 16)), mask=((((_lv0 * 16) + tl.arange(0, 16)) < 16) & True), other=0.0)), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t006_s1(out, ins):
    grid = (1612800,)
    t006_s1_kernel[grid](out, ins[0], ins[1], ins[2], ins[3])
    return out


@triton.jit
def t006_s2_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr):
    _acc0 = tl.zeros([1], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), (tl.exp(tl.load(in3_ptr + (tl.program_id(0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)) * (1.0 / tl.load(in4_ptr + (tl.maximum((((tl.program_id(0) // (16 * 12600)) * 12600) + (tl.program_id(0) % 12600)) - tl.maximum((((tl.program_id(0) // (16 * 12600)) * 12600) + (tl.program_id(0) % 12600)) - 1612799, 0), 0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0))), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t006_s2(out, ins):
    grid = (25804800,)
    t006_s2_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4])
    return out


@triton.jit
def t006_s3_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr):
    _acc0 = tl.zeros([8], dtype=tl.float32) + (tl.load(in5_ptr + ((((((((((tl.program_id(0) // 25200) * 16) + ((tl.program_id(0) // 1575) % 16)) * 14) + tl.maximum(((((tl.program_id(0) // 225) % 7) * 2) + tl.maximum(((0 // 4) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 225) % 7) * 2), 0) - (0 // 4), 0)) - tl.maximum(((0 // 4) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 225) % 7) * 2), 0) - (0 // 4), 0)) - tl.maximum(13 - (((tl.program_id(0) // 225) % 7) * 2), 0), 0), 0)) - tl.maximum(((((tl.program_id(0) // 225) % 7) * 2) + tl.maximum(((0 // 4) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 225) % 7) * 2), 0) - (0 // 4), 0)) - tl.maximum(((0 // 4) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 225) % 7) * 2), 0) - (0 // 4), 0)) - tl.maximum(13 - (((tl.program_id(0) // 225) % 7) * 2), 0), 0), 0)) - 13, 0), 0)) * 30) + tl.maximum(((((tl.program_id(0) // 15) % 15) * 2) + tl.maximum((((0 // 2) % 2) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 15) % 15) * 2), 0) - ((0 // 2) % 2), 0)) - tl.maximum((((0 // 2) % 2) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 15) % 15) * 2), 0) - ((0 // 2) % 2), 0)) - tl.maximum(29 - (((tl.program_id(0) // 15) % 15) * 2), 0), 0), 0)) - tl.maximum(((((tl.program_id(0) // 15) % 15) * 2) + tl.maximum((((0 // 2) % 2) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 15) % 15) * 2), 0) - ((0 // 2) % 2), 0)) - tl.maximum((((0 // 2) % 2) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 15) % 15) * 2), 0) - ((0 // 2) % 2), 0)) - tl.maximum(29 - (((tl.program_id(0) // 15) % 15) * 2), 0), 0), 0)) - 29, 0), 0)) * 30) + tl.maximum((((tl.program_id(0) % 15) * 2) + tl.maximum(((0 % 2) + tl.maximum(tl.maximum(0 - ((tl.program_id(0) % 15) * 2), 0) - (0 % 2), 0)) - tl.maximum(((0 % 2) + tl.maximum(tl.maximum(0 - ((tl.program_id(0) % 15) * 2), 0) - (0 % 2), 0)) - tl.maximum(29 - ((tl.program_id(0) % 15) * 2), 0), 0), 0)) - tl.maximum((((tl.program_id(0) % 15) * 2) + tl.maximum(((0 % 2) + tl.maximum(tl.maximum(0 - ((tl.program_id(0) % 15) * 2), 0) - (0 % 2), 0)) - tl.maximum(((0 % 2) + tl.maximum(tl.maximum(0 - ((tl.program_id(0) % 15) * 2), 0) - (0 % 2), 0)) - tl.maximum(29 - ((tl.program_id(0) % 15) * 2), 0), 0), 0)) - 29, 0), 0)))))
    for _lv0 in range(0, 1):
        _acc0 = tl.maximum(_acc0, tl.load(in5_ptr + ((((((((((tl.program_id(0) // 25200) * 16) + ((tl.program_id(0) // 1575) % 16)) * 14) + tl.maximum(((((tl.program_id(0) // 225) % 7) * 2) + tl.maximum(((tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) // 4) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 225) % 7) * 2), 0) - (tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) // 4), 0)) - tl.maximum(((tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) // 4) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 225) % 7) * 2), 0) - (tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) // 4), 0)) - tl.maximum(13 - (((tl.program_id(0) // 225) % 7) * 2), 0), 0), 0)) - tl.maximum(((((tl.program_id(0) // 225) % 7) * 2) + tl.maximum(((tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) // 4) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 225) % 7) * 2), 0) - (tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) // 4), 0)) - tl.maximum(((tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) // 4) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 225) % 7) * 2), 0) - (tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) // 4), 0)) - tl.maximum(13 - (((tl.program_id(0) // 225) % 7) * 2), 0), 0), 0)) - 13, 0), 0)) * 30) + tl.maximum(((((tl.program_id(0) // 15) % 15) * 2) + tl.maximum((((tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) // 2) % 2) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 15) % 15) * 2), 0) - ((tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) // 2) % 2), 0)) - tl.maximum((((tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) // 2) % 2) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 15) % 15) * 2), 0) - ((tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) // 2) % 2), 0)) - tl.maximum(29 - (((tl.program_id(0) // 15) % 15) * 2), 0), 0), 0)) - tl.maximum(((((tl.program_id(0) // 15) % 15) * 2) + tl.maximum((((tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) // 2) % 2) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 15) % 15) * 2), 0) - ((tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) // 2) % 2), 0)) - tl.maximum((((tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) // 2) % 2) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 15) % 15) * 2), 0) - ((tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) // 2) % 2), 0)) - tl.maximum(29 - (((tl.program_id(0) // 15) % 15) * 2), 0), 0), 0)) - 29, 0), 0)) * 30) + tl.maximum((((tl.program_id(0) % 15) * 2) + tl.maximum(((tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) % 2) + tl.maximum(tl.maximum(0 - ((tl.program_id(0) % 15) * 2), 0) - (tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) % 2), 0)) - tl.maximum(((tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) % 2) + tl.maximum(tl.maximum(0 - ((tl.program_id(0) % 15) * 2), 0) - (tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) % 2), 0)) - tl.maximum(29 - ((tl.program_id(0) % 15) * 2), 0), 0), 0)) - tl.maximum((((tl.program_id(0) % 15) * 2) + tl.maximum(((tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) % 2) + tl.maximum(tl.maximum(0 - ((tl.program_id(0) % 15) * 2), 0) - (tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) % 2), 0)) - tl.maximum(((tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) % 2) + tl.maximum(tl.maximum(0 - ((tl.program_id(0) % 15) * 2), 0) - (tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) % 2), 0)) - tl.maximum(29 - ((tl.program_id(0) % 15) * 2), 0), 0), 0)) - 29, 0), 0)))))
    _v = tl.max(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t006_s3(out, ins):
    grid = (3225600,)
    t006_s3_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5])
    return out


@triton.jit
def t006_s4_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr):
    _acc0 = tl.zeros([8], dtype=tl.float32) + (tl.load(in6_ptr + ((((((((((tl.program_id(0) // 2352) * 16) + ((tl.program_id(0) // 147) % 16)) * 7) + tl.maximum(((((tl.program_id(0) // 49) % 3) * 2) + tl.maximum(((0 // 4) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 49) % 3) * 2), 0) - (0 // 4), 0)) - tl.maximum(((0 // 4) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 49) % 3) * 2), 0) - (0 // 4), 0)) - tl.maximum(6 - (((tl.program_id(0) // 49) % 3) * 2), 0), 0), 0)) - tl.maximum(((((tl.program_id(0) // 49) % 3) * 2) + tl.maximum(((0 // 4) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 49) % 3) * 2), 0) - (0 // 4), 0)) - tl.maximum(((0 // 4) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 49) % 3) * 2), 0) - (0 // 4), 0)) - tl.maximum(6 - (((tl.program_id(0) // 49) % 3) * 2), 0), 0), 0)) - 6, 0), 0)) * 15) + tl.maximum(((((tl.program_id(0) // 7) % 7) * 2) + tl.maximum((((0 // 2) % 2) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 7) % 7) * 2), 0) - ((0 // 2) % 2), 0)) - tl.maximum((((0 // 2) % 2) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 7) % 7) * 2), 0) - ((0 // 2) % 2), 0)) - tl.maximum(14 - (((tl.program_id(0) // 7) % 7) * 2), 0), 0), 0)) - tl.maximum(((((tl.program_id(0) // 7) % 7) * 2) + tl.maximum((((0 // 2) % 2) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 7) % 7) * 2), 0) - ((0 // 2) % 2), 0)) - tl.maximum((((0 // 2) % 2) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 7) % 7) * 2), 0) - ((0 // 2) % 2), 0)) - tl.maximum(14 - (((tl.program_id(0) // 7) % 7) * 2), 0), 0), 0)) - 14, 0), 0)) * 15) + tl.maximum((((tl.program_id(0) % 7) * 2) + tl.maximum(((0 % 2) + tl.maximum(tl.maximum(0 - ((tl.program_id(0) % 7) * 2), 0) - (0 % 2), 0)) - tl.maximum(((0 % 2) + tl.maximum(tl.maximum(0 - ((tl.program_id(0) % 7) * 2), 0) - (0 % 2), 0)) - tl.maximum(14 - ((tl.program_id(0) % 7) * 2), 0), 0), 0)) - tl.maximum((((tl.program_id(0) % 7) * 2) + tl.maximum(((0 % 2) + tl.maximum(tl.maximum(0 - ((tl.program_id(0) % 7) * 2), 0) - (0 % 2), 0)) - tl.maximum(((0 % 2) + tl.maximum(tl.maximum(0 - ((tl.program_id(0) % 7) * 2), 0) - (0 % 2), 0)) - tl.maximum(14 - ((tl.program_id(0) % 7) * 2), 0), 0), 0)) - 14, 0), 0)))))
    for _lv0 in range(0, 1):
        _acc0 = tl.maximum(_acc0, tl.load(in6_ptr + ((((((((((tl.program_id(0) // 2352) * 16) + ((tl.program_id(0) // 147) % 16)) * 7) + tl.maximum(((((tl.program_id(0) // 49) % 3) * 2) + tl.maximum(((tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) // 4) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 49) % 3) * 2), 0) - (tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) // 4), 0)) - tl.maximum(((tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) // 4) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 49) % 3) * 2), 0) - (tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) // 4), 0)) - tl.maximum(6 - (((tl.program_id(0) // 49) % 3) * 2), 0), 0), 0)) - tl.maximum(((((tl.program_id(0) // 49) % 3) * 2) + tl.maximum(((tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) // 4) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 49) % 3) * 2), 0) - (tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) // 4), 0)) - tl.maximum(((tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) // 4) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 49) % 3) * 2), 0) - (tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) // 4), 0)) - tl.maximum(6 - (((tl.program_id(0) // 49) % 3) * 2), 0), 0), 0)) - 6, 0), 0)) * 15) + tl.maximum(((((tl.program_id(0) // 7) % 7) * 2) + tl.maximum((((tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) // 2) % 2) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 7) % 7) * 2), 0) - ((tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) // 2) % 2), 0)) - tl.maximum((((tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) // 2) % 2) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 7) % 7) * 2), 0) - ((tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) // 2) % 2), 0)) - tl.maximum(14 - (((tl.program_id(0) // 7) % 7) * 2), 0), 0), 0)) - tl.maximum(((((tl.program_id(0) // 7) % 7) * 2) + tl.maximum((((tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) // 2) % 2) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 7) % 7) * 2), 0) - ((tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) // 2) % 2), 0)) - tl.maximum((((tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) // 2) % 2) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 7) % 7) * 2), 0) - ((tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) // 2) % 2), 0)) - tl.maximum(14 - (((tl.program_id(0) // 7) % 7) * 2), 0), 0), 0)) - 14, 0), 0)) * 15) + tl.maximum((((tl.program_id(0) % 7) * 2) + tl.maximum(((tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) % 2) + tl.maximum(tl.maximum(0 - ((tl.program_id(0) % 7) * 2), 0) - (tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) % 2), 0)) - tl.maximum(((tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) % 2) + tl.maximum(tl.maximum(0 - ((tl.program_id(0) % 7) * 2), 0) - (tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) % 2), 0)) - tl.maximum(14 - ((tl.program_id(0) % 7) * 2), 0), 0), 0)) - tl.maximum((((tl.program_id(0) % 7) * 2) + tl.maximum(((tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) % 2) + tl.maximum(tl.maximum(0 - ((tl.program_id(0) % 7) * 2), 0) - (tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) % 2), 0)) - tl.maximum(((tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) % 2) + tl.maximum(tl.maximum(0 - ((tl.program_id(0) % 7) * 2), 0) - (tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) % 2), 0)) - tl.maximum(14 - ((tl.program_id(0) % 7) * 2), 0), 0), 0)) - 14, 0), 0)))))
    _v = tl.max(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t006_s4(out, ins):
    grid = (301056,)
    t006_s4_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6])
    return out


def t006(out, ins):
    _t0 = torch.empty(25804800, device=ins[0].device, dtype=torch.float32)
    _t1 = torch.empty(1612800, device=ins[0].device, dtype=torch.float32)
    _t2 = torch.empty(25804800, device=ins[0].device, dtype=torch.float32)
    _t3 = torch.empty(3225600, device=ins[0].device, dtype=torch.float32)
    t006_s0(_t0, list(ins))
    t006_s1(_t1, list(ins) + [_t0])
    t006_s2(_t2, list(ins) + [_t0, _t1])
    t006_s3(_t3, list(ins) + [_t0, _t1, _t2])
    t006_s4(out, list(ins) + [_t0, _t1, _t2, _t3])
    return out
