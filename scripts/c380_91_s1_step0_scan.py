#!/usr/bin/env python3
"""C-380 Step 0 -- S1 DOMAIN DECISION SCAN.

Spec: docs/C380-S1-FREEZE.md section 8.
This is NOT a proof. It only asks:
    does there exist a candidate in the FULL locus T_{k>=4} with
        max_{0<=r<=12} |F_{2r+1}|  <=  1/2   ?
with the structural families the order requires:
    (F1) same-angle cancellation  (one cancelling pair + 3 singletons; more pairs force k<=3)
    (F2) phi = pi/2 type nodes    (a node at pi/2 contributes 0 to every odd frequency)
    (F3) commensurate (exotic-relation) families: phi_j = 2*pi*m/M
    (F4) local minimisation from many random starts (worst-case hunting)
plus plain random sampling as a baseline.

k := number of distinct u_j^2 with u_j = cos 2 phi_j; configurations whose z-values are
near-degenerate (gap < 1e-6) are flagged AMBIGUOUS and excluded from the strict-k count.
"""
import itertools
import math
import sys
import time

import numpy as np

PI = math.pi
RS = np.arange(0, 13)                 # r = 0..12
FREQ = 2 * RS + 1                     # odd frequencies 1,3,...,25
TOL = 1e-6


def Fvec(phis, sigs):
    ang = np.outer(FREQ, np.asarray(phis, float))
    return (np.cos(ang) * np.asarray(sigs, float)).sum(axis=1)


def maxabsF(phis, sigs):
    return float(np.max(np.abs(Fvec(phis, sigs))))


def ksupport(phis):
    u2 = np.cos(2.0 * np.asarray(phis, float)) ** 2
    s = np.sort(u2)
    gaps = np.diff(s)
    k = 1 + int((gaps > TOL).sum())
    amb = bool((gaps <= TOL).any())
    return k, amb, (float(gaps.min()) if len(gaps) else 1.0)


def record(best, phis, sigs):
    v = maxabsF(phis, sigs)
    k, amb, g = ksupport(phis)
    if k >= 4 and not amb:
        if v < best["v"]:
            best.update(v=v, phis=list(phis), sigs=list(sigs), k=k, gap=g)
        if v <= 0.5:
            best.setdefault("hits", []).append((v, list(phis), list(sigs), k))
    return v


def layer_sigs():
    """all sign layers up to global flip (fix sigma_1 = +1)."""
    out = []
    for rest in itertools.product([1, -1], repeat=4):
        out.append((1,) + rest)
    return out


def run():
    t0 = time.time()
    best = {"v": 1e9}
    rng = np.random.default_rng(20260922)
    layers = layer_sigs()
    print(f"[step0] sign layers (mod global flip): {len(layers)}")
    print(f"[step0] frequency set: {list(FREQ)}")

    # ---------- F4: random starts + local minimisation (worst-case hunting) ----------
    from scipy.optimize import minimize
    nstart = 120
    nloc = 0
    for sig in layers:
        for _ in range(nstart):
            x0 = rng.uniform(1e-3, PI / 2 - 1e-3, 5)
            res = minimize(lambda x: maxabsF(x, sig), x0, method="Nelder-Mead",
                           options={"maxiter": 900, "xatol": 1e-10, "fatol": 1e-12})
            nloc += 1
            record(best, np.clip(res.x, 1e-9, PI / 2 - 1e-9), sig)
    print(f"[step0] F4 random+local: {nloc} runs, best so far v={best['v']:.6f}")

    # ---------- F2: a node pinned at phi = pi/2 ----------
    for sig in layers:
        for _ in range(60):
            x0 = rng.uniform(1e-3, PI / 2 - 1e-3, 4)
            def obj(x):
                return maxabsF(list(x) + [PI / 2], sig)
            res = minimize(obj, x0, method="Nelder-Mead",
                           options={"maxiter": 900, "xatol": 1e-10, "fatol": 1e-12})
            record(best, list(np.clip(res.x, 1e-9, PI / 2 - 1e-9)) + [PI / 2], sig)
    print(f"[step0] F2 (phi=pi/2 node): best v={best['v']:.6f}")

    # ---------- F1: exactly one cancelling pair (same phi, opposite sigma) + 3 singletons ----------
    for sig3 in itertools.product([1, -1], repeat=3):
        for _ in range(60):
            x0 = rng.uniform(1e-3, PI / 2 - 1e-3, 4)   # (phi_pair, phi_a, phi_b, phi_c)
            def obj(x):
                phis = [x[0], x[0], x[1], x[2], x[3]]
                return maxabsF(phis, (1, -1) + sig3)
            res = minimize(obj, x0, method="Nelder-Mead",
                           options={"maxiter": 900, "xatol": 1e-10, "fatol": 1e-12})
            x = np.clip(res.x, 1e-9, PI / 2 - 1e-9)
            record(best, [x[0], x[0], x[1], x[2], x[3]], (1, -1) + sig3)
    print(f"[step0] F1 (one cancelling pair): best v={best['v']:.6f}")

    # ---------- F3: commensurate families phi_j = 2*pi*m/M (exhaustive per M) ----------
    for M in (9, 13, 18, 25, 26, 39, 52):
        A = [2 * PI * m / M for m in range(1, M) if 2 * PI * m / M < PI / 2 - 1e-12]
        if len(A) < 2:
            continue
        cnt = 0
        for combo in itertools.combinations_with_replacement(A, 5):
            for sig in layers:
                record(best, list(combo), sig)
                cnt += 1
        print(f"[step0] F3 M={M}: |A|={len(A)}, evaluated {cnt} (phi,sigma) pairs; best v={best['v']:.6f}")

    # ---------- baseline random sampling ----------
    nrand = 200000
    P = rng.uniform(1e-6, PI / 2 - 1e-6, size=(nrand, 5))
    for sig in layers:
        for i in range(0, nrand, 20000):
            for ph in P[i:i + 20000]:
                record(best, ph, sig)
    print(f"[step0] random baseline: {nrand * len(layers)} evaluations")

    # ---------- report ----------
    print("\n" + "=" * 74)
    print(f"[step0] global best (lowest max_r |F_2r+1| over k>=4, non-ambiguous): v = {best['v']:.9f}")
    print(f"[step0]        at phi = {[round(x, 9) for x in best['phis']]}")
    print(f"[step0]        sigma = {best['sigs']}   k = {best['k']}   min z-gap = {best['gap']:.6g}")
    print(f"[step0] candidates with v <= 1/2 : {len(best.get('hits', []))}")
    if best.get("hits"):
        for h in best["hits"][:10]:
            print(f"[step0]   CANDIDATE v={h[0]:.9f} phi={[round(y,9) for y in h[1]]} sig={h[2]} k={h[3]}")
    print(f"[step0] elapsed {time.time() - t0:.1f} s")
    print("=" * 74)
    # machine-readable verdict line
    verdict = "COUNTEREXAMPLE-CANDIDATE" if best.get("hits") else "NO-CANDIDATE-FOUND"
    print(f"[step0] VERDICT: {verdict}")
    return 0


if __name__ == "__main__":
    sys.exit(run())
