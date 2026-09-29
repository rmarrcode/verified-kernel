import torch
import triton
import triton.language as tl


@triton.jit
def _mul_combine(a, b):
    return a * b


@triton.jit
def t055_s0_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 32):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 32768) & True), (tl.load(in0_ptr + ((((tl.program_id(0) // 32768) * 32768) + ((_lv0 * 1024) + tl.arange(0, 1024))) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 32768) & True), other=0.0) * tl.load(in1_ptr + ((((tl.program_id(0) % 32768) * 32768) + ((_lv0 * 1024) + tl.arange(0, 1024))) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 32768) & True), other=0.0)), 0.0))
    _v = (tl.sum(_acc0, axis=0) + tl.load(in2_ptr + ((tl.program_id(0) % 32768))))
    tl.store(out_ptr + tl.program_id(0), _v)


def t055_s0(out, ins):
    grid = (4194304,)
    t055_s0_kernel[grid](out, ins[0], ins[1], ins[2])
    return out


@triton.jit
def t055_s1_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr):
    _acc0 = tl.zeros([2], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = tl.maximum(_acc0, tl.load(in3_ptr + ((((tl.program_id(0) // 16384) * 32768) + tl.maximum((((tl.program_id(0) % 16384) * 2) + tl.maximum((tl.maximum(((_lv0 * 2) + tl.arange(0, 2)) - tl.maximum(((_lv0 * 2) + tl.arange(0, 2)) - 1, 0), 0) + tl.maximum(tl.maximum(0 - ((tl.program_id(0) % 16384) * 2), 0) - tl.maximum(((_lv0 * 2) + tl.arange(0, 2)) - tl.maximum(((_lv0 * 2) + tl.arange(0, 2)) - 1, 0), 0), 0)) - tl.maximum((tl.maximum(((_lv0 * 2) + tl.arange(0, 2)) - tl.maximum(((_lv0 * 2) + tl.arange(0, 2)) - 1, 0), 0) + tl.maximum(tl.maximum(0 - ((tl.program_id(0) % 16384) * 2), 0) - tl.maximum(((_lv0 * 2) + tl.arange(0, 2)) - tl.maximum(((_lv0 * 2) + tl.arange(0, 2)) - 1, 0), 0), 0)) - tl.maximum(32767 - ((tl.program_id(0) % 16384) * 2), 0), 0), 0)) - tl.maximum((((tl.program_id(0) % 16384) * 2) + tl.maximum((tl.maximum(((_lv0 * 2) + tl.arange(0, 2)) - tl.maximum(((_lv0 * 2) + tl.arange(0, 2)) - 1, 0), 0) + tl.maximum(tl.maximum(0 - ((tl.program_id(0) % 16384) * 2), 0) - tl.maximum(((_lv0 * 2) + tl.arange(0, 2)) - tl.maximum(((_lv0 * 2) + tl.arange(0, 2)) - 1, 0), 0), 0)) - tl.maximum((tl.maximum(((_lv0 * 2) + tl.arange(0, 2)) - tl.maximum(((_lv0 * 2) + tl.arange(0, 2)) - 1, 0), 0) + tl.maximum(tl.maximum(0 - ((tl.program_id(0) % 16384) * 2), 0) - tl.maximum(((_lv0 * 2) + tl.arange(0, 2)) - tl.maximum(((_lv0 * 2) + tl.arange(0, 2)) - 1, 0), 0), 0)) - tl.maximum(32767 - ((tl.program_id(0) % 16384) * 2), 0), 0), 0)) - 32767, 0), 0)))))
    _v = tl.max(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t055_s1(out, ins):
    grid = (2097152,)
    t055_s1_kernel[grid](out, ins[0], ins[1], ins[2], ins[3])
    return out


@triton.jit
def t055_s2_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 16):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 16384) & True), tl.load(in4_ptr + (((tl.program_id(0) * 16384) + ((_lv0 * 1024) + tl.arange(0, 1024))) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 16384) & True), other=0.0), 0.0))
    _v = (tl.sum(_acc0, axis=0) * (1.0 * (1.0 / 2.0)))
    tl.store(out_ptr + tl.program_id(0), _v)


def t055_s2(out, ins):
    grid = (128,)
    t055_s2_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4])
    return out


def t055(out, ins):
    _t0 = torch.empty(4194304, device=ins[0].device, dtype=torch.float32)
    _t1 = torch.empty(2097152, device=ins[0].device, dtype=torch.float32)
    t055_s0(_t0, list(ins))
    t055_s1(_t1, list(ins) + [_t0])
    t055_s2(out, list(ins) + [_t0, _t1])
    return out
