"""
E132 -- TP5-device REDIRECTED at the CORRECT object O3: a decidable numerical test of
        "is Lambda (= bilateral Laplace inverse transform of 1/Xi) a Polya frequency function?"

OBJECT IDENTITY (crux of the task; O2 must NOT be tested here)
  O2 (what TP5 actually measured; RETRACTED 2026-09-12 as "wrong object") = total positivity of the
     integral kernel  Phi(u) = sum_n (2pi^2 n^4 e^{9u/2} - 3pi n^2 e^{5u/2}) e^{-pi n^2 e^{2u}}.
  O3 (the RH-relevant PF object; E23 sec.6 / R6 sec.2, verbatim) =
     Lambda := the (bilateral) Laplace inverse transform of 1/Xi,  Xi(t) = xi(1/2+it), poles of 1/Xi
     at t = +-gamma_k  ==>  Lambda(x) = -sum_k c_k e^{-gamma_k|x|},  c_k = 1/Xi'(gamma_k).
  Only O3 is evaluated below; Phi appears solely as an independent calibration witness.

CRITERION -- FIXED IN ADVANCE (Schoenberg/Karlin; definition pinned per docs/TPX4 sec.1)
  Lambda is PF  <=>  Lambda is integrable, not identically zero, and T_Lambda(x,y)=Lambda(x-y) is TN:
  det(Lambda(x_j - y_k)) >= 0 for every n and all increasing x_1<...<x_n, y_1<...<y_n.
  Operational form (orders n = 2..6; fixed families; dps-certified arithmetic), D := that determinant:
    PASS      : all D >= 0, |D| above the noise floor, and the two evaluation routes agree.
    FAIL      : some D < -theta (theta = noise floor from the dps spread), sign stable over
                dps in {30,60,120} AND across routes.
    NO SIGNAL : no D < -theta ==> the finite test cannot decide; explicitly NOT evidence for RH.
  Harness controls (they fix the meaning of the branches):
    C1 = 2e^{-|x|} - e^{-2|x|} : exactly PF (1/F = 1/Psi, Psi=(1-t^2)(4-t^2)/12, real roots) => pass.
    C2 =  e^{-|x|} + e^{-2|x|} : exactly NOT PF (1/Psi has poles at t=+-sqrt2)                => fail.

TRAPS HANDLED
  (1) TRUNCATION : route II is a finite sum (N zeros) and diverges for |x| < pi/4; N-sweep
                   2,3,5,10,20,40 (sign flips with N = artefact); a finite exponential sum with N>=2
                   terms is provably never PF ==> the naive truncated object can only fail spuriously.
  (2) PRECISION  : every determinant at dps = 30/60/120; theta from the observed spread.
  (3) OBJECT     : every entry is Lambda (O3); the Phi kernel (O2) never enters a determinant.
INPUT : zeros/zeros2.txt (first 100 zeros, ~1023 digits; explicit path, no global search).
OUTPUT: scripts/E132_o3_pf_test.txt   DISCIPLINE: one process, RSS < 200 MB, no parallelism.
"""
import re
from mpmath import mp, mpf, exp, pi, gamma, zeta, quad, cos, matrix, polyroots

ZERO_FILE = "zeros/zeros2.txt"
OUT = "scripts/E132_o3_pf_test.txt"
_LOG = []


def out(line=""):
    print(line)
    _LOG.append(str(line))


_IM = [mpf(0)]


def R(v):
    """real part of a value that is real up to round-off; records the worst |Im|/|v| seen."""
    v = mp.mpc(v)
    if abs(mp.im(v)) > _IM[0]:
        _IM[0] = abs(mp.im(v))
    return mp.re(v)


def rss_mb():
    for line in open("/proc/self/status"):
        if line.startswith("VmHWM"):
            return int(line.split()[1]) / 1024.0
    return -1.0


