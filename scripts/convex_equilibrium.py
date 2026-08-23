#!/usr/bin/env python3
"""凸势深入：平衡条件 Σ1/(γ−t) = θ'(t) 的大 t 渐近——GUE 凸方法的正确版本
验证：大 t 处平衡是否渐近成立？——以及"零点是凸势 ψ 的平衡配置"？
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

z = load_zeros(200000)

# 平衡条件：Σ_{j} 1/(γ_j−t) = θ'(t)——在零点之间
print("凸势平衡条件 Σ1/(γ_j−t) vs θ'(t)（零点之间——大 t）：")
print(f"{'t(mid)':>12} {'Sum 1/(g-t)':>12} {'theta_p':>10} {'ratio':>8}")
for k in [1000, 5000, 10000, 50000, 100000, 150000]:
    if k >= len(z)-1: break
    mid = 0.5*(z[k-1]+z[k])
    g = z
    vals = 1.0/(g - mid)
    mask = np.abs(g-mid) > 0.5
    s = np.sum(vals[mask])
    tp = 0.5*log(mid/(2*pi)) + 1.0/(48*mid*mid)
    ratio = s/tp if tp != 0 else 0
    print(f"{mid:12.2f} {s:+12.4f} {tp:+10.4f} {ratio:8.3f}")

# 全范围 vs 局部（窗口效应）
print("\n窗口效应（t≈γ_50000 中点）：")
mid = 0.5*(z[49999]+z[50000])
for W in [100, 500, 2000, 10000, 50000]:
    idx = np.searchsorted(z, mid)
    lo = max(0, idx-W); hi = min(len(z), idx+W)
    s = 0.0
    for j in range(lo, hi):
        d = mid - z[j]
        if abs(d) > 0.5:
            s += 1.0/d
    print(f"  窗口 ±{W:6d}: Σ1/(γ−t) = {s:+.4f}")

# 关键：Σ1/(γ−t) 的"主项"——如果零点"均匀密度"——Σ1/(γ−t) 的主项
# 均匀密度 ρ(t) = N₀'(t)——Σ1/(γ−t) ~ PV∫ρ(x)/(x−t)dx——主值积分
# 对 ρ(x) = log(x/2π)/2π——PV∫ρ/(x−t)dx——这是 Hilbert 变换！
print("\n主值积分（Hilbert 变换）vs 数值：")
from scipy.integrate import quad
for t in [500, 1000, 5000]:
    # PV∫_2^∞ ρ(x)/(x−t)dx——ρ = N₀'
    def integrand(x):
        return (log(x/(2*pi))/(2*pi))/(x-t)
    # 主值（对称跳过 t）
    val1, _ = quad(integrand, 2, t-0.5, limit=200)
    val2, _ = quad(integrand, t+0.5, 1e7, limit=200)
    pv = val1 + val2
    tp = 0.5*log(t/(2*pi))
    print(f"  t={t:5d}: PV∫ρ/(x−t)dx = {pv:+.4f} vs θ' = {tp:+.4f}")
