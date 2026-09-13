#!/usr/bin/env python3
"""
PAPERA candidate A -- band-limited approximation of g(z) = f(n*theta(z)): error budget test.

Object.  f = 1 - cos,  theta(t) = 2*arctan(1/(2t)),  g(z) = f(n*theta(z)).
    Fluc(n) = sum_{gamma<=T0} g(gamma) - int_0^{T0} g(t) d main(t),   main = Riemann-von Mangoldt.
    Want |Fluc(n)| < allowance = N(T0) - n*B_{T0},  B_{T0} = (log T0 + 1)/(4*pi*T0),  n <= T0^2.

Obstruction.  theta has branch points at z = +-i/2, so g is analytic in |Im z| < 1/2 but its
    first singularities sit ON the boundary |Im z| = 1/2, for EVERY n.  Near z = i/2,
        theta(z) ~ (1/i) log(z - i/2)   =>   g(z) ~ c * (z - i/2)^{-n},  |c| = 1/2,
    i.e. an n-th order branch point.  The admissible class of the Guinand-Weil explicit formula
    needs analyticity in |Im z| <= 1/2 + eps with eps > 0.

Construction tested (option (i) of the assignment: band-limiting).
    g_Delta(t) := int_{-Delta}^{Delta} ghat(x) e^{2*pi*i*x*t} dx   (FT of g truncated at bandwidth Delta).
    Admissibility: g_Delta is entire of exponential type 2*pi*Delta (Paley-Wiener), hence analytic in
    |Im z| <= 1/2 + eps for EVERY eps > 0, and |g_Delta(t)| << (1+|t|)^{-2} (g decays like t^{-2}),
    so g_Delta belongs to the admissible class for every Delta.  The construction never fails
    admissibility; it can only fail QUANTITATIVELY.

Error.  h = g - g_Delta satisfies  sup_R |h| <= int_{|x|>Delta} |ghat(x)| dx.  From the n-th order
    branch point, ghat decays exactly like e^{-pi|x|} |x|^{n-1} (rate set by the boundary distance
    1/2, polynomial factor set by the ORDER n).  Normalising on the singular part (t - i/2)^{-n}:
        |ghat(x)| = 2*pi*(2*pi|x|)^{n-1} e^{-pi|x|} / (n-1)!      (one frequency side)
    so that the two-sided tail integrates to
        eps(Delta,n) = 2^n * Gamma(n, pi*Delta) / (n-1)!  =  2^n * P( Poisson(pi*Delta) <= n-1 ).
    (Identity used: Gamma(n,x) = (n-1)! e^{-x} sum_{k<n} x^k/k!.)  The 1/k! in the Poisson sum is
    precisely the "lost n!" : the natural bandwidth pi*Delta = n/2 is suppressed by (n-1)!.

Budget.  |Fluc_g - Fluc_{g_Delta}| <= eps * ( #{gamma<=T0} + main(T0) )  ~=  2*eps*N(T0);
    allowance = 0.41*N(T0)  =>  need eps < 0.205  (the survey's 0.41 neglects this factor 2).

Inputs : data/zeros_odlyzko_2M.npy  (zeros to gamma ~ 1.13249e6 = the first T0)
Outputs: scripts/PAPERA_bandlimited_route.txt
"""
import os
import numpy as np
from mpmath import mp, mpf, mpc, log as mlog, exp as mexp, pi as mpi, findroot, factorial, quadosc, cos as mcos, sin as msin

mp.dps = 30
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
OUT = os.path.join(HERE, 'PAPERA_bandlimited_route.txt')

ZP = os.path.join(ROOT, 'data', 'zeros_odlyzko_2M.npy')
G = np.sort(np.load(ZP).astype(np.float64).ravel()) if os.path.exists(ZP) else None

def main_count(T):
    T = mpf(T)
    return T / (2 * mpi) * mlog(T / (2 * mpi)) - T / (2 * mpi) + mpf(7) / 8

def B_T0(T):
    return (mlog(mpf(T)) + 1) / (4 * mpi * mpf(T))

def D(a):                      # Poisson / KL rate  D(a) = a log a - a + 1
    return a * mlog(a) - a + 1

