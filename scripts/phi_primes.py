#!/usr/bin/env python3
"""推导 φ（S 的回归系数）从素数项加权平均
S(t) = −(1/π)Σ_p sin(t log p)/(√p log p)——Titchmarsh
φ = E[corr(S_{k+1}, S_k)] ≈ Σ_p cos(log p·⟨Δγ⟩)·⟨sin²⟩/(p log²p) / Σ_p ⟨sin²⟩/(p log²p)
⟨Δγ⟩ = 1/N₀'(T)——cos 的加权平均——小 p 主导（cos~1）——φ>0
"""
import numpy as np
import gc
from math import log, pi

def primes_upto(n):
    sieve = np.ones(n+1, dtype=bool); sieve[:2]=False
    for i in range(2, int(n**0.5)+1):
        if sieve[i]: sieve[i*i::i]=False
    return np.nonzero(sieve)[0]

# 1. φ 的素数项预测
def phi_pred(T, pmax):
    Np_T = log(T/(2*pi))/(2*pi)
    avg_dg = 1.0/Np_T
    ps = primes_upto(pmax)
    logp = np.log(ps)
    w = 1.0/(ps * logp**2)  # 权重（⟨sin²⟩=1/2 常数——抵消）
    cos_w = np.cos(logp * avg_dg)
    return np.sum(w * cos_w)/np.sum(w), avg_dg

# 不同 pmax（截断——收敛性）
print("φ 的素数项预测（加权平均 cos）：")
for pmax in [100, 1000, 10000, 100000]:
    phi, avg_dg = phi_pred(1000000, pmax)
    print(f"  p≤{pmax:6d}: φ_pred = {phi:.6f}（⟨Δγ⟩ = {avg_dg:.4f}）")

# 2. 实测 φ（S 的回归）
def load_zeros(n):
    path = '/home/node/.openclaw/workspace/dn-project/zeros/zeros6'
    z = np.zeros(n)
    with open(path) as f:
        for i in range(n):
            z[i] = float(f.readline())
    return z

z = load_zeros(1000000)
def N0(t):
    return (t/(2*pi))*log(t/(2*pi)) - t/(2*pi) + 7/8
S_k = np.array([(k+1) - N0(z[k]) for k in range(1000000)], dtype=float)
del z
gc.collect()
s = S_k - np.mean(S_k)
g0 = np.var(s)
g1 = np.mean(s[:-1]*s[1:])
phi_actual = g1/g0
print(f"\n实测：φ = {phi_actual:.6f}")

# 3. 修正：Δγ 的分布（不只是平均）——⟨cos(log p·Δγ_k)⟩ 逐点平均
print("\n修正：用实际 Δγ 分布（逐点 ⟨cos⟩）：")
z2 = load_zeros(1000000)
dg_arr = np.diff(z2)
del z2
gc.collect()
ps = primes_upto(10000)
logp = np.log(ps)
w = 1.0/(ps * logp**2)
cos_vals = np.zeros(len(ps))
for i, lp in enumerate(logp):
    cos_vals[i] = np.mean(np.cos(lp * dg_arr))
phi_corr = np.sum(w * cos_vals)/np.sum(w)
print(f"  φ_pred（分布修正）= {phi_corr:.6f} vs 实测 {phi_actual:.6f}")
print(f"  （cos 加权平均——小 p 主导 cos~1——φ>0 回归）")

del dg_arr, s, S_k
gc.collect()
print("内存已释放")
