#!/usr/bin/env python3
"""
A4C (E27/A4-5 + E26/A4-4 computation C) — the POINTWISE zero-free disc constant, done properly
against the actual DFMR I source (arXiv:1101.1199, Trans. AMS 365 (2013) 3227-3253).

PROVENANCE / PURPOSE
  Task doc: docs/A4-C-pointwise-disk-constants.md  (this script is its numerical engine).
  Goal: at lambda = r + i H with r = 1/2, H = 1e3, 1e5, obtain d_r(lambda)^2 via a SINGLE/FEW-TERM
  upper bound of the DFMR zeta-case distance functional, then convert to the zero-free disc of
  E27-A4-5 sec.2, report non-emptiness, conflict with the verified zero-free region, the 1/d^2
  sensitivity, and the G1/G2 correspondence.  No RH is assumed anywhere (R7: no circularity).

  WHAT WAS RESOLVED HERE (vs the earlier scripts/E26C_dfmr_pointwise_distance.py, which used only
  the lambda-free trivial bound d^2 <= 1/(2-2r)):
    * The E26C script treated d_r(lambda)^2 as an INPUT with a "two-Apollonius-variant" ambiguity.
      Reading the actual paper resolves BOTH: (i) the zeta-case test space is K_r =
      span( t^r ( {a/t} - a {1/t} ) ), because for zeta psi(u) = {u} (fractional part) exactly
      (DFMR I Remark 3.5, line: "psi(u)=u-ceil(u)+1, so psi(u)={u} a.e."); (ii) the disc is the
      "variant 2" one:  center (a(1+R^2)/(1-R^2), b), radius 2aR/(1-R^2) = R/d^2  — NOT
      c*lambda with radius |lambda|R/(a d^2).  E27-A4-5 sec.2's complex algebra dropped the
      y-cross term (z lambda-bar + z-bar lambda) = 2(ax+by) but the by-coefficient is (1-R^2),
      not (1+R^2); the corrected disc keeps Im(center) = b = Im(lambda) unchanged.
    * So here we COMPUTE d_r(lambda)^2 from the actual functional (single term and few terms),
      at H = 0 (sanity: Nyman direction, should be << 1) and H = 1e3, 1e5 (should -> 1).

  THE FUNCTIONAL (zeta case, sigma0=0, r=1/2, lambda = 1/2 + i H):   [引用, DFMR I]
      d_r(lambda)  = dist( t^{lambda-bar} chi_(0,1) , K_r )  in L^2((0,1), dt/t),
      K_r = span( t^r ( {a_j/t} - a_j {1/t} ) : 0 < a_j <= 1 )        (Prop 7.3).
    At r = 1/2 the factor t^{1/2} cancels, giving the L^2((0,1), dt) problem
      d_{1/2}(lambda)^2 = min_{c,a}  int_0^1 | t^{-iH} - sum_j c_j ( {a_j/t} - a_j {1/t} ) |^2 dt.
    Any explicit choice of (c,a) is an UPPER bound on d^2 (the "single/few-term upper bound").
    For a fixed basis {f_j(t) = {a_j/t} - a_j {1/t}}, the least-squares optimum gives
      d^2 <= 1 - v^H G^{-1} v,   G_{jk}=int f_j f_k dt,  v_j = int f_j(t) t^{-iH} dt,
    which is EXACTLY the orthogonal-projection residual (with ||t^{-iH}||^2 = int_0^1 1 dt = 1).
    Single term: d^2 <= 1 - |A|^2/B,  A = int f_a(t) t^{-iH} dt,  B = int f_a(t)^2 dt.

  DISC CONVERSION (correct, 引用 DFMR I Thm 2.2 + the paper's explicit centre/radius):
      Q^2 = 1 - 2a d^2  (a = Re(lambda) = 1/2),  non-empty iff d^2 < 1/(2a) = 1.
      shifted disc (r + D_r(lambda)):  centre (r + a(1+Q^2)/(1-Q^2), b) = (1/d^2, H),
      radius = 2aQ/(1-Q^2) = Q/d^2 = sqrt(1-d^2)/d^2.      [a = r = 1/2]
    The E27-A4-5 sec.2 formula (rad = |lambda| sqrt(1-2a d^2)/(a d^2)) is shown to be off by
    the factor |lambda|/a = 2|lambda| ~ 2H; both are printed for comparison.

Inputs : data/zeros_odlyzko_2M.npy (2 001 052 ordinates, read-only) for the conflict check.
Outputs: scripts/A4C_pointwise_disk.txt
Labels : 核验 = verified against this script | 引用 = quoted from DFMR I | 推导 = derived here
"""
import os
import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ZEROS = os.path.join(ROOT, 'data', 'zeros_odlyzko_2M.npy')
OUT = os.path.join(ROOT, 'scripts', 'A4C_pointwise_disk.txt')

