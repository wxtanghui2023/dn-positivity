#!/usr/bin/env python3
"""紧型分离性普查：所有 (q∈Q, x_i∈D 且 x_i 非 q 的锚点) 对的距离谱。
   锚点判定：d(q, x_i) <= 1（因 q∈C_j ⟹ S(q)⊆D，可能多锚；此处按"最近且≤1"计）。
"""
import random, sys, itertools
from collections import Counter
sys.argv = ['x', '5', 'none']
exec(open('/home/node/.openclaw/workspace/dn-project/work/k10/exact_pack.py').read().split('def main()')[0])
d = lambda a, b: (a ^ b).bit_count()

random.seed(31337)
spec = Counter()
minsep = Counter()
tight_inst = 0
pairs = 0
worst = []
for _ in range(300):
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
            if len(F) != 2:
                continue
            tight_inst += 1
            for q in Q:
                # q 的锚点 = D 中距 q <=1 的字
                anch = {i for i in range(4) if d(q, Xw[i]) <= 1}
                ds = [d(q, Xw[i]) for i in range(4) if i not in anch]
                for v in ds:
                    spec[v] += 1
                    pairs += 1
                if ds:
                    minsep[min(ds)] += 1
                    if min(ds) <= 3 and len(worst) < 6:
                        worst.append((list(D), t, rs, q, sorted(anch), sorted(ds)))
print(f"紧型实例数 = {tight_inst};  非锚点对数 = {pairs}")
print(f"非锚点距离谱 = {dict(sorted(spec.items()))}")
print(f"每个 q 的 min 非锚点距离分布 = {dict(sorted(minsep.items()))}")
print(f"\n最小距离 <=3 的样例（若有）:")
for w in worst:
    print("   ", w)
