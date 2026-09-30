import torch
import triton
import triton.language as tl


@triton.jit
def _mul_combine(a, b):
    return a * b


@triton.jit
def sm3_s1_kernel(out_ptr, in0_ptr):
    _acc0 = tl.zeros([16], dtype=tl.float32) + (tl.load(in0_ptr + ((((((tl.program_id(0) // 8) * 16) + 0) * 8) + (tl.program_id(0) % 8)))))
    for _lv0 in range(0, 1):
        _acc0 = tl.maximum(_acc0, tl.load(in0_ptr + ((((((tl.program_id(0) // 8) * 16) + tl.maximum(((_lv0 * 16) + tl.arange(0, 16)) - tl.maximum(((_lv0 * 16) + tl.arange(0, 16)) - 15, 0), 0)) * 8) + (tl.program_id(0) % 8)))))
    _v = tl.max(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def sm3_s1(out, ins):
    grid = (32,)
    sm3_s1_kernel[grid](out, ins[0])
    return out


@triton.jit
def sm3_s2_kernel(out_ptr, in0_ptr, in1_ptr):
    _acc0 = tl.zeros([16], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 16) + tl.arange(0, 16)) < 16) & True), tl.exp((tl.load(in0_ptr + ((((((tl.program_id(0) // 8) * 16) + ((_lv0 * 16) + tl.arange(0, 16))) * 8) + (tl.program_id(0) % 8)) + 0 * tl.arange(0, 16)), mask=((((_lv0 * 16) + tl.arange(0, 16)) < 16) & True), other=0.0) - tl.load(in1_ptr + (tl.program_id(0) + 0 * tl.arange(0, 16)), mask=((((_lv0 * 16) + tl.arange(0, 16)) < 16) & True), other=0.0))), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def sm3_s2(out, ins):
    grid = (32,)
    sm3_s2_kernel[grid](out, ins[0], ins[1])
    return out


@triton.jit
def sm3_s3_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr):
    _acc0 = tl.zeros([1], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), (tl.exp((tl.load(in0_ptr + (tl.program_id(0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) - tl.load(in1_ptr + ((((tl.program_id(0) // (16 * 8)) * 8) + (tl.program_id(0) % 8)) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0))) * (1.0 / tl.load(in2_ptr + ((((tl.program_id(0) // (16 * 8)) * 8) + (tl.program_id(0) % 8)) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0))), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def sm3_s3(out, ins):
    grid = (512,)
    sm3_s3_kernel[grid](out, ins[0], ins[1], ins[2])
    return out


def sm3(out, ins):
    _t1 = torch.empty(32, device=ins[0].device, dtype=torch.float32)
    _t2 = torch.empty(32, device=ins[0].device, dtype=torch.float32)
    sm3_s1(_t1, ins)
    sm3_s2(_t2, list(ins) + [_t1])
    sm3_s3(out, list(ins) + [_t1, _t2])
    return out