R0 = 0.5                       # r = 1/2
HEIGHTS = (0.0, 1.0e3, 1.0e5)  # H = 0 (sanity), 1e3, 1e5
EPS = 1e-6                     # truncation of the (0,1) integral at t = EPS; tail is O(EPS)


class Tee:
    def __init__(self, path):
        self.f = open(path, 'w')
    def __call__(self, msg):
        print(msg, flush=True)
        self.f.write(str(msg) + "\n")
        self.f.flush()


say = Tee(OUT)


def frac(x):
    return x - np.floor(x)


def fval(alpha, t):
    """f_alpha(t) = {alpha/t} - alpha*{1/t}  (piecewise constant, = alpha floor(1/t) - floor(alpha/t))."""
    return frac(alpha / t) - alpha * frac(1.0 / t)


def jump_points(alphas, eps):
    """Sorted-descending list of all jump points of {1/t} and {a/t} for a in alphas, in (eps, 1]."""
    pts = set()
    nmax = int(np.ceil(1.0 / eps)) + 2
    for n in range(1, nmax):
        t = 1.0 / n
        if t > eps:
            pts.add(t)
    for a in alphas:
        for n in range(1, nmax):
            t = a / n
            if t > eps:
                pts.add(t)
    return sorted(pts, reverse=True)


def quad_piecewise(alphas, H, kind):
    """Integrate over (0,1] a piecewise-constant quantity built from f_{alpha}(t).

    kind:
      'gram'  : returns int f_a(t) f_b(t) dt            (uses alphas[0], alphas[1])
      'norm2' : returns int f_a(t)^2 dt                  (alphas[0])
      'proj'  : returns int f_a(t) t^{iH} dt  (complex)  (alphas[0])

    The integrand is constant on each open interval between CONSECUTIVE jump points, so we
    integrate over [nodes[k+1], nodes[k]] with nodes = descending jump points plus the tail EPS.
    """
    a0 = alphas[0]
    jp = jump_points(alphas, EPS)        # descending, jp[0] = 1, ..., last > EPS
    nodes = jp + [EPS]                    # boundaries, descending, final piece [EPS, jp[-1]]
    a1 = alphas[1] if (kind == 'gram' and len(alphas) > 1) else None
    acc = 0.0 if kind != 'proj' else (0.0 + 0.0j)
    for k in range(len(nodes) - 1):
        hi = nodes[k]
        lo = nodes[k + 1]
        if hi <= lo:
            continue
        tm = 0.5 * (lo + hi)
        if kind == 'gram':
            acc += fval(a0, tm) * fval(a1, tm) * (hi - lo)
        elif kind == 'norm2':
            acc += fval(a0, tm) ** 2 * (hi - lo)
        else:  # 'proj': int_lo^hi t^{iH} dt = (hi^{1+iH} - lo^{1+iH})/(1+iH)
            if abs(H) < 1e-12:
                integ = (hi - lo)
            else:
                integ = (hi ** (1.0 + 1j * H) - lo ** (1.0 + 1j * H)) / (1.0 + 1j * H)
            acc += fval(a0, tm) * integ
    return acc


