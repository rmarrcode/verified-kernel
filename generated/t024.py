import torch
import triton
import triton.language as tl


@triton.jit
def _mul_combine(a, b):
    return a * b


@triton.jit
def t024_s0_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr):
    _acc0 = tl.zeros([64], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 64) + tl.arange(0, 64)) < 81) & ((((((tl.program_id(0) // 900) % 22) + ((((_lv0 * 64) + tl.arange(0, 64)) // 9) % 3)) < 24) & ((((tl.program_id(0) // 30) % 30) + ((((_lv0 * 64) + tl.arange(0, 64)) // 3) % 3)) < 32)) & (((tl.program_id(0) % 30) + (((_lv0 * 64) + tl.arange(0, 64)) % 3)) < 32))), (tl.load(in0_ptr + ((((((((((tl.program_id(0) // 475200) * 3) + (((_lv0 * 64) + tl.arange(0, 64)) // 27)) * 24) + (((tl.program_id(0) // 900) % 22) + ((((_lv0 * 64) + tl.arange(0, 64)) // 9) % 3))) * 32) + (((tl.program_id(0) // 30) % 30) + ((((_lv0 * 64) + tl.arange(0, 64)) // 3) % 3))) * 32) + ((tl.program_id(0) % 30) + (((_lv0 * 64) + tl.arange(0, 64)) % 3))) + 0 * tl.arange(0, 64)), mask=((((_lv0 * 64) + tl.arange(0, 64)) < 81) & ((((((tl.program_id(0) // 900) % 22) + ((((_lv0 * 64) + tl.arange(0, 64)) // 9) % 3)) < 24) & ((((tl.program_id(0) // 30) % 30) + ((((_lv0 * 64) + tl.arange(0, 64)) // 3) % 3)) < 32)) & (((tl.program_id(0) % 30) + (((_lv0 * 64) + tl.arange(0, 64)) % 3)) < 32))), other=0.0) * tl.load(in1_ptr + (((((((((((tl.program_id(0) // 19800) % 24) * 3) + (((_lv0 * 64) + tl.arange(0, 64)) // 27)) * 3) + ((((_lv0 * 64) + tl.arange(0, 64)) // 9) % 3)) * 3) + ((((_lv0 * 64) + tl.arange(0, 64)) // 3) % 3)) * 3) + (((_lv0 * 64) + tl.arange(0, 64)) % 3)) + 0 * tl.arange(0, 64)), mask=((((_lv0 * 64) + tl.arange(0, 64)) < 81) & ((((((tl.program_id(0) // 900) % 22) + ((((_lv0 * 64) + tl.arange(0, 64)) // 9) % 3)) < 24) & ((((tl.program_id(0) // 30) % 30) + ((((_lv0 * 64) + tl.arange(0, 64)) // 3) % 3)) < 32)) & (((tl.program_id(0) % 30) + (((_lv0 * 64) + tl.arange(0, 64)) % 3)) < 32))), other=0.0)), 0.0))
    _v = (tl.sum(_acc0, axis=0) + tl.load(in2_ptr + (((tl.program_id(0) // 19800) % 24))))
    tl.store(out_ptr + tl.program_id(0), _v)


def t024_s0(out, ins):
    grid = (60825600,)
    t024_s0_kernel[grid](out, ins[0], ins[1], ins[2])
    return out


@triton.jit
def t024_s1_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr):
    _acc0 = tl.zeros([16], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = tl.maximum(_acc0, ((0.0 * (1.0 / 1.0)) - tl.load(in3_ptr + ((((((tl.program_id(0) // 900) * 22) + tl.maximum(((_lv0 * 16) + tl.arange(0, 16)) - tl.maximum(((_lv0 * 16) + tl.arange(0, 16)) - 21, 0), 0)) * 900) + (tl.program_id(0) % 900))))))
    _v = ((0.0 * (1.0 / 1.0)) - tl.max(_acc0, axis=0))
    tl.store(out_ptr + tl.program_id(0), _v)


def t024_s1(out, ins):
    grid = (2764800,)
    t024_s1_kernel[grid](out, ins[0], ins[1], ins[2], ins[3])
    return out


@triton.jit
def t024_s2_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr):
    _acc0 = tl.zeros([16], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 16) + tl.arange(0, 16)) < 24) & True), tl.exp(tl.load(in4_ptr + ((((((tl.program_id(0) // 900) * 24) + ((_lv0 * 16) + tl.arange(0, 16))) * 900) + (tl.program_id(0) % 900)) + 0 * tl.arange(0, 16)), mask=((((_lv0 * 16) + tl.arange(0, 16)) < 24) & True), other=0.0)), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t024_s2(out, ins):
    grid = (115200,)
    t024_s2_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4])
    return out


@triton.jit
def t024_s3_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr):
    _acc0 = tl.zeros([1], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), (tl.exp(tl.load(in4_ptr + (tl.program_id(0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)) * (1.0 / tl.load(in5_ptr + (tl.maximum((((tl.program_id(0) // (24 * 900)) * 900) + (tl.program_id(0) % 900)) - tl.maximum((((tl.program_id(0) // (24 * 900)) * 900) + (tl.program_id(0) % 900)) - 115199, 0), 0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0))), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t024_s3(out, ins):
    grid = (2764800,)
    t024_s3_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5])
    return out


def t024(out, ins):
    _t0 = torch.empty(60825600, device=ins[0].device, dtype=torch.float32)
    _t1 = torch.empty(2764800, device=ins[0].device, dtype=torch.float32)
    _t2 = torch.empty(115200, device=ins[0].device, dtype=torch.float32)
    t024_s0(_t0, list(ins))
    t024_s1(_t1, list(ins) + [_t0])
    t024_s2(_t2, list(ins) + [_t0, _t1])
    t024_s3(out, list(ins) + [_t0, _t1, _t2])
    return out
