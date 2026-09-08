#!/usr/bin/env python3
"""
唐先生审计后的新方向：平凡零点剥离
η_j = Σ_{m≥1} (-1)^j/(2m+1)^{j+1}（平凡层——s=-2,-4,-6...）+ E_j（非平凡层）
验证：
A. η_j 的平凡层拟合（首项 3^{-j}——次项 5^{-j}——）
B. E_j = η_j - η_j^triv——剥离后看是否 ~ Σ_ρ(ρ-1)^{-j-1}
C. Ê_n = -Σ C(n,j)E_{j-1}——二项式变换——行为？
"""
import mpmath as mp
mp.mp.dps = 60

def stieltjes_ma(m):
    return (-1)**m * mp.stieltjes(m) / mp.factorial(m)

def compute_etas(n_max):
    """Maślanka 递推算 η_j 到 n_max-1"""
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

def eta_triv(j, m_max=20):
    """平凡层贡献：Σ_{m=1}^{m_max} (-1)^j/(2m+1)^{j+1}
    （m=1 → s=-2 → t=-3——m=2 → s=-4 → t=-5——等）
    注意：ζ'/ζ 的 residue——需要检查符号——先试纯 (-1)^j/d^{j+1}
    """
    total = mp.mpf(0)
    for m in range(1, m_max+1):
        d = 2*m + 1
        total += (-1)**j / d**(j+1)
    return total

def main():
    print("="*70)
    print("平凡零点剥离：η_j 的分层结构验证")
    print("="*70)
    
    n_max = 40
    etas = compute_etas(n_max)
    
    # A. η_j 与平凡层首项对比
    print("\nA. η_j vs 首层 3^{-j}（s=-2——）:")
    for j in [0, 5, 10, 15, 20, 25, 30]:
        eta = etas[j]
        first = (-1)**j / mp.mpf(3)**(j+1)
        ratio = eta/first
        print(f"   j={j:>3}: η_j = {mp.nstr(eta, 10)}——首层 = {mp.nstr(first, 10)}——比值 = {mp.nstr(ratio, 6)}")
    
    # B. 剥离：E_j = η_j - triv（含前 20 个平凡零点层——）
    print("\nB. E_j = η_j - η_j^triv（剥离平凡层——）:")
    E = []
    for j in range(n_max):
        triv = eta_triv(j, 20)
        E.append(etas[j] - triv)
    for j in [0, 5, 10, 15, 20, 25, 30]:
        print(f"   j={j:>3}: E_j = {mp.nstr(E[j], 10)}——|E_j| = {mp.nstr(abs(E[j]), 6)}")
    
    # C. 剥离后剩余 ~ Σ_ρ (ρ-1)^{-j-1}?（在线零点模型——）
    print("\nC. E_j vs 非平凡零点模型（前若干零点——）:")
    # 非平凡零点贡献：Σ_ρ 1/(ρ-1)^{j+1}——需要符号校准
    # 先看 E_j 的比率（如果 ~ d^{-j}——d 是什么——）
    for j in range(5, 25):
        if abs(E[j-1]) > 1e-40:
            r = E[j]/E[j-1]
            if j >= 10:
                print(f"   j={j}: E_j/E_{j-1} = {mp.nstr(r, 8)}（若 ~1/5——是 s=-4 剥离不完全——若更小——非平凡层——）")
    
    # D. 非平凡层理论值：Σ_ρ 1/(ρ-1)^{j+1}（第一零点主导——）
    print("\nD. 理论对比（第一非平凡零点 ρ₁=½+14.13i——）:")
    rho1 = 0.5 + 1j*mp.mpf('14.13472514173469379045725198356247')
    a = 1/(rho1-1)  # |a| = 1/|ρ₁-1| ≈ 1/14.17 ≈ 0.0706
    print(f"   |1/(ρ₁-1)| = {mp.nstr(abs(a), 6)}——第一零点层衰减率")
    for j in [10, 15, 20]:
        contrib = a**j
        print(f"   j={j}: 第一零点贡献 |a|^j = {mp.nstr(abs(contrib), 6)}——vs |E_j| = {mp.nstr(abs(E[j]),6)}")

if __name__ == "__main__":
    main()
