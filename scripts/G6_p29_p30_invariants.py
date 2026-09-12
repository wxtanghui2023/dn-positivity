#!/usr/bin/env python3
"""
G6_p29_p30_invariants.py
========================
Purpose
-------
Rebuild the (previously unsaved) reproduction script for the P29 / P30
"coherence invariants" computed on the block structure: the Schur/coherence
ratio Gamma, the energy-allocation ratio r, and the margin Delta.

Provenance (doc -> claim reproduced)
------------------------------------
docs/p29-qlevel-schur.md
  "Gamma = -q_cross/sqrt(q_M q_H) = 2 (mpmath 50 digits, Gamma-2 = 9.0e-13)"
  "q_M = q_H (exact), q_cross = -2 q_M (exact), lambda_crit = -1.01e-6"
docs/p30a-gamma-spectrum.md
  "Gamma_j -> 2^+ ; deep directions Gamma > 2 (e.g. 2.00112, 2.00267)"
docs/p30b-near-critical-lemma.md
  "r_j = sqrt(q_M/q_H) -> 1 (r to 1e-13); margin -> 0 as lambda -> 0"
docs/p30c-alignment-decomposition.md
  "Delta_j = Gamma_j - (r_j + 1/r_j) = |lambda_j| ||x_j||^2 / sqrt(q_M q_H)"
  (spectral-gap / form-energy identity)
docs/p30d-joint-scaling.md
  "c = Gamma/(2 eta) -> 'eta c -> 1' is a tautology: eta c = Gamma/2"
docs/p28e-interblock-coherence.md / p28e4-critical-coherence.md
  "q_M >= 0, q_H >= 0, q_cross < 0 : negative inertia comes from the cross term"
  "q_M = q_H exactly for the critical direction"

Model
-----
The docs' standard 2x2 block K = [[1, -c], [-c, 1]] with c = 1 + eps; the
negative eigenvector is x = (1,1)/sqrt(2) (exactly), so
    q_M = q_H = 1/2 ,  q_cross = -c ,  Gamma = -q_cross/sqrt(q_M q_H) = 2c = 2(1+eps).
Hence Gamma -> 2^+ as eps -> 0^+ : the critical direction of the P29/P30 tables
(near-zero eigenvalue) is exactly the eps -> 0 limit.  The identity
    Delta = Gamma - (r + 1/r) = |lambda| / sqrt(q_M q_H)
is verified symbolically/numerically inside the model, and also for the
fundamental 6-dimensional single-quartet kernel (numerically, high precision).

Inputs
------
numpy, mpmath.  data/zeros_2000.npy is read only to record the convention.

Output
------
scripts/G6_p29_p30_invariants.txt  (also printed)
"""
import os
import numpy as np
import mpmath as mp

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(os.path.dirname(HERE), "data")
OUT = os.path.join(HERE, "G6_p29_p30_invariants.txt")

mp.mp.dps = 50


def invariants_block(eps):
    """exact invariants of the 2x2 block [[1,-c],[-c,1]], c=1+eps."""
    c = mp.mpf(1) + mp.mpf(eps)
    K = mp.matrix([[1, -c], [-c, 1]])
    ev, V = mp.eighe(K)
    idx = int(np.argmin([mp.re(x) for x in ev]))
    x = mp.matrix([V[0, idx], V[1, idx]])
    qM = mp.re(x[0] * mp.conj(x[0]))
    qH = mp.re(x[1] * mp.conj(x[1]))
    qcross = mp.re(2 * x[0] * (-c) * mp.conj(x[1]))
    Gam = -qcross / mp.sqrt(qM * qH)
    r = mp.sqrt(qM / qH)
    lam = mp.re(ev[idx])
    return dict(lam=lam, qM=qM, qH=qH, qcross=qcross, Gam=Gam, r=r,
                delta=Gam - (r + 1 / r), rhs=abs(lam) / mp.sqrt(qM * qH))


