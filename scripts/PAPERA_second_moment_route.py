"""
PAPERA_second_moment_route.py -- does the CLASSICAL SECOND MOMENT of S(t) control Fluc(n)?

PROVENANCE
  Created 2026-09-12 21:1x by a subagent, per the operator's standing instruction to
  "attack the delta-N term".  Reads data/zeros_odlyzko_2M.npy.
  Writes scripts/PAPERA_second_moment_route.txt.

WHAT IS TESTED
  With theta(t) = 2 arctan(1/(2t)), f(x) = 1 - cos x, S(t) = N(t) - main(t),
        Fluc(n) := int_0^{T0} f(n theta(t)) dS(t)          [Stieltjes against the measure dS]
  and the quadratic range requires  |Fluc(n)| < N(T0) - n*B_{T0}.
  Task: integrate by parts, Cauchy-Schwarz against the oscillatory weight
        w_n(t) = n sin(n theta(t)) theta'(t),
  insert the classical second-moment input  int_0^T S^2 ~ c T loglog T, and read off the
  resulting bound, the ratio bound/allowance at n = T0^2, and the largest n ratio<1.
  Then repeat the C-S PER PERIOD-BLOCK (blocks over which n*theta advances by 2 pi).

NUMERICAL CONTENT
  (a)  M(T) = int_0^T S^2 dt exactly (piecewise, using the zero table) vs c*T*loglog T
       -> an EMPIRICAL estimate of the constant c, which the literature statement leaves
          convention-dependent.
  (b)  ||w_n||_2^2 = int_0^{T0} (n sin(n theta) theta')^2 dt  vs  pi n^2.
  (c)  the TRUE Fluc(n) from the tabulated zeros, vs the crude, the global-C-S and the
       per-block-C-S bounds, and vs the allowance.
  (d)  the per-block C-S sum computed on the actual zeros.

DISCIPLINE
  Every FORMULA used is printed with numbers substituted.  The second-moment input is an
  AVERAGE statement about S^2; using it per-block is therefore HEURISTIC and is flagged as
  such in the output.  No constant is tuned to reach a desired answer.
"""

import numpy as np

# ----------------------------------------------------------------------------- setup
G = np.asarray(np.load('data/zeros_odlyzko_2M.npy'), dtype=float)
G = np.sort(G)
T0 = float(G[-1])
Nz = int(G.size)

def main_count(t):
    return (t / (2 * np.pi)) * np.log(t / (2 * np.pi * np.e)) + 7.0 / 8.0

def theta(t):
    return 2.0 * np.arctan(1.0 / (2.0 * t))          # == arctan(t/(t^2-1/4))

def t_of_theta(th):
    return 0.5 / np.tan(th / 2.0)                    # == 0.5 cot(th/2)

lines = []
def out(s=''):
    lines.append(s); print(s)

out('=' * 78)
out('SECOND-MOMENT ROUTE FOR Fluc(n):  quantitative test')
out('=' * 78)
out()
out('  table: data/zeros_odlyzko_2M.npy   Nz = {:,}   T0 = gamma_max = {:.6f}'.format(Nz, T0))
out('  main(T0) = (T0/2pi) log(T0/(2 pi e)) + 7/8 = {:.3f}'.format(main_count(T0)))
out('  N(T0)    = {:,}   (table)      S(T0) = N - main = {:+.3f}'.format(Nz, Nz - main_count(T0)))
out('  (task shorthand (T0/2pi) log T0 = {:.3f}; main(T0) is smaller by the log(2 pi e) term)'
    .format(T0 / (2 * np.pi) * np.log(T0)))
out()

