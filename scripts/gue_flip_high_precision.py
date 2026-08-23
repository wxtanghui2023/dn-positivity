#!/usr/bin/env python3
"""高精度确认 p_GUE——是否 = 0.618（黄金比例）？
大样本 GUE 模拟——p_GUE 的精确值——黄金比例验证
"""
import numpy as np
import gc
from math import sqrt

def gue_spacings_fast(N, n_samples, seed=42):
    rng = np.random.default_rng(seed)
    all_s = np.zeros(n_samples*(N-1))
    idx = 0
    for _ in range(n_samples):
        X = rng.standard_normal((N, N))
        Y = rng.standard_normal((N, N))
        A = (X + 1j*Y)/np.sqrt(2)
        H = (A + A.conj().T)/np.sqrt(2)
        eigs = np.sort(np.linalg.eigvalsh(H))
        x = eigs/np.sqrt(N)
        mid = 0.5*(x[:-1]+x[1:])
        rho = np.sqrt(np.maximum(0, 4 - mid**2))/(2*np.pi)
        raw = np.diff(x)
        s = raw * N * rho
        all_s[idx:idx+len(s)] = s
        idx += len(s)
        del A, H, eigs, x, mid, rho, raw, s
        gc.collect()
    return all_s[:idx]

PHI_INV = 0.6180339887

# 大样本：N=400 × 30（12000 间距）
print("大样本 GUE 模拟：")
for N, ns in [(300, 20), (400, 20), (500, 10)]:
    sp = gue_spacings_fast(N, ns, seed=7)
    deltas = sp - 1.0
    sign = np.sign(deltas)
    flips = np.sum(sign[:-1] != sign[1:]) / (len(sign)-1)
    n = len(sign)-1
    err = sqrt(flips*(1-flips)/n)
    print(f"  N={N}×{ns}: n={n:6d}  p = {flips:.6f} ± {err:.5f}")

# 合并所有样本
sp_all = gue_spacings_fast(400, 20, seed=11)
sp_all2 = gue_spacings_fast(300, 20, seed=12)
sp = np.concatenate([sp_all, sp_all2])
deltas = sp - 1.0
sign = np.sign(deltas)
flips = np.sum(sign[:-1] != sign[1:]) / (len(sign)-1)
n = len(sign)-1
err = sqrt(flips*(1-flips)/n)
print(f"\n合并（{len(sp)} 间距）：p = {flips:.6f} ± {err:.5f}")
print(f"1/φ = {PHI_INV:.6f}——差 = {abs(flips-PHI_INV):.5f}（{abs(flips-PHI_INV)/err:.1f}σ）")
print(f"ζ = 0.617554——差 = {abs(flips-0.617554):.5f}（{abs(flips-0.617554)/err:.1f}σ）")

del sp, deltas, sign
gc.collect()
print("内存已释放")
