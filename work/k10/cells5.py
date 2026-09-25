#!/usr/bin/env python3
"""紧型 5 格定向检验：(d(q,x_i), |T_i∩S|) 的出现计数（只看簇锚点）。
   理论关注格: (2,1),(2,2),(3,1),(3,2),(3,3)。|T_i∩S|=0 自动 A=∅。
"""
import random, sys, itertools
from collections import Counter
sys.argv = ['x', '5', 'none']
exec(open('/home/node/.openclaw/workspace/dn-project/work/k10/exact_pack.py').read().split('def main()')[0])
d = lambda a, b: (a ^ b).bit_count()

random.seed(777001)
cells = Counter()
dd_hist = Counter()
inst = 0
for _ in range(700):
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
            inst += 1
            for ci in other:
                xi = Xw[ci]
                Ci = Cs[ci]
                T_i = {a for a in range(10) if (xi ^ (1 << a)) in Ci}
                for j, q in enumerate(Q):
                    if other[j] == ci:
                        continue
                    S = {a for a in range(10) if ((q ^ xi) >> a) & 1}
                    Dq = len(S)
                    inter = len(T_i & S)
                    dd_hist[Dq] += 1
                    cells[(Dq, inter)] += 1
print(f"紧型实例 = {inst}")
print(f"簇锚点 (q,x_i) 距离 D_q 谱 = {dict(sorted(dd_hist.items()))}")
print(f"\n5 格及全体 (D_q, |T_i∩S|) 计数:")
for key in sorted(cells):
    tag = "  ★关注" if key in ((2, 1), (2, 2), (3, 1), (3, 2), (3, 3)) else ""
    print(f"   (d={key[0]}, |T_i∩S|={key[1]}): {cells[key]}{tag}")
print(f"\n关注 5 格总计数 = {sum(cells[k] for k in ((2,1),(2,2),(3,1),(3,2),(3,3)))}")
print(f"D_q<=3 的全部计数 = {sum(v for k, v in cells.items() if k[0] <= 3)}")
