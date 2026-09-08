#!/usr/bin/env python3
"""
Ê_n = -Σ C(n,j)E_{j-1}——剥离平凡层后的二项式变换
（唐先生审计的核心对象——）
E_j = η_j - η_j^triv（非平凡零点层——无条件可算——）
理论：每个零点贡献 (ρ/(ρ-1))^n 型——|ρ/(ρ-1)|=1 ⟺ β=½

问题：Ê_n 数值行为？——O(1)/振荡（在线——）还是增长（离线——）？
"""
import mpmath as mp
mp.mp.dps = 50

def stieltjes_ma(m):
    return (-1)**m * mp.stieltjes(m) / mp.factorial(m)

def compute_etas(n_max):
    gamma0 = stieltjes_ma(0)
    gammas = [stieltjes_ma(m) for m in range(n_max+1)]
    C = {}
    for k in range(1, n_max+2):
        C[(k,0)] = gamma0**k
        for m in range(1, n_max+1):
            s = mp.mpf(0)
            for i in range(m):
                s += (k*m - (k+1)*i) * gammas[m-i] * C[(k,i)]
            C[(k,m)] = s / (m*gamma0)
    etas = []
    for n in range(n_max):
        s = mp.mpf(0)
        for k in range(n+1):
            s += (-1)**(k+1) / (k+1) * C[(k+1, n-k)]
        etas.append((n+1)*s)
    return etas

def main():
    print("="*70)
    print("Ê_n = 剥离平凡层后的二项式变换")
    print("="*70)
    
    n_max = 35  # Ê_n 需要 η 到 n——η 到 n_max
    etas = compute_etas(n_max + 5)
    
    # 剥离平凡层（前 20 个平凡零点——s=-2 到 s=-40——）
    E = []
    for j in range(n_max + 5):
        triv = mp.mpf(0)
        for m in range(1, 21):
            d = 2*m + 1
            triv += -(-1)**j / d**(j+1)  # 真实符号（residue -1——）
        E.append(etas[j] - triv)
    
    # Ê_n = -Σ_{j=1}^n C(n,j)·E_{j-1}
    print("\nÊ_n（剥离后——）:")
    Ehat = []
    for n in range(1, n_max+1):
        s = mp.mpf(0)
        for j in range(1, n+1):
            s += mp.binomial(n, j) * E[j-1]
        Ehat.append(-s)
    
    for n in range(1, n_max+1):
        if n <= 10 or n % 5 == 0:
            print(f"   n={n:>3}: Ê_n = {mp.nstr(Ehat[n-1], 12)}——|Ê_n| = {mp.nstr(abs(Ehat[n-1]), 6)}")
    
    # 对比：未剥离的 λ~_n
    print("\n未剥离 λ~_n（对照——）:")
    for n in [5, 10, 15, 20, 25, 30, 35]:
        s = mp.mpf(0)
        for j in range(1, n+1):
            s += mp.binomial(n, j) * etas[j-1]
        lt = -s
        print(f"   n={n:>3}: λ~_n = {mp.nstr(lt, 10)}")
    
    # 理论：在线零点 Ê_n ~ Σ_ρ[(ρ/(ρ-1))^n 配对]——第一零点主导？
    print("\n理论（第一零点 ρ₁——）:")
    rho1 = 0.5 + 1j*mp.mpf('14.13472514173469379045725198356247')
    q1 = rho1/(rho1-1)  # |q1| = 1（在线——）
    print(f"   q₁ = ρ₁/(ρ₁-1)——|q₁| = {mp.nstr(abs(q1), 10)}（在线=1——）")
    # (q1^n + conj(q1^n)) 配对——ρ 和 ρ̄
    for n in [5, 10, 20, 30]:
        pair = q1**n + q1.conjugate()**n
        print(f"   n={n}: q₁^n + q̄₁^n = {mp.nstr(pair, 8)}（实——振荡——）")

if __name__ == "__main__":
    main()
