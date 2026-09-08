#!/usr/bin/env python3
"""
Λ(s) = χ^{-1/2}(s)ζ(s) 的 Re Λ=0 分支结构
Λ(s)=Λ(1-s)——Re Λ=0 水平集 FE 配对
Λ(½+it) 实值——Re Λ=0 ∩ 临界线 = 在线零点

问题：
1. Re Λ=0 分支（零点附近——）结构——与 u=0（Re ζ=0）的区别
2. 分支的 FE 镜像（s ↔ 1-s——）
3. 分支与临界线的交点
"""
import numpy as np
import mpmath as mp
mp.mp.dps = 15

def Lambda_re(sig, t):
    s = mp.mpc(sig, t)
    chi = 2**(s-1) * mp.pi**s / (mp.gamma(s) * mp.cos(mp.pi*s/2))
    L = chi**mp.mpf('-0.5') * mp.zeta(s)
    return float(L.real)

def Lambda_im(sig, t):
    s = mp.mpc(sig, t)
    chi = 2**(s-1) * mp.pi**s / (mp.gamma(s) * mp.cos(mp.pi*s/2))
    L = chi**mp.mpf('-0.5') * mp.zeta(s)
    return float(L.imag)

def main():
    print("="*70)
    print("Re Λ=0 分支结构（第一零点附近——）")
    print("="*70)
    
    gamma1 = 14.1347
    # 1. Re Λ=0 的位置（σ 扫描——t 在零点附近——）
    print("\n1. Re Λ=0 vs Re ζ=0（零点 γ₁ 附近——）:")
    for sig in [0.45, 0.48, 0.50, 0.52, 0.55, 0.6, 0.65]:
        ts = np.linspace(gamma1-2, gamma1+2, 500)
        zeros_L = []
        zeros_u = []
        prev_L = None
        prev_u = None
        for t in ts:
            rL = Lambda_re(sig, t)
            u = float(mp.zeta(mp.mpc(sig, t)).real)
            if prev_L is not None and prev_L*rL < 0:
                zeros_L.append(t)
            if prev_u is not None and prev_u*u < 0:
                zeros_u.append(t)
            prev_L, prev_u = rL, u
        print(f"   σ={sig:.2f}: Re Λ=0 在 {['%.3f'%z for z in zeros_L]}——Re ζ=0 在 {['%.3f'%z for z in zeros_u]}")
    
    # 2. Re Λ=0 在 FE 镜像点（1-σ 处——）的关系
    print("\n2. FE 镜像：Re Λ(σ,t)=0 ⟺ Re Λ(1-σ,t)=0？")
    for sig in [0.45, 0.6]:
        ts = np.linspace(gamma1-2, gamma1+2, 500)
        z_sig = []
        z_mirror = []
        prev = None
        for t in ts:
            v = Lambda_re(sig, t)
            if prev is not None and prev*v < 0:
                z_sig.append(t)
            prev = v
        prev = None
        for t in ts:
            v = Lambda_re(1-sig, t)
            if prev is not None and prev*v < 0:
                z_mirror.append(t)
            prev = v
        print(f"   σ={sig}: Re Λ=0 在 {['%.3f'%z for z in z_sig]}")
        print(f"   1-σ={1-sig:.2f}: Re Λ=0 在 {['%.3f'%z for z in z_mirror]}")
        print(f"   ——应该相同位置（FE 不变——）？")
    
    # 3. Λ 的 Im 在临界带（非临界线——）
    print("\n3. Λ 的虚部（σ≠0.5——）:")
    for sig in [0.4, 0.45, 0.5, 0.55, 0.6]:
        # 在零点附近（非零点处——）的 Im Λ
        t0 = gamma1 + 0.3  # 偏离零点
        imL = Lambda_im(sig, t0)
        print(f"   σ={sig}: Im Λ({sig}+{t0:.1f}i) = {imL:+.6f}")

if __name__ == "__main__":
    main()
