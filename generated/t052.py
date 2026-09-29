import torch
import triton
import triton.language as tl


@triton.jit
def _mul_combine(a, b):
    return a * b


@triton.jit
def t052_s0_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr):
    _acc0 = tl.zeros([512], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 512) + tl.arange(0, 512)) < 576) & (((((tl.program_id(0) // 126) % 126) + ((((_lv0 * 512) + tl.arange(0, 512)) // 3) % 3)) < 128) & (((tl.program_id(0) % 126) + (((_lv0 * 512) + tl.arange(0, 512)) % 3)) < 128))), (tl.load(in0_ptr + ((((((((tl.program_id(0) // 2032128) * 64) + (((_lv0 * 512) + tl.arange(0, 512)) // 9)) * 128) + (((tl.program_id(0) // 126) % 126) + ((((_lv0 * 512) + tl.arange(0, 512)) // 3) % 3))) * 128) + ((tl.program_id(0) % 126) + (((_lv0 * 512) + tl.arange(0, 512)) % 3))) + 0 * tl.arange(0, 512)), mask=((((_lv0 * 512) + tl.arange(0, 512)) < 576) & (((((tl.program_id(0) // 126) % 126) + ((((_lv0 * 512) + tl.arange(0, 512)) // 3) % 3)) < 128) & (((tl.program_id(0) % 126) + (((_lv0 * 512) + tl.arange(0, 512)) % 3)) < 128))), other=0.0) * tl.load(in1_ptr + (((((((((tl.program_id(0) // 15876) % 128) * 64) + (((_lv0 * 512) + tl.arange(0, 512)) // 9)) * 3) + ((((_lv0 * 512) + tl.arange(0, 512)) // 3) % 3)) * 3) + (((_lv0 * 512) + tl.arange(0, 512)) % 3)) + 0 * tl.arange(0, 512)), mask=((((_lv0 * 512) + tl.arange(0, 512)) < 576) & (((((tl.program_id(0) // 126) % 126) + ((((_lv0 * 512) + tl.arange(0, 512)) // 3) % 3)) < 128) & (((tl.program_id(0) % 126) + (((_lv0 * 512) + tl.arange(0, 512)) % 3)) < 128))), other=0.0)), 0.0))
    _v = (tl.sum(_acc0, axis=0) + tl.load(in2_ptr + (((tl.program_id(0) // 15876) % 128))))
    tl.store(out_ptr + tl.program_id(0), _v)


def t052_s0(out, ins):
    grid = (130056192,)
    t052_s0_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4])
    return out


@triton.jit
def t052_s1_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr):
    _acc0 = tl.zeros([1], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), tl.log(((1.0 * (1.0 / 1.0)) + tl.exp(tl.load(in5_ptr + ((((((((tl.program_id(0) // 2032128) * 128) + ((tl.program_id(0) // 15876) % 128)) * 126) + ((tl.program_id(0) // 126) % 126)) * 126) + (tl.program_id(0) % 126)) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)))), 0.0))
    _v = (2.0 * tl.sigmoid(2.0 * (tl.sum(_acc0, axis=0))) - 1.0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t052_s1(out, ins):
    grid = (130056192,)
    t052_s1_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5])
    return out


@triton.jit
def t052_s2_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr):
    _acc0 = tl.zeros([1], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), (tl.load(in6_ptr + ((((((((tl.program_id(0) // 2032128) * 128) + ((tl.program_id(0) // 15876) % 128)) * 126) + ((tl.program_id(0) // 126) % 126)) * 126) + (tl.program_id(0) % 126)) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) * tl.load(in5_ptr + ((((((((tl.program_id(0) // 2032128) * 128) + ((tl.program_id(0) // 15876) % 128)) * 126) + ((tl.program_id(0) // 126) % 126)) * 126) + (tl.program_id(0) % 126)) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t052_s2(out, ins):
    grid = (130056192,)
    t052_s2_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6])
    return out


@triton.jit
def t052_s3_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 993):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 1016064) & True), tl.load(in7_ptr + (tl.maximum((((((((_lv0 * 1024) + tl.arange(0, 1024)) // 15876) * 128) + tl.program_id(0)) * 15876) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 15876)) - tl.maximum((((((((_lv0 * 1024) + tl.arange(0, 1024)) // 15876) * 128) + tl.program_id(0)) * 15876) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 15876)) - 130056191, 0), 0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 1016064) & True), other=0.0), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t052_s3(out, ins):
    grid = (128,)
    t052_s3_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7])
    return out


@triton.jit
def t052_s4_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 993):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 1016064) & True), ((tl.load(in7_ptr + (tl.maximum((((((((_lv0 * 1024) + tl.arange(0, 1024)) // 15876) * 128) + tl.program_id(0)) * 15876) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 15876)) - tl.maximum((((((((_lv0 * 1024) + tl.arange(0, 1024)) // 15876) * 128) + tl.program_id(0)) * 15876) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 15876)) - 130056191, 0), 0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 1016064) & True), other=0.0) - (tl.load(in8_ptr + (tl.program_id(0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 1016064) & True), other=0.0) * (1.0 * (1.0 / 1016064.0)))) * (tl.load(in7_ptr + (tl.maximum((((((((_lv0 * 1024) + tl.arange(0, 1024)) // 15876) * 128) + tl.program_id(0)) * 15876) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 15876)) - tl.maximum((((((((_lv0 * 1024) + tl.arange(0, 1024)) // 15876) * 128) + tl.program_id(0)) * 15876) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 15876)) - 130056191, 0), 0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 1016064) & True), other=0.0) - (tl.load(in8_ptr + (tl.program_id(0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 1016064) & True), other=0.0) * (1.0 * (1.0 / 1016064.0))))), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t052_s4(out, ins):
    grid = (128,)
    t052_s4_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8])
    return out


@triton.jit
def t052_s5_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr):
    _acc0 = tl.zeros([1], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), ((((tl.load(in7_ptr + (tl.program_id(0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) - (tl.load(in8_ptr + (tl.maximum(((tl.program_id(0) // 15876) % 128) - tl.maximum(((tl.program_id(0) // 15876) % 128) - 127, 0), 0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) * (1.0 * (1.0 / 1016064.0)))) * (1.0 / tl.sqrt(((tl.load(in9_ptr + (tl.maximum(((tl.program_id(0) // 15876) % 128) - tl.maximum(((tl.program_id(0) // 15876) % 128) - 127, 0), 0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) * (1.0 * (1.0 / 1016064.0))) + (1.0 * (1.0 / 100000.0)))))) * tl.load(in3_ptr + (((tl.program_id(0) // 15876) % 128) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)) + tl.load(in4_ptr + (((tl.program_id(0) // 15876) % 128) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t052_s5(out, ins):
    grid = (130056192,)
    t052_s5_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9])
    return out


def t052(out, ins):
    _t0 = torch.empty(130056192, device=ins[0].device, dtype=torch.float32)
    _t1 = torch.empty(130056192, device=ins[0].device, dtype=torch.float32)
    _t2 = torch.empty(130056192, device=ins[0].device, dtype=torch.float32)
    _t3 = torch.empty(128, device=ins[0].device, dtype=torch.float32)
    _t4 = torch.empty(128, device=ins[0].device, dtype=torch.float32)
    t052_s0(_t0, list(ins))
    t052_s1(_t1, list(ins) + [_t0])
    t052_s2(_t2, list(ins) + [_t0, _t1])
    t052_s3(_t3, list(ins) + [_t0, _t1, _t2])
    t052_s4(_t4, list(ins) + [_t0, _t1, _t2, _t3])
    t052_s5(out, list(ins) + [_t0, _t1, _t2, _t3, _t4])
    return out
