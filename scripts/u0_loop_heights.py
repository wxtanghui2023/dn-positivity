#!/usr/bin/env python3
"""
u=0 环高追踪——多个零点
对每个零点 ρ=½+iγ_k——找 u=0 环的拱顶（最大 σ——）
环高 = σ_max − ½——γ 依赖？
"""
import numpy as np
import mpmath as mp

# 已知前几个零点
gammas = [14.134725, 21.022040, 25.010858, 30.424876, 32.935062,
          37.586178, 40.918719, 43.327073, 48.005151, 49.773832]

def zeta_re(sig, t):
    return float(mp.zeta(mp.mpc(sig, t)).real)

def find_u0_near(sig, gamma, width=2.0):
    """找 u=0 在 gamma 附近的 t（±width——）"""
    ts = np.linspace(gamma-width, gamma+width, 600)
    zeros = []
    prev = None
    for t in ts:
        u = zeta_re(sig, t)
        if prev is not None and prev*u < 0:
            # 粗插值
            zeros.append(t)
        prev = u
    # 去重（相邻的合并——）
    merged = []
    for z in zeros:
        if not merged or z - merged[-1] > 0.05:
            merged.append(z)
    return merged

def find_loop_top(gamma):
    """找 u=0 环的拱顶（从 σ=0.5 向上扫——找 u=0 消失的 σ——）"""
    # u=0 在零点附近（σ=0.5——）应该有 1-2 个
    # 环顶 = u=0 数从 2 变 0 的 σ（两支合并——）
    # 或者从 1 变 0（如果只有零点那支——）
    for sig in np.arange(0.5, 1.0, 0.005):
        zs = find_u0_near(sig, gamma, width=3.0)
        # 零点那支总在（u(½,γ)=0——）——但 σ>½ 后零点不在 u=0 上了（除非 β=½ 的零点——）
        # 零点在 σ=½——σ>½ 时 u(σ,γ)≠0（数值——）——所以 σ>½ 的 u=0 都是"额外"的
        # 环顶 = 额外 u=0 消失的 σ
        if len(zs) == 0:
            return sig, 0  # 无 u=0——环顶在此之前
    return 1.0, len(zs)

def main():
    print("="*70)
    print("u=0 环高追踪（多个零点——）")
    print("="*70)
    
    print("\n各零点附近的 u=0 随 σ（粗略——）:")
    for gi, gamma in enumerate(gammas[:6]):
        print(f"\n零点 {gi+1}（γ={gamma:.3f}——）:")
        for sig in [0.50, 0.52, 0.55, 0.58, 0.62, 0.66, 0.70]:
            zs = find_u0_near(sig, gamma, width=2.5)
            print(f"   σ={sig:.2f}: u=0 数 = {len(zs)}——位置 = {['%.2f'%z for z in zs[:4]]}")

if __name__ == "__main__":
    main()
