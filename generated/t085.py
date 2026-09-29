import torch
import triton
import triton.language as tl


@triton.jit
def _mul_combine(a, b):
    return a * b


@triton.jit
def t085_s0_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr):
    _acc0 = tl.zeros([64], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 64) + tl.arange(0, 64)) < 72) & (((((tl.program_id(0) // 126) % 126) + ((((_lv0 * 64) + tl.arange(0, 64)) // 3) % 3)) < 128) & (((tl.program_id(0) % 126) + (((_lv0 * 64) + tl.arange(0, 64)) % 3)) < 128))), (tl.load(in0_ptr + ((((((((tl.program_id(0) // 1016064) * 8) + (((_lv0 * 64) + tl.arange(0, 64)) // 9)) * 128) + (((tl.program_id(0) // 126) % 126) + ((((_lv0 * 64) + tl.arange(0, 64)) // 3) % 3))) * 128) + ((tl.program_id(0) % 126) + (((_lv0 * 64) + tl.arange(0, 64)) % 3))) + 0 * tl.arange(0, 64)), mask=((((_lv0 * 64) + tl.arange(0, 64)) < 72) & (((((tl.program_id(0) // 126) % 126) + ((((_lv0 * 64) + tl.arange(0, 64)) // 3) % 3)) < 128) & (((tl.program_id(0) % 126) + (((_lv0 * 64) + tl.arange(0, 64)) % 3)) < 128))), other=0.0) * tl.load(in1_ptr + (((((((((tl.program_id(0) // 15876) % 64) * 8) + (((_lv0 * 64) + tl.arange(0, 64)) // 9)) * 3) + ((((_lv0 * 64) + tl.arange(0, 64)) // 3) % 3)) * 3) + (((_lv0 * 64) + tl.arange(0, 64)) % 3)) + 0 * tl.arange(0, 64)), mask=((((_lv0 * 64) + tl.arange(0, 64)) < 72) & (((((tl.program_id(0) // 126) % 126) + ((((_lv0 * 64) + tl.arange(0, 64)) // 3) % 3)) < 128) & (((tl.program_id(0) % 126) + (((_lv0 * 64) + tl.arange(0, 64)) % 3)) < 128))), other=0.0)), 0.0))
    _v = (tl.sum(_acc0, axis=0) + tl.load(in2_ptr + (((tl.program_id(0) // 15876) % 64))))
    tl.store(out_ptr + tl.program_id(0), _v)


def t085_s0(out, ins):
    grid = (130056192,)
    t085_s0_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5])
    return out


@triton.jit
def t085_s1_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 63):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 63504) & True), tl.load(in6_ptr + (tl.maximum(((((((tl.program_id(0) // 16) * 64) + ((tl.program_id(0) % 16) * 4)) + (((_lv0 * 1024) + tl.arange(0, 1024)) // 15876)) * 15876) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 15876)) - tl.maximum(((((((tl.program_id(0) // 16) * 64) + ((tl.program_id(0) % 16) * 4)) + (((_lv0 * 1024) + tl.arange(0, 1024)) // 15876)) * 15876) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 15876)) - 130056191, 0), 0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 63504) & True), other=0.0), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t085_s1(out, ins):
    grid = (2048,)
    t085_s1_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6])
    return out


@triton.jit
def t085_s2_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 63):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 63504) & True), ((tl.load(in6_ptr + (tl.maximum(((((((tl.program_id(0) // 16) * 64) + ((tl.program_id(0) % 16) * 4)) + (((_lv0 * 1024) + tl.arange(0, 1024)) // 15876)) * 15876) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 15876)) - tl.maximum(((((((tl.program_id(0) // 16) * 64) + ((tl.program_id(0) % 16) * 4)) + (((_lv0 * 1024) + tl.arange(0, 1024)) // 15876)) * 15876) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 15876)) - 130056191, 0), 0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 63504) & True), other=0.0) - (tl.load(in7_ptr + (tl.program_id(0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 63504) & True), other=0.0) * (1.0 * (1.0 / 63504.0)))) * (tl.load(in6_ptr + (tl.maximum(((((((tl.program_id(0) // 16) * 64) + ((tl.program_id(0) % 16) * 4)) + (((_lv0 * 1024) + tl.arange(0, 1024)) // 15876)) * 15876) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 15876)) - tl.maximum(((((((tl.program_id(0) // 16) * 64) + ((tl.program_id(0) % 16) * 4)) + (((_lv0 * 1024) + tl.arange(0, 1024)) // 15876)) * 15876) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 15876)) - 130056191, 0), 0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 63504) & True), other=0.0) - (tl.load(in7_ptr + (tl.program_id(0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 63504) & True), other=0.0) * (1.0 * (1.0 / 63504.0))))), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t085_s2(out, ins):
    grid = (2048,)
    t085_s2_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7])
    return out


@triton.jit
def t085_s3_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr):
    _acc0 = tl.zeros([1], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), ((((tl.load(in6_ptr + (tl.program_id(0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) - (tl.load(in7_ptr + (tl.maximum((((tl.program_id(0) // 1016064) * 16) + (((tl.program_id(0) // 15876) % 64) // 4)) - tl.maximum((((tl.program_id(0) // 1016064) * 16) + (((tl.program_id(0) // 15876) % 64) // 4)) - 2047, 0), 0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) * (1.0 * (1.0 / 63504.0)))) * (1.0 / tl.sqrt(((tl.load(in8_ptr + (tl.maximum((((tl.program_id(0) // 1016064) * 16) + (((tl.program_id(0) // 15876) % 64) // 4)) - tl.maximum((((tl.program_id(0) // 1016064) * 16) + (((tl.program_id(0) // 15876) % 64) // 4)) - 2047, 0), 0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) * (1.0 * (1.0 / 63504.0))) + (1.0 * (1.0 / 100000.0)))))) * tl.load(in3_ptr + (((tl.program_id(0) // 15876) % 64) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)) + tl.load(in4_ptr + (((tl.program_id(0) // 15876) % 64) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t085_s3(out, ins):
    grid = (130056192,)
    t085_s3_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8])
    return out


@triton.jit
def t085_s4_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr):
    _acc0 = tl.zeros([1], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), (tl.load(in9_ptr + ((((((((tl.program_id(0) // 1016064) * 64) + ((tl.program_id(0) // 15876) % 64)) * 126) + ((tl.program_id(0) // 126) % 126)) * 126) + (tl.program_id(0) % 126)) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) * tl.load(in5_ptr + (((tl.program_id(0) // 15876) % 64) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t085_s4(out, ins):
    grid = (130056192,)
    t085_s4_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9])
    return out


@triton.jit
def t085_s5_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr):
    _acc0 = tl.zeros([16], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = tl.maximum(_acc0, tl.load(in10_ptr + ((((((((tl.program_id(0) // 61504) * 64) + ((tl.program_id(0) // 961) % 64)) * 126) + tl.maximum(((((tl.program_id(0) // 31) % 31) * 4) + tl.maximum(((tl.maximum(((_lv0 * 16) + tl.arange(0, 16)) - tl.maximum(((_lv0 * 16) + tl.arange(0, 16)) - 15, 0), 0) // 4) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 31) % 31) * 4), 0) - (tl.maximum(((_lv0 * 16) + tl.arange(0, 16)) - tl.maximum(((_lv0 * 16) + tl.arange(0, 16)) - 15, 0), 0) // 4), 0)) - tl.maximum(((tl.maximum(((_lv0 * 16) + tl.arange(0, 16)) - tl.maximum(((_lv0 * 16) + tl.arange(0, 16)) - 15, 0), 0) // 4) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 31) % 31) * 4), 0) - (tl.maximum(((_lv0 * 16) + tl.arange(0, 16)) - tl.maximum(((_lv0 * 16) + tl.arange(0, 16)) - 15, 0), 0) // 4), 0)) - tl.maximum(125 - (((tl.program_id(0) // 31) % 31) * 4), 0), 0), 0)) - tl.maximum(((((tl.program_id(0) // 31) % 31) * 4) + tl.maximum(((tl.maximum(((_lv0 * 16) + tl.arange(0, 16)) - tl.maximum(((_lv0 * 16) + tl.arange(0, 16)) - 15, 0), 0) // 4) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 31) % 31) * 4), 0) - (tl.maximum(((_lv0 * 16) + tl.arange(0, 16)) - tl.maximum(((_lv0 * 16) + tl.arange(0, 16)) - 15, 0), 0) // 4), 0)) - tl.maximum(((tl.maximum(((_lv0 * 16) + tl.arange(0, 16)) - tl.maximum(((_lv0 * 16) + tl.arange(0, 16)) - 15, 0), 0) // 4) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 31) % 31) * 4), 0) - (tl.maximum(((_lv0 * 16) + tl.arange(0, 16)) - tl.maximum(((_lv0 * 16) + tl.arange(0, 16)) - 15, 0), 0) // 4), 0)) - tl.maximum(125 - (((tl.program_id(0) // 31) % 31) * 4), 0), 0), 0)) - 125, 0), 0)) * 126) + tl.maximum((((tl.program_id(0) % 31) * 4) + tl.maximum(((tl.maximum(((_lv0 * 16) + tl.arange(0, 16)) - tl.maximum(((_lv0 * 16) + tl.arange(0, 16)) - 15, 0), 0) % 4) + tl.maximum(tl.maximum(0 - ((tl.program_id(0) % 31) * 4), 0) - (tl.maximum(((_lv0 * 16) + tl.arange(0, 16)) - tl.maximum(((_lv0 * 16) + tl.arange(0, 16)) - 15, 0), 0) % 4), 0)) - tl.maximum(((tl.maximum(((_lv0 * 16) + tl.arange(0, 16)) - tl.maximum(((_lv0 * 16) + tl.arange(0, 16)) - 15, 0), 0) % 4) + tl.maximum(tl.maximum(0 - ((tl.program_id(0) % 31) * 4), 0) - (tl.maximum(((_lv0 * 16) + tl.arange(0, 16)) - tl.maximum(((_lv0 * 16) + tl.arange(0, 16)) - 15, 0), 0) % 4), 0)) - tl.maximum(125 - ((tl.program_id(0) % 31) * 4), 0), 0), 0)) - tl.maximum((((tl.program_id(0) % 31) * 4) + tl.maximum(((tl.maximum(((_lv0 * 16) + tl.arange(0, 16)) - tl.maximum(((_lv0 * 16) + tl.arange(0, 16)) - 15, 0), 0) % 4) + tl.maximum(tl.maximum(0 - ((tl.program_id(0) % 31) * 4), 0) - (tl.maximum(((_lv0 * 16) + tl.arange(0, 16)) - tl.maximum(((_lv0 * 16) + tl.arange(0, 16)) - 15, 0), 0) % 4), 0)) - tl.maximum(((tl.maximum(((_lv0 * 16) + tl.arange(0, 16)) - tl.maximum(((_lv0 * 16) + tl.arange(0, 16)) - 15, 0), 0) % 4) + tl.maximum(tl.maximum(0 - ((tl.program_id(0) % 31) * 4), 0) - (tl.maximum(((_lv0 * 16) + tl.arange(0, 16)) - tl.maximum(((_lv0 * 16) + tl.arange(0, 16)) - 15, 0), 0) % 4), 0)) - tl.maximum(125 - ((tl.program_id(0) % 31) * 4), 0), 0), 0)) - 125, 0), 0)))))
    _v = tl.minimum(tl.maximum(tl.max(_acc0, axis=0), (0.0 * (1.0 / 1.0))), (1.0 * (1.0 / 1.0)))
    tl.store(out_ptr + tl.program_id(0), _v)


def t085_s5(out, ins):
    grid = (7872512,)
    t085_s5_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10])
    return out


def t085(out, ins):
    _t0 = torch.empty(130056192, device=ins[0].device, dtype=torch.float32)
    _t1 = torch.empty(2048, device=ins[0].device, dtype=torch.float32)
    _t2 = torch.empty(2048, device=ins[0].device, dtype=torch.float32)
    _t3 = torch.empty(130056192, device=ins[0].device, dtype=torch.float32)
    _t4 = torch.empty(130056192, device=ins[0].device, dtype=torch.float32)
    t085_s0(_t0, list(ins))
    t085_s1(_t1, list(ins) + [_t0])
    t085_s2(_t2, list(ins) + [_t0, _t1])
    t085_s3(_t3, list(ins) + [_t0, _t1, _t2])
    t085_s4(_t4, list(ins) + [_t0, _t1, _t2, _t3])
    t085_s5(out, list(ins) + [_t0, _t1, _t2, _t3, _t4])
    return out
