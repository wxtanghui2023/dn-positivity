#!/usr/bin/env python3
"""n=8 关键判定：以 doubled Hamming (32=K(8,1)) 为起点做"保覆盖切换"搜索，
   看是否存在 Q != 0 的最优码 ⟹ 若存在则"最小覆盖钉住"在 n=8 被反驳 ✗"""
import random
from itertools import combinations
from collections import Counter

n = 8; N = 1 << n; M = 32
E = M * (n + 1) - N

def balls():
    b = []
    for v in range(N):
        m = 1 << v
        for i in range(n): m |= 1 << (v ^ (1 << i))
        b.append(m)
    return b
BALL = balls()

def covcnt(C):
    cnt = [0] * N
    for c in C:
        m = BALL[c]
        while m:
            low = m & -m; cnt[low.bit_length() - 1] += 1; m ^= low
    return cnt

def Qof(C):
    A = sum(1 for a, b in combinations(sorted(C), 2) if (a ^ b).bit_count() <= 2)
    return 2 * A - E, A

# Hamming(7)
H = [[1,1,1,0,1,0,0],[1,1,0,1,0,1,0],[1,0,1,1,0,0,1]]
H7 = [x for x in range(128) if all(sum(H[r][i] * ((x >> i) & 1) for i in range(7)) % 2 == 0 for r in range(3))]
start = set()
for c in H7:
    start.add(c << 1); start.add((c << 1) | 1)
print(f"起点: doubled Hamming, |C|={len(start)}, Q={Qof(start)[0]}")

random.seed(7)
found = {}
cur = set(start)
cnt = covcnt(cur)
for step in range(60000):
    w = random.choice(list(cur))
    # w 的"私有点"：仅被 w 覆盖的点
    priv = [p for p in range(N) if cnt[p] == 1 and (p == w or (p ^ w).bit_count() == 1)]
    # 需要 w' 覆盖 priv 中所有点 ⟹ w' ∈ ∩ N[p]
    cand = None
    if priv:
        inter = None
        for p in priv:
            s = set([p] + [p ^ (1 << i) for i in range(n)])
            inter = s if inter is None else (inter & s)
            if not inter: break
        if inter:
            opts = [x for x in inter if x != w]
            if opts: cand = random.choice(opts)
    if cand is None:
        continue
    cur.discard(w); cur.add(cand)
    cnt = covcnt(cur)
    if min(cnt) > 0 and len(cur) == M:
        q, a = Qof(cur)
        found.setdefault(frozenset(cur), (q, a))
    else:
        cur.discard(cand); cur.add(w); cnt = covcnt(cur)

print(f"切换搜索后收集到不同最优码: {len(found)} 个")
qd = Counter(v[0] for v in found.values())
print(f"Q 分布 = {dict(sorted(qd.items()))}")
for q in sorted(qd):
    ex = [k for k, v in found.items() if v[0] == q][0]
    print(f"   Q={q}: A1+A2={found[ex][1]}  例={' '.join(format(x,'08b') for x in sorted(ex))}")
print()
print("判定: 若 Q 分布只有一个值 ⟹ n=8 亦钉住 ✓；若出现多个值 ⟹ 钉住被反驳 ✗")
