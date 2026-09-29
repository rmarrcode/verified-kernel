import torch
import triton
import triton.language as tl


@triton.jit
def t069_kernel(out_ptr, in0_ptr, in1_ptr):
    _acc0 = tl.zeros([512], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 512) + tl.arange(0, 512)) < 960) & ((((((((((_lv0 * 512) + tl.arange(0, 512)) // 5) % 3) <= ((tl.program_id(0) // 260) % 130)) & (0 == 0)) & (tl.maximum(((tl.program_id(0) // 260) % 130) - ((((_lv0 * 512) + tl.arange(0, 512)) // 5) % 3), 0) < 128)) & ((((_lv0 * 512) + tl.arange(0, 512)) % 5) <= (tl.program_id(0) % 260))) & (0 == 0)) & (tl.maximum((tl.program_id(0) % 260) - (((_lv0 * 512) + tl.arange(0, 512)) % 5), 0) < 256))), (tl.load(in0_ptr + ((((((((tl.program_id(0) // 4326400) * 64) + (((((tl.program_id(0) // 33800) % 128) // 128) * 64) + (((_lv0 * 512) + tl.arange(0, 512)) // 15))) * 128) + tl.maximum(((tl.program_id(0) // 260) % 130) - ((((_lv0 * 512) + tl.arange(0, 512)) // 5) % 3), 0)) * 256) + tl.maximum((tl.program_id(0) % 260) - (((_lv0 * 512) + tl.arange(0, 512)) % 5), 0)) + 0 * tl.arange(0, 512)), mask=((((_lv0 * 512) + tl.arange(0, 512)) < 960) & ((((((((((_lv0 * 512) + tl.arange(0, 512)) // 5) % 3) <= ((tl.program_id(0) // 260) % 130)) & (0 == 0)) & (tl.maximum(((tl.program_id(0) // 260) % 130) - ((((_lv0 * 512) + tl.arange(0, 512)) // 5) % 3), 0) < 128)) & ((((_lv0 * 512) + tl.arange(0, 512)) % 5) <= (tl.program_id(0) % 260))) & (0 == 0)) & (tl.maximum((tl.program_id(0) % 260) - (((_lv0 * 512) + tl.arange(0, 512)) % 5), 0) < 256))), other=0.0) * tl.load(in1_ptr + ((((((((((((tl.program_id(0) // 33800) % 128) // 128) * 64) + (((_lv0 * 512) + tl.arange(0, 512)) // 15)) * 128) + (((tl.program_id(0) // 33800) % 128) % 128)) * 3) + ((((_lv0 * 512) + tl.arange(0, 512)) // 5) % 3)) * 5) + (((_lv0 * 512) + tl.arange(0, 512)) % 5)) + 0 * tl.arange(0, 512)), mask=((((_lv0 * 512) + tl.arange(0, 512)) < 960) & ((((((((((_lv0 * 512) + tl.arange(0, 512)) // 5) % 3) <= ((tl.program_id(0) // 260) % 130)) & (0 == 0)) & (tl.maximum(((tl.program_id(0) // 260) % 130) - ((((_lv0 * 512) + tl.arange(0, 512)) // 5) % 3), 0) < 128)) & ((((_lv0 * 512) + tl.arange(0, 512)) % 5) <= (tl.program_id(0) % 260))) & (0 == 0)) & (tl.maximum((tl.program_id(0) % 260) - (((_lv0 * 512) + tl.arange(0, 512)) % 5), 0) < 256))), other=0.0)), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t069(out, ins):
    grid = (276889600,)
    t069_kernel[grid](out, ins[0], ins[1])
    return out
