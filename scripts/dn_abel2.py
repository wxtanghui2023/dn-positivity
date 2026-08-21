#!/usr/bin/env python3
# Quantify: D_n = Σ(a_j-a_{j+1})B_j + a_J B_J = positive part - negative part
# Can we show positive part dominates?
import numpy as np
import mpmath as mp
mp.mp.dps = 20
zeros = np.load('/tmp/zeros_odlyzko_100k.npy')
gmax = float(zeros[-1])

def theta_doc(t):
    return np.pi - 2.0*np.arctan(2.0*t)
th = theta_doc(zeros)
a = np.sin(th/2)  # decreasing, > 0
da = a[:-1] - a[1:]  # ≥ 0

print(f"{'n':>6} {'D_n':>10} {'pos':>10} {'neg':>10} {'margin':>10} {'min B_j':>10} {'at j':>6}")
for n in [44, 50, 75, 100, 200, 500, 1000, 2000, 5000]:
    b = 2*np.sin((n+0.5)*th)
    B = np.cumsum(b)
    # Abel: D = Σ da·B[:-1] + a[-1]·B[-1]
    terms = da*B[:-1]
    pos = np.sum(terms[terms > 0]) + (a[-1]*B[-1] if a[-1]*B[-1] > 0 else 0)
    neg = -np.sum(terms[terms < 0]) - (a[-1]*B[-1] if a[-1]*B[-1] < 0 else 0)
    D = np.sum(terms) + a[-1]*B[-1]
    jmin = np.argmin(B) + 1
    print(f"{n:6d} {D:+10.4f} {pos:+10.4f} {neg:+10.4f} {pos-neg:+10.4f} {B.min():+10.4f} {jmin:6d}", flush=True)

# Where do negative B_j occur relative to θ?
print("\n=== negative B_j region vs θ ===")
for n in [100, 500]:
    b = 2*np.sin((n+0.5)*th)
    B = np.cumsum(b)
    negj = np.where(B < 0)[0]
    if len(negj):
        print(f"n={n}: {len(negj)} negative B_j, j range [{negj[0]+1},{negj[-1]+1}], "
              f"θ range [{th[negj[-1]]:.4f}, {th[negj[0]]:.4f}], "
              f"θ* = π/(n+½) = {np.pi/(n+0.5):.4f}")
    else:
        print(f"n={n}: no negative B_j")
