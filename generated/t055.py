import torch
import triton
import triton.language as tl


@triton.jit
def t055_kernel(out_ptr, in0_ptr, in1_ptr):
    _acc0 = tl.zeros([512], dtype=tl.float32)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 512) + tl.arange(0, 512)) < 576) & ((((0 <= ((((tl.program_id(0) // 1022) % 510) * 1) + (((((_lv0 * 512) + tl.arange(0, 512)) // 3) % 3) * 1))) & (((((tl.program_id(0) // 1022) % 510) * 1) + (((((_lv0 * 512) + tl.arange(0, 512)) // 3) % 3) * 1)) < 512)) & (0 <= (((tl.program_id(0) % 1022) * 1) + ((((_lv0 * 512) + tl.arange(0, 512)) % 3) * 1)))) & ((((tl.program_id(0) % 1022) * 1) + ((((_lv0 * 512) + tl.arange(0, 512)) % 3) * 1)) < 1024))), (tl.load(in0_ptr + ((((((((tl.program_id(0) // 66716160) * 64) + (((((tl.program_id(0) // 521220) % 128) // 128) * 64) + (((_lv0 * 512) + tl.arange(0, 512)) // 9))) * 512) + tl.maximum(((((tl.program_id(0) // 1022) % 510) * 1) + (((((_lv0 * 512) + tl.arange(0, 512)) // 3) % 3) * 1)) - 0, 0)) * 1024) + tl.maximum((((tl.program_id(0) % 1022) * 1) + ((((_lv0 * 512) + tl.arange(0, 512)) % 3) * 1)) - 0, 0))), mask=((((_lv0 * 512) + tl.arange(0, 512)) < 576) & ((((0 <= ((((tl.program_id(0) // 1022) % 510) * 1) + (((((_lv0 * 512) + tl.arange(0, 512)) // 3) % 3) * 1))) & (((((tl.program_id(0) // 1022) % 510) * 1) + (((((_lv0 * 512) + tl.arange(0, 512)) // 3) % 3) * 1)) < 512)) & (0 <= (((tl.program_id(0) % 1022) * 1) + ((((_lv0 * 512) + tl.arange(0, 512)) % 3) * 1)))) & ((((tl.program_id(0) % 1022) * 1) + ((((_lv0 * 512) + tl.arange(0, 512)) % 3) * 1)) < 1024))), other=0.0) * tl.load(in1_ptr + (((((((((tl.program_id(0) // 521220) % 128) * 64) + (((_lv0 * 512) + tl.arange(0, 512)) // 9)) * 3) + ((((_lv0 * 512) + tl.arange(0, 512)) // 3) % 3)) * 3) + (((_lv0 * 512) + tl.arange(0, 512)) % 3))), mask=((((_lv0 * 512) + tl.arange(0, 512)) < 576) & ((((0 <= ((((tl.program_id(0) // 1022) % 510) * 1) + (((((_lv0 * 512) + tl.arange(0, 512)) // 3) % 3) * 1))) & (((((tl.program_id(0) // 1022) % 510) * 1) + (((((_lv0 * 512) + tl.arange(0, 512)) // 3) % 3) * 1)) < 512)) & (0 <= (((tl.program_id(0) % 1022) * 1) + ((((_lv0 * 512) + tl.arange(0, 512)) % 3) * 1)))) & ((((tl.program_id(0) % 1022) * 1) + ((((_lv0 * 512) + tl.arange(0, 512)) % 3) * 1)) < 1024))), other=0.0)), 0.0))
    _v = tl.where(True, tl.sum(_acc0, axis=0), 0.0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t055(out, ins):
    grid = (266864640,)
    t055_kernel[grid](out, ins[0], ins[1])
    return out
