#!/usr/bin/env python3
"""
X1 / K(10,1): tabu search with FIXED size k, objective = number of uncovered vertices.
Classic approach (cf. Ostergard's tabu search for covering codes).
Run: tabu.py k seed seconds
Writes best_code_<k>.json whenever an uncovered==0 solution is found (=> cover of size k).
"""
import random, sys, time, json

n = 10
N = 1 << n
FULL = (1 << N) - 1
BALL = []
for w in range(N):
    m = 0
    for v in (w, *[w ^ (1 << i) for i in range(n)]):
        m |= 1 << v
    BALL.append(m)


def uncovered_of(cov):
    return bin(FULL & ~cov).count("1")


def main():
    k = int(sys.argv[1]) if len(sys.argv) > 1 else 119
    seed = int(sys.argv[2]) if len(sys.argv) > 2 else 0
    secs = float(sys.argv[3]) if len(sys.argv) > 3 else 300.0
    rng = random.Random(seed)
    T0 = time.time()

    best_unc = 10**9
    restarts = 0
    while time.time() - T0 < secs:
        restarts += 1
        cur = rng.sample(range(N), k)
        # counts of how many chosen words cover each vertex
        cnt = [0] * N
        for wdeg in cur:
            m = BALL[wdeg]
            while m:
                b = m & -m
                cnt[b.bit_length() - 1] += 1
                m ^= b
        tabu_until = {}
        it = 0
        while time.time() - T0 < secs:
            it += 1
            curset = set(cur)
            # pick the word with the largest private contribution (or random)
            i = rng.randrange(k)
            w_old = cur[i]
            # candidate: best swap among a random sample
            best = None
            for _ in range(40):
                w_new = rng.randrange(N)
                if w_new in curset:
                    continue
                # delta uncovered = vertices covered only by w_old and not by w_new, minus new
                delta = 0
                m = BALL[w_old]
                while m:
                    b = m & -m
                    j = b.bit_length() - 1
                    if cnt[j] == 1 and not (BALL[w_new] >> j) & 1:
                        delta += 1
                    m ^= b
                m = BALL[w_new]
                while m:
                    b = m & -m
                    j = b.bit_length() - 1
                    if cnt[j] == 0:
                        delta -= 1
                    m ^= b
                if (delta, rng.random()) < (best[0], best[1]) if best else True:
                    if w_new not in tabu_until or tabu_until.get(w_new, 0) < it:
                        best = (delta, rng.random(), w_new)
            if best is None:
                break
            _, _, w_new = best
            # apply swap
            m = BALL[w_old]
            while m:
                b = m & -m
                cnt[b.bit_length() - 1] -= 1
                m ^= b
            m = BALL[w_new]
            while m:
                b = m & -m
                cnt[b.bit_length() - 1] += 1
                m ^= b
            cur[i] = w_new
            tabu_until[w_old] = it + rng.randint(5, 20)
            unc = sum(1 for j in range(N) if cnt[j] == 0)
            if unc < best_unc:
                best_unc = unc
                print(f"  k={k} unc={unc} restart={restarts} it={it} t={time.time()-T0:.0f}s", flush=True)
                if unc == 0:
                    json.dump({"n": n, "k": k, "code": sorted(cur), "verified": True},
                              open(f"best_code_{k}.json", "w"))
                    print(f"*** FOUND COVER of size {k} *** written best_code_{k}.json", flush=True)
                    return
            if it % 3000 == 0:
                # diversification: random restart if stuck
                break
    print(f"end: k={k} best_unc={best_unc} restarts={restarts}")


main()
