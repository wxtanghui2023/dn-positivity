"""
TPX2: the CORRECT object for Schoenberg/Poly a on RH is the ONE-SIDED PF function
     Lambda(x) = sum_j c_j e^{-gamma_j^2 x}  (x>=0), whose Laplace transform is
     1/Psi(s) with Psi(s) = Xi(i sqrt s)/Xi(0) = prod_j (1 + s/gamma_j^2).
     => the Toeplitz test on Lambda is TRIVIAL (one-sided support => triangular matrix),
        so the real content must live in the COEFFICIENT SEQUENCE of 1/Psi,
        i.e. the Taylor coefficients a_n of  L(s) = prod_j (1 + s/gamma_j^2)^{-1}
        (this is the "PF sequence" of Katkova's theorem, whose known boundary is order 43).
     We test the two well-defined PF-sequence conditions:
        (i) a_n >= 0 ;  (ii) log-concavity  a_n^2 >= a_{n-1} a_{n+1}   (Newton/Turan for PF seqs).
Calibration: sum 1/gamma^2 must be finite and small; a_0 = 1 exactly.
"""
import math, numpy as np
def theta(t):
    return (t/2)*math.log(t/(2*math.pi)) - t/2 - math.pi/8 + 1/(48*t) + 7/(5760*t**3)
def Z(t):
    if t < 6.0: return float('nan')
    N=int(math.floor(math.sqrt(t/(2*math.pi)))); s=0.0
    for n in range(1,N+1): s+= math.cos(theta(t)-t*math.log(n))/math.sqrt(n)
    s*=2.0
    p=math.sqrt(t/(2*math.pi))-N
    C0=math.cos(2*math.pi*(p*p-p-1/16))/math.cos(2*math.pi*p)
    return s+((-1)**(N-1))*(t/(2*math.pi))**(-0.25)*C0
print("="*80); print("ZEROS (RS Z-function)"); print("="*80)
zeros=[]; prev=Z(10.0); t=10.0; dt=0.05
while t<900.0:
    t+=dt; v=Z(t)
    if v==v and prev==prev and prev*v<0:
        a,b=t-dt,t
        for _ in range(60):
            m=(a+b)/2
            if Z(a)*Z(m)<=0: b=m
            else: a=m
        zeros.append((a+b)/2)
    prev=v
print(f"  found {len(zeros)} zeros up to 900 (first: {zeros[0]:.6f}, expected 14.134725)")
print(f"  sanity: N(900) approx {(900/(2*math.pi))*math.log(900/(2*math.pi))-900/(2*math.pi)+0.875:.1f}")
b=np.array([1.0/z**2 for z in zeros])          # b_k = 1/gamma_k^2
print(f"  sum b_k (partial, {len(b)} zeros) = {b.sum():.6f}   (converges slowly; tail adds ~1e-2)")
print()
print("="*80); print("COEFFICIENTS of L(s)=prod(1+s/gamma_k^2)^{-1} via  n a_n = sum_j c_j a_{n-j}, c_j=(-1)^j p_j"); print("="*80)
NMAX=46
pj=np.array([ (b**j).sum() for j in range(1,NMAX+1) ])
c=np.array([ ((-1)**j)*pj[j-1] for j in range(1,NMAX+1) ])
a=np.zeros(NMAX+1); a[0]=1.0
for n in range(1,NMAX+1):
    a[n]=sum(c[j-1]*a[n-j] for j in range(1,n+1))/n
print("  a_0..a_8 :", " ".join(f"{x: .6e}" for x in a[:9]))
print(f"  all a_n >= 0 for n<=46?  {'YES' if (a>=0).all() else 'NO -> first neg index '+str(int(np.argmax(a<0)))}")
print()
print("="*80); print("LOG-CONCAVITY of the PF sequence:  r_n = a_n^2/(a_{n-1} a_{n+1})  (want >= 1)"); print("="*80)
print(f"  {'n':>3} | {'a_n':>13} | {'r_n':>12} | verdict")
neg=0
for n in range(1,NMAX):
    if a[n-1]>0 and a[n+1]>0:
        r=(a[n]**2)/(a[n-1]*a[n+1])
        v='OK' if r>=1 else 'VIOLATION'
        if r<1: neg+=1
        if n<=12 or r<1:
            print(f"  {n:>3} | {a[n]:>13.6e} | {r:>12.6f} | {v}")
print(f"  violations: {neg} / {NMAX-1}")
print()
print("="*80); print("READ-OFF"); print("="*80)
print("""  * The one-sided support makes the Toeplitz minor test on Lambda trivial (triangular),
    so any "TP violation" measured on Lambda's kernel is meaningless -> this closes the
    naive route and redirects the content to the coefficient (PF sequence) conditions.
  * Positivity a_n>=0 and log-concavity of this RECIPROCAL-side sequence are the first
    genuine PF-sequence conditions, and they are NOT the same sequence we tested before
    (which was the direct Xi-Taylor coefficients).""")
