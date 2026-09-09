#!/usr/bin/env python3
"""R 的物理频率结构——找 R 的来源（非 log p 频率——）
R = Sbar - Bohr 展开——60% 方差——积分有界——
R 的物理频率（t 空间——）——用 Lomb-Scargle 类（不均匀——）或分段相关——
"""
import numpy as np
from math import log, pi

path = '/home/node/.openclaw/workspace/dn-project/zeros/zeros6'
K = 60000
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
t_mid = (z[:-1] + z[1:])/2
T = t_mid[-1]

# Bohr 展开
primes = []
for n in range(2, 300):
    if all(n % p for p in primes if p*p <= n):
        primes.append(n)
R = Sbar.copy()
for p in primes:
    if p > 200: break
    a = np.sum(Sbar * np.sin(t_mid * log(p)) * dg) / T
    R = R - a * np.sin(t_mid * log(p))

print('=== R 的物理频率扫描 ===')
# 用相关法（不均匀数据的频谱——）对候选频率
# R ~ A sin(ωt) + B cos(ωt)——拟合幅度 vs ω
def amp_at(w):
    s = np.sum(R * np.sin(w * t_mid) * dg)
    c = np.sum(R * np.cos(w * t_mid) * dg)
    return np.hypot(s, c) / T

# 扫描物理频率（log p 之间的——差频/和频/谐波——）
cands = []
# log p 的差频
lp = [log(p) for p in primes[:20]]
for i in range(len(lp)):
    for j in range(i+1, len(lp)):
        cands.append(abs(lp[j]-lp[i]))
# 和频
for i in range(5):
    for j in range(i, 5):
        cands.append(lp[i]+lp[j])
# 已知 log p
cands += lp[:10]

# 测量每个候选的幅度
print('候选频率的 R 幅度（vs R std——）:')
results = []
for w in sorted(set(round(c, 4) for c in cands)):
    a = amp_at(w)
    results.append((w, a))
results.sort(key=lambda x: -x[1])
for w, a in results[:15]:
    print(f'  ω={w:.4f}: 幅度={a:.5f}')
print(f'  （R std = {R.std():.4f}——随机基线 ~ sqrt(2/N)·std ~ {np.sqrt(2/len(R))*R.std():.4f}——）')

# 幅度最大的频率的物理意义
w0, a0 = results[0]
print(f'主频 ω={w0:.4f}——对应 p={np.exp(w0):.2f}（如果 log p——）——或差频?')
