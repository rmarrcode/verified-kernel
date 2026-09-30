import torch
import triton
import triton.language as tl


@triton.jit
def _mul_combine(a, b):
    return a * b


@triton.jit
def t007_s0_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr):
    _acc0 = tl.zeros([128], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 128) + tl.arange(0, 128)) < 216) & ((((((tl.program_id(0) // 3844) % 30) + ((((_lv0 * 128) + tl.arange(0, 128)) // 9) % 3)) < 32) & ((((tl.program_id(0) // 62) % 62) + ((((_lv0 * 128) + tl.arange(0, 128)) // 3) % 3)) < 64)) & (((tl.program_id(0) % 62) + (((_lv0 * 128) + tl.arange(0, 128)) % 3)) < 64))), (tl.load(in0_ptr + ((((((((((tl.program_id(0) // 3690240) * 8) + (((_lv0 * 128) + tl.arange(0, 128)) // 27)) * 32) + (((tl.program_id(0) // 3844) % 30) + ((((_lv0 * 128) + tl.arange(0, 128)) // 9) % 3))) * 64) + (((tl.program_id(0) // 62) % 62) + ((((_lv0 * 128) + tl.arange(0, 128)) // 3) % 3))) * 64) + ((tl.program_id(0) % 62) + (((_lv0 * 128) + tl.arange(0, 128)) % 3))) + 0 * tl.arange(0, 128)), mask=((((_lv0 * 128) + tl.arange(0, 128)) < 216) & ((((((tl.program_id(0) // 3844) % 30) + ((((_lv0 * 128) + tl.arange(0, 128)) // 9) % 3)) < 32) & ((((tl.program_id(0) // 62) % 62) + ((((_lv0 * 128) + tl.arange(0, 128)) // 3) % 3)) < 64)) & (((tl.program_id(0) % 62) + (((_lv0 * 128) + tl.arange(0, 128)) % 3)) < 64))), other=0.0) * tl.load(in1_ptr + (((((((((((tl.program_id(0) // 115320) % 32) * 8) + (((_lv0 * 128) + tl.arange(0, 128)) // 27)) * 3) + ((((_lv0 * 128) + tl.arange(0, 128)) // 9) % 3)) * 3) + ((((_lv0 * 128) + tl.arange(0, 128)) // 3) % 3)) * 3) + (((_lv0 * 128) + tl.arange(0, 128)) % 3)) + 0 * tl.arange(0, 128)), mask=((((_lv0 * 128) + tl.arange(0, 128)) < 216) & ((((((tl.program_id(0) // 3844) % 30) + ((((_lv0 * 128) + tl.arange(0, 128)) // 9) % 3)) < 32) & ((((tl.program_id(0) // 62) % 62) + ((((_lv0 * 128) + tl.arange(0, 128)) // 3) % 3)) < 64)) & (((tl.program_id(0) % 62) + (((_lv0 * 128) + tl.arange(0, 128)) % 3)) < 64))), other=0.0)), 0.0))
    _v = (1.0 / ((1.0 * (1.0 / 1.0)) + tl.exp(((0.0 * (1.0 / 1.0)) - (((1.0 * (1.0 / 2.0)) * tl.where(tl.maximum((tl.sum(_acc0, axis=0) + tl.load(in2_ptr + (((tl.program_id(0) // 115320) % 32)))), (0.0 * (1.0 / 1.0))) <= (0.0 * (1.0 / 1.0)), ((1.0 * (1.0 / 100.0)) * tl.maximum((tl.sum(_acc0, axis=0) + tl.load(in2_ptr + (((tl.program_id(0) // 115320) % 32)))), (0.0 * (1.0 / 1.0)))), tl.maximum((tl.sum(_acc0, axis=0) + tl.load(in2_ptr + (((tl.program_id(0) // 115320) % 32)))), (0.0 * (1.0 / 1.0))))) * ((1.0 * (1.0 / 1.0)) + tl.erf((tl.where(tl.maximum((tl.sum(_acc0, axis=0) + tl.load(in2_ptr + (((tl.program_id(0) // 115320) % 32)))), (0.0 * (1.0 / 1.0))) <= (0.0 * (1.0 / 1.0)), ((1.0 * (1.0 / 100.0)) * tl.maximum((tl.sum(_acc0, axis=0) + tl.load(in2_ptr + (((tl.program_id(0) // 115320) % 32)))), (0.0 * (1.0 / 1.0)))), tl.maximum((tl.sum(_acc0, axis=0) + tl.load(in2_ptr + (((tl.program_id(0) // 115320) % 32)))), (0.0 * (1.0 / 1.0)))) * (1.0 / tl.sqrt((2.0 * (1.0 / 1.0))))))))))))
    tl.store(out_ptr + tl.program_id(0), _v)


def t007_s0(out, ins):
    grid = (236175360,)
    t007_s0_kernel[grid](out, ins[0], ins[1], ins[2], ins[3])
    return out


@triton.jit
def t007_s1_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr):
    _acc0 = tl.zeros([1], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), (tl.load(in4_ptr + ((((((((((tl.program_id(0) // 3690240) * 32) + ((tl.program_id(0) // 115320) % 32)) * 30) + ((tl.program_id(0) // 3844) % 30)) * 62) + ((tl.program_id(0) // 62) % 62)) * 62) + (tl.program_id(0) % 62)) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) + tl.load(in3_ptr + (((tl.program_id(0) // 115320) % 32) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t007_s1(out, ins):
    grid = (236175360,)
    t007_s1_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4])
    return out


def t007(out, ins):
    _t0 = torch.empty(236175360, device=ins[0].device, dtype=torch.float32)
    t007_s0(_t0, list(ins))
    t007_s1(out, list(ins) + [_t0])
    return out
