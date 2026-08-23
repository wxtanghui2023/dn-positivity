#!/usr/bin/env python3
"""γ(1) 的素数项推导：cov(S_k, S_{k+1}) ≈ (1/π²)Σ_p cos(log p·Δγ)/(p log²p)·修正
S(t) ≈ −(1/π)Σ_p sin(t log p)/(√p log p)——Titchmarsh 主项
相邻零点：sin(γ_k log p)sin(γ_{k+1} log p) ≈ sin²(γ_k log p)·cos(log p·Δγ)——Δγ~1/N₀'
"""
import numpy as np
import gc
from math import log, pi

def load_zeros(n):
    path = '/home/node/.openclaw/workspace/dn-project/zeros/zeros6'
    z = np.zeros(n)
    with open(path) as f:
        for i in range(n):
            z[i] = float(f.readline())
    return z

def primes_upto(n):
    sieve = np.ones(n+1, dtype=bool); sieve[:2]=False
    for i in range(2, int(n**0.5)+1):
        if sieve[i]: sieve[i*i::i]=False
    return np.nonzero(sieve)[0]

# γ(1) 的素数项预测
# γ(1) = cov(S_k, S_{k+1}) ≈ (1/π²)Σ_p cos(log p·⟨Δγ⟩)/(p log²p)·⟨sin²⟩
# ⟨sin²(γ log p)⟩ = 1/2（均匀相位）
# ⟨Δγ⟩ = 平均间距 = 1/N₀'(T)
T = 1000000
Np_T = log(T/(2*pi))/(2*pi)
avg_dg = 1.0/Np_T

ps = primes_upto(200000)
# 修正：cos(log p·Δγ) 需要 log p·Δγ < ~1 的 p（否则振荡抵消）
logp = np.log(ps)
cos_term = np.cos(logp * avg_dg)
# 相位均匀性修正：⟨sin²⟩ = 1/2——但实际相位非均匀（S 结构）——先用 1/2
pred_g1 = (1/(pi*pi)) * np.sum(cos_term/(ps*logp**2)) * 0.5
print(f"γ(1) 素数项预测（T=1e6——Δγ = {avg_dg:.4f}）：")
print(f"  Σ_p cos(log p·Δγ)/(p log²p) = {np.sum(cos_term/(ps*logp**2)):.6f}")
print(f"  γ(1)_pred = {pred_g1:.6f}")

# 实测
z = load_zeros(500000)
def N0(t):
    return (t/(2*pi))*log(t/(2*pi)) - t/(2*pi) + 7/8
S_k = np.array([(k+1) - N0(z[k]) for k in range(500000)], dtype=float)
s = S_k - np.mean(S_k)
g1_meas = np.mean(s[:-1]*s[1:])
g0_meas = np.var(s)
print(f"实测：γ(1) = {g1_meas:.6f}  γ(0) = {g0_meas:.6f}  φ = {g1_meas/g0_meas:.4f}")

# 修正：⟨sin²⟩ 不是 1/2（S 的结构）——用实际相位
# 更精确：γ(1) = (1/π²)Σ_p Σ_q ⟨sin(γ_k log p)sin(γ_{k+1} log q)⟩/(√p√q log p log q)
# 对角 p=q 主导：≈ (1/π²)Σ_p ⟨sin(γ_k log p)sin(γ_{k+1} log p)⟩/(p log²p)
# = (1/π²)Σ_p cos(log p·Δγ_k)⟨sin²(γ_k log p)⟩/(p log²p)——Δγ_k 逐点
# 用代表性值：⟨cos(log p·Δγ_k)⟩——Δγ_k 的分布
print(f"\n更精确：考虑 Δγ_k 的分布（非平均）：")
# 从数据算 ⟨cos(log p·Δγ_k)⟩ 对若干 p
z2 = load_zeros(500000)
dg_arr = np.diff(z2)
for p in [2, 3, 5, 11, 101]:
    avg_cos = np.mean(np.cos(log(p)*dg_arr[:len(dg_arr)//2]))
    print(f"  p={p:4d}: ⟨cos(log p·Δγ)⟩ = {avg_cos:.6f}（预测 cos(log p·⟨Δγ⟩) = {np.cos(log(p)*avg_dg):.6f}）")

del z, z2, s, S_k, dg_arr
gc.collect()
print("内存已释放")
