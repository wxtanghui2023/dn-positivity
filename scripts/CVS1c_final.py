"""
CVS1c: FINAL corrected minimal instance of the Connes-van Suijlekom mechanism.
Two construction errors corrected (recorded as ERR):
 E1 c_k = sum_{j=1..n} w_j cos(k th_j) with n atoms: rank <= 2n >= n+1, so NO forced deficiency.
 E2 "Gram of windows" of length n over b of length 2n is NOT Toeplitz (the inner-product range
    depends on the pair), so that route does not produce a Toeplitz matrix at all.
Correct construction: use r = n/2 atoms (symmetric measure, w>0, distinct thetas in (0,pi)).
  T_{kl} = sum_j w_j cos((k-l)th_j) = (1/2)[sum_j w_j z_j^{k-l} + c.c.]  => rank(T) <= 2r = n
  with generic data rank = n exactly => size n+1, deficiency exactly 1.
Then Prop 2.1 predicts: (1) kernel vector palindromic up to sign;
 (4) equivalently/visibly: the kernel polynomial P(X)=sum a_j X^j has ALL roots on the unit circle.
We test both, plus controls.
"""
import numpy as np
rng=np.random.default_rng(2026)
def build(n,r):
    th=np.sort(rng.uniform(0.2,np.pi-0.2,r)); w=rng.uniform(0.5,2.0,r)
    c=np.array([sum(w[j]*np.cos(k*th[j]) for j in range(r)) for k in range(n+1)])
    T=np.array([[c[abs(i-j)] for j in range(n+1)] for i in range(n+1)])
    return th,w,c,T
print("="*92)
print("MAIN: r = n/2 atoms (symmetric measure) => rank n, deficiency 1, kernel vector a")
print("="*92)
print(f"  {'n':>2} | {'r':>2} | {'size':>4} | {'rank':>4} | {'defic':>5} | {'palind':>9} | {'antipal':>9} | {'max||root|-1|':>13} | verdict")
res=[]
for n in (2,4,6,8,10,12):
    r=n//2; th,w,c,T=build(n,r)
    ev=np.linalg.eigvalsh(T); scale=max(1.0,abs(ev).max())
    rank=int(np.sum(ev>1e-9*scale)); defic=n+1-rank
    a=np.linalg.svd(T)[2][-1]
    pal =max(abs(a[j]-a[n-j]) for j in range(n+1))/max(abs(a))
    apal=max(abs(a[j]+a[n-j]) for j in range(n+1))/max(abs(a))
    roots=np.roots(a[::-1]); dev=max(abs(abs(roots)-1)) if len(roots) else float('nan')
    ok = (defic==1) and (min(pal,apal)<1e-7) and (dev<1e-7)
    res.append(ok)
    print(f"  {n:>2} | {r:>2} | {n+1:>4} | {rank:>4} | {defic:>5} | {pal:>9.2e} | {apal:>9.2e} | {dev:>13.2e} | {'PASS' if ok else 'FAIL'}")
print()
print("="*92); print("CONTROL i: r = n atoms => rank <= 2n, no forced deficiency (the earlier ERR)"); print("="*92)
for n in (4,6):
    th,w,c,T=build(n,n)
    ev=np.linalg.eigvalsh(T); rank=int(np.sum(ev>1e-9*max(1.0,abs(ev).max())))
    print(f"  n={n}, r={n}: size {n+1}, rank {rank}, deficiency {n+1-rank}  -> {'NO deficiency (as predicted)' if rank==n+1 else 'deficient'}")
print()
print("="*92); print("CONTROL ii: indefinite symbol (one weight negative) => positivity fails"); print("="*92)
for n in (4,6):
    r=n//2; th=np.sort(rng.uniform(0.2,np.pi-0.2,r)); w=rng.uniform(0.5,2.0,r); w[0]=-2.0
    c=np.array([sum(w[j]*np.cos(k*th[j]) for j in range(r)) for k in range(n+1)])
    T=np.array([[c[abs(i-j)] for j in range(n+1)] for i in range(n+1)]); ev=np.linalg.eigvalsh(T)
    print(f"  n={n}: min eig={ev.min():.3e} -> {'INDEFINITE (positivity fails, as expected)' if ev.min()<-1e-9 else 'PSD'}")
print()
print("="*92); print("SUMMARY"); print("="*92)
print(f"  main-test PASS count: {sum(res)}/{len(res)}")
print("""  If all PASS: the mechanism 'positive Toeplitz + rank deficiency 1 => kernel polynomial with
  all roots on the unit circle' is verified at the minimal instance. That is the algebraic form of
  'the Fourier transform has only real zeros', i.e. the engine of Connes-van Suijlekom.""")
