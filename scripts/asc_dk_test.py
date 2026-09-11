#!/usr/bin/env python3
"""
Provenance: retroactive archive header added 2026-09-11 by scripts/fix_archive_compliance.py
under the code-archive protocol (docs/PROTOCOL-CODE-ARCHIVE.md, R4).
The analysis itself was performed earlier; this header only records the file's existence
in the committed archive so that the computation is reproducible. Original code below.
"""
# ASC: 加法-乘法尺度曲率 D_k(q,n) = det(A(q^{i+j}n))_{0<=i,j<=k}
# D1 = A(n)A(q²n) - A(qn)²  (2x2 Hankel)
# D2 = 3x3 Hankel
# 检查 D_k >= 0 的纯算术符号性质
import numpy as np, math, time
from acpc_loop_test import sieve_primes, compute_A

def prime_powers_upto(X):
    items = []
    for p in sieve_primes(X):
        lp = math.log(p)
        pk = p
        while pk <= X:
            items.append((pk, lp))
            pk *= p
    items.sort()
    return items

def analyze_D1(A, X, Q=None):
    """D1(q,n) = A(n)A(q²n)-A(qn)² 符号统计"""
    if Q is None:
        Q = int(math.sqrt(X))
    ppq = prime_powers_upto(Q)
    pos = neg = zero = 0
    neg_examples = []
    total = 0
    maxrel = 0
    for q, lq in ppq:
        if q*q > X: continue
        lim = X // (q*q)
        # n 从 1 到 lim (A(n)>0 才有效——n 需有加法分解——但 A(n) 可能 0 (n 小/奇数? 不——A(n)>0 几乎所有 n>=4?)——)
        for n in range(1, lim+1):
            an = A[n]
            if an <= 0: continue
            aqn = A[q*n]
            aq2n = A[q*q*n]
            d1 = an*aq2n - aqn*aqn
            # 相对大小 (曲率 vs 主项)
            rel = abs(d1) / (an*aq2n) if an*aq2n > 0 else 0
            if rel > maxrel: maxrel = rel
            total += 1
            if d1 > 0: pos += 1
            elif d1 < 0: neg += 1
            else: zero += 1
            if d1 < 0 and len(neg_examples) < 10:
                neg_examples.append((q, n, d1, an, aqn, aq2n))
    print(f"D1: X={X}, q<=√X={Q}: 总 {total} 正 {pos} ({pos/total*100:.1f}%) 负 {neg} ({neg/total*100:.1f}%) 零 {zero}")
    print(f"  最大相对曲率 {maxrel:.4f}")
    if neg_examples:
        print("  负例 (q,n,D1,A(n),A(qn),A(q²n)):")
        for e in neg_examples[:5]:
            print(f"    q={e[0]} n={e[1]}: D1={e[2]:.4e} A(n)={e[3]:.2f} A(qn)={e[4]:.2f} A(q²n)={e[5]:.2f}")
    return pos, neg, zero

def analyze_D2(A, X, Q=None):
    """D2 = 3x3 Hankel det(A(q^{i+j}n))"""
    if Q is None:
        Q = int(X**0.25)
    ppq = prime_powers_upto(Q)
    pos = neg = zero = 0
    total = 0
    neg_ex = []
    for q, lq in ppq:
        q2 = q*q; q3 = q2*q; q4 = q3*q
        if q4 > X: continue
        lim = X // q4
        for n in range(1, lim+1):
            a0 = A[n]; a1 = A[q*n]; a2 = A[q2*n]; a3 = A[q3*n]; a4 = A[q4*n]
            if a0 <= 0: continue
            # 3x3 Hankel det
            d2 = a0*(a2*a4 - a3*a3) - a1*(a1*a4 - a2*a3) + a2*(a1*a3 - a2*a2)
            total += 1
            if d2 > 0: pos += 1
            elif d2 < 0: neg += 1
            else: zero += 1
            if d2 < 0 and len(neg_ex) < 5:
                neg_ex.append((q, n, d2, a0, a1, a2))
    print(f"D2: X={X}, q<=X^(1/4)={Q}: 总 {total} 正 {pos} ({pos/total*100:.1f}%) 负 {neg} ({neg/total*100:.1f}%) 零 {zero}")
    if neg_ex:
        print("  负例 (q,n,D2,A(n),A(qn),A(q²n)):")
        for e in neg_ex[:3]:
            print(f"    q={e[0]} n={e[1]}: D2={e[2]:.4e} A(n)={e[3]:.2f} A(qn)={e[4]:.2f} A(q²n)={e[5]:.2f}")
    return pos, neg, zero

if __name__ == "__main__":
    import sys
    X = int(sys.argv[1]) if len(sys.argv) > 1 else 100000
    t0 = time.time()
    A = compute_A(X)
    print(f"A 计算 {time.time()-t0:.1f}s (X={X})")
    analyze_D1(A, X)
    print()
    analyze_D2(A, X)
    print(f"总耗时 {time.time()-t0:.1f}s")
