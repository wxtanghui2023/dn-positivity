#!/usr/bin/env python3
"""第二步实验：最小覆盖是否"刚性"（在 Aut(Q_n)=B_n 下唯一轨道 ⟹ 钉住自动成立）？
   同步给出 Q 与 |E(G)| = #{相交球对} = A1+A2 的轨道级数据。
"""
from itertools import combinations, permutations
from collections import Counter

def analyze(n, M):
    N = 1 << n
    balls = []
    for v in range(N):
        m = 1 << v
        for i in range(n):
            m |= 1 << (v ^ (1 << i))
        balls.append(m)
    full = (1 << N) - 1
    covs = []
    for comb in combinations(range(N), M):
        c = 0
        for x in comb:
            c |= balls[x]
        if c == full:
            covs.append(comb)
    # 群 B_n = (Z2)^n ⋊ S_n：x -> 按 p 置换坐标后再 xor t
    maps = []
    for p in permutations(range(n)):
        base = []
        for x in range(N):
            y = 0
            for i in range(n):
                if (x >> i) & 1:
                    y |= 1 << p[i]
            base.append(y)
        for t in range(N):
            maps.append([b ^ t for b in base])
    print(f"n={n} M={M}: 覆盖码 {len(covs)} 个；群阶 {len(maps)}")
    orb = {}
    for comb in covs:
        best = None
        for mp in maps:
            img = tuple(sorted(mp[x] for x in comb))
            if best is None or img < best:
                best = img
        orb.setdefault(best, []).append(comb)
    print(f"  ⟹ B_n-轨道数 = {len(orb)}")
    for k, (rep, members) in enumerate(sorted(orb.items()), 1):
        E = M * (n + 1) - N
        A = sum(1 for a, b in combinations(rep, 2) if (a ^ b).bit_count() <= 2)
        Q = 2 * A - E
        print(f"    轨道{k}: 大小={len(members):5d}  E={E}  |E(G)|=A1+A2={A}  Q={Q}"
              f"  代表={' '.join(format(x, '0%db' % n) for x in rep)}")

analyze(4, 4)
print()
analyze(5, 7)
