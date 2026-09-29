import torch
import triton
import triton.language as tl


@triton.jit
def t052_s1_kernel(out_ptr, in0_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (((0.0 * (1.0 / 1.0)) - tl.load(in0_ptr + ((((((tl.program_id(0) // 4095) * 4096) + 0) * 4095) + (tl.program_id(0) % 4095))))))
    for _lv0 in range(0, 4):
        _acc0 = tl.maximum(_acc0, ((0.0 * (1.0 / 1.0)) - tl.load(in0_ptr + ((((((tl.program_id(0) // 4095) * 4096) + tl.maximum(((_lv0 * 1024) + tl.arange(0, 1024)) - tl.maximum(((_lv0 * 1024) + tl.arange(0, 1024)) - 4095, 0), 0)) * 4095) + (tl.program_id(0) % 4095))))))
    _v = ((0.0 * (1.0 / 1.0)) - tl.max(_acc0, axis=0))
    tl.store(out_ptr + tl.program_id(0), _v)


def t052_s1(out, ins):
    grid = (262080,)
    t052_s1_kernel[grid](out, ins[0])
    return out


@triton.jit
def t052_s2_kernel(out_ptr, in0_ptr, in1_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (((0.0 * (1.0 / 1.0)) - tl.where(tl.load(in0_ptr + ((((((tl.program_id(0) // 4095) * 4096) + 0) * 4095) + (tl.program_id(0) % 4095)))) <= tl.load(in1_ptr + (tl.program_id(0))), tl.where(tl.load(in1_ptr + (tl.program_id(0))) <= tl.load(in0_ptr + ((((((tl.program_id(0) // 4095) * 4096) + 0) * 4095) + (tl.program_id(0) % 4095)))), 0.0, (4096.0 * (1.0 / 1.0))), (4096.0 * (1.0 / 1.0)))))
    for _lv0 in range(0, 4):
        _acc0 = tl.maximum(_acc0, ((0.0 * (1.0 / 1.0)) - tl.where(tl.load(in0_ptr + ((((((tl.program_id(0) // 4095) * 4096) + tl.maximum(((_lv0 * 1024) + tl.arange(0, 1024)) - tl.maximum(((_lv0 * 1024) + tl.arange(0, 1024)) - 4095, 0), 0)) * 4095) + (tl.program_id(0) % 4095)))) <= tl.load(in1_ptr + (tl.program_id(0))), tl.where(tl.load(in1_ptr + (tl.program_id(0))) <= tl.load(in0_ptr + ((((((tl.program_id(0) // 4095) * 4096) + tl.maximum(((_lv0 * 1024) + tl.arange(0, 1024)) - tl.maximum(((_lv0 * 1024) + tl.arange(0, 1024)) - 4095, 0), 0)) * 4095) + (tl.program_id(0) % 4095)))), (tl.maximum(((_lv0 * 1024) + tl.arange(0, 1024)) - tl.maximum(((_lv0 * 1024) + tl.arange(0, 1024)) - 4095, 0), 0)).to(tl.float32), (4096.0 * (1.0 / 1.0))), (4096.0 * (1.0 / 1.0)))))
    _v = ((0.0 * (1.0 / 1.0)) - tl.max(_acc0, axis=0))
    tl.store(out_ptr + tl.program_id(0), _v)


def t052_s2(out, ins):
    grid = (262080,)
    t052_s2_kernel[grid](out, ins[0], ins[1])
    return out


def t052(out, ins):
    _tmp = torch.empty(262080, device=ins[0].device, dtype=torch.float32)
    t052_s1(_tmp, ins)
    t052_s2(out, list(ins) + [_tmp])
    return out
