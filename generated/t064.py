import torch
import triton
import triton.language as tl


@triton.jit
def t064_kernel(out_ptr, in0_ptr, in1_ptr):
    _acc0 = tl.zeros([256], dtype=tl.float32)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 256) + tl.arange(0, 256)) < 384) & (((((((_lv0 * 256) + tl.arange(0, 256)) % 3) * 1) <= ((tl.program_id(0) % 65538) + 0)) & ((tl.maximum(((tl.program_id(0) % 65538) + 0) - ((((_lv0 * 256) + tl.arange(0, 256)) % 3) * 1), 0) % 1) == 0)) & ((tl.maximum(((tl.program_id(0) % 65538) + 0) - ((((_lv0 * 256) + tl.arange(0, 256)) % 3) * 1), 0) // 1) < 65536))), (tl.load(in0_ptr + ((((((tl.program_id(0) // 8388864) * 128) + (((((tl.program_id(0) // 65538) % 128) // 128) * 128) + (((_lv0 * 256) + tl.arange(0, 256)) // 3))) * 65536) + (tl.maximum(((tl.program_id(0) % 65538) + 0) - ((((_lv0 * 256) + tl.arange(0, 256)) % 3) * 1), 0) // 1))), mask=((((_lv0 * 256) + tl.arange(0, 256)) < 384) & (((((((_lv0 * 256) + tl.arange(0, 256)) % 3) * 1) <= ((tl.program_id(0) % 65538) + 0)) & ((tl.maximum(((tl.program_id(0) % 65538) + 0) - ((((_lv0 * 256) + tl.arange(0, 256)) % 3) * 1), 0) % 1) == 0)) & ((tl.maximum(((tl.program_id(0) % 65538) + 0) - ((((_lv0 * 256) + tl.arange(0, 256)) % 3) * 1), 0) // 1) < 65536))), other=0.0) * tl.load(in1_ptr + ((((((((((tl.program_id(0) // 65538) % 128) // 128) * 128) + (((_lv0 * 256) + tl.arange(0, 256)) // 3)) * 128) + (((tl.program_id(0) // 65538) % 128) % 128)) * 3) + (((_lv0 * 256) + tl.arange(0, 256)) % 3))), mask=((((_lv0 * 256) + tl.arange(0, 256)) < 384) & (((((((_lv0 * 256) + tl.arange(0, 256)) % 3) * 1) <= ((tl.program_id(0) % 65538) + 0)) & ((tl.maximum(((tl.program_id(0) % 65538) + 0) - ((((_lv0 * 256) + tl.arange(0, 256)) % 3) * 1), 0) % 1) == 0)) & ((tl.maximum(((tl.program_id(0) % 65538) + 0) - ((((_lv0 * 256) + tl.arange(0, 256)) % 3) * 1), 0) // 1) < 65536))), other=0.0)), 0.0))
    _v = tl.where(True, tl.sum(_acc0, axis=0), 0.0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t064(out, ins):
    grid = (268443648,)
    t064_kernel[grid](out, ins[0], ins[1])
    return out
