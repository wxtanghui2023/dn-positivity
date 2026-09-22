#!/usr/bin/env python3
"""C-380 (2,2,1) certified-infeasibility experiment -- EXECUTOR.

Spec: docs/C380-221-COMPUTATION-SPEC-FREEZE.md  (§15 execution protocol, §16 dry-run gate)

Object fixed by spec:
    Theta = { (th_a, th_b, th_c) : 0 <= th_b <= th_a <= pi }
    F_q(th) = 2 cos(q th_a) + 2 cos(q th_b) + cos(q th_c),  q = 1..12
    goal:  for all th in Theta,  max_q F_q(th) > 1/2

Method (spec 15.3/15.4/15.5):
    one witness q per box; variables separate so
        L_q(B) = 2*CosMin(q,Ia) + 2*CosMin(q,Ib) + CosMin(q,Ic)  <=  inf_B F_q
    only a *certified outward-enveloped* bound L_q(B) > 1/2 certifies a box.

Implementation choice (stronger, one fewer dependency):
    we tile the FULL cube [0,pi]^3  (which contains Theta), so no symmetry
    reduction is used and no reliance on it is declared.

Modes:
    --dryrun : the six instrument validations of spec section 16 (no B1 budget)
    --b1     : batch 1 coarse sweep + adaptive bisection, time-capped
    --selftest : pure logic checks of CosMin/CosMax (used inside dryrun)
"""
import argparse
import math
import os
import sys
import time
from fractions import Fraction

import numpy as np

PI = math.pi
INFL = 1e-12          # outward inflation: >> float64 error (~1e-16), << margins (~0.4)
HALF = 0.5


# ----------------------------------------------------------------------------
# 1-D certified bounds for cos(q t) on t in [u,v]   (spec 15.4)
# ----------------------------------------------------------------------------
def cos_min(q, u, v):
    """Certified lower bound of min_{t in [u,v]} cos(q t)."""
    s = q * u - INFL
    e = q * v + INFL
    val = min(math.cos(s), math.cos(e)) - INFL
    # interior odd multiples of pi give the minimum -1
    k = math.ceil((s / PI - 1.0) / 2.0)
    if (2 * k + 1) * PI <= e:
        return -1.0 - INFL
    return val


def cos_max(q, u, v):
    """Certified upper bound of max_{t in [u,v]} cos(q t)."""
    s = q * u - INFL
    e = q * v + INFL
    val = min(1.0 + INFL, max(math.cos(s), math.cos(e)) + INFL)
    # interior even multiples of pi give the maximum +1
    k = math.ceil(s / (2.0 * PI))
    if 2.0 * k * PI <= e and 2.0 * k * PI >= s:
        return 1.0 + INFL
    return val


def F_lower(q, B):
    """Certified lower bound L_q(B) <= inf_B F_q."""
    return (2.0 * cos_min(q, B[0], B[1])
            + 2.0 * cos_min(q, B[2], B[3])
            + cos_min(q, B[4], B[5]))


def F_upper(q, B):
    """Certified upper bound >= sup_B F_q."""
    return (2.0 * cos_max(q, B[0], B[1])
            + 2.0 * cos_max(q, B[2], B[3])
            + cos_max(q, B[4], B[5]))


def F_point(q, th):
    return 2.0 * math.cos(q * th[0]) + 2.0 * math.cos(q * th[1]) + math.cos(q * th[2])


def certify_box(B):
    """Return (q, L) if some witness q certifies B, else (None, None)."""
    for q in range(1, 13):
        L = F_lower(q, B)
        if L > HALF:
            return q, L
    return None, None


def s3_check(B):
    """S3: certified upper bounds show all twelve F_q <= 1/2 on B."""
    if all(F_upper(q, B) <= HALF for q in range(1, 13)):
        return True
    return False


def bisect(B):
    """Spec 15.6: split along the longest edge; tie-break a -> b -> c."""
    w = [B[1] - B[0], B[3] - B[2], B[5] - B[4]]
    i = int(np.argmax(np.array(w)))          # argmax takes the first maximum => a,b,c order
    l, u = B[2 * i], B[2 * i + 1]
    m = 0.5 * (l + u)
    B1 = list(B); B2 = list(B)
    B1[2 * i + 1] = m
    B2[2 * i] = m
    return tuple(B1), tuple(B2)


