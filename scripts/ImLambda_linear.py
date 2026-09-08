#!/usr/bin/env python3
"""
关键验证：Im Λ(σ+it) 是否 = (σ-½)·W(t)（线性——）？
如果精确——Im Λ=0 只在 σ=½ 或 W(t)=0（=在线零点——）——RH！
Λ(s) = χ^{-1/2}(s)ζ(s)——Λ(s)=Λ(1-s)
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
    print("Im Λ 的线性验证")
    print("="*70)
    
    # 1. 多个 t——扫 σ——看 Im Λ 是否线性（过 σ=½——）
    for t in [10, 14.4, 20, 25, 30]:
        print(f"\nt={t}:")
        vals = []
        for sig in [0.4, 0.45, 0.5, 0.55, 0.6]:
            L = Lambda_val(sig, t)
            vals.append((sig, L.imag))
            print(f"   σ={sig:.2f}: Im Λ = {L.imag:+.6f}——Re Λ = {L.real:+.6f}")
        # 线性检查：Im Λ/(σ-½) 是否常数
        if len(vals) >= 3:
            ratios = []
            for sig, im in vals:
                if abs(sig-0.5) > 1e-6:
                    ratios.append(im/(sig-0.5))
            if ratios:
                print(f"   Im Λ/(σ-½) = {['%+.4f'%r for r in ratios]}——常数？——")
    
    # 2. Re Λ 的 σ 对称性
    print("\n2. Re Λ 的对称性（偶函数？——）:")
    for t in [14.4, 20]:
        L1 = Lambda_val(0.4, t)
        L2 = Lambda_val(0.6, t)
        print(f"   t={t}: Re Λ(0.4)={L1.real:+.6f} vs Re Λ(0.6)={L2.real:+.6f}——差={L1.real-L2.real:+.6f}")
        print(f"         Im Λ(0.4)={L1.imag:+.6f} vs Im Λ(0.6)={L2.imag:+.6f}——和={L1.imag+L2.imag:+.6f}")
    
    # 3. W(t) = Im Λ(σ+it)/(σ-½) 的 t 依赖——W(t)=0 ⟺ 在线零点？
    print("\n3. W(t) = Im Λ/(σ-½)（σ=0.6——）:")
    for t in [5, 10, 14.1347, 14.4, 20, 21.02, 25, 30]:
        L = Lambda_val(0.6, t)
        W = L.imag/0.1
        # Re Λ 在 σ=0.5
        Lhalf = Lambda_val(0.5, t)
        print(f"   t={t:.3f}: W = {W:+.6f}——Re Λ(½+it) = {Lhalf.real:+.6f}（零点处 ~0——）")

if __name__ == "__main__":
    main()
