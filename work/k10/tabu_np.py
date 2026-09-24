#!/usr/bin/env python3
"""
X1 / K(10,1): numpy vectorised FULL-NEIGHBOURHOOD tabu search.
State: chosen set C of size k. Object: #uncovered vertices.
Iteration: pick word w_out (with tabu tenure) to remove; compute private(w_out)
  = vertices covered only by w_out; then choose w_in maximising |B(w_in) & private|
  (full neighbourhood scan via matrix-vector product over the 1024x1024 incidence).
Tenure on recently removed/inserted words; aspiration if it reaches 0 uncovered.
Writes best_code_<k>.json when uncovered == 0 (=> valid cover of size k).
Usage: tabu_np.py k seed seconds
"""
import numpy as np, random, sys, time, json

n = 10
N = 1 << n
B = np.zeros((N, N), dtype=np.int32)
for w in range(N):
    B[w, w] = 1
    for i in range(n):
        B[w, w ^ (1 << i)] = 1
Bt = B.T.copy()  # Bt[v] = words covering v   (same as B here since symmetric-ish; keep for clarity)


def main():
    k = int(sys.argv[1]); seed = int(sys.argv[2]); secs = float(sys.argv[3])
    rng = np.random.default_rng(seed)
    T0 = time.time()
    best_unc = 10**9
    best_cover = None
    while time.time() - T0 < secs:
        cur = rng.choice(N, size=k, replace=False)
        cnt = B[cur].sum(axis=0)             # cnt[v] = #chosen covering v
        tabu = np.zeros(N, dtype=np.int64)
        it = 0
        while time.time() - T0 < secs:
            it += 1
            # candidates to remove: sample a few, evaluate private sets, pick best removal
            outs = rng.choice(k, size=min(k, 8), replace=False)
            best_choice = None
            for oi in outs:
                w_out = int(cur[oi])
                if tabu[w_out] > it:
                    continue
                # private vertices of w_out
                priv_mask = (cnt == 1) & (B[w_out] == 1)
                npv = int(priv_mask.sum())
                if npv == 0:
                    # redundant word: remove it -> cover of size k-1
                    cur = np.delete(cur, oi)
                    k -= 1
                    cnt = B[cur].sum(axis=0)
                    best_unc = min(best_unc, int((cnt == 0).sum()))
                    print(f"  k={k} redundant removed, unc={int((cnt==0).sum())} t={time.time()-T0:.0f}s", flush=True)
                    break
                gains = B @ priv_mask.astype(np.int32)      # for each w_in: how many private vertices covered
                gains[cur] = -1                             # cannot pick an already chosen word
                gains[w_out] = -1
                order = np.argsort(-gains)[:5]
                for w_in in order:
                    w_in = int(w_in)
                    if tabu[w_in] > it and gains[w_in] < npv:
                        continue
                    delta = npv - int(gains[w_in])
                    cand = (delta, w_in, oi, w_out)
                    if best_choice is None or delta < best_choice[0]:
                        best_choice = cand
                if best_choice is not None and best_choice[0] == 0:
                    break
            if best_choice is None:
                break
            delta, w_in, oi, w_out = best_choice
            # apply
            m = B[w_out] == 1
            cnt[m] -= 1
            m2 = B[w_in] == 1
            cnt[m2] += 1
            cur[oi] = w_in
            tabu[w_out] = it + rng.integers(5, 25)
            unc = int((cnt == 0).sum())
            if unc < best_unc:
                best_unc = unc
                print(f"  k={k} unc={unc} it={it} t={time.time()-T0:.0f}s", flush=True)
                if unc == 0:
                    code = sorted(int(x) for x in cur)
                    json.dump({"n": n, "k": k, "code": code, "verified": True}, open(f"best_code_{k}.json", "w"))
                    print(f"*** COVER FOUND size={k} -> best_code_{k}.json ***", flush=True)
                    return
            if it % 20000 == 0:
                break   # restart
    print(f"end k={k} best_unc={best_unc}")


main()
