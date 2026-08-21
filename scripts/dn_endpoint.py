#!/usr/bin/env python3
"""
Decompose sum eps_m in phi-coordinate:
sum eps_m = int_{gamma1}^{t*} f dS = -f(gamma1)S(gamma1) - int f' S dt
In phi-coord (u = phi = (n+1/2)theta):
  int f' S dt = (1/(n+1/2)) int_{pi}^{phi_max} [phi cos(phi) + sin(phi)] S(t(phi)) dphi

Split: Endpoint term E = f(gamma1)*S(gamma1)  [O(1) bounded]
       Interior I = (1/(n+1/2)) * int_{pi}^{phi_max} [phi cosphi + sinphi] S(t(phi)) dphi

Numerically measure E and I separately, plus the oscillatory structure of I.
"""
import numpy as np, math

z = np.load('/home/node/.openclaw/workspace/dn-project/data/zeros_odlyzko_100k.npy')
def theta(t): return math.pi - 2*np.arctan(2*np.asarray(t, dtype=float))
def theta_RS(t):
    import mpmath as mp
    mp.mp.dps = 15
    return float(mp.im(mp.loggamma(mp.mpc(0.25, t/2))) - (t/2)*mp.log(mp.pi))
def S_of_t(t):
    return np.searchsorted(z, t, side='right') - theta_RS(t)/math.pi - 1
def t_of_phi(phi, n):
    th = phi/(n+0.5)
    return 0.5/np.tan(th/2)

def f_t(t, n):
    th = theta(t); phi = (n+0.5)*th
    return 2*np.sin(phi)*np.sin(th/2)

print("n        |E|=|f(g1)S(g1)|   |I|=|interior|   |E+I|   (eps sum)")
for n in [1000, 5000, 10000, 20000]:
    g1 = z[0]
    E = f_t(g1, n)*S_of_t(g1)
    phi_max = (n+0.5)*theta(g1)
    # interior: int_{pi}^{phi_max} [phi cosphi + sinphi] S(t(phi)) dphi, split at zeros
    # zeros in t-range [g1, t*]: their phi values
    tstar = (n+0.5)/math.pi
    zz = z[(z >= g1) & (z <= tstar)]
    phi_zeros = (n+0.5)*theta(zz)  # decreasing from phi_max to ~pi
    edges = np.concatenate([[phi_max], phi_zeros, [math.pi]])
    I = 0.0
    for i in range(len(edges)-1):
        a, b = edges[i], edges[i+1]  # phi from high to low
        if abs(a-b) < 1e-10: continue
        mid = 0.5*(a+b)
        Smid = S_of_t(t_of_phi(mid, n))
        phs = np.linspace(b, a, 200)  # increasing order for trapz
        kern = phs*np.cos(phs) + np.sin(phs)
        I += np.trapz(kern*Smid, phs)
    I = I/(n+0.5)
    # total eps sum from blocks
    th = theta(z); ph_all = (n+0.5)*th; f_all = 2*np.sin(ph_all)*np.sin(th/2)
    mask = ph_all >= math.pi
    m_idx = np.floor(ph_all[mask]/math.pi).astype(int); Mmax = m_idx.max()
    J = np.zeros(Mmax+1)
    for i,m in enumerate(m_idx): J[m] += f_all[mask][i]
    Jsm = np.zeros(Mmax+1)
    for m in range(1, Mmax+1):
        xi = (m+0.5)*math.pi
        Jsm[m] = (-1)**m*math.log((n+0.5)/(2*math.pi*xi))/(math.pi*xi)
    eps_sum = (J[1:]-Jsm[1:]).sum()
    print(f"{n:7d}  {abs(E):14.6f}  {abs(I):14.6f}  {abs(E+I):10.6f}  {eps_sum:+10.6f}")
