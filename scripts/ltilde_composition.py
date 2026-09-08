#!/usr/bin/env python3
"""
正确理解验证：λ~_n 的组成
λ_n = Σ_{非平凡}[1-(1-1/ρ)^n]（无平凡零点——）
Maślanka：λ_n = 趋势 + λ~_n——λ~_n = -ΣC(n,j)η_{j-1}（η 含平凡层——）
问题：η 的平凡层在 λ~_n 里的净贡献是什么？（应该被"趋势"抵消——）

验证：λ~_n 减"平凡层二项式变换" = 非平凡振荡（应该 O(1)——）
平凡层二项式变换：-Σ_j C(n,j)·η^triv_{j-1}
η^triv_{j-1} = -Σ_m (-1)^{j-1}/(2m+1)^j（ζ'/ζ 平凡零点——）
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
    print("λ~_n 的组成：平凡层 vs 非平凡振荡")
    print("="*70)
    
    n_max = 30
    etas = compute_etas(n_max + 5)
    
    # λ~_n（完整——）
    def ltilde_from_etas(etas_arr, n):
        s = mp.mpf(0)
        for j in range(1, n+1):
            s += mp.binomial(n, j) * etas_arr[j-1]
        return -s
    
    # 平凡层二项式变换（解析——）
    # η^triv_{j-1} = -Σ_m (-1)^{j-1}/(2m+1)^j
    # λ~_n^triv = -Σ_j C(n,j)η^triv_{j-1} = +Σ_m Σ_j C(n,j)(-1)^{j-1}/(2m+1)^j
    # 内层 = 1-(1-1/(2m+1))^n = 1-(2m/(2m+1))^n
    # λ~_n^triv = Σ_m [1-(2m/(2m+1))^n]·(2m+1)？——不对——Σ C(n,j)(-1)^{j-1}x^j = 1-(1-x)^n——x=1/(2m+1)
    # λ~_n^triv = -Σ_m [1-(1-1/(2m+1))^n]·(1)·(-1)？——符号——直接数值：η^triv 用显式和
    print("\nλ~_n 分解（n=5..25——）:")
    print(f"   {'n':>4} {'λ~_n(全)':>12} {'λ~_n^triv(M=100)':>16} {'净非平凡':>12}")
    for n in [5, 10, 15, 20, 25]:
        lt = ltilde_from_etas(etas, n)
        # triv 直接数值（二项式变换 η^triv——）
        s_triv = mp.mpf(0)
        for j in range(1, n+1):
            eta_triv_j = mp.mpf(0)
            for m in range(1, 101):
                d = 2*m + 1
                eta_triv_j += -(-1)**(j-1) / d**j
            s_triv += mp.binomial(n, j) * eta_triv_j
        lt_triv = -s_triv
        net = lt - lt_triv
        print(f"   {n:>4} {mp.nstr(lt,10):>12} {mp.nstr(lt_triv,10):>16} {mp.nstr(net,10):>12}")
    
    print("\n说明：如果 '净非平凡' O(1)——λ~_n 的 O(1) 主要来自平凡层抵消后")
    print("     的非平凡振荡——需要相位均匀性（配对——）")

if __name__ == "__main__":
    main()
