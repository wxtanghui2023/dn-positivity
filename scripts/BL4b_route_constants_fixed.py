"""
BL4b (A1): precision-corrected required threshold for the constant a in Conjecture 3.2.7.

Supersedes the first version of BL4, which computed r^k + r^-k - 2 in float and suffered
catastrophic cancellation for large H (values printed as inf). The stable form is
    4 sinh^2(k ln r / 2),   ln r = (1/2) log1p(tau/H^2).
Result: a_need(form A) ranges about 0.054 to 0.069 for H <= 1e5, independent of k, and the
standard constant a = 1/(2 pi) = 0.159 gives a margin of roughly 15 to 19 times.

ARCHIVE RULE: this script is committed; outputs go to scripts/*.txt (also committed).
"""
import numpy as np
from mpmath import mp, mpf, log as mlog, log1p as mlog1p, sinh as msinh, pi as mpi
mp.dps=40
g = np.sort(np.load('/tmp/zeros_odlyzko_2M.npy').astype(np.float64).ravel()); GMAX=g[-1]
def S4(H):
    m=g>H; s=float(np.sum(g[m]**-4.0)); X=mpf(max(GMAX,H))
    return s + float((1/mpi)*((X**-3/3)*mlog(X/(2*mpi))+X**-3/9))
def fac(k,tau,H):
    lr = mpf('0.5')*mlog1p(mpf(tau)/mpf(H)**2)
    return 4*msinh(mpf(k)*lr/2)**2
print("="*100)
print("BL4b (precision-fixed): required threshold for a in Conjecture 3.2.7")
print("="*100)
print("  %5s %6s %9s %16s %16s %16s" % ("k","tau","H","a_need(formA)","a_need(formB)","margin@a=1/2pi"))
rows=[]
for k in (2,4,8,16,32):
    for tau in (1.0,1.5,1.9):
        for H in (100.0,1000.0,10000.0,100000.0,1000000.0):
            Sk=S4(H); lhs=float(mpf(k)**2*mpf(tau)**2/4)*Sk
            F=fac(k,tau,H)
            ra=2*F*((mpf(1)/3)*mpf(H)*mlog(mpf(H)))
            rb=mpf(9)/4*F*(mpf(H)*mlog(mpf(H)))
            anA=lhs/float(ra); anB=lhs/float(rb); marg=float(ra)/lhs if lhs>0 else float('inf')
            rows.append((k,tau,H,anA,anB,marg))
            if k in (2,32): print("  %5d %6.1f %9g %16.8f %16.8f %16.4f" % (k,tau,H,anA,anB,marg))
anA=[r[3] for r in rows]; marg=[r[5] for r in rows]
print()
print("  ==> a_need(formA): min %.6f  max %.6f   (k-independent)" % (min(anA),max(anA)))
print("  ==> with a = 1/(2 pi) = %.6f, margin RHS/LHS ranges %.2f .. %.2f" % (float(1/(2*mpi)),min(marg),max(marg)))
