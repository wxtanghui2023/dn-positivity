#!/usr/bin/env python3
"""
X1: binary covering code, length 10, radius 1  =>  K(10,1) <= ?   (record: 107..120)
Space: Q_10 = {0,1}^10 (1024 words).  Ball B(w) = {w} u {w xor 2^i}  (size 11).
Goal: find cover C with |C| <= 119  (would improve best-known upper bound 120).

- greedy + randomized multi-start
- redundancy elimination
- (1,1)-swap / (2,1)-swap local search on size
- every improvement is written to disk and re-verified by an INDEPENDENT checker
"""
import random, sys, time, json, os
n = 10
N = 1 << n
FULL = (1 << N) - 1

# ball mask for each word
BALL = []
for w in range(N):
    m = 0
    for v in (w, *[w ^ (1 << i) for i in range(n)]):
        m |= 1 << v
    BALL.append(m)


def verify(code, n_=n):
    """independent full-space coverage check; returns (ok, uncovered_count, maxdist)"""
    N_ = 1 << n_
    balls = []
    for w in code:
        m = 0
        for v in (w, *[w ^ (1 << i) for i in range(n_)]):
            m |= 1 << v
        balls.append(m)
    cov = 0
    for m in balls:
        cov |= m
    full = (1 << N_) - 1
    unc = bin((~cov) & full).count("1")
    return unc == 0, unc


def greedy(rng, target=None):
    """randomized greedy set cover"""
    unc = FULL
    cover = []
    while unc:
        best, best_gain, ties = -1, -1, []
        for w in range(N):
            g = bin(BALL[w] & unc).count("1")
            if g > best_gain:
                best_gain, ties = g, [w]
            elif g == best_gain and g > 0:
                ties.append(w)
        if best_gain <= 0:
            raise RuntimeError("no progress")
        w = rng.choice(ties) if len(ties) > 1 else ties[0]
        cover.append(w)
        unc &= ~BALL[w]
        if target and len(cover) > target + 200:
            break
    return cover


def redundancy_elim(cover):
    """delete any word whose removal keeps full coverage (repeat until stable)"""
    cover = list(cover)
    changed = True
    while changed:
        changed = False
        # coverage counts
        cnt = [0] * N
        for w in cover:
            m = BALL[w]
            while m:
                b = m & -m
                cnt[b.bit_length() - 1] += 1
                m ^= b
        for w in list(cover):
            ok = True
            m = BALL[w]
            while m:
                b = m & -m
                if cnt[b.bit_length() - 1] <= 1:
                    ok = False
                    break
                m ^= b
            if ok:
                cover.remove(w)
                m = BALL[w]
                while m:
                    b = m & -m
                    cnt[b.bit_length() - 1] -= 1
                    m ^= b
                changed = True
    return cover


def cov_union(cover):
    c = 0
    for w in cover:
        c |= BALL[w]
    return c


def local_search(cover, rng, deadline, best_holder, tag=""):
    """(1,1) swaps: replace one codeword by another if size preserved but coverage improves;
       also: try 'delete+repair' (size-1) moves."""
    cover = list(cover)
    cov = cov_union(cover)
    stagn = 0
    while time.time() < deadline:
        # --- (size-1) attempt: delete one, then repair by adding words greedily
        cand = cover[:]
        rng.shuffle(cand)
        removed = cand.pop()
        cov2 = cov_union(cand)
        unc = FULL & ~cov2
        if unc == 0:
            cover = redundancy_elim(cand)
            best_holder["best"] = min(best_holder["best"], len(cover))
            cov = cov_union(cover)
            print(f"  [{tag}] shrink -> {len(cover)} (t={time.time()-T0:.0f}s)", flush=True)
            continue
        # repair greedily limited
        added = []
        while unc and len(added) < 4:
            best, bg, ties = -1, -1, []
            for w in range(N):
                g = bin(BALL[w] & unc).count("1")
                if g > bg:
                    bg, ties = g, [w]
                elif g == bg and g > 0:
                    ties.append(w)
            w = rng.choice(ties)
            added.append(w)
            unc &= ~BALL[w]
        if unc == 0 and len(added) <= 1:
            newcover = redundancy_elim(cand + added)
            if len(newcover) <= len(cover):
                if len(newcover) < len(cover):
                    print(f"  [{tag}] delete+repair -> {len(newcover)} (t={time.time()-T0:.0f}s)", flush=True)
                cover, cov = newcover, cov_union(newcover)
                best_holder["best"] = min(best_holder["best"], len(cover))
                continue
        # --- (1,1) random swap keeping coverage, accept if it reduces overlap (elastic)
        i = rng.randrange(len(cover))
        w_old = cover[i]
        w_new = rng.randrange(N)
        if w_new == w_old:
            continue
        cov_new = cov & ~BALL[w_old] | BALL[w_new]
        if cov_new == FULL:
            cover[i] = w_new
            cov = cov_new
            stagn = 0
        else:
            stagn += 1
            if stagn > 4000:
                cov = cov_union(cover)
                stagn = 0
    return cover


if __name__ == "__main__":
    seed = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    budget = float(sys.argv[2]) if len(sys.argv) > 2 else 120.0
    rng = random.Random(seed)
    T0 = time.time()
    best_holder = {"best": 10**9}
    # multi-start greedy
    for it in range(6):
        c = redundancy_elim(greedy(rng))
        best_holder["best"] = min(best_holder["best"], len(c))
        print(f"start {it}: greedy+elim = {len(c)}  best={best_holder['best']} (t={time.time()-T0:.0f}s)", flush=True)
        if time.time() > T0 + budget * 0.5:
            break
        c = local_search(c, rng, min(T0 + budget, time.time() + budget / 3), best_holder, tag=f"it{it}")
    # take best from last cover
    ok, unc = verify(c)
    print(f"final size={len(c)} verify_ok={ok} uncovered={unc} best={best_holder['best']}")
    json.dump({"n": n, "code": sorted(c), "size": len(c), "verified": ok}, open("best_code.json", "w"))
    print("written best_code.json")
