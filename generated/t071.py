import torch
import triton
import triton.language as tl


@triton.jit
def t071_kernel(out_ptr, in0_ptr, in1_ptr):
    _acc0 = tl.zeros([256], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 256) + tl.arange(0, 256)) < 288) & ((((((((((_lv0 * 256) + tl.arange(0, 256)) // 3) % 3) <= ((tl.program_id(0) // 1026) % 514)) & (0 == 0)) & (tl.maximum(((tl.program_id(0) // 1026) % 514) - ((((_lv0 * 256) + tl.arange(0, 256)) // 3) % 3), 0) < 512)) & ((((_lv0 * 256) + tl.arange(0, 256)) % 3) <= (tl.program_id(0) % 1026))) & (0 == 0)) & (tl.maximum((tl.program_id(0) % 1026) - (((_lv0 * 256) + tl.arange(0, 256)) % 3), 0) < 1024))), (tl.load(in0_ptr + ((((((((tl.program_id(0) // 16875648) * 32) + (((((tl.program_id(0) // 527364) % 32) // 32) * 32) + (((_lv0 * 256) + tl.arange(0, 256)) // 9))) * 512) + tl.maximum(((tl.program_id(0) // 1026) % 514) - ((((_lv0 * 256) + tl.arange(0, 256)) // 3) % 3), 0)) * 1024) + tl.maximum((tl.program_id(0) % 1026) - (((_lv0 * 256) + tl.arange(0, 256)) % 3), 0)) + 0 * tl.arange(0, 256)), mask=((((_lv0 * 256) + tl.arange(0, 256)) < 288) & ((((((((((_lv0 * 256) + tl.arange(0, 256)) // 3) % 3) <= ((tl.program_id(0) // 1026) % 514)) & (0 == 0)) & (tl.maximum(((tl.program_id(0) // 1026) % 514) - ((((_lv0 * 256) + tl.arange(0, 256)) // 3) % 3), 0) < 512)) & ((((_lv0 * 256) + tl.arange(0, 256)) % 3) <= (tl.program_id(0) % 1026))) & (0 == 0)) & (tl.maximum((tl.program_id(0) % 1026) - (((_lv0 * 256) + tl.arange(0, 256)) % 3), 0) < 1024))), other=0.0) * tl.load(in1_ptr + ((((((((((((tl.program_id(0) // 527364) % 32) // 32) * 32) + (((_lv0 * 256) + tl.arange(0, 256)) // 9)) * 32) + (((tl.program_id(0) // 527364) % 32) % 32)) * 3) + ((((_lv0 * 256) + tl.arange(0, 256)) // 3) % 3)) * 3) + (((_lv0 * 256) + tl.arange(0, 256)) % 3)) + 0 * tl.arange(0, 256)), mask=((((_lv0 * 256) + tl.arange(0, 256)) < 288) & ((((((((((_lv0 * 256) + tl.arange(0, 256)) // 3) % 3) <= ((tl.program_id(0) // 1026) % 514)) & (0 == 0)) & (tl.maximum(((tl.program_id(0) // 1026) % 514) - ((((_lv0 * 256) + tl.arange(0, 256)) // 3) % 3), 0) < 512)) & ((((_lv0 * 256) + tl.arange(0, 256)) % 3) <= (tl.program_id(0) % 1026))) & (0 == 0)) & (tl.maximum((tl.program_id(0) % 1026) - (((_lv0 * 256) + tl.arange(0, 256)) % 3), 0) < 1024))), other=0.0)), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t071(out, ins):
    grid = (135005184,)
    t071_kernel[grid](out, ins[0], ins[1])
    return out
