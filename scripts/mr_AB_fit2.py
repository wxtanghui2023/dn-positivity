#!/usr/bin/env python3
"""
Provenance: retroactive archive header added 2026-09-11 by scripts/fix_archive_compliance.py
under the code-archive protocol (docs/PROTOCOL-CODE-ARCHIVE.md, R4).
The analysis itself was performed earlier; this header only records the file's existence
in the committed archive so that the computation is reproducible. Original code below.
"""
# 任务3 (优化版): A,B 数值拟合 - 积分聚焦 t~γ₀ 主导区
import numpy as np
import mpmath as mp

mp.mp.dps = 15

def off_dominant_fast(N, sigma0, gamma0, zp, eps=0.05, n_pts=2000, half_width=150.0):
    """I(N) 数值 - 聚焦 t ~ ±γ₀ 区域 (分母主导)"""
    logN = float(mp.log(N))
    zeta_p = zp
    zeta_m = mp.conj(zp)
    rho_p = sigma0 + 1j*gamma0
    rho_m = sigma0 - 1j*gamma0
    s0r = 0.5 - eps
    # t 网格: 覆盖 -γ₀±w 和 +γ₀±w (两个主导区)
    w = half_width
    ts1 = np.linspace(-gamma0-w, -gamma0+w, n_pts//2)
    ts2 = np.linspace(gamma0-w, gamma0+w, n_pts//2)
    ts = np.concatenate([ts1, ts2])
    dt1 = ts1[1]-ts1[0]
    total = 0j
    for t in ts:
        s = s0r + 1j*float(t)
        sm = 1 - s
        # Σ(2)(s)
        t1p = N**(rho_p - s) / (zeta_p * (rho_p - s)**2)
        t1m = N**(rho_m - s) / (zeta_m * (rho_m - s)**2)
        sig2_s = (t1p + t1m) / logN
        # Σ(2)(1-s)
        t2p = N**(rho_p - sm) / (zeta_p * (rho_p - sm)**2)
        t2m = N**(rho_m - sm) / (zeta_m * (rho_m - sm)**2)
        sig2_sm = (t2p + t2m) / logN
        zs = mp.zeta(s); zsm = mp.zeta(sm)
        integrand = sig2_s * sig2_sm * zs * zsm / (s * sm)
        total += integrand * dt1
    return total / (2*mp.pi) / logN**2

if __name__ == "__main__":
    sigma0, gamma0 = 0.6, 50.0
    print(f"A,B 拟合 (σ₀={sigma0}, γ₀={gamma0}) - 不同 ζ'(ρ)")
    Ns = [200, 400, 800, 1600]
    for (m, theta) in [(1.0, 0), (1.0, 0.5), (1.0, 1.0), (1.0, 1.5), (2.0, 0.5), (0.5, 0.5)]:
        zp = mp.mpc(m*np.cos(theta), m*np.sin(theta))
        vals = []
        ok = True
        for N in Ns:
            try:
                v = off_dominant_fast(N, sigma0, gamma0, zp)
                vals.append(v)
            except Exception as e:
                print(f"  err N={N}: {e}")
                ok = False
                break
        if not ok: continue
        # 拟合 y = A cos + B (y = I·log²N/N^{2σ₀−1})
        ys, cs = [], []
        for N, v in zip(Ns, vals):
            y = float(v.real) / (N**(2*sigma0-1)/np.log(N)**2)
            ys.append(y); cs.append(np.cos(2*gamma0*np.log(N)))
        ys = np.array(ys); cs = np.array(cs)
        M = np.vstack([cs, np.ones_like(cs)]).T
        sol, *_ = np.linalg.lstsq(M, ys, rcond=None)
        A, B = sol
        # 归一化: 除 m² (ζ' 大小²)? 检查 A,B 是否 ~1/m²
        print(f"ζ'={m:.1f}e^{theta:.1f}i: A={A:+.5f} B={B:+.5f} |A|={abs(A):.5f} {'≤B ✓' if abs(A)<=B+1e-6 else '>B ✗'}  A·m²={A*m*m:+.5f} B·m²={B*m*m:+.5f}")
