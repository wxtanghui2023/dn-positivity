#!/usr/bin/env python3
"""Step 2：不依赖文献表格，直接构造最优码并算 Q
   (A) n=6, M=K(6,1)=12：随机局部搜索大量成功覆盖码，统计 Q 分布
   (B) n=8：doubled Hamming 码（32=K(8,1)）解析+实算 Q
"""
import random
from itertools import combinations
from collections import Counter

def Qof(n, C):
    N = 1 << n; M = len(C)
    E = M * (n + 1) - N
    A = sum(1 for a, b in combinations(sorted(C), 2) if (a ^ b).bit_count() <= 2)
    return 2 * A - E, E, A

def search(n, M, trials=250, iters=400, seed=1):
    random.seed(seed)
    N = 1 << n
    nbr = [[v ^ (1 << i) for i in range(n)] for v in range(N)]
    ok = {}
    for _ in range(trials):
        C = set(random.sample(range(N), M))
        cnt = [0] * N
        for c in C:
            cnt[c] += 1
            for u in nbr[c]: cnt[u] += 1
        for _it in range(iters):
            unc = [x for x in range(N) if cnt[x] == 0]
            if not unc: break
            p = random.choice(unc)
            cadd = random.choice([p] + nbr[p])
            if cadd in C: continue
            C.add(cadd); cnt[cadd] += 1
            for u in nbr[cadd]: cnt[u] += 1
            best, bestw = -1, None
            for w in list(C):
                if w == cadd: continue
                cnt[w] -= 1
                for u in nbr[w]: cnt[u] -= 1
                sc = sum(1 for x in [w] + nbr[w] if cnt[x] == 0)
                if bestw is None or sc < best:
                    best, bestw = sc, w
                cnt[w] += 1
                for u in nbr[w]: cnt[u] += 1
            if bestw is not None:
                C.discard(bestw); cnt[bestw] -= 1
                for u in nbr[bestw]: cnt[u] -= 1
        if all(cnt[x] > 0 for x in range(N)) and len(C) == M:
            ok[frozenset(C)] = Qof(n, C)
    return ok

print("=== (A) n=6, M=12 (=K(6,1)) ===")
ok = search(6, 12, trials=250, iters=400)
print(f"  成功找到不同的 12-字覆盖码: {len(ok)} 个")
qdist = Counter(v[0] for v in ok.values())
print(f"  Q 分布 = {dict(sorted(qdist.items()))}")
E6 = 12 * 7 - 64
print(f"  E = {E6}；若 Q 唯一 ⟹ 钉住 ✓；若多个值 ⟹ 钉住被反驳 ✗")
for q in sorted(qdist)[:3]:
    ex = [k for k, v in ok.items() if v[0] == q][0]
    print(f"    Q={q}: A1+A2={ok[ex][2]}  例={' '.join(format(x,'06b') for x in sorted(ex))}")

print()
print("=== (B) n=8: doubled Hamming 码（K(8,1)=32）===")
# Hamming(7) 码：所有 7-bit 字，其校验和(parity-check)为 0；标准取 {c: H c^T = 0}，|C|=16
H = [[1,1,1,0,1,0,0],[1,1,0,1,0,1,0],[1,0,1,1,0,0,1]]  # 3x7 校验矩阵（列=1..7 二进制）
def ham7():
    out = []
    for x in range(128):
        bits = [(x >> i) & 1 for i in range(7)]
        if all(sum(H[r][i] * bits[i] for i in range(7)) % 2 == 0 for r in range(3)):
            out.append(x)
    return out
H7 = ham7()
print(f"  Hamming(7) 码字数 = {len(H7)} (应 16 ✓)")
# doubled: 加一个坐标（0/1）⟹ 32 字，长 8
C8 = set()
for c in H7:
    C8.add(c << 1)        # 末位 0
    C8.add((c << 1) | 1)  # 末位 1
print(f"  doubled 码字数 = {len(C8)}")
q8, E8, A8 = Qof(8, C8)
print(f"  E={E8}  A1+A2={A8}  Q={q8}")
# 覆盖性与重数分布核对
N8 = 1 << 8
cnt8 = [0] * N8
for c in C8:
    cnt8[c] += 1
    for i in range(8): cnt8[c ^ (1 << i)] += 1
print(f"  min b(x) = {min(cnt8)} (>0 ⟹ 覆盖 ✓)  b 分布 = {dict(sorted(Counter(cnt8).items()))}")
