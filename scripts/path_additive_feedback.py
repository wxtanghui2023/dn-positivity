#!/usr/bin/env python3
"""最小"乘法路径 × 加法反馈"对象——四硬测试——2026-09-09
路径：1 = d₀ → d₁ → ... → d_k = n（d_{j+1}/d_j ∈ ℙ——素因子排列——）
加法反馈：ε_j = sign(μ(d_j + d_{j+1}))——决定转移 M₊/M₋/I
M₊ = [[1,1],[0,1]]——M₋ = [[1,0],[1,1]]（非交换——）
测试：1 [M₊,M₋]≠0？2 可约成字符？3 J T J⁻¹ → δ→−δ？
      4 独立于外加 t 的振荡量？
"""
import numpy as np
from math import sqrt
from itertools import permutations

# Möbius（到 N——）
def mobius_sieve(n):
    mu = [1]*(n+1)
    is_prime = [True]*(n+1)
    primes = []
    for i in range(2, n+1):
        if is_prime[i]:
            primes.append(i)
            for j in range(i, n+1, i):
                mu[j] *= -1
                is_prime[j] = False
        # 平方因子
        for p in primes:
            if p*p > i: break
            # 简化：直接筛平方
    # 标准线性筛 μ
    mu = [1]*(n+1)
    lp = [0]*(n+1)
    primes = []
    mu[0] = 0
    for i in range(2, n+1):
        if lp[i] == 0:
            lp[i] = i
            primes.append(i)
            mu[i] = -1
        for p in primes:
            if p > lp[i] or i*p > n: break
            lp[i*p] = p
            if i % p == 0:
                mu[i*p] = 0
                break
            else:
                mu[i*p] = -mu[i]
    return mu

Mp = np.array([[1.0,1.0],[0.0,1.0]])
Mm = np.array([[1.0,0.0],[1.0,1.0]])
I2 = np.eye(2)

def M_from_mu(mu_val):
    if mu_val > 0: return Mp
    if mu_val < 0: return Mm
    return I2

def prime_factors(n):
    fac = []
    d = 2
    while d*d <= n:
        while n % d == 0:
            fac.append(d)
            n //= d
        d += 1
    if n > 1: fac.append(n)
    return fac

def path_transfer(factors, mu):
    """一条路径（factors 的排列——1 → f1 → f1f2 → ... → n）的转移"""
    T = I2.copy()
    d = 1
    for f in factors:
        d_next = d*f
        # 加法反馈：μ(d + d_next)
        mu_val = mu[d + d_next] if d + d_next < len(mu) else 0
        T = M_from_mu(mu_val) @ T
        d = d_next
    return T

print('=== 测试 1：[M₊,M₋] ≠ 0？===')
comm = Mp@Mm - Mm@Mp
print(f'  [M₊,M₋] = {comm.tolist()}——非零 = {np.linalg.norm(comm) > 1e-12}')
print(f'  M₊M₋ = {Mp@Mm}——M₋M₊ = {Mm@Mp}')

# 测试 2 和 3：用实际路径
print()
print('=== 测试 2+3：路径转移（pq vs qp——reversal——）===')
mu = mobius_sieve(2000)
tests = [(2,3), (2,5), (3,5), (2,3,5), (2,7), (3,7)]
for fac in tests:
    perms = list(permutations(fac))
    Ts = {p: path_transfer(list(p), mu) for p in perms}
    # 交换（pq vs qp——）
    diff = any(np.linalg.norm(Ts[p] - Ts[q]) > 1e-12 for p in perms for q in perms if p != q)
    print(f'  路径 {fac}: {len(perms)} 排列——不同排列的 T 不同 = {diff}')
    if len(perms) == 2:
        p1, p2 = perms[0], perms[1]
        print(f'    T({p1}) = {Ts[p1].round(3).tolist()}——T({p2}) = {Ts[p2].round(3).tolist()}')
        # reversal 关系
        print(f'    reversal（{p2} = {p1} 的反序——）: T 相等 = '
              f'{np.linalg.norm(Ts[p1]-Ts[p2])<1e-12}')

# 测试 4：独立振荡——T 的迹/角随 n 的序列
print()
print('=== 测试 4：独立于外加 t 的量（Tr/角——随 n——）===')
vals = []
ns = []
for n in range(2, 300):
    fac = prime_factors(n)
    if len(fac) >= 2 and len(set(fac)) == len(fac):  # squarefree 复合
        perms = list(permutations(fac))
        trs = [np.trace(path_transfer(list(p), mu)) for p in perms]
        vals.append((n, min(trs), max(trs)))
        ns.append(n)
# 波动性（随 n——）
tr_min = [v[1] for v in vals]
tr_max = [v[2] for v in vals]
print(f'  n = 2..299 的 squarefree 复合（{len(vals)} 个——）:')
print(f'  Tr 范围: min∈[{min(tr_min):.3f}, {max(tr_min):.3f}]——'
      f'max∈[{min(tr_max):.3f}, {max(tr_max):.3f}]')
print(f'  序列波动（相邻差——）: max|ΔTr| = {max(abs(tr_max[i]-tr_max[i-1]) for i in range(1,len(tr_max))):.3f}')
# 是否依赖素因子多重集之外的东西（同 n 不同排列——）
print(f'  同 n 不同排列的 Tr 变化: max = {max(v[2]-v[1] for v in vals):.3f}')
