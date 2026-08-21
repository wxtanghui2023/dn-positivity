#!/usr/bin/env python3
# Verify: |C(n) - C∞| decay rate. van der Corput predicts O(log n / n^{3/2}).
# Test numerically: compute C(n) at large n, fit decay.
import numpy as np
from scipy import integrate
import mpmath as mp
mp.mp.dps = 20

zeros = np.load('/tmp/zeros_odlyzko_100k.npy')
gmax = float(zeros[-1]); g1 = float(zeros[0])

def theta_prime_asy(t):
    return 0.5*np.log(t/(2*np.pi)) - 1/(48*t*t) - 7/(1920*t**4)
def theta_prime_mp(t):
    z = mp.mpf('0.25') + 1j*mp.mpf(t)/2
    return float(mp.re(mp.psi(0, z))/2 - mp.log(mp.pi)/2)
def sinc(x):
    return np.where(x==0, 1.0, np.sin(x)/x)

STEP = 0.25
tg = np.arange(0.0, gmax, STEP)
tp = np.zeros_like(tg)
small = tg < 50
for i in np.nonzero(small)[0]:
    tp[i] = theta_prime_mp(float(tg[i]))
tp[~small] = theta_prime_asy(tg[~small])

def C_of_n(n):
    m = tg < g1
    A = -np.trapz(tp[m]*sinc(tg[m]/n), tg[m])/np.pi
    return np.sum(sinc(zeros/n)) - np.trapz(tp*sinc(tg/n), tg)/np.pi - A + sinc(g1/n)

# C(n) for large n; truncation at gmax=74921: for n large, sinc(γ/n) tail beyond gmax matters
# Use n up to ~15000 where gmax/n >= 5
ns = [100, 200, 500, 1000, 2000, 5000, 8000, 12000, 15000]
Cvals = [C_of_n(n) for n in ns]
print(f"{'n':>7} {'C(n)':>10} {'C(n)-C(15000)':>14} {'·n^1.5':>10} {'·n^0.5':>10}")
Cref = Cvals[-1]
for n, C in zip(ns, Cvals):
    d = C - Cref
    print(f"{n:7d} {C:+10.4f} {d:+14.6f} {d*n**1.5:+10.3f} {d*n**0.5:+10.3f}")

# fit exponent: log|C(n)-Cref| vs log n for the tail
import math
print("\nlocal decay exponent (between consecutive large n):")
for i in range(4, len(ns)-1):
    n1, n2 = ns[i], ns[i+1]
    d1, d2 = abs(Cvals[i]-Cref), abs(Cvals[i+1]-Cref)
    if d1 > 0 and d2 > 0:
        exp = math.log(d1/d2)/math.log(n2/n1)
        print(f"  n {n1}->{n2}: exponent ≈ {exp:+.2f}")
