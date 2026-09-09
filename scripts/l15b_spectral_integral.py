#!/usr/bin/env python3
"""L1.5-B 验证：谱积分机制 + A 的约束分析——2026-09-09
公式链：
  Tr_prim(Ae^{-sA}) = Σ_{p,r} λ(p)e^{-srλ(p)} = c·(−ζ'/ζ)(cs)
  −∫_s^∞ Tr_prim(Ae^{-uA})du = log ζ(cs)
① 数值验证：Σ_{p,r}λ(p)e^{−srλ(p)}（λ=c log p）↔ c·(−ζ'/ζ)(cs)
② ∫ 谱积分 ↔ log ζ(cs)
"""
import numpy as np
from math import log
from mpmath import zeta, log as mlog, mp, mpf, diff

mp.dps = 30

def primes_below(n):
    sieve = np.ones(n+1, dtype=bool)
    sieve[:2] = False
    for i in range(2, int(n**0.5)+1):
        if sieve[i]:
            sieve[i*i::i] = False
    return [int(x) for x in np.nonzero(sieve)[0]]

# ① Σ_{p,r} λ(p)e^{-srλ(p)}——直接求和（λ = log p——c=1——）
def prim_trace(s, pr, rmax=12):
    total = mpf(0)
    for p in pr:
        lp = log(p)
        for r in range(1, rmax+1):
            total += lp * np.exp(-s*r*lp)
    return total

print('=== ① primitive trace Σλ(p)e^{-srλ(p)} vs c·(−ζ\'/ζ)(cs) ===')
pr = primes_below(500)  # 95 primes
for s in [1.5, 2.0, 2.5, 3.0]:
    # −ζ'/ζ(cs)（mpmath——）——用 −(d/ds)log ζ(s) 在 cs
    cs = s  # c=1
    # −ζ'/ζ(cs)：mpmath 无直接——用数值导数 log ζ
    lz = lambda x: mlog(zeta(x))
    zeta_ratio = -diff(lz, cs)  # = −ζ'/ζ(cs)
    pt = prim_trace(s, pr)
    print(f'  s={s}: Σλ(p)e^(−srλ(p)) (N=95, r≤12) = {float(pt):.4f}——'
          f'c(−ζ\'/ζ)(cs) = {float(zeta_ratio):.4f}——比 {float(pt/zeta_ratio):.3f}')

# ② ∫ 谱积分 = log ζ(cs)——用数值积分验证
print()
print('=== ② −∫_s^∞ Tr_prim du vs log ζ(cs) ===')
# 解析：∫_s^∞ Σλ(p)e^{-urλ(p)}du = Σ (1/r)e^{-srλ(p)}
def logzeta_from_integral(s, pr, rmax=12):
    total = mpf(0)
    for p in pr:
        lp = log(p)
        for r in range(1, rmax+1):
            total += np.exp(-s*r*lp) / r
    return total

for s in [1.5, 2.0, 2.5]:
    li = logzeta_from_integral(s, pr)
    lz = mlog(zeta(s))
    print(f'  s={s}: Σ(1/r)e^(−srλ(p)) (N=95, r≤12) = {float(li):.4f}——'
          f'log ζ(s) = {float(lz):.4f}——比 {float(li/lz):.3f}')

print()
print('=== ③ A 的约束分析（谱 = λ(n)——全迹 vs primitive 迹）===')
print('  A 对角（Ae_n = λ(n)e_n——谱 = {λ(n)} = {c log n}——）:')
print('    Tr(e^(−sA)) = Σ_n e^(−sλ(n)) = Σ_n n^(−sc) = ζ(cs)【全迹——】')
print('    Tr_prim（素数幂子谱——加权 λ(p)——）= Σ_{p,r}λ(p)e^(−srλ(p))')
print('      = c·(−ζ\'/ζ)(cs)【primitive 迹——】')
print('  ——d/ds 把全迹（ζ——）变 primitive 迹（ζ\'/ζ——）——')
print('  ——log ζ 从 ∫（谱积分——）自动得 1/r——机制链完整——')
print('  ——但 A 的构造（谱 = λ(n)——不含 log 定义——）是核心缺口——')
