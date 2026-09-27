#!/usr/bin/env python3
"""P2 construction attack v4 (k=119 fixed) — breakout search on weighted uncovered cost.

Spec (source-first verified 2026-09-27; v2 best-tracking bug and v3 strict-acceptance
stall both fixed here):
  state    : code C, |C| = 119, distinct words of {0,1}^10
  objective: unc(C) = #{p : |C ∩ B1(p)| = 0};  target  unc == 0   (119-witness)
  move     : replace word w by candidate w' ∉ C.  Weighted cost change
             delta = (weights of cnt==1 points of w) - (weights of newly covered points)
             (first term is an upper bound on loss: overlap recovery ignored)
  accept   : best sampled move with delta <= 0 (plateau walks allowed); 5% forced noise
  breakout : on stall, bump weights of uncovered points (reset above 40)
  seeds    : Kamenetsky 120-code minus one word, ordered by fewest private points
  budget   : internal wall-clock deadline (argv[1] s); single process; numpy 1-thread
Output: p2k119_best.json + independent bit-level verification.
"""
import json
import random
import sys
import time

import numpy as np

N, n = 1024, 10
BUDGET = float(sys.argv[1]) if len(sys.argv) > 1 else 600.0
T0 = time.time()
DEADLINE = T0 + BUDGET
random.seed(20260927)

words = [int(t, 2) for t in open("kamenetsky120.txt").read().split()]
assert len(words) == 120 and len(set(words)) == 120

INC = np.zeros((N, N), dtype=np.uint8)
for c in range(N):
    INC[c, c] = 1
    for i in range(n):
        INC[c ^ (1 << i), c] = 1
NB = [np.array([c] + [c ^ (1 << i) for i in range(n)]) for c in range(N)]

base = INC[:, words].sum(axis=1).astype(np.int16)
priv = sorted((int((base[NB[c]] == 1).sum()), c) for c in words)
print("[seed table]", priv[:6], flush=True)

best, best_unc, it_total, chains = None, 10 ** 9, 0, 0

for priv_k, drop_word in priv[:8]:
    if time.time() >= DEADLINE or best_unc == 0:
        break
    chains += 1
    cur = [c for c in words if c != drop_word]
    cnt = INC[:, cur].sum(axis=1).astype(np.int32)
    u0 = int((cnt == 0).sum())
    if u0 < best_unc:
        best, best_unc = list(cur), u0
        print(f"[chain {chains}] seed unc={best_unc} t={time.time()-T0:.0f}s", flush=True)
    wts = np.ones(N, dtype=np.int64)
    inC = np.zeros(N, dtype=bool)
    inC[cur] = True
    tabu, it, stall = {}, 0, 0
    while time.time() < DEADLINE and best_unc > 0:
        it += 1
        it_total += 1
        top = None
        wa = int(wts[cnt == 0].sum())
        for p in random.sample(range(119), 6):
            w = cur[p]
            rem = cnt.copy()
            rem[NB[w]] -= 1
            z = rem == 0
            wz = int(wts[z].sum())
            gain = (INC[z].astype(np.int64) * wts[z][:, None]).sum(axis=0)
            base_delta = wz - wa
            inc2 = INC[rem <= 1].sum(axis=0).astype(np.int64)
            score = (gain - base_delta) * 4096 + inc2
            score[inC] = -1 << 40
            for c, exp in tabu.items():
                if exp > it:
                    score[c] = -1 << 40
            cand = int(np.argmax(score))
            if top is None or score[cand] > top[0]:
                top = (int(score[cand]), p, w, cand, rem, base_delta, int(gain[cand]))
        if top is None:
            stall += 1
            continue
        _, p, w, cand, rem, base_delta, g = top
        if (base_delta - g) <= 0 or random.random() < 0.05:
            cur[p] = cand
            inC[w] = False
            inC[cand] = True
            cnt = rem
            cnt[NB[cand]] += 1
            tabu[w] = it + 5
            unc = int((cnt == 0).sum())
            if unc < best_unc:
                best, best_unc = list(cur), unc
                json.dump({"n": n, "code": best, "size": len(best), "uncovered": best_unc},
                          open("p2k119_best.json", "w"))
                print(f"[chain {chains} it {it}] new best unc={best_unc} t={time.time()-T0:.0f}s",
                      flush=True)
                stall = 0
                if best_unc == 0:
                    break
            else:
                stall += 1
        else:
            stall += 1
        if stall > 200:
            wts[cnt == 0] += 1
            if wts.max() > 40:
                wts[:] = 1
            tabu.clear()
            stall = 0
        if it % 100000 == 0:
            print(f"[chain {chains} it {it}] unc={int((cnt==0).sum())} best_unc={best_unc} "
                  f"wmax={int(wts.max())} t={time.time()-T0:.0f}s", flush=True)
    print(f"[chain {chains}] seed priv={priv_k} end best_unc={best_unc} iters={it} "
          f"t={time.time()-T0:.0f}s", flush=True)

if best is None:
    best = [c for c in words if c != priv[0][1]]
cov = set()
for c in best:
    cov.add(c)
    for i in range(n):
        cov.add(c ^ (1 << i))
uncov = [x for x in range(N) if x not in cov]
ok = len(best) == 119 and len(set(best)) == 119 and not uncov
print(f"[verdict] |C|={len(best)} distinct={len(set(best))} uncovered={len(uncov)} "
      f"{'*** 119-WITNESS ***' if ok else 'no 119 witness in budget'} "
      f"| chains={chains} iters={it_total} elapsed={time.time()-T0:.0f}s", flush=True)
json.dump({"n": n, "code": best, "size": len(best), "uncovered": len(uncov), "witness": ok},
          open("p2k119_best.json", "w"))
