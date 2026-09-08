#!/usr/bin/env python3
"""
u=0 曲线轨迹追踪——"斜 vs 直"验证
u=0（Re ζ=0）的位置随 σ 变化（斜——）——v=0（直——）
追踪一条 u=0 曲线——看它为什么在 σ>½ 不与 v=0 相交
"""
import numpy as np
import mpmath as mp

def zeta_re(sig, t):
    z = mp.zeta(mp.mpc(sig, t))
    return float(z.real)

def zeta_im(sig, t):
    z = mp.zeta(mp.mpc(sig, t))
    return float(z.imag)

def find_zero(fn, sig, t_lo, t_hi, n=200):
    """找 fn(sig, t) 在 [t_lo, t_hi] 的过零"""
    ts = np.linspace(t_lo, t_hi, n)
    vals = [fn(sig, t) for t in ts]
    zeros = []
    for i in range(len(ts)-1):
        if vals[i] * vals[i+1] < 0:
            # 二分
            a, b = ts[i], ts[i+1]
            fa, fb = vals[i], vals[i+1]
            for _ in range(20):
                m = (a+b)/2
                fm = fn(sig, m)
                if fa*fm < 0:
                    b, fb = m, fm
                else:
                    a, fa = m, fm
            zeros.append((a+b)/2)
    return zeros

def main():
    print("="*70)
    print("u=0 曲线轨迹（斜 vs 直——）")
    print("="*70)
    
    # 追踪 v=0 在 14.1 附近随 σ
    print("1. v=0 的位置随 σ（在零点高度附近——）:")
    for sig in [0.2, 0.35, 0.5, 0.65, 0.8]:
        zs = find_zero(zeta_im, sig, 13.5, 15.0)
        print(f"   σ={sig}: v=0 在 {['%.4f'%z for z in zs]}")
    
    # 追踪 u=0 曲线——从 σ=0.5 的零点高度开始——随 σ 怎么走
    print("\n2. u=0 的轨迹（从 σ=0.4 到 0.7——追踪各零点附近的——）:")
    # 在 σ=0.5——u=0 在零点高度（14.13——）附近
    for sig in [0.4, 0.45, 0.5, 0.52, 0.55, 0.6, 0.65, 0.7]:
        # 找 u=0 在 10-50 的所有位置
        zs = find_zero(zeta_re, sig, 10, 55, 400)
        # 分类：接近零点高度（14.1, 21, 25, 30.4, 32.9——）的
        print(f"   σ={sig:.2f}: u=0 位置 = {['%.1f'%z for z in zs]}")
    
    # 3. 关键：追踪特定 u=0 曲线（比如从 14.13 零点附近出发的——）
    print("\n3. 从零点附近出发的 u=0 曲线轨迹:")
    # u=0 在 σ 略小于 ½ 时在零点高度左边/右边？
    for sig in [0.45, 0.48, 0.5, 0.52, 0.55]:
        zs = find_zero(zeta_re, sig, 13.0, 15.5, 300)
        print(f"   σ={sig:.2f}: u=0 在 13-15.5 = {['%.3f'%z for z in zs]}（零点 14.13——）")

if __name__ == "__main__":
    main()
