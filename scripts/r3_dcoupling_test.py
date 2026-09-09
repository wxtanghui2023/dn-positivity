#!/usr/bin/env python3
"""R₃ 的 d-耦合真伪测试（数值——）
T₂ = Σ_d μ(d)·C_d(n,m)·1{d|n+m}
C_d(n,m) = Σ_{p|n,p<P^-(d)}Σ_{q|m,q≥P^+(d)} sgn(q-p) 的规范化（两情形——）

测试：拆 d = 单素因子 vs 复合（≥2 素因子）——比较贡献
——若复合 d 贡献可忽略（Möbius 抵消）→ 跨 d 耦合假象 → 可压回单 r
——若复合 d 贡献显著 → 跨 d 耦合真（多素因子信息——）
"""
import numpy as np
from math import log

def primes_upto(n):
    sieve = np.ones(n+1, dtype=bool)
    sieve[:2] = False
    for i in range(2, int(n**0.5)+1):
        if sieve[i]:
            sieve[i*i::i] = False
    return [int(x) for x in np.nonzero(sieve)[0]]

def pf_set(x, pr):
    """素因子集（含幂次 1 次——）"""
    out = set()
    for p in pr:
        if p*p > x:
            break
        if x % p == 0:
            out.add(p)
            while x % p == 0:
                x //= p
    if x > 1:
        out.add(x)
    return out

def squarefree_divisors(P_set):
    """P_set 的所有 squarefree 因子（含 1——）返回 [(d, μ(d), P^-(d), P^+(d))]"""
    items = sorted(P_set)
    divs = [(1, 1, None, None)]  # (d, mu, Pmin, Pmax)——d=1 特例
    for r in items:
        new = []
        for (d, mu, pmin, pmax) in divs:
            new.append((d*r, -mu, r if pmin is None else pmin, r))  # r 是最大的（有序添加）
        divs.extend(new)
    return divs

def C_d(n, m, d, mu, pmin, pmax, pr):
    """C_d(n,m) = Σ_{p|n,p<pmin}Σ_{q|m,q≥pmax} 1 − Σ_{p|n,p≥pmax}Σ_{q|m,q<pmin} 1
    （sgn 展开的两情形——q>p 情形 p 来自 n 小、q 来自 m 大——等等——直接算 sgn——）"""
    if d == 1:
        # 空区间——1{∃} = 0——T₂ 无 d=1 净贡献问题——实际 K 的 1-Σ 里 d=1 的 μ=1
        # 但 T₂ = Σ_{p,q}sgn·Σ_{d|P(p,q),d|k}μ(d)——d=1 时 P(p,q) 必须空——特殊——
        return 0.0
    Pn = pf_set(n, pr)
    Pm = pf_set(m, pr)
    s = 0.0
    for p in Pn:
        for q in Pm:
            # d|P(p,q)：min(p,q) < pmin 且 pmax ≤ max(p,q)——（d 素因子都在 (min,max]——）
            lo, hi = (p, q) if p < q else (q, p)
            if lo < pmin and pmax <= hi:
                s += 1.0 if q > p else -1.0
    return s

def T2_split(n, m, pr):
    """T₂ 拆成单素因子 d 与复合 d 的贡献——
    T₂ = Σ_{p|n,q|m} sgn(q-p)·Σ_{d|P(p,q), d|n+m} μ(d)
    按 (p,q) 对的区间 P(p,q) 的 squarefree 因子算——"""
    k = n + m
    Pn = pf_set(n, pr)
    Pm = pf_set(m, pr)
    single = 0.0
    comp = 0.0
    for p in Pn:
        for q in Pm:
            if p == q:
                continue
            lo, hi = (p, q) if p < q else (q, p)
            sgn = 1.0 if q > p else -1.0
            # P(p,q) = (lo, hi] 内素数积——因子 d|P 且 d|k——μ(d)
            # 直接枚举 d（P 的 squarefree 因子——）用素因子区间
            interval_primes = [r for r in pr if lo < r <= hi]
            if not interval_primes:
                # P = 1——Σ_{d|P,d|k}μ(d) = μ(1)·1 = 1（1|k）——但 1{∃}=1-1=0——T₂ 贡献 = sgn·1
                # 嗯——T₂ = Σ sgn·Σ_{d|P,d|k}μ(d)——d=1 恒在——Σ = 1（只有 d=1——）
                single += sgn * 1.0  # d=1 项
                continue
            # 枚举 squarefree 因子（含 1——）只取 |k 的——
            divs = [(1, 1)]
            for r in interval_primes:
                divs += [(d*r, -mu) for (d, mu) in divs]
            for (d, mu) in divs:
                if k % d == 0:
                    if d == 1 or len(pf_set(d, pr)) == 1:
                        single += sgn * mu
                    else:
                        comp += sgn * mu
    return single, comp

pr = primes_upto(300)
print('=== T₂ 的单素因子 d vs 复合 d 贡献（R₃ 的 d-耦合真伪——）===')
print('（若复合贡献 ~0——Möbius 抵消——可压回单 r——假象——）')
print('（若复合贡献显著——多素因子信息——真耦合——）')
print()
total_s, total_c = 0.0, 0.0
count = 0
for n in range(2, 60):
    for m in range(2, 60):
        s, c = T2_split(n, m, pr)
        total_s += s
        total_c += c
        count += 1
print(f'  样本 {count} 个 (n,m)——单 d 总贡献 = {total_s:.1f}——复合 d 总贡献 = {total_c:.1f}')
print(f'  复合/单 比例 = {abs(total_c)/max(abs(total_s),1e-9):.3f}')

# 展示一些具体的 (n,m)
print()
print('  具体样本（单 vs 复合——）:')
for (n, m) in [(6, 10), (10, 15), (30, 42), (12, 18), (6, 6), (30, 30), (6, 35), (10, 21), (15, 14), (70, 30)]:
    s, c = T2_split(n, m, pr)
    print(f'    ({n},{m}): 单 d = {s:+.0f}——复合 d = {c:+.0f}——总 T₂ = {s+c:+.0f}')
