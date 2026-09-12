#!/usr/bin/env python3
"""
AR4: Refined saddle analysis of the binomial route

  (1) Z_j is evaluated in the numerically safe polar form
          Z_j = 2 sum_{gamma} exp(-j log r) cos(j phi),   r = sqrt(1/4+gamma^2), phi = atan(2 gamma)
      (the complex form rho^{-j} overflows in float64 for j >~ 70).
      Only the first 40000 zeros are used: for odd j the real-part tail of rho^{-j} is
      O(gamma^{-(j+1)}), so this is amply sufficient for j >= 3.  Z_1, Z_2 come from the
      arithmetic formula (validated in AR1).
  (2) the smooth envelope of |Z_j| (rolling median) defines the saddle, removing the
      pseudo-random factor |cos(j phi_1)| that biases a naive argmax.
  (3) the decay radius is fitted both from r_eff(j) = |Z_j|^{-1/j} and from a regression of
      log envelope against j; the saddle is compared with the model j = n/(1+r).

Inputs : data/zeros_odlyzko_2M.npy (first 40000 zeros)
Outputs: scripts/AR4_saddle_refined.txt
"""
import os, time
import numpy as np
import mpmath as mp

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
ZP = os.path.join(ROOT, 'data', 'zeros_odlyzko_2M.npy')
OUT = []


def emit(s=''):
    print(s)
    OUT.append(str(s))


T0 = time.time()
gam = np.sort(np.load(ZP).astype(np.float64).ravel())
gam = gam[gam > 0.5][:40000]
R1 = float(gam[0])
emit("using first %d zeros, gamma_1 = %.10f   |rho_1| = %.10f" % (gam.size, R1, R1))

mp.mp.dps = 50
Z1 = 1 + mp.euler / 2 - mp.log(4 * mp.pi) / 2
eta1 = mp.euler ** 2 + 2 * mp.stieltjes(1)
Z2 = 1 - (1 - mp.mpf(2) ** (-2)) * mp.zeta(2) + eta1

JMAX = 1200
logr = 0.5 * np.log(0.25 + gam ** 2)
phi = np.arctan(2.0 * gam)
Z = {1: float(Z1), 2: float(Z2)}
for j in range(3, JMAX + 1):
    Z[j] = 2.0 * float(np.sum(np.exp(-j * logr) * np.cos(j * phi)))

emit()
emit("effective decay radius  r_eff(j) = |Z_j|^{-1/j}   (should tend to |rho_1| = %.4f)" % R1)
emit("%6s %-24s %-14s" % ("j", "Z_j", "r_eff(j)"))
for j in list(range(1, 21)) + [25, 30, 40, 50, 60, 80, 100, 150, 200]:
    reff = abs(Z[j]) ** (-1.0 / j)
    emit("%6d %-24s %-14.6f" % (j, "%.12e" % Z[j], reff))

Js = np.array([j for j in range(3, JMAX + 1)])
absZ = np.array([abs(Z[j]) for j in Js])
env = {}
for i, j in enumerate(Js):
    lo, hi = max(0, i - 4), min(len(Js), i + 5)
    env[j] = float(np.median(absZ[lo:hi]))

# regression of log envelope against j on the geometric region
sel = [j for j in range(20, 161)]
x = np.array(sel, dtype=float)
y = np.array([np.log(env[j]) for j in sel])
A = np.vstack([x, np.ones_like(x)]).T
slope, icpt = np.linalg.lstsq(A, y, rcond=None)[0]
r_reg = float(np.exp(-slope))
emit()
emit("regression of log(median|Z_j|) on j, j in [20,160]:  |Z_j| ~ C * r^{-j} with")
emit("    r_fit = %.5f     (|rho_1| = %.5f ; 3 (trivial-zero scale) = 3.00000)" % (r_reg, R1))


def vlog(n, j):
    return float(mp.log(mp.binomial(n, j)) + mp.log(mp.mpf(repr(env[j]))))


def j_env(n):
    """discrete argmax of log C(n,j) + log envelope, then one parabolic refinement"""
    best, bj = -1e18, 0
    for j in range(3, min(n, JMAX) + 1):
        v = vlog(n, j)
        if v > best:
            best, bj = v, j
    if 3 < bj < min(n, JMAX):
        a, b, c = vlog(n, bj - 1), vlog(n, bj), vlog(n, bj + 1)
        den = a - 2 * b + c
        if den != 0:
            return bj + 0.5 * (a - c) / den
    return float(bj)


def j_model(n, r):
    """solve digamma(n-j+1)-digamma(j+1) = log r  (exact saddle condition d/dj[log C(n,j) - j log r]=0)"""
    f = lambda j: mp.digamma(n - j + 1) - mp.digamma(j + 1) - mp.log(r)
    a, bb = mp.mpf(2), mp.mpf(n) / 2
    fa, fb = f(a), f(bb)
    if fa * fb > 0:
        return float('nan')
    for _ in range(200):
        m = (a + bb) / 2
        fm = f(m)
        if fa * fm <= 0:
            bb, fb = m, fm
        else:
            a, fa = m, fm
    return float((a + bb) / 2)


emit()
emit("=" * 110)
emit("TASK 3 (refined)   saddle of the binomial summand")
emit("=" * 110)
emit("%6s %8s %10s %12s %12s %12s %12s" %
     ("n", "j_peak", "j_env", "n/j_peak", "n/j_env", "n/(1+r1)", "n/(1+r_fit)"))
