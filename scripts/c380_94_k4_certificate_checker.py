#!/usr/bin/env python3
"""K4 T-a CERTIFICATE CHECKER -- INDEPENDENT verification (4 variables, weights 2,1,1,1).

Usage: c380_94_k4_certificate_checker.py CERT.tsv RESID.tsv

Independence: re-implements the 1-D cosine range by critical-point enumeration (different
algorithm from the executor's ceil-based version) and imports nothing from the executor.
Endpoints are exact dyadic integers n with theta = n * pi / 2^K (K read from the header).

Verifies:
 (A) every certified box: independently recomputed witness bound > 1/2
 (B) exact dyadic volume accounting: vol(certified) + vol(residual) == vol([0,pi]^4)
 (C) exact TILING by recursion: each initial cell's listed sub-boxes tile it
     (tries all 4 axes at the cell midpoint; does NOT replicate the executor's rule)
 (D) randomised containment: each sampled point lies in exactly one box

Exit code 0 = PASS.
"""
import bisect
import math
import random
import sys

PI = math.pi
HALF = 0.5


def cos_range_indep(q, u, v):
    a, b = math.cos(q * u), math.cos(q * v)
    lo = min(a, b)
    m0 = math.ceil(q * u / PI - 1e-12)
    m1 = math.floor(q * v / PI + 1e-12)
    for m in range(m0, m1 + 1):
        if m % 2:
            lo = -1.0
    return lo


def bound(q, box, K):
    s = PI / (1 << K)
    lo = 0.0
    for (n1, n2, w) in ((box[0], box[1], 2.0), (box[2], box[3], 1.0),
                        (box[4], box[5], 1.0), (box[6], box[7], 1.0)):
        lo += w * cos_range_indep(q, n1 * s, n2 * s)
    return lo


def load_cert(path):
    K = None
    boxes = []
    with open(path) as f:
        for line in f:
            if line.startswith("#"):
                if line.startswith("# K ="):
                    K = int(line.split("=")[1])
                continue
            if not line.strip():
                continue
            p = line.split()
            boxes.append((tuple(int(x) for x in p[:8]), int(p[8]), float(p[9])))
    return K, boxes


def load_resid(path):
    out = []
    with open(path) as f:
        for line in f:
            if line.startswith("#") or not line.strip():
                continue
            p = line.split()
            out.append(tuple(int(x) for x in p[:8]))
    return out


def inside(b, R):
    return all(R[2 * i] <= b[2 * i] and b[2 * i + 1] <= R[2 * i + 1] for i in range(4))


def tiles(R, S, depth=0):
    """Exact recursive tiling test: do the boxes in S tile the box R?"""
    if not S:
        return False
    if len(S) == 1:
        return S[0] == R
    for axis in range(4):
        mid2 = R[2 * axis] + R[2 * axis + 1]
        if mid2 % 2:
            continue
        mid = mid2 // 2
        if mid <= R[2 * axis] or mid >= R[2 * axis + 1]:
            continue
        R1 = list(R); R1[2 * axis + 1] = mid
        R2 = list(R); R2[2 * axis] = mid
        R1 = tuple(R1); R2 = tuple(R2)
        S1 = [b for b in S if b[2 * axis + 1] <= mid]
        S2 = [b for b in S if b[2 * axis] >= mid]
        if len(S1) + len(S2) == len(S) and S1 and S2:
            if tiles(R1, S1, depth + 1) and tiles(R2, S2, depth + 1):
                return True
    return False


def main():
    if len(sys.argv) < 3:
        print("usage: checker.py CERT.tsv RESID.tsv")
        return 2
    K, cert = load_cert(sys.argv[1])
    resid = load_resid(sys.argv[2])
    print(f"[checker] K = {K}   certified boxes = {len(cert)}   residual boxes = {len(resid)}")

    # ---------- (A) independent recomputation ----------
    worst, nfail, qdist = None, 0, {}
    for (box, q, Lrep) in cert:
        L = bound(q, box, K)
        qdist[q] = qdist.get(q, 0) + 1
        if not (Lrep > HALF):
            nfail += 1
        worst = L if worst is None else min(worst, L)
    print(f"[checker] (A) min independently recomputed witness bound = {worst!r}  (>1/2 required)")
    print(f"[checker] (A) witness-q distribution: {dict(sorted(qdist.items()))}")
    okA = (nfail == 0) and (worst is not None) and (worst > HALF)
    if not okA:
        print(f"[checker] (A) FAIL: {nfail} boxes with reported bound <= 1/2; min indep = {worst}")

    # ---------- (B) exact dyadic volume accounting ----------
    def vol(b):
        v = 1
        for i in range(4):
            v *= (b[2 * i + 1] - b[2 * i])
        return v
    ncells = 1 << K
    tot = ncells ** 4
    vc = sum(vol(b) for (b, _, _) in cert)
    vr = sum(vol(b) for b in resid)
    print(f"[checker] (B) volume: certified={vc} residual={vr} sum={vc + vr} total={tot}  "
          f"coverage={vc / tot:.9f}")
    okB = (vc + vr == tot)

    # ---------- (C) exact tiling by recursion, per initial cell ----------
    allb = [b for (b, _, _) in cert] + list(resid)
    # initial cells: the executor used N0 = 8  => cell edge = ncells/8 units
    n0 = 8
    step = ncells // n0
    grid = {}
    for b in allb:
        key = tuple(int(b[2 * i] // step) for i in range(4))
        grid.setdefault(key, []).append(b)
    bad_cells = 0
    nopart = 0
    for key, S in grid.items():
        R = []
        for i in range(4):
            R += [key[i] * step, (key[i] + 1) * step]
        R = tuple(R)
        if not all(inside(b, R) for b in S):
            nopart += 1
            continue
        if not tiles(R, S):
            bad_cells += 1
    print(f"[checker] (C) initial cells occupied = {len(grid)} ; cells failing tiling = {bad_cells} ; "
          f"boxes outside their cell = {nopart}")
    okC = (bad_cells == 0 and nopart == 0)

    # ---------- (D) randomised containment (vectorised; sanity only -- (B)+(C) carry the exact proof) ----------
    import numpy as _np
    AR = _np.array(allb, dtype=_np.int64)          # (N, 8)
    random.seed(2024)
    bad0 = bad1 = 0
    pts = _np.array([[random.randrange(ncells) for _ in range(4)] for _ in range(2000)], dtype=_np.int64)
    for k in range(0, len(pts), 200):
        block = pts[k:k + 200]                      # (200, 4)
        for pt in block:
            mask = ((AR[:, 0] <= pt[0]) & (pt[0] < AR[:, 1]) &
                    (AR[:, 2] <= pt[1]) & (pt[1] < AR[:, 3]) &
                    (AR[:, 4] <= pt[2]) & (pt[2] < AR[:, 5]) &
                    (AR[:, 6] <= pt[3]) & (pt[3] < AR[:, 7]))
            c = int(mask.sum())
            if c == 0:
                bad0 += 1
            elif c > 1:
                bad1 += 1
    print(f"[checker] (D) sampled points with 0 boxes = {bad0}, with >1 box = {bad1}  "
          f"(vectorised, {len(pts)} points; exact coverage/non-overlap is carried by (B)+(C))")
    okD = (bad0 == 0 and bad1 == 0)

    ok = okA and okB and okC and okD
    print(f"[checker] VERDICT: {'PASS' if ok else 'FAIL'}  "
          f"(A={'ok' if okA else 'fail'} B={'ok' if okB else 'fail'} "
          f"C={'ok' if okC else 'fail'} D={'ok' if okD else 'fail'})")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
