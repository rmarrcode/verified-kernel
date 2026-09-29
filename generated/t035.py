import torch
import triton
import triton.language as tl


@triton.jit
def t035_s1_kernel(out_ptr, in0_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2048):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 2097152) & True), tl.load(in0_ptr + (((((((tl.program_id(0) // 8) * 64) + ((tl.program_id(0) % 8) * 8)) + (((_lv0 * 1024) + tl.arange(0, 1024)) // 262144)) * 262144) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 262144)) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 2097152) & True), other=0.0), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t035_s1(out, ins):
    grid = (112,)
    t035_s1_kernel[grid](out, ins[0])
    return out


@triton.jit
def t035_s2_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2048):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 2097152) & True), ((tl.load(in0_ptr + (((((((tl.program_id(0) // 8) * 64) + ((tl.program_id(0) % 8) * 8)) + (((_lv0 * 1024) + tl.arange(0, 1024)) // 262144)) * 262144) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 262144)) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 2097152) & True), other=0.0) - (tl.load(in3_ptr + (tl.program_id(0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 2097152) & True), other=0.0) * (1.0 * (1.0 / 2097152.0)))) * (tl.load(in0_ptr + (((((((tl.program_id(0) // 8) * 64) + ((tl.program_id(0) % 8) * 8)) + (((_lv0 * 1024) + tl.arange(0, 1024)) // 262144)) * 262144) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 262144)) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 2097152) & True), other=0.0) - (tl.load(in3_ptr + (tl.program_id(0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 2097152) & True), other=0.0) * (1.0 * (1.0 / 2097152.0))))), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t035_s2(out, ins):
    grid = (112,)
    t035_s2_kernel[grid](out, ins[0], ins[1], ins[2], ins[3])
    return out


@triton.jit
def t035_s3_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr):
    _acc0 = tl.zeros([1], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), ((((tl.load(in0_ptr + (tl.program_id(0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) - (tl.load(in3_ptr + ((((tl.program_id(0) // 16777216) * 8) + (((tl.program_id(0) // 262144) % 64) // 8)) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) * (1.0 * (1.0 / 2097152.0)))) * (1.0 / tl.sqrt(((tl.load(in4_ptr + ((((tl.program_id(0) // 16777216) * 8) + (((tl.program_id(0) // 262144) % 64) // 8)) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) * (1.0 * (1.0 / 2097152.0))) + (1.0 * (1.0 / 100000.0)))))) * tl.load(in1_ptr + (((tl.program_id(0) // 262144) % 64) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)) + tl.load(in2_ptr + (((tl.program_id(0) // 262144) % 64) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t035_s3(out, ins):
    grid = (234881024,)
    t035_s3_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4])
    return out


def t035(out, ins):
    _t1 = torch.empty(112, device=ins[0].device, dtype=torch.float32)
    _t2 = torch.empty(112, device=ins[0].device, dtype=torch.float32)
    t035_s1(_t1, ins)
    t035_s2(_t2, list(ins) + [_t1])
    t035_s3(out, list(ins) + [_t1, _t2])
    return out
