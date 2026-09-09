#!/usr/bin/env python3
"""三问审计——第一问：J 的纤维 vs S₃ 轨道——2026-09-09
J(x) = (x²−x+1)³/(x²(x−1)²)——S₃ 不变——检验：
① 纤维 = 轨道（在 ℚ 上——generic——）
② 整数约束：J 在 ℤ_{>1} 上是否单射（轨道 ∩ ℤ_{>1} = 单点——）
③ 退化轨道（固定点——）
"""
from math import gcd
from fractions import Fraction

def J(x):
    """精确有理 J"""
    x = Fraction(x)
    num = (x*x - x + 1)**3
    den = x*x*(x-1)**2
    return num/den

def J_float(x):
    x2 = x*x
    return (x2-x+1)**3/(x2*(x-1)**2)

# ① S₃ 轨道点（对给定的 x——）
def orbit(x):
    if isinstance(x, Fraction):
        return set([x, 1-x, Fraction(1,1)/x if x != 0 else None,
                    Fraction(1,1)/(1-x) if x != 1 else None,
                    x/(x-1) if x != 1 else None,
                    (x-1)/x if x != 0 else None])
    return None

print('=== ① 纤维 = 轨道（generic——）验证 ===')
# 对随机有理点——解 J(x) = J(x0) 的 6 个根应该 = 轨道
# 用数值：J 的 6 次方程 (x²−x+1)³ − J0·x²(x−1)² = 0
import numpy as np
for x0 in [Fraction(2), Fraction(3), Fraction(5,3)]:
    J0 = J(x0)
    # 多项式系数：(x²−x+1)³ − J0 x²(x−1)²——展开
    # (x²−x+1)³ = x⁶−3x⁵+6x⁴−7x³+6x²−3x+1
    # x²(x−1)² = x⁴−2x³+x²
    # 系数（从高到低）：
    coeff = [1, -3, 6-float(J0), -7+2*float(J0), 6-float(J0), -3, 1]
    roots = np.roots(coeff)
    # 轨道点的数值
    x0f = float(x0)
    orb_pts = set([x0f, 1-x0f, 1/x0f if x0f != 0 else 99,
                   1/(1-x0f) if x0f != 1 else 99,
                   x0f/(x0f-1) if x0f != 1 else 99,
                   (x0f-1)/x0f if x0f != 0 else 99])
    # 检查每个根是否 ≈ 轨道点
    matched = 0
    for r in roots:
        if any(abs(r - p) < 1e-6 for p in orb_pts):
            matched += 1
    print(f'  x0={x0}: 根数={len(roots)}——匹配轨道点={matched}/6——'
          f'纤维=轨道: {matched >= 6}')

print()
print('=== ② J 在 ℤ_{>1} 上单射？===')
# 检查不同整数 d1≠d2 是否可能同 J（通过轨道 ∩ 整数——）
# 直接暴力：J(d1) == J(d2) 对 d1,d2 ∈ [2,500]
from collections import defaultdict
vals = defaultdict(list)
for d in range(2, 2000):
    vals[float(J(d))].append(d)
collisions = {k: v for k, v in vals.items() if len(v) > 1}
print(f'  d ∈ [2,2000]: 碰撞组数 = {len(collisions)}')
for k, v in list(collisions.items())[:5]:
    print(f'    J={k:.6f}: d = {v}')

print()
print('=== ③ 退化轨道（固定点——）===')
# A: x=1/2——M: x=±1——AM 固定点：x = (x−1)/x ⟹ x²−x+1=0（Φ₆ 根——）
print('  A 固定点: x=1/2——M 固定点: x=±1——AM 固定点: Φ₆ 根（e^{±iπ/3}——）')
print(f'  J(1/2) = {J(Fraction(1,2))}——J(1) = 极点——J(0) = 极点')
# J(1/2) 的轨道（退化——{1/2, 1/2, 2, 2, -1, -1}——）
print(f'  x=1/2 的轨道（6 点但重合）: {{1/2, 1/2, 2, 2, −1, −1}}——'
      f'J = {float(J(Fraction(1,2))):.4f}——纤维 < 6 不同点（退化——）')
