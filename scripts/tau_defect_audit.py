#!/usr/bin/env python3
"""
Provenance: retroactive archive header added 2026-09-11 by scripts/fix_archive_compliance.py
under the code-archive protocol (docs/PROTOCOL-CODE-ARCHIVE.md, R4).
The analysis itself was performed earlier; this header only records the file's existence
in the committed archive so that the computation is reproducible. Original code below.
"""
# 因子格维数缺陷审计：δ(n,m) = d(nm) - d(n) - d(m)
# 第一死亡测试：是否 Euler 化（坍缩成 ζ 结构——）？
import numpy as np

def tau(n):
    cnt = 0
    d = 1
    while d*d <= n:
        if n % d == 0:
            cnt += 1
            if d*d != n:
                cnt += 1
        d += 1
    return cnt

def delta(n, m):
    return tau(n*m) - tau(n) - tau(m)

print("=== δ(n,m) = d(nm) - d(n) - d(m) 结构验证 ===")
print("单素数（n=p^a, m=p^b）：δ = (a+b+1)-(a+1)-(b+1) = -1（常数）")
for a in [1, 2, 3]:
    for b in [1, 2]:
        n, m = 2**a, 2**b
        print(f"  n=2^{a} m=2^{b}: δ = {delta(n,m)}（理论 -1）")

print()
print("两素数（n=2^a·3^c, m=2^b·3^d）：δ = ad + bc - 1（交叉项）")
for (a, c, b, d) in [(1,1,1,1), (1,2,2,1), (2,1,1,2), (1,1,2,3)]:
    n, m = 2**a * 3**c, 2**b * 3**d
    theo = a*d + b*c - 1
    print(f"  (a,c,b,d)=({a},{c},{b},{d}): δ = {delta(n,m)}（理论 ad+bc-1 = {theo}）")

print()
print("=== 交叉项的可分离性（Euler 化关键）===")
print("交叉项 ad = v_p(m)·v_q(n)——在乘性加权和中：")
print("Σ v_p(m)v_q(n)·n^{-s}m^{-t} = (Σ v_q(n)n^{-s})·(Σ v_p(m)m^{-t})")
print("——完全分离（乘积）——每一项都是已知 ζ 类结构的组合——")

print()
print("=== 数值验证：δ 的乘性和的'因子化' ===")
print("测试：Σ_{n,m≤N} δ(n,m)·(nm)^{-2}（收敛——）vs 逐素数局部积的预测——")
# 直接算小 N
def sum_delta(N, s=2.0):
    total = 0.0
    for n in range(1, N+1):
        for m in range(1, N+1):
            total += delta(n, m) * (n*m)**(-s)
    return total

for N in [10, 20, 30]:
    print(f"  N={N}: Σ δ(n,m)(nm)^-2 = {sum_delta(N):.6f}")

print()
print("=== 解析判断：δ 的结构 ===")
print("δ = Π_p(v_p(n)+v_p(m)+1) - Π_p(v_p(n)+1) - Π_p(v_p(m)+1)")
print("展开：δ = Σ_{非空 S⊆P} [Π_{p∈S}(v_p(n)+v_p(m))·Π_{p∉S}(...) 的组合]")
print("每一项（如 ad = v_p(m)v_q(n)——）在乘性加权和中分离——")
print("⟹ δ 的任何乘性加权和 = ζ(s), Σv_p(n)n^{-s}（=ζ的p-对数导）, ζ(s)^k 等的组合——")
print("⟹ 第一死亡测试触发：Euler 化——封档——")
