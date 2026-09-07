#!/usr/bin/env python3
"""
扩大范围检查 φ(n+1) = −G(2n)/(8(n+1)G(2n+2)) 的符号与渐近
F(n) 先减后增（观察——）——G 可能在某 n 变号——φ 的符号关键
"""
import mpmath as mp

mp.mp.dps = 30

def theta_deriv(x):
    s = mp.mpf(0)
    n = 1
    while True:
        term = mp.mpf(n)**2 * mp.exp(-mp.pi * n*n * x)
        s += term
        if term < mp.mpf(10)**(-40):
            break
        n += 1
    return -mp.pi * s

def F_int(n):
    # F(n) = ∫₀^∞ tⁿ e^{t/4} θ'(e^t) dt（x=e^t 替换——）
    integrand = lambda t: t**n * mp.e**(t/4) * theta_deriv(mp.e**t)
    val = mp.quad(integrand, [0, mp.mpf(25)])
    return val

def main():
    print("F(n) 数值（n=0..32——）")
    N_MAX = 32
    F = {}
    for n in range(0, N_MAX+1):
        F[n] = F_int(n)
    for n in range(0, N_MAX+1, 2):
        print(f"  F({n:2d}) = {mp.nstr(F[n], 8)}")
    
    print("\nφ(n+1) = −G(2n)/(8(n+1)G(2n+2))——n=1..15")
    print(f"{'n':>3} {'G(2n)':>14} {'φ(n+1)':>16} {'φ符号':>6}")
    G = {}
    for n in range(1, 16):
        G_val = 64*n*(2*n-1)*F[2*n-2]/F[2*n] - 1
        G[2*n] = G_val
        G_next = 64*(n+1)*(2*(n+1)-1)*F[2*n]/F[2*n+2] - 1
        G[2*(n+1)] = G_next
        phi_val = -G_val / (8*(n+1)*G_next)
        sign = '+' if phi_val > 0 else ('−' if phi_val < 0 else '0')
        print(f"{n:>3} {mp.nstr(G_val, 12):>14} {mp.nstr(phi_val, 14):>16} {sign:>6}")
    
    # Bernstein 检查要点：φ 需非负——凸——φ(u)/u 完全单调——φ(0+)=0
    print("\n" + "="*70)
    print("结论分析")
    print("="*70)
    print("""
如果 φ(n+1) 对某 n 为负——则不存在非负 Bernstein φ 匹配 (4.17)
→ ξ ∉ D_P（该路径排除——）
如果 φ(n+1) 全正——需要进一步检查凸性/完全单调性

注意：BD ⊂ Bernstein（φ ≥ 0——）——(4.17) 要求 φ ∈ BD
""")

if __name__ == "__main__":
    main()
