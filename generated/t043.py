import torch
import triton
import triton.language as tl


@triton.jit
def _mul_combine(a, b):
    return a * b


@triton.jit
def t043_kernel(out_ptr, in0_ptr):
    _acc0 = tl.zeros([16], dtype=tl.float32) + (tl.load(in0_ptr + ((((((((((tl.program_id(0) // 7626496) * 32) + ((tl.program_id(0) // 238328) % 32)) * 128) + tl.maximum(((((tl.program_id(0) // 3844) % 62) * 2) + (tl.maximum(((0 // 9) + tl.maximum(((tl.maximum(1 - (((tl.program_id(0) // 3844) % 62) * 2), 0) + 2) // 3) - (0 // 9), 0)) - tl.maximum(((0 // 9) + tl.maximum(((tl.maximum(1 - (((tl.program_id(0) // 3844) % 62) * 2), 0) + 2) // 3) - (0 // 9), 0)) - (tl.maximum(128 - (((tl.program_id(0) // 3844) % 62) * 2), 0) // 3), 0), 0) * 3)) - 1, 0)) * 128) + tl.maximum(((((tl.program_id(0) // 62) % 62) * 2) + (tl.maximum((((0 // 3) % 3) + tl.maximum(((tl.maximum(1 - (((tl.program_id(0) // 62) % 62) * 2), 0) + 2) // 3) - ((0 // 3) % 3), 0)) - tl.maximum((((0 // 3) % 3) + tl.maximum(((tl.maximum(1 - (((tl.program_id(0) // 62) % 62) * 2), 0) + 2) // 3) - ((0 // 3) % 3), 0)) - (tl.maximum(128 - (((tl.program_id(0) // 62) % 62) * 2), 0) // 3), 0), 0) * 3)) - 1, 0)) * 128) + tl.maximum((((tl.program_id(0) % 62) * 2) + (tl.maximum(((0 % 3) + tl.maximum(((tl.maximum(1 - ((tl.program_id(0) % 62) * 2), 0) + 2) // 3) - (0 % 3), 0)) - tl.maximum(((0 % 3) + tl.maximum(((tl.maximum(1 - ((tl.program_id(0) % 62) * 2), 0) + 2) // 3) - (0 % 3), 0)) - (tl.maximum(128 - ((tl.program_id(0) % 62) * 2), 0) // 3), 0), 0) * 3)) - 1, 0)))))
    for _lv0 in range(0, 2):
        _acc0 = tl.maximum(_acc0, tl.load(in0_ptr + ((((((((((tl.program_id(0) // 7626496) * 32) + ((tl.program_id(0) // 238328) % 32)) * 128) + tl.maximum(((((tl.program_id(0) // 3844) % 62) * 2) + (tl.maximum(((tl.maximum(((_lv0 * 16) + tl.arange(0, 16)) - tl.maximum(((_lv0 * 16) + tl.arange(0, 16)) - 26, 0), 0) // 9) + tl.maximum(((tl.maximum(1 - (((tl.program_id(0) // 3844) % 62) * 2), 0) + 2) // 3) - (tl.maximum(((_lv0 * 16) + tl.arange(0, 16)) - tl.maximum(((_lv0 * 16) + tl.arange(0, 16)) - 26, 0), 0) // 9), 0)) - tl.maximum(((tl.maximum(((_lv0 * 16) + tl.arange(0, 16)) - tl.maximum(((_lv0 * 16) + tl.arange(0, 16)) - 26, 0), 0) // 9) + tl.maximum(((tl.maximum(1 - (((tl.program_id(0) // 3844) % 62) * 2), 0) + 2) // 3) - (tl.maximum(((_lv0 * 16) + tl.arange(0, 16)) - tl.maximum(((_lv0 * 16) + tl.arange(0, 16)) - 26, 0), 0) // 9), 0)) - (tl.maximum(128 - (((tl.program_id(0) // 3844) % 62) * 2), 0) // 3), 0), 0) * 3)) - 1, 0)) * 128) + tl.maximum(((((tl.program_id(0) // 62) % 62) * 2) + (tl.maximum((((tl.maximum(((_lv0 * 16) + tl.arange(0, 16)) - tl.maximum(((_lv0 * 16) + tl.arange(0, 16)) - 26, 0), 0) // 3) % 3) + tl.maximum(((tl.maximum(1 - (((tl.program_id(0) // 62) % 62) * 2), 0) + 2) // 3) - ((tl.maximum(((_lv0 * 16) + tl.arange(0, 16)) - tl.maximum(((_lv0 * 16) + tl.arange(0, 16)) - 26, 0), 0) // 3) % 3), 0)) - tl.maximum((((tl.maximum(((_lv0 * 16) + tl.arange(0, 16)) - tl.maximum(((_lv0 * 16) + tl.arange(0, 16)) - 26, 0), 0) // 3) % 3) + tl.maximum(((tl.maximum(1 - (((tl.program_id(0) // 62) % 62) * 2), 0) + 2) // 3) - ((tl.maximum(((_lv0 * 16) + tl.arange(0, 16)) - tl.maximum(((_lv0 * 16) + tl.arange(0, 16)) - 26, 0), 0) // 3) % 3), 0)) - (tl.maximum(128 - (((tl.program_id(0) // 62) % 62) * 2), 0) // 3), 0), 0) * 3)) - 1, 0)) * 128) + tl.maximum((((tl.program_id(0) % 62) * 2) + (tl.maximum(((tl.maximum(((_lv0 * 16) + tl.arange(0, 16)) - tl.maximum(((_lv0 * 16) + tl.arange(0, 16)) - 26, 0), 0) % 3) + tl.maximum(((tl.maximum(1 - ((tl.program_id(0) % 62) * 2), 0) + 2) // 3) - (tl.maximum(((_lv0 * 16) + tl.arange(0, 16)) - tl.maximum(((_lv0 * 16) + tl.arange(0, 16)) - 26, 0), 0) % 3), 0)) - tl.maximum(((tl.maximum(((_lv0 * 16) + tl.arange(0, 16)) - tl.maximum(((_lv0 * 16) + tl.arange(0, 16)) - 26, 0), 0) % 3) + tl.maximum(((tl.maximum(1 - ((tl.program_id(0) % 62) * 2), 0) + 2) // 3) - (tl.maximum(((_lv0 * 16) + tl.arange(0, 16)) - tl.maximum(((_lv0 * 16) + tl.arange(0, 16)) - 26, 0), 0) % 3), 0)) - (tl.maximum(128 - ((tl.program_id(0) % 62) * 2), 0) // 3), 0), 0) * 3)) - 1, 0)))))
    _v = tl.max(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t043(out, ins):
    grid = (122023936,)
    t043_kernel[grid](out, ins[0])
    return out
