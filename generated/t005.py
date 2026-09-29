import torch
import triton
import triton.language as tl


@triton.jit
def _mul_combine(a, b):
    return a * b


@triton.jit
def t005_s0_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 1024) & ((((((((((_lv0 * 1024) + tl.arange(0, 1024)) // 4) % 4) <= (((tl.program_id(0) // 513) % 513) + 1)) & ((tl.maximum((((tl.program_id(0) // 513) % 513) + 1) - ((((_lv0 * 1024) + tl.arange(0, 1024)) // 4) % 4), 0) % 2) == 0)) & ((tl.maximum((((tl.program_id(0) // 513) % 513) + 1) - ((((_lv0 * 1024) + tl.arange(0, 1024)) // 4) % 4), 0) // 2) < 256)) & ((((_lv0 * 1024) + tl.arange(0, 1024)) % 4) <= ((tl.program_id(0) % 513) + 1))) & ((tl.maximum(((tl.program_id(0) % 513) + 1) - (((_lv0 * 1024) + tl.arange(0, 1024)) % 4), 0) % 2) == 0)) & ((tl.maximum(((tl.program_id(0) % 513) + 1) - (((_lv0 * 1024) + tl.arange(0, 1024)) % 4), 0) // 2) < 256))), (tl.load(in0_ptr + ((((((((tl.program_id(0) // 16842816) * 64) + (((((tl.program_id(0) // 263169) % 64) // 64) * 64) + (((_lv0 * 1024) + tl.arange(0, 1024)) // 16))) * 256) + (tl.maximum((((tl.program_id(0) // 513) % 513) + 1) - ((((_lv0 * 1024) + tl.arange(0, 1024)) // 4) % 4), 0) // 2)) * 256) + (tl.maximum(((tl.program_id(0) % 513) + 1) - (((_lv0 * 1024) + tl.arange(0, 1024)) % 4), 0) // 2)) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 1024) & ((((((((((_lv0 * 1024) + tl.arange(0, 1024)) // 4) % 4) <= (((tl.program_id(0) // 513) % 513) + 1)) & ((tl.maximum((((tl.program_id(0) // 513) % 513) + 1) - ((((_lv0 * 1024) + tl.arange(0, 1024)) // 4) % 4), 0) % 2) == 0)) & ((tl.maximum((((tl.program_id(0) // 513) % 513) + 1) - ((((_lv0 * 1024) + tl.arange(0, 1024)) // 4) % 4), 0) // 2) < 256)) & ((((_lv0 * 1024) + tl.arange(0, 1024)) % 4) <= ((tl.program_id(0) % 513) + 1))) & ((tl.maximum(((tl.program_id(0) % 513) + 1) - (((_lv0 * 1024) + tl.arange(0, 1024)) % 4), 0) % 2) == 0)) & ((tl.maximum(((tl.program_id(0) % 513) + 1) - (((_lv0 * 1024) + tl.arange(0, 1024)) % 4), 0) // 2) < 256))), other=0.0) * tl.load(in1_ptr + ((((((((((((tl.program_id(0) // 263169) % 64) // 64) * 64) + (((_lv0 * 1024) + tl.arange(0, 1024)) // 16)) * 64) + (((tl.program_id(0) // 263169) % 64) % 64)) * 4) + ((((_lv0 * 1024) + tl.arange(0, 1024)) // 4) % 4)) * 4) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 4)) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 1024) & ((((((((((_lv0 * 1024) + tl.arange(0, 1024)) // 4) % 4) <= (((tl.program_id(0) // 513) % 513) + 1)) & ((tl.maximum((((tl.program_id(0) // 513) % 513) + 1) - ((((_lv0 * 1024) + tl.arange(0, 1024)) // 4) % 4), 0) % 2) == 0)) & ((tl.maximum((((tl.program_id(0) // 513) % 513) + 1) - ((((_lv0 * 1024) + tl.arange(0, 1024)) // 4) % 4), 0) // 2) < 256)) & ((((_lv0 * 1024) + tl.arange(0, 1024)) % 4) <= ((tl.program_id(0) % 513) + 1))) & ((tl.maximum(((tl.program_id(0) % 513) + 1) - (((_lv0 * 1024) + tl.arange(0, 1024)) % 4), 0) % 2) == 0)) & ((tl.maximum(((tl.program_id(0) % 513) + 1) - (((_lv0 * 1024) + tl.arange(0, 1024)) % 4), 0) // 2) < 256))), other=0.0)), 0.0))
    _v = (tl.sum(_acc0, axis=0) + tl.load(in2_ptr + (((tl.program_id(0) // 263169) % 64))))
    tl.store(out_ptr + tl.program_id(0), _v)


def t005_s0(out, ins):
    grid = (269485056,)
    t005_s0_kernel[grid](out, ins[0], ins[1], ins[2], ins[3])
    return out


@triton.jit
def t005_s1_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr):
    _acc0 = tl.zeros([1], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), (tl.load(in4_ptr + ((((((((tl.program_id(0) // 16842816) * 64) + ((tl.program_id(0) // 263169) % 64)) * 513) + ((tl.program_id(0) // 513) % 513)) * 513) + (tl.program_id(0) % 513)) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) - tl.load(in3_ptr + (((tl.program_id(0) // 263169) % 64) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)), 0.0))
    _v = (2.0 * tl.sigmoid(2.0 * (tl.sum(_acc0, axis=0))) - 1.0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t005_s1(out, ins):
    grid = (269485056,)
    t005_s1_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4])
    return out


def t005(out, ins):
    _t0 = torch.empty(269485056, device=ins[0].device, dtype=torch.float32)
    t005_s0(_t0, list(ins))
    t005_s1(out, list(ins) + [_t0])
    return out
