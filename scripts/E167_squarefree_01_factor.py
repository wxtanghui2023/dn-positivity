#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
E167：(甲) 的定向判定 —— 平方自由 GF 的“0/1 系数分解”是否存在？
纪律：不碰 RH；不引入 ζ/Ξ；纯整数；内存安全（NMAX 小）。

问题：M(x) = Σ_{n≥1} μ²(n) x^n  （平方自由指示）
     是否存在 0/1 系数幂级数 A, B，使 A(x)B(x) = M(x)，且 A,B ∉ {1, M}？

做法：逐 n 递推 + 分支 + 剪枝（每层至多 4 种赋值），检查到 NMAX。
若找到 ⟹ 0/1 分解存在（但【仍需】判定是否属于 blind 语法）；
若穷尽失败 ⟹ 在 NMAX 内不存在。
"""
import sys

NMAX = 46

# 平方自由指示（用整数分解自算，避免依赖）
def is_sf(n):
    d = 2
    while d * d <= n:
        if n % (d * d) == 0:
            return 0
        d += 1
    return 1

M = [0] + [is_sf(n) for n in range(1, NMAX + 1)]


def search(limit=NMAX):
    """DFS：逐层同时确定 a_n, b_n（b_0=0 固定为 A,M 之一的最小支路时另处理）"""
    A = [None] * (limit + 1)
    B = [None] * (limit + 1)
    sols = []

    def ok(n):
        """检查 x^n 系数（所有已定项）"""
        s = 0
        for i in range(0, n + 1):
            ai, bj = A[i], B[n - i]
            if ai is None or bj is None:
                continue
            s += ai * bj
            if s > M[n]:
                return False
        return s == M[n]

    def consistent(n):
        for k in range(0, n + 1):
            s = 0
            for i in range(0, k + 1):
                if A[i] is None or B[k - i] is None:
                    return False
                s += A[i] * B[k - i]
            if s != M[k]:
                return False
        return True

    # 仅取 b_0 = 0（另支路 b_0=1 等价于 A=M 平凡，见文档说明）
    def dfs(n):
        if len(sols) >= 3:
            return
        if n > limit:
            sols.append((A[:], B[:]))
            return
        # 用 [x^n] 约束：a_0*b_n + b_0*a_n + Σ_{0<i<n} a_i b_{n-i} = M[n]
        inner = 0
        for i in range(1, n):
            if A[i] is None or B[n - i] is None:
                return
            inner += A[i] * B[n - i]
        # a_0, b_0 已定；分四种情形
        for bn in (0, 1):
            for an in (0, 1):
                if A[0] * bn + B[0] * an + inner != M[n]:
                    continue
                A[n], B[n] = an, bn
                if consistent(n):
                    dfs(n + 1)
                A[n] = B[n] = None

    A[0], B[0] = 1, 0
    dfs(1)
    return sols


def main():
    print("NMAX =", NMAX)
    print("M[0..20] =", M[:21])
    print()
    sols = search()
    print("找到 0/1 分解数（≤3）：", len(sols))
    for A, B in sols:
        print("  A[0..20] =", A[:21])
        print("  B[0..20] =", B[:21])
        print("  A支撑点数 =", sum(1 for x in A if x), " B支撑点数 =", sum(1 for x in B if x))
    if not sols:
        print("  ⟹ 在 N≤%d 内【不存在】满足 a_0=1,b_0=0 的 0/1 分解" % NMAX)


if __name__ == "__main__":
    main()
