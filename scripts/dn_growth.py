#!/usr/bin/env python3
"""Growth law of sum|eps_m| and |sum eps_m| over n."""
import numpy as np, math

z = np.load('/home/node/.openclaw/workspace/dn-project/data/zeros_odlyzko_100k.npy')
def theta(t): return math.pi - 2*np.arctan(2*np.asarray(t, dtype=float))
def theta_RS(t):
    import mpmath as mp
    mp.mp.dps = 15
    return float(mp.im(mp.loggamma(mp.mpc(0.25, t/2))) - (t/2)*mp.log(mp.pi))
def S_of_t(t):
    return np.searchsorted(z, t, side='right') - theta_RS(t)/math.pi - 1

def blocks_eps(n):
    th = theta(z)
    phi = (n+0.5)*th
    f = 2*np.sin(phi)*np.sin(th/2)
    mask = phi >= math.pi
    phi_n, f_n = phi[mask], f[mask]
    m_idx = np.floor(phi_n/math.pi).astype(int)
    Mmax = m_idx.max() if len(m_idx) else 0
    J = np.zeros(Mmax+1)
    for i, m in enumerate(m_idx): J[m] += f_n[i]
    Jsm = np.zeros(Mmax+1)
    for m in range(1, Mmax+1):
        xi = (m+0.5)*math.pi
        Jsm[m] = (-1)**m * math.log((n+0.5)/(2*math.pi*xi))/(math.pi*xi)
    return J[1:] - Jsm[1:]

print("n        M'      sum|eps|   |sum eps|  sum|eps|/logn  |sum|/logn")
for n in [100, 200, 500, 1000, 2000, 5000, 10000, 20000]:
    eps = blocks_eps(n)
    s_abs = np.abs(eps).sum()
    s_sum = abs(eps.sum())
    Mprime = len(eps)
    print(f"{n:7d} {Mprime:6d} {s_abs:10.4f} {s_sum:10.4f} {s_abs/math.log(n):12.4f} {s_sum/math.log(n):10.4f}")
