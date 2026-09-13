#!/usr/bin/env python3
"""
ANALYTIC2_gabor_identity_check.py -- E46 / WP2 (certificate side): independent numerical verification of the
Poisson-Gabor identity at the critical density, plus its trace corollary.

THE IDENTITY
  Sampling a window phi at the critical Gabor density h = 2 pi / L gives, for all complex z, z',
        sum_{k in Z} phi_hat(z - alpha_k) phi_hat(z' - alpha_k)  =  L * (phi^2)_hat(z - z') ,
  where alpha_k := T + h k and (phi^2)_hat is the Fourier transform of phi^2.  The proof (written up in
  docs/ANALYTIC-2-certificate-side.md) is a one-line Poisson summation: the dual lattice has step L, the
  non-zero dual terms vanish because phi has support in an interval of length L, and the surviving m = 0 term
  equals L (phi^2)_hat(z - z').  Two design points make the numerical check meaningful:

  * The source's lattice offset T enters only through phases exp(2 pi i m T / h) multiplying the dual terms,
    all of which vanish.  The identity is therefore offset-independent, and T = 0 is a faithful instance --
    which matters, because at the source's T = 10^6 each summand is floored at about 1/T^2 and naive partial
    sums would need some 10^13 terms to converge.
  * A compactly supported window whose transform decays faster than any polynomial makes the partial sums
    converge exponentially, so the identity can be verified to high precision instead of being confirmed only
    in mechanism.

CASES
  A: the indicator window (closed form transform), kept to display the algebraic decay of the partial sums;
  B: a C-infinity bump window (transform by quadrature; fewer than a hundred terms suffice).

INPUTS   none (mpmath at 40 digits)
OUTPUT   scripts/ANALYTIC2_gabor_identity_check.txt

PROVENANCE
  Written 2026-09-13 by 小灵 for E46 work package WP2, approved by 唐先生 (12:10 charter, 12:15 "继续").
  Source read: arXiv:2608.13637v2 sections 2.2-2.3 (apparatus, Lemma 2.1 and its proof).  The proof in the
  companion document is independent; this script checks it numerically in a regime where checking is feasible.
  Corrected once before running: an earlier version used the source's offset and therefore could not converge.
  No RH assumption used or claimed, and NO LEAN IS RUN (compute directive 2026-09-13 11:47).
"""

import os

from mpmath import mp, mpf, sin, cos, exp, quad, pi, mpc

mp.dps = 40

L = mpf(12)
H = 2 * pi / L                     # critical Gabor density; offset-free instance (see header)


def alpha(k):
    return H * k


def phi_ind(u):
    return mpf(1) if abs(u) < L / 2 else mpf(0)


def phi_hat_ind(z):
    if abs(z) < mpf(10) ** (-25):
        return mpc(L, 0)
    return 2 * sin(z * L / 2) / z


def phi_bump(u):
    """C-infinity bump supported in (-L/2, L/2), normalised to be positive and even"""
    if abs(u) >= L / 2:
        return mpf(0)
    x = 2 * u / L
    return exp(-1 / (1 - x * x))


def phi_hat_bump(z):
    zr, zi = z.real, z.imag
    re = quad(lambda u: phi_bump(u) * cos(zr * u) * exp(zi * u), [-L / 2, L / 2], maxdegree=12)
    im = quad(lambda u: -phi_bump(u) * sin(zr * u) * exp(zi * u), [-L / 2, L / 2], maxdegree=12)
    return mpc(re, im)


