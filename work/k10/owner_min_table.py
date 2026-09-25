#!/usr/bin/env python3
"""极小表：在真实码 C_120 上算 S(E_S) 的最小 union。
   S(e) = {码字下标 : d(词, e) <= 1}；e ∈ U_D 要求 S(e) ⊆ D，而 |D|=4 ⟹ |S(e)|>=5 必非候选。
   对每个码字 x 与坐标集 {a,b,...} 算 |S(x^e_a) ∪ ...|，输出分布与最小值（按 |E_S|=1,2,3）。
"""
import sys, itertools
from collections import Counter
sys.argv = ['x', '5', 'none']
exec(open('/home/node/.openclaw/workspace/dn-project/work/k10/exact_pack.py').read().split('def main()')[0])
d = lambda a, b: (a ^ b).bit_count()

# 预计算：所有距码字 <=1 的点 e 的 owner 集（做记忆化）
cache = {}


def S_of(e):
    if e not in cache:
        cache[e] = frozenset(i for i, w in enumerate(WORDS) if d(w, e) <= 1)
    return cache[e]


hist1 = Counter()
hist2 = Counter()
hist3 = Counter()
best = {1: (10 ** 9, None), 2: (10 ** 9, None), 3: (10 ** 9, None)}
for xi_idx, xi in enumerate(WORDS):
    # |E_S| = 1
    for a in range(10):
        e = xi ^ (1 << a)
        s = len(S_of(e))
        hist1[s] += 1
        if s < best[1][0]:
            best[1] = (s, (xi_idx, a, sorted(S_of(e))))
    # |E_S| = 2
    for a, b in itertools.combinations(range(10), 2):
        u = len(S_of(xi ^ (1 << a)) | S_of(xi ^ (1 << b)))
        hist2[u] += 1
        if u < best[2][0]:
            best[2] = (u, (xi_idx, (a, b), sorted(S_of(xi ^ (1 << a)) | S_of(xi ^ (1 << b)))))
    # |E_S| = 3
    for a, b, c in itertools.combinations(range(10), 3):
        u = len(S_of(xi ^ (1 << a)) | S_of(xi ^ (1 << b)) | S_of(xi ^ (1 << c)))
        hist3[u] += 1
        if u < best[3][0]:
            best[3] = (u, (xi_idx, (a, b, c), sorted(S_of(xi ^ (1 << a)) | S_of(xi ^ (1 << b)) | S_of(xi ^ (1 << c)))))
print("=== 极小表：S(E_S) 的 union 大小分布（真实码，120 个旋转 × 坐标组合）===")
print(f"|E_S|=1: 分布 = {dict(sorted(hist1.items()))}   最小 = {best[1][0]}")
print(f"|E_S|=2: 分布 = {dict(sorted(hist2.items()))}   最小 = {best[2][0]}")
print(f"|E_S|=3: 分布 = {dict(sorted(hist3.items()))}   最小 = {best[3][0]}")
print()
for r in (1, 2, 3):
    v, info = best[r]
    print(f"最小值样例 |E_S|={r}: union={v}  (x_idx={info[0]}, 坐标={info[1]})  S(union)={info[2]}")
print()
print("★ 判据: union <= 4 才可能装入 D（|D|=4）")
for r in (1, 2, 3):
    n = sum(c for k, c in {1: hist1, 2: hist2, 3: hist3}[r].items() if k <= 4)
    tot = sum({1: hist1, 2: hist2, 3: hist3}[r].values())
    print(f"  |E_S|={r}: union<=4 的比例 = {n}/{tot} = {n / tot:.4f}")
