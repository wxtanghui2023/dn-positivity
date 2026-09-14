#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
E170：(1) p=2 (mod 4) 穷举，验证唐先生的二分结论
     (2) 自我更正：{奇数} 在 mod p^2 下的像【不是】奇剩余，而是【全部剩余】
"""
from itertools import combinations

print("=== (1) mod 4 (p=2)：A2⊆{0,1,2}, B2⊆{1,2,3} ===")
G = 4
SA = [0, 1, 2]          # A ⊆ S-1 mod 4  (S mod 4 = {1,2,3})
SB = [1, 2, 3]          # B ⊆ S mod 4
sols = []
for ra in range(1, len(SA)+1):
    for A in combinations(SA, ra):
        for rb in range(1, len(SB)+1):
            for B in combinations(SB, rb):
                pairs = [(a+b) % G for a in A for b in B]
                # (A) 覆盖 {1,2,3}；(C) 唯一（每个和恰一次）
                if set(pairs) != {1, 2, 3}:
                    continue
                if len(pairs) != 3:
                    continue
                sols.append((sorted(A), sorted(B)))
print("  满足 (A)+唯一 的解数 =", len(sols))
for A, B in sols:
    print("    A=%s  B=%s   |A|=%d |B|=%d" % (A, B, len(A), len(B)))

print()
print("=== (2) 自我更正：{奇数} mod p^2 的像 ===")
for p in (3, 5, 7):
    p2 = p*p
    # 取足够长的奇数样本（含 p^2 的奇数倍）
    odds = [n for n in range(1, 40*p2) if n % 2 == 1]
    img = sorted({n % p2 for n in odds})
    print("  p=%d p^2=%d  奇数的像 = %s  (size=%d, 全部剩余? %s)"
          % (p, p2, img, len(img), img == list(range(p2))))
    print("     理由：p^2 是奇数 ⟹ p^2 ∈ {奇数} ⟹ p^2 ≡ 0 (mod p^2) ⟹ 0 在像中")
