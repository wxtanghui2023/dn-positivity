#!/usr/bin/env python3
"""
Measure the ACTUAL constants for the oscillation-cancellation bound.

Target: |sum eps_m| = |int S f~' dtheta| <= c * log n with EXPLICIT small c < 0.19.
If the measured constant is small enough, an explicit van der Corput /
integration-by-parts estimate with numerical constants might close the gap.

We measure:
1. |int S f~' dtheta| / log n   (the actual ratio)
2. The endpoint terms |f~(theta1) S(theta1)| 
3. V(S) on the negative region (total variation) / (n log n) constant
4. The "second IBP" constants: M(T) boundedness scale

All in theta-coordinate: negative region theta in [theta*, theta1].
"""
import numpy as np, math

z = np.load('/home/node/.openclaw/workspace/dn-project/data/zeros_odlyzko_100k.npy')
def theta(t): return math.pi - 2*np.arctan(2*np.asarray(t, dtype=float))

def theta_RS(t):
    import mpmath as mp
    mp.mp.dps = 18
    return float(mp.im(mp.loggamma(mp.mpc(0.25, t/2))) - (t/2)*mp.log(mp.pi))

def S_of_t(t):
    t = float(t)
    return np.searchsorted(z, t, side='right') - theta_RS(t)/math.pi - 1

def S_of_theta(th):
    t = 0.5/math.tan(th/2)   # inverse of theta
    return S_of_t(t)

def f_tilde(th, n):
    phi = (n+0.5)*th
    return 2*np.sin(phi)*np.sin(th/2)

def f_tilde_prime(th, n):
    phi = (n+0.5)*th
    return 2*(n+0.5)*np.cos(phi)*np.sin(th/2) + np.sin(phi)*np.cos(th/2)

for n in [1000, 5000, 10000, 20000]:
    th1 = theta(z[0])
    th_star = math.pi/(n+0.5)
    # S samples on grid (theta increasing = t decreasing)
    ths = np.linspace(th_star, th1, 4000)
    Ss = np.array([S_of_theta(th) for th in ths])
    # sum eps = -f~(th1) S(th1) - int S f~' (IBP)
    fp = f_tilde_prime(ths, n)
    I = np.trapz(Ss*fp, ths)
    f1 = f_tilde(th1, n); S1 = Ss[-1]  # at th1
    sum_eps = -f1*S1 - I
    # V(S): total variation
    V = np.abs(np.diff(Ss)).sum()
    # actual ratio
    r = abs(sum_eps)/math.log(n)
    # endpoint
    ep = abs(f1*S1)
    # V(S)/(n log n)
    Vnl = V/(n*math.log(n))
    # f~' L1 norm
    L1 = np.trapz(np.abs(fp), ths)
    print(f"n={n:6d}: |Σε|={abs(sum_eps):.5f}  /logn={r:.5f}  |端|={ep:.5f}  ∫|f̃'|={L1:.4f}  V(S)={V:.1f}  V/(nlogn)={Vnl:.5f}")
