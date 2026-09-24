#!/usr/bin/env python3
"""X1: fixed-k tabu, WARM START from the verified 120-code (delete the words with
smallest private coverage to reach size k).  Objective: #uncovered -> 0.
Writes best_code_<k>.json on success.  Usage: tabu3.py k seed seconds"""
import numpy as np, sys, time, json

n = 10; N = 1 << n
B = np.zeros((N, N), dtype=np.int32)
for w in range(N):
    B[w, w] = 1
    for i in range(n):
        B[w, w ^ (1 << i)] = 1

words = [int(s, 2) for s in open("kamenetsky120.txt").read().split()]


def run(k, seed, secs):
    rng = np.random.default_rng(seed)
    T0 = time.time()
    cnt = np.zeros(N, dtype=np.int32)
    for w in words:
        cnt += B[w]
    priv = sorted((int(((cnt == 1) & (B[w] == 1)).sum()), w) for w in words)
    drop = [w for _, w in priv[:120 - k]]
    cur = [w for w in words if w not in drop]
    cnt = np.zeros(N, dtype=np.int32)
    for w in cur:
        cnt += B[w]
    best = int((cnt == 0).sum())
    print(f"start k={k} unc={best} (dropped {len(drop)})", flush=True)
    tabu = np.zeros(N, dtype=np.int64)
    it = 0
    while time.time() - T0 < secs:
        it += 1
        best_move = None
        for oi in rng.choice(len(cur), size=min(len(cur), 20), replace=False):
            oi = int(oi); wo = cur[oi]
            if tabu[wo] > it:
                continue
            privm = (cnt == 1) & (B[wo] == 1)
            npv = int(privm.sum())
            g = B @ privm.astype(np.int32)
            g[cur] = -1
            for wi in np.argsort(-g)[:3]:
                wi = int(wi)
                d = npv - int(g[wi])
                if tabu[wi] > it and d > 0:
                    continue
                if best_move is None or d < best_move[0]:
                    best_move = (d, oi, wo, wi)
            if best_move is not None and best_move[0] == 0:
                break
        if best_move is None:
            continue
        d, oi, wo, wi = best_move
        cnt -= B[wo]; cnt += B[wi]; cur[oi] = wi
        tabu[wo] = it + int(rng.integers(5, 30))
        unc = int((cnt == 0).sum())
        if unc < best:
            best = unc
            print(f"  k={k} unc={unc} it={it} t={time.time()-T0:.0f}s", flush=True)
            if unc == 0:
                json.dump({"n": n, "k": k, "code": sorted(int(x) for x in cur)},
                          open(f"best_code_{k}.json", "w"))
                print(f"*** FOUND {k}-COVER ***", flush=True)
                return
        if it % 20000 == 0:
            for _ in range(2):
                i = int(rng.integers(len(cur))); wo = cur[i]; wi = int(rng.integers(N))
                if wi in cur:
                    continue
                cnt -= B[wo]; cnt += B[wi]; cur[i] = wi
    print(f"end k={k} best_unc={best}", flush=True)


run(int(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3]))
