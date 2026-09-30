import torch
import triton
import triton.language as tl


@triton.jit
def _mul_combine(a, b):
    return a * b


@triton.jit
def sm0_s1_kernel(out_ptr, in0_ptr):
    _acc0 = tl.zeros([64], dtype=tl.float32) + (tl.load(in0_ptr + (((tl.program_id(0) * 64) + 0))))
    for _lv0 in range(0, 1):
        _acc0 = tl.maximum(_acc0, tl.load(in0_ptr + (((tl.program_id(0) * 64) + tl.maximum(((_lv0 * 64) + tl.arange(0, 64)) - tl.maximum(((_lv0 * 64) + tl.arange(0, 64)) - 63, 0), 0)))))
    _v = tl.max(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def sm0_s1(out, ins):
    grid = (8,)
    sm0_s1_kernel[grid](out, ins[0])
    return out


@triton.jit
def sm0_s2_kernel(out_ptr, in0_ptr, in1_ptr):
    _acc0 = tl.zeros([64], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 64) + tl.arange(0, 64)) < 64) & True), tl.exp((tl.load(in0_ptr + (((tl.program_id(0) * 64) + ((_lv0 * 64) + tl.arange(0, 64))) + 0 * tl.arange(0, 64)), mask=((((_lv0 * 64) + tl.arange(0, 64)) < 64) & True), other=0.0) - tl.load(in1_ptr + (tl.program_id(0) + 0 * tl.arange(0, 64)), mask=((((_lv0 * 64) + tl.arange(0, 64)) < 64) & True), other=0.0))), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def sm0_s2(out, ins):
    grid = (8,)
    sm0_s2_kernel[grid](out, ins[0], ins[1])
    return out


@triton.jit
def sm0_s3_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr):
    _acc0 = tl.zeros([1], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), (tl.exp((tl.load(in0_ptr + (tl.program_id(0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) - tl.load(in1_ptr + ((tl.program_id(0) // 64) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0))) * (1.0 / tl.load(in2_ptr + ((tl.program_id(0) // 64) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0))), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def sm0_s3(out, ins):
    grid = (512,)
    sm0_s3_kernel[grid](out, ins[0], ins[1], ins[2])
    return out


def sm0(out, ins):
    _t1 = torch.empty(8, device=ins[0].device, dtype=torch.float32)
    _t2 = torch.empty(8, device=ins[0].device, dtype=torch.float32)
    sm0_s1(_t1, ins)
    sm0_s2(_t2, list(ins) + [_t1])
    sm0_s3(out, list(ins) + [_t1, _t2])
    return out
