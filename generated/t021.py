import torch
import triton
import triton.language as tl


@triton.jit
def _mul_combine(a, b):
    return a * b


@triton.jit
def t021_s0_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr):
    _acc0 = tl.zeros([64], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 64) + tl.arange(0, 64)) < 72) & (((((tl.program_id(0) // 254) % 254) + ((((_lv0 * 64) + tl.arange(0, 64)) // 3) % 3)) < 256) & (((tl.program_id(0) % 254) + (((_lv0 * 64) + tl.arange(0, 64)) % 3)) < 256))), (tl.load(in0_ptr + ((((((((tl.program_id(0) // 2064512) * 8) + (((_lv0 * 64) + tl.arange(0, 64)) // 9)) * 256) + (((tl.program_id(0) // 254) % 254) + ((((_lv0 * 64) + tl.arange(0, 64)) // 3) % 3))) * 256) + ((tl.program_id(0) % 254) + (((_lv0 * 64) + tl.arange(0, 64)) % 3))) + 0 * tl.arange(0, 64)), mask=((((_lv0 * 64) + tl.arange(0, 64)) < 72) & (((((tl.program_id(0) // 254) % 254) + ((((_lv0 * 64) + tl.arange(0, 64)) // 3) % 3)) < 256) & (((tl.program_id(0) % 254) + (((_lv0 * 64) + tl.arange(0, 64)) % 3)) < 256))), other=0.0) * tl.load(in1_ptr + (((((((((tl.program_id(0) // 64516) % 32) * 8) + (((_lv0 * 64) + tl.arange(0, 64)) // 9)) * 3) + ((((_lv0 * 64) + tl.arange(0, 64)) // 3) % 3)) * 3) + (((_lv0 * 64) + tl.arange(0, 64)) % 3)) + 0 * tl.arange(0, 64)), mask=((((_lv0 * 64) + tl.arange(0, 64)) < 72) & (((((tl.program_id(0) // 254) % 254) + ((((_lv0 * 64) + tl.arange(0, 64)) // 3) % 3)) < 256) & (((tl.program_id(0) % 254) + (((_lv0 * 64) + tl.arange(0, 64)) % 3)) < 256))), other=0.0)), 0.0))
    _v = (tl.sum(_acc0, axis=0) + tl.load(in2_ptr + (((tl.program_id(0) // 64516) % 32))))
    tl.store(out_ptr + tl.program_id(0), _v)


def t021_s0(out, ins):
    grid = (264257536,)
    t021_s0_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6])
    return out


@triton.jit
def t021_s1_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr):
    _acc0 = tl.zeros([1], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), (tl.load(in7_ptr + ((((((((tl.program_id(0) // 2064512) * 32) + ((tl.program_id(0) // 64516) % 32)) * 254) + ((tl.program_id(0) // 254) % 254)) * 254) + (tl.program_id(0) % 254)) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) + tl.load(in3_ptr + (((tl.program_id(0) // 64516) % 32) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t021_s1(out, ins):
    grid = (264257536,)
    t021_s1_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7])
    return out


@triton.jit
def t021_s2_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr):
    _acc0 = tl.zeros([1], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), (tl.load(in8_ptr + ((((((((tl.program_id(0) // 2064512) * 32) + ((tl.program_id(0) // 64516) % 32)) * 254) + ((tl.program_id(0) // 254) % 254)) * 254) + (tl.program_id(0) % 254)) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) * tl.load(in4_ptr + (((tl.program_id(0) // 64516) % 32) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)), 0.0))
    _v = (1.0 / ((1.0 * (1.0 / 1.0)) + tl.exp(((0.0 * (1.0 / 1.0)) - tl.sum(_acc0, axis=0)))))
    tl.store(out_ptr + tl.program_id(0), _v)


def t021_s2(out, ins):
    grid = (264257536,)
    t021_s2_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8])
    return out


@triton.jit
def t021_s3_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 253):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 258064) & True), tl.load(in9_ptr + (tl.maximum(((((((tl.program_id(0) // 8) * 32) + ((tl.program_id(0) % 8) * 4)) + (((_lv0 * 1024) + tl.arange(0, 1024)) // 64516)) * 64516) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 64516)) - tl.maximum(((((((tl.program_id(0) // 8) * 32) + ((tl.program_id(0) % 8) * 4)) + (((_lv0 * 1024) + tl.arange(0, 1024)) // 64516)) * 64516) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 64516)) - 264257535, 0), 0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 258064) & True), other=0.0), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t021_s3(out, ins):
    grid = (1024,)
    t021_s3_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9])
    return out


@triton.jit
def t021_s4_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 253):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 258064) & True), ((tl.load(in9_ptr + (tl.maximum(((((((tl.program_id(0) // 8) * 32) + ((tl.program_id(0) % 8) * 4)) + (((_lv0 * 1024) + tl.arange(0, 1024)) // 64516)) * 64516) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 64516)) - tl.maximum(((((((tl.program_id(0) // 8) * 32) + ((tl.program_id(0) % 8) * 4)) + (((_lv0 * 1024) + tl.arange(0, 1024)) // 64516)) * 64516) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 64516)) - 264257535, 0), 0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 258064) & True), other=0.0) - (tl.load(in10_ptr + (tl.program_id(0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 258064) & True), other=0.0) * (1.0 * (1.0 / 258064.0)))) * (tl.load(in9_ptr + (tl.maximum(((((((tl.program_id(0) // 8) * 32) + ((tl.program_id(0) % 8) * 4)) + (((_lv0 * 1024) + tl.arange(0, 1024)) // 64516)) * 64516) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 64516)) - tl.maximum(((((((tl.program_id(0) // 8) * 32) + ((tl.program_id(0) % 8) * 4)) + (((_lv0 * 1024) + tl.arange(0, 1024)) // 64516)) * 64516) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 64516)) - 264257535, 0), 0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 258064) & True), other=0.0) - (tl.load(in10_ptr + (tl.program_id(0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 258064) & True), other=0.0) * (1.0 * (1.0 / 258064.0))))), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t021_s4(out, ins):
    grid = (1024,)
    t021_s4_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10])
    return out


@triton.jit
def t021_s5_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr, in10_ptr, in11_ptr):
    _acc0 = tl.zeros([1], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), ((((tl.load(in9_ptr + (tl.program_id(0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) - (tl.load(in10_ptr + (tl.maximum((((tl.program_id(0) // 2064512) * 8) + (((tl.program_id(0) // 64516) % 32) // 4)) - tl.maximum((((tl.program_id(0) // 2064512) * 8) + (((tl.program_id(0) // 64516) % 32) // 4)) - 1023, 0), 0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) * (1.0 * (1.0 / 258064.0)))) * (1.0 / tl.sqrt(((tl.load(in11_ptr + (tl.maximum((((tl.program_id(0) // 2064512) * 8) + (((tl.program_id(0) // 64516) % 32) // 4)) - tl.maximum((((tl.program_id(0) // 2064512) * 8) + (((tl.program_id(0) // 64516) % 32) // 4)) - 1023, 0), 0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) * (1.0 * (1.0 / 258064.0))) + (1.0 * (1.0 / 100000.0)))))) * tl.load(in5_ptr + (((tl.program_id(0) // 64516) % 32) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)) + tl.load(in6_ptr + (((tl.program_id(0) // 64516) % 32) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t021_s5(out, ins):
    grid = (264257536,)
    t021_s5_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9], ins[10], ins[11])
    return out


def t021(out, ins):
    _t0 = torch.empty(264257536, device=ins[0].device, dtype=torch.float32)
    _t1 = torch.empty(264257536, device=ins[0].device, dtype=torch.float32)
    _t2 = torch.empty(264257536, device=ins[0].device, dtype=torch.float32)
    _t3 = torch.empty(1024, device=ins[0].device, dtype=torch.float32)
    _t4 = torch.empty(1024, device=ins[0].device, dtype=torch.float32)
    t021_s0(_t0, list(ins))
    t021_s1(_t1, list(ins) + [_t0])
    t021_s2(_t2, list(ins) + [_t0, _t1])
    t021_s3(_t3, list(ins) + [_t0, _t1, _t2])
    t021_s4(_t4, list(ins) + [_t0, _t1, _t2, _t3])
    t021_s5(out, list(ins) + [_t0, _t1, _t2, _t3, _t4])
    return out
