#!/usr/bin/env python3
"""完备性极限: 加更多谐波和高频——残差 → 0?
S̄ = Σ_{p,k} a_{p,k} sin(k log p · t)——测试残差的极限——
"""
import numpy as np
from math import log, pi

path = 'zeros/zeros6'
K = 60000
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

primes = []
for n in range(2, 300):
    if all(n % p for p in primes if p*p <= n):
        primes.append(n)

# 残差模型: 加基频到 P + 谐波组合（频率 = 所有 k·log p ≤ log 300——）
# 频率集合: 所有形如 k·log p（p 素数——k≥1——频率 ≤ log 300 ~ 5.7——）
freqs_set = {}
for p in primes:
    k = 1
    while k * log(p) <= log(300):
        freqs_set[k*log(p)] = (p, k)
        k += 1
freq_list = sorted(freqs_set.items())
print(f'频率数: {len(freq_list)}（k·log p ≤ log 300——）')

# 逐步加频率——残差
cols_base = []
for w, (p, k) in freq_list:
    cols_base.append(np.sin(t_mid * w))
    cols_base.append(np.cos(t_mid * w))
X = np.stack(cols_base, axis=1)
print(f'X 列数: {X.shape[1]}——')

# 直接全拟合
coef, _, _, _ = np.linalg.lstsq(X, Sbar, rcond=None)
R = Sbar - X @ coef
print(f'全频率拟合（≤log300——{len(freq_list)}频率——）:')
print(f'  R²={1-R.var()/Sbar.var():.6f}——残差std={R.std():.6f}')

# 关键: 残差是否'纯噪声'（高频极限——）还是还有结构
print(f'  残差 ρ(1)={np.corrcoef(R[:-1],R[1:])[0,1]:+.3f}——ρ(2)={np.corrcoef(R[:-2],R[2:])[0,1]:+.3f}')
# 残差积分
cumR = np.cumsum(R * dg)
print(f'  ∫R max|={np.max(np.abs(cumR)):.4f}')

# 检查: 残差随频率上限（log Pmax——）的减小——外推
print()
print('残差 vs 频率上限:')
for Pmax_log in [3.0, 4.0, 5.0, 5.7]:
    cols = []
    for w, (p, k) in freq_list:
        if w <= Pmax_log:
            cols.append(np.sin(t_mid * w))
            cols.append(np.cos(t_mid * w))
    Xp = np.stack(cols, axis=1)
    cp, _, _, _ = np.linalg.lstsq(Xp, Sbar, rcond=None)
    Rp = Sbar - Xp @ cp
    print(f'  ω≤{Pmax_log:.1f}: R²={1-Rp.var()/Sbar.var():.6f}——残差std={Rp.std():.6f}')
