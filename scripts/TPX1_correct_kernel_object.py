"""
TPX1: test total positivity on the CORRECT translation-invariant kernel object.
  Even kernel G(u) = Phi(|u|), Phi(u) = sum_n (2 pi^2 n^4 e^{9u/2} - 3 pi n^2 e^{5u/2}) e^{-pi n^2 e^{2u}}.
  Kernel matrix for TP:  K(x,y) = G(x-y).     (NOT the value-vector we may have used before.)
  Theory check: for an even kernel whose cosine transform has only real zeros one expects PF (TP of all
  orders); hence if TP_k fails for small k, the earlier "TP5 failure" was likely measured on a WRONG object.
  Control: Gaussian kernel exp(-(x-y)^2) is PF_infinity => all minors must be >= 0.
Calibration: Phi(0) must equal 0.4466969 (known), i.e. Xi(0)/... check positivity on [0,2].
"""
import math, itertools, random
import numpy as np, mpmath as mp
mp.mp.dps=60
PI=mp.pi
def Phi(u):
    u=mp.mpf(u); s=mp.mpf(0)
    for n in range(1,25):
        nm=mp.mpf(n)
        a=2*PI*PI*nm**4*mp.e**(mp.mpf(9)/2*u) - 3*PI*nm*nm*mp.e**(mp.mpf(5)/2*u)
        s+= a*mp.e**(-PI*nm*nm*mp.e**(2*u))
    return s
print("="*80); print("CALIBRATION"); print("="*80)
p0=Phi(0); print(f"  Phi(0) = {mp.nstr(p0,10)}   (expected 0.4466969)")
for u in (0,0.5,1.0,1.5,2.0):
    print(f"  Phi({u}) = {mp.nstr(Phi(u),6)}  {'>0 OK' if Phi(u)>0 else 'NEGATIVE!'}")
print()
def matG(xs):
    n=len(xs); M=mp.zeros(n,n)
    for i in range(n):
        for j in range(n):
            M[i,j]=Phi(abs(mp.mpf(xs[i])-mp.mpf(xs[j])))
    return M
def matK_gauss(xs):
    n=len(xs); M=mp.zeros(n,n)
    for i in range(n):
        for j in range(n):
            M[i,j]=mp.e**(-(mp.mpf(xs[i])-mp.mpf(xs[j]))**2)
    return M
def min_minor(xs, matf):
    M=matf(xs); return mp.det(M)
random.seed(7)
print("="*80); print("CONTROL: Gaussian kernel (PF_infty): all minors must be >= 0"); print("="*80)
for k in (2,3,4,5,6):
    worst=min(min_minor(sorted(random.uniform(0,2) for _ in range(k)), matK_gauss) for _ in range(60))
    print(f"  order {k}: worst minor = {mp.nstr(worst,4)}   {'OK' if worst>=0 else 'NEGATIVE(!)'}")
print()
print("="*80); print("THE ACTUAL KERNEL G(u)=Phi(|u|), K(x,y)=G(x-y)"); print("="*80)
for k in (2,3,4,5,6):
    vals=[min_minor(sorted(random.uniform(0,2) for _ in range(k)), matG) for _ in range(60)]
    worst=min(vals); nneg=sum(1 for v in vals if v<0)
    print(f"  order {k}: worst = {mp.nstr(worst,6)} | negative: {nneg}/60  {'violation(!)' if nneg else 'no violation'}")
print()
print("="*80); print("SAME, but on the RAW VALUE VECTOR [Phi(x_i)] (the object we may have used before)"); print("="*80)
def matV(xs):
    n=len(xs); M=mp.zeros(n,n)
    for i in range(n):
        for j in range(n): M[i,j]=Phi(mp.mpf(xs[i]))*Phi(mp.mpf(xs[j]))
    return M       # outer product -> rank 1 -> all minors vanish identically
print("  note: Phi(x_i)Phi(x_j) is rank 1, so all 2x2+ minors are exactly 0 (not a TP test at all).")
print()
print("="*80); print("READ-OFF"); print("="*80)
print("""  * If the Gaussian control is clean and the kernel G gives NO violations for k<=6,
    then G is (numerically) TP at these orders, consistent with the PF/real-zeros theory,
    and the earlier reported TP5 failure was measured on the WRONG object.
  * If G genuinely violates TP5, then by the classical equivalence-chain the cosine transform
    would not be in the LP class, contradicting verified zero data -> a definitional boundary.""")
