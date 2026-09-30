#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
逐坐标构造 + 同构约化 + 纤维体积剪枝 (Keri Ch.9 mechanism)
FIX: pruning must count MULTIPLICITY (union <= sum over codewords' balls).
     Distinct-prefix counting was UNSOUND (pruned valid configurations).
Positive controls included: (4,4) and (5,7) must FIND a cover.
"""
import itertools, time, sys
from math import comb

def ball_vol(r, m):
    if r < 0: return 0
    if r >= m: return 1 << m
    return sum(comb(m, i) for i in range(r + 1))

def hd(a, b):
    return sum(x != y for x, y in zip(a, b))

def canon(words, k):
    if k <= 1:
        return tuple(sorted(words))
    best = None
    for perm in itertools.permutations(range(k)):
        w2 = tuple(sorted(tuple(w[i] for i in perm) for w in words))
        if best is None or w2 < best:
            best = w2
    return best

def run(n, M, R=1, tl=120.0):
    t0 = time.time()
    stats = {"nodes": 0, "levels": {}}
    visited = set()
    found = [False]

    def level_ok(cand, k):
        """cand: list of M prefixes length k. Necessary (sound) condition:
           for each v in F_2^k: sum over ALL M codewords of V(R-d(c,v), n-k) >= 2^(n-k)"""
        fiber = 1 << (n - k)
        for v in itertools.product((0, 1), repeat=k):
            s = 0
            for c in cand:
                d = hd(c, v)
                if d <= R:
                    s += ball_vol(R - d, n - k)
            if s < fiber:
                return False
        return True

    def optimistic(assigned, k, remaining, v):
        """sound upper bound of union over assigned (with multiplicity) + remaining words"""
        s = 0
        for c in assigned:
            d = hd(c, v)
            if d <= R:
                s += ball_vol(R - d, n - k)
        if remaining > 0:
            s += remaining * ball_vol(R, n - k)
        return s

    sys.setrecursionlimit(100000)

    def dfs(k, words, idx):
        if time.time() - t0 > tl:
            raise TimeoutError
        if idx == M:
            k2 = k + 1
            key = (k2, canon(words, k2)) if k2 <= 5 else (k2, tuple(sorted(words)))
            if key in visited:
                return
            visited.add(key)
            stats["nodes"] += 1
            stats["levels"][k2] = stats["levels"].get(k2, 0) + 1
            if k2 == n:
                if level_ok(words, n):
                    found[0] = True
                return
            if not level_ok(words, k2):
                return
            dfs(k2, words, 0)
            return
        rem = M - idx - 1
        base = words[idx]
        for bit in (0, 1):
            words[idx] = base + (bit,)
            if rem > 0:
                assigned = words[:idx + 1]
                ok = True
                for v in itertools.product((0, 1), repeat=k + 1):
                    if optimistic(assigned, k + 1, rem, v) < (1 << (n - k - 1)):
                        ok = False
                        break
                if not ok:
                    continue
            dfs(k, words, idx + 1)
        words[idx] = base

    words = [tuple()] * M
    try:
        dfs(0, words, 0)
    except TimeoutError:
        return None, stats, time.time() - t0
    return found[0], stats, time.time() - t0

if __name__ == "__main__":
    tests = [(4, 3, False), (4, 4, True), (5, 6, False), (5, 7, True), (6, 11, False)]
    for (n, M, expect) in tests:
        r, st, el = run(n, M, tl=100.0)
        if r is None:
            verdict = "TIMEOUT"
        elif r and expect:
            verdict = "COVER FOUND  (correct, positive control OK)"
        elif (not r) and (not expect):
            verdict = "NO COVER -> K>M (lower bound, correct)"
        else:
            verdict = "*** MISMATCH ***"
        print(f"n={n} M={M} expect_cover={expect}: {verdict} | nodes={st['nodes']} | lvl={st['levels']} | {el:.1f}s", flush=True)
