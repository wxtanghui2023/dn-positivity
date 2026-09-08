#!/usr/bin/env python3
"""
高空局部漂移检验（唐先生实验——）
数据：Odlyzko zeros3——第 10^12+1 到 10^12+10^4 零点（γ~2.6765×10^11——）
问题：高空窗口内 M 的局部增量——能否测到 log 漂移（a~0.04——）？

理论：若 M = a·log T + R(T)——
  每零点的 M 增量 ~ a·dlog = a·Δγ/γ ~ a·(2π/(γ log γ))·(1/γ)·?
  实际上 dM/dk（每零点——）= S̄_k·Δγ_k ~ 局部——a 的贡献 ~a·(Δγ/γ)——极小
  高空窗口内主要测 R 的振荡（非 a——）
"""
import numpy as np
from math import log, pi

def load_high_zeros():
    path = '/home/node/.openclaw/workspace/dn-project/zeros/zeros3_high.txt'
    vals = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('Values') or line.startswith('zero') or line.startswith('     1/2') or line.startswith('Zeros'):
                continue
            try:
                vals.append(float(line))
            except:
                pass
    base = 267653395647.0
    return np.array(vals) + base

def N0(t):
    return (t/(2*pi))*log(t/(2*pi)) - t/(2*pi) + 7/8

def main():
    print("="*70)
    print("高空局部漂移检验（zeros3——γ~2.6765e11——）")
    print("="*70)
    
    z = load_high_zeros()
    print(f"高空零点数: {len(z)}")
    print(f"γ 范围: {z[0]:.6f} 到 {z[-1]:.6f}")
    span = z[-1]-z[0]
    print(f"跨度: {span:.2f}——相对 {span/z[0]:.2e}")
    
    # 高空平均间距
    dg = np.diff(z)
    print(f"\n平均间距 = {dg.mean():.6f}（理论 2π/log(γ/2π) = {2*pi/log(z[0]/(2*pi)):.6f}——）")
    
    # S 在窗口内（用零点——N0 的——）
    # S(γ_k) = k_local - N0(γ_k)——但 k 是全局（10^12+k——）——S 是全局的
    # S(γ_n) = n - N0(γ_n)——n = 10^12 + i
    n_start = 10**12
    N0v = np.array([N0(t) for t in z])
    k_global = n_start + np.arange(1, len(z)+1)
    S_at_zero = k_global - N0v  # S(γ_n) 右极限
    
    # S 的局部统计
    print(f"\nS(γ) 在窗口的统计:")
    print(f"   mean = {S_at_zero.mean():+.4f}（低空 ~0.5——对比——）")
    print(f"   std = {S_at_zero.std():.4f}")
    
    # 窗口内 M 的增量（S 的积分——）
    # 区间平均 S（用 S(γ_k) 和 S(γ_{k+1})——）
    S_left = k_global[:-1] - N0v[:-1]  # γ_k 右
    # 区间 (γ_k, γ_{k+1}) 的 S 平均 ≈ k_global - N0(mid)
    mid = (z[:-1]+z[1:])/2
    N0mid = np.array([N0(t) for t in mid])
    Sbar = k_global[:-1] - N0mid
    M_inc = Sbar * dg
    M_local = np.cumsum(M_inc)
    
    print(f"\n窗口内 M 的局部增量（累积——）:")
    print(f"   max|ΔM_local| = {np.abs(M_local).max():.4f}")
    print(f"   末值 = {M_local[-1]:+.4f}")
    
    # 漂移率估计：ΔM/Δlog
    dlog_total = log(z[-1]) - log(z[0])
    drift = M_local[-1]/dlog_total
    print(f"\n局部漂移率 ΔM/Δlog γ = {drift:+.4f}")
    print(f"  （若 M=a·log——应 ~a≈0.04——但这是 10^4 零点的——含 R 振荡——）")
    
    # R 振荡的量级 vs a 的贡献
    print(f"\n分析：a 的贡献 vs R 的振荡:")
    print(f"   a·Δlog（全程——）= 0.04·{dlog_total:.6f} = {0.04*dlog_total:.6f}")
    print(f"   R 振荡（max|ΔM_local|——）= {np.abs(M_local).max():.4f}")
    print(f"   ⟹ R 振荡 >> a 贡献（{np.abs(M_local).max():.4f} vs {0.04*dlog_total:.6f}——）")
    print(f"   ⟹ 10^4 零点窗口测不到 a（R 主导——）")
    
    # 需要多长的窗口才能测 a？——Δlog ~ 1（e 倍——）——零点数 ~ e 倍高度/间距
    print(f"\n测 a 需要的窗口: Δlog~0.1 需零点 ~ {0.1*z[0]/(2*pi/log(z[0]/(2*pi))):.2e}")
    print(f"   （现有 10^4——远不够——）")

if __name__ == "__main__":
    main()
