#!/usr/bin/env python3
"""
Maślanka-Li 模长刚性问题：离线玩具三组对照（Prony/矩阵 pencil）
唐先生第七节指示——A/B/C 三组对照

E_j = Σ_k C_k z_k^j——z_k = 1/(ρ_k-1)——Prony 恢复 z_k
q_k = 1/(1+z_k) = 1-1/ρ_k——|q_k| = 1 ⟺ β = ½

A. RH 模型：ρ_k = ½+iγ_k——期望 |q_k| = 1
B. 微弱离线：ρ_k = ½+δ+iγ_k——期望 |q_k|-1 ~ -δ/γ_k²
C. 对称离线四元组：ρ,1-ρ,ρ̄,1-ρ̄——关键对照
"""
import mpmath as mp
import numpy as np
mp.mp.dps = 60

def make_E(gammas, betas, j_max, K_zeros=None):
    """E_j = Σ_k C_k(ρ_k-1)^{-j-1}——用前 K 个零点（C_k 设 1——简化——）"""
    E = [mp.mpf(0)] * j_max
    ks = range(len(gammas)) if K_zeros is None else range(K_zeros)
    for k in ks:
        rho = mp.mpc(betas[k], gammas[k])
        z = 1/(rho-1)
        # E_j = Σ z^{j+1}（单零点贡献 (ρ-1)^{-(j+1)}——）
        zj = z  # z^1
        for j in range(j_max):
            E[j] += zj
            zj *= z
    return E

def prony_pencil(E, K, j0=0):
    """矩阵 pencil 恢复主导指数 z_k——用 E_j, j=j0..j0+2K
    Hankel: H[m][l] = E[j0+m+l]——m,l = 0..K-1
    找核向量 c: H·c = 0——多项式系数——根 = z_k
    """
    n = len(E)
    if j0 + 2*K > n:
        return None
    # 构造 Hankel 矩阵 K×K 和移位版
    H = mp.matrix(K, K)
    Hshift = mp.matrix(K, K)
    for m in range(K):
        for l in range(K):
            H[m,l] = E[j0+m+l]
            Hshift[m,l] = E[j0+m+l+1]
    # 广义特征值问题：Hshift·v = z·H·v
    # 数值：解 det(Hshift - z·H) = 0——用 mpmath 的特征值（需要 H 可逆——）
    # 简化：H^{-1}·Hshift 的特征值 = z_k
    try:
        Hinv = H**-1
        M = Hinv * Hshift
        evals = mp.eig(M)[0]  # mpmath eig 返回 (values, vectors)？
        return evals
    except Exception as e:
        return None

def main():
    print("="*70)
    print("Maślanka-Li 模长刚性问题——离线玩具对照")
    print("="*70)
    
    # 用前 5 个真实零点高度（γ——）
    gammas_real = [14.1347, 21.0220, 25.0109, 30.4249, 32.9351]
    
    # A. RH 模型
    print("\nA. RH 模型（β=½——）:")
    gammas_A = gammas_real
    betas_A = [0.5]*5
    j_max = 30
    E_A = make_E(gammas_A, betas_A, j_max)
    # Prony——K=3 恢复前 3 个 z
    K_pron = 3
    evals = prony_pencil(E_A, K_pron, 2)
    if evals:
        for z in evals[:K_pron]:
            z = mp.mpc(z)
            q = 1/(1+z)  # q = 1-1/ρ = 1/(1+z)
            qm = abs(q)
            # 恢复的 ρ：z = 1/(ρ-1) → ρ = 1+1/z
            rho_rec = 1 + 1/z
            print(f"   z = {mp.nstr(z, 6)}——恢复 ρ = {mp.nstr(rho_rec,6)}——|q| = {mp.nstr(qm, 8)}（期望 1——）")
    
    # B. 微弱离线
    print("\nB. 微弱离线（δ=0.01——β=0.51——）:")
    betas_B = [0.51]*5
    E_B = make_E(gammas_real, betas_B, j_max)
    evals = prony_pencil(E_B, K_pron, 2)
    if evals:
        for z in evals[:K_pron]:
            z = mp.mpc(z)
            q = 1/(1+z)
            qm = abs(q)
            rho_rec = 1 + 1/z
            print(f"   z = {mp.nstr(z, 6)}——恢复 ρ = {mp.nstr(rho_rec,6)}——|q| = {mp.nstr(qm, 8)}（β=0.51 期望 |q|<1——）")
    
    # 理论 |q|-1 的 δ 依赖
    print("\n   理论：|q_k|-1 ≈ (1-2β)/(2γ²)（β=0.51——γ=14.1——）:")
    for g in gammas_real[:3]:
        dq = (1-2*0.51)/(2*g**2)
        print(f"   γ={g}: |q|-1 ≈ {dq:.2e}")
    
    # C. 对称离线四元组（β=0.51 + FE 伙伴 0.49——同 γ——）
    print("\nC. 对称离线四元组（ρ: β=0.51——1-ρ̄: β=0.49——）:")
    gammas_C = gammas_real + gammas_real  # 每组两个（β=0.51 和 1-β=0.49——）
    betas_C = [0.51]*5 + [0.49]*5
    E_C = make_E(gammas_C, betas_C, j_max)
    evals = prony_pencil(E_C, K_pron, 2)
    if evals:
        for z in evals[:K_pron]:
            z = mp.mpc(z)
            q = 1/(1+z)
            qm = abs(q)
            rho_rec = 1 + 1/z
            b_rec = rho_rec.real
            print(f"   恢复 ρ = {mp.nstr(rho_rec,6)}——β_rec = {mp.nstr(b_rec,6)}——|q| = {mp.nstr(qm, 8)}")
    
    print("\n说明：Prony 从 E_j 恢复 z_k——q=1/(1+z)——|q|=1 ⟺ β=½")
    print("     A: |q| 应全 1——B: β=0.51 的 |q|<1——C: 四元组混合")

if __name__ == "__main__":
    main()
