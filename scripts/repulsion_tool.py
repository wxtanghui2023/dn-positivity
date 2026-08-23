#!/usr/bin/env python3
"""凸势工具创造：排斥强度 R(t) = Σ1/|t−γ|²（ψ'' 的零点部分——墙的曲率）
想法：S(t) 大（零点聚集）→ R 大（墙密）→ "偏离平衡代价"高
验证：R(t) 与 S(t) 的关系——凸势能否控制 S？
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

def N0(t):
    return (t/(2*pi))*log(t/(2*pi)) - t/(2*pi) + 7/8

# S(t)（零点处）与排斥强度 R(t) = Σ1/|t−γ|²
S_k = np.array([(k+1) - N0(z[k]) for k in range(200000)], dtype=float)

# R(t) 在零点之间（墙密度——曲率）
def repulsion(t, z, W=1000):
    idx = np.searchsorted(z, t)
    lo = max(0, idx-W); hi = min(len(z), idx+W)
    s = 0.0
    for j in range(lo, hi):
        d = t - z[j]
        if abs(d) > 0.5:
            s += 1.0/(d*d)
    return s

# 关键检验：S_k 与"局部墙密度"的关系
print("S(γ_k) 与局部墙密度（零点间距倒数——局部排斥）：")
print(f"{'k':>7} {'S_k':>8} {'dg':>8} {'1/dg':>8} {'dg*Np':>8} {'delta':>8}")
for k in [1000, 5000, 10000, 50000, 100000, 150000]:
    dg = z[k] - z[k-1]
    Np = log(z[k]/(2*pi))/(2*pi)
    delta = dg - 1.0/Np
    print(f"{k:7d} {S_k[k]:+8.3f} {dg:8.4f} {1/dg:8.3f} {dg*Np:8.3f} {delta:+8.3f}")

# 相关：S_k 与 δ_k 或间距
print("\nS(γ_k) 与间距偏差的相关性：")
dg_all = np.diff(z[:200000])
Np_all = np.log(z[:199999]/(2*pi))/(2*pi)
delta_all = dg_all - 1.0/Np_all
# S_k（右极限）与 δ
corr_S_delta = np.corrcoef(S_k[1:], delta_all)[0,1]
corr_S_dg = np.corrcoef(S_k[1:], dg_all)[0,1]
print(f"  corr(S(γ_k), δ_k) = {corr_S_delta:+.4f}")
print(f"  corr(S(γ_k), Δγ_k) = {corr_S_dg:+.4f}")

# 关键：S 与 R（墙密度）的关系——R 大处 S 如何？
print("\nS(γ_k) vs 局部墙密度 R_k（窗口 ±10 的 Σ1/d²）：")
Rs = []
Ss = []
for k in range(100, 199900, 100):
    t = z[k]
    lo = max(0, k-10); hi = min(200000, k+10)
    r = 0.0
    for j in range(lo, hi):
        if j != k:
            r += 1.0/((t-z[j])**2)
    Rs.append(r); Ss.append(S_k[k])
Rs = np.array(Rs); Ss = np.array(Ss)
corr = np.corrcoef(Ss, Rs)[0,1]
print(f"  corr(S, R_局部) = {corr:+.4f}（R 大 = 墙密——S 关系？）")