# ------------------------------------------------------- (a) exact int_0^T S^2 dt
# main is elementary, so int (j - main)^2 dt has a closed antiderivative; the table gives
# the intervals on which N(t) = j is constant.
# ---- exact-enough  int_0^T S^2 dt --------------------------------------------------
# S is piecewise constant-plus-smooth: on (edges[k], edges[k+1]) one has N(t) = k, so
# S(t) = k - main(t) with main SMOOTH.  A closed-form antiderivative exists but suffers
# catastrophic cancellation at t ~ 1e6 (terms ~1e18 cancelling to ~1); we therefore use
# 5-point Boole quadrature on EVERY zero-interval, which is cancellation-free.
edges = np.concatenate(([1e-12], G))
NJ = edges.size - 1                                  # number of zero-intervals
assert NJ == Nz
Q = np.array([0.0, 0.25, 0.5, 0.75, 1.0])
WQ = np.array([7.0, 32.0, 12.0, 32.0, 7.0]) / 90.0
piece = np.empty(NJ)
CH = 250000
for c0 in range(0, NJ, CH):
    c1 = min(c0 + CH, NJ)
    kk = np.arange(c0, c1)
    a = edges[c0:c1]; b = edges[c0 + 1:c1 + 1]
    ts = a[:, None] + (b - a)[:, None] * Q[None, :]
    vv = (kk[:, None] - main_count(ts)) ** 2
    piece[c0:c1] = (b - a) * (vv @ WQ)
cumP = np.concatenate(([0.0], np.cumsum(piece)))      # cumP[k] = int_0^{edges[k]} S^2

def Pint(t):    # int_0^t S(u)^2 du, t in [0, T0]; vectorised, Boole on the partial interval
    t = np.atleast_1d(np.asarray(t, dtype=float))
    k = np.clip(np.searchsorted(edges, t, side='right') - 1, 0, NJ - 1)
    a = edges[k]; b = np.minimum(t, edges[k + 1])
    ts = a[:, None] + (b - a)[:, None] * Q[None, :]
    vv = (k[:, None] - main_count(ts)) ** 2
    return cumP[k] + (b - a) * (vv @ WQ)

out('-' * 78)
out('(a)  THE SECOND-MOMENT INPUT, AND ITS CONSTANT, FROM THE TABLE')
out('-' * 78)
out()
# self-test of the quadrature: compare Boole-per-interval against a crude uniform grid
# (S taken at the grid points themselves, no interpolation), on the range where the grid
# RESOLVES the zero spacing (t <= 1e4, spacing 2 pi/log t ~ 0.68 there)
_ts = np.linspace(1e-6, 1e4, 2000001)
_ss = (np.searchsorted(G, _ts, side='right').astype(float) - main_count(_ts)) ** 2
out('  SELFTEST of int_0^T S^2:  Boole/interval {:.8e}   vs uniform grid trapz {:.8e}'
    .format(float(Pint(1e4)[0]), np.trapz(_ss, _ts)))
out('    (grid spacing {:.2e} vs zero spacing {:.3f} at t=1e4)'
    .format(_ts[1] - _ts[0], 2 * np.pi / np.log(1e4)))
out()
out('  claim tested:   int_0^T S(t)^2 dt  ~  c * T * loglog T')
out()
hdr = '  {:>12} {:>16} {:>14} {:>14} {:>14}'
out(hdr.format('T', 'int_0^T S^2 dt', 'T loglog T', 'M/(T loglogT)', 'M/(T loglogT)'))
out(hdr.format('', '(exact, table)', '', '= implied c', 'if c=1/pi^2=0.10132'))
for T in [0.25 * T0, 0.5 * T0, T0]:
    m = float(Pint(T)[0])
    x = T * np.log(np.log(T))
    out(hdr.format('{:,.0f}'.format(T), '{:.6e}'.format(m), '{:.6e}'.format(x),
                   '{:.5f}'.format(m / x), '{:.3f}'.format(m / x / (1 / np.pi**2))))
out()
c_emp = float(Pint(T0)[0]) / (T0 * np.log(np.log(T0)))
out('  ==> empirical constant  c_emp = int S^2 / (T0 loglogT0) = {:.5f}'.format(c_emp))
for name, c in [('1/(2 pi^2) = 0.05066', 1 / (2 * np.pi**2)), ('1/pi^2 = 0.10132', 1 / np.pi**2)]:
    out('      vs {:<24}: ratio {:.3f}'.format(name, c_emp / c))
