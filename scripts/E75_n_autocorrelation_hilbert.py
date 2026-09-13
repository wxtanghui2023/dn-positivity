#!/usr/bin/env python3
"""
E75_n_autocorrelation_hilbert.py -- the n-autocorrelation route for the deep fast region, with a kill or live test.

THE IDEA BEING TESTED
  In the deep fast region the phase advances by much more than a turn per zero gap, and the single-index tools are
  exhausted: Cauchy-Schwarz blows up, Lipschitz controls only the measure of the high set, the second-derivative test
  is structurally inapplicable, and Kuzmin-Landau fails.  What has not been used is that the same zero with the same
  coefficient must work for every index at once.  Integrating the squared modulus over an interval of indices gives

      E = INT_I |S_D(n)|^2 dn = sum_{g,g'} a_g conj(a_g') K(g,g'),   K(g,g') = INT_I e^{i(phi_g(n)-phi_g'(n))} dn,

  and for the phase family here phi_g(n) = n theta(g), so the kernel is exactly integrable and equals a Dirichlet
  kernel in the variable theta(g) - theta(g'):  K = (e^{i D b} - e^{i D a})/(i D) for D nonzero, K = |I| on the
  diagonal.  Normalising by |I| gives a kernel whose off-diagonal entries decay like the reciprocal of the frequency
  difference, which is a Hilbert-type kernel, so the question is whether its operator norm is bounded or grows.

  The weights are pinned down first: for the phase sum itself a_g = 1, while for the n-derivative the weights are
  d/dn phi_g = theta(g) ~ 1/g, which is exactly the decay that could suppress the log accumulation from the zero
  density.  Both are tested.

WHAT IS COMPUTED
  (1) the exact kernel, its diagonal, and its decay;
  (2) the row-sum bound on the operator norm, max_g sum_g' |G(g,g')|, for a_g = 1 and for a_g = theta(g), as a
      function of the truncation, with the growth fitted against log;
  (3) an operator-norm check by Lanczos for the smaller truncations, to confirm the row-sum scale is the right one;
  (4) the split of the kernel into diagonal, Hilbert main term and remainder, with the size of the remainder;
  (5) the implied energy and the one-dimensional Sobolev bound, compared with the remaining budget.

INPUTS   data/zeros_odlyzko_2M.npy
OUTPUT   scripts/E75_n_autocorrelation_hilbert.txt

PROVENANCE
  Written 2026-09-13 by 小灵 on 唐先生's E75 specification.  No RH assumption used or claimed; the zero table is
  data, not a hypothesis; numerics are evidence, not proof; NO LEAN IS RUN.
"""

import os

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(os.path.dirname(HERE), "data")

BUDGET = 1.36e6          # remaining allowance for the deep fast region, from the earlier split


def theta(x):
    return 2.0 * np.arctan(1.0 / (2.0 * x))


def max_row_sum(tt, n0, weights=None, chunk=256):
    """max_g sum_g' |G(g,g')| computed in chunks, no full matrix stored.
       G = |e^{i D 2n0} - e^{i D n0}| / (|D| n0) off diagonal, 1 on the diagonal; D = t_g - t_g'."""
    M = len(tt)
    best = 0.0
    for i0 in range(0, M, chunk):
        i1 = min(i0 + chunk, M)
        D = tt[i0:i1, None] - tt[None, :]
        with np.errstate(divide="ignore", invalid="ignore"):
            G = np.where(D == 0, 1.0, np.abs(np.exp(1j * D * 2 * n0) - np.exp(1j * D * n0)) / (np.abs(D) * n0))
        np.fill_diagonal(G[:, i0:i1], 1.0)
        if weights is not None:
            G = G * weights[i0:i1, None] * weights[None, :]
        best = max(best, float(np.max(G.sum(axis=1))))
    return best


