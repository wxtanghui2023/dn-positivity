#!/usr/bin/env python3
# INDEPENDENT verification of M(T) = ∫₀^T S(u)du
# Method 1: M(T) = Σ_{γ≤T}(T-γ) - ∫₀^T(θ/π+1)du   (sum of distances - smooth integral)
# Method 2: mean/distribution of S(γ_k) for all 100k zeros
# If M(T) ~ O(1) is real, mean(S(γ_k)) should be ≈ 1/2 (sawtooth cancel); if mean ≈ 0, M ~ -T/2 (bug!)
import numpy as np
from scipy import integrate
import mpmath as mp
mp.mp.dps = 20

zeros = np.load('/tmp/zeros_odlyzko_100k.npy')
N = len(zeros)

def theta_scalar(t):
    if t < 50:
        z = mp.mpf('0.25') + 1j*mp.mpf(t)/2
        return float(mp.im(mp.loggamma(z)) - mp.mpf(t)/2*mp.log(mp.pi))
    return float(0.5*t*np.log(t/(2*np.pi)) - 0.5*t - np.pi/8 + 1/(48*t) + 7/(5760*t**3) + 31/(80640*t**5))

# ---- Method 1: M(T) via sum-of-distances ----
def M_indep(T):
    k = int(np.searchsorted(zeros, T, side='right'))  # zeros <= T
    Sdist = np.sum(T - zeros[:k])                     # Σ_{γ≤T}(T-γ)
    # ∫₀^T (θ(u)/π + 1) du  via global quad (theta smooth - no jumps)
    I, _ = integrate.quad(lambda u: theta_scalar(u)/np.pi + 1.0, 0.0, T, limit=1000)
    return Sdist - I

print("=== Method 1: M(T) = Σ(T-γ) - ∫(θ/π+1)du ===")
print(f"{'T':>9} {'M_indep':>14} {'vs Simpson M':>14}")
simpson_vals = {236.5: -1.0728, 1419.4: -1.4503, 9877.8: -1.1045, 40433.7: -1.2743, 74920.8: -0.6927}
for T in [236.5, 1419.4, 9877.8, 40433.7, 74920.8]:
    m = M_indep(T)
    print(f"{T:9.1f} {m:+14.4f} {simpson_vals.get(T, float('nan')):+14.4f}")

# ---- Method 2: S(γ_k) statistics ----
print("\n=== S(γ_k) = k - θ(γ_k)/π - 1 statistics ===")
Sk = np.zeros(N)
for i in range(N):
    Sk[i] = (i+1) - theta_scalar(float(zeros[i]))/np.pi - 1.0
print(f"mean(S(γ_k))    = {Sk.mean():+.4f}")
print(f"median(S(γ_k))  = {np.median(Sk):+.4f}")
print(f"std(S(γ_k))     = {Sk.std():+.4f}")
print(f"min/max         = {Sk.min():+.4f} / {Sk.max():+.4f}")
print(f"frac positive   = {(Sk > 0).mean():.4f}")
# running mean
for idx in [100, 1000, 10000, 50000, 100000]:
    print(f"  mean S(γ_k), k≤{idx:6d}: {Sk[:idx].mean():+.4f}")

# ---- Method 3: direct check of sawtooth identity ----
# M(γ_N) ≈ Σ_k (S(γ_k) - 1/2)·(γ_{k+1}-γ_k) + boundary  (derived from sawtooth)
print("\n=== sawtooth consistency: Σ (S(γ_k)-1/2)·spacing ===")
spacing = np.diff(np.concatenate([[0.0], zeros]))
saw = np.sum((Sk - 0.5) * spacing)
print(f"Σ (S(γ_k)-1/2)·spacing = {saw:+.4f}   (should ≈ M(74921))")
# and Σ S(γ_k)·spacing - γ_N/2:
alt = np.sum(Sk * spacing) - zeros[-1]/2
print(f"Σ S·spacing - T/2       = {alt:+.4f}")
