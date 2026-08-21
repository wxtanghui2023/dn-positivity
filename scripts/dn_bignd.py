#!/usr/bin/env python3
# CRITICAL: n·D_n at large n (100..60000). Does it stay > 0? Does C(n) really wander?
import numpy as np
from scipy import integrate
import mpmath as mp
mp.mp.dps = 20

zeros = np.load('/tmp/zeros_odlyzko_100k.npy')
gmax = float(zeros[-1]); g1 = float(zeros[0])

def theta_asy(t):
    return 0.5*t*np.log(t/(2*np.pi)) - 0.5*t - np.pi/8 + 1/(48*t) + 7/(5760*t**3) + 31/(80640*t**5)
def theta_prime_asy(t):
    return 0.5*np.log(t/(2*np.pi)) - 1/(48*t*t) - 7/(1920*t**4) - 31/(16128*t**6)
def theta_mp(t):
    z = mp.mpf('0.25') + 1j*mp.mpf(t)/2
    return float(mp.im(mp.loggamma(z)) - mp.mpf(t)/2*mp.log(mp.pi))
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

print(f"{'n':>7} {'n·D_n':>10} {'γmax/n':>8} {'S(n)':>8}")
for n in [100, 500, 1000, 2000, 5000, 8000, 10000, 15000, 20000, 30000, 40000, 50000, 60000]:
    v = ndn(n)
    N = int(np.searchsorted(zeros, n, side='right'))
    Sn = N - theta_mp(float(n))/np.pi - 1
    print(f"{n:7d} {v:+10.4f} {gmax/n:8.1f} {Sn:+8.4f}")
