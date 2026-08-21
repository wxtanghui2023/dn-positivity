#!/usr/bin/env python3
# C(n) split at fixed T0:  C(n) = main(n) + tail(n)
# main(n) = Σ_{γ₁<γ≤T0} sinc(γ/n) - (1/π)∫_{γ₁}^{T0} θ'sinc dt  →  S(T0)+θ(γ₁)/π as n→∞
# tail(n) = ∫_{T0}^∞ sinc(t/n)dS(t)
# Test: does main(n) → S(T0)+θ(γ₁)/π rapidly? Is tail(n) small for T0 large?
import numpy as np
from scipy import integrate
import mpmath as mp
mp.mp.dps = 20

zeros = np.load('/tmp/zeros_odlyzko_100k.npy')
gmax = float(zeros[-1]); g1 = float(zeros[0])

def theta_asy(t):
    return 0.5*t*np.log(t/(2*np.pi)) - 0.5*t - np.pi/8 + 1/(48*t) + 7/(5760*t**3)
def theta_prime_asy(t):
    return 0.5*np.log(t/(2*np.pi)) - 1/(48*t*t) - 7/(1920*t**4)
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

# S(T0) exact from zero count
def S_of_T(T0):
    N = int(np.searchsorted(zeros, T0, side='right'))
    return N - theta_mp(T0)/np.pi - 1.0

print("=== C(n) split at T0: main(n) vs S(T0)+θ(γ₁)/π ===")
for T0 in [500, 2000, 5000]:
    mask = (zeros > g1) & (zeros <= T0)
    zeros_T0 = zeros[mask]
    m = (tg >= g1) & (tg <= T0)
    S_T0 = S_of_T(T0)
    th1 = theta_mp(g1)
    target = S_T0 + th1/np.pi
    print(f"\nT0={T0}: S(T0)={S_T0:+.4f}, S+θ(γ₁)/π = {target:+.4f}")
    for n in [50, 200, 1000, 5000]:
        main = np.sum(sinc(zeros_T0/n)) - np.trapz(tp[m]*sinc(tg[m]/n), tg[m])/np.pi
        print(f"  n={n:5d}: main(n)={main:+.4f}   main - target = {main-target:+.4f}")

print("\n=== tail(n) = ∫_{T0}^∞ sinc dS = C(n) - main(n) ===")
def C_of_n(n):
    m = tg < g1
    A = -np.trapz(tp[m]*sinc(tg[m]/n), tg[m])/np.pi
    return np.sum(sinc(zeros/n)) - np.trapz(tp*sinc(tg/n), tg)/np.pi - A + sinc(g1/n)

for T0 in [500, 2000, 5000]:
    mask = (zeros > g1) & (zeros <= T0)
    zeros_T0 = zeros[mask]
    m = (tg >= g1) & (tg <= T0)
    print(f"\nT0={T0}:")
    for n in [50, 200, 1000, 5000, 20000]:
        main = np.sum(sinc(zeros_T0/n)) - np.trapz(tp[m]*sinc(tg[m]/n), tg[m])/np.pi
        C = C_of_n(n)
        print(f"  n={n:5d}: C(n)={C:+.4f}  main={main:+.4f}  tail=C-main={C-main:+.4f}")
