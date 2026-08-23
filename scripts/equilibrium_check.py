#!/usr/bin/env python3
"""探索凹势方向：ζ 零点是否是完整势（零点 + Γ 主项）的平衡配置？
完整势：φ(t) = Σ_{γ≠t} log|t−γ| + θ(t)（Γ 主项——Riemann-Siegel θ）
平衡条件：φ'(t) = 0——Σ_{γ≠t} 1/(t−γ) + θ'(t) = 0
验证：在零点 γ_k 处（跳过自己）——Σ_{j≠k}1/(γ_k−γ_j) ≈ −θ'(γ_k)？
"""
import numpy as np
import math
from math import log, pi

def load_zeros(n):
    path = '/home/node/.openclaw/workspace/dn-project/zeros/zeros6'
    z = np.zeros(n)
    with open(path) as f:
        for i in range(n):
            z[i] = float(f.readline())
    return z

z = load_zeros(20000)

# Riemann-Siegel θ(t)：θ(t) = Im log Γ(¼+it/2) − (t/2)log π
# θ'(t) ≈ (1/2)log(t/2π)（Stirling 主项）——更精确：
def theta_prime(t):
    # θ'(t) = (1/2)ψ(¼+it/2) + (1/2)ψ(¼−it/2) − (1/2)log π（ψ 是 digamma）
    # 用 Stirling：θ'(t) ≈ (1/2)log(t/2π) + 1/(48t²)·... 
    return 0.5*log(t/(2*pi)) + 1.0/(48*t*t)  # 主项 + 修正

# 平衡条件：Σ_{j≠k} 1/(γ_k−γ_j) ≈ −θ'(γ_k)？
print("平衡条件验证：Σ_{j≠k}1/(γ_k−γ_j) vs −θ'(γ_k)")
print(f"{'k':>6} {'gamma_k':>10} {'Sum 1/(gk-gj)':>14} {'-theta_p':>12} {'ratio':>8}")
for k in [100, 500, 1000, 2000, 5000, 10000]:
    gk = z[k]
    # Σ_{j≠k} 1/(γ_k−γ_j)——Cauchy 主值（跳过自己——两边对称）
    g = z
    idx = k
    # 用局部窗口（远离的贡献小——1/(γ_k−γ_j) ~ 1/(大距离)）
    # 但全部求和收敛慢——用部分：前后各 5000
    lo = max(0, idx-5000); hi = min(len(g), idx+5000)
    s = 0.0
    for j in range(lo, hi):
        if j != idx:
            s += 1.0/(gk - g[j])
    tp = theta_prime(gk)
    print(f"{k:6d} {gk:10.3f} {s:+14.4f} {-tp:+12.4f} {s/(-tp) if tp!=0 else 0:8.3f}")

# 更精确：全范围（向量化——避免循环）
print("\n全范围平衡条件（向量化）：")
for k in [1000, 5000, 10000]:
    gk = z[k]
    g = z
    # 1/(gk−g)——全向量（跳过 k）
    vals = 1.0/(gk - g)
    vals[k] = 0.0  # 跳过自己
    s = np.sum(vals)
    tp = theta_prime(gk)
    print(f"  γ_{k} = {gk:.3f}: Σ1/(γ_k−γ_j) = {s:+.4f} vs −θ' = {-tp:+.4f}（比值 {s/(-tp):.3f}）")
