#!/usr/bin/env python3
"""素数态重叠矩阵——log|det| 观测（避免下溢——）
问：det M_N(s) 是否有 σ 或 t 的结构（σ=½ 特殊？离散零点？）
"""
import numpy as np
from math import log, sqrt

def primes_below(n):
    sieve = np.ones(n+1, dtype=bool)
    sieve[:2] = False
    for i in range(2, int(n**0.5)+1):
        if sieve[i]:
            sieve[i*i::i] = False
    return [int(x) for x in np.nonzero(sieve)[0]]

def M_pq(p, q, sigma, t):
    if p == q:
        a = p**(-2*sigma); b = p**(-2+2*sigma)
        return sqrt((1-a)*(1-b))/(1-1.0/p)
    lp = log(p); lq = log(q)
    phase = np.exp(1j*t*(lp - lq))
    denom = 1 - p**(-sigma)*q**(-(1-sigma))*phase
    num = sqrt((1-p**(-2*sigma))*(1-q**(-2+2*sigma)))
    return num/denom

def logdet_MN(primes, sigma, t):
    N = len(primes)
    M = np.zeros((N, N), dtype=complex)
    for i in range(N):
        for j in range(N):
            M[i,j] = M_pq(primes[i], primes[j], sigma, t)
    # 归一化（每行除对角——）避免动态范围
    for i in range(N):
        M[i,:] /= abs(M[i,i])
    sign, logdet = np.linalg.slogdet(M)
    return logdet

pr = primes_below(300)
print('=== log|det M_N|（N=20——归一化——）σ-t 扫描 ===')
pr20 = pr[:20]
for sigma in [0.2, 0.3, 0.4, 0.45, 0.5, 0.55, 0.6, 0.7, 0.8]:
    row = []
    for t in [0, 5, 10, 14.13, 20, 25, 30, 35]:
        ld = logdet_MN(pr20, sigma, t)
        row.append(f'{ld:+.1f}')
    print(f'  σ={sigma}: ' + ' '.join(row))

# σ 扫描（t 固定——）——看 log|det| 的 σ 依赖
print()
print('=== log|det| vs σ（t=14.13——N=20——）===')
for sigma in np.linspace(0.05, 0.95, 19):
    ld = logdet_MN(pr20, sigma, 14.13)
    print(f'  σ={sigma:.3f}: {ld:+.2f}')

# N 依赖（σ=0.5——log|det| 随 N——）
print()
print('=== log|det| vs N（σ=0.5, t=14.13——）===')
for N in [5, 10, 15, 20, 25, 30, 35, 40]:
    ld = logdet_MN(pr[:N], 0.5, 14.13)
    print(f'  N={N}: {ld:+.2f}')
print('（若 log|det| ~ -cN——每加一个素数 det 指数降——像区域——）')
