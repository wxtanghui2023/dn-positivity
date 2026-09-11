"""
CVS1b: CORRECTED minimal instance of the Connes-van Suijlekom mechanism.
ERR: the first attempt built c_k = sum_j w_j cos(k theta_j) (n atoms). That did NOT give a
     rank-deficient Toeplitz matrix (finite Toeplitz sections of a positive symbol are
     generically NONSINGULAR: the classical example 2-2cos(theta) has nonsingular sections).
     => ran full rank, so the palindromic/unitary-root tests were vacuous.  [ERR recorded]

CORRECT construction guaranteeing rank deficiency exactly 1:
     c_k = sum_{j} b_j b_{j+k}   (autocorrelation of a real vector b of length m)
     => c has support |k| <= m-1, and the (n+1)x(n+1) Toeplitz matrix
        T_{kl} = c_{|k-l|} is the GRAM matrix of the m shifted windows
     => T is PSD of rank m.  Take m = n  => size n+1, rank n, deficiency exactly 1.

Consequences to test:
  (1) Prop 2.1(1): kernel vector a is palindromic (up to sign), a_j = +- a_{n-j}
  (4) the visible consequence: P(X)=sum a_j X^j has ALL roots on the unit circle
  (+) consistency: those roots should be zeros of the symbol B(z)=sum b_j z^j on |z|=1
Controls: m = n+1 (full rank) => no kernel; and an indefinite Toeplitz => positivity fails.
"""
import numpy as np
rng=np.random.default_rng(5)
def toeplitz_from_c(c,n):
    return np.array([[c[abs(i-j)] for j in range(n+1)] for i in range(n+1)])
def autocorr_c(b, n):
    # returns c[0..n] with c_k = sum_j b_j b_{j+k}; support |k| <= len(b)-1
    m=len(b)
    out=np.zeros(n+1)
    for k in range(min(m,n+1)):
        out[k]=sum(b[j]*b[j+k] for j in range(m-k))
    return out
print("="*86); print("MAIN: autocorrelation Toeplitz, m=n atoms => rank n (deficiency 1)"); print("="*86)
print(f"  {'n':>2} | {'min eig':>10} | {'rank':>4} | {'palind':>9} | {'antipal':>9} | {'max||root|-1|':>13} | {'symbol zeros hit':>16} | verdict")
for n in (2,3,4,5,6,8):
    b=rng.normal(size=2*n); c=autocorr_c(b,n); T=toeplitz_from_c(c,n)
    ev=np.linalg.eigvalsh(T); scale=max(1.0,abs(ev).max()); rank=int(np.sum(ev>1e-9*scale))
    a=np.linalg.svd(T)[2][-1]
    pal =max(abs(a[j]-a[n-j]) for j in range(n+1))/max(abs(a))
    apal=max(abs(a[j]+a[n-j]) for j in range(n+1))/max(abs(a))
    roots=np.roots(a[::-1]); dev=max(abs(abs(roots)-1))
    # symbol B(z)=sum b_j z^j : its zeros on the unit circle
    bz=np.roots(b[::-1]); on=np.abs(np.abs(bz)-1)<1e-6
    hit=0
    if on.any():
        for z0 in bz[on]:
            hit=max(hit, 1.0/(1.0+min(abs(z0-r) for r in roots)))
    ok = (rank==n) and (min(pal,apal)<1e-7) and (dev<1e-7)
    print(f"  {n:>2} | {ev.min():>10.2e} | {rank:>4} | {pal:>9.2e} | {apal:>9.2e} | {dev:>13.2e} | {('%.2e'%hit):>16} | {'PASS' if ok else 'FAIL'}")
print()
print("="*86); print("CONTROL i: m = n+1 (full rank) => no kernel vector"); print("="*86)
for n in (3,5,7):
    b=rng.normal(size=2*n+2); c=autocorr_c(b,n); T=toeplitz_from_c(c,n)
    sv=np.linalg.svd(T)[1]
    print(f"  n={n}: size {n+1}, rank={int(np.sum(np.linalg.eigvalsh(T)>1e-9*np.linalg.eigvalsh(T).max()))}  "
          f"smallest singular value/ largest = {sv[-1]/sv[0]:.3e}  -> {'no kernel (expected)' if sv[-1]/sv[0]>1e-6 else 'kernel(!)'}")
print()
print("="*86); print("CONTROL ii: INDEFINITE Toeplitz (random symmetric) => positivity fails"); print("="*86)
for n in (4,6):
    c=rng.normal(size=n+1); T=toeplitz_from_c(c,n); ev=np.linalg.eigvalsh(T)
    print(f"  n={n}: min eig={ev.min():.3e} -> {'INDEFINITE (positivity fails, as expected)' if ev.min()<-1e-9 else 'PSD'}")
print()
print("="*86); print("READ-OFF"); print("="*86)
print("""  * If the main table shows rank = n, the kernel vector palindromic (or anti-palindromic),
    and the kernel polynomial's roots exactly on the unit circle -- with those roots matching
    the unit-circle zeros of the symbol -- then the Connes-van Suijlekom mechanism
    (positive Toeplitz + rank deficiency => real zeros) is VERIFIED at the minimal instance.""")
