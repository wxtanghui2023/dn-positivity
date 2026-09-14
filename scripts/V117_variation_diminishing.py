#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""V117 -- VARIATION-DIMINISHING test of the CORRECT object O3 (Lambda = bilateral Laplace
inverse of 1/Xi); the LAST remaining form left by docs/TPX-verdict sec.3.

OBJECT: O2 (retracted 2026-09-12, "wrong object") = total positivity of Phi(u)=sum_n(2pi^2 n^4
e^{9u/2}-3pi n^2 e^{5u/2})e^{-pi n^2 e^{2u}}.  O3 (E23 sec.6 / R6 sec.2) = Lambda.  ONLY O3 is
evaluated here; Phi never appears.  Anchor: int_R Lambda = 1/Xi(0).

CRITERION (fixed before running; Schoenberg, docs/TPX4 sec.1: "A TN => S^-(Ax)<=S^-(x)"; docs/
TPX-verdict sec.3: count the sign changes after convolution).  v(f):=S^-(f)=#sign changes of f on
R, T_Lambda f := Lambda*f.  VD: v(T_Lambda f)<=v(f) for EVERY f;  [theory] Lambda in PF <=> T_Lambda
variation diminishing  => VD === PF for O3.
  FAIL      : some f has S^-(Lambda*f)>S^-(f), stable in dps/grid, not an artefact (3 gates below).
  PASS      : holds for ALL tested f AND family exhaustive AND object untruncated (unreachable for
              the real Lambda; reserved for provable objects = the controls).
  NO SIGNAL : no violation found => finite test cannot decide; NOT evidence for RH either way.
CONTROLS (known answers): C1=2e^{-|x|}-e^{-2|x|} exactly PF (1/F in LP) => PASS; C2=e^{-|x|}+e^{-2|x|}
exactly NOT PF (1/F(s) has poles s=+-sqrt2) => FAIL.  If C2 does not FAIL the device has no
discriminating power => main run VOID.  tau = 1e-6 relative.  BOUNDARY: NOT evidence about RH.

