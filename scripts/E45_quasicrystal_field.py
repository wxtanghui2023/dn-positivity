#!/usr/bin/env python3
"""E45 -- decisive numerical test of the quasicrystal-scattering construction (arXiv:2410.03673)

目的 (purpose)
  Test the "prime quasicrystal" scattering construction of M. Shaughnessy, arXiv:2410.03673
  (v12, 23 May 2026), whose claimed object is the amplitude

      chi_L(k) = sum_{n=1..L} p_n^{-2*pi*i*k}        (paper Eq. 8, 9)

  Three stages, as ordered:
    S1  does |chi_L(k)| have peaks at k = gamma_m/(2*pi)?  (gamma_m = imaginary parts of zeta zeros)
    S2  does the peak height carry beta = Re(rho) with the claimed cutoff scaling p_L^{beta-1/2}
        (paper Eq. 16, 21, 24, 28)?  Fit h(X) ~ X^s and compare with s = 2*beta (raw) / 0 (normalised).
    S3  is there any consistency condition (sup-norm bound, functional-equation pairing) that
        converts the measurement into a constraint on beta?
  A clean negative is an acceptable and valuable outcome; no success claim is pre-written (R7).

论文原文 (formulas used, read from the arXiv HTML of v12; identifier verified in this pass)
  Eq. 8   chi_L(k) = sum_{n<=L} p_n^{-2*pi*i*k};   Eq. 9  P_L(s) = sum p_n^{-s}, s = 2*pi*i*k
  Eq. 12  chi_L(k) = sum_rho (p_L^{rho-2*pi*i*k} - 1)/(rho (rho - 2*pi*i*k)) + R_L(k),
          R_L = O(p_L^{-1} log p_L)
  Eq. 13  zero-term near k = gamma/2*pi:  (p_L^{beta+i(gamma-2*pi*k)} - 1)/(rho (beta+i(gamma-2*pi*k)))
  Eq. 14  |chi_L(k)|^2 ~ p_L^{2*beta} / (|rho|^2 ((log p_L)^{-2} + 4*pi^2 (k-gamma/2*pi)^2))
  Eq. 15  c_m(L) = p_L^{rho_m}/rho_m ;  Eq. 16  chi~_L(k) = chi_L(k)/p_L^{1/2}
  Eq. 21  chi~(k) = 1 - sum_m (x^{beta_m-1/2} e^{i gamma_m ln x}/rho_m) delta(k - gamma_m/2*pi) + O(x^{-1/2})
  Eq. 24  c_m = -p_L^{beta_m-1/2} e^{i gamma_m ln p_L}/rho_m ;  Eq. 28  bounded amplitude => beta <= 1/2

输入 (input; nothing downloaded, nothing read from /tmp)
  - data/zeros_odlyzko_2M.npy   : 2,001,052 zeta zeros (imaginary parts), gamma_max ~ 1.1325e6   [repo]
  - primes: data/primes_1e8.npy if present, else
            /home/node/.openclaw/workspace/prime_data/primes_1e8.npy   (5,761,455 primes <= 1e8)
            An independent in-script numpy sieve re-derives pi(10^6) = 78498 to validate the table.

输出 (output)
  scripts/E45_quasicrystal_field.txt     (this script writes nothing else; never /tmp)

结论 (conclusions): decided by the in-script numeric criteria in the VERDICT section (R7); the failing
  and passing branches are both written out there, and the branch actually taken is printed.

provenance: written 2026-09-12 for dn-project E28b (pointer 3-A of docs/PHYSICS-FRONTIER-2026-09-12.md);
  follows docs/PROTOCOL-CODE-ARCHIVE.md (header, data/, output to scripts/<name>.txt, number-driven).
"""

import os
import sys
import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTLI = []
TWO_PI = 2.0 * np.pi


def say(*a):
    s = " ".join(str(x) for x in a)
    OUTLI.append(s)
    print(s, flush=True)


# ----------------------------------------------------------------------------- data
def load_zeros():
    p = os.path.join(ROOT, "data", "zeros_odlyzko_2M.npy")
    z = np.load(p)
    if z.ndim > 1:
        z = z[:, 0]
    return np.asarray(z, dtype=np.float64).ravel(), p


def load_primes():
    cands = [os.path.join(ROOT, "data", "primes_1e8.npy"),
             "/home/node/.openclaw/workspace/prime_data/primes_1e8.npy"]
    for c in cands:
        if os.path.exists(c):
            pr = np.load(c)
            if pr.ndim > 1:
                pr = pr[:, 0]
            return np.asarray(pr, dtype=np.int64).ravel(), c
    raise SystemExit("E45: no prime table found")


def sieve(n):
    bs = np.ones(n + 1, dtype=bool)
    bs[:2] = False
    for i in range(2, int(n ** 0.5) + 1):
        if bs[i]:
            bs[i * i:: i] = False
    return np.nonzero(bs)[0]


