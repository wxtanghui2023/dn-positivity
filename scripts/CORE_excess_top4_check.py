#!/usr/bin/env python3
"""
CORE_excess_top4_check.py — OPEN CORE 精确核验：max_D Sigma_D|S_z| <= |E|+1 ？

目的
  1) 核验 §5.22 的「远距(c=0)无候选 ⟹ c(D)>=2」是否足够（预期：不足，只给 c>=1）
  2) 精确判定 OPEN CORE：max_{|D|=4} Sigma_D|S_z| <= |E|+1
     （关键恒真化简：Sigma 只依赖四个权重 W(z)=|B_1(z)∩E| ⟹ max = top-4 权重和）

输入
  work/k10/c62/keri_pool/K_9_1_classif.txt   码 C 的 124 个 9-bit 词（来源：K_9_1 分类枚举）
  work/k10/c62/residual16_A.txt              16 个残余四元组 A（来源：L3-α 残余，kopt20/kopt22 产物）
  （若 work/ 路径缺失，回退 /tmp/kopt22_fails.txt）

输出
  scripts/CORE_excess_top4_check.txt         逐例读数 + 汇总

结论（2026-09-27）
  ① 远距(c=0) max Sigma = 16 < 17 <= |E|，但 c<=1 max Sigma 达 18 ⟹ 只给 c>=1；c>=2 需单独排除 c=1
     ⟹ 补算逐例 c<=1 max Sigma < |E|（余量 1~5）⟹ c>=2 结论成立，依据替换
  ② 16/16 例 top-4 <= |E|+1（excess ∈{0,1}，0 越界）；池内 873,472 四元组 excess>1 = 0
  ③ 恒等式 |∪S_z| = |E| - U ⟹ 链条净内容 = U>=3

provenance: /tmp/kopt37b_core.py（本轮原始）；池缩减 P={|S_z|>=2} 由 M3+1<|E| 严格保证
"""
import re, itertools, os, sys

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

gM4 = 0; gM4over = 0; gfar = 0; gc1 = 0; EMIN = 99
viol = []; gt1 = 0; nq = 0; profmax = {}; profu = {}
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
    m_all = len(Q)
    P = [i for i in range(m_all) if W[i] >= 2]
    Ws = sorted(W, reverse=True)
    M4 = sum(Ws[:4]); M3 = sum(Ws[:3])
    near = {}
    for i in P:
        mi = 0
        for j in P:
            if i != j and bin(Q[i] ^ Q[j]).count('1') <= 2:
                mi |= 1 << j
        near[i] = mi
    bestAll = (-1, None, 0); bestFar = (-1, None); bestC1 = (-1, None, 0)
    exmin = 10**9; exmax = -10**9; egt1 = 0; npq = 0
    for comb in itertools.combinations(P, 4):
        s = W[comb[0]] + W[comb[1]] + W[comb[2]] + W[comb[3]]
        nf = 0
        for x in range(4):
            for y in range(x + 1, 4):
                if not (near[comb[x]] >> comb[y]) & 1:
                    nf += 1
        c = 6 - nf; ex = s - NE; npq += 1
        exmin = min(exmin, ex); exmax = max(exmax, ex)
        if ex > 1:
            egt1 += 1; gt1 += 1
        if s > bestAll[0]: bestAll = (s, comb, c, ex)
        if c == 0 and s > bestFar[0]: bestFar = (s, comb)
        if c <= 1 and s > bestC1[0]: bestC1 = (s, comb, c)
    s, comb, c, ex = bestAll
    mult = {}
    for i in comb:
        for y in pts:
            if (BM[Q[i]] >> y) & 1:
                mult[y] = mult.get(y, 0) + 1
    L = s - len(mult); U = NE - len(mult)
    prof = {}
    for y in pts:
        k = mult.get(y, 0)
        prof[k] = prof.get(k, 0) + 1
    profu[tuple(sorted(prof.items()))] = profu.get(tuple(sorted(prof.items())), 0) + 1
    kk = tuple(sorted([W[i] for i in comb]))
    profmax[kk] = profmax.get(kk, 0) + 1
    nq += npq; EMIN = min(EMIN, NE)
    gM4 = max(gM4, M4); gfar = max(gfar, bestFar[0]); gc1 = max(gc1, bestC1[0])
    if M4 > NE + 1:
        gM4over += 1; viol.append((idxs, NE, M4))
    print("[CORE_top4] A=%-22s |E|=%2d |Q|=%3d |P|=%2d | top4=%2d (<=|E|+1? %s) | far_max=%2d | c<=1_max=%2d(c=%d) | ex:[%d,%d] gt1=%d"
          % (str(idxs), NE, m_all, len(P), M4, "Y" if M4 <= NE + 1 else "N!", bestFar[0], bestC1[0], bestC1[2], exmin, exmax, egt1))
    print("            argmax sizes=%s L=%d U=%d ex=L-U=%d prof=%s | M3+1=%d"
          % ([W[i] for i in comb], L, U, L - U, sorted(prof.items()), M3 + 1))
print("[CORE_top4] ==== 汇总 ====")
print("[CORE_top4] P-四元组总数 = %d ｜ min|E| = %d" % (nq, EMIN))
print("[CORE_top4] top4(=max Σ over ALL 四元组) 全局最大 = %d ｜ 越界例数 = %d %s" % (gM4, gM4over, viol[:3]))
print("[CORE_top4] far(c=0, 池内) max Σ = %d  (只给 c>=1)" % gfar)
print("[CORE_top4] c<=1(池内) max Σ = %d  (逐例须 < |E| 才得 c>=2)" % gc1)
print("[CORE_top4] excess>1 的池内四元组数 = %d" % gt1)
print("[CORE_top4] argmax sizes 轮廓 = %s" % sorted(profmax.items(), key=lambda x: -x[1]))
print("[CORE_top4] 多重度剖面分布 = %s" % sorted(profu.items(), key=lambda x: -x[1]))
