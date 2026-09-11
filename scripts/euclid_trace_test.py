#!/usr/bin/env python3
"""
Provenance: retroactive archive header added 2026-09-11 by scripts/fix_archive_compliance.py
under the code-archive protocol (docs/PROTOCOL-CODE-ARCHIVE.md, R4).
The analysis itself was performed earlier; this header only records the file's existence
in the committed archive so that the computation is reproducible. Original code below.
"""
# Euclidean Cocycle: Tr(P_s^k) 结构测试
# P_s f(x) = Σ_n Λ(n)(n+x)^{-2s} f(1/(n+x))
# Tr(P_s^k) = Σ_{周期k连分数} Π_j Λ(n_j)(n_j+x_j)^{-2s} / |1-(T^k)'(x)|
# k=1: 周期1固定点 x_n = (√(n²+4)-n)/2,  x=1/(n+x), T'(x)=-x², |1-T'(x)|=1+x²
# 预测: Tr(P_s) ≈ -ζ'(2s)/ζ(2s) (塌缩) + 修正
import numpy as np, math, time

def prime_power_lams(N):
    """素幂列表 (n, log p)"""
    is_p = np.ones(N+1, dtype=bool)
    is_p[:2] = False
    for i in range(2, int(N**0.5)+1):
        if is_p[i]:
            is_p[i*i::i] = False
    items = []
    for p in range(2, N+1):
        if is_p[p]:
            lp = math.log(p)
            pk = p
            while pk <= N:
                items.append((pk, lp))
                pk *= p
    return items

def trace_k1(sigma, N):
    """Tr(P_s) 周期1: Σ Λ(n)(n+x_n)^{-2σ}/(1+x_n²), x_n=(√(n²+4)-n)/2"""
    total = 0.0
    for n, lam in prime_power_lams(N):
        x = (math.sqrt(n*n+4) - n) / 2.0
        total += lam * (n+x)**(-2*sigma) / (1 + x*x)
    return total

def zeta_prime_ratio(ss, N):
    """-ζ'(s)/ζ(s) ≈ Σ_{n素幂≤N} Λ(n)n^{-s}"""
    total = 0.0
    for n, lam in prime_power_lams(N):
        total += lam * n**(-ss)
    return total

if __name__ == "__main__":
    N = 200000
    print("k=1 迹测试: Tr(P_s) vs -ζ'(2σ)/ζ(2σ)  (N=%d)" % N)
    hdr1 = 'Tr(P_s)'
    hdr2 = '-zp/zp(2s)'
    print(f"{'σ':>5} {hdr1:>16} {hdr2:>16} {'比值':>10} {'差':>14}")
    for sig in [0.8, 1.0, 1.2, 1.5, 2.0, 3.0]:
        t1 = trace_k1(sig, N)
        t2 = zeta_prime_ratio(2*sig, N)
        ratio = t1/t2 if t2 != 0 else 0
        print(f"{sig:>5} {t1:>16.6f} {t2:>16.6f} {ratio:>10.6f} {t1-t2:>14.6f}")
