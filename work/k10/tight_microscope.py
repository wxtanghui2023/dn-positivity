#!/usr/bin/env python3
"""抽取"自由候选数=1"的紧例，展开 q* 的完整局部 support 结构。"""
import random, sys
sys.argv = ['x', '5', 'none']
exec(open('/home/node/.openclaw/workspace/dn-project/work/k10/exact_pack.py').read().split('def main()')[0])
CODE = set(WORDS)
idx_of = {w: i for i, w in enumerate(WORDS)}


def S(q):
    """code-word 邻域：距 q 不超过 1 的码字下标集合。"""
    return {i for i, w in enumerate(WORDS) if (w ^ q).bit_count() <= 1}


def greedy_pack(pts, target):
    rem = pts
    got = []
    while len(got) < target and rem:
        v = (rem & -rem).bit_length() - 1
        got.append(v)
        t = rem
        nxt = 0
        while t:
            u = (t & -t).bit_length() - 1
            t &= t - 1
            if (u ^ v).bit_count() >= 3:
                nxt |= 1 << u
        rem = nxt
    return got


random.seed(2024)
found = []
for _ in range(300):
    D = tuple(sorted(random.sample(range(120), 4)))
    Xw = [WORDS[i] for i in D]
    U = U_of(D)
    if U == 0:
        continue
    pts = [v for v in range(1024) if (U >> v) & 1]
    P = greedy_pack(U, 3)
    if len(P) < 3:
        continue
    anchored = set()
    for p in P:
        for i, x in enumerate(Xw):
            if (p ^ x).bit_count() <= 1:
                anchored.add(i)
    uncov = [i for i in range(4) if i not in anchored]
    for i in uncov:
        x = Xw[i]
        Cx = [q for q in pts if (q ^ x).bit_count() <= 1]
        Fx = [q for q in Cx if any((q ^ p).bit_count() <= 2 for p in P)]
        free = [q for q in Cx if q not in Fx]
        if len(free) == 1:
            found.append((D, Xw, pts, P, i, x, Cx, Fx, free[0]))

print(f"== 自由候选=1 的紧例：共 {len(found)} 例 ==\n")
for n, (D, Xw, pts, P, i, x, Cx, Fx, q) in enumerate(found, 1):
    print(f"########## 紧例 {n} ##########")
    print(f"D (索引) = {D}")
    print(f"对应码字  = {Xw}")
    print(f"|U_D| = {len(pts)}   packing P = {P}   (k=3)")
    print(f"未覆盖 anchor: 位置 {i}, x = {x}  (码字下标 {D[i]})")
    print(f"|C_x| = {len(Cx)}  |F_x| = {len(Fx)}  自由候选 = {[q]}")
    print(f"\n-- 固定 x=0 前的原始坐标关系 --")
    print(f"  d(q*, x) = {(q ^ x).bit_count()}")
    print(f"  q* 到各 p 的距离 = {[(q ^ p).bit_count() for p in P]}   （须 ≥3）")
    print(f"  x 到各 p 的距离 = {[(x ^ p).bit_count() for p in P]}")
    print(f"  C_x 全部候选 = {Cx}")
    print(f"  F_x（被吃掉的）= {Fx}")
    print(f"\n-- q* 的 code 邻域 S(q*) --")
    Sq = S(q)
    print(f"  S(q*) = {sorted(Sq)}  （码字 {[WORDS[j] for j in sorted(Sq)]}）")
    print(f"  S(q*) ∩ D = {sorted(Sq & set(D))}")
    Nbad = sorted(Sq - set(D))
    print(f"  S(q*) \\ D = {Nbad}   （危险邻居：码字 {[WORDS[j] for j in Nbad]}）")
    print(f"\n-- 对每个 y ∈ S(q*) 的 A(y) 与距离型 --")
    for j in sorted(Sq):
        y = WORDS[j]
        Ay = [t for t, xx in enumerate(Xw) if (xx ^ y).bit_count() <= 1]
        print(f"  y={y} (下标 {j}){'  [在D中]' if j in D else '  [不在D]'}: "
              f"d(y,x)={(y ^ x).bit_count()}  A(y)={Ay}  "
              f"d(y,p)={[(y ^ p).bit_count() for p in P]}")
    print(f"\n-- 该例的 U_D 是否含 x 的其它邻点（|B_1(x)∩U_D| 与 C_x 关系）--")
    print(f"  B_1(x)∩U_D 大小 = {len(Cx)}（即 C_x）;  B_1(x) 共 11 点")
    print(f"  U_D 中与 x 距离 ≥2 的点数 = {sum(1 for v in pts if (v ^ x).bit_count() >= 2)}")
    print()
