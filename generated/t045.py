import torch
import triton
import triton.language as tl


@triton.jit
def _mul_combine(a, b):
    return a * b


@triton.jit
def t045_s0_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 2048) & True), (tl.load(in0_ptr + ((((tl.program_id(0) // 4096) * 2048) + ((_lv0 * 1024) + tl.arange(0, 1024))) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 2048) & True), other=0.0) * tl.load(in1_ptr + ((((tl.program_id(0) % 4096) * 2048) + ((_lv0 * 1024) + tl.arange(0, 1024))) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 2048) & True), other=0.0)), 0.0))
    _v = (1.0 / ((1.0 * (1.0 / 1.0)) + tl.exp(((0.0 * (1.0 / 1.0)) - (tl.sum(_acc0, axis=0) + tl.load(in2_ptr + ((tl.program_id(0) % 4096))))))))
    tl.store(out_ptr + tl.program_id(0), _v)


def t045_s0(out, ins):
    grid = (67108864,)
    t045_s0_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4])
    return out


@triton.jit
def t045_s1_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 4):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 4096) & True), (tl.load(in5_ptr + ((((tl.program_id(0) // 1024) * 4096) + ((_lv0 * 1024) + tl.arange(0, 1024))) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 4096) & True), other=0.0) * tl.load(in3_ptr + ((((tl.program_id(0) % 1024) * 4096) + ((_lv0 * 1024) + tl.arange(0, 1024))) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 4096) & True), other=0.0)), 0.0))
    _v = (tl.sum(_acc0, axis=0) + tl.load(in4_ptr + ((tl.program_id(0) % 1024))))
    tl.store(out_ptr + tl.program_id(0), _v)


def t045_s1(out, ins):
    grid = (16777216,)
    t045_s1_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5])
    return out


@triton.jit
def t045_s2_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 1024) & True), tl.exp(tl.load(in6_ptr + (((tl.program_id(0) * 1024) + ((_lv0 * 1024) + tl.arange(0, 1024))) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 1024) & True), other=0.0)), 0.0))
    _v = tl.log(tl.sum(_acc0, axis=0))
    tl.store(out_ptr + tl.program_id(0), _v)


def t045_s2(out, ins):
    grid = (16384,)
    t045_s2_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6])
    return out


def t045(out, ins):
    _t0 = torch.empty(67108864, device=ins[0].device, dtype=torch.float32)
    _t1 = torch.empty(16777216, device=ins[0].device, dtype=torch.float32)
    t045_s0(_t0, list(ins))
    t045_s1(_t1, list(ins) + [_t0])
    t045_s2(out, list(ins) + [_t0, _t1])
    return out
