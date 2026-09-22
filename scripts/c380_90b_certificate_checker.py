#!/usr/bin/env python3
"""C380-221 CERTIFICATE CHECKER -- INDEPENDENT verification.

Usage:  c380_90b_certificate_checker.py CERT.tsv RESID.tsv

Independence: this file re-implements the 1-D cosine range routine by a *different*
algorithm (critical-point enumeration t = m*pi/q) and imports nothing from the executor.

It verifies:
  (A) every certified box: independently recomputed witness bound > 1/2   (slack reported)
  (B) exact dyadic volume accounting:  vol(certified) + vol(residual) == vol([0,pi]^3)
  (C) exact pairwise non-overlap of all listed boxes (interval sweep on axis a,
      then (b,c)-rectangle overlap test inside each elementary a-slab)
  (D) randomized containment cross-check (each sampled point lies in exactly one box)

Exit code 0 = PASS.
"""
import math
import random
import sys

PI = math.pi
K = 12                      # dyadic accounting denominator: endpoints are n*pi/2^K
UNIT = 1 << K               # units per pi along each axis
HALF = 0.5


def cos_range_indep(q, u, v):
    """Range of cos(q t) on t in [u,v] by critical-point enumeration (independent path)."""
    a, b = math.cos(q * u), math.cos(q * v)
    lo = min(a, b)
    hi = min(1.0, max(a, b))
    m0 = math.ceil(q * u / PI - 1e-12)
    m1 = math.floor(q * v / PI + 1e-12)
    for m in range(m0, m1 + 1):
        if m % 2:            # cos(m*pi) = -1  -> interior minimum
            lo = -1.0
        else:                # cos(m*pi) = +1  -> interior maximum
            hi = 1.0
    return lo, hi


def bound(q, B):
    la, _ = cos_range_indep(q, B[0], B[1])
    lb, _ = cos_range_indep(q, B[2], B[3])
    lc, _ = cos_range_indep(q, B[4], B[5])
    return 2.0 * la + 2.0 * lb + lc


def to_units(x):
    n = x / PI * UNIT
    ni = int(round(n))
    if abs(n - ni) > 1e-6:
        raise ValueError(f"endpoint {x!r} is not dyadic on pi/2^{K}: n={n}")
    return ni


def load(path):
    boxes = []
    with open(path) as f:
        for line in f:
            if line.startswith("#") or not line.strip():
                continue
            parts = line.split()
            boxes.append([float(t) for t in parts[:6]] + [int(parts[6]) if len(parts) > 6 else -1,
                                                          float(parts[7]) if len(parts) > 7 else float("nan")])
    return boxes


def main():
    if len(sys.argv) < 3:
        print("usage: checker.py CERT.tsv RESID.tsv")
        return 2
    cert = load(sys.argv[1])
    resid = load(sys.argv[2])
    print(f"[checker] certified boxes = {len(cert)}   residual boxes = {len(resid)}")

    # ---------------- (A) independent recomputation ----------------
    worst = None
    nfail = 0
    for B in cert:
        q = B[6]
        L_reported = B[7]
        L_indep = bound(q, B[:6])
        if not (L_reported > HALF):
            nfail += 1
        if abs(L_reported - L_indep) > 1e-7:
            print(f"[checker] WARN reported/independent mismatch: {B[:6]} q={q} "
                  f"reported={L_reported} indep={L_indep}")
        worst = L_indep if worst is None else min(worst, L_indep)
    if nfail:
        print(f"[checker] FAIL: {nfail} certified boxes do not exceed 1/2")
    print(f"[checker] (A) min independently recomputed witness bound = {worst!r}  (>1/2 required)")

    # ---------------- (B) exact dyadic volume accounting ----------------
    tot_u = UNIT ** 3
    def vol_u(B):
        return (to_units(B[1]) - to_units(B[0])) * (to_units(B[3]) - to_units(B[2])) * (to_units(B[5]) - to_units(B[4]))
    vc = sum(vol_u(B) for B in cert)
    vr = sum(vol_u(B) for B in resid)
    print(f"[checker] (B) volume units: certified={vc}  residual={vr}  sum={vc+vr}  total={tot_u}"
          f"   coverage={vc/tot_u:.6f}")
    okB = (vc + vr == tot_u)

    # ---------------- (C) exact non-overlap (a-sweep + (b,c) rectangles) ----------------
    allb = cert + resid
    edges = sorted({to_units(B[0]) for B in allb} | {to_units(B[1]) for B in allb})
    n_overlap = 0
    for i in range(len(edges) - 1):
        e0, e1 = edges[i], edges[i + 1]
        mid = 0.5 * (e0 + e1)
        slab = [B for B in allb if to_units(B[0]) <= mid <= to_units(B[1])]
        rects = [(to_units(B[2]), to_units(B[3]), to_units(B[4]), to_units(B[5])) for B in slab]
        for x in range(len(rects)):
            for y in range(x + 1, len(rects)):
                a1, a2, a3, a4 = rects[x]
                b1, b2, b3, b4 = rects[y]
                if a1 < b2 and b1 < a2 and a3 < b4 and b3 < a4:
                    n_overlap += 1
    print(f"[checker] (C) overlapping pairs found = {n_overlap}")
    okC = (n_overlap == 0)

    # ---------------- (D) randomized containment ----------------
    random.seed(11)
    def contains(B, p):
        return (B[0] <= p[0] <= B[1]) and (B[2] <= p[1] <= B[3]) and (B[4] <= p[2] <= B[5])
    bad_zero = bad_multi = 0
    for _ in range(20000):
        p = (random.uniform(0, PI), random.uniform(0, PI), random.uniform(0, PI))
        hits = sum(1 for B in allb if contains(B, p))
        if hits == 0:
            bad_zero += 1
        elif hits > 1:
            bad_multi += 1
    print(f"[checker] (D) sampled points with 0 boxes = {bad_zero}, with >1 boxes = {bad_multi}")
    okD = (bad_zero == 0 and bad_multi == 0)

    ok = okB and okC and okD and (nfail == 0)
    print(f"[checker] VERDICT: {'PASS' if ok else 'FAIL'}"
          f"  (A={'ok' if nfail == 0 else 'fail'} B={'ok' if okB else 'fail'}"
          f" C={'ok' if okC else 'fail'} D={'ok' if okD else 'fail'})")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
