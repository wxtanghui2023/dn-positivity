#!/usr/bin/env python3
"""D-结构层最后一刀：A_j（= C_i 被其它簇 packing 点覆盖的坐标集）在一般设置下能否非空？
   同时记录 packing 点是否为码字（q ∈ C_120 ?），因为 §36/§37 的反例只覆盖"双方皆码字"。
"""
import random, sys, itertools
from collections import Counter
sys.argv = ['x', '5', 'none']
exec(open('/home/node/.openclaw/workspace/dn-project/work/k10/exact_pack.py').read().split('def main()')[0])
d = lambda a, b: (a ^ b).bit_count()
CODE = set(WORDS)

random.seed(424242)
nonempty = 0
checks = 0
qcodes = Counter()      # packing 点是否码字
ex = []
for _ in range(800):
    D = tuple(sorted(random.sample(range(120), 4)))
    Xw = [WORDS[i] for i in D]
    U = U_of(D)
    if U == 0:
        continue
    pts = [v for v in range(1024) if (U >> v) & 1]
    Cs = [[q for q in pts if d(q, x) <= 1] for x in Xw]
    for t in range(4):
        if any(not c for c in [Cs[i] for i in range(4) if i != t]):
            continue
        other = [i for i in range(4) if i != t]
        # 贪心取一个三点 packing（每簇一点）
        Q = []
        for i in other:
            for q in Cs[i]:
                if all(d(q, p) >= 3 for p in Q):
                    Q.append(q)
                    break
        if len(Q) < 3:
            continue
        for k, ci in enumerate(other):
            xi = Xw[ci]
            Ci = Cs[ci]
            keep = [Q[j] for j in range(3) if j != k]
            for q in Q:
                qcodes[q in CODE] += 1
            Aj = {a for a in range(10)
                  if (xi ^ (1 << a)) in Ci and d(xi ^ (1 << a), keep[0]) <= 2}
            Ak = {a for a in range(10)
                  if (xi ^ (1 << a)) in Ci and d(xi ^ (1 << a), keep[1]) <= 2}
            checks += 1
            if Aj | Ak:
                nonempty += 1
                if len(ex) < 6:
                    ex.append((list(D), t, ci, sorted(Aj), sorted(Ak), keep,
                               [q in CODE for q in keep], d(keep[0], xi), d(keep[1], xi)))
print(f"检查的 (D,target,簇) 数 = {checks}")
print(f"packing 点是否码字: {dict(qcodes)}")
print(f"★ A_j ∪ A_k 非空的次数 = {nonempty}   （0 ⟹ D-结构层强制）")
for e in ex:
    print("   样例:", e)
