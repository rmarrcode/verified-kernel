import torch
import triton
import triton.language as tl


@triton.jit
def _mul_combine(a, b):
    return a * b


@triton.jit
def t098_s0_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 8):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 8192) & True), (tl.load(in0_ptr + ((((tl.program_id(0) // 8192) * 8192) + ((_lv0 * 1024) + tl.arange(0, 1024))) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 8192) & True), other=0.0) * tl.load(in1_ptr + ((((tl.program_id(0) % 8192) * 8192) + ((_lv0 * 1024) + tl.arange(0, 1024))) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 8192) & True), other=0.0)), 0.0))
    _v = (tl.sum(_acc0, axis=0) + tl.load(in2_ptr + ((tl.program_id(0) % 8192))))
    tl.store(out_ptr + tl.program_id(0), _v)


def t098_s0(out, ins):
    grid = (8388608,)
    t098_s0_kernel[grid](out, ins[0], ins[1], ins[2])
    return out


@triton.jit
def t098_s1_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr):
    _acc0 = tl.zeros([16], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 16) + tl.arange(0, 16)) < 16) & ((0 <= (((tl.program_id(0) % 512) * 16) + ((_lv0 * 16) + tl.arange(0, 16)))) & ((((tl.program_id(0) % 512) * 16) + ((_lv0 * 16) + tl.arange(0, 16))) < 8192))), tl.load(in3_ptr + (tl.maximum((((tl.program_id(0) // 512) * 8192) + (((tl.program_id(0) % 512) * 16) + ((_lv0 * 16) + tl.arange(0, 16)))) - tl.maximum((((tl.program_id(0) // 512) * 8192) + (((tl.program_id(0) % 512) * 16) + ((_lv0 * 16) + tl.arange(0, 16)))) - 8388607, 0), 0) + 0 * tl.arange(0, 16)), mask=((((_lv0 * 16) + tl.arange(0, 16)) < 16) & ((0 <= (((tl.program_id(0) % 512) * 16) + ((_lv0 * 16) + tl.arange(0, 16)))) & ((((tl.program_id(0) % 512) * 16) + ((_lv0 * 16) + tl.arange(0, 16))) < 8192))), other=0.0), 0.0))
    _v = ((((1.0 * (1.0 / 2.0)) * (tl.sum(_acc0, axis=0) * (1.0 * (1.0 / 16.0)))) * ((1.0 * (1.0 / 1.0)) + tl.erf(((tl.sum(_acc0, axis=0) * (1.0 * (1.0 / 16.0))) * (1.0 / tl.sqrt((2.0 * (1.0 / 1.0)))))))) * (2.0 * (1.0 / 1.0)))
    tl.store(out_ptr + tl.program_id(0), _v)


def t098_s1(out, ins):
    grid = (524288,)
    t098_s1_kernel[grid](out, ins[0], ins[1], ins[2], ins[3])
    return out


@triton.jit
def t098_s2_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr):
    _acc0 = tl.zeros([512], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = tl.maximum(_acc0, tl.load(in4_ptr + (((tl.program_id(0) * 512) + tl.maximum(((_lv0 * 512) + tl.arange(0, 512)) - tl.maximum(((_lv0 * 512) + tl.arange(0, 512)) - 511, 0), 0)))))
    _v = tl.max(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t098_s2(out, ins):
    grid = (1024,)
    t098_s2_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4])
    return out


def t098(out, ins):
    _t0 = torch.empty(8388608, device=ins[0].device, dtype=torch.float32)
    _t1 = torch.empty(524288, device=ins[0].device, dtype=torch.float32)
    t098_s0(_t0, list(ins))
    t098_s1(_t1, list(ins) + [_t0])
    t098_s2(out, list(ins) + [_t0, _t1])
    return out
