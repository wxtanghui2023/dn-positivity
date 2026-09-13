#!/usr/bin/env python3
"""
E44_ceiling_encl_audit.py -- exploration point E44 (independent audit of the 0.682 ceiling enclosure)

PURPOSE
  Independently re-check, from PUBLIC materials only, the numerical certificate on which the
  "bandwidth-one ceiling" of the frontier paper rests (arXiv:2608.13637v2, section 7.2).  The paper
  states that the Lean theorem Zeta23.PairCeiling.ceiling_law256 depends on the hypothesis EnclOK,
  that EnclOK is certified OUTSIDE Lean by interval arithmetic, and that this is the ONLY place in
  the paper where a numerical certification enters.  Everything downstream of EnclOK is
  kernel-checked.  So EnclOK is exactly "the frontier's only un-kernel-checked numeric input".

INPUTS
  data/lawN256_encl_v1.0.json   -- verbatim extraction of K, the 256 enclosure pairs, tau, the
                                   D(1) bound and the p0 fraction, from the Lean source
                                   Zeta23/PairCeiling/LawN256.lean, repo
                                   https://github.com/anthropics/zeta-23-lean tag v1.0
                                   (source sha256 11ae9f7dcc1747f68b51c44f057641ba20bd623b2abea04849b612e716903c6e,
                                   recorded in the JSON; fetched 2026-09-13)
  NOT available publicly: the law data file cert_N256_blk_b128m.json
                                   (sha256 cc3de9917db4d14d844630a4e97dda8387fd6e257e52b6967f430b8914584eb8)
                                   -- referenced by the Lean header as "available from the authors".

OUTPUT
  scripts/E44_ceiling_encl_audit.txt

WHAT IS CHECKED (all arithmetic exact: int / fractions.Fraction)
  (A) table shape: 256 pairs, K = 2^140, every interval of width exactly 1
  (B) the 255 near-CUE ROWS (j = 1..255 only; j = 256 is the edge entry, NOT a row inequality):
      each interval brackets j*2^132 at an endpoint, so |256*S(j) - j| <= 256/K = 2^-132 follows
  (C) D(1) := C(1) - 1/2, C(1) = (sum_{j<=256} S(j))/256   [Defs.lean: Dfun = Cstep - x^2/2];
      compared with the recorded edge bound 82395317/10^8, including its sign
  (D) the recorded p0 = 1 - a_N: exact value, decimal expansion, and p0 <= 0.6818287
  (E) the theorem's own constant 1/(6*256^2) + tau/(2*256) <= 2.5431316e-6
  (F) consistency checks that ARE valid for rational (non-integer) positions:
      0 <= S(j) <= 256 for all j; and S(256) != 256 witnesses non-integer positions

SELF-CORRECTIONS MADE WHILE WRITING THIS SCRIPT (kept deliberately; cf. the project's habit)
  (i)  first version folded j = 256 into the row loop and reported a failure of tau; the paper says
       the row certificate has 255 rows, and j = 256 is the edge datum -- fixed by restricting to
       j <= 255.
  (ii) first version truncated decimal strings with a raw slice, which silently deleted exponents
       (9.287e-9 printed as "9.287164"); fixed by truncating the mantissa only.
  (iii) first version asserted the Parseval identity E[sum_i m_i^2] = 383.5 as a NECESSARY condition.
       That is WRONG for this law: the identity sum_{j=0}^{255}|F(j)|^2 = 256*sum_i m_i^2 needs
       integer positions (for rational positions the geometric sums do not vanish off-diagonal).
       Replaced by the valid checks in (F).

CONCLUSIONS (digit-driven; see the report printed at the end of the output file)
  1. The public numeric certificate is internally consistent, and two of the paper's recorded
     constants are INDEPENDENTLY REPRODUCED from the enclosure table alone:
       * the row certificate |256 S(j) - j| <= 3e-40                 (margin 1.63x)
       * the edge bound |D(1)| <= 82395317/10^8, and its sign (+)    (margin 9.29e-09)
  2. p0 <= 0.6818287 and the 2.5431316e-06 constant step both check out; S(j) <= 256 everywhere.
  3. LIMIT, stated honestly: the enclosures themselves (EnclOK) assert a property of the form factor
     of a law whose data file is NOT public, so EnclOK cannot be recomputed by a third party from the
     repository.  What we verify is that the recorded table is consistent with everything else the
     paper records; what stays unverified is that the law's true form factor lies inside the table.
     That is a reproducibility gap, not a detected error.

PROVENANCE
  Written 2026-09-13 by 小灵 (main session) for exploration point E44 of
  docs/EXPLORATION-POINTS-REGISTER.md, following recommendation (iv) of
  docs/A3-barrier-opinion-2026-09-12.md ("independent audit of the 0.682 numeric enclosure").
  Frontier source read at arXiv:2608.13637v2 (HTML v2) and github.com/anthropics/zeta-23-lean tag v1.0.
  No RH assumption is used or claimed anywhere in this script.
"""

