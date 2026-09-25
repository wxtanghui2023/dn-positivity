#!/usr/bin/env python3
"""最小阻塞证书分析（d=4）：max_{兼容 q1q2q3} |C_4 ∩ ∪B₂(q_i)| 相对 |C_4|。
   满覆盖 ⟺ 阻塞成立（μ≤3 的必要条件）。并记录"未覆盖余量"分布与最紧例。
"""
import random, sys, itertools
from collections import Counter
sys.argv = ['x', '5', 'none']
exec(open('/home/node/.openclaw/workspace/dn-project/work/k10/exact_pack.py').read().split('def main()')[0])

B2 = {}
for w in range(1024):
    m = 1 << w
    for i in range(10):
        m |= 1 << (w ^ (1 << i))
        for j in range(i + 1, 10):
            m |= 1 << (w ^ (1 << i) ^ (1 << j))
    B2[w] = m


def triples_compatible(Cs):
    for q1 in Cs[0]:
        for q2 in Cs[1]:
            if (q1 ^ q2).bit_count() < 3:
                continue
            for q3 in Cs[2]:
                if (q1 ^ q3).bit_count() < 3 or (q2 ^ q3).bit_count() < 3:
                    continue
                yield (q1, q2, q3)


random.seed(4242)
margin_hist = Counter()
full_cover = 0
tight = []
tot = 0
for _ in range(300):
    D = tuple(sorted(random.sample(range(120), 4)))
    Xw = [WORDS[i] for i in D]
    U = U_of(D)
    if U == 0:
        continue
    pts = [v for v in range(1024) if (U >> v) & 1]
    Cs = [[q for q in pts if (q ^ x).bit_count() <= 1] for x in Xw]
    for target in range(4):
        others = [Cs[i] for i in range(4) if i != target]
        C4 = Cs[target]
        worst = len(C4) + 1
        ntri = 0
        for (q1, q2, q3) in triples_compatible(others):
            ntri += 1
            cov = sum(1 for v in C4 if ((B2[q1] | B2[q2] | B2[q3]) >> v) & 1)
            if cov < worst:
                worst = cov
        if ntri == 0:
            continue
        best = worst                      # 最小覆盖（决定是否存在可增广三元组）
        tot += 1
        margin = len(C4) - best
        margin_hist[margin] += 1
        if margin == 0:
            full_cover += 1
        elif margin <= 1 and len(tight) < 6:
            tight.append((list(D), target, len(C4), best))
print(f"样本(每 D × 4 个 target 簇) = {tot}")
print(f"未覆盖余量 |C₄|-max覆盖 分布 = {dict(sorted(margin_hist.items()))}")
print(f"满覆盖（阻塞成立）例数 = {full_cover}   （应为 0 —— μ=4 已 500/500）")
print(f"最紧例（余量=1，D, target, |C₄|, 覆盖）:")
for t in tight:
    print("   ", t)
