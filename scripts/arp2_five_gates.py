#!/usr/bin/env python3
"""
ARP-2 五关审计（A-E）——差商×gcd 候选

候选：φ_s(m,n) = Σ_{d|(m,n)} w(d)·Ψ_s(m/d, n/d)——Ψ 用差-积组合
先测最简非可分离核（s=½+it 临界线 Hermitian 化——）：

A 可分离性：矩阵秩（特征值衰减——）
C cycle defect：Ω(m,n,r) = φφφ − φφφ（反向——）
E σ-刚性：正性是否 σ 无关
"""
import numpy as np

def phi_candidates(m, n, s):
    """候选核——返回复数——s = σ+it"""
    sigma, t = s.real, s.imag
    if m == n:
        return 0.0 + 0j  # 对角约定 0（差为 0——）
    # 候选 1：纯差幂 (√(mn)/|m−n|)^{s−½}
    A = np.sqrt(m*n)/abs(m-n)
    return A**(s - 0.5)

def phi_candidates2(m, n, s):
    """候选 2：和-差 (√(mn)/(m+n))^{s−½}？——测试——"""
    if m == n:
        return 1.0 + 0j
    A = np.sqrt(m*n)/(m+n)
    return A**(s - 0.5)

def main():
    print("="*70)
    print("ARP-2 五关审计：非可分离差-积核")
    print("="*70)
    N = 40
    
    for name, phi in [("候选1: (√mn/|m−n|)^{s−½}", phi_candidates), 
                      ("候选2: (√mn/(m+n))^{s−½}", phi_candidates2)]:
        print(f"\n{'='*60}\n{name}\n{'='*60}")
        # A. 可分离性测试（临界线 s=½+i·14——秩——）
        s = 0.5 + 14.0j
        K = np.zeros((N, N), dtype=complex)
        for m in range(1, N+1):
            for n in range(1, N+1):
                if m != n:
                    K[m-1, n-1] = phi(m, n, s)
        # 秩检测（奇异值——）
        sv = np.linalg.svd(K, compute_uv=False)
        sv_norm = sv/sv[0]
        print(f"  A 可分离性: 奇异值比 {sv_norm[:5]}...——有效秩(>1e-8): {sum(sv_norm>1e-8)}/{N}")
        print(f"    （秩 1 = 可分离——死——高秩 = 非可分离——）")
        
        # C. cycle defect（临界线——）
        print(f"  C cycle defect Ω(m,n,r):")
        m, n, r = 6, 10, 15
        phi_mn = phi(m, n, s); phi_nr = phi(n, r, s); phi_rm = phi(r, m, s)
        phi_nm = phi(n, m, s); phi_rn = phi(r, n, s); phi_mr = phi(m, r, s)
        Omega = phi_mn*phi_nr*phi_rm - phi_nm*phi_rn*phi_mr
        # 若 φ 对称（φ(m,n)=φ(n,m)——）Ω ≡ 0——检查对称性
        asym = max(abs(phi(m,n,s)-phi(n,m,s)) for m in range(2,20) for n in range(2,20) if m!=n)
        print(f"    Ω(6,10,15) = {Omega:.6e}——非对称度 max|φ(mn)−φ(nm)| = {asym:.6e}")
        print(f"    （若 φ 对称——Ω≡0——cycle defect 平凡——需非对称 φ——）")
        
        # E. σ-刚性（正性 vs σ——）
        print(f"  E σ-刚性（Hermitian 化 (K+K*)/2 的最小特征值——t=14——）:")
        for sigma in [0.3, 0.4, 0.5, 0.6, 0.7]:
            s2 = sigma + 14.0j
            K2 = np.zeros((N, N), dtype=complex)
            for m in range(1, N+1):
                for n in range(1, N+1):
                    if m != n:
                        K2[m-1, n-1] = phi(m, n, s2)
            H = (K2 + K2.conj().T)/2
            ev = np.linalg.eigvalsh(H)
            print(f"    σ={sigma}: λ_min = {ev.min():.4e}——{'✓' if ev.min()>=-1e-8 else '✗'}")

if __name__ == "__main__":
    main()
