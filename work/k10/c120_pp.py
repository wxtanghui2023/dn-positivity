#!/usr/bin/env python3
"""C120-PP 检验（修正版）：∀ x,y ∈ C_120, d(x,y)=4, ∀ r∈I, ∀ s∈I, s≠r:
      NOT ( S(x⊕e_r) = {x}  AND  S(y⊕e_s) = {y} )
   其中 I = supp(x⊕y)。同时给出 d_min(C_120) 与距离 4 码字对数量。
"""
import sys, itertools
from collections import Counter
sys.argv = ['x', '5', 'none']
exec(open('/home/node/.openclaw/workspace/dn-project/work/k10/exact_pack.py').read().split('def main()')[0])
d = lambda a, b: (a ^ b).bit_count()

owners = {}
for i, w in enumerate(WORDS):
    for v in [w] + [w ^ (1 << j) for j in range(10)]:
        owners.setdefault(v, set()).add(i)

# 1) d_min
dmin = min(d(WORDS[i], WORDS[j]) for i, j in itertools.combinations(range(120), 2))
dist_hist = Counter()
for i, j in itertools.combinations(range(120), 2):
    dist_hist[d(WORDS[i], WORDS[j])] += 1
print(f"C_{'{120}'} 最小距离 = {dmin};  距离分布 = {dict(sorted(dist_hist.items()))}")

# 2) C120-PP
pairs4 = 0
cand = 0
viol = 0
ex = []
for i, j in itertools.combinations(range(120), 2):
    x, y = WORDS[i], WORDS[j]
    if d(x, y) != 4:
        continue
    pairs4 += 1
    I = [r for r in range(10) if ((x ^ y) >> r) & 1]
    for r in I:
        p = x ^ (1 << r)
        ppriv = (owners.get(p, set()) == {i})
        for s in I:
            if s == r:
                continue
            q = y ^ (1 << s)
            cand += 1
            qpriv = (owners.get(q, set()) == {j})
            if ppriv and qpriv:
                viol += 1
                if len(ex) < 8:
                    ex.append((i, j, x, y, r, s, p, q))
print(f"距离 4 的码字对 = {pairs4};  候选 (r,s) 检验数 = {cand}")
print(f"★ 违反 C120-PP 的次数 = {viol}   （0 即禁形成立、分离性可闭合）")
for e in ex:
    print("   违例:", e)
