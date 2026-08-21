#!/usr/bin/env python3
# Check: for n >= 10, is C(n) > 0.4497 always? And n·D_n > 0 for ALL n?
import numpy as np
from scipy import integrate
import mpmath as mp
mp.mp.dps = 20

zeros = np.load('/tmp/zeros_odlyzko_100k.npy')
gmax = float(zeros[-1]); g1 = float(zeros[0])

def theta_prime_asy(t):
    return 0.5*np.log(t/(2*np.pi)) - 1/(48*t*t) - 7/(1920*t**4) - 31/(16128*t**6)
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

def ndn(n):
    return np.sum(sinc(zeros/n)) - np.trapz(tp*sinc(tg/n), tg)/np.pi

def C_of_n(n):
    m = tg < g1
    A = -np.trapz(tp[m]*sinc(tg[m]/n), tg[m])/np.pi
    return ndn(n) - A + sinc(g1/n)

# dense scan n=10..8000
ns = list(range(10, 101, 1)) + list(range(100, 1001, 10)) + list(range(1000, 8001, 100))
Cmin = 1e9; Cmin_n = None; Dmin = 1e9; Dmin_n = None; Dmax = -1e9
for n in ns:
    C = C_of_n(n)
    D = ndn(n)
    if C < Cmin: Cmin, Cmin_n = C, n
    if D < Dmin: Dmin, Dmin_n = D, n
    if D > Dmax: Dmax = D
print(f"n ∈ [10, 8000]: {len(ns)} values")
print(f"  min C(n) = {Cmin:.6f} at n={Cmin_n}   (threshold 0.4497)")
print(f"  min n·D_n = {Dmin:.6f} at n={Dmin_n}")
print(f"  max n·D_n = {Dmax:.6f}")
print(f"  → C(n) > 0.4497 for all n≥10: {Cmin > 0.4497}")
print(f"  → n·D_n > 0 for all n≥10: {Dmin > 0}")
