import torch
import triton
import triton.language as tl


@triton.jit
def _mul_combine(a, b):
    return a * b


@triton.jit
def t057_s0_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr):
    _acc0 = tl.zeros([64], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 64) + tl.arange(0, 64)) < 72) & (((((tl.program_id(0) // 126) % 126) + ((((_lv0 * 64) + tl.arange(0, 64)) // 3) % 3)) < 128) & (((tl.program_id(0) % 126) + (((_lv0 * 64) + tl.arange(0, 64)) % 3)) < 128))), (tl.load(in0_ptr + ((((((((tl.program_id(0) // 1016064) * 8) + (((_lv0 * 64) + tl.arange(0, 64)) // 9)) * 128) + (((tl.program_id(0) // 126) % 126) + ((((_lv0 * 64) + tl.arange(0, 64)) // 3) % 3))) * 128) + ((tl.program_id(0) % 126) + (((_lv0 * 64) + tl.arange(0, 64)) % 3))) + 0 * tl.arange(0, 64)), mask=((((_lv0 * 64) + tl.arange(0, 64)) < 72) & (((((tl.program_id(0) // 126) % 126) + ((((_lv0 * 64) + tl.arange(0, 64)) // 3) % 3)) < 128) & (((tl.program_id(0) % 126) + (((_lv0 * 64) + tl.arange(0, 64)) % 3)) < 128))), other=0.0) * tl.load(in1_ptr + (((((((((tl.program_id(0) // 15876) % 64) * 8) + (((_lv0 * 64) + tl.arange(0, 64)) // 9)) * 3) + ((((_lv0 * 64) + tl.arange(0, 64)) // 3) % 3)) * 3) + (((_lv0 * 64) + tl.arange(0, 64)) % 3)) + 0 * tl.arange(0, 64)), mask=((((_lv0 * 64) + tl.arange(0, 64)) < 72) & (((((tl.program_id(0) // 126) % 126) + ((((_lv0 * 64) + tl.arange(0, 64)) // 3) % 3)) < 128) & (((tl.program_id(0) % 126) + (((_lv0 * 64) + tl.arange(0, 64)) % 3)) < 128))), other=0.0)), 0.0))
    _v = tl.maximum((tl.sum(_acc0, axis=0) + tl.load(in2_ptr + (((tl.program_id(0) // 15876) % 64)))), (0.0 * (1.0 / 1.0)))
    tl.store(out_ptr + tl.program_id(0), _v)


def t057_s0(out, ins):
    grid = (130056192,)
    t057_s0_kernel[grid](out, ins[0], ins[1], ins[2])
    return out


@triton.jit
def t057_s1_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr):
    _acc0 = tl.zeros([1], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), (tl.load(in3_ptr + ((((((((tl.program_id(0) // 1016064) * 64) + ((tl.program_id(0) // 15876) % 64)) * 126) + ((tl.program_id(0) // 126) % 126)) * 126) + (tl.program_id(0) % 126)) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) + (3.0 * (1.0 / 1.0))), 0.0))
    _v = tl.minimum(tl.maximum((tl.sum(_acc0, axis=0) / (6.0 * (1.0 / 1.0))), (0.0 * (1.0 / 1.0))), (1.0 * (1.0 / 1.0)))
    tl.store(out_ptr + tl.program_id(0), _v)


def t057_s1(out, ins):
    grid = (130056192,)
    t057_s1_kernel[grid](out, ins[0], ins[1], ins[2], ins[3])
    return out


@triton.jit
def t057_s2_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr):
    _acc0 = tl.zeros([1], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), (tl.load(in3_ptr + ((((((((tl.program_id(0) // 1016064) * 64) + ((tl.program_id(0) // 15876) % 64)) * 126) + ((tl.program_id(0) // 126) % 126)) * 126) + (tl.program_id(0) % 126)) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) * tl.load(in4_ptr + ((((((((tl.program_id(0) // 1016064) * 64) + ((tl.program_id(0) // 15876) % 64)) * 126) + ((tl.program_id(0) // 126) % 126)) * 126) + (tl.program_id(0) % 126)) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t057_s2(out, ins):
    grid = (130056192,)
    t057_s2_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4])
    return out


def t057(out, ins):
    _t0 = torch.empty(130056192, device=ins[0].device, dtype=torch.float32)
    _t1 = torch.empty(130056192, device=ins[0].device, dtype=torch.float32)
    t057_s0(_t0, list(ins))
    t057_s1(_t1, list(ins) + [_t0])
    t057_s2(out, list(ins) + [_t0, _t1])
    return out
