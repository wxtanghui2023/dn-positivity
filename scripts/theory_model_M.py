#!/usr/bin/env python3
"""理论系数 M 模型: 用 log ζ 展开的理论系数（无条件——）直接构造 M 模型
S̄ 展开理论: S̄ ~ -(1/π)Σ_p Σ_k sin(k log p · t)·w_{p,k}/(k p^{k/2})
w = 区间平均修正——先试 w=1（无修正——）看复现度
M_model = -(1/π)Σ_p Σ_k (w/(k p^{k/2}))·(1-cos(k log p · T))/(k log p)·?——
即 ∫sin(k log p t)/π/(k p^{k/2}) dt = (1-cos)/(π k p^{k/2} k log p)——
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
cumM = np.cumsum(Sbar * dg)
t_mid = (z[:-1] + z[1:])/2

primes = []
for n in range(2, 300):
    if all(n % p for p in primes if p*p <= n):
        primes.append(n)
primes = np.array(primes)

print('=== 理论系数 M 模型（log ζ 展开——无条件——）===')
# M_model(T) = ∫S̄ ≈ -(1/π)Σ_{p,k} (1/(k p^{k/2}))·(1-cos(k log p T))/(k log p)
# 注意符号: S ~ -(1/π)Σ sin/(√p log p)——但实测 Sbar 拟合的 sin 系数是正的?
# 先检查符号——直接用公式（含负号——）并看相关
def M_model(T, pmax, kmax):
    M = np.zeros(len(T))
    for p in primes[primes <= pmax]:
        for k in range(1, kmax+1):
            if k*p**0.5 > 1e6: break
            w = 1.0/(k * p**(k/2))
            M += -(1.0/pi) * w * (1 - np.cos(k*log(p)*T)) / (k*log(p))
    return M

# 也试无负号版本（检查符号——）
def M_model_plus(T, pmax, kmax):
    M = np.zeros(len(T))
    for p in primes[primes <= pmax]:
        for k in range(1, kmax+1):
            w = 1.0/(k * p**(k/2))
            M += (1.0/pi) * w * (1 - np.cos(k*log(p)*T)) / (k*log(p))
    return M

sample = np.linspace(5000, len(t_mid)-1, 200).astype(int)
for pmax, kmax, name in [(100, 1, '基频 p≤100'), (100, 3, '基频+谐波 p≤100'),
                          (300, 1, '基频 p≤300'), (300, 3, '基频+谐波 p≤300')]:
    M1 = M_model(t_mid[sample], pmax, kmax)
    M2 = M_model_plus(t_mid[sample], pmax, kmax)
    c1 = np.corrcoef(cumM[sample], M1)[0,1]
    c2 = np.corrcoef(cumM[sample], M2)[0,1]
    print(f'{name}: 负号版相关={c1:+.4f}——正号版相关={c2:+.4f}')

# 详细看 p≤300 k≤3 的（更好的——）
M_best = M_model_plus(t_mid, 300, 3)
M_best_n = M_model(t_mid, 300, 3)
print()
print('真实 M vs 理论模型（p≤300——k≤3——）:')
print(f'  真实: mean={cumM[sample].mean():.3f}——max={cumM[sample].max():.3f}——min={cumM[sample].min():.3f}')
print(f'  正号: mean={M_best[sample].mean():.3f}——max={M_best[sample].max():.3f}——min={M_best[sample].min():.3f}')
print(f'  负号: mean={M_best_n[sample].mean():.3f}——max={M_best_n[sample].max():.3f}——min={M_best_n[sample].min():.3f}')
