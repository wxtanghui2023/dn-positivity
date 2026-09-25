#!/usr/bin/env python3
"""Level B 紧型局部禁形分析：|F| = 2 时，两个自由点的 U_D 归属与"缺失见证 y"结构。"""
import random, sys, itertools
from collections import Counter
sys.argv = ['x', '5', 'none']
exec(open('/home/node/.openclaw/workspace/dn-project/work/k10/exact_pack.py').read().split('def main()')[0])


def Sset(q):
    """code 邻域（下标集合）"""
    return frozenset(i for i, w in enumerate(WORDS) if (w ^ q).bit_count() <= 1)


random.seed(31337)
tight_cnt = 0
inU_cnt = Counter()          # |F ∩ U_D| 分布（|F|=2 时）
miss_struct = Counter()      # 缺失见证的结构签名
samples = []
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
        B1x = [x] + [x ^ (1 << j) for j in range(10)]
        others = [Cs[i] for i in range(4) if i != t]
        for (q1, q2, q3) in itertools.product(*others):
            if min((q1 ^ q2).bit_count(), (q1 ^ q3).bit_count(), (q2 ^ q3).bit_count()) < 3:
                continue
            r = tuple(sorted((q1 ^ x).bit_count() and 0 or 0 for _ in ()) )  # placeholder
            rs = tuple(sorted(((q ^ x).bit_count()) for q in (q1, q2, q3)))
            if rs != (2, 3, 3) and rs != (3, 3, 3):
                continue
            F = [v for v in B1x if all((v ^ q).bit_count() >= 3 for q in (q1, q2, q3))]
            if len(F) != 2:
                continue
            tight_cnt += 1
            inU = [v in pts for v in F]
            inU_cnt[sum(inU)] += 1
            if sum(inU) < 2:
                # 记录"不属于 U_D"的自由点所产生的缺失见证
                sig = []
                for v, ok in zip(F, inU):
                    if ok:
                        sig.append("IN")
                    else:
                        Sv = Sset(v)
                        bad = sorted(Sv - set(D))
                        sig.append(f"OUT|S|={len(Sv)}|bad={len(bad)}|d(v,x)={(v^x).bit_count()}")
                miss_struct[(tuple(sig), rs, (F[0] ^ F[1]).bit_count())] += 1
                if len(samples) < 6:
                    samples.append((list(D), t, x, (q1, q2, q3), rs, F, inU,
                                    [sorted(Sset(v) - set(D)) for v in F]))
print(f"紧型 (2,3,3)/(3,3,3) 且 |F|=2 的实例数 = {tight_cnt}")
print(f"其中 |F ∩ U_D| 分布 = {dict(sorted(inU_cnt.items()))}   （≥1 才可能有第四点）")
print(f"\n|F∩U_D|<2 时的缺失见证签名（top8）:")
for k, c in miss_struct.most_common(8):
    print(f"   {k}: {c}")
print(f"\n样例 (D, target, x, (q1,q2,q3), rs, F, inU, bad_sets):")
for s in samples[:4]:
    print("   ", s)
