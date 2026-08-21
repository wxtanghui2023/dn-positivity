#!/usr/bin/env python3
# CRITICAL: determine B_j growth law |B_j| ~ j^α?
# If |B_j| ~ √j (random walk) -> path A works, neg contribution = O(1)
# If |B_j| ~ j (linear) -> need finer structure
import numpy as np
import mpmath as mp
mp.mp.dps = 20
zeros = np.load('/tmp/zeros_odlyzko_100k.npy')
gmax = float(zeros[-1])

def theta_doc(t):
    return np.pi - 2.0*np.arctan(2.0*t)
th = theta_doc(zeros)

print("=== B_j = Σ_{k≤j} 2sin((n+½)θ_k): growth law ===")
for n in [100, 500, 1000, 2000, 5000, 10000]:
    b = 2*np.sin((n+0.5)*th)
    B = np.cumsum(b)
    # track sup|B_j|, and |B_j| at various j, and where negative region ends
    j_neg = np.where(B < 0)[0]
    j0 = j_neg[-1] + 1 if len(j_neg) else 0
    # fit |B_j| ~ j^α locally: log|B| vs log j for j in [100, 1000] say
    js = np.array([100, 300, 1000, 3000, 10000, 30000])
    js = js[js < len(B)]
    print(f"n={n:6d}: j0(neg region)={j0:6d}, min B={B.min():+10.1f}, "
          f"|min|/j0={abs(B.min())/max(j0,1):.3f}", flush=True)
    # print |B_j| at sample j
    vals = []
    for jj in js:
        vals.append(f"j={jj}:{abs(B[jj-1]):8.1f}")
    print(f"        {'  '.join(vals)}")

print("\n=== local exponent α: log|B_j| vs log j (n=5000) ===")
n = 5000
b = 2*np.sin((n+0.5)*th)
B = np.cumsum(b)
for jj in [100, 300, 1000, 3000, 10000, 30000, 60000]:
    if jj <= len(B):
        print(f"  j={jj:6d}: |B_j|={abs(B[jj-1]):10.1f}  j^0.5={np.sqrt(jj):6.1f}  j^1={jj:6d}")

# negative contribution decomposition: which j dominate?
print("\n=== negative contribution by j-region (n=5000) ===")
n = 5000
a = np.sin(th/2)
da = a[:-1] - a[1:]
b = 2*np.sin((n+0.5)*th)
B = np.cumsum(b)
neg_contrib_j = da * np.where(B[:-1] < 0, -B[:-1], 0)
# cumulative negative contribution
cum_neg = np.cumsum(neg_contrib_j)
for jj in [10, 50, 100, 200, 500, 1000, 1150, 2000, 5000]:
    if jj <= len(cum_neg):
        print(f"  j≤{jj:5d}: cum neg = {cum_neg[jj-1]:+.5f}")
print(f"  total neg contrib = {cum_neg[-1]:+.5f}  (bound: (log j0)²/π ≈ {np.log(1150)**2/np.pi:.1f})")
