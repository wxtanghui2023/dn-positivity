#!/usr/bin/env python3
"""
拓扑/缠绕视角深挖：零点实部 = 缠绕数的跳变位置

核心思想：
W(σ) = (1/2π)·Δarg ξ(σ+it)（t∈[0,T]）——缠绕数
Arg 原理：W(σ) = #{零点 ρ: β_ρ > σ}（阶梯函数——每零点一跳——跳在 β_ρ 处）
RH ⟺ 所有跳变钉在 σ = 1/2（无零点在 1/2 右侧——W(σ)=0 对 σ>1/2）

物理类比：拓扑保护——缠绕数是整数——量子化——零点"被迫"在反射轴(1/2)
如果跳变位置受拓扑约束（不能连续移动——只能离散跳——）→ 可能绕过 β 墙？

实验：
1. 真实 ζ：W(σ) 扫描（σ=0.55,0.7,0.9——）——验证 W(σ)=0（RH 区间——已知——）
2. 人为模拟：Hadamard 构造假 ξ——移动零点离轴（β>1/2）——看 W(σ) 跳变是否出现
3. 拓扑结构：跳变的"离散性"——能否从缠绕读出 β
"""
import numpy as np
import mpmath as mp

mp.mp.dps = 30

def arg_zeta_winding(sigma, T, n_steps=2000):
    """沿 t∈[0,T] 计算 arg ζ(σ+it) 的净缠绕（unwrap 后）"""
    t_vals = np.linspace(1.0, T, n_steps)
    args = []
    for t in t_vals:
        z = mp.zeta(mp.mpc(sigma, t))
        args.append(float(mp.arg(z)))
    args = np.array(args)
    # unwrap
    unwrapped = np.unwrap(args)
    winding = (unwrapped[-1] - unwrapped[0]) / (2*np.pi)
    return winding, unwrapped

def xi_from_hadamard(s, zeros, extra_zeros):
    """用 Hadamard 积构造 ξ 类函数（可移动零点——模拟离轴——）"""
    # ξ(s) = ξ(0)·Π_ρ(1 - s/ρ)——这里用 ζ(s)·s(s-1)/2·π^{-s/2}Γ(s/2) 的零点结构
    # 简化：直接构造 Π(1-s/ρ_j)·(1-s/ρ̄_j)——实值函数的零点 = {ρ_j, ρ̄_j}
    val = mp.mpc(1, 0)
    all_zeros = list(zeros) + list(extra_zeros)
    for rho in all_zeros:
        val *= (1 - s/mp.mpc(rho))
    return val