# ----------------------------------------------------------------------------
# instrument self-tests (spec 15.4 correctness of the extremum logic)
# ----------------------------------------------------------------------------
def selftest(verbose=True):
    ok = True
    rng = np.random.default_rng(20260922)
    # (1) exact cases
    cases = [
        (1, 0.0, PI),          # cos t: min -1 (interior pi)
        (2, 0.0, PI / 2),      # cos 2t: interval [0,pi] -> min -1
        (5, 0.0, PI / 5),      # cos 5t on [0,pi/5] -> t=0 gives 1, no interior min -> min 0
        (3, 0.3, 0.31),        # no critical point -> endpoints
        (12, 2.0, 2.05),       # high q, wide image
    ]
    for (q, u, v) in cases:
        lo = cos_min(q, u, v)
        hi = cos_max(q, u, v)
        xs = np.linspace(u, v, 200001)
        true_min = float(np.min(np.cos(q * xs)))
        true_max = float(np.max(np.cos(q * xs)))
        if not (lo <= true_min + 1e-9 and hi >= true_max - 1e-9):
            ok = False
            print(f"  [FAIL] q={q} [{u},{v}] lo={lo} true_min={true_min} hi={hi} true_max={true_max}")
    # (2) randomized conservativity: bounds must hold at every sampled point
    nbad = 0
    for _ in range(300):
        q = int(rng.integers(1, 13))
        u = float(rng.uniform(0, PI)); v = float(rng.uniform(u, PI))
        lo = cos_min(q, u, v); hi = cos_max(q, u, v)
        xs = rng.uniform(u, v, 4000)
        vals = np.cos(q * xs)
        if lo > float(np.min(vals)) + 1e-9 or hi < float(np.max(vals)) - 1e-9:
            nbad += 1
    if nbad:
        ok = False
        print(f"  [FAIL] randomized conservativity violations: {nbad}/300")
    if verbose:
        print(f"  selftest: exact cases + randomized conservativity -> {'PASS' if ok else 'FAIL'}")
    return ok


