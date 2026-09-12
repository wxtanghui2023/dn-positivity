"""
TRACK A: is  A(n) = sum_{gamma<=T} [1 - cos(n theta_gamma)]  uniformly bounded below
         by a positive fraction of N(T) ?
theta_gamma = arg(1 - 1/rho) with rho = 1/2 + i gamma  =>  theta = atan2(gamma, gamma^2 - 1/4).
On the critical line |1-1/rho| = 1 exactly, so the contribution is 1 - cos(n theta) in [0,2].

Why it matters:
  lambda_n >= A(n) + (on-line tail) - n * B_T ,   B_T = (1/2) sum_{gamma>T} gamma^{-2}
  => positivity for n up to  ~ A(n)/B_T  ~ N(T)/B_T ~ T^2 * (log T)
  If min_n A(n) is a positive fraction of N(T), the range is REAL and can be much larger than
  the published n <= 1e5.  If A(n) dips to o(N(T)) for some n, the uniform bound fails.
"""
import numpy as np, time
g = np.load('data/zeros_odlyzko_2M.npy').astype(np.float64).ravel()
g = np.sort(g); T = float(g[-1]); N = g.size
th = np.arctan2(g, g**2 - 0.25)          # exact phase
S2 = float(np.sum(th**2)); S1 = float(np.sum(th))
print("="*94)
print("TRACK A: uniform lower bound for A(n) = sum_{gamma<=T}[1 - cos(n theta_gamma)]")
print("="*94)
print(f"  zeros: {N}   T = max gamma = {T:.6g}   N(T)/N = {N}")
print(f"  sum theta = {S1:.6g}   sum theta^2 = {S2:.6g}   (small-n prediction A(n) ~ n^2 S2/2)")
print(f"  B_T ~ (log T + 1)/(4 pi T) = {(np.log(T)+1)/(4*np.pi*T):.6g}")
print()
ns = list(range(1,401)) + [1000,5000,20000,100000,400000,1000000,4000000,20000000,100000000]
ns = np.array(sorted(set(ns)))
res = np.empty(len(ns))
t0=time.time()
for i,n in enumerate(ns):
    res[i] = np.sum(1.0 - np.cos(n*th))
print(f"  computed {len(ns)} values in {time.time()-t0:.1f}s")
print()
print("  %12s | %14s | %10s | %12s | %s" % ("n","A(n)","A(n)/N","pred n^2 S2/2","ratio A/pred"))
for i,n in enumerate(ns):
    if n<=20 or n in (400,1000,5000,20000,100000,400000,1000000,4000000,20000000,100000000):
        pred = n*n*S2/2.0
        r = res[i]/pred if pred>0 else float('nan')
        print("  %12d | %14.6e | %10.6f | %12.4e | %.4f" % (n,res[i],res[i]/N,pred,r))
print()
print("  minimum over sampled n:", res.min(), "at n =", ns[int(np.argmin(res))], " ratio =", res.min()/N)
print("  mean:", res.mean(), " ratio =", res.mean()/N)
print("  max A(n)/N:", res.max()/N)
print()
print("="*94); print("READ-OFF"); print("="*94)
print("""  * small n: A(n) should follow n^2 S2/2 (a PARABOLA) -- this sets the lower threshold.
  * large n: A(n) ~ N (the average of 1-cos over uniformly spread phases).
  * the decisive quantity is min_n A(n)/N over the sampled range: if it stays a healthy
    fraction of N, then lambda_n >= 0 holds for n up to ~ A(n)/B_T, i.e. a REAL range.""")
