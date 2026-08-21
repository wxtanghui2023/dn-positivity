#!/usr/bin/env python3
# Document definitions: θ=π-2arctan(2t), g_n=[t sin(nθ)+0.5cos(nθ)]/(1/4+t²)
# ANALYTIC: ∫₀^∞ θ'g_n dt = 0 for n≥1 (verified below numerically)
# So D_n = Σ_γ g_n(γ) directly!
import numpy as np
from scipy import integrate
import mpmath as mp
mp.mp.dps = 20

zeros = np.load('/tmp/zeros_odlyzko_100k.npy')
gmax = float(zeros[-1])

def theta_doc(t):
    return np.pi - 2.0*np.arctan(2.0*t)
def theta_doc_prime(t):
    return -4.0/(1.0 + 4.0*t*t)
def g_n_doc(t, n):
    th = theta_doc(t)
    return (t*np.sin(n*th) + 0.5*np.cos(n*th)) / (0.25 + t*t)

# verify integral = 0 analytically via substitution: θ=π-2arctan(2t) -> t=½cot(θ/2)
# ∫₀^∞ θ'g_n dt = -∫₀^π [sinθ sin(nθ) + (1-cosθ)cos(nθ)]dθ
# n=1: sinθsinθ + (1-cosθ)cosθ = sin²θ+cosθ-cos²θ = cosθ-cos2θ -> ∫=0
# n≥2: sinθsin(nθ) integral 0; (1-cosθ)cos(nθ) = cos(nθ)-cosθcos(nθ) -> 0
from scipy.integrate import quad
print("verify ∫₀^∞ θ'g_n dt = 0 numerically (should be ~0):")
for n in [1, 2, 3, 5, 10]:
    I, e = quad(lambda t: theta_doc_prime(t)*g_n_doc(t, n), 0.0, gmax, limit=300)
    print(f"  n={n}:  ∫θ'g_n dt = {I:+.8f}  (per unit π: {I/np.pi:+.8f})")

print("\nD_n = Σ_γ g_n(γ)  (integral = 0 analytically):")
print(f"{'n':>6} {'Σg_n(γ)=D_n':>14} {'n·D_n':>12}")
for n in [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000, 2000]:
    s = np.sum(g_n_doc(zeros, n))
    print(f"{n:6d} {s:+14.6f} {n*s:+12.4f}", flush=True)
