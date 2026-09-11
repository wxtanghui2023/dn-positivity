#!/usr/bin/env python3
"""
Provenance: retroactive archive header added 2026-09-11 by scripts/fix_archive_compliance.py
under the code-archive protocol (docs/PROTOCOL-CODE-ARCHIVE.md, R4).
The analysis itself was performed earlier; this header only records the file's existence
in the committed archive so that the computation is reproducible. Original code below.
"""
# GPY/Maynard 概念复现 (闭式修正版)
# 支撑 Δ_k(L) = {t_i≥0, Σt_i ≤ L} (L=1/4 对 BV - 分布水平 θ 相关)
# F_b(t) = (L - Σt_i)^b
# I = L^{2b+k}·B(2b+1,k)/(k-1)!
# J = L^{2b+k+1}·B(2b+3,k-1)/((b+1)²(k-2)!)
# R = k·J/I = k·L·(k-1)·B(2b+3,k-1)/((b+1)²·B(2b+1,k))
import numpy as np
from math import lgamma, exp

def B(x, y):
    return exp(lgamma(x) + lgamma(y) - lgamma(x + y))

def R_value(k, b, L):
    """R(F_b, k, L)"""
    if k < 2:
        return 0
    return k * L * (k-1) * B(2*b+3, k-1) / ((b+1)**2 * B(2*b+1, k))

if __name__ == "__main__":
    print("=== GPY/Maynard 概念复现 (闭式修正): R = k·J/I > 1? ===")
    print("支撑 Σt_i ≤ L - L=1/4 (BV) 或 L 更大 (Zhang/EH)")
    print()
    
    for L in [1/4, 1/3, 1/2, 0.7, 1.0]:
        print(f"--- L={L} (分布水平 θ={L*2} 类) ---")
        for b in [0, 1, 2]:
            found_k = None
            for k in [2, 3, 5, 8, 10, 15, 20, 30, 50, 70, 100, 150, 200]:
                R = R_value(k, b, L)
                if R > 1 and found_k is None:
                    found_k = k
            if found_k:
                print(f"  b={b}: R 首次>1 在 k={found_k} (Maynard 参考: k~105 for L=1/4)")
            else:
                print(f"  b={b}: k≤200 未超 1 (R(200)={R_value(200,b,L):.4f})")
        print()
    
    print("验证: k=2 (孪生) 应该 R<1 对所有 L<1 的 - L=1/4: R(2,0) =",
          f"{R_value(2,0,1/4):.4f}")
