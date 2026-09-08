#!/usr/bin/env python3
"""
完整剥离平凡零点层——看剩余的非平凡层
η_j = -Σ_{m≥1} (-1)^j/(2m+1)^{j+1} + E_j^final
剥离到 s=-2M——剩余应 ~ Σ_ρ(ρ-1)^{-j-1}（非平凡——衰减 ~1/14.2——）
"""
import mpmath as mp
import numpy as np
mp.mp.dps = 80

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
    print("完整平凡层剥离——剩余非平凡层")
    print("="*70)
    
    n_max = 60
    etas = compute_etas(n_max)
    
    # 逐层剥离：E^(1)_j = η_j + (-1)^j/3^{j+1}（剥 s=-2）
    # E^(2)_j = E^(1)_j + (-1)^j/5^{j+1}（剥 s=-4）...
    # 每层的贡献：-(-1)^j/d^{j+1}——剥离 = 加 (-1)^j/d^{j+1}
    print("\n逐层剥离的比率演变（每层应显示下一个平凡零点——）:")
    E = list(etas)
    for layer in range(1, 8):  # 剥 7 层（s=-2 到 s=-14——）
        d = 2*layer + 1
        for j in range(n_max):
            E[j] = E[j] + (-1)**j / mp.mpf(d)**(j+1)  # 剥掉 -(-1)^j/d^{j+1}
        # 显示剥离后的中间比率（几个 j——）
        sample = []
        for j in range(n_max-3, n_max-8, -1):
            if abs(E[j-1]) > 1e-60:
                sample.append(f"{mp.nstr(E[j]/E[j-1], 4)}")
        print(f"   剥 s={-2*layer}（d={d}）后 E_j 末段比率: {sample[:3]}")
    
    # 最终剩余——看是否 ~Σ_ρ(ρ-1)^{-j}
    print("\n最终 E_j（剥 7 层后——）量级:")
    for j in [20, 30, 40, 50]:
        print(f"   j={j}: E_j = {mp.nstr(E[j], 8)}——|E_j| = {mp.nstr(abs(E[j]), 5)}")
    
    # 与非平凡零点模型对比（第一零点主导——）
    print("\n非平凡层理论（Σ_ρ(ρ-1)^{-j-1}——第一零点主导——）:")
    rho1 = 0.5 + 1j*mp.mpf('14.13472514173469379045725198356247')
    a1 = 1/(rho1-1)
    print(f"   |a₁| = |1/(ρ₁-1)| = {mp.nstr(abs(a1), 8)}")
    for j in [20, 30, 40]:
        model = abs(a1)**j
        print(f"   j={j}: 第一零点模型 |a₁|^j = {mp.nstr(model, 5)} vs |E_j| = {mp.nstr(abs(E[j]), 5)}")
    
    # 末段比率（如果 ~1/14.2 是 ρ₁ 主导——）
    print("\n末段 E_j 比率（期望 ~ -1/|ρ₁-1| 类——复数——模 ~0.0707——）:")
    for j in range(45, 58):
        if abs(E[j-1]) > 1e-70:
            r = E[j]/E[j-1]
            print(f"   j={j}: E_j/E_{j-1} = {mp.nstr(r, 6)}——模 = {mp.nstr(abs(r),6)}")

if __name__ == "__main__":
    main()
