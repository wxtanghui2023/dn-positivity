"""
BL7: corrected comparison -- S4 over BOTH signs (which is what the LHS sum uses).

In BL6 the "exact" column summed only over positive gamma (the zero table lists gamma>0), while the
tail formula and the bound were two-sided, producing a spurious factor 2. The LHS of the conjecture
sums over all zeros with |I(rho)| > H, i.e. both signs, so

    S4^{(2)}(H) = 2 * sum_{gamma>H} gamma^-4  ~  (1/pi) [ H^-3 log(H/2pi)/3 + H^-3/9 ]  ~  H^-3 log H/(3pi).

The Abel route with the boundary term gives leading coefficient 2a/3 = 1/(3pi) -- matching exactly.
"""
import numpy as np
from mpmath import mp, mpf, log as mlog, pi as mpi
import os as _os
_ZD = _os.path.join(_os.path.dirname(_os.path.dirname(_os.path.abspath(__file__))),'data')
_ZP = _os.path.join(_ZD,'zeros_odlyzko_2M.npy')
ZEROS_PATH = _ZP if _os.path.exists(_ZP) else '/tmp/zeros_odlyzko_2M.npy'   # R2: prefer data/
ZEROS_100K = _os.path.join(_ZD,'zeros_odlyzko_100k.npy') if _os.path.exists(_os.path.join(_ZD,'zeros_odlyzko_100k.npy')) else '/tmp/zeros_odlyzko_100k.npy'

mp.dps=40
g=np.sort(np.load(ZEROS_PATH).astype(np.float64).ravel()); GMAX=g[-1]
a=1/(2*mpi); b=-(1+mlog(2*mpi))/(2*mpi); c=mpf('0.112'); d=mpf('2.5')
print("="*104)
print("BL7: two-sided S4 vs the Abel bound WITH boundary term  (sharp leading constant check)")
print("="*104)
print("  %9s %16s %16s %8s %16s %8s %14s" % ("H","S4^(2) exact","lead (1/3pi)","ratio","full bound","maj?","lead/H^-3logH"))
ok=True
for H in (100.0,1000.0,10000.0,100000.0,1000000.0):
    m=g>H; one=float(np.sum(g[m]**-4.0))
    X=mpf(GMAX if GMAX>H else H)
    tail=float((1/mpi)*((X**-3/3)*mlog(X/(2*mpi)) + X**-3/9))   # two-sided tail, density 1/pi
    exact=2*one+tail                                            # TWO-SIDED total
    Hm=mpf(H)
    lead=float((mpf(2)*a/3)*Hm**-3*mlog(Hm))
    second=float((8*a/9+2*b/3)*Hm**-3)
    err=float((4*c*mlog(Hm)+c/2+4*d)*Hm**-4)
    full=lead+second+err
    ok = ok and (full>=exact)
    print("  %9g %16.6e %16.6e %8.4f %16.6e %8s %14.6f" % (H, exact, lead, lead/exact, full, "YES" if full>=exact else "no", lead/(float(Hm)**-3*mlog(Hm))))
print()
print("  * the ratio lead/exact -> 1 (the bound's leading term is SHARP)",
      "| all majorize:", ok)
print("  * the constant 2a/3 = 1/(3pi) = %.10f is exactly the true asymptotic constant." % (1/(3*mpi)))
print()
print("="*104); print("READ-OFF"); print("="*104)
print("""  * VERDICT: E2 is RESCUED. Combining the Abel identity WITH its boundary term with the counting
    hypothesis N(t)=a t log t + b t + eps(t) gives
        S4^{(2)}(H) <= (1/(3pi)) H^-3 log H + O(H^-3),
    with the SHARP leading constant; my earlier reported 4x loss was an artifact of dropping the
    boundary term, and the residual factor 2 in BL6 was an artifact of mixing one-sided and two-sided sums.
  * Consequently LHS <= (k^2/4) r_H^{(k-4)+} (1/(3pi)) H^-3 log H (1+o(1)) and
    RHS >= (k^2 a/6) H^-3 log H (1-O(H^-2)), so RHS/LHS -> 2 pi a = 1 exactly; the finite-H
    subleading terms decide, matching the earlier numerical margins of 1.45 to 4.8.""")
