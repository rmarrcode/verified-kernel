import torch
import triton
import triton.language as tl


@triton.jit
def t041_kernel(out_ptr, in0_ptr):
    _acc0 = tl.zeros([8], dtype=tl.float32) + (tl.load(in0_ptr + ((((((tl.program_id(0) // 12580416) * 192) + ((tl.program_id(0) // 65523) % 192)) * 65536) + tl.maximum(((tl.program_id(0) % 65523) + (tl.maximum((0 + tl.maximum(((tl.maximum(4 - (tl.program_id(0) % 65523), 0) + 2) // 3) - 0, 0)) - tl.maximum((0 + tl.maximum(((tl.maximum(4 - (tl.program_id(0) % 65523), 0) + 2) // 3) - 0, 0)) - (tl.maximum(65539 - (tl.program_id(0) % 65523), 0) // 3), 0), 0) * 3)) - 4, 0)))))
    for _lv0 in range(0, 1):
        _acc0 = tl.maximum(_acc0, tl.load(in0_ptr + ((((((tl.program_id(0) // 12580416) * 192) + ((tl.program_id(0) // 65523) % 192)) * 65536) + tl.maximum(((tl.program_id(0) % 65523) + (tl.maximum((tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) + tl.maximum(((tl.maximum(4 - (tl.program_id(0) % 65523), 0) + 2) // 3) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0), 0)) - tl.maximum((tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0) + tl.maximum(((tl.maximum(4 - (tl.program_id(0) % 65523), 0) + 2) // 3) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - tl.maximum(((_lv0 * 8) + tl.arange(0, 8)) - 7, 0), 0), 0)) - (tl.maximum(65539 - (tl.program_id(0) % 65523), 0) // 3), 0), 0) * 3)) - 4, 0)))))
    _v = tl.max(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t041(out, ins):
    grid = (402573312,)
    t041_kernel[grid](out, ins[0])
    return out
