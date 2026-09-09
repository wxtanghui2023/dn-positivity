#!/usr/bin/env python3
"""验证: Sbar 的非周期残差 R 与零点间距偏差 δ_k 的关系
δ_k = Δγ_k - 1/N0'(γ_k)——Σδ_k = O(1)（8/23 无条件——）
若 R ~ δ 的函数——R 的积分 O(1) 可从 Σδ=O(1) 推——
"""
import numpy as np
from math import log, pi

path = 'zeros/zeros6'
K = 100000
z = np.zeros(K)
with open(path) as f:
    for i in range(K):
        z[i] = float(f.readline())

dg = np.diff(z[:K])
def IntN0(t):
    if t <= 1: return 0.0
    return t*t/(4*pi)*log(t/(2*pi)) - 3*t*t/(8*pi) + 7*t/8
kk = np.arange(1, K)
IntN = np.array([IntN0(t) for t in z[:K]])
Sbar = kk - (IntN[1:] - IntN[:-1])/dg
t_mid = (z[:-1] + z[1:])/2

# δ_k（间距偏差——）
N0p = np.array([log(t/(2*pi))/(2*pi) for t in t_mid])  # N0'(t) = (1/2π)log(t/2π)
delta = dg - 1.0/N0p

# 非周期残差 R（P≤199 拟合后——）
primes = []
for n in range(2, 200):
    if all(n % p for p in primes if p*p <= n):
        primes.append(n)
cols = []
for p in primes:
    cols.append(np.sin(t_mid * log(p)))
    cols.append(np.cos(t_mid * log(p)))
X = np.stack(cols, axis=1)
coef, _, _, _ = np.linalg.lstsq(X, Sbar, rcond=None)
R = Sbar - X @ coef

print('=== R（非周期残差）与 δ_k 的关系 ===')
print(f'R std={R.std():.4f}——δ std={delta.std():.4f}——mean|δ|={np.mean(np.abs(delta)):.4f}')

# 1. R 与 δ 的相关（逐点——）
c = np.corrcoef(R, delta)[0,1]
print(f'R vs δ 相关: {c:+.4f}')

# 2. R 的积分 vs Σδ 的累积——直接对比
cumR = np.cumsum(R * dg)
cumD = np.cumsum(delta)
# 采样点对比
print()
print('累积对比（R 的积分 vs Σδ——）:')
for i in range(0, K, 20000):
    print(f'  零点{i}: ∫R={cumR[i]:+.3f}——Σδ={cumD[i]:+.3f}')
c2 = np.corrcoef(cumR[::100], cumD[::100])[0,1]
print(f'  ∫R vs Σδ 相关: {c2:+.4f}')

# 3. R 与 δ 的差分（Δδ——）或二阶——的关系
# R 的 ρ(2) ~ -0.49——δ 的 ρ(2)？
print()
print('δ 的自相关:')
for lag in [1, 2, 3, 5]:
    c = np.corrcoef(delta[:-lag], delta[lag:])[0,1]
    print(f'  δ ρ({lag}) = {c:+.4f}')

# 4. 直接假设: R_k ~ c·Δδ_k（R 是 δ 的变化率——）？
# 检验 R 与 Δδ = δ_{k+1}-δ_k 的相关
dd = np.diff(delta)
c3 = np.corrcoef(R[:-1], dd)[0,1]
print(f'R vs Δδ 相关: {c3:+.4f}')

# 5. R 与 S(γ_k)（计数误差——）的关系
# S(γ_k) ≈ k - N0(γ_k)——区间平均 Sbar vs 逐点
S_point = kk[:-1] - IntN[:-1]  # N(γ_k^-) - N0 —— 左极限
c4 = np.corrcoef(R, S_point - Sbar)[0,1]
print(f'R vs (S_point - Sbar) 相关: {c4:+.4f}')
