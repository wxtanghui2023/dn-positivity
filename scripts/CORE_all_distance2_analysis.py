#!/usr/bin/env python3
"""
CORE_all_distance2_analysis.py — A-型最小分析：全距 2 型

目的
  只打一个距离型：四个中心两两距离恰为 2（"全距 2 型"）。
  问：(i) 该型有几种形状？(ii) Σ_D|S_z| = |E|+1 时是否被强制 L>=4（即 U>=3）？
  判据：若可 index-free ⟹ 完成压缩；若必须用具体坐标 ⟹ STOP 转 B。

数学要点（本脚本核验的对象）
  取 z1=0（平移），则 z2,z3,z4 权恰 2，且支撑两两相交恰 1 元 ⟹ 只有两种形状：
    · 星形：S2={a,b}, S3={a,c}, S4={a,d}（共同坐标 a）⟹ e_a 落在四个球内（公共点）
    · 三角：S2={a,b}, S3={b,c}, S4={a,c}                ⟹ 无公共点
  ⟹ 用"四球交是否非空"可分形状（星形 ⟺ 存在点距四点均 <=1）

输入
  work/k10/c62/keri_pool/K_9_1_classif.txt    码 C（124 个 9-bit 词）
  work/k10/c62/residual16_A.txt               16 个残余四元组 A

输出
  scripts/CORE_all_distance2_analysis.txt     该型的全部候选读数（Σ,L,U,形状,坐标）

provenance: 本轮（唐先生 2026-09-27 20:52 指令"A-型最小分析，只打一型"）
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

agg = {}          # shape -> [nquad, minL_cand, minU_cand, ncand, ncommon_in_E, minL_all]
rows = []
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
        w = [W[z] for z in zs]
        S = sum(w)
        efl = E
        cover = 0
        for z in zs:
            cover |= (BM[Q[z]] & E)
        U = NE - bin(cover).count('1')
        L = S - bin(cover).count('1')
        com = BM[Q[zs[0]]] & BM[Q[zs[1]]] & BM[Q[zs[2]]] & BM[Q[zs[3]]]
        shape = "STAR" if com else "TRI"
        comE = (com & E) != 0
        # 公共点的重数（星形下应为 4）
        mult4 = 0
        if com:
            cy = (com & -com).bit_length() - 1
            mult4 = sum(1 for z in zs if (BM[Q[z]] >> cy) & 1)
        st = agg.setdefault(shape, [0, 99, 99, 0, 0, 99])
        st[0] += 1
        st[5] = min(st[5], L)
        if S >= NE:
            st[3] += 1
            st[1] = min(st[1], L)
            st[2] = min(st[2], U)
            if comE:
                st[4] += 1
            rows.append((idxs, NE, shape, S, L, U, w, [Q[z] for z in zs], comE, mult4))
print("[D2] ==== 全距 2 型：全部候选（Σ>=|E|）逐条 ====")
for r in sorted(rows, key=lambda x: (x[2], -x[3])):
    print("[D2] A=%-22s |E|=%2d %-4s Σ=%2d L=%2d U=%2d sizes=%s 公共点∈E=%s mult=%d zs=%s"
          % (str(r[0]), r[1], r[2], r[3], r[4], r[5], r[6], r[8], r[9], r[7]))
print("[D2] ==== 形状汇总 ====")
print("[D2] 形状: [四元组数, 候选内 minL, 候选内 minU, 候选数, 公共点∈E 的次数, 全体 minL]")
for k, v in sorted(agg.items()):
    print("[D2]   %-4s %s" % (k, v))
