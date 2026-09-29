import torch
import triton
import triton.language as tl


@triton.jit
def _mul_combine(a, b):
    return a * b


@triton.jit
def t013_s0_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr):
    _acc0 = tl.zeros([256], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 256) + tl.arange(0, 256)) < 432) & (((((((((((((_lv0 * 256) + tl.arange(0, 256)) // 9) % 3) <= (((tl.program_id(0) // 16384) % 32) + 1)) & (0 == 0)) & (tl.maximum((((tl.program_id(0) // 16384) % 32) + 1) - ((((_lv0 * 256) + tl.arange(0, 256)) // 9) % 3), 0) < 32)) & (((((_lv0 * 256) + tl.arange(0, 256)) // 3) % 3) <= (((tl.program_id(0) // 128) % 128) + 1))) & (0 == 0)) & (tl.maximum((((tl.program_id(0) // 128) % 128) + 1) - ((((_lv0 * 256) + tl.arange(0, 256)) // 3) % 3), 0) < 128)) & ((((_lv0 * 256) + tl.arange(0, 256)) % 3) <= ((tl.program_id(0) % 128) + 1))) & (0 == 0)) & (tl.maximum(((tl.program_id(0) % 128) + 1) - (((_lv0 * 256) + tl.arange(0, 256)) % 3), 0) < 128))), (tl.load(in0_ptr + ((((((((((tl.program_id(0) // 33554432) * 16) + (((((tl.program_id(0) // 524288) % 64) // 64) * 16) + (((_lv0 * 256) + tl.arange(0, 256)) // 27))) * 32) + tl.maximum((((tl.program_id(0) // 16384) % 32) + 1) - ((((_lv0 * 256) + tl.arange(0, 256)) // 9) % 3), 0)) * 128) + tl.maximum((((tl.program_id(0) // 128) % 128) + 1) - ((((_lv0 * 256) + tl.arange(0, 256)) // 3) % 3), 0)) * 128) + tl.maximum(((tl.program_id(0) % 128) + 1) - (((_lv0 * 256) + tl.arange(0, 256)) % 3), 0)) + 0 * tl.arange(0, 256)), mask=((((_lv0 * 256) + tl.arange(0, 256)) < 432) & (((((((((((((_lv0 * 256) + tl.arange(0, 256)) // 9) % 3) <= (((tl.program_id(0) // 16384) % 32) + 1)) & (0 == 0)) & (tl.maximum((((tl.program_id(0) // 16384) % 32) + 1) - ((((_lv0 * 256) + tl.arange(0, 256)) // 9) % 3), 0) < 32)) & (((((_lv0 * 256) + tl.arange(0, 256)) // 3) % 3) <= (((tl.program_id(0) // 128) % 128) + 1))) & (0 == 0)) & (tl.maximum((((tl.program_id(0) // 128) % 128) + 1) - ((((_lv0 * 256) + tl.arange(0, 256)) // 3) % 3), 0) < 128)) & ((((_lv0 * 256) + tl.arange(0, 256)) % 3) <= ((tl.program_id(0) % 128) + 1))) & (0 == 0)) & (tl.maximum(((tl.program_id(0) % 128) + 1) - (((_lv0 * 256) + tl.arange(0, 256)) % 3), 0) < 128))), other=0.0) * tl.load(in1_ptr + ((((((((((((((tl.program_id(0) // 524288) % 64) // 64) * 16) + (((_lv0 * 256) + tl.arange(0, 256)) // 27)) * 64) + (((tl.program_id(0) // 524288) % 64) % 64)) * 3) + ((((_lv0 * 256) + tl.arange(0, 256)) // 9) % 3)) * 3) + ((((_lv0 * 256) + tl.arange(0, 256)) // 3) % 3)) * 3) + (((_lv0 * 256) + tl.arange(0, 256)) % 3)) + 0 * tl.arange(0, 256)), mask=((((_lv0 * 256) + tl.arange(0, 256)) < 432) & (((((((((((((_lv0 * 256) + tl.arange(0, 256)) // 9) % 3) <= (((tl.program_id(0) // 16384) % 32) + 1)) & (0 == 0)) & (tl.maximum((((tl.program_id(0) // 16384) % 32) + 1) - ((((_lv0 * 256) + tl.arange(0, 256)) // 9) % 3), 0) < 32)) & (((((_lv0 * 256) + tl.arange(0, 256)) // 3) % 3) <= (((tl.program_id(0) // 128) % 128) + 1))) & (0 == 0)) & (tl.maximum((((tl.program_id(0) // 128) % 128) + 1) - ((((_lv0 * 256) + tl.arange(0, 256)) // 3) % 3), 0) < 128)) & ((((_lv0 * 256) + tl.arange(0, 256)) % 3) <= ((tl.program_id(0) % 128) + 1))) & (0 == 0)) & (tl.maximum(((tl.program_id(0) % 128) + 1) - (((_lv0 * 256) + tl.arange(0, 256)) % 3), 0) < 128))), other=0.0)), 0.0))
    _v = (tl.sum(_acc0, axis=0) + tl.load(in2_ptr + (((tl.program_id(0) // 524288) % 64))))
    tl.store(out_ptr + tl.program_id(0), _v)


def t013_s0(out, ins):
    grid = (536870912,)
    t013_s0_kernel[grid](out, ins[0], ins[1], ins[2], ins[3])
    return out


@triton.jit
def t013_s1_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr):
    _acc0 = tl.zeros([32], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 32) + tl.arange(0, 32)) < 32) & True), tl.load(in4_ptr + ((((((((((tl.program_id(0) // 1048576) * 64) + ((tl.program_id(0) // 16384) % 64)) * 32) + ((_lv0 * 32) + tl.arange(0, 32))) * 128) + ((tl.program_id(0) // 128) % 128)) * 128) + (tl.program_id(0) % 128)) + 0 * tl.arange(0, 32)), mask=((((_lv0 * 32) + tl.arange(0, 32)) < 32) & True), other=0.0), 0.0))
    _v = (tl.sum(_acc0, axis=0) * (1.0 * (1.0 / 32.0)))
    tl.store(out_ptr + tl.program_id(0), _v)


def t013_s1(out, ins):
    grid = (16777216,)
    t013_s1_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4])
    return out


@triton.jit
def t013_s2_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr):
    _acc0 = tl.zeros([1], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), (tl.load(in5_ptr + ((((((((tl.program_id(0) // 1048576) * 64) + ((tl.program_id(0) // 16384) % 64)) * 128) + ((tl.program_id(0) // 128) % 128)) * 128) + (tl.program_id(0) % 128)) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) + tl.load(in3_ptr + (((tl.program_id(0) // 16384) % 64) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t013_s2(out, ins):
    grid = (16777216,)
    t013_s2_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5])
    return out


@triton.jit
def t013_s3_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr):
    _acc0 = tl.zeros([64], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 64) + tl.arange(0, 64)) < 64) & True), tl.exp(tl.load(in6_ptr + ((((((tl.program_id(0) // 16384) * 64) + ((_lv0 * 64) + tl.arange(0, 64))) * 16384) + (tl.program_id(0) % 16384)) + 0 * tl.arange(0, 64)), mask=((((_lv0 * 64) + tl.arange(0, 64)) < 64) & True), other=0.0)), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t013_s3(out, ins):
    grid = (262144,)
    t013_s3_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6])
    return out


@triton.jit
def t013_s4_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr):
    _acc0 = tl.zeros([1], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), (tl.exp(tl.load(in6_ptr + (tl.program_id(0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)) * (1.0 / tl.load(in7_ptr + (tl.maximum((((tl.program_id(0) // (64 * 16384)) * 16384) + (tl.program_id(0) % 16384)) - tl.maximum((((tl.program_id(0) // (64 * 16384)) * 16384) + (tl.program_id(0) % 16384)) - 262143, 0), 0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0))), 0.0))
    _v = ((2.0 * tl.sigmoid(2.0 * (tl.sum(_acc0, axis=0))) - 1.0) * (2.0 * (1.0 / 1.0)))
    tl.store(out_ptr + tl.program_id(0), _v)


def t013_s4(out, ins):
    grid = (16777216,)
    t013_s4_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7])
    return out


def t013(out, ins):
    _t0 = torch.empty(536870912, device=ins[0].device, dtype=torch.float32)
    _t1 = torch.empty(16777216, device=ins[0].device, dtype=torch.float32)
    _t2 = torch.empty(16777216, device=ins[0].device, dtype=torch.float32)
    _t3 = torch.empty(262144, device=ins[0].device, dtype=torch.float32)
    t013_s0(_t0, list(ins))
    t013_s1(_t1, list(ins) + [_t0])
    t013_s2(_t2, list(ins) + [_t0, _t1])
    t013_s3(_t3, list(ins) + [_t0, _t1, _t2])
    t013_s4(out, list(ins) + [_t0, _t1, _t2, _t3])
    return out
