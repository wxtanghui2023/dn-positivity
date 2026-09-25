#!/usr/bin/env python3
"""joint-deletion 模式：紧型下，B_1(x_i) 中每个点 e 的 S(e)\\D 状态与"是否合法候选"的关系。
   —— 这是分离性 A_j∪A_k=∅ 的 joint-deletion 等价刻画。
"""
import random, sys, itertools
from collections import Counter
sys.argv = ['x', '5', 'none']
exec(open('/home/node/.openclaw/workspace/dn-project/work/k10/exact_pack.py').read().split('def main()')[0])
d = lambda a, b: (a ^ b).bit_count()


def S_idx(e):
    return frozenset(i for i, w in enumerate(WORDS) if d(w, e) <= 1)


random.seed(31337)
pat = Counter()          # (是否合法, |S(e)\\D|, |S(e)|) 
n = 0
esc_examples = []
for _ in range(200):
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
            for ci in other:
                xi = Xw[ci]
                Ci = set(Cs[ci])
                for a in range(10):
                    e = xi ^ (1 << a)
                    Se = S_idx(e)
                    bad = Se - set(D)
                    legal = e in Ci
                    pat[(legal, len(bad), len(Se))] += 1
                    n += 1
                    if legal and bad and len(esc_examples) < 4:
                        esc_examples.append((list(D), ci, e, sorted(bad)))
print(f"检查点数 = {n}（每个紧型簇的 B₁(x_i) 的 10 个邻点）")
print("(合法候选?, |S(e)\\\\D|, |S(e)|) 分布:")
for k in sorted(pat, key=lambda k: (-pat[k],)):
    if pat[k] > 0:
        print(f"   legal={k[0]}, |S(e)\\\\D|={k[1]}, |S(e)|={k[2]}: {pat[k]}")
legal_ok = sum(v for k, v in pat.items() if k[0] and k[1] == 0)
legal_bad = sum(v for k, v in pat.items() if k[0] and k[1] > 0)
print(f"\n★ 合法候选 (e∈C_i) 中: |S(e)\\\\D|=0 的 {legal_ok} 个;  >0 的 {legal_bad} 个  （应为 0 ✓）")
print("样例（若 legal 且 bad 非空，则会破坏 C_i 定义）:")
for e in esc_examples:
    print("   ", e)
