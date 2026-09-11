"""
PF2: remove the "atoms placed by hand" caveat of PF1.
PF1 used c_k = sum_p (log p)/sqrt(p) * cos(k log p)  -- atoms AT log p.
Is that canonical, or did we place the atoms?  In the EXPLICIT FORMULA the prime side is
    sum_p sum_{k>=1} (log p) p^{-k/2} [ f(k log p) + f(-k log p) ],
whose Fourier coefficients (f(x) = e^{i t x}) are carried by the discrete measure
    mu = sum_p sum_k (log p) p^{-k/2} ( delta_{k log p} + delta_{-k log p} ).
So the k-th Toeplitz coefficient of that measure is, by definition,
    c_k = sum_p sum_{k'>=1} (log p) p^{-k'/2} cos(k * k' log p),
which is NOT what PF1 used (PF1 kept only k'=1 and weights (log p)/sqrt(p) = (log p) p^{-1/2}).
=> PF2 = the canonical prime-side version: include the FULL prime-power series.
Question: does the C-vS mechanism still hold, and are the roots located at the
prime-power frequencies {+/- k log p}?
Also: does truncating the prime-power series (k' <= K) or the primes (p <= P) change the rank law?
"""
import numpy as np
from mpmath import mp, log as mlog, cos as mcos, sqrt as msqrt
mp.dps=40
def primes_upto(P):
    return [x for x in range(2,P+1) if all(x%q for q in range(2,int(x**0.5)+1))]
def coeffs(ps, K, kmax):
    """c_k for k=0..kmax using prime powers p^{k'} with k'<=K"""
    out=[]
    for k in range(kmax+1):
        s=mp.mpf(0)
        for p in ps:
            lp=mlog(p)
            for kp in range(1,K+1):
                s += (lp/msqrt(p)**kp)*mcos(k*kp*lp)
        out.append(s)
    return out
def analyze(c, kmax, label):
    T=np.array([[float(c[abs(i-j)]) for j in range(kmax+1)] for i in range(kmax+1)])
    ev=np.linalg.eigvalsh(T); scale=max(1.0,abs(ev).max()); rank=int(np.sum(ev>1e-9*scale))
    print(f'      [guard] size={kmax+1}, 2r={2*r} -> deficiency {"possible" if kmax+1>2*r else "IMPOSSIBLE"}')
    a=np.linalg.svd(T)[2][-1]
    pal=max(abs(a[j]-a[kmax-j]) for j in range(kmax+1))/max(abs(a))
    roots=np.roots(a[::-1]); dev=max(abs(abs(roots)-1))
    ang=sorted([float(np.angle(z))%(2*np.pi) for z in roots if abs(abs(z)-1)<1e-6])
    return rank, ev.min(), pal, dev, ang
print("="*96)
print("PF2: CANONICAL prime side (full prime-power series) -- does the mechanism survive?")
print("="*96)
ps=primes_upto(19); r=len(ps)
for K in (1,2,3):
    kmax=2*r+3   # GUARD: size=kmax+1 must exceed 2r, else no forced deficiency
    c=coeffs(ps,K,kmax)
    rank,mineig,pal,dev,ang=analyze(c,kmax,f"K={K}")
    # expected frequencies: {+/- k' log p}, k'<=K
    exp=sorted({float((s*kp*mlog(p))%(2*np.pi)) for p in ps for kp in range(1,K+1) for s in (1,-1)})
    m=len(ang)
    if m==len(exp): d=max(abs(ang[i]-exp[i]) for i in range(m))
    else: d=float(min(max(min(abs(x-y) for y in exp) for x in ang),9.99))
    print(f"  K={K} (prime powers up to p^{K}): size={kmax+1} rank={rank} minEig={mineig:+.2e} "
          f"palind={pal:.1e} |root|-1<={dev:.1e}  #roots={m} #freqs={len(exp)}  mismatch={d:.2e}")
print()
print("="*96)
print("PF2b: which object does the mechanism lock onto -- prime locations or prime-power locations?")
print("="*96)
for K in (1,2):
    kmax=2*r+3; c=coeffs(ps,K,kmax); rank,mineig,pal,dev,ang=analyze(c,kmax,f"K={K}")
    exp1=sorted({float((s*mlog(p))%(2*np.pi)) for p in ps for s in (1,-1)})
    exp2=sorted({float((s*kp*mlog(p))%(2*np.pi)) for p in ps for kp in range(1,K+1) for s in (1,-1)})
    def mm(l):
        if not ang or not l: return float('nan')
        return float(max(min(abs(x-y) for y in l) for x in ang))
    print(f"  K={K}: mismatch vs prime locations only = {mm(exp1):.3e} | vs prime-power set = {mm(exp2):.3e}")
print()
print("="*96); print("READ-OFF"); print("="*96)
print("""  * K=1 reproduces PF1 (prime locations only).  K>=2 adds the prime-power terms that the
    explicit formula actually contains.  If the mechanism still puts all roots on the unit circle
    for K>=2, then the rank-deficiency mechanism survives the canonical prime side, and the root
    locations tell us WHICH arithmetic data the mechanism locks onto.""")
