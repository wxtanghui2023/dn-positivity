#!/usr/bin/env python3
"""
Provenance: retroactive archive header added 2026-09-11 by scripts/fix_archive_compliance.py
under the code-archive protocol (docs/PROTOCOL-CODE-ARCHIVE.md, R4).
The analysis itself was performed earlier; this header only records the file's existence
in the committed archive so that the computation is reproducible. Original code below.
"""
# 任务3: A,B 显式形式数值推导 - 离轴主导项 I(N) = ∫ Σ(2)·Σ(2)·ζζ/(s(1-s))
# 检查 |A| ≤ B 约束 - 与 ζ'(ρ) 相位/大小的关系
import numpy as np
import mpmath as mp

mp.mp.dps = 25

def Sigma2(N, s, sigma0, gamma0, zeta_p):
    """Σ(2)(N,s) = (1/logN)[N^{ρ+−s}/(ζ'(ρ+)(ρ+−s)²) + N^{ρ−−s}/(ζ'(ρ−)(ρ−−s)²)]
    ρ+ = σ₀+iγ₀, ρ− = σ₀−iγ₀, ζ'(ρ−) = conj(ζ'(ρ+))"""
    logN = mp.log(N)
    rho_p = sigma0 + 1j*gamma0
    rho_m = sigma0 - 1j*gamma0
    zp = zeta_p  # ζ'(σ₀+iγ₀)
    zm = mp.conj(zp)
    term1 = N**(rho_p - s) / (zp * (rho_p - s)**2)
    term2 = N**(rho_m - s) / (zm * (rho_m - s)**2)
    return (term1 + term2) / logN

def off_line_dominant(N, sigma0, gamma0, zeta_p, eps=0.05, t_max=500, n_pts=3000):
    """I(N) = (1/2πi)∫_{½−ε} Σ(2)(s)Σ(2)(1−s)ζ(s)ζ(1−s)/(s(1−s)) ds / log²N"""
    logN = mp.log(N)
    # 数值积分 (垂直线 s = ½−ε+it)
    ts = np.linspace(-t_max, t_max, n_pts)
    dt = ts[1] - ts[0]
    total = 0j
    s0_real = 0.5 - eps
    for t in ts:
        s = s0_real + 1j*float(t)
        sm = 1 - s
        sig2_s = Sigma2(N, s, sigma0, gamma0, zeta_p)
        sig2_sm = Sigma2(N, sm, sigma0, gamma0, zeta_p)
        zeta_s = mp.zeta(s)
        zeta_sm = mp.zeta(sm)
        integrand = sig2_s * sig2_sm * zeta_s * zeta_sm / (s * sm)
        total += integrand * dt
    # 1/2πi ∫ ... ds = 1/2π ∫ ... dt (ds = i dt)
    return total / (2*mp.pi) / logN**2

def fit_AB(Ns, vals, sigma0, gamma0):
    """拟合: vals ~ (A·cos(2γ₀logN) + B)·N^{2σ₀−1}/log²N
    先除 N^{2σ₀−1}/log²N → y = A cos + B"""
    ys = []
    cosvals = []
    for N, v in zip(Ns, vals):
        y = v / (N**(2*sigma0-1) / np.log(N)**2)
        ys.append(float(y.real))
        cosvals.append(np.cos(2*gamma0*np.log(N)))
    ys = np.array(ys); cosvals = np.array(cosvals)
    # 最小二乘: y = A·cos + B
    M = np.vstack([cosvals, np.ones_like(cosvals)]).T
    sol, res, rank, sv = np.linalg.lstsq(M, ys, rcond=None)
    A, B = sol
    return A, B

if __name__ == "__main__":
    sigma0, gamma0 = 0.6, 50.0
    print(f"=== 离轴主导项 A,B 数值拟合 (σ₀={sigma0}, γ₀={gamma0}) ===")
    print(f"|A|≤B 约束检查 - 不同 ζ'(ρ) 相位/大小\n")
    
    # ζ'(ρ) 的候选: 相位 θ, 大小 m
    for (m, theta) in [(1.0, 0), (1.0, 0.5), (1.0, 1.0), (2.0, 0.3), (0.5, 1.2)]:
        zp = m * np.exp(1j*theta)
        # 数值算 I(N) 对几个 N
        Ns = [100, 200, 400, 800, 1600, 3200]
        vals = []
        for N in Ns:
            try:
                v = off_line_dominant(N, sigma0, gamma0, mp.mpc(zp.real, zp.imag))
                vals.append(v)
            except Exception as e:
                vals.append(0j)
        try:
            A, B = fit_AB(Ns, vals, sigma0, gamma0)
            print(f"ζ'={m:.1f}e^{theta:.1f}i: A={A:+.4f} B={B:+.4f} |A|={abs(A):.4f} {'|A|≤B ✓' if abs(A)<=B else '|A|>B ✗'}")
        except Exception as e:
            print(f"ζ'={m:.1f}e^{theta:.1f}i: fit failed ({e})")
