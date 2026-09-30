import torch
import triton
import triton.language as tl


@triton.jit
def _mul_combine(a, b):
    return a * b


@triton.jit
def t016_s0_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr):
    _acc0 = tl.zeros([512], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 512) + tl.arange(0, 512)) < 576) & ((((((((((_lv0 * 512) + tl.arange(0, 512)) // 3) % 3) <= (((tl.program_id(0) // 256) % 256) + 1)) & ((tl.maximum((((tl.program_id(0) // 256) % 256) + 1) - ((((_lv0 * 512) + tl.arange(0, 512)) // 3) % 3), 0) % 2) == 0)) & ((tl.maximum((((tl.program_id(0) // 256) % 256) + 1) - ((((_lv0 * 512) + tl.arange(0, 512)) // 3) % 3), 0) // 2) < 128)) & ((((_lv0 * 512) + tl.arange(0, 512)) % 3) <= ((tl.program_id(0) % 256) + 1))) & ((tl.maximum(((tl.program_id(0) % 256) + 1) - (((_lv0 * 512) + tl.arange(0, 512)) % 3), 0) % 2) == 0)) & ((tl.maximum(((tl.program_id(0) % 256) + 1) - (((_lv0 * 512) + tl.arange(0, 512)) % 3), 0) // 2) < 128))), (tl.load(in0_ptr + ((((((((tl.program_id(0) // 4194304) * 64) + (((((tl.program_id(0) // 65536) % 64) // 64) * 64) + (((_lv0 * 512) + tl.arange(0, 512)) // 9))) * 128) + (tl.maximum((((tl.program_id(0) // 256) % 256) + 1) - ((((_lv0 * 512) + tl.arange(0, 512)) // 3) % 3), 0) // 2)) * 128) + (tl.maximum(((tl.program_id(0) % 256) + 1) - (((_lv0 * 512) + tl.arange(0, 512)) % 3), 0) // 2)) + 0 * tl.arange(0, 512)), mask=((((_lv0 * 512) + tl.arange(0, 512)) < 576) & ((((((((((_lv0 * 512) + tl.arange(0, 512)) // 3) % 3) <= (((tl.program_id(0) // 256) % 256) + 1)) & ((tl.maximum((((tl.program_id(0) // 256) % 256) + 1) - ((((_lv0 * 512) + tl.arange(0, 512)) // 3) % 3), 0) % 2) == 0)) & ((tl.maximum((((tl.program_id(0) // 256) % 256) + 1) - ((((_lv0 * 512) + tl.arange(0, 512)) // 3) % 3), 0) // 2) < 128)) & ((((_lv0 * 512) + tl.arange(0, 512)) % 3) <= ((tl.program_id(0) % 256) + 1))) & ((tl.maximum(((tl.program_id(0) % 256) + 1) - (((_lv0 * 512) + tl.arange(0, 512)) % 3), 0) % 2) == 0)) & ((tl.maximum(((tl.program_id(0) % 256) + 1) - (((_lv0 * 512) + tl.arange(0, 512)) % 3), 0) // 2) < 128))), other=0.0) * tl.load(in1_ptr + ((((((((((((tl.program_id(0) // 65536) % 64) // 64) * 64) + (((_lv0 * 512) + tl.arange(0, 512)) // 9)) * 64) + (((tl.program_id(0) // 65536) % 64) % 64)) * 3) + ((((_lv0 * 512) + tl.arange(0, 512)) // 3) % 3)) * 3) + (((_lv0 * 512) + tl.arange(0, 512)) % 3)) + 0 * tl.arange(0, 512)), mask=((((_lv0 * 512) + tl.arange(0, 512)) < 576) & ((((((((((_lv0 * 512) + tl.arange(0, 512)) // 3) % 3) <= (((tl.program_id(0) // 256) % 256) + 1)) & ((tl.maximum((((tl.program_id(0) // 256) % 256) + 1) - ((((_lv0 * 512) + tl.arange(0, 512)) // 3) % 3), 0) % 2) == 0)) & ((tl.maximum((((tl.program_id(0) // 256) % 256) + 1) - ((((_lv0 * 512) + tl.arange(0, 512)) // 3) % 3), 0) // 2) < 128)) & ((((_lv0 * 512) + tl.arange(0, 512)) % 3) <= ((tl.program_id(0) % 256) + 1))) & ((tl.maximum(((tl.program_id(0) % 256) + 1) - (((_lv0 * 512) + tl.arange(0, 512)) % 3), 0) % 2) == 0)) & ((tl.maximum(((tl.program_id(0) % 256) + 1) - (((_lv0 * 512) + tl.arange(0, 512)) % 3), 0) // 2) < 128))), other=0.0)), 0.0))
    _v = (tl.minimum(tl.maximum((((tl.sum(_acc0, axis=0) + tl.load(in2_ptr + (((tl.program_id(0) // 65536) % 64)))) * (2.0 * tl.sigmoid(2.0 * (tl.log(((1.0 * (1.0 / 1.0)) + tl.exp((tl.sum(_acc0, axis=0) + tl.load(in2_ptr + (((tl.program_id(0) // 65536) % 64))))))))) - 1.0)) + (1.0 * (1.0 / 2.0))), (0.0 - (1.0 * (1.0 / 1.0)))), (1.0 * (1.0 / 1.0))) * (2.0 * (1.0 / 1.0)))
    tl.store(out_ptr + tl.program_id(0), _v)


def t016_s0(out, ins):
    grid = (134217728,)
    t016_s0_kernel[grid](out, ins[0], ins[1], ins[2])
    return out


def t016(out, ins):
    t016_s0(out, list(ins))
    return out
