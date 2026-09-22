#!/usr/bin/env python3
"""Thin-margin analysis + 60-digit independent recheck (spec 15.10 / 14(2)).

Reads the dry-run certificate, reports the margin distribution, and re-verifies every
box whose certified margin is below 0.05 with mpmath at 60 decimal digits
(the 60-digit pass is a SECOND INDEPENDENT NUMERICAL CHECK -- never the certificate itself).
"""
import math
import sys

PI = math.pi
THIN = 0.05


def load(path):
    out = []
    with open(path) as f:
        for line in f:
            if line.startswith("#") or not line.strip():
                continue
            p = line.split()
            out.append(([float(x) for x in p[:6]], int(p[6]), float(p[7])))
    return out


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else "../out/dryrun_221/dryrun_certificate.tsv"
    boxes = load(path)
    margins = [L - 0.5 for _, _, L in boxes]
    thin = [(B, q, L) for (B, q, L) in boxes if (L - 0.5) < THIN]
    idx_min = min(range(len(margins)), key=lambda i: margins[i])
    print(f"[thin] total certified boxes = {len(boxes)}")
    print(f"[thin] margin: min = {min(margins):.10g}   median = {sorted(margins)[len(margins)//2]:.6g}"
          f"   max = {max(margins):.6g}")
    print(f"[thin] boxes with margin < {THIN}  = {len(thin)}  ({100.0*len(thin)/len(boxes):.2f}%)")
    B, q, L = boxes[idx_min]
    print(f"[thin] thinnest box: {tuple(round(x, 12) for x in B)}  witness q={q}  L={L:.12f}")

    # ---- 60-digit recheck of the thin boxes (independent implementation, mpmath) ----
    from mpmath import mp, mpf, cos
    mp.dps = 60
    bad = 0
    worst = None
    for (Bx, qx, Lx) in thin:
        lo = mpf(0)
        for (u, v, w) in ((Bx[0], Bx[1], 2), (Bx[2], Bx[3], 2), (Bx[4], Bx[5], 1)):
            uu = mpf(u); vv = mpf(v)
            a = cos(qx * uu); b = cos(qx * vv)
            val = min(a, b)
            # interior odd multiples of pi at 60 digits
            k0 = int(math.ceil(qx * u / PI - 1e-12))
            k1 = int(math.floor(qx * v / PI + 1e-12))
            for m in range(k0, k1 + 1):
                if m % 2:
                    val = min(val, mpf(-1))
            lo += w * val
        margin60 = lo - mpf(1) / 2
        worst = margin60 if worst is None else min(worst, margin60)
        if margin60 <= 0:
            bad += 1
            print(f"[thin] 60-digit FAILURE: {tuple(round(x, 12) for x in Bx)} q={qx} margin60={margin60}")
    print(f"[thin] 60-digit recheck: checked {len(thin)} thin boxes, failures = {bad},"
          f" worst 60-digit margin = {float(worst) if worst is not None else float('nan'):.12g}")
    print(f"[thin] VERDICT: {'PASS' if bad == 0 else 'FAIL'}")


if __name__ == "__main__":
    main()
