#!/usr/bin/env python3
"""
CORE_distance_type_probe.py — OPEN CORE 结构路线：excess 是否只由四元组的「距离型」决定？

目的
  判定 Sigma_D|S_z| - |E| <= 1 能否靠「4 个中心的距离型」做有限 case analysis
  （若型决定 excess ⟹ index-free 型证明可行；若否 ⟹ 必须用 E 的 A-专有结构）

输入
  work/k10/c62/keri_pool/K_9_1_classif.txt   码 C（124 个 9-bit 词）
  work/k10/c62/residual16_A.txt              16 个残余四元组 A

输出
  scripts/CORE_distance_type_probe.txt       型数 / 型级 max excess / 达到 excess=1 的型明细

结论（2026-09-27）
  相异距离型 33；含候选(Σ>=|E|) 12 型；达 excess=1 5 型（28 个四元组）；max excess>1 的型 0
  ⟹ case-list 有限 ✓，但同型可取 excess = -1/0/+1 ⟹ 型不决定 excess ⟹ 型分析须配 A-专有结构

provenance: /tmp/kopt38_types.py（本轮原始）；型签名 = 4 点各自距离三元组（排序后）的排序元组
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

sig_maxex = {}; sig_maxS = {}; sig_cand = {}; sig_n = {}; ex1 = {}
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
    WP = [W[i] for i in P]; mP = len(P)
    Dmat = [[bin(Q[P[i]] ^ Q[P[j]]).count('1') for j in range(mP)] for i in range(mP)]
    for comb in itertools.combinations(range(mP), 4):
        s = WP[comb[0]] + WP[comb[1]] + WP[comb[2]] + WP[comb[3]]
        if s < NE - 1:
            continue
        rows = []
        for x in range(4):
            rows.append(tuple(sorted(Dmat[comb[x]][comb[y]] for y in range(4) if y != x)))
        sig = tuple(sorted(rows)); ex = s - NE
        sig_maxex[sig] = max(sig_maxex.get(sig, -99), ex)
        sig_maxS[sig] = max(sig_maxS.get(sig, -99), s)
        sig_n[sig] = sig_n.get(sig, 0) + 1
        if s >= NE:
            sig_cand[sig] = sig_cand.get(sig, 0) + 1
        if ex == 1:
            ex1[sig] = ex1.get(sig, 0) + 1
print("[CORE_type] 相异距离型数 = %d" % len(sig_maxex))
bad = [k for k, v in sig_maxex.items() if v > 1]
print("[CORE_type] max excess > 1 的距离型 = %d  %s" % (len(bad), bad[:5]))
print("[CORE_type] 有候选(Σ>=|E|)的距离型 = %d" % len(sig_cand))
print("[CORE_type] 达到 excess=1 的距离型 = %d （四元组数 %d）" % (len(ex1), sum(ex1.values())))
print("[CORE_type] --- 出现次数最多的距离型（n / max excess / max Σ / 候选数）---")
for sig, c in sorted(sig_n.items(), key=lambda x: -x[1])[:12]:
    print("   n=%5d maxex=%2d maxS=%2d cand=%5d  sig=%s" % (c, sig_maxex[sig], sig_maxS[sig], sig_cand.get(sig, 0), sig))
print("[CORE_type] --- 达到 excess=1 的型明细 ---")
for sig, c in sorted(ex1.items(), key=lambda x: -x[1]):
    print("   n=%4d maxS=%2d  sig=%s" % (c, sig_maxS[sig], sig))
