#!/usr/bin/env python3
"""检验 crux 真实性：小 n 上『最小覆盖码是否被迫平展』(Q=0)？
   Q = 2(A1+A2) - E,  E = M(n+1) - 2^n,  A1+A2 = #{pairs: dist<=2}
"""
from itertools import combinations
from collections import Counter

def run(n, M):
    N = 1 << n
    balls = []
    for v in range(N):
        m = 1 << v
        for i in range(n):
            m |= 1 << (v ^ (1 << i))
        balls.append(m)
    full = (1 << N) - 1
    E = M * (n + 1) - N
    Qs = Counter(); ex = {}
    tot = 0
    for comb in combinations(range(N), M):
        cov = 0
        for c in comb:
            cov |= balls[c]
        if cov != full:
            continue
        tot += 1
        A = sum(1 for a, b in combinations(comb, 2) if (a ^ b).bit_count() <= 2)
        Q = 2 * A - E
        Qs[Q] += 1
        if Q not in ex:
            ex[Q] = comb
    return E, Qs, ex, tot

for (n, M) in ((4, 4), (5, 7)):
    E, Qs, ex, tot = run(n, M)
    print(f"n={n} M={M} (K({n},1)={M} 为精确最小值): E={E}  覆盖码总数={tot}")
    print(f"  Q 分布 = {dict(sorted(Qs.items()))}")
    print(f"  Q >= 1 的比例 = {sum(c for q,c in Qs.items() if q>=1)}/{tot}"
          f"  ({100*sum(c for q,c in Qs.items() if q>=1)/max(tot,1):.1f}%)")
    qmin, qmax = min(Qs), max(Qs)
    print(f"  Q_min={qmin}  例: {[format(x,'0%db'%n) for x in ex[qmin]]}")
    print(f"  Q_max={qmax}  例: {[format(x,'0%db'%n) for x in ex[qmax]]}")
    print()
