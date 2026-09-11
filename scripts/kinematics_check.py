#!/usr/bin/env python3
"""
Provenance: retroactive archive header added 2026-09-11 by scripts/fix_archive_compliance.py
under the code-archive protocol (docs/PROTOCOL-CODE-ARCHIVE.md, R4).
The analysis itself was performed earlier; this header only records the file's existence
in the committed archive so that the computation is reproducible. Original code below.
"""
# 运动学验证：β(X) 到高 X（5000, 10000）——是否仍精确 = β_ζ − c/X（无高阶？）
import numpy as np
import mpmath as mp
mp.mp.dps = 15

def zeta_smooth_np(s, X, nmax_factor=25):
    nmax = max(int(nmax_factor*X), 300)
    n = np.arange(1, nmax+1, dtype=np.float64)
    logn = np.log(n)
    s_c = complex(s)
    ns = np.exp(-s_c * logn)
    w = np.exp(-n/X)
    return np.sum(ns * w)

def beta_numeric(X, gamma, beta_guess=0.5):
    z = complex(beta_guess, gamma)
    for it in range(80):
        f = zeta_smooth_np(z, X)
        h = 1e-6 + 1e-6j
        fp = (zeta_smooth_np(z+h, X) - zeta_smooth_np(z-h, X)) / (2*h)
        step = f/fp
        z = z - step
        if abs(step) < 1e-11:
            break
    return z.real

# γ₁ 的 c
gamma1 = 14.1347
rho = 0.5 + 1j*gamma1
c1 = -float(mp.re(mp.zeta(rho-1)/mp.zeta(rho, derivative=1)))
print(f"γ₁ = {gamma1}: c = {c1:.4f}")

print("\n=== 运动学精确性：β(X) vs ½ − c/X（推高 X——） ===")
print(f"{'X':>7} {'β_num':>12} {'½−c/X':>12} {'残差':>10} {'(½−β)·X':>10}")
for X in [1000, 2000, 3000, 5000, 8000]:
    b = beta_numeric(X, gamma1)
    pred = 0.5 - c1/X
    resid = abs(b - pred)
    print(f"{X:>7} {b:>12.8f} {pred:>12.8f} {resid:>10.2e} {(0.5-b)*X:>10.4f}")
