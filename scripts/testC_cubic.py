#!/usr/bin/env python3
"""
Test C：Im Λ 的奇函数展开三阶项
F_t(x) = Im Λ(½+x+it)——奇函数：F_t(x) = a₁x + a₃x³ + a₅x⁵ + ...
检查 R₃(t,x) = [F_t(x) - a₁x]/x³——是否 → 非零常数（三阶项存在——）

如果 a₃ ≠ 0——"精确线性"死——但单调性仍可能（a₃ 小——）
"""
import numpy as np
import mpmath as mp
mp.mp.dps = 20

def Lambda_im_half(x, t):
    """F_t(x) = Im Λ(½+x+it)"""
    s = mp.mpc(0.5+x, t)
    chi = 2**(s-1) * mp.pi**s / (mp.gamma(s) * mp.cos(mp.pi*s/2))
    L = chi**mp.mpf('-0.5') * mp.zeta(s)
    return float(L.imag)

def main():
    print("="*70)
    print("Test C：Im Λ 三阶项检查")
    print("="*70)
    
    for t in [5, 10, 14.4, 20, 25, 30, 40, 50]:
        # 小 x 的 F_t(x)
        xs = [0.001, 0.002, 0.005, 0.01, 0.02, 0.05, 0.1, 0.15, 0.2]
        print(f"\nt={t}:")
        # a₁ = F_t'(0)——用小 x 估计 F_t(x)/x → a₁
        F_small = [Lambda_im_half(x, t) for x in xs[:3]]
        a1_est = F_small[0]/xs[0]  # 粗略
        # 更准：用 x=0.001 和 0.002 外推
        a1 = (Lambda_im_half(0.002, t)*4 - Lambda_im_half(0.001, t))/3  # Richardson
        print(f"   a₁ ≈ {a1:+.6f}")
        # R₃(t,x) = [F(x) - a₁x]/x³
        for x in [0.05, 0.1, 0.15, 0.2]:
            Fx = Lambda_im_half(x, t)
            R3 = (Fx - a1*x)/x**3
            print(f"   x={x:.2f}: F={Fx:+.6f}——R₃={R3:+.6f}")
        # 也看奇数更高阶（x=0.2 的 R₃ vs x=0.1 的——如果常数——纯 a₃——如果变——高阶——）
        R3_1 = (Lambda_im_half(0.1, t) - a1*0.1)/0.001
        R3_2 = (Lambda_im_half(0.2, t) - a1*0.2)/0.008
        print(f"   R₃(0.1)={R3_1:+.4f}——R₃(0.2)={R3_2:+.4f}——{'常数≈' if abs(R3_1-R3_2)<0.5*max(abs(R3_1),abs(R3_2)) else '有高阶'}")

if __name__ == "__main__":
    main()
