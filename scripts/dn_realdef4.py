#!/usr/bin/env python3
# Full picture with TRUE document definitions
# θ=π-2arctan(2t), g_n=[t sin(nθ)+0.5cos(nθ)]/(1/4+t²), D_n = Σ_γ g_n(γ)
# (integral part ≡ 0 analytically & numerically)
import numpy as np
import mpmath as mp
mp.mp.dps = 20

zeros = np.load('/tmp/zeros_odlyzko_100k.npy')
gmax = float(zeros[-1])

def theta_doc(t):
    return np.pi - 2.0*np.arctan(2.0*t)
def g_n_doc(t, n):
    th = theta_doc(t)
    return (t*np.sin(n*th) + 0.5*np.cos(n*th)) / (0.25 + t*t)

print("=== D_n = Σg_n(γ) with TRUE document g_n ===")
print(f"{'n':>6} {'D_n':>12} {'n·D_n':>12} {'ΔD_n':>10}")
prev = 0
for n in [1, 2, 3, 5, 7, 10, 15, 20, 30, 50, 75, 100, 150, 200, 300, 500, 750, 1000, 1500, 2000]:
    s = np.sum(g_n_doc(zeros, n))
    print(f"{n:6d} {s:+12.6f} {n*s:+12.4f} {s-prev:+10.6f}", flush=True)
    prev = s

# check convergence: D_n limit as n→∞
# g_n(γ) ≈ n/γ² for γ≫n; D_n → Σ_all? no: g_n(γ)→? as n→∞ for fixed γ: sin(nθ(γ)) oscillates
# Actually for large n, sin(nθ(γ)) with θ(γ)=π-2atan(2γ)≈1/γ: sin(n/γ) - for γ≫n: ≈n/γ; for γ≪n: oscillates
print("\n=== D_n vs n: growth check ===")
for n in [100, 500, 1000, 2000]:
    s = np.sum(g_n_doc(zeros, n))
    # tail beyond γmax: ≈ ∫_{γmax}^∞ n/γ² dN(γ) = n·(1/2π)∫log(γ/2π)/γ² dγ ≈ n·(log γmax)/(2π γmax)
    tail_est = n*np.log(gmax)/(2*np.pi*gmax)
    print(f"  n={n}: D_n={s:+.6f}  tail_est≈{tail_est:+.6f}  corrected D_n≈{s+tail_est:+.6f}")
