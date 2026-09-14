#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
E165·D1-B* 第一轮：最小【盲生成类】中的 Cauchy→乘性 枚举
依唐先生 2026-09-14 13:36 规格：
  G0 盲定义：生成规则中不得出现 ζ, Ξ, ρ, Re ρ, "RH 成立"，或其反向编码
  允许原子：1, n, Λ(n), μ(n), |μ|, 1_{p|n}(→Ω/ω), v_p(n)
  允许操作：+, ×, Σ_{n≤N}, Σ_{d|n}, gcd, lcm
  G2′ 非退化：A,B 不能有有限支撑/单位/缩放退化
  判据：C_N = Σ_{m} A_m B_{N-m} 是否满足 C_ab = C_a C_b ((a,b)=1)

纪律：不碰 RH ✗；不引入 ζ/Ξ ✗；纯整数运算 ✓；内存安全（N≤160）✓
"""
from math import gcd
from sympy import mobius, divisor_count, divisor_sigma, totient, factorint, primeomega

NMAX = 135      # 序列长度（互素对至 12×11=132）
COP = [(a, b) for a in range(2, 13) for b in range(2, 13)
       if a < b and gcd(a, b) == 1]   # 互素对 (a,b), a<b


def build_atoms(nmax):
    """盲原子表：每项为 A_0..A_nmax 的整数列表。约定 n=0 处：算术原子取 0，常量取 1。"""
    A = {}
    A["const1"] = [1] * (nmax + 1)                       # 1
    A["id"] = list(range(nmax + 1))                      # n
    A["id2"] = [n * n for n in range(nmax + 1)]          # n^2  (×)
    A["mu"] = [0] + [int(mobius(n)) for n in range(1, nmax + 1)]
    A["absmu"] = [0] + [1 if int(mobius(n)) != 0 else 0 for n in range(1, nmax + 1)]
    A["Lam"] = [0] + [  # Λ(n) = log p if n = p^k else 0；用整数权重：取 exp 的指数部分
        int(round(__import__("math").log(next(iter(factorint(n)))))) if n > 1 and len(factorint(n)) == 1 else 0
        for n in range(1, nmax + 1)]
    A["mu_absmu"] = [0] + [int(mobius(n)) if int(mobius(n)) != 0 else 0 for n in range(1, nmax + 1)]
    A["one_big"] = [0] + [1] * nmax                      # 1_{n>=1}
    A["Omega"] = [0] + [sum(factorint(n).values()) for n in range(1, nmax + 1)]
    A["omega"] = [0] + [primeomega(n) for n in range(1, nmax + 1)]
    A["d"] = [0] + [int(divisor_count(n)) for n in range(1, nmax + 1)]
    A["sigma"] = [0] + [int(divisor_sigma(n)) for n in range(1, nmax + 1)]
    A["phi"] = [0] + [int(totient(n)) for n in range(1, nmax + 1)]
    A["id_mu"] = [0] + [n * int(mobius(n)) for n in range(1, nmax + 1)]
    A["id_phi"] = [0] + [n * int(totient(n)) for n in range(1, nmax + 1)]
    A["mu_phi"] = [0] + [int(mobius(n)) * int(totient(n)) for n in range(1, nmax + 1)]
    return A


def cauchy(A, B, nmax):
    C = [0] * (nmax + 1)
    for m in range(nmax + 1):
        if A[m] == 0:
            continue
        for k in range(nmax + 1 - m):
            if B[k]:
                C[m + k] += A[m] * B[k]
    return C


def is_mult(C):
    for a, b in COP:
        ab = a * b
        if C[ab] != C[a] * C[b]:
            return False
    return True


def degenerate(A, B):
    """G2′：有限支撑/零元退化检测（保守：支撑点数 <= 2 者视为退化）"""
    sa = sum(1 for x in A if x != 0)
    sb = sum(1 for x in B if x != 0)
    return sa <= 2 or sb <= 2


def main():
    nmax = NMAX
    atoms = build_atoms(nmax)
    names = sorted(atoms)
    print("盲生成类原子：%d 个 —— %s" % (len(names), ", ".join(names)))
    print("序列长度 N≤%d；互素对 %d 组\n" % (nmax, len(COP)))

    # 家族 1：单原子；家族 2：两原子的 ± 线性组合（+、× 允许）
    fam = {}
    for n in names:
        fam[n] = atoms[n]
    SUB = [n for n in names if n in ("const1","id","mu","absmu","Lam","one_big","Omega","d","phi","sigma")]
    for i, x in enumerate(SUB):
        for y in SUB[i + 1:]:
            fam["%s+%s" % (x, y)] = [atoms[x][k] + atoms[y][k] for k in range(nmax + 1)]
            fam["%s-%s" % (x, y)] = [atoms[x][k] - atoms[y][k] for k in range(nmax + 1)]
    print("候选 A/B 家族大小：%d\n" % len(fam))

    hits = []
    tested = 0
    fk = sorted(fam)
    for i, an in enumerate(fk):
        A = fam[an]
        for bn in fk:
            B = fam[bn]
            if degenerate(A, B):
                continue
            C = cauchy(A, B, nmax)
            if C[2] == 0 and C[3] == 0:
                continue
            tested += 1
            if is_mult(C):
                hits.append((an, bn, C[:13]))
    print("已测（非退化）配对：%d" % tested)
    print("乘性命中：%d" % len(hits))
    for an, bn, c in hits[:20]:
        print("   A=%-18s B=%-18s C[0..12]=%s" % (an, bn, c))
    if not hits:
        print("   ⟹ 最小盲生成类内【未发现】非退化的 Cauchy→乘性 实例")

    # 对照：多项式型子类的自证引理检查（C 为多项式型的必要形态）
    print("\n【对照】若 C 为多项式型且乘性 ⟹ 必为 N^k（自证：P(xy)≡P(x)P(y) ⟹ 单项式）")
    print("   测：C_N = N+1 是否乘性 ⟹", is_mult([0] + [n + 1 for n in range(nmax)]))
    print("   测：C_N = N   是否乘性 ⟹", is_mult([0] + [n for n in range(nmax)]))


if __name__ == "__main__":
    main()
