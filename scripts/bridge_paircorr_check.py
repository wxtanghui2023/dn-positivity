#!/usr/bin/env python3
"""
桥检验：对关联（BGST 型——）→ 间距补偿（δ 负相关——）→ a_j 交替
8/22 办法一被"间距补偿无条件证明"挡住
2026 BGST 给了无条件对关联——能否桥到间距补偿？

检验：
1. 数值确认 δ 补偿（ρ(δ_k,δ_{k+1})<0——条件概率——）
2. 对关联函数（短距排斥——）与 δ 补偿的联系
3. "局部密度守恒"：过密区间（δ<0——）后必补偿（δ>0——）——这对关联能解释吗？
"""
import numpy as np
from math import log, pi

def main():
    print("="*70)
    print("桥检验：对关联 → 间距补偿 → a_j 交替")
    print("="*70)
    
    # 加载零点
    zeros = np.load('/home/node/.openclaw/workspace/dn-project/data/zeros_odlyzko_100k.npy')
    z = zeros[:100000]
    print(f"零点数: {len(z)}——到 γ={z[-1]:.0f}")
    
    # 1. δ_k = Δγ_k - 1/N₀'(γ_k)
    dg = np.diff(z)
    Np = np.log(z[:-1]/(2*pi))/(2*pi)
    delta = dg - 1.0/Np
    
    # 2. δ 补偿确认
    print("\n1. δ 补偿（8/22 数值——重新确认——）:")
    rho = np.corrcoef(delta[:-1], delta[1:])[0,1]
    print(f"   ρ(δ_k, δ_k+1) = {rho:.4f}")
    # 条件概率
    neg = delta[:-1] < 0
    pos_next = delta[1:] > 0
    P_pos_given_neg = np.mean(pos_next[neg])
    print(f"   P(δ_next>0 | δ_k<0) = {P_pos_given_neg:.4f}")
    
    # 3. 对关联函数（短距——BGST 型——）
    print("\n2. 对关联（短距排斥——）:")
    # 归一化间距 δ̂ = Δγ·N₀'——对关联 = 间距分布 vs 泊松
    dg_norm = dg * Np  # 归一化间距（平均 1——）
    small = dg_norm < 0.5
    medium = (dg_norm >= 0.5) & (dg_norm < 1.5)
    print(f"   间距<0.5（短距——排斥区——）比例 = {np.mean(small):.4f}（泊松期望 0.39——）")
    print(f"   0.5≤间距<1.5 比例 = {np.mean(medium):.4f}（泊松期望 0.48——）")
    
    # 4. 关键桥检验：短距排斥与 δ 补偿的联系
    # 问：过密（δ_k<0——间距小——）后的补偿——是"局部守恒"（纯机制——）
    # 还是"全局统计"（对关联——）？——检验：补偿强度随"过密程度"变化？
    print("\n3. 补偿的分层结构（δ_k 越小——补偿越强？——）:")
    # 按 δ_k 分位数分层——看 P(δ_next>0) 和 E(δ_next)
    for q_label, lo, hi in [('δ_k<-0.5', -10, -0.5), ('-0.5<δ_k<0', -0.5, 0), ('0<δ_k<0.5', 0, 0.5), ('δ_k>0.5', 0.5, 10)]:
        mask = (delta[:-1] > lo) & (delta[:-1] < hi)
        if mask.sum() > 0:
            P = np.mean(delta[1:][mask] > 0)
            E_next = np.mean(delta[1:][mask])
            print(f"   {q_label}: P(next>0)={P:.4f}——E(δ_next)={E_next:+.4f}（n={mask.sum()}）")
    
    # 5. 间隔分析：补偿的"记忆长度"
    print("\n4. 补偿的记忆长度（δ_k 与 δ_{k+j} 的相关——）:")
    for j in [1, 2, 3, 5, 10]:
        c = np.corrcoef(delta[:-j], delta[j:])[0,1]
        print(f"   ρ(δ_k, δ_k+{j}) = {c:+.4f}")

if __name__ == "__main__":
    main()
