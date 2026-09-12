#!/usr/bin/env python3
"""
E26B (E26/A4-4, computation B): the truncation floor and the N-trend of d_N^2 at larger T.

PROVENANCE / PURPOSE
   Designed in docs/E26-A4-4-constructive-direction.md section 6(B): tabulate d_N^2(N,T) for
   T in {400, 2000, 8000} with T >> N, N <= 400, and report d_N^2 * log N.  Success criterion
   (L2 of that note): d_N^2 * log N must DECREASE monotonically in N and enter [C, 3C] with
   C = 2 + gamma - log 4pi = 0.046191417932.  At T = 400 the project measured the opposite
   (0.52 -> 3.45, rising) - see docs/A4-1-dN-fixed.md section 3.  This script tests whether the
   rise is caused by the T = 400 truncation floor or is a genuine failure of the criterion at
   these degrees.

   TWO CONVENTIONS ARE COMPUTED (this matters - see docs/E26A-result.md):
     convention A (literal Baez-Duarte / BCF definition, verified by direct integration in E26A):
         d_N^2 = inf_A (1/2pi) int |1 - zeta(1/2+it) A_N(1/2+it)|^2 dt/(1/4+t^2),
         A_N(s) = sum_{n<=N} a_n n^{-s}   ==>   K(m,n) = (mn)^{-1/2} g(log(n/m)).
     convention B (as actually implemented in scripts/NB3_dN_fourier_kernel.py, which omits the
         (mn)^{-1/2} weight):  K(m,n) = g(log(n/m)).
   Both are reported; A is the quantity the literature (BCF, arXiv:1211.5191 section 1) is about.

   KNOWN-ANSWER CHECK (mandatory): for every (N,T) the minimising coefficients a_n must follow
   the sign of the Moebius function mu(n) on the squarefree n <= N - reported both over all such
   n and restricted to n <= N/2 (docs/E26A-result.md section 4 explains why the restriction
   matters: cond(K) ~ 4e9 at N=160 leaves a null-space boundary layer near n ~ N).
   Also reported: I(V_N) for the explicit BCF polynomial V_N(s) = sum_{n<=N}(1 - log n/log N)
   mu(n) n^{-s}, the quantity BCF Thm 1 predicts to be ~ C/log N under RH.

   ZETA VALUES: zeta(1/2+it) = Z(t) exp(i theta(t)) via the Riemann-Siegel functions of mpmath
   (t >= 15), mpmath's zeta below.  Computed on the fly and cached OUTSIDE the repository
   (default /tmp/dn_e26b_cache) so that no existing project file is touched.  The T = 400,
   h = 0.05 grid is read from the project cache data/nb3_grid_H0.050_T400.npz when present.
   Grid step: h = 0.05 at T = 400 (project cache); h = 0.10 at T = 2000, 8000 (the step
   sensitivity of d_N^2 was checked at T = 400 by subsampling: h = 0.05 -> 0.0489309,
   h = 0.10 -> 0.0491299, h = 0.20 -> 0.0495331 at N = 160, i.e. 0.4% and 1.2%).

Inputs : data/nb3_grid_H0.050_T400.npz (optional cache; regenerated if absent)
Outputs: scripts/E26B_dN_larger_T_N.txt  (and a grid cache outside the repository)
"""
import os, time
import numpy as np
from mpmath import mp, mpf, mpc, zeta as mzeta, exp as mexp, siegelz, siegeltheta
from mpmath import pi as mpi, log as mlog, euler as meuler

mp.dps = 26
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CACHE = os.environ.get('E26B_CACHE', os.path.join('/tmp', 'dn_e26b_cache'))
OUT = os.path.join(ROOT, 'scripts', 'E26B_dN_larger_T_N.txt')
C_BURNOL = 2 + float(meuler) - float(mlog(4 * mpi))
NS = (20, 40, 80, 160, 240, 320, 400)

class Tee:
    def __init__(self, path):
        self.f = open(path, 'w')
    def __call__(self, msg):
        print(msg, flush=True)
        self.f.write(str(msg) + "\n"); self.f.flush()
say = Tee(OUT)

def zeta_half(t):
    """zeta(1/2 + i t): Riemann-Siegel above 15, mpmath's zeta below (as in NB3)."""
    if t < 15.0:
        z = mzeta(mpc(mpf('0.5'), mpf(t)))
    else:
        tm = mpf(t)
        z = mpf(siegelz(tm)) * mexp(mpc(0, 1) * siegeltheta(tm))
    return complex(z)

def _chunk_complex(tvals):
    tv = np.asarray(tvals, dtype=float)
    zc = np.empty(len(tv), dtype=complex); fi = np.empty(len(tv))
    for i, t in enumerate(tv):
        z = zeta_half(t)
        w = 1.0 / (0.25 + t * t)
        zc[i] = z * w
        fi[i] = (z.real * z.real + z.imag * z.imag) * w
    return zc, fi

