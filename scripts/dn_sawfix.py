#!/usr/bin/env python3
# Resolve the sawtooth inconsistency: why Σ(S(γ_k)-1/2)·spacing = -6003 but M(T) ≈ O(1)?
# Hypothesis: the sawtooth integral over (γ_k, γ_{k+1}) is NOT (S(γ_k)-1/2)·spacing
# because θ/π increases NON-linearly. Correct integral:
#   ∫_{γ_k}^{γ_{k+1}} S(u)du = ∫ [k - θ(u)/π - 1]du = (k-1)(γ_{k+1}-γ_k) - ∫θ/π du
# Let me compute the EXACT per-interval integral and compare to (S(γ_k)-1/2)·spacing.
import numpy as np
from scipy import integrate
import mpmath as mp
mp.mp.dps = 20

zeros = np.load('/tmp/zeros_odlyzko_100k.npy')

def theta_scalar(t):
    if t < 50:
        z = mp.mpf('0.25') + 1j*mp.mpf(t)/2
        return float(mp.im(mp.loggamma(z)) - mp.mpf(t)/2*mp.log(mp.pi))
    return float(0.5*t*np.log(t/(2*np.pi)) - 0.5*t - np.pi/8 + 1/(48*t) + 7/(5760*t**3) + 31/(80640*t**5))

# exact per-interval integral via 8-point Gauss (theta is smooth)
def gauss8_int(a, b):
    x, w = np.polynomial.legendre.leggauss(8)
    xs = 0.5*(b-a)*x + 0.5*(a+b)
    return 0.5*(b-a)*np.sum(w*np.array([theta_scalar(float(t)) for t in xs]))/np.pi

# compare for a few intervals
print("per-interval analysis:")
print(f"{'k':>7} {'γ_k':>10} {'S(γ_k)':>8} {'exact∫S':>10} {'(S-1/2)Δ':>10} {'diff':>10}")
tot_exact = 0.0; tot_saw = 0.0
for k in [1, 2, 3, 10, 100, 1000, 10000, 50000, 99999]:
    a = 0.0 if k == 1 else float(zeros[k-2])
    b = float(zeros[k-1])
    Sk = k - theta_scalar(b)/np.pi - 1.0
    exact = (k-1)*(b-a) - gauss8_int(a, b)   # ∫[k-1 - θ/π - 1]... wait check below
    # S(u) = N(u) - θ(u)/π - 1, N(u) = k-1 on (γ_{k-1}, γ_k)
    # ∫S = (k-1-1)(b-a) - ∫θ/π = (k-2)(b-a) - ∫θ/π
    exact = (k-2)*(b-a) - gauss8_int(a, b)
    saw = (Sk - 0.5)*(b-a)
    tot_exact += exact; tot_saw += saw
    print(f"{k:7d} {b:10.4f} {Sk:+8.4f} {exact:+10.4f} {saw:+10.4f} {exact-saw:+10.4f}")

# cumulative exact M over ALL intervals (first pass, sample every interval)
print("\ncumulative exact M(γ_k) at selected k (all intervals, 8-pt Gauss):")
Mcum = 0.0
report = {}
for k in range(1, len(zeros)+1):
    a = 0.0 if k == 1 else float(zeros[k-2])
    b = float(zeros[k-1])
    Mcum += (k-2)*(b-a) - gauss8_int(a, b)
    if k in [1, 10, 100, 1000, 10000, 50000, 100000]:
        report[k] = Mcum
        print(f"  k={k:6d}:  M(γ_k) = {Mcum:+.4f}")
