#!/usr/bin/env python3
"""验证 E_k 的界：|E_k| ≤ C/(γ_k log³γ_k)——绝对收敛
E_k = ∫_{γ_k}^{γ_{k+1}}(k−N₀)g dt − S_k·g(γ_k)·Δγ_k
"""
import numpy as np
import math
from math import log, pi

def g(t):
    t = np.asarray(t, dtype=float)
    return 2*pi/(t*np.log(t/(2*pi))**2)

def load_zeros(n):
    path = '/home/node/.openclaw/workspace/dn-project/zeros/zeros6'
    z = np.zeros(n)
    with open(path) as f:
        for i in range(n):
            z[i] = float(f.readline())
    return z

K = 200000
z = load_zeros(K)

def N0(t):
    t = np.asarray(t, dtype=float)
    return (t/(2*pi))*np.log(t/(2*pi)) - t/(2*pi) + 7/8

S_k = np.array([(k+1) - N0(z[k]) for k in range(K)], dtype=float)
from numpy.polynomial.legendre import leggauss
xg, wg = leggauss(8)

# 计算每个区间的 E_k（采样——每 20 个区间）
print("E_k 的界验证（|E_k| vs 1/(γ log³γ)）：")
ratio_sum = 0.0
E_samples = []
for k in range(0, K-1, 20):
    a, b = z[k], z[k+1]
    ts = 0.5*(b-a)*xg + 0.5*(a+b)
    S_vals = (k+1) - N0(ts)
    exact = 0.5*(b-a)*np.sum(wg*S_vals*g(ts))
    approx = S_k[k]*g(a)*(b-a)
    Ek = exact - approx
    bound = 1.0/(a*log(a)**3)
    ratio = abs(Ek)/bound
    ratio_sum += abs(Ek)*20  # 补偿采样——Σ|E_k| 估计
    E_samples.append((a, Ek, bound, ratio))

print(f"  Σ|E_k|（采样估计）≈ {ratio_sum:.4f}（应 < C·∫1/(t log³t)dt ~ 有限）")
print(f"  采样点 |E_k|/bound 的 max = {max(e[3] for e in E_samples):.3f}")
print(f"  前几个 E_k：")
for a, Ek, bd, r in E_samples[:5]:
    print(f"    γ={a:10.2f}: E_k={Ek:+.6f}  bound={bd:.6f}  比值={r:.3f}")

# Σ|E_k| 的真正收敛性——看累积
print(f"\nΣ|E_k| 累积（采样）：")
cum = 0.0
for i, (a, Ek, bd, r) in enumerate(E_samples):
    cum += abs(Ek)*20
    if i in [49, 99, 199, 499, 999, 4999, 9999]:
        print(f"  到 γ≈{a:10.2f}: Σ|E_k| ≈ {cum:.4f}")
