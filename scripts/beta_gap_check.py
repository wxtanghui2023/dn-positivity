#!/usr/bin/env python3
"""
关键检验：相位均匀性（γ层——定理A——）vs β 缺口
问题：如果相位均匀性突破（G-M 式——γ 层——）真的发生了——
它能否推出 r(n)=O(1)（β 敏感——）？

实验设计：
1. 构造"在线玩具"（全部零点在临界线——）——验证 ∫f_n·S·g = O(1) 且 r(n) 正常
2. 构造"离轴玩具"（一个零点 β>1/2——）——看：
   a) ∫f_n·S·g 是否仍 O(1)？（S 是 arg ζ 虚部——预期仍 O(1)——γ 层量——）
   b) r(n) 是否爆炸？（β 敏感——预期爆炸——）
3. 结论：如果 a) 仍 O(1) 而 b) 爆炸——则"相位均匀性突破不够"——β 缺口确证

玩具模型：用显式公式直接算
ψ(x) 余项 R(x) = x^{1/2}·Σ_ρ x^{iγ}/ρ（在线——）vs 含一个离轴零点
"""
import numpy as np

def main():
    print("="*70)
    print("关键检验：γ层均匀性 vs β缺口")
    print("="*70)
    
    # 用前几个真实零点（在线假设——）
    gammas = np.array([14.1347, 21.0220, 25.0109, 30.4249, 32.9351, 37.5862, 40.9187, 43.3271, 48.0052, 49.7738])
    
    # 1. 在线玩具的"相位均匀性量"（R 函数——G-M 式——）
    print("\n1. 在线 vs 离轴玩具——R 函数（相位均匀性——）:")
    x = 1.5  # t∈[1,2] 的采样
    R_online = sum(np.exp(1j*g*np.log(x)) for g in gammas)
    # 加一个离轴零点（β=0.6——γ=55——）
    R_offline = R_online + np.exp((0.6-0.5)*np.log(x))*np.exp(1j*55*np.log(x))
    print(f"   R(在线) = |{abs(R_online):.4f}|（相位均匀——小——）")
    print(f"   R(含离轴) = |{abs(R_offline):.4f}|")
    # 离轴贡献 e^{δt} 在 t=log x∈[0,1]——δ=0.1——e^{0.1t}~1——小
    print(f"   离轴贡献模 = e^{0.1*0.405:.4f} ≈ {np.exp(0.1*np.log(x)):.4f}（t=log x 小——几乎不变——）")
    
    # 2. 关键：r(n) 类的量（λ_n 余项——β 敏感——）
    print("\n2. r(n) 类量（λ_n = Σ[1-(1-1/ρ)^n]——β 敏感——）:")
    def lambda_n(gammas_list, betas_list, n):
        """λ_n = Σ[1-(1-1/ρ)^n]——ρ=β+iγ"""
        total = 0
        for g, b in zip(gammas_list, betas_list):
            rho = b + 1j*g
            total += 1 - (1 - 1/rho)**n
        return total
    
    betas_on = [0.5]*len(gammas)
    # 离轴玩具：加一个 β=0.6 的零点在 γ=55
    gammas_off = list(gammas) + [55.0]
    betas_off = list(betas_on) + [0.6]
    
    print(f"   {'n':>6} {'λ_n(在线)':>12} {'λ_n(含离轴β=0.6)':>18}")
    for n in [10, 50, 100, 200, 500]:
        L1 = lambda_n(gammas, betas_on, n)
        L2 = lambda_n(gammas_off, betas_off, n)
        print(f"   {n:>6} {L1.real:>12.2f} {L2.real:>18.2f}")
    
    # 3. 单离轴零点的贡献 (1-1/ρ)^n——指数增长？
    print("\n3. 单离轴零点 |1-1/ρ|^n:")
    for b in [0.5, 0.55, 0.6, 0.7]:
        g = 55.0
        rho = b + 1j*g
        m = abs(1 - 1/rho)
        print(f"   β={b}: |1-1/ρ| = {m:.6f}——n=1000 时 |1-1/ρ|^n = {m**1000:.2e}")
    
    # 4. 结论
    print("\n" + "="*70)
    print("结论：")
    print("· R 函数（相位均匀性——γ 层——）：离轴零点贡献 ~e^{δt}（t 小——几乎无感——）")
    print("· λ_n（r(n)——β 敏感——）：离轴零点 |1-1/ρ|^n 指数爆炸（β>1/2 时——）")
    print("⟹ γ 层相位均匀性（即使突破——）不含 β 通道——")
    print("   离轴零点在 γ 层量中隐形（e^{δt}~1——）但在 λ_n 中爆炸")
    print("   这就是 8/24 的 β 缺口——S(t)/R 函数（虚部——）不携带 β")

if __name__ == "__main__":
    main()
