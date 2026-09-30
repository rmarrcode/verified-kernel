import torch
import triton
import triton.language as tl


@triton.jit
def _mul_combine(a, b):
    return a * b


@triton.jit
def t017_s0_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr):
    _acc0 = tl.zeros([512], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 512) + tl.arange(0, 512)) < 576) & (((((tl.program_id(0) // 126) % 126) + ((((_lv0 * 512) + tl.arange(0, 512)) // 3) % 3)) < 128) & (((tl.program_id(0) % 126) + (((_lv0 * 512) + tl.arange(0, 512)) % 3)) < 128))), (tl.load(in0_ptr + ((((((((tl.program_id(0) // 2032128) * 64) + (((_lv0 * 512) + tl.arange(0, 512)) // 9)) * 128) + (((tl.program_id(0) // 126) % 126) + ((((_lv0 * 512) + tl.arange(0, 512)) // 3) % 3))) * 128) + ((tl.program_id(0) % 126) + (((_lv0 * 512) + tl.arange(0, 512)) % 3))) + 0 * tl.arange(0, 512)), mask=((((_lv0 * 512) + tl.arange(0, 512)) < 576) & (((((tl.program_id(0) // 126) % 126) + ((((_lv0 * 512) + tl.arange(0, 512)) // 3) % 3)) < 128) & (((tl.program_id(0) % 126) + (((_lv0 * 512) + tl.arange(0, 512)) % 3)) < 128))), other=0.0) * tl.load(in1_ptr + (((((((((tl.program_id(0) // 15876) % 128) * 64) + (((_lv0 * 512) + tl.arange(0, 512)) // 9)) * 3) + ((((_lv0 * 512) + tl.arange(0, 512)) // 3) % 3)) * 3) + (((_lv0 * 512) + tl.arange(0, 512)) % 3)) + 0 * tl.arange(0, 512)), mask=((((_lv0 * 512) + tl.arange(0, 512)) < 576) & (((((tl.program_id(0) // 126) % 126) + ((((_lv0 * 512) + tl.arange(0, 512)) // 3) % 3)) < 128) & (((tl.program_id(0) % 126) + (((_lv0 * 512) + tl.arange(0, 512)) % 3)) < 128))), other=0.0)), 0.0))
    _v = (tl.sum(_acc0, axis=0) + tl.load(in2_ptr + (((tl.program_id(0) // 15876) % 128))))
    tl.store(out_ptr + tl.program_id(0), _v)


def t017_s0(out, ins):
    grid = (130056192,)
    t017_s0_kernel[grid](out, ins[0], ins[1], ins[2])
    return out


@triton.jit
def t017_s1_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 16):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 15876) & True), tl.load(in3_ptr + (((tl.program_id(0) * 15876) + ((_lv0 * 1024) + tl.arange(0, 1024))) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 15876) & True), other=0.0), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t017_s1(out, ins):
    grid = (8192,)
    t017_s1_kernel[grid](out, ins[0], ins[1], ins[2], ins[3])
    return out


@triton.jit
def t017_s2_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 16):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 15876) & True), ((tl.load(in3_ptr + (((tl.program_id(0) * 15876) + ((_lv0 * 1024) + tl.arange(0, 1024))) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 15876) & True), other=0.0) - (tl.load(in4_ptr + (tl.program_id(0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 15876) & True), other=0.0) * (1.0 * (1.0 / 15876.0)))) * (tl.load(in3_ptr + (((tl.program_id(0) * 15876) + ((_lv0 * 1024) + tl.arange(0, 1024))) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 15876) & True), other=0.0) - (tl.load(in4_ptr + (tl.program_id(0) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 15876) & True), other=0.0) * (1.0 * (1.0 / 15876.0))))), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t017_s2(out, ins):
    grid = (8192,)
    t017_s2_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4])
    return out


@triton.jit
def t017_s3_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr):
    _acc0 = tl.zeros([1], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), ((tl.load(in3_ptr + (tl.program_id(0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) - (tl.load(in4_ptr + (tl.maximum((tl.program_id(0) // 15876) - tl.maximum((tl.program_id(0) // 15876) - 8191, 0), 0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) * (1.0 * (1.0 / 15876.0)))) * (1.0 / tl.sqrt(((tl.load(in5_ptr + (tl.maximum((tl.program_id(0) // 15876) - tl.maximum((tl.program_id(0) // 15876) - 8191, 0), 0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) * (1.0 * (1.0 / 15876.0))) + (1.0 * (1.0 / 100000.0)))))), 0.0))
    _v = (tl.sum(_acc0, axis=0) / (2.0 * (1.0 / 1.0)))
    tl.store(out_ptr + tl.program_id(0), _v)


def t017_s3(out, ins):
    grid = (130056192,)
    t017_s3_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5])
    return out


def t017(out, ins):
    _t0 = torch.empty(130056192, device=ins[0].device, dtype=torch.float32)
    _t1 = torch.empty(8192, device=ins[0].device, dtype=torch.float32)
    _t2 = torch.empty(8192, device=ins[0].device, dtype=torch.float32)
    t017_s0(_t0, list(ins))
    t017_s1(_t1, list(ins) + [_t0])
    t017_s2(_t2, list(ins) + [_t0, _t1])
    t017_s3(out, list(ins) + [_t0, _t1, _t2])
    return out