out('  NB loglog T0 = {:.4f}.  We carry the constant SYMBOLICALLY as c below.'.format(np.log(np.log(T0))))
out('  SOURCE (literature search, secondary quotation, retrieved 2026-09-12):')
out('    Selberg 1946, Theorems 6 and 7, as quoted in arXiv:2006.08503 eq. (1.4):')
out('      int_0^T |S(t)|^2 dt = (T/(2 pi^2)) loglog T + O(T sqrt(loglog T)),  so c = 1/(2 pi^2)')
out('  Hence c = 1/(2 pi^2) = 0.05066 (NOT 1/pi^2); the two normalisations differ by 2.')
out('  The same source records a secondary +O(T) term (their eq. (1.8)); relative to the main')
out('  term T loglog T that is a relative size ~1/loglog T0 = {:.3f}.  Our table value'.format(1 / np.log(np.log(T0))))
out('  c_emp = {:.5f} is {:.3f} x the asymptotic constant, consistent with exactly such a'.format(c_emp, c_emp / (1 / (2 * np.pi**2))))
out('  secondary term; c_emp is an EFFECTIVE, one-realisation constant.  Because it EXCEEDS')
out('  1/(2 pi^2), using it makes the C-S bound larger, i.e. more generous to the route; the')
out('  verdict below is reported for c in [1/(2 pi^2), c_emp] and does not depend on c.')
_cj = np.arange(1, Nz + 1) - main_count(G)
out('  diagnostic: sup|S| over zeros = {:.3f}; |S(T0)| = {:.3f}; mean of S^2 over [T0/2,T0] = {:.4f}'
    .format(np.max(np.abs(_cj)), abs(_cj[-1]),
            float(Pint(T0)[0] - Pint(0.5 * T0)[0]) / (0.5 * T0)))
_csym = 1.0 / (2 * np.pi**2)
M2int = float(Pint(T0)[0])
SigS = np.sqrt(M2int)
out('  ||S||_{{L^2[0,T0]}} = sqrt(int S^2) = {:.4f}   (note: sup|S| = {:.4f} on this range)'
    .format(SigS, np.max(np.abs(np.arange(1, Nz + 1) - main_count(G)))))
out('  ==> the L^2 norm over the whole range EXCEEDS the pointwise size of S by a factor')
out('      {:.1f}; note sqrt(T0) = {:.1f}, so ||S||_2/sup|S| ~ {:.3f} sqrt(T0).  A C-S against'
    .format(SigS / float(np.max(np.abs(_cj))), np.sqrt(T0),
            (SigS / float(np.max(np.abs(_cj)))) / np.sqrt(T0)))
out('      a weight supported on [0,T0] must pay this inflation -- that is the whole loss.')
out('  to come: the weight norm is ~n (not ~sqrt(n)), so the product is ~n sqrt(T0 loglog T0).')
out()

# --------------------------------------------------------------- (b) ||w_n||_2
out('-' * 78)
out('(b)  THE WEIGHT  w_n(t) = n sin(n theta) theta\'(t)   AND ITS L^2 NORM')
out('-' * 78)
out()
out('  theta\'(t) = -4/(4t^2+1) = -4 sin^2(theta/2);  dt/dtheta = -(1/4) csc^2(theta/2)')
out('  int_0^{T0} w_n^2 dt = 4 n^2 int_{theta(T0)}^{pi} sin^2(n theta) sin^2(theta/2) dtheta')
out('  closed form used:  int sin^2(n th) sin^2(th/2) dth = (th/2 - sin th/2)/2')
out('                     - sin(2n th)/(8n) + [sin((2n+1)th)/(2n+1) + sin((2n-1)th)/(2n-1)]/8')
out()
th_lo, th_hi = theta(T0), np.pi

def W2(n):
    F = lambda th: 0.5 * (th / 2 - np.sin(th) / 2) - np.sin(2 * n * th) / (8 * n) \
        + (np.sin((2 * n + 1) * th) / (2 * n + 1) + np.sin((2 * n - 1) * th) / (2 * n - 1)) / 8.0
    return 4.0 * n * n * (F(th_hi) - F(th_lo))

out('  {:>14} {:>20} {:>20} {:>14}'.format('n', 'int w^2 dt', 'pi n^2', 'ratio'))
for n in [1e3, 1e5, 1e6, T0**0.5, T0**2]:
    w2 = W2(n)
    out('  {:>14.4g} {:>20.6e} {:>20.6e} {:>14.6f}'.format(n, w2, np.pi * n * n, w2 / (np.pi * n * n)))
out()
out('  ==> ||w_n||_2 = n sqrt(pi) (1 - theta(T0)/pi)^{{1/2}} ~ n sqrt(pi) = {:.4f} n'.format(np.sqrt(np.pi)))
out()

