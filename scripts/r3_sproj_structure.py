#!/usr/bin/env python3
"""
R3 考古——S_proj(a) 全 a 结构数值分析
S_proj(a) = Σ_γ 1/(a²+γ²)²（在线——零点虚部——）
W(a)/2 = Weil 素数侧（无条件——全 a 可算——）

检查：
1. S_proj(a) 单调性/凸性/完全单调性（a 函数——）
2. 在线 vs 离轴配置的 S_proj(a) 全 a 函数形状（形状指纹——）
3. 完全单调性（Bernstein）检验
"""
import numpy as np
import mpmath as mp

mp.mp.dps = 15

def S_proj_direct(gammas, a):
    return np.sum(1.0/(a*a + gammas**2)**2)

def main():
    print("="*65)
    print("R3 考古：S_proj(a) 全 a 结构")
    print("="*65)

    from mpmath import zetazero
    N = 500
    gammas = np.array([float(zetazero(k).imag) for k in range(1, N+1)])
    print(f"前 {N} 零点（γ 到 {gammas[-1]:.1f}）")

    # 1. 完全单调性检验：(-1)^k S^(k)(a) ≥ 0？
    print("\n1. 完全单调性（Bernstein——数值导数——）:")
    # f(a) = 1/(a²+γ²)² 逐项导数
    # f' = -4a/(a²+γ²)³
    # f'' = -4/(a²+γ²)³ + 12a²/(a²+γ²)⁴
    # f''' = 48a/(a²+γ²)⁴ - 96a³/(a²+γ²)⁵
    # f'''' = 48/(a²+γ²)⁴ - 384a²/(a²+γ²)⁵ + 480a⁴/(a²+γ²)⁶
    for a in [0.5, 1.0, 2.0, 3.0, 5.0, 10.0]:
        g2 = gammas**2
        d = a*a + g2
        S1 = np.sum(-4*a/d**3)
        S2 = np.sum(-4/d**3 + 12*a*a/d**4)
        S3 = np.sum(48*a/d**4 - 96*a**3/d**5)
        S4 = np.sum(48/d**4 - 384*a*a/d**5 + 480*a**4/d**6)
        # Bernstein: (-1)^k S^(k) ≥ 0——S 本身 > 0（k=0——）
        b0 = S_proj_direct(gammas, a) > 0
        b1 = (-S1) >= 0
        b2 = (S2) >= 0
        b3 = (-S3) >= 0
        b4 = (S4) >= 0
        print(f"  a={a:>5.1f}: S={S_proj_direct(gammas,a):.4e}——(-S')={-S1:+.3e}——S''={S2:+.3e}——(-S''')={-S3:+.3e}——S''''={S4:+.3e}")
        print(f"    Bernstein 符号: {b0}{b1}{b2}{b3}{b4}（全 T = 完全单调——）")

    # 2. 在线 vs 模拟离轴配置——S_proj(a) 全 a 形状指纹
    print("\n2. 在线 vs 扰动配置——S_proj(a) 全 a 相对形状:")
    a_grid = np.logspace(-0.3, 1.5, 25)
    configs = [
        ("在线（对照）", gammas),
        ("γ₁ 移 +0.5", np.concatenate([gammas[1:], [gammas[0]+0.5]])),
        ("γ₁ 移 +2.0", np.concatenate([gammas[1:], [gammas[0]+2.0]])),
        ("γ₁ 移到 γ₂+0.01", np.concatenate([gammas[1:], [gammas[1]+0.01]])),
    ]
    S_ref = None
    for name, gm in configs:
        S_mod = np.array([S_proj_direct(gm, a) for a in a_grid])
        if S_ref is None:
            S_ref = S_mod
            print(f"  {name}: S_proj 全 a 范围 [{S_mod.min():.4e}, {S_mod.max():.4e}]")
        else:
            rel = (S_mod - S_ref)/S_ref
            # 形状差异（归一化后——消除整体缩放——）
            norm = S_mod/S_mod[0] - S_ref/S_ref[0]  # 形状差（首点归一——）
            print(f"  {name}: 相对差 [{rel.min():+.2e}, {rel.max():+.2e}]——形状差 max|Δnorm| = {np.abs(norm).max():.2e}")
            print(f"    小a({a_grid[2]:.2f}): {rel[2]:+.2e}——中a({a_grid[12]:.2f}): {rel[12]:+.2e}——大a({a_grid[-1]:.1f}): {rel[-1]:+.2e}")

if __name__ == "__main__":
    main()
