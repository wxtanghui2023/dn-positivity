#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""H1（唐先生改造版）：owner-conditioned 类型×覆盖 联合分布 + 零格检测 + 资源测试

几何侧（已由 F1 证：E_x=∅，几何干净 ⟹ 单独的 τ / Γ 不含新信息）：
  π: Q_2^10 → {0,1,2}^5 ，τ(x)=(n_0,n_1,n_2) 共 21 型
  对码字 c 与其邻点 x=c⊕e_i：设 i 属于 block b，c 在该 block 之状态 s∈{0,1,2}
     翻 i 后状态 → 转移类 cls ∈ {(0,1),(2,1),(1,0),(1,2)}（几何决定，无例外）

owner 侧（真信息只能来自此处）：
  对每个 (c, x) 对，c∈C, x∈N[c], x≠c：记录三元 (τ(c), cls, μ(x))
  —— 若某组合在全部样本中**零出现**而期望计数不小 ⟹ 候选局部规则（Level 0）

输出：① 联合表零格（含期望计数）② 各候选之 ΔR（该规则强迫的额外资源＝"必须另找覆盖"的点数下界）③ 判定
"""
import itertools, random, os, numpy as np

N = 10
Q = 1 << N
MASK = [1 << i for i in range(N)]
NB = [[v] + [v ^ m for m in MASK] for v in range(Q)]
BLOCKS = [(2 * i, 2 * i + 1) for i in range(5)]
BLOF = {}
for bi, (a, b) in enumerate(BLOCKS):
    BLOF[a] = bi
    BLOF[b] = bi
HERE = os.path.dirname(os.path.abspath(__file__))
CERT = os.path.join(HERE, "..", "sources", "K10-1-120-cover-CERTIFICATE.txt")


def tau(x):
    n1 = 0
    for a, b in BLOCKS:
        if ((x >> a) & 1) != ((x >> b) & 1):
            n1 += 1
    n0 = 0
    for a, b in BLOCKS:
        if ((x >> a) & 1) == 0 and ((x >> b) & 1) == 0:
            n0 += 1
    return (n0, n1, 5 - n0 - n1)


TAU = [tau(x) for x in range(Q)]
TYPES = sorted(set(TAU))
TI = {t: i for i, t in enumerate(TYPES)}


def block_state(c, b):
    a1, b1 = BLOCKS[b]
    x, y = (c >> a1) & 1, (c >> b1) & 1
    return x + y if x == y else 1        # 00→0, 11→2, 不等→1


def cls_of(c, i):
    b = BLOF[i]
    s = block_state(c, b)
    a1, b1 = BLOCKS[b]
    y = c ^ (1 << i)
    s2 = block_state(y, b)
    return (s, s2)


def load120():
    return [int(l.strip(), 2) for l in open(CERT) if l.strip() and not l.startswith("#")]


def cover_ok(C):
    cnt = [0] * Q
    for c in C:
        for x in NB[c]:
            cnt[x] += 1
    return all(k >= 1 for k in cnt), cnt


def greedy(rng):
    C, left = [], set(range(Q))
    while left:
        best, bc = None, -1
        for _ in range(300):
            v = rng.randrange(Q)
            c = len(set(NB[v]) & left)
            if c > bc:
                best, bc = v, c
        C.append(best)
        left -= set(NB[best])
    return C


def main():
    rng = random.Random(777)
    samples = [("120-码", load120())] + [(f"贪心{i}", greedy(rng)) for i in range(24)]
    # 联合累积： key=(type_idx, cls) × μ
    joint = np.zeros((len(TYPES), 4, 12))
    CLS = [(0, 1), (2, 1), (1, 0), (1, 2)]
    CLOF = {c: k for k, c in enumerate(CLS)}
    ncode = 0
    tpres = np.zeros(len(TYPES))
    for name, C in samples:
        ok, cnt = cover_ok(C)
        if not ok:
            continue
        ncode += 1
        for t in range(len(TYPES)):
            tpres[t] += sum(1 for x in range(Q) if TI[TAU[x]] == t)
        for c in C:
            tc = TI[TAU[c]]
            for i in range(N):
                x = c ^ (1 << i)
                joint[tc, CLOF[cls_of(c, i)], cnt[x]] += 1
    tot = joint.sum()
    print(f"样本数（真覆盖码）= {ncode}；联合样本点 = {int(tot)}")
    print(f"\n[表2] τ(c) × 转移类 × μ(邻点) 之**零格**（仅列 μ≥2 侧，期望计数≥5）")
    print(f"{'τ(c)':<14}{'cls':<10}{'μ':>3}{'期望':>10}{'实计':>7}")
    zeros = []
    rowsum = joint.sum(axis=(1, 2))
    colsum = joint.sum(axis=(0, 1))
    for t in range(len(TYPES)):
        for k in range(4):
            for m in range(2, 12):
                num = joint[t, k, m]
                exp = (joint[t].sum() / tot) * (joint[:, :, m].sum() / tot) * tot if tot else 0
                if num == 0 and exp >= 5:
                    zeros.append((TYPES[t], CLS[k], m, exp))
    if zeros:
        for t, cl, m, e in sorted(zeros, key=lambda z: -z[3])[:25]:
            print(f"  {str(t):<14}{str(cl):<10}{m:>3}{e:>10.1f}{0:>7}")
    else:
        print("  （无满足期望阈值的零格）")
    print(f"\n[表1] 21 型之总体出现次数（几何决定；仅供核对）")
    print("  " + "  ".join(f"{t}:{int(v)}" for t, v in list(zip(TYPES, tpres / max(ncode, 1)))[:21]))
    # ── 修正版：按 (τ, 情形) 统计 μ 分布（情形=eq→uneq / uneq→eq / c 自身）──
    print("\n[修正表] 按 (τ, 情形) 之 μ 分布。情形: E=00/11→不等(即 cls(0,1)/(2,1)) | U=不等→00/11(cls(1,0)/(1,2)) | self=码字自身")
    print(f"{'τ':<12}{'情形':<6}{'n':>7}  μ取值分布（出现之 μ:次数）")
    gaps=[]
    for t in range(len(TYPES)):
        for case, ks in (("E",[0,1]),("U",[2,3])):
            cnt_by_m={}
            for k in ks:
                for m in range(12):
                    if joint[t,k,m]: cnt_by_m[m]=cnt_by_m.get(m,0)+int(joint[t,k,m])
            n=sum(cnt_by_m.values())
            if n<50: continue
            obs=sorted(cnt_by_m)
            lo,hi=obs[0],obs[-1]
            missing=[m for m in range(lo,hi+1) if m not in cnt_by_m]
            tag=" ⟸ **缺 "+str(missing)+"**" if missing else ""
            if missing: gaps.append((TYPES[t],case,n,missing))
            if missing or n>500:
                print(f"  {str(TYPES[t]):<12}{case:<6}{n:>7}  "+" ".join(f"{m}:{cnt_by_m[m]}" for m in obs)+tag)
    print("\n" + "="*62)
    if gaps:
        print(f"[真候选] 存在 {len(gaps)} 个 (τ,情形) 其 μ 分布有\u003c内部空洞\u003e（非几何必然）⟹ Level-0 候选 ⚠️")
        for g in gaps[:12]: print("   ",g)
        print("   ⟹ 须 Level-1 稳健性（更多样本/定向扰动）＋ Level-2 证明；**ΔR 未定前不得当 H 规则**")
    else:
        print("判定：**无内部空洞** ⟹ 未能找到 owner-conditioned 规则 ⟹ 按硬规则 F/H 暂停 ✗")


if __name__ == "__main__":
    main()
