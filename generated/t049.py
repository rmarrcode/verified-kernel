import torch
import triton
import triton.language as tl


@triton.jit
def t049_kernel(out_ptr, in0_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (tl.load(in0_ptr + ((((((tl.program_id(0) // 4095) * 4096) + 0) * 4095) + (tl.program_id(0) % 4095)))))
    for _lv0 in range(0, 4):
        _acc0 = tl.maximum(_acc0, tl.load(in0_ptr + ((((((tl.program_id(0) // 4095) * 4096) + tl.maximum(((_lv0 * 1024) + tl.arange(0, 1024)) - tl.maximum(((_lv0 * 1024) + tl.arange(0, 1024)) - 4095, 0), 0)) * 4095) + (tl.program_id(0) % 4095)))))
    _v = tl.max(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t049(out, ins):
    grid = (262080,)
    t049_kernel[grid](out, ins[0])
    return out
