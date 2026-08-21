#!/usr/bin/env python3
# THE BIG ONE: g_n(t) = cos(nθ(t)) - cos((n+1)θ(t)) ?!
# If true: D_n = Σ_γ [cos(nθ_k) - cos((n+1)θ_k)] = telescoping structure
# θ_k = θ(γ_k) = π - 2arctan(2γ_k), decreasing from θ₁≈0.0707 to 0
import numpy as np
import mpmath as mp
mp.mp.dps = 20
zeros = np.load('/tmp/zeros_odlyzko_100k.npy')
gmax = float(zeros[-1])

def theta_doc(t):
    return np.pi - 2.0*np.arctan(2.0*t)
def g_n_doc(t, n):
    th = theta_doc(t)
    return (t*np.sin(n*th) + 0.5*np.cos(n*th))/(0.25+t*t)

# verify identity
print("=== verify g_n(t) = cos(nθ) - cos((n+1)θ) ===")
ok = True
for n in [1, 2, 3, 5, 10, 20]:
    for t in [0.5, 1.0, 5.0, 14.13, 100.0, 1000.0]:
        th = theta_doc(t)
        lhs = g_n_doc(t, n)
        rhs = np.cos(n*th) - np.cos((n+1)*th)
        if abs(lhs-rhs) > 1e-10:
            ok = False
            print(f"  MISMATCH n={n} t={t}: {lhs:+.8f} vs {rhs:+.8f}")
print(f"  identity holds: {ok}")

# D_n = Σ [cos(nθ_k) - cos((n+1)θ_k)]
print("\n=== D_n = Σ_k [cos(nθ_k) - cos((n+1)θ_k)] ===")
th_zeros = theta_doc(zeros)   # θ_k decreasing
print(f"θ₁ = θ(γ₁) = {th_zeros[0]:.6f}, θ_100000 = {th_zeros[-1]:.8f}")
for n in [1, 2, 3, 5, 10, 20, 50, 100]:
    s = np.sum(np.cos(n*th_zeros) - np.cos((n+1)*th_zeros))
    s2 = np.sum(g_n_doc(zeros, n))
    print(f"  n={n}: telescoped={s:+.6f}  direct={s2:+.6f}  match={abs(s-s2)<1e-8}")

# KEY INSIGHT: since θ_k strictly decreasing to 0, and cos(nθ)-cos((n+1)θ) = 2sin((n+1/2)θ)sin(θ/2)
print("\n=== cos(nθ)-cos((n+1)θ) = 2sin((n+1/2)θ)·sin(θ/2) ===")
# This is positive iff sin((n+1/2)θ) has the right sign...
# θ_k ∈ (0, θ₁] ≈ (0, 0.0707]. (n+1/2)θ_k ≤ (n+1/2)·0.0707.
# For n ≤ 43: (n+1/2)·0.0707 < π → sin > 0 → g_n(γ_k) > 0 ALL TERMS!
print(f"θ₁·(n+0.5) < π ⟺ n < π/θ₁ - 0.5 ≈ {np.pi/th_zeros[0] - 0.5:.1f}")
print("→ for n ≤ 43, ALL terms cos(nθ_k)-cos((n+1)θ_k) > 0!")
print(f"  check: D_43 = Σ positive terms = {np.sum(np.cos(43*th_zeros) - np.cos(44*th_zeros)):+.6f}")

# larger n: terms oscillate but sum may still be positive; check D_n sign for all n
print("\n=== D_n sign for all n up to 5000 ===")
mn = 1e9; mn_n = 0
for n in range(1, 5001):
    s = np.sum(np.cos(n*th_zeros) - np.cos((n+1)*th_zeros))
    if s < mn: mn, mn_n = s, n
print(f"  min D_n over n∈[1,5000] = {mn:+.6f} at n={mn_n}  (positive: {mn > 0})")
