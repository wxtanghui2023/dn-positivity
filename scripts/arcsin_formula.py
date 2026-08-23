#!/usr/bin/env python3
"""arcsin 公式验证 + GUE vs ζ 的 ρ₁ 对比
p = 1/2 − arcsin(ρ₁)/π（二元高斯近似——从相邻相关）
GUE 的 ρ₁ vs ζ 的 ρ₁ = −0.3496——量化排斥强度差
"""
import numpy as np
import gc
from math import sqrt, asin, pi

# 1. arcsin 公式验证（ζ 数据）
def load_zeros(n):
    path = '/home/node/.openclaw/workspace/dn-project/zeros/zeros6'
    z = np.zeros(n)
    with open(path) as f:
        for i in range(n):
            z[i] = float(f.readline())
    return z

z = load_zeros(1000000)
gz = z[:-1]
dg = np.diff(z)
Np = np.log(gz/(2*pi))/(2*pi)
delta = dg - 1.0/Np
del dg, Np, gz
gc.collect()

d = delta - np.mean(delta)
s2 = np.var(d)
rho1 = np.mean(d[:-1]*d[1:])/s2
p_actual = np.mean(np.sign(delta[:-1]) != np.sign(delta[1:]))
p_arcsin = 0.5 - asin(rho1)/pi
print(f"ζ 数据：")
print(f"  ρ₁ = {rho1:.6f}")
print(f"  实际 p = {p_actual:.6f}")
print(f"  arcsin 公式 p = {p_arcsin:.6f}（差 {abs(p_actual-p_arcsin):.5f}）")

# 2. GUE 的 ρ₁（bulk）
def gue_rho1(N, n_samples, seed=42):
    rng = np.random.default_rng(seed)
    all_rho = []
    all_p = []
    for _ in range(n_samples):
        X = rng.standard_normal((N, N))
        Y = rng.standard_normal((N, N))
        A = (X + 1j*Y)/np.sqrt(2)
        H = (A + A.conj().T)/np.sqrt(2)
        eigs = np.sort(np.linalg.eigvalsh(H))
        x = eigs/np.sqrt(N)
        mid = 0.5*(x[:-1]+x[1:])
        rho_sc = np.sqrt(np.maximum(0, 4 - mid**2))/(2*np.pi)
        s = np.diff(x) * N * rho_sc
        mask = np.abs(mid) < 1.0
        s_c = s[mask]
        if len(s_c) > 3:
            dd = s_c - 1.0
            dd = dd - np.mean(dd)
            v = np.var(dd)
            r1 = np.mean(dd[:-1]*dd[1:])/v
            pp = np.mean(np.sign(dd[:-1]) != np.sign(dd[1:]))
            all_rho.append(r1)
            all_p.append(pp)
        del A, H, eigs, x, mid, rho_sc, s
        gc.collect()
    return np.mean(all_rho), np.mean(all_p)

rho_gue, p_gue = gue_rho1(400, 15, seed=8)
print(f"\nGUE（N=400×15——bulk）：")
print(f"  ρ₁ = {rho_gue:.6f}（ζ: {rho1:.6f}——差 {abs(rho_gue-rho1):.5f}）")
print(f"  p = {p_gue:.6f}（ζ: {p_actual:.6f}）")
print(f"  arcsin 预测（GUE ρ₁）：p = {0.5 - asin(rho_gue)/pi:.6f}")

del delta, d
gc.collect()
print("\n内存已释放")
