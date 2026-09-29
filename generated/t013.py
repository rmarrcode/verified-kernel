import torch
import triton
import triton.language as tl


@triton.jit
def _mul_combine(a, b):
    return a * b


@triton.jit
def t013_s0_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 32):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 32768) & ((((tl.program_id(0) % 256) * 32768) + ((_lv0 * 1024) + tl.arange(0, 1024))) < 8388608)), tl.load(in0_ptr + (((((((((tl.program_id(0) % 256) * 32768) + ((_lv0 * 1024) + tl.arange(0, 1024))) // 65536) * 32) + (tl.program_id(0) // 256)) * 65536) + ((((tl.program_id(0) % 256) * 32768) + ((_lv0 * 1024) + tl.arange(0, 1024))) % 65536)) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 32768) & ((((tl.program_id(0) % 256) * 32768) + ((_lv0 * 1024) + tl.arange(0, 1024))) < 8388608)), other=0.0), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t013_s0(out, ins):
    grid = (8192,)
    t013_s0_kernel[grid](out, ins[0], ins[1], ins[2], ins[3])
    return out


@triton.jit
def t013_s1_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr):
    _acc0 = tl.zeros([256], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 256) + tl.arange(0, 256)) < 256) & True), tl.load(in4_ptr + (((tl.program_id(0) * 256) + ((_lv0 * 256) + tl.arange(0, 256))) + 0 * tl.arange(0, 256)), mask=((((_lv0 * 256) + tl.arange(0, 256)) < 256) & True), other=0.0), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t013_s1(out, ins):
    grid = (32,)
    t013_s1_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4])
    return out


@triton.jit
def t013_s2_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 32):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 32768) & ((((tl.program_id(0) % 256) * 32768) + ((_lv0 * 1024) + tl.arange(0, 1024))) < 8388608)), ((tl.load(in0_ptr + (((((((((tl.program_id(0) % 256) * 32768) + ((_lv0 * 1024) + tl.arange(0, 1024))) // 65536) * 32) + (tl.program_id(0) // 256)) * 65536) + ((((tl.program_id(0) % 256) * 32768) + ((_lv0 * 1024) + tl.arange(0, 1024))) % 65536)) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 32768) & ((((tl.program_id(0) % 256) * 32768) + ((_lv0 * 1024) + tl.arange(0, 1024))) < 8388608)), other=0.0) - (tl.load(in5_ptr + (tl.maximum((tl.program_id(0) // 256) - tl.maximum((tl.program_id(0) // 256) - 31, 0), 0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 32768) & ((((tl.program_id(0) % 256) * 32768) + ((_lv0 * 1024) + tl.arange(0, 1024))) < 8388608)), other=0.0) * (1.0 * (1.0 / 8388608.0)))) * (tl.load(in0_ptr + (((((((((tl.program_id(0) % 256) * 32768) + ((_lv0 * 1024) + tl.arange(0, 1024))) // 65536) * 32) + (tl.program_id(0) // 256)) * 65536) + ((((tl.program_id(0) % 256) * 32768) + ((_lv0 * 1024) + tl.arange(0, 1024))) % 65536)) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 32768) & ((((tl.program_id(0) % 256) * 32768) + ((_lv0 * 1024) + tl.arange(0, 1024))) < 8388608)), other=0.0) - (tl.load(in5_ptr + (tl.maximum((tl.program_id(0) // 256) - tl.maximum((tl.program_id(0) // 256) - 31, 0), 0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 32768) & ((((tl.program_id(0) % 256) * 32768) + ((_lv0 * 1024) + tl.arange(0, 1024))) < 8388608)), other=0.0) * (1.0 * (1.0 / 8388608.0))))), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t013_s2(out, ins):
    grid = (8192,)
    t013_s2_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5])
    return out


@triton.jit
def t013_s3_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr):
    _acc0 = tl.zeros([256], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 256) + tl.arange(0, 256)) < 256) & True), tl.load(in6_ptr + (((tl.program_id(0) * 256) + ((_lv0 * 256) + tl.arange(0, 256))) + 0 * tl.arange(0, 256)), mask=((((_lv0 * 256) + tl.arange(0, 256)) < 256) & True), other=0.0), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t013_s3(out, ins):
    grid = (32,)
    t013_s3_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6])
    return out


@triton.jit
def t013_s4_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr):
    _acc0 = tl.zeros([1], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), ((((tl.load(in0_ptr + (tl.program_id(0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) - (tl.load(in5_ptr + (tl.maximum(((tl.program_id(0) // 65536) % 32) - tl.maximum(((tl.program_id(0) // 65536) % 32) - 31, 0), 0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) * (1.0 * (1.0 / 8388608.0)))) * (1.0 / tl.sqrt(((tl.load(in7_ptr + (tl.maximum(((tl.program_id(0) // 65536) % 32) - tl.maximum(((tl.program_id(0) // 65536) % 32) - 31, 0), 0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) * (1.0 * (1.0 / 8388608.0))) + (1.0 * (1.0 / 100000.0)))))) * tl.load(in1_ptr + (((tl.program_id(0) // 65536) % 32) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)) + tl.load(in2_ptr + (((tl.program_id(0) // 65536) % 32) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)), 0.0))
    _v = tl.maximum(tl.sum(_acc0, axis=0), (0.0 * (1.0 / 1.0)))
    tl.store(out_ptr + tl.program_id(0), _v)


def t013_s4(out, ins):
    grid = (268435456,)
    t013_s4_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7])
    return out


@triton.jit
def t013_s5_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr):
    _acc0 = tl.zeros([32], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 32) + tl.arange(0, 32)) < 32) & ((((tl.program_id(0) // 256) % 256) < 256) & ((tl.program_id(0) % 256) < 256))), (tl.load(in8_ptr + ((((((((tl.program_id(0) // 4194304) * 32) + ((_lv0 * 32) + tl.arange(0, 32))) * 256) + ((tl.program_id(0) // 256) % 256)) * 256) + (tl.program_id(0) % 256)) + 0 * tl.arange(0, 32)), mask=((((_lv0 * 32) + tl.arange(0, 32)) < 32) & ((((tl.program_id(0) // 256) % 256) < 256) & ((tl.program_id(0) % 256) < 256))), other=0.0) * tl.load(in3_ptr + (((((tl.program_id(0) // 65536) % 64) * 32) + ((_lv0 * 32) + tl.arange(0, 32))) + 0 * tl.arange(0, 32)), mask=((((_lv0 * 32) + tl.arange(0, 32)) < 32) & ((((tl.program_id(0) // 256) % 256) < 256) & ((tl.program_id(0) % 256) < 256))), other=0.0)), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t013_s5(out, ins):
    grid = (536870912,)
    t013_s5_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8])
    return out


@triton.jit
def t013_s6_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr):
    _acc0 = tl.zeros([4], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 4) + tl.arange(0, 4)) < 4) & ((((0 <= ((((tl.program_id(0) // 128) % 128) * 2) + (((_lv0 * 4) + tl.arange(0, 4)) // 2))) & (((((tl.program_id(0) // 128) % 128) * 2) + (((_lv0 * 4) + tl.arange(0, 4)) // 2)) < 256)) & (0 <= (((tl.program_id(0) % 128) * 2) + (((_lv0 * 4) + tl.arange(0, 4)) % 2)))) & ((((tl.program_id(0) % 128) * 2) + (((_lv0 * 4) + tl.arange(0, 4)) % 2)) < 256))), tl.load(in9_ptr + (tl.maximum((((((((tl.program_id(0) // 1048576) * 64) + ((tl.program_id(0) // 16384) % 64)) * 256) + ((((tl.program_id(0) // 128) % 128) * 2) + (((_lv0 * 4) + tl.arange(0, 4)) // 2))) * 256) + (((tl.program_id(0) % 128) * 2) + (((_lv0 * 4) + tl.arange(0, 4)) % 2))) - tl.maximum((((((((tl.program_id(0) // 1048576) * 64) + ((tl.program_id(0) // 16384) % 64)) * 256) + ((((tl.program_id(0) // 128) % 128) * 2) + (((_lv0 * 4) + tl.arange(0, 4)) // 2))) * 256) + (((tl.program_id(0) % 128) * 2) + (((_lv0 * 4) + tl.arange(0, 4)) % 2))) - 536870911, 0), 0) + 0 * tl.arange(0, 4)), mask=((((_lv0 * 4) + tl.arange(0, 4)) < 4) & ((((0 <= ((((tl.program_id(0) // 128) % 128) * 2) + (((_lv0 * 4) + tl.arange(0, 4)) // 2))) & (((((tl.program_id(0) // 128) % 128) * 2) + (((_lv0 * 4) + tl.arange(0, 4)) // 2)) < 256)) & (0 <= (((tl.program_id(0) % 128) * 2) + (((_lv0 * 4) + tl.arange(0, 4)) % 2)))) & ((((tl.program_id(0) % 128) * 2) + (((_lv0 * 4) + tl.arange(0, 4)) % 2)) < 256))), other=0.0), 0.0))
    _v = (tl.sum(_acc0, axis=0) * (1.0 * (1.0 / 4.0)))
    tl.store(out_ptr + tl.program_id(0), _v)


def t013_s6(out, ins):
    grid = (134217728,)
    t013_s6_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9])
    return out


def t013(out, ins):
    _t0 = torch.empty(8192, device=ins[0].device, dtype=torch.float32)
    _t1 = torch.empty(32, device=ins[0].device, dtype=torch.float32)
    _t2 = torch.empty(8192, device=ins[0].device, dtype=torch.float32)
    _t3 = torch.empty(32, device=ins[0].device, dtype=torch.float32)
    _t4 = torch.empty(268435456, device=ins[0].device, dtype=torch.float32)
    _t5 = torch.empty(536870912, device=ins[0].device, dtype=torch.float32)
    t013_s0(_t0, list(ins))
    t013_s1(_t1, list(ins) + [_t0])
    t013_s2(_t2, list(ins) + [_t0, _t1])
    t013_s3(_t3, list(ins) + [_t0, _t1, _t2])
    t013_s4(_t4, list(ins) + [_t0, _t1, _t2, _t3])
    t013_s5(_t5, list(ins) + [_t0, _t1, _t2, _t3, _t4])
    t013_s6(out, list(ins) + [_t0, _t1, _t2, _t3, _t4, _t5])
    return out
