#!/usr/bin/env python3
"""Level B 余量测量：d=4 抽样，取 k=3 packing + 未覆盖 anchor x，统计 (|C_x|, |F_x|, r_i)。"""
import random, sys
from collections import Counter
sys.argv = ['x', '5', 'none']
exec(open('/home/node/.openclaw/workspace/dn-project/work/k10/exact_pack.py').read().split('def main()')[0])
CODE = set(WORDS)
BALL = {}
for w in range(1024):
    m = 1 << w
    for b in range(10):
        m |= 1 << (w ^ (1 << b))
    BALL[w] = m
BALL2 = {}
for w in range(1024):
    m = BALL[w]
    for b in range(10):
        m |= BALL[w ^ (1 << b)]
    BALL2[w] = m


def greedy_pack(pts, target):
    rem = pts
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


random.seed(2024)
r_hist = Counter()
slack_hist = Counter()
Cx_hist = Counter()
fail = 0
tot = 0
for _ in range(300):
    D = tuple(sorted(random.sample(range(120), 4)))
    Xw = [WORDS[i] for i in D]
    U = U_of(D)
    if U == 0:
        continue
    pts = [v for v in range(1024) if (U >> v) & 1]
    P = greedy_pack(U, 3)                      # 取 3 个 packing 点
    if len(P) < 3:
        continue
    anchored = set()
    for p in P:
        for i, x in enumerate(Xw):
            if (p ^ x).bit_count() <= 1:
                anchored.add(i)
    uncov = [i for i in range(4) if i not in anchored]
    if not uncov:
        continue
    for i in uncov:
        x = Xw[i]
        Cx = [q for q in pts if (q ^ x).bit_count() <= 1]        # 合法候选（含 U_D 约束）
        Fx = [q for q in Cx if any((q ^ p).bit_count() <= 2 for p in P)]
        free = [q for q in Cx if q not in Fx]
        tot += 1
        Cx_hist[len(Cx)] += 1
        slack_hist[len(free)] += 1
        r_hist[tuple(sorted((x ^ p).bit_count() for p in P))] += 1
        if len(free) == 0:
            fail += 1
print(f"样本(未覆盖 anchor 情形) {tot} 例")
print(f"|C_x| 分布 = {dict(sorted(Cx_hist.items()))}")
print(f"自由候选数分布 = {dict(sorted(slack_hist.items()))}   （0 即增广失败）")
print(f"增广失败例数 = {fail}   （应为 0 —— α₂=|D| 全量已验）")
print(f"r_i=(d(x,p)) 型分布 top8 = {r_hist.most_common(8)}")
