#!/usr/bin/env python3
# CORRECTED: C(n) = n·D_n - A(n) - B(n), with A=-(1/π)∫₀^{γ1}θ'sinc, B=-sinc(γ1/n)
import numpy as np
from scipy import integrate
import mpmath as mp
mp.mp.dps = 20

zeros = np.load('/tmp/zeros_odlyzko_100k.npy')
g1 = float(zeros[0]); gmax = float(zeros[-1])

def theta_prime_asy(t):
    return 0.5*np.log(t/(2*np.pi)) - 1/(48*t*t) - 7/(1920*t**4) - 31/(16128*t**6)
def theta_prime_mp(t):
    z = mp.mpf('0.25') + 1j*mp.mpf(t)/2
    return float(mp.re(mp.psi(0, z))/2 - mp.log(mp.pi)/2)
def sinc(x):
    return np.where(x==0, 1.0, np.sin(x)/x)

def ndn(n):
    s = np.sum(sinc(zeros/n))
    I1, _ = integrate.quad(lambda t: theta_prime_mp(t)*sinc(t/n), 0.0, 50.0, limit=500)
    tg = np.arange(50.0, gmax, 0.25)
    I2 = np.trapz(theta_prime_asy(tg)*sinc(tg/n), tg)
    return s - (I1+I2)/np.pi

print(f"{'n':>6} {'n·D_n':>12} {'A':>10} {'B':>10} {'C=n·D-A-B':>14} {'C-C∞(1.4453)':>14} {'n·(C-C∞)':>12} {'n²·(C-C∞)':>12}")
for n in [20, 50, 100, 200, 300, 400, 500, 700, 1000, 1500, 2000, 3000]:
    v = ndn(n)
    A, _ = integrate.quad(lambda t: theta_prime_mp(t)*sinc(t/n), 0.0, g1, limit=500)
    A = -A/np.pi
    B = -sinc(g1/n)
    C = v - A - B
    d = C - 1.4453
    print(f"{n:6d} {v:+12.6f} {A:+10.6f} {B:+10.6f} {C:+14.6f} {d:+14.6f} {n*d:+12.5f} {n*n*d:+12.1f}", flush=True)
