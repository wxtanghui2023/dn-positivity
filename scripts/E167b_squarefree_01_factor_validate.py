#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
E167b：平方自由 GF 的 0/1 分解 —— 有界搜索 + 延伸验证
要点：双线性系统 A·B = M 的有界搜索会产出【不延伸】的伪解，
      故必须对每个解在【更大 N】上验证。

A(x)B(x) = M(x)，M[n] = μ²(n)；约定 b_0 = 0（另一支 b_0=1 迫使 A=M，平凡）。
排除 A ≡ 1 与 B ≡ 1。
"""
NSEARCH = 60     # 搜索范围
NTEST = 260      # 延伸验证范围


def is_sf(n):
    if n == 0:
        return 0
    d = 2
    while d * d <= n:
        if n % (d * d) == 0:
            return 0
        d += 1
    return 1


MT = [0] + [is_sf(n) for n in range(1, NTEST + 1)]


def find_solutions(limit, cap=5):
    A = [None] * (limit + 1)
    B = [None] * (limit + 1)
    sols = []

    def ok_all(n):
        for k in range(0, n + 1):
            s = 0
            for i in range(0, k + 1):
                if A[i] is None or B[k - i] is None:
                    return False
                s += A[i] * B[k - i]
            if s != MT[k]:
                return False
        return True

    def dfs(n):
        if len(sols) >= cap:
            return
        if n > limit:
            sols.append((A[:], B[:]))
            return
        inner = 0
        for i in range(1, n):
            inner += A[i] * B[n - i]
        for bn in (0, 1):
            for an in (0, 1):
                if A[0] * bn + B[0] * an + inner != MT[n]:
                    continue
                A[n], B[n] = an, bn
                if ok_all(n):
                    dfs(n + 1)
                A[n] = B[n] = None

    A[0], B[0] = 1, 0
    dfs(1)
    return sols


def validate(A, B, upto):
    """在 upto 内验证乘积；返回首个失败 n 或 None"""
    for n in range(0, upto + 1):
        s = 0
        for i in range(0, n + 1):
            if i < len(A) and (n - i) < len(B):
                s += A[i] * B[n - i]
        if s != MT[n]:
            return n, s, MT[n]
    return None


def main():
    print("搜索 N ≤ %d ；延伸验证 N ≤ %d" % (NSEARCH, NTEST))
    print("M[0..24] =", MT[:25])
    sols = find_solutions(NSEARCH)
    print("\n搜索到解数（≤5）：", len(sols))
    nontrivial = 0
    for idx, (A, B) in enumerate(sols):
        sa = sorted(i for i, x in enumerate(A) if x)
        sb = sorted(i for i, x in enumerate(B) if x)
        triv = (sa == [0]) or (sb == [0])
        v = validate(A, B, NTEST)
        print("  解#%d A支撑=%s B支撑点数=%d 平凡=%s 延伸验证=%s"
              % (idx, sa[:6], len(sb), triv, ("通过" if v is None else "失败于 n=%d（得%d 期望%d）" % v)))
        if not triv:
            nontrivial += 1
    print("\n非平凡解数：", nontrivial)
    if nontrivial == 0:
        print("⟹ 在 N ≤ %d 内【不存在】非平凡的 0/1 分解（且在 N ≤ %d 上验证）" % (NSEARCH, NTEST))


if __name__ == "__main__":
    main()
