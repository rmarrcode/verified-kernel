import torch
import triton
import triton.language as tl


@triton.jit
def _mul_combine(a, b):
    return a * b


@triton.jit
def t054_s0_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr):
    _acc0 = tl.zeros([512], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 512) + tl.arange(0, 512)) < 576) & (((((tl.program_id(0) // 254) % 254) + ((((_lv0 * 512) + tl.arange(0, 512)) // 3) % 3)) < 256) & (((tl.program_id(0) % 254) + (((_lv0 * 512) + tl.arange(0, 512)) % 3)) < 256))), (tl.load(in0_ptr + ((((((((tl.program_id(0) // 4129024) * 64) + (((_lv0 * 512) + tl.arange(0, 512)) // 9)) * 256) + (((tl.program_id(0) // 254) % 254) + ((((_lv0 * 512) + tl.arange(0, 512)) // 3) % 3))) * 256) + ((tl.program_id(0) % 254) + (((_lv0 * 512) + tl.arange(0, 512)) % 3))) + 0 * tl.arange(0, 512)), mask=((((_lv0 * 512) + tl.arange(0, 512)) < 576) & (((((tl.program_id(0) // 254) % 254) + ((((_lv0 * 512) + tl.arange(0, 512)) // 3) % 3)) < 256) & (((tl.program_id(0) % 254) + (((_lv0 * 512) + tl.arange(0, 512)) % 3)) < 256))), other=0.0) * tl.load(in1_ptr + (((((((((tl.program_id(0) // 64516) % 64) * 64) + (((_lv0 * 512) + tl.arange(0, 512)) // 9)) * 3) + ((((_lv0 * 512) + tl.arange(0, 512)) // 3) % 3)) * 3) + (((_lv0 * 512) + tl.arange(0, 512)) % 3)) + 0 * tl.arange(0, 512)), mask=((((_lv0 * 512) + tl.arange(0, 512)) < 576) & (((((tl.program_id(0) // 254) % 254) + ((((_lv0 * 512) + tl.arange(0, 512)) // 3) % 3)) < 256) & (((tl.program_id(0) % 254) + (((_lv0 * 512) + tl.arange(0, 512)) % 3)) < 256))), other=0.0)), 0.0))
    _v = (tl.sum(_acc0, axis=0) + tl.load(in2_ptr + (((tl.program_id(0) // 64516) % 64))))
    tl.store(out_ptr + tl.program_id(0), _v)


def t054_s0(out, ins):
    grid = (264257536,)
    t054_s0_kernel[grid](out, ins[0], ins[1], ins[2], ins[3])
    return out


@triton.jit
def t054_s1_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr):
    _acc0 = tl.zeros([1], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), (tl.load(in4_ptr + ((((((((tl.program_id(0) // 4129024) * 64) + ((tl.program_id(0) // 64516) % 64)) * 254) + ((tl.program_id(0) // 254) % 254)) * 254) + (tl.program_id(0) % 254)) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) * tl.load(in3_ptr + (((tl.program_id(0) // 64516) % 64) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)), 0.0))
    _v = (((1.0 * (1.0 / 2.0)) * tl.where(tl.sum(_acc0, axis=0) <= (0.0 * (1.0 / 1.0)), ((1.0 * (1.0 / 100.0)) * tl.sum(_acc0, axis=0)), tl.sum(_acc0, axis=0))) * ((1.0 * (1.0 / 1.0)) + tl.erf((tl.where(tl.sum(_acc0, axis=0) <= (0.0 * (1.0 / 1.0)), ((1.0 * (1.0 / 100.0)) * tl.sum(_acc0, axis=0)), tl.sum(_acc0, axis=0)) * (1.0 / tl.sqrt((2.0 * (1.0 / 1.0))))))))
    tl.store(out_ptr + tl.program_id(0), _v)


def t054_s1(out, ins):
    grid = (264257536,)
    t054_s1_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4])
    return out


def t054(out, ins):
    _t0 = torch.empty(264257536, device=ins[0].device, dtype=torch.float32)
    t054_s0(_t0, list(ins))
    t054_s1(out, list(ins) + [_t0])
    return out
