import torch
import triton
import triton.language as tl


@triton.jit
def t065_kernel(out_ptr, in0_ptr, in1_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 1344) & ((((((((((_lv0 * 1024) + tl.arange(0, 1024)) // 7) % 3) <= ((tl.program_id(0) // 518) % 514)) & (0 == 0)) & (tl.maximum(((tl.program_id(0) // 518) % 514) - ((((_lv0 * 1024) + tl.arange(0, 1024)) // 7) % 3), 0) < 512)) & ((((_lv0 * 1024) + tl.arange(0, 1024)) % 7) <= (tl.program_id(0) % 518))) & (0 == 0)) & (tl.maximum((tl.program_id(0) % 518) - (((_lv0 * 1024) + tl.arange(0, 1024)) % 7), 0) < 512))), (tl.load(in0_ptr + ((((((((tl.program_id(0) // 17040128) * 64) + (((((tl.program_id(0) // 266252) % 64) // 64) * 64) + (((_lv0 * 1024) + tl.arange(0, 1024)) // 21))) * 512) + tl.maximum(((tl.program_id(0) // 518) % 514) - ((((_lv0 * 1024) + tl.arange(0, 1024)) // 7) % 3), 0)) * 512) + tl.maximum((tl.program_id(0) % 518) - (((_lv0 * 1024) + tl.arange(0, 1024)) % 7), 0)) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 1344) & ((((((((((_lv0 * 1024) + tl.arange(0, 1024)) // 7) % 3) <= ((tl.program_id(0) // 518) % 514)) & (0 == 0)) & (tl.maximum(((tl.program_id(0) // 518) % 514) - ((((_lv0 * 1024) + tl.arange(0, 1024)) // 7) % 3), 0) < 512)) & ((((_lv0 * 1024) + tl.arange(0, 1024)) % 7) <= (tl.program_id(0) % 518))) & (0 == 0)) & (tl.maximum((tl.program_id(0) % 518) - (((_lv0 * 1024) + tl.arange(0, 1024)) % 7), 0) < 512))), other=0.0) * tl.load(in1_ptr + ((((((((((((tl.program_id(0) // 266252) % 64) // 64) * 64) + (((_lv0 * 1024) + tl.arange(0, 1024)) // 21)) * 64) + (((tl.program_id(0) // 266252) % 64) % 64)) * 3) + ((((_lv0 * 1024) + tl.arange(0, 1024)) // 7) % 3)) * 7) + (((_lv0 * 1024) + tl.arange(0, 1024)) % 7)) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 1344) & ((((((((((_lv0 * 1024) + tl.arange(0, 1024)) // 7) % 3) <= ((tl.program_id(0) // 518) % 514)) & (0 == 0)) & (tl.maximum(((tl.program_id(0) // 518) % 514) - ((((_lv0 * 1024) + tl.arange(0, 1024)) // 7) % 3), 0) < 512)) & ((((_lv0 * 1024) + tl.arange(0, 1024)) % 7) <= (tl.program_id(0) % 518))) & (0 == 0)) & (tl.maximum((tl.program_id(0) % 518) - (((_lv0 * 1024) + tl.arange(0, 1024)) % 7), 0) < 512))), other=0.0)), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t065(out, ins):
    grid = (136321024,)
    t065_kernel[grid](out, ins[0], ins[1])
    return out