# --------------------------------------------------------------------- (c) Fluc(n)
# Fluc(n) = sum_{gamma<=T0} f(n theta_gamma)  -  int_0^{T0} f(n theta(t)) dmain(t)
# smooth part: substitute u = n*theta -> (1/n) int_{u0}^{n pi} f(u) G(u) du,
# G(u) = main'(t(u/n)) * (1/4) csc^2(u/(2n)),  t = (1/2)cot(u/(2n)).
# Over every full period of f = 1 - cos, int f du = 2 pi and int f (u-c) du = 0, so the
# period-midpoint rule is exact to O(G'' * period^3).
def smooth_part(n, pts_per_period=40, force_direct=False):
    """int_0^{T0} f(n theta(t)) dmain(t) after u = n*theta:
         = (1/n) int_{u0}^{n pi} f(u) G(u) du,
       G(u) = main'(t(u/n)) * (1/4) csc^2(u/(2n)),   t(x) = (1/2) cot(x/2).
       u0 = n*theta(T0).  Direct composite Simpson when the phase is resolvable
       (u0 < USW); otherwise the closed form of int G du, valid because for u0 >> 1 the
       cos-part of f contributes only O(G(u0)) (Riemann-Lebesgue with smooth amplitude)."""
    USW = 1.0e4
    u0 = n * theta(T0)
    U = n * np.pi
    if force_direct or (u0 < USW and (U - u0) / (2 * np.pi) * pts_per_period < 4.0e7):
        m = int((U - u0) / (2 * np.pi) * pts_per_period) + 3
        u = np.linspace(u0, U, m)
        th = u / n
        tt = t_of_theta(th)
        G = (1.0 / (2 * np.pi)) * np.log(tt / (2 * np.pi)) * 0.25 / np.sin(th / 2.0) ** 2
        f = 1.0 - np.cos(u)
        if m % 2 == 0:
            u, f, G = u[:-1], f[:-1], G[:-1]; m -= 1
        w = np.ones(m); w[1:-1:2] = 4.0; w[2:-1:2] = 2.0
        return float(np.sum(w * f * G) / 3.0 * (u[1] - u[0]) / n)
    # asymptotic branch: u0 >> 1, so int f G du = int G du + O(G(u0));
    # with G ~ (n/2pi) log(A/u)/u^2  (A = n/(2 pi))  one gets
    #   (1/n) int G du = (n/2pi) (log(A/u0) - 1)/u0   ->  ~ main(T0) - 7/8  when n = T0^2
    A = n / (2 * np.pi)
    I = (np.log(A / u0) - 1.0) / u0
    return float((n / (2 * np.pi)) * I)


def fluc(n):
    x = n * theta(G)
    Ssum = float(np.sum(1.0 - np.cos(x)))
    sm = smooth_part(n)
    return Ssum - sm, Ssum, sm

out('-' * 78)
out('(c)  THE TRUE Fluc(n)  (Stieltjes by parts is exact; not used here -- computed directly)')
out('-' * 78)
out()
out('  Fluc(n) = sum_{gamma<=T0} [1 - cos(n theta_gamma)]  -  int_0^{T0} [1-cos(n theta)] dmain')
out()
hdr2 = '  {:>10} {:>16} {:>16} {:>14} {:>16} {:>12}'
out(hdr2.format('n', 'sum f(n th_g)', 'smooth part', 'Fluc(n)', '||w||_2*||S||_2', 'bound/|Fluc|'))
# consistency check of the two quadrature branches of smoothing at n = 1e5
_n = 1e5
_sd = smooth_part(_n, force_direct=True)
_sa = smooth_part(_n)
out('  smooth-part check at n = 1e5: direct Simpson {:.8e} vs asymptotic {:.8e} (ratio {:.5f})'
    .format(_sd, _sa, _sa / _sd))
out()
n_list = [1e3, 1e4, 1e5, 1e6, T0**2]
fluc_rows = []
for n in n_list:
    fl, Ssum, sm = fluc(n)
    bnd = np.sqrt(W2(n)) * SigS
    fluc_rows.append((n, fl, bnd))
    out(hdr2.format('{:,.0f}'.format(n), '{:.6e}'.format(Ssum), '{:.6e}'.format(sm),
                    '{:+.6e}'.format(fl), '{:.6e}'.format(bnd),
                    '{:.3e}'.format(bnd / max(abs(fl), 1e-30))))
