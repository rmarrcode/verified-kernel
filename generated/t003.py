import torch
import triton
import triton.language as tl


@triton.jit
def _mul_combine(a, b):
    return a * b


@triton.jit
def t003_s0_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr):
    _acc0 = tl.zeros([512], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 512) + tl.arange(0, 512)) < 864) & (((((((((((((_lv0 * 512) + tl.arange(0, 512)) // 9) % 3) <= (((tl.program_id(0) // 4096) % 32) + 1)) & ((tl.maximum((((tl.program_id(0) // 4096) % 32) + 1) - ((((_lv0 * 512) + tl.arange(0, 512)) // 9) % 3), 0) % 2) == 0)) & ((tl.maximum((((tl.program_id(0) // 4096) % 32) + 1) - ((((_lv0 * 512) + tl.arange(0, 512)) // 9) % 3), 0) // 2) < 16)) & (((((_lv0 * 512) + tl.arange(0, 512)) // 3) % 3) <= (((tl.program_id(0) // 64) % 64) + 1))) & ((tl.maximum((((tl.program_id(0) // 64) % 64) + 1) - ((((_lv0 * 512) + tl.arange(0, 512)) // 3) % 3), 0) % 2) == 0)) & ((tl.maximum((((tl.program_id(0) // 64) % 64) + 1) - ((((_lv0 * 512) + tl.arange(0, 512)) // 3) % 3), 0) // 2) < 32)) & ((((_lv0 * 512) + tl.arange(0, 512)) % 3) <= ((tl.program_id(0) % 64) + 1))) & ((tl.maximum(((tl.program_id(0) % 64) + 1) - (((_lv0 * 512) + tl.arange(0, 512)) % 3), 0) % 2) == 0)) & ((tl.maximum(((tl.program_id(0) % 64) + 1) - (((_lv0 * 512) + tl.arange(0, 512)) % 3), 0) // 2) < 32))), (tl.load(in0_ptr + ((((((((((tl.program_id(0) // 8388608) * 32) + (((((tl.program_id(0) // 131072) % 64) // 64) * 32) + (((_lv0 * 512) + tl.arange(0, 512)) // 27))) * 16) + (tl.maximum((((tl.program_id(0) // 4096) % 32) + 1) - ((((_lv0 * 512) + tl.arange(0, 512)) // 9) % 3), 0) // 2)) * 32) + (tl.maximum((((tl.program_id(0) // 64) % 64) + 1) - ((((_lv0 * 512) + tl.arange(0, 512)) // 3) % 3), 0) // 2)) * 32) + (tl.maximum(((tl.program_id(0) % 64) + 1) - (((_lv0 * 512) + tl.arange(0, 512)) % 3), 0) // 2)) + 0 * tl.arange(0, 512)), mask=((((_lv0 * 512) + tl.arange(0, 512)) < 864) & (((((((((((((_lv0 * 512) + tl.arange(0, 512)) // 9) % 3) <= (((tl.program_id(0) // 4096) % 32) + 1)) & ((tl.maximum((((tl.program_id(0) // 4096) % 32) + 1) - ((((_lv0 * 512) + tl.arange(0, 512)) // 9) % 3), 0) % 2) == 0)) & ((tl.maximum((((tl.program_id(0) // 4096) % 32) + 1) - ((((_lv0 * 512) + tl.arange(0, 512)) // 9) % 3), 0) // 2) < 16)) & (((((_lv0 * 512) + tl.arange(0, 512)) // 3) % 3) <= (((tl.program_id(0) // 64) % 64) + 1))) & ((tl.maximum((((tl.program_id(0) // 64) % 64) + 1) - ((((_lv0 * 512) + tl.arange(0, 512)) // 3) % 3), 0) % 2) == 0)) & ((tl.maximum((((tl.program_id(0) // 64) % 64) + 1) - ((((_lv0 * 512) + tl.arange(0, 512)) // 3) % 3), 0) // 2) < 32)) & ((((_lv0 * 512) + tl.arange(0, 512)) % 3) <= ((tl.program_id(0) % 64) + 1))) & ((tl.maximum(((tl.program_id(0) % 64) + 1) - (((_lv0 * 512) + tl.arange(0, 512)) % 3), 0) % 2) == 0)) & ((tl.maximum(((tl.program_id(0) % 64) + 1) - (((_lv0 * 512) + tl.arange(0, 512)) % 3), 0) // 2) < 32))), other=0.0) * tl.load(in1_ptr + ((((((((((((((tl.program_id(0) // 131072) % 64) // 64) * 32) + (((_lv0 * 512) + tl.arange(0, 512)) // 27)) * 64) + (((tl.program_id(0) // 131072) % 64) % 64)) * 3) + ((((_lv0 * 512) + tl.arange(0, 512)) // 9) % 3)) * 3) + ((((_lv0 * 512) + tl.arange(0, 512)) // 3) % 3)) * 3) + (((_lv0 * 512) + tl.arange(0, 512)) % 3)) + 0 * tl.arange(0, 512)), mask=((((_lv0 * 512) + tl.arange(0, 512)) < 864) & (((((((((((((_lv0 * 512) + tl.arange(0, 512)) // 9) % 3) <= (((tl.program_id(0) // 4096) % 32) + 1)) & ((tl.maximum((((tl.program_id(0) // 4096) % 32) + 1) - ((((_lv0 * 512) + tl.arange(0, 512)) // 9) % 3), 0) % 2) == 0)) & ((tl.maximum((((tl.program_id(0) // 4096) % 32) + 1) - ((((_lv0 * 512) + tl.arange(0, 512)) // 9) % 3), 0) // 2) < 16)) & (((((_lv0 * 512) + tl.arange(0, 512)) // 3) % 3) <= (((tl.program_id(0) // 64) % 64) + 1))) & ((tl.maximum((((tl.program_id(0) // 64) % 64) + 1) - ((((_lv0 * 512) + tl.arange(0, 512)) // 3) % 3), 0) % 2) == 0)) & ((tl.maximum((((tl.program_id(0) // 64) % 64) + 1) - ((((_lv0 * 512) + tl.arange(0, 512)) // 3) % 3), 0) // 2) < 32)) & ((((_lv0 * 512) + tl.arange(0, 512)) % 3) <= ((tl.program_id(0) % 64) + 1))) & ((tl.maximum(((tl.program_id(0) % 64) + 1) - (((_lv0 * 512) + tl.arange(0, 512)) % 3), 0) % 2) == 0)) & ((tl.maximum(((tl.program_id(0) % 64) + 1) - (((_lv0 * 512) + tl.arange(0, 512)) % 3), 0) // 2) < 32))), other=0.0)), 0.0))
    _v = (tl.sum(_acc0, axis=0) + tl.load(in2_ptr + (((tl.program_id(0) // 131072) % 64))))
    tl.store(out_ptr + tl.program_id(0), _v)


def t003_s0(out, ins):
    grid = (268435456,)
    t003_s0_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5])
    return out


@triton.jit
def t003_s1_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr):
    _acc0 = tl.zeros([1], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), (tl.load(in6_ptr + ((((((((((tl.program_id(0) // 8388608) * 64) + ((tl.program_id(0) // 131072) % 64)) * 32) + ((tl.program_id(0) // 4096) % 32)) * 64) + ((tl.program_id(0) // 64) % 64)) * 64) + (tl.program_id(0) % 64)) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) + tl.load(in3_ptr + (0 + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t003_s1(out, ins):
    grid = (268435456,)
    t003_s1_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6])
    return out


@triton.jit
def t003_s2_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr):
    _acc0 = tl.zeros([64], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 64) + tl.arange(0, 64)) < 64) & True), tl.load(in7_ptr + (((tl.program_id(0) * 64) + ((_lv0 * 64) + tl.arange(0, 64))) + 0 * tl.arange(0, 64)), mask=((((_lv0 * 64) + tl.arange(0, 64)) < 64) & True), other=0.0), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t003_s2(out, ins):
    grid = (4194304,)
    t003_s2_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7])
    return out


@triton.jit
def t003_s3_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr):
    _acc0 = tl.zeros([64], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 64) + tl.arange(0, 64)) < 64) & True), ((tl.load(in7_ptr + (((tl.program_id(0) * 64) + ((_lv0 * 64) + tl.arange(0, 64))) + 0 * tl.arange(0, 64)), mask=((((_lv0 * 64) + tl.arange(0, 64)) < 64) & True), other=0.0) - (tl.load(in8_ptr + (tl.program_id(0) + 0 * tl.arange(0, 64)), mask=((((_lv0 * 64) + tl.arange(0, 64)) < 64) & True), other=0.0) * (1.0 * (1.0 / 64.0)))) * (tl.load(in7_ptr + (((tl.program_id(0) * 64) + ((_lv0 * 64) + tl.arange(0, 64))) + 0 * tl.arange(0, 64)), mask=((((_lv0 * 64) + tl.arange(0, 64)) < 64) & True), other=0.0) - (tl.load(in8_ptr + (tl.program_id(0) + 0 * tl.arange(0, 64)), mask=((((_lv0 * 64) + tl.arange(0, 64)) < 64) & True), other=0.0) * (1.0 * (1.0 / 64.0))))), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t003_s3(out, ins):
    grid = (4194304,)
    t003_s3_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8])
    return out


@triton.jit
def t003_s4_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr):
    _acc0 = tl.zeros([1], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), ((((tl.load(in7_ptr + (tl.program_id(0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) - (tl.load(in8_ptr + (tl.maximum((tl.program_id(0) // 64) - tl.maximum((tl.program_id(0) // 64) - 4194303, 0), 0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) * (1.0 * (1.0 / 64.0)))) * (1.0 / tl.sqrt(((tl.load(in9_ptr + (tl.maximum((tl.program_id(0) // 64) - tl.maximum((tl.program_id(0) // 64) - 4194303, 0), 0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) * (1.0 * (1.0 / 64.0))) + (1.0 * (1.0 / 100000.0)))))) * tl.load(in4_ptr + ((tl.program_id(0) % 64) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)) + tl.load(in5_ptr + ((tl.program_id(0) % 64) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t003_s4(out, ins):
    grid = (268435456,)
    t003_s4_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9])
    return out


@triton.jit
def t003_s5_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr):
    _acc0 = tl.zeros([8], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 8) + tl.arange(0, 8)) < 8) & ((((((0 <= ((((tl.program_id(0) // 1024) % 16) * 2) + (((_lv0 * 8) + tl.arange(0, 8)) // 4))) & (((((tl.program_id(0) // 1024) % 16) * 2) + (((_lv0 * 8) + tl.arange(0, 8)) // 4)) < 32)) & (0 <= ((((tl.program_id(0) // 32) % 32) * 2) + ((((_lv0 * 8) + tl.arange(0, 8)) // 2) % 2)))) & (((((tl.program_id(0) // 32) % 32) * 2) + ((((_lv0 * 8) + tl.arange(0, 8)) // 2) % 2)) < 64)) & (0 <= (((tl.program_id(0) % 32) * 2) + (((_lv0 * 8) + tl.arange(0, 8)) % 2)))) & ((((tl.program_id(0) % 32) * 2) + (((_lv0 * 8) + tl.arange(0, 8)) % 2)) < 64))), tl.load(in10_ptr + (tl.maximum((((((((((tl.program_id(0) // 1048576) * 64) + ((tl.program_id(0) // 16384) % 64)) * 32) + ((((tl.program_id(0) // 1024) % 16) * 2) + (((_lv0 * 8) + tl.arange(0, 8)) // 4))) * 64) + ((((tl.program_id(0) // 32) % 32) * 2) + ((((_lv0 * 8) + tl.arange(0, 8)) // 2) % 2))) * 64) + (((tl.program_id(0) % 32) * 2) + (((_lv0 * 8) + tl.arange(0, 8)) % 2))) - tl.maximum((((((((((tl.program_id(0) // 1048576) * 64) + ((tl.program_id(0) // 16384) % 64)) * 32) + ((((tl.program_id(0) // 1024) % 16) * 2) + (((_lv0 * 8) + tl.arange(0, 8)) // 4))) * 64) + ((((tl.program_id(0) // 32) % 32) * 2) + ((((_lv0 * 8) + tl.arange(0, 8)) // 2) % 2))) * 64) + (((tl.program_id(0) % 32) * 2) + (((_lv0 * 8) + tl.arange(0, 8)) % 2))) - 268435455, 0), 0) + 0 * tl.arange(0, 8)), mask=((((_lv0 * 8) + tl.arange(0, 8)) < 8) & ((((((0 <= ((((tl.program_id(0) // 1024) % 16) * 2) + (((_lv0 * 8) + tl.arange(0, 8)) // 4))) & (((((tl.program_id(0) // 1024) % 16) * 2) + (((_lv0 * 8) + tl.arange(0, 8)) // 4)) < 32)) & (0 <= ((((tl.program_id(0) // 32) % 32) * 2) + ((((_lv0 * 8) + tl.arange(0, 8)) // 2) % 2)))) & (((((tl.program_id(0) // 32) % 32) * 2) + ((((_lv0 * 8) + tl.arange(0, 8)) // 2) % 2)) < 64)) & (0 <= (((tl.program_id(0) % 32) * 2) + (((_lv0 * 8) + tl.arange(0, 8)) % 2)))) & ((((tl.program_id(0) % 32) * 2) + (((_lv0 * 8) + tl.arange(0, 8)) % 2)) < 64))), other=0.0), 0.0))
    _v = (((1.0 * (1.0 / 2.0)) * (tl.sum(_acc0, axis=0) * (1.0 * (1.0 / 8.0)))) * ((1.0 * (1.0 / 1.0)) + tl.erf(((tl.sum(_acc0, axis=0) * (1.0 * (1.0 / 8.0))) * (1.0 / tl.sqrt((2.0 * (1.0 / 1.0))))))))
    tl.store(out_ptr + tl.program_id(0), _v)


def t003_s5(out, ins):
    grid = (33554432,)
    t003_s5_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10])
    return out


def t003(out, ins):
    _t0 = torch.empty(268435456, device=ins[0].device, dtype=torch.float32)
    _t1 = torch.empty(268435456, device=ins[0].device, dtype=torch.float32)
    _t2 = torch.empty(4194304, device=ins[0].device, dtype=torch.float32)
    _t3 = torch.empty(4194304, device=ins[0].device, dtype=torch.float32)
    _t4 = torch.empty(268435456, device=ins[0].device, dtype=torch.float32)
    t003_s0(_t0, list(ins))
    t003_s1(_t1, list(ins) + [_t0])
    t003_s2(_t2, list(ins) + [_t0, _t1])
    t003_s3(_t3, list(ins) + [_t0, _t1, _t2])
    t003_s4(_t4, list(ins) + [_t0, _t1, _t2, _t3])
    t003_s5(out, list(ins) + [_t0, _t1, _t2, _t3, _t4])
    return out
