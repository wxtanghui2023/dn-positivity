#!/usr/bin/env python3
"""GUE bulk 区域 p——排除边缘效应（半圆边缘间距异常）
只用中心区域（x ∈ [-c, c]）的间距——p_bulk vs ζ 的 0.618
"""
import numpy as np
import gc
from math import sqrt

def gue_bulk_flip(N, n_samples, c=1.0, seed=42):
    """GUE 中心区域（|x| < c）的相邻间距——符号翻转概率"""
    rng = np.random.default_rng(seed)
    total_flips = 0
    total_n = 0
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
        # 只保留中心区域（|mid| < c）
        mask = np.abs(mid) < c
        s_c = s[mask]
        if len(s_c) > 1:
            d = s_c - 1.0
            sign = np.sign(d)
            flips = np.sum(sign[:-1] != sign[1:])
            total_flips += flips
            total_n += len(sign) - 1
        del A, H, eigs, x, mid, rho, raw, s
        gc.collect()
    return total_flips, total_n

print("GUE bulk（|x| < c）的符号翻转概率：")
for c in [0.5, 1.0, 1.5]:
    flips, n = gue_bulk_flip(400, 20, c=c, seed=5)
    p = flips/n
    err = sqrt(p*(1-p)/n)
    print(f"  c={c}: n={n:6d}  p = {p:.6f} ± {err:.5f}")

print(f"\nζ 的 p = 0.617554（1/φ = 0.618034）")
