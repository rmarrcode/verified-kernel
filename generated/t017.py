import torch
import triton
import triton.language as tl


@triton.jit
def _mul_combine(a, b):
    return a * b


@triton.jit
def t017_s0_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr):
    _acc0 = tl.zeros([2], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 2) + tl.arange(0, 2)) < 3) & ((((tl.program_id(0) // 256) % 256) < 256) & ((tl.program_id(0) % 256) < 256))), (tl.load(in0_ptr + ((((((((tl.program_id(0) // 393216) * 3) + ((_lv0 * 2) + tl.arange(0, 2))) * 256) + ((tl.program_id(0) // 256) % 256)) * 256) + (tl.program_id(0) % 256)) + 0 * tl.arange(0, 2)), mask=((((_lv0 * 2) + tl.arange(0, 2)) < 3) & ((((tl.program_id(0) // 256) % 256) < 256) & ((tl.program_id(0) % 256) < 256))), other=0.0) * tl.load(in1_ptr + (((((tl.program_id(0) // 65536) % 6) * 3) + ((_lv0 * 2) + tl.arange(0, 2))) + 0 * tl.arange(0, 2)), mask=((((_lv0 * 2) + tl.arange(0, 2)) < 3) & ((((tl.program_id(0) // 256) % 256) < 256) & ((tl.program_id(0) % 256) < 256))), other=0.0)), 0.0))
    _v = tl.maximum((tl.sum(_acc0, axis=0) + tl.load(in2_ptr + (((tl.program_id(0) // 65536) % 6)))), (0.0 * (1.0 / 1.0)))
    tl.store(out_ptr + tl.program_id(0), _v)


def t017_s0(out, ins):
    grid = (25165824,)
    t017_s0_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6])
    return out


@triton.jit
def t017_s1_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr):
    _acc0 = tl.zeros([4], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 4) + tl.arange(0, 4)) < 6) & ((((tl.program_id(0) // 256) % 256) < 256) & ((tl.program_id(0) % 256) < 256))), (tl.load(in7_ptr + ((((((((tl.program_id(0) // 4194304) * 6) + ((_lv0 * 4) + tl.arange(0, 4))) * 256) + ((tl.program_id(0) // 256) % 256)) * 256) + (tl.program_id(0) % 256)) + 0 * tl.arange(0, 4)), mask=((((_lv0 * 4) + tl.arange(0, 4)) < 6) & ((((tl.program_id(0) // 256) % 256) < 256) & ((tl.program_id(0) % 256) < 256))), other=0.0) * tl.load(in3_ptr + (((((tl.program_id(0) // 65536) % 64) * 6) + ((_lv0 * 4) + tl.arange(0, 4))) + 0 * tl.arange(0, 4)), mask=((((_lv0 * 4) + tl.arange(0, 4)) < 6) & ((((tl.program_id(0) // 256) % 256) < 256) & ((tl.program_id(0) % 256) < 256))), other=0.0)), 0.0))
    _v = tl.maximum((tl.sum(_acc0, axis=0) + tl.load(in4_ptr + (((tl.program_id(0) // 65536) % 64)))), (0.0 * (1.0 / 1.0)))
    tl.store(out_ptr + tl.program_id(0), _v)


def t017_s1(out, ins):
    grid = (268435456,)
    t017_s1_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7])
    return out


@triton.jit
def t017_s2_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr):
    _acc0 = tl.zeros([32], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 32) + tl.arange(0, 32)) < 54) & ((((1 <= (((tl.program_id(0) // 256) % 256) + ((((_lv0 * 32) + tl.arange(0, 32)) // 3) % 3))) & ((((tl.program_id(0) // 256) % 256) + ((((_lv0 * 32) + tl.arange(0, 32)) // 3) % 3)) < 257)) & (1 <= ((tl.program_id(0) % 256) + (((_lv0 * 32) + tl.arange(0, 32)) % 3)))) & (((tl.program_id(0) % 256) + (((_lv0 * 32) + tl.arange(0, 32)) % 3)) < 257))), (tl.load(in7_ptr + (tl.maximum((((((((tl.program_id(0) // 4194304) * 6) + (((_lv0 * 32) + tl.arange(0, 32)) // 9)) * 256) + tl.maximum((((tl.program_id(0) // 256) % 256) + ((((_lv0 * 32) + tl.arange(0, 32)) // 3) % 3)) - 1, 0)) * 256) + tl.maximum(((tl.program_id(0) % 256) + (((_lv0 * 32) + tl.arange(0, 32)) % 3)) - 1, 0)) - tl.maximum((((((((tl.program_id(0) // 4194304) * 6) + (((_lv0 * 32) + tl.arange(0, 32)) // 9)) * 256) + tl.maximum((((tl.program_id(0) // 256) % 256) + ((((_lv0 * 32) + tl.arange(0, 32)) // 3) % 3)) - 1, 0)) * 256) + tl.maximum(((tl.program_id(0) % 256) + (((_lv0 * 32) + tl.arange(0, 32)) % 3)) - 1, 0)) - 25165823, 0), 0) + 0 * tl.arange(0, 32)), mask=((((_lv0 * 32) + tl.arange(0, 32)) < 54) & ((((1 <= (((tl.program_id(0) // 256) % 256) + ((((_lv0 * 32) + tl.arange(0, 32)) // 3) % 3))) & ((((tl.program_id(0) // 256) % 256) + ((((_lv0 * 32) + tl.arange(0, 32)) // 3) % 3)) < 257)) & (1 <= ((tl.program_id(0) % 256) + (((_lv0 * 32) + tl.arange(0, 32)) % 3)))) & (((tl.program_id(0) % 256) + (((_lv0 * 32) + tl.arange(0, 32)) % 3)) < 257))), other=0.0) * tl.load(in5_ptr + (((((((((tl.program_id(0) // 65536) % 64) * 6) + (((_lv0 * 32) + tl.arange(0, 32)) // 9)) * 3) + ((((_lv0 * 32) + tl.arange(0, 32)) // 3) % 3)) * 3) + (((_lv0 * 32) + tl.arange(0, 32)) % 3)) + 0 * tl.arange(0, 32)), mask=((((_lv0 * 32) + tl.arange(0, 32)) < 54) & ((((1 <= (((tl.program_id(0) // 256) % 256) + ((((_lv0 * 32) + tl.arange(0, 32)) // 3) % 3))) & ((((tl.program_id(0) // 256) % 256) + ((((_lv0 * 32) + tl.arange(0, 32)) // 3) % 3)) < 257)) & (1 <= ((tl.program_id(0) % 256) + (((_lv0 * 32) + tl.arange(0, 32)) % 3)))) & (((tl.program_id(0) % 256) + (((_lv0 * 32) + tl.arange(0, 32)) % 3)) < 257))), other=0.0)), 0.0))
    _v = tl.maximum((tl.sum(_acc0, axis=0) + tl.load(in6_ptr + (((tl.program_id(0) // 65536) % 64)))), (0.0 * (1.0 / 1.0)))
    tl.store(out_ptr + tl.program_id(0), _v)


def t017_s2(out, ins):
    grid = (268435456,)
    t017_s2_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8])
    return out


@triton.jit
def t017_s3_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr, in6_ptr, in7_ptr, in8_ptr, in9_ptr):
    _acc0 = tl.zeros([2], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 2) + tl.arange(0, 2)) < 2) & ((((((_lv0 * 2) + tl.arange(0, 2)) == 0) & (0 <= ((tl.program_id(0) // 65536) % 128))) & (((tl.program_id(0) // 65536) % 128) < 64)) | (((((_lv0 * 2) + tl.arange(0, 2)) == 1) & (64 <= ((tl.program_id(0) // 65536) % 128))) & (((tl.program_id(0) // 65536) % 128) < 128)))), tl.where((((_lv0 * 2) + tl.arange(0, 2))).to(tl.float32) <= (1.0 * (1.0 / 2.0)), tl.load(in8_ptr + (tl.maximum((((((((tl.program_id(0) // 8388608) * 64) + ((tl.program_id(0) // 65536) % 128)) * 256) + ((tl.program_id(0) // 256) % 256)) * 256) + (tl.program_id(0) % 256)) - tl.maximum((((((((tl.program_id(0) // 8388608) * 64) + ((tl.program_id(0) // 65536) % 128)) * 256) + ((tl.program_id(0) // 256) % 256)) * 256) + (tl.program_id(0) % 256)) - 268435455, 0), 0) + 0 * tl.arange(0, 2)), mask=((((_lv0 * 2) + tl.arange(0, 2)) < 2) & ((((((_lv0 * 2) + tl.arange(0, 2)) == 0) & (0 <= ((tl.program_id(0) // 65536) % 128))) & (((tl.program_id(0) // 65536) % 128) < 64)) | (((((_lv0 * 2) + tl.arange(0, 2)) == 1) & (64 <= ((tl.program_id(0) // 65536) % 128))) & (((tl.program_id(0) // 65536) % 128) < 128)))), other=0.0), tl.load(in9_ptr + (tl.maximum((((((((tl.program_id(0) // 8388608) * 64) + tl.maximum(((tl.program_id(0) // 65536) % 128) - 64, 0)) * 256) + ((tl.program_id(0) // 256) % 256)) * 256) + (tl.program_id(0) % 256)) - tl.maximum((((((((tl.program_id(0) // 8388608) * 64) + tl.maximum(((tl.program_id(0) // 65536) % 128) - 64, 0)) * 256) + ((tl.program_id(0) // 256) % 256)) * 256) + (tl.program_id(0) % 256)) - 268435455, 0), 0) + 0 * tl.arange(0, 2)), mask=((((_lv0 * 2) + tl.arange(0, 2)) < 2) & ((((((_lv0 * 2) + tl.arange(0, 2)) == 0) & (0 <= ((tl.program_id(0) // 65536) % 128))) & (((tl.program_id(0) // 65536) % 128) < 64)) | (((((_lv0 * 2) + tl.arange(0, 2)) == 1) & (64 <= ((tl.program_id(0) // 65536) % 128))) & (((tl.program_id(0) // 65536) % 128) < 128)))), other=0.0)), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t017_s3(out, ins):
    grid = (536870912,)
    t017_s3_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5], ins[6], ins[7], ins[8], ins[9])
    return out


def t017(out, ins):
    _t0 = torch.empty(25165824, device=ins[0].device, dtype=torch.float32)
    _t1 = torch.empty(268435456, device=ins[0].device, dtype=torch.float32)
    _t2 = torch.empty(268435456, device=ins[0].device, dtype=torch.float32)
    t017_s0(_t0, list(ins))
    t017_s1(_t1, list(ins) + [_t0])
    t017_s2(_t2, list(ins) + [_t0, _t1])
    t017_s3(out, list(ins) + [_t0, _t1, _t2])
    return out
