#!/usr/bin/env python3
"""
SSH 模板对照：为什么 SSH 能传输（体-边对应——）而我们 P28-P33 不能？

SSH 成功的三要素：
1. 体有能隙：|d(k)| ≥ gap > 0（对所有 k——Bloch——）
2. 指标常数：W = deg(d̂) 不随链长变（拓扑稳定——）
3. 边缘态在隙中：E=0 远离连续谱——稳定

我们的 P27-P33：
1. 体能隙：??（素数侧哪个量恒正？——候选检查——）
2. 指标：n_-(K_N) = N（增长——非恒定——）
3. 负方向 λ→0⁻（堆积边缘——无能隙——不稳定）

关键猜想：如果 ζ 的"体"（素数侧——）有某个恒正的量（能隙——）
——像 SSH 的 |d(k)| ≥ gap——则零点（边缘态——）被保护在 σ=½

本实验：检查"算术能隙"候选——哪个量可能恒正且有下界？
候选：
A. Re ζ'(ρ)——前 N 个零点（我们数值发现 > 0——最小 +0.0136@γ=169.9——）
B. |ζ'(ρ)|——零点导数的模
C. Re[ζ(ρ−1)/ζ'(ρ)] 的符号（运动学 c(γ)>0——）
D. P_γ(δ) 的逐轨道正性（δ²M₂/(2U²D₊D₋)——）
E. 1/|ζ'(ρ)|——反导数——分布
"""
import numpy as np
import mpmath as mp
from mpmath import zetazero

mp.mp.dps = 20

def main():
    print("="*70)
    print("算术'能隙'候选检查——哪个量恒正且有下界（像 SSH 的 |d(k)|≥gap）？")
    print("="*70)
    
    N = 200
    print(f"\n检查前 {N} 个零点（γ_1={float(zetazero(1).imag):.2f}——γ_{N}={float(zetazero(N).imag):.1f}）")
    
    # 候选 A：Re ζ'(ρ)
    print("\n【候选 A：Re ζ'(ρ)】——零点的导数实部")
    re_zp_list = []
    min_val = 1e9
    min_idx = -1
    for k in range(1, N+1):
        rho = zetazero(k)
        zp = mp.zeta(rho, derivative=1)
        re_zp = float(mp.re(zp))
        re_zp_list.append(re_zp)
        if re_zp < min_val:
            min_val = re_zp
            min_idx = k
    re_zp_arr = np.array(re_zp_list)
    print(f"  min Re ζ'(ρ) = {min_val:.6f} @ γ_{min_idx}={float(zetazero(min_idx).imag):.1f}")
    print(f"  全部 > 0: {np.all(re_zp_arr > 0)}——分布: [{re_zp_arr.min():.4f}, {re_zp_arr.max():.2f}]")
    
    # 候选 B：|ζ'(ρ)|
    print("\n【候选 B：|ζ'(ρ)|】")
    abs_zp_list = []
    for k in range(1, N+1):
        rho = zetazero(k)
        zp = mp.zeta(rho, derivative=1)
        abs_zp_list.append(float(mp.fabs(zp)))
    abs_zp_arr = np.array(abs_zp_list)
    print(f"  min |ζ'(ρ)| = {abs_zp_arr.min():.6f}——max = {abs_zp_arr.max():.2f}")
    print(f"  与 γ 关系：|ζ'(ρ)| ~ γ^{0.5}?——检查 log-log 斜率")
    gammas = np.array([float(zetazero(k).imag) for k in range(1, N+1)])
    slope = np.polyfit(np.log(gammas[50:]), np.log(abs_zp_arr[50:]), 1)[0]
    print(f"  log|ζ'| vs log γ 斜率 = {slope:.3f}（~0.5 = 平均——但涨落大——）")
    
    # 候选 E：1/|ζ'(ρ)|
    print("\n【候选 E：1/|ζ'(ρ)|】——反导数（在 BNBD/对关联里出现——）")
    inv_arr = 1.0/abs_zp_arr
    print(f"  min 1/|ζ'| = {inv_arr.min():.6f}——max = {inv_arr.max():.4f}")
    print(f"  Σ1/|ζ'(ρ)|² = {np.sum(inv_arr**2):.4f}（部分和——收敛性？——）")
    for frac in [0.25, 0.5, 0.75, 1.0]:
        m = int(N*frac)
        print(f"    前 {m} 个: {np.sum(inv_arr[:m]**2):.4f}")
    
    # 候选 C：运动学系数 c(γ) = -Re[ζ(ρ-1)/ζ'(ρ)]（我们 9/5 发现 > 0——）
    print("\n【候选 C：c(γ) = -Re[ζ(ρ-1)/ζ'(ρ)]】——运动学——零点向 1/2 移动的速度")
    c_list = []
    for k in range(1, min(N, 100)+1):
        rho = zetazero(k)
        z_prev = mp.zeta(rho - 1)  # ζ(ρ-1)
        zp = mp.zeta(rho, derivative=1)
        c_val = -float(mp.re(z_prev/zp))
        c_list.append(c_val)
    c_arr = np.array(c_list)
    print(f"  前 {len(c_arr)} 个: min c(γ) = {c_arr.min():.4f}——全部 > 0: {np.all(c_arr > 0)}")
    
    # SSH 对照总结
    print("\n" + "="*70)
    print("SSH 对照分析")
    print("="*70)
    print("""
SSH 能隙：|d(k)| ≥ gap > 0——从 Bloch 哈密顿直接算——恒正有界
→ 边缘态 E=0 在隙中——拓扑保护——链长无关——传输到无限

ζ 侧候选（本实验）：
  A. Re ζ'(ρ) > 0（数值——200 个全正——min +0.0136——但随 γ 涨落——无证明恒正）
  B. |ζ'(ρ)|（无下界——涨落大——分布随 γ 增——）
  C. c(γ) = -Re[ζ(ρ-1)/ζ'(ρ)] > 0（数值——前 100 全正——运动学——）
  
⚠️ 关键区别：SSH 的 gap 是"体量"（对所有 k 的 Bloch 态——连续——）
   ζ 的候选（Re ζ' 等）是"边缘量"（只在零点——离散——）
   ——像用边缘态本身去证明边缘态的稳定性——循环风险
  
真正需要的"算术体能隙"：一个从素数侧算出的量（不含零点——）
  恒正 + 有下界——类似 |d(k)|——目前未找到（候选全在零点上——）
""")

if __name__ == "__main__":
    main()
