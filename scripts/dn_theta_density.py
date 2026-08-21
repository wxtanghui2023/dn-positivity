#!/usr/bin/env python3
# D_n = Σ_k [cos(nθ_k) - cos((n+1)θ_k)], θ_k = θ(γ_k) strictly decreasing to 0
# Density analysis: θ_k ≈ uniform-ish? D_n ≈ ∫₀^{θ₁} [cos(nθ)-cos((n+1)θ)] ρ(θ)dθ?
# ρ(θ)dθ = zero count in dθ: dt/dθ = -(1+4t²)/4, dN/dt ≈ (1/2π)log(t/2π) smooth part
# ρ(θ) ≈ (1/2π)log(t(θ)/2π)·(1+4t(θ)²)/4, t(θ) = ½cot(θ/2)
# Small θ: t ≈ 1/θ, ρ(θ) ≈ (1/2π)log(1/(2πθ))·(1/θ²)/4 ~ (1/8π)·(1/θ²)·log(1/θ) - DIVERGENT at θ→0!
import numpy as np
import mpmath as mp
mp.mp.dps = 20
zeros = np.load('/tmp/zeros_odlyzko_100k.npy')
gmax = float(zeros[-1])

def theta_doc(t):
    return np.pi - 2.0*np.arctan(2.0*t)

th = theta_doc(zeros)  # θ_k decreasing
dth = np.diff(np.concatenate([[0.0], th[::-1]])[::-1])  # θ_{k} - θ_{k+1} > 0
# better: spacing Δθ_k = θ_k - θ_{k+1}
dth = th[:-1] - th[1:]

# numerical density: how many zeros per dθ
print("=== θ_k distribution ===")
print(f"θ₁={th[0]:.6f}, θ_{100}={th[99]:.8f}, θ_1000={th[999]:.8f}, θ_100000={th[-1]:.10f}")
# check: θ_k vs 1/γ_k (since θ(t)≈1/t)
print(f"check θ_k·γ_k ≈ 1: θ₁·γ₁={th[0]*zeros[0]:.6f}, θ_1000·γ_1000={th[999]*zeros[999]:.6f}")

# D_n via integral approx with ρ(θ):  ρ(θ) ≈ (1/2π)·log(t/2π)·(dt/dθ)/... 
# exact relation: Σ_k f(θ_k) vs ∫ f(θ) dN(θ)... use Abel summation:
# Σ_k [cos(nθ_k)-cos((n+1)θ_k)] = -Σ_k [cos(nθ_{k+1})-cos((n+1)θ_{k+1}) - (cos(nθ_k)-cos((n+1)θ_k))]
# actually: = Σ_k Δg(θ_k) where Δg(θ) = g(θ)-g(next)... telescoping:
# Σ_{k=1}^K [f(θ_k) - f(θ_{k+1})] with f(θ)=cos(nθ): = f(θ₁) - f(θ_{K+1})
# BUT we have cos(nθ_k) - cos((n+1)θ_k), NOT cos(nθ_k) - cos(nθ_{k+1})... 
# Let g_n(θ) = cos(nθ). Then D_n = Σ [g_n(θ_k) - g_{n+1}(θ_k)] - NOT telescoping in k.
# Hmm - but the SUM over k of g_n(θ_k) relates to θ_k distribution. Let me compute Σ_k cos(nθ_k):
print("\n=== Σ_k cos(nθ_k) (key quantity) ===")
for n in [1, 5, 10, 20, 43, 50, 100, 200, 500]:
    S_n = np.sum(np.cos(n*th))
    S_n1 = np.sum(np.cos((n+1)*th))
    print(f"  n={n}: Σcos(nθ)={S_n:+10.4f}  Σcos((n+1)θ)={S_n1:+10.4f}  D_n={S_n-S_n1:+10.4f}")

# Abel summation: Σ_k cos(nθ_k) with θ_k dense near 0
# S_n = Σ cos(nθ_k) ≈ ∫_0^{θ₁} cos(nθ) ρ(θ)dθ where ρ = density of θ_k
# ρ(θ) = (1/2π)log(t(θ)/2π)·|dt/dθ| = (1/2π)log(½cot(θ/2)/2π)·(1+4t²)/4
# verify numerically: cumulative count N(θ) = #{k: θ_k > θ}... 
# Let me compute the smoothed sum to see if D_n → const:
print("\n=== D_n large n behavior (should → const if ρ diverges at 0) ===")
for n in [100, 200, 500, 1000, 2000, 5000, 10000]:
    S = np.sum(np.cos(n*th) - np.cos((n+1)*th))
    print(f"  n={n}: D_n = {S:+.6f}")
