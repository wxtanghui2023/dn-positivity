#!/usr/bin/env python3
"""C-380 K4 SCALE PROBE  (<= 15 min, feasibility gate ONLY -- not a proof).

Spec: docs/C380-K4-GATE-FREEZE.md  sections 6/7/9.
Object: F_q(theta) = 2cos(q th1) + cos(q th2) + cos(q th3) + cos(q th4),  theta in [0,pi]^4, q = 1..12.
Question answered here: can adaptive dyadic subdivision compress the remaining region to a
budget-affordable order of magnitude?  (NOT "is K4 proved".)

Mandatory outputs:
  (1) initial boxes / depth
  (2) box-count growth curve after subdivision
  (3) thinnest margin location and order of magnitude
  (4) estimated full-certificate scale, with the inference basis
Anomaly check (immediate STOP + report if found):
  a box B with  sup_B F_q <= 1/2  for all twelve q   (S3-class: potential counterexample region)
"""
import argparse
import math
import time

import numpy as np

PI = math.pi
INFL = 1e-12

# ---- vectorised certified 1-D cosine bounds (same logic validated on (2,2,1)) ----
def cos_min_vec(q, U, V):
    s = q * U - INFL
    e = q * V + INFL
    val = np.minimum(np.cos(s), np.cos(e)) - INFL
    k = np.ceil((s / PI - 1.0) / 2.0)
    interior = (2.0 * k + 1.0) * PI <= e
    return np.where(interior, -1.0 - INFL, val)


def cos_max_vec(q, U, V):
    s = q * U - INFL
    e = q * V + INFL
    val = np.minimum(1.0 + INFL, np.maximum(np.cos(s), np.cos(e)) + INFL)
    k = np.ceil(s / (2.0 * PI))
    interior = (2.0 * k * PI <= e) & (2.0 * k * PI >= s)
    return np.where(interior, 1.0 + INFL, val)


def Lq(q, B):
    return (2.0 * cos_min_vec(q, B[:, 0], B[:, 1])
            + cos_min_vec(q, B[:, 2], B[:, 3])
            + cos_min_vec(q, B[:, 4], B[:, 5])
            + cos_min_vec(q, B[:, 6], B[:, 7]))


def Uq(q, B):
    return (2.0 * cos_max_vec(q, B[:, 0], B[:, 1])
            + cos_max_vec(q, B[:, 2], B[:, 3])
            + cos_max_vec(q, B[:, 4], B[:, 5])
            + cos_max_vec(q, B[:, 6], B[:, 7]))


def classify(B):
    """returns (witness q, best lower bound, max upper bound over q)"""
    best = np.full(len(B), -1e18)
    bestq = np.zeros(len(B), dtype=int)
    maxU = np.full(len(B), -1e18)
    for q in range(1, 13):
        L = Lq(q, B)
        upd = L > best
        best = np.where(upd, L, best)
        bestq = np.where(upd, q, bestq)
        maxU = np.maximum(maxU, Uq(q, B))
    return bestq, best, maxU


