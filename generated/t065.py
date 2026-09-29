import torch
import triton
import triton.language as tl


@triton.jit
def _mul_combine(a, b):
    return a * b


@triton.jit
def t065_s0_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr):
    _acc0 = tl.zeros([64], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 64) + tl.arange(0, 64)) < 72) & (((((tl.program_id(0) // 382) % 382) + ((((_lv0 * 64) + tl.arange(0, 64)) // 3) % 3)) < 384) & (((tl.program_id(0) % 382) + (((_lv0 * 64) + tl.arange(0, 64)) % 3)) < 384))), (tl.load(in0_ptr + ((((((((tl.program_id(0) // 9339136) * 8) + (((_lv0 * 64) + tl.arange(0, 64)) // 9)) * 384) + (((tl.program_id(0) // 382) % 382) + ((((_lv0 * 64) + tl.arange(0, 64)) // 3) % 3))) * 384) + ((tl.program_id(0) % 382) + (((_lv0 * 64) + tl.arange(0, 64)) % 3))) + 0 * tl.arange(0, 64)), mask=((((_lv0 * 64) + tl.arange(0, 64)) < 72) & (((((tl.program_id(0) // 382) % 382) + ((((_lv0 * 64) + tl.arange(0, 64)) // 3) % 3)) < 384) & (((tl.program_id(0) % 382) + (((_lv0 * 64) + tl.arange(0, 64)) % 3)) < 384))), other=0.0) * tl.load(in1_ptr + (((((((((tl.program_id(0) // 145924) % 64) * 8) + (((_lv0 * 64) + tl.arange(0, 64)) // 9)) * 3) + ((((_lv0 * 64) + tl.arange(0, 64)) // 3) % 3)) * 3) + (((_lv0 * 64) + tl.arange(0, 64)) % 3)) + 0 * tl.arange(0, 64)), mask=((((_lv0 * 64) + tl.arange(0, 64)) < 72) & (((((tl.program_id(0) // 382) % 382) + ((((_lv0 * 64) + tl.arange(0, 64)) // 3) % 3)) < 384) & (((tl.program_id(0) % 382) + (((_lv0 * 64) + tl.arange(0, 64)) % 3)) < 384))), other=0.0)), 0.0))
    _v = (tl.sum(_acc0, axis=0) + tl.load(in2_ptr + (((tl.program_id(0) // 145924) % 64))))
    tl.store(out_ptr + tl.program_id(0), _v)


def t065_s0(out, ins):
    grid = (1195409408,)
    t065_s0_kernel[grid](out, ins[0], ins[1], ins[2])
    return out


@triton.jit
def t065_s1_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr):
    _acc0 = tl.zeros([16], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 16) + tl.arange(0, 16)) < 16) & ((((0 <= ((((tl.program_id(0) // 95) % 95) * 4) + (((_lv0 * 16) + tl.arange(0, 16)) // 4))) & (((((tl.program_id(0) // 95) % 95) * 4) + (((_lv0 * 16) + tl.arange(0, 16)) // 4)) < 382)) & (0 <= (((tl.program_id(0) % 95) * 4) + (((_lv0 * 16) + tl.arange(0, 16)) % 4)))) & ((((tl.program_id(0) % 95) * 4) + (((_lv0 * 16) + tl.arange(0, 16)) % 4)) < 382))), tl.load(in3_ptr + (tl.maximum((((((((tl.program_id(0) // 577600) * 64) + ((tl.program_id(0) // 9025) % 64)) * 382) + ((((tl.program_id(0) // 95) % 95) * 4) + (((_lv0 * 16) + tl.arange(0, 16)) // 4))) * 382) + (((tl.program_id(0) % 95) * 4) + (((_lv0 * 16) + tl.arange(0, 16)) % 4))) - tl.maximum((((((((tl.program_id(0) // 577600) * 64) + ((tl.program_id(0) // 9025) % 64)) * 382) + ((((tl.program_id(0) // 95) % 95) * 4) + (((_lv0 * 16) + tl.arange(0, 16)) // 4))) * 382) + (((tl.program_id(0) % 95) * 4) + (((_lv0 * 16) + tl.arange(0, 16)) % 4))) - 1195409407, 0), 0) + 0 * tl.arange(0, 16)), mask=((((_lv0 * 16) + tl.arange(0, 16)) < 16) & ((((0 <= ((((tl.program_id(0) // 95) % 95) * 4) + (((_lv0 * 16) + tl.arange(0, 16)) // 4))) & (((((tl.program_id(0) // 95) % 95) * 4) + (((_lv0 * 16) + tl.arange(0, 16)) // 4)) < 382)) & (0 <= (((tl.program_id(0) % 95) * 4) + (((_lv0 * 16) + tl.arange(0, 16)) % 4)))) & ((((tl.program_id(0) % 95) * 4) + (((_lv0 * 16) + tl.arange(0, 16)) % 4)) < 382))), other=0.0), 0.0))
    _v = (1.0 / ((1.0 * (1.0 / 1.0)) + tl.exp(((0.0 * (1.0 / 1.0)) - (tl.sum(_acc0, axis=0) * (1.0 * (1.0 / 16.0)))))))
    tl.store(out_ptr + tl.program_id(0), _v)


def t065_s1(out, ins):
    grid = (73932800,)
    t065_s1_kernel[grid](out, ins[0], ins[1], ins[2], ins[3])
    return out


@triton.jit
def t065_s2_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 565):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 577600) & True), tl.load(in4_ptr + (((tl.program_id(0) * 577600) + ((_lv0 * 1024) + tl.arange(0, 1024))) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 577600) & True), other=0.0), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t065_s2(out, ins):
    grid = (128,)
    t065_s2_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4])
    return out


def t065(out, ins):
    _t0 = torch.empty(1195409408, device=ins[0].device, dtype=torch.float32)
    _t1 = torch.empty(73932800, device=ins[0].device, dtype=torch.float32)
    t065_s0(_t0, list(ins))
    t065_s1(_t1, list(ins) + [_t0])
    t065_s2(out, list(ins) + [_t0, _t1])
    return out
