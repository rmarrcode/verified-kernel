import torch
import triton
import triton.language as tl


@triton.jit
def t086_s1_kernel(out_ptr, in0_ptr, in1_ptr):
    _acc0 = tl.zeros([8], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 8) + tl.arange(0, 8)) < 9) & ((((1 <= (((tl.program_id(0) // 512) % 512) + (((_lv0 * 8) + tl.arange(0, 8)) // 3))) & ((((tl.program_id(0) // 512) % 512) + (((_lv0 * 8) + tl.arange(0, 8)) // 3)) < 513)) & (1 <= ((tl.program_id(0) % 512) + (((_lv0 * 8) + tl.arange(0, 8)) % 3)))) & (((tl.program_id(0) % 512) + (((_lv0 * 8) + tl.arange(0, 8)) % 3)) < 513))), (tl.load(in0_ptr + ((((((((tl.program_id(0) // 16777216) * 64) + ((tl.program_id(0) // 262144) % 64)) * 512) + tl.maximum((((tl.program_id(0) // 512) % 512) + (((_lv0 * 8) + tl.arange(0, 8)) // 3)) - 1, 0)) * 512) + tl.maximum(((tl.program_id(0) % 512) + (((_lv0 * 8) + tl.arange(0, 8)) % 3)) - 1, 0)) + 0 * tl.arange(0, 8)), mask=((((_lv0 * 8) + tl.arange(0, 8)) < 9) & ((((1 <= (((tl.program_id(0) // 512) % 512) + (((_lv0 * 8) + tl.arange(0, 8)) // 3))) & ((((tl.program_id(0) // 512) % 512) + (((_lv0 * 8) + tl.arange(0, 8)) // 3)) < 513)) & (1 <= ((tl.program_id(0) % 512) + (((_lv0 * 8) + tl.arange(0, 8)) % 3)))) & (((tl.program_id(0) % 512) + (((_lv0 * 8) + tl.arange(0, 8)) % 3)) < 513))), other=0.0) * tl.load(in1_ptr + (((((((tl.program_id(0) // 262144) % 64) * 3) + (((_lv0 * 8) + tl.arange(0, 8)) // 3)) * 3) + (((_lv0 * 8) + tl.arange(0, 8)) % 3)) + 0 * tl.arange(0, 8)), mask=((((_lv0 * 8) + tl.arange(0, 8)) < 9) & ((((1 <= (((tl.program_id(0) // 512) % 512) + (((_lv0 * 8) + tl.arange(0, 8)) // 3))) & ((((tl.program_id(0) // 512) % 512) + (((_lv0 * 8) + tl.arange(0, 8)) // 3)) < 513)) & (1 <= ((tl.program_id(0) % 512) + (((_lv0 * 8) + tl.arange(0, 8)) % 3)))) & (((tl.program_id(0) % 512) + (((_lv0 * 8) + tl.arange(0, 8)) % 3)) < 513))), other=0.0)), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t086_s1(out, ins):
    grid = (134217728,)
    t086_s1_kernel[grid](out, ins[0], ins[1])
    return out


@triton.jit
def t086_s2_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr):
    _acc0 = tl.zeros([64], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 64) + tl.arange(0, 64)) < 64) & True), (tl.load(in3_ptr + ((((((((tl.program_id(0) // 33554432) * 64) + ((_lv0 * 64) + tl.arange(0, 64))) * 512) + ((tl.program_id(0) // 512) % 512)) * 512) + (tl.program_id(0) % 512)) + 0 * tl.arange(0, 64)), mask=((((_lv0 * 64) + tl.arange(0, 64)) < 64) & True), other=0.0) * tl.load(in2_ptr + (((((tl.program_id(0) // 262144) % 128) * 64) + ((_lv0 * 64) + tl.arange(0, 64))) + 0 * tl.arange(0, 64)), mask=((((_lv0 * 64) + tl.arange(0, 64)) < 64) & True), other=0.0)), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t086_s2(out, ins):
    grid = (268435456,)
    t086_s2_kernel[grid](out, ins[0], ins[1], ins[2], ins[3])
    return out


def t086(out, ins):
    _tmp = torch.empty(134217728, device=ins[0].device, dtype=torch.float32)
    t086_s1(_tmp, ins)
    t086_s2(out, list(ins) + [_tmp])
    return out
