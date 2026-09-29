import torch
import triton
import triton.language as tl


@triton.jit
def _mul_combine(a, b):
    return a * b


@triton.jit
def t051_s0_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 8):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 8192) & True), (tl.load(in0_ptr + ((((tl.program_id(0) // 8192) * 8192) + ((_lv0 * 1024) + tl.arange(0, 1024))) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 8192) & True), other=0.0) * tl.load(in1_ptr + ((((tl.program_id(0) % 8192) * 8192) + ((_lv0 * 1024) + tl.arange(0, 1024))) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 8192) & True), other=0.0)), 0.0))
    _v = (tl.sum(_acc0, axis=0) + tl.load(in2_ptr + ((tl.program_id(0) % 8192))))
    tl.store(out_ptr + tl.program_id(0), _v)


def t051_s0(out, ins):
    grid = (16777216,)
    t051_s0_kernel[grid](out, ins[0], ins[1], ins[2], ins[3])
    return out


@triton.jit
def t051_s1_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr):
    _acc0 = tl.zeros([1], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), (tl.load(in4_ptr + ((((tl.program_id(0) // 8192) * 8192) + (tl.program_id(0) % 8192)) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) - tl.load(in3_ptr + ((tl.program_id(0) % 8192) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t051_s1(out, ins):
    grid = (16777216,)
    t051_s1_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4])
    return out


@triton.jit
def t051_s2_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 8):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 8192) & True), tl.load(in5_ptr + (((tl.program_id(0) * 8192) + ((_lv0 * 1024) + tl.arange(0, 1024))) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 8192) & True), other=0.0), 0.0))
    _v = (tl.sum(_acc0, axis=0) * (1.0 * (1.0 / 8192.0)))
    tl.store(out_ptr + tl.program_id(0), _v)


def t051_s2(out, ins):
    grid = (2048,)
    t051_s2_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5])
    return out


@triton.jit
def t051_s3_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr):
    _acc0 = tl.zeros([1], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), tl.exp(tl.load(in6_ptr + (tl.program_id(0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)), 0.0))
    _v = (((1.0 * (1.0 / 2.0)) * tl.log(tl.sum(_acc0, axis=0))) * ((1.0 * (1.0 / 1.0)) + tl.erf((tl.log(tl.sum(_acc0, axis=0)) * (1.0 / tl.sqrt((2.0 * (1.0 / 1.0))))))))
    tl.store(out_ptr + tl.program_id(0), _v)


def t051_s3(out, ins):
    grid = (2048,)
    t051_s3_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6])
    return out


@triton.jit
def t051_s4_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr):
    _acc0 = tl.zeros([1], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), (tl.load(in7_ptr + ((tl.program_id(0) // 8192) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) + tl.load(in0_ptr + ((((tl.program_id(0) // 8192) * 8192) + (tl.program_id(0) % 8192)) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t051_s4(out, ins):
    grid = (16777216,)
    t051_s4_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7])
    return out


def t051(out, ins):
    _t0 = torch.empty(16777216, device=ins[0].device, dtype=torch.float32)
    _t1 = torch.empty(16777216, device=ins[0].device, dtype=torch.float32)
    _t2 = torch.empty(2048, device=ins[0].device, dtype=torch.float32)
    _t3 = torch.empty(2048, device=ins[0].device, dtype=torch.float32)
    t051_s0(_t0, list(ins))
    t051_s1(_t1, list(ins) + [_t0])
    t051_s2(_t2, list(ins) + [_t0, _t1])
    t051_s3(_t3, list(ins) + [_t0, _t1, _t2])
    t051_s4(out, list(ins) + [_t0, _t1, _t2, _t3])
    return out
