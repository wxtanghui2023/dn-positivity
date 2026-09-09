#!/usr/bin/env python3
"""验证 24 真假: 固定窗口 ∫R 随区间长度 T 的增长
真发散（~√T 或线性——）→ 路线封存
饱和（O(1)——）→ 采样伪象——重审测度转换
用多段 t 区间——每段的 ∫R max——看增长标度——
"""
import numpy as np
from math import log, pi
from bisect import bisect_right

path = '/home/node/.openclaw/workspace/dn-project/zeros/zeros6'
K = 200000
z = np.zeros(K)
with open(path) as f:
    for i in range(K):
        z[i] = float(f.readline())

def N0(t):
    if t <= 1: return 0.0
    return (t/(2*pi))*(log(t/(2*pi)) - 1) + 7.0/8

def S_at(u):
    k = bisect_right(z, u)
    return k - N0(u)

primes_t = []
for n in range(2, 100):
    if all(n % p for p in primes_t if p*p <= n):
        primes_t.append(n)

H = 1.0
ds = 0.5  # 粗网格（省时间——多段——）

print('=== 固定窗口 ∫R 的增长验证 ===')
print('（真发散 ~√T——封存；饱和——采样伪象——）')
for (ta, tb) in [(500, 20000), (500, 40000), (500, 80000), (500, 160000), (500, 200000)]:
    t_grid = np.arange(ta, tb, ds)
    S_grid = np.array([S_at(t) for t in t_grid])
    nH = max(1, int(round(H/ds)))
    kernel = np.ones(nH)/nH
    sb = np.convolve(S_grid, kernel, mode='valid')
    tg = t_grid[nH//2 : nH//2 + len(sb)]
    T = tg[-1]
    # Bohr k=1 模型（p≤97——）
    model = np.zeros(len(tg))
    for p in primes_t:
        a = np.trapz(sb*np.sin(tg*log(p)), tg)/T
        model += a*np.sin(tg*log(p))
    R = sb - model
    cumR = np.cumsum(R)*ds
    rw_est = R.std()*np.sqrt(len(R))*ds
    print(f'T到{tb:>7}: S̄ std={sb.std():.4f}——残差std={R.std():.4f}——'
          f'∫R max|={np.max(np.abs(cumR)):8.2f}——末值={cumR[-1]:+8.2f}——'
          f'√T·σ·ds 估计={rw_est:8.1f}——比值={np.max(np.abs(cumR))/max(rw_est,1e-9):.3f}')