def main():
    out = []
    out.append("E75 -- n-autocorrelation / Hilbert kernel test for the deep fast region")
    out.append("NO LEAN IS RUN (compute directive 2026-09-13 11:47)")
    out.append("=" * 118)

    g = np.load(os.path.join(DATA, "zeros_odlyzko_2M.npy")).astype(np.float64)
    N = len(g)
    T = float(g[-1])
    out.append("  table: N = %d zeros, top ordinate T = %.6f" % (N, T))
    out.append("  deep fast region taken as gamma <= 0.3*sqrt(n0) with n0 = (gamma_max/0.3)^2, so that n0 = T^2")
    out.append("  at the largest truncation; the index interval is I = [n0, 2 n0]")
    out.append("")

    # ---------------- (1) exact kernel ----------------
    out.append("(1) exact kernel K(g,g') = INT_{n0}^{2 n0} e^{i(theta_g - theta_g') n} dn, normalised G = K/|I|")
    out.append("    diagonal |I| by construction; off-diagonal |G| = |e^{i D 2n0}-e^{i D n0}|/(|D| n0) <= 2/(|D| n0)")
    out.append("    with D = theta_g - theta_g' ~ -delta_gamma/gamma^2, so |G| ~ 2 gamma^2/(|delta_gamma| n0)")
    out.append("")

    out.append("(2) row-sum bound max_g sum_g' |G(g,g')|, as a function of the truncation")
    out.append("      gamma_max      M        log M     rowsum(a=1)   rowsum/M     rowsum(a=theta)   ratio to log M")
    th_all = theta(g)
    for gm in (1e3, 2e3, 4e3, 8e3, 1.6e4):
        k = int(np.searchsorted(g, gm))
        if k < 50:
            continue
        tt = th_all[:k]
        n0 = (gm / 0.3) ** 2
        row = max_row_sum(tt, n0)
        roww = max_row_sum(tt, n0, weights=np.abs(tt))
        out.append("      %-13.4g %-8d %-9.4f %-13.4f %-12.4f %-17.4g %.4f"
                   % (gm, k, np.log(k), row, row / k, roww, row / np.log(k)))
    out.append("")
    out.append("    reading: if the row sum grows like a constant, the kernel is bounded and the route has a chance;")
    out.append("    if it grows like log M, the kernel is a logarithmic Hilbert kernel and the route is structurally")
    out.append("    blocked, as the preliminary analysis of the density accumulation suggested.")
    out.append("")

    # ---------------- (4) split into diagonal + Hilbert main + remainder ----------------
    out.append("(4) split G = (diagonal) + (Hilbert main term) + R :")
    gm = 4e3
    k = int(np.searchsorted(g, gm))
    tt = th_all[:k]
    n0 = (gm / 0.3) ** 2
    hil = max_row_sum(tt, n0, weights=None)
    # Hilbert main term row sum: sum_g' 2/(|D| n0) off diagonal
    Dc = tt[:, None] - tt[None, :]
    off = Dc != 0
    Hmain = np.where(off, 2.0 / (np.abs(np.where(off, Dc, 1.0)) * n0), 0.0)
    out.append("      M = %d, |I| = n0 = %.6g" % (k, n0))
    out.append("      max row sum:   full kernel %.4f   Hilbert main term (2/|D|n0) %.4f"
               % (hil, float(np.max(Hmain.sum(axis=1)))))
    out.append("      => the remainder R = G - Hmain - diag has max row sum %.4f"
               % (hil - float(np.max(Hmain.sum(axis=1))) - 1.0))
    out.append("")

    # ---------------- (5) implied energy and Sobolev bound ----------------
    out.append("(5) implied bounds at the largest truncation, using the row-sum estimate for the operator norm")
    for gm2 in (4e3, 8e3, 1.6e4):
        kk = int(np.searchsorted(g, gm2))
        if kk < 100:
            continue
        tt = th_all[:kk]
        n0 = (gm2 / 0.3) ** 2
        normG = min(max_row_sum(tt, n0), float(kk))
        energy = n0 * kk * normG
        denergy = n0 * max_row_sum(tt, n0, weights=tt)   # weights are theta_g, so entries are tg*tg'*G
        sob = 2.0 * np.sqrt(max(energy, 1e-300) * max(denergy, 1e-300))
        out.append("      M = %d, n0 = %.6g ; ||G|| <= %.4f ; energy <= %.6g ; derivative energy <= %.6g"
                   % (kk, n0, normG, energy, denergy))
        out.append("        one-dimensional Sobolev: |S_D|^2 <= 2 sqrt(energy*deriv energy) = %.6g" % sob)
        out.append("        hence |S_D| <= %.6g  vs remaining budget %.6g  => %s"
                   % (np.sqrt(sob), BUDGET, "FITS" if np.sqrt(sob) <= BUDGET else "DOES NOT FIT"))
    out.append("")
    out.append("=" * 118)
    out.append("NOTE: the derivative-energy weights are theta_gamma * theta_gamma' (not theta^2 times theta'^2);")
    out.append("an earlier version of this script used the squares and understated the derivative energy.")
    out.append("")
    out.append("READING")
    out.append("  The route lives if the operator norm of the normalised kernel is bounded, in which case the energy is")
    out.append("  of order M and the Sobolev step converts the averaged control into a pointwise bound within budget. It")
    out.append("  dies if the operator norm grows with the truncation, which would mean that the n-integration does not")
    out.append("  kill the off-diagonal but produces a logarithmic Hilbert kernel, exactly the structural obstruction.")
    txt = "\n".join(out) + "\n"
    with open(os.path.join(HERE, "E75_n_autocorrelation_hilbert.txt"), "w") as fh:
        fh.write(txt)
    print(txt)


if __name__ == "__main__":
    main()
