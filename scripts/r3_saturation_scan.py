#!/usr/bin/env python3
"""
R3 考古 v3——D(a) 全-a 结构与饱和泛函扫描（唐先生框架——聚焦）

D(a) = S_proj(γ_ρ)(a) − W(a)/2 ≥ 0（变分定理——逐点）
成功标准：找到 zero-blind 全-a 约束比逐点 ≥ 强（L[D]=0 型饱和——）

注意：W(a)/2 = 在线参考（Weil 素数侧——zero-blind——）
S_proj(γ_ρ) = 实际零点虚部投影和（γ 层——）
RH ⟺ D ≡ 0（所有 a——）

实验：
1. 在线自洽：D(a) = 0（机器精度——真实零点在线——）
2. 模拟离轴：D'(a) 全 a 形状（合法四重奏微扰——）
3. 泛函扫描：∫D'(a)w(a)da 是否对某些 w 恒零（配置无关——）
"""
import numpy as np
import mpmath as mp
from mpmath import zetazero, log

mp.mp.dps = 20

def S_proj(gammas, a):
    g = np.array(gammas, dtype=float)
    return np.sum(1.0/(a*a + g*g)**2)

def main():
    print("="*70)
    print("R3 考古 v3：D(a) 结构与饱和泛函扫描")
    print("="*70)
    
    # 真实零点（用 Odlyzko 数据——快——）
    zdata = np.load('/home/node/.openclaw/workspace/dn-project/data/zeros_odlyzko_100k.npy')
    N = 300
    gammas = zdata[:N]
    print(f"真实零点: 前 {N}（γ 到 {gammas[-1]:.1f}）")
    
    # 注意：数值上真实零点在线——所以"实际配置"= 在线——S_proj(实际) 需要模拟离轴才有 D>0
    # 但真实 ζ 的在线性是数值事实——变分定理的 D ≥ 0 对"合法离轴 ξ'"——我们无法直接数值构造
    # 因此：用"局部微扰"近似离轴配置（8/31 方法——注意可能非法——但看形状——）
    
    a_grid = np.logspace(-0.5, 1.5, 40)
    
    # 参考：在线 S_proj（= W/2——8/31 已验 Weil 装配——）
    S_ref = np.array([S_proj(gammas, a) for a in a_grid])
    
    # 模拟离轴配置（微扰——移动一个零点的虚部——近似——）
    configs = {
        "γ₁ +0.1": np.concatenate([gammas[1:], [gammas[0]+0.1]]),
        "γ₁ +0.5": np.concatenate([gammas[1:], [gammas[0]+0.5]]),
        "γ₁ +1.0": np.concatenate([gammas[1:], [gammas[0]+1.0]]),
        "γ₁,γ₂ 各 +0.3": np.concatenate([gammas[2:], [gammas[0]+0.3, gammas[1]+0.3]]),
    }
    
    print("\n1. D'(a) = S_proj(扰动) − S_proj(在线) 的全 a 形状:")
    D_curves = {}
    for name, gm in configs.items():
        S_mod = np.array([S_proj(gm, a) for a in a_grid])
        D = S_mod - S_ref
        D_curves[name] = D
        # 形状特征
        D_norm = D / np.max(D) if np.max(D) > 0 else D
        # 单峰性/位置
        peak_idx = np.argmax(D)
        print(f"  {name}: D max = {np.max(D):.4e} @a={a_grid[peak_idx]:.2f}——D(小a)={D[1]:.2e}——D(大a)={D[-1]:.2e}")
    
    # 2. 泛函扫描：找 w 使 ∫D'(a)w(a)da = 0（对所有扰动——）
    print("\n2. 饱和泛函扫描（找 L[D] = 0 型——）:")
    # 候选 w：a^k（幂——）——e^{-ca}——1/(1+a²)——等
    # 对每个扰动算 L_k = ∫D(a)·a^k da（梯形——）
    da = np.diff(a_grid)
    a_mid = (a_grid[:-1] + a_grid[1:])/2
    print(f"{'泛函 w':>14}", end="")
    for name in D_curves:
        print(f" {'L['+name+']':>16}", end="")
    print()
    for k in [-3, -2, -1, 0, 1, 2]:
        row = f"a^{k:+d}"
        for name, D in D_curves.items():
            D_mid = (D[:-1] + D[1:])/2
            L = np.sum(D_mid * a_mid**k * da)
            print(f" {row:>14} {L:>16.3e}", end="")
        print()
    
    # 3. 归一化形状比较：D'(a)/D'(a_max) 是否配置无关（普适形状——）？
    print("\n3. D' 归一化形状（如果普适——有结构——）:")
    for name, D in D_curves.items():
        if np.max(D) > 0:
            peak_idx = np.argmax(D)
            # 半峰宽
            half = np.max(D)/2
            above = D > half
            if np.any(above):
                idxs = np.where(above)[0]
                width = a_grid[idxs[-1]] - a_grid[idxs[0]]
                print(f"  {name}: 峰位 a={a_grid[peak_idx]:.2f}——半峰宽 Δa={width:.2f}")

if __name__ == "__main__":
    main()
