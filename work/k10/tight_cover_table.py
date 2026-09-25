#!/usr/bin/env python3
"""紧型最小枚举：对每个 C_i 输出 P_f,P_j,P_k（B₂(z)∩C_i）、并集、owner 模式；
   并检验 Level I: |C_i ∩ B₂(z)| ≤ 2 对 z∈{f,q_j,q_k}。
★ 索引纪律：D=下标元组；Xw=码字；owners[v]=点的码字下标集合；Cs=候选点（码字空间）。
"""
import random, sys, itertools
from collections import Counter, defaultdict
sys.argv = ['x', '5', 'none']
exec(open('/home/node/.openclaw/workspace/dn-project/work/k10/exact_pack.py').read().split('def main()')[0])


def S_idx(q):
    return frozenset(i for i, w in enumerate(WORDS) if (w ^ q).bit_count() <= 1)


random.seed(31337)
L1_hist = Counter()          # 每个 z 的 |P_z| 分布
union_hist = Counter()       # |P_f ∪ P_j ∪ P_k|
rows = []
viol1 = 0
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
                for k, ci in enumerate(other_idx):
                    Ci = Cs[ci]
                    keep = [Q[j] for j in range(3) if j != k]
                    P = [[c for c in Ci if (c ^ z).bit_count() <= 2] for z in [f] + keep]
                    for Pz in P:
                        L1_hist[len(Pz)] += 1
                        if len(Pz) > 2:
                            viol1 += 1
                    un = sorted({c for Pz in P for c in Pz})
                    union_hist[len(un)] += 1
                    if len(un) <= 3 and len(rows) < 14:
                        rows.append({
                            "D": list(D), "t": t, "rs": rs, "ci": ci,
                            "Ci": sorted(Ci), "P_f": sorted(P[0]),
                            "P_j": sorted(P[1]), "P_k": sorted(P[2]),
                            "union": un,
                            "owner": {c: sorted(S_idx(c)) for c in un},
                        })
print(f"Level I 检验: |C_i∩B₂(z)| 分布 = {dict(sorted(L1_hist.items()))}")
print(f"  ⟹ 违例（>2）次数 = {viol1}")
print(f"并集大小 |P_f∪P_j∪P_k| 分布 = {dict(sorted(union_hist.items()))}")
print(f"\n并集 ≤3 的样例（含 owner 模式）:")
for r in rows:
    print(f"  D={r['D']} t={r['t']} rs={r['rs']} 簇={r['ci']}")
    print(f"    C_i({len(r['Ci'])})={r['Ci']}")
    print(f"    P_f={r['P_f']}  P_j={r['P_j']}  P_k={r['P_k']}  union={r['union']}")
    print(f"    owners: {r['owner']}")
