import torch
import triton
import triton.language as tl


@triton.jit
def _mul_combine(a, b):
    return a * b


@triton.jit
def slc4_s0_kernel(out_ptr, in0_ptr):
    _acc0 = tl.zeros([1], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), tl.load(in0_ptr + ((((((tl.program_id(0) // 48) * 8) + ((tl.program_id(0) // 12) % 4)) * 12) + (tl.program_id(0) % 12)) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def slc4_s0(out, ins):
    grid = (96,)
    slc4_s0_kernel[grid](out, ins[0])
    return out


@triton.jit
def slc4_s1_kernel(out_ptr, in0_ptr, in1_ptr):
    _acc0 = tl.zeros([1], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), tl.load(in0_ptr + ((((((tl.program_id(0) // 48) * 8) + (((tl.program_id(0) // 12) % 4) + 4)) * 12) + (tl.program_id(0) % 12)) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def slc4_s1(out, ins):
    grid = (96,)
    slc4_s1_kernel[grid](out, ins[0], ins[1])
    return out


@triton.jit
def slc4_s2_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr):
    _acc0 = tl.zeros([2], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 2) + tl.arange(0, 2)) < 2) & ((((((_lv0 * 2) + tl.arange(0, 2)) == 0) & (0 <= ((tl.program_id(0) // 12) % 8))) & (((tl.program_id(0) // 12) % 8) < 4)) | (((((_lv0 * 2) + tl.arange(0, 2)) == 1) & (4 <= ((tl.program_id(0) // 12) % 8))) & (((tl.program_id(0) // 12) % 8) < 8)))), tl.where((((_lv0 * 2) + tl.arange(0, 2))).to(tl.float32) <= (1.0 * (1.0 / 2.0)), tl.load(in2_ptr + ((((((tl.program_id(0) // 96) * 4) + tl.maximum(((tl.program_id(0) // 12) % 8) - tl.maximum(((tl.program_id(0) // 12) % 8) - 3, 0), 0)) * 12) + (tl.program_id(0) % 12)) + 0 * tl.arange(0, 2)), mask=((((_lv0 * 2) + tl.arange(0, 2)) < 2) & ((((((_lv0 * 2) + tl.arange(0, 2)) == 0) & (0 <= ((tl.program_id(0) // 12) % 8))) & (((tl.program_id(0) // 12) % 8) < 4)) | (((((_lv0 * 2) + tl.arange(0, 2)) == 1) & (4 <= ((tl.program_id(0) // 12) % 8))) & (((tl.program_id(0) // 12) % 8) < 8)))), other=0.0), tl.load(in1_ptr + ((((((tl.program_id(0) // 96) * 4) + tl.maximum(tl.maximum(((tl.program_id(0) // 12) % 8) - 4, 0) - tl.maximum(tl.maximum(((tl.program_id(0) // 12) % 8) - 4, 0) - 3, 0), 0)) * 12) + (tl.program_id(0) % 12)) + 0 * tl.arange(0, 2)), mask=((((_lv0 * 2) + tl.arange(0, 2)) < 2) & ((((((_lv0 * 2) + tl.arange(0, 2)) == 0) & (0 <= ((tl.program_id(0) // 12) % 8))) & (((tl.program_id(0) // 12) % 8) < 4)) | (((((_lv0 * 2) + tl.arange(0, 2)) == 1) & (4 <= ((tl.program_id(0) // 12) % 8))) & (((tl.program_id(0) // 12) % 8) < 8)))), other=0.0)), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def slc4_s2(out, ins):
    grid = (192,)
    slc4_s2_kernel[grid](out, ins[0], ins[1], ins[2])
    return out


def slc4(out, ins):
    _t0 = torch.empty(96, device=ins[0].device, dtype=torch.float32)
    _t1 = torch.empty(96, device=ins[0].device, dtype=torch.float32)
    slc4_s0(_t0, list(ins))
    slc4_s1(_t1, list(ins) + [_t0])
    slc4_s2(out, list(ins) + [_t0, _t1])
    return out