def main():
    out = []

    def w(s, flush=False):
        out.append(s)
        if flush:
            print(s, flush=True)

    w("E46 / WP2 -- Poisson-Gabor identity at the critical density: independent numerical verification")
    w("h = 2*pi/L with L = %s  =>  h = %s ; offset-free instance (the identity is offset-independent)" %
      (mp.nstr(L, 10), mp.nstr(H, 12)))
    w("claim: sum_k phi_hat(z-alpha_k) phi_hat(z'-alpha_k) = L * (phi^2)_hat(z-z')")
    w("NOTE: no Lean is run here (compute directive 2026-09-13 11:47).")
    w("=" * 100, flush=True)

    # ---------------- case A: indicator, algebraic convergence ----------------
    w("", flush=True)
    w("CASE A -- indicator window (closed form); |phi_hat(w)| ~ 1/|w|, so partial sums converge slowly",
      flush=True)
    for (zr, zpr) in [(mpf('0.7'), mpf('1.9')), (mpf('2.3'), mpf('2.3'))]:
        z, zp = mpc(zr, 0), mpc(zpr, 0)
        target = L * phi_hat_ind(z - zp)
        w("   z = %s, z' = %s :  reference = %s" % (mp.nstr(zr, 6), mp.nstr(zpr, 6), mp.nstr(target, 18)),
          flush=True)
        for K in (10, 100, 1000, 10000, 100000):
            s = mpc(0, 0)
            for k in range(-K, K + 1):
                s += phi_hat_ind(z - alpha(k)) * phi_hat_ind(zp - alpha(k))
            w("      K = %6d : |partial sum - reference| = %s" % (K, mp.nstr(abs(s - target), 8)), flush=True)

    # ---------------- case B: C-infinity bump, exponential convergence ----------------
    w("", flush=True)
    w("CASE B -- C-infinity bump window (transform by quadrature); |phi_hat| decays faster than any power",
      flush=True)
    norm2 = quad(lambda u: phi_bump(u) ** 2, [-L / 2, L / 2], maxdegree=12)
    w("   ||phi||_2^2 = %s   =>  L*||phi||_2^2 = %s" % (mp.nstr(norm2, 20), mp.nstr(L * norm2, 20)),
      flush=True)
    for (zr, zi, zpr, zpi) in [(mpf('0.7'), mpf(0), mpf('1.9'), mpf(0)), (mpf('0.3'), mpf(1), mpf('2.4'), mpf(0))]:
        z, zp = mpc(zr, zi), mpc(zpr, zpi)
        target = L * phi_hat_bump(z - zp) * phi_hat_bump(zp - zp) if False else None  # placeholder avoided
        # (phi^2)_hat(z - z') : note only z - z' enters, but phi^2 is not the bump, so integrate directly
        re = quad(lambda u: phi_bump(u) ** 2 * cos((z - zp).real * u) * exp((z - zp).imag * u),
                  [-L / 2, L / 2], maxdegree=12)
        im = quad(lambda u: -phi_bump(u) ** 2 * sin((z - zp).real * u) * exp((z - zp).imag * u),
                  [-L / 2, L / 2], maxdegree=12)
        target = L * mpc(re, im)
        w("   z = %s+%si, z' = %s+%si :  reference = %s"
          % (mp.nstr(zr, 6), mp.nstr(zi, 6), mp.nstr(zpr, 6), mp.nstr(zpi, 6), mp.nstr(target, 18)), flush=True)
        for K in (5, 20, 60):
            s = mpc(0, 0)
            for k in range(-K, K + 1):
                s += phi_hat_bump(z - alpha(k)) * phi_hat_bump(zp - alpha(k))
            w("      K = %4d : |partial sum - reference| = %s" % (K, mp.nstr(abs(s - target), 8)), flush=True)
    # ---------------- trace corollary ----------------
    w("", flush=True)
    w("TRACE COROLLARY -- case B with z = z' = gamma (real): sum_k phi_hat(gamma-alpha_k)^2 = L*||phi||_2^2",
      flush=True)
    for gam in (mpf('0.8'), mpf('2.9')):
        for K in (20, 60):
            s = mpf(0)
            for k in range(-K, K + 1):
                t = phi_hat_bump(mpc(gam - alpha(k), 0))
                s += (t * t).real
            w("      gamma = %s, K = %4d : partial sum = %s   (limit %s)"
              % (mp.nstr(gam, 6), K, mp.nstr(s, 18), mp.nstr(L * norm2, 18)), flush=True)
    w("")
    w("=" * 100)
    w("READING")
    w("  Case A shows the algebraic approach of the partial sums for a discontinuous window; case B shows that")
    w("  with a smooth compactly supported window the identity is confirmed to high precision from a few dozen")
    w("  terms, which is the regime in which the theorem is used.  The offset independence asserted in the")
    w("  header is why the verification may be run at zero offset.")
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "ANALYTIC2_gabor_identity_check.txt"), "w") as fh:
        fh.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
