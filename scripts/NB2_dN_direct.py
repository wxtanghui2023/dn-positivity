#!/usr/bin/env python3
"""
NB2 (A4/E24-full): direct numerical evaluation of the Baez-Duarte distance d_N.

Object
------
  d_N^2 = inf_{A_N} (1/2pi) int_R |1 - zeta(1/2+it) A_N(1/2+it)|^2 dt/(1/4+t^2),
  A_N(s) = sum_{n<=N} a_n n^{-s}.
Writing f_n(t) := zeta(1/2+it) n^{-1/2-it} and the weight w(t) = 1/(1/4+t^2), this is
  d_N^2 = 1 - 2 Re(a.c) + a* G a ,   c_n = (1/2pi) int f_n w ,  G_{mn} = (1/2pi) int f_m conj(f_n) w,
so G is the Gram matrix (Hermitian PSD) and the minimiser solves G a = c, giving
  d_N^2 = 1 - conj(c) G^{-1} c .
Frontier (BBLS / Burnol):  d_N^2 ~ C/log N  with  C = 2 + gamma - log(4 pi) = 0.0461914179,
and the lower bound d_N^2 >= (C+o(1))/log N is PROVED, so any computed value must exceed C/log N
(up to truncation error) -- this is the calibration used here.

Inputs   : data/zeros_odlyzko_2M.npy is NOT needed; only mpmath's zeta.
Outputs  : scripts/NB2_dN_direct.txt
Caveats  : fixed quadrature grid and small N; |zeta|^2 ~ log^2 t so the t-integral converges.

STATUS: KNOWN FAILURE (2026-09-11 23:20)
----------------------------------------
This first implementation returns NEGATIVE d_N^2, which is impossible for a squared distance, so the
numbers are meaningless. Two concrete defects were identified:
  (1) the oscillatory integral (1/2pi) int |zeta|^2 (m/n)^{-it} w dt was handed to a general-purpose
      quadrature with maxdegree 6 over an interval of length 400, which cannot resolve the oscillation
      with period 2*pi/log(m/n) (about 9 in t for m,n = 1,2);
  (2) the precomputed zeta table was never used -- the integrand recomputed zeta at every node.
The correct route is the classical series/closed form for the multiplicative autocorrelation of the
fractional part (Baez-Duarte-Balazard-Landreau-Saias), or a Filon-type oscillatory quadrature; the
raw-quadrature approach is recorded here as a failed attempt, not as a result.
"""
import numpy as np, os
from mpmath import mp, mpf, mpc, zeta as mzeta, pi as mpi, log as mlog, euler as meuler, quad as mquad
mp.dps=25
C = 2 + meuler - mlog(4*mpi)
print("="*100)
print("NB2: direct d_N^2 vs the frontier constant  C = 2 + gamma - log(4 pi) = %.10f" % C)
print("="*100)
TMAX = 200.0; NODES = 1201
ts = np.linspace(-TMAX, TMAX, NODES)
def f(n, t):
    z = mzeta(mpc(mpf('0.5'), t))
    return z * mpc(mpf(n))**mpc(mpf('-0.5'), -t)
print("  precomputing zeta on the critical line (%d nodes, t up to %g) ..." % (NODES, TMAX))
tab = {}
for i,t in enumerate(ts):
    tab[i] = mzeta(mpc(mpf('0.5'), mpf(t)))
print("  done. computing c and G for N up to 10 ...")
def w(t): return mpf(1)/(mpf('0.25')+mpf(t)**2)
def integrand_c(n, t):
    z = mzeta(mpc(mpf('0.5'), mpf(t)))
    return z * mpc(mpf(n))**mpc(mpf('-0.5'), -mpf(t)) * w(t)
def integrand_G(m, n, t):
    z = mzeta(mpc(mpf('0.5'), mpf(t)))
    return (z*mpc(mpf(m))**mpc(mpf('-0.5'),-mpf(t))) * (z*mpc(mpf(n))**mpc(mpf('-0.5'),-mpf(t))).conjugate() * w(t)
print()
print("  %4s %16s %16s %16s %10s" % ("N","d_N^2 computed","C/log N","ratio","note"))
for N in (2,4,6,8,10):
    c = np.zeros(N, dtype=complex); G = np.zeros((N,N), dtype=complex)
    for m in range(1,N+1):
        c[m-1] = complex(mquad(lambda t: integrand_c(m,t), [-TMAX, TMAX], maxdegree=6)/(2*mpi))
        for n in range(1,m+1):
            v = complex(mquad(lambda t: integrand_G(m,n,t), [-TMAX, TMAX], maxdegree=6)/(2*mpi))
            G[m-1,n-1] = v; G[n-1,m-1] = v.conjugate()
    G = 0.5*(G+G.conj().T)
    try:
        w_, V = np.linalg.eigh(G)
        w_ = np.clip(w_, 1e-30, None)
        Gi = (V/w_) @ V.conj().T
        d2 = float(np.real(1 - c.conj() @ Gi @ c))
    except Exception as e:
        d2 = float('nan')
    ref = float(C/mlog(N))
    print("  %4d %16.8f %16.8f %16.4f %10s" % (N, d2, ref, d2/ref if ref>0 else float('nan'),
          "ok" if d2>=0 else "neg!"))
print()
print("  ratio column: computed d_N^2 divided by the conjectured asymptotic C/log N.")
print("  theory says the ratio should approach 1 slowly from above (Burnol's proved lower bound).")
print()
print("="*100); print("READ-OFF  (conclusion is generated from the numbers above)"); print("="*100)
print("""  * if all printed distances are positive and grow relative to C/log N as N decreases, the
    computation is consistent with the proved lower bound and the conjectured asymptotic;
  * with this fixed grid and these small N the truncation and quadrature errors dominate the
    constant, so the numbers are a calibration exercise, not a verification of the asymptotic.""")
