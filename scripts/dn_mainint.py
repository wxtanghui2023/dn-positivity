#!/usr/bin/env python3
# D_n = Σ_k 2sin((n+1/2)θ_k)·sin(θ_k/2), θ_k ≈ 1/γ_k
# Smooth approx: D_n ≈ (1/2π)∫_{γ₁}^∞ 2sin((n+1/2)/γ)·sin(1/(2γ))·log(γ/2π) dγ
# u = (n+1/2)/γ: = (1/2π)∫_0^{u_max} 2sin(u)sin(u/(2n+1))·log((n+1/2)/(2πu))·(n+1/2)/u² du
# Evaluate this integral numerically; compare to D_n; check sign & asymptotics
import numpy as np
from scipy.integrate import quad
import mpmath as mp
mp.mp.dps = 20
zeros = np.load('/tmp/zeros_odlyzko_100k.npy')
gmax = float(zeros[-1]); g1 = float(zeros[0])

def theta_doc(t):
    return np.pi - 2.0*np.arctan(2.0*t)
th = theta_doc(zeros)

def D_direct(n):
    return np.sum(np.cos(n*th) - np.cos((n+1)*th))

def D_smooth(n):
    # (1/2π)∫_{γ₁}^∞ 2sin((n+½)/γ)sin(1/(2γ))log(γ/2π)dγ, split [γ₁, gmax] + tail estimate
    a = (n+0.5)
    f = lambda g: 2*np.sin(a/g)*np.sin(1/(2*g))*np.log(g/(2*np.pi))
    I1, _ = quad(lambda g: f(g), g1, gmax, limit=2000)
    # tail γ>gmax: sin(a/γ)≈a/γ, sin(1/2γ)≈1/2γ → f≈2·(a/γ)(1/2γ)log = a·log(γ/2π)/γ²
    # ∫_{gmax}^∞ a log(γ/2π)/γ² dγ = a·(log(gmax/2π)+1)/gmax
    tail = a*(np.log(gmax/(2*np.pi))+1)/gmax
    return (1/(2*np.pi))*(I1 + tail)

print("=== D_n: direct sum vs smooth integral ===")
print(f"{'n':>6} {'D_direct':>12} {'D_smooth':>12} {'D_smooth/D':>10}")
for n in [10, 43, 50, 100, 200, 500, 1000, 2000]:
    Dd = D_direct(n)
    Ds = D_smooth(n)
    print(f"{n:6d} {Dd:+12.6f} {Ds:+12.6f} {Ds/Dd:10.3f}", flush=True)

# asymptotics of D_smooth: u-substitution
# D_smooth = (1/2π)∫ 2sin(u)sin(u/(2n+1))·log(a/(2πu))·(a/u²)du, a=n+½, u∈(0, a/γ₁]
# large n: sin(u/(2n+1))≈u/(2n+1)·(1 - u²/(6(2n+1)²)), log(a/2πu)=log n - log(2πu)+...
# leading: (1/2π)∫ 2sin(u)·(u/(2n+1))·log(a/2πu)·a/u² du = (1/2π)·(a/(2n+1))∫2sin(u)log(a/2πu)/u du
# a/(2n+1) ≈ 1/2: D_smooth ≈ (1/2π)·(1/2)·2∫sin(u)log(a/2πu)/u du = (1/2π)∫sin(u)[log n - log(2πu)]/u du
# ∫sin(u)/u du = π/2; ∫sin(u)log u/u du = -πγ/2 (γ=Euler)
# D_smooth ≈ (1/2π)[(π/2)log(n/2π) - (-πγ/2)·... ] hmm let me just verify numerically
print("\n=== D_n vs log: is D_n ≈ (1/4)log n + const? ===")
for n in [100, 200, 500, 1000, 2000, 5000, 10000]:
    Dd = D_direct(n)
    print(f"  n={n}: D_n={Dd:+.6f}  (1/4)log n={0.25*np.log(n):.4f}  ratio D/log={Dd/np.log(n):.4f}")
