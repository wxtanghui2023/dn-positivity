#!/usr/bin/env python3
"""
Provenance: retroactive archive header added 2026-09-11 by scripts/fix_archive_compliance.py
under the code-archive protocol (docs/PROTOCOL-CODE-ARCHIVE.md, R4).
The analysis itself was performed earlier; this header only records the file's existence
in the committed archive so that the computation is reproducible. Original code below.
"""
# 素数 vs 合数的速度/力比较
import numpy as np

def is_prime(n):
    if n < 2:
        return False
    for d in range(2, int(n**0.5)+1):
        if n % d == 0:
            return False
    return True

N = 10000
gamma1 = 14.1347

print("=== 素数 vs 合数速度 v(n) = log n/sqrt(n)（sigma=1/2）===")
print("（贡献向量 n^{-sigma-it} 随 t 的运动速度——）")
pv = np.mean([np.log(p)/np.sqrt(p) for p in range(2, N+1) if is_prime(p)])
cv = np.mean([np.log(c)/np.sqrt(c) for c in range(2, N+1) if not is_prime(c)])
print(f"素数平均速度 = {pv:.5f}")
print(f"合数平均速度 = {cv:.5f}")
print("（合数平均更大——因为合数可很大——这是大小效应——）")

print()
print("=== 同大小邻域比较（消除大小效应）===")
for lo in range(1, 1001, 200):
    hi = lo + 199
    plist = [p for p in range(lo, hi+1) if is_prime(p)]
    clist = [c for c in range(lo, hi+1) if not is_prime(c)]
    if plist:
        pv2 = np.mean([np.log(p)/np.sqrt(p) for p in plist])
        cv2 = np.mean([np.log(c)/np.sqrt(c) for c in clist])
        print(f"  n in [{lo},{hi}]: 素数={pv2:.5f}  合数={cv2:.5f}  比={pv2/cv2:.4f}")
    else:
        print(f"  n in [{lo},{hi}]: 无素数")

print()
print("=== 相位锁定（集体结构——非单数速度——）===")
def weighted_phase(is_p):
    tw = 0.0
    tc = 0.0
    for n in range(2, N+1):
        if is_prime(n) == is_p:
            w = 1.0/np.sqrt(n)
            tw += w
            tc += w*np.cos(gamma1*np.log(n))
    return tc/tw

wp = weighted_phase(True)
wc = weighted_phase(False)
print(f"素数加权平均 cos(gamma1 log n) = {wp:+.4f}")
print(f"合数加权平均 cos(gamma1 log n) = {wc:+.4f}")
print("（素数为负=锁定；合数接近0=分散——）")