# ----------------------------------------------------------------------------
# DRY RUN (spec section 16): six instrument validations
# ----------------------------------------------------------------------------
def dryrun(outdir, N0=8):
    os.makedirs(outdir, exist_ok=True)
    rep = []
    t0 = time.time()
    print("=" * 78)
    print("C-380 (2,2,1) DRY RUN -- spec section 16, six validations")
    print("=" * 78)

    # ---- item 2: CosMin / CosMax extremum logic ----
    print("\n[item 2] CosMin / CosMax extremum logic")
    ok2 = selftest()
    rep.append(("item2_cosmin_logic", ok2))

    # ---- item 1: box generation ----
    print("\n[item 1] box generation (initial division fixed in advance)")
    h = PI / N0
    boxes = []
    for i in range(N0):
        for j in range(N0):
            for k in range(N0):
                boxes.append((i * h, (i + 1) * h, j * h, (j + 1) * h, k * h, (k + 1) * h))
    total_vol = sum((b[1] - b[0]) * (b[3] - b[2]) * (b[5] - b[4]) for b in boxes)
    print(f"  N0={N0}  boxes={len(boxes)}  total volume={total_vol:.12f}  (pi^3={PI**3:.12f})")
    ok1 = abs(total_vol - PI ** 3) < 1e-9 and len(boxes) == N0 ** 3
    print(f"  sample box B0 = {tuple(round(x, 9) for x in boxes[0])}")
    rep.append(("item1_box_generation", ok1))

    # ---- item 3: outward rounding is conservative ----
    print("\n[item 3] outward rounding: certified lower bounds must never exceed sampled truth")
    rng = np.random.default_rng(7)
    worst_slack = 1e9
    viol = 0
    for _ in range(200):
        b = boxes[int(rng.integers(0, len(boxes)))]
        pts = [rng.uniform(b[0], b[1]), rng.uniform(b[2], b[3]), rng.uniform(b[4], b[5])]
        for q in range(1, 13):
            L = F_lower(q, b)
            f = F_point(q, pts)
            if L > f + 1e-12:
                viol += 1
            worst_slack = min(worst_slack, f - L)
    print(f"  violations={viol}/2400   min (F_point - L) = {worst_slack:.6f}  (>=0 required)")
    ok3 = (viol == 0)
    rep.append(("item3_outward_rounding", ok3))

    # ---- item 5: an unresolved box must enter bisection correctly ----
    print("\n[item 5] unresolved box -> fixed-rule bisection")
    big = (0.0, PI, 0.0, PI, 0.0, PI)              # deliberately coarse
    q, L = certify_box(big)
    unresolved_demo = (q is None)
    print(f"  coarse box certify attempt: witness={q} L={L} -> {'UNRESOLVED (expected)' if unresolved_demo else 'certified'}")
    B1, B2 = bisect(big)
    w = [big[1] - big[0], big[3] - big[2], big[5] - big[4]]
    split_axis = int(np.argmax(np.array(w)))
    ok5 = (unresolved_demo
           and abs((B1[1] - B1[0]) + (B2[1] - B2[0]) - (big[1] - big[0])) < 1e-15
           and (B1[1] == B2[0] or B1[3] == B2[2] or B1[5] == B2[4]))
    print(f"  split on axis {split_axis} ('a','b','c'[axis]); children share a face, volumes add up -> {'ok' if ok5 else 'FAIL'}")
    rep.append(("item5_bisection", ok5))

    # ---- item 4 + 6: write a tiny certificate and let the INDEPENDENT checker verify it ----
    print("\n[item 4+6] certificate emission + independent checker (coverage + recomputation)")
    cert_path = os.path.join(outdir, "dryrun_certificate.tsv")
    resid_path = os.path.join(outdir, "dryrun_residual.tsv")
    ncert, unres = 0, []
    cells = []
    DEPTH_CAP = 9                      # box edge >= pi/2^12  (dyadic on pi/2^12, per spec 15/16)
    stack = [(b, 0) for b in boxes]
    s3_hits = 0
    while stack:
        b, d = stack.pop()
        q, L = certify_box(b)
        if q is not None:
            ncert += 1
            cells.append(b + (q, L))
            continue
        if s3_check(b):
            print(f"  [S3] certified box with all F_q <= 1/2: {b}  -> STOP (anomaly)")
            s3_hits += 1
            unres.append(b)
            continue
        if d >= DEPTH_CAP:
            unres.append(b)            # kept in the residual set (NEVER dropped)
            continue
        c1, c2 = bisect(b)
        stack.append((c1, d + 1))
        stack.append((c2, d + 1))
    with open(cert_path, "w") as f:
        f.write("# C380-221 DRY-RUN CERTIFICATE (complete tiling of [0,pi]^3 at depth cap 9)\n")
        f.write("# a1 a2 b1 b2 c1 c2 witness_q certified_lower_bound\n")
        for b in cells:
            f.write(" ".join(f"{x:.17g}" for x in b[:6]) + f" {b[6]} {b[7]:.17g}\n")
    with open(resid_path, "w") as f:
        for b in unres:
            f.write(" ".join(f"{x:.17g}" for x in b) + "\n")
    vol = lambda B: (B[1] - B[0]) * (B[3] - B[2]) * (B[5] - B[4])
    print(f"  certified boxes written: {ncert}   unresolved boxes: {len(unres)}"
          f"   S3 hits: {s3_hits}")
    print(f"  raw coverage = {sum(vol(b[:6]) for b in cells) / PI**3:.6f}")
    chk = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "c380_90b_certificate_checker.py")
    print(f"  running independent checker: {chk} CERT RESID")
    rc = os.system(f"{sys.executable} {chk} {cert_path} {resid_path}")
    ok46 = (rc == 0)
    rep.append(("item4_independent_recompute+item6_coverage", ok46))
    rep.append(("item1b_no_S3_anomaly", s3_hits == 0))

    print("\n" + "=" * 78)
    print(f"DRY RUN elapsed {time.time() - t0:.2f} s")
    for name, ok in rep:
        print(f"   {name:38s} : {'PASS' if ok else 'FAIL'}")
    allok = all(ok for _, ok in rep)
    print(f"DRY RUN VERDICT: {'PASS -- instrument validated' if allok else 'FAIL'}")
    print("=" * 78)
    return allok


