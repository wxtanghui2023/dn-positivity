#!/usr/bin/env python3
"""
u=0 分支追踪——从零点出发——它去哪？
零点 ρ=½+iγ——u=0 和 v=0 垂直交叉（共形——）
u=0 分支方向——为什么 σ>½ 无 u=0（数值——）
"""
import numpy as np
import mpmath as mp

def zeta_re(sig, t):
    return float(mp.zeta(mp.mpc(sig, t)).real)

def main():
    print("="*70)
    print("u=0 分支追踪（从零点出发——）")
    print("="*70)
    
    # 第一零点 ρ = 0.5 + 14.1347i
    gamma1 = 14.1347251417
    
    # 1. 零点处 u 的梯度方向（Re ζ'——）
    rho = mp.mpc(0.5, gamma1)
    zp = mp.zeta(rho, derivative=1)
    print(f"\n1. ζ'(ρ₁) = {mp.nstr(zp, 8)}")
    print(f"   Re ζ' = {float(zp.real):.4f}——Im ζ' = {float(zp.imag):.4f}")
    
    # 2. 追踪 u=0 曲线（从零点出发——沿 u=0——）
    # u=0 局部：(σ-½)Re = (t-γ)Im——用数值跟随
    print("\n2. u=0 分支追踪（σ 从 0.5 向两侧——找 u=0 的 t——）:")
    # u(σ, t) 在零点附近——对固定 σ——u=0 的 t（接近 γ₁——）
    for sig in [0.49, 0.495, 0.5, 0.505, 0.51, 0.52, 0.55, 0.6]:
        # 在 γ₁ 附近找 u=0——密集扫描
        ts = np.linspace(gamma1-1.5, gamma1+1.5, 1000)
        zeros = []
        prev = None
        for t in ts:
            u = zeta_re(sig, t)
            if prev is not None and prev*u < 0:
                zeros.append(t)
            prev = u
        # 保留接近零点（±0.5）的
        close = [z for z in zeros if abs(z-gamma1) < 1.0]
        print(f"   σ={sig:.3f}: u=0 在 γ₁ 附近 = {['%.4f'%z for z in close]}（零点={gamma1:.4f}——）")
    
    # 3. u 在零点附近的行为（沿 σ 方向——固定 t=γ₁——）
    print("\n3. u(σ, γ₁)（沿 σ 穿过零点——）:")
    for sig in [0.45, 0.48, 0.5, 0.52, 0.55, 0.6]:
        u = zeta_re(sig, gamma1)
        print(f"   σ={sig:.3f}: u = {u:+.6f}（v 应该 ~0——在零点高度——）")
    
    # 4. 关键：u 在零点两侧的符号（σ<½ vs σ>½——固定 t 略偏零点——）
    print("\n4. u 的符号结构（t 固定 γ₁+0.1——σ 扫描——）:")
    t0 = gamma1 + 0.1
    for sig in [0.4, 0.45, 0.48, 0.5, 0.55, 0.6, 0.7]:
        u = zeta_re(sig, t0)
        v = float(mp.zeta(mp.mpc(sig, t0)).imag)
        print(f"   σ={sig:.3f}: u={u:+.4f}——v={v:+.4f}")

if __name__ == "__main__":
    main()
