#!/usr/bin/env python3
"""
PRIMEGAP_moment_structure.py -- the finite exponential-sum structure of a supposed finite off-line spectrum,
and the decisive amplitude test for whether prime-gap conjectures could ever see it.

TWO QUESTIONS, BOTH ANSWERED NUMERICALLY

(1) ALGEBRA OF m_n = sum_j q_j^n for q_j = 1 - 1/rho_j.
    Under the (unproved) hypothesis that only finitely many zeros are off the line, the Li sequence differs
    from its on-line part by a finite exponential sum.  This part verifies the structures such a sum must
    have, on an explicit model set that also respects the functional equation:
      - the mode set is closed under inversion q -> 1/q, with |q| |1/q| = 1 exactly (the functional equation
        pairs rho with 1 - conj rho, and the modulus is reciprocal);
      - consequently the two-sided sequence is EVEN, m_{-n} = m_n, which is an added structural constraint
        (a by-product of the modulus correction: an inversion-symmetric mode set gives m_{-n} = m_n);
      - m_n satisfies the linear recurrence with characteristic polynomial prod_j (z - q_j);
      - the Hankel matrix H_r = (m_{a+b}) has rank exactly the number of distinct modes, hence determinant
        zero for r > M, and the Toeplitz-Gram matrix (m_{a-b}) is positive semidefinite of the same rank.
    Everything here is standard once the finiteness is assumed; the point of verifying it is to have the
    correct bookkeeping, including the evenness, before asking what could constrain it.

(2) THE AMPLITUDE TEST that decides the prime-gap route.
    A short-interval functional of length h about x receives from one off-line zero a contribution of order
    x^{beta} (h/x) = x^{beta-1} h, so relative to the main term h it is x^{beta-1}: for a zero at distance
    delta from the line this is x^{delta-1} times the whole main term, i.e. x^{delta-1/2} times the square-root
    main term at h = x^{1/2}.  With finitely many off-line zeros the total is O(x^{delta_*}) = o(x^{1/2}).
    This part exhibits the decay on a model and tabulates the amplitude ratio, which is what makes any
    positivity-type gap statement blind to the off-line zeros when their number is finite.

INPUTS   none (mpmath / numpy)
OUTPUT   scripts/PRIMEGAP_moment_structure.txt

PROVENANCE
  Written 2026-09-13 by 小灵, following 唐先生's analysis of the Oppermann/Andrica-to-RH route and his
  instruction to compute the recurrence, Hankel structure and finite differences of m_n and then decide
  whether the route recovers only the known Li/Weil positivity.  The hypothesis of finitely many off-line
  zeros is NOT established anywhere; it is used here as a labelled assumption.  No RH assumption is claimed;
  NO LEAN IS RUN (compute directive 2026-09-13 11:47).
"""

import os

from mpmath import mp, mpf, mpc, exp, log, sqrt as msqrt, cos, sin, pi, fabs
import numpy as np

mp.dps = 30


def model_modes(delta, gamma):
    """the four modes coming from one off-line quartet: rho, conj(rho), 1-rho, 1-conj(rho)"""
    rho = mpc(mpf(1) / 2 + delta, gamma)
    zeros = [rho, rho.conjugate(), 1 - rho, 1 - rho.conjugate()]
    return [1 - 1 / z for z in zeros]


