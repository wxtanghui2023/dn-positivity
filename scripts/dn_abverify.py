#!/usr/bin/env python3
"""
Verify the A/B decomposition: epsilon_m = -int_{B_m} f' S dt
f' = A cosφ + B sinφ
A项(振荡): -int A_m cosφ S dt,  A_m = 2θ'(n+½)sin(θ/2)
B项(同号): -int B_m sinφ S dt,  B_m = θ'cos(θ/2)

Check: (1) identity epsilon_m = -int f'S dt
       (2) A/B split: which dominates? signs?
       (3) sum over m of A-part and B-part separately
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

def fprime(t, n):
    th = theta(t); dth = dtheta(t); phi = (n+0.5)*th
    A = 2*dth*(n+0.5)*np.sin(th/2)
    B = 2*dth*0.5*np.cos(th/2)
    return A*np.cos(phi) + B*np.sin(phi), A, B, phi

def t_of_phi(phi, n):
    th = phi/(n+0.5)
    return 0.5/np.tan(th/2)

for n in [1000, 5000]:
    # blocks m=1..M'
    Mprime = int(math.floor((n+0.5)*theta(z[0])/math.pi))
    t1 = t_of_phi(math.pi, n)
    epsA_sum = epsB_sum = 0.0
    print(f"\nn={n}: M'={Mprime}")
    print(f"  {'m':>4} {'epsA':>10} {'epsB':>10} {'epsA+epsB':>10} {'eps_dir':>10}")
    for m in range(1, min(Mprime, 12)+1):
        ta = t_of_phi((m+1)*math.pi, n); tb = t_of_phi(m*math.pi, n)
        ts = np.linspace(ta, tb, 4000)
        Ss = np.array([S_of_t(t) for t in ts])
        fp, A, B, phi = fprime(ts, n)
        epsA = -np.trapz(A*np.cos(phi)*Ss, ts)
        epsB = -np.trapz(B*np.sin(phi)*Ss, ts)
        # direct: eps_m from block sums
        th_all = theta(z); ph_all = (n+0.5)*th_all; f_all = 2*np.sin(ph_all)*np.sin(th_all/2)
        mask = np.floor(ph_all/math.pi).astype(int) == m
        eps_dir = f_all[mask].sum() - (-1)**m * math.log((n+0.5)/(2*math.pi*(m+0.5)*math.pi))/(math.pi*(m+0.5)*math.pi)
        if m <= 10:
            print(f"  {m:4d} {epsA:10.5f} {epsB:10.5f} {epsA+epsB:10.5f} {eps_dir:10.5f}")
        epsA_sum += epsA; epsB_sum += epsB
    print(f"  ΣepsA = {epsA_sum:+.5f}   ΣepsB = {epsB_sum:+.5f}   Σ = {epsA_sum+epsB_sum:+.5f}")
