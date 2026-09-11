#!/usr/bin/env python3
"""
Provenance: retroactive archive header added 2026-09-11 by scripts/fix_archive_compliance.py
under the code-archive protocol (docs/PROTOCOL-CODE-ARCHIVE.md, R4).
The analysis itself was performed earlier; this header only records the file's existence
in the committed archive so that the computation is reproducible. Original code below.
"""
# 理论推导: R(k,b,L) 的渐近 + 临界结构
# R = k·L·(k-1)·B(2b+3,k-1)/((b+1)²·B(2b+1,k))
# 渐近 (k→∞): R → L·2(2b+1)/(b+1)
# 临界: R_limit > 1 ⟺ L > (b+1)/(2(2b+1))
import numpy as np
from math import lgamma, exp

def B(x, y):
    return exp(lgamma(x) + lgamma(y) - lgamma(x + y))

def R_value(k, b, L):
    if k < 2:
        return 0
    return k * L * (k-1) * B(2*b+3, k-1) / ((b+1)**2 * B(2*b+1, k))

def R_limit(b, L):
    """k→∞ 的极限"""
    return L * 2 * (2*b+1) / (b+1)

if __name__ == "__main__":
    print("=== 理论推导: R(k,b,L) 的结构 ===")
    print()
    print("1. 渐近极限 (k→∞): R → L·2(2b+1)/(b+1)")
    print("   b=0: 2L | b=1: 3L | b=2: 3.33L | b→∞: 4L")
    print()
    print("2. 验证渐近 (数值 vs 极限):")
    for b in [0, 1, 2, 5]:
        for L in [0.25, 0.3, 0.5]:
            R200 = R_value(200, b, L)
            Rlim = R_limit(b, L)
            print(f"   b={b} L={L}: R(200)={R200:.4f}  R(∞)={Rlim:.4f}")
    print()
    print("3. 临界 L (R_limit > 1): L > (b+1)/(2(2b+1))")
    for b in [0, 1, 2, 5, 10, 100]:
        Lcrit = (b+1)/(2*(2*b+1))
        print(f"   b={b}: L_crit = {Lcrit:.4f}")
    print()
    print("4. ★ 关键洞察: L=1/4 是临界值 (b→∞: L_crit → 1/4)")
    print("   BV 单独 (L=1/4): R_lim = 1 (需要度→∞或极大 k) - 边缘")
    print("   L > 1/4 (任何): R_lim > 1 - 大门打开 (Stadlmann 的合并!)")
    print()
    print("5. 最小成功 k 的预测 (给定 b, L):")
    for (b, L) in [(1, 0.26), (2, 0.26), (5, 0.26), (1, 0.3), (2, 0.3), (2, 0.5)]:
        kmin = None
        for k in range(2, 500):
            if R_value(k, b, L) > 1:
                kmin = k
                break
        if kmin:
            print(f"   b={b} L={L}: 最小成功 k = {kmin}")
        else:
            print(f"   b={b} L={L}: k<500 未成功")
