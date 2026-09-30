import torch
import triton
import triton.language as tl


@triton.jit
def _mul_combine(a, b):
    return a * b


@triton.jit
def t050_s0_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr):
    _acc0 = tl.zeros([64], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 64) + tl.arange(0, 64)) < 81) & (((((((((((((_lv0 * 64) + tl.arange(0, 64)) // 9) % 3) <= (((tl.program_id(0) // 3969) % 31) + 1)) & ((tl.maximum((((tl.program_id(0) // 3969) % 31) + 1) - ((((_lv0 * 64) + tl.arange(0, 64)) // 9) % 3), 0) % 2) == 0)) & ((tl.maximum((((tl.program_id(0) // 3969) % 31) + 1) - ((((_lv0 * 64) + tl.arange(0, 64)) // 9) % 3), 0) // 2) < 16)) & (((((_lv0 * 64) + tl.arange(0, 64)) // 3) % 3) <= (((tl.program_id(0) // 63) % 63) + 1))) & ((tl.maximum((((tl.program_id(0) // 63) % 63) + 1) - ((((_lv0 * 64) + tl.arange(0, 64)) // 3) % 3), 0) % 2) == 0)) & ((tl.maximum((((tl.program_id(0) // 63) % 63) + 1) - ((((_lv0 * 64) + tl.arange(0, 64)) // 3) % 3), 0) // 2) < 32)) & ((((_lv0 * 64) + tl.arange(0, 64)) % 3) <= ((tl.program_id(0) % 63) + 1))) & ((tl.maximum(((tl.program_id(0) % 63) + 1) - (((_lv0 * 64) + tl.arange(0, 64)) % 3), 0) % 2) == 0)) & ((tl.maximum(((tl.program_id(0) % 63) + 1) - (((_lv0 * 64) + tl.arange(0, 64)) % 3), 0) // 2) < 32))), (tl.load(in0_ptr + ((((((((((tl.program_id(0) // 1968624) * 3) + (((((tl.program_id(0) // 123039) % 16) // 16) * 3) + (((_lv0 * 64) + tl.arange(0, 64)) // 27))) * 16) + (tl.maximum((((tl.program_id(0) // 3969) % 31) + 1) - ((((_lv0 * 64) + tl.arange(0, 64)) // 9) % 3), 0) // 2)) * 32) + (tl.maximum((((tl.program_id(0) // 63) % 63) + 1) - ((((_lv0 * 64) + tl.arange(0, 64)) // 3) % 3), 0) // 2)) * 32) + (tl.maximum(((tl.program_id(0) % 63) + 1) - (((_lv0 * 64) + tl.arange(0, 64)) % 3), 0) // 2)) + 0 * tl.arange(0, 64)), mask=((((_lv0 * 64) + tl.arange(0, 64)) < 81) & (((((((((((((_lv0 * 64) + tl.arange(0, 64)) // 9) % 3) <= (((tl.program_id(0) // 3969) % 31) + 1)) & ((tl.maximum((((tl.program_id(0) // 3969) % 31) + 1) - ((((_lv0 * 64) + tl.arange(0, 64)) // 9) % 3), 0) % 2) == 0)) & ((tl.maximum((((tl.program_id(0) // 3969) % 31) + 1) - ((((_lv0 * 64) + tl.arange(0, 64)) // 9) % 3), 0) // 2) < 16)) & (((((_lv0 * 64) + tl.arange(0, 64)) // 3) % 3) <= (((tl.program_id(0) // 63) % 63) + 1))) & ((tl.maximum((((tl.program_id(0) // 63) % 63) + 1) - ((((_lv0 * 64) + tl.arange(0, 64)) // 3) % 3), 0) % 2) == 0)) & ((tl.maximum((((tl.program_id(0) // 63) % 63) + 1) - ((((_lv0 * 64) + tl.arange(0, 64)) // 3) % 3), 0) // 2) < 32)) & ((((_lv0 * 64) + tl.arange(0, 64)) % 3) <= ((tl.program_id(0) % 63) + 1))) & ((tl.maximum(((tl.program_id(0) % 63) + 1) - (((_lv0 * 64) + tl.arange(0, 64)) % 3), 0) % 2) == 0)) & ((tl.maximum(((tl.program_id(0) % 63) + 1) - (((_lv0 * 64) + tl.arange(0, 64)) % 3), 0) // 2) < 32))), other=0.0) * tl.load(in1_ptr + ((((((((((((((tl.program_id(0) // 123039) % 16) // 16) * 3) + (((_lv0 * 64) + tl.arange(0, 64)) // 27)) * 16) + (((tl.program_id(0) // 123039) % 16) % 16)) * 3) + ((((_lv0 * 64) + tl.arange(0, 64)) // 9) % 3)) * 3) + ((((_lv0 * 64) + tl.arange(0, 64)) // 3) % 3)) * 3) + (((_lv0 * 64) + tl.arange(0, 64)) % 3)) + 0 * tl.arange(0, 64)), mask=((((_lv0 * 64) + tl.arange(0, 64)) < 81) & (((((((((((((_lv0 * 64) + tl.arange(0, 64)) // 9) % 3) <= (((tl.program_id(0) // 3969) % 31) + 1)) & ((tl.maximum((((tl.program_id(0) // 3969) % 31) + 1) - ((((_lv0 * 64) + tl.arange(0, 64)) // 9) % 3), 0) % 2) == 0)) & ((tl.maximum((((tl.program_id(0) // 3969) % 31) + 1) - ((((_lv0 * 64) + tl.arange(0, 64)) // 9) % 3), 0) // 2) < 16)) & (((((_lv0 * 64) + tl.arange(0, 64)) // 3) % 3) <= (((tl.program_id(0) // 63) % 63) + 1))) & ((tl.maximum((((tl.program_id(0) // 63) % 63) + 1) - ((((_lv0 * 64) + tl.arange(0, 64)) // 3) % 3), 0) % 2) == 0)) & ((tl.maximum((((tl.program_id(0) // 63) % 63) + 1) - ((((_lv0 * 64) + tl.arange(0, 64)) // 3) % 3), 0) // 2) < 32)) & ((((_lv0 * 64) + tl.arange(0, 64)) % 3) <= ((tl.program_id(0) % 63) + 1))) & ((tl.maximum(((tl.program_id(0) % 63) + 1) - (((_lv0 * 64) + tl.arange(0, 64)) % 3), 0) % 2) == 0)) & ((tl.maximum(((tl.program_id(0) % 63) + 1) - (((_lv0 * 64) + tl.arange(0, 64)) % 3), 0) // 2) < 32))), other=0.0)), 0.0))
    _v = (tl.sum(_acc0, axis=0) + tl.load(in2_ptr + (((tl.program_id(0) // 123039) % 16))))
    tl.store(out_ptr + tl.program_id(0), _v)


def t050_s0(out, ins):
    grid = (251983872,)
    t050_s0_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5])
    return out


@triton.jit
def t050_s1_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr):
    _acc0 = tl.zeros([1], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), (tl.load(in6_ptr + ((((((((((tl.program_id(0) // 1968624) * 16) + ((tl.program_id(0) // 123039) % 16)) * 31) + ((tl.program_id(0) // 3969) % 31)) * 63) + ((tl.program_id(0) // 63) % 63)) * 63) + (tl.program_id(0) % 63)) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) * tl.load(in3_ptr + (0 + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t050_s1(out, ins):
    grid = (251983872,)
    t050_s1_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6])
    return out


@triton.jit
def t050_s2_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr):
    _acc0 = tl.zeros([8], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 8) + tl.arange(0, 8)) < 8) & ((((((0 <= ((((tl.program_id(0) // 961) % 15) * 2) + (((_lv0 * 8) + tl.arange(0, 8)) // 4))) & (((((tl.program_id(0) // 961) % 15) * 2) + (((_lv0 * 8) + tl.arange(0, 8)) // 4)) < 31)) & (0 <= ((((tl.program_id(0) // 31) % 31) * 2) + ((((_lv0 * 8) + tl.arange(0, 8)) // 2) % 2)))) & (((((tl.program_id(0) // 31) % 31) * 2) + ((((_lv0 * 8) + tl.arange(0, 8)) // 2) % 2)) < 63)) & (0 <= (((tl.program_id(0) % 31) * 2) + (((_lv0 * 8) + tl.arange(0, 8)) % 2)))) & ((((tl.program_id(0) % 31) * 2) + (((_lv0 * 8) + tl.arange(0, 8)) % 2)) < 63))), tl.load(in7_ptr + (tl.maximum((((((((((tl.program_id(0) // 230640) * 16) + ((tl.program_id(0) // 14415) % 16)) * 31) + ((((tl.program_id(0) // 961) % 15) * 2) + (((_lv0 * 8) + tl.arange(0, 8)) // 4))) * 63) + ((((tl.program_id(0) // 31) % 31) * 2) + ((((_lv0 * 8) + tl.arange(0, 8)) // 2) % 2))) * 63) + (((tl.program_id(0) % 31) * 2) + (((_lv0 * 8) + tl.arange(0, 8)) % 2))) - tl.maximum((((((((((tl.program_id(0) // 230640) * 16) + ((tl.program_id(0) // 14415) % 16)) * 31) + ((((tl.program_id(0) // 961) % 15) * 2) + (((_lv0 * 8) + tl.arange(0, 8)) // 4))) * 63) + ((((tl.program_id(0) // 31) % 31) * 2) + ((((_lv0 * 8) + tl.arange(0, 8)) // 2) % 2))) * 63) + (((tl.program_id(0) % 31) * 2) + (((_lv0 * 8) + tl.arange(0, 8)) % 2))) - 251983871, 0), 0) + 0 * tl.arange(0, 8)), mask=((((_lv0 * 8) + tl.arange(0, 8)) < 8) & ((((((0 <= ((((tl.program_id(0) // 961) % 15) * 2) + (((_lv0 * 8) + tl.arange(0, 8)) // 4))) & (((((tl.program_id(0) // 961) % 15) * 2) + (((_lv0 * 8) + tl.arange(0, 8)) // 4)) < 31)) & (0 <= ((((tl.program_id(0) // 31) % 31) * 2) + ((((_lv0 * 8) + tl.arange(0, 8)) // 2) % 2)))) & (((((tl.program_id(0) // 31) % 31) * 2) + ((((_lv0 * 8) + tl.arange(0, 8)) // 2) % 2)) < 63)) & (0 <= (((tl.program_id(0) % 31) * 2) + (((_lv0 * 8) + tl.arange(0, 8)) % 2)))) & ((((tl.program_id(0) % 31) * 2) + (((_lv0 * 8) + tl.arange(0, 8)) % 2)) < 63))), other=0.0), 0.0))
    _v = (tl.sum(_acc0, axis=0) * (1.0 * (1.0 / 8.0)))
    tl.store(out_ptr + tl.program_id(0), _v)


def t050_s2(out, ins):
    grid = (29521920,)
    t050_s2_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7])
    return out


@triton.jit
def t050_s3_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr):
    _acc0 = tl.zeros([1], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), (tl.load(in8_ptr + ((((((((((tl.program_id(0) // 230640) * 16) + ((tl.program_id(0) // 14415) % 16)) * 15) + ((tl.program_id(0) // 961) % 15)) * 31) + ((tl.program_id(0) // 31) % 31)) * 31) + (tl.program_id(0) % 31)) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) + tl.load(in4_ptr + (((tl.program_id(0) // 14415) % 16) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t050_s3(out, ins):
    grid = (29521920,)
    t050_s3_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8])
    return out


@triton.jit
def t050_s4_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr):
    _acc0 = tl.zeros([1], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), (tl.load(in9_ptr + ((((((((((tl.program_id(0) // 230640) * 16) + ((tl.program_id(0) // 14415) % 16)) * 15) + ((tl.program_id(0) // 961) % 15)) * 31) + ((tl.program_id(0) // 31) % 31)) * 31) + (tl.program_id(0) % 31)) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) * tl.load(in5_ptr + (0 + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t050_s4(out, ins):
    grid = (29521920,)
    t050_s4_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9])
    return out


def t050(out, ins):
    _t0 = torch.empty(251983872, device=ins[0].device, dtype=torch.float32)
    _t1 = torch.empty(251983872, device=ins[0].device, dtype=torch.float32)
    _t2 = torch.empty(29521920, device=ins[0].device, dtype=torch.float32)
    _t3 = torch.empty(29521920, device=ins[0].device, dtype=torch.float32)
    t050_s0(_t0, list(ins))
    t050_s1(_t1, list(ins) + [_t0])
    t050_s2(_t2, list(ins) + [_t0, _t1])
    t050_s3(_t3, list(ins) + [_t0, _t1, _t2])
    t050_s4(out, list(ins) + [_t0, _t1, _t2, _t3])
    return out
