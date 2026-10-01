import torch
import triton
import triton.language as tl


@triton.jit
def _mul_combine(a, b):
    return a * b


@triton.jit
def t097_s1_kernel(out_ptr, in0_ptr, in1_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 1024) & True), (tl.load(in0_ptr + ((((((tl.program_id(0) // 262144) * 512) + ((tl.program_id(0) // 512) % 512)) * 1024) + ((_lv0 * 1024) + tl.arange(0, 1024))) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 1024) & True), other=0.0) * tl.load(in1_ptr + ((((((tl.program_id(0) // 262144) * 512) + (tl.program_id(0) % 512)) * 1024) + ((_lv0 * 1024) + tl.arange(0, 1024))) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 1024) & True), other=0.0)), 0.0))
    _v = (tl.sum(_acc0, axis=0) * (1.0 / tl.sqrt((1024.0 * (1.0 / 1.0)))))
    tl.store(out_ptr + tl.program_id(0), _v)


def t097_s1(out, ins):
    grid = (67108864,)
    t097_s1_kernel[grid](out, ins[0], ins[1])
    return out


@triton.jit
def t097_s2_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr):
    _acc0 = tl.zeros([512], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 512) + tl.arange(0, 512)) < 512) & True), tl.exp(tl.load(in3_ptr + (((tl.program_id(0) * 512) + ((_lv0 * 512) + tl.arange(0, 512))) + 0 * tl.arange(0, 512)), mask=((((_lv0 * 512) + tl.arange(0, 512)) < 512) & True), other=0.0)), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t097_s2(out, ins):
    grid = (131072,)
    t097_s2_kernel[grid](out, ins[0], ins[1], ins[2], ins[3])
    return out


@triton.jit
def t097_s3_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr):
    _acc0 = tl.zeros([512], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 512) + tl.arange(0, 512)) < 512) & True), (tl.exp(tl.load(in3_ptr + ((((tl.program_id(0) // 1024) * 512) + ((_lv0 * 512) + tl.arange(0, 512))) + 0 * tl.arange(0, 512)), mask=((((_lv0 * 512) + tl.arange(0, 512)) < 512) & True), other=0.0)) * tl.load(in2_ptr + ((((((tl.program_id(0) // 524288) * 512) + ((_lv0 * 512) + tl.arange(0, 512))) * 1024) + (tl.program_id(0) % 1024)) + 0 * tl.arange(0, 512)), mask=((((_lv0 * 512) + tl.arange(0, 512)) < 512) & True), other=0.0)), 0.0))
    _v = (tl.sum(_acc0, axis=0) * (1.0 / tl.load(in4_ptr + ((tl.program_id(0) // 1024)))))
    tl.store(out_ptr + tl.program_id(0), _v)


def t097_s3(out, ins):
    grid = (134217728,)
    t097_s3_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4])
    return out


def t097(out, ins):
    _t1 = torch.empty(67108864, device=ins[0].device, dtype=torch.float32)
    _t2 = torch.empty(131072, device=ins[0].device, dtype=torch.float32)
    t097_s1(_t1, ins)
    t097_s2(_t2, list(ins) + [_t1])
    t097_s3(out, list(ins) + [_t1, _t2])
    return out
