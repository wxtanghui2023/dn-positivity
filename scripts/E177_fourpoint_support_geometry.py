#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
E177：四点支撑几何的局部—全局终审
问：G_S = {(h,k) : 存在 x 使 x, x+h, x+k, x+h+k 全平方自由} 是否严格小于 prod_p G_{S,p}？
做法：对每个素数 p，枚举 (h,k) mod p^2，判断禁区 F = {0,-h,-k,-h-k} 是否覆盖全部 p^2 个残类。
"""
from itertools import product

def zet(p):
    p2 = p * p
    Z = []
    for h in range(p2):
        for k in range(p2):
            F = {0 % p2, (-h) % p2, (-k) % p2, (-h - k) % p2}
            if len(F) >= p2:          # 禁区覆盖全部残类 ⟹ 无可用 x
                Z.append((h, k))
    return Z

print("=== 四点禁区 Z_p（h,k 取自 Z/p^2，F={0,-h,-k,-h-k} 覆盖全部残类）===")
for p in (2, 3, 5, 7):
    Z = zet(p)
    print("  p=%2d  p^2=%3d  |Z_p| = %-6d  Z_p = %s" % (p, p*p, len(Z), Z[:12]))
print()
print("=== 一般原理验证：k 点构型仅 p <= sqrt(k) 可能禁阻 ===")
for k in (2, 3, 4, 5):
    lim = int(k ** 0.5) + 1
    bad = []
    for p in [2, 3, 5, 7, 11]:
        p2 = p * p
        found = False
        for hs in product(range(p2), repeat=k-1):
            F = {(-h) % p2 for h in hs} | {0}
            if len(F) >= p2:
                found = True
                break
        if found:
            bad.append(p)
    print("  k=%d 点：能禁阻的素数 = %s   （理论界 p <= sqrt(k)=%.1f）" % (k, bad, k ** 0.5))
print()
print("=== 与 E170 的 p=2 刚性联用 ===")
print("  p=2 解 (A2,B2) = ({0},{1,2,3}) 或 ({0,1,2},{1})")
print("  ⟹ A-A ⊆ 4Z  或  B-B ⊆ 4Z  （至少一个坐标 ≡ 0 mod 4）")
print("  而 Z_2 中的 (h,k) 需要 h ≠ 0 且 k ≠ 0 mod 4（因 h=0 时 |F| <= 2 < 4）")
print("  ⟹ (A-A)×(B-B) ∩ Z_2 = ∅  【自动成立，无矛盾】")