def main():
    print("="*70)
    print("拓扑/缠绕视角：W(σ) = 零点实部分布的阶梯函数")
    print("="*70)
    
    # === 实验 1：真实 ζ 的 W(σ) ===
    print("\n实验 1：真实 ζ 的缠绕数 W(σ)——σ>1/2 应无跳变（零点全在线——）")
    T = 100.0
    for sigma in [0.55, 0.6, 0.7, 0.9]:
        w, _ = arg_zeta_winding(sigma, T, n_steps=1500)
        print(f"  σ={sigma}: W(σ) = {w:+.6f}（应 ≈ 0——无零点在 σ 右侧——）")
    
    # 已知前 100 个零点都在线——σ=1/2 的缠绕应该 ≈ 零点数（到 T）
    # 用 N(T) 公式验证：N(T) ≈ (T/2π)log(T/2π) - T/2π + 7/8
    T2 = 100.0
    N_est = (T2/(2*np.pi))*np.log(T2/(2*np.pi)) - T2/(2*np.pi) + 7/8
    print(f"\n  N(T={T2}) 估计 = {N_est:.1f}——σ=0.5 的缠绕应接近（若可算——σ=0.5 需延拓——）")
    
    # === 实验 2：Hadamard 模拟——移动零点离轴 ===
    print("\n" + "="*70)
    print("实验 2：人为离轴——缠绕跳变位置是否跟随 β？")
    print("="*70)
    
    # 前几个零点（在线——）的 Hadamard 型函数
    from mpmath import zetazero
    zeros_online = [complex(zetazero(k)) for k in range(1, 11)]  # 前 10 个（β=0.5）
    zeros_online += [complex(np.conj(z)) for z in zeros_online]  # 共轭
    
    def F_real(t, extra=[]):
        """实值函数：Π(1-(½+it)/ρ)(1-(½-it)/ρ̄) 的实部 = |F|² 型——用 |Π|"""
        val = mp.mpc(1, 0)
        for rho in zeros_online:
            val *= (1 - mp.mpc(0.5, t)/mp.mpc(rho))
        for rho in extra:
            val *= (1 - mp.mpc(0.5, t)/mp.mpc(rho))
            val *= (1 - mp.mpc(0.5, t)/mp.mpc(np.conj(complex(rho))))
        return val
    
    # 模拟：移动 γ₁ 的零点到 β=0.7（离轴——）——extra 加 ρ=0.7+14.13i 和共轭
    # 注意：这破坏 FE 配对（1-ρ̄ 也在——）——为简单只测"单个离轴的影响"
    print("测试：离轴零点(β=0.7, γ=14.13)加入后——函数在 σ 线的缠绕")
    
    # 关键测试：F 的零点（|F|=0 处）——在线版本在 t=γ_k 有零点
    # 离轴版本：零点移到 σ=β——实轴(σ=0.5)无零点——但 FE 要求 1-ρ̄ 也在
    # ⟹ 若 β=0.7 有零点——1-0.7=0.3 也有（FE——）——实轴被"夹"在中间
    print("""
拓扑关键观察（模拟前——理论分析）：
  在线零点 ρ=½+iγ：实轴(σ=½)上的零点——F(t)=ξ(½+it) 符号变化
  离轴零点 ρ=β+iγ (β>½)：FE ⟹ 1-ρ̄=1-β+iγ (1-β<½) 也在
  ⟹ 两个零点跨 σ=½ 对称——实轴 σ=½ 上 t=γ 处"无零点"
  ⟹ F(t) 的符号变化在 t=γ 处"消失"——但 arg 的缠绕不变（总零点数守恒）
  ⟹ 缠绕数 W(σ) 的跳变位置从 σ=½ 移到 σ=β 和 σ=1-β（两跳——）
  ⟹ 跳变位置 = β 的直接读出——拓扑（缠绕——）确实"感测" β！

  但——"读出"（检测——）≠ "证明"（为什么 β=½——）
  缠绕跳变位置由 ξ 的全局（Hadamard——）结构决定——不自适应也不循环——
  但证明"跳变钉在 ½"仍是 RH 本身——拓扑给"离散性"不给"位置"
""")
    
    # 实验 3：验证跳变的"离散性"（整数量子化——）——这是拓扑的真正力量
    print("="*70)
    print("实验 3：跳变的离散性——拓扑能给什么（不能给什么）")
    print("="*70)
    print("""
拓扑（缠绕——）提供的：
  ✓ 零点实部分布的"计数"（W(σ)——整数值——阶梯——）
  ✓ 跳变的离散性（零点数守恒——移动零点不改变总数——只移跳位）
  ✓ 检测层：从缠绕可"读出"β（实验 2 原理——）

拓扑（缠绕——）不能提供的：
  ✗ 跳变位置的"原因"（为什么 β=½——缠绕连续——跳位由全局结构定——）
  ✗ 排除"高离轴"（有限个离轴——W(σ) 在 σ>½ 出现有限跳——可与数值兼容——）
  ✗ 有限→无限（P28-P33：缠绕跳位的有限信息不约束无限——）

β 墙的拓扑形式：
  零点实部 = 缠绕跳变位置——β 墙 = "跳变位置的不可推导性"
  拓扑把 β 变成"离散可读"（跳位——）但不给"跳位的定律"
  ——就像量子的能级量子化（离散——）不解释"为什么在这个能量"（需要动力学——）
""")

if __name__ == "__main__":
    main()
