import torch
import triton
import triton.language as tl


@triton.jit
def _mul_combine(a, b):
    return a * b


@triton.jit
def t010_s0_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr):
    _acc0 = tl.zeros([512], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 2):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 512) + tl.arange(0, 512)) < 576) & ((((((((((_lv0 * 512) + tl.arange(0, 512)) // 3) % 3) <= (((tl.program_id(0) // 256) % 256) + 1)) & (0 == 0)) & (tl.maximum((((tl.program_id(0) // 256) % 256) + 1) - ((((_lv0 * 512) + tl.arange(0, 512)) // 3) % 3), 0) < 256)) & ((((_lv0 * 512) + tl.arange(0, 512)) % 3) <= ((tl.program_id(0) % 256) + 1))) & (0 == 0)) & (tl.maximum(((tl.program_id(0) % 256) + 1) - (((_lv0 * 512) + tl.arange(0, 512)) % 3), 0) < 256))), (tl.load(in0_ptr + ((((((((tl.program_id(0) // 4194304) * 64) + (((((tl.program_id(0) // 65536) % 64) // 64) * 64) + (((_lv0 * 512) + tl.arange(0, 512)) // 9))) * 256) + tl.maximum((((tl.program_id(0) // 256) % 256) + 1) - ((((_lv0 * 512) + tl.arange(0, 512)) // 3) % 3), 0)) * 256) + tl.maximum(((tl.program_id(0) % 256) + 1) - (((_lv0 * 512) + tl.arange(0, 512)) % 3), 0)) + 0 * tl.arange(0, 512)), mask=((((_lv0 * 512) + tl.arange(0, 512)) < 576) & ((((((((((_lv0 * 512) + tl.arange(0, 512)) // 3) % 3) <= (((tl.program_id(0) // 256) % 256) + 1)) & (0 == 0)) & (tl.maximum((((tl.program_id(0) // 256) % 256) + 1) - ((((_lv0 * 512) + tl.arange(0, 512)) // 3) % 3), 0) < 256)) & ((((_lv0 * 512) + tl.arange(0, 512)) % 3) <= ((tl.program_id(0) % 256) + 1))) & (0 == 0)) & (tl.maximum(((tl.program_id(0) % 256) + 1) - (((_lv0 * 512) + tl.arange(0, 512)) % 3), 0) < 256))), other=0.0) * tl.load(in1_ptr + ((((((((((((tl.program_id(0) // 65536) % 64) // 64) * 64) + (((_lv0 * 512) + tl.arange(0, 512)) // 9)) * 64) + (((tl.program_id(0) // 65536) % 64) % 64)) * 3) + ((((_lv0 * 512) + tl.arange(0, 512)) // 3) % 3)) * 3) + (((_lv0 * 512) + tl.arange(0, 512)) % 3)) + 0 * tl.arange(0, 512)), mask=((((_lv0 * 512) + tl.arange(0, 512)) < 576) & ((((((((((_lv0 * 512) + tl.arange(0, 512)) // 3) % 3) <= (((tl.program_id(0) // 256) % 256) + 1)) & (0 == 0)) & (tl.maximum((((tl.program_id(0) // 256) % 256) + 1) - ((((_lv0 * 512) + tl.arange(0, 512)) // 3) % 3), 0) < 256)) & ((((_lv0 * 512) + tl.arange(0, 512)) % 3) <= ((tl.program_id(0) % 256) + 1))) & (0 == 0)) & (tl.maximum(((tl.program_id(0) % 256) + 1) - (((_lv0 * 512) + tl.arange(0, 512)) % 3), 0) < 256))), other=0.0)), 0.0))
    _v = (tl.sum(_acc0, axis=0) + tl.load(in2_ptr + (((tl.program_id(0) // 65536) % 64))))
    tl.store(out_ptr + tl.program_id(0), _v)


def t010_s0(out, ins):
    grid = (536870912,)
    t010_s0_kernel[grid](out, ins[0], ins[1], ins[2])
    return out


@triton.jit
def t010_s1_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr):
    _acc0 = tl.zeros([4], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = tl.maximum(_acc0, tl.load(in3_ptr + ((((((((tl.program_id(0) // 1048576) * 64) + ((tl.program_id(0) // 16384) % 64)) * 256) + tl.maximum(((((tl.program_id(0) // 128) % 128) * 2) + tl.maximum(((tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - 3, 0), 0) // 2) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 128) % 128) * 2), 0) - (tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - 3, 0), 0) // 2), 0)) - tl.maximum(((tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - 3, 0), 0) // 2) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 128) % 128) * 2), 0) - (tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - 3, 0), 0) // 2), 0)) - tl.maximum(255 - (((tl.program_id(0) // 128) % 128) * 2), 0), 0), 0)) - tl.maximum(((((tl.program_id(0) // 128) % 128) * 2) + tl.maximum(((tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - 3, 0), 0) // 2) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 128) % 128) * 2), 0) - (tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - 3, 0), 0) // 2), 0)) - tl.maximum(((tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - 3, 0), 0) // 2) + tl.maximum(tl.maximum(0 - (((tl.program_id(0) // 128) % 128) * 2), 0) - (tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - 3, 0), 0) // 2), 0)) - tl.maximum(255 - (((tl.program_id(0) // 128) % 128) * 2), 0), 0), 0)) - 255, 0), 0)) * 256) + tl.maximum((((tl.program_id(0) % 128) * 2) + tl.maximum(((tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - 3, 0), 0) % 2) + tl.maximum(tl.maximum(0 - ((tl.program_id(0) % 128) * 2), 0) - (tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - 3, 0), 0) % 2), 0)) - tl.maximum(((tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - 3, 0), 0) % 2) + tl.maximum(tl.maximum(0 - ((tl.program_id(0) % 128) * 2), 0) - (tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - 3, 0), 0) % 2), 0)) - tl.maximum(255 - ((tl.program_id(0) % 128) * 2), 0), 0), 0)) - tl.maximum((((tl.program_id(0) % 128) * 2) + tl.maximum(((tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - 3, 0), 0) % 2) + tl.maximum(tl.maximum(0 - ((tl.program_id(0) % 128) * 2), 0) - (tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - 3, 0), 0) % 2), 0)) - tl.maximum(((tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - 3, 0), 0) % 2) + tl.maximum(tl.maximum(0 - ((tl.program_id(0) % 128) * 2), 0) - (tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - tl.maximum(((_lv0 * 4) + tl.arange(0, 4)) - 3, 0), 0) % 2), 0)) - tl.maximum(255 - ((tl.program_id(0) % 128) * 2), 0), 0), 0)) - 255, 0), 0)))))
    _v = tl.minimum(tl.maximum(tl.max(_acc0, axis=0), (0.0 - (1.0 * (1.0 / 1.0)))), (1.0 * (1.0 / 1.0)))
    tl.store(out_ptr + tl.program_id(0), _v)


def t010_s1(out, ins):
    grid = (134217728,)
    t010_s1_kernel[grid](out, ins[0], ins[1], ins[2], ins[3])
    return out


@triton.jit
def t010_s2_kernel(out_ptr, in0_ptr, in1_ptr, in2_ptr, in3_ptr, in4_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 16):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 16384) & True), tl.load(in4_ptr + (((tl.program_id(0) * 16384) + ((_lv0 * 1024) + tl.arange(0, 1024))) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 16384) & True), other=0.0), 0.0))
    _v = (2.0 * tl.sigmoid(2.0 * ((tl.sum(_acc0, axis=0) * (1.0 * (1.0 / 16384.0))))) - 1.0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t010_s2(out, ins):
    grid = (8192,)
    t010_s2_kernel[grid](out, ins[0], ins[1], ins[2], ins[3], ins[4])
    return out


def t010(out, ins):
    _t0 = torch.empty(536870912, device=ins[0].device, dtype=torch.float32)
    _t1 = torch.empty(134217728, device=ins[0].device, dtype=torch.float32)
    t010_s0(_t0, list(ins))
    t010_s1(_t1, list(ins) + [_t0])
    t010_s2(out, list(ins) + [_t0, _t1])
    return out
