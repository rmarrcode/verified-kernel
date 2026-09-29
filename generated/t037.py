import torch
import triton
import triton.language as tl


@triton.jit
def _mul_combine(a, b):
    return a * b


@triton.jit
def t037_s1_kernel(out_ptr, in0_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 56):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 57344) & (((tl.program_id(0) * 57344) + ((_lv0 * 1024) + tl.arange(0, 1024))) < 234881024)), (tl.load(in0_ptr + (((tl.program_id(0) * 57344) + ((_lv0 * 1024) + tl.arange(0, 1024))) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 57344) & (((tl.program_id(0) * 57344) + ((_lv0 * 1024) + tl.arange(0, 1024))) < 234881024)), other=0.0) * tl.load(in0_ptr + (((tl.program_id(0) * 57344) + ((_lv0 * 1024) + tl.arange(0, 1024))) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 57344) & (((tl.program_id(0) * 57344) + ((_lv0 * 1024) + tl.arange(0, 1024))) < 234881024)), other=0.0)), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t037_s1(out, ins):
    grid = (4096,)
    t037_s1_kernel[grid](out, ins[0])
    return out


@triton.jit
def t037_s2_kernel(out_ptr, in0_ptr, in1_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 4):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 4096) & True), tl.load(in1_ptr + (((_lv0 * 1024) + tl.arange(0, 1024)) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 4096) & True), other=0.0), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t037_s2(out, ins):
    grid = (1,)
    t037_s2_kernel[grid](out, ins[0], ins[1])
    return out


@triton.jit
def t037_s3_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr):
    _acc0 = tl.zeros([1], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), (tl.load(in0_ptr + (tl.program_id(0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) / tl.sqrt(tl.load(in2_ptr + (0 + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0))), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t037_s3(out, ins):
    grid = (234881024,)
    t037_s3_kernel[grid](out, ins[0], ins[1], ins[2])
    return out


def t037(out, ins):
    _t1 = torch.empty(4096, device=ins[0].device, dtype=torch.float32)
    _t2 = torch.empty(1, device=ins[0].device, dtype=torch.float32)
    t037_s1(_t1, ins)
    t037_s2(_t2, list(ins) + [_t1])
    t037_s3(out, list(ins) + [_t1, _t2])
    return out
