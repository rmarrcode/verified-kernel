import torch
import triton
import triton.language as tl


@triton.jit
def _mul_combine(a, b):
    return a * b


@triton.jit
def t074_s0_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr):
    _acc0 = tl.zeros([256], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 256) + tl.arange(0, 256)) < 432) & (((((((((((((_lv0 * 256) + tl.arange(0, 256)) // 9) % 3) <= (((tl.program_id(0) // 4096) % 32) + 1)) & ((tl.maximum((((tl.program_id(0) // 4096) % 32) + 1) - ((((_lv0 * 256) + tl.arange(0, 256)) // 9) % 3), 0) % 2) == 0)) & ((tl.maximum((((tl.program_id(0) // 4096) % 32) + 1) - ((((_lv0 * 256) + tl.arange(0, 256)) // 9) % 3), 0) // 2) < 16)) & (((((_lv0 * 256) + tl.arange(0, 256)) // 3) % 3) <= (((tl.program_id(0) // 64) % 64) + 1))) & ((tl.maximum((((tl.program_id(0) // 64) % 64) + 1) - ((((_lv0 * 256) + tl.arange(0, 256)) // 3) % 3), 0) % 2) == 0)) & ((tl.maximum((((tl.program_id(0) // 64) % 64) + 1) - ((((_lv0 * 256) + tl.arange(0, 256)) // 3) % 3), 0) // 2) < 32)) & ((((_lv0 * 256) + tl.arange(0, 256)) % 3) <= ((tl.program_id(0) % 64) + 1))) & ((tl.maximum(((tl.program_id(0) % 64) + 1) - (((_lv0 * 256) + tl.arange(0, 256)) % 3), 0) % 2) == 0)) & ((tl.maximum(((tl.program_id(0) % 64) + 1) - (((_lv0 * 256) + tl.arange(0, 256)) % 3), 0) // 2) < 32))), (tl.load(in0_ptr + ((((((((((tl.program_id(0) // 4194304) * 16) + (((((tl.program_id(0) // 131072) % 32) // 32) * 16) + (((_lv0 * 256) + tl.arange(0, 256)) // 27))) * 16) + (tl.maximum((((tl.program_id(0) // 4096) % 32) + 1) - ((((_lv0 * 256) + tl.arange(0, 256)) // 9) % 3), 0) // 2)) * 32) + (tl.maximum((((tl.program_id(0) // 64) % 64) + 1) - ((((_lv0 * 256) + tl.arange(0, 256)) // 3) % 3), 0) // 2)) * 32) + (tl.maximum(((tl.program_id(0) % 64) + 1) - (((_lv0 * 256) + tl.arange(0, 256)) % 3), 0) // 2)) + 0 * tl.arange(0, 256)), mask=((((_lv0 * 256) + tl.arange(0, 256)) < 432) & (((((((((((((_lv0 * 256) + tl.arange(0, 256)) // 9) % 3) <= (((tl.program_id(0) // 4096) % 32) + 1)) & ((tl.maximum((((tl.program_id(0) // 4096) % 32) + 1) - ((((_lv0 * 256) + tl.arange(0, 256)) // 9) % 3), 0) % 2) == 0)) & ((tl.maximum((((tl.program_id(0) // 4096) % 32) + 1) - ((((_lv0 * 256) + tl.arange(0, 256)) // 9) % 3), 0) // 2) < 16)) & (((((_lv0 * 256) + tl.arange(0, 256)) // 3) % 3) <= (((tl.program_id(0) // 64) % 64) + 1))) & ((tl.maximum((((tl.program_id(0) // 64) % 64) + 1) - ((((_lv0 * 256) + tl.arange(0, 256)) // 3) % 3), 0) % 2) == 0)) & ((tl.maximum((((tl.program_id(0) // 64) % 64) + 1) - ((((_lv0 * 256) + tl.arange(0, 256)) // 3) % 3), 0) // 2) < 32)) & ((((_lv0 * 256) + tl.arange(0, 256)) % 3) <= ((tl.program_id(0) % 64) + 1))) & ((tl.maximum(((tl.program_id(0) % 64) + 1) - (((_lv0 * 256) + tl.arange(0, 256)) % 3), 0) % 2) == 0)) & ((tl.maximum(((tl.program_id(0) % 64) + 1) - (((_lv0 * 256) + tl.arange(0, 256)) % 3), 0) // 2) < 32))), other=0.0) * tl.load(in1_ptr + ((((((((((((((tl.program_id(0) // 131072) % 32) // 32) * 16) + (((_lv0 * 256) + tl.arange(0, 256)) // 27)) * 32) + (((tl.program_id(0) // 131072) % 32) % 32)) * 3) + ((((_lv0 * 256) + tl.arange(0, 256)) // 9) % 3)) * 3) + ((((_lv0 * 256) + tl.arange(0, 256)) // 3) % 3)) * 3) + (((_lv0 * 256) + tl.arange(0, 256)) % 3)) + 0 * tl.arange(0, 256)), mask=((((_lv0 * 256) + tl.arange(0, 256)) < 432) & (((((((((((((_lv0 * 256) + tl.arange(0, 256)) // 9) % 3) <= (((tl.program_id(0) // 4096) % 32) + 1)) & ((tl.maximum((((tl.program_id(0) // 4096) % 32) + 1) - ((((_lv0 * 256) + tl.arange(0, 256)) // 9) % 3), 0) % 2) == 0)) & ((tl.maximum((((tl.program_id(0) // 4096) % 32) + 1) - ((((_lv0 * 256) + tl.arange(0, 256)) // 9) % 3), 0) // 2) < 16)) & (((((_lv0 * 256) + tl.arange(0, 256)) // 3) % 3) <= (((tl.program_id(0) // 64) % 64) + 1))) & ((tl.maximum((((tl.program_id(0) // 64) % 64) + 1) - ((((_lv0 * 256) + tl.arange(0, 256)) // 3) % 3), 0) % 2) == 0)) & ((tl.maximum((((tl.program_id(0) // 64) % 64) + 1) - ((((_lv0 * 256) + tl.arange(0, 256)) // 3) % 3), 0) // 2) < 32)) & ((((_lv0 * 256) + tl.arange(0, 256)) % 3) <= ((tl.program_id(0) % 64) + 1))) & ((tl.maximum(((tl.program_id(0) % 64) + 1) - (((_lv0 * 256) + tl.arange(0, 256)) % 3), 0) % 2) == 0)) & ((tl.maximum(((tl.program_id(0) % 64) + 1) - (((_lv0 * 256) + tl.arange(0, 256)) % 3), 0) // 2) < 32))), other=0.0)), 0.0))
    _v = tl.where((tl.sum(_acc0, axis=0) + tl.load(in2_ptr + (((tl.program_id(0) // 131072) % 32)))) <= (0.0 * (1.0 / 1.0)), ((1.0 * (1.0 / 5.0)) * (tl.sum(_acc0, axis=0) + tl.load(in2_ptr + (((tl.program_id(0) // 131072) % 32))))), (tl.sum(_acc0, axis=0) + tl.load(in2_ptr + (((tl.program_id(0) // 131072) % 32)))))
    tl.store(out_ptr + tl.program_id(0), _v)


def t074_s0(out, ins):
    grid = (67108864,)
    t074_s0_kernel[grid](out, ins[0], ins[1], ins[2], ins[3])
    return out


@triton.jit
def t074_s1_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr):
    _acc0 = tl.zeros([1], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), (tl.load(in4_ptr + ((((((((((tl.program_id(0) // 4194304) * 32) + ((tl.program_id(0) // 131072) % 32)) * 32) + ((tl.program_id(0) // 4096) % 32)) * 64) + ((tl.program_id(0) // 64) % 64)) * 64) + (tl.program_id(0) % 64)) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) * tl.load(in3_ptr + (((tl.program_id(0) // 131072) % 32) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)), 0.0))
    _v = tl.where(tl.sum(_acc0, axis=0) <= (0.0 * (1.0 / 1.0)), ((1.0 * (1.0 / 5.0)) * tl.sum(_acc0, axis=0)), tl.sum(_acc0, axis=0))
    tl.store(out_ptr + tl.program_id(0), _v)


def t074_s1(out, ins):
    grid = (67108864,)
    t074_s1_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4])
    return out


@triton.jit
def t074_s2_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr):
    _acc0 = tl.zeros([8], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = tl.maximum(_acc0, tl.load(in5_ptr + ((((((((((tl.program_id(0) // 524288) * 32) + ((tl.program_id(0) // 16384) % 32)) * 32) + tl.maximum(((((tl.program_id(0) // 1024) % 16) * 2) + tl.maximum(((tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) // 4) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 1024) % 16) * 2), 0) - (tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) // 4), 0)) - tl.maximum(((tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) // 4) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 1024) % 16) * 2), 0) - (tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) // 4), 0)) - tl.maximum(31 - (((tl.program_id(0) // 1024) % 16) * 2), 0), 0), 0)) - tl.maximum(((((tl.program_id(0) // 1024) % 16) * 2) + tl.maximum(((tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) // 4) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 1024) % 16) * 2), 0) - (tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) // 4), 0)) - tl.maximum(((tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) // 4) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 1024) % 16) * 2), 0) - (tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) // 4), 0)) - tl.maximum(31 - (((tl.program_id(0) // 1024) % 16) * 2), 0), 0), 0)) - 31, 0), 0)) * 64) + tl.maximum(((((tl.program_id(0) // 32) % 32) * 2) + tl.maximum((((tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) // 2) % 2) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 32) % 32) * 2), 0) - ((tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) // 2) % 2), 0)) - tl.maximum((((tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) // 2) % 2) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 32) % 32) * 2), 0) - ((tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) // 2) % 2), 0)) - tl.maximum(63 - (((tl.program_id(0) // 32) % 32) * 2), 0), 0), 0)) - tl.maximum(((((tl.program_id(0) // 32) % 32) * 2) + tl.maximum((((tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) // 2) % 2) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 32) % 32) * 2), 0) - ((tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) // 2) % 2), 0)) - tl.maximum((((tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) // 2) % 2) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 32) % 32) * 2), 0) - ((tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) // 2) % 2), 0)) - tl.maximum(63 - (((tl.program_id(0) // 32) % 32) * 2), 0), 0), 0)) - 63, 0), 0)) * 64) + tl.maximum((((tl.program_id(0) % 32) * 2) + tl.maximum(((tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) % 2) + tl.maximum(tl.maximum(0 - ((tl.program_id(0) % 32) * 2), 0) - (tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) % 2), 0)) - tl.maximum(((tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) % 2) + tl.maximum(tl.maximum(0 - ((tl.program_id(0) % 32) * 2), 0) - (tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) % 2), 0)) - tl.maximum(63 - ((tl.program_id(0) % 32) * 2), 0), 0), 0)) - tl.maximum((((tl.program_id(0) % 32) * 2) + tl.maximum(((tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) % 2) + tl.maximum(tl.maximum(0 - ((tl.program_id(0) % 32) * 2), 0) - (tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) % 2), 0)) - tl.maximum(((tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) % 2) + tl.maximum(tl.maximum(0 - ((tl.program_id(0) % 32) * 2), 0) - (tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) % 2), 0)) - tl.maximum(63 - ((tl.program_id(0) % 32) * 2), 0), 0), 0)) - 63, 0), 0)))))
    _v = tl.max(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t074_s2(out, ins):
    grid = (8388608,)
    t074_s2_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5])
    return out


def t074(out, ins):
    _t0 = torch.empty(67108864, device=ins[0].device, dtype=torch.float32)
    _t1 = torch.empty(67108864, device=ins[0].device, dtype=torch.float32)
    t074_s0(_t0, list(ins))
    t074_s1(_t1, list(ins) + [_t0])
    t074_s2(out, list(ins) + [_t0, _t1])
    return out
