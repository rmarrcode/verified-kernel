import torch
import triton
import triton.language as tl


@triton.jit
def t036_s1_kernel(out_ptr, in0_ptr):
    _acc0 = tl.zeros([64], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 64) + tl.arange(0, 64)) < 64) & True), (tl.load(in0_ptr + ((((((tl.program_id(0) // 262144) * 64) + ((_lv0 * 64) + tl.arange(0, 64))) * 262144) + (tl.program_id(0) % 262144)) + 0 * tl.arange(0, 64)), mask=((((_lv0 * 64) + tl.arange(0, 64)) < 64) & True), other=0.0) * tl.load(in0_ptr + ((((((tl.program_id(0) // 262144) * 64) + ((_lv0 * 64) + tl.arange(0, 64))) * 262144) + (tl.program_id(0) % 262144)) + 0 * tl.arange(0, 64)), mask=((((_lv0 * 64) + tl.arange(0, 64)) < 64) & True), other=0.0)), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t036_s1(out, ins):
    grid = (3670016,)
    t036_s1_kernel[grid](out, ins[0])
    return out


@triton.jit
def t036_s2_kernel(out_ptr, in0_ptr, in1_ptr):
    _acc0 = tl.zeros([1], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), (tl.load(in0_ptr + (tl.program_id(0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) / tl.sqrt(((tl.load(in1_ptr + ((((tl.program_id(0) // (64 * 262144)) * 262144) + (tl.program_id(0) % 262144)) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) * (1.0 * (1.0 / 64.0))) + (1.0 * (1.0 / 100000.0))))), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t036_s2(out, ins):
    grid = (234881024,)
    t036_s2_kernel[grid](out, ins[0], ins[1])
    return out


def t036(out, ins):
    _tmp = torch.empty(3670016, device=ins[0].device, dtype=torch.float32)
    t036_s1(_tmp, ins)
    t036_s2(out, list(ins) + [_tmp])
    return out
