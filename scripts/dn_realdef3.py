#!/usr/bin/env python3
# Check the analytic integral claim carefully for ALL n
# θ=π-2arctan(2t), t=½cot(θ/2), 1/(1/4+t²)=2(1-cosθ), t/(1/4+t²)=sinθ
# ∫₀^∞ θ'g_n dt = ∫_π^0 [sinθ·sin(nθ) + 2(1-cosθ)·0.5·cos(nθ)]dθ  [dt=dθ/θ', θ'dt=dθ]
#   = ∫_π^0 [sinθ sin(nθ) + (1-cosθ)cos(nθ)]dθ
#   = -∫_0^π [sinθ sin(nθ) + (1-cosθ)cos(nθ)]dθ
# ∫₀^π sinθ sin(nθ)dθ = π/2 if n=1, 0 if n≥2
# ∫₀^π (1-cosθ)cos(nθ)dθ = ∫₀^π cos(nθ)dθ - ∫₀^π cosθ cos(nθ)dθ = 0 - (π/2 if n=1 else 0)
# n=1: -(π/2 + 0 - π/2) = 0 ; n≥2: -(0 + 0) = 0  → all zero ✓
import numpy as np
from scipy.integrate import quad
print("=== numeric check of ∫₀^∞ θ'g_n dt (quad with high limit, split at 100) ===")
def theta_doc(t): return np.pi - 2.0*np.arctan(2.0*t)
def theta_doc_prime(t): return -4.0/(1.0+4.0*t*t)
def g_n_doc(t, n):
    th = theta_doc(t)
    return (t*np.sin(n*th) + 0.5*np.cos(n*th))/(0.25+t*t)
for n in [10, 20, 50, 100]:
    # split [0,100] quad + [100, gmax] with high limit; and [0,gmax] points grid
    I1, e1 = quad(lambda t: theta_doc_prime(t)*g_n_doc(t,n), 0, 100, limit=1000)
    I2, e2 = quad(lambda t: theta_doc_prime(t)*g_n_doc(t,n), 100, 74921, limit=2000)
    print(f"  n={n}: ∫₀^100={I1:+.6f} (err {e1:.0e})  ∫100^∞={I2:+.6f} (err {e2:.0e})  total={I1+I2:+.6f}")

print("\n=== g_n tail asymptotics: g_n(γ) ≈ sin(n/γ)/γ ≈ n/γ² (γ≫n) ===")
# verify: D_n = Σ g_n(γ) should ≈ n·Σ1/γ² + boundary if g_n ≈ n/γ² for γ≫n
# but g_n(γ) for γ≪n: sin(nθ(γ)) oscillates... check partial sums
zeros = np.load('/tmp/zeros_odlyzko_100k.npy')
print(f"\npartial sums of g_n(γ) up to T (n=20):")
for T in [50, 100, 500, 1000, 5000, 20000, 74921]:
    zsel = zeros[zeros <= T]
    s = np.sum(g_n_doc(zsel, 20))
    print(f"  T={T:6d}: Σg_20(γ) = {s:+.6f}")