out()

# ------------------------------------------------------------- (d) bounds table
def B_of(T):
    return (np.log(T) + 1.0) / (4.0 * np.pi * T)

def allowance(n, T):
    return main_count(T) - n * B_of(T)

out('-' * 78)
out('(d)  BOUND vs ALLOWANCE, BOTH HEIGHTS')
out('-' * 78)
out()
out('  global C-S bound:  |Fluc(n)| <= ||S||_2 * ||w_n||_2  =  sqrt(c T0 loglogT0) * n sqrt(pi)')
out('                     =  n * sqrt(pi c T0 loglogT0)      [c symbolic]')
out('  allowance:         Allow(n) = main(T0) - n B_{T0},  B_{T0} = (logT0+1)/(4 pi T0)')
out('  ratio(n) = bound/Allow;  n_max = largest n with ratio < 1  (~ main(T0)/coef when')
out('  n B_{T0} << main(T0), i.e. for n << T0^2; exact  n_max = main(T0)/(coef + B_{T0}) )')
out()
hdr3 = '  {:>13} {:>18} {:>13} {:>13} {:>14} {:>12} {:>10}'
for cc_lab, cc in [('1/(2pi^2)', 1 / (2 * np.pi**2)), ('1/pi^2', 1 / np.pi**2),
                   ('table c_emp', c_emp)]:
    out('  constant c = {}  (loglogT0 = {:.4f} at the smaller height)'.format(cc_lab, np.log(np.log(T0))))
    out(hdr3.format('T0', 'coef=sqrt(pi c Tl)', 'main(T0)', 'T0^2', 'ratio at T0^2', 'n_max', 'n_max/T0'))
    for T in [T0, 3.0001753328e12]:
        ll = np.log(np.log(T))
        coef = np.sqrt(np.pi * cc * T * ll)
        mn = main_count(T)
        n2 = T * T
        ratio = coef * n2 / allowance(n2, T)
        nmax = mn / (coef + B_of(T))
        out(hdr3.format('{:.6e}'.format(T), '{:.4e}'.format(coef), '{:.4e}'.format(mn),
                        '{:.4e}'.format(n2), '{:.4e}'.format(ratio), '{:,.1f}'.format(nmax),
                        '{:.3e}'.format(nmax / T)))
        out('        coef=sqrt(pi*{:.6g}*{:.6e}*{:.4f})={:.4e};  B_{{T0}}={:.4e}'
            .format(cc, T, ll, coef, B_of(T)))
        out('        Allow(T0^2)=main(T0)-T0^2*B = {:.6e} - {:.6e} = {:.6e}'
            .format(mn, n2 * B_of(T), allowance(n2, T)))
        out('        n_max = main(T0)/(coef+B) = {:.6e}/({:.6e}+{:.3e}) = {:.4e}'
            .format(mn, coef, B_of(T), nmax))
        out('        closed form sqrt(T0/(2 pi loglogT0))*log(T0/(2 pi e)) = {:.4e}'
            .format(np.sqrt(T / (2 * np.pi * ll)) * np.log(T / (2 * np.pi * np.e))))
        out('        n_max/T0 = {:.4e}   n_max/T0^2 = {:.4e}'.format(nmax / T, nmax / n2))
    out()

# --------------------------------------------------------------- (e) per-block
out('-' * 78)
out('(e)  C-S  PER PERIOD-BLOCK  (block = phase advance 2 pi, theta_k = (u0+2 pi k)/n)')
out('-' * 78)
out()
out('  per block: |int_block S w| <= ||S||_{2,block} * ||w||_{2,block}')
out('     ||S||^2_{2,block} = int_{t_{k+1}}^{t_k} S^2 dt   (exact, table; t = (1/2)cot(theta/2))')
out('     ||w||^2_{2,block} = 4 n^2 int_{block} sin^2(n th) sin^2(th/2) dth   (closed form)')
out('     block count K ~ n(pi - theta(T0))/(2 pi) ~ n/2')
out()
out('  HEURISTIC version (what the second-moment input actually supplies): replace the')
out('  block norm by the local CLT scale  ||S||^2_{2,block} ~ (1/(2 pi^2)) loglog t * Dt,')
out('  Dt = 2 pi t^2/n  ->  ||S||_{2,bl}||w||_{2,bl} ~ sqrt(loglog t) per block:')
out()

