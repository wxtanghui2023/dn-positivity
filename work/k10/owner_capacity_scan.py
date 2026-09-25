#!/usr/bin/env python3
"""扩大样本确认 |A_j∪A_k| ≥ 3 是否出现；并测机制 supp(q⊕x_i) ∩ T_i = ∅。"""
import random, sys, itertools
from collections import Counter
sys.argv = ['x', '5', 'none']
exec(open('/home/node/.openclaw/workspace/dn-project/work/k10/exact_pack.py').read().split('def main()')[0])
d = lambda a, b: (a ^ b).bit_count()

random.seed(20260925)
size_hist = Counter()
mech_ok = 0
mech_bad = 0
mech_bad_rows = []
n_ci = 0
tight = 0
for _ in range(400):
    D = tuple(sorted(random.sample(range(120), 4)))
    Xw = [WORDS[i] for i in D]
    U = U_of(D)
    if U == 0:
        continue
    pts = [v for v in range(1024) if (U >> v) & 1]
    Cs = [[q for q in pts if d(q, x) <= 1] for x in Xw]
    for t in range(4):
        x = Xw[t]
        other = [i for i in range(4) if i != t]
        for Q in itertools.product(*[Cs[i] for i in other]):
            if min(d(Q[a], Q[b]) for a, b in itertools.combinations(range(3), 2)) < 3:
                continue
            rs = tuple(sorted(d(q, x) for q in Q))
            if rs not in ((2, 3, 3), (3, 3, 3)):
                continue
            B1x = [x] + [x ^ (1 << j) for j in range(10)]
            F = [v for v in B1x if all(d(v, q) >= 3 for q in Q)]
            if len(F) != 2 or not [v for v in F if v not in pts]:
                continue
            tight += 1
            for ci in other:
                xi = Xw[ci]
                Ci = Cs[ci]
                T_i = {a for a in range(10) if (xi ^ (1 << a)) in Ci}
                k = other.index(ci)
                keep = [Q[j] for j in range(3) if j != k]
                Aj = {a for a in T_i if d(xi ^ (1 << a), keep[0]) <= 2}
                Ak = {a for a in T_i if d(xi ^ (1 << a), keep[1]) <= 2}
                n_ci += 1
                size_hist[len(Aj | Ak)] += 1
                # 机制检验：supp(q ⊕ x_i) ∩ T_i 是否为空
                for q in keep:
                    S = {a for a in range(10) if ((q ^ xi) >> a) & 1}
                    if S & T_i:
                        mech_bad += 1
                        if len(mech_bad_rows) < 6:
                            mech_bad_rows.append((list(D), t, ci, q, xi, sorted(S), sorted(T_i), sorted(S & T_i)))
                    else:
                        mech_ok += 1
print(f"紧型实例 {tight};  检查簇数 {n_ci}")
print(f"|A_j ∪ A_k| 分布 = {dict(sorted(size_hist.items()))}")
print(f"\n机制 supp(q⊕x_i) ∩ T_i = ∅:  成立 {mech_ok} / 违例 {mech_bad}")
for r in mech_bad_rows:
    print("   违例:", r)
