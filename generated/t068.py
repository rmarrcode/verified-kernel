import torch
import triton
import triton.language as tl


@triton.jit
def _mul_combine(a, b):
    return a * b


@triton.jit
def t068_kernel(out_ptr, in0_ptr, in1_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 3):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 2400) & (((((((((((((_lv0 * 1024) + tl.arange(0, 1024)) // 25) % 3) <= ((tl.program_id(0) // 4624) % 66)) & (0 == 0)) & (tl.maximum(((tl.program_id(0) // 4624) % 66) - ((((_lv0 * 1024) + tl.arange(0, 1024)) // 25) % 3), 0) < 64)) & (((((_lv0 * 1024) + tl.arange(0, 1024)) // 5) % 5) <= ((tl.program_id(0) // 68) % 68))) & (0 == 0)) & (tl.maximum(((tl.program_id(0) // 68) % 68) - ((((_lv0 * 1024) + tl.arange(0, 1024)) // 5) % 5), 0) < 64)) & ((((_lv0 * 1024) + tl.arange(0, 1024)) % 5) <= (tl.program_id(0) % 68))) & (0 == 0)) & (tl.maximum((tl.program_id(0) % 68) - (((_lv0 * 1024) + tl.arange(0, 1024)) % 5), 0) < 64))), (tl.load(in0_ptr + ((((((((((tl.program_id(0) // 19531776) * 32) + (((((tl.program_id(0) // 305184) % 64) // 64) * 32) + (((_lv0 * 1024) + tl.arange(0, 1024)) // 75))) * 64) + tl.maximum(((tl.program_id(0) // 4624) % 66) - ((((_lv0 * 1024) + tl.arange(0, 1024)) // 25) % 3), 0)) * 64) + tl.maximum(((tl.program_id(0) // 68) % 68) - ((((_lv0 * 1024) + tl.arange(0, 1024)) // 5) % 5), 0)) * 64) + tl.maximum((tl.program_id(0) % 68) - (((_lv0 * 1024) + tl.arange(0, 1024)) % 5), 0)) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 2400) & (((((((((((((_lv0 * 1024) + tl.arange(0, 1024)) // 25) % 3) <= ((tl.program_id(0) // 4624) % 66)) & (0 == 0)) & (tl.maximum(((tl.program_id(0) // 4624) % 66) - ((((_lv0 * 1024) + tl.arange(0, 1024)) // 25) % 3), 0) < 64)) & (((((_lv0 * 1024) + tl.arange(0, 1024)) // 5) % 5) <= ((tl.program_id(0) // 68) % 68))) & (0 == 0)) & (tl.maximum(((tl.program_id(0) // 68) % 68) - ((((_lv0 * 1024) + tl.arange(0, 1024)) // 5) % 5), 0) < 64)) & ((((_lv0 * 1024) + tl.arange(0, 1024)) % 5) <= (tl.program_id(0) % 68))) & (0 == 0)) & (tl.maximum((tl.program_id(0) % 68) - (((_lv0 * 1024) + tl.arange(0, 1024)) % 5), 0) < 64))), other=0.0) * tl.load(in1_ptr + ((((((((((((((tl.program_id(0) // 305184) % 64) // 64) * 32) + (((_lv0 * 1024) + tl.arange(0, 1024)) // 75)) * 64) + (((tl.program_id(0) // 305184) % 64) % 64)) * 3) + ((((_lv0 * 1024) + tl.arange(0, 1024)) // 25) % 3)) * 5) + ((((_lv0 * 1024) + tl.arange(0, 1024)) // 5) % 5)) * 5) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 5)) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 2400) & (((((((((((((_lv0 * 1024) + tl.arange(0, 1024)) // 25) % 3) <= ((tl.program_id(0) // 4624) % 66)) & (0 == 0)) & (tl.maximum(((tl.program_id(0) // 4624) % 66) - ((((_lv0 * 1024) + tl.arange(0, 1024)) // 25) % 3), 0) < 64)) & (((((_lv0 * 1024) + tl.arange(0, 1024)) // 5) % 5) <= ((tl.program_id(0) // 68) % 68))) & (0 == 0)) & (tl.maximum(((tl.program_id(0) // 68) % 68) - ((((_lv0 * 1024) + tl.arange(0, 1024)) // 5) % 5), 0) < 64)) & ((((_lv0 * 1024) + tl.arange(0, 1024)) % 5) <= (tl.program_id(0) % 68))) & (0 == 0)) & (tl.maximum((tl.program_id(0) % 68) - (((_lv0 * 1024) + tl.arange(0, 1024)) % 5), 0) < 64))), other=0.0)), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t068(out, ins):
    grid = (312508416,)
    t068_kernel[grid](out, ins[0], ins[1])
    return out