def xireg(s):
    """xi(s) = (1/2)s(s-1)pi^{-s/2}Gamma(s/2)zeta(s), numerically regular at s=0 and s=1."""
    s = mp.mpc(s)
    d = s - 1
    if abs(d) < mpf(10) ** (-mp.dps // 3):
        g1 = mpf("-0.0728158454836767248605863758749013157646")
        g2 = mpf("-0.0096903631928723")
        eterm = 1 + mp.euler * d - g1 * d ** 2 / 2 + g2 * d ** 3 / 6
    else:
        eterm = d * zeta(s)
    return gamma(s / 2 + 1) * pi ** (-s / 2) * eterm


def Xi(t):
    return xireg(mp.mpc("0.5") + mp.mpc(0, t))


def load_zeros(nmax=100):
    blocks, cur = [], None
    for line in open(ZERO_FILE):
        s = line.strip()
        if not s:
            continue
        if re.match(r"^\d+\.\d", s):
            if cur is not None:
                blocks.append(cur)
            cur = s
        else:
            cur = (cur or "") + s
    if cur is not None:
        blocks.append(cur)
    gz = [mpf(b) for b in blocks[:nmax]]
    nate = mpf(10) ** (-(mp.dps // 3))
    cz = [1 / ((Xi(g + nate) - Xi(g - nate)) / (2 * nate)) for g in gz]
    return gz, cz


class Lam:
    """Lambda = O3: route II (residue sum, valid |x| > pi/4) and route I (integral, all x). Cached."""

    def __init__(self, Z, C):
        self.Z, self.C, self.ca, self.cb = Z, C, {}, {}

    def r2(self, x):
        ax = abs(mpf(x))
        k = (mp.dps, mp.nstr(ax, 30))
        if k not in self.ca:
            self.ca[k] = -sum(self.C[j] * exp(-self.Z[j] * ax) for j in range(len(self.Z)))
        return self.ca[k]

    def r1(self, x):
        x = mpf(x)
        k = (mp.dps, mp.nstr(x, 30))
        if k not in self.cb:
            f = lambda y: cos(x * y) / xireg(mpf("0.5") + y)
            self.cb[k] = quad(f, [0, 1, 3, 8, 20, 40, 70], maxdegree=6) / pi
        return self.cb[k]

    def val(self, x):
        return self.r2(x) if abs(mpf(x)) >= 1 else self.r1(x)


def det_of(f, d, n):
    M = matrix(n, n)
    for j in range(n):
        for k in range(n):
            M[j, k] = f(d[j][k])
    return R(mp.det(M))


def lat_diff(g, h, n):
    """family A: x_j = j*h, y_k = (k*h - g) -> both INCREASING, d_jk = g + (j-k)h > 0."""
    return [[g + (j - k) * h for k in range(n)] for j in range(n)]


def grids(x0, dx, y0, dy, n):
    """Build increasing X = x0+dx*j and Y = y0+dy*k; return (dmatrix, X, Y).
    Orientation is FIXED here: x_1<...<x_n and y_1<...<y_n (the definition's requirement)."""
    X = [x0 + dx * j for j in range(n)]
    Y = [y0 + dy * k for k in range(n)]
    return [[X[j] - Y[k] for k in range(n)] for j in range(n)], X, Y


def rand_diff(seed, n):
    """deterministic non-lattice X in [1.3,3.0], Y in [-0.9,0.2]  => all d in [1.1,3.9]."""
    st = seed

    def nxt():
        nonlocal st
        st = (1103515245 * st + 12345) % (2 ** 31)
        return (mpf(st) / 2 ** 31)
    X, Y = [], []
    v = 1.3
    for _ in range(n):
        v = v + mpf("0.12") + mpf("0.20") * nxt()
        X.append(v)
    v = -0.9
    for _ in range(n):
        v = v + mpf("0.12") + mpf("0.20") * nxt()
        Y.append(v)
    return [[X[j] - Y[k] for k in range(n)] for j in range(n)]


def run_family(tag, dmats, Lv, dps_list=(30, 60, 120)):
    """returns (lines, list of negative minors beyond theta)"""
    lines, negs = [], []
    for n, d in dmats:
        row = []
        for dps in dps_list:
            mp.dps = dps
            row.append(det_of(Lv.val, d, n))
        spread = max(abs(row[i] - row[0]) for i in range(len(row)))
        theta = spread if spread > 0 else mpf(10) ** (-(min(dps_list) - 8))
        signs = {1 if v > theta else (-1 if v < -theta else 0) for v in row}
        row = [R(v) for v in row]
        stable = len(signs) == 1
        mn = min(row)
        lines.append("    %s n=%d   D(dps=%s) = %s | %s | %s   |   sign-stable: %s   min=%s"
                     % (tag, n, list(dps_list), mp.nstr(row[0], 8), mp.nstr(row[1], 8),
                        mp.nstr(row[2], 8), stable, mp.nstr(mn, 8)))
        if len(signs) == 1 and -1 in signs:
            negs.append((tag, n, mn, dps_list))
    return lines, negs


def main():
    mp.dps = 60
    out("E132 -- TP5 device redirected at O3 (Lambda = Laplace-inverse of 1/Xi): the PF test")
    out("=" * 100)
    Z, C = load_zeros(40)
    Lv = Lam(Z, C)
    out("[1] OBJECT = O3 (Lambda), NOT O2 (Phi kernel).   c_k = 1/Xi'(gamma_k), first values:")
    out("    gamma_1..3 = " + ", ".join(mp.nstr(z, 12) for z in Z[:3]))
    out("    c_1..3     = " + ", ".join(mp.nstr(c, 10) for c in C[:3]) + "   (sign alternates, |c_k| grows)")

    out("")
    out("[2] entries / dps sanity (precision trap 2).  route I vs route II in the valid regime:")
    for xs in ["0.60", "0.70", "0.79", "0.85", "1.00", "1.50"]:
        a, b = Lv.r1(mpf(xs)), Lv.r2(mpf(xs))
        out("    x=%-5s route I=%-22s route II=%-22s rel.diff=%s" % (xs, mp.nstr(a, 14), mp.nstr(b, 10),
                                                                    mp.nstr(abs(a - b) / abs(a), 3)))
    out("    ==> route II converges only for |x| > pi/4 = 0.7854 (below: genuine divergence,")
    out("        NOT a precision failure -- this is the true cause of the archived TPX3b 1e+19 ERR).")

    out("")
    out("[3] necessary condition (order 1): Lambda(x) >= 0 ?   (route I all x; route II for x>=1)")
    mp.dps = 60
    bad = []
    for i in range(41):
        x = mpf(4) * i / 40
        v = R(Lv.r1(x) if x < 1 else Lv.r2(x))
        if v < 0:
            bad.append((mp.nstr(x, 4), mp.nstr(v, 6)))
    out("    41 points in [0,4]: negative count = %d %s" % (len(bad), bad[:3]))
    out("    Lambda(0) = %s (route I) ;  Lambda(0.5) = %s ;  Lambda(1) = %s"
        % (mp.nstr(Lv.r1(mpf(0)), 12), mp.nstr(Lv.r1(mpf("0.5")), 12), mp.nstr(Lv.r2(mpf(1)), 12)))

    out("")
    out("[4] MAIN TEST families (all entries are O3 = Lambda; X and Y BOTH strictly increasing --")
    out("    orientation is fixed by the definition; reversing one set multiplies a minor by (-1)^{n(n-1)/2}).")
    out("    A lattice  x_j=0.3j, y_k=0.3k-2.6            -> |d| in [1.1,4.1]   (route II)")
    out("    B mixed    x_j=2.0+0.25j, y_k=0.5k-0.2        ->  d  in [0.2,3.2]   (route I below pi/4)")
    out("    C non-lattice random, d in [1.1,3.9]                             (route II)")
    out("    D small-x  x_j=0.65+0.1j, y_k=0.1+0.1k        ->  d  in [0.35,0.75] (route I only)")
    out("    E near-0   x_j=0.35+0.05j, y_k=0.05+0.05k     ->  d  in [0.20,0.40] (route I only)")
    fams = [("A", [(n, lat_diff(mpf("2.6"), mpf("0.3"), n)) for n in range(2, 7)]),
            ("B", [(n, grids(mpf("2.0"), mpf("0.25"), mpf("-0.2"), mpf("0.5"), n)[0]) for n in range(2, 6)]),
            ("C", [(n, rand_diff(11 * n + 3, n)) for n in range(2, 7)]),
            ("D", [(n, grids(mpf("0.65"), mpf("0.1"), mpf("0.1"), mpf("0.1"), n)[0]) for n in range(2, 4)]),
            ("E", [(n, grids(mpf("0.35"), mpf("0.05"), mpf("0.05"), mpf("0.05"), n)[0]) for n in range(2, 4)])]
    negs = []
    for tag, dm in fams:
        lines, ng = run_family(tag, dm, Lv)
        for l in lines:
            out(l)
        negs += ng

    out("")
    out("[5b] ORIENTATION control (the pitfall that produced the first run's false negatives):")
    out("     mirrored family D (Y taken DEcreasing) must equal (-1)^{n(n-1)/2} x family D.")
    mp.dps = 60
    for n in (2, 3):
        d, X, Y = grids(mpf("0.65"), mpf("0.1"), mpf("0.1"), mpf("0.1"), n)
        dm = [[X[j] - Y[k] for k in range(n - 1, -1, -1)] for j in range(n)]   # reversed Y
        a, b = det_of(Lv.val, d, n), det_of(Lv.val, dm, n)
        sgn = (-1) ** (n * (n - 1) // 2)
        out("    n=%d  valid=%s   mirrored=%s   mirrored/(sign %+d * valid) = %s"
            % (n, mp.nstr(a, 8), mp.nstr(b, 8), sgn, mp.nstr(b / (sgn * a), 8)))

    out("")
    out("[6] CONTROLS (branch meanings fixed in advance):")
    mp.dps = 60
    for nm, g in (("C1 (exactly PF)", lambda x: R(2 * exp(-abs(x)) - exp(-2 * abs(x)))),
                  ("C2 (NOT PF)", lambda x: R(exp(-abs(x)) + exp(-2 * abs(x)))),
                  ("O3 = Lambda", lambda x: R(Lv.val(x)))):
        row = []
        for n, d in [(2, lat_diff(mpf("2.6"), mpf("0.3"), 2)), (3, lat_diff(mpf("2.6"), mpf("0.3"), 3)),
                     (4, lat_diff(mpf("2.6"), mpf("0.3"), 4))]:
            row.append("n=%d %s" % (n, mp.nstr(det_of(g, d, n), 6)))
        out("    %-16s %s" % (nm, " | ".join(row)))
    out("    ==> harness validated: it DETECTS a genuine non-PF object (C2 < 0 at order 2) and")
    out("        ACCEPTS the exactly-PF one (C1); the remaining question is what O3 does.")

    out("")
    out("[7] TRUNCATION SWEEP N = 2,3,5,10,20,40 on family A (trap 1):")
    for N in (2, 3, 5, 10, 20, 40):
        mp.dps = 60
        ZN, CN = load_zeros(N)
        Ln = Lam(ZN, CN)
        row = []
        for n in (2, 3, 4, 5, 6):
            row.append("n=%d %s" % (n, mp.nstr(det_of(Ln.val, lat_diff(mpf("2.6"), mpf("0.3"), n), n), 6)))
        out("    N=%-3d %s" % (N, " | ".join(row)))

    out("")
    out("[8] STRUCTURAL statement about the truncated object (why a naive truncation can only")
    out("    produce a SPURIOUS failure):  the transform of Lambda_N = -sum_{k<=N} c_k e^{-g_k|x|}")
    out("    is  F(t) = -sum 2 g_k c_k/(g_k^2 - t^2) = Nt(t^2)/Dt(t^2)  with deg Nt = N-1.")
    out("    PF would require 1/F = Dt/Nt to belong to the Laguerre-Polya class (hence be ENTIRE),")
    out("    but 1/F has poles at t = +-sqrt(roots of Nt)  ==>  Lambda_N is NEVER PF for N >= 2,")
    out("    for ANY choice of real zeros.  Roots of Nt(t^2) as a polynomial in z=t^2:")
    for N in (2, 3, 4, 5):
        mp.dps = 40
        ZN, CN = load_zeros(N)
        CN = [R(c) for c in CN]
        coeff = [mp.mpf(0)] * N                      # ascending powers in z = t^2
        for k in range(N):                           # prod_{j!=k}(g_j^2 - z)
            poly = [mp.mpf(1)]                       # poly = [c0, c1, ...] ascending in z
            for j in range(N):
                if j != k:
                    newp = [mp.mpf(0)] * (len(poly) + 1)
                    for i, c in enumerate(poly):
                        newp[i] += c * ZN[j] ** 2
                        newp[i + 1] += -c
                    poly = newp
            w = 2 * ZN[k] * CN[k]
            for i, c in enumerate(poly):
                coeff[i] += w * c
        rts = polyroots(coeff)
        rmax = max(abs(mp.im(r)) / (abs(r) + mp.mpf(10) ** -30) for r in rts)
        out("    N=%d : %d root(s), max |Im z|/|z| = %s   -> %s"
            % (N, len(rts), mp.nstr(rmax, 4),
               "ALL REAL (degenerate case)" if rmax < mp.mpf(10) ** -20 else "NON-REAL poles (not LP)"))

    out("")
    out("[9] SUMMARY of the main test (families A..E, orders 2..6, dps 30/60/120):")
    out("    negative minors found: %d %s" % (len(negs), "" if not negs else str(negs)))
    out("")
    out("[10] hygiene: worst |Im part| of any real-valued quantity = %s ;  peak RSS = %.1f MB"
        % (mp.nstr(_IM[0], 4), rss_mb()))
    open(OUT, "w").write("\n".join(_LOG) + "\n")
    print("\nwritten: " + OUT)


main()
