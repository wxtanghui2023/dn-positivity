#!/usr/bin/env python3
"""
E67_T1_true_scale_constants.py -- measure the moment constants at the ACTUAL scales of the trigger.

WHY THE SCALE MATTERS
  The requirement distilled earlier is that the fourth moment of the phase sum satisfy M_4 <= C*N^2 with C < 2.55,
  which came from the Markov arithmetic at the scales of the problem: block length |I| = T0^2/2 and count
  N = 2.001e6 zeros up to T0 = 1.1325e6.  The earlier measurement was made on a hundred-thousand-zero table whose
  height is sixteen times smaller, and the constants are scale-dependent, so the decisive number has to be measured
  where the trigger actually lives.  This script does that: it samples indices in the range the argument uses,
  starting near three tenths of T0 squared, and computes the exact second and fourth moments of the phase sum over
  the full two-million-zero table.

WHAT IS MEASURED
   S_n = sum_{gamma<=T0} exp(i n theta_gamma),  theta_gamma = 2 arctan(1/(2 gamma))
   M_2 = mean |S_n|^2 over sampled n,  M_4 = mean |S_n|^4,  and the normalised constant C = M_4 / N^2.
  For reference the Gaussian-complex value is M_4 = 2 (M_2)^2, and the Markov requirement is C < 2.55.

INPUTS   data/zeros_odlyzko_2M.npy
OUTPUT   scripts/E67_T1_true_scale_constants.txt

PROVENANCE
  Written 2026-09-13 by 小灵 on 唐先生's instruction to continue the derivation.  No RH assumption used or claimed;
  the zero table is data, not a hypothesis; numerics are evidence, not proof; NO LEAN IS RUN.
"""

import os

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(os.path.dirname(HERE), "data")


def main():
    out = []
    out.append("E67 -- moment constants of the phase sum at the true scales of the trigger")
    out.append("NO LEAN IS RUN (compute directive 2026-09-13 11:47)")
    out.append("=" * 118)

    g = np.load(os.path.join(DATA, "zeros_odlyzko_2M.npy")).astype(np.float64)
    N = len(g)
    T0 = float(g[-1])
    X = T0 * T0
    th = 2.0 * np.arctan(1.0 / (2.0 * g))
    out.append("  N = %d zeros, T0 = %.6f, X = T0^2 = %.6g, |I| = X/2 = %.6g" % (N, T0, X, X / 2))
    out.append("")

    rng = np.random.default_rng(20260913)
    ns = 0.30 * X + rng.random(400) * (X - 0.30 * X)
    out.append("  sampling 400 indices n uniformly in [0.30*X, X]  (the range the argument uses)")
    absS = np.empty(len(ns))
    for i, n in enumerate(ns):
        absS[i] = abs(np.exp(1j * n * th).sum())
    m2 = float(np.mean(absS ** 2))
    m4 = float(np.mean(absS ** 4))
    out.append("")
    out.append("      quantity            value                 normalised                comment")
    out.append("      M_2                 %-21.6g M_2/N = %-16.6f (random-phase value 1)" % (m2, m2 / N))
    out.append("      M_4                 %-21.6g M_4/N^2 = %-14.6f (requirement: < 2.55)" % (m4, m4 / N ** 2))
    out.append("      2*(M_2)^2/N^2       %-21.6g %-24.6f (Gaussian-complex prediction)" % (2 * m2 ** 2 / N ** 2, 2 * m2 ** 2 / N ** 2))
    out.append("      max |S_n|           %-21.6g max|S_n|/N = %-13.6f (requirement: <= 0.8)" % (float(np.max(absS)), float(np.max(absS)) / N))
    out.append("      rms |S_n|           %-21.6g rms/N = %-17.6f" % (float(np.sqrt(m2)), float(np.sqrt(m2)) / N))
    out.append("      sqrt(N)             %-21.6g rms/sqrt(N) = %-14.6f" % (float(np.sqrt(N)), float(np.sqrt(m2)) / float(np.sqrt(N))))
    out.append("")
    out.append("=" * 118)
    out.append("READING")
    out.append("  C = M_4/N^2 is the constant the derivation must bound below 2.55.  If the measured constant is far below")
    out.append("  that, the fourth-moment route has room and the remaining task is the uniform inequality.  If it is close")
    out.append("  to or above it, the route cannot work with the fourth moment and would need a higher order instead.")
    out.append("  The ratio M_2/N says how far the phases are from equidistribution at these indices, and rms/sqrt(N)")
    out.append("  says whether the sum sits at the random-phase scale.")
    txt = "\n".join(out) + "\n"
    with open(os.path.join(HERE, "E67_T1_true_scale_constants.txt"), "w") as fh:
        fh.write(txt)
    print(txt)


if __name__ == "__main__":
    main()
