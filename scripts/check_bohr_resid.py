#!/usr/bin/env python3
"""Bohr 残差 R 的结构——38% 方差的非几乎周期部分——为什么积分 O(1)?
R = Sbar - Bohr 展开（真谱——）——频谱/自相关/积分——
"""
import numpy as np
from math import log, pi

path = '/home/node/.openclaw/workspace/dn-project/zeros/zeros6'
K = 100000
z = np.zeros(K)
with open(path) as f:
    for i in range(K):
        z[i] = float(f.readline())

dg = np.diff(z)
def IntN0(t):
    if t <= 1: return 0.0
    return t*t/(4*pi)*log(t/(2*pi)) - 3*t*t/(8*pi) + 7*t/8
kk = np.arange(1, K)
IntN = np.array([IntN0(t) for t in z[:K]])
Sbar = kk - (IntN[1:] - IntN[:-1])/dg
cumM = np.cumsum(Sbar * dg)
t_mid = (z[:-1] + z[1:])/2
T = t_mid[-1]

# Bohr 展开（到 p≤200——）
primes = []
for n in range(2, 300):
    if all(n % p for p in primes if p*p <= n):
        primes.append(n)
R = Sbar.copy()
for p in primes:
    if p > 200: break
    a = np.sum(Sbar * np.sin(t_mid * log(p)) * dg) / T
    R = R - a * np.sin(t_mid * log(p))

print('=== Bohr 残差 R 的结构 ===')
print(f'R: std={R.std():.4f}——Sbar std={Sbar.std():.4f}——占比 {R.std()/Sbar.std():.3f}')

# R 的自相关
print('R 自相关:')
for lag in [1, 2, 3, 5, 10, 20]:
    c = np.corrcoef(R[:-lag], R[lag:])[0,1]
    print(f'  ρ({lag}) = {c:+.4f}')

# R 的积分（累积——）
cumR = np.cumsum(R * dg)
print(f'∫R: 末值={cumR[-1]:+.3f}——max|={np.max(np.abs(cumR)):.3f}')

# R 的频谱（k 空间——）
Rc = R - R.mean()
spec = np.abs(np.fft.fft(Rc * np.hanning(len(Rc))))**2
fr = np.fft.fftfreq(len(Rc))
pos = fr > 0
top = np.argsort(spec[pos])[-8:][::-1]
print('R 主频（k 空间——）:')
for idx in top:
    print(f'  周期={1/fr[pos][idx]:.1f} k——功率占比={spec[pos][idx]/spec[pos].sum():.4f}')

# R 与零点间距涨落 δ 的关系（再查——用 Bohr 残差——）
N0p = np.array([log(t/(2*pi))/(2*pi) for t in t_mid])
delta = dg - 1.0/N0p
c = np.corrcoef(R, delta)[0,1]
print(f'R vs δ 相关: {c:+.4f}')

# R 与 S 逐点锯齿的关系——R 是否含锯齿残余?
# S 逐点（右极限——）的锯齿部分 ~ (S_pt - S_titch) 的平滑——太难——先看 R 的'波形'
print()
print('R 的波形样本（前 200 个区间——）:')
print(' '.join(f'{v:+.3f}' for v in R[:100:5]))
