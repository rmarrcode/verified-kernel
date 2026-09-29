import torch
import triton
import triton.language as tl


@triton.jit
def t039_s1_kernel(out_ptr, in0_ptr):
    _acc0 = tl.zeros([1024], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 64):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1024) + tl.arange(0, 1024)) < 65535) & True), (tl.load(in0_ptr + ((((((tl.program_id(0) // 1) * 65535) + ((_lv0 * 1024) + tl.arange(0, 1024))) * 1) + (tl.program_id(0) % 1)) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 65535) & True), other=0.0) * tl.load(in0_ptr + ((((((tl.program_id(0) // 1) * 65535) + ((_lv0 * 1024) + tl.arange(0, 1024))) * 1) + (tl.program_id(0) % 1)) + 0 * tl.arange(0, 1024)), mask=((((_lv0 * 1024) + tl.arange(0, 1024)) < 65535) & True), other=0.0)), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t039_s1(out, ins):
    grid = (4096,)
    t039_s1_kernel[grid](out, ins[0])
    return out


@triton.jit
def t039_s2_kernel(out_ptr, in0_ptr, in1_ptr):
    _acc0 = tl.zeros([1], dtype=tl.float32) + (0.0)
    for _lv0 in range(0, 1):
        _acc0 = (_acc0 + tl.where(((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), (tl.load(in0_ptr + (tl.program_id(0) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0) / tl.sqrt(tl.load(in1_ptr + ((((tl.program_id(0) // (65535 * 1)) * 1) + (tl.program_id(0) % 1)) + 0 * tl.arange(0, 1)), mask=((((_lv0 * 1) + tl.arange(0, 1)) < 1) & True), other=0.0))), 0.0))
    _v = tl.sum(_acc0, axis=0)
    tl.store(out_ptr + tl.program_id(0), _v)


def t039_s2(out, ins):
    grid = (268431360,)
    t039_s2_kernel[grid](out, ins[0], ins[1])
    return out


def t039(out, ins):
    _tmp = torch.empty(4096, device=ins[0].device, dtype=torch.float32)
    t039_s1(_tmp, ins)
    t039_s2(out, list(ins) + [_tmp])
    return out
