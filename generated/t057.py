import torch
import triton
import triton.language as tl


@triton.jit
def t057_kernel(out_ptr, in0_ptr, in1_ptr):
    _acc0 = tl.zeros([512], dtype=tl.float32)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 512) + tl.arange(0, 512)) < 576) & (((((((((((_lv0 * 512) + tl.arange(0, 512)) // 3) % 3) * 1) <= (((tl.program_id(0) // 1026) % 1026) + 0)) & ((tl.maximum((((tl.program_id(0) // 1026) % 1026) + 0) - (((((_lv0 * 512) + tl.arange(0, 512)) // 3) % 3) * 1), 0) % 1) == 0)) & ((tl.maximum((((tl.program_id(0) // 1026) % 1026) + 0) - (((((_lv0 * 512) + tl.arange(0, 512)) // 3) % 3) * 1), 0) // 1) < 1024)) & (((((_lv0 * 512) + tl.arange(0, 512)) % 3) * 1) <= ((tl.program_id(0) % 1026) + 0))) & ((tl.maximum(((tl.program_id(0) % 1026) + 0) - ((((_lv0 * 512) + tl.arange(0, 512)) % 3) * 1), 0) % 1) == 0)) & ((tl.maximum(((tl.program_id(0) % 1026) + 0) - ((((_lv0 * 512) + tl.arange(0, 512)) % 3) * 1), 0) // 1) < 1024))), (tl.load(in0_ptr + ((((((((tl.program_id(0) // 67371264) * 64) + (((((tl.program_id(0) // 1052676) % 64) // 64) * 64) + (((_lv0 * 512) + tl.arange(0, 512)) // 9))) * 1024) + (tl.maximum((((tl.program_id(0) // 1026) % 1026) + 0) - (((((_lv0 * 512) + tl.arange(0, 512)) // 3) % 3) * 1), 0) // 1)) * 1024) + (tl.maximum(((tl.program_id(0) % 1026) + 0) - ((((_lv0 * 512) + tl.arange(0, 512)) % 3) * 1), 0) // 1)) + 0 * tl.arange(0, 512)), mask=((((_lv0 * 512) + tl.arange(0, 512)) < 576) & (((((((((((_lv0 * 512) + tl.arange(0, 512)) // 3) % 3) * 1) <= (((tl.program_id(0) // 1026) % 1026) + 0)) & ((tl.maximum((((tl.program_id(0) // 1026) % 1026) + 0) - (((((_lv0 * 512) + tl.arange(0, 512)) // 3) % 3) * 1), 0) % 1) == 0)) & ((tl.maximum((((tl.program_id(0) // 1026) % 1026) + 0) - (((((_lv0 * 512) + tl.arange(0, 512)) // 3) % 3) * 1), 0) // 1) < 1024)) & (((((_lv0 * 512) + tl.arange(0, 512)) % 3) * 1) <= ((tl.program_id(0) % 1026) + 0))) & ((tl.maximum(((tl.program_id(0) % 1026) + 0) - ((((_lv0 * 512) + tl.arange(0, 512)) % 3) * 1), 0) % 1) == 0)) & ((tl.maximum(((tl.program_id(0) % 1026) + 0) - ((((_lv0 * 512) + tl.arange(0, 512)) % 3) * 1), 0) // 1) < 1024))), other=0.0) * tl.load(in1_ptr + ((((((((((((tl.program_id(0) // 1052676) % 64) // 64) * 64) + (((_lv0 * 512) + tl.arange(0, 512)) // 9)) * 64) + (((tl.program_id(0) // 1052676) % 64) % 64)) * 3) + ((((_lv0 * 512) + tl.arange(0, 512)) // 3) % 3)) * 3) + (((_lv0 * 512) + tl.arange(0, 512)) % 3)) + 0 * tl.arange(0, 512)), mask=((((_lv0 * 512) + tl.arange(0, 512)) < 576) & (((((((((((_lv0 * 512) + tl.arange(0, 512)) // 3) % 3) * 1) <= (((tl.program_id(0) // 1026) % 1026) + 0)) & ((tl.maximum((((tl.program_id(0) // 1026) % 1026) + 0) - (((((_lv0 * 512) + tl.arange(0, 512)) // 3) % 3) * 1), 0) % 1) == 0)) & ((tl.maximum((((tl.program_id(0) // 1026) % 1026) + 0) - (((((_lv0 * 512) + tl.arange(0, 512)) // 3) % 3) * 1), 0) // 1) < 1024)) & (((((_lv0 * 512) + tl.arange(0, 512)) % 3) * 1) <= ((tl.program_id(0) % 1026) + 0))) & ((tl.maximum(((tl.program_id(0) % 1026) + 0) - ((((_lv0 * 512) + tl.arange(0, 512)) % 3) * 1), 0) % 1) == 0)) & ((tl.maximum(((tl.program_id(0) % 1026) + 0) - ((((_lv0 * 512) + tl.arange(0, 512)) % 3) * 1), 0) // 1) < 1024))), other=0.0)), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t057(out, ins):
    grid = (269485056,)
    t057_kernel[grid](out, ins[0], ins[1])
    return out
