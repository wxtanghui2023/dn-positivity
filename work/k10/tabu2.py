#!/usr/bin/env python3
"""
X1 / K(10,1) : fixed-k tabu search (uncovered-minimising), warm start from greedy cover.
- init: load best_code.json (greedy solution), greedily drop words to reach size k
- iteration: remove one chosen word (tabu tenure), insert best replacement (full neighbourhood)
- no size drift; restart by perturbation if stagnant
- writes best_code_<k>.json on uncovered == 0
Usage: tabu2.py k seed seconds
"""
import numpy as np, sys, time, json

n = 10; N = 1 << n
B = np.zeros((N, N), dtype=np.int32)
for w in range(N):
    B[w, w] = 1
    for i in range(n):
        B[w, w ^ (1 << i)] = 1


def load_start():
    try:
        d = json.load(open("best_code.json"))
        return list(map(int, d["code"]))
    except Exception:
        return list(range(N))


def shrink_to(code, k):
    cur = list(code)
    while len(cur) > k:
        cnt = np.zeros(N, dtype=np.int32)
        for w in cur:
            cnt += B[w]
        # drop the word whose private set is smallest
        best, bestpv = None, 10**9
        for idx, w in enumerate(cur):
            pv = int(((cnt == 1) & (B[w] == 1)).sum())
            if pv < bestpv:
                bestpv, best = pv, idx
        cur.pop(best)
    return cur


def run(k, seed, secs):
    rng = np.random.default_rng(seed)
    T0 = time.time()
    cur = shrink_to(load_start(), k)
    cnt = np.zeros(N, dtype=np.int32)
    for w in cur:
        cnt += B[w]
    best_unc = int((cnt == 0).sum())
    print(f"start k={k} unc={best_unc}", flush=True)
    tabu = np.zeros(N, dtype=np.int64)
    it = 0
    while time.time() - T0 < secs:
        it += 1
        # sample removal candidates; pick the one with fewest private vertices (cheapest to repair)
        cand_idx = rng.choice(len(cur), size=min(len(cur), 12), replace=False)
        best = None
        for oi in cand_idx:
            oi = int(oi); w_out = cur[oi]
            if tabu[w_out] > it:
                continue
            priv = (cnt == 1) & (B[w_out] == 1)
            npv = int(priv.sum())
            gains = B @ priv.astype(np.int32)
            gains[cur] = -1
            order = np.argsort(-gains)[:3]
            for w_in in order:
                w_in = int(w_in)
                d = npv - int(gains[w_in])
                if tabu[w_in] > it and d > 0:
                    continue
                if best is None or d < best[0]:
                    best = (d, oi, w_out, w_in)
            if best is not None and best[0] == 0:
                break
        if best is None:
            it += 1
            continue
        d, oi, w_out, w_in = best
        cnt -= B[w_out]; cnt += B[w_in]; cur[oi] = w_in
        tabu[w_out] = it + int(rng.integers(5, 30))
        unc = int((cnt == 0).sum())
        if unc < best_unc:
            best_unc = unc
            print(f"  k={k} unc={unc} it={it} t={time.time()-T0:.0f}s", flush=True)
            if unc == 0:
                code = sorted(int(x) for x in cur)
                json.dump({"n": n, "k": k, "code": code, "verified": True}, open(f"best_code_{k}.json", "w"))
                print(f"*** COVER size={k} written best_code_{k}.json ***", flush=True)
                return
        if it % 15000 == 0:
            # perturbation: replace 3 random chosen words
            for _ in range(3):
                i = int(rng.integers(len(cur)))
                w_old = cur[i]; w_new = int(rng.integers(N))
                if w_new in cur: continue
                cnt -= B[w_old]; cnt += B[w_new]; cur[i] = w_new
            print(f"  perturb k={k} unc={int((cnt==0).sum())} t={time.time()-T0:.0f}s", flush=True)
    print(f"end k={k} best_unc={best_unc}", flush=True)


if __name__ == "__main__":
    run(int(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3]))
