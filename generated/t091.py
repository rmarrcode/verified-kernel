import torch
import triton
import triton.language as tl


@triton.jit
def _mul_combine(a, b):
    return a * b


@triton.jit
def t091_s1_kernel(out_ptr, in0_ptr):
    _acc0 = tl.zeros([256], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 256) + tl.arange(0, 256)) < 256) & True), tl.load(in0_ptr + (((((tl.program_id(0) // 128) * 32768) + ((tl.program_id(0) % 128) * 256)) + ((_lv0 * 256) + tl.arange(0, 256))) + 0 * tl.arange(0, 256)), mask=((((_lv0 * 256) + tl.arange(0, 256)) < 256) & True), other=0.0), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t091_s1(out, ins):
    grid = (1048576,)
    t091_s1_kernel[grid](out, ins[0])
    return out


@triton.jit
def t091_s2_kernel(out_ptr, in0_ptr, in1_ptr):
    _acc0 = tl.zeros([128], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 128) + tl.arange(0, 128)) < 128) & ((tl.program_id(0) % 128) < ((_lv0 * 128) + tl.arange(0, 128)))), tl.load(in1_ptr + ((((tl.program_id(0) // 128) * 128) + ((_lv0 * 128) + tl.arange(0, 128))) + 0 * tl.arange(0, 128)), mask=((((_lv0 * 128) + tl.arange(0, 128)) < 128) & ((tl.program_id(0) % 128) < ((_lv0 * 128) + tl.arange(0, 128)))), other=0.0), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t091_s2(out, ins):
    grid = (1048576,)
    t091_s2_kernel[grid](out, ins[0], ins[1])
    return out


@triton.jit
def t091_s3_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr):
    _acc0 = tl.zeros([256], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 256) + tl.arange(0, 256)) < 256) & ((tl.program_id(0) % 256) <= ((_lv0 * 256) + tl.arange(0, 256)))), tl.load(in0_ptr + (((((tl.program_id(0) // 32768) * 32768) + (((tl.program_id(0) % 32768) // 256) * 256)) + ((_lv0 * 256) + tl.arange(0, 256))) + 0 * tl.arange(0, 256)), mask=((((_lv0 * 256) + tl.arange(0, 256)) < 256) & ((tl.program_id(0) % 256) <= ((_lv0 * 256) + tl.arange(0, 256)))), other=0.0), 0.0))
    _v = (tl.sum(_acc0, axis=0) + tl.load(in2_ptr + ((((tl.program_id(0) // 32768) * 128) + ((tl.program_id(0) % 32768) // 256)))))
    tl.store(out_ptr + tl.program_id(0), _v)


def t091_s3(out, ins):
    grid = (268435456,)
    t091_s3_kernel[grid](out, ins[0], ins[1], ins[2])
    return out


def t091(out, ins):
    _t1 = torch.empty(1048576, device=ins[0].device, dtype=torch.float32)
    _t2 = torch.empty(1048576, device=ins[0].device, dtype=torch.float32)
    t091_s1(_t1, ins)
    t091_s2(_t2, list(ins) + [_t1])
    t091_s3(out, list(ins) + [_t1, _t2])
    return out
