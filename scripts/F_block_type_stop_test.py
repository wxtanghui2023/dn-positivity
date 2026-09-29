#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""F 首个实验 + STOP#1 判定（唐先生 23:08 程序：F-G-H-B）

F：pair-block 映射 π: Q_2^10 → {0,1,2}^5
   5 个 block，每 block 状态 0=00, 2=11, 1∈{01,10}
   不变量：block 类型向量 τ(x) = (n_0,n_1,n_2)（n_0+n_1+n_2 = 5，共 C(7,2)=21 型）

STOP#1（唐先生）：若所有 mixed 关系最终都写回旧量（M, A_1..A_3, ΣC(μ,k), #priv）的函数 ⟹ **STOP**

做法（仓库既有方法学：残差检验）：
  ① 采 40+ 个覆盖码（120-码 ＋ 保覆盖扰动 ＋ 贪心）
  ② 旧特征（6）：M, A_1, A_2, A_3, ΣC(μ,3), #priv
  ③ 新特征（5）：T_k := Σ_{x: π(x) 之不等 block 数 = k} μ(x), k=0..4（k=5 由总和决定）
  ④ 线性回归 新~旧（样本数 > 参数量，照"欠定假象"纪律）⟹ 看残差
"""
import itertools, random, os, sys
import numpy as np

N = 10
Q = 1 << N
MASK = [1 << i for i in range(N)]
NB = [[v] + [v ^ m for m in MASK] for v in range(Q)]
HERE = os.path.dirname(os.path.abspath(__file__))
CERT = os.path.join(HERE, "..", "sources", "K10-1-120-cover-CERTIFICATE.txt")

# ── F：pair-block 类型 ──
BLOCKS = [(2 * i, 2 * i + 1) for i in range(5)]     # 5 个 block

def uneq(x):
    """不等 block 数 = {i : x 之第 i 对两坐标不相等} 的个数"""
    c = 0
    for a, b in BLOCKS:
        if ((x >> a) & 1) != ((x >> b) & 1):
            c += 1
    return c

PI = [uneq(x) for x in range(Q)]


def load120():
    return [int(l.strip(), 2) for l in open(CERT) if l.strip() and not l.startswith("#")]


def cover_ok(C):
    cnt = [0] * Q
    for c in C:
        for x in NB[c]:
            cnt[x] += 1
    return all(k >= 1 for k in cnt), cnt


def feats(C):
    ok, cnt = cover_ok(C)
    M = len(C)
    S = set(C)
    A = [0] * (N + 1)
    for u, v in itertools.combinations(C, 2):
        A[bin(u ^ v).count("1")] += 1
    c3 = sum(c * (c - 1) * (c - 2) // 6 for c in cnt)
    npriv = cnt.count(1)
    T = [0] * 5
    for x in range(Q):
        k = PI[x]
        if k < 5:
            T[k] += cnt[x]
    return ok, [M, A[1], A[2], A[3], c3, npriv], T


def perturb(rng, C, nsw):
    """真扰动：随机加 3 词 + 贪心删冗余（保覆盖），可产生大小/结构都变的新码"""
    C = set(C)
    for _ in range(nsw):
        C |= {rng.randrange(Q) for _ in range(3)}
        words = sorted(C, key=lambda _: rng.random())
        for w in words:
            C2 = C - {w}
            if cover_ok(sorted(C2))[0]:
                C = C2
    return sorted(C)


def greedy(rng, Mtarget=None):
    C = []
    cov = [0] * Q
    left = set(range(Q))
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
    rng = random.Random(20260929)
    base = load120()
    sample = []
    sample.append(("120-码", base))
    for i in range(24):
        sample.append((f"扰动{i}", perturb(rng, base, 2 + i % 6)))
    for i in range(20):
        sample.append((f"贪心{i}", greedy(rng)))
    rows_old, rows_new, names = [], [], []
    print("=== F 实验样本（须全部为真覆盖码）===")
    for name, C in sample:
        ok, old, T = feats(C)
        if not ok:
            print(f"  [skip] {name} 非覆盖码")
            continue
        rows_old.append(old)
        rows_new.append(T)
        names.append(name)
        print(f"  {name:<8} M={old[0]:<4} A1={old[1]:<4} A2={old[2]:<5} A3={old[3]:<5} "
              f"ΣC(μ,3)={old[4]:<6} #priv={old[5]:<5}  T={T}")
    X = np.array(rows_old, float)
    Y = np.array(rows_new, float)
    n = X.shape[0]
    print(f"\n样本数={n}（旧特征 {X.shape[1]} 维 ＋ 截距 ⟹ 参数 {X.shape[1]+1} 个；须 n > 参数 ✓）")
    print("\n=== STOP#1 判定：新特征 T_k 能否由旧特征线性解释 ===")
    print(f"{'新特征':<8}{'R²':>10}{'最大相对残差':>16}  判定")
    stop = True
    for j in range(Y.shape[1]):
        A = np.hstack([X, np.ones((n, 1))])
        coef, *_ = np.linalg.lstsq(A, Y[:, j], rcond=None)
        pred = A @ coef
        resid = Y[:, j] - pred
        ss_res = float((resid ** 2).sum())
        ss_tot = float(((Y[:, j] - Y[:, j].mean()) ** 2).sum())
        r2 = 1 - ss_res / ss_tot if ss_tot > 0 else float("nan")
        scale = max(1e-9, float(np.abs(Y[:, j]).mean()))
        mr = float(np.abs(resid).max()) / scale
        verdict = "可解释（旧量足够）" if (r2 > 0.99 and mr < 0.02) else "**新信息候选**"
        if not (r2 > 0.99 and mr < 0.02):
            stop = False
        print(f"T_{j:<6}{r2:>10.4f}{mr:>16.4f}  {verdict}")
    print("\n" + "=" * 66)
    if stop:
        print("⟹ **STOP#1 触发**：F/G 的 block-类型坐标**未产生**超出旧量的信息 ⟹ 按唐先生规则砍掉 ✗")
    else:
        print("⟹ **STOP#1 未触发**：存在 T_k 残差 ⟹ F/G 有继续价值 ✓（下一步接 H：传播）")


if __name__ == "__main__":
    main()
