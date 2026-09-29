import torch
import triton
import triton.language as tl


@triton.jit
def _mul_combine(a, b):
    return a * b


@triton.jit
def t008_s0_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr):
    _acc0 = tl.zeros([128], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 128) + tl.arange(0, 128)) < 216) & ((((((tl.program_id(0) // 3844) % 14) + ((((_lv0 * 128) + tl.arange(0, 128)) // 9) % 3)) < 16) & ((((tl.program_id(0) // 62) % 62) + ((((_lv0 * 128) + tl.arange(0, 128)) // 3) % 3)) < 64)) & (((tl.program_id(0) % 62) + (((_lv0 * 128) + tl.arange(0, 128)) % 3)) < 64))), (tl.load(in0_ptr + ((((((((((tl.program_id(0) // 861056) * 8) + (((_lv0 * 128) + tl.arange(0, 128)) // 27)) * 16) + (((tl.program_id(0) // 3844) % 14) + ((((_lv0 * 128) + tl.arange(0, 128)) // 9) % 3))) * 64) + (((tl.program_id(0) // 62) % 62) + ((((_lv0 * 128) + tl.arange(0, 128)) // 3) % 3))) * 64) + ((tl.program_id(0) % 62) + (((_lv0 * 128) + tl.arange(0, 128)) % 3))) + 0 * tl.arange(0, 128)), mask=((((_lv0 * 128) + tl.arange(0, 128)) < 216) & ((((((tl.program_id(0) // 3844) % 14) + ((((_lv0 * 128) + tl.arange(0, 128)) // 9) % 3)) < 16) & ((((tl.program_id(0) // 62) % 62) + ((((_lv0 * 128) + tl.arange(0, 128)) // 3) % 3)) < 64)) & (((tl.program_id(0) % 62) + (((_lv0 * 128) + tl.arange(0, 128)) % 3)) < 64))), other=0.0) * tl.load(in1_ptr + (((((((((((tl.program_id(0) // 53816) % 16) * 8) + (((_lv0 * 128) + tl.arange(0, 128)) // 27)) * 3) + ((((_lv0 * 128) + tl.arange(0, 128)) // 9) % 3)) * 3) + ((((_lv0 * 128) + tl.arange(0, 128)) // 3) % 3)) * 3) + (((_lv0 * 128) + tl.arange(0, 128)) % 3)) + 0 * tl.arange(0, 128)), mask=((((_lv0 * 128) + tl.arange(0, 128)) < 216) & ((((((tl.program_id(0) // 3844) % 14) + ((((_lv0 * 128) + tl.arange(0, 128)) // 9) % 3)) < 16) & ((((tl.program_id(0) // 62) % 62) + ((((_lv0 * 128) + tl.arange(0, 128)) // 3) % 3)) < 64)) & (((tl.program_id(0) % 62) + (((_lv0 * 128) + tl.arange(0, 128)) % 3)) < 64))), other=0.0)), 0.0))
    _v = ((tl.sum(_acc0, axis=0) + tl.load(in2_ptr + (((tl.program_id(0) // 53816) % 16)))) / (2.0 * (1.0 / 1.0)))
    tl.store(out_ptr + tl.program_id(0), _v)


def t008_s0(out, ins):
    grid = (110215168,)
    t008_s0_kernel[grid](out, ins[0], ins[1], ins[2], ins[3])
    return out


@triton.jit
def t008_s1_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr):
    _acc0 = tl.zeros([8], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = tl.maximum(_acc0, tl.load(in4_ptr + ((((((((((tl.program_id(0) // 107632) * 16) + ((tl.program_id(0) // 6727) % 16)) * 14) + tl.maximum(((((tl.program_id(0) // 961) % 7) * 2) + tl.maximum(((tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) // 4) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 961) % 7) * 2), 0) - (tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) // 4), 0)) - tl.maximum(((tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) // 4) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 961) % 7) * 2), 0) - (tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) // 4), 0)) - tl.maximum(13 - (((tl.program_id(0) // 961) % 7) * 2), 0), 0), 0)) - tl.maximum(((((tl.program_id(0) // 961) % 7) * 2) + tl.maximum(((tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) // 4) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 961) % 7) * 2), 0) - (tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) // 4), 0)) - tl.maximum(((tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) // 4) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 961) % 7) * 2), 0) - (tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) // 4), 0)) - tl.maximum(13 - (((tl.program_id(0) // 961) % 7) * 2), 0), 0), 0)) - 13, 0), 0)) * 62) + tl.maximum(((((tl.program_id(0) // 31) % 31) * 2) + tl.maximum((((tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) // 2) % 2) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 31) % 31) * 2), 0) - ((tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) // 2) % 2), 0)) - tl.maximum((((tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) // 2) % 2) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 31) % 31) * 2), 0) - ((tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) // 2) % 2), 0)) - tl.maximum(61 - (((tl.program_id(0) // 31) % 31) * 2), 0), 0), 0)) - tl.maximum(((((tl.program_id(0) // 31) % 31) * 2) + tl.maximum((((tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) // 2) % 2) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 31) % 31) * 2), 0) - ((tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) // 2) % 2), 0)) - tl.maximum((((tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) // 2) % 2) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 31) % 31) * 2), 0) - ((tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) // 2) % 2), 0)) - tl.maximum(61 - (((tl.program_id(0) // 31) % 31) * 2), 0), 0), 0)) - 61, 0), 0)) * 62) + tl.maximum((((tl.program_id(0) % 31) * 2) + tl.maximum(((tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) % 2) + tl.maximum(tl.maximum(0 - ((tl.program_id(0) % 31) * 2), 0) - (tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) % 2), 0)) - tl.maximum(((tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) % 2) + tl.maximum(tl.maximum(0 - ((tl.program_id(0) % 31) * 2), 0) - (tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) % 2), 0)) - tl.maximum(61 - ((tl.program_id(0) % 31) * 2), 0), 0), 0)) - tl.maximum((((tl.program_id(0) % 31) * 2) + tl.maximum(((tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) % 2) + tl.maximum(tl.maximum(0 - ((tl.program_id(0) % 31) * 2), 0) - (tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) % 2), 0)) - tl.maximum(((tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) % 2) + tl.maximum(tl.maximum(0 - ((tl.program_id(0) % 31) * 2), 0) - (tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) % 2), 0)) - tl.maximum(61 - ((tl.program_id(0) % 31) * 2), 0), 0), 0)) - 61, 0), 0)))))
    _v = tl.max(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t008_s1(out, ins):
    grid = (13776896,)
    t008_s1_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4])
    return out


@triton.jit
def t008_s2_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 7):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 6727) & True), tl.load(in5_ptr + (((tl.program_id(0) * 6727) + ((_lv0 * 1024) + tl.arange(0, 1024))) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 6727) & True), other=0.0), 0.0))
    _v = (tl.sum(_acc0, axis=0) * (1.0 * (1.0 / 6727.0)))
    tl.store(out_ptr + tl.program_id(0), _v)


def t008_s2(out, ins):
    grid = (2048,)
    t008_s2_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5])
    return out


@triton.jit
def t008_s3_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr):
    _acc0 = tl.zeros([1], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), (tl.load(in6_ptr + ((((tl.program_id(0) // 16) * 16) + (tl.program_id(0) % 16)) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) + tl.load(in3_ptr + ((tl.program_id(0) % 16) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t008_s3(out, ins):
    grid = (2048,)
    t008_s3_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6])
    return out


@triton.jit
def t008_s4_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr):
    _acc0 = tl.zeros([16], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 16) + tl.arange(0, 16)) < 16) & True), tl.load(in7_ptr + (((tl.program_id(0) * 16) + ((_lv0 * 16) + tl.arange(0, 16))) + 0 * tl.arange(0, 16)), mask=((((_lv0 * 16) + tl.arange(0, 16)) < 16) & True), other=0.0), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t008_s4(out, ins):
    grid = (128,)
    t008_s4_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7])
    return out


def t008(out, ins):
    _t0 = torch.empty(110215168, device=ins[0].device, dtype=torch.float32)
    _t1 = torch.empty(13776896, device=ins[0].device, dtype=torch.float32)
    _t2 = torch.empty(2048, device=ins[0].device, dtype=torch.float32)
    _t3 = torch.empty(2048, device=ins[0].device, dtype=torch.float32)
    t008_s0(_t0, list(ins))
    t008_s1(_t1, list(ins) + [_t0])
    t008_s2(_t2, list(ins) + [_t0, _t1])
    t008_s3(_t3, list(ins) + [_t0, _t1, _t2])
    t008_s4(out, list(ins) + [_t0, _t1, _t2, _t3])
    return out
