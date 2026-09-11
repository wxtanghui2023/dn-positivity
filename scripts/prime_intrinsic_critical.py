#!/usr/bin/env python3
"""
Provenance: retroactive archive header added 2026-09-11 by scripts/fix_archive_compliance.py
under the code-archive protocol (docs/PROTOCOL-CODE-ARCHIVE.md, R4).
The analysis itself was performed earlier; this header only records the file's existence
in the committed archive so that the computation is reproducible. Original code below.
"""
# 素数内在临界（不含零点）——σ=1/2 是否从素数统计自然出现
import numpy as np

N = 2000000
print("筛素数到 2M...")
sieve = np.ones(N+1, dtype=bool)
sieve[:2] = False
for i in range(2, int(N**0.5)+1):
    if sieve[i]:
        sieve[i*i::i] = False
primes = np.nonzero(sieve)[0]
print(f"素数个数：{len(primes)}")

print()
print("=== 素数倒数和的发散（Σ 1/p ~ log log N）===")
s = np.sum(primes**(-1.0))
print(f"Σ 1/p = {s:.3f}（~log log N = {np.log(np.log(N)):.3f}——发散——）")

print()
print("=== 素数波动均方 Σ_p p^{-2σ}——临界在哪？===")
for sg in [0.4, 0.45, 0.48, 0.5, 0.52, 0.55, 0.6, 0.7, 1.0]:
    val = np.sum(primes**(-2*sg))
    print(f"sigma={sg:.2f}: Sum_p p^(-2sigma) = {val:.4f}")

print()
print("=== 素数相位波动容量 |Σ_p p^{-σ-iγ1}|——σ 的函数 ===")
gamma1 = 14.1347
for sg in [0.4, 0.45, 0.5, 0.55, 0.6, 0.7]:
    S = np.sum(primes**(-sg-1j*gamma1))
    print(f"sigma={sg:.2f}: |Sum_p p^(-sigma-iγ1)| = {abs(S):.4f}")

print()
print("=== 全整数对比：Σ_n n^{-2σ}（已知——ζ(2σ) 在 σ=1/2 发散——）===")
print("素数的 Σ_p p^{-2σ}：在 2σ=1（σ=1/2）时 = Σ_p 1/p——发散（log log——）")
print("——素数的波动均方临界也在 σ=1/2（与全整数一致——）——")