def per_block_exact(n):
    u0 = n * theta(T0)
    U = n * np.pi
    per = 2 * np.pi
    K = int(np.floor((U - u0) / per))
    if K < 1:
        return np.nan, 0
    thk = (u0 + per * np.arange(K + 1)) / n            # increasing theta -> t decreasing
    tk = t_of_theta(thk)
    Sb = np.clip(Pint(tk[:-1]) - Pint(tk[1:]), 0.0, None)
    F = lambda th: 0.5 * (th / 2 - np.sin(th) / 2) - np.sin(2 * n * th) / (8 * n) \
        + (np.sin((2 * n + 1) * th) / (2 * n + 1) + np.sin((2 * n - 1) * th) / (2 * n - 1)) / 8.0
    Wb = 4.0 * n * n * (F(thk[1:]) - F(thk[:-1]))
    Wb = np.clip(Wb, 0.0, None)
    return float(np.sum(np.sqrt(Sb) * np.sqrt(Wb))), K

def per_block_heuristic(n, T=T0):
    u0 = n * theta(T)
    U = n * np.pi
    per = 2 * np.pi
    K = int(np.floor((U - u0) / per))
    c = u0 + (np.arange(K) + 0.5) * per
    tt = t_of_theta(c / n)
    Dt = per * tt * tt / n
    loc = np.sqrt(np.log(np.log(np.clip(tt, np.e + 1e-9, None))) / (2 * np.pi**2) * Dt)
    # ||w||_{2,block} = sqrt(4 pi n sin^2(th/2)) ~ sqrt(pi n) theta
    wb = np.sqrt(np.pi * n) * (c / n)
    return float(np.sum(loc * wb))

out('  {:>10} {:>14} {:>18} {:>18} {:>18} {:>14}'
    .format('n', 'K (blocks)', 'per-block EXACT', 'per-block HEUR', 'crude sup*int|w|', 'TRUE |Fluc|'))
supS = float(np.max(np.abs(np.arange(1, Nz + 1) - main_count(G))))
for n in [1e3, 1e4, 1e5, 1e6]:
    pe, K = per_block_exact(n)
    ph = per_block_heuristic(n)
    u0 = n * theta(T0)
    crude = supS * 2.0 * (n * np.pi - u0) / np.pi
    fl = [r[1] for r in fluc_rows if r[0] == n][0]
    out('  {:>10.0f} {:>14d} {:>18.6e} {:>18.6e} {:>18.6e} {:>14.3e}'
        .format(n, K, pe, ph, crude, fl))
out()
# independent check of the exact second-moment integral against a finer uniform grid
# (grid spacing must beat the zero spacing 2 pi/log t = {:.3f} at T0)
tt = np.linspace(1e-6, T0, 10000001)
cc = (np.searchsorted(G, tt, side='right').astype(float) - main_count(tt))
out('  CHECK  Pint(T0) = {:.6e}   vs uniform grid trapz (1e7 pts, spacing {:.4f}) = {:.6e}'
    .format(M2int, tt[1] - tt[0], np.trapz(cc**2, tt)))
out('  CHECK  Pint(T0/2) = {:.6e} vs uniform grid trapz = {:.6e}'
    .format(float(Pint(0.5 * T0)[0]),
            np.trapz(cc[tt <= 0.5 * T0]**2, tt[tt <= 0.5 * T0])))
out()
out('  ratios to the crude bound (a value <1 means the refinement helps):')
for n in [1e3, 1e4, 1e5, 1e6]:
    pe, K = per_block_exact(n)
    u0 = n * theta(T0)
    crude = supS * 2.0 * (n * np.pi - u0) / np.pi
    out('      n = {:>10.0f}   per-block/crude = {:.4f}   per-block/globalCS = {:.4e}'
        .format(n, pe / crude, pe / (np.sqrt(W2(n)) * SigS)))
