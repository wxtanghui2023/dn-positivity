#!/usr/bin/env python3
"""
EXACT chain: |sum eps| <= |E| + |interior|/n
interior/n = (1/(n+1/2)) * int phi sinphi S'(t) dt/dphi dphi  [unnormalized interior_un/n]

From earlier: interior_un = int_{pi}^{phi_max} phi sinphi * (-theta_RS'(t)/pi) * dt/dphi dphi
  dt/dphi = 1/((n+1/2)theta'(t)), theta_RS'(t) ~ (1/2)log(t/2pi), theta'(t) ~ -1/t^2
  interior_un ≈ (1/(2pi(n+1/2))) * int phi sinphi * t^2 log(t/2pi) dphi, t ~ n/phi
  interior_un ≈ (n^2/(2pi(n+1/2))) * int sinphi log(n/2pi phi)/phi dphi
  interior_un/(n+1/2) ≈ (n^2/(2pi(n+1/2)^2)) * J ≈ (1/2pi) * J,  J = int sinphi g dphi

So |interior|/n ≈ |J|/(2pi) <= 2g(pi)/(2pi) = g(pi)/pi = log(n/2pi^2)/pi^2  -- the bound I used.

Let me verify the NUMERICAL conversion: |interior_un|/(n+0.5) vs |J|/(2pi):
"""
import numpy as np, math

z = np.load('/home/node/.openclaw/workspace/dn-project/data/zeros_odlyzko_100k.npy')
def theta(t): return math.pi - 2*np.arctan(2*np.asarray(t, dtype=float))
def dtheta(t): return -4.0/(1+4*np.asarray(t, dtype=float)**2)
def theta_RS(t):
    import mpmath as mp
    mp.mp.dps = 15
    return float(mp.im(mp.loggamma(mp.mpc(0.25, t/2))) - (t/2)*mp.log(mp.pi))
def dtheta_RS(t):
    import mpmath as mp
    mp.mp.dps = 15
    return float(mp.re(mp.digamma(mp.mpc(0.25, t/2)))/2 - mp.log(mp.pi)/2)
def S_of_t(t):
    return np.searchsorted(z, t, side='right') - theta_RS(t)/math.pi - 1
def t_of_phi(phi, n):
    th = phi/(n+0.5)
    return 0.5/np.tan(th/2)

def g(phi, n):
    A = n/(2*math.pi)
    return np.log(A/np.maximum(phi,1e-12))/np.maximum(phi,1e-12)

print("n        |interior|/n   |J|/(2pi)   ratio   2g(pi)/(2pi)=g(pi)/pi")
for n in [1000, 5000, 10000]:
    g1 = z[0]; phi_max = (n+0.5)*theta(g1); tstar = (n+0.5)/math.pi
    zz = z[(z >= g1) & (z <= tstar)]
    phi_zeros = (n+0.5)*theta(zz)
    edges = np.concatenate([[phi_max], phi_zeros, [math.pi]])
    interior_un = 0.0
    for i in range(len(edges)-1):
        a, b = edges[i], edges[i+1]
        if abs(a-b) < 1e-10: continue
        mid = t_of_phi(0.5*(a+b), n)
        Sp = -dtheta_RS(mid)/math.pi
        phs = np.linspace(b, a, 200)
        ts = t_of_phi(phs, n)
        dt_dphi = 1.0/((n+0.5)*dtheta(ts))
        interior_un += np.trapz(phs*np.sin(phs)*Sp*dt_dphi, phs)
    interior_n = abs(interior_un)/(n+0.5)
    phis = np.linspace(math.pi, phi_max, 300000)
    J = np.trapz(np.sin(phis)*g(phis, n), phis)
    J2pi = abs(J)/(2*math.pi)
    gp = g(math.pi, n)/math.pi
    print(f"{n:7d} {interior_n:12.6f} {J2pi:10.6f} {interior_n/max(J2pi,1e-9):6.3f} {gp:12.6f}")