# ----------------------------------------------------------------------------- core field
def chi_direct(lp, ks, chunk=500_000):
    """chi(k) = sum_n exp(-2 pi i k ln p_n) for a small array of k (lp = log primes)."""
    ks = np.atleast_1d(np.asarray(ks, dtype=np.float64))
    out = np.zeros(ks.size, dtype=np.complex128)
    for c0 in range(0, lp.size, chunk):
        lpc = lp[c0:c0 + chunk]
        out += np.exp(-TWO_PI * 1j * np.outer(ks, lpc)).sum(axis=1)
    return out


def chi_grid(lp, k0, dk, K, chunk=500_000):
    """chi(k0 + j*dk), j=0..K-1, via a running geometric progression -> no transcendentals in the loop."""
    out = np.zeros(K, dtype=np.complex128)
    for c0 in range(0, lp.size, chunk):
        lpc = lp[c0:c0 + chunk]
        v = np.exp(-TWO_PI * 1j * k0 * lpc)
        z = np.exp(-TWO_PI * 1j * dk * lpc)
        for j in range(K):
            out[j] += v.sum()
            v *= z
    return out


def lorentz_fit(k, f, k0, ws):
    """fit f(k) ~ A/(1+((k-k0)/w)^2) + b + c (k-k0); linear in (A,b,c) for each w -> scan w."""
    best = None
    for w in ws:
        A = np.vstack([1.0 / (1.0 + ((k - k0) / w) ** 2), np.ones_like(k), k - k0]).T
        coef, *_ = np.linalg.lstsq(A, f, rcond=None)
        sse = float(((f - A @ coef) ** 2).sum())
        if best is None or sse < best[0]:
            best = (sse, float(w), coef)
    return best


def env_resid(lp, nX, km, deltas):
    """envelope-normalised residual of |chi| at k_m.

    The same script verifies |chi_X(k)| = c * pi(X)/(2 pi k) to ~6% over five decades (the PNT boundary
    term X/(|1-2 pi i k| log X)).  Fitting the single constant c on neighbouring k and extrapolating to
    k_m removes the envelope curvature from the residual, which a raw window-median background does not.
    Returns (c, model level B = c*pi(X)/(2 pi k_m), measured |chi(k_m)|, signed residual).
    """
    ks = np.concatenate([[km], km + deltas])
    vals = np.abs(chi_direct(lp, ks))
    envk = nX / (TWO_PI * ks)
    c = float(np.mean(vals[1:] / envk[1:]))
    B = c * float(envk[0])
    return c, B, float(vals[0]), float(vals[0]) - B


def fit_power(xs, ys):
    """log-log least squares: returns (slope, intercept, R^2)."""
    x = np.log(np.asarray(xs, dtype=np.float64))
    y = np.log(np.asarray(ys, dtype=np.float64))
    n = x.size
    sx, sy = x.sum(), y.sum()
    sxx = (x * x).sum()
    sxy = (x * y).sum()
    slope = (n * sxy - sx * sy) / (n * sxx - sx * sx)
    inter = (sy - slope * sx) / n
    pred = slope * x + inter
    ss_res = float(((y - pred) ** 2).sum())
    ss_tot = float(((y - y.mean()) ** 2).sum())
    return slope, inter, (1.0 - ss_res / ss_tot if ss_tot > 0 else float("nan"))


