#!/usr/bin/env python3
"""
GLOBAL van der Corput: bound sum_m epsA_m = int_{gamma1}^{t*} A(t) cos(phi(t)) S(t) dt
directly, using phi monotone over WHOLE interval [gamma1, t*].
phi' = (n+1/2)theta', |phi'| >= (n+1/2)*4/(1+4 t*^2) ~ pi^2/n on whole range.

Global vdC: |int g cos(phi) dt| <= (2/|phi'|_min) * (|g(t*)| + |g(gamma1)| + V(g))
where g = A*S. But V(g) global ~ supA*V(S) + supS*V(A) — V(S) global saturates ~1000!

That gives ~ (2n/pi^2)*1000*supA ~ n*supA... supA ~ 2*4/(1+4*14^2)*(n)*sin(0.035) ~ 8/800*n*0.035 ~ 0.00035 n.
So bound ~ (2n/pi^2)*0.00035n*1000 ~ 70n^2?? No wait.

Let me actually compute the global vdC bound numerically vs true value.
Also try: integration by parts ONCE with M(T) replaced by S's primitive along the
SMOOTH part... Or: exact identity using phi as variable (u-substitution).
"""
import numpy as np, math

z = np.load('/home/node/.openclaw/workspace/dn-project/data/zeros_odlyzko_100k.npy')
def theta(t): return math.pi - 2*np.arctan(2*np.asarray(t, dtype=float))
def dtheta(t): return -4.0/(1+4*np.asarray(t, dtype=float)**2)
def theta_RS(t):
    import mpmath as mp
    mp.mp.dps = 18
    return float(mp.im(mp.loggamma(mp.mpc(0.25, t/2))) - (t/2)*mp.log(mp.pi))
def S_of_t(t):
    return np.searchsorted(z, t, side='right') - theta_RS(t)/math.pi - 1
def A_of_t(t, n): return 2*dtheta(t)*(n+0.5)*np.sin(theta(t)/2)

for n in [1000, 5000, 10000]:
    tstar = (n+0.5)/math.pi
    g1 = z[0]
    # TRUE global integral: int_{g1}^{t*} A cos(phi) S dt, split at zeros
    zz = z[(z >= g1) & (z <= tstar)]
    edges = np.concatenate([[g1], zz, [tstar]])
    true_val = 0.0
    for i in range(len(edges)-1):
        a, b = edges[i], edges[i+1]
        if b - a < 1e-10: continue
        Smid = S_of_t(0.5*(a+b))
        ts = np.linspace(a, b, 60)
        phs = (n+0.5)*theta(ts)
        true_val += np.trapz(A_of_t(ts, n)*np.cos(phs)*Smid, ts)
    # GLOBAL vdC bound (Stein form): |int g e^{i phi}| <= (C/|phi'|_min)(|g(b)|+|g(a)|+V(g))
    lam_min = (n+0.5)*4.0/(1+4*tstar*tstar)
    # V(g): g = A*S. Sample on grid
    ts = np.linspace(g1, tstar, 20000)
    Ss = np.array([S_of_t(t) for t in ts])
    g = A_of_t(ts, n)*Ss
    Vg = np.abs(np.diff(g)).sum()
    ga, gb = abs(g[0]), abs(g[-1])
    # Stein: C=4? Use both C=2 and C=4
    for C in [2, 4, 8]:
        bd = (C/lam_min)*(ga + gb + Vg)
        print(f"n={n}: true={true_val:+.5f}  vdC(C={C})={bd:.3f}  ratio={bd/max(abs(true_val),1e-9):.0f}  bd/logn={bd/math.log(n):.3f}")
    # diagnostics
    print(f"   lam_min={lam_min:.4f}, V(g)={Vg:.1f}, |g(g1)|={ga:.4f}, |g(t*)|={gb:.6f}")
    print()
