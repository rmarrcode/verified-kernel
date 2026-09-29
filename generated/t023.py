import torch
import triton
import triton.language as tl


@triton.jit
def t023_s1_kernel(out_ptr, in0_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 384):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 393216) & True), tl.exp(tl.load(in0_ptr + (((tl.program_id(0) * 393216) + ((_lv0 * 1024) + tl.arange(0, 1024))) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 393216) & True), other=0.0)), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t023_s1(out, ins):
    grid = (1024,)
    t023_s1_kernel[grid](out, ins[0])
    return out


@triton.jit
def t023_s2_kernel(out_ptr, in0_ptr, in1_ptr):
    _acc0 = tl.zeros([1], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), (tl.exp(tl.load(in0_ptr + (tl.program_id(0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)) * (1.0 / tl.load(in1_ptr + ((tl.program_id(0) // 393216) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0))), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t023_s2(out, ins):
    grid = (402653184,)
    t023_s2_kernel[grid](out, ins[0], ins[1])
    return out


def t023(out, ins):
    _tmp = torch.empty(1024, device=ins[0].device, dtype=torch.float32)
    t023_s1(_tmp, ins)
    t023_s2(out, list(ins) + [_tmp])
    return out
