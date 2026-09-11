#!/usr/bin/env python3
"""
Provenance: retroactive archive header added 2026-09-11 by scripts/fix_archive_compliance.py
under the code-archive protocol (docs/PROTOCOL-CODE-ARCHIVE.md, R4).
The analysis itself was performed earlier; this header only records the file's existence
in the committed archive so that the computation is reproducible. Original code below.
"""
# AXD: Arithmetic Exchange Defect
# σ: 素因子中 p<->q 互换 (乘法同态, 非加法同态)
# 加法关系 a+b=c 在交换 p,q 乘法角色后保持 iff σ(a)+σ(b) = σ(c)
# AXD_N(p,q) = #{a+b<=N : σ(a)+σ(b) != σ(a+b)}
# τ(p,q) = min N 使冲突出现 (第一个被破坏的加法关系的最小和)
import sys

def sigma(n, p, q):
    """素因子中 p<->q 互换"""
    m = n
    vp = 0
    while m % p == 0:
        vp += 1
        m //= p
    vq = 0
    while m % q == 0:
        vq += 1
        m //= q
    return m * (p ** vq) * (q ** vp)

def axd_stats(N, p, q):
    """返回 (冲突数, 保持数, 总加法关系数, 第一个冲突的和)"""
    conflict = 0
    keep = 0
    first_conflict = None
    # 预计算 sigma
    sig = [0] * (N + 1)
    for n in range(1, N + 1):
        sig[n] = sigma(n, p, q)
    for a in range(1, N):
        sa = sig[a]
        for b in range(1, N - a + 1):
            c = a + b
            if sa + sig[b] == sig[c]:
                keep += 1
            else:
                conflict += 1
                if first_conflict is None:
                    first_conflict = c
    return conflict, keep, conflict + keep, first_conflict

if __name__ == "__main__":
    pairs = [(2,3),(2,5),(3,5),(2,7),(3,7)]
    Ns = [30, 60, 100, 150, 200]
    print("AXD 测试: σ(a)+σ(b) vs σ(a+b)  (a+b<=N)")
    print(f"{'pair':>8} | " + " | ".join(f"N={N}: AXD/总 (保持)" for N in Ns))
    for p, q in pairs:
        row = []
        for N in Ns:
            conflict, keep, total, _ = axd_stats(N, p, q)
            row.append(f"{conflict}/{total} ({keep})")
        print(f"({p},{q}) | " + " | ".join(row))
    print()
    # τ(p,q): 第一个冲突的最小 N (= 最小被破坏的 a+b 的和)
    print("τ(p,q) = 第一个被 σ 破坏的加法关系的最小和:")
    for p, q in pairs:
        # 扫描小的 a+b
        tau = None
        # 预计算 sigma 到足够大
        LIM = 500
        sig = [0]*(LIM+1)
        for n in range(1, LIM+1):
            sig[n] = sigma(n, p, q)
        for c in range(2, LIM+1):
            found = False
            for a in range(1, c):
                b = c - a
                if sig[a] + sig[b] != sig[c]:
                    found = True
                    break
            if found:
                tau = c
                break
        # 也找保持的 (非平凡信息)
        print(f"  τ({p},{q}) = {tau}")
