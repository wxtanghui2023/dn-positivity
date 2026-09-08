#!/usr/bin/env python3
"""
M(T) 增长的决定性检查
问题：M(T) 是 O(1)（不随 T 增长——）还是 O(log T)（常数小——）？
方法：分段算 M 的"范围"随 T——看增长
如果 O(1)：max|M| 稳定（~常数）
如果 O(log)：max|M| ~ c·log T（增长——）
"""
import numpy as np
from math import log, pi

def load_zeros(n, offset=0):
    path = '/home/node/.openclaw/workspace/dn-project/zeros/zeros6'
    z = np.zeros(n)
    with open(path) as f:
        for _ in range(offset):
            f.readline()
        for i in range(n):
            z[i] = float(f.readline())
    return z

def IntN0(t):
    if t <= 1: return 0.0
    return t*t/(4*pi)*log(t/(2*pi)) - 3*t*t/(8*pi) + 7*t/8

def main():
    print("="*70)
    print("M(T) 增长检查（分段——）")
    print("="*70)
    
    # 用 400k 零点（快速——分 8 段每段 50k——）
    SEG = 50000
    NSEG = 8
    K = SEG * NSEG
    z = load_zeros(K)
    print(f"零点到 γ={z[-1]:.0f}（K={K}——）")
    
    # 逐段算 M——段内递推——段间连续
    # M(γ_{k+1}) = M(γ_k) + k·Δγ_k - [IntN0(γ_{k+1})-IntN0(γ_k)]
    # 用 float128 全程递推
    M_val = np.float128(0.0)
    print(f"\n{'段':>4} {'γ 范围':>18} {'max|M|':>10} {'末值':>10} {'log T':>8}")
    seg_max = 0
    for seg in range(NSEG):
        k0 = seg*SEG
        k1 = min((seg+1)*SEG, K)
        seg_local_max = 0
        for k in range(k0, k1-1):
            kk = k + 1  # 区间 (γ_k, γ_{k+1})——N = kk
            dg_k = z[k+1] - z[k]
            dInt = IntN0(z[k+1]) - IntN0(z[k])
            M_val += np.float128(kk)*np.float128(dg_k) - np.float128(dInt)
            m = abs(float(M_val))
            if m > seg_local_max: seg_local_max = m
        if seg_local_max > seg_max: seg_max = seg_local_max
        T = z[k1-1]
        print(f"{seg+1:>4} {z[k0]:>10.0f}-{T:>8.0f} {seg_local_max:>10.3f} {float(M_val):>10.3f} {log(T):>8.2f}")
    
    print(f"\n全程 max|M| = {seg_max:.3f}（到 γ={z[-1]:.0f}——T~{z[-1]:.0f}——log T ~ {log(z[-1]):.1f}——）")
    print(f"对比：8/22 用 2M 零点 max|M| = 1.33——log(2.5e6) ~ 14.7")
    print(f"如果 O(log)：c ~ max|M|/log T——比较不同范围")

if __name__ == "__main__":
    main()
