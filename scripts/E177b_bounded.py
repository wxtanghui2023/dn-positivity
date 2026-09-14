#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""E177b：四点禁区 Z_p 的有界枚举（p<=7；及 p^2>k 的一般原理表）"""
def zet(p):
    p2 = p * p
    return [(h, k) for h in range(p2) for k in range(p2)
            if len({0 % p2, (-h) % p2, (-k) % p2, (-h - k) % p2}) >= p2]

print("=== 四点禁区 Z_p ===")
for p in (2, 3, 5, 7):
    Z = zet(p)
    print("  p=%2d p^2=%3d |Z_p|=%3d  %s" % (p, p*p, len(Z), Z[:10]))
print()
print("=== Z_2 的结构 ===")
Z2 = zet(2)
print("  Z_2 =", Z2)
print("  含 h=0 的?", [x for x in Z2 if x[0] == 0])
print("  含 k=0 的?", [x for x in Z2 if x[1] == 0])
print("  ⟹ Z_2 中 h,k 皆非 0 mod 4")
print()
print("=== 一般原理：k 点构型只能被 p <= sqrt(k) 的素数禁阻 ===")
print("  k=2: p<=1.41 → 无素数 ⟹ 恒可满足（两点必可同平方自由）")
print("  k=3: p<=1.73 → 无素数 ⟹ 恒可满足")
print("  k=4: p<=2.00 → 仅 p=2")
print("  k=5: p<=2.24 → 仅 p=2")
print("  k=9: p<=3.00 → p=2,3")
