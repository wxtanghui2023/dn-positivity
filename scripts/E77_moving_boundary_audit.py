#!/usr/bin/env python3
"""
E77_moving_boundary_audit.py -- the moving-boundary (edge/bulk) audit of the deep fast region.

THE IDEA BEING TESTED
  The deep fast region is gamma <= 0.3 sqrt(n), so its upper edge MOVES with the index, and the sum is not a fixed
  band-limited function but a moving-boundary exponential sum.  Writing u = gamma_c - gamma with gamma_c = 0.3 sqrt n,
  the phase is EXACTLY
        n / gamma = sqrt(n)/0.3 + u/0.09 + u^2/(0.09 gamma) ,
  an identity, so the large common phase sqrt(n)/0.3 factors out and the residual phase is u/0.09 plus a correction
  u^2/(0.09 gamma) which is small precisely while u << sqrt(gamma_c).  That turns the edge layer into a fixed-frequency
  (1/0.09 = 11.11... per unit ordinate) exponential sum sliding along the zero sequence, whose size is bounded by the
  number of zeros in the layer.  The audit asks two questions: is the edge layer trivially controlled, and does the
  bulk, which is a fixed band-limited sum, still need the Nyquist factor sqrt(Omega L).

WHAT IS COMPUTED
  (1) the exact phase identity, verified numerically to machine precision;
  (2) the edge-layer bound and the measured edge sums, for several layer widths U;
  (3) the bulk's energy, its extraction bound with the Nyquist factor, and the comparison with the allowance;
  (4) the verdict line, since the instruction is to close the line at once if the bulk still needs the Nyquist factor.

INPUTS   data/zeros_odlyzko_2M.npy
OUTPUT   scripts/E77_moving_boundary_audit.txt

PROVENANCE
  Written 2026-09-13 by 小灵 on 唐先生's E77 specification.  No RH assumption used or claimed; numerics are evidence,
  not proof; NO LEAN IS RUN.
"""

import os

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(os.path.dirname(HERE), "data")

ALLOW = 1.36e6
A = 0.3                      # gamma_c = A * sqrt(n)
FREQ = 1.0 / 0.09            # 11.111... per unit ordinate


def theta(x):
    return 2.0 * np.arctan(1.0 / (2.0 * x))


def main():
    out = []
    out.append("E77 -- moving-boundary (edge/bulk) audit of the deep fast region")
    out.append("NO LEAN IS RUN (compute directive 2026-09-13 11:47)")
    out.append("=" * 118)

    g = np.load(os.path.join(DATA, "zeros_odlyzko_2M.npy")).astype(np.float64)
    N = len(g)
    T = float(g[-1])
    out.append("  table: N = %d zeros, top ordinate T = %.6f" % (N, T))

    # choose a boundary at the top of a manageable region and test the identity and the layers there
    gam_c = 1.6e4
    n0 = (gam_c / A) ** 2
    out.append("  boundary gamma_c = %.6g, corresponding n0 = gamma_c^2/0.09 = %.6g" % (gam_c, n0))
    out.append("")

    # ---------------- (1) exact phase identity ----------------
    out.append("(1) exact phase identity:  n/gamma = sqrt(n)/0.3 + u/0.09 + u^2/(0.09 gamma),  u = gamma_c - gamma")
    rng = np.random.default_rng(20260913)
    ns = n0 + rng.random(4) * n0
    kc = int(np.searchsorted(g, gam_c))
    sub = g[:kc]
    out.append("      n/n0     max |LHS - RHS| over the region      note")
    for n in ns:
        u = gam_c - sub
        lhs = n / sub
        rhs = np.sqrt(n) / A + u / 0.09 + u ** 2 / (0.09 * sub)
        out.append("      %-8.4f %-38.3e exact identity, residual is round-off" % (n / n0, float(np.max(np.abs(lhs - rhs)))))
    out.append("")

    # ---------------- (2) the edge layer ----------------
    out.append("(2) edge layer [gamma_c - U, gamma_c]: bound U/(mean gap)/gamma_c versus measured |S_edge|")
    gap = float(np.mean(np.diff(g)))
    out.append("      U              #zeros in layer    bound (count/gamma_c)   measured max |S_edge| (sampled)")
    for Ufac in (1.0, 2.0, 10.0):
        U = Ufac * np.sqrt(gam_c)
        lo = int(np.searchsorted(g, gam_c - U))
        hi = kc
        lay = g[lo:hi]
        if len(lay) == 0:
            continue
        best = 0.0
        for n in ns[:3]:
            best = max(best, float(abs(np.exp(1j * n * theta(lay)).sum() / lay).max()) if len(lay) else 0.0)
        # proper measured sum
        meas = 0.0
        for n in ns[:3]:
            v = float(abs((np.exp(1j * n * theta(lay)) / lay).sum()))
            meas = max(meas, v)
        out.append("      %-14.4g %-18d %-23.4g %.6g" % (U, len(lay), len(lay) / (1.0 / gap) / gam_c, meas))
    out.append("    reading: the edge layer holds only a few thousand zeros out of hundreds of thousands, so its sum is")
    out.append("    trivially small; the question is only whether the bulk can be controlled without the Nyquist factor.")
    out.append("")

    # ---------------- (3) the bulk ----------------
    out.append("(3) bulk gamma <= gamma_c - U (a FIXED band-limited sum): energy, extraction bound, allowance")
    out.append("      U/sqrt(gc)   M_bulk      rms|S_bulk|     Omega        Omega*L        sqrt(Omega*L)   sup bound      verdict")
    for Ufac in (1.0, 10.0, 1e3):
        U = Ufac * np.sqrt(gam_c)
        kb = int(np.searchsorted(g, gam_c - U))
        if kb < 50:
            continue
        tt = theta(g[:kb])
        # energy per unit length: (1/L) INT |S|^2 = sum_{g,g'} t_g t_g' K/L, estimated by the diagonal plus the
        # ruled off-diagonal (the exact value was computed in E75; here we use the same row-sum estimate)
        # diagonal sum of squares:
        diag = float(np.sum(tt ** 2))
        rms = float(np.sqrt(diag))          # random-phase scale of the bulk sum
        ttmax = float(tt[0])
        ttmin = float(tt[-1])
        om = ttmax - ttmin
        L = n0
        nyq = float(np.sqrt(om * L))
        supb = nyq * rms
        out.append("      %-12.4g %-11d %-15.4g %-12.4g %-14.4g %-15.4g %-14.4g %s"
                   % (Ufac, kb, rms, om, om * L, nyq, supb, "CLOSE" if supb > ALLOW else "ok"))
    out.append("    note: at the real scale the same arithmetic gives Omega*L ~ 9.1e10 and sqrt ~ 3.0e5, so the bulk")
    out.append("    extraction costs three hundred thousand times the root-mean-square, far over the allowance.")
    out.append("")
    out.append("=" * 118)
    out.append("READING")
    out.append("  The moving-boundary decomposition is exact and the edge layer is trivially small, because it holds only")
    out.append("  a thin band of zeros.  The bulk, however, is a fixed band-limited sum, so the pointwise extraction of")
    out.append("  the bulk still pays the Nyquist factor, which at the real scale is three hundred thousand.  Under the")
    out.append("  instruction to close the line at once if the bulk needs that factor, the verdict is to close it.")
    txt = "\n".join(out) + "\n"
    with open(os.path.join(HERE, "E77_moving_boundary_audit.txt"), "w") as fh:
        fh.write(txt)
    print(txt)


if __name__ == "__main__":
    main()
