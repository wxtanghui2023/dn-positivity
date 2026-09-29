#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""A 线：距离层覆盖不等式族（LAYER-COVER）

推导：码字 c 与距离 k≥2 —— Y_k(c) = {y : d(y,c)=k}，|Y_k| = C(n,k)，每点须被某码字覆盖。
若 d(c,c')=j，则 c' 覆盖的 Y_k 点数 ψ(k,j) = (n+1-k) if j=k-1; 1 if j=k; (k+1) if j=k+1; 0 else。
⟹ C(n,k) ≤ (n+1-k)·d_{k-1}(c) + d_k(c) + (k+1)·d_{k+1}(c)
对 c 求和（Σ_c d_j(c) = 2A_j）：
   M·C(n,k) ≤ 2(n+1-k)A_{k-1} + 2A_k + 2(k+1)A_{k+1}       (k=2..n-1)

用法：① 在两已知码上验证（若违反 ⟹ ψ 推错）② 对 M=106 求 min ΣA_k 与 C(M,2) 比较
"""
import itertools, sys, os

HERE = os.path.dirname(os.path.abspath(__file__))


def dists(N, C):
    Q = 1 << N
    A = [0] * (N + 1)
    for u, v in itertools.combinations(C, 2):
        A[bin(u ^ v).count("1")] += 1
    return A


def wts(N):
    """ψ 表：列表 (psi_{k,k-1}, psi_{k,k}, psi_{k,k+1}) 对 k=2..N-1"""
    return {k: (N + 1 - k, 1, k + 1) for k in range(2, N)}


def check(N, C, tag):
    A = dists(N, C)
    M = len(C)
    print(f"--- {tag}: n={N} M={M}  ΣA_k={sum(A[1:])} (应=C(M,2)={M*(M-1)//2})")
    print(f"    A_1..A_N = {A[1:]}")
    ok = True
    for k in range(2, N):
        lhs = M * (len(list(itertools.combinations(range(N), k))))  # C(N,k)
        rhs = (N + 1 - k) * 2 * A[k - 1] + 2 * A[k] + (k + 1) * 2 * A[k + 1]
        good = lhs <= rhs
        ok &= good
        print(f"    k={k}: LHS={lhs} ≤ RHS={rhs}  {'✓' if good else '✗✗ ψ 推错'}")
    print(f"    ⟹ 层覆盖不等式族 {'全部成立 ✓✓' if ok else '**有违反 ✗**'}")
    return A


def milp_min_sumA(N, M, a1_max=None):
    """min Σ A_k  s.t. 层覆盖不等式 (+ A_1 ≤ a1_max)"""
    import numpy as np, math
    from scipy.optimize import milp, LinearConstraint, Bounds
    K = N
    rows, lb = [], []
    for k in range(2, N):
        row = [0.0] * K
        row[k - 2] += 2 * (N + 1 - k)
        row[k - 1] += 2
        if k + 1 <= N:
            row[k] += 2 * (k + 1)
        rows.append(row)
        lb.append(M * math.comb(N, k))
    r = [0.0] * K
    r[0] += 1.0
    r[1] += 1.0
    rows.append(r)
    lb.append((11 * M - 2 ** N) / 2.0)
    ub = np.full(K, np.inf)
    if a1_max is not None:
        ub[0] = a1_max
    res = milp(c=np.ones(K), constraints=LinearConstraint(np.array(rows), lb=lb, ub=np.inf),
               integrality=np.ones(K), bounds=Bounds(0, ub))
    return res


def main():
    print("=" * 74)
    print("A 线：距离层覆盖不等式族 —— 验证 + 对 M=106 求下界")
    print("=" * 74)
    C9 = [sum(int(b) << i for i, b in enumerate(l.split()))
          for l in open(os.path.join(HERE, "..", "sources",
                                     "KERI-CD-K_9_1-the-optimal-9-62-binary-covering-code.txt"))
          if len(l.split()) == 9]
    check(9, C9, "62-码")
    C10 = [int(l.strip(), 2) for l in open(os.path.join(HERE, "..", "sources",
                                                        "K10-1-120-cover-CERTIFICATE.txt"))
           if l.strip() and not l.startswith("#")]
    A120 = check(10, C10, "120-码")

    print("\n[对 M=106 求解：min ΣA_k（在层覆盖不等式下）]")
    res = milp_min_sumA(10, 106)
    if res.success:
        A = [round(v) for v in res.x]
        print(f"    min ΣA_k = {sum(A)}   A_1..A_10 = {A}")
        print(f"    而 ΣA_k 必须 = C(106,2) = {106*105//2}")
        print(f"    ⟹ {'**矛盾：min > C(106,2) ⟹ 排除 M=106 ⟹ K ≥ 107** ✓✓✓' if sum(A) > 106*105//2 else '无矛盾（min ≤ C(M,2)）✗ —— 层覆盖族单独不足'}")
    else:
        print("   MILP 失败:", res.message)

    print("\n[对照：若把 A_1 ≤ 49（档案界）也加入]")
    res2 = milp_min_sumA(10, 106, a1_max=49)
    if res2.success:
        A = [round(v) for v in res2.x]
        print(f"    min ΣA_k = {sum(A)}   A = {A}")
        print(f"    ⟹ {'**矛盾 ⟹ 排除 M=106** ✓✓✓' if sum(A) > 106*105//2 else '无矛盾 ✗'}")
    else:
        print("    MILP 失败:", res2.message)


if __name__ == "__main__":
    main()