def build_grid(T, H, say):
    os.makedirs(CACHE, exist_ok=True)
    cache = os.path.join(CACHE, 'grid_H%.3f_T%.0f.npz' % (H, T))
    ts = np.arange(0.0, T + H / 2, H)
    repo = os.path.join(ROOT, 'data', 'nb3_grid_H0.050_T400.npz')
    if T == 400.0 and abs(H - 0.05) < 1e-9 and os.path.exists(repo):
        c = np.load(repo)
        say("  [grid] T=%.0f h=%.3f: project cache data/nb3_grid_H0.050_T400.npz (%d pts)"
            % (T, H, len(c['ts'])))
        return c['ts'], c['zvals'], c['fvals']
    if os.path.exists(cache):
        c = np.load(cache)
        say("  [grid] T=%.0f h=%.3f: cache %s (%d pts)" % (T, H, cache, len(c['ts'])))
        return c['ts'], c['zvals'], c['fvals']
    say("  [grid] T=%.0f h=%.3f: computing %d zeta values ..." % (T, H, len(ts)))
    t0 = time.time()
    zc = np.empty(len(ts), dtype=complex); fi = np.empty(len(ts))
    nw = min(4, max(1, os.cpu_count() or 2))
    blocks = [(i * len(ts)) // nw for i in range(nw + 1)]
    parts = [(blocks[i], blocks[i + 1]) for i in range(nw) if blocks[i + 1] > blocks[i]]
    if len(parts) > 1 and len(ts) > 2000:
        from multiprocessing import Pool
        with Pool(len(parts)) as pool:
            res = pool.map(_chunk_complex, [ts[a:b] for a, b in parts])
        for (a, b), (z, f) in zip(parts, res):
            zc[a:b] = z; fi[a:b] = f
    else:
        zc, fi = _chunk_complex(ts)
    say("    done in %.1f s (%.4f s/point, %d workers)" % (time.time() - t0,
        (time.time() - t0) / len(ts), len(parts)))
    np.savez_compressed(cache, ts=ts, zvals=zc, fvals=fi)
    return ts, zc, fi

def g_interp(ts, fvals, XMAX=6.6, STEP=0.0025, say=None):
    XS = np.arange(0.0, XMAX, STEP)
    GS = np.empty(len(XS))
    block = max(1, int(40e6 // max(1, len(ts))))       # keep memory bounded
    for a in range(0, len(XS), block):
        b = min(len(XS), a + block)
        xb = XS[a:b][:, None]
        M = fvals[None, :] * np.cos(ts[None, :] * xb)
        GS[a:b] = np.trapz(M, ts, axis=1) / float(mpi)
    GS[0] = float(np.trapz(fvals, ts)) / float(mpi)
    def gI(x):
        r = np.interp(np.abs(np.asarray(x, float)), XS, GS)
        return r if r.ndim else float(r)
    return gI

def mu_table(N):
    mu = np.zeros(N + 1, dtype=int); mu[1] = 1
    for i in range(1, N + 1):
        for j in range(2 * i, N + 1, i): mu[j] -= mu[i]
    return mu

def solve(N, ts, fvals, zvals, gI, conv):
    nn = np.arange(1, N + 1); lgn = np.log(nn)
    L = np.empty(N)
    for n in range(1, N + 1):
        L[n - 1] = float(np.trapz((zvals * np.exp(-1j * ts * np.log(n))).real, ts)) / float(mpi)
    l = L / np.sqrt(nn)
    K = np.empty((N, N))
    for m in range(1, N + 1):
        K[m - 1] = gI(lgn - np.log(m))
    if conv == 'A':
        K = K / np.sqrt(np.outer(nn, nn))
    a = np.linalg.solve(K, l)
    d2 = 1.0 - float(l @ a)
    mu = mu_table(N)
    V = (1 - lgn / np.log(N)) * mu[1:].astype(float)
    IV = 1.0 - 2.0 * float(l @ V) + float(V @ K @ V)
    idx = [n for n in range(1, N + 1) if mu[n] != 0]
    agree = sum(1 for n in idx if np.sign(a[n - 1]) == mu[n] and abs(a[n - 1]) > 1e-12)
    half = [n for n in idx if n <= N // 2]
    agree2 = sum(1 for n in half if np.sign(a[n - 1]) == mu[n] and abs(a[n - 1]) > 1e-12)
    return d2, agree, len(idx), agree2, len(half), IV

def main():
    say("=" * 108)
    say("E26B: d_N^2(N,T) for larger T (success criterion L2: d_N^2*log N decreasing into [C,3C])")
    say("=" * 108)
    say("  Burnol constant C = 2 + gamma - log(4pi) = %.12f ; [C,3C] = [%.6f, %.6f]"
        % (C_BURNOL, C_BURNOL, 3 * C_BURNOL))
    grids = {}
    res = {}
    for T, H in ((400.0, 0.05), (2000.0, 0.10), (8000.0, 0.10)):
        ts, zv, fv = build_grid(T, H, say)
        grids[(T, H)] = (ts, zv, fv)
        if (T, H) == (400.0, 0.05):                       # free step check by subsampling
            grids[(400.0, 0.10)] = (ts[::2], zv[::2], fv[::2])
        res[(T, H)] = {}
    for (T, H), (ts, zv, fv) in list(grids.items()):
        say("")
        say("  T = %.0f   h = %.3f   points = %d   (t in [0, %.1f])" % (T, H, len(ts), ts[-1]))
        gI = g_interp(ts, fv, say=say)
        say("      %5s | %-40s | %-40s" % ("N", "convention A  ((mn)^-1/2 g; BCF)", "convention B  (g; NB3 as implemented)"))
        say("      %5s | %11s %11s %8s %9s | %11s %11s %8s %9s"
            % ("", "d_N^2", "d^2*logN", "mu all", "mu n<=N/2", "d_N^2", "d^2*logN", "mu all", "mu n<=N/2"))
        for N in NS:
            dA, aA, nA, aA2, nA2, IVA = solve(N, ts, fv, zv, gI, 'A')
            dB, aB, nB, aB2, nB2, IVB = solve(N, ts, fv, zv, gI, 'B')
            res.setdefault((T, H), {})[N] = (dA, IVA, dB, IVB)
            say("      %5d | %11.8f %11.6f %4d/%-3d %4d/%-4d | %11.8f %11.6f %4d/%-3d %4d/%-4d"
                % (N, dA, dA * np.log(N), aA, nA, aA2, nA2,
                   dB, dB * np.log(N), aB, nB, aB2, nB2))
            say("            I(V_N) A = %.8f (x logN = %.6f, /C = %.3f) | B = %.8f (x logN = %.6f)"
                % (IVA, IVA * np.log(N), IVA * np.log(N) / C_BURNOL, IVB, IVB * np.log(N)))
    say("")
    say("  T-DEPENDENCE AT FIXED N (convention A; the true d_N^2 uses T = infinity)")
    say("  %5s | %13s %13s %13s %13s | %12s %12s %9s"
        % ("N", "T=400 h=.05", "T=400 h=.10", "T=2000 h=.10", "T=8000 h=.10",
           "d2*logN(T8k)", "C/logN", "ratio"))
    for N in NS:
        v4a = res[(400.0, 0.05)][N][0]; v4b = res[(400.0, 0.10)][N][0]
        v2k = res[(2000.0, 0.10)][N][0]; v8k = res[(8000.0, 0.10)][N][0]
        say("  %5d | %13.8f %13.8f %13.8f %13.8f | %12.6f %12.6f %9.3f"
            % (N, v4a, v4b, v2k, v8k, v8k * np.log(N), C_BURNOL / np.log(N),
               v8k * np.log(N) / C_BURNOL))
    say("  %5s | %13s %13s %13s %13s | %12s %12s %9s"
        % ("N", "I(V)T=400", "I(V)T=400h.1", "I(V)T=2000", "I(V)T=8000", "I*logN(T8k)", "C/logN", "ratio"))
    for N in NS:
        i4a = res[(400.0, 0.05)][N][1]; i4b = res[(400.0, 0.10)][N][1]
        i2k = res[(2000.0, 0.10)][N][1]; i8k = res[(8000.0, 0.10)][N][1]
        say("  %5d | %13.8f %13.8f %13.8f %13.8f | %12.6f %12.6f %9.3f"
            % (N, i4a, i4b, i2k, i8k, i8k * np.log(N), C_BURNOL / np.log(N),
               i8k * np.log(N) / C_BURNOL))
    say("")
    say("=" * 108)
    say("READ-OFF (generated from the numbers above)")
    say("=" * 108)
    say("  * the mu-agreement columns are the known-answer check; they must stay near 100%.")
    say("  * criterion L2 is met only if d_N^2*log N falls monotonically into [%.4f, %.4f]."
        % (C_BURNOL, 3 * C_BURNOL))
    say("  * convention A is the literal BCF functional (cross-checked by direct integration in")
    say("    scripts/E26A_dN_vs_literature_polynomial.py); convention B is NB3's kernel, which")
    say("    omits the (mn)^-1/2 weight and does not match the defining integral.")
    say("  * I(V_N) lines (printed above each row) give the explicit BCF polynomial's own value;")
    say("    BCF Thm 1 predicts I(V_N) ~ C/log N under RH + the moment hypothesis (引用).")
    say("  * conclusion on L2: report honestly whether d_N^2*log N moves INTO [%.4f, %.4f] as T grows."
        % (C_BURNOL, 3 * C_BURNOL))
    say("")
    say("Output written to %s" % OUT)

if __name__ == '__main__':
    main()
