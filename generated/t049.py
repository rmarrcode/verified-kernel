import torch
import triton
import triton.language as tl


@triton.jit
def _mul_combine(a, b):
    return a * b


@triton.jit
def t049_s0_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr):
    _acc0 = tl.zeros([512], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 512) + tl.arange(0, 512)) < 864) & (((((((((((((_lv0 * 512) + tl.arange(0, 512)) // 9) % 3) <= (((tl.program_id(0) // 4096) % 32) + 1)) & ((tl.maximum((((tl.program_id(0) // 4096) % 32) + 1) - ((((_lv0 * 512) + tl.arange(0, 512)) // 9) % 3), 0) % 2) == 0)) & ((tl.maximum((((tl.program_id(0) // 4096) % 32) + 1) - ((((_lv0 * 512) + tl.arange(0, 512)) // 9) % 3), 0) // 2) < 16)) & (((((_lv0 * 512) + tl.arange(0, 512)) // 3) % 3) <= (((tl.program_id(0) // 64) % 64) + 1))) & ((tl.maximum((((tl.program_id(0) // 64) % 64) + 1) - ((((_lv0 * 512) + tl.arange(0, 512)) // 3) % 3), 0) % 2) == 0)) & ((tl.maximum((((tl.program_id(0) // 64) % 64) + 1) - ((((_lv0 * 512) + tl.arange(0, 512)) // 3) % 3), 0) // 2) < 32)) & ((((_lv0 * 512) + tl.arange(0, 512)) % 3) <= ((tl.program_id(0) % 64) + 1))) & ((tl.maximum(((tl.program_id(0) % 64) + 1) - (((_lv0 * 512) + tl.arange(0, 512)) % 3), 0) % 2) == 0)) & ((tl.maximum(((tl.program_id(0) % 64) + 1) - (((_lv0 * 512) + tl.arange(0, 512)) % 3), 0) // 2) < 32))), (tl.load(in0_ptr + ((((((((((tl.program_id(0) // 8388608) * 32) + (((((tl.program_id(0) // 131072) % 64) // 64) * 32) + (((_lv0 * 512) + tl.arange(0, 512)) // 27))) * 16) + (tl.maximum((((tl.program_id(0) // 4096) % 32) + 1) - ((((_lv0 * 512) + tl.arange(0, 512)) // 9) % 3), 0) // 2)) * 32) + (tl.maximum((((tl.program_id(0) // 64) % 64) + 1) - ((((_lv0 * 512) + tl.arange(0, 512)) // 3) % 3), 0) // 2)) * 32) + (tl.maximum(((tl.program_id(0) % 64) + 1) - (((_lv0 * 512) + tl.arange(0, 512)) % 3), 0) // 2)) + 0 * tl.arange(0, 512)), mask=((((_lv0 * 512) + tl.arange(0, 512)) < 864) & (((((((((((((_lv0 * 512) + tl.arange(0, 512)) // 9) % 3) <= (((tl.program_id(0) // 4096) % 32) + 1)) & ((tl.maximum((((tl.program_id(0) // 4096) % 32) + 1) - ((((_lv0 * 512) + tl.arange(0, 512)) // 9) % 3), 0) % 2) == 0)) & ((tl.maximum((((tl.program_id(0) // 4096) % 32) + 1) - ((((_lv0 * 512) + tl.arange(0, 512)) // 9) % 3), 0) // 2) < 16)) & (((((_lv0 * 512) + tl.arange(0, 512)) // 3) % 3) <= (((tl.program_id(0) // 64) % 64) + 1))) & ((tl.maximum((((tl.program_id(0) // 64) % 64) + 1) - ((((_lv0 * 512) + tl.arange(0, 512)) // 3) % 3), 0) % 2) == 0)) & ((tl.maximum((((tl.program_id(0) // 64) % 64) + 1) - ((((_lv0 * 512) + tl.arange(0, 512)) // 3) % 3), 0) // 2) < 32)) & ((((_lv0 * 512) + tl.arange(0, 512)) % 3) <= ((tl.program_id(0) % 64) + 1))) & ((tl.maximum(((tl.program_id(0) % 64) + 1) - (((_lv0 * 512) + tl.arange(0, 512)) % 3), 0) % 2) == 0)) & ((tl.maximum(((tl.program_id(0) % 64) + 1) - (((_lv0 * 512) + tl.arange(0, 512)) % 3), 0) // 2) < 32))), other=0.0) * tl.load(in1_ptr + ((((((((((((((tl.program_id(0) // 131072) % 64) // 64) * 32) + (((_lv0 * 512) + tl.arange(0, 512)) // 27)) * 64) + (((tl.program_id(0) // 131072) % 64) % 64)) * 3) + ((((_lv0 * 512) + tl.arange(0, 512)) // 9) % 3)) * 3) + ((((_lv0 * 512) + tl.arange(0, 512)) // 3) % 3)) * 3) + (((_lv0 * 512) + tl.arange(0, 512)) % 3)) + 0 * tl.arange(0, 512)), mask=((((_lv0 * 512) + tl.arange(0, 512)) < 864) & (((((((((((((_lv0 * 512) + tl.arange(0, 512)) // 9) % 3) <= (((tl.program_id(0) // 4096) % 32) + 1)) & ((tl.maximum((((tl.program_id(0) // 4096) % 32) + 1) - ((((_lv0 * 512) + tl.arange(0, 512)) // 9) % 3), 0) % 2) == 0)) & ((tl.maximum((((tl.program_id(0) // 4096) % 32) + 1) - ((((_lv0 * 512) + tl.arange(0, 512)) // 9) % 3), 0) // 2) < 16)) & (((((_lv0 * 512) + tl.arange(0, 512)) // 3) % 3) <= (((tl.program_id(0) // 64) % 64) + 1))) & ((tl.maximum((((tl.program_id(0) // 64) % 64) + 1) - ((((_lv0 * 512) + tl.arange(0, 512)) // 3) % 3), 0) % 2) == 0)) & ((tl.maximum((((tl.program_id(0) // 64) % 64) + 1) - ((((_lv0 * 512) + tl.arange(0, 512)) // 3) % 3), 0) // 2) < 32)) & ((((_lv0 * 512) + tl.arange(0, 512)) % 3) <= ((tl.program_id(0) % 64) + 1))) & ((tl.maximum(((tl.program_id(0) % 64) + 1) - (((_lv0 * 512) + tl.arange(0, 512)) % 3), 0) % 2) == 0)) & ((tl.maximum(((tl.program_id(0) % 64) + 1) - (((_lv0 * 512) + tl.arange(0, 512)) % 3), 0) // 2) < 32))), other=0.0)), 0.0))
    _v = (tl.sum(_acc0, axis=0) + tl.load(in2_ptr + (((tl.program_id(0) // 131072) % 64))))
    tl.store(out_ptr + tl.program_id(0), _v)


def t049_s0(out, ins):
    grid = (134217728,)
    t049_s0_kernel[grid](out, ins[0], ins[1], ins[2])
    return out


@triton.jit
def t049_s1_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr):
    _acc0 = tl.zeros([64], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 64) + tl.arange(0, 64)) < 64) & True), tl.exp(tl.load(in3_ptr + ((((((tl.program_id(0) // 131072) * 64) + ((_lv0 * 64) + tl.arange(0, 64))) * 131072) + (tl.program_id(0) % 131072)) + 0 * tl.arange(0, 64)), mask=((((_lv0 * 64) + tl.arange(0, 64)) < 64) & True), other=0.0)), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t049_s1(out, ins):
    grid = (2097152,)
    t049_s1_kernel[grid](out, ins[0], ins[1], ins[2], ins[3])
    return out


@triton.jit
def t049_s2_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr):
    _acc0 = tl.zeros([1], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), (tl.exp(tl.load(in3_ptr + (tl.program_id(0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)) * (1.0 / tl.load(in4_ptr + (tl.maximum((((tl.program_id(0) // (64 * 131072)) * 131072) + (tl.program_id(0) % 131072)) - tl.maximum((((tl.program_id(0) // (64 * 131072)) * 131072) + (tl.program_id(0) % 131072)) - 2097151, 0), 0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0))), 0.0))
    _v = (1.0 / ((1.0 * (1.0 / 1.0)) + tl.exp(((0.0 * (1.0 / 1.0)) - tl.sum(_acc0, axis=0)))))
    tl.store(out_ptr + tl.program_id(0), _v)


def t049_s2(out, ins):
    grid = (134217728,)
    t049_s2_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4])
    return out


def t049(out, ins):
    _t0 = torch.empty(134217728, device=ins[0].device, dtype=torch.float32)
    _t1 = torch.empty(2097152, device=ins[0].device, dtype=torch.float32)
    t049_s0(_t0, list(ins))
    t049_s1(_t1, list(ins) + [_t0])
    t049_s2(out, list(ins) + [_t0, _t1])
    return out