def log10_eps(Delta, n):
    """log10 of the sup-norm band-limiting error eps(Delta,n) = 2^n P(Poisson(pi*Delta) <= n-1)."""
    s = mpi * mpf(Delta)
    k = mpf(n) - 1
    if s >= k:                                   # lower tail (rare): P ~ exp(-s D(k/s))
        logP = -s * D(k / s)
    else:                                        # nearly 1: P = 1 - P(Poisson(s) >= k+1)
        z = s * D((k + 1) / s)
        logP = mlog(1 - mexp(-z)) if z < 400 else mpf(0)
    return (mpf(n) * mlog(2) + logP) / mlog(10)

def Delta_star(n, eps_target):
    """bandwidth needed to push eps(Delta,n) down to eps_target:  solve 1+log(2c)-c = log(eps)/n, Delta = c n/pi."""
    c = findroot(lambda x: 1 + mlog(2 * x) - x - mlog(eps_target) / mpf(n), mpf('2.678'))
    return c * mpf(n) / mpi, c

def ft_check(n, x):
    """numeric FT of G(t) = (t-i/2)^{-n} + (t+i/2)^{-n} at x (oscillatory quadrature on the full
    line), vs the closed form 2*pi*(2*pi|x|)^{n-1}e^{-pi|x|}/(n-1)!  (constant check)."""
    x = mpf(x)
    per = 1 / abs(x)

    def Gre(t):
        return 2 * mp.re((mpc(t) - mpc(0, mpf(1) / 2)) ** (-n))
    tot_r = tot_i = mpf(0)
    for a, b in [(-mp.inf, mpf(0)), (mpf(0), mp.inf)]:
        tot_r += quadosc(lambda t: Gre(t) * mcos(2 * mpi * x * t), [a, b], period=per)
        tot_i += -quadosc(lambda t: Gre(t) * msin(2 * mpi * x * t), [a, b], period=per)
    mag = mp.sqrt(tot_r * tot_r + tot_i * tot_i)
    pred = 2 * mpi * (2 * mpi * abs(x)) ** (n - 1) * mexp(-mpi * abs(x)) / factorial(n - 1)
    return mag, pred

lines = []
P = lambda s='': lines.append(s)

P("=" * 100)
P("PAPERA candidate A -- band-limited approximation of g = f(n*theta): error vs allowance")
P("=" * 100)

# ---- constant check of the FT tail formula (validates the '|c|=1/2, factor 2^n' bookkeeping) ----
P()
P("[0] constant check: |ghat(x)| for the singular part (t-i/2)^-n  vs  2*pi*(2*pi|x|)^(n-1)e^(-pi|x|)/(n-1)!")
for (n_, x_) in [(1, -0.7), (2, -0.7), (3, -0.7), (3, -1.3), (4, -1.0), (5, -0.9)]:
    mag, pred = ft_check(n_, mpf(x_))
    P("    n=%d  x=%5.1f :  numeric |FT| = %12.6f   closed form = %12.6f   ratio = %.4f"
      % (n_, x_, float(mag), float(pred), float(mag / pred)))

# ---- empirical zero count (data) ----
P()
if G is not None:
    P("[1] data check: data/zeros_odlyzko_2M.npy holds %d zeros, max gamma = %.4f" % (G.size, G[-1]))
    for Tc in (mpf('1000'), mpf('100000'), mpf('1132490')):
        emp = int(np.searchsorted(G, float(Tc)))
        P("    N(%.0f): empirical = %9d   Riemann-von Mangoldt = %12.3f   main/emp = %.6f"
          % (float(Tc), emp, float(main_count(Tc)), float(main_count(Tc)) / max(emp, 1)))
    T0_1 = mpf('1.1325e6')
    N1_emp = int(np.searchsorted(G, float(T0_1)))
else:
    T0_1 = mpf('1.1325e6'); N1_emp = None

CASES = [("T0 = 1.1325e6", mpf('1.1325e6')), ("T0 = 3.0001753328e12", mpf('3.0001753328e12'))]

