#!/usr/bin/env python3
"""探索凸势：ψ(t) = −φ_total(t) = Σ_γ log(1/|t−γ|) − θ(t)——凹变凸（唐先生洞察）
ψ 是凸函数（零点处 +∞——凸尖峰——ψ'' = Σ1/(t−γ)² − θ'' > 0）
GUE 凸方法：凸函数的最小值（唯一平衡）——零点与 ψ 的关系
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

z = load_zeros(10000)

# ψ(t) = Σ_γ log(1/|t−γ|) − θ(t)——用局部窗口（log 奇点——跳过近零点）
def psi(t, z, W=500):
    """凸势（局部——跳过 |t−γ|<0.5 的奇点）"""
    idx = np.searchsorted(z, t)
    lo = max(0, idx-W); hi = min(len(z), idx+W)
    s = 0.0
    for j in range(lo, hi):
        d = abs(t - z[j])
        if d > 0.5:
            s += log(1.0/d)
    # −θ(t)：θ(t) ≈ (t/2)log(t/2π) − t/2 + π/8（Stirling——但这里用导数关系）
    # ψ 的常数部分不重要——看形状
    return s

def psi_second(t, z, W=500):
    """ψ''(t) = Σ1/(t−γ)² − θ''(t)——凸性检验"""
    idx = np.searchsorted(z, t)
    lo = max(0, idx-W); hi = min(len(z), idx+W)
    s = 0.0
    for j in range(lo, hi):
        d = t - z[j]
        if abs(d) > 0.5:
            s += 1.0/(d*d)
    # θ''(t) ~ 1/(2t)（Riemann-Siegel——Stirling）——小
    return s - 1.0/(2*t)

# 1. 凸性验证：ψ'' > 0？
print("ψ''(t) 的凸性检验（应 > 0）：")
for t in [50, 100, 200, 500, 1000, 2000, 5000]:
    # 零点之间的点
    idx = np.searchsorted(z, t)
    if idx > 0 and idx < len(z):
        mid = 0.5*(z[idx-1]+z[idx])
        d2 = psi_second(mid, z)
        print(f"  t={mid:10.2f}: ψ'' = {d2:+.4f}（{'凸' if d2>0 else '凹'}）")

# 2. ψ 的形状——最小值在哪？
print("\nψ(t) 的形状（凸函数——最小值位置）：")
t_vals = [30, 50, 80, 100, 150, 200, 300, 500]
psi_vals = [(t, psi(t, z)) for t in t_vals]
for t, p in psi_vals:
    print(f"  t={t:5d}: ψ = {p:+.4f}")

# 3. 关键：ψ 的"平衡"（凸最小化）——梯度 ψ' = Σ1/(γ−t) − θ' = 0
print("\n凸势 ψ 的平衡条件（ψ' = 0——凸最小化）：")
for t in [100, 500, 1000]:
    idx = np.searchsorted(z, t)
    mid = 0.5*(z[idx-1]+z[idx]) if idx>0 else t
    # ψ'(t) = −φ_total'(t) = −Σ1/(t−γ) + θ'(t)（符号——检查）
    # 平衡：Σ1/(γ−t) = θ'(t)？
    g = z
    vals = 1.0/(g - mid)
    mask = np.abs(g-mid) > 0.5
    s = np.sum(vals[mask])
    theta_p = 0.5*log(mid/(2*pi))
    print(f"  t={mid:10.2f}: Σ1/(γ−t) = {s:+.4f} vs θ' = {theta_p:+.4f}")
