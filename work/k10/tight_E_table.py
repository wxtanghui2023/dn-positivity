#!/usr/bin/env python3
"""紧型：坏 f 下三个候选簇的 (|C_i|, e_i) 原始分布。
e_i = |C_i \\ (B2(f) ∪ B2(q_j) ∪ B2(q_k))|，q_j,q_k 为另两个保留 packing 点。
e_i ≥ 1 ⟺ 该簇可直接交换（保持兼容且避开 f）。
"""
import random, sys, itertools
from collections import Counter, defaultdict
sys.argv = ['x', '5', 'none']
exec(open('/home/node/.openclaw/workspace/dn-project/work/k10/exact_pack.py').read().split('def main()')[0])


def S_idx_of(q):
    return [i for i, w in enumerate(WORDS) if (w ^ q).bit_count() <= 1]


random.seed(31337)
tab = defaultdict(Counter)      # |C_i| -> Counter(e_i)
emin_hist = Counter()
emin_ge5 = Counter()
rows = []
for _ in range(120):
    D = tuple(sorted(random.sample(range(120), 4)))
    Xw = [WORDS[i] for i in D]
    U = U_of(D)
    if U == 0:
        continue
    pts = [v for v in range(1024) if (U >> v) & 1]
    Cs = [[q for q in pts if (q ^ x).bit_count() <= 1] for x in Xw]
    for t in range(4):
        x = Xw[t]
        other_idx = [i for i in range(4) if i != t]
        for Q in itertools.product(*[Cs[i] for i in other_idx]):
            if min((Q[a] ^ Q[b]).bit_count() for a, b in itertools.combinations(range(3), 2)) < 3:
                continue
            rs = tuple(sorted((q ^ x).bit_count() for q in Q))
            if rs not in ((2, 3, 3), (3, 3, 3)):
                continue
            B1x = [x] + [x ^ (1 << j) for j in range(10)]
            F = [v for v in B1x if all((v ^ q).bit_count() >= 3 for q in Q)]
            if len(F) != 2:
                continue
            for f in [v for v in F if v not in pts]:
                es = []
                sizes = []
                for k, ci in enumerate(other_idx):
                    keep = [Q[j] for j in range(3) if j != k]
                    Ei = [qp for qp in Cs[ci]
                          if (qp ^ f).bit_count() >= 3
                          and all((qp ^ qq).bit_count() >= 3 for qq in keep)]
                    es.append(len(Ei))
                    sizes.append(len(Cs[ci]))
                emin_hist[min(es)] += 1
                for s, e in zip(sizes, es):
                    tab[s][e] += 1
                if all(s >= 5 for s in sizes):
                    emin_ge5[min(es)] += 1
                if len(rows) < 12:
                    rows.append((list(D), t, rs, sizes, es))
print(f"坏 f 实例数 = {sum(emin_hist.values())}")
print(f"min_i e_i 分布 = {dict(sorted(emin_hist.items()))}")
print(f"\n(|C_i|, e_i) 交叉表（行=|C_i|，列=e_i 计数）:")
for s in sorted(tab):
    print(f"  |C_i|={s:2d}: {dict(sorted(tab[s].items()))}   （共 {sum(tab[s].values())} 簇）")
print(f"\n所有 |C_i|>=5 的实例: min_i e_i 分布 = {dict(sorted(emin_ge5.items()))}")
print(f"\n样例 (D, t, rs, sizes, e_i):")
for r in rows:
    print("   ", r)