# ----------------------------------------------------------------------------
# OFFICIAL BATCH 1  (spec 15.6): initial division fixed in advance, adaptive bisection
# ----------------------------------------------------------------------------
def run_b1(outdir, N0, DEPTH_CAP):
    """Coarse sweep + adaptive bisection. Returns True iff the cover is complete.

    Pre-fixed before the run (never changed during it):
        initial division  N0 x N0 x N0  with h = pi/N0
        bisection rule    longest edge, tie-break a -> b -> c
        certification     only an outward-enveloped L_q(B) > 1/2 counts
        depth cap         DEPTH_CAP
    """
    os.makedirs(outdir, exist_ok=True)
    t0 = time.time()
    h = PI / N0
    stack = []
    for i in range(N0):
        for j in range(N0):
            for k in range(N0):
                stack.append(((i * h, (i + 1) * h, j * h, (j + 1) * h, k * h, (k + 1) * h), 0))
    n0_boxes = len(stack)
    cert_cells, resid = [], []
    s3 = 0
    maxdepth = 0
    while stack:
        b, d = stack.pop()
        maxdepth = max(maxdepth, d)
        q, L = certify_box(b)
        if q is not None:
            cert_cells.append(b + (q, L))
            continue
        if s3_check(b):
            print(f"[B1][S3] box with all F_q <= 1/2 (certified): {b}  -> STOP, report anomaly")
            s3 += 1
            resid.append(b)
            continue
        if d >= DEPTH_CAP:
            resid.append(b)
            continue
        c1, c2 = bisect(b)
        stack.append((c1, d + 1))
        stack.append((c2, d + 1))
    vol = lambda B: (B[1] - B[0]) * (B[3] - B[2]) * (B[5] - B[4])
    vcert = sum(vol(b[:6]) for b in cert_cells)
    vres = sum(vol(b) for b in resid)
    cov = vcert / PI ** 3
    cert_path = os.path.join(outdir, "C380-221-CERTIFICATE.tsv")
    resid_path = os.path.join(outdir, "C380-221-RESIDUAL.tsv")
    with open(cert_path, "w") as f:
        f.write("# C380-221 CERTIFICATE (official, batch 1)\n")
        f.write(f"# initial division N0={N0} (h=pi/{N0}); bisection: longest edge, tie-break a,b,c\n")
        f.write(f"# depth cap {DEPTH_CAP}; outward inflation 1e-12; strict criterion L > 1/2\n")
        f.write("# a1 a2 b1 b2 c1 c2 witness_q certified_lower_bound\n")
        for b in cert_cells:
            f.write(" ".join(f"{x:.17g}" for x in b[:6]) + f" {b[6]} {b[7]:.17g}\n")
    with open(resid_path, "w") as f:
        for b in resid:
            f.write(" ".join(f"{x:.17g}" for x in b) + "\n")
    el = time.time() - t0
    print(f"[B1] initial boxes={n0_boxes}  certified={len(cert_cells)}  residual={len(resid)}")
    print(f"[B1] coverage={cov:.9f}  volume residual={vres:.12g}  max depth={maxdepth}"
          f"  S3 hits={s3}  elapsed={el:.2f} s")
    print(f"[B1] certificate -> {cert_path}")
    print(f"[B1] residual    -> {resid_path}")
    return (len(resid) == 0 and s3 == 0)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--dryrun", action="store_true")
    ap.add_argument("--b1", action="store_true")
    ap.add_argument("--outdir", default="dryrun_out")
    ap.add_argument("--n0", type=int, default=8)
    ap.add_argument("--depth", type=int, default=12)
    a = ap.parse_args()
    if a.dryrun:
        ok = dryrun(a.outdir, a.n0)
        sys.exit(0 if ok else 1)
    if a.b1:
        sys.exit(0 if run_b1(a.outdir, a.n0, a.depth) else 1)
    print("use --dryrun (instrument validation) or --b1 (official batch 1)")
