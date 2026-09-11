"""
BL4: strictify the route to Conjecture 3.2.7 and VERIFY THE CONSTANT CONDITION.

Route (elementary, avoids the failing power-series step):
  x_r := 1 + tau/gamma_r^2 > 1  for gamma_r != 0.
  (i)   x^{k/2} + x^{-k/2} - 2 = (x^{k/4} - x^{-k/4})^2 >= 0.
  (ii)  F(x) := x^{k/2}+x^{-k/2}-2 is strictly increasing for x > 1  [proved: F' > 0 for x>1, k>=2].
  (iii) Bound each term by the H-threshold, using  F(1+u) <= (k^2/4) r_H^{k-1} u^2  (u = tau/gamma^2),
        and sum with the explicit counting bound implied by the hypothesis on N(T).

Then LHS <= (k^2 r_H^{k-1} tau^2 / 4) * S4(H),   S4(H) := sum_{|gamma|>H} gamma^{-4}.

The conjecture's RHS has two forms in the thesis:
   RHS_A = 2 (r_H^k + r_H^{-k} - 2) [ (a/3) H log H + ((4a+3b^+)/9) H + 2c log H + 2d + c/4 ]
   RHS_B = (9/4)(r_H^k + r_H^{-k} - 2) [ a H log H + b^+ H + 2c log H + 2d ]     (the simplified form)

We compute the EXACT required threshold for the constant a (dominant term) for both forms:
   need  (k^2 r_H^{k-1} tau^2/4) * S4  <=  RHS  for all admissible (k, tau, H).
"""
import numpy as np
from mpmath import mp, mpf, log as mlog, e as me, pi as mpi
mp.dps=30
g = np.sort(np.load('/tmp/zeros_odlyzko_2M.npy').astype(np.float64).ravel())
GMAX = g[-1]
print("="*98)
print("BL4: route strictification -- S4(H) = sum_{|gamma|>H} gamma^{-4}   (data + analytic tail)")
print("="*98)
print("  zeros: %d, gamma_max = %.8g" % (g.size, GMAX))
def S4(H):
    """exact on data + analytic tail beyond GMAX using the smooth zero density (both signs)."""
    m = g > H
    s = float(np.sum(g[m]**-4.0))
    if GMAX > max(H,1.0):
        # tail for one sign: int_{GMAX}^inf t^-4 (1/2pi) log(t/2pi) dt ; both signs => factor 2
        X=mpf(GMAX) if GMAX>H else mpf(H)
        A = float((1/mpi)*( (X**-3/3)*mlog(X/(2*mpi)) + X**-3/9 ))
        s += A
    return s
print()
print("  %12s %18s %18s" % ("H","S4(H)","S4*H^3/logH (should -> ~1/(3pi)=0.1061)"))
for H in (10.0,100.0,1000.0,10000.0,100000.0,1000000.0):
    s=S4(H); print("  %12g %18.8e %18.6f" % (H,s,s*H**3/np.log(H)))
print()
print("="*98)
print("REQUIRED THRESHOLD for a:  a_need = [ (k^2 r_H^{k-1} tau^2/4) S4(H) ] / [ 2 (r_H^k+r_H^{-k}-2) * (H log H)/3 ]")
print("="*98)
rng=[(2,1.0),(2,1.5),(4,1.0),(4,1.5),(8,1.0),(8,1.5),(16,1.5),(32,1.9)]
print("  %5s %6s %10s %14s %14s %14s" % ("k","tau","H","a_need (form A)","a_need (form B)","RHS_A/LHS at a=0.112"))
for k,tau in rng:
    for H in (100.0,1000.0,10000.0,100000.0):
        rH=(1.0+tau/H**2)**0.5
        S=S4(H)
        lhs=(k*k*rH**(k-1)*tau*tau/4.0)*S
        fac=rH**k+rH**(-k)-2.0
        ra=2.0*fac*((1.0/3.0)*H*np.log(H))
        rb=(9.0/4.0)*fac*(H*np.log(H))
        print("  %5d %6.1f %10g %14.6f %14.6f %14.4f" % (k,tau,H, lhs/ra, lhs/rb, ra/lhs))
print()
print("  a_need (form A) = the smallest a for which the rigorous bound fits form A's dominant term.")
print("  a_need (form B) = the same for the simplified (9/4)-form.")
print()
print("="*98); print("READ-OFF"); print("="*98)
print("""  * a_need is INDEPENDENT of k (the k-dependence cancels in the leading term) -- check the table.
  * form A requires a > a_need(A); form B requires a > a_need(B) = (3/8)*a_need(A).
  * the hypothesis's own constants (a,b,c,d) come from the explicit N(T) bound; whether they meet
    the threshold is THE remaining check.""")
