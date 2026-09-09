#!/usr/bin/env python3
"""Test 1: Sbar_H(t) = 固定 H 窗口平均 S——拟合系数 a_p√p vs ŵ_H(log p)
S(u) = N(u) - N0(u)——N = 零点计数——窗口平均（矩形——ŵ = sinc(Hω/2)——）
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
    """S(u) = N(u) - N0(u)——N(u) = #{γ<=u}"""
    k = bisect_right(z, u)
    return k - N0(u)

# 在均匀网格上构造 S(t)（从 t0 到 t1——步长 ds——）
t0, t1 = 200.0, 60000.0
ds = 0.2
t_grid = np.arange(t0, t1, ds)
print(f'网格: {len(t_grid)} 点——步长 {ds}')
S_grid = np.array([S_at(t) for t in t_grid])
print(f'S(t): mean={S_grid.mean():+.4f}——std={S_grid.std():.4f}')

# 窗口平均（固定 H——）
def Sbar_H(t_grid, S_grid, H):
    """滑动平均（矩形窗——）Sbar(t) = (1/H)∫_{t-H/2}^{t+H/2}S(u)du"""
    # 用卷积（均匀网格——）
    nH = max(1, int(round(H/ds)))
    kernel = np.ones(nH)/nH
    # 有效卷积（same——但边界——用有效区——）
    sb = np.convolve(S_grid, kernel, mode='valid')
    # 对应的时间点
    tb = t_grid[nH//2 : nH//2 + len(sb)]
    return tb, sb

# 对每个 H——拟合系数（Bohr——）——a_p√p vs sinc(H log p/2)
primes_t = []
for n in range(2, 500):
    if all(n % p for p in primes_t if p*p <= n):
        primes_t.append(n)

print()
print('=== Test 1: a_p·√p vs ŵ_H(log p) ===')
for H in [0.5, 1.0, 2.0, 4.0]:
    tb, sb = Sbar_H(t_grid, S_grid, H)
    T = tb[-1]
    print(f'\nH={H}: S̄ std={sb.std():.4f}')
    # Bohr 系数（对前几个素数——）
    for p in primes_t[:6]:
        # a_p = (1/T)∫Sbar sin(t log p)dt（均匀网格——trapz——）
        a = np.trapz(sb * np.sin(tb*log(p)), tb)/T
        # ŵ = sinc(H log p / 2)——矩形窗的 Fourier
        w_hat = np.sinc(H*log(p)/(2*pi))  # np.sinc(x) = sin(πx)/(πx)——sinc(Hω/2) 其中 ω=log p——np.sinc(y) 的 y = H·log p/(2π)? 检查
        # 标准: 矩形窗 [-H/2,H/2] 的 Fourier at ω: ŵ(ω) = sin(Hω/2)/(Hω/2) = sinc(Hω/(2π))（np.sinc 约定）
        w_hat = np.sinc(H*log(p)/(2*pi)) if H*log(p) > 1e-9 else 1.0
        # 理论: a_p ~ -(1/π)·(1/(√p log p))·ŵ？——或别的——先看 a_p√p 的形状
        print(f'  p={p:2d}: a_p={a:+.5f}——a_p√p={a*np.sqrt(p):+.5f}——ŵ={w_hat:.4f}——比值 a_p√p·π·log p /ŵ = {a*np.sqrt(p)*pi*log(p)/w_hat if abs(w_hat)>0.01 else float("nan"):+.3f}')
