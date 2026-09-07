#!/usr/bin/env python3
"""
ARP 首轮测试——G_s(m,n) = Σ_{d|gcd(m,n)} w(d)·(d/√(mn))^{s−1/2}
判死线：因子化成普通 Dirichlet 正性（w≥0⟹正——σ无关——）→ 立即判死（线 8）

预分析：
设 m=da, n=db——(d/√(mn))^{s−½} = (ab)^{−(s−½)/2} = (m/d·n/d)^{−α}——α=(s−½)/2
⟹ G_s(m,n) = (mn)^{−α}·Σ_{d|gcd(m,n)} w(d)d^{2α} = (mn)^{−α}F(gcd)——F=f*1——f(d)=w(d)d^{2α}
对角化（Möbius——）：c*Gc = Σ_d f(d)|Σ_{dk≤N}c_{dk}(dk)^{−α}|²
测试：
1. 对角化公式数值验证
2. σ 扫描：正性是否 σ 无关（w≥0 时——）
3. 判死判定
"""
import numpy as np

def gcd_matrix_F(N, Fvals):
    """F(gcd(m,n)) 矩阵——Fvals[g] = F(g)"""
    G = np.zeros((N, N))
    for m in range(1, N+1):
        for n in range(1, N+1):
            g = np.gcd(m, n)
            G[m-1, n-1] = Fvals[g]
    return G

def main():
    print("="*70)
    print("ARP 首轮测试：gcd 关系矩阵 G_s")
    print("="*70)
    N = 30
    print(f"N = {N}")
    
    # α = (s−½)/2——先试 s 实（t=0——）——σ 扫描
    for sigma in [0.3, 0.5, 0.7, 0.9, 1.2]:
        alpha = (sigma - 0.5)/2
        # f(d) = w(d)d^{2α}——w(d) = 1（最简——）
        # F(g) = Σ_{d|g} d^{2α}
        Fvals = [0]*(N+1)
        for g in range(1, N+1):
            Fvals[g] = sum(d**(2*alpha) for d in range(1, g+1) if g % d == 0)
        # 对角缩放
        D = np.diag([n**(-alpha) for n in range(1, N+1)])
        G = D @ gcd_matrix_F(N, Fvals) @ D
        # 特征值
        ev = np.linalg.eigvalsh((G + G.T)/2)  # Hermitian 部分（s 实——G 对称——）
        print(f"σ={sigma}: α={alpha:.3f}——最小特征值 λ_min = {ev.min():.6e}——正性 {'✓' if ev.min() >= -1e-10 else '✗'}")
    
    # 对角化验证（s 实——）
    print("\n对角化验证（σ=0.7——α=0.1——w=1——）:")
    sigma = 0.7
    alpha = (sigma - 0.5)/2
    Fvals = [0]*(N+1)
    for g in range(1, N+1):
        Fvals[g] = sum(d**(2*alpha) for d in range(1, g+1) if g % d == 0)
    D = np.diag([n**(-alpha) for n in range(1, N+1)])
    G = D @ gcd_matrix_F(N, Fvals) @ D
    # 随机 c——两侧算
    rng = np.random.default_rng(42)
    c = rng.normal(size=N)
    Q_direct = c @ G @ c
    # 对角化：Q = Σ_d f(d)|Σ_{dk≤N} c_{dk}(dk)^{−α}|²
    Q_diag = 0
    for d in range(1, N+1):
        f_d = d**(2*alpha)  # w(d)=1
        S = sum(c[d*k-1]*(d*k)**(-alpha) for k in range(1, N//d + 1))
        Q_diag += f_d * S**2
    print(f"  直接: {Q_direct:.10f}——对角化: {Q_diag:.10f}——差: {abs(Q_direct-Q_diag):.2e}")
    
    # 复 s 测试（t ≠ 0——Hermitian 化——）
    print("\n复 s 测试（σ=0.5——t 扫描——Hermitian 化——）:")
    sigma, N2 = 0.5, 20
    for t in [1.0, 5.0, 14.0]:
        alpha = (sigma - 0.5)/2 + 1j*t/2
        Fvals = [0]*(N2+1)
        for g in range(1, N2+1):
            Fvals[g] = sum(d**(2*alpha) for d in range(1, g+1) if g % d == 0)
        # G(m,n) = (mn)^{−α}F(gcd)——Hermitian 化：(G + G*)/2——但 G_s 对称复——
        G = np.zeros((N2, N2), dtype=complex)
        for m in range(1, N2+1):
            for n in range(1, N2+1):
                g = np.gcd(m, n)
                G[m-1, n-1] = (m*n)**(-alpha) * Fvals[g]
        # 二次型 c* G c 的实部（用共轭——）
        H = (G + G.conj().T)/2
        ev = np.linalg.eigvalsh(H)
        print(f"  σ={sigma}, t={t}: Hermitian 部分 λ_min = {ev.min():.6e}——{'✓' if ev.min() >= -1e-8 else '✗'}")

if __name__ == "__main__":
    main()