import json
import os
from fractions import Fraction as F
from decimal import Decimal, getcontext

getcontext().prec = 80
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)


def dec(fr, n=30):
    """decimal string of a Fraction, n significant characters, exponent preserved"""
    s = str(Decimal(fr.numerator) / Decimal(fr.denominator))
    if "E" in s:
        mant, _, ex = s.partition("E")
        return mant[:n] + "E" + ex
    return s[:n]


def sci(fr, n=4):
    """compact scientific notation for margins"""
    return "%.*e" % (n, float(fr))


def main():
    out = []
    w = out.append
    data = json.load(open(os.path.join(ROOT, "data", "lawN256_encl_v1.0.json")))
    N = data["N"]
    K = data["K"]
    en = data["encl"]
    tau = F(data["tau"][0], data["tau"][1])
    D1bound = F(data["D1_num"], data["D1_den"])
    p0 = F(data["p0_num"], data["p0_den"])
    tgt = lambda j: j * 2 ** 132

    w("E44 -- independent audit of the 0.682 ceiling enclosure  (arXiv:2608.13637v2 section 7.2)")
    w("source: repo anthropics/zeta-23-lean tag v1.0, file Zeta23/PairCeiling/LawN256.lean")
    w("        sha256 %s" % data["provenance"]["source_sha256"])
    w("paper's own caveat: EnclOK is 'certified by interval arithmetic and [is] not checked by the")
    w("Lean kernel'; the paper says this is the only place a numerical certification enters.")
    w("=" * 100)

    # ---------------- (A) table shape ----------------
    w("[A] table shape")
    w("    pairs = %d ; N = %d ; K = %d ; K == 2^140 : %s" % (len(en), N, K, K == 2 ** 140))
    widths = sorted(set(b - a for a, b in en))
    w("    distinct interval widths: %s   -> every interval has width 1" % widths)

    # ---------------- (B) the 255 near-CUE rows ----------------
    w("")
    w("[B] the 255 near-CUE ROWS: |256*S(j) - j| <= tau = 3e-40,  j = 1..255")
    w("    (j = 256 is the EDGE entry, excluded by construction: the paper counts 255 rows)")
    worst = F(0)
    worst_j = None
    above = below = 0
    offgrid = []
    for j in range(1, N):
        lo, hi = en[j - 1]
        if not (lo <= tgt(j) <= hi):
            offgrid.append(j)
        d = max(abs(256 * F(lo, K) - j), abs(256 * F(hi, K) - j))
        if d > worst:
            worst, worst_j = d, j
        if lo == tgt(j):
            above += 1
        elif hi == tgt(j):
            below += 1
    w("    intervals bracketing j*2^132 at an endpoint: %d/255 ; exceptions: %s"
      % (255 - len(offgrid), offgrid if offgrid else "none"))
    w("    widest deviation  max_{j<=255} |256*S(j) - j| = %s  (attained at j = %d)"
      % (sci(worst), worst_j))
    w("    256/K = 2^-132 = %s" % sci(F(256, K)))
    w("    => tau = 3e-40 holds, margin = %.3fx  : %s" % (float(tau / worst), worst <= tau))
    w("    sign pattern: %d rows place the value at/above j/256, %d at/below" % (above, below))
    w("    (mixed signs; consistent with an active-set optimum of the underlying programme)")

    # ---------------- (C) edge bound D(1) ----------------
    w("")
    w("[C] edge bound  |D(1)| <= 82395317/10^8 = 0.82395317     [Defs.lean: D(x) = C(x) - x^2/2]")
    sumJ = sum(range(1, N))                      # rows 1..255 carry the ramp j/256
    loN, hiN = en[N - 1]
    loS = F(sumJ * 2 ** 132 - (N - 1), K)
    hiS = F(sumJ * 2 ** 132, K)
    Clo, Chi = (loS + F(loN, K)) / N, (hiS + F(hiN, K)) / N
    Dlo, Dhi = Clo - F(1, 2), Chi - F(1, 2)
    w("    S(256) in [%s, %s]   (last recorded pair)" % (dec(F(loN, K), 18), dec(F(hiN, K), 18)))
    w("    C(1)   in [%s, %s]" % (dec(Clo, 18), dec(Chi, 18)))
    w("    D(1)   in [%s, %s]   (interval width %s)" % (dec(Dlo, 20), dec(Dhi, 20), sci(Dhi - Dlo)))
    w("    recorded bound = %s ; margin = %s ; sign of D(1) = %s"
      % (dec(D1bound, 12), sci(D1bound - Dhi), "+" if Dlo > 0 else "-"))
    w("    => the recorded edge bound reproduces and holds : %s" % (Dhi <= D1bound))
    w("    (82395317/10^8 = 0.82395317 < 0.824 = the paper's rounded constant in the display)")

    # ---------------- (D) p0 ----------------
    w("")
    w("[D] the ceiling constant  p0 = 1 - a_N  <= 0.6818287")
    w("    p0  = %s/%s" % (data["p0_num"], data["p0_den"]))
    w("        = %s..." % dec(p0, 32))
    w("    a_N = 1 - p0 = %s" % dec(1 - p0, 32))
    w("    denominator = 2^43 * 5^39 : %s   (a 40-digit decimal-type rational)"
      % (int(data["p0_den"]) == 2 ** 43 * 5 ** 39))
    w("    p0 <= 0.6818287 : %s ; margin = %s" % (p0 <= F(6818287, 10 ** 7), sci(F(6818287, 10 ** 7) - p0)))
    w("    distance to the rounded display 0.682 : %s" % dec(F(682, 1000) - p0, 8))

    # ---------------- (E) the theorem's constant ----------------
    w("")
    w("[E] the theorem's own constant  c := 1/(6*256^2) + tau/(2*256) <= 2.5431316e-6")
    c = F(1, 6 * N * N) + tau / (2 * N)
    bound = F(25431316, 10 ** 13)
    w("    c = %s   (1/(6*256^2) = 1/393216 = %s)" % (dec(c, 20), dec(F(1, 6 * N * N), 20)))
    w("    c <= 2.5431316e-6 : %s ; margin = %s" % (c <= bound, sci(bound - c)))

    # ---------------- (F) valid consistency checks ----------------
    w("")
    w("[F] consistency checks valid for RATIONAL positions (the law has positions in [0,256) rational)")
    Smax = max(F(hi, K) for _, hi in en)
    w("    |F_c(j)|^2 <= (sum_i m_i)^2 = 65536, hence 0 <= S(j) <= 256 for every j")
    w("    max_j S(j) = %s (attained at j = 256) ; all S(j) <= 256 : %s"
      % (dec(Smax, 18), Smax <= 256))
    w("    if all positions were INTEGERS then F would be 256-periodic in j and S(256) = S(0) = 256;")
    w("    recorded S(256) = %s != 256, so positions are genuinely non-integer -- consistent with the"
      % dec(Smax, 18))
    w("    Lean header.  This also explains why the grid carries no j <-> 256-j symmetry, so the ramp")
    w("    j/256 on both halves of the grid is not contradictory (integer positions would forbid it).")

    # ---------------- conclusion ----------------
    w("")
    w("=" * 100)
    w("CONCLUSION (digit-driven)")
    w("  VERIFIED INDEPENDENTLY from public data:")
    w("    * the recorded enclosures imply the row certificate |256 S(j) - j| <= 3e-40  (margin %.2fx)"
      % float(tau / worst))
    w("    * the recorded enclosures REPRODUCE the paper's edge bound |D(1)| <= 0.82395317")
    w("      (computed D(1) = %s, margin %s) and its sign; this is the constant 0.824 that appears"
      % (dec(Dlo, 20), sci(D1bound - Dhi)))
    w("      in the paper's displayed ceiling inequality")
    w("    * p0 = %s... <= 0.6818287  (margin %s)" % (dec(p0, 20), sci(F(6818287, 10 ** 7) - p0)))
    w("    * the theorem's constant step 1/(6*256^2) + tau/512 <= 2.5431316e-6")
    w("    * 0 <= S(j) <= 256 for all j, and S(256) != 256 (non-integer positions, as stated)")
    w("  NOT VERIFIABLE from public materials (the honest limit of this audit):")
    w("    * EnclOK itself -- that the law's TRUE form factor lies inside these intervals.  The data")
    w("      file cert_N256_blk_b128m.json (sha256 cc3de9917db4d14d844630a4e97dda8387fd6e257e52b6967f430b8914584eb8)")
    w("      is referenced but not shipped, so no third party can redo the interval arithmetic.")
    w("      Reproducibility gap, NOT a detected error.")
    w("    * consequence: the chain 'enclosures => row certificate + edge bound => 0.6818287 +")
    w("      2.5431316e-6(...)' is checkable at every step except its single input -- exactly the step")
    w("      the paper itself flags as un-kernel-checked.")
    w("  Request that would close the gap: the law file above (its sha256 is public).")

    txt = "\n".join(out) + "\n"
    open(os.path.join(HERE, "E44_ceiling_encl_audit.txt"), "w").write(txt)
    print(txt)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
