#!/usr/bin/env python3
"""
High-precision A-part analysis: epsA_m = -int A cosφ S dt
A = 2θ'(n+½)sin(θ/2). Key: is |epsA_m| small? van der Corput structure?
Since A cosφ has EXACT oscillation (cosφ zero-crossing in block), use
analytic integration: int A cosφ S dt, S slowly varying + jumps.
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

def t_of_phi(phi, n):
    th = phi/(n+0.5)
    return 0.5/np.tan(th/2)

for n in [1000, 5000, 10000]:
    Mprime = int(math.floor((n+0.5)*theta(z[0])/math.pi))
    epsA_vals = []
    for m in range(1, Mprime+1):
        ta = t_of_phi((m+1)*math.pi, n); tb = t_of_phi(m*math.pi, n)
        if tb - ta < 1e-8: continue
        # fine grid, but S jumps at zeros -> use midpoints between zeros
        # zero positions in [ta, tb]
        zz = z[(z >= ta) & (z <= tb)]
        # integrate A cosφ S over intervals between consecutive zeros + edges
        edges = np.concatenate([[ta], zz, [tb]])
        val = 0.0
        for i in range(len(edges)-1):
            a, b = edges[i], edges[i+1]
            if b - a < 1e-10: continue
            tmid = 0.5*(a+b)
            Smid = S_of_t(tmid)  # S constant between zeros? S = N - θ_RS/π -1, N const, θ_RS smooth => S smooth between zeros
            ts = np.linspace(a, b, 50)
            ths = theta(ts); dths = dtheta(ts); phs = (n+0.5)*ths
            A = 2*dths*(n+0.5)*np.sin(ths/2)
            val += -np.trapz(A*np.cos(phs)*Smid, ts)  # S ~ const in sub-interval
        epsA_vals.append((m, val))
    S_A = sum(v for _,v in epsA_vals)
    S_absA = sum(abs(v) for _,v in epsA_vals)
    print(f"n={n}: M'={Mprime}, ΣepsA = {S_A:+.5f}, Σ|epsA| = {S_absA:.5f}")
    print(f"  前8块: {[f'{v:+.4f}' for _,v in epsA_vals[:8]]}")
