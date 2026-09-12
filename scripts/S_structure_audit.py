#!/usr/bin/env python3
"""
S(t) 一次结构审计（唐先生授权——2026-09-08 21:25）
命题：S(t) = 结构项（低素数几乎周期——）+ 不可约残差
问题：残差是否受"新刚性"约束（与零点结构 δ 耦合——）还是纯已知噪声？

方法：S(mid_k) = N(mid_k) − θ(mid_k)/π − 1（非零点——零点数据快算）
     δ_k = Δγ_k − 1/N₀'(γ_k)（间距偏差——零点结构——）
分解：S(mid) = Σ_{p≤P} a_p sin(mid·log p)（几乎周期——）+ 残差
测：残差与 δ 的相关——残差自相关——残差漂移
"""
import numpy as np
from math import log, pi

# θ(t) = Im log Γ(¼ + it/2) − (t/2)log π——Stirling
def theta(t):
    if t < 10: t = 10.0
    z = 0.25 + 0.5j*t
    # Stirling log Γ(z) ≈ (z−½)log z − z + ½log(2π) + 1/(12z)
    lz = np.log(z)
    lg = (z-0.5)*lz - z + 0.5*np.log(2*np.pi) + 1.0/(12*z)
    return float(np.imag(lg)) - 0.5*t*np.log(pi)

def N0(t):
    """光滑零点计数 ~ θ(t)/π + 1"""
    return theta(t)/pi + 1

def main():
    print("="*70)
    print("S(t) 结构审计：结构项 + 残差——残差与 δ 的耦合")
    print("="*70)
    
    z = np.load('data/zeros_odlyzko_100k.npy')
    print(f"零点数: {len(z)}——γ范围: {z[0]:.1f} 到 {z[-1]:.1f}")
    
    # 取前 20000 零点（快——）
    z = z[:20000]
    K = len(z) - 1
    gamma = z[:K]
    dg = np.diff(z)  # Δγ_k
    mid = (z[:-1] + z[1:])/2
    
    # S(mid_k) = N(mid_k) − θ(mid_k)/π − 1
    print("\n1. 算 S(mid_k)——(N 二分计数——)")
    S_mid = np.zeros(K)
    for k in range(K):
        t = mid[k]
        # N(t) = #{γ_j ≤ t}——零点在 mid 两侧——k+1 个 ≤ γ_{k+1}？——二分
        cnt = np.searchsorted(z, t)  # 零点 ≤ t 的数
        S_mid[k] = cnt - theta(t)/pi - 1
    print(f"   S(mid) 统计: mean={S_mid.mean():.4f}——std={S_mid.std():.4f}——max|S|={np.max(np.abs(S_mid)):.4f}")
    
    # δ_k = Δγ_k − 1/N₀'(γ_k)——N₀'(t) ≈ (1/2π)log(t/2π)
    N0p = np.log(mid/(2*pi))/(2*pi)
    delta = dg - 1.0/N0p
    print(f"   δ 统计: mean={delta.mean():.6f}——std={delta.std():.4f}")
    
    # 2. 几乎周期拟合（低素数——）
    print("\n2. 几乎周期结构项（p≤P 拟合——）:")
    # 已知系数 ~ 1/(p^{1/2}log p)——直接理论构造（不拟合——）
    ps = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]
    def ap_series(t, plist):
        s = 0.0
        for p in plist:
            s -= (1.0/pi) * np.sin(t*np.log(p)) / (np.sqrt(p)*np.log(p))
        return s
    S_struct = np.array([ap_series(t, ps) for t in mid])
    corr = np.corrcoef(S_mid, S_struct)[0,1]
    print(f"   结构项（p≤53——）与 S(mid) 相关: {corr:.4f}")
    
    # 3. 残差
    res = S_mid - S_struct
    print(f"   残差: std={res.std():.4f}——max|res|={np.max(np.abs(res)):.4f}")
    
    # 4. 关键审计：残差与 δ 的相关
    print("\n3. ⭐ 残差与零点结构 δ 的耦合（文献盲点测试——）:")
    c_res_delta = np.corrcoef(res, delta)[0,1]
    print(f"   corr(残差, δ) = {c_res_delta:+.4f}")
    # 残差与 δ 的滞后相关
    for lag in [1, 2, 3]:
        c = np.corrcoef(res[:-lag], delta[lag:])[0,1]
        print(f"   corr(残差_k, δ_{k+lag}) = {c:+.4f}")
    
    # 5. 残差的自相关（是否纯噪声——）
    print("\n4. 残差自相关:")
    for lag in [1, 2, 5, 10, 20]:
        c = np.corrcoef(res[:-lag], res[lag:])[0,1]
        print(f"   ρ({lag}) = {c:+.4f}")
    
    # 6. 残差的累积（漂移——）
    cum = np.cumsum(res)
    print(f"\n5. 残差累积: max|Σres| = {np.max(np.abs(cum)):.3f}（随机游走预期 ~std·√K = {res.std()*np.sqrt(K):.1f}——）")
    # 分段
    seg = 2000
    seg_max = [np.max(np.abs(cum[i:i+seg])) for i in range(0, K, seg)]
    print(f"   分段 max|Σres|（每 {seg}——）: {['%.2f'%s for s in seg_max[:8]]}")

if __name__ == "__main__":
    main()
