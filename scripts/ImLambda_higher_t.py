#!/usr/bin/env python3
"""
⚠️ 漏洞检查：Im Λ 单调性的来源 + 更高 t
1. ∂_σ Im Λ = Im(Λ') 的符号（单调的解析来源——）
2. 更高 t（到 200——）的单调性
3. Λ' 与 ζ' 的关系
"""
import numpy as np
import mpmath as mp
mp.mp.dps = 20

def Lambda_im(sig, t):
    s = mp.mpc(sig, t)
    chi = 2**(s-1) * mp.pi**s / (mp.gamma(s) * mp.cos(mp.pi*s/2))
    L = chi**mp.mpf('-0.5') * mp.zeta(s)
    return float(L.imag)

def main():
    print("="*70)
    print("Im Λ 单调性来源 + 更高 t")
    print("="*70)
    
    # 1. 单调方向（σ 增——Im Λ 增还是减——）斜率符号
    print("\n1. Im Λ 的 σ 斜率（∂_σ Im Λ 的符号——）:")
    for t in [5, 10, 14.4, 20, 25, 30, 40, 50, 60]:
        im1 = Lambda_im(0.49, t)
        im2 = Lambda_im(0.51, t)
        slope = (im2-im1)/0.02
        print(f"   t={t}: 斜率 = {slope:+.4f}（σ 增——Im Λ {'增' if slope>0 else '减'}——）")
    
    # 2. 更高 t 的单调性（粗采样——）
    print("\n2. 更高 t（到 200——粗——）的过零:")
    sigs = np.linspace(0.05, 0.95, 100)
    for t in [70, 80, 90, 100, 120, 150, 200]:
        prev = None
        zeros = []
        for sig in sigs:
            im = Lambda_im(sig, t)
            if prev is not None and prev*im < 0:
                zeros.append(sig)
            prev = im
        ok = len(zeros) == 1 and abs(zeros[0]-0.5) < 0.02 if zeros else False
        print(f"   t={t}: 过零 = {['%.3f'%z for z in zeros]}——{'✓' if ok else '⚠️'}")
    
    # 3. 在零点处（t=γ_k——）的行为——零点本身 Im Λ=0（σ=½——）——单调穿过
    print("\n3. 零点高度 t=γ_k 处的 Im Λ（σ 扫描——过零斜率——）:")
    for t in [14.1347, 21.022, 25.011]:
        im1 = Lambda_im(0.499, t)
        im2 = Lambda_im(0.501, t)
        print(f"   t={t}: Im Λ(0.499)={im1:+.6f}——Im Λ(0.501)={im2:+.6f}——斜率 {(im2-im1)/0.002:+.3f}")

if __name__ == "__main__":
    main()
