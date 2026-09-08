#!/usr/bin/env python3
"""
Ê_n 的线性项来源 + 余项结构
Ê_n ~ -0.43n（线性——非平凡层）——被平凡层 λ~_n^triv ~ +0.43n 抵消
问：
A. 线性项的精确斜率（拟合——）
B. 线性项的来源（Σ_ρ q^n 的正则化——配对——）
C. 余项 Ê_n + 0.43n 是否 O(1) 振荡（相位均匀性——）
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
    print("Ê_n 线性项 + 余项结构")
    print("="*70)
    
    n_max = 40
    etas = compute_etas(n_max + 5)
    
    # 剥离平凡层
    E = []
    for j in range(n_max + 5):
        triv = mp.mpf(0)
        for m in range(1, 25):
            d = 2*m + 1
            triv += -(-1)**j / d**(j+1)
        E.append(etas[j] - triv)
    
    # Ê_n
    Ehat = []
    for n in range(1, n_max+1):
        s = mp.mpf(0)
        for j in range(1, n+1):
            s += mp.binomial(n, j) * E[j-1]
        Ehat.append(-s)
    
    # A. 线性拟合（末段——）
    print("\nA. Ê_n 的线性斜率（相邻差——）:")
    diffs = [Ehat[n] - Ehat[n-1] for n in range(1, n_max)]
    for n in [10, 15, 20, 25, 30, 35]:
        print(f"   n={n}: ΔÊ = {mp.nstr(diffs[n-1], 8)}")
    # 末段斜率
    slope = (Ehat[-1] - Ehat[20])/(n_max - 20)
    print(f"   末段斜率 ≈ {mp.nstr(slope, 8)}")
    
    # B. 理论：斜率 = ? Σ_ρ 的正则化——q^n 展开
    # q = ρ/(ρ-1)——q^n = (1+1/(ρ-1))^n ≈ exp(n·log(1+1/(ρ-1)))
    # log q ≈ 1/(ρ-1) - 1/(2(ρ-1)^2)...
    # Σ_ρ q^n 配对（ρ,ρ̄）——主项 n·Σ Re[1/(ρ-1)]？——Σ 1/(ρ-1) 收敛吗？
    # 配对 (ρ, ρ̄)：Re[1/(ρ-1)] = Re[(ρ̄-1)/|ρ-1|²] = (β-1)/|ρ-1|²
    # Σ_ρ (β-1)/|ρ-1|²——β=½ 在线——(β-1)/|ρ-1|² = -1/(2|ρ-1|²)——Σ 收敛！
    # 斜率 ~ -2·n·Σ 1/(2|ρ-1|²)·... 
    print("\nB. 理论斜率检验：")
    print("   q^n = (1+1/(ρ-1))^n——展开主项 n/(ρ-1)——配对 Re 部分")
    print("   Σ_ρ Re[1/(ρ-1)] = Σ(β-1)/|ρ-1|²——在线 β=½——Σ-1/(2|ρ-1|²)")
    # 数值
    import numpy as np
    zeros = np.load('/home/node/.openclaw/workspace/dn-project/data/zeros_odlyzko_100k.npy')
    s = mp.mpf(0)
    for g in zeros[:5000]:
        rho = 0.5 + 1j*float(g)
        s += (0.5-1)/(abs(rho-1)**2)  # Re[1/(ρ-1)] 的 2 倍？
    # Re[1/(ρ-1)] = Re[(ρ̄-1)/|ρ-1|²] = (β-1)/|ρ-1|²——β=0.5 → -0.5/|ρ-1|²
    print(f"   Σ_ρ Re[1/(ρ-1)]（5000 零点——）= {mp.nstr(s, 6)}")
    # 配对 ρ,ρ̄ 的完整 Re 贡献 = 2·Σ_ρ Re[...]？
    # Ê_n 斜率 ~ -2·Σ_ρ Re[1/(ρ-1)]·(1)？——看符号——Ê_n 负——斜率 -0.43
    print(f"   -2·ΣRe[1/(ρ-1)] = {mp.nstr(-2*s, 6)}（对比斜率 -0.43？）")

if __name__ == "__main__":
    main()
