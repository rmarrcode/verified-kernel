import torch
import triton
import triton.language as tl


@triton.jit
def _mul_combine(a, b):
    return a * b


@triton.jit
def t035_s0_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr):
    _acc0 = tl.zeros([512], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 512) + tl.arange(0, 512)) < 576) & (((((tl.program_id(0) // 126) % 126) + ((((_lv0 * 512) + tl.arange(0, 512)) // 3) % 3)) < 128) & (((tl.program_id(0) % 126) + (((_lv0 * 512) + tl.arange(0, 512)) % 3)) < 128))), (tl.load(in0_ptr + ((((((((tl.program_id(0) // 2032128) * 64) + (((_lv0 * 512) + tl.arange(0, 512)) // 9)) * 128) + (((tl.program_id(0) // 126) % 126) + ((((_lv0 * 512) + tl.arange(0, 512)) // 3) % 3))) * 128) + ((tl.program_id(0) % 126) + (((_lv0 * 512) + tl.arange(0, 512)) % 3))) + 0 * tl.arange(0, 512)), mask=((((_lv0 * 512) + tl.arange(0, 512)) < 576) & (((((tl.program_id(0) // 126) % 126) + ((((_lv0 * 512) + tl.arange(0, 512)) // 3) % 3)) < 128) & (((tl.program_id(0) % 126) + (((_lv0 * 512) + tl.arange(0, 512)) % 3)) < 128))), other=0.0) * tl.load(in1_ptr + (((((((((tl.program_id(0) // 15876) % 128) * 64) + (((_lv0 * 512) + tl.arange(0, 512)) // 9)) * 3) + ((((_lv0 * 512) + tl.arange(0, 512)) // 3) % 3)) * 3) + (((_lv0 * 512) + tl.arange(0, 512)) % 3)) + 0 * tl.arange(0, 512)), mask=((((_lv0 * 512) + tl.arange(0, 512)) < 576) & (((((tl.program_id(0) // 126) % 126) + ((((_lv0 * 512) + tl.arange(0, 512)) // 3) % 3)) < 128) & (((tl.program_id(0) % 126) + (((_lv0 * 512) + tl.arange(0, 512)) % 3)) < 128))), other=0.0)), 0.0))
    _v = ((((tl.sum(_acc0, axis=0) + tl.load(in2_ptr + (((tl.program_id(0) // 15876) % 128)))) - (1.0 * (1.0 / 2.0))) * tl.minimum(tl.maximum((((tl.sum(_acc0, axis=0) + tl.load(in2_ptr + (((tl.program_id(0) // 15876) % 128)))) - (1.0 * (1.0 / 2.0))) + (3.0 * (1.0 / 1.0))), (0.0 * (1.0 / 1.0))), (6.0 * (1.0 / 1.0)))) / (6.0 * (1.0 / 1.0)))
    tl.store(out_ptr + tl.program_id(0), _v)


def t035_s0(out, ins):
    grid = (260112384,)
    t035_s0_kernel[grid](out, ins[0], ins[1], ins[2])
    return out


@triton.jit
def t035_s1_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr):
    _acc0 = tl.zeros([4], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = tl.maximum(_acc0, tl.load(in3_ptr + ((((((((tl.program_id(0) // 508032) * 128) + ((tl.program_id(0) // 3969) % 128)) * 126) + tl.maximum(((((tl.program_id(0) // 63) % 63) * 2) + tl.maximum(((tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - 3, 0), 0) // 2) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 63) % 63) * 2), 0) - (tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - 3, 0), 0) // 2), 0)) - tl.maximum(((tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - 3, 0), 0) // 2) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 63) % 63) * 2), 0) - (tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - 3, 0), 0) // 2), 0)) - tl.maximum(125 - (((tl.program_id(0) // 63) % 63) * 2), 0), 0), 0)) - tl.maximum(((((tl.program_id(0) // 63) % 63) * 2) + tl.maximum(((tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - 3, 0), 0) // 2) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 63) % 63) * 2), 0) - (tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - 3, 0), 0) // 2), 0)) - tl.maximum(((tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - 3, 0), 0) // 2) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 63) % 63) * 2), 0) - (tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - 3, 0), 0) // 2), 0)) - tl.maximum(125 - (((tl.program_id(0) // 63) % 63) * 2), 0), 0), 0)) - 125, 0), 0)) * 126) + tl.maximum((((tl.program_id(0) % 63) * 2) + tl.maximum(((tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - 3, 0), 0) % 2) + tl.maximum(tl.maximum(0 - ((tl.program_id(0) % 63) * 2), 0) - (tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - 3, 0), 0) % 2), 0)) - tl.maximum(((tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - 3, 0), 0) % 2) + tl.maximum(tl.maximum(0 - ((tl.program_id(0) % 63) * 2), 0) - (tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - 3, 0), 0) % 2), 0)) - tl.maximum(125 - ((tl.program_id(0) % 63) * 2), 0), 0), 0)) - tl.maximum((((tl.program_id(0) % 63) * 2) + tl.maximum(((tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - 3, 0), 0) % 2) + tl.maximum(tl.maximum(0 - ((tl.program_id(0) % 63) * 2), 0) - (tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - 3, 0), 0) % 2), 0)) - tl.maximum(((tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - 3, 0), 0) % 2) + tl.maximum(tl.maximum(0 - ((tl.program_id(0) % 63) * 2), 0) - (tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - 3, 0), 0) % 2), 0)) - tl.maximum(125 - ((tl.program_id(0) % 63) * 2), 0), 0), 0)) - 125, 0), 0)))))
    _v = (tl.max(_acc0, axis=0) * (2.0 * tl.sigmoid(2.0 * (tl.log(((1.0 * (1.0 / 1.0)) + tl.exp(tl.max(_acc0, axis=0)))))) - 1.0))
    tl.store(out_ptr + tl.program_id(0), _v)


def t035_s1(out, ins):
    grid = (65028096,)
    t035_s1_kernel[grid](out, ins[0], ins[1], ins[2], ins[3])
    return out


def t035(out, ins):
    _t0 = torch.empty(260112384, device=ins[0].device, dtype=torch.float32)
    t035_s0(_t0, list(ins))
    t035_s1(out, list(ins) + [_t0])
    return out
