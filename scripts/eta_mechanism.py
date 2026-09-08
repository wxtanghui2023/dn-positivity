#!/usr/bin/env python3
"""
η 交错级数——t=0 零-free 机制的解剖
η(s) = Σ(−1)^{n−1}n^{−s}——σ>0 收敛（不含解析延拓——）
t=0：η(σ)>0（Leibniz——）——ζ(σ)=η(σ)/(1−2^{1−σ})——(0,1) 无零点——【纯算术——】
t≠0：η(σ+it) 复——正性丢失——零点条件=实虚部都零

问题：
1. t=0 机制的精确结构（配对——）——为什么 Leibniz 有效
2. t≠0 失效点（复变量——配对破坏——）
3. η 部分和的配对能否推广（成对 |Δη|——）
"""
import numpy as np
import mpmath as mp
mp.mp.dps = 15

def main():
    print("="*70)
    print("η 交错级数 t=0 机制解剖")
    print("="*70)
    
    # 1. t=0：η(σ) 的部分和（配对结构——）
    print("\n1. t=0 的 Leibniz 配对:")
    print("   η_N(σ) = Σ_{n≤N}(−1)^{n−1}n^{−σ}——奇偶配对:")
    for sig in [0.3, 0.5, 0.8]:
        print(f"\n   σ={sig}:")
        S = 0.0
        for n in range(1, 30, 2):  # 每步加两项（奇偶——）
            term_o = (n)**(-sig)          # 奇数项 +（−1)^{n−1}=+1
            term_e = -(n+1)**(-sig)       # 偶数项 −
            pair = term_o + term_e        # 配对
            S += pair
            print(f"   对 ({n},{n+1}): 配对贡献 = {pair:+.6f}——累计 η = {S:+.6f}")
    
    # 2. t≠0：配对破坏
    print("\n2. t≠0 的配对（复——）:")
    t = 14.1347  # 第一零点高度
    for sig in [0.3, 0.5]:
        print(f"\n   σ={sig}——t={t}:")
        # η_N 的部分和——看实/虚部的收敛
        S_re, S_im = 0.0, 0.0
        for n in range(1, 60):
            term = (-1)**(n-1) * n**(-sig) * np.cos(t*np.log(n))
            term_im = (-1)**(n-1) * n**(-sig) * np.sin(t*np.log(n))
            S_re += term
            S_im += term_im
            if n % 10 == 0:
                print(f"   N={n}: η_N = {S_re:+.4f}{S_im:+.4f}i——|η_N| = {np.hypot(S_re,S_im):.4f}")
    
    # 3. η(½+it) 在零点处 = 0？——η 与 ζ 的关系
    print("\n3. η = (1−2^{1−s})ζ——在零点处:")
    s1 = mp.mpc(0.5, 14.1347)
    eta1 = mp.nsum(lambda n: (-1)**(n-1) * n**(-s1), [1, mp.inf])
    zeta1 = mp.zeta(s1)
    factor = 1 - 2**(1-s1)
    print(f"   η(ρ₁) = {mp.nstr(eta1, 6)}")
    print(f"   (1−2^{{1−s}})ζ(ρ₁) = {mp.nstr(factor*zeta1, 6)}")
    print(f"   ——η 的零点 = ζ 的零点（除 1−2^{{1−s}}=0——）")

if __name__ == "__main__":
    main()
