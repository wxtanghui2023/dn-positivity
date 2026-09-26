#!/usr/bin/env python3
"""Q 的钉住现象：固定 n，随 M 变化，所有覆盖码的 Q 分布是否唯一/受限"""
from itertools import combinations
from collections import Counter
import sys

def run(n, M, cap=4_000_000):
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
    cnt = 0
    for comb in combinations(range(N), M):
        cnt += 1
        cov = 0
        for c in comb:
            cov |= balls[c]
        if cov != full:
            continue
        A = sum(1 for a, b in combinations(comb, 2) if (a ^ b).bit_count() <= 2)
        Q = 2 * A - E
        Qs[Q] += 1
        ex.setdefault(Q, comb)
        if cnt > cap:
            return E, Qs, ex, -1
    return E, Qs, ex, cnt

for (n, M) in ((4, 4), (4, 5), (4, 6), (5, 7), (5, 8)):
    E, Qs, ex, cnt = run(n, M)
    tag = "完整枚举" if cnt >= 0 else "未跑完"
    print(f"n={n} M={M}: E={E} 覆盖码数={sum(Qs.values())} Q分布={dict(sorted(Qs.items()))} [{tag}]")
    if Qs:
        for q in (min(Qs), max(Qs)):
            print(f"    Q={q} 例: {[format(x,'0%db'%n) for x in ex[q]]}")
