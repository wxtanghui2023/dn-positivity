#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""§5.4a 深化：j-for-(j−1) 下降阶梯（2→3→4），目标 62

种子：HiGHS MIP（≤90s）⟹ 反复施加 2-for-1 / 3-for-2 / 4-for-3（低 crit 优先，按层级穷举）
纪律：pyguard；单线程；bitmask 加速
"""
import random, time, os, sys, itertools

N = 9
Q = 1 << N
MASK = [1 << i for i in range(N)]
NB = [[v] + [v ^ m for m in MASK] for v in range(Q)]
FULL = (1 << Q) - 1
NM = [0] * Q
for v in range(Q):
    m = 0
    for x in NB[v]:
        m |= 1 << x
    NM[v] = m
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "out")


def umask(S):
    m = 0
    for v in S:
        m |= NM[v]
    return FULL & ~m


def to_count(S):
    cnt = [0] * Q
    for v in S:
        for x in NB[v]:
            cnt[x] += 1
    return cnt


def report(S, tag=""):
    cnt = to_count(S)
    unc = sum(1 for c in cnt if c == 0)
    red = [v for v in S if all(cnt[x] > 1 for x in NB[v])]
    print(f"  {tag}|C|={len(S)} 覆盖={Q-unc}/512 未覆盖={unc} 可删={len(red)}", flush=True)
    return unc, red


def save_cert(S, tag):
    os.makedirs(OUT, exist_ok=True)
    p = os.path.join(OUT, f"n9_certificate_{tag}.txt")
    with open(p, "w") as f:
        f.write(f"# n=9 |C|={len(S)} track={tag}\n")
        for v in sorted(S):
            f.write(" ".join(str((v >> i) & 1) for i in range(N)) + "\n")
    print(f"  证书：{os.path.relpath(p)}", flush=True)


def crits(S):
    cnt = to_count(S)
    return {v: sum(1 for x in NB[v] if cnt[x] == 1) for v in S}


def cands_for(U, S):
    c = set()
    x = U
    while x:
        b = (x & -x).bit_length() - 1
        x ^= 1 << b
        for v in NB[b]:
            if v not in S:
                c.add(v)
    return c


def refill(U, S, maxk):
    """找 ≤maxk 个词覆盖 U（S_v 去支配后小规模穷举）；返回词表或 None"""
    if U == 0:
        return []
    cs = list(cands_for(U, S))
    sub = [(v, NM[v] & U) for v in cs]
    sub.sort(key=lambda t: -bin(t[1]).count("1"))
    keep = []
    for v, s in sub:
        if not any((s | s2) == s2 for _, s2 in keep):     # s ⊆ s2 ⟹ 丢弃 s
            keep.append((v, s))
        if len(keep) >= 40:
            break
    for k in range(1, maxk + 1):
        for comb in itertools.combinations(range(len(keep)), k):
            m = 0
            for i in comb:
                m |= keep[i][1]
            if U & ~m == 0:
                return [keep[i][0] for i in comb]
    return None


def hiGHS_seed(limit=90):
    import numpy as np
    from scipy.optimize import milp, LinearConstraint, Bounds
    A = np.zeros((Q, Q))
    for t in range(Q):
        for v in NB[t]:
            A[t, v] = 1.0
    r = milp(c=np.ones(Q), constraints=LinearConstraint(A, lb=1.0, ub=np.inf),
             integrality=np.ones(Q), bounds=Bounds(0, 1),
             options={"time_limit": limit})
    S = {v for v in range(Q) if r.x[v] > 0.5}
    print(f"  HiGHS seed: obj={r.fun} |C|={len(S)}", flush=True)
    return S


def ladder(S, rng, t_budget=240):
    """返回改进后的 S；逐层 j-for-(j−1)"""
    t0 = time.time()
    improved = True
    while improved and time.time() - t0 < t_budget:
        improved = False
        cs = crits(S)
        L = sorted(S, key=lambda v: cs[v])
        # ── j=2 ──
        hit = None
        for a, b in itertools.combinations(range(min(len(L), 30)), 2):
            R = set(S) - {L[a], L[b]}
            U = umask(R)
            if U == 0:
                hit = ("2-for-0", (L[a], L[b]), (), R); break
            rf = refill(U, S, 1)
            if rf is not None and len(rf) <= 1:
                hit = ("2-for-1", (L[a], L[b]), rf, R); break
        # ── j=3 ──
        if hit is None:
            for t3 in itertools.combinations(range(min(len(L), 26)), 3):
                R = set(S) - {L[i] for i in t3}
                U = umask(R)
                if bin(U).count("1") > 26:
                    continue
                rf = refill(U, S, 2)
                if rf is not None:
                    hit = ("3-for-2", tuple(L[i] for i in t3), rf, R); break
        # ── j=4 ──
        if hit is None:
            budget4 = min(60000, max(20000, int(4e4)))
            cnt4 = 0
            for t4 in itertools.combinations(range(min(len(L), 30)), 4):
                cnt4 += 1
                if cnt4 > budget4 or time.time() - t0 > t_budget:
                    break
                R = set(S) - {L[i] for i in t4}
                U = umask(R)
                if bin(U).count("1") > 20:
                    continue
                rf = refill(U, S, 3)
                if rf is not None:
                    hit = ("4-for-3", tuple(L[i] for i in t4), rf, R); break
        if hit is None:
            break
        kind, removed, added, R = hit
        for v in added:
            R.add(v)
        S = R
        improved = True
        report(S, f"  [{kind}] ")
        if len(S) <= 62:
            break
    return S


def main():
    t_all = time.time()
    print("=" * 72)
    print("§5.4a 深化：j-for-(j−1) 阶梯   |   目标 62")
    print("=" * 72)
    S = hiGHS_seed(limit=90)
    report(S, "seed: ")
    best = set(S)
    rng = random.Random(7)
    for rnd in range(3):
        S = ladder(S, rng, t_budget=180)
        if len(S) < len(best):
            best = set(S)
        if len(best) <= 62:
            break
        print(f"  第 {rnd+1} 轮阶梯结束：|C|={len(S)}（best {len(best)}）", flush=True)
        if time.time() - t_all > 400:
            break
    report(best, "best: ")
    save_cert(best, "reduce_deep")
    print(f"★ {'判据达成 |C|=62' if len(best) <= 62 else f'判据未达成，最好 |C|={len(best)}'}")
    print(f"总耗时 {time.time()-t_all:.1f}s")


if __name__ == "__main__":
    main()
