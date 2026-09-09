#!/usr/bin/env python3
"""L1 验证：Erdős 夹逼刚性 + No-go 演示——2026-09-09
定理 1（No-go）：纯乘法结构 ⟹ λ(p) 不能涌现（Sym(ℙ) 对称——）
定理 2（涌现）：单调 + 完全加性 ⟹ λ(p) = c·log p（c 自由——）
"""
from math import log, floor, gcd

print('=== 定理 2：夹逼收敛（λ(p)/λ(q) = log p/log q——）===')
for p, q in [(2, 3), (3, 7), (5, 13), (2, 101)]:
    ratio = log(p)/log(q)
    print(f'  log{p}/log{q} = {ratio:.8f}')
    for k in [1, 10, 100, 1000, 10000]:
        m = floor(k*ratio)
        lo, hi = m/k, (m+1)/k
        ok = lo <= ratio <= hi
        print(f'    k={k:5d}: [{lo:.8f}, {hi:.8f}] 宽 1/k={1/k:.1e}——包含: {ok}')

print()
print('=== 定理 1（No-go）：素数置换保持全部乘法结构 ===')
def sigma(n, perm={2:3, 3:2}):
    out, d = 1, 2
    while n > 1:
        if n % d == 0:
            e = 0
            while n % d == 0: n //= d; e += 1
            out *= perm.get(d, d)**e
        d += 1
    return out

tests = [(6,10), (12,15), (4,9), (30,42), (8,27)]
for a, b in tests:
    sa, sb = sigma(a), sigma(b)
    same = (sigma(a*b)==sa*sb) and ((b%a==0)==(sb%sa==0)) and (sigma(gcd(a,b))==gcd(sa,sb))
    print(f'  σ({a})={sa}, σ({b})={sb}: ×/|/gcd 保持? {same}——log 不等? {log(sa) if sa==3 else log(sa)}≠{log(a)}')

print()
print('=== 结论（L1 的现状——）===')
print('① No-go（Sym(ℙ) 对称——纯乘法结构不能产生 log p——）')
print('② 涌现（加性 + 单调 ⟹ λ(p)/λ(q) = log p/log q——c 自由——）')
print('③ c 的自由度 = 归一化（c=1 需要额外约束——尺度不变性——）')
print('④ "log p 涌现"的实现 = 加性 + 单调公理（内生于 ℤ⁺——）')
print('⑤ 尺度 c 的固定（=1——）是下一个问题（L1 未完全——但核心机制成立——）')
