#!/usr/bin/env python3
"""消解构造: M(T) = 绝对收敛素数项——追 E = M - M_main 的逐素数分解
M_main(T) = -(1/π)Σ_p (1-cos(T log p))/(√p log²p)·(2π/π? 校对)
目标: E(T) = M(T) - M_main(T) 是否 = Σ_p e_p(T)（绝对可和——）？
如果 E 闭合到常数 + 绝对收敛尾——M 完全消解为素数项——
"""
import numpy as np
from math import log, pi

# 零点数据
z = np.load('/tmp/zeros_odlyzko_2M.npy')
K = min(len(z), 100000)
z = z[:K]

def N0(t):
    return (t/(2*pi))*(log(t/(2*pi)) - 1) + 7.0/8
N0v = np.array([N0(t) for t in z])
S_k = np.arange(1, K+1) - N0v  # S(γ_k+)

# M(T) = Σ_{γ_k ≤ T}(T - γ_k) - ∫_0^T N0(t)dt（S₁ 的零点矩形式——）
# 在零点处: M_k = M(γ_k)——用累积
# S₁(γ_k) ≈ Σ_{j≤k}(γ_k - γ_j) - ∫N0——先算 ∫N0（原函数——）
def I_N0(t):
    # ∫N0 dt——N0 = (t/2π)(log(t/2π)-1) + 7/8
    # ∫ = (t²/4π)(log(t/2π) - 3/2) + 7t/8——（验证——）
    return (t*t/(4*pi))*(log(t/(2*pi)) - 1.5) + 7.0*t/8

# 高效: S₁(T) = Σ_{γ≤T}(T-γ)/π·?——用标准定义 M(T)=∫₀^T S(t)dt ≈ S₁
# S₁(γ_k) = Σ_{j<k}(γ_k-γ_j) 的涨落部分——直接累积 dS 的加权
# M_k = Σ_{j<k} ΔS_j·(γ_k - γ_j) 的——不对——用 S₁ 的差分:
# S₁'(t) = S(t)——M(γ_k) = ∫₀^{γ_k}S = Σ_{j<k}∫_{γ_j}^{γ_{j+1}}S——分段（S 连续版——）
# 简化: M_k ≈ Σ_{j<k} S̄_j·Δγ_j（S̄_j = 区间平均——≈ (S(γ_j)+S(γ_{j+1}))/2——）
S_mid = (S_k[:-1] + S_k[1:])/2 - 0.5  # 去 0.5 偏移（S̄ mean≈0——）
dg = np.diff(z)
M_k = np.cumsum(S_mid * dg)  # M(γ_k) 的近似（积分——）

# M_main(T) = -(1/π)Σ_p (1-cos(T log p))/(√p log²p)
def M_main(T, pmax):
    total = 0.0
    for p in primes_below(pmax):
        total += (1 - np.cos(T*log(p)))/(np.sqrt(p)*log(p)**2)
    return -total/pi

# 素数（试除筛——到 pmax——）
def primes_below(n):
    sieve = np.ones(n, dtype=bool)
    sieve[:2] = False
    for i in range(2, int(n**0.5)+1):
        if sieve[i]:
            sieve[i*i::i] = False
    return np.nonzero(sieve)[0]

pmax = 200000
pr = primes_below(pmax)

# E(T) = M(T) - M_main(T)——在采样点（每 5000 零点——）
print('=== E = M - M_main 的闭合测试 ===')
idxs = np.arange(0, K, 5000, dtype=int)
for i in idxs:
    T = z[i]
    Mm = M_main(T, pmax)
    E = M_k[i] - Mm
    print(f'  γ={T:.0f}（零点{i}）: M={M_k[i]:+.3f}——M_main(p<{pmax})={Mm:+.3f}——E={E:+.3f}')

# M_main 的 pmax 收敛（尾部——）
print()
print('M_main 尾部（高 p——）:')
T0 = z[50000]
for pm in [1000, 10000, 50000, pmax]:
    Mm = M_main(T0, pm)
    print(f'  pmax={pm}: M_main={Mm:+.4f}')