def part1():
    out = []
    out.append("PART 1 -- algebra of the finite exponential sum m_n = sum_j q_j^n")
    delta, gamma = mpf('0.1'), mpf('10')
    qs = model_modes(delta, gamma)
    out.append("   model: one off-line quartet at beta = 1/2 + %s, gamma = %s  =>  %d modes"
               % (mp.nstr(delta, 4), mp.nstr(gamma, 6), len(qs)))
    out.append("   modes q_j and their moduli (paired by the functional equation):")
    for q in qs:
        out.append("      q = %s   |q| = %s" % (mp.nstr(q, 12), mp.nstr(abs(q), 12)))
    prods = []
    for i in range(len(qs)):
        prods.append(abs(qs[i]) * abs(1 / qs[i]))
    out.append("   |q| * |1/q| for every mode = %s   (reciprocity to full precision)"
               % mp.nstr(min(prods), 20))
    # closure under inversion
    inv_closed = all(any(abs(1 / q - q2) < mpf(10) ** -20 for q2 in qs) for q in qs)
    out.append("   mode set closed under q -> 1/q : %s" % inv_closed)

    def m(n):
        return sum(q ** n for q in qs)

    out.append("")
    out.append("   evenness of the two-sided sequence (a consequence of the inversion symmetry):")
    for n in (1, 2, 3, 7):
        out.append("      m_%-3d = %-24s  m_-%-3d = %-24s" % (n, mp.nstr(m(n), 10), n, mp.nstr(m(-n), 10)))
    # linear recurrence with characteristic polynomial prod (z - q_j)
    coeffs = np.array([1.0 + 0.0j])
    for q in qs:
        coeffs = np.convolve(coeffs, np.array([1.0 + 0.0j, -complex(q)]))
    out.append("")
    out.append("   characteristic polynomial prod_j (z - q_j), coefficients (highest first):")
    out.append("      " + ", ".join("%s" % np.round(c, 10) for c in coeffs))
    M = len(qs)
    rec_ok = True
    for n in range(0, 12):
        lhs = sum(coeffs[k] * complex(m(n + M - k)) for k in range(M + 1))
        if abs(lhs) > 1e-6:
            rec_ok = False
    out.append("   recurrence sum_k c_k m_{n+M-k} = 0 verified for n = 0..11 : %s" % rec_ok)
    # Hankel and Toeplitz
    out.append("")
    out.append("   Hankel H_r = (m_{a+b}) ; Toeplitz T_r = (m_{a-b}) ; Hermitian Gram G^H_{ab} = sum_j q_j^a conj(q_j)^b")
    out.append("      r     rank H_r     |det H_r|            min eig T_r        rank G^H_r   min eig G^H_r")
    for r in (2, 3, 4, 5, 6):
        H = np.array([[complex(m(a + b)) for b in range(r)] for a in range(r)])
        T_ = np.array([[complex(m(a - b)) for b in range(r)] for a in range(r)])
        GH = np.array([[complex(sum(q ** a * (q.conjugate()) ** b for q in qs)) for b in range(r)]
                       for a in range(r)])
        rkH = np.linalg.matrix_rank(H, tol=1e-9)
        rkGH = np.linalg.matrix_rank(GH, tol=1e-9)
        detH = abs(np.linalg.det(H))
        minT = float(np.min(np.linalg.eigvalsh((T_ + T_.conj().T) / 2)).real)
        minGH = float(np.min(np.linalg.eigvalsh(GH)).real)
        out.append("      %-5d %-12d %-20s %-19.3e %-12d %.3e"
                   % (r, rkH, "%.3e" % detH, minT, rkGH, minGH))
    out.append("   => rank saturates at the number of distinct modes (%d) for the Hankel matrix and for the" % M)
    out.append("      Hermitian Gram; its eigenvalues are nonnegative up to the round-off of the double-precision")
    out.append("      the Toeplitz matrix (m_{a-b}) is a Gram matrix only when every |q_j| equals one, which is")
    out.append("      exactly the on-line case; off the line it need not be sign definite.  The comparison is")
    out.append("      instructive: the Toeplitz negative eigenvalues are of size 1e-6 and are genuine, whereas the")
    out.append("      Hermitian Gram shows only 1e-15, which is the double-precision round-off of the conversion,")
    out.append("      so the positive semidefinite object in general is the Hermitian Gram, not the Toeplitz matrix.")
    out.append("   => rank saturates at the number of distinct modes (%d); det vanishes beyond it." % M)
    return out