def bisect(B):
    """split each box along its longest edge; tie-break coordinate 1 -> 4"""
    W = np.stack([B[:, 1] - B[:, 0], B[:, 3] - B[:, 2], B[:, 5] - B[:, 4], B[:, 7] - B[:, 6]], axis=1)
    idx = np.argmax(W, axis=1)
    A = B.copy()
    C = B.copy()
    for i in range(4):
        m = (B[:, 2 * i] + B[:, 2 * i + 1]) / 2.0
        sel = idx == i
        A[sel, 2 * i + 1] = m[sel]
        C[sel, 2 * i] = m[sel]
    return A, C


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--n0", type=int, default=8)
    ap.add_argument("--maxdepth", type=int, default=16)
    ap.add_argument("--timecap", type=float, default=840.0)   # <= 15 min incl. margin
    ap.add_argument("--boxcap", type=int, default=2_000_000)
    a = ap.parse_args()

    t0 = time.time()
    h = PI / a.n0
    g = np.arange(a.n0) * h
    A1, A2 = np.meshgrid(g, g, indexing="ij")
    B1, B2 = np.meshgrid(g, g, indexing="ij")
    A1 = A1.ravel(); A2 = A1 + h
    # build the 4-D grid explicitly (n0^4 boxes) in chunks to limit memory
    boxes = []
    per = a.n0 ** 2
    for i in range(a.n0):
        for j in range(a.n0):
            x = np.arange(a.n0) * h
            y = np.arange(a.n0) * h
            XX, YY = np.meshgrid(x, y, indexing="ij")
            blk = np.empty((a.n0 * a.n0, 8))
            blk[:, 0] = i * h; blk[:, 1] = (i + 1) * h
            blk[:, 2] = j * h; blk[:, 3] = (j + 1) * h
            blk[:, 4] = XX.ravel(); blk[:, 5] = blk[:, 4] + h
            blk[:, 6] = YY.ravel(); blk[:, 7] = blk[:, 6] + h
            boxes.append(blk)
    B = np.vstack(boxes)
    print(f"[probe] spec: F_q = 2cos(q th1)+cos(q th2)+cos(q th3)+cos(q th4), theta in [0,pi]^4, q=1..12", flush=True)
    print(f"[probe] OUTPUT 1 (initial): N0={a.n0}  initial boxes = {len(B)}  initial edge h = pi/{a.n0} = {h:.6f}", flush=True)
    print(f"[probe] caps: maxdepth={a.maxdepth}  timecap={a.timecap:.0f}s  boxcap={a.boxcap}", flush=True)

    level = 0
    curve = []
    thin_margin = None
    thin_box = None
    s3_hits = 0
    status = "maxdepth-reached"
    while True:
        if time.time() - t0 > a.timecap:
            status = "time-cap"
            break
        if len(B) > a.boxcap:
            status = "box-cap"
            break
        q, L, maxU = classify(B)
        cert = L > 0.5
        s3 = maxU <= 0.5
        if s3.any():
            s3_hits = int(s3.sum())
            print(f"[probe][S3-ANOMALY] {s3_hits} box(es) with sup_B F_q <= 1/2 for ALL q at level {level}", flush=True)
            print(f"[probe][S3-ANOMALY] example box = {B[np.argmax(s3)]}", flush=True)
            status = "S3-anomaly"
            curve.append((level, len(B), int(cert.sum()), int((~cert).sum()), np.nan))
            break
        resid = B[~cert]
        mcert = float(L[cert].min()) if cert.any() else float("nan")
        if cert.any():
            if thin_margin is None or mcert < thin_margin:
                thin_margin = mcert
                thin_box = B[np.argmin(np.where(cert, L, np.inf))]
        curve.append((level, len(B), int(cert.sum()), int(resid.shape[0]), mcert))
        print(f"[probe] level {level:2d}: leaves={len(B):8d}  certified={int(cert.sum()):8d}  "
              f"residual={resid.shape[0]:7d}  min_cert_margin={mcert:.6g}  edge={PI/(a.n0*2**level):.3e}",
              flush=True)
        if resid.shape[0] == 0:
            status = "FULL-COVER"
            break
        if level >= a.maxdepth:
            status = "maxdepth-reached"
            break
        # adaptive bisection of the unresolved set only
        A, C = bisect(resid)
        B = np.vstack([B[cert], A, C]) if cert.any() else np.vstack([A, C])
        level += 1

    el = time.time() - t0
    print("\n" + "=" * 78, flush=True)
    print(f"[probe] OUTPUT 2 (growth curve):  level | leaves | certified | residual | min cert margin", flush=True)
    for (lv, n, c, r, m) in curve:
        print(f"[probe]   {lv:2d} | {n:8d} | {c:8d} | {r:7d} | {m:.6g}", flush=True)

    print(f"\n[probe] OUTPUT 3 (thinnest certified margin): {thin_margin}", flush=True)
    if thin_box is not None:
        print(f"[probe]   attained on box {np.round(thin_box, 6).tolist()}", flush=True)
        print(f"[probe]   order of magnitude: {thin_margin - 0.5:.3e} above 1/2", flush=True)

    # ---- OUTPUT 4: estimated full-certificate scale, with inference basis ----
    print(f"\n[probe] OUTPUT 4 (scale estimate):", flush=True)
    res = [(lv, r) for (lv, n, c, r, m) in curve if r > 0]
    if len(res) >= 2:
        lv = np.array([x[0] for x in res], float)
        rr = np.array([x[1] for x in res], float)
        mask = rr > 0
        slope = float(np.polyfit(lv[mask], np.log2(rr[mask]), 1)[0])
        d_eff = slope
        print(f"[probe]   residual growth per level: slope = {slope:.3f} bits/level "
              f"=> effective dimension of residual set ~ {d_eff:.2f} (in 4-D ambient)", flush=True)
        # resolution needed: 60*h < thinnest margin  (60 = 5*q_max)
        if thin_margin is not None:
            need_h = (thin_margin - 0.5) / 60.0
            need_level = math.log2(PI / (a.n0 * need_h)) if need_h > 0 else float("inf")
            print(f"[probe]   thinnest margin / 60 => required edge h* = {need_h:.3e} "
                  f"=> required level d* = {need_level:.2f}", flush=True)
            r_now = rr[-1]
            extra = max(0.0, need_level - lv[-1])
            est = r_now * (2 ** (d_eff * extra))
            print(f"[probe]   residual now = {int(r_now)} at level {int(lv[-1])}; extrapolating "
                  f"x 2^({d_eff:.2f} * {extra:.2f}) => estimated residual boxes at d* = {est:.3e}", flush=True)
            print(f"[probe]   (certified boxes ~ initial_{len(B)} + residual, so full-cert scale ~ 1 + "
                  f"{est:.2e} x correction from re-certification)", flush=True)
        else:
            print(f"[probe]   no certified box yet, cannot normalise margin", flush=True)
    else:
        print(f"[probe]   residual empty during probe (see curve) -- no extrapolation needed", flush=True)

    print(f"\n[probe] status = {status}   elapsed = {el:.1f} s   levels run = {level}   "
          f"S3 hits = {s3_hits}", flush=True)
    # ---- classification per the frozen gate ----
    est = None
    if len(res) >= 2 and thin_margin is not None:
        r_now = rr[-1]
        extra = max(0.0, need_level - lv[-1])
        est = r_now * (2 ** (d_eff * extra))
    if status == "S3-anomaly":
        verdict = "S3-STOP (potential counterexample region; report + independent verification)"
    elif status == "FULL-COVER":
        verdict = "FULL-COVER within probe budget (T-a strongly indicated)"
    elif est is None:
        verdict = "INDETERMINATE (insufficient curve)"
    elif est <= 1e5:
        verdict = "<=1e5 : stable growth -> T-a justified"
    elif est <= 1e6:
        verdict = "1e5-1e6 : inspect growth rate and thin region before deciding"
    elif est <= 1e7:
        verdict = "1e6-1e7 : only if a controllable local refinement structure exists"
    else:
        verdict = ">1e7 (or near-exponential) : K4 = GAP/NO-GO candidate; do NOT run full budget"
    print(f"[probe] VERDICT (gate classification): {verdict}", flush=True)
    print("=" * 78, flush=True)


if __name__ == "__main__":
    main()
