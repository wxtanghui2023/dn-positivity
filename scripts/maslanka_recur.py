#!/usr/bin/env python3
"""
Maślanka 递推：λ~_n = -Σ C(n,j)·η_{j-1}——验证 O(1) 并探索结构
η_n = (n+1)Σ_{k=0}^n (-1)^{k+1}/(k+1)·c^{(k+1)}_{n-k}
c^{(k)}_0 = γ_0^k；c^{(k)}_m = (1/(mγ_0))Σ_{i<m}[km-(k+1)i]γ_{m-i}c^{(k)}_i
γ_m = Maślanka Stieltjes = (-1)^m/m!·γ_m^std
"""
import mpmath as mp
mp.mp.dps = 50

def stieltjes_ma(m):
    """Maślanka 约定 Stieltjes"""
    return (-1)**m * mp.stieltjes(m) / mp.factorial(m)

def compute_lambda_tilde(n_max, verbose=False):
    """计算 λ~_n 到 n_max——用 Maślanka 递推"""
    gamma0 = stieltjes_ma(0)  # = 欧拉常数？
    # 预取 Stieltjes 到 n_max
    gammas = [stieltjes_ma(m) for m in range(n_max+1)]
    
    # c^{(k)}_m 递推——需要 c^{(k)} 对 k=1..n_max+1, m=0..n_max
    # 存储 c[k][m]——k 从 1 到 n_max+1
    C = {}  # (k,m) -> value
    for k in range(1, n_max+2):
        C[(k,0)] = gamma0**k
        for m in range(1, n_max+1):
            # c^{(k)}_m = (1/(m·γ0))Σ_{i=0}^{m-1}[km-(k+1)i]γ_{m-i}c^{(k)}_i
            s = mp.mpf(0)
            for i in range(m):
                s += (k*m - (k+1)*i) * gammas[m-i] * C[(k,i)]
            C[(k,m)] = s / (m*gamma0)
    
    # η_n = (n+1)Σ_{k=0}^n (-1)^{k+1}/(k+1)·c^{(k+1)}_{n-k}
    etas = []
    for n in range(n_max):
        s = mp.mpf(0)
        for k in range(n+1):
            s += (-1)**(k+1) / (k+1) * C[(k+1, n-k)]
        etas.append((n+1)*s)
    
    # λ~_n = -Σ_{j=1}^n C(n,j)·η_{j-1}
    results = []
    for n in range(1, n_max+1):
        s = mp.mpf(0)
        for j in range(1, n+1):
            s += mp.binomial(n, j) * etas[j-1]
        results.append(-s)
    
    return results, etas

def main():
    print("="*70)
    print("Maślanka λ~_n 验证 + 结构探索")
    print("="*70)
    
    n_max = 40
    print(f"计算到 n={n_max}（dps=50——高精度——）")
    lambdas, etas = compute_lambda_tilde(n_max)
    
    print("\nλ~_n 值:")
    for n in range(1, n_max+1):
        v = lambdas[n-1]
        print(f"   n={n:>3}: λ~_n = {mp.nstr(v, 10)}")
    
    # 统计
    vals = [abs(lambdas[n-1]) for n in range(1, n_max+1)]
    print(f"\nmax|λ~_n| (n≤{n_max}) = {mp.nstr(max(vals), 6)}")
    
    # η 的衰减
    print("\nη_j 的衰减（看超衰减——）:")
    for j in range(min(10, n_max)):
        print(f"   η_{j} = {mp.nstr(etas[j], 8)}")
    
    # 关键结构检查：λ~_n 的相邻差/模式
    print("\nλ~_n 的结构:")
    print(f"   值域 [{mp.nstr(min(lambdas),6)}, {mp.nstr(max(lambdas),6)}]")

if __name__ == "__main__":
    main()
