import torch
import triton
import triton.language as tl


@triton.jit
def _mul_combine(a, b):
    return a * b


@triton.jit
def t025_s0_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr):
    _acc0 = tl.zeros([128], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 128) + tl.arange(0, 128)) < 144) & (((((tl.program_id(0) // 254) % 254) + ((((_lv0 * 128) + tl.arange(0, 128)) // 3) % 3)) < 256) & (((tl.program_id(0) % 254) + (((_lv0 * 128) + tl.arange(0, 128)) % 3)) < 256))), (tl.load(in0_ptr + ((((((((tl.program_id(0) // 4129024) * 16) + (((_lv0 * 128) + tl.arange(0, 128)) // 9)) * 256) + (((tl.program_id(0) // 254) % 254) + ((((_lv0 * 128) + tl.arange(0, 128)) // 3) % 3))) * 256) + ((tl.program_id(0) % 254) + (((_lv0 * 128) + tl.arange(0, 128)) % 3))) + 0 * tl.arange(0, 128)), mask=((((_lv0 * 128) + tl.arange(0, 128)) < 144) & (((((tl.program_id(0) // 254) % 254) + ((((_lv0 * 128) + tl.arange(0, 128)) // 3) % 3)) < 256) & (((tl.program_id(0) % 254) + (((_lv0 * 128) + tl.arange(0, 128)) % 3)) < 256))), other=0.0) * tl.load(in1_ptr + (((((((((tl.program_id(0) // 64516) % 64) * 16) + (((_lv0 * 128) + tl.arange(0, 128)) // 9)) * 3) + ((((_lv0 * 128) + tl.arange(0, 128)) // 3) % 3)) * 3) + (((_lv0 * 128) + tl.arange(0, 128)) % 3)) + 0 * tl.arange(0, 128)), mask=((((_lv0 * 128) + tl.arange(0, 128)) < 144) & (((((tl.program_id(0) // 254) % 254) + ((((_lv0 * 128) + tl.arange(0, 128)) // 3) % 3)) < 256) & (((tl.program_id(0) % 254) + (((_lv0 * 128) + tl.arange(0, 128)) % 3)) < 256))), other=0.0)), 0.0))
    _v = (tl.sum(_acc0, axis=0) + tl.load(in2_ptr + (((tl.program_id(0) // 64516) % 64))))
    tl.store(out_ptr + tl.program_id(0), _v)


def t025_s0(out, ins):
    grid = (528515072,)
    t025_s0_kernel[grid](out, ins[0], ins[1], ins[2])
    return out


@triton.jit
def t025_s1_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr):
    _acc0 = tl.zeros([64], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = tl.maximum(_acc0, ((0.0 * (1.0 / 1.0)) - tl.load(in3_ptr + ((((((tl.program_id(0) // 64516) * 64) + tl.maximum(((_lv0 * 64) + tl.arange(0, 64)) - tl.maximum(((_lv0 * 64) + tl.arange(0, 64)) - 63, 0), 0)) * 64516) + (tl.program_id(0) % 64516))))))
    _v = (2.0 * tl.sigmoid(2.0 * ((2.0 * tl.sigmoid(2.0 * (((0.0 * (1.0 / 1.0)) - tl.max(_acc0, axis=0)))) - 1.0))) - 1.0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t025_s1(out, ins):
    grid = (8258048,)
    t025_s1_kernel[grid](out, ins[0], ins[1], ins[2], ins[3])
    return out


def t025(out, ins):
    _t0 = torch.empty(528515072, device=ins[0].device, dtype=torch.float32)
    t025_s0(_t0, list(ins))
    t025_s1(out, list(ins) + [_t0])
    return out
