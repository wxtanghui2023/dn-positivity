#!/usr/bin/env python3
"""
E65_T1_minimal_input.py -- what is the minimal input that would make the phase-uniformity statement pointwise?

THE QUESTION
  The remaining trigger needs the zero-side phase sum S_n = sum_{gamma<=T} e^{i n theta_gamma} to satisfy
  |S_n| <= (1-c) N for EVERY n in the relevant range, with a fixed c > 0.  What is provable from the block moment
  bound is only a density statement, because a finite moment plus Markov always leaves a positive-density
  exceptional set.  The question here is which moment order would actually suffice for zero exceptions, and how
  large the moments really are compared with the Gaussian prediction.

THE ARITHMETIC TESTED
  With a 2k-th moment bound M_{2k} <= C_k N^k of Gaussian size, Markov at threshold cN gives
        #exceptions  <=  |I| * C_k N^k / (cN)^{2k}  =  C_k |I| / (c^{2k} N^k) ,
  which drops below one, hence gives zero exceptions, as soon as
        c  >  (C_k |I| / N^k)^{1/(2k)} .
  So each order k has a threshold c_k; if c_k is below the value the argument actually needs, that order suffices.
  The script computes these thresholds from the scales of the problem and lists them, then measures the real
  moments M_2, M_4, M_6 of S_n on the project's zero tables and compares them with the Gaussian values N, 3N^2,
  15N^3.

INPUTS   data/zeros_odlyzko_100k.npy
OUTPUT   scripts/E65_T1_minimal_input.txt

PROVENANCE
  Written 2026-09-13 by 小灵 after 唐先生 said to continue with the first trigger.  No RH assumption used or claimed;
  numerics are evidence, not proof; NO LEAN IS RUN.
"""

import os

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(os.path.dirname(HERE), "data")


def theta(g):
    """theta(gamma) = 2 arctan(1/(2 gamma)) = arctan(gamma/(gamma^2-1/4))"""
    return 2.0 * np.arctan(1.0 / (2.0 * g))


def main():
    out = []
    out.append("E65 -- minimal input for a pointwise phase-uniformity statement")
    out.append("NO LEAN IS RUN (compute directive 2026-09-13 11:47)")
    out.append("=" * 118)

    g = np.load(os.path.join(DATA, "zeros_odlyzko_100k.npy")).astype(np.float64)
    N = len(g)
    T = float(g[-1])
    X = T * T
    I = X / 2.0                      # the block I = [X/2, X]
    th = theta(g)

    out.append("  scales: N = %d zeros, T = %.1f, X = T^2 = %.4g, |I| = X/2 = %.4g" % (N, T, X, I))
    out.append("")

    # ---- thresholds from the Markov arithmetic (Gaussian constants C_k = (2k-1)!!) ----
    out.append("  (1) thresholds c_k from the Markov arithmetic with Gaussian moment constants C_k = (2k-1)!!")
    out.append("      k    C_k          c_k = (C_k*|I|/N^k)^(1/(2k))      is c_k < 0.2 (the needed value)?")
    from math import factorial
    for k in (1, 2, 3, 4):
        Ck = float(factorial(2 * k)) / (2.0 ** k * factorial(k))       # (2k-1)!!
        ck = (Ck * I / (N ** k)) ** (1.0 / (2 * k))
        out.append("      %-4d %-12.4g %-32.6g %s" % (k, Ck, ck, "yes" if ck < 0.2 else "no"))
    out.append("")

    # ---- measured moments on real zeros ----
    out.append("  (2) measured moments of S_n on the real zeros (sampled over n)")
    rng = np.random.default_rng(20260913)
    ns = rng.integers(int(I / 2), int(I), size=400) + rng.random(400)
    S = np.exp(1j * np.outer(ns, th)).sum(axis=1)                      # S_n for each sampled n
    S = np.abs(S)
    out.append("      samples n in [X/2, X], 400 draws")
    out.append("      moment      measured mean        Gaussian prediction     ratio measured/predicted")
    m2 = float(np.mean(S ** 2))
    m4 = float(np.mean(S ** 4))
    m6 = float(np.mean(S ** 6))
    for name, meas, pred in (("M_2", m2, float(N)), ("M_4", m4, 3.0 * N ** 2), ("M_6", m6, 15.0 * N ** 3)):
        out.append("      %-10s  %-19.6g %-23.6g %.4f" % (name, meas, pred, meas / pred))
    out.append("")
    out.append("      max |S_n| observed: %-14.6g  = %.3e x N        (needed: <= (1-c) N)" % (float(np.max(S)), float(np.max(S)) / N))
    out.append("      rms |S_n| observed: %-14.6g  = %.3e x N" % (float(np.sqrt(m2)), float(np.sqrt(m2)) / N))
    out.append("")
    out.append("=" * 118)
    out.append("READING")
    out.append("  The thresholds decide the question: the order k suffices if its threshold c_k is below the value the")
    out.append("  argument needs, because then Markov already gives zero exceptions at a threshold stricter than")
    out.append("  necessary.  The measured moments then say whether real zeros really sit at the Gaussian size, which is")
    out.append("  what the arithmetic assumes.  Together they identify the minimal order, and thereby whether this")
    out.append("  trigger needs the same kind of input as the other one, namely an unconditional higher moment.")
    txt = "\n".join(out) + "\n"
    with open(os.path.join(HERE, "E65_T1_minimal_input.txt"), "w") as fh:
        fh.write(txt)
    print(txt)


if __name__ == "__main__":
    main()