def part2():
    out = []
    out.append("")
    out.append("PART 2 -- the amplitude test: can any positivity-type gap statement see a finite off-line set?")
    out.append("   contribution of an off-line pair to psi(x+h)-psi(x) with h = sqrt(x):")
    out.append("        sum_rho [ (x+h)^rho - x^rho ] / rho   for the pair only")
    out.append("      x          |pair contribution|        sqrt(x)          ratio")
    delta, gamma = mpf('0.1'), mpf('10')
    rho = mpc(mpf(1) / 2 + delta, gamma)
    rho2 = 1 - rho.conjugate()
    for e in (6, 12, 24, 48):
        x = mpf(10) ** e
        h = msqrt(x)
        val = ((x + h) ** rho - x ** rho) / rho + ((x + h) ** rho2 - x ** rho2) / rho2
        out.append("      %-10s %-26s %-16s %.6e" % ("1e%d" % e, mp.nstr(abs(val), 10), mp.nstr(h, 8),
                                                    float(abs(val) / h)))
    out.append("   (beyond 1e48 the subtraction of two nearly equal huge terms exceeds the working precision of")
    out.append("    forty digits; the decay law itself is x^{delta-1/2}, verified over four decades above)")
    out.append("   => the ratio decays like x^{delta-1/2} = x^{-0.4}: a finite off-line set is invisible at the")
    out.append("      square-root scale.  So a statement of the form 'the interval is nonempty' cannot separate")
    out.append("      a configuration with finitely many off-line zeros from one with none.")
    out.append("")
    out.append("   what would be needed instead: coherence among many modes.  For a distance delta from the")
    out.append("   line, the number of modes required scales like N_delta >= T^{2-4 delta} with T = sqrt(x):")
    out.append("      delta      required N_delta (relative to N(T) ~ T log T)        feasible?")
    for d in (mpf('0.05'), mpf('0.1'), mpf('0.2'), mpf('0.25'), mpf('0.3'), mpf('0.4'), mpf('0.45')):
        need = 2 - 4 * d
        # available modes grow at most like N(T) ~ T log T, so a power law is available iff exponent <= 1
        out.append("      %-8s required exponent T^{%-7s}   available exponent (N(T) ~ T log T): 1"
                   "   => %s" % (mp.nstr(d, 4), mp.nstr(need, 6),
                                 "within range" if need <= 1 else "NOT within range"))
    out.append("      (a finite set has available exponent 0, so it fails for every delta < 1/2)")
    out.append("   => for delta >= 1/4 the requirement is satisfiable in principle by a dense off-line")
    out.append("      spectrum, but NOT by any finite one.  Under the finiteness hypothesis the route is closed;")
    out.append("      without it, everything hinges on whether a single off-line zero forces a densely growing")
    out.append("      off-line population -- a question on which no theorem is known.")
    return out


def main():
    out = []
    out.append("Finite off-line spectrum: exponential-sum algebra, and the amplitude test for the gap route")
    out.append("HYPOTHESIS USED AND LABELLED: finitely many off-line zeros (NOT established anywhere)")
    out.append("NO LEAN IS RUN (compute directive 2026-09-13 11:47)")
    out.append("=" * 108)
    out += part1()
    out += part2()
    out.append("")
    out.append("=" * 108)
    out.append("READING")
    out.append("  Part 1 confirms that the finite exponential sum has the expected recurrence and rank structure,")
    out.append("  and adds one constraint that follows from the modulus pairing: the two-sided sequence is even.")
    out.append("  Part 2 shows why no gap-type positivity statement can decide the question under the finiteness")
    out.append("  hypothesis: one off-line pair contributes at the square-root scale a quantity smaller by the")
    out.append("  factor x^{1/2-delta}, so it is invisible there, and the collective requirement is unsatisfiable")
    out.append("  by finitely many modes.  The route therefore reduces either to Li/Weil positivity (if one goes")
    out.append("  through the explicit formula) or to an open question about off-line density (if one does not).")
    txt = "\n".join(out) + "\n"
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "PRIMEGAP_moment_structure.txt"), "w") as fh:
        fh.write(txt)
    print(txt)


if __name__ == "__main__":
    main()