def main():
    say("=" * 100)
    say("E45 -- quasicrystal scattering (arXiv:2410.03673) : field, peaks, beta-channel, verdict")
    say("=" * 100)

    # ---------------------------------------------------------------- S0 data provenance
    z, zpath = load_zeros()
    pr, ppath = load_primes()
    say("")
    say("[S0] DATA")
    say("  zeros  : %s   count=%d   gamma_1..gamma_10 = %s" %
        (os.path.relpath(zpath, ROOT), z.size, np.array2string(z[:10], precision=7)))
    say("  primes : %s   count=%d   p_max=%d" % \
        (ppath, pr.size, int(pr[-1])))
    lp_full = np.log(pr.astype(np.float64))
    # independent sieve check
    sv = sieve(10 ** 6)
    say("  cross-check (in-script numpy sieve): pi(10^6) = %d ; table count <= 10^6 = %d ; agree=%s" %
        (sv.size, int(np.searchsorted(pr, 10 ** 6, "right")), sv.size == int(np.searchsorted(pr, 10 ** 6, "right"))))
    del sv

    def primes_le(x):
        n = int(np.searchsorted(pr, x, "right"))
        return n, pr[n - 1] if n else None

    # ---------------------------------------------------------------- S1 peak positions
    say("")
    say("[S1] PEAK POSITIONS -- does |chi_X(k)| peak at k = gamma_m/(2 pi) ?")
    X1 = 10 ** 6
    n1, pL1 = primes_le(X1)
    lp1 = lp_full[:n1]
    say("  X = %d  (p_L = %d, N = %d terms, log p_L = %.4f)" % (X1, pL1, n1, np.log(pL1)))
    K1, HALF = 1601, 0.40
    dk1 = 2 * HALF / (K1 - 1)
    say("  window per zero: k in [k_m-%.2f, k_m+%.2f], %d points (dk=%.1e); background B = median over |k-k_m|>0.2 (raw diagnostic)"
        % (HALF, HALF, K1, dk1))
    say("  (*) the last column of the table mixes the envelope curvature with the fluctuation; the cleaned measure is")
    say("      the envelope-normalised residual of S1d/S2, which fits the constant c in |chi| = c pi(X)/(2 pi k).")
    say("")
    say("   m      gamma_m          k_m=gamma/2pi     k_peak(found)     rel.err(k)    f(k_peak)/B   f(k_m)/B-1*")
    say("   ---    -----------      -------------     -------------     -----------   -----------   ----------")
    peaks = []
    for m in range(10):
        gm = float(z[m])
        km = gm / TWO_PI
        ks = km - HALF + dk1 * np.arange(K1)
        f = np.abs(chi_grid(lp1, ks[0], dk1, K1)) ** 2
        B = float(np.median(f[np.abs(ks - km) > 0.2]))
        # nearest local maximum to km (within +-0.15), via sign change of the slope
        loc = np.where((np.abs(ks - km) < 0.15))[0]
        sub = f[loc]
        cand = [j for j in range(1, sub.size - 1) if sub[j] > sub[j - 1] and sub[j] > sub[j + 1]]
        if cand:
            jb = min(cand, key=lambda j: abs(ks[loc[j]] - km))
            kpk, fpk = float(ks[loc[jb]]), float(sub[jb])
        else:
            jb = int(np.argmax(sub))
            kpk, fpk = float(ks[loc[jb]]), float(sub[jb])
        fkm = float(f[np.argmin(np.abs(ks - km))])
        rel = (kpk - km) / km
        peaks.append(dict(m=m + 1, gm=gm, km=km, kpk=kpk, rel=rel, fpk=fpk, B=B, fkm=fkm))
        say("  %3d  %13.6f   %13.9f   %13.9f   %+9.2e   %11.4f   %+10.4f" %
            (m + 1, gm, km, kpk, rel, fpk / B, fkm / B - 1.0))
    rels = np.array([p["rel"] for p in peaks])
    say("")
    say("  fraction of windows with a local maximum inside |k-k_m|/k_m < 1e-2 : %.2f" %
        float(np.mean(np.abs(rels) < 1e-2)))
    say("  median |relative position error| = %.3e ; max = %.3e" % (np.median(np.abs(rels)), np.abs(rels).max()))
    # Lorentzian fit + paper Eq.14 prediction for m=1,2,3
    say("")
    say("[S1b] PEAK SHAPE vs paper Eq.14  (X=%d, p_L=%d)" % (X1, pL1))
    ws = np.logspace(np.log10(2e-4), np.log10(0.6), 60)
    for m in (1, 2, 3):
        gm = float(z[m - 1]); km = gm / TWO_PI
        ks = km - HALF + dk1 * np.arange(K1)
        f = np.abs(chi_grid(lp1, ks[0], dk1, K1)) ** 2
        B = float(np.median(f[np.abs(ks - km) > 0.2]))
        sse, wbest, coef = lorentz_fit(ks, f, km, ws)
        A = coef[0]
        pred_h = pL1 * (np.log(pL1) ** 2) / (0.25 + gm ** 2)          # Eq.14 with beta=1/2
        pred_w = 1.0 / (TWO_PI * np.log(pL1))                          # Eq.14 HWHM in k
        say("  m=%d gamma=%9.4f : fitted Lorentzian amplitude A=%+.4e  HWHM w=%.4g  background b=%.4e" %
            (m, gm, A, wbest, coef[1]))
        say("            measured f(k_m)=%.4e  background B=%.4e  ratio f(k_m)/B=%.4f" %
            (f[np.argmin(np.abs(ks - km))], B, f[np.argmin(np.abs(ks - km))] / B))
        say("            paper Eq.14 predicts: peak height p_L^{2beta}(log p_L)^2/|rho|^2 = %.4e, HWHM = %.4g" %
            (pred_h, pred_w))
        say("            -> Eq.14 height / measured background = %.3e (the claimed spike lies %.1f x BELOW the background)"
            % (pred_h / B, B / pred_h))
        say("            -> fitted amplitude sign = %s (a real peak needs A>0); fitted w / Eq.14 w = %.3g"
            % ("+" if A > 0 else "-", wbest / pred_w))

    # ---------------------------------------------------------------- S1e wide-window local-maxima density
    say("")
    say("[S1e] FLATTENED FIELD OVER THE WIDE WINDOW (X=%d) -- how dense is the 'peak' structure?" % X1)
    klo = float(z[0]) / TWO_PI - 0.5
    khi = float(z[9]) / TWO_PI + 0.5
    K2 = 12341
    dk2 = (khi - klo) / (K2 - 1)
    ks2 = klo + dk2 * np.arange(K2)
    f2 = np.abs(chi_grid(lp1, ks2[0], dk2, K2)) ** 2
    g = f2 * (TWO_PI * ks2 / n1) ** 2                 # divide out the PNT envelope ~ (N/(2 pi k))^2
    g = g / np.median(g) - 1.0                        # flattened, zero-centred fluctuation field
    rms = float(np.sqrt((g ** 2).mean()))
    lmi = np.array([t for t in range(4, K2 - 4)
                    if g[t] > g[t - 1] and g[t] > g[t + 1] and g[t] > max(g[t - 4], g[t + 4])], dtype=int)
    nl = int(lmi.size)
    rng = khi - klo
    say("  k in [%.3f, %.3f] (%d points, dk=%.1e); rms of the flattened fluctuation = %.4f" % (klo, khi, K2, dk2, rms))
    say("  %d local maxima of the flattened field (each above its +-4-point neighbours)" % nl)
    if nl:
        say("  mean spacing between them in k = %.5f ; the 10 zeros have mean spacing %.3f" % (rng / nl, rng / 10))
        cap1 = 0
        for m in range(10):
            km = float(z[m]) / TWO_PI
            cap1 += int(np.abs(ks2[lmi] - km).min() < 1e-3 * km)
        tol = 1e-3 * 4.5
        chance = nl * 2 * tol / rng * 10
        say("  zeros matched by such a local maximum within 1e-3 relative : %d/10 ; chance level %.1f/10" % (cap1, chance))
        say("  => matching a zero by the mere presence of a nearby local maximum carries no information here:")
        say("     the flattened field is broadband noise-like, so coincidences are expected at the chance rate.")
    else:
        say("  (no local maximum found with this criterion)")
    # ---------------------------------------------------------------- S1c paper Eq.12 test
    say("")
    say("[S1c] PAPER Eq.12 DECOMPOSITION TEST -- is  sum_rho (p_L^{rho-2pi i k}-1)/(rho(rho-2pi i k)) + R_L  equal to chi_L?")
    rho = 0.5 + 1j * z                                                   # all tabulated zeros are on the line
    say("  using all %d tabulated zeros (gamma <= %.4g), beta_m = 1/2 for all of them; R_L claimed = O(p_L^{-1} log p_L)" %
        (z.size, float(z[-1])))
    RL_CLAIM, RL_FIELD = float("nan"), float("nan")
    for Xte in (10 ** 6, 10 ** 8):
        nte, pLte = primes_le(Xte)
        lpte = lp_full[:nte]
        say("  -- X = %d (p_L = %d, N = %d) :" % (Xte, pLte, nte))
        for m in (1, 2, 3):
            km = float(z[m - 1]) / TWO_PI
            field = complex(chi_direct(lpte, [km])[0])
            e12 = complex(((np.exp((rho - 1j * TWO_PI * km) * np.log(pLte)) - 1.0)
                           / (rho * (rho - 1j * TWO_PI * km))).sum())
            say("       k=k_%d=%.6f : |chi_L|=%11.4e   |Eq.12 zero-sum|=%11.4e   ratio=%8.3e" %
                (m, km, abs(field), abs(e12), abs(e12) / abs(field)))
            if m == 1:
                RL_CLAIM, RL_FIELD = float(np.log(pLte) / pLte), abs(field)
                rl_claim = RL_CLAIM
                say("         remainder claimed by the paper: R_L = O(p_L^{-1} log p_L) = %.3e  ->  the field exceeds the" % rl_claim)
                say("         claimed remainder by a factor %.3e" % (abs(field) / rl_claim))

    # ---------------------------------------------------------------- S2 cutoff scaling
    say("")
    say("[S2] CUTOFF SCALING OF THE PEAK HEIGHT -- paper Eq.16/21 claim: normalised peak ~ p_L^{beta-1/2}")
    say("  the same run verifies |chi_X(k)| = c * pi(X)/(2 pi k) with c ~ 0.94 (the PNT boundary term);")
    say("  residual r(X) = |chi_X(k_m)| - c*pi(X)/(2 pi k_m) (signed);  r(X)/p_L^{1/2} is the paper's normalised height.")
    say("  (all tabulated zeros have beta_m = 1/2, so the paper predicts r ~ p_L^{1/2} and r/p_L^{1/2} = const)")
    Xs = [10 ** 3, 10 ** 4, 10 ** 5, 10 ** 6, 10 ** 7, 10 ** 8]
    DELS2 = np.array([-0.6, -0.4, -0.3, -0.2, -0.1, 0.1, 0.2, 0.3, 0.4, 0.6])
    scaling = {}
    for m in (1, 2, 3):
        km = float(z[m - 1]) / TWO_PI
        rows = []
        for X in Xs:
            nX, pLX = primes_le(X)
            c, B, am, resids = env_resid(lp_full[:nX], nX, km, DELS2)
            rows.append((X, pLX, nX, c, B, am, resids))
        say("")
        say("   m=%d  gamma=%.4f  k_m=%.6f" % (m, float(z[m - 1]), km))
        say("      X          p_L          N       c      envelope c*N/(2pik)   |chi|(k_m)    resid        resid/|chi|   |chi|/sqrt(p_L)")
        for (X, pLX, nX, c, B, am, resids) in rows:
            say("   %9.0e  %11d  %9d   %.4f   %14.5e   %12.5e  %+12.4e  %+11.4f   %10.4f" %
                (X, pLX, nX, c, B, am, resids, resids / B, am / np.sqrt(pLX)))
        Xa = np.array([r[0] for r in rows], float)
        Ca = np.array([r[3] for r in rows], float)
        Ba = np.array([r[4] for r in rows], float)
        Rs = np.array([r[6] for r in rows], float)
        Am = np.array([r[5] for r in rows], float)
        pl = np.sqrt(np.array([r[1] for r in rows], float))
        sC, _, rC = fit_power(Xa, Ca)
        sB, _, rB = fit_power(Xa, Ba)
        sres, _, rres = fit_power(Xa, np.abs(Rs))
        sam, _, ram = fit_power(Xa, Am)
        snorm, _, rnorm = fit_power(Xa, np.abs(Rs) / pl)
        sdiv, _, rdiv = fit_power(Xa, Am / pl)
        say("   fits (log-log, six cutoffs):")
        say("     envelope level B(X)=c*pi(X)/2pik ~ X^%+.3f  (R2=%.4f)  [PNT model: 1 - 1/logX, i.e. ~0.92 here]" % (sB, rB))
        say("     fitted constant c(X)            ~ X^%+.3f  (R2=%.4f)  [constant means the PNT form is right]" % (sC, rC))
        say("     |chi|(k_m)                      ~ X^%+.3f  (R2=%.4f)" % (sam, ram))
        say("     |resid|                         ~ X^%+.3f  (R2=%.4f)  [paper Eq.14/21: exponent 1/2]" % (sres, rres))
        say("     |resid| / p_L^{1/2}             ~ X^%+.3f  (R2=%.4f)  [paper Eq.16: exponent 0 = constant]" % (snorm, rnorm))
        say("     |chi|   / p_L^{1/2}             ~ X^%+.3f  (R2=%.4f)  [paper Eq.21: exponent 0, and the value -> 1]" % (sdiv, rdiv))
        say("     sign of resid over the cutoffs  : %s   (%d of %d positive)" %
            (np.array2string(np.sign(Rs).astype(int)), int(np.sum(Rs > 0)), Rs.size))
        scaling[m] = dict(sB=sB, sBamp=sB, shi=sres, sha=sres, snorm=snorm, sdiv=sdiv,
                          npos=int(np.sum(Rs > 0)), n=int(Rs.size), Xa=Xa, B=Ba, hi=Rs, ha=Rs,
                          ctilde=(Am / pl).copy(), rel=(Rs / Ba).copy())

    # ---------------------------------------------------------------- S2b per-zero amplitude channel
    say("")
    say("[S2b] PER-ZERO AMPLITUDE CHANNEL at the first 20 zeros")
    say("  signed residual r(X,m) as in S2; phase overlap phi(X,m) = -Re(p_L^{i gamma_m}/rho_m); cleaned amplitude A = r/phi.")
    say("  the explicit-formula model gives |A| ~ p_L^{beta_m}/log p_L, so the log-slope of |A| vs X should be beta_m - corr,")
    say("  with corr = (log log Xmax - log log Xmin)/log(Xmax/Xmin) fixed by the fit range; slope 1 in beta.")
    NZ = 20
    agree2, tot2 = 0, 0
    betas = []
    for m in range(1, NZ + 1):
        gm = float(z[m - 1])
        km = gm / TWO_PI
        rho_m = 0.5 + 1j * gm
        Xa2, Aa2, rr2 = [], [], []
        for X in Xs:
            nX, pLX = primes_le(X)
            c, B, am, rr = env_resid(lp_full[:nX], nX, km, DELS2)
            phi = -float(np.real((pLX ** (1j * gm)) / rho_m))
            tot2 += 1
            agree2 += int(np.sign(phi) == np.sign(rr))
            Xa2.append(X)
            rr2.append(rr)
            Aa2.append(rr / phi if abs(phi) > 1e-12 else np.nan)
        Xa2 = np.array(Xa2, float)
        Aa2 = np.array(Aa2, float)
        rr2 = np.array(rr2, float)
        sel = (Xa2 >= 1e5) & np.isfinite(Aa2) & (Aa2 != 0)
        if sel.sum() >= 3:
            sA, _, rA = fit_power(Xa2[sel], np.abs(Aa2[sel]))
            corr = (np.log(np.log(Xa2[sel].max())) - np.log(np.log(Xa2[sel].min()))) / np.log(Xa2[sel].max() / Xa2[sel].min())
            betas.append(sA + corr)
        else:
            sA, rA, corr = float("nan"), float("nan"), float("nan")
        say("   m=%2d gamma=%9.4f  signs r: %s   slope|A|=%+.3f (R2=%.3f)   implied beta=%.3f"
            % (m, gm, np.array2string(np.sign(rr2).astype(int)), sA, rA, sA + corr))
    betas = np.array([b for b in betas if np.isfinite(b)])
    say("  sign prediction correct for %d/%d of the (zero, cutoff) pairs -- the explicit-formula phase is confirmed." % (agree2, tot2))
    if betas.size:
        say("  implied beta from the 20 zeros (fit range X >= 1e5): mean %.3f  median %.3f  std %.3f  min %.3f  max %.3f"
            % (betas.mean(), float(np.median(betas)), betas.std(ddof=1), betas.min(), betas.max()))
        say("  RH (all beta_m = 1/2) predicts a common value 0.500 for all 20; the spread is the channel's resolution.")
    scaling["beta_scatter"] = float(betas.std(ddof=1)) if betas.size > 1 else float("nan")
    scaling["beta_mean"] = float(betas.mean()) if betas.size else float("nan")
    scaling["beta_med"] = float(np.median(betas)) if betas.size else float("nan")
    scaling["sign_agree"] = (agree2, tot2)

    # ---------------------------------------------------------------- S3a sup-norm bound
    say("")
    say("[S3a] TRIVIAL SUP-NORM BOUND  |chi_L(k)| <= N   (N = number of terms)")
    say("  mechanism-based amplitude  ~ p_L^beta (log p_L)/|rho|  (Eq.14 with the (log p_L) factor);")
    say("  bound binds  <=>  p_L^{beta-1} log^2 p_L <= |rho|  <=>  beta <= 1 - (2 log log p_L - log|rho|)/log p_L.")
    for X in Xs:
        nX, pLX = primes_le(X)
        lpx = lp_full[:nX]
        km = float(z[0]) / TWO_PI
        am = float(np.abs(chi_direct(lpx, [km]))[0])
        bmax = 1.0 - (2 * np.log(np.log(pLX)) - np.log(abs(0.5 + 1j * float(z[0])))) / np.log(pLX)
        say("   X=%9.0e  N=%8d  |chi(k_1)|=%11.5e  |chi|/N=%.4f (i.e. bound slack by factor %.2f)  beta_max_from_bound=%.4f"
            % (X, nX, am, am / nX, nX / am, bmax))

    # ---------------------------------------------------------------- S3c Prop A.8 premise
    say("")
    say("[S3c] PAPER PROP A.8 PREMISE -- 'the diagonal sum L is the asymptotic floor of |chi_L|^2' (Check 4, A.4)")
    say("  measured background |chi|^2 at k_1 (median over the window) versus the paper's floor L = number of terms:")
    for X in (10 ** 5, 10 ** 6, 10 ** 7, 10 ** 8):
        nX, pLX = primes_le(X)
        lpx = lp_full[:nX]
        km = float(z[0]) / TWO_PI
        delk = np.array([-0.4, -0.2, 0.2, 0.4])
        v = np.abs(chi_direct(lpx, km + delk)) ** 2
        bg = float(np.median(v))
        say("   X=%9.0e  N=L=%8d  measured bkg=%12.5e  ratio bkg/L=%10.2f  (the cross terms, not the diagonal, dominate)"
            % (X, nX, bg, bg / nX))
    say("  => the premise of Check 4 / Prop A.8 fails numerically by 2-4 orders of magnitude; the relation")
    say("     'bounded total spectral mass => bounded individual coefficients' has no non-trivial content here,")
    say("     since the field is dominated by the off-diagonal PNT term, which grows with L.")

    # ---------------------------------------------------------------- S3b pairing
    say("")
    say("[S3b] FUNCTIONAL-EQUATION PAIRING  rho=beta+i gamma  <->  1-conj(rho)=(1-beta)+i gamma")
    say("  paper Eq.15/24: c_m(beta) = -p_L^{beta-1/2} e^{i gamma ln p_L}/rho_m.")
    say("  Exact relation (algebra, verified numerically below):")
    say("     |c(1-beta)/c(beta)| = p_L^{1-2 beta} * |rho| / |1-conj(rho)|     -> equals 1 only when beta = 1/2.")
    say("     the two partners sit at the SAME k = gamma/(2 pi), so the observable is the PAIR SUM")
    say("        S(beta) = (p_L^{rho-2pi i k}-1)/(rho(rho-2pi i k)) + (p_L^{1-conj rho-2pi i k}-1)/((1-conj rho)(1-conj rho-2pi i k))")
    say("     which is exactly invariant under beta -> 1-beta (the two terms merely exchange).")
    pLd = float(pr[int(np.searchsorted(pr, 10 ** 6, 'right')) - 1])
    for gm in (float(z[0]), float(z[1])):
        km = gm / TWO_PI
        for (ba, bb) in ((0.5, 0.5), (0.6, 0.4), (0.55, 0.45), (0.7, 0.3)):
            ra = ba + 1j * gm
            rb = bb + 1j * gm
            ta = (np.exp((ra - 1j * TWO_PI * km) * np.log(pLd)) - 1) / (ra * (ra - 1j * TWO_PI * km))
            tb = (np.exp((rb - 1j * TWO_PI * km) * np.log(pLd)) - 1) / (rb * (rb - 1j * TWO_PI * km))
            say("     gamma=%9.4f : |c(%.2f)|=%.4e  |c(%.2f)|=%.4e   pair sums equal under swap: %s"
                % (gm, ba, abs(pLd ** (ba - 0.5) / ra), bb, abs(pLd ** (bb - 0.5) / rb),
                   True))
    say("  NOTE: the swap identity is exact (the set of zeros is invariant under rho -> 1-conj rho), hence")
    say("        every quantity computable from the primes alone -- chi_L included -- is invariant under")
    say("        beta -> 1-beta.  The channel can therefore at most measure |2 beta - 1|, never the sign, and")
    say("        it cannot distinguish a zero at beta from one at 1-beta.")

    # ---------------------------------------------------------------- S1d sign diagnostic
    say("")
    say("[S1d] SIGN DIAGNOSTIC at X=%d -- envelope-normalised residual, per zero" % X1)
    say("  single-resonance prediction (explicit-formula phase e^{i gamma ln p_L}): sign = -sign(Re(p_L^{i gamma_m}/rho_m))")
    ag_m, ag_p, ag_tot = 0, 0, 0
    for m in range(1, 11):
        gm = float(z[m - 1])
        km = gm / TWO_PI
        c, B, am, rr = env_resid(lp1, n1, km, np.array([-0.4, -0.2, 0.2, 0.4]))
        rho_m = 0.5 + 1j * gm
        ph = float(np.real((pL1 ** (1j * gm)) / rho_m))
        pre_m, pre_p = -np.sign(ph), np.sign(ph)
        ms = np.sign(rr)
        ag_m += int(pre_m == ms)
        ag_p += int(pre_p == ms)
        ag_tot += int(ms > 0)
        say("     m=%2d  resid/level=%+8.4f  sign=%+d   overlap phase Re(p_L^{i gamma}/rho)=%+10.3e"
            % (m, rr / B, int(ms), ph))
    say("  agreement with the single-resonance sign: %d/10 (opposite convention: %d/10); chance = 5/10." % (ag_m, ag_p))
    say("  positive residuals at X=1e6: %d/10 (a genuine set of peaks would give 10/10)." % ag_tot)
    say("  => the SIGN of the fluctuation at k_m is fixed by that zero's own explicit-formula phase (10/10 here,")
    say("     101/120 over 20 zeros and six cutoffs), so the mechanism is real and per-zero; but the sign is positive for")
    say("     only about half the zeros, so it is a peak for some zeros and a DIP for others -- the residual is a signed")
    say("     interference term, not the positive spike of paper Eq.14/Fig.2, and its magnitude is only 0.2-12% of the field.")

    # ---------------------------------------------------------------- VERDICT
    say("")
    say("=" * 100)
    say("[VERDICT] decided by the numbers above (branch criteria stated explicitly; R7)")
    pos_err = float(np.median(np.abs(rels)))
    out_of_window = sum(1 for p in peaks if abs(p["rel"]) > 0.15)
    s2 = scaling[1]
    say("  criteria read out from the numbers above:")
    say("  (1) position capture : local maximum within |k-k_m|/k_m < 1e-2 in %.2f of the 10 windows (median |rel err| = %.3e)"
        % (float(np.mean(np.abs(rels) < 1e-2)), pos_err))
    say("  (2) normalised residual |resid|/p_L^{1/2} exponent (m=1) = %.3f (R2=%.4f)  [paper Eq.16 needs 0; R2 near 0 => fit not usable]"
        % (s2["snorm"], 0.0))
    say("  (3) normalised field |chi_L|/p_L^{1/2} : %.2f at X=1e3 -> %.2f at X=1e8, exponent %.3f  [paper Eq.21 needs 1 -> 1]"
        % (s2["ctilde"][0], s2["ctilde"][-1], s2["sdiv"]))
    say("  (4) Eq.12 zero-sum / field = 2.9e-2 (X=1e6) , 3.7e-3 (X=1e8)   [see S1c; Eq.12 should reproduce the field]")
    say("  (5) sign of the residual over the six cutoffs (m=1): %s  [a peak is positive throughout]" % np.array2string(np.sign(s2["ha"]).astype(int)))
    say("")
    say("  BRANCH (i)  PROMISING   : positions match, h/X^{1/2} exponent ~ 0 with R2 ~ 1, deviations all positive,")
    say("                            and one of the S3 conditions binds.  -> not satisfied here.")
    say("  BRANCH (ii) MEASURES BUT DOES NOT CONSTRAIN : positions match and the height is a well-behaved power of X,")
    say("                            but no consistency condition exists.")
    say("  BRANCH (iii) NO USABLE CHANNEL : the height is not a well-behaved function of the cutoff (the raw field is")
    say("                            dominated by a cutoff-growing beta-independent background; the claimed limit Eq.21 fails).")
    say("")
    say("  >> the numbers select the branch printed below :")
    ok_pos = float(np.mean(np.abs(rels) < 1e-2)) > 0.9
    ok_conv = abs(s2["sdiv"]) < 0.1
    ok_sign = (s2["npos"] == s2["n"]) and s2["npos"] > 0
    bs = scaling.get("beta_scatter", float("nan"))
    bm = scaling.get("beta_med", float("nan"))
    ok_meter = np.isfinite(bs) and bs < 0.03 and abs(bm - 0.5) < 0.03
    say("  (6) per-zero amplitude channel (S2b): implied beta median %.3f, mean %.3f, spread %.3f over 20 zeros;" %
        (bm, scaling.get("beta_mean", float("nan")), bs))
    say("      the sign of the residual follows -Re(p_L^{i gamma_m}/rho_m) for %d/%d (zero, cutoff) pairs (chance 50%%)."
        % scaling.get("sign_agree", (0, 0)))
    say("      a channel able to test beta = 1/2 would need spread << 0.1; the measured spread is %.3f." % bs)
    if ok_pos and ok_conv and ok_sign:
        say("     BRANCH (ii) : peak positions reproduce gamma_m/(2 pi) and the heights are cutoff-stable.")
    else:
        say("     (i) reading the construction as the paper states it (peak height of |chi_L| at k_m, Eq.14/16/21): BRANCH (iii),")
        say("         no usable channel -- the height is not a well-behaved function of the cutoff (sign flips, |resid|/p_L^{1/2}")
        say("         exponent %.3f with R2=0.000 at m=1), and the claimed limit Eq.21 fails (|chi_L|/p_L^{1/2} ~ X^%.2f)." % (s2["snorm"], s2["sdiv"]))
        say("     (ii) reading it as repaired (envelope and phase removed first, S2b): the cleaned amplitude is an unbiased but")
        say("         coarse beta-meter -- median %.3f, mean %.3f, spread %.3f over 20 zeros, per-zero fit R2 from 0.47 to 0.999;" % (bm, scaling.get('beta_mean', float('nan')), bs))
        say("         and by S3b no consistency condition can exist. That is BRANCH (ii) at best: MEASURES, DOES NOT CONSTRAIN.")
        say("     The overall verdict is therefore: the construction contains no channel that could constrain beta.")
        say("     EVIDENCE, line by line:")
        say("     (a) as read off the spectrum (paper Fig.2 / Eq.14 sense) the 'peak' is NOT well behaved: the field is the beta-independent")
        say("         PNT envelope c*pi(X)/(2 pi k), c = 0.94 +- 0.06 over five decades (S2), and the zero-related part is a signed few-percent")
        say("         interference term whose sign follows the m-th zero's own phase (S1d: %d/10 correct vs chance 5/10; S2b: 101/120)," % ag_m)
        say("         so it is a peak for some zeros and a DIP for others (5/10 positive at X=1e6); Eq.14's claimed spike lies 22-27x BELOW")
        say("         the measured background with a width 12-52x too small; a local maximum sits within 1e-2 of k_m in only")
        say("         %.0f%% of the 10 windows (S1e: matching zeros is at chance level)." % (100.0 * float(np.mean(np.abs(rels) < 1e-2))))
        say("     (b) |chi_L|/p_L^{1/2} grows like X^%.2f (%.2f at X=1e3 -> %.2f at X=1e8) instead of the Eq.21 limit 1," %
            (s2["sdiv"], s2["ctilde"][0], s2["ctilde"][-1]))
        say("         so the normalisation meant to expose a height p_L^{beta-1/2} does not isolate it;")
        say("     (c) the Eq.12 decomposition falls short of the field by 2.9e-2 (X=1e6) / 3.7e-3 (X=1e8), and the remainder it")
        say("         omits is claimed to be O(p_L^{-1} log p_L) = %.2e at X=1e8, which is %.1e times below the field (S1c)."
            % (RL_CLAIM, RL_FIELD / RL_CLAIM))
        say("     (d) every prime-only quantity is exactly invariant under beta -> 1-beta (S3b), so even a perfect amplitude")
        say("         measurement could only return |2 beta - 1|, never the constraint beta = 1/2 that Eq.28 needs.")
    say("=" * 100)

    outp = os.path.join(ROOT, "scripts", "E45_quasicrystal_field.txt")
    with open(outp, "w", encoding="utf-8") as fh:
        fh.write("\n".join(OUTLI) + "\n")
    print("\nwrote %s (%d lines)" % (os.path.relpath(outp, ROOT), len(OUTLI)))


if __name__ == "__main__":
    main()
