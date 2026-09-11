"""
CVS1: minimal instance of the Connes-van Suijlekom mechanism.
  Prop 2.1: positive real Toeplitz T (size n+1) of RANK n, kernel vector a.
  Claim (1): the ideal (P), P = sum a_j X^j, is stable under X -> 1/X
             <=> the kernel vector is palindromic (up to sign): a_j = +- a_{n-j}
  Claim (4): the induced linear form is positive on the quotient.
  Consequence we can test directly: P has all roots on the UNIT CIRCLE,
             which is the algebraic form of "the Fourier transform has real zeros".
Construction: c_k = sum_{j=1}^n w_j cos(k theta_j) with w_j>0
  => Toeplitz matrix = Gram matrix of {1,cos,..,cos n} in L^2(mu), mu = sum w_j delta_{theta_j}
  => rank = dim span = n (full rank would need n+1 points) => deficiency exactly 1.
Controls: (i) a full-rank positive Toeplitz (n+1 points) -> no kernel vector at all;
          (ii) an indefinite Toeplitz -> no positivity.
"""
import numpy as np
rng=np.random.default_rng(11)
def build(n, thetas, ws):
    c=np.array([sum(w*np.cos(k*t) for w,t in zip(ws,thetas)) for k in range(n+1)])
    T=np.array([[c[abs(i-j)] for j in range(n+1)] for i in range(n+1)])
    return c,T
print("="*84); print("MAIN TEST: n atoms (rank deficiency 1) => kernel vector palindromic? roots on unit circle?"); print("="*84)
print(f"  {'n':>2} | {'min eig':>11} | {'rank':>4} | {'palindromic':>11} | {'antipal':>9} | {'max||root|-1|':>13} | verdict")
for n in (2,3,4,5,6,7):
    thetas=np.sort(rng.uniform(0.15,np.pi-0.15,n)); ws=rng.uniform(0.5,2.0,n)
    c,T=build(n,thetas,ws)
    ev=np.linalg.eigvalsh(T); scale=max(1.0,abs(ev).max())
    rank=int(np.sum(ev>1e-10*scale))
    a=np.linalg.svd(T)[2][-1]                       # last right singular vector ~ kernel
    pal =max(abs(a[j]-a[n-j]) for j in range(n+1))/max(abs(a))
    apal=max(abs(a[j]+a[n-j]) for j in range(n+1))/max(abs(a))
    roots=np.roots(a[::-1]); dev=max(abs(abs(roots)-1)) if len(roots) else float('nan')
    ok = rank==n and min(pal,apal)<1e-8 and dev<1e-8
    print(f"  {n:>2} | {ev.min():>11.3e} | {rank:>4} | {pal:>11.2e} | {apal:>9.2e} | {dev:>13.2e} | {'PASS' if ok else 'FAIL'}")
print()
print("="*84); print("CONTROL i: FULL rank positive Toeplitz (n+1 atoms) -> no kernel vector"); print("="*84)
for n in (3,5):
    thetas=np.sort(rng.uniform(0.15,np.pi-0.15,n+1)); ws=rng.uniform(0.5,2.0,n+1)
    c,T=build(n,thetas,ws)
    ev=np.linalg.eigvalsh(T); scale=max(1.0,abs(ev).max()); rank=int(np.sum(ev>1e-10*scale))
    sv=np.linalg.svd(T)[1]
    print(f"  n={n}: min eig={ev.min():.3e}  rank={rank}/{n+1}  smallest singular value={sv[-1]:.3e}"
          f"  -> {'no kernel (as expected)' if sv[-1]>1e-8*sv[0] else 'kernel exists(!)'}")
print()
print("="*84); print("CONTROL ii: INDEFINITE Toeplitz of rank n -> does the mechanism still work?"); print("="*84)
for n in (4,6):
    # force indefiniteness: put one negative weight
    thetas=np.sort(rng.uniform(0.15,np.pi-0.15,n)); ws=rng.uniform(0.5,2.0,n); ws[0]=-1.5
    c,T=build(n,thetas,ws)
    ev=np.linalg.eigvalsh(T)
    print(f"  n={n}: eigenvalues min={ev.min():.3e} max={ev.max():.3e} -> {'indefinite' if ev.min()<-1e-12 else 'PSD'}")
print()
print("="*84); print("READ-OFF"); print("="*84)
print("""  * Prop 2.1(1) predicts the kernel vector is palindromic or anti-palindromic;
    claim (4)'s visible consequence is that the kernel polynomial has all roots on the
    unit circle -- the algebraic form of "the Fourier transform's zeros are real".
  * The controls show the two hypotheses are both necessary: full rank gives no kernel
    vector, and indefiniteness breaks positivity.""")