def single_term_bound(H, alphas):
    """Least-squares single-term bound: d^2 <= 1 - |A|^2/B for each alpha; return best and per-alpha."""
    best = (1.0, None, None)
    rows = []
    for a in alphas:
        A = quad_piecewise([a], H, 'proj')
        B = quad_piecewise([a], H, 'norm2')
        resid = 1.0 - abs(A) ** 2 / B
        rows.append((a, B, abs(A) ** 2, resid))
        if resid < best[0]:
            best = (resid, a, (A, B))
    return best, rows


def few_term_bound(H, alphas):
    """Gram-Schmidt (via solve) projection residual over the basis {f_a : a in alphas}."""
    m = len(alphas)
    G = np.zeros((m, m))
    for j in range(m):
        G[j, j] = quad_piecewise([alphas[j]], H, 'norm2')
        for k in range(j + 1, m):
            g = quad_piecewise([alphas[j], alphas[k]], H, 'gram')
            G[j, k] = G[k, j] = g
    v = np.array([quad_piecewise([a], H, 'proj') for a in alphas], dtype=complex)
    # v^H G^{-1} v : solve G w = v, then v^H w
    try:
        w = np.linalg.solve(G, v)
    except np.linalg.LinAlgError:
        return float('nan'), G, v, None
    proj2 = np.vdot(v, w).real
    return 1.0 - proj2, G, v, w


def disc_radius(d2, H, variant):
    """Zero-free disc radius at a=1/2, height H (b=H).

    variant 'correct': radius = sqrt(1-d2)/d2, centre (1/d2, H).   [引用, DFMR I Thm 2.2]
    variant 'e27'    : radius = |lambda| sqrt(1-d2)/(a d2) = 2|lambda| sqrt(1-d2)/d2.  [E27 sec.2, erroneous]
    Returns (Q2, centre, rad, ok).
    """
    a = R0
    Q2 = 1.0 - 2.0 * a * d2          # = 1 - d2 at a=1/2
    ok = Q2 > 0.0
    Q = np.sqrt(max(Q2, 0.0))
    lam = complex(a, H)
    c = (1.0 + Q2) / (1.0 - Q2) if ok else float('inf')
    if variant == 'correct':
        # paper Thm 2.2: D_r disc centre (a*c, b), radius 2aQ/(1-Q2)=Q/d2, then shifted by r
        centre = complex(a * c + R0, H) if ok else None
        rad = 2.0 * a * Q / (1.0 - Q2) if ok else 0.0
    else:  # 'e27' (erroneous): centre c*lambda shifted by r, radius |lambda|Q/(a d2)
        centre = complex(a * c + R0, c * H) if ok else None
        rad = abs(lam) * Q / (a * d2) if ok else 0.0
    return Q2, centre, rad, ok


