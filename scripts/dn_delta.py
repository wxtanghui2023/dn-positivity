#!/usr/bin/env python3
"""Delta = D_pos - Main_pos check."""
import numpy as np, math

z = np.load('/home/node/.openclaw/workspace/dn-project/data/zeros_odlyzko_100k.npy')
def theta(t): return math.pi - 2*np.arctan(2*np.asarray(t, dtype=float))
def dtheta(t): return -4.0/(1+4*np.asarray(t, dtype=float)**2)
def theta_RS(t):
    import mpmath as mp
    mp.mp.dps = 15
    return float(mp.im(mp.loggamma(mp.mpc(0.25, t/2))) - (t/2)*mp.log(mp.pi))
def dtheta_RS_arr(t):
    import mpmath as mp
    mp.mp.dps = 15
    return np.array([float(mp.re(mp.digamma(mp.mpc(0.25, x/2)))/2 - mp.log(mp.pi)/2) for x in t])
def S_of_t(t):
    return np.searchsorted(z, t, side='right') - theta_RS(t)/math.pi - 1
def f_of_t(t, n):
    th = theta(t); phi = (n+0.5)*th
    return 2*np.sin(phi)*np.sin(th/2)
def fprime_of_t(t, n):
    th = theta(t); dth = dtheta(t); phi = (n+0.5)*th
    A = 2*dth*(n+0.5)*np.sin(th/2); B = 2*dth*0.5*np.cos(th/2)
    return A*np.cos(phi) + B*np.sin(phi)

print("n        D_pos      Main_pos    Delta     |Delta|    |Delta|/(logn/n)   bound=supS·∫|f'|")
for n in [100, 500, 1000, 5000, 10000, 20000]:
    tstar = (n+0.5)/math.pi
    th = theta(z); phi = (n+0.5)*th
    mask_pos = phi < math.pi
    D_pos = (2*np.sin(phi[mask_pos])*np.sin(th[mask_pos]/2)).sum()
    gmax = z[-1]
    ts = np.linspace(tstar, gmax, 30000)
    Main_pos = np.trapz(f_of_t(ts, n)*dtheta_RS_arr(ts), ts)/math.pi
    Delta = D_pos - Main_pos
    # bound
    supS = max(abs(S_of_t(t)) for t in np.linspace(tstar, gmax, 300))
    ts2 = np.linspace(tstar, gmax, 30000)
    int_fp = np.trapz(np.abs(fprime_of_t(ts2, n)), ts2)
    bd = supS * int_fp
    print(f"{n:7d} {D_pos:+10.5f} {Main_pos:+10.5f} {Delta:+10.5f} {abs(Delta):9.5f} {abs(Delta)/(math.log(n)/n):12.4f} {bd:10.5f}")