NS = [60, 80, 100, 120, 150, 200, 250, 300, 350, 400]
peaks = []
for n in NS:
    T = {j: Z[j] for j in range(1, min(n, JMAX) + 1)}
    jpk = max(T, key=lambda j: abs(T[j]))
    je = j_env(n)
    peaks.append((n, je))
    emit("%6d %8d %10.1f %12.4f %12.4f %12.4f %12.4f" %
         (n, jpk, je, n / jpk, n / je, n / (1 + R1), n / (1 + r_reg)))
emit()
emit("exact saddle condition  digamma(n-j+1)-digamma(j+1) = log r :")
emit("%6s %12s %12s %12s %12s" % ("n", "j_model(r1)", "j_model(r_fit)", "j_env(observed)", "j_model/n"))
for n in [100, 200, 300, 400, 600, 800, 1000]:
    jm1 = j_model(n, mp.mpf(repr(R1)))
    jm2 = j_model(n, mp.mpf(repr(r_reg)))
    emit("%6d %12.3f %12.3f %12s %12.5f" %
         (n, jm1, jm2, "%.2f" % j_env(n), jm1 / n))
sel2 = [(n, j) for (n, j) in peaks if n >= 200]
nn = np.array([p[0] for p in sel2], float)
jj = np.array([p[1] for p in sel2], float)
c_ls = float(np.dot(nn, jj) / np.dot(nn, nn))          # through origin: j = c n
emit()
emit("least squares through the origin, n>=200:   j_saddle = n / %.3f   (i.e. j_saddle = %.5f n)"
     % (1 / c_ls, c_ls))
emit("model comparison: 1/(1+gamma_1) = %.5f   1/(1+r_fit) = %.5f" % (1 / (1 + R1), 1 / (1 + r_reg)))

emit()
emit("dominant range (|T_j| >= max/10), cancellation, and comparison with the direct zero sum")
emit("   lambda_ref = 4 sum sin^2(n theta_gamma) over the 2M table + analytic tail n^2*coef")
GF = np.sort(np.load(ZP).astype(np.float64).ravel())
GF = GF[GF > 0.5]
THF = np.arctan(1.0 / (2.0 * GF))
COEF = (1 / (2 * np.pi)) * (np.log(GF[-1] / (2 * np.pi)) + 1) / GF[-1]


def lam_ref(n):
    return float(4.0 * np.sum(np.sin(n * THF) ** 2) + n * n * COEF)


emit("%6s %7s %7s %14s %14s %12s %12s %9s %10s" %
     ("n", "j_lo", "j_hi", "max|T_j|", "sum|T_j|", "lambda_binom", "lambda_ref", "relerr", "D2"))
budget = []
for n in [100, 200, 300, 400, 500, 600, 800, 1000]:
    T = {j: (-1) ** (j + 1) * mp.binomial(n, j) * mp.mpf(repr(Z[j]))
         for j in range(1, min(n, JMAX) + 1)}
    aT = {j: abs(v) for j, v in T.items()}
    mx = max(aT.values())
    jlo = min(j for j in aT if aT[j] >= mx / 10)
    jhi = max(j for j in aT if aT[j] >= mx / 10)
    S = mp.fsum(list(aT.values()))
    lam = mp.fsum(list(T.values()))
    lref = lam_ref(n)
    d2 = float(mp.log10(S / abs(mp.mpf(repr(lref)))))
    jsm = j_env(n)
    budget.append((n, jsm, 0.6690 * jsm, d2, 0.6690 * jsm + d2))
    emit("%6d %7d %7d %14s %14s %12s %12.4f %9.2e %10.3f" %
         (n, jlo, jhi, mp.nstr(mx, 6), mp.nstr(S, 6), mp.nstr(lam, 8), lref,
          abs(lam - mp.mpf(repr(lref))) / lref, d2))
emit("   NOTE: sum|T_j| is reliable (no cancellation) but the final sum needs D2 digits.")
emit("   With float64 Z_j (16 digits) the row n=600 already shows relerr ~ 0.49 and n>=800 is nonsense;")
emit("   this is the precision wall of the binomial route, observed, not assumed.")

emit()
emit("precision budget (decimal digits) required by the pure-arithmetic route")
emit("   D1 = 0.6690 * j_saddle  (cancellation inside Z_j, geometric ratio 3/14)")
emit("   D2 = log10(sum|T_j| / |lambda_n|)  (cancellation of the transform)")
emit("%8s %8s %8s %8s %8s %10s" % ("n", "j_saddle", "D1", "D2", "total", "total/n"))
for n in [100, 200, 300, 400, 500, 600, 800, 1000, 5000, 10000]:
    js = n / (1 + r_reg)
    d1 = 0.6690 * js
    lam_est = mp.mpf('0.30') * n * mp.log(n)
    sT = mp.exp(mp.log(mp.binomial(n, int(round(js)))) - js * mp.log(mp.mpf(repr(r_reg)))) * 30
    d2 = float(mp.log10(sT / lam_est))
    emit("%8d %8.1f %8.1f %8.1f %8.1f %10.4f" % (n, js, d1, d2, d1 + d2, (d1 + d2) / n))
for (n, jsm, d1, d2, tt) in budget:
    emit("   measured n=%-4d j_saddle=%-5.1f  D1+D2 = %.1f digits" % (n, jsm, tt))

with open(os.path.join(HERE, 'AR4_saddle_refined.txt'), 'w') as f:
    f.write("\n".join(OUT) + "\n")
print("\n[AR4 done, %.1fs]" % (time.time() - T0))
