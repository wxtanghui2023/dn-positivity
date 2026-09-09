#!/usr/bin/env python3
"""R₁(n,m) = Σ_{p|n,q|m} 1{P^+(p+q)|n+m} 的三重测试（数值——）
A: primewise?（否——结构上——）
B: 单整数函数 F(n+m)+G(n)+H(m)?
C: 有限秩 ΣA_j(n)B_j(m)?
测试：R₁ 矩阵的秩（C——）+ 与 F(n+m) 类单体量的偏差（B——）
"""
import numpy as np
from math import sqrt

def primes_upto(n):
    sieve = np.ones(n+1, dtype=bool)
    sieve[:2] = False
    for i in range(2, int(n**0.5)+1):
        if sieve[i]:
            sieve[i*i::i] = False
    return [int(x) for x in np.nonzero(sieve)[0]]

def pf(n, pr):
    """素因子集——"""
    out = set()
    for p in pr:
        if p*p > n:
            break
        if n % p == 0:
            out.add(p)
            while n % p == 0:
                n //= p
    if n > 1:
        out.add(n)
    return out

def Pplus(k, pr):
    """k 的最大素因子——"""
    if k < 2:
        return 1
    best = 1
    for p in pr:
        if p*p > k:
            break
        if k % p == 0:
            best = p
            while k % p == 0:
                k //= p
    if k > 1:
        best = k
    return best

def R1(n, m, pr):
    """R₁——p|n, q|m——P^+(p+q)|n+m 的计数——"""
    Pn = pf(n, pr)
    Pm = pf(m, pr)
    cnt = 0
    for p in Pn:
        for q in Pm:
            r = Pplus(p+q, pr)
            if r > 1 and (n+m) % r == 0:
                cnt += 1
    return cnt

N = 120
pr = primes_upto(2*N+50)
# R₁ 矩阵
M = np.zeros((N-1, N-1))
for n in range(2, N+1):
    for m in range(2, N+1):
        M[n-2, m-2] = R1(n, m, pr)

print('=== R₁ 矩阵秩（C 测试——有限秩?）===')
r = np.linalg.matrix_rank(M, tol=1e-10)
print(f'  矩阵 {N-1}x{N-1}——秩 = {r}（满秩 = {N-1}——低秩死——高秩过——）')

# SVD 谱（看奇异值衰减——）
s = np.linalg.svd(M, compute_uv=False)
print(f'  奇异值前 10: {[f"{x:.1f}" for x in s[:10]]}')
print(f'  奇异值比（σ10/σ1——）: {s[9]/s[0]:.4f}（低秩则 ~0——）')

# B 测试: R₁ vs F(n+m)（单体——）——残差
print()
print('=== B 测试（单整数函数——）===')
# R₁ 与 n+m 的函数的相关（若强——可能 F(n+m) 主导——）
sumnm = np.array([[n+m for m in range(2, N+1)] for n in range(2, N+1)])
corr = np.corrcoef(M.flatten(), sumnm.flatten())[0,1]
print(f'  corr(R₁, n+m) = {corr:.4f}')
# R₁ 的"行均值"随 n——列均值随 m——（若 R₁ ≈ G(n)+H(m)——行+列可解释大部分——）
row_mean = M.mean(axis=1)
col_mean = M.mean(axis=0)
total_mean = M.mean()
recon = row_mean[:,None] + col_mean[None,:] - total_mean
resid = M - recon
var_total = (M**2).mean()
var_resid = (resid**2).mean()
print(f'  行+列重构解释方差: {1-var_resid/var_total:.3f}（≈1 则 G(n)+H(m) 型——B 死——）')

# A 测试（结构——）: 固定 p 的投影是否解释 R₁?
print()
print('=== 样本 R₁ 值（检查结构——）===')
for (n,m) in [(6,10), (6,15), (10,15), (30,42), (12,18), (14,21), (6,6), (10,10)]:
    print(f'  R₁({n},{m}) = {R1(n,m,pr)}')
