#!/usr/bin/env python3
"""
决定性检验：Im Λ(σ+it)=0 的过零位置
如果 Im Λ=0 只在 σ=½（对每个 t——）——零点（Re=0 也——）在临界线——RH？
Λ(s)=Λ(1-s)——Λ(½+it) 实值——Im Λ(σ+it) 的零点集？
"""
import numpy as np
import mpmath as mp
mp.mp.dps = 15

def Lambda_val(sig, t):
    s = mp.mpc(sig, t)
    chi = 2**(s-1) * mp.pi**s / (mp.gamma(s) * mp.cos(mp.pi*s/2))
    L = chi**mp.mpf('-0.5') * mp.zeta(s)
    return complex(float(L.real), float(L.imag))

def main():
    print("="*70)
    print("Im Λ=0 的 σ 过零检验")
    print("="*70)
    
    # 对多个 t——扫 σ∈[0.05, 0.95]——找 Im Λ 的过零
    sigs = np.linspace(0.05, 0.95, 901)
    print("\nIm Λ(σ+it) 的过零位置（对每个 t——）:")
    for t in [3, 5, 8, 10, 14.1347, 14.5, 17, 20, 21.022, 23, 25, 28, 30]:
        prev = None
        zeros = []
        for sig in sigs:
            L = Lambda_val(sig, t)
            im = L.imag
            if prev is not None and prev*im < 0:
                # 二分精化
                a, b = sig-0.001, sig
                fa = prev
                for _ in range(30):
                    m = (a+b)/2
                    fm = Lambda_val(m, t).imag
                    if fa*fm < 0:
                        b = m
                    else:
                        a, fa = m, fm
                zeros.append((a+b)/2)
            prev = im
        # 过零位置（应该在 0.5——如果有别的——离轴可能——）
        zstr = ", ".join(f"{z:.4f}" for z in zeros)
        print(f"   t={t:>8}: Im Λ=0 在 σ = [{zstr}]——过零数 = {len(zeros)}")
    
    # 如果都在 0.5——检查非零点高度的 Re Λ（是否也 0——）
    print("\n如果 Im Λ=0 只在 σ=½——那零点需 Re Λ(½+it)=0（在线——）")
    print("——RH 的几何证明——检查 Re Λ=0 的 t（在线零点——）")

if __name__ == "__main__":
    main()
