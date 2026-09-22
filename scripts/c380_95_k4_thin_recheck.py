#!/usr/bin/env python3
"""Thin-margin 60-digit independent recheck for the K4 T-a certificate.

Per spec: every box with certified margin < 0.05 is re-verified with mpmath at dps=60.
This is a SECOND INDEPENDENT NUMERICAL CHECK -- it is not the certificate itself.
"""
import math
import sys

PI = math.pi
THIN = 0.05


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else "../out/k4_ta/K4-CERTIFICATE.tsv"
    K = None
    rows = []
    with open(path) as f:
        for line in f:
            if line.startswith("#"):
                if line.startswith("# K ="):
                    K = int(line.split("=")[1])
                continue
            if not line.strip():
                continue
            p = line.split()
            rows.append(([int(x) for x in p[:8]], int(p[8]), float(p[9])))
    margins = [L - 0.5 for _, _, L in rows]
    thin = [(b, q, L) for (b, q, L) in rows if (L - 0.5) < THIN]
    print(f"[thin] K={K} certified boxes = {len(rows)}")
    print(f"[thin] margin: min = {min(margins):.10g}  median = {sorted(margins)[len(margins)//2]:.6g}  "
          f"max = {max(margins):.6g}")
    print(f"[thin] boxes with margin < {THIN} = {len(thin)}  ({100.0*len(thin)/len(rows):.2f}%)")
    i = min(range(len(margins)), key=lambda j: margins[j])
    print(f"[thin] thinnest: box={rows[i][0]} witness q={rows[i][1]} L={rows[i][2]:.12f}")

    from mpmath import mp, mpf, cos
    mp.dps = 60
    s = mpf(1) / (1 << K)
    bad = 0
    worst = None
    for (box, q, L) in thin:
        lo = mpf(0)
        for (n1, n2, w) in ((box[0], box[1], 2), (box[2], box[3], 1), (box[4], box[5], 1), (box[6], box[7], 1)):
            u = mpf(n1) * s * mp.pi
            v = mpf(n2) * s * mp.pi
            val = min(cos(q * u), cos(q * v))
            k0 = int(math.ceil(q * float(u) / PI - 1e-12))
            k1 = int(math.floor(q * float(v) / PI + 1e-12))
            for m in range(k0, k1 + 1):
                if m % 2:
                    val = min(val, mpf(-1))
            lo += w * val
        rg = lo - mpf(1) / 2
        worst = rg if worst is None else min(worst, rg)
        if rg <= 0:
            bad += 1
            print(f"[thin] 60-digit FAILURE: box={box} q={q} margin60={rg}")
    print(f"[thin] 60-digit recheck: checked {len(thin)} thin boxes, failures = {bad}, "
          f"worst 60-digit margin = {float(worst) if worst is not None else float('nan'):.12g}")
    print(f"[thin] VERDICT: {'PASS' if bad == 0 else 'FAIL'}")


if __name__ == "__main__":
    main()
