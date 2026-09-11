#!/usr/bin/env python3
"""
Provenance: retroactive archive header added 2026-09-11 by scripts/fix_archive_compliance.py
under the code-archive protocol (docs/PROTOCOL-CODE-ARCHIVE.md, R4).
The analysis itself was performed earlier; this header only records the file's existence
in the committed archive so that the computation is reproducible. Original code below.
"""
# 细扫描 γ₀: A/B = f(γ₀) 的形状 - 是否总 <1? 标度 (A~1/γ₀²?)
import numpy as np
from mpmath import fp as mpf

def off_fast(N, sigma0, gamma0, zpr=1.0, zpi=0.0, eps=0.05, n_pts=300, half_width=100.0):
    logN = np.log(N)
    rho_pr = sigma0; rho_pi = gamma0
    rho_mr = sigma0; rho_mi = -gamma0
    s0r = 0.5 - eps
    w = half_width
    # t 网格覆盖 ±γ₀ 主导区 (加宽 for larger γ₀)
    ts = np.concatenate([np.linspace(-gamma0-w, -gamma0+w, n_pts//2),
                          np.linspace(gamma0-w, gamma0+w, n_pts//2)])
    dt = ts[1]-ts[0]
    total = 0j
    zp = zpr + 1j*zpi; zm = zpr - 1j*zpi
    for t in ts:
        sr = s0r; si = float(t)
        def Npow(rr, ri):
            mag = N**rr
            return mag*np.cos(ri*logN) + 1j*mag*np.sin(ri*logN)
        dr = rho_pr - sr; di = rho_pi - si
        term1 = Npow(dr, di) / (zp * (dr+1j*di)**2)
        dr2 = rho_mr - sr; di2 = rho_mi - si
        term2 = Npow(dr2, di2) / (zm * (dr2+1j*di2)**2)
        sig2_s = (term1 + term2) / logN
        smr = 1-sr; smi = -si
        d1r = rho_pr - smr; d1i = rho_pi - smi
        term1m = Npow(d1r, d1i) / (zp * (d1r+1j*d1i)**2)
        d2r = rho_mr - smr; d2i = rho_mi - smi
        term2m = Npow(d2r, d2i) / (zm * (d2r+1j*d2i)**2)
        sig2_sm = (term1m + term2m) / logN
        zs = complex(mpf.zeta(sr + 1j*si))
        zsm = complex(mpf.zeta(smr + 1j*smi))
        s = sr + 1j*si
        integrand = sig2_s * sig2_sm * zs * zsm / (s * (1-s))
        total += integrand * dt
    return total / (2*np.pi) / logN**2

def fit_AB(sigma0, gamma0):
    # N 范围: 覆盖足够振荡 (γ₀ 小需更大 N)
    Ns = [200, 400, 800, 1600, 3200, 6400]
    vals = []
    for N in Ns:
        v = off_fast(N, sigma0, gamma0)
        vals.append(v)
    ys, cs = [], []
    for N, v in zip(Ns, vals):
        y = float(v.real) / (N**(2*sigma0-1)/np.log(N)**2)
        ys.append(y); cs.append(np.cos(2*gamma0*np.log(N)))
    ys = np.array(ys); cs = np.array(cs)
    M = np.vstack([cs, np.ones_like(cs)]).T
    sol, *_ = np.linalg.lstsq(M, ys, rcond=None)
    return sol[0], sol[1]

if __name__ == "__main__":
    sigma0 = 0.6
    print(f"细扫描 γ₀ (σ₀={sigma0}): A/B 比值 + 标度")
    print(f"{'γ₀':>6} {'A':>12} {'B':>12} {'|A|/B':>8} {'A·γ₀²':>12} {'B·γ₀²':>12}")
    gammas = list(range(15, 101, 5)) + [120, 150, 200]
    max_ratio = 0
    for gamma0 in gammas:
        try:
            A, B = fit_AB(sigma0, gamma0)
            ratio = abs(A)/B if B != 0 else float('inf')
            max_ratio = max(max_ratio, ratio)
            flag = " <-- >1!" if ratio > 1 else ""
            print(f"{gamma0:>6.0f} {A:>12.5f} {B:>12.5f} {ratio:>8.4f} {A*gamma0**2:>12.4f} {B*gamma0**2:>12.4f}{flag}")
        except Exception as e:
            print(f"{gamma0:>6.0f} err: {e}")
    print(f"\n最大 |A|/B = {max_ratio:.4f} ({'全部 <1' if max_ratio < 1 else '有 >1!'})")
