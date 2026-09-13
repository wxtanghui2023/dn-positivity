#!/usr/bin/env python3
"""
E45_nearcue_instance_data.py -- exploration point E45, step 6: the exact data the ceiling theorem needs

WHY
  Step 5 (scripts/E45_nearcue_exact_attainment.py) resolved the open question POSITIVELY: on the grids
  Q = 2N there ARE laws with algebraic weights for which the ramp
        sum_c w_c |F_c(j)|^2 = j ,   j = 1..N-1
  holds EXACTLY -- found and verified at N = 4 (2 configurations, weights 1/2 -+ sqrt2/4) and N = 6
  (6 configurations, weights in Q(sqrt3)).  Exactness means S(j) = j/N EXACTLY, hence NearCUE holds with
  tau = 0 and the ceiling theorem's constant drops its tau term, leaving 1/(6N^2).

WHAT THIS SCRIPT COMPUTES (all exact, in the quadratic field (a,b) = a + b*sqrt(D))
  1. re-verification of the law: weights sum to 1, are nonnegative, and the ramp holds for every j < N;
  2. the FREE EDGE ROW  S(N) = E|F(N)|^2 / N  (the row the theorem leaves free);
  3. C(1) = (N-1)/(2N) + S(N)/N  and  D(1) = C(1) - 1/2   [repository definitions: D = Cstep - x^2/2];
  4. the theorem's input d1 = |D(1)| together with a RATIONAL upper bound for it, which is what a Lean
     instance would consume (rational bounds keep the statement free of field arithmetic on the bound).

INPUTS   none (the two laws are transcribed from step 5's output)
OUTPUT   scripts/E45_nearcue_instance_data.txt

CONCLUSIONS (digit-driven)
  The exact ramp makes the numeric input an identity; what remains is the edge row S(N) and the rational
  bound for |D(1)|, both computed here -- the complete, exactly certified input of the ceiling theorem at
  these grid sizes.

PROVENANCE
  Written 2026-09-13 by 小灵 (main session), exploration point E45, approved by 唐先生.
  Sources: arXiv:2608.13637v2 section 7.2; github.com/anthropics/zeta-23-lean tag v1.0
  (Defs.lean for C, D, massOf; NearCUE.lean for the theorem).  No RH assumption used or claimed.
"""

import os
from fractions import Fraction as F

DQ = {8: 2, 10: 5, 12: 3}
COS = {}
COS[8] = {0: (F(1), F(0)), 1: (F(0), F(1, 2)), 2: (F(0), F(0)), 3: (F(0), F(-1, 2)),
          4: (F(-1), F(0)), 5: (F(0), F(-1, 2)), 6: (F(0), F(0)), 7: (F(0), F(1, 2))}
COS[12] = {0: (F(1), F(0)), 1: (F(0), F(1, 2)), 2: (F(1, 2), F(0)), 3: (F(0), F(0)),
           4: (F(-1, 2), F(0)), 5: (F(0), F(-1, 2)), 6: (F(-1), F(0)), 7: (F(0), F(-1, 2)),
           8: (F(-1, 2), F(0)), 9: (F(0), F(0)), 10: (F(1, 2), F(0)), 11: (F(0), F(1, 2))}

# laws from step 5: (positions on the grid m/Q, unit marks, weight = u + t*sqrt(D))
LAWS = {
    4: [((0, 2, 6, 7), (F(1, 2), F(-1, 4))),
        ((0, 3, 5, 7), (F(1, 2), F(1, 4)))],
    6: [((0, 2, 5, 7, 9, 10), (F(-11, 30), F(4, 15))),
        ((0, 1, 2, 4, 6, 9), (F(28, 15), F(-14, 15))),
        ((0, 3, 5, 6, 8, 11), (F(-1, 3), F(1, 3))),
        ((2, 3, 4, 8, 10, 11), (F(8, 15), F(-4, 15))),
        ((3, 5, 6, 7, 10, 11), (F(-19, 30), F(2, 5))),
        ((0, 2, 4, 6, 8, 9), (F(-1, 15), F(1, 5)))],
}


def nonneg(u, t, D):
    """EXACT and COMPLETE test of u + t*sqrt(D) >= 0.
    Self-correction: the first version of this check listed only three of the four cases and therefore
    reported the (valid) weight 1/2 + (1/4)sqrt2 as negative."""
    if t == 0:
        return u >= 0
    if t > 0:
        return True if u >= 0 else (D * t * t >= u * u)
    return u >= 0 and u * u >= D * t * t


