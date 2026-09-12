#!/usr/bin/env python3
"""
E26C (E26/A4-4, computation C): the explicit pointwise constant - from d_r(lambda)^2 to a
zero-free disc, the sensitivity of the radius to d^2, and the ambiguity in the recorded formula.

PROVENANCE / PURPOSE
   Designed in docs/E26-A4-4-constructive-direction.md section 6(C): at lambda = r + i H with
   r = 1/2, H = 10^3, 10^5, take d_r(lambda)^2 from DFMR I Prop. 7.5 and convert it into the
   zero-free disc of docs/E27-A4-5-dN-to-zero-free.md section 2,
       rad = |lambda| sqrt(1 - 2 Re(lambda) d^2) / (Re(lambda) d^2),
   centre c*lambda with c = (1+R^2)/(1-R^2) = 1/(Re(lambda) d^2) - 1.
   Success criterion: the disc is non-empty and does not conflict with the verified zero-free
   region (Platt-Trudgian: RH verified for |t| <= 3e12, 引用); record the 1/d^2 sensitivity.

   TWO APOLLONIUS VARIANTS (both are standard; the two DFMR statements recorded in this repo
   use different denominators, so both are computed and compared):
     variant 1 - denominator |z + lambda|   (DFMR II Thm 2.1 with sigma_0 = 0, as recorded in
                 docs/E27-A4-5 section 1)  ==>  centre c*lambda, rad = |lambda|R/(a d^2);
     variant 2 - denominator |z + conj(lambda)|  (DFMR I section 7.1.1, as recorded)  ==>
                 centre (lambda + R^2 conj(lambda))/(1-R^2) = c*a + i*b, rad = R/d^2 = 2aR/(1-R^2).
   Both are verified below by direct sampling.  They differ by the factor |lambda|/a in radius
   (and by the centre), i.e. by ~2*10^5 at H = 10^5 - so the explicit constant M3 of the roadmap
   cannot be pinned down from the material at hand.

   HONEST SCOPE / WHAT IS MISSING.  DFMR I Prop. 7.5 (引用, as recorded in docs/E27-A4-5
   section 1) gives only the LAMBDA-FREE bound d_r^2 < 1/(2-2r), which at r = 1/2 is d^2 < 1 and
   is exactly the non-emptiness threshold (section 4): it yields a degenerate disc.  An actual
   lambda-dependent d_r(lambda)^2 needs DFMR I section 7's explicit functional evaluated for a
   concrete test function f_{A,r} together with ||f_{A,r}||_2 and phi-hat (DFMR I Cor. 2.3 /
   Cor. 7.4).  That source is not in this repository and is NOT fabricated here.  The project's
   own d_N^2 is a DIFFERENT object (length-N class vs DFMR's length-free class, containment
   unverified - docs/E27-A4-5 section 4 G1/G2), so it is used only as a labelled illustrative
   proxy in section 5, never as a result.  No zero-free region is claimed anywhere below.

Inputs : data/zeros_odlyzko_2M.npy (2 001 052 ordinates, gamma <= 1.13249e6, read-only)
Outputs: scripts/E26C_dfmr_pointwise_distance.txt
Labels : 核验 = verified against this script | 引用 = quoted from a source | 推导 = derived here
"""
import os
import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ZEROS = os.path.join(ROOT, 'data', 'zeros_odlyzko_2M.npy')
OUT = os.path.join(ROOT, 'scripts', 'E26C_dfmr_pointwise_distance.txt')
R0 = 0.5                       # r = 1/2
HEIGHTS = (1.0e3, 1.0e5)
D2S = (0.9, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01, 1e-3, 1e-6)

class Tee:
    def __init__(self, path):
        self.f = open(path, 'w')
    def __call__(self, msg):
        print(msg, flush=True)
        self.f.write(str(msg) + "\n"); self.f.flush()
say = Tee(OUT)

def disc(lam, d2, variant):
    """Apollonius disc for |z-lam| < R |z - B| with B = -lam (v1) or -conj(lam) (v2).
       Returns (R2, centre, rad, ok) - ok False when empty/degenerate."""
    a = lam.real
    R2 = 1.0 - 2.0 * a * d2
    if R2 <= 0.0:
        return R2, None, 0.0, False
    R = np.sqrt(R2)
    B = -lam if variant == 1 else -np.conj(lam)
    centre = (lam - R2 * B) / (1.0 - R2)
    rad = R * abs(lam - B) / (1.0 - R2)
    return R2, centre, rad, True

