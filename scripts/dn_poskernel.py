#!/usr/bin/env python3
# KEY IDEA: C(n) = ∫ sinc(t/n)dS(t). Can we write it as convolution with a POSITIVE kernel?
# If S(t) = N(t) - θ(t)/π - 1, then dS = dN - θ'/π dt.
# C(n) = Σ sinc(γ_k/n) - (1/π)∫ θ'(t)sinc(t/n)dt  [over γ ≥ γ1]
# Try: use identity ∫sinc = π/2, ∫sinc² = π/2... 
# Alternative: express via the "second moment" of zero distribution:
# C(n) relates to Σ_{j,k} sinc((γ_j-γ_k)/n)-type pair sums? (Montgomery pair correlation!)
import numpy as np
from scipy import integrate
import mpmath as mp
mp.mp.dps = 20

zeros = np.load('/tmp/zeros_odlyzko_100k.npy')
gmax = float(zeros[-1]); g1 = float(zeros[0])

def theta_mp(t):
    z = mp.mpf('0.25') + 1j*mp.mpf(t)/2
    return float(mp.im(mp.loggamma(z)) - mp.mpf(t)/2*mp.log(mp.pi))
def theta_prime_asy(t):
    return 0.5*np.log(t/(2*np.pi)) - 1/(48*t*t) - 7/(1920*t**4)
def theta_prime_mp(t):
    z = mp.mpf('0.25') + 1j*mp.mpf(t)/2
    return float(mp.re(mp.psi(0, z))/2 - mp.log(mp.pi)/2)
def sinc(x):
    return np.where(x==0, 1.0, np.sin(x)/x)

# N(T) - θ(T)/π - 1 = S(T); test pair-correlation style:
# Σ_{j≠k} sinc((γ_j-γ_k)/n) type sums? 
# First: verify C(n) can be rewritten via counting:
# C(n) = ∫ sinc(t/n)dN(t) - (1/π)∫θ'sinc dt  (over [γ1, ∞))
# By Stieltjes: = [sinc(T/n)N(T)] - ∫ N(t) d(sinc(t/n)) - (1/π)∫θ'sinc dt ... 
# Try instead: D_n = ∫g_n dS, g_n(t)=sin(t/n)/t. Pair correlation form:
# Known: for the SECOND moment, Σ_γ g(γ)² relates to pair sums. But D_n is FIRST moment.

# Test: is C(n) = ∫_{γ1}^∞ sinc(t/n)dS(t) close to S(n) - S(γ1)·(stuff)?
# From earlier: tail(n) at T0=2000 ≈ 1.96 + O(0.3 drift). S(γ1)=S(14.13)≈?
Sg1 = 1 - theta_mp(g1)/np.pi - 1
print(f"S(γ₁) = {Sg1:+.4f}")

# C(n) vs [S(n) - S(γ1)] comparison:
print(f"\n{'n':>7} {'C(n)':>10} {'S(n)-S(γ1)':>12} {'C - (S(n)-S(γ1))':>18}")
for n in [100, 500, 1000, 2000, 5000, 10000, 20000, 50000]:
    N = int(np.searchsorted(zeros, n, side='right'))
    Sn = N - theta_mp(float(n))/np.pi - 1
    # C(n) fast compute
    STEP=0.25
    tg = np.arange(0.0, gmax, STEP)
    tp = np.zeros_like(tg); small = tg<50
    for i in np.nonzero(small)[0]: tp[i]=theta_prime_mp(float(tg[i]))
    tp[~small]=theta_prime_asy(tg[~small])
    m = tg < g1
    A = -np.trapz(tp[m]*sinc(tg[m]/n), tg[m])/np.pi
    C = np.sum(sinc(zeros/n)) - np.trapz(tp*sinc(tg/n), tg)/np.pi - A + sinc(g1/n)
    print(f"{n:7d} {C:+10.4f} {Sn-Sg1:+12.4f} {C-(Sn-Sg1):+18.4f}")
