#!/usr/bin/env python3
"""
S̄ 波包结构分析——M 有界性的直接来源
M = Σ S̄_k·Δγ——S̄ 波包（正负交替——）——每波包净面积
如果波包面积交替/有界——M 徘徊——O(1)

问题：
1. S̄ 的符号段（波包——）长度分布
2. 每波包的净面积——是否交替（正负——）？
3. 波包面积的部分和（=M 的分段——）行为
"""
import numpy as np
from math import log, pi

def load_zeros(n):
    path = '/home/node/.openclaw/workspace/dn-project/zeros/zeros6'
    z = np.zeros(n)
    with open(path) as f:
        for i in range(n):
            z[i] = float(f.readline())
    return z

def main():
    print("="*70)
    print("S̄ 波包结构分析")
    print("="*70)
    
    K = 200000
    z = load_zeros(K)
    mid = (z[:-1]+z[1:])/2
    dg = np.diff(z[:K])
    
    def IntN0(t):
        if t <= 1: return 0.0
        return t*t/(4*pi)*log(t/(2*pi)) - 3*t*t/(8*pi) + 7*t/8
    
    kk = np.arange(1, K)
    IntN = np.array([IntN0(t) for t in z[:K]])
    Sbar = kk - (IntN[1:] - IntN[:-1])/dg
    
    # M 增量
    M_inc = Sbar * dg
    
    # 1. S̄ 的符号段（波包——）
    print("\n1. S̄ 符号段（波包）统计:")
    signs = np.sign(Sbar)
    # 找符号变化点
    flips = np.where(signs[:-1] != signs[1:])[0] + 1
    segments = np.diff(np.concatenate([[0], flips, [len(Sbar)]]))
    seg_signs = signs[flips[0] if len(flips)>0 else 0:0]  # 每段的符号
    # 简化——算每段长度
    print(f"   波包数 = {len(flips)+1}——平均长度 = {len(Sbar)/(len(flips)+1):.1f} 零点")
    lens = np.diff(np.concatenate([[0], flips, [len(Sbar)]]))
    print(f"   长度分布: min={lens.min()}——max={lens.max()}——中位={np.median(lens):.0f}")
    # 长度直方图
    hist, edges = np.histogram(lens, bins=20)
    print(f"   长度直方图: {hist}")
    
    # 2. 每波包的净面积（M 增量累积——）
    print("\n2. 波包净面积:")
    bounds = np.concatenate([[0], flips, [len(Sbar)]])
    areas = []
    for i in range(len(bounds)-1):
        a = M_inc[bounds[i]:bounds[i+1]].sum()
        areas.append(a)
    areas = np.array(areas)
    print(f"   波包面积: mean={areas.mean():+.4f}——std={areas.std():.4f}——max|={np.abs(areas).max():.4f}")
    print(f"   前 20 个波包面积: {np.array2string(areas[:20], precision=3)}")
    
    # 3. 波包面积的自相关（交替？——）
    if len(areas) > 5:
        corr1 = np.corrcoef(areas[:-1], areas[1:])[0,1] if len(areas) > 2 else 0
        print(f"\n3. 波包面积自相关 ρ(1) = {corr1:+.4f}（负=交替——）")
        # 符号模式
        sa = np.sign(areas)
        if len(sa) > 2:
            same = np.sum(sa[1:] == sa[:-1])
            print(f"   相邻同号比例 = {same/(len(sa)-1):.3f}（0.5=随机——<0.5=交替——）")
    
    # 4. 波包面积的部分和（=M 的分段——）
    print("\n4. 波包面积累积（M 的粗轨迹——）:")
    cum_areas = np.cumsum(areas)
    print(f"   max|累积| = {np.abs(cum_areas).max():.4f}——末值 = {cum_areas[-1]:+.4f}")
    # 与真实 M 对比
    M_cum = np.cumsum(M_inc)
    print(f"   真实 M: max|M| = {np.abs(M_cum).max():.4f}")

if __name__ == "__main__":
    main()