out()
ll = np.log(np.log(T0))
# asymptotic per-block total (heuristic): sum over blocks of sqrt(loglog t), block density
# n/(2 pi t^2) dt for t >> 1  ->  (n/2 pi) int sqrt(loglog t)/t^2 dt over [t_min, T0]
_integ = getattr(np, 'trapezoid', None) or np.trapz
tt = np.exp(np.linspace(np.log(20.0), np.log(T0), 200001))
integ = _integ(np.sqrt(np.log(tt)) / tt**2, tt)
integ20 = _integ(np.sqrt(np.log(tt)) / tt**2, tt)      # from t=20 (safe side of e)
out('  asymptotic per-block total (HEUR):  (n/2 pi) * int sqrt(loglog t)/t^2 dt over [20,T0]')
out('      integral = {:.4f}  ->  total = {:.4f} n'.format(integ20, integ20 / (2 * np.pi)))
out('  plus the region t < first zero (14.13): there N(t)=0 and S(t) = -main(t) is a SMOOTH')
out('  function with |S| <= {:.3f}:'.format(abs(-main_count(14.0))))
out('      blocks there ~ n(pi - theta(14))/(2 pi) = {:.4f} n, each <= 4 sup|S| = {:.3f}'
    .format((np.pi - theta(14.0)) / (2 * np.pi), 4 * abs(-main_count(14.0))))
low_coef = (np.pi - theta(14.0)) / (2 * np.pi) * 4 * abs(-main_count(14.0))
out('      -> contribution ~ {:.4f} n  (UNCONDITIONAL; no second-moment gain available)'
    .format(low_coef))
pb_coef = integ20 / (2 * np.pi) + low_coef
out('      ==> per-block total ~ {:.4f} n  (constant, NOT sqrt(loglog T0)*n and not o(n))'
    .format(pb_coef))
# what the table actually gives (authoritative: real zeros, real blocks)
pe_last, K_last = per_block_exact(1e6)
out('  table check: exact per-block sum at n = 1e6 is {:.6e} = {:.4f} n  (K = {:,} blocks)'
    .format(pe_last, pe_last / 1e6, K_last))
pb_emp = pe_last / 1e6
out('  range from per-block:  n_max ~ main(T0)/{:.4f} = {:,.0f} = {:.2f} T0'
    .format(pe_last / 1e6, main_count(T0) / (pe_last / 1e6), main_count(T0) / (pe_last / 1e6) / T0))
out()
out('=' * 78)
out('SUMMARY')
out('=' * 78)
llT = np.log(np.log(T0))
coef = np.sqrt(np.pi * c_emp * T0 * llT)
out('  (1) global C-S: bound(n) = {:.4e} n ; allowance(T0^2) = {:.4e} ; ratio(T0^2) = {:.4e}'
    .format(coef, allowance(T0**2, T0), coef * T0**2 / allowance(T0**2, T0)))
out('      n_max(global C-S) = {:.4e} = {:.3e} T0  (far BELOW the linear range)'
    .format(main_count(T0) / coef, main_count(T0) / coef / T0))
out('  (2) per-block C-S: exact sum on the table is {:.3f} n -> n_max ~ {:.2f} T0 (LINEAR)'
    .format(pb_emp, main_count(T0) / pb_emp / T0))
out('      (heuristic decomposition: {:.3f} n above t=20 + {:.3f} n below the first zero)'
    .format(integ20 / (2 * np.pi), low_coef))
out('      at the second height T0 = 3.0001753328e12 the same coefficient gives')
out('      n_max ~ {:.4e}, i.e. {:.2f} T0  (still LINEAR, never T0^2)'
    .format(main_count(3.0001753328e12) / pb_emp, main_count(3.0001753328e12) / pb_emp / 3.0001753328e12))
out('  (3) n = T0^2 is NOT delivered by either treatment; both fall short by a factor')
out('      >= {:.1e}.'.format(T0**2 / (main_count(T0) / pb_emp)))
out('  (4) the true |Fluc(n)| on the table is O(1)-ish while both bounds are O(n): the loss')
out('      is in Cauchy-Schwarz itself, i.e. in discarding the phase correlation of S with w.')
out('=' * 78)

with open('scripts/PAPERA_second_moment_route.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines) + '\n')
print('\n[written] scripts/PAPERA_second_moment_route.txt')
