"""
TRACK C: the elementary PROVABLE argument, and its falsifiable core inequality.

Claim (proof sketch):  for rho = 1/2 + i gamma on the critical line,
  1 - (1-1/rho)^n = 1 - exp(i n theta_gamma),  theta_gamma = arg(1-1/rho) = atan2(gamma, gamma^2-1/4),
  so its real part is 1 - cos(n theta_gamma) in [0,2].
For gamma in the WINDOW [n/2, min(2n,T)]  we have n*theta_gamma in [~1/2, ~2]  because
theta_gamma = (1/gamma)(1 + O(gamma^-2)).  Hence each window term >= 1 - cos(1/2) = 0.12242...
Since ALL terms are >= 0 on the line, and the off-line contribution is bounded below by -n*B_T,
        lambda_n  >=  A_T(n) - n*B_T  >=  0.12242 * #{gamma in window} - n*B_T .
CORE INEQUALITY TO FALSIFY:   A_T(n)  >=  0.12242 * #{gamma in window}.

If this holds for every n, then lambda_n >= 0 as soon as
   0.12242 * #window  >=  n * B_T ,
and #window ~ (3 n log n)/(4 pi) for n << T, so the condition is met from tiny n onward,
giving a PROVABLE range n < 2T.
"""
import numpy as np
g = np.load('data/zeros_odlyzko_2M.npy').astype(np.float64).ravel(); g=np.sort(g)
T=float(g[-1]); N=g.size
th = np.arctan2(g, g**2-0.25)
B_T = (np.log(T)+1)/(4*np.pi*T)
C0 = 1.0-np.cos(0.5)
print("="*96)
print("TRACK C: falsify-or-confirm the core inequality  A_T(n) >= 0.12242 * #window")
print("="*96)
print("  T=%.6g  N=%d  B_T=%.6e  C0=1-cos(1/2)=%.6f" % (T,N,B_T,C0))
# count zeros <= x via searchsorted
def count_le(x): return int(np.searchsorted(g,x))
def A_direct(n, imax=None):
    ii = N if imax is None else min(imax,N)
    return float(np.sum(1.0-np.cos(n*th[:ii])))
rows=[]
for n in list(range(2,21))+[50,100,500,1000,5000,10000,20000,100000,300000,600000,1000000,1132490]:
    lo=n/2.0; hi=min(2.0*n,T)
    if hi<=lo: continue
    cw = count_le(hi)-count_le(lo)
    A  = A_direct(n)
    ratio = A/cw if cw>0 else float('nan')
    ok = (cw==0) or (A >= C0*cw)
    rows.append((n,cw,A,C0*cw,ratio,ok))
print("  %10s %8s %14s %14s %9s %s" % ("n","#window","A_T(n)","C0*#window","ratio","verdict"))
for n,cw,A,b,ratio,ok in rows:
    print("  %10d %8d %14.4e %14.4e %9.4f %s" % (n,cw,A,b,ratio,"OK" if ok else "**FAILS**"))
allok = all(r[5] for r in rows)
print()
print("  CORE INEQUALITY:", "HOLDS on all tested n" if allok else "FAILS on some n")
print()
print("="*96); print("RESIDUAL: can 2*A_T(n) >= n*B_T  be met for ALL n<2T ?"); print("="*96)
print("  %10s %16s %16s %12s" % ("n","2A_T(n)","n*B_T","margin factor"))
for n in [2,10,100,1000,10000,100000,300000,600000,1000000,1132490,1500000,2000000]:
    if n>int(2*T): continue
    A=A_direct(n); lhs=2*A; rhs=n*B_T
    print("  %10d %16.6e %16.6e %12.3e" % (n,lhs,rhs,lhs/rhs))
print()
print("="*96); print("READ-OFF"); print("="*96)
print("""  * if the core inequality holds everywhere, the proof goes through: positivity of every
    lambda_n for 2 <= n < 2T follows from (i) non-negativity of on-line terms, (ii) the window
    bound, (iii) zero-counting, (iv) the off-line bound -n*B_T.
  * the margin column shows how much room the argument has at each n.""")
