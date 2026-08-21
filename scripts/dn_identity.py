#!/usr/bin/env python3
# CRITICAL: verify mean(S(γ_k)) = 1/2 is an ANALYTIC IDENTITY
# Claim: S(γ_k) = k - θ(γ_k)/π - 1, and Σ_{k=1}^K S(γ_k) = K/2 + (known correction)
# Test the identity: Σ_{k=1}^K [S(γ_k) - 1/2] vs boundary terms θ(γ_K)/π - K - 1/2...
# If Σ(S(γ_k)-1/2) = [θ(γ_K)/π - K - 1/2]-related, it's analytic!
import numpy as np
import mpmath as mp
mp.mp.dps = 20

zeros = np.load('/tmp/zeros_odlyzko_100k.npy')
gmax = float(zeros[-1])

def theta_mp(t):
    z = mp.mpf('0.25') + 1j*mp.mpf(t)/2
    return float(mp.im(mp.loggamma(z)) - mp.mpf(t)/2*mp.log(mp.pi))

# Σ_{k=1}^K (S(γ_k) - 1/2) where S(γ_k) = k - θ(γ_k)/π - 1
print("=== analytic identity test: Σ(S(γ_k)-1/2) ===")
print(f"{'K':>7} {'Σ(S-1/2)':>12} {'(K-1/2)-θ(γ_K)/π':>18} {'Σ+θ(γ_K)/π-(K-1/2)':>20}")
for K in [100, 1000, 10000, 100000]:
    gK = float(zeros[K-1])
    Sk = np.array([(k+1) - theta_mp(float(zeros[k]))/np.pi - 1.0 for k in range(K)])
    S_sum = np.sum(Sk - 0.5)
    lhs = S_sum + theta_mp(gK)/np.pi - (K - 0.5)
    print(f"{K:7d} {S_sum:+12.4f} {(K-0.5)-theta_mp(gK)/np.pi:+18.4f} {lhs:+20.6f}")

# The sawtooth integral identity:
# M(γ_K) = Σ_{k=1}^K ∫_{γ_{k-1}}^{γ_k} S(u)du = Σ (γ_k-γ_{k-1})(S(γ_k)-1/2) + O(Σ spacing³ θ'')
# If S(γ_k) ≈ 1/2 + (θ(γ_k)/π - (k-1/2))-type fluctuation, then... 
# Let me directly test: S(γ_k) - 1/2 vs θ(γ_k)/π - (k-1/2) - 1/2 = θ(γ_k)/π - k
print("\n=== S(γ_k) - 1/2 vs θ(γ_k)/π - k ===")
print(f"{'k':>7} {'γ_k':>10} {'S(γ_k)':>8} {'θ/π - k':>10} {'S-1/2':>8} {'diff':>10}")
for k in [1, 2, 3, 10, 100, 1000, 10000, 100000]:
    g = float(zeros[k-1])
    Sk = k - theta_mp(g)/np.pi - 1.0
    print(f"{k:7d} {g:10.4f} {Sk:+8.4f} {theta_mp(g)/np.pi-k:+10.4f} {Sk-0.5:+8.4f} {Sk-0.5-(theta_mp(g)/np.pi-k):+10.6f}")
