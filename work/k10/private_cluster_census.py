#!/usr/bin/env python3
"""私有簇 census + 4-簇独立横截面（d=4）：
   C_x = B_1(x)∩U_D；检查是否 partition；κ(x,y)；μ(D)（回溯，从最小簇起）；
   输出见证 (q_1..q_4) 与距离矩阵 R_ij=d(q_i,x_j)。
"""
import random, sys, itertools
from collections import Counter
sys.argv = ['x', '5', 'none']
exec(open('/home/node/.openclaw/workspace/dn-project/work/k10/exact_pack.py').read().split('def main()')[0])


def mu_transversal(Cs):
    """Cs: list of lists（每簇候选）。返回 (size, witness) 最大独立横截面（两两 d>=3）。"""
    order = sorted(range(len(Cs)), key=lambda i: len(Cs[i]))
    best, bw = 0, None

    def rec(t, chosen):
        nonlocal best, bw
        if len(chosen) + (len(Cs) - t) <= best:
            return
        if t == len(Cs):
            if len(chosen) > best:
                best, bw = len(chosen), list(chosen)
            return
        i = order[t]
        for q in Cs[i]:
            if all((q ^ p).bit_count() >= 3 for p in chosen):
                chosen.append(q)
                rec(t + 1, chosen)
                chosen.pop()
        rec(t + 1, chosen)                      # 允许跳过该簇

    rec(0, [])
    return best, bw


random.seed(9090)
minC = Counter()
part_ok = 0
part_bad = 0
shared_hist = Counter()
mu_hist = Counter()
kappa_hist = Counter()
R_examples = []
fails = []
for _ in range(500):
    D = tuple(sorted(random.sample(range(120), 4)))
    Xw = [WORDS[i] for i in D]
    U = U_of(D)
    if U == 0:
        continue
    pts = [v for v in range(1024) if (U >> v) & 1]
    Cs = [[q for q in pts if (q ^ x).bit_count() <= 1] for x in Xw]
    # partition 检查：U_D 中每个点是否恰属一个簇
    cnt = [0] * len(pts)
    for j, c in enumerate(Cs):
        for q in c:
            cnt[pts.index(q)] += 1
    if all(c == 1 for c in cnt):
        part_ok += 1
    else:
        part_bad += 1
        shared_hist[sum(1 for c in cnt if c > 1)] += 1
    minC[min(len(c) for c in Cs)] += 1
    # κ(x,y)
    for a, b in itertools.combinations(range(4), 2):
        k = max(((q ^ r).bit_count() for q in Cs[a] for r in Cs[b]), default=0)
        kappa_hist[k] += 1
    m, w = mu_transversal(Cs)
    mu_hist[m] += 1
    if m < 4:
        fails.append((D, [len(c) for c in Cs], m, w))
    elif len(R_examples) < 5 and w:
        R_examples.append((D, w, [[(q ^ x).bit_count() for x in Xw] for q in w]))
print(f"样本 500 例")
print(f"① 簇是否 partition U_D: 是 {part_ok} | 否 {part_bad}")
if part_bad:
    print(f"   非 partition 例中，共享点数分布 = {dict(sorted(shared_hist.items()))}")
print(f"② min|C_x| 分布 = {dict(sorted(minC.items()))}")
print(f"③ κ(x,y) 分布（6 对/例） = {dict(sorted(kappa_hist.items()))}")
print(f"④ μ(D)（最大独立横截面）分布 = {dict(sorted(mu_hist.items()))}   （4 为目标）")
print(f"⑤ μ(D)<4 的失败例 = {len(fails)}")
for f in fails[:4]:
    print("   ", f)
print(f"\n⑥ 见证与距离矩阵样例 (D, (q_1..q_4), R_ij=d(q_i,x_j)):")
for D, w, R in R_examples[:3]:
    print(f"   D={D} 见证={w}")
    print(f"      R={R}   （对角≤1 且非对角≥2? {all(R[i][i]<=1 for i in range(4)) and all(R[i][j]>=2 for i in range(4) for j in range(4) if i!=j)}）")