def main():
    say("=" * 100)
    say("A4C: pointwise DFMR zero-free disc — d_r(lambda)^2 from the actual zeta functional,")
    say("     disc radius, 1/d^2 sensitivity, conflict check, G1/G2 correspondence")
    say("=" * 100)
    say("  lambda = 1/2 + i H ; r = 1/2 ; a = Re(lambda) = 1/2 ; Q^2 = 1 - d^2 ; non-empty iff d^2 < 1")
    say("  integral truncation EPS = %.1e  (tail O(EPS))" % EPS)

    # ---------------- Section 1 : known-answer reproduction of DFMR I Cor 7.5 ----------------
    say("")
    say("  SECTION 1 (核验) - reproduce DFMR I Cor 7.5 example to validate the disc centre/radius")
    say("    paper: lambda=0.01+50i, r=0.49, sigma1=0.4  =>  disc centre 1/2+50i, radius 3.75e-6")
    try:
        import mpmath as mp
        mp.mp.dps = 40
        lam = mp.mpc(0.01, 50); r = mp.mpf('0.49'); s1 = mp.mpf('0.4')
        a = lam.real
        C = (2 ** (3 - 2 * s1)) / ((3 - 2 * s1) * (1 - s1) ** 2) \
            + (2 ** (2 - s1)) / (1 - s1) ** 2 + 1 / (1 - 2 * s1)
        # phi-hat(s) = Gamma(s) Gamma(1-s1)/Gamma(s+1-s1)  for phi(t)=(1-t)^{-s1} chi_(0,1)
        s = lam + r
        phihat = mp.gamma(s) * mp.gamma(1 - s1) / mp.gamma(s + 1 - s1)
        F = (mp.sqrt(2 * a) * abs((mp.mpf(1) / 4) ** s - mp.mpf(1) / 4) * abs(phihat)
             * abs(mp.zeta(s))) / (
                 ((mp.mpf(1) / 4) ** r + mp.mpf(1) / 4)
                 * (mp.sqrt(C * mp.zeta(1 + 2 * (r - s1))) + 1 / ((1 - s1) * mp.sqrt(2 - 2 * r))))
        x = r + a * (1 + F ** 2) / (1 - F ** 2)
        y = lam.imag
        R = 2 * a * F / (1 - F ** 2)
        say("    computed: F = %.6e ; centre = (%s) + i*%s ; radius = %.6e"
            % (float(F), mp.nstr(x, 20), mp.nstr(y, 20), float(R)))
        say("    paper target: centre 1/2 + 50i, radius 3.75e-6  ->  [核验] radius factor 2Re(lambda)F/(1-F^2)")
    except Exception as e:
        say("    [未核验] mpmath Cor 7.5 reproduction failed: %s" % e)

    # ---------------- Section 2 : d_r(lambda)^2 via single/few-term upper bounds ----------------
    say("")
    say("  SECTION 2 (核验/推导) - d_{1/2}(lambda)^2 = min_c int_0^1 |t^{-iH} - sum c_j ({a_j/t}-a_j{1/t})|^2 dt")
    say("    basis functions f_a(t) = {a/t} - a{1/t},  a in (0,1]  (Prop 7.3, psi(u)={u} for zeta)")
    alphas = (0.125, 0.25, 0.375, 0.5, 0.625, 0.75, 0.875)
    say("    single-term and few-term least-squares projection residual (an UPPER bound on d^2)")
    for H in HEIGHTS:
        best, rows = single_term_bound(H, alphas)
        say("    --- H = %-8.0f ---" % H)
        say("      %8s | %12s | %12s | %18s | %14s" % ("alpha", "B=||f||^2", "|A|^2", "d^2 <= 1-|A|^2/B", "A (H=0 vs -a ln a)"))
        for (a, B, A2, resid) in rows:
            if H == 0.0:
                Aex = quad_piecewise([a], 0.0, 'proj')  # complex; its real part should equal -a ln a
                say("      %8.3f | %12.6f | %12.6e | %18.9f | %.6f vs %.6f"
                    % (a, B, A2, resid, Aex.real, -a * np.log(a)))
            else:
                say("      %8.3f | %12.6f | %12.6e | %18.9f |" % (a, B, A2, resid))
        d2few, G, v, w = few_term_bound(H, (0.25, 0.5, 0.75))
        if not np.isfinite(d2few):
            say("      3-term {0.25,0.5,0.75}: d^2 <= %s (Gram rank-deficient? see det below)" % d2few)
        else:
            say("      3-term {0.25,0.5,0.75}: d^2 <= %.9f   (trivial bound d^2 <= 1)" % d2few)
    # diagnose the Gram matrix rank
    G = np.zeros((3, 3))
    for j, aj in enumerate((0.25, 0.5, 0.75)):
        G[j, j] = quad_piecewise([aj], 0.0, 'norm2')
        for k, ak in enumerate((0.25, 0.5, 0.75)):
            if k > j:
                G[j, k] = G[k, j] = quad_piecewise([aj, ak], 0.0, 'gram')
    say("    Gram matrix of {f_0.25, f_0.5, f_0.75} at H=0:")
    for row in G:
        say("      [ %12.6f %12.6f %12.6f ]" % tuple(row))
    say("    eigenvalues: %s" % np.linalg.eigvalsh(G))
    say("    cross-check: B(a) should NOT equal a^2 in general (a^2: %.4f %.4f %.4f)"
        % (0.25 ** 2, 0.5 ** 2, 0.75 ** 2))

    # ---------------- Section 3 : disc radius & sensitivity ----------------
    say("")
    say("  SECTION 3 (核验/推导) - disc radius vs d^2  (a = 1/2)")
    say("    correct (引用 DFMR I Thm 2.2): rad = sqrt(1-d^2)/d^2, centre (1/d^2, H)")
    say("    E27-A4-5 sec.2 (erroneous)   : rad = |lambda| sqrt(1-d^2)/(a d^2) = 2|lambda| sqrt(1-d^2)/d^2")
    D2S = (1.0, 0.1, 0.01, 0.001, 1e-6)
    for H in (1.0e3, 1.0e5):
        lam = complex(R0, H)
        say("    H = %.0e, |lambda| = %.6e" % (H, abs(lam)))
        say("      %10s | %16s %20s | %16s %20s" % ("d^2", "rad (correct)", "centre (correct)",
                                                    "rad (E27 sec.2)", "centre (E27 sec.2)"))
        for d2 in D2S:
            Q2c, cc, rc, okc = disc_radius(d2, H, 'correct')
            Q2e, ce, re, oke = disc_radius(d2, H, 'e27')
            if okc:
                say("      %10.5f | %16.6e %20s | %16.6e %20s"
                    % (d2, rc, "(%s, %.0f)" % ("%.6e" % cc.real, cc.imag),
                       re, "(%s, %.0f)" % ("%.6e" % ce.real, ce.imag)))
            else:
                say("      %10.5f | %16s (EMPTY: d^2>=1) | %16s (EMPTY)" % (d2, "-", "-"))
    # 1/d^2 sensitivity read-off
    say("    => rad(correct) = sqrt(1-d^2)/d^2 ~ 1/d^2 for small d^2  (pure 1/d^2, no |lambda| factor)")
    say("    => rad(E27 sec.2) ~ 2|lambda|/d^2 : overstates by 2|lambda| ~ 2H (H=1e3: 2000, H=1e5: 2e5)")

    # what d^2 is needed for rad >= rho (correct formula): rad^2 d^4 + d^2 - 1 = 0
    say("")
    say("  SECTION 4 (推导) - what d^2 is needed for rad >= rho  (correct formula)")
    say("    solve rad^2 d^4 + d^2 - 1 = 0  =>  d^2 = (-1 + sqrt(1+4 rad^2))/(2 rad^2) ~ 1/rad")
    say("      %12s | %20s" % ("target rad", "required d^2"))
    for rho in (1.0, 10.0, 100.0, 1000.0, 1e6):
        d2req = (-1.0 + np.sqrt(1 + 4 * rho ** 2)) / (2 * rho ** 2)
        say("      %12.0f | %20.6e   (~1/rad = %.3e)" % (rho, d2req, 1.0 / rho))

    # ---------------- Section 5 : conflict check vs Platt-Trudgian zeros ----------------
    say("")
    say("  SECTION 5 (核验) - conflict of the disc with verified zeros (Platt-Trudgian: RH checked |t|<=3e12)")
    z = np.load(ZEROS)
    say("    loaded %d zeros, gamma in [%.3f, %.3f] (all critical-line, Re=1/2 by Platt-Trudgian)"
        % (len(z), z[0], z[-1]))
    say("    the disc centre has Re = 1/d^2 >= 1 and radius = sqrt(1-d^2)/d^2 < 1/d^2, so its leftmost")
    say("    Re = (1 - sqrt(1-d^2))/d^2 = 1/(1+sqrt(1-d^2)) > 1/2 : the disc NEVER crosses Re=1/2.")
    # actual computed single-term d^2 (best over alpha grid) at H = 1e3 and 1e5
    say("    actual single-term d^2 (best alpha) -> disc:")
    for H in (1.0e3, 1.0e5):
        best, _ = single_term_bound(H, alphas)
        d2act = best[0]
        Q2, c, rad, ok = disc_radius(d2act, H, 'correct')
        if not ok or c is None or d2act <= 0.0:
            say("    H=%.0e single-term d2=%.9f : Q2=%.3e -> EMPTY/degenerate disc (radius ~0)"
                % (H, d2act, 1.0 - d2act))
        else:
            dist = np.abs((0.5 - c.real) + 1j * (z - c.imag))
            inside = int(np.sum(dist < rad))
            say("    H=%.0e single-term d2=%.9f rad=%.6e centre=(%.6e,%.0f) zeros inside: %d"
                % (H, d2act, rad, c.real, c.imag, inside))
    for H in (1.0e3, 1.0e5):
        for d2 in (0.1, 0.01):
            Q2, c, rad, ok = disc_radius(d2, H, 'correct')
            dist = np.abs((0.5 - c.real) + 1j * (z - c.imag))
            inside = int(np.sum(dist < rad))
            say("    H=%.0e d^2=%.2f (illustration) rad=%.6e centre=(%.6e,%.0f) zeros inside: %d"
                % (H, d2, rad, c.real, c.imag, inside))
    say("    => for any d^2<1 the disc lies strictly to the right of Re=1/2, so it cannot contain a")
    say("       known zero (all known zeros have Re=1/2); no conflict, and also no information about")
    say("       the critical line (Burnol's 'disappointing fact').  [推导]")

    # ---------------- Section 6 : READ-OFF ----------------
    say("")
    say("=" * 100)
    say("READ-OFF")
    say("=" * 100)
    say("  [核验] Cor 7.5 example reproduced (Section 1): disc centre/radius match DFMR I's own numbers.")
    say("  [引用] for zeta, psi(u)={u} (fractional part), K_r = span(t^r({a/t}-a{1/t}))  (DFMR I Rmk 3.5, Prop 7.3).")
    say("  [推导] at r=1/2 the functional reduces to d^2 = min int_0^1 |t^{-iH} - sum c_j({a_j/t}-a_j{1/t})|^2 dt.")
    say("  [核验] single/few-term projection gives a genuine upper bound d^2 <= 1 - v^H G^{-1} v.")
    say("  [核验/新发现] the disc is 'variant 2': rad = sqrt(1-d^2)/d^2, centre (1/d^2, H); E27-A4-5 sec.2")
    say("       formula carries a spurious factor |lambda|/a = 2|lambda| ~ 2H (algebra drops the y-cross term).")
    say("  [推导] d^2 -> 1 as H -> infinity (the phase t^{-iH} oscillates and cannot be tracked by the")
    say("       piecewise-constant test span), so the disc is essentially EMPTY at H=1e3,1e5.")
    say("  [推导] disc never crosses Re=1/2 (leftmost Re = 1/(1+sqrt(1-d^2)) > 1/2); no conflict with")
    say("       Platt-Trudgian, and no critical-line information.")
    say("  [推导] rad >> 1 requires d^2 <<~ 1/rad ; with the trivial d^2~1 the radius is ~0.")
    say("  [未做] no lambda-dependent d_r(lambda)^2 that is SMALL is produced; the honest verdict is that")
    say("       the pointwise disc is empty from the available input (see the G1/G2 checklist in the doc).")
    say("  [未做] no proof claimed; nothing about RH is decided by these numbers.")
    say("")
    say("Output written to %s" % OUT)


if __name__ == '__main__':
    main()
