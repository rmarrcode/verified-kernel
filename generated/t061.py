import torch
import triton
import triton.language as tl


@triton.jit
def t061_kernel(out_ptr, in0_ptr, in1_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 1296) & (((((((((((((_lv0 * 1024) + tl.arange(0, 1024)) // 9) % 3) <= ((tl.program_id(0) // 4356) % 66)) & (0 == 0)) & (tl.maximum(((tl.program_id(0) // 4356) % 66) - ((((_lv0 * 1024) + tl.arange(0, 1024)) // 9) % 3), 0) < 64)) & (((((_lv0 * 1024) + tl.arange(0, 1024)) // 3) % 3) <= ((tl.program_id(0) // 66) % 66))) & (0 == 0)) & (tl.maximum(((tl.program_id(0) // 66) % 66) - ((((_lv0 * 1024) + tl.arange(0, 1024)) // 3) % 3), 0) < 64)) & ((((_lv0 * 1024) + tl.arange(0, 1024)) % 3) <= (tl.program_id(0) % 66))) & (0 == 0)) & (tl.maximum((tl.program_id(0) % 66) - (((_lv0 * 1024) + tl.arange(0, 1024)) % 3), 0) < 64))), (tl.load(in0_ptr + ((((((((((tl.program_id(0) // 13799808) * 48) + (((((tl.program_id(0) // 287496) % 48) // 48) * 48) + (((_lv0 * 1024) + tl.arange(0, 1024)) // 27))) * 64) + tl.maximum(((tl.program_id(0) // 4356) % 66) - ((((_lv0 * 1024) + tl.arange(0, 1024)) // 9) % 3), 0)) * 64) + tl.maximum(((tl.program_id(0) // 66) % 66) - ((((_lv0 * 1024) + tl.arange(0, 1024)) // 3) % 3), 0)) * 64) + tl.maximum((tl.program_id(0) % 66) - (((_lv0 * 1024) + tl.arange(0, 1024)) % 3), 0)) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 1296) & (((((((((((((_lv0 * 1024) + tl.arange(0, 1024)) // 9) % 3) <= ((tl.program_id(0) // 4356) % 66)) & (0 == 0)) & (tl.maximum(((tl.program_id(0) // 4356) % 66) - ((((_lv0 * 1024) + tl.arange(0, 1024)) // 9) % 3), 0) < 64)) & (((((_lv0 * 1024) + tl.arange(0, 1024)) // 3) % 3) <= ((tl.program_id(0) // 66) % 66))) & (0 == 0)) & (tl.maximum(((tl.program_id(0) // 66) % 66) - ((((_lv0 * 1024) + tl.arange(0, 1024)) // 3) % 3), 0) < 64)) & ((((_lv0 * 1024) + tl.arange(0, 1024)) % 3) <= (tl.program_id(0) % 66))) & (0 == 0)) & (tl.maximum((tl.program_id(0) % 66) - (((_lv0 * 1024) + tl.arange(0, 1024)) % 3), 0) < 64))), other=0.0) * tl.load(in1_ptr + ((((((((((((((tl.program_id(0) // 287496) % 48) // 48) * 48) + (((_lv0 * 1024) + tl.arange(0, 1024)) // 27)) * 48) + (((tl.program_id(0) // 287496) % 48) % 48)) * 3) + ((((_lv0 * 1024) + tl.arange(0, 1024)) // 9) % 3)) * 3) + ((((_lv0 * 1024) + tl.arange(0, 1024)) // 3) % 3)) * 3) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 3)) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 1296) & (((((((((((((_lv0 * 1024) + tl.arange(0, 1024)) // 9) % 3) <= ((tl.program_id(0) // 4356) % 66)) & (0 == 0)) & (tl.maximum(((tl.program_id(0) // 4356) % 66) - ((((_lv0 * 1024) + tl.arange(0, 1024)) // 9) % 3), 0) < 64)) & (((((_lv0 * 1024) + tl.arange(0, 1024)) // 3) % 3) <= ((tl.program_id(0) // 66) % 66))) & (0 == 0)) & (tl.maximum(((tl.program_id(0) // 66) % 66) - ((((_lv0 * 1024) + tl.arange(0, 1024)) // 3) % 3), 0) < 64)) & ((((_lv0 * 1024) + tl.arange(0, 1024)) % 3) <= (tl.program_id(0) % 66))) & (0 == 0)) & (tl.maximum((tl.program_id(0) % 66) - (((_lv0 * 1024) + tl.arange(0, 1024)) % 3), 0) < 64))), other=0.0)), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t061(out, ins):
    grid = (110398464,)
    t061_kernel[grid](out, ins[0], ins[1])
    return out
