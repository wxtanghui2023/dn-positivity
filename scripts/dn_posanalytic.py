#!/usr/bin/env python3
# KEY: derive g_n(t) explicitly via trig identities!
# θ = π - 2arctan(2t):
#   sin θ = sin(2 arctan(2t)) = 2(2t)/(1+4t²) = 4t/(1+4t²)
#   cos θ = -cos(2 arctan(2t)) = -(1-4t²)/(1+4t²) = (4t²-1)/(1+4t²)
# g_n(t) = [t sin(nθ) + 0.5 cos(nθ)]/(1/4+t²)
# n=1: g_1(t) = [t·4t/(1+4t²) + 0.5(4t²-1)/(1+4t²)]/(1/4+t²)
#            = (6t² - 0.5)/((1+4t²)(1/4+t²))  > 0 iff t > 1/√12 ≈ 0.289
import numpy as np
import mpmath as mp
mp.mp.dps = 20
zeros = np.load('/tmp/zeros_odlyzko_100k.npy')

def g1_explicit(t):
    # (6t² - 0.5)/((1+4t²)(1/4+t²))
    return (6.0*t*t - 0.5)/((1.0+4.0*t*t)*(0.25+t*t))

def theta_doc(t):
    return np.pi - 2.0*np.arctan(2.0*t)
def g_n_doc(t, n):
    th = theta_doc(t)
    return (t*np.sin(n*th) + 0.5*np.cos(n*th))/(0.25+t*t)

# verify g_1 explicit matches
print("=== verify g_1 explicit form ===")
for t in [0.5, 1.0, 5.0, 14.13, 100.0]:
    print(f"  t={t}: explicit={g1_explicit(t):+.8f}  doc formula={g_n_doc(t,1):+.8f}  match={abs(g1_explicit(t)-g_n_doc(t,1))<1e-10}")

# g_1(γ) > 0 for all zeros? (need γ > 0.289, all zeros satisfy)
print(f"\nmin g_1(γ) over zeros: {np.min(g1_explicit(zeros)):+.6f}  (γ₁={zeros[0]:.2f})")
print(f"g_1(γ) > 0 for all zeros: {np.all(g1_explicit(zeros) > 0)}")
print(f"D_1 = Σ g_1(γ) = {np.sum(g1_explicit(zeros)):+.6f}")

# general n: try to find explicit form via Chebyshev
# sin(nθ), cos(nθ) in terms of sinθ, cosθ: T_n, U_n polynomials
# sin(nθ) = sinθ·U_{n-1}(cosθ); cos(nθ) = T_n(cosθ)
# g_n(t) = [t·sinθ·U_{n-1}(cosθ) + 0.5·T_n(cosθ)]/(1/4+t²)
# with sinθ = 4t/(1+4t²), cosθ = (4t²-1)/(1+4t²)
# Let x = cosθ = (4t²-1)/(1+4t²) ∈ (-1,1). t = ½cot(θ/2), 1/4+t² = ¼csc²(θ/2) = (1+4t²)/4·...
# Actually t/(1/4+t²) = sinθ (verified before), 1/(1/4+t²) = 2(1-cosθ) = 2(1-x)
# So g_n(t) = sinθ·U_{n-1}(x)·... let me verify: t/(1/4+t²)=sinθ ✓, 0.5/(1/4+t²) = (1-cosθ) = 1-x
# g_n(t) = sinθ·U_{n-1}(cosθ) + (1-cosθ)·T_n(cosθ)   [in θ-domain]
# With x=cosθ: g_n = sinθ·U_{n-1}(x) + (1-x)·T_n(x), sinθ=√(1-x²)
# For n=1: U_0=1, T_1=x: g_1 = √(1-x²) + (1-x)·x  ... check vs explicit
print("\n=== Chebyshev form: g_n = √(1-x²)·U_{n-1}(x) + (1-x)·T_n(x), x=cosθ ===")
from numpy.polynomial.chebyshev import Chebyshev
from numpy.polynomial import Polynomial
# verify n=1: sqrt(1-x²) + x - x²
import math
for t in [1.0, 14.13, 100.0]:
    th = theta_doc(t)
    x = math.cos(th)
    g_cheb = math.sqrt(1-x*x) + (1-x)*x
    print(f"  t={t}: g_cheb={g_cheb:+.8f} vs g_doc={g_n_doc(t,1):+.8f} match={abs(g_cheb-g_n_doc(t,1))<1e-10}")
