import torch
import triton
import triton.language as tl


@triton.jit
def _mul_combine(a, b):
    return a * b


@triton.jit
def slc3_s0_kernel(out_ptr, in0_ptr):
    _acc0 = tl.zeros([1], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), tl.load(in0_ptr + ((((((tl.program_id(0) // 36) * 9) + ((tl.program_id(0) // 4) % 9)) * 12) + (tl.program_id(0) % 4)) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def slc3_s0(out, ins):
    grid = (72,)
    slc3_s0_kernel[grid](out, ins[0])
    return out


@triton.jit
def slc3_s1_kernel(out_ptr, in0_ptr, in1_ptr):
    _acc0 = tl.zeros([1], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), tl.load(in0_ptr + ((((((tl.program_id(0) // 36) * 9) + ((tl.program_id(0) // 4) % 9)) * 12) + ((tl.program_id(0) % 4) + 4)) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def slc3_s1(out, ins):
    grid = (72,)
    slc3_s1_kernel[grid](out, ins[0], ins[1])
    return out


@triton.jit
def slc3_s2_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr):
    _acc0 = tl.zeros([1], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), tl.load(in0_ptr + ((((((tl.program_id(0) // 36) * 9) + ((tl.program_id(0) // 4) % 9)) * 12) + ((tl.program_id(0) % 4) + 8)) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def slc3_s2(out, ins):
    grid = (72,)
    slc3_s2_kernel[grid](out, ins[0], ins[1], ins[2])
    return out


@triton.jit
def slc3_s3_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr):
    _acc0 = tl.zeros([1], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), (tl.load(in1_ptr + ((((((tl.program_id(0) // 36) * 9) + ((tl.program_id(0) // 4) % 9)) * 4) + (tl.program_id(0) % 4)) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) + tl.load(in3_ptr + ((((((tl.program_id(0) // 36) * 9) + ((tl.program_id(0) // 4) % 9)) * 4) + (tl.program_id(0) % 4)) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def slc3_s3(out, ins):
    grid = (72,)
    slc3_s3_kernel[grid](out, ins[0], ins[1], ins[2], ins[3])
    return out


def slc3(out, ins):
    _t0 = torch.empty(72, device=ins[0].device, dtype=torch.float32)
    _t1 = torch.empty(72, device=ins[0].device, dtype=torch.float32)
    _t2 = torch.empty(72, device=ins[0].device, dtype=torch.float32)
    slc3_s0(_t0, list(ins))
    slc3_s1(_t1, list(ins) + [_t0])
    slc3_s2(_t2, list(ins) + [_t0, _t1])
    slc3_s3(out, list(ins) + [_t0, _t1, _t2])
    return out
