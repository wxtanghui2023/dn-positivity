#!/usr/bin/env python3
"""
QW_λ 完整数值实现——子问题 A/C
基：Mellin 变量 t ∈ [−L,L] 上的偶三角基 F_j(t) = cos(πjt/L)
f_j(x) = F_j(log x)——支撑 [λ^{-1}, λ]

QW_λ(i,j) = Q(f_i, f_j) = Σ_v W_v(f_i · f_j~)
其中 (f_i · f_j~)(x) = 乘法卷积——在 Mellin 变量 = (F_i * F_j)(log x)——普通卷积

W_p(g) = (log p)Σ_m p^{-m/2}(g(p^m) + g(p^{-m}))——g = f_i·f_j~——在 t = ±m log p 取值
W_R(g) = (log 4π+γ)g(1) + ∫(Archimedean——)
"""
import numpy as np
import mpmath as mp
mp.mp.dps = 15

def conv_FiFj(Fi, Fj, L, t):
    """(F_i * F_j)(t)——F 支撑 [−L,L]——普通卷积——数值积分"""
    # (Fi*Fj)(t) = ∫ Fi(u)Fj(t−u) du——u ∈ [−L,L], t−u ∈ [−L,L]
    lo = max(-L, t-L)
    hi = min(L, t+L)
    if lo >= hi:
        return 0.0
    # mpmath 积分
    return mp.quad(lambda u: Fi(u)*Fj(t-u), [lo, hi])

def make_Fj(j, L):
    def Fj(t):
        if abs(t) > L:
            return mp.mpf('0')
        return mp.cos(mp.pi*j*t/L)
    return Fj

def Wp_conv(Fi, Fj, L, p, m_max=30):
    """W_p(f_i·f_j~)——(f_i·f_j~)(p^m) = (Fi*Fj)(m log p)"""
    lp = mp.log(p)
    total = mp.mpf('0')
    for m in range(1, m_max+1):
        t1 = m*lp
        c1 = conv_FiFj(Fi, Fj, L, t1)
        c2 = conv_FiFj(Fi, Fj, L, -t1)
        total += p**(-m/2.0)*(c1+c2)
    return lp*total

def WR_conv(Fi, Fj, L):
    """W_R(f_i·f_j~)——g(x) = (Fi*Fj)(log x)——"""
    gE = mp.euler
    # g(1) = (Fi*Fj)(0)
    g1 = conv_FiFj(Fi, Fj, L, mp.mpf('0'))
    total = (mp.log(4*mp.pi)+gE)*g1
    # ∫₁^∞ [g(x)+g(1/x)−2x^{−1/2}g(1)] x^{1/2}/(x−x^{-1}) d*x——d*x=dx/x
    def integrand(x):
        lx = mp.log(x)
        gx = conv_FiFj(Fi, Fj, L, lx)
        gix = conv_FiFj(Fi, Fj, L, -lx)
        return (gx + gix - 2*x**(-0.5)*g1) * x**0.5/(x-x**(-1)) / x
    total += mp.quad(integrand, [1, mp.inf])
    return total

def main():
    print("="*70)
    print("QW_λ 数值实现——最小特征值/向量")
    print("="*70)
    
    # λ = 3（小——只有 p=2,3——）
    lam = 3.0
    L = mp.log(lam)
    primes = [2, 3]
    Nbasis = 5  # j = 0..4
    
    print(f"λ={lam}——L=logλ={float(L):.3f}——素数 {primes}——基 {Nbasis} 个（j=0..{Nbasis-1}）")
    
    # 构造矩阵 QW(i,j) = Σ_v W_v(f_i·f_j~)
    # 注意：Weil 正性用 Q(g) = ΣW_v(g*g*)——g*g* = g·g~（自卷积——）
    # QW_λ 的二次型 = Q(f,f)——双线性型 B(f,g) = Σ_v W_v(f·g~)
    # 最小特征向量 = 使 Q(f,f) 最小（归一化——）
    QW = np.zeros((Nbasis, Nbasis))
    for i in range(Nbasis):
        Fi = make_Fj(i, L)
        for j in range(Nbasis):
            Fj = make_Fj(j, L)
            val = mp.mpf('0')
            for p in primes:
                val += Wp_conv(Fi, Fj, L, p)
            val += WR_conv(Fi, Fj, L)
            QW[i, j] = float(val)
    
    print("\nQW_λ 矩阵（前 5x5——）:")
    for i in range(Nbasis):
        print("  " + " ".join(f"{QW[i,j]:+.4f}" for j in range(Nbasis)))
    
    # 对称化（应该对称——）
    QWsym = (QW + QW.T)/2
    print(f"\n非对称度: {np.abs(QW-QW.T).max():.2e}")
    
    # 特征值
    evals, evecs = np.linalg.eigh(QWsym)
    print(f"\n特征值: {evals}")
    print(f"最小特征值: {evals[0]:.6e}——第二小: {evals[1]:.6e}——simple? {evals[1]-evals[0] > 1e-6*max(1,abs(evals[1]))}")
    
    # 最小特征向量（偶性——基全是偶的——自动偶——）
    v0 = evecs[:, 0]
    print(f"最小特征向量系数: {v0}")
    # 归一化检查
    print(f"|v0| = {np.linalg.norm(v0):.4f}")

if __name__ == "__main__":
    main()
