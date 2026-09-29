import torch
import triton
import triton.language as tl


@triton.jit
def _mul_combine(a, b):
    return a * b


@triton.jit
def t061_s0_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 1728) & (((((((((((((_lv0 * 1024) + tl.arange(0, 1024)) // 9) % 3) <= ((tl.program_id(0) // 1156) % 34)) & (0 == 0)) & (tl.maximum(((tl.program_id(0) // 1156) % 34) - ((((_lv0 * 1024) + tl.arange(0, 1024)) // 9) % 3), 0) < 32)) & (((((_lv0 * 1024) + tl.arange(0, 1024)) // 3) % 3) <= ((tl.program_id(0) // 34) % 34))) & (0 == 0)) & (tl.maximum(((tl.program_id(0) // 34) % 34) - ((((_lv0 * 1024) + tl.arange(0, 1024)) // 3) % 3), 0) < 32)) & ((((_lv0 * 1024) + tl.arange(0, 1024)) % 3) <= (tl.program_id(0) % 34))) & (0 == 0)) & (tl.maximum((tl.program_id(0) % 34) - (((_lv0 * 1024) + tl.arange(0, 1024)) % 3), 0) < 32))), (tl.load(in0_ptr + ((((((((((tl.program_id(0) // 5030912) * 64) + (((((tl.program_id(0) // 39304) % 128) // 128) * 64) + (((_lv0 * 1024) + tl.arange(0, 1024)) // 27))) * 32) + tl.maximum(((tl.program_id(0) // 1156) % 34) - ((((_lv0 * 1024) + tl.arange(0, 1024)) // 9) % 3), 0)) * 32) + tl.maximum(((tl.program_id(0) // 34) % 34) - ((((_lv0 * 1024) + tl.arange(0, 1024)) // 3) % 3), 0)) * 32) + tl.maximum((tl.program_id(0) % 34) - (((_lv0 * 1024) + tl.arange(0, 1024)) % 3), 0)) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 1728) & (((((((((((((_lv0 * 1024) + tl.arange(0, 1024)) // 9) % 3) <= ((tl.program_id(0) // 1156) % 34)) & (0 == 0)) & (tl.maximum(((tl.program_id(0) // 1156) % 34) - ((((_lv0 * 1024) + tl.arange(0, 1024)) // 9) % 3), 0) < 32)) & (((((_lv0 * 1024) + tl.arange(0, 1024)) // 3) % 3) <= ((tl.program_id(0) // 34) % 34))) & (0 == 0)) & (tl.maximum(((tl.program_id(0) // 34) % 34) - ((((_lv0 * 1024) + tl.arange(0, 1024)) // 3) % 3), 0) < 32)) & ((((_lv0 * 1024) + tl.arange(0, 1024)) % 3) <= (tl.program_id(0) % 34))) & (0 == 0)) & (tl.maximum((tl.program_id(0) % 34) - (((_lv0 * 1024) + tl.arange(0, 1024)) % 3), 0) < 32))), other=0.0) * tl.load(in1_ptr + ((((((((((((((tl.program_id(0) // 39304) % 128) // 128) * 64) + (((_lv0 * 1024) + tl.arange(0, 1024)) // 27)) * 128) + (((tl.program_id(0) // 39304) % 128) % 128)) * 3) + ((((_lv0 * 1024) + tl.arange(0, 1024)) // 9) % 3)) * 3) + ((((_lv0 * 1024) + tl.arange(0, 1024)) // 3) % 3)) * 3) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 3)) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 1728) & (((((((((((((_lv0 * 1024) + tl.arange(0, 1024)) // 9) % 3) <= ((tl.program_id(0) // 1156) % 34)) & (0 == 0)) & (tl.maximum(((tl.program_id(0) // 1156) % 34) - ((((_lv0 * 1024) + tl.arange(0, 1024)) // 9) % 3), 0) < 32)) & (((((_lv0 * 1024) + tl.arange(0, 1024)) // 3) % 3) <= ((tl.program_id(0) // 34) % 34))) & (0 == 0)) & (tl.maximum(((tl.program_id(0) // 34) % 34) - ((((_lv0 * 1024) + tl.arange(0, 1024)) // 3) % 3), 0) < 32)) & ((((_lv0 * 1024) + tl.arange(0, 1024)) % 3) <= (tl.program_id(0) % 34))) & (0 == 0)) & (tl.maximum((tl.program_id(0) % 34) - (((_lv0 * 1024) + tl.arange(0, 1024)) % 3), 0) < 32))), other=0.0)), 0.0))
    _v = tl.maximum(tl.sum(_acc0, axis=0), (0.0 * (1.0 / 1.0)))
    tl.store(out_ptr + tl.program_id(0), _v)


def t061_s0(out, ins):
    grid = (80494592,)
    t061_s0_kernel[grid](out, ins[0], ins[1], ins[2], ins[3])
    return out


@triton.jit
def t061_s1_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 615):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 628864) & True), tl.load(in4_ptr + (tl.maximum(((((((tl.program_id(0) // 8) * 128) + ((tl.program_id(0) % 8) * 16)) + (((_lv0 * 1024) + tl.arange(0, 1024)) // 39304)) * 39304) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 39304)) - tl.maximum(((((((tl.program_id(0) // 8) * 128) + ((tl.program_id(0) % 8) * 16)) + (((_lv0 * 1024) + tl.arange(0, 1024)) // 39304)) * 39304) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 39304)) - 80494591, 0), 0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 628864) & True), other=0.0), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t061_s1(out, ins):
    grid = (128,)
    t061_s1_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4])
    return out


@triton.jit
def t061_s2_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 615):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 628864) & True), ((tl.load(in4_ptr + (tl.maximum(((((((tl.program_id(0) // 8) * 128) + ((tl.program_id(0) % 8) * 16)) + (((_lv0 * 1024) + tl.arange(0, 1024)) // 39304)) * 39304) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 39304)) - tl.maximum(((((((tl.program_id(0) // 8) * 128) + ((tl.program_id(0) % 8) * 16)) + (((_lv0 * 1024) + tl.arange(0, 1024)) // 39304)) * 39304) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 39304)) - 80494591, 0), 0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 628864) & True), other=0.0) - (tl.load(in5_ptr + (tl.program_id(0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 628864) & True), other=0.0) * (1.0 * (1.0 / 628864.0)))) * (tl.load(in4_ptr + (tl.maximum(((((((tl.program_id(0) // 8) * 128) + ((tl.program_id(0) % 8) * 16)) + (((_lv0 * 1024) + tl.arange(0, 1024)) // 39304)) * 39304) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 39304)) - tl.maximum(((((((tl.program_id(0) // 8) * 128) + ((tl.program_id(0) % 8) * 16)) + (((_lv0 * 1024) + tl.arange(0, 1024)) // 39304)) * 39304) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 39304)) - 80494591, 0), 0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 628864) & True), other=0.0) - (tl.load(in5_ptr + (tl.program_id(0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 628864) & True), other=0.0) * (1.0 * (1.0 / 628864.0))))), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t061_s2(out, ins):
    grid = (128,)
    t061_s2_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5])
    return out


@triton.jit
def t061_s3_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr):
    _acc0 = tl.zeros([1], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), ((((tl.load(in4_ptr + (tl.program_id(0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) - (tl.load(in5_ptr + (tl.maximum((((tl.program_id(0) // 5030912) * 8) + (((tl.program_id(0) // 39304) % 128) // 16)) - tl.maximum((((tl.program_id(0) // 5030912) * 8) + (((tl.program_id(0) // 39304) % 128) // 16)) - 127, 0), 0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) * (1.0 * (1.0 / 628864.0)))) * (1.0 / tl.sqrt(((tl.load(in6_ptr + (tl.maximum((((tl.program_id(0) // 5030912) * 8) + (((tl.program_id(0) // 39304) % 128) // 16)) - tl.maximum((((tl.program_id(0) // 5030912) * 8) + (((tl.program_id(0) // 39304) % 128) // 16)) - 127, 0), 0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) * (1.0 * (1.0 / 628864.0))) + (1.0 * (1.0 / 100000.0)))))) * tl.load(in2_ptr + (((tl.program_id(0) // 39304) % 128) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)) + tl.load(in3_ptr + (((tl.program_id(0) // 39304) % 128) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t061_s3(out, ins):
    grid = (80494592,)
    t061_s3_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6])
    return out


def t061(out, ins):
    _t0 = torch.empty(80494592, device=ins[0].device, dtype=torch.float32)
    _t1 = torch.empty(128, device=ins[0].device, dtype=torch.float32)
    _t2 = torch.empty(128, device=ins[0].device, dtype=torch.float32)
    t061_s0(_t0, list(ins))
    t061_s1(_t1, list(ins) + [_t0])
    t061_s2(_t2, list(ins) + [_t0, _t1])
    t061_s3(out, list(ins) + [_t0, _t1, _t2])
    return out
