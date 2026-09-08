#!/usr/bin/env python3
"""
M(T) 轨迹结构——为什么 O(1)？
M(T) = Σ_{γ≤T}(T-γ) - ∫N0——数值 O(1) 到 γ~1.3e5
问题：
1. M(t) 作为 t 的函数——振荡模式（周期——幅度——）
2. S(t) = M'(t)——S 的符号结构（为什么净面积 O(1)——）
3. M 的主要频率（与 log p 的关系？——素数相位？）
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

def N0_arr(t):
    t = np.maximum(t, 1.0)
    return (t/(2*pi))*np.log(t/(2*pi)) - t/(2*pi) + 7/8

def main():
    print("="*70)
    print("M(T) 轨迹结构分析")
    print("="*70)
    
    K = 200000
    z = load_zeros(K)
    
    # M 递推（float128——）
    M_vals = np.zeros(K, dtype=np.float128)
    M_val = np.float128(0)
    for k in range(K-1):
        dg_k = z[k+1] - z[k]
        intN = np.float128((N0_arr(z[k]) + N0_arr(z[k+1]))/2 * dg_k)
        M_val += np.float128(k+1)*np.float128(dg_k) - intN
        M_vals[k+1] = M_val
    
    Mf = np.array(M_vals, dtype=float)
    
    # 1. M 的统计
    print("\n1. M(γ_k) 统计:")
    print(f"   max M = {Mf.max():+.4f}——min M = {Mf.min():+.4f}——max|M| = {np.abs(Mf).max():.4f}")
    
    # 2. 局部振荡（每 1000 个零点的 M 轨迹——）
    print("\n2. M 轨迹采样（每 5000 零点——）:")
    for k in range(0, K, 5000):
        print(f"   k={k:>7}（γ={z[k]:7.0f}）: M={Mf[k]:+.4f}", end='')
        if k % 25000 == 0: print()
    print()
    
    # 3. S(t) 的结构（M 的导数——）——相邻 M 差
    print("\n3. S(γ_k) = M 的增量率——M 的导数信息")
    # M'(t) = S(t)——在 γ_k 处 S 跳跃——M(γ_{k+1})−M(γ_k) = ∫S over (γ_k,γ_{k+1})
    dM = np.diff(Mf)  # 每个区间的 ∫S
    print(f"   dM 统计: mean={dM.mean():+.6f}——std={dM.std():.6f}")
    print(f"   （如果 S 强烈振荡——dM 应该正负交替——）")
    
    # 4. dM 的符号模式（S 的净面积交替——）
    signs = np.sign(dM)
    flips = np.sum(signs[1:] != signs[:-1])
    print(f"\n4. dM 符号翻转次数 = {flips}/{len(dM)}——{flips/len(dM)*100:.1f}%（随机 ~50%——）")
    
    # 5. M 的累计绝对变化 vs 净变化
    total_var = np.sum(np.abs(dM))
    print(f"\n5. M 的总变差 = {total_var:.2f}——但净变化 O(1)——")
    print(f"   ⟹ 强相消：总变差 {total_var:.0f} vs 净 O(1)——比率 {total_var:.0f}")
    
    # 6. 区间平均的 dM（看趋势——）
    print("\n6. dM 的区间平均（每 10000 区间——）:")
    for i in range(0, len(dM), 10000):
        seg = dM[i:i+10000]
        print(f"   k={i:>7}-{i+10000}: mean(dM)={seg.mean():+.6f}——sum={seg.sum():+.4f}")

if __name__ == "__main__":
    main()
