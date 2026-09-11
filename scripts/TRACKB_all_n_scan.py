"""
TRACK B: extend the verification from ~410 sampled n to ALL n <= NMAX.
Method: split A(n) = sum_{gamma<=T}[1-cos(n theta_gamma)] into
   NEAR  part: gamma <= K*n        (phases not small, must be summed directly)
   FAR   part: gamma >  K*n        (n*theta <= 1/K small => asymptotic expansion)
For the far part use 1-cos(x) = sum_{k>=1} (-1)^{k+1} x^{2k}/(2k)!  which converges fast for x<=0.1.
So  FAR(n) ~ sum_k (-1)^{k+1} n^{2k}/(2k)! * M_{2k}(K*n)
with M_{2j}(g) = sum_{gamma>g} theta_gamma^{2j}  (precomputed as reverse cumulative sums).
Calibration: must reproduce the earlier direct values A(1)=0.0115469338, A(20)=4.3843,
A(400)=374.0105, A(1000)=1162.106  -- if the split is implemented correctly.
"""
import numpy as np, time, sys
g = np.load('/tmp/zeros_odlyzko_2M.npy').astype(np.float64).ravel()
g = np.sort(g); T = float(g[-1]); N = g.size
th = np.arctan2(g, g**2 - 0.25)
K = 10.0
# reverse cumulative moments: M[j][i] = sum_{k>=i} th[k]^{2j}
J = 8
mom = np.zeros((J+1, N+1))
for j in range(1, J+1):
    mom[j, :-1] = np.cumsum((th**(2*j))[::-1])[::-1]
far_terms = np.array([1.0/np.math.factorial(2*k) for k in range(1, J+1)]) * \
            np.array([(-1)**(k+1) for k in range(1, J+1)])
def A_n(n):
    idx = np.searchsorted(g, K*n)                 # number of zeros with gamma <= K*n
    near = float(np.sum(1.0 - np.cos(n*th[:idx]))) if idx > 0 else 0.0
    i2 = min(idx, N)
    powers = np.array([float(n)**(2*k) for k in range(1, J+1)])
    far = float(np.sum(far_terms * powers * mom[1:J+1, i2]))
    return near + far, near, far
print("="*94)
print("TRACK B: calibration of the split (must reproduce the earlier direct values)")
print("="*94)
ref = {1:0.0115469338, 20:4.384270, 400:374.0105, 1000:1162.106}
ok = True
for n, r in ref.items():
    a, near, far = A_n(n)
    rel = abs(a-r)/max(1e-30, abs(r))
    print("  n=%5d : split=%.10f  direct=%.10f  rel.err=%.2e  (near=%.6f far=%.6f)" % (n, a, r, rel, near, far))
    if rel > 1e-4: ok = False
print("  CALIBRATION:", "PASS" if ok else "FAIL")
if not ok:
    print("  !! aborting: split not calibrated"); sys.exit(1)
NMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 20000
print()
print("="*94); print("SCAN: A(n) for ALL n = 1..%d ; positivity needs 2A(n) >= n*B_T" % NMAX); print("="*94)
B_T = (np.log(T)+1)/(4*np.pi*T)
print("  B_T = %.6e   (so the threshold is A(n)/n >= B_T/2 = %.3e)" % (B_T, B_T/2))
t0=time.time(); vals=np.empty(NMAX+1)
for n in range(1, NMAX+1):
    vals[n] = A_n(n)[0]
print("  computed in %.1f s" % (time.time()-t0))
rat = np.array([vals[n]/n for n in range(1, NMAX+1)])     # A(n)/n
print()
print("  min over n of A(n)/n      = %.6e  at n = %d" % (rat.min(), int(np.argmin(rat))+1))
print("  threshold B_T/2           = %.6e" % (B_T/2))
print("  margin factor at the min  = %.3e" % (rat.min()/(B_T/2)))
worst = np.argsort(rat)[:15]+1
print("  15 worst n (smallest A(n)/n):", list(map(int,worst)))
print("  corresponding A(n)/n       :", ["%.3e"%rat[n-1] for n in worst])
print()
print("  A(n)/N at selected n:", {n: round(vals[n]/N,4) for n in (1,10,100,1000,5000,10000,NMAX) if n<=NMAX})
np.save('scripts/trackB_vals.npy', vals)
print()
print("="*94); print("READ-OFF"); print("="*94)
print("""  * if min_n A(n)/n over ALL n <= NMAX still exceeds the threshold B_T/2 by a large factor,
    then positivity holds for EVERY n <= NMAX (not just sampled) at this height.
  * the list of worst n reveals whether the small values have structure (e.g. arithmetic).""")
