#!/usr/bin/env python3
# 验证 Connes 2026 "Letter" 的核心数值声称:
# 极小化 Weil 二次型 Q(φ) (素数≤13), 得到 η, Mellin 变换零点逼近 ζ 零点
# Q(φ) = Σ_v W_v(ψ), ψ(v) = ∫φ(u)φ(uv)du/u
# W_p(f) = (log p)Σ_m p^{-m/2}[f(p^m)+f(p^{-m})]
# 参考: arXiv 2602.04022, Weil 显式公式 (9)(10)
import numpy as np

def build_weil_matrix(xmax=13.0, N=400, primes=None, include_arch=True):
    """离散化 u∈[1,xmax] (log 网格), 构造 Weil 二次型矩阵 A: Q(φ)=φ^T A φ
    Q(φ) = Σ_p (log p)Σ_m p^{-m/2} ∫[φ(u)φ(p^m u)+φ(u)φ(p^{-m}u)]du/u + W_R(ψ)
    缩放 T_a: (T_a φ)(u) = φ(au), 但积分域限制: φ 支撑 [1,xmax]
    用 log 坐标: x = log u ∈ [0, log xmax], T_a 变平移: φ(au) → x+log a
    """
    if primes is None:
        primes = [2,3,5,7,11,13]
    L = np.log(xmax)
    x = np.linspace(0, L, N)  # log u 网格
    dx = x[1] - x[0]
    # 质量矩阵 (∫φ²du/u = ∫φ̃²dx, φ̃(x)=φ(e^x))
    M = np.eye(N) * dx
    A = np.zeros((N, N))
    # 素数项: Σ_p (log p)Σ_m p^{-m/2}[ψ(p^m)+ψ(p^{-m})]
    # ψ(p^m) = ∫φ(u)φ(p^m u)du/u = ∫φ̃(x)φ̃(x+log(p^m))dx (若 x+log(p^m) ≤ L)
    for p in primes:
        lp = np.log(p)
        # m 范围: p^m ≤ xmax (使平移在域内非平凡)
        mmax = int(np.log(xmax)/lp) + 1
        for m in range(1, mmax+1):
            shift = m * lp
            w = lp * p**(-m/2.0)
            if shift < L:  # p^m 方向
                for i in range(N - int(shift/dx)):
                    j = i + int(round(shift/dx))
                    if j < N:
                        A[i,j] += w * dx  # ∫φ(x)φ(x+shift)dx 的离散
                        A[j,i] += w * dx
            # p^{-m} 方向 (对称, 由 A 对称性覆盖: 反向平移)
            # 已由 A[j,i] 项覆盖 (T_{p^{-m}} = T_{p^m}^T)
    # Archimedean 项 W_R(ψ): 简化为对角修正 (初步: 主项近似)
    # W_R(f) = (log 4π + γ)f(1) + ∫_1^∞ [f(x)+f(x^{-1})-2x^{-1/2}f(1)] x^{1/2}/(x-x^{-1}) d*x
    # 初步: 加入 f(1) 项的对角近似
    if include_arch:
        # f(1) 项: ψ(1) = ∫φ(u)φ(u)du/u = ||φ||²  → 对角
        gamma = 0.5772156649015329
        c1 = np.log(4*np.pi) + gamma
        # 核项: ∫∫ φ(u)φ(v) K(uv) 类 - 近似: 用 W_R 的离散核 (简化版)
        # 完整 W_R 核: k(u) = u^{1/2}/(u-u^{-1}) for u>1 类
        # 对 ψ(v)=∫φ(u)φ(uv)du/u, W_R 的核贡献 ≈ ∫∫ φ(u)φ(w) [核(u/w)类] du/u dw/w
        # 近似: 主对角 + 平滑修正 (完整 Archimedean 核后续加)
        A += c1 * M  # f(1) 项近似 (ψ(1) = ||φ||²)
        # 注: 完整的 W_R 核 (x^{1/2}/(x-x^{-1}) 类) 需要更仔细; 此项先占位
    return A, M, x

def smallest_eigvec(A, M, N):
    """广义最小特征向量: A η = λ M η (Rayleigh 极小化)"""
    # 用 Cholesky 转标准特征问题
    from scipy.linalg import eigh, cholesky
    Lc = cholesky(M, lower=True)
    # A η = λ M η → Lc^{-1} A Lc^{-T} (Lc^T η) = λ (Lc^T η)
    Linv = np.linalg.inv(Lc)
    A_std = Linv @ A @ Linv.T
    evals, evecs = eigh(A_std)
    eta_std = evecs[:, 0]
    eta = Linv.T @ eta_std  # 转回
    # 归一化: ∫η²du/u = 1 → η^T M η = 1
    norm = np.sqrt(eta @ M @ eta)
    eta = eta / norm
    return evals[0], eta

def mellin_zeros(eta, x, xmax, t_range=(5, 40), nt=2000):
    """M(η)(s) = ∫η(u)u^{s-1}du, s=1/2+it. 用 log 坐标:
    M(t) = ∫ φ̃(x) e^{(1/2+it)x} dx (φ̃(x)=φ(e^x), 支撑 [0,log xmax])
    找 |M(t)| 的零点 (符号变化)"""
    L = x[-1]
    # 高精度积分 (梯形)
    def Mval(t):
        integrand = eta * np.exp((0.5 + 1j*t) * x)
        return np.trapz(integrand, x)
    ts = np.linspace(t_range[0], t_range[1], nt)
    Ms = np.array([Mval(t) for t in ts])
    re = Ms.real
    # 找符号变化 (|M| 的零点 = 实部和虚部同时为0, 但临界线上只需 |M| 极小/实部过零)
    # 实际: M(1/2+it) 在零点处 Re=0 且 Im=0; 用 |M| 的局部极小检测
    mag = np.abs(Ms)
    zeros = []
    for i in range(1, nt-1):
        if mag[i] < mag[i-1] and mag[i] < mag[i+1] and mag[i] < 1e-3 * max(mag):
            zeros.append(ts[i])
    return np.array(zeros), ts, mag

if __name__ == "__main__":
    print("验证 Connes Letter: Weil 二次型极小化 (素数≤13)")
    xmax = 13.0
    for N in [200, 400]:
        print(f"\n--- N={N} ---")
        A, M, x = build_weil_matrix(xmax=xmax, N=N)
        lam, eta = smallest_eigvec(A, M, N)
        print(f"最小特征值 λ = {lam:.6e}")
        # Mellin 零点
        zeros, ts, mag = mellin_zeros(eta, x, xmax)
        # 真实 ζ 零点 (前几个)
        zeta_gamma = [14.134725, 21.022040, 25.010858, 30.424876, 32.935062,
                      37.586178, 40.918719, 43.327073, 48.005151, 49.773832]
        print(f"检测到 {len(zeros)} 个 Mellin 零点候选 (t∈[5,40])")
        print(f"{'Mellin 零点':>12} {'ζ 零点':>12} {'误差':>12}")
        for i, z in enumerate(zeros[:10]):
            ztrue = zeta_gamma[i] if i < len(zeta_gamma) else float('nan')
            err = abs(z - ztrue) if i < len(zeta_gamma) else float('nan')
            print(f"{z:>12.6f} {ztrue:>12.6f} {err:>12.2e}")
