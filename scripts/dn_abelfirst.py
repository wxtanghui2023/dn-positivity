#!/usr/bin/env python3
# KEY: D_n = Σ_j a_j·b_j, a_j = sin(θ_j/2) > 0 decreasing, b_j = 2sin((n+½)θ_j)
# Abel: D_n = Σ(a_j - a_{j+1})·B_j + a_J·B_J,  B_j = Σ_{k≤j} b_k
# If B_j ≥ 0 for all j ⟹ D_n ≥ 0 (STRICT PROOF!)
import numpy as np
import mpmath as mp
mp.mp.dps = 20
zeros = np.load('/tmp/zeros_odlyzko_100k.npy')
gmax = float(zeros[-1])

def theta_doc(t):
    return np.pi - 2.0*np.arctan(2.0*t)
th = theta_doc(zeros)  # θ_j decreasing

def g_n(tt, n):
    return np.cos(n*tt) - np.cos((n+1)*tt)

print("=== B_j = Σ_{k≤j} 2sin((n+½)θ_k): is it ≥ 0 for all j? ===")
for n in [1, 2, 5, 10, 20, 43, 44, 50, 100, 200, 500, 1000, 2000, 5000]:
    b = 2*np.sin((n+0.5)*th)
    B = np.cumsum(b)
    print(f"n={n:5d}: min B_j = {B.min():+10.4f} at j={np.argmin(B)+1}, max={B.max():+10.4f}, B_end={B[-1]:+10.4f}  all≥0: {B.min() >= -1e-9}", flush=True)

# check a_j = sin(θ_j/2) decreasing
a = np.sin(th/2)
print(f"\na_j = sin(θ_j/2): decreasing = {np.all(np.diff(a) <= 0)}, a_1 = {a[0]:.6f}")

# verify Abel identity: D_n = Σ(a_j-a_{j+1})B_j + a_J B_J
print("\n=== Abel identity check ===")
for n in [10, 50, 200, 1000]:
    a = np.sin(th/2)
    b = 2*np.sin((n+0.5)*th)
    B = np.cumsum(b)
    # D_n = Σ_j a_j b_j  (over ALL zeros, truncated at 100k)
    D_direct = np.sum(a*b)
    J = len(a)
    D_abel = np.sum((a[:-1]-a[1:])*B[:-1]) + a[-1]*B[-1]
    print(f"  n={n}: D_direct={D_direct:+.6f}  D_abel={D_abel:+.6f}  match={abs(D_direct-D_abel)<1e-6}")
