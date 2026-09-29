#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""M=106 压力测试 v2：对每条不等式求 slack 的**最小值**（聚合可行集上）

约定：不等式写作 L ≥ R；slack := L − R；min slack ≤ 0 ⟹ 该不等式在 M=106 处可能被违反。
变量：n_1..n_11(11) , A_1..A_10(10) , P , E   => 23
"""
import math, numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds

N = 10; M = 106; Q = 1 << N; NV = 23
IN = lambda i: i - 1
IA = lambda k: 11 + k - 1
IP, IE = 21, 22
TOT = M * (M - 1) // 2


def Kraw(j, k, n=N):
    return sum((-1) ** i * math.comb(k, i) * math.comb(n - k, j - i)
               for i in range(0, min(k, j) + 1) if j - i <= n - k)


def base():
    rows, lb, ub = [], [], []
    r = [0.0] * NV
    for i in range(1, 12): r[IN(i)] = 1
    rows.append(r); lb.append(Q); ub.append(Q)
    r = [0.0] * NV
    for i in range(1, 12): r[IN(i)] = i - 1
    rows.append(r); lb.append(11 * M - Q); ub.append(11 * M - Q)
    r = [0.0] * NV
    for i in range(1, 12): r[IN(i)] = i * (i - 1) // 2
    r[IA(1)] = -2; r[IA(2)] = -2
    rows.append(r); lb.append(0); ub.append(0)
    r = [0.0] * NV
    for i in range(1, 12): r[IN(i)] = i * (i - 1) * (i - 2) // 6
    r[IP] = -1; r[IE] = -1
    rows.append(r); lb.append(0); ub.append(0)
    r = [0.0] * NV
    for k in range(1, N + 1): r[IA(k)] = 1
    rows.append(r); lb.append(TOT); ub.append(TOT)
    return np.array(rows), np.array(lb), np.array(ub)


BASE = base()


def slack(terms, const, tag, maximize=False):
    c = np.array(terms, dtype=float) * (-1.0 if maximize else 1.0)
    res = milp(c=c, constraints=LinearConstraint(*BASE), integrality=np.ones(NV),
               bounds=Bounds(0, np.inf))
    if not res.success:
        print(f"  {tag:<44} 失败: {res.message}"); return None
    v = (-1.0 if maximize else 1.0) * float(res.fun)
    x = [round(t) for t in res.x]
    print(f"  {tag:<44} min slack = {v:>10.2f}   [A1={x[IA(1)]},A2={x[IA(2)]},A3={x[IA(3)]},"
          f"A4={x[IA(4)]},P={x[IP]},E={x[IE]}]")
    return v


def main():
    print("=== M=106 压力测试（每条不等式之 min slack；≤0 ⟹ 该式可能被违反）===\n")
    print("[组 1] 离散/非线性不等式")
    r = [0.0] * NV; r[IA(1)] = 1; r[IA(2)] = 1
    slack(r, -71, "I-01  F7: A1+A2 ≥ 71")
    r = [0.0] * NV; r[IA(2)] = 2; r[IP] = -1
    slack(r, 0, "I-02  F5: 2A2 − P ≥ 0")
    r = [0.0] * NV; r[IA(1)] = -1; r[IA(2)] = -1
    slack(r, 161, "I-03  INV2: 161 − (A1+A2) ≥ 0")
    print("\n[组 2] 层覆盖族 k=2..10")
    for k in range(2, N + 1):
        r = [0.0] * NV
        if k - 1 >= 1: r[IA(k - 1)] = 2 * (N + 1 - k)
        r[IA(k)] += 2
        if k + 1 <= N: r[IA(k + 1)] = 2 * (k + 1)
        slack(r, -M * math.comb(N, k), f"I-04  layer-cover k={k}")
    print("\n[组 3] 匹配界 / Krawtchouk 正性")
    r = [0.0] * NV; r[IA(1)] = -1
    slack(r, 59, "I-05  匹配界: 59 − A1 ≥ 0（基线）")
    r = [0.0] * NV; r[IA(1)] = -1
    slack(r, 49, "I-05b Delsarte×Q=1: 49 − A1 ≥ 0")
    for j in (1, 2, 3, 4):
        r = [0.0] * NV
        for k in range(1, N + 1): r[IA(k)] = Kraw(j, k)
        slack(r, M * math.comb(N, j), f"I-06  Krawtchouk j={j}")
    print("\n[组 4] M-型界（M 固定 106，故 slack = 106 − 界值）")
    for name, val in (("球界", 93.09), ("van Wee", 102.4), ("SDP-3", 105.2223)):
        print(f"  {name:<20} 界值 = {val:>8.4f}  ⟹ slack = {106 - val:>7.4f}")
    print("\n[组 5] 恒等式（**直接 KILL**）")
    for nm in ("E + Σδ² = 4(A1+A2)", "F9: 2A2 = Σ_{x∉C}C(μ,2) + P", "S2: ΣC(μ,2) = 2(A1+A2)",
               "恒等式 T: P + E = ΣC(μ,3)", "δ_N[v] = 11·1[v∈C] + 2a1+2a2 − 11"):
        print(f"  {nm:<44} 是恒等式 ⟹ KILL（不产生严格性）")


if __name__ == "__main__":
    main()
