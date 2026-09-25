#!/usr/bin/env python3
"""紧型(2,3,3)/(3,3,3) Level B 有限禁形分类（干净版）。
★ 索引纪律：owners 存下标；D 是下标元组；Xw 是码字；Cs 是"候选点"（码字空间）。
"""
import random, sys, itertools
from collections import Counter
sys.argv = ['x', '5', 'none']
exec(open('/home/node/.openclaw/workspace/dn-project/work/k10/exact_pack.py').read().split('def main()')[0])


def S_idx_of(q):
    """距码字 q 不超过 1 的码字下标集合"""
    return [i for i, w in enumerate(WORDS) if (w ^ q).bit_count() <= 1]


random.seed(31337)
f_shape = Counter()
y_shape = Counter()
dyq = Counter()
exch = Counter()
table = []
n_bad = 0
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
        others = [Cs[i] for i in other_idx]
        for Q in itertools.product(*others):
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
                ys = [WORDS[i] for i in S_idx_of(f) if i not in D]
                if not ys:
                    continue
                n_bad += 1
                y = ys[0]
                fn, yn = f ^ x, y ^ x
                f_shape["x(0)" if fn == 0 else f"e{fn.bit_length()-1}"] += 1
                y_shape[(yn.bit_count(), tuple(i for i in range(10) if (yn >> i) & 1))] += 1
                dq = tuple(sorted((y ^ q).bit_count() for q in Q))
                dyq[dq] += 1
                # 交换对检验：替换簇 other_idx[k] 上的 Q[k]，保持与其余两点兼容且与 f 远
                sw = []
                for k, ci in enumerate(other_idx):
                    keep = [Q[j] for j in range(3) if j != k]
                    found = any((qp ^ f).bit_count() >= 3 and
                                all((qp ^ qq).bit_count() >= 3 for qq in keep)
                                for qp in Cs[ci])
                    sw.append(found)
                exch[tuple(sw)] += 1
                if len(table) < 8:
                    table.append({"D": list(D), "t": t, "rs": rs,
                                  "F_norm": [f ^ x for f in F], "f_norm": fn, "y_norm": yn,
                                  "d_y_q": dq, "swappable": sw})
print(f"紧型坏自由点实例数 = {n_bad}")
print(f"坏 f 归一化形态 = {dict(f_shape)}")
print(f"坏 y 形态 (|y|,support) top6 = {y_shape.most_common(6)}")
print(f"d(y,q_i) 三元组分布 = {dict(sorted(dyq.items()))}")
print(f"各簇交换对存在性 (k=0,1,2 对应 Q 的三个来源簇) = {dict(exch)}")
print(f"⟹ 至少存在一个可交换簇的比例 = "
      f"{sum(c for k, c in exch.items() if any(k))/max(1, sum(exch.values())):.3f}")
print("\n样例:")
for r in table:
    print("   ", r)
