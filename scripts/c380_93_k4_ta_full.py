#!/usr/bin/env python3
"""C-380 K4 T-a FULL CERTIFICATE run  (authorised by Tang's GO, 2026-09-22 18:20).

Spec: docs/C380-K4-GATE-FREEZE.md sections 4/5/7/8.
Target:  for all theta in [0,pi]^4, exists q <= 12 with
             F_q(theta) = 2cos(q th1) + cos(q th2) + cos(q th3) + cos(q th4) > 1/2.

Pre-fixed before the run (never changed during it):
    initial division  N0 = 8  (h = pi/8)              -> 4096 initial boxes
    bisection rule    longest edge, tie-break th1 -> th2 -> th3 -> th4
    certification     single witness q, outward inflation 1e-12, strict L_q(B) > 1/2
    depth cap         20   (hard stop d > 20 without closure trend)
    box cap           2,000,000
Certificate is emitted in EXACT dyadic integer units  n  with  theta = n * pi / 2^K
so the independent checker can verify the tiling arithmetically.
"""
import argparse
import math
import time

import numpy as np

PI = math.pi
INFL = 1e-12
K_DY = 24                       # dyadic denominator exponent: theta = n * pi / 2^K


# ---------------- vectorised certified 1-D cosine bounds ----------------
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
    return (2.0 * cos_min_vec(q, B[:, 0], B[:, 1]) + cos_min_vec(q, B[:, 2], B[:, 3])
            + cos_min_vec(q, B[:, 4], B[:, 5]) + cos_min_vec(q, B[:, 6], B[:, 7]))


def Uq(q, B):
    return (2.0 * cos_max_vec(q, B[:, 0], B[:, 1]) + cos_max_vec(q, B[:, 2], B[:, 3])
            + cos_max_vec(q, B[:, 4], B[:, 5]) + cos_max_vec(q, B[:, 6], B[:, 7]))


def classify(B):
    best = np.full(len(B), -1e18)
    bestq = np.zeros(len(B), dtype=np.int8)
    maxU = np.full(len(B), -1e18)
    for q in range(1, 13):
        L = Lq(q, B)
        upd = L > best
        best = np.where(upd, L, best)
        bestq = np.where(upd, q, bestq)
        maxU = np.maximum(maxU, Uq(q, B))
    return bestq, best, maxU


def bisect(B):
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
    ap.add_argument("--maxdepth", type=int, default=20)
    ap.add_argument("--boxcap", type=int, default=2_000_000)
    ap.add_argument("--timecap", type=float, default=7200.0)
    ap.add_argument("--outdir", default="../out/k4_ta")
    a = ap.parse_args()
    import os
    os.makedirs(a.outdir, exist_ok=True)

    t0 = time.time()
    h = PI / a.n0
    blks = []
    for i in range(a.n0):
        for j in range(a.n0):
            g = np.arange(a.n0) * h
            XX, YY = np.meshgrid(g, g, indexing="ij")
            blk = np.empty((a.n0 * a.n0, 8))
            blk[:, 0] = i * h; blk[:, 1] = (i + 1) * h
            blk[:, 2] = j * h; blk[:, 3] = (j + 1) * h
            blk[:, 4] = XX.ravel(); blk[:, 5] = blk[:, 4] + h
            blk[:, 6] = YY.ravel(); blk[:, 7] = blk[:, 6] + h
            blks.append(blk)
    B = np.vstack(blks)
    print(f"[K4-T-a] BATON 1: initial division N0={a.n0} -> {len(B)} boxes (h = pi/{a.n0})", flush=True)

    level, status, s3_hits = 0, "maxdepth-reached", 0
    curve, thin_margin, thin_box = [], None, None
    while True:
        if time.time() - t0 > a.timecap:
            status = "time-cap"; break
        if len(B) > a.boxcap:
            status = "box-cap"; break
        q, L, maxU = classify(B)
        cert = L > 0.5
        s3 = maxU <= 0.5
        if s3.any():
            s3_hits = int(s3.sum())
            print(f"[K4-T-a][S3-ANOMALY] {s3_hits} box(es) with sup_B F_q <= 1/2 for ALL q at level {level}", flush=True)
            print(f"[K4-T-a][S3-ANOMALY] example = {B[np.argmax(s3)].tolist()}", flush=True)
            status = "S3-anomaly"
            curve.append((level, len(B), int(cert.sum()), int((~cert).sum()), float("nan")))
            break
        resid = B[~cert]
        mc = float(L[cert].min()) if cert.any() else float("nan")
        if cert.any() and (thin_margin is None or mc < thin_margin):
            thin_margin = mc
            thin_box = B[int(np.argmin(np.where(cert, L, np.inf)))]
        curve.append((level, len(B), int(cert.sum()), int(resid.shape[0]), mc))
        print(f"[K4-T-a] level {level:2d}: leaves={len(B):8d} certified={int(cert.sum()):8d} "
              f"residual={resid.shape[0]:7d} min_cert_margin={mc:.6g}", flush=True)
        if resid.shape[0] == 0:
            status = "FULL-COVER"; break
        if level >= a.maxdepth:
            status = "maxdepth-reached"; break
        A, C = bisect(resid)
        B = np.vstack([B[cert], A, C]) if cert.any() else np.vstack([A, C])
        level += 1

    el = time.time() - t0
    # ---------- emit certificate in exact dyadic integer units ----------
    cert_path = os.path.join(a.outdir, "K4-CERTIFICATE.tsv")
    resid_path = os.path.join(a.outdir, "K4-RESIDUAL.tsv")
    scale = (1 << K_DY) / PI
    qq, LL, _ = classify(B)
    certmask = LL > 0.5
    with open(cert_path, "w") as f:
        f.write("# K4 T-a CERTIFICATE (exact dyadic integer units; theta = n * pi / 2^K)\n")
        f.write(f"# K = {K_DY}\n")
        f.write(f"# target: for all theta in [0,pi]^4 exists q<=12 with "
                f"2cos(q t1)+cos(q t2)+cos(q t3)+cos(q t4) > 1/2\n")
        f.write(f"# initial division N0={a.n0}; bisection longest-edge tie-break 1,2,3,4; "
                f"depth cap {a.maxdepth}; outward inflation {INFL}; strict criterion L > 1/2\n")
        f.write("# n_a1 n_a2 n_b1 n_b2 n_c1 n_c2 n_d1 n_d2 witness_q certified_lower_bound\n")
        for row, qv, lv in zip(B[certmask], qq[certmask], LL[certmask]):
            ns = [int(round(x * scale)) for x in row]
            f.write(" ".join(str(n) for n in ns) + f" {int(qv)} {lv:.17g}\n")
    with open(resid_path, "w") as f:
        for row in B[~certmask]:
            ns = [int(round(x * scale)) for x in row]
            f.write(" ".join(str(n) for n in ns) + "\n")
    ncert, nres = int(certmask.sum()), int((~certmask).sum())
    print(f"\n[K4-T-a] status={status} elapsed={el:.2f}s levels={level} S3={s3_hits}", flush=True)
    print(f"[K4-T-a] certificate boxes = {ncert}   residual boxes = {nres}", flush=True)
    print(f"[K4-T-a] thinnest certified margin = {thin_margin!r}", flush=True)
    if thin_box is not None:
        print(f"[K4-T-a]   on box {[round(x,6) for x in thin_box]}", flush=True)
    print(f"[K4-T-a] wrote {cert_path} and {resid_path}", flush=True)
    print(f"[K4-T-a] VERDICT: {'CERTIFICATE (FULL COVER)' if status=='FULL-COVER' else status}", flush=True)


if __name__ == "__main__":
    main()
