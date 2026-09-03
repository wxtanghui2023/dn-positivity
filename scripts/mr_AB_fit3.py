#!/usr/bin/env python3
# 任务3 (fp 快速版): A,B 数值拟合
import numpy as np
from mpmath import fp as mpf

def off_fast(N, sigma0, gamma0, zp_re, zp_im, eps=0.05, n_pts=600, half_width=100.0):
    logN = np.log(N)
    zeta_pr = zp_re; zeta_pi = zp_im  # ζ'(ρ₊) = zeta_pr + i·zeta_pi
    rho_pr = sigma0; rho_pi = gamma0
    rho_mr = sigma0; rho_mi = -gamma0
    s0r = 0.5 - eps
    w = half_width
    ts = np.concatenate([np.linspace(-gamma0-w, -gamma0+w, n_pts//2),
                          np.linspace(gamma0-w, gamma0+w, n_pts//2)])
    dt = ts[1]-ts[0]
    total = 0j
    for t in ts:
        sr = s0r; si = float(t)
        # s = sr + i si
        # ρ₊−s = (rho_pr−sr) + i(rho_pi−si)
        # N^{ρ₊−s} = N^{(rho_pr−sr) + i(rho_pi−si)} = N^{rho_pr−sr}·e^{i(rho_pi−si)logN}
        # 复数运算手工
        def Npow(rr, ri):
            # N^{rr + i·ri}
            mag = N**rr
            return mag*np.cos(ri*logN) + 1j*mag*np.sin(ri*logN)
        # term1 = N^{ρ₊−s}/(ζ'(ρ₊)(ρ₊−s)²)
        dr = rho_pr - sr; di = rho_pi - si  # ρ₊−s
        denom_sq = (dr+1j*di)**2
        zp = zeta_pr + 1j*zeta_pi
        term1 = Npow(dr, di) / (zp * denom_sq)
        # term2: ρ₋−s
        dr2 = rho_mr - sr; di2 = rho_mi - si
        zm = zeta_pr - 1j*zeta_pi
        term2 = Npow(dr2, di2) / (zm * (dr2+1j*di2)**2)
        sig2_s = (term1 + term2) / logN
        # 1−s = (1−sr) − i·si
        smr = 1-sr; smi = -si
        # Σ(2)(1−s): ρ₊−(1−s) = rho_pr−smr + i(rho_pi−smi)
        d1r = rho_pr - smr; d1i = rho_pi - smi
        term1m = Npow(d1r, d1i) / (zp * (d1r+1j*d1i)**2)
        d2r = rho_mr - smr; d2i = rho_mi - smi
        term2m = Npow(d2r, d2i) / (zm * (d2r+1j*d2i)**2)
        sig2_sm = (term1m + term2m) / logN
        # ζ(s), ζ(1−s) 用 fp
        zs = complex(mpf.zeta(sr + 1j*si))
        zsm = complex(mpf.zeta(smr + 1j*smi))
        s = sr + 1j*si
        integrand = sig2_s * sig2_sm * zs * zsm / (s * (1-s))
        total += integrand * dt
    return total / (2*np.pi) / logN**2

if __name__ == "__main__":
    sigma0, gamma0 = 0.6, 50.0
    print(f"A,B fit (σ₀={sigma0}, γ₀={gamma0})")
    Ns = [200, 400, 800, 1600]
    for (m, theta) in [(1.0, 0), (1.0, 0.5), (1.0, 1.0), (1.0, 1.5), (2.0, 0.5), (0.5, 0.5)]:
        zpr, zpi = m*np.cos(theta), m*np.sin(theta)
        vals = []
        for N in Ns:
            v = off_fast(N, sigma0, gamma0, zpr, zpi)
            vals.append(v)
        ys, cs = [], []
        for N, v in zip(Ns, vals):
            y = float(v.real) / (N**(2*sigma0-1)/np.log(N)**2)
            ys.append(y); cs.append(np.cos(2*gamma0*np.log(N)))
        ys = np.array(ys); cs = np.array(cs)
        M = np.vstack([cs, np.ones_like(cs)]).T
        sol, *_ = np.linalg.lstsq(M, ys, rcond=None)
        A, B = sol
        print(f"ζ'={m:.1f}e^{theta:.1f}i: A={A:+.5f} B={B:+.5f} |A|={abs(A):.5f} {'<=B OK' if abs(A)<=B+1e-4 else '>B FAIL'}  A·m²={A*m*m:+.5f} B·m²={B*m*m:+.5f}")
