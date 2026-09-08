#!/usr/bin/env python3
"""
决定性测试：M(T) 是 O(1) 还是慢漂移（O(log log T)——）？
用 2M 零点数据——全程 M 轨迹——分块平均——看漂移是否持续
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
    print("M(T) O(1) vs 慢漂移——2M 决定性测试")
    print("="*70)
    
    # 分段处理 2M（每 200k 一段——float128——）
    SEG = 200000
    NSEG = 10
    print("处理 2M 零点（10 段×200k——）...")
    
    M_val = np.float128(0.0)
    seg_means = []
    seg_maxs = []
    for seg in range(NSEG):
        z = load_zeros(SEG, seg*SEG)
        # 段内递推——但注意段间连续性——M_val 延续
        M_seg = np.zeros(SEG, dtype=np.float128)
        for k in range(SEG-1):
            kk = k + 1 + seg*SEG  # 全局零点序号
            M_val += np.float128(kk)*np.float128(z[k+1]-z[k]) - np.float128(IntN0(z[k+1])-IntN0(z[k]))
            M_seg[k+1] = M_val
        Mf = np.array(M_seg[1:], dtype=float)
        seg_means.append(Mf.mean())
        seg_maxs.append(np.abs(Mf).max())
        g_end = z[-1]
        print(f"   段{seg+1}: γ到{g_end:.0f}——mean={Mf.mean():+.6f}——max|M|={np.abs(Mf).max():.4f}——末值={float(M_val):+.4f}")
    
    print("\n分块平均（每 200k——）:")
    for i, m in enumerate(seg_means):
        print(f"   段{i+1}: mean = {m:+.6f}")
    
    # 理论对比：log log γ
    print("\nlog log γ（各段末——）:")
    gammas_end = []
    for seg in range(NSEG):
        z = load_zeros(1, (seg+1)*SEG - 1)
        gammas_end.append(z[0])
    for i, g in enumerate(gammas_end):
        print(f"   段{i+1}: loglog(γ={g:.0f}) = {log(log(g)):.4f}")

if __name__ == "__main__":
    main()
