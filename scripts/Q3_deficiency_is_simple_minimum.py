"""
Q3: WHERE DOES THE RANK DEFICIENCY COME FROM?
Hypothesis to verify:
   rank deficiency 1  <==>  the minimum eigenvalue is 0 with MULTIPLICITY 1
                        <==>  "simple minimum"  (the hypothesis of Theorem 6.1)
   palindromic kernel vector  <==>  the minimiser is EVEN under z -> 1/z
                        <==>  "even eigenfunction" (the other hypothesis of Theorem 6.1)
So Corollary 1.1 (Toeplitz) should be EXACTLY the finite case of Theorem 6.1 -- i.e. the "rank
deficiency" is not an extra hypothesis but the finite realisation of "simple, isolated, even
minimum".  Test it numerically:
   (1) build PSD Toeplitz of size n+1 with rank n  =>  eigenvalues: one 0 + n positive
   (2) the kernel vector minimises the quadratic form (eigenvalue 0)
   (3) it is palindromic  <=>  P(z) = z^n P(1/z) up to sign  <=>  EVEN
   (4) contrast: the full-rank case has NO zero eigenvalue and no even minimiser
"""
import numpy as np
rng=np.random.default_rng(2026)
def build(n, r):
    th=np.sort(rng.uniform(0.2,np.pi-0.2,r)); w=rng.uniform(0.5,2.0,r)
    c=np.array([sum(w[j]*np.cos(k*th[j]) for j in range(r)) for k in range(n+1)])
    return np.array([[c[abs(i-j)] for j in range(n+1)] for i in range(n+1)])
print("="*94)
print("Q3: is 'rank deficiency 1' the same as 'simple minimum'?  (and palindromic = even?)")
print("="*94)
print("  %3s | %-8s | %-22s | %-12s | %-16s | %s" % ("n","size","eigenvalue spectrum","min mult","palindromic?","P(z)=z^n P(1/z)?"))
for n in (2,4,6,8,10,12):
    r=n//2; T=build(n,r)
    ev=np.linalg.eigvalsh(T); scale=max(1.0,abs(ev).max())
    zero=np.sum(abs(ev)<1e-9*scale); pos=np.sum(ev>1e-9*scale)
    v=np.linalg.svd(T)[2][-1]          # eigenvector for eigenvalue 0
    # residual: is it really the minimiser?
    res=float(np.linalg.norm(T@v)/max(1e-30,np.linalg.norm(v)))
    pal=max(abs(v[j]-v[n-j]) for j in range(n+1))/max(abs(v))
    apal=max(abs(v[j]+v[n-j]) for j in range(n+1))/max(abs(v))
    # evenness of the polynomial: P(z)/z^{n/2} should be even  <=> palindromic
    spec="0 x%d + %d positive" % (zero,pos)
    print("  %3d | %-8d | %-22s | %-12s | %-16s | %s   [||Tv||/||v|| = %.1e]" % (
        n, n+1, spec, "simple" if zero==1 else "mult %d"%zero,
        "yes (%.1e)"%pal if pal<1e-8 else ("ANTI (%.1e)"%apal if apal<1e-8 else "no"),
        "yes" if min(pal,apal)<1e-8 else "no", res))
print()
print("="*94); print("CONTROL: full-rank PSD Toeplitz (r = n) -> no zero eigenvalue, no even minimiser"); print("="*94)
for n in (4,6,8):
    T=build(n,n); ev=np.linalg.eigvalsh(T); scale=max(1.0,abs(ev).max())
    zero=np.sum(abs(ev)<1e-9*scale); v=np.linalg.svd(T)[2][-1]
    pal=max(abs(v[j]-v[n-j]) for j in range(n+1))/max(abs(v))
    print("  n=%d: zero eigenvalues = %d, min eig = %.3e, palindromic deviation = %.2e -> %s"
          % (n, zero, ev.min(), pal, "no simple minimum (as expected)" if zero==0 else "unexpected"))
print()
print("="*94); print("READ-OFF"); print("="*94)
print("""  * If the main table shows exactly one zero eigenvalue together with palindromicity, then
      rank deficiency 1  ==  simple minimum  ==  hypothesis of Theorem 6.1,
    and the palindromic (or anti-palindromic) kernel vector IS the even eigenfunction.
    => Corollary 1.1 is the finite case of Theorem 6.1; the "deficiency" is not an extra
       hypothesis, it is the finite realisation of "simple, isolated, even minimum".
  * Consequently PF2's negative result says: the PRIME-SIDE matrix does not automatically have
    this property -- establishing it for the actual Weil form is exactly open problem (1).""")