for name, T0 in CASES:
    n = T0 ** 2
    N = main_count(T0)
    allow41 = mpf('0.41') * N
    allow_exact = N - n * B_T0(T0)
    Dnat = n / (2 * mpi)                      # natural bandwidth = max instantaneous frequency
    P()
    P("-" * 100)
    P("[%s]  n = T0^2 = %s" % (name, mp.nstr(n, 8)))
    P("     N(T0) (Riemann-von Mangoldt main) = %.6e" % float(N))
    if name.startswith("T0 = 1.1325") and N1_emp is not None:
        P("     empirical zero count <= T0          = %d   (S(T0) = %.1f)" % (N1_emp, N1_emp - float(N)))
    P("     allowance  0.41*N                 = %.4e     N - n*B_T0 = %.4e" % (float(allow41), float(allow_exact)))
    P("     natural bandwidth  Delta_nat = n/2pi = %.6e   (pi*Delta_nat = n/2)" % float(Dnat))
    l10_nat = log10_eps(Dnat, n)
    P("     eps(Delta_nat, n) = 2^n P(Poisson(n/2) <= n-1)  ~=  2^n :  log10 eps = %.4e" % float(l10_nat))
    P("     ratio eps(Delta_nat)/allowance      :  log10 = %.4e" % float(l10_nat - mp.log10(allow41)))
    # bandwidth required for eps = 0.205
    Ds, c = Delta_star(n, mpf('0.205'))
    P("     bandwidth needed for eps < 0.205 :  Delta* = %.6e  ( = %.6f * n,  pi*Delta* = %.6f * n )"
      % (float(Ds), float(Ds / n), float(c)))
    P("        vs natural: Delta*/Delta_nat = %.3f" % float(Ds / Dnat))
    l10_Ds = log10_eps(Ds, n)
    P("        check: log10 eps(Delta*) = %.3f  (target log10 0.205 = %.3f); the O(1) large-deviation"
      % (float(l10_Ds), float(mp.log10(mpf('0.205')))))
    P("        prefactor shifts the threshold by O((log n)/n) only -- immaterial")
    s_pr = 2 * mpi * Ds                        # exponential type of g_Delta
    P("        prime side then needs m <= e^(2*pi*Delta*) = e^(%.4e) :  log10 = %.4e"
      % (float(s_pr), float(s_pr / mlog(10))))
    # what bandwidth keeps the prime side polynomial in T0 ?  2*pi*Delta <= K log T0
    for K in (10, 1000, 10 ** 6):
        Dmax = K * mlog(T0) / (2 * mpi)
        n_max = (Dmax * mpi) / c                  # n_max with Delta* <= Dmax
        P("        if prime side capped at m <= T0^%d : Delta <= %.3e  =>  route works only for n <= %.3e"
          % (K, float(Dmax), float(n_max)))
    # construction (iii): smooth theta itself, then compose
    eta = mpf('0.41') / n                          # need sup|theta - theta_d| < eta
    Dth = mlog(1 / eta) / mpi
    for _ in range(40):
        Dth = (mlog(1 / eta) + mlog(Dth)) / mpi
    sig = 2 * mpi * n * Dth                        # exp type of f(n*theta_d), amplified by n
    P("     construction (iii) [smooth theta, then compose]: need eta < 0.41/n = %.3e" % float(eta))
    P("        theta-bandwidth Delta_theta = %.3e  (logarithmic!)  but composed type 2*pi*n*Delta_theta = %.4e"
      % (float(Dth), float(sig)))
    P("        prime side needs m <= e^(%.4e) :  log10 = %.4e  -- same blow-up, now from the n-fold type amplification"
      % (float(sig), float(sig / mlog(10))))

P()
P("=" * 100)
P("VERDICT: candidate A does NOT land.  With any bandwidth that keeps the explicit-formula prime side")
P("evaluable, eps(Delta,n) ~ 2^n (or worse) at n = T0^2, versus a required 0.205 -- a failure by")
P(" 10^(1e11) orders (case 1) / 10^(1e24) orders (case 2).  Making eps small forces pi*Delta >= 2.68 n.")
P("=" * 100)

with open(OUT, 'w') as fh:
    fh.write("\n".join(lines) + "\n")
print("\n".join(lines))
print("\n[written] " + OUT)
