import torch
import triton
import triton.language as tl


@triton.jit
def t100_s1_kernel(out_ptr, in0_ptr, in1_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 128):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 131072) & (((tl.program_id(0) * 131072) + ((_lv0 * 1024) + tl.arange(0, 1024))) < 536870912)), tl.maximum(((1.0 * (1.0 / 1.0)) - (tl.load(in0_ptr + ((((((tl.program_id(0) * 131072) + ((_lv0 * 1024) + tl.arange(0, 1024))) // 32768) * 32768) + (((tl.program_id(0) * 131072) + ((_lv0 * 1024) + tl.arange(0, 1024))) % 32768)) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 131072) & (((tl.program_id(0) * 131072) + ((_lv0 * 1024) + tl.arange(0, 1024))) < 536870912)), other=0.0) * tl.load(in1_ptr + ((((tl.program_id(0) * 131072) + ((_lv0 * 1024) + tl.arange(0, 1024))) % 32768) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 131072) & (((tl.program_id(0) * 131072) + ((_lv0 * 1024) + tl.arange(0, 1024))) < 536870912)), other=0.0))), (0.0 * (1.0 / 1.0))), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t100_s1(out, ins):
    grid = (4096,)
    t100_s1_kernel[grid](out, ins[0], ins[1])
    return out


@triton.jit
def t100_s2_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 4):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 4096) & True), tl.load(in2_ptr + (((_lv0 * 1024) + tl.arange(0, 1024)) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 4096) & True), other=0.0), 0.0))
    _v = (tl.sum(_acc0, axis=0) * (1.0 * (1.0 / 536870912.0)))
    tl.store(out_ptr + tl.program_id(0), _v)


def t100_s2(out, ins):
    grid = (1,)
    t100_s2_kernel[grid](out, ins[0], ins[1], ins[2])
    return out


def t100(out, ins):
    _tmp = torch.empty(4096, device=ins[0].device, dtype=torch.float32)
    t100_s1(_tmp, ins)
    t100_s2(out, list(ins) + [_tmp])
    return out
