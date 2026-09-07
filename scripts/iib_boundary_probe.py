#!/usr/bin/env python3
"""
II-B 算术边界形式探索
D = 卷积 A_a: (Df)(n) = Σ_{d|n} a(d) f(n/d)
D^♯ = 向上 dilation: (D^♯g)(n) = Σ_{k: n|k} b(k/n) g(k)（截断 k≤N——）
边界形式: B_N(f,g) = ⟨Df,g⟩_N − ⟨f,D^♯g⟩_N

关键：若 D^♯ = D*（伴随——）B_N ≡ 0（对称抵消——）——需要非伴随对
测试 h_s(n) = n^{-s}——B_N(h_s,h_s) 的 N→∞ 渐近——vanishing 条件？
死线：若结果 = ζ'/ζ 或 Σ1/(s−ρ)——立即关闭
"""
import numpy as np
import mpmath as mp
mp.mp.dps = 20

def B_N(a, b, s, N):
    """B_N(h_s,h_s)——h_s(n) = n^{-s}——conj 用 s̄"""
    s_c = s.conjugate()
    total = mp.mpf('0')
    # ⟨A_a h_s, h_s⟩_N = Σ_{dm≤N} a(d) (dm)^{-s_c} (d)^(-s)?? ——重新推导：
    # (A_a h_s)(n) = Σ_{d|n} a(d) (n/d)^{-s}——⟨A_a h_s, h_s⟩ = Σ_{n≤N}(A_a h_s)(n)·n^{-s_c}
    # = Σ_{n≤N} Σ_{d|n} a(d)(n/d)^{-s} n^{-s_c}
    # ⟨h_s, D^♯h_s⟩ = Σ_{n≤N} n^{-s_c} Σ_{k:n|k,k≤N} b(k/n) k^{-s}
    term1 = mp.mpf('0')
    for n in range(1, N+1):
        acc = mp.mpf('0')
        for d in range(1, n+1):
            if n % d == 0:
                acc += a(d) * (n/d)**(-s)
        term1 += acc * n**(-s_c)
    term2 = mp.mpf('0')
    for n in range(1, N+1):
        acc = mp.mpf('0')
        for k in range(n, N+1, n):
            acc += b(k//n) * k**(-s)
        term2 += n**(-s_c) * acc
    return term1 - term2

def main():
    print("="*70)
    print("II-B 边界形式 B_N(h_s,h_s)——数值探索")
    print("="*70)
    
    # 情形 1：a=b=1（伴随对——预期 B_N ≈ 0——）
    print("\n情形 1: a=b=1（伴随对——）")
    for s_val in [0.5+14.0j, 0.6+14.0j, 0.5+21.0j]:
        B200 = B_N(lambda d: 1, lambda d: 1, s_val, 200)
        B400 = B_N(lambda d: 1, lambda d: 1, s_val, 400)
        print(f"  s={s_val}: B_200 = {float(B200.real):.6e}{float(B200.imag):+.6e}j——B_400 = {float(B400.real):.6e}{float(B400.imag):+.6e}j")
    
    # 情形 2：a=1, b=μ（Möbius——非伴随——）
    import sympy
    mu = sympy.mobius
    print("\n情形 2: a=1, b=μ（非伴随——）")
    for s_val in [0.5+14.0j, 0.6+14.0j]:
        B200 = B_N(lambda d: 1, lambda d: mu(d), s_val, 200)
        print(f"  s={s_val}: B_200 = {float(B200.real):.6e}{float(B200.imag):+.6e}j")
    
    # 情形 3: a=μ, b=1
    print("\n情形 3: a=μ, b=1（非伴随——）")
    for s_val in [0.5+14.0j, 0.6+14.0j]:
        B200 = B_N(lambda d: mu(d), lambda d: 1, s_val, 200)
        print(f"  s={s_val}: B_200 = {float(B200.real):.6e}{float(B200.imag):+.6e}j")

if __name__ == "__main__":
    main()
