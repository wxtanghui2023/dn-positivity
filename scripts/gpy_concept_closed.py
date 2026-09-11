#!/usr/bin/env python3
"""
Provenance: retroactive archive header added 2026-09-11 by scripts/fix_archive_compliance.py
under the code-archive protocol (docs/PROTOCOL-CODE-ARCHIVE.md, R4).
The analysis itself was performed earlier; this header only records the file's existence
in the committed archive so that the computation is reproducible. Original code below.
"""
# GPY/Maynard 概念复现 (闭式版)
# F_b(t) = (1-Σt_i)^b on Δ_k
# I = ∫_{Δ_k} F² = B(2b+1, k)/(k-1)!
# J = ∫_{Δ_{k-1}} (∫F du)² = B(2b+3, k-1)/((b+1)²·(k-2)!)
# R = k·J/I
# Maynard: sup R > 1 ⟹ H_1 有界 (需 k 足够大)
import numpy as np
from math import gamma, lgamma

def B(x, y):
    """Beta 函数 (用 lgamma 避免溢出)"""
    return np.exp(lgamma(x) + lgamma(y) - lgamma(x + y))

def R_value(k, b):
    """R(F_b, k) = k·J/I"""
    if k < 2:
        return 0
    # I = B(2b+1, k) / (k-1)!
    I_val = B(2*b + 1, k) / gamma(k)
    # J = B(2b+3, k-1) / ((b+1)² (k-2)!)
    J_val = B(2*b + 3, k - 1) / ((b+1)**2 * gamma(k-1))
    return k * J_val / I_val if I_val > 0 else 0

if __name__ == "__main__":
    print("=== GPY/Maynard 概念复现 (闭式): R = k·J/I > 1? ===")
    print("F_b = (1-Σt_i)^b - 若 sup_b R > 1 → H_1 有界")
    print()
    
    for b in [0, 1, 2, 4, 8]:
        print(f"--- b={b} ---")
        found = False
        for k in [2, 3, 5, 8, 10, 15, 20, 30, 50, 70, 100, 150, 200, 300]:
            R = R_value(k, b)
            flag = " *** >1!***" if R > 1 else ""
            if R > 1 and not found:
                print(f"  k={k:>4}: R={R:.4f}{flag}  ← 首次超过 1")
                found = True
            elif k <= 20 or k % 50 == 0:
                print(f"  k={k:>4}: R={R:.4f}{flag}")
        if not found:
            print(f"  (b={b}: k≤300 未超过 1)")
        print()
    
    print("Maynard 参考: 用最优 F (对称多项式 - 度1) - k≈105 时超过 1")
    print("这里 F=(1-Σt)^b 是次优的 - 超过 1 的 k 应该更大 (验证框架)")
