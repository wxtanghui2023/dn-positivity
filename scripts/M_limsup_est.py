#!/usr/bin/env python3
"""
M(T)/log T 的 limsup 估计——改进显式界 A1=0.059 的可能
如果数值 limsup < 0.059——显式界可改进（真实的数学贡献——）
Brent-Platt (3): |S1(T) - c| <= A0 + A1 log T——A1 = 0.059（[12] Thm 2.2——）
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
    print("M(T)/log T 的 limsup 估计")
    print("="*70)
    
    # 用 2M 数据——分块算 M 的最大值（相对 log——）
    SEG = 200000
    NSEG = 10
    M_val = np.float128(0.0)
    print("\n各段 max|M| 与 log γ:")
    max_ratios = []
    for seg in range(NSEG):
        z = load_zeros(SEG, seg*SEG)
        seg_max = 0
        for k in range(SEG-1):
            kk = k + 1 + seg*SEG
            M_val += np.float128(kk)*np.float128(z[k+1]-z[k]) - np.float128(IntN0(z[k+1])-IntN0(z[k]))
            mv = abs(float(M_val))
            if mv > seg_max: seg_max = mv
        g = z[-1]
        # max|M| 从 0 到该段末——但 seg_max 是该段内的——需要全程 max
        ratio = seg_max / log(g)
        max_ratios.append(ratio)
        print(f"   段{seg+1}: γ={g:.0f}——log γ={log(g):.2f}——段内 max|M|={seg_max:.4f}——比 {ratio:.4f}")
    
    # 全程 max|M| 的界（各段 max 的最大——）
    print(f"\n各段 max|M|/log 的最大 = {max(max_ratios):.4f}")
    print(f"（对比显式 A1 = 0.059——如果数值 < 0.059——改进可能——）")
    
    # 注意：段内 max 不是全程 max——需要跨段累积
    # 重新算：全程 max（一次递推——但存每段 max——已在上面——seg_max 是段内相对 M_val 的——）
    # M_val 跨段延续——seg_max 是该段内 |M| 相对全局的最大增量——但起点 M_val 可能不是 0
    print(f"\n⚠️ 注意：段内 max 是相对段起点的——全程 max 需要看 M_val 的绝对范围")
    print(f"   用分块平均数据（前面——）: max|M| 全程 ~1.9（段 9——）")

if __name__ == "__main__":
    main()
