#!/usr/bin/env python3
"""k=3,d=4 逐类展开 + Level B 机制检验：x 的私有点能否全部被 ∪B₂(pᵢ) 吃掉？"""
import random, sys, itertools
from collections import Counter, defaultdict
sys.argv = ['x', '5', 'none']
exec(open('/home/node/.openclaw/workspace/dn-project/work/k10/exact_pack.py').read().split('def main()')[0])
CODE = set(WORDS)
BALL2 = {}
for w in range(1024):
    m = 0
    for i in range(10):
        m |= 1 << (w ^ (1 << i))
        for j in range(i + 1, 10):
            m |= 1 << (w ^ (1 << i) ^ (1 << j))
    m |= 1 << w
    BALL2[w] = m

PRIV = {i: [v for v in range(1024) if owners[v] == [i]] for i in range(120)}


def greedy_pack(pts, target, banned=0):
    rem = pts & ~banned
    got = []
    while len(got) < target and rem:
        v = (rem & -rem).bit_length() - 1
        got.append(v)
        t = rem
        nxt = 0
        while t:
            u = (t & -t).bit_length() - 1
            t &= t - 1
            if (u ^ v).bit_count() >= 3:
                nxt |= 1 << u
        rem = nxt
    return got


random.seed(555)
type_hist = Counter()
priv_covered = Counter()
surv_hist = Counter()
fail = 0
tot = 0
for _ in range(400):
    D = tuple(sorted(random.sample(range(120), 4)))
    Xw = [WORDS[i] for i in D]
    U = U_of(D)
    if U == 0:
        continue
    pts = [v for v in range(1024) if (U >> v) & 1]
    for xi in range(4):
        x = Xw[xi]
        B1x = (1 << x) | sum(1 << (x ^ (1 << j)) for j in range(10))
        # k=3 packing，且不含 x 的锚点（banned 掉 B1(x) 以免 anchor x）
        P = greedy_pack(U, 3, banned=B1x)
        if len(P) < 3:
            continue
        r = tuple(sorted((x ^ p).bit_count() for p in P))
        type_hist[r] += 1
        # x 的私有点（全部落在 B1(x) 内）
        pv = [v for v in PRIV[D[xi]] if (B1x >> v) & 1]   # D[xi]=码字索引
        surv = [v for v in pv if not any((v ^ p).bit_count() <= 2 for p in P)]
        tot += 1
        surv_hist[len(surv)] += 1
        priv_covered[len(pv)] += 1
        if len(surv) == 0:
            fail += 1
print(f"样本 {tot} 例（每个 x 一个 k=3 packing）")
print(f"r 型分布 top10: {type_hist.most_common(10)}")
print(f"x 私有点（在 B₁(x) 内）数-被吃数 = 存活数分布: {dict(sorted(surv_hist.items()))}")
print(f"存活 = 0（即 Level B 失败）例数 = {fail}   （应为 0）")
