#!/usr/bin/env python3
# Precision study of tail(n) = ∫_{T0}^∞ sinc(t/n)dS(t)
# Hypothesis: tail(n) ≈ [something like S-mean] + const
# Test: does tail(n) converge as n→∞? To what?
# Also: relation to ∫_{T0}^{n} dS = S(n)-S(T0) averaged by sinc window
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

def S_of_T(T0):
    N = int(np.searchsorted(zeros, T0, side='right'))
    return N - theta_mp(T0)/np.pi - 1.0

def C_of_n(n):
    m = tg < g1
    A = -np.trapz(tp[m]*sinc(tg[m]/n), tg[m])/np.pi
    return np.sum(sinc(zeros/n)) - np.trapz(tp*sinc(tg/n), tg)/np.pi - A + sinc(g1/n)

# tail(n) at T0=2000 for larger n
T0 = 2000
mask = (zeros > g1) & (zeros <= T0)
zeros_T0 = zeros[mask]
m = (tg >= g1) & (tg <= T0)
print("=== tail(n) = C(n) - main(n), T0=2000 ===")
print(f"{'n':>7} {'C(n)':>10} {'main(n)':>10} {'tail(n)':>10} {'S(n)':>8} {'S(n)-S(2000)':>12}")
for n in [100, 200, 500, 1000, 2000, 5000, 10000, 20000, 30000, 50000]:
    main = np.sum(sinc(zeros_T0/n)) - np.trapz(tp[m]*sinc(tg[m]/n), tg[m])/np.pi
    C = C_of_n(n)
    Sn = S_of_T(float(n))
    print(f"{n:7d} {C:+10.4f} {main:+10.4f} {C-main:+10.4f} {Sn:+8.4f} {Sn-S_of_T(T0):+12.4f}")

# What is the tail limit? try: tail(n) ≈ S(T0)+1+θ(γ1)/π - main_target + ... 
# compute S_cesaro-like: mean of S(γ_k) for γ in (T0, n]
print("\n=== mean of S(γ_k) over (T0, n] ===")
for n in [1000, 5000, 20000, 50000]:
    zsel = zeros[(zeros > T0) & (zeros <= n)]
    Svals = np.array([S_of_T(float(z)) for z in zsel])
    print(f"  n={n:6d}: mean(S(γ_k)) over ({T0},{n}] = {Svals.mean():+.4f}  (n_zeros={len(zsel)})")