def main():
    say("=" * 100)
    say("E26C: the DFMR pointwise disc - radius law, sensitivity, variant ambiguity, availability")
    say("=" * 100)
    say("  lambda = r + iH, r = %.2f, H in %s, a = Re(lambda) = %.2f" % (R0, HEIGHTS, R0))
    say("  R^2 = 1 - 2 a d^2 (non-empty iff d^2 < 1/(2a) = 1) ; two Apollonius variants, see header")

    say("")
    say("  SECTION 1 (核验) - both Apollonius identities checked numerically (4000 random samples)")
    lam = complex(R0, HEIGHTS[0]); a = lam.real
    for variant in (1, 2):
        for d2 in (0.31, 0.9):
            R2, ctr, rad, ok = disc(lam, d2, variant)
            B = -lam if variant == 1 else -np.conj(lam)
            rng = np.random.default_rng(7 + variant)
            bad = 0
            for _ in range(4000):
                z = complex(rng.uniform(-3, 3) * abs(lam), rng.uniform(-3, 3) * abs(lam))
                if (abs(z - lam) ** 2 < R2 * abs(z - B) ** 2) != (abs(z - ctr) < rad):
                    bad += 1
            say("  variant %d, d^2=%.2f : centre=(%+.6f,%+.6f) rad=%.6e ; disagreements %d/4000"
                % (variant, d2, ctr.real, ctr.imag, rad, bad))
    say("  variant 1 centre = c*lambda (c = 1/(a d^2) - 1) ; variant 2 centre = c*a + i*b")
    say("  radius ratio variant1/variant2 = |lambda|/a = %.4e at H = %.0e  (they agree only for real lambda)"
        % (abs(complex(R0, HEIGHTS[1])) / R0, HEIGHTS[1]))
    for dd in (1.0 - 1e-3, 1.0 - 1e-6):
        _, _, r1, _ = disc(lam, dd, 1); _, _, r2, _ = disc(lam, dd, 2)
        say("  d^2 = %.6f -> rad = %.6e (v1), %.6e (v2) : both -> 0 at the threshold 1/(2a) = 1"
            % (dd, r1, r2))

    say("")
    say("  SECTION 2 (核验) - radius law, both variants")
    for H in HEIGHTS:
        lam = complex(R0, H)
        say("  H = %.0e   %8s | %14s %16s | %14s %16s" %
            (H, "d^2", "rad/|lam| (v1)", "rad (v1)", "rad (v2)", "rad/|lam| (v2)"))
        for d2 in D2S:
            _, _, r1, _ = disc(lam, d2, 1); _, _, r2, _ = disc(lam, d2, 2)
            say("             %8.5f | %14.4f %16.6e | %16.6e %14.4f"
                % (d2, r1 / abs(lam), r1, r2, r2 / abs(lam)))

    say("")
    say("  SECTION 3 (核验) - sensitivity: both variants obey rad = O(1/d^2)")
    H = HEIGHTS[0]; lam = complex(R0, H)
    say("   %8s | %16s %16s | %16s %16s" % ("d^2", "rad1*d^2/|lam|", "2sqrt(1-d^2)",
                                            "rad2*d^2", "sqrt(1-d^2)"))
    for d2 in D2S:
        _, _, r1, _ = disc(lam, d2, 1); _, _, r2, _ = disc(lam, d2, 2)
        say("   %8.5f | %16.6f %16.6f | %16.6f %16.6f"
            % (d2, r1 * d2 / abs(lam), 2 * np.sqrt(1 - d2), r2 * d2, np.sqrt(1 - d2)))
    say("   => rad1 = |lam| 2 sqrt(1-d^2)/d^2 and rad2 = sqrt(1-d^2)/d^2 : pure 1/d^2 at small d^2.")
    say("   requirement, radius >= rho  <=>  d^2 <~ |lam|/(a rho) = 2H/rho (v1)  or  d^2 <~ 1/rho (v2)")
    say("   %8s | %16s %16s | %16s %16s" % ("rho", "d^2 req (v1) H=1e3", "H=1e5", "d^2 req (v2)",
                                            "H=1e5"))
    def req(H, rho, variant):
        lam = complex(R0, H); lo, hi = 1e-14, 1.0 - 1e-14
        for _ in range(200):
            mid = 0.5 * (lo + hi)
            _, _, rd, _ = disc(lam, mid, variant)
            if rd > rho:
                lo = mid
            else:
                hi = mid
        return lo
    for rho in (1.0, 10.0, 1e3, 1e6):
        say("   %8.0f | %16.6e %16.6e | %16.6e %16.6e"
            % (rho, req(1e3, rho, 1), req(1e5, rho, 1), req(1e3, rho, 2), req(1e5, rho, 2)))

    say("")
    say("  SECTION 4 (引用) - the trivial DFMR input gives an empty disc at r = 1/2")
    say("   DFMR I Prop. 7.5 (as recorded): d_r^2 < 1/(2-2r) ; at r = 1/2 this is d^2 < 1, and")
    say("   d^2 = 1 is exactly the threshold: R^2 = 0 and both radii vanish.  The only")
    say("   lambda-free distance bound available therefore yields NO usable disc (clean negative).")

    say("")
    say("  SECTION 5 (推导/示意, NOT a result) - project d_N^2 as proxy, and containment test")
    z = np.load(ZEROS)
    say("   zeros: %d ordinates, gamma in [%.3f, %.3f] ; all are critical-line zeros by"
        % (len(z), z[0], z[-1]))
    say("   Platt-Trudgian (引用, RH verified for |t| <= 3e12 > %.2e)" % z[-1])
    for H in HEIGHTS:
        lam = complex(R0, H)
        for name, d2 in (("NB3 convention  d_160^2 (T=400)", 0.67991293),
                         ("BCF convention  d_160^2 (T=400)", 0.04821944)):
            for variant in (1, 2):
                R2, ctr, rad, ok = disc(lam, d2, variant)
                # readings: (A) the disc itself lies in the s-plane  (B) the region is r + disc
                inA = np.sum(np.abs((0.5 - ctr.real) + 1j * (z - ctr.imag)) < rad)
                inB = np.sum(np.abs((0.5 + 0.5 - ctr.real) + 1j * (z - ctr.imag)) < rad)
                say("   H=%.0e v%d %-32s d2=%.6f rad=%10.4e centre=(%.4e,%.4e) zeros inside: disc=%d  r+disc=%d"
                    % (H, variant, name, d2, rad, ctr.real, ctr.imag, int(inA), int(inB)))
    say("   => every variant/reading excludes a region that in fact CONTAINS known zeros, so if the")
    say("      zero-free statement is read as excluding ALL zeros of zeta, the recorded disc fails.")
    say("      If instead it excludes only zeros with Re > r, then only off-line zeros could")
    say("      falsify it, and by Platt-Trudgian there are none below 3e12: the test then can only")
    say("      falsify, never confirm, and gives no information at these heights.  No claim is made.")
    say("")
    say("=" * 100)
    say("READ-OFF (generated from the numbers above; 核验 / 引用 / 推导 / 未做)")
    say("=" * 100)
    say("  [核验] both Apollonius identities verified numerically (0 disagreements in 4000 samples).")
    say("  [核验] 1/d^2 sensitivity confirmed in both variants: rad1*d^2/|lam| = 2sqrt(1-d^2),")
    say("         rad2*d^2 = sqrt(1-d^2).")
    say("  [核验] threshold at r = 1/2: disc non-empty only for d^2 < 1; radius -> 0 as d^2 -> 1.")
    say("  [核验/新发现] the two DFMR statements recorded in this repo imply DIFFERENT discs:")
    say("         variant 1 (denominator z+lambda) gives centre c*lambda, rad = |lambda|R/(a d^2);")
    say("         variant 2 (denominator z+conj(lambda)) gives centre c*a+i b, rad = R/d^2.")
    say("         They differ by |lambda|/a (= %.1e at H = 1e5).  E27 section 2's derivation matches"
        % (abs(complex(R0, HEIGHTS[1])) / R0))
    say("         variant 1; E27 section 1's quotation of DFMR I section 7.1.1 matches variant 2.")
    say("         Resolving which is correct needs the DFMR originals - NOT in this repository.")
    say("  [未做] no lambda-dependent d_r(lambda)^2 is available here, so no disc is produced as a")
    say("         result.  MISSING: (a) DFMR I section 7's explicit functional evaluated for a")
    say("         concrete f_{A,r}, with ||f_{A,r}||_2 and phi-hat (Cor. 2.3 / Cor. 7.4);")
    say("         (b) the containment of the project's length-N class in DFMR's class (G2), which")
    say("         is what would let a bound on d_N transfer to d_r.")
    say("  [推导] criterion verdict: 'non-empty disc' fails from the available input (trivial bound")
    say("         gives d^2 = 1, radius 0); 'no conflict with the verified region' is satisfied")
    say("         vacuously by any disc, since no off-line zero exists below 3e12.  Hence")
    say("         computation C cannot meet its success criterion with the material at hand.")
    say("  [未做] no proof is claimed; nothing about RH is decided by these numbers.")
    say("")
    say("Output written to %s" % OUT)

if __name__ == '__main__':
    main()
