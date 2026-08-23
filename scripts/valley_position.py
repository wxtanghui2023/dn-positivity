#!/usr/bin/env python3
"""凸势工具：谷底位置（ψ 最小值在区间内）与 S(γ_k) 的关系
想法：S 大（零点靠前）→ 谷底偏移？→ δ 补偿结构
如果谷底位置 ≈ 0.5 − c·S_k——凸势给出 δ 补偿的几何推导
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

z = load_zeros(50000)

def N0(t):
    return (t/(2*pi))*log(t/(2*pi)) - t/(2*pi) + 7/8

S_k = np.array([(k+1) - N0(z[k]) for k in range(len(z))], dtype=float)

# ψ' = −Σ1/(t−γ) − θ'——谷底（ψ'=0）在 [γ_{k-1}, γ_k] 内
def psi_prime(t, z, W=500):
    idx = np.searchsorted(z, t)
    lo = max(0, idx-W); hi = min(len(z), idx+W)
    s = 0.0
    for j in range(lo, hi):
        d = t - z[j]
        if abs(d) > 0.5:
            s += 1.0/d
    return -s - 0.5*log(t/(2*pi))  # ψ' = −Σ1/(t−γ) − θ'

# 谷底位置 vs S_k
fracs = []
Svals = []
for k in range(500, 49000, 20):
    a, b = z[k-1], z[k]
    if b - a < 0.3: continue  # 太窄跳过
    ts = np.linspace(a+0.3, b-0.3, 12)
    pps = [psi_prime(t, z) for t in ts]
    for i in range(len(ts)-1):
        if pps[i]*pps[i+1] < 0:
            t_star = 0.5*(ts[i]+ts[i+1])
            fracs.append((t_star-a)/(b-a))
            Svals.append(S_k[k])
            break

fracs = np.array(fracs); Svals = np.array(Svals)
print(f"谷底位置 vs S(γ_k)：{len(fracs)} 个样本")
print(f"  平均谷底 = {np.mean(fracs):.4f}  std = {np.std(fracs):.4f}")
print(f"  corr(谷底位置, S_k) = {np.corrcoef(fracs, Svals)[0,1]:+.4f}")

# 分组看：S 大 vs S 小 的谷底位置
S_hi = Svals > np.median(Svals)
S_lo = Svals <= np.median(Svals)
print(f"  S 大（>中位数）：平均谷底 = {np.mean(fracs[S_hi]):.4f}")
print(f"  S 小（≤中位数）：平均谷底 = {np.mean(fracs[S_lo]):.4f}")

# 拟合：谷底 ≈ 0.5 − c·(S−½)？
A = np.vstack([Svals - 0.5, np.ones(len(Svals))]).T
coef = np.linalg.lstsq(A, fracs - 0.5, rcond=None)[0]
print(f"  谷底 − 0.5 ≈ {coef[0]:.3f}·(S_k − ½) + {coef[1]:.4f}")
print(f"  （如果 c < 0——S 大 → 谷底偏前——补偿）")

# 理论预测：谷底位置与 δ 的关系
# 如果谷底 ≈ 区间中点（0.5）——零点在墙之间对称——δ 无偏差
# 如果谷底偏移——零点"重心"偏移——δ 补偿
print("\n谷底位置（几何）与 δ_k 的关系：")
deltas = []
for k in range(500, 49000, 20):
    a, b = z[k-1], z[k]
    if b - a < 0.3: continue
    Np = log(z[k]/(2*pi))/(2*pi)
    deltas.append((b-a) - 1.0/Np)
deltas = np.array(deltas[:len(fracs)])
print(f"  corr(谷底位置, δ_k) = {np.corrcoef(fracs, deltas)[0,1]:+.4f}")
