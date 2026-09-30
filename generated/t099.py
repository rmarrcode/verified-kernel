import torch
import triton
import triton.language as tl


@triton.jit
def _mul_combine(a, b):
    return a * b


@triton.jit
def t099_s1_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 8):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 8192) & True), (((tl.load(in0_ptr + (((tl.program_id(0) * 8192) + ((_lv0 * 1024) + tl.arange(0, 1024))) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 8192) & True), other=0.0) - tl.load(in1_ptr + (((tl.program_id(0) * 8192) + ((_lv0 * 1024) + tl.arange(0, 1024))) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 8192) & True), other=0.0)) + (1.0 * (1.0 / 1000000.0))) * ((tl.load(in0_ptr + (((tl.program_id(0) * 8192) + ((_lv0 * 1024) + tl.arange(0, 1024))) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 8192) & True), other=0.0) - tl.load(in1_ptr + (((tl.program_id(0) * 8192) + ((_lv0 * 1024) + tl.arange(0, 1024))) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 8192) & True), other=0.0)) + (1.0 * (1.0 / 1000000.0)))), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t099_s1(out, ins):
    grid = (32768,)
    t099_s1_kernel[grid](out, ins[0], ins[1], ins[2])
    return out


@triton.jit
def t099_s2_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 8):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 8192) & True), (((tl.load(in0_ptr + (((tl.program_id(0) * 8192) + ((_lv0 * 1024) + tl.arange(0, 1024))) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 8192) & True), other=0.0) - tl.load(in2_ptr + (((tl.program_id(0) * 8192) + ((_lv0 * 1024) + tl.arange(0, 1024))) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 8192) & True), other=0.0)) + (1.0 * (1.0 / 1000000.0))) * ((tl.load(in0_ptr + (((tl.program_id(0) * 8192) + ((_lv0 * 1024) + tl.arange(0, 1024))) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 8192) & True), other=0.0) - tl.load(in2_ptr + (((tl.program_id(0) * 8192) + ((_lv0 * 1024) + tl.arange(0, 1024))) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 8192) & True), other=0.0)) + (1.0 * (1.0 / 1000000.0)))), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t099_s2(out, ins):
    grid = (32768,)
    t099_s2_kernel[grid](out, ins[0], ins[1], ins[2], ins[3])
    return out


@triton.jit
def t099_s3_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 32):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 32768) & True), tl.maximum(((tl.sqrt(tl.load(in3_ptr + (((_lv0 * 1024) + tl.arange(0, 1024)) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 32768) & True), other=0.0)) - tl.sqrt(tl.load(in4_ptr + (((_lv0 * 1024) + tl.arange(0, 1024)) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 32768) & True), other=0.0))) + (1.0 * (1.0 / 1.0))), (0.0 * (1.0 / 1.0))), 0.0))
    _v = (tl.sum(_acc0, axis=0) * (1.0 * (1.0 / 32768.0)))
    tl.store(out_ptr + tl.program_id(0), _v)


def t099_s3(out, ins):
    grid = (1,)
    t099_s3_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4])
    return out


def t099(out, ins):
    _t1 = torch.empty(32768, device=ins[0].device, dtype=torch.float32)
    _t2 = torch.empty(32768, device=ins[0].device, dtype=torch.float32)
    t099_s1(_t1, ins)
    t099_s2(_t2, list(ins) + [_t1])
    t099_s3(out, list(ins) + [_t1, _t2])
    return out