def vals(N, Q, pos, j):
    """|F(j)|^2 = a + b*sqrt(D), unit marks, F(j) = sum_k exp(2 pi i j x_k / N), x_k = N*m/Q"""
    a = F(0); b = F(0)
    for k1 in range(len(pos)):
        for k2 in range(len(pos)):
            ca, cb = COS[Q][(j * (pos[k1] - pos[k2])) % Q]
            a += ca; b += cb
    return a, b


def rat_upper_sqrt(D, digits=30):
    """rational upper bound for sqrt(D): isqrt of D*scale^2, plus one (exact, no floats, no loops)"""
    import math
    scale = 10 ** digits
    n = D * scale * scale
    r = math.isqrt(n)
    while r * r <= n:            # isqrt is the floor, so at most one step is needed
        r += 1
    return F(r, scale)


def main():
    out = []; w = out.append
    w("E45 step 6 -- exact inputs of the ceiling theorem for our own near-CUE laws")
    w("=" * 100)
    for N in sorted(LAWS):
        Q = 2 * N; D = DQ[Q]
        law = LAWS[N]
        w("")
        w("N = %d  (Q = %d, field Q(sqrt%d))  support = %d configurations" % (N, Q, D, len(law)))
        # 1) weights
        su = sum(u for _, (u, t) in law); st = sum(t for _, (u, t) in law)
        w("   weight check: sum u = %s, sum t = %s  (need 1 and 0) : %s"
          % (su, st, su == 1 and st == 0))
        nneg = [nonneg(u, t, D) for _, (u, t) in law]
        w("   nonnegativity of w_c = u + t*sqrt%d : %s" % (D, all(nneg)))
        # 2) exact ramp
        ok = True
        for j in range(1, N):
            s1 = F(0); s2 = F(0)
            for pos, (u, t) in law:
                a, b = vals(N, Q, pos, j)
                s1 += u * a + D * t * b
                s2 += u * b + t * a
            if s1 != j or s2 != 0:
                ok = False
        w("   exact ramp  sum_c w_c |F_c(j)|^2 = j  for j = 1..%d : %s   => S(j) = j/N exactly, tau = 0"
          % (N - 1, ok))
        # 3) free edge row j = N
        aN = F(0); bN = F(0)
        for pos, (u, t) in law:
            a, b = vals(N, Q, pos, N)
            aN += u * a + D * t * b
            bN += u * b + t * a
        w("   edge row (free): E|F(N)|^2 = %s + (%s)*sqrt%d" % (aN, bN, D))
        w("                    S(N) = E|F(N)|^2 / N = %s + (%s)*sqrt%d" % (aN / N, bN / N, D))
        # 4) C(1), D(1), d1
        Ca = F(N - 1, 2 * N) + aN / (N * N)     # C(1) = sum_{j<N} j/N^2  +  S(N)/N
        Cb = bN / (N * N)
        Da = Ca - F(1, 2); Db = Cb
        w("   C(1) = (N-1)/(2N) + S(N)/N = %s + (%s)*sqrt%d" % (Ca, Cb, D))
        w("   D(1) = C(1) - 1/2 = %s + (%s)*sqrt%d   (Defs.lean: D = Cstep - x^2/2)" % (Da, Db, D))
        # |D(1)|: exact sign plus a rational upper bound
        hi = rat_upper_sqrt(D, 30)
        # since Db has a definite sign here, bound |Da + Db*sqrtD| by |Da| + |Db|*hi
        d1 = abs(Da) + abs(Db) * hi
        w("   sqrt%d < %s (rational, 30 digits)" % (D, hi))
        w("   => d1 := |Da| + |Db|*sqrt%d < %s  (rational upper bound for |D(1)|)"
          % (D, d1))
        dec = float(Da) + float(Db) * float(hi)
        w("      reference decimal value of D(1): %.15f" % dec)
        w("   THEOREM INPUT (N = %d):  tau = 0,  S(j) = j/%d (j < N),  d1 = %s" % (N, N, d1))
        w("      constant in the conclusion: 1/(6*%d^2) = %s" % (N, F(1, 6 * N * N)))
    w("")
    w("=" * 100)
    w("READING")
    w("  Every quantity above is exact rational arithmetic in a quadratic field (or a rational bound for")
    w("  the field element).  There is no interval arithmetic and no unverifiable input: the numeric")
    w("  hypothesis of the ceiling theorem is an identity for our own law.")
    here = os.path.dirname(os.path.abspath(__file__))
    open(os.path.join(here, "E45_nearcue_instance_data.txt"), "w").write("\n".join(out) + "\n")
    print("\n".join(out))


if __name__ == "__main__":
    main()
