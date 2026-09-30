import torch
import triton
import triton.language as tl


@triton.jit
def _mul_combine(a, b):
    return a * b


@triton.jit
def t048_s0_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr):
    _acc0 = tl.zeros([64], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 64) + tl.arange(0, 64)) < 81) & ((((((tl.program_id(0) // 3844) % 14) + ((((_lv0 * 64) + tl.arange(0, 64)) // 9) % 3)) < 16) & ((((tl.program_id(0) // 62) % 62) + ((((_lv0 * 64) + tl.arange(0, 64)) // 3) % 3)) < 64)) & (((tl.program_id(0) % 62) + (((_lv0 * 64) + tl.arange(0, 64)) % 3)) < 64))), (tl.load(in0_ptr + ((((((((((tl.program_id(0) // 861056) * 3) + (((_lv0 * 64) + tl.arange(0, 64)) // 27)) * 16) + (((tl.program_id(0) // 3844) % 14) + ((((_lv0 * 64) + tl.arange(0, 64)) // 9) % 3))) * 64) + (((tl.program_id(0) // 62) % 62) + ((((_lv0 * 64) + tl.arange(0, 64)) // 3) % 3))) * 64) + ((tl.program_id(0) % 62) + (((_lv0 * 64) + tl.arange(0, 64)) % 3))) + 0 * tl.arange(0, 64)), mask=((((_lv0 * 64) + tl.arange(0, 64)) < 81) & ((((((tl.program_id(0) // 3844) % 14) + ((((_lv0 * 64) + tl.arange(0, 64)) // 9) % 3)) < 16) & ((((tl.program_id(0) // 62) % 62) + ((((_lv0 * 64) + tl.arange(0, 64)) // 3) % 3)) < 64)) & (((tl.program_id(0) % 62) + (((_lv0 * 64) + tl.arange(0, 64)) % 3)) < 64))), other=0.0) * tl.load(in1_ptr + (((((((((((tl.program_id(0) // 53816) % 16) * 3) + (((_lv0 * 64) + tl.arange(0, 64)) // 27)) * 3) + ((((_lv0 * 64) + tl.arange(0, 64)) // 9) % 3)) * 3) + ((((_lv0 * 64) + tl.arange(0, 64)) // 3) % 3)) * 3) + (((_lv0 * 64) + tl.arange(0, 64)) % 3)) + 0 * tl.arange(0, 64)), mask=((((_lv0 * 64) + tl.arange(0, 64)) < 81) & ((((((tl.program_id(0) // 3844) % 14) + ((((_lv0 * 64) + tl.arange(0, 64)) // 9) % 3)) < 16) & ((((tl.program_id(0) // 62) % 62) + ((((_lv0 * 64) + tl.arange(0, 64)) // 3) % 3)) < 64)) & (((tl.program_id(0) % 62) + (((_lv0 * 64) + tl.arange(0, 64)) % 3)) < 64))), other=0.0)), 0.0))
    _v = (tl.sum(_acc0, axis=0) + tl.load(in2_ptr + (((tl.program_id(0) // 53816) % 16))))
    tl.store(out_ptr + tl.program_id(0), _v)


def t048_s0(out, ins):
    grid = (110215168,)
    t048_s0_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4])
    return out


@triton.jit
def t048_s1_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr):
    _acc0 = tl.zeros([1], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), (tl.load(in5_ptr + ((((((((((tl.program_id(0) // 861056) * 16) + ((tl.program_id(0) // 53816) % 16)) * 14) + ((tl.program_id(0) // 3844) % 14)) * 62) + ((tl.program_id(0) // 62) % 62)) * 62) + (tl.program_id(0) % 62)) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) * tl.load(in3_ptr + (((tl.program_id(0) // 53816) % 16) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)), 0.0))
    _v = (2.0 * tl.sigmoid(2.0 * (tl.sum(_acc0, axis=0))) - 1.0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t048_s1(out, ins):
    grid = (110215168,)
    t048_s1_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5])
    return out


@triton.jit
def t048_s2_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr):
    _acc0 = tl.zeros([1], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), (tl.load(in6_ptr + ((((((((((tl.program_id(0) // 861056) * 16) + ((tl.program_id(0) // 53816) % 16)) * 14) + ((tl.program_id(0) // 3844) % 14)) * 62) + ((tl.program_id(0) // 62) % 62)) * 62) + (tl.program_id(0) % 62)) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) * tl.load(in4_ptr + (((tl.program_id(0) // 53816) % 16) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)), 0.0))
    _v = (1.0 / ((1.0 * (1.0 / 1.0)) + tl.exp(((0.0 * (1.0 / 1.0)) - tl.sum(_acc0, axis=0)))))
    tl.store(out_ptr + tl.program_id(0), _v)


def t048_s2(out, ins):
    grid = (110215168,)
    t048_s2_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6])
    return out


def t048(out, ins):
    _t0 = torch.empty(110215168, device=ins[0].device, dtype=torch.float32)
    _t1 = torch.empty(110215168, device=ins[0].device, dtype=torch.float32)
    t048_s0(_t0, list(ins))
    t048_s1(_t1, list(ins) + [_t0])
    t048_s2(out, list(ins) + [_t0, _t1])
    return out
