import torch
import triton
import triton.language as tl


@triton.jit
def _mul_combine(a, b):
    return a * b


@triton.jit
def t043_s0_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr):
    _acc0 = tl.zeros([512], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 512) + tl.arange(0, 512)) < 864) & ((((((1 <= (((tl.program_id(0) // 16384) % 32) + ((((_lv0 * 512) + tl.arange(0, 512)) // 9) % 3))) & ((((tl.program_id(0) // 16384) % 32) + ((((_lv0 * 512) + tl.arange(0, 512)) // 9) % 3)) < 33)) & (1 <= (((tl.program_id(0) // 128) % 128) + ((((_lv0 * 512) + tl.arange(0, 512)) // 3) % 3)))) & ((((tl.program_id(0) // 128) % 128) + ((((_lv0 * 512) + tl.arange(0, 512)) // 3) % 3)) < 129)) & (1 <= ((tl.program_id(0) % 128) + (((_lv0 * 512) + tl.arange(0, 512)) % 3)))) & (((tl.program_id(0) % 128) + (((_lv0 * 512) + tl.arange(0, 512)) % 3)) < 129))), (tl.load(in0_ptr + ((((((((((tl.program_id(0) // 33554432) * 32) + (((_lv0 * 512) + tl.arange(0, 512)) // 27)) * 32) + tl.maximum((((tl.program_id(0) // 16384) % 32) + ((((_lv0 * 512) + tl.arange(0, 512)) // 9) % 3)) - 1, 0)) * 128) + tl.maximum((((tl.program_id(0) // 128) % 128) + ((((_lv0 * 512) + tl.arange(0, 512)) // 3) % 3)) - 1, 0)) * 128) + tl.maximum(((tl.program_id(0) % 128) + (((_lv0 * 512) + tl.arange(0, 512)) % 3)) - 1, 0)) + 0 * tl.arange(0, 512)), mask=((((_lv0 * 512) + tl.arange(0, 512)) < 864) & ((((((1 <= (((tl.program_id(0) // 16384) % 32) + ((((_lv0 * 512) + tl.arange(0, 512)) // 9) % 3))) & ((((tl.program_id(0) // 16384) % 32) + ((((_lv0 * 512) + tl.arange(0, 512)) // 9) % 3)) < 33)) & (1 <= (((tl.program_id(0) // 128) % 128) + ((((_lv0 * 512) + tl.arange(0, 512)) // 3) % 3)))) & ((((tl.program_id(0) // 128) % 128) + ((((_lv0 * 512) + tl.arange(0, 512)) // 3) % 3)) < 129)) & (1 <= ((tl.program_id(0) % 128) + (((_lv0 * 512) + tl.arange(0, 512)) % 3)))) & (((tl.program_id(0) % 128) + (((_lv0 * 512) + tl.arange(0, 512)) % 3)) < 129))), other=0.0) * tl.load(in1_ptr + (((((((((((tl.program_id(0) // 524288) % 64) * 32) + (((_lv0 * 512) + tl.arange(0, 512)) // 27)) * 3) + ((((_lv0 * 512) + tl.arange(0, 512)) // 9) % 3)) * 3) + ((((_lv0 * 512) + tl.arange(0, 512)) // 3) % 3)) * 3) + (((_lv0 * 512) + tl.arange(0, 512)) % 3)) + 0 * tl.arange(0, 512)), mask=((((_lv0 * 512) + tl.arange(0, 512)) < 864) & ((((((1 <= (((tl.program_id(0) // 16384) % 32) + ((((_lv0 * 512) + tl.arange(0, 512)) // 9) % 3))) & ((((tl.program_id(0) // 16384) % 32) + ((((_lv0 * 512) + tl.arange(0, 512)) // 9) % 3)) < 33)) & (1 <= (((tl.program_id(0) // 128) % 128) + ((((_lv0 * 512) + tl.arange(0, 512)) // 3) % 3)))) & ((((tl.program_id(0) // 128) % 128) + ((((_lv0 * 512) + tl.arange(0, 512)) // 3) % 3)) < 129)) & (1 <= ((tl.program_id(0) % 128) + (((_lv0 * 512) + tl.arange(0, 512)) % 3)))) & (((tl.program_id(0) % 128) + (((_lv0 * 512) + tl.arange(0, 512)) % 3)) < 129))), other=0.0)), 0.0))
    _v = (tl.sum(_acc0, axis=0) + tl.load(in2_ptr + (((tl.program_id(0) // 524288) % 64))))
    tl.store(out_ptr + tl.program_id(0), _v)


def t043_s0(out, ins):
    grid = (134217728,)
    t043_s0_kernel[grid](out, ins[0], ins[1], ins[2])
    return out


@triton.jit
def t043_s1_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr):
    _acc0 = tl.zeros([8], dtype=tl.float32) + (tl.load(in3_ptr + ((((((((((tl.program_id(0) // 4194304) * 64) + ((tl.program_id(0) // 65536) % 64)) * 32) + tl.maximum(((((tl.program_id(0) // 4096) % 16) * 2) + tl.maximum(((0 // 4) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 4096) % 16) * 2), 0) - (0 // 4), 0)) - tl.maximum(((0 // 4) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 4096) % 16) * 2), 0) - (0 // 4), 0)) - tl.maximum(31 - (((tl.program_id(0) // 4096) % 16) * 2), 0), 0), 0)) - tl.maximum(((((tl.program_id(0) // 4096) % 16) * 2) + tl.maximum(((0 // 4) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 4096) % 16) * 2), 0) - (0 // 4), 0)) - tl.maximum(((0 // 4) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 4096) % 16) * 2), 0) - (0 // 4), 0)) - tl.maximum(31 - (((tl.program_id(0) // 4096) % 16) * 2), 0), 0), 0)) - 31, 0), 0)) * 128) + tl.maximum(((((tl.program_id(0) // 64) % 64) * 2) + tl.maximum((((0 // 2) % 2) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 64) % 64) * 2), 0) - ((0 // 2) % 2), 0)) - tl.maximum((((0 // 2) % 2) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 64) % 64) * 2), 0) - ((0 // 2) % 2), 0)) - tl.maximum(127 - (((tl.program_id(0) // 64) % 64) * 2), 0), 0), 0)) - tl.maximum(((((tl.program_id(0) // 64) % 64) * 2) + tl.maximum((((0 // 2) % 2) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 64) % 64) * 2), 0) - ((0 // 2) % 2), 0)) - tl.maximum((((0 // 2) % 2) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 64) % 64) * 2), 0) - ((0 // 2) % 2), 0)) - tl.maximum(127 - (((tl.program_id(0) // 64) % 64) * 2), 0), 0), 0)) - 127, 0), 0)) * 128) + tl.maximum((((tl.program_id(0) % 64) * 2) + tl.maximum(((0 % 2) + tl.maximum(tl.maximum(0 - ((tl.program_id(0) % 64) * 2), 0) - (0 % 2), 0)) - tl.maximum(((0 % 2) + tl.maximum(tl.maximum(0 - ((tl.program_id(0) % 64) * 2), 0) - (0 % 2), 0)) - tl.maximum(127 - ((tl.program_id(0) % 64) * 2), 0), 0), 0)) - tl.maximum((((tl.program_id(0) % 64) * 2) + tl.maximum(((0 % 2) + tl.maximum(tl.maximum(0 - ((tl.program_id(0) % 64) * 2), 0) - (0 % 2), 0)) - tl.maximum(((0 % 2) + tl.maximum(tl.maximum(0 - ((tl.program_id(0) % 64) * 2), 0) - (0 % 2), 0)) - tl.maximum(127 - ((tl.program_id(0) % 64) * 2), 0), 0), 0)) - 127, 0), 0)))))
    for _lv0 in range(0, 1):
        _acc0 = tl.maximum(_acc0, tl.load(in3_ptr + ((((((((((tl.program_id(0) // 4194304) * 64) + ((tl.program_id(0) // 65536) % 64)) * 32) + tl.maximum(((((tl.program_id(0) // 4096) % 16) * 2) + tl.maximum(((tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) // 4) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 4096) % 16) * 2), 0) - (tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) // 4), 0)) - tl.maximum(((tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) // 4) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 4096) % 16) * 2), 0) - (tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) // 4), 0)) - tl.maximum(31 - (((tl.program_id(0) // 4096) % 16) * 2), 0), 0), 0)) - tl.maximum(((((tl.program_id(0) // 4096) % 16) * 2) + tl.maximum(((tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) // 4) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 4096) % 16) * 2), 0) - (tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) // 4), 0)) - tl.maximum(((tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) // 4) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 4096) % 16) * 2), 0) - (tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) // 4), 0)) - tl.maximum(31 - (((tl.program_id(0) // 4096) % 16) * 2), 0), 0), 0)) - 31, 0), 0)) * 128) + tl.maximum(((((tl.program_id(0) // 64) % 64) * 2) + tl.maximum((((tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) // 2) % 2) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 64) % 64) * 2), 0) - ((tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) // 2) % 2), 0)) - tl.maximum((((tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) // 2) % 2) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 64) % 64) * 2), 0) - ((tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) // 2) % 2), 0)) - tl.maximum(127 - (((tl.program_id(0) // 64) % 64) * 2), 0), 0), 0)) - tl.maximum(((((tl.program_id(0) // 64) % 64) * 2) + tl.maximum((((tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) // 2) % 2) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 64) % 64) * 2), 0) - ((tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) // 2) % 2), 0)) - tl.maximum((((tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) // 2) % 2) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 64) % 64) * 2), 0) - ((tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) // 2) % 2), 0)) - tl.maximum(127 - (((tl.program_id(0) // 64) % 64) * 2), 0), 0), 0)) - 127, 0), 0)) * 128) + tl.maximum((((tl.program_id(0) % 64) * 2) + tl.maximum(((tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) % 2) + tl.maximum(tl.maximum(0 - ((tl.program_id(0) % 64) * 2), 0) - (tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) % 2), 0)) - tl.maximum(((tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) % 2) + tl.maximum(tl.maximum(0 - ((tl.program_id(0) % 64) * 2), 0) - (tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) % 2), 0)) - tl.maximum(127 - ((tl.program_id(0) % 64) * 2), 0), 0), 0)) - tl.maximum((((tl.program_id(0) % 64) * 2) + tl.maximum(((tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) % 2) + tl.maximum(tl.maximum(0 - ((tl.program_id(0) % 64) * 2), 0) - (tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) % 2), 0)) - tl.maximum(((tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) % 2) + tl.maximum(tl.maximum(0 - ((tl.program_id(0) % 64) * 2), 0) - (tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) % 2), 0)) - tl.maximum(127 - ((tl.program_id(0) % 64) * 2), 0), 0), 0)) - 127, 0), 0)))))
    _v = tl.max(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t043_s1(out, ins):
    grid = (16777216,)
    t043_s1_kernel[grid](out, ins[0], ins[1], ins[2], ins[3])
    return out


@triton.jit
def t043_s2_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr):
    _acc0 = tl.zeros([64], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 64) + tl.arange(0, 64)) < 64) & True), tl.exp(tl.load(in4_ptr + ((((((((((tl.program_id(0) // 65536) * 64) + ((_lv0 * 64) + tl.arange(0, 64))) * 16) + ((tl.program_id(0) // 4096) % 16)) * 64) + ((tl.program_id(0) // 64) % 64)) * 64) + (tl.program_id(0) % 64)) + 0 * tl.arange(0, 64)), mask=((((_lv0 * 64) + tl.arange(0, 64)) < 64) & True), other=0.0)), 0.0))
    _v = tl.maximum(tl.log(tl.sum(_acc0, axis=0)), (0.0 * (1.0 / 1.0)))
    tl.store(out_ptr + tl.program_id(0), _v)


def t043_s2(out, ins):
    grid = (262144,)
    t043_s2_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4])
    return out


def t043(out, ins):
    _t0 = torch.empty(134217728, device=ins[0].device, dtype=torch.float32)
    _t1 = torch.empty(16777216, device=ins[0].device, dtype=torch.float32)
    t043_s0(_t0, list(ins))
    t043_s1(_t1, list(ins) + [_t0])
    t043_s2(out, list(ins) + [_t0, _t1])
    return out
