#!/usr/bin/env python3
"""
v 沿 u=0 环的行为——单调性验证
u=0 环从零点出发（σ>½——）——v 沿环是否单调离开 0？
局部：v ~ (σ-½)·|ζ'|²/Im ζ'——一阶离开
如果 v 沿环单调（不回来）——环上（除零点）无 v=0——无第二零点
"""
import numpy as np
import mpmath as mp

def zeta_uv(sig, t):
    z = mp.zeta(mp.mpc(sig, t))
    return float(z.real), float(z.imag)

def find_u0(sig, gamma, width=3.0):
    """u=0 在 gamma 附近的 t"""
    ts = np.linspace(gamma-width, gamma+width, 800)
    zeros = []
    prev = None
    for t in ts:
        u, v = zeta_uv(sig, t)
        if prev is not None and prev*u < 0:
            zeros.append(t)
        prev = u
    merged = []
    for z in zeros:
        if not merged or z - merged[-1] > 0.04:
            merged.append(z)
    return merged

def main():
    print("="*70)
    print("v 沿 u=0 环的行为")
    print("="*70)
    
    # 对几个零点——追踪 u=0 环（σ 增——）——看 v 在环上的值
    for gi, gamma in enumerate([14.1347, 21.0220, 30.4249]):
        print(f"\n零点 {gi+1}（γ={gamma}——）:")
        print(f"   {'σ':>6} | {'u=0 的 t':>12} | {'v 在 u=0 处':>12}")
        for sig in [0.50, 0.505, 0.51, 0.515, 0.52, 0.53, 0.55, 0.58]:
            zs = find_u0(sig, gamma, width=2.5)
            if zs:
                # 对每个 u=0 的 t——算 v
                v_vals = []
                for t in zs:
                    u, v = zeta_uv(sig, t)
                    v_vals.append(v)
                print(f"   {sig:.3f} | {['%.3f'%z for z in zs]} | {['%+.4f'%v for v in v_vals]}")
            else:
                print(f"   {sig:.3f} | 无 | 无")
    
    # 局部理论：v ~ (σ-½)|ζ'|²/Im ζ'——验证斜率
    print("\n局部理论验证（第一零点——）:")
    rho = mp.mpc(0.5, 14.1347)
    zp = mp.zeta(rho, derivative=1)
    Re = float(zp.real); Im = float(zp.imag)
    print(f"   ζ'(ρ₁) = {Re:.4f} + {Im:.4f}i")
    slope = abs(zp)**2/Im  # v ~ (σ-½)·slope
    print(f"   理论斜率 |ζ'|²/Im = {slope:.4f}——v ~ (σ-½)·{slope:.4f}")
    # 数值：σ=0.505 的 v（环上——）vs (0.505-0.5)·slope
    zs = find_u0(0.505, 14.1347, width=2.0)
    if zs:
        for t in zs:
            u, v = zeta_uv(0.505, t)
            print(f"   σ=0.505: u=0 在 t={t:.4f}——v={v:+.4f}——理论 (0.005)·{slope:.2f}={0.005*slope:+.4f}")

if __name__ == "__main__":
    main()
