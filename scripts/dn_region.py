#!/usr/bin/env python3
# NEW: split D_n by phase region
# D_n = Σ 2sin(φ_k)sin(θ_k/2), φ_k = (n+½)θ_k
# POSITIVE region: φ_k < π (θ_k < π/(n+½), γ_k > (n+½)/π) - all terms positive
# NEGATIVE region: φ_k > π - can be negative, use alternating series (Leibniz)
import numpy as np
import mpmath as mp
mp.mp.dps = 20
zeros = np.load('/tmp/zeros_odlyzko_100k.npy')
gmax = float(zeros[-1])

def theta_doc(t):
    return np.pi - 2.0*np.arctan(2.0*t)
th = theta_doc(zeros)  # θ_k decreasing
a = np.sin(th/2)

print(f"{'n':>7} {'D_pos':>10} {'D_neg':>10} {'D_total':>10} {'D_neg/D_pos':>11} {'log n/2':>8} {'log n/π²':>9}")
for n in [50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000]:
    phi = (n+0.5)*th
    terms = 2*np.sin(phi)*a
    pos_mask = phi < np.pi
    D_pos = np.sum(terms[pos_mask])
    D_neg = np.sum(terms[~pos_mask])
    D_tot = D_pos + D_neg
    print(f"{n:7d} {D_pos:+10.4f} {D_neg:+10.4f} {D_tot:+10.4f} {abs(D_neg)/D_pos:11.4f} {np.log(n)/2:8.4f} {np.log(n)/np.pi**2:9.4f}", flush=True)

# check: D_pos ≈ (1/2)log n? D_neg ≈ -(log n)/π²?
print("\n=== asymptotics check ===")
for n in [500, 1000, 2000, 5000, 10000, 20000]:
    phi = (n+0.5)*th
    terms = 2*np.sin(phi)*a
    pos_mask = phi < np.pi
    D_pos = np.sum(terms[pos_mask])
    D_neg = np.sum(terms[~pos_mask])
    print(f"n={n:6d}: D_pos/log n = {D_pos/np.log(n):.4f} (expect 0.5), "
          f"D_neg·π²/log n = {D_neg*np.pi**2/np.log(n):.4f} (expect -1)")

# negative region structure: alternating half-wave blocks
print("\n=== negative region: half-wave block decomposition (n=5000) ===")
n = 5000
phi = (n+0.5)*th
terms = 2*np.sin(phi)*a
neg_mask = phi > np.pi
# blocks: φ ∈ (mπ, (m+1)π)
m_max = int(np.ceil(phi[0]/np.pi))
print(f"φ₁/π = {phi[0]/np.pi:.2f}, blocks m=1..{m_max}")
block_sums = []
for m in range(1, m_max+1):
    blk = (phi > m*np.pi) & (phi < (m+1)*np.pi)
    block_sums.append((m, np.sum(terms[blk])))
for m, s in block_sums:
    print(f"  block m={m:2d} (φ∈({m}π,{m+1}π)): sum = {s:+10.4f}  (sign {'+' if m%2==0 else '-'})")
