#!/usr/bin/env python3
"""
CORE_all_distance2_forcing_probe.py — A-型最小分析（第二问）：bound 是否 index-free？

目的
  上一档（CORE_all_distance2_analysis）已把"全距 2 型"拆成两形状：
    STAR：公共点 y* 落在四球交内（重数 4）+ 6 个配对中点
    TRI ：四点 e_a,e_b,e_c,e_ab c 各具重数 3
  本档判定：L>=4（或 U>=3）究竟由【形状】强制，还是由【Σ>=|E| 这个全局尺寸条件】强制？
  判据（唐先生 20:52）：若必须依赖具体坐标/E-结构 ⟹ STOP 转 B

问法与输出
  Q1 该型全体四元组中，"特殊点 ∈ E"的频率（STAR: y*；TRI: 四个角点全 ∈ E）
  Q2 列联表：(特殊点 ∈ E) × (Σ >= |E|)  ⟹ 看 Σ>=|E| 是否等价于特殊点 ∈ E
  Q3 L 的分布：全体 vs 候选；以及"给定特殊点 ∈ E"时的 min L
  Q4 若 Σ>=|E| 时特殊点必 ∈ E，则该型内 L 的下界可由几何给出（index-free 候选命题）

输入
  work/k10/c62/keri_pool/K_9_1_classif.txt / work/k10/c62/residual16_A.txt
输出
  scripts/CORE_all_distance2_forcing_probe.txt

provenance: 本轮（唐先生 2026-09-27 20:52）
"""
import re, itertools, os

n = 10; N = 1 << n
BALL = [[y for y in range(N) if bin(y ^ p).count('1') <= 1] for p in range(N)]
BM = [0] * N
for p in range(N):
    m = 0
    for y in BALL[p]:
        m |= 1 << y
    BM[p] = m
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PATH = os.path.join(BASE, "work/k10/c62/keri_pool/K_9_1_classif.txt")
FAILS = os.path.join(BASE, "work/k10/c62/residual16_A.txt")
if not os.path.exists(FAILS):
    FAILS = "/tmp/kopt22_fails.txt"
ws = []
for line in open(PATH, encoding='utf-8', errors='ignore'):
    t = line.split()
    if len(t) == 9 and all(x in ("0", "1") for x in t):
        ws.append(int("".join(t), 2))
C = [(c << 1) for c in ws[:62]] + [(c << 1) | 1 for c in ws[62:124]]
Cset = set(C)
cnt = [0] * N
for p in C:
    for y in BALL[p]:
        cnt[y] += 1
FCfree = [None] * N
for z in range(N):
    FCfree[z] = [p for p in BALL[z] if p not in Cset]
fails = []
for line in open(FAILS, encoding='utf-8', errors='ignore'):
    mm = re.search(r"\((\d+), (\d+), (\d+), (\d+)\)", line)
    if mm:
        fails.append(tuple(int(x) for x in mm.groups()))

stat = {}   # (shape, special_in_E) -> [count, n_cand, minL, minL_cand, sumL]
Lall = {}   # shape -> L 分布
for idxs in fails:
    A = [C[x] for x in idxs]
    for a in A:
        for z in BALL[a]:
            cnt[z] -= 1
    E = 0
    for a in A:
        for z in BALL[a]:
            if cnt[z] == 0:
                E |= 1 << z
    for a in A:
        for z in BALL[a]:
            cnt[z] += 1
    pts = []
    e = E
    while e:
        b = e & -e
        pts.append(b.bit_length() - 1)
        e ^= b
    NE = len(pts)
    Q = sorted(set(w for z in pts for w in FCfree[z]))
    W = [bin(BM[z] & E).count('1') for z in Q]
    P = [i for i in range(len(Q)) if W[i] >= 2]
    mP = len(P)
    if mP < 4:
        continue
    Dmat = [[bin(Q[P[i]] ^ Q[P[j]]).count('1') for j in range(mP)] for i in range(mP)]
    for comb in itertools.combinations(range(mP), 4):
        if any(Dmat[comb[x]][comb[y]] != 2 for x in range(4) for y in range(x + 1, 4)):
            continue
        zs = [P[c] for c in comb]
        w = [W[z] for z in zs]; S = sum(w)
        cover = 0
        for z in zs:
            cover |= (BM[Q[z]] & E)
        U = NE - bin(cover).count('1'); L = S - bin(cover).count('1')
        com = BM[Q[zs[0]]] & BM[Q[zs[1]]] & BM[Q[zs[2]]] & BM[Q[zs[3]]]
        shape = "STAR" if com else "TRI"
        spec = (com & E) != 0           # STAR 用公共点；TRI 单独算
        if shape == "TRI":
            # TRI 的四个角点 = 三点对交集里"重数 3"的点（此处用几何：距 z_i<=1 的点按重数分组）
            mult = {}
            for zi in zs:
                e2 = BM[Q[zi]] & E
                while e2:
                    b = e2 & -e2
                    yy = b.bit_length() - 1
                    mult[yy] = mult.get(yy, 0) + 1
                    e2 ^= b
            spec = sum(1 for k, v in mult.items() if v == 3) >= 3   # 至少 3 个重数 3 的点 ∈ E
        Lall.setdefault(shape, []).append(L)
        key = (shape, spec)
        st = stat.setdefault(key, [0, 0, 99, 99])
        st[0] += 1
        st[2] = min(st[2], L)
        if S >= NE:
            st[1] += 1
            st[3] = min(st[3], L)
print("[D2F] ==== 列联表：(形状, 特殊点∈E) × (Σ>=|E|) ====")
print("[D2F] 形状 | 特殊点∈E | 总四元组 | 候选数 | 全体 minL | 候选 minL")
for k in sorted(stat):
    v = stat[k]
    print("[D2F]   %-4s | %-5s | %8d | %6d | %6d | %6d" % (k[0], k[1], v[0], v[1], v[2], v[3]))
print("[D2F] ==== L 分布（该型全体）====")
for k in sorted(Lall):
    d = {}
    for L in Lall[k]:
        d[L] = d.get(L, 0) + 1
    print("[D2F]   %-4s n=%d  L分布=%s" % (k, len(Lall[k]), sorted(d.items())))
