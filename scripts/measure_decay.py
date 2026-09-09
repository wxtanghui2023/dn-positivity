#!/usr/bin/env python3
"""系数衰减精确测量: a_{p,1}（基频）和 a_{p,2}（谐波——）的衰减律
为严格化提供系数界（Σa/(k log p) 收敛的证明基础——）
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

primes = []
for n in range(2, 500):
    if all(n % p for p in primes if p*p <= n):
        primes.append(n)
primes = np.array(primes)

print('=== 系数衰减精确测量 ===')
# 基频拟合（p ≤ 400——）+ 谐波（2p ≤ 400——）
cols = []
plist = primes[primes <= 400]
for p in plist:
    cols.append(np.sin(t_mid * log(p)))
    cols.append(np.cos(t_mid * log(p)))
plist2 = primes[primes <= 200]
for p in plist2:
    cols.append(np.sin(2*t_mid * log(p)))
    cols.append(np.cos(2*t_mid * log(p)))
X = np.stack(cols, axis=1)
coef, _, _, _ = np.linalg.lstsq(X, Sbar, rcond=None)

# 基频系数 vs p——拟合衰减律 a ~ C·p^{-α}
n1 = len(plist)
amps1 = np.array([np.hypot(coef[2*i], coef[2*i+1]) for i in range(n1)])
n2 = len(plist2)
amps2 = np.array([np.hypot(coef[2*n1+2*i], coef[2*n1+2*i+1]) for i in range(n2)])

# 分段测指数（基频——）
print('基频衰减（log a vs log p 的斜率——）:')
for i0 in range(0, n1, 20):
    i1 = min(i0+20, n1)
    seg_p = plist[i0:i1].astype(float)
    seg_a = amps1[i0:i1]
    # 线性拟合 log a = -α log p + C
    if len(seg_p) > 5 and seg_a.min() > 0:
        alpha = -np.polyfit(np.log(seg_p), np.log(seg_a), 1)[0]
        print(f'  p∈[{plist[i0]},{plist[i1-1]}]: α≈{alpha:.3f}')

# 谐波衰减（k=2——）
print()
print('谐波(k=2)衰减:')
for i0 in range(0, n2, 10):
    i1 = min(i0+10, n2)
    seg_p = plist2[i0:i1].astype(float)
    seg_a = amps2[i0:i1]
    if len(seg_p) > 3 and seg_a.min() > 1e-6:
        alpha = -np.polyfit(np.log(seg_p), np.log(seg_a), 1)[0]
        print(f'  p∈[{plist2[i0]},{plist2[i1-1]}]: α≈{alpha:.3f}')

# Σ a/log p 收敛的数值（基频 + 谐波——）
print()
print('Σ a/(k log p)（M 的 DC 常数——）收敛性:')
# 外推尾部（用拟合的 α——）
s1 = np.sum(amps1 / np.log(plist))
s2 = np.sum(amps2 / (2*np.log(plist2)))
print(f'  基频到 p≤400: Σa/log p = {s1:.4f}')
print(f'  谐波到 p≤200: Σa/(2log p) = {s2:.4f}')
print(f'  合计（拟合部分——）= {s1+s2:.4f}')

# 尾部外推: a(p) ~ C p^{-α}——尾部积分 ∫ C p^{-α}/(log p) dp
# 用最后一段的 α 和 C
last_a = amps1[-5:]
last_p = plist[-5:].astype(float)
alpha_tail = -np.polyfit(np.log(last_p), np.log(last_a), 1)[0]
C_tail = np.exp(np.polyfit(np.log(last_p), np.log(last_a), 1)[1])
print(f'  尾部（p>400——）α={alpha_tail:.3f}——C={C_tail:.2e}')
if alpha_tail > 0:
    # ∫_400^∞ C p^{-α}/log p dp ~ C/(α-1)·400^{-(α-1)}/log 400 类
    tail_est = C_tail * 400**(-(alpha_tail-1)) / ((alpha_tail-1) * log(400))
    print(f'  尾部估计（p>400——）: ~{tail_est:.4f}（α={alpha_tail:.2f}——收敛需 α>1——）')
    print(f'  → α={alpha_tail:.2f}——{"收敛（α>1——）" if alpha_tail > 1 else "不收敛？"}(谐波——)')
