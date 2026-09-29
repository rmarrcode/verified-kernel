import torch
import triton
import triton.language as tl


@triton.jit
def _mul_combine(a, b):
    return a * b


@triton.jit
def t041_s0_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 4):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 4096) & True), (tl.load(in0_ptr + ((((tl.program_id(0) // 4096) * 4096) + ((_lv0 * 1024) + tl.arange(0, 1024))) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 4096) & True), other=0.0) * tl.load(in1_ptr + ((((tl.program_id(0) % 4096) * 4096) + ((_lv0 * 1024) + tl.arange(0, 1024))) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 4096) & True), other=0.0)), 0.0))
    _v = (tl.sum(_acc0, axis=0) + tl.load(in2_ptr + ((tl.program_id(0) % 4096))))
    tl.store(out_ptr + tl.program_id(0), _v)


def t041_s0(out, ins):
    grid = (67108864,)
    t041_s0_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4])
    return out


@triton.jit
def t041_s1_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 16):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 16384) & True), tl.load(in5_ptr + (((((_lv0 * 1024) + tl.arange(0, 1024)) * 4096) + tl.program_id(0)) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 16384) & True), other=0.0), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t041_s1(out, ins):
    grid = (4096,)
    t041_s1_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5])
    return out


@triton.jit
def t041_s2_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 16):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 16384) & True), ((tl.load(in5_ptr + (((((_lv0 * 1024) + tl.arange(0, 1024)) * 4096) + tl.program_id(0)) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 16384) & True), other=0.0) - (tl.load(in6_ptr + (tl.program_id(0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 16384) & True), other=0.0) * (1.0 * (1.0 / 16384.0)))) * (tl.load(in5_ptr + (((((_lv0 * 1024) + tl.arange(0, 1024)) * 4096) + tl.program_id(0)) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 16384) & True), other=0.0) - (tl.load(in6_ptr + (tl.program_id(0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 16384) & True), other=0.0) * (1.0 * (1.0 / 16384.0))))), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t041_s2(out, ins):
    grid = (4096,)
    t041_s2_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6])
    return out


@triton.jit
def t041_s3_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr):
    _acc0 = tl.zeros([1], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), ((((tl.load(in5_ptr + (tl.program_id(0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) - (tl.load(in6_ptr + (tl.maximum((tl.program_id(0) % 4096) - tl.maximum((tl.program_id(0) % 4096) - 4095, 0), 0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) * (1.0 * (1.0 / 16384.0)))) * (1.0 / tl.sqrt(((tl.load(in7_ptr + (tl.maximum((tl.program_id(0) % 4096) - tl.maximum((tl.program_id(0) % 4096) - 4095, 0), 0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) * (1.0 * (1.0 / 16384.0))) + (1.0 * (1.0 / 100000.0)))))) * tl.load(in3_ptr + ((tl.program_id(0) % 4096) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)) + tl.load(in4_ptr + ((tl.program_id(0) % 4096) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)), 0.0))
    _v = tl.maximum((((1.0 * (1.0 / 2.0)) * tl.sum(_acc0, axis=0)) * ((1.0 * (1.0 / 1.0)) + tl.erf((tl.sum(_acc0, axis=0) * (1.0 / tl.sqrt((2.0 * (1.0 / 1.0)))))))), (0.0 * (1.0 / 1.0)))
    tl.store(out_ptr + tl.program_id(0), _v)


def t041_s3(out, ins):
    grid = (67108864,)
    t041_s3_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7])
    return out


def t041(out, ins):
    _t0 = torch.empty(67108864, device=ins[0].device, dtype=torch.float32)
    _t1 = torch.empty(4096, device=ins[0].device, dtype=torch.float32)
    _t2 = torch.empty(4096, device=ins[0].device, dtype=torch.float32)
    t041_s0(_t0, list(ins))
    t041_s1(_t1, list(ins) + [_t0])
    t041_s2(_t2, list(ins) + [_t0, _t1])
    t041_s3(out, list(ins) + [_t0, _t1, _t2])
    return out
