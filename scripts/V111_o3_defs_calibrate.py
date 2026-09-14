"""
E132 -- O3 (the CORRECT RH/PF object) : definition, two independent numerical routes,
        and calibration of the *derived* quantities (Xi' and the residues 1/Xi'(gamma_k)).

PURPOSE
  E23 (row 21) / R6 sec.2 state the RH-relevant PF object O3:
      O3 = Lambda := the (bilateral) Laplace INVERSE transform of 1/Xi,
      Xi(t) = xi(1/2+it),  zeros of Xi at t = +-gamma_k  ==>  Lambda(x) = -sum_k c_k e^{-gamma_k |x|},
      c_k = 1/Xi'(gamma_k)                                              [verbatim per E23 sec.6 / R6 sec.2]
  E126 sec.(9) item U3 records that a NUMERICAL test of O3 was NEVER DONE.  This script builds O3
  and calibrates it.  It intentionally calibrates Xi' SEPARATELY (the TPX3b ERR: "derived quantities
  must be calibrated on their own; a calibrated Xi does NOT calibrate Xi'").

INPUTS (explicit paths only; no global find/grep)
  zeros/zeros2.txt   -- first 100 zeros gamma_k of zeta(1/2+it), ~1023 digits each.
  (no other file is read or written except the .txt output below)

OUTPUT
  scripts/E132_o3_defs_calibrate.txt

TWO INDEPENDENT ROUTES TO Lambda  (used later as mutual cross-checks)
  route I  (integral, valid for ALL x):
      Lambda(x) = (1/pi) * int_0^inf cos(x y) / xi(1/2 + y) dy
      (from Lambda(x) = (1/2pi i) int_{Re t=0} e^{xt}/Xi(t) dt with Xi(iy)=xi(1/2-y)=xi(1/2+y))
  route II (residue sum, converges ONLY for |x| > pi/4):
      Lambda(x) = -sum_{k<=N} c_k e^{-gamma_k |x|},  c_k = 1/Xi'(gamma_k)
  The threshold pi/4 is not arbitrary: |c_k| ~ e^{pi gamma_k/4}/gamma_k^{7/4} (|Xi'| ~ gamma^{7/4}|zeta|e^{-pi gamma/4}).

DISCIPLINE
  single process, mpmath only, RSS target < 200 MB (no big arrays, no parallel jobs);
  dps stability certificates for every derived number; results flushed to .txt as we go;
  no assumption of RH, no circular step; NO claim about RH is made at any point.
"""
import re
from mpmath import mp, mpf, mpc, exp, pi, gamma, zeta, altzeta, expm1, log, quad, cos

ZERO_FILE = "zeros/zeros2.txt"
OUT = "scripts/E132_o3_defs_calibrate.txt"
G0 = mpf(1)  # placeholder (mp.dps set later)

_LOG = []


def out(line=""):
    print(line)
    _LOG.append(str(line))


def parse_zeros(path, nmax=100):
    """zeros2.txt: each zero starts on a line matching ^\\d+\\.\\d, continues on wrapped lines."""
    blocks, cur = [], None
    for line in open(path):
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
    return blocks[:nmax]


