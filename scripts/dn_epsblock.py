#!/usr/bin/env python3
"""
Last-step analysis: block structure of epsilon_m = J_m - J_m^smooth.

Goal: find a strictifiable pattern in epsilon_m (alternation, decay, cancellation)
to prove sum|epsilon_m| = O(1) or |sum epsilon_m| <= c log n with c < 0.1934.

D_neg blocks: B_m = {phi in (m*pi,(m+1)*pi)}, phi = (n+1/2)*theta, m = 1..M
J_m = sum_{k in B_m} f~(theta_k),  f~(theta) = 2 sin(phi) sin(theta/2)
J_m^smooth = (-1)^m g(xi_m), g(u) = log((n+1/2)/(2*pi*u))/(pi*u), xi_m = midpoint
epsilon_m = J_m - J_m^smooth
"""
import numpy as np, math

z = np.load('/home/node/.openclaw/workspace/dn-project/data/zeros_odlyzko_100k.npy')

def theta(t): return math.pi - 2*math.atan(2*t)

def analyze(n, verbose=True):
    th = np.array([theta(g) for g in z])          # theta_k decreasing
    phi = (n+0.5)*th                               # phase at zeros
    f = 2*np.sin(phi)*np.sin(th/2.0)               # f~(theta_k)
    # negative region: phi >= pi  =>  theta <= theta_* = pi/(n+0.5)
    mask = phi >= math.pi
    phi_n, f_n, th_n = phi[mask], f[mask], th[mask]
    # block index for each zero
    m_idx = np.floor(phi_n/math.pi).astype(int)    # block m (>=1)
    Mmax = m_idx.max() if len(m_idx) else 0
    J = np.zeros(Mmax+1); cnt = np.zeros(Mmax+1)
    for i, m in enumerate(m_idx):
        J[m] += f_n[i]; cnt[m] += 1
    # smooth main term at block midpoint
    Jsm = np.zeros(Mmax+1)
    for m in range(1, Mmax+1):
        xi = (m+0.5)*math.pi
        Jsm[m] = (-1)**m * math.log((n+0.5)/(2*math.pi*xi))/(math.pi*xi)
    eps = J[1:Mmax+1] - Jsm[1:Mmax+1]
    mlist = np.arange(1, Mmax+1)
    if verbose:
        print(f"n={n}: 负区零点数={len(phi_n)}, 块数 M={Mmax}")
        print(f"  {'m':>4} {'J_m':>10} {'Jsm':>10} {'eps_m':>10} {'sign':>4} {'(-1)^m':>6} {'cnt':>5}")
        for i in range(min(10, Mmax)):
            m = mlist[i]
            sgn = '+' if eps[i]>=0 else '-'
            alt = '+' if (-1)**m>=0 else '-'
            print(f"  {m:4d} {J[m]:10.5f} {Jsm[m]:10.5f} {eps[i]:10.5f} {sgn:>4} {alt:>6} {int(cnt[m]):5d}")
        print("  ...")
        for i in range(max(0,Mmax-5), Mmax):
            m = mlist[i]
            print(f"  {m:4d} {J[m]:10.5f} {Jsm[m]:10.5f} {eps[i]:10.5f} {'+/-':>4} {int(cnt[m]):5d}")
    # aggregates
    S_abs = np.abs(eps).sum()
    S_sum = eps.sum()
    S_absJ = np.abs(J[1:]).sum()
    # correlation of eps with (-1)^m
    corr = np.sum(eps * ((-1.0)**mlist)) / (np.linalg.norm(eps)*np.sqrt(len(eps))) if len(eps)>1 else 0
    # last block partial sums
    psum = np.cumsum(eps)
    print(f"  Σ|eps_m| = {S_abs:.5f}   |Σ eps_m| = {abs(S_sum):.5f}   Σ|J_m| = {S_absJ:.5f}")
    print(f"  max|cumsum eps| = {np.abs(psum).max():.5f}   corr(eps,(-1)^m) = {corr:+.3f}")
    print(f"  参考: log n/π² = {math.log(n)/math.pi**2:.5f}, margin 0.1934·logn = {0.1934*math.log(n):.5f}")
    return S_abs, abs(S_sum)

print("="*70)
for n in [1000, 5000, 10000, 20000]:
    analyze(n)
    print("-"*70)
