"""
BL1: CHANGE THE DECOMPOSITION.  Replace our "phase + window" argument by the
     Bombieri-Lagarias / Lagarias arithmetic decomposition and recompute the range.

Structure (Lagarias; B-L 1999 Thm 2; Voros for the explicit trend):
    lambda_n = S_inf(n) - S_f(n) + delta
    S_inf(n) = (n/2)(log n - 1 + gamma_E - log 2pi) + 3/4 + ...      [UNCONDITIONAL trend]
    S_f(n)   is the finite (zero-sum) part, bounded by an error budget B(n)
              built from: the zero count up to T, a zeta'/zeta bound on the horizontal
              segments at height T, and the classical explicit counting bounds.
              D-037 shape (its (4.1)):  B(n) ~ 2.54 sqrt(n) log n + O(sqrt n) + O(log^2 n)
              with   T = sqrt(n) + 1 .
    => margin(n) = S_inf(n) - B(n)      (need margin > 0)

TWO COMPETING CONSTRAINTS -- this script decides WHICH ONE BINDS:
  (K1) the ERROR BUDGET:  margin(n) > 0  <=>  the main term dominates B(n)
  (K2) the INPUT:         the method needs zero-freeness up to height T = sqrt(n)+1,
                          so with RH verified to T0 we get  n <= (T0-1)^2 .
If K1 already holds for small n, then K2 is the binding one and the range is (T0-1)^2
-- i.e. quadratic, as in the literature.  If instead K1 only holds up to ~c*T0^2 with
c<<1, then the budget binds and the constant c is the real target.

CALIBRATION: under RH, lambda_n = sum_{on-line}(1-cos(n theta_g)) which we can compute
from our zero data (the "2A(n)" of TRACK A/B).  Use it to check S_inf(n) against data.
"""
import numpy as np
from mpmath import mp, mpf, log as mlog, pi as mpi, euler as meuler
mp.dps=40
gam=meuler; LOG2PI=mlog(2*mpi)
def S_inf(n):
    n=mpf(n)
    return (n/2)*(mlog(n)-1+gam-LOG2PI)+mpf(3)/4
def B_D037(n, A=2.0, B0=2.0):
    """D-037 (4.1) shape, leading orders only, with its traced constants A,B0.
       B(n) = 2N(T) + 4T[(2/3)C0(T) + A log(T+2) + B0] + 40M0 + 2(e^4+1)[7H(T)+3.3] + I_I + 1
       We keep the first two pieces (dominant) and use classical bounds for N, C0."""
    n=mpf(n); T=(n**mpf('0.5'))+1
    FT=(T/(2*mpi))*mlog(T/(2*mpi*mpi)) + mpf(7)/8        # F(T) (R-vM main term)
    S_bnd=mpf('0.137')*mlog(T)+mpf('0.443')*mlog(mlog(T))+mpf('1.588')
    NT=FT+S_bnd                                          # classical upper bound for N(T)
    C0=(FT+mpf(1)-FT)+S_bnd+ (mpf('0.137')*mlog(T+1)+mpf('0.443')*mlog(mlog(T+1))+mpf('1.588'))
    piece1=2*NT
    piece2=4*T*((mpf(2)/3)*C0 + A*mlog(T+2) + B0)
    return piece1+piece2
print("="*96)
print("BL1: arithmetic decomposition -- which constraint binds?")
print("="*96)
print("  CALIBRATION: S_inf(n) vs our on-line computation 2A(n) (which equals lambda_n under RH)")
g=np.load('/tmp/zeros_odlyzko_2M.npy').astype(np.float64).ravel(); g=np.sort(g)
th=np.arctan2(g, g**2-0.25)
for n in (1,10,100,1000,10000):
    A=float(np.sum(1.0-np.cos(n*th)))
    print("    n=%6d : S_inf=%.6f   2A(n)=%.6f   ratio=%.4f" % (n,float(S_inf(n)),2*A,float(S_inf(n))/(2*A) if A else float('nan')))
print()
print("  MARGIN (main term minus the D-037-shaped budget):")
print("  %12s %16s %16s %12s" % ("n","S_inf(n)","B(n)","margin>0?"))
for n in (10,100,1000,10**4,10**5,10**6,10**8,10**10,10**12):
    s=float(S_inf(n)); b=float(B_D037(n))
    print("  %12d %16.6e %16.6e %12s" % (n,s,b,"YES" if s>b else "no"))
print()
print("="*96)
print("  INPUT LIMIT: with RH verified to T0, the method needs T=sqrt(n)+1 <= T0  =>  n <= (T0-1)^2")
print("="*96)
T0=3.000175e12
print("  T0 = %.6g  =>  input-limited range n <= (T0-1)^2 = %.6e" % (T0,(T0-1)**2))
print()
print("  COMBINED: range = min( budget-crossover , (T0-1)^2 )")
print("  -> if the budget allows all n up to the input limit, the range is QUADRATIC (as in the literature)")
print()
print("="*96); print("READ-OFF"); print("="*96)
print("""  * if S_inf(n) > B(n) from tiny n onward, then the budget is NOT binding and the range is
    purely the input limit (T0-1)^2 -- i.e. our '2T' was an artefact of the window argument.
  * the constant c in 'n <= c*T0^2' would then be exactly 1, and any improvement needs a
    BETTER BUDGET or a better choice of the height T(n) inside the method -- not the
    detection threshold.""")
