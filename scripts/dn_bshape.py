#!/usr/bin/env python3
# Examine the SHAPE of B_j in the negative region - single dent or oscillatory?
# If B_j dips negative smoothly then recovers, the weighted area is small.
import numpy as np
import mpmath as mp
mp.mp.dps = 20
zeros = np.load('/tmp/zeros_odlyzko_100k.npy')
def theta_doc(t):
    return np.pi - 2.0*np.arctan(2.0*t)
th = theta_doc(zeros)
a = np.sin(th/2)
da = a[:-1] - a[1:]

for n in [100, 500, 1000, 5000]:
    b = 2*np.sin((n+0.5)*th)
    B = np.cumsum(b)
    neg = np.where(B < 0)[0]
    if len(neg) == 0:
        print(f"n={n}: no negative B_j"); continue
    j0, j1 = neg[0], neg[-1]
    # sample B_j across the negative region
    span = j1 - j0 + 1
    idxs = np.unique(np.linspace(j0, j1, 9).astype(int))
    shape = ' '.join(f"{B[i]:+.0f}" for i in idxs)
    print(f"n={n:5d}: neg region j∈[{j0+1},{j1+1}] (span {span}), B shape: {shape}")
    # is it one smooth dent? count sign changes of b within
    b_neg_region = b[j0:j1+1]
    sign_changes = np.sum(np.diff(np.sign(b_neg_region)) != 0)
    print(f"        sign changes of b in region: {sign_changes}  (dent structure)")

# weighted area analysis: Σ da·(-B) over negative region vs continuous approx
print("\n=== negative contribution decomposition (n=5000) ===")
n = 5000
b = 2*np.sin((n+0.5)*th)
B = np.cumsum(b)
neg = np.where(B < 0)[0]
j0, j1 = neg[0], neg[-1]
# contribution by deciles
span = j1 - j0 + 1
for p in range(10):
    lo = j0 + p*span//10
    hi = j0 + (p+1)*span//10
    contrib = np.sum(da[lo:hi]*(-B[lo:hi]))
    print(f"  decile {p}: j∈[{lo+1},{hi}], contrib={contrib:+.5f}")
