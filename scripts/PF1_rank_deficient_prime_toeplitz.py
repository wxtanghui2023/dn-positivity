"""
PF1: REOPEN the total-positivity / Polya-frequency line in the RANK-DEFICIENT case,
     using a PRIME-side Toeplitz matrix.
Motivation (lens L2): our earlier TP/PF work tested FULL-RANK objects, where (by Cor 1.1 of
Connes-van Suijlekom / Caratheodory-Fejer 1911) nothing can follow.  The content lives in the
RANK-DEFICIENT case.  C-vS's mechanism says the rank deficiency comes from using FINITELY MANY
primes.  So build exactly that:

    c_k = sum_{j: p_j <= P} w_j * cos(k * log p_j),     w_j > 0
    T_{kl} = c_{|k-l|},  size n+1,  rank(T) <= 2 r  (r = number of primes)

Question set:
 (q1) is T PSD and rank-deficient at the predicted rank 2r (r primes)?
 (q2) is the kernel vector palindromic (Prop 2.1(1)) ?
 (q3) does the kernel polynomial have ALL roots on the unit circle (Cor 1.1) ?
 (q4) *** do those unit-circle roots sit at angles equal to the PRIME FREQUENCIES log p_j *** ?
In (q4) a unit-circle root e^{i theta} means an oscillation at frequency theta, so if the
mechanism outputs roots at theta = log p_j then the positivity mechanism is CARRYING the prime
data -- which is the zeta-relevant question our earlier full-rank work could not reach.
"""
import numpy as np
from mpmath import mp, mpf, log as mlog, cos as mcos, polyroots, mpc
mp.dps=40
def primes_upto(P):
    ps=[]; 
    for x in range(2,P+1):
        if all(x%q for q in range(2,int(x**0.5)+1)): ps.append(x)
    return ps
def build(n, ps, weights=None):
    r=len(ps); lg=[mlog(p) for p in ps]
    w=weights if weights is not None else [mlog(p)/mp.sqrt(p) for p in ps]
    c=[sum(w[j]*mcos(k*lg[j]) for j in range(r)) for k in range(n+1)]
    T=np.array([[float(c[abs(i-j)]) for j in range(n+1)] for i in range(n+1)])
    return c,T,lg,w
print("="*94)
print("PF1: PRIME-SIDE rank-deficient Toeplitz (atoms at theta_j = log p_j), C-vS mechanism")
print("="*94)
print(f"  {'P':>4} {'r':>3} {'size':>5} {'rank':>5} {'2r':>4} {'min eig':>10} {'palind':>9} {'max||root|-1|':>13} {'root angles vs log p':>22}")
for P,ncap in ((7,24),(11,30),(13,32),(17,36),(19,40)):
    ps=primes_upto(P); r=len(ps); n=2*r   # size n+1 = 2r+1 > 2r => forced deficiency
    c,T,lg,w=build(n,ps)
    ev=np.linalg.eigvalsh(T); scale=max(1.0,abs(ev).max())
    rank=int(np.sum(ev>1e-9*scale))
    a=np.linalg.svd(T)[2][-1]
    pal=max(abs(a[j]-a[n-j]) for j in range(n+1))/max(abs(a))
    roots=np.roots(a[::-1]); mods=np.abs(roots)
    dev=max(abs(mods-1))
    ang=sorted([float(np.angle(z))%(2*np.pi) for z in roots if abs(abs(z)-1)<1e-6])
    lgmod=sorted([float(t)%(2*np.pi) for t in lg])
    # compare root angles with prime frequencies
    if ang and lgmod:
        d=max(min(abs(x-y) for y in lgmod) for x in ang)
        dsc=f"{d:.3e}"
    else: dsc="n/a"
    print(f"  {P:>4} {r:>3} {n+1:>5} {rank:>5} {2*r:>4} {ev.min():>10.2e} {pal:>9.2e} {dev:>13.2e} {dsc:>22}")
print()
print("="*94); print("CONTROL: same construction with NON-prime frequencies (random thetas) -- do roots still track them?"); print("="*94)
rng=np.random.default_rng(3)
for r in (3,5,7):
    th=np.sort(rng.uniform(0.3,np.pi-0.3,r)); w=[1.0]*r; n=2*r
    c=[sum(w[j]*np.cos(k*th[j]) for j in range(r)) for k in range(n+1)]
    T=np.array([[c[abs(i-j)] for j in range(n+1)] for i in range(n+1)])
    ev=np.linalg.eigvalsh(T); rank=int(np.sum(ev>1e-9*max(1,abs(ev).max())))
    a=np.linalg.svd(T)[2][-1]; roots=np.roots(a[::-1]); dev=max(abs(abs(roots)-1))
    ang=sorted([float(np.angle(z))%(2*np.pi) for z in roots if abs(abs(z)-1)<1e-6])
    d=max((min(abs(x-y) for y in (list(th)+[2*np.pi-t for t in th])) for x in ang), default=float('nan'))
    print(f"  r={r}: rank={rank} (2r={2*r})  max||root|-1|={dev:.2e}  root-angle vs theta mismatch={d:.3e}")
print()
print("="*94); print("READ-OFF"); print("="*94)
print("""  * rank = 2r  and  roots on the unit circle  =>  the C-vS mechanism is CONFIRMED in the
    prime-side (rank-deficient) setting, i.e. the very setting our earlier full-rank test could
    not reach.
  * if the root angles match log p_j, the positivity mechanism carries the prime frequencies.""" )