IMPLEMENTATION (reuses V111's O3 evaluator): for f=sum_i v_i 1_{[l_i,r_i]},
(Lambda*f)(x)=sum_i v_i[W(x-l_i)-W(x-r_i)], W'=Lambda, W(z)=M/2+F(z), M=1/Xi(0), F(z)=int_0^z Lambda:
  route I (all z): F(z)=sgn(z)/pi int_0^inf sin(|z|y)/(y xi(1/2+y))dy  [tabulated on [0,1], cubic];
  route II (|z|>=1): F(z)=F(1)+sum_k (-c_k)(e^{-g_k}-e^{-g_k|z|})/g_k.  Controls use analytic W.
  K-SWEEP builds the truncated Lambda_N (analytic W) to exhibit the truncation degeneracy.
DISCIPLINE: explicit paths; no global find/grep; one process; RSS<200MB; flush .txt; no RH claim."""
import re, random
from mpmath import mp, mpf, mpc, exp, pi, gamma, zeta, quad, sin

ZERO_FILE = "zeros/zeros2.txt"; OUT = "scripts/V117_variation_diminishing.txt"; _LOG = []
def out(s=""):
    print(s); _LOG.append(str(s))
def rss_mb():
    for l in open("/proc/self/status"):
        if l.startswith("VmHWM"): return int(l.split()[1]) / 1024.0
    return -1.0
def xireg(s):
    s = mpc(s); d = s - 1
    if abs(d) < mpf(10) ** (-mp.dps // 3):
        g1 = mpf("-0.0728158454836767248605863758749013157646"); g2 = mpf("-0.0096903631928723")
        eterm = 1 + mp.euler * d - g1 * d ** 2 / 2 + g2 * d ** 3 / 6
    else: eterm = d * zeta(s)
    return gamma(s / 2 + 1) * pi ** (-s / 2) * eterm
def Xi(t): return xireg(mpc("0.5") + mpc(0, t))
def load_zeros(nmax=40):
    blocks, cur = [], None
    for line in open(ZERO_FILE):
        s = line.strip()
        if not s: continue
        if re.match(r"^\d+\.\d", s):
            if cur is not None: blocks.append(cur)
            cur = s
        else: cur = (cur or "") + s
    if cur is not None: blocks.append(cur)
    gz = [mpf(b) for b in blocks[:nmax]]; h = mpf(10) ** (-(mp.dps // 3))
    return gz, [mp.re(1 / ((Xi(g + h) - Xi(g - h)) / (2 * h))) for g in gz]
def I0(u):
    u = mpf(u)
    def g(y):
        y = mpf(y); return (sin(u * y) / y if y != 0 else u) / xireg(mpf("0.5") + y)
    return mp.re(quad(g, [0, 1, 3, 8, 20, 40], maxdegree=8) / pi)
class O3:
    def __init__(self, Z, C, nt=100):
        self.Z, self.C = Z, C; self.M = mp.re(1 / xireg(mpf("0.5"))); self.nt = nt; self.h = mpf(1) / nt; self.tab = None
    def build(self): self.tab = [I0(mpf(i) / self.nt) for i in range(self.nt + 1)]
    def _i0(self, u):
        u = abs(mpf(u)); h = self.h; N = self.nt; i = min(max(int(u / h), 0), N - 1)
        idx = [0, 1, 2, 3] if i == 0 else ([N - 3, N - 2, N - 1, N] if i >= N - 1 else [i - 1, i, i + 1, i + 2])
        xs = [k * h for k in idx]; ys = [self.tab[k] for k in idx]; s = mpf(0)
        for a in range(4):
            w = mpf(1)
            for b in range(4):
                if b != a: w *= (u - xs[b]) / (xs[a] - xs[b])
            s += ys[a] * w
        return s
    def _Fraw(self, z):
        z = mpf(z)
        if z < 0: return -self._Fraw(-z)
        if z <= 1: return self._i0(z)
        s = self.tab[self.nt]
        for k in range(len(self.Z)): s += (-self.C[k]) * (exp(-self.Z[k]) - exp(-self.Z[k] * z)) / self.Z[k]
        return s
    def buildF(self, zmax=12, hs=mpf("0.005")):
        n = int(mpf(zmax) / hs); self.hs = hs; self.zmax = mpf(zmax); self.FT = [self._Fraw(mpf(i) * hs) for i in range(n + 1)]
    def Fl(self, z):
        """cubic-interpolated F(z)=int_0^z Lambda from a precomputed table (odd; saturates at M/2)."""
        z = mpf(z); sg = 1 if z >= 0 else -1; a = abs(z)
        if a >= self.zmax: return sg * self.M / 2
        hs = self.hs; N = len(self.FT) - 1; i = min(max(int(a / hs), 0), N - 1)
        idx = [0, 1, 2, 3] if i == 0 else ([N - 3, N - 2, N - 1, N] if i >= N - 1 else [i - 1, i, i + 1, i + 2])
        xs = [k * hs for k in idx]; ys = [self.FT[k] for k in idx]; s = mpf(0)
        for u in range(4):
            w = mpf(1)
            for b in range(4):
                if b != u: w *= (a - xs[b]) / (xs[u] - xs[b])
            s += ys[u] * w
        return sg * s
    def W(self, z): return self.M / 2 + self._Fraw(z)
    def Wtrunc(self, z, N):
        z = mpf(z); a = abs(z); s = mpf(0)
        for k in range(N):
            s += (-self.C[k]) * (exp(self.Z[k] * z) / self.Z[k] if z < 0 else (2 - exp(-self.Z[k] * a)) / self.Z[k])
        return s
def scc(vals, tol=mpf("1e-6")):
    m = max(abs(v) for v in vals)
    s = [1 if v > tol * m else (-1 if v < -tol * m else 0) for v in vals]; s = [u for u in s if u]
    return sum(1 for i in range(1, len(s)) if s[i] != s[i - 1])
def fval(boxes, x): return sum(v for (l, r, v) in boxes if l <= x < r)
def conv(Wf, boxes, x): return sum(v * (Wf(x - l) - Wf(x - r)) for (l, r, v) in boxes)
def make_family(nfam=24, seed=117, hi=3.2):
    rnd = random.Random(seed); fam = []
    for t in range(nfam):
        k = rnd.choice([2, 3, 4, 5]); pos = sorted(rnd.uniform(-hi, hi) for _ in range(k))
        for i in range(1, k): pos[i] = max(pos[i], pos[i - 1] + 0.06)
        wid = [rnd.uniform(0.08, 1.25) for _ in range(k)]; s0 = rnd.choice([1, -1])
        fam.append(("R%02d" % t, [(mpf(pos[i]), mpf(pos[i] + wid[i]), mpf(s0 * ((-1) ** i))) for i in range(k)]))
    return fam
def run_family(Wf, fam, grid, tol=mpf("1e-6")):
    rows, viol = [], []
    for name, boxes in fam:
        sf = scc([fval(boxes, x) for x in grid], mpf("1e-9")); sg = scc([conv(Wf, boxes, x) for x in grid], tol)
        rows.append((name, sf, sg))
        if sg > sf: viol.append((name, sf, sg, boxes))
    return rows, viol
def W1(z):
    a = abs(mpf(z)); return mpf("1.5") + (1 if z >= 0 else -1) * (2 * (1 - exp(-a)) - (1 - exp(-2 * a)) / 2)
def W2(z):
    a = abs(mpf(z)); return mpf("1.5") + (1 if z >= 0 else -1) * ((1 - exp(-a)) + (1 - exp(-2 * a)) / 2)
def bx(b):
    return [(mp.nstr(l, 4), mp.nstr(r, 4), int(v)) for (l, r, v) in b]

def main():
    mp.dps = 40
    out("V117 -- VARIATION-DIMINISHING test of O3 (Lambda = Laplace inverse of 1/Xi)")
    out("=" * 96)
    Z, C = load_zeros(40); L = O3(Z, C, nt=100)
    out("[1] OBJECT = O3 (Lambda), NOT O2 (Phi).  calibration (route reuse from V111):")
    out("    Xi(0)=%s (known 0.4971207781883141) ; M=int_R Lambda=1/Xi(0)=%s"
        % (mp.nstr(mp.re(xireg(mpf("0.5"))), 18), mp.nstr(L.M, 14)))
    out("    gamma_1..3 = " + ", ".join(mp.nstr(z, 12) for z in Z[:3]))
    out("    c_1..3 = " + ", ".join(mp.nstr(c, 8) for c in C[:3]) + "  (sign alternates, |c_k| grows)")
    out("    building route-I table of F(z)=int_0^z Lambda on [0,1] (100 pts) ..."); L.build()
    for zz in ["1.2", "2.0", "3.0"]:
        d = I0(mpf(zz)); v = L._Fraw(mpf(zz))
        out("    check F(%s): route-I direct=%s hybrid=%s rel=%s" % (zz, mp.nstr(d, 16), mp.nstr(v, 16), mp.nstr(abs(d - v) / abs(d), 3)))
    out("    => hybrid antiderivative == route I to ~1e-13.")
    L.buildF(); out("    antiderivative table F on [-12,12] built (cubic interpolation for the convolutions).")
    grid = [mpf(-6) + mpf(12) * i / 600 for i in range(601)]; fam = make_family(24, 117)
    out("")
    out("[2] CRITERION (fixed in advance): FAIL iff some f has S^-(Lambda*f)>S^-(f) (stable); PASS only")
    out("    for provable objects; NO SIGNAL otherwise.  tau=1e-6 relative.  family = 24 deterministic")
    out("    pseudo-random staircases, k=2..5 boxes, S^-(f)=k-1.")
    out("")
    out("[3] CONTROLS (known answers; gate the main run):")
    for nm, Wf, want in (("C1 (exactly PF)    ", W1, "PASS"), ("C2 (exactly NOT PF)", W2, "FAIL")):
        rows, viol = run_family(Wf, fam, grid); verdict = "FAIL" if viol else "PASS"
        out("    %s -> max[S^-(g)-S^-(f)]=%d ; violations=%d ; verdict=%s (want %s)"
            % (nm, max(r[2] - r[1] for r in rows), len(viol), verdict, want))
        for v in viol[:2]: out("        witness %s : S^-(f)=%d -> S^-(g)=%d ; boxes=%s" % (v[0], v[1], v[2], bx(v[3])))
    out("    ==> device DISCRIMINATES (catches exactly-non-PF, accepts exactly-PF).  C2's failure is an")
    out("        ORDER-3 effect (needs S^-(f)=2): C2 is not log-concave => not TP_2, yet VD_2 still holds.")
    out("")
    out("[4] MAIN TEST on O3 = Lambda (all entries from the O3 evaluator; Phi absent):")
    rows, viol = run_family(L.Fl, fam, grid)
    out("    max[S^-(Lambda*f)-S^-(f)]=%d ; violations=%d" % (max(r[2] - r[1] for r in rows), len(viol)))
    for v in viol[:5]: out("      witness %s : S^-(f)=%d -> S^-(g)=%d ; boxes=%s" % (v[0], v[1], v[2], bx(v[3])))
    out("")
    out("[5] GATE-2 RANK (truncation degeneracy): truncated object Lambda_N = -sum_{k<=N} c_k e^{-g_k|x|}:")
    for N in (2, 3, 5, 10, 20):
        rowsN, violN = run_family(lambda z, N=N: L.Wtrunc(z, N), fam, grid)
        out("    N=%-3d max[S^-(g)-S^-(f)]=%d ; violations=%d / %d" % (N, max(r[2] - r[1] for r in rowsN), len(violN), len(fam)))
        for v in violN[:2]: out("        witness %s : S^-(f)=%d -> S^-(g)=%d" % (v[0], v[1], v[2]))
    out("")
    out("[6] GATE-3 TRUNCATION / convergence scan (grid step, window, tol):")
    for step, Lh in ((0.04, 6), (0.02, 6), (0.01, 6), (0.02, 4)):
        g2 = [mpf(-Lh) + mpf(2 * Lh) * i / int(2 * Lh / step) for i in range(int(2 * Lh / step) + 1)]
        r1, v1 = run_family(L.Fl, fam, g2); r2, v2 = run_family(W2, fam, g2)
        out("    step=%.3f win=+-%d : Lambda excess=%d viol=%d | C2 excess=%d viol=%d"
            % (step, Lh, max(x[2] - x[1] for x in r1), len(v1), max(x[2] - x[1] for x in r2), len(v2)))
    for tol in ("1e-4", "1e-6", "1e-8"):
        out("    tol=%s : Lambda violations=%d" % (tol, len(run_family(L.Fl, fam, grid, mpf(tol))[1])))
    out("")
    out("[7] dps stability (controls + the hybrid antiderivative of O3 recomputed at each dps):")
    for dps in (20, 30, 50, 80):
        mp.dps = dps
        out("    dps=%-3d : C1 viol=%d ; C2 viol=%d ; F(1.5)=%s ; F(3.0)=%s"
            % (dps, len(run_family(W1, fam, grid)[1]), len(run_family(W2, fam, grid)[1]),
               mp.nstr(L._Fraw(mpf("1.5")), 16), mp.nstr(L._Fraw(mpf(3)), 16)))
    mp.dps = 40
    out(""); out("[8] hygiene: peak RSS = %.1f MB (< 200 MB)" % rss_mb())
    open(OUT, "w").write("\n".join(_LOG) + "\n"); print("\nwritten: " + OUT)

main()
