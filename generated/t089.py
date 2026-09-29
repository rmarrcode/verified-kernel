import torch
import triton
import triton.language as tl


@triton.jit
def _mul_combine(a, b):
    return a * b


@triton.jit
def t089_s0_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr):
    _acc0 = tl.zeros([64], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 64) + tl.arange(0, 64)) < 81) & (((((((((((((_lv0 * 64) + tl.arange(0, 64)) // 9) % 3) <= (((tl.program_id(0) // 4096) % 32) + 1)) & ((tl.maximum((((tl.program_id(0) // 4096) % 32) + 1) - ((((_lv0 * 64) + tl.arange(0, 64)) // 9) % 3), 0) % 2) == 0)) & ((tl.maximum((((tl.program_id(0) // 4096) % 32) + 1) - ((((_lv0 * 64) + tl.arange(0, 64)) // 9) % 3), 0) // 2) < 16)) & (((((_lv0 * 64) + tl.arange(0, 64)) // 3) % 3) <= (((tl.program_id(0) // 64) % 64) + 1))) & ((tl.maximum((((tl.program_id(0) // 64) % 64) + 1) - ((((_lv0 * 64) + tl.arange(0, 64)) // 3) % 3), 0) % 2) == 0)) & ((tl.maximum((((tl.program_id(0) // 64) % 64) + 1) - ((((_lv0 * 64) + tl.arange(0, 64)) // 3) % 3), 0) // 2) < 32)) & ((((_lv0 * 64) + tl.arange(0, 64)) % 3) <= ((tl.program_id(0) % 64) + 1))) & ((tl.maximum(((tl.program_id(0) % 64) + 1) - (((_lv0 * 64) + tl.arange(0, 64)) % 3), 0) % 2) == 0)) & ((tl.maximum(((tl.program_id(0) % 64) + 1) - (((_lv0 * 64) + tl.arange(0, 64)) % 3), 0) // 2) < 32))), (tl.load(in0_ptr + ((((((((((tl.program_id(0) // 2097152) * 3) + (((((tl.program_id(0) // 131072) % 16) // 16) * 3) + (((_lv0 * 64) + tl.arange(0, 64)) // 27))) * 16) + (tl.maximum((((tl.program_id(0) // 4096) % 32) + 1) - ((((_lv0 * 64) + tl.arange(0, 64)) // 9) % 3), 0) // 2)) * 32) + (tl.maximum((((tl.program_id(0) // 64) % 64) + 1) - ((((_lv0 * 64) + tl.arange(0, 64)) // 3) % 3), 0) // 2)) * 32) + (tl.maximum(((tl.program_id(0) % 64) + 1) - (((_lv0 * 64) + tl.arange(0, 64)) % 3), 0) // 2)) + 0 * tl.arange(0, 64)), mask=((((_lv0 * 64) + tl.arange(0, 64)) < 81) & (((((((((((((_lv0 * 64) + tl.arange(0, 64)) // 9) % 3) <= (((tl.program_id(0) // 4096) % 32) + 1)) & ((tl.maximum((((tl.program_id(0) // 4096) % 32) + 1) - ((((_lv0 * 64) + tl.arange(0, 64)) // 9) % 3), 0) % 2) == 0)) & ((tl.maximum((((tl.program_id(0) // 4096) % 32) + 1) - ((((_lv0 * 64) + tl.arange(0, 64)) // 9) % 3), 0) // 2) < 16)) & (((((_lv0 * 64) + tl.arange(0, 64)) // 3) % 3) <= (((tl.program_id(0) // 64) % 64) + 1))) & ((tl.maximum((((tl.program_id(0) // 64) % 64) + 1) - ((((_lv0 * 64) + tl.arange(0, 64)) // 3) % 3), 0) % 2) == 0)) & ((tl.maximum((((tl.program_id(0) // 64) % 64) + 1) - ((((_lv0 * 64) + tl.arange(0, 64)) // 3) % 3), 0) // 2) < 32)) & ((((_lv0 * 64) + tl.arange(0, 64)) % 3) <= ((tl.program_id(0) % 64) + 1))) & ((tl.maximum(((tl.program_id(0) % 64) + 1) - (((_lv0 * 64) + tl.arange(0, 64)) % 3), 0) % 2) == 0)) & ((tl.maximum(((tl.program_id(0) % 64) + 1) - (((_lv0 * 64) + tl.arange(0, 64)) % 3), 0) // 2) < 32))), other=0.0) * tl.load(in1_ptr + ((((((((((((((tl.program_id(0) // 131072) % 16) // 16) * 3) + (((_lv0 * 64) + tl.arange(0, 64)) // 27)) * 16) + (((tl.program_id(0) // 131072) % 16) % 16)) * 3) + ((((_lv0 * 64) + tl.arange(0, 64)) // 9) % 3)) * 3) + ((((_lv0 * 64) + tl.arange(0, 64)) // 3) % 3)) * 3) + (((_lv0 * 64) + tl.arange(0, 64)) % 3)) + 0 * tl.arange(0, 64)), mask=((((_lv0 * 64) + tl.arange(0, 64)) < 81) & (((((((((((((_lv0 * 64) + tl.arange(0, 64)) // 9) % 3) <= (((tl.program_id(0) // 4096) % 32) + 1)) & ((tl.maximum((((tl.program_id(0) // 4096) % 32) + 1) - ((((_lv0 * 64) + tl.arange(0, 64)) // 9) % 3), 0) % 2) == 0)) & ((tl.maximum((((tl.program_id(0) // 4096) % 32) + 1) - ((((_lv0 * 64) + tl.arange(0, 64)) // 9) % 3), 0) // 2) < 16)) & (((((_lv0 * 64) + tl.arange(0, 64)) // 3) % 3) <= (((tl.program_id(0) // 64) % 64) + 1))) & ((tl.maximum((((tl.program_id(0) // 64) % 64) + 1) - ((((_lv0 * 64) + tl.arange(0, 64)) // 3) % 3), 0) % 2) == 0)) & ((tl.maximum((((tl.program_id(0) // 64) % 64) + 1) - ((((_lv0 * 64) + tl.arange(0, 64)) // 3) % 3), 0) // 2) < 32)) & ((((_lv0 * 64) + tl.arange(0, 64)) % 3) <= ((tl.program_id(0) % 64) + 1))) & ((tl.maximum(((tl.program_id(0) % 64) + 1) - (((_lv0 * 64) + tl.arange(0, 64)) % 3), 0) % 2) == 0)) & ((tl.maximum(((tl.program_id(0) % 64) + 1) - (((_lv0 * 64) + tl.arange(0, 64)) % 3), 0) // 2) < 32))), other=0.0)), 0.0))
    _v = (tl.sum(_acc0, axis=0) + tl.load(in2_ptr + (((tl.program_id(0) // 131072) % 16))))
    tl.store(out_ptr + tl.program_id(0), _v)


def t089_s0(out, ins):
    grid = (268435456,)
    t089_s0_kernel[grid](out, ins[0], ins[1], ins[2], ins[3])
    return out


@triton.jit
def t089_s1_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr):
    _acc0 = tl.zeros([8], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = tl.maximum(_acc0, tl.load(in4_ptr + ((((((((((tl.program_id(0) // 262144) * 16) + ((tl.program_id(0) // 16384) % 16)) * 32) + tl.maximum(((((tl.program_id(0) // 1024) % 16) * 2) + tl.maximum(((tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) // 4) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 1024) % 16) * 2), 0) - (tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) // 4), 0)) - tl.maximum(((tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) // 4) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 1024) % 16) * 2), 0) - (tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) // 4), 0)) - tl.maximum(31 - (((tl.program_id(0) // 1024) % 16) * 2), 0), 0), 0)) - tl.maximum(((((tl.program_id(0) // 1024) % 16) * 2) + tl.maximum(((tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) // 4) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 1024) % 16) * 2), 0) - (tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) // 4), 0)) - tl.maximum(((tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) // 4) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 1024) % 16) * 2), 0) - (tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) // 4), 0)) - tl.maximum(31 - (((tl.program_id(0) // 1024) % 16) * 2), 0), 0), 0)) - 31, 0), 0)) * 64) + tl.maximum(((((tl.program_id(0) // 32) % 32) * 2) + tl.maximum((((tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) // 2) % 2) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 32) % 32) * 2), 0) - ((tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) // 2) % 2), 0)) - tl.maximum((((tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) // 2) % 2) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 32) % 32) * 2), 0) - ((tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) // 2) % 2), 0)) - tl.maximum(63 - (((tl.program_id(0) // 32) % 32) * 2), 0), 0), 0)) - tl.maximum(((((tl.program_id(0) // 32) % 32) * 2) + tl.maximum((((tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) // 2) % 2) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 32) % 32) * 2), 0) - ((tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) // 2) % 2), 0)) - tl.maximum((((tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) // 2) % 2) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 32) % 32) * 2), 0) - ((tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) // 2) % 2), 0)) - tl.maximum(63 - (((tl.program_id(0) // 32) % 32) * 2), 0), 0), 0)) - 63, 0), 0)) * 64) + tl.maximum((((tl.program_id(0) % 32) * 2) + tl.maximum(((tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) % 2) + tl.maximum(tl.maximum(0 - ((tl.program_id(0) % 32) * 2), 0) - (tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) % 2), 0)) - tl.maximum(((tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) % 2) + tl.maximum(tl.maximum(0 - ((tl.program_id(0) % 32) * 2), 0) - (tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) % 2), 0)) - tl.maximum(63 - ((tl.program_id(0) % 32) * 2), 0), 0), 0)) - tl.maximum((((tl.program_id(0) % 32) * 2) + tl.maximum(((tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) % 2) + tl.maximum(tl.maximum(0 - ((tl.program_id(0) % 32) * 2), 0) - (tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) % 2), 0)) - tl.maximum(((tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) % 2) + tl.maximum(tl.maximum(0 - ((tl.program_id(0) % 32) * 2), 0) - (tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) % 2), 0)) - tl.maximum(63 - ((tl.program_id(0) % 32) * 2), 0), 0), 0)) - 63, 0), 0)))))
    _v = tl.max(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t089_s1(out, ins):
    grid = (33554432,)
    t089_s1_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4])
    return out


@triton.jit
def t089_s2_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr):
    _acc0 = tl.zeros([16], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 16) + tl.arange(0, 16)) < 16) & True), tl.exp(tl.load(in5_ptr + ((((((tl.program_id(0) // 16384) * 16) + ((_lv0 * 16) + tl.arange(0, 16))) * 16384) + (tl.program_id(0) % 16384)) + 0 * tl.arange(0, 16)), mask=((((_lv0 * 16) + tl.arange(0, 16)) < 16) & True), other=0.0)), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t089_s2(out, ins):
    grid = (2097152,)
    t089_s2_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5])
    return out


@triton.jit
def t089_s3_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr):
    _acc0 = tl.zeros([1], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), (tl.exp(tl.load(in5_ptr + (tl.program_id(0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)) * (1.0 / tl.load(in6_ptr + (tl.maximum((((tl.program_id(0) // (16 * 16384)) * 16384) + (tl.program_id(0) % 16384)) - tl.maximum((((tl.program_id(0) // (16 * 16384)) * 16384) + (tl.program_id(0) % 16384)) - 2097151, 0), 0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0))), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t089_s3(out, ins):
    grid = (33554432,)
    t089_s3_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6])
    return out


@triton.jit
def t089_s4_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr):
    _acc0 = tl.zeros([1], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), (tl.load(in7_ptr + ((((((((((tl.program_id(0) // 262144) * 16) + ((tl.program_id(0) // 16384) % 16)) * 16) + ((tl.program_id(0) // 1024) % 16)) * 32) + ((tl.program_id(0) // 32) % 32)) * 32) + (tl.program_id(0) % 32)) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) - tl.load(in3_ptr + (((tl.program_id(0) // 16384) % 16) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t089_s4(out, ins):
    grid = (33554432,)
    t089_s4_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7])
    return out


@triton.jit
def t089_s5_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr):
    _acc0 = tl.zeros([1], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), (1.0 / ((1.0 * (1.0 / 1.0)) + tl.exp(((0.0 * (1.0 / 1.0)) - tl.load(in8_ptr + ((((((((((tl.program_id(0) // 262144) * 16) + ((tl.program_id(0) // 16384) % 16)) * 16) + ((tl.program_id(0) // 1024) % 16)) * 32) + ((tl.program_id(0) // 32) % 32)) * 32) + (tl.program_id(0) % 32)) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0))))), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t089_s5(out, ins):
    grid = (33554432,)
    t089_s5_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8])
    return out


@triton.jit
def t089_s6_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr):
    _acc0 = tl.zeros([1], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), (tl.load(in9_ptr + ((((((((((tl.program_id(0) // 262144) * 16) + ((tl.program_id(0) // 16384) % 16)) * 16) + ((tl.program_id(0) // 1024) % 16)) * 32) + ((tl.program_id(0) // 32) % 32)) * 32) + (tl.program_id(0) % 32)) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) * tl.load(in8_ptr + ((((((((((tl.program_id(0) // 262144) * 16) + ((tl.program_id(0) // 16384) % 16)) * 16) + ((tl.program_id(0) // 1024) % 16)) * 32) + ((tl.program_id(0) // 32) % 32)) * 32) + (tl.program_id(0) % 32)) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t089_s6(out, ins):
    grid = (33554432,)
    t089_s6_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9])
    return out


@triton.jit
def t089_s7_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr):
    _acc0 = tl.zeros([16], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = tl.maximum(_acc0, tl.load(in10_ptr + ((((((tl.program_id(0) // 16384) * 16) + tl.maximum(((_lv0 * 16) + tl.arange(0, 16)) - tl.maximum(((_lv0 * 16) + tl.arange(0, 16)) - 15, 0), 0)) * 16384) + (tl.program_id(0) % 16384)))))
    _v = tl.max(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t089_s7(out, ins):
    grid = (2097152,)
    t089_s7_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10])
    return out


def t089(out, ins):
    _t0 = torch.empty(268435456, device=ins[0].device, dtype=torch.float32)
    _t1 = torch.empty(33554432, device=ins[0].device, dtype=torch.float32)
    _t2 = torch.empty(2097152, device=ins[0].device, dtype=torch.float32)
    _t3 = torch.empty(33554432, device=ins[0].device, dtype=torch.float32)
    _t4 = torch.empty(33554432, device=ins[0].device, dtype=torch.float32)
    _t5 = torch.empty(33554432, device=ins[0].device, dtype=torch.float32)
    _t6 = torch.empty(33554432, device=ins[0].device, dtype=torch.float32)
    t089_s0(_t0, list(ins))
    t089_s1(_t1, list(ins) + [_t0])
    t089_s2(_t2, list(ins) + [_t0, _t1])
    t089_s3(_t3, list(ins) + [_t0, _t1, _t2])
    t089_s4(_t4, list(ins) + [_t0, _t1, _t2, _t3])
    t089_s5(_t5, list(ins) + [_t0, _t1, _t2, _t3, _t4])
    t089_s6(_t6, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5])
    t089_s7(out, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5, _t6])
    return out
