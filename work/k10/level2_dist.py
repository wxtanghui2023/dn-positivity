#!/usr/bin/env python3
"""63 簇的 |A_j ∪ A_k| 分布 + =2 情形按 owner 类型分类（含重复/共享 owner 与重量型）。"""
import random, sys, itertools
from collections import Counter
sys.argv = ['x', '5', 'none']
exec(open('/home/node/.openclaw/workspace/dn-project/work/k10/exact_pack.py').read().split('def main()')[0])


def S_idx(q):
    return set(i for i, w in enumerate(WORDS) if (w ^ q).bit_count() <= 1)


def d(a, b):
    return (a ^ b).bit_count()


random.seed(31337)
size_hist = Counter()
breakdown = Counter()
weight_type = Counter()
owner_sig = Counter()
dupowner = Counter()
rows = []
n_ci = 0
for _ in range(120):
    D = tuple(sorted(random.sample(range(120), 4)))
    Xw = [WORDS[i] for i in D]
    U = U_of(D)
    if U == 0:
        continue
    pts = [v for v in range(1024) if (U >> v) & 1]
    Cs = [[q for q in pts if d(q, x) <= 1] for x in Xw]
    for t in range(4):
        x = Xw[t]
        other_idx = [i for i in range(4) if i != t]
        for Q in itertools.product(*[Cs[i] for i in other_idx]):
            if min(d(Q[a], Q[b]) for a, b in itertools.combinations(range(3), 2)) < 3:
                continue
            rs = tuple(sorted(d(q, x) for q in Q))
            if rs not in ((2, 3, 3), (3, 3, 3)):
                continue
            B1x = [x] + [x ^ (1 << j) for j in range(10)]
            F = [v for v in B1x if all(d(v, q) >= 3 for q in Q)]
            if len(F) != 2 or not [v for v in F if v not in pts]:
                continue
            for ci in other_idx:
                xi = Xw[ci]
                Ci = Cs[ci]
                T_i = {a for a in range(10) if (xi ^ (1 << a)) in Ci}
                k = other_idx.index(ci)
                keep = [Q[j] for j in range(3) if j != k]
                Aj = {a for a in T_i if d(xi ^ (1 << a), keep[0]) <= 2}
                Ak = {a for a in T_i if d(xi ^ (1 << a), keep[1]) <= 2}
                un = Aj | Ak
                n_ci += 1
                size_hist[len(un)] += 1
                if len(un) != 2:
                    continue
                breakdown[(len(Aj), len(Ak), len(Aj & Ak))] += 1
                wj, wk = d(keep[0], xi), d(keep[1], xi)
                weight_type[tuple(sorted((wj, wk)))] += 1
                aa = sorted(un)
                owners = {a: sorted(S_idx(xi ^ (1 << a)) - {ci}) for a in aa}
                o1, o2 = set(owners[aa[0]]), set(owners[aa[1]])
                owner_sig[(len(o1), len(o2), len(o1 & o2))] += 1
                dup = "相同" if o1 == o2 else ("相交" if o1 & o2 else "不交")
                dupowner[dup] += 1
                if len(rows) < 10:
                    rows.append({"D": list(D), "ci": ci, "T_i": sorted(T_i),
                                 "w": (wj, wk), "Aj": sorted(Aj), "Ak": sorted(Ak),
                                 "un": aa, "owners": owners, "rel": dup,
                                 "coord_dist": d(xi ^ (1 << aa[0]), xi ^ (1 << aa[1]))})
print(f"簇数 = {n_ci}")
print(f"|A_j ∪ A_k| 分布 = {dict(sorted(size_hist.items()))}")
print(f"\n=2 情形细分 (|A_j|,|A_k|,|交|) = {dict(sorted(breakdown.items()))}")
print(f"=2 情形的重量型 (d(q_j,x_i), d(q_k,x_i)) = {dict(sorted(weight_type.items()))}")
print(f"=2 情形的 owner 签名 (|O(a)|,|O(b)|,|交|) = {dict(sorted(owner_sig.items()))}")
print(f"=2 情形的 owner 关系 = {dict(dupowner)}")
print(f"\n=2 样例:")
for r in rows:
    print(f"  D={r['D']} 簇={r['ci']} |T_i|={len(r['T_i'])} 重量={r['w']}")
    print(f"    A_j={r['Aj']} A_k={r['Ak']} 并集={r['un']}  两坐标距离={r['coord_dist']}")
    print(f"    owners={r['owners']}  owner关系={r['rel']}")
