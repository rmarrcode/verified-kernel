import torch
import triton
import triton.language as tl


@triton.jit
def t081_kernel(out_ptr, in0_ptr, in1_ptr):
    _acc0 = tl.zeros([256], dtype=tl.float32)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 256) + tl.arange(0, 256)) < 288) & (((((((((((_lv0 * 256) + tl.arange(0, 256)) // 3) % 3) * 2) <= (((tl.program_id(0) // 638) % 318) + 1)) & ((tl.maximum((((tl.program_id(0) // 638) % 318) + 1) - (((((_lv0 * 256) + tl.arange(0, 256)) // 3) % 3) * 2), 0) % 5) == 0)) & ((tl.maximum((((tl.program_id(0) // 638) % 318) + 1) - (((((_lv0 * 256) + tl.arange(0, 256)) // 3) % 3) * 2), 0) // 5) < 64)) & (((((_lv0 * 256) + tl.arange(0, 256)) % 3) * 2) <= ((tl.program_id(0) % 638) + 1))) & ((tl.maximum(((tl.program_id(0) % 638) + 1) - ((((_lv0 * 256) + tl.arange(0, 256)) % 3) * 2), 0) % 5) == 0)) & ((tl.maximum(((tl.program_id(0) % 638) + 1) - ((((_lv0 * 256) + tl.arange(0, 256)) % 3) * 2), 0) // 5) < 128))), (tl.load(in0_ptr + ((((((((tl.program_id(0) // 12984576) * 32) + (((((tl.program_id(0) // 202884) % 64) // 64) * 32) + (((_lv0 * 256) + tl.arange(0, 256)) // 9))) * 64) + (tl.maximum((((tl.program_id(0) // 638) % 318) + 1) - (((((_lv0 * 256) + tl.arange(0, 256)) // 3) % 3) * 2), 0) // 5)) * 128) + (tl.maximum(((tl.program_id(0) % 638) + 1) - ((((_lv0 * 256) + tl.arange(0, 256)) % 3) * 2), 0) // 5))), mask=((((_lv0 * 256) + tl.arange(0, 256)) < 288) & (((((((((((_lv0 * 256) + tl.arange(0, 256)) // 3) % 3) * 2) <= (((tl.program_id(0) // 638) % 318) + 1)) & ((tl.maximum((((tl.program_id(0) // 638) % 318) + 1) - (((((_lv0 * 256) + tl.arange(0, 256)) // 3) % 3) * 2), 0) % 5) == 0)) & ((tl.maximum((((tl.program_id(0) // 638) % 318) + 1) - (((((_lv0 * 256) + tl.arange(0, 256)) // 3) % 3) * 2), 0) // 5) < 64)) & (((((_lv0 * 256) + tl.arange(0, 256)) % 3) * 2) <= ((tl.program_id(0) % 638) + 1))) & ((tl.maximum(((tl.program_id(0) % 638) + 1) - ((((_lv0 * 256) + tl.arange(0, 256)) % 3) * 2), 0) % 5) == 0)) & ((tl.maximum(((tl.program_id(0) % 638) + 1) - ((((_lv0 * 256) + tl.arange(0, 256)) % 3) * 2), 0) // 5) < 128))), other=0.0) * tl.load(in1_ptr + ((((((((((((tl.program_id(0) // 202884) % 64) // 64) * 32) + (((_lv0 * 256) + tl.arange(0, 256)) // 9)) * 64) + (((tl.program_id(0) // 202884) % 64) % 64)) * 3) + ((((_lv0 * 256) + tl.arange(0, 256)) // 3) % 3)) * 3) + (((_lv0 * 256) + tl.arange(0, 256)) % 3))), mask=((((_lv0 * 256) + tl.arange(0, 256)) < 288) & (((((((((((_lv0 * 256) + tl.arange(0, 256)) // 3) % 3) * 2) <= (((tl.program_id(0) // 638) % 318) + 1)) & ((tl.maximum((((tl.program_id(0) // 638) % 318) + 1) - (((((_lv0 * 256) + tl.arange(0, 256)) // 3) % 3) * 2), 0) % 5) == 0)) & ((tl.maximum((((tl.program_id(0) // 638) % 318) + 1) - (((((_lv0 * 256) + tl.arange(0, 256)) // 3) % 3) * 2), 0) // 5) < 64)) & (((((_lv0 * 256) + tl.arange(0, 256)) % 3) * 2) <= ((tl.program_id(0) % 638) + 1))) & ((tl.maximum(((tl.program_id(0) % 638) + 1) - ((((_lv0 * 256) + tl.arange(0, 256)) % 3) * 2), 0) % 5) == 0)) & ((tl.maximum(((tl.program_id(0) % 638) + 1) - ((((_lv0 * 256) + tl.arange(0, 256)) % 3) * 2), 0) // 5) < 128))), other=0.0)), 0.0))
    _v = tl.where(True, tl.sum(_acc0, axis=0), 0.0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t081(out, ins):
    grid = (207753216,)
    t081_kernel[grid](out, ins[0], ins[1])
    return out