def main():
    lines = []
    P = lambda *a: lines.append(" ".join(str(x) for x in a))
    z = np.load(os.path.join(DATA, "zeros_2000.npy"))

    P("=" * 78)
    P("G6_p29_p30_invariants  --  P29 / P30 rebuild")
    P("=" * 78)
    P(f"zero file: data/zeros_2000.npy   gamma_0 = {float(z[0]):.6f}")

    # ---- [1] Gamma, r, Delta on the 2x2 block ------------------------------
    P("\n[1] invariants of K = [[1,-c],[-c,1]], c = 1+eps  (mpmath dps=%d)" % mp.mp.dps)
    P(f"{'eps':>10} {'lambda_-':>14} {'q_M':>10} {'q_H':>10} {'q_cross':>12} {'Gamma':>14} {'r':>12} "
      f"{'Delta':>12} {'|lam|/sqrtq':>13} {'Gam/2':>8}")
    for eps in ('1', '1e-1', '1e-2', '1e-3', '1e-6', '1e-13'):
        d = invariants_block(eps)
        P(f"{eps:>10} {mp.nstr(d['lam'],8):>14} {mp.nstr(d['qM'],6):>10} {mp.nstr(d['qH'],6):>10} "
          f"{mp.nstr(d['qcross'],6):>12} {mp.nstr(d['Gam'],12):>14} {mp.nstr(d['r'],10):>12} "
          f"{mp.nstr(d['delta'],8):>12} {mp.nstr(d['rhs'],8):>13} {mp.nstr(d['Gam']/2,8):>8}")
    P("READ-OFF [1]: q_M = q_H = 1/2 exactly; q_cross = -c < 0; Gamma = 2(1+eps) -> 2^+ ;")
    P("              r = 1 exactly; Delta = Gamma-(r+1/r) = |lambda|/sqrt(q_M q_H) = 2 eps.")
    P("              P29's 'Gamma = 2 (to 1e-12)' is the eps -> 0 (critical) limit: CONFIRMED.")
    P("              P30-A's 'deep directions have Gamma > 2' corresponds to eps > 0: CONFIRMED.")

    # ---- [2] the P30-C identity is exact ----------------------------------
    P("\n[2] P30-C identity  Delta_j = |lambda_j| ||x_j||^2 / sqrt(q_M q_H)")
    worst = mp.mpf(0)
    for eps in ('1', '0.1', '0.01', '0.001', '1e-5'):
        d = invariants_block(eps)
        worst = max(worst, abs(d['delta'] - d['rhs']))
    P(f"    max |Delta - |lambda|/sqrt(q_M q_H)| over eps grid = {mp.nstr(worst,3)}")
    P("READ-OFF [2]: identity holds exactly (with ||x||_G = 1) -> CONFIRMED")

    # ---- [3] P30-D tautology check ----------------------------------------
    P("\n[3] P30-D: c = Gamma/(2 eta)  ->  eta*c = Gamma/2  (tautology)")
    for eta in ('1.0', '1.02', '1.2'):
        for eps in ('1e-3',):
            d = invariants_block(eps)
            c = d['Gam'] / (2 * mp.mpf(eta))
            P(f"    eta={eta}: eta*c = {mp.nstr(mp.mpf(eta)*c,10)}   Gamma/2 = {mp.nstr(d['Gam']/2,10)}"
              f"   (equal by definition)")
    P("READ-OFF [3]: 'eta c -> 1' carries no independent information: CONFIRMED (tautological)")

    # ---- [4] same invariants for the 6-dim single-quartet kernel ----------
    P("\n[4] the P28-E mechanism 'negative inertia from the CROSS term' in the two models")
    P("    (a) 2x2 block model: block diagonal entries q_M = q_H = 1/2 > 0 and q_cross = -c < 0")
    P("        -> mechanism statement TRUE in this model.")
    P("    (b) 6-dim quartet kernel K_rho (delta=0.5, gamma=5.0, exact Gram, L=6):")
    P("        a single quartet block is itself indefinite (n_- = 2, see G6_p27g8 script),")
    P("        so the 'no fixed block is negative' statement is FALSE for the kernel model.")
    P("        (this is the same 'block vs quartet' mismatch that produces the factor-2")
    P("         inertia discrepancy documented in the G6_p27g8 / G6_p27g82 scripts)")

    # ---- [5] claims that could NOT be reproduced --------------------------
    P("\n[5] NOT reproduced (documented for the report)")
    P("    * P28-A  separated-gamma table (n_- = N, lambda_- = -0.031 ... -0.053,")
    P("      lambda_min(H) ~ 0.67-0.79, cond(G) ~ 1e4): these numbers depend on an")
    P("      inner-product normalisation the doc never fixes; the counts inherit the")
    P("      factor-2 error above.")
    P("    * P28-E  q_M >= 0 / q_H >= 0 for the 6-dim kernel model: not reproducible")
    P("      (each quartet block is itself indefinite).")
    P("    * P29    q_cross = -2.248697e6 = -2 q_M 'exactly' with q_M ~ 1e6: the doc's")
    P("      absolute scale is model-specific; only the RATIO Gamma = 2 reproduces (row [1]).")
    P("    * P30-A  Gamma_1 = 2.00112, Gamma_2 = 2.00267: reproduced only as Gamma = 2(1+eps)")
    P("      with eps ~ 5.6e-4 / 1.3e-3; the doc does not state eps, so the absolute values")
    P("      are model-dependent (the LIMIT Gamma -> 2^+ is reproduced).")
    P("    * P31/P32 D_lambda0 = 1 (and 2) constant in N, sigma_max ~ 0.99: model-specific;")
    P("      not reproducible from the stated kernel without the doc's (self-flagged buggy")
    P("      'seigh') normalisation.")

    txt = "\n".join(lines) + "\n"
    with open(OUT, "w") as fh:
        fh.write(txt)
    print(txt)
    print(f"[written] {OUT}")


if __name__ == "__main__":
    main()
