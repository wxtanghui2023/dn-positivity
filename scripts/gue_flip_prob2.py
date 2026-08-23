#!/usr/bin/env python3
"""GUE 符号翻转概率（修正版）——标准 GUE 生成
H = (A + A†)/√2——A 条目 = (X+iY)/√2（X,Y ~ N(0,1)）
特征值/N^{1/2} ~ 半圆 [-2, 2]——ρ(x) = √(4−x²)/(2π)
"""
import numpy as np
import gc

def gue_spacings(N, n_samples, seed=42):
    rng = np.random.default_rng(seed)
    all_s = []
    for _ in range(n_samples):
        X = rng.standard_normal((N, N))
        Y = rng.standard_normal((N, N))
        A = (X + 1j*Y)/np.sqrt(2)
        H = (A + A.conj().T)/np.sqrt(2)  # 标准 GUE
        eigs = np.sort(np.linalg.eigvalsh(H))
        # 半圆归一化：x = λ/√N——ρ(x) = √(4−x²)/(2π)——支撑 [-2,2]
        x = eigs/np.sqrt(N)
        mid = 0.5*(x[:-1]+x[1:])
        rho = np.sqrt(np.maximum(0, 4 - mid**2))/(2*np.pi)
        raw = np.diff(x)
        s = raw * N * rho  # 归一化间距（平均 ~1）
        all_s.extend(s)
        del A, H, eigs, x, mid, rho, raw, s
        gc.collect()
    return np.array(all_s)

for (N, ns, seed) in [(200, 10, 1), (300, 10, 2), (400, 5, 3)]:
    sp = gue_spacings(N, ns, seed)
    deltas = sp - 1.0
    sign = np.sign(deltas)
    flips = np.sum(sign[:-1] != sign[1:]) / (len(sign)-1)
    print(f"N={N} × {ns}: 间距数 = {len(sp):6d}  mean(s) = {np.mean(sp):.4f}  p_GUE = {flips:.6f}")

print(f"\nζ 的 p = 0.617554")
