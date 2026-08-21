#!/usr/bin/env python3
"""
Strictification attempt: explicit van der Corput bound for A-part.
epsA_m = -int_{B_m} A(t) cos(phi(t)) S(t) dt,  A = 2 theta'(n+1/2) sin(theta/2)
phi(t) = (n+1/2) theta(t), theta(t) = pi - 2 arctan(2t), theta' = -4/(1+4t^2)

van der Corput (1st derivative form, Stein Ch.VIII):
If |phi'| >= lambda and phi' monotone on [a,b], then
  |int_a^b e^{i phi} g dt| <= (1/lambda) [4 V(g) + 2|g(b)-g(a)|]  (roughly)
Actually standard: |int_a^b e^{i phi} g dt| <= C (1/lambda) (|g(b)| + int |g'|)
where C = 2 or so.

A(t) is EXPLICIT. S(t): |S| <= C_B log t, V(S) = total variation (saturates ~1000).
g = A*S.  V(g) <= sup|A| V(S) + sup|S| V(A).

Compute: (1) the actual vdC bound terms per block, (2) sum over blocks,
(3) compare with true |sum epsA|, (4) extract the effective constant vs log n.
"""
import numpy as np, math

z = np.load('/home/node/.openclaw/workspace/dn-project/data/zeros_odlyzko_100k.npy')
def theta(t): return math.pi - 2*np.arctan(2*np.asarray(t, dtype=float))
def dtheta(t): return -4.0/(1+4*np.asarray(t, dtype=float)**2)
def theta_RS(t):
    import mpmath as mp
    mp.mp.dps = 18
    return float(mp.im(mp.loggamma(mp.mpc(0.25, t/2))) - (t/2)*mp.log(mp.pi))
def S_of_t(t):
    return np.searchsorted(z, t, side='right') - theta_RS(t)/math.pi - 1
def t_of_phi(phi, n):
    th = phi/(n+0.5)
    return 0.5/np.tan(th/2)

def A_of_t(t, n):
    return 2*dtheta(t)*(n+0.5)*np.sin(theta(t)/2)

for n in [1000, 5000, 10000]:
    Mprime = int(math.floor((n+0.5)*theta(z[0])/math.pi))
    t1 = t_of_phi(math.pi, n)
    # van der Corput bound: sum over blocks of (1/lambda_m)*(|g(b)|+|g(a)|+V_m(g))
    # lambda_m = min|phi'| on block = |phi'(t_m)| (phi' increasing in |.| as t decreases? phi'=-c/(1+4t^2), |phi'| decreasing in t)
    # block B_m = [t_{m+1}, t_m], t_{m+1} < t_m, so min |phi'| at t_m (larger t)
    total_bound = 0.0
    total_true = 0.0
    total_absA = 0.0
    for m in range(1, Mprime+1):
        ta = t_of_phi((m+1)*math.pi, n)  # smaller t
        tb = t_of_phi(m*math.pi, n)      # larger t
        # min |phi'| on block: at tb
        lam = (n+0.5)*4.0/(1+4*tb*tb)
        # sup|A| on block
        Aa, Ab = abs(A_of_t(ta, n)), abs(A_of_t(tb, n))
        supA = max(Aa, Ab)
        # sup|S| on block: use max |S| at zeros in block (approx)
        zz = z[(z >= ta) & (z <= tb)]
        if len(zz): supS = max(abs(S_of_t(t)) for t in zz)
        else: supS = max(abs(S_of_t(ta)), abs(S_of_t(tb)))
        # V(g) on block ~ supA*V(S_block) + supS*V(A_block)
        # V(A): A monotone? A = 2 theta'(n+1/2) sin(theta/2), theta' decreasing magnitude, sin(theta/2) increasing... 
        # crude: V(A) <= |A(ta)| + |A(tb)| + intermediate; use |A| variation via samples
        As = np.abs(A_of_t(np.linspace(ta, tb, 100), n))
        VA = np.abs(np.diff(As)).sum()
        # V(S_block): S varies ~ jumps at zeros
        VS_block = len(zz)  # crude: each zero contributes ~1 jump
        Vg = supA*VS_block + supS*VA
        bd = (1.0/lam)*(Vg + 2*supA*supS)
        total_bound += bd
        # true epsA
        edges = np.concatenate([[ta], zz, [tb]])
        val = 0.0
        for i in range(len(edges)-1):
            a, b = edges[i], edges[i+1]
            if b - a < 1e-10: continue
            Smid = S_of_t(0.5*(a+b))
            ts = np.linspace(a, b, 40)
            phs = (n+0.5)*theta(ts)
            val += -np.trapz(A_of_t(ts, n)*np.cos(phs)*Smid, ts)
        total_true += val
        total_absA += abs(val)
    print(f"n={n}: M'={Mprime}")
    print(f"  真实 ΣepsA = {total_true:+.5f}  Σ|epsA| = {total_absA:.5f}")
    print(f"  vdC 上界 Σ = {total_bound:.3f}  (vdC/|真实| = {total_bound/max(abs(total_true),1e-9):.1f})")
    print(f"  vdC 界 / log n = {total_bound/math.log(n):.4f}  (裕量常数 = 0.1934)")
