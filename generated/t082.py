import torch
import triton
import triton.language as tl


@triton.jit
def _mul_combine(a, b):
    return a * b


@triton.jit
def t082_s0_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr):
    _acc0 = tl.zeros([64], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 64) + tl.arange(0, 64)) < 72) & (((((tl.program_id(0) // 254) % 254) + ((((_lv0 * 64) + tl.arange(0, 64)) // 3) % 3)) < 256) & (((tl.program_id(0) % 254) + (((_lv0 * 64) + tl.arange(0, 64)) % 3)) < 256))), (tl.load(in0_ptr + ((((((((tl.program_id(0) // 4129024) * 8) + (((_lv0 * 64) + tl.arange(0, 64)) // 9)) * 256) + (((tl.program_id(0) // 254) % 254) + ((((_lv0 * 64) + tl.arange(0, 64)) // 3) % 3))) * 256) + ((tl.program_id(0) % 254) + (((_lv0 * 64) + tl.arange(0, 64)) % 3))) + 0 * tl.arange(0, 64)), mask=((((_lv0 * 64) + tl.arange(0, 64)) < 72) & (((((tl.program_id(0) // 254) % 254) + ((((_lv0 * 64) + tl.arange(0, 64)) // 3) % 3)) < 256) & (((tl.program_id(0) % 254) + (((_lv0 * 64) + tl.arange(0, 64)) % 3)) < 256))), other=0.0) * tl.load(in1_ptr + (((((((((tl.program_id(0) // 64516) % 64) * 8) + (((_lv0 * 64) + tl.arange(0, 64)) // 9)) * 3) + ((((_lv0 * 64) + tl.arange(0, 64)) // 3) % 3)) * 3) + (((_lv0 * 64) + tl.arange(0, 64)) % 3)) + 0 * tl.arange(0, 64)), mask=((((_lv0 * 64) + tl.arange(0, 64)) < 72) & (((((tl.program_id(0) // 254) % 254) + ((((_lv0 * 64) + tl.arange(0, 64)) // 3) % 3)) < 256) & (((tl.program_id(0) % 254) + (((_lv0 * 64) + tl.arange(0, 64)) % 3)) < 256))), other=0.0)), 0.0))
    _v = ((2.0 * tl.sigmoid(2.0 * ((tl.sum(_acc0, axis=0) + tl.load(in2_ptr + (((tl.program_id(0) // 64516) % 64)))))) - 1.0) * (2.0 * (1.0 / 1.0)))
    tl.store(out_ptr + tl.program_id(0), _v)


def t082_s0(out, ins):
    grid = (528515072,)
    t082_s0_kernel[grid](out, ins[0], ins[1], ins[2], ins[3])
    return out


@triton.jit
def t082_s1_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr):
    _acc0 = tl.zeros([1], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), (tl.load(in4_ptr + ((((((((tl.program_id(0) // 4129024) * 64) + ((tl.program_id(0) // 64516) % 64)) * 254) + ((tl.program_id(0) // 254) % 254)) * 254) + (tl.program_id(0) % 254)) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) + tl.load(in3_ptr + (((tl.program_id(0) // 64516) % 64) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0)), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t082_s1(out, ins):
    grid = (528515072,)
    t082_s1_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4])
    return out


@triton.jit
def t082_s2_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr, in5_ptr):
    _acc0 = tl.zeros([16], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = tl.maximum(_acc0, tl.load(in5_ptr + ((((((((tl.program_id(0) // 254016) * 64) + ((tl.program_id(0) // 3969) % 64)) * 254) + tl.maximum(((((tl.program_id(0) // 63) % 63) * 4) + tl.maximum(((tl.maximum(((_lv0 * 16) + tl.arange(0, 16)) - tl.maximum(((_lv0 * 16) + tl.arange(0, 16)) - 15, 0), 0) // 4) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 63) % 63) * 4), 0) - (tl.maximum(((_lv0 * 16) + tl.arange(0, 16)) - tl.maximum(((_lv0 * 16) + tl.arange(0, 16)) - 15, 0), 0) // 4), 0)) - tl.maximum(((tl.maximum(((_lv0 * 16) + tl.arange(0, 16)) - tl.maximum(((_lv0 * 16) + tl.arange(0, 16)) - 15, 0), 0) // 4) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 63) % 63) * 4), 0) - (tl.maximum(((_lv0 * 16) + tl.arange(0, 16)) - tl.maximum(((_lv0 * 16) + tl.arange(0, 16)) - 15, 0), 0) // 4), 0)) - tl.maximum(253 - (((tl.program_id(0) // 63) % 63) * 4), 0), 0), 0)) - tl.maximum(((((tl.program_id(0) // 63) % 63) * 4) + tl.maximum(((tl.maximum(((_lv0 * 16) + tl.arange(0, 16)) - tl.maximum(((_lv0 * 16) + tl.arange(0, 16)) - 15, 0), 0) // 4) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 63) % 63) * 4), 0) - (tl.maximum(((_lv0 * 16) + tl.arange(0, 16)) - tl.maximum(((_lv0 * 16) + tl.arange(0, 16)) - 15, 0), 0) // 4), 0)) - tl.maximum(((tl.maximum(((_lv0 * 16) + tl.arange(0, 16)) - tl.maximum(((_lv0 * 16) + tl.arange(0, 16)) - 15, 0), 0) // 4) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 63) % 63) * 4), 0) - (tl.maximum(((_lv0 * 16) + tl.arange(0, 16)) - tl.maximum(((_lv0 * 16) + tl.arange(0, 16)) - 15, 0), 0) // 4), 0)) - tl.maximum(253 - (((tl.program_id(0) // 63) % 63) * 4), 0), 0), 0)) - 253, 0), 0)) * 254) + tl.maximum((((tl.program_id(0) % 63) * 4) + tl.maximum(((tl.maximum(((_lv0 * 16) + tl.arange(0, 16)) - tl.maximum(((_lv0 * 16) + tl.arange(0, 16)) - 15, 0), 0) % 4) + tl.maximum(tl.maximum(0 - ((tl.program_id(0) % 63) * 4), 0) - (tl.maximum(((_lv0 * 16) + tl.arange(0, 16)) - tl.maximum(((_lv0 * 16) + tl.arange(0, 16)) - 15, 0), 0) % 4), 0)) - tl.maximum(((tl.maximum(((_lv0 * 16) + tl.arange(0, 16)) - tl.maximum(((_lv0 * 16) + tl.arange(0, 16)) - 15, 0), 0) % 4) + tl.maximum(tl.maximum(0 - ((tl.program_id(0) % 63) * 4), 0) - (tl.maximum(((_lv0 * 16) + tl.arange(0, 16)) - tl.maximum(((_lv0 * 16) + tl.arange(0, 16)) - 15, 0), 0) % 4), 0)) - tl.maximum(253 - ((tl.program_id(0) % 63) * 4), 0), 0), 0)) - tl.maximum((((tl.program_id(0) % 63) * 4) + tl.maximum(((tl.maximum(((_lv0 * 16) + tl.arange(0, 16)) - tl.maximum(((_lv0 * 16) + tl.arange(0, 16)) - 15, 0), 0) % 4) + tl.maximum(tl.maximum(0 - ((tl.program_id(0) % 63) * 4), 0) - (tl.maximum(((_lv0 * 16) + tl.arange(0, 16)) - tl.maximum(((_lv0 * 16) + tl.arange(0, 16)) - 15, 0), 0) % 4), 0)) - tl.maximum(((tl.maximum(((_lv0 * 16) + tl.arange(0, 16)) - tl.maximum(((_lv0 * 16) + tl.arange(0, 16)) - 15, 0), 0) % 4) + tl.maximum(tl.maximum(0 - ((tl.program_id(0) % 63) * 4), 0) - (tl.maximum(((_lv0 * 16) + tl.arange(0, 16)) - tl.maximum(((_lv0 * 16) + tl.arange(0, 16)) - 15, 0), 0) % 4), 0)) - tl.maximum(253 - ((tl.program_id(0) % 63) * 4), 0), 0), 0)) - 253, 0), 0)))))
    _v = tl.max(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t082_s2(out, ins):
    grid = (32514048,)
    t082_s2_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4], ins[5])
    return out


def t082(out, ins):
    _t0 = torch.empty(528515072, device=ins[0].device, dtype=torch.float32)
    _t1 = torch.empty(528515072, device=ins[0].device, dtype=torch.float32)
    t082_s0(_t0, list(ins))
    t082_s1(_t1, list(ins) + [_t0])
    t082_s2(out, list(ins) + [_t0, _t1])
    return out
