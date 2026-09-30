import torch
import triton
import triton.language as tl


@triton.jit
def _mul_combine(a, b):
    return a * b


@triton.jit
def t059_s0_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 32):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 32768) & True), (tl.load(in0_ptr + ((((tl.program_id(0) // 32768) * 32768) + ((_lv0 * 1024) + tl.arange(0, 1024))) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 32768) & True), other=0.0) * tl.load(in1_ptr + ((((tl.program_id(0) % 32768) * 32768) + ((_lv0 * 1024) + tl.arange(0, 1024))) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 32768) & True), other=0.0)), 0.0))
    _v = (tl.sum(_acc0, axis=0) + tl.load(in2_ptr + ((tl.program_id(0) % 32768))))
    tl.store(out_ptr + tl.program_id(0), _v)


def t059_s0(out, ins):
    grid = (4194304,)
    t059_s0_kernel[grid](out, ins[0], ins[1], ins[2])
    return out


@triton.jit
def t059_s1_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr):
    _acc0 = tl.zeros([1], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), (1.0 / ((1.0 * (1.0 / 1.0)) + tl.exp(((0.0 * (1.0 / 1.0)) - tl.load(in3_ptr + ((((tl.program_id(0) // 32768) * 32768) + (tl.program_id(0) % 32768)) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0))))), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t059_s1(out, ins):
    grid = (4194304,)
    t059_s1_kernel[grid](out, ins[0], ins[1], ins[2], ins[3])
    return out


@triton.jit
def t059_s2_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr):
    _acc0 = tl.zeros([1], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), (tl.load(in3_ptr + ((((tl.program_id(0) // 32768) * 32768) + (tl.program_id(0) % 32768)) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) * tl.load(in4_ptr + ((((tl.program_id(0) // 32768) * 32768) + (tl.program_id(0) % 32768)) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)), 0.0))
    _v = (tl.sum(_acc0, axis=0) * (2.0 * (1.0 / 1.0)))
    tl.store(out_ptr + tl.program_id(0), _v)


def t059_s2(out, ins):
    grid = (4194304,)
    t059_s2_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4])
    return out


def t059(out, ins):
    _t0 = torch.empty(4194304, device=ins[0].device, dtype=torch.float32)
    _t1 = torch.empty(4194304, device=ins[0].device, dtype=torch.float32)
    t059_s0(_t0, list(ins))
    t059_s1(_t1, list(ins) + [_t0])
    t059_s2(out, list(ins) + [_t0, _t1])
    return out
