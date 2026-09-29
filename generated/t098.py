import torch
import triton
import triton.language as tl


@triton.jit
def _mul_combine(a, b):
    return a * b


@triton.jit
def t098_s1_kernel(out_ptr, in0_ptr, in1_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 64):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 65536) & (((tl.program_id(0) * 65536) + ((_lv0 * 1024) + tl.arange(0, 1024))) < 268435456)), (tl.load(in1_ptr + ((((((tl.program_id(0) * 65536) + ((_lv0 * 1024) + tl.arange(0, 1024))) // 16384) * 16384) + (((tl.program_id(0) * 65536) + ((_lv0 * 1024) + tl.arange(0, 1024))) % 16384)) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 65536) & (((tl.program_id(0) * 65536) + ((_lv0 * 1024) + tl.arange(0, 1024))) < 268435456)), other=0.0) * (tl.log(tl.load(in1_ptr + ((((((tl.program_id(0) * 65536) + ((_lv0 * 1024) + tl.arange(0, 1024))) // 16384) * 16384) + (((tl.program_id(0) * 65536) + ((_lv0 * 1024) + tl.arange(0, 1024))) % 16384)) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 65536) & (((tl.program_id(0) * 65536) + ((_lv0 * 1024) + tl.arange(0, 1024))) < 268435456)), other=0.0)) - tl.log(tl.load(in0_ptr + ((((((tl.program_id(0) * 65536) + ((_lv0 * 1024) + tl.arange(0, 1024))) // 16384) * 16384) + (((tl.program_id(0) * 65536) + ((_lv0 * 1024) + tl.arange(0, 1024))) % 16384)) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 65536) & (((tl.program_id(0) * 65536) + ((_lv0 * 1024) + tl.arange(0, 1024))) < 268435456)), other=0.0)))), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t098_s1(out, ins):
    grid = (4096,)
    t098_s1_kernel[grid](out, ins[0], ins[1])
    return out


@triton.jit
def t098_s2_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 4):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 4096) & True), tl.load(in2_ptr + (((_lv0 * 1024) + tl.arange(0, 1024)) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 4096) & True), other=0.0), 0.0))
    _v = (tl.sum(_acc0, axis=0) * (1.0 * (1.0 / 16384.0)))
    tl.store(out_ptr + tl.program_id(0), _v)


def t098_s2(out, ins):
    grid = (1,)
    t098_s2_kernel[grid](out, ins[0], ins[1], ins[2])
    return out


def t098(out, ins):
    _tmp = torch.empty(4096, device=ins[0].device, dtype=torch.float32)
    t098_s1(_tmp, ins)
    t098_s2(out, list(ins) + [_tmp])
    return out