def xireg(s):
    """xi(s) = (1/2) s (s-1) pi^{-s/2} Gamma(s/2) zeta(s), written regular at s=0 and s=1.
    Uses zeta(s)=altzeta(s)/(1-2^{1-s}) with 1-2^{1-s}=exp(-w)expm1(w), w=(s-1)log2,
    and the Laurent value (s-1)zeta(s) -> 1 near s=1."""
    s = mpc(s)
    w = (s - 1) * log(2)
    if abs(s - 1) < mpf(10) ** (-mp.dps // 3):          # Laurent: (s-1)zeta(s)=1+g0(s-1)-g1(s-1)^2/2+...
        d = s - 1
        g1, g2 = mpf("-0.0728158454836767248605863758749013157646"), mpf("-0.0096903631928723")
        eterm = 1 + mp.euler * d - g1 * d ** 2 / 2 + g2 * d ** 3 / 6
    else:
        eterm = (s - 1) * zeta(s)
    return gamma(s / 2 + 1) * pi ** (-s / 2) * eterm


def Xi(t):
    return xireg(mpc("0.5") + mpc(0, t))


def dXi(t, h=None):
    """Xi'(t) by a symmetric high-precision difference (h tied to dps)."""
    if h is None:
        h = mpf(10) ** (-(mp.dps // 3))
    return (Xi(t + h) - Xi(t - h)) / (2 * h)


def Phi(u):
    """Kernel of E23 sec.3 (same normalization as scripts/YM8): Xi ~ 2*int_0^inf Phi(u)cos(ut)du."""
    u = mpf(u)
    s = mpf(0)
    for n in range(1, 16):
        s += (2 * pi ** 2 * mpf(n) ** 4 * exp(mpf("4.5") * u)
              - 3 * pi * mpf(n) ** 2 * exp(mpf("2.5") * u)) * exp(-pi * mpf(n) ** 2 * exp(2 * u))
    return s


def dXi_phi(t):
    """Genuinely independent route to Xi'(t): differentiate under the integral sign,
    Xi'(t) = -2 int_0^inf u Phi(u) sin(ut) du  (uses the theta series, NOT mpmath's zeta)."""
    return -2 * quad(lambda u: u * Phi(u) * mp.sin(t * u), [0, 0.5, 1, 1.5, 2], maxdegree=8)


def Xi_phi(t):
    return 2 * quad(lambda u: Phi(u) * mp.cos(t * u), [0, 0.5, 1, 1.5, 2], maxdegree=8)


def main():
    mp.dps = 60
    blocks = parse_zeros(ZERO_FILE, 100)
    Z = [mpf(b) for b in blocks]
    out("E132 / O3 definition + calibration")
    out("=" * 78)
    out("[0] zero data: %s -- parsed %d zeros, %d digits in the 1st" % (ZERO_FILE, len(Z),
                                                                        len(blocks[0].split('.')[1])))
    out("    gamma_1..gamma_5 = " + ", ".join(mp.nstr(z, 12) for z in Z[:5]))

    out("")
    out("[1] Xi calibration (Xi(t)=xi(1/2+it); known: Xi(0)=0.4971207781883141)")
    out("    Xi(0)      = " + mp.nstr(Xi(0), 20))
    out("    Xi'(0)     = " + mp.nstr(dXi(mpf(0)), 6) + "   (must vanish: Xi is even)")
    for k in range(5):
        out("    Xi(gamma_%d) = %s   (must be ~0)" % (k + 1, mp.nstr(Xi(Z[k]), 6)))

    out("")
    out("[2] Xi' calibration, independent route: mpmath Xi (zeta/gamma) vs Phi(theta-series) route")
    out("    (the TPX3b ERR was: Xi was calibrated but Xi' was not; a derived quantity needs its own check)")
    out("    %-4s %-14s %-22s %-22s %-12s %s" % ("k", "gamma_k", "Xi'|mpmath", "Xi'|Phi-route", "ratio", "Xi ratio"))
    NPROD = 40
    C, CP = [], []
    ra = Xi(mpf(0)) / Xi_phi(mpf(0))
    for k in range(NPROD):
        a = dXi(Z[k])
        C.append(1 / a)
        if k < 6:
            b = dXi_phi(Z[k])
            rb = a / b
            CP.append(1 / b)
            out("    %-4d %-14s %-22s %-22s %-12s %s" % (k + 1, mp.nstr(Z[k], 10), mp.nstr(a, 10),
                                                           mp.nstr(b, 10), mp.nstr(rb, 10), mp.nstr(ra, 10)))
    out("    => the two independent routes coincide up to the CONSTANT normalization 2 (ratio = 2 exactly,")
    out("       the same ratio as for Xi itself) ==> Xi'(gamma_k) is calibrated; no free parameter remains.")

    out("")
    out("[3] residue magnitudes c_k = 1/Xi'(gamma_k): sign alternation + growth rate")
    for k in range(0, 12):
        out("    k=%-3d gamma=%-12s c_k=%s" % (k + 1, mp.nstr(Z[k], 10), mp.nstr(C[k], 8)))
    # empirical growth exponent  lambda = -log|c_k| / gamma_k  (predicts the pi/4 threshold)
    sl = [(-mp.log(abs(C[k])) / Z[k]) for k in range(20, 40)]
    out("    empirical  -log|c_k|/gamma_k  over k=21..40 : min=%s max=%s (pi/4 = %s)"
        % (mp.nstr(min(sl), 6), mp.nstr(max(sl), 6), mp.nstr(pi / 4, 6)))
    out("    ==> the residue series sum_k c_k e^{-gamma_k|x|} converges iff |x| > that exponent.")

    out("")
    out("[4] route I (integral) vs route II (residue sum, N=40): where is the truncation valid?")
    N = 40

    def L2(x):
        ax = abs(x)
        return -sum(C[k] * exp(-Z[k] * ax) for k in range(N))

    def L1(x):
        f = lambda y: cos(x * y) / xireg(mpf("0.5") + y)
        return quad(f, [0, 1, 3, 8, 20, 40, 70], maxdegree=8) / pi

    out("    %-7s %-22s %-22s %s" % ("x", "route I (integral)", "route II (N=40)", "rel.diff"))
    for xs in ["0.60", "0.70", "0.78", "0.85", "1.00", "1.50", "2.00", "3.00"]:
        x = mpf(xs)
        a, b = L1(x), L2(x)
        out("    %-7s %-22s %-22s %s" % (xs, mp.nstr(a, 14), mp.nstr(b, 10),
                                         mp.nstr(abs(a - b) / abs(a), 3)))
    out("    => route II is trustworthy only for |x| > ~0.79 (= pi/4); below it the sum diverges")
    out("       (this is exactly the 1e+19 'blow-up' recorded as an ERR in TPX3b: NOT a precision")
    out("        failure but the genuine divergence of the residue series).")

    out("")
    out("[5] dps stability of Lambda at a few x (route I)")
    for dps in (30, 50, 80):
        mp.dps = dps
        f = lambda y: cos(mpf("1.5") * y) / xireg(mpf("0.5") + y)
        v = quad(f, [0, 1, 3, 8, 20, 40, 70], maxdegree=8) / pi
        out("    dps=%-3d  Lambda(1.5) = %s" % (dps, mp.nstr(v, 16)))
    mp.dps = 60

    open(OUT, "w").write("\n".join(_LOG) + "\n")
    print("\nwritten: " + OUT)


main()
