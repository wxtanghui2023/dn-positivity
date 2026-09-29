#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""§5.4a 二阶段：①从零可行性（CP-SAT Σx ≤ k）②规模下降搜索（k-for-(k−1)）66 → 62

判据：从零得覆盖 512/512 的 62 词码（真值 K(9,1)=62）
纪律：pyguard 受控；单线程；bitmask（512 位 Python int）加速；每步落盘
"""
import random, time, os, sys

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
    print(f"  {tag}|C|={len(S)} 覆盖={Q-unc}/512 未覆盖={unc} 可删={len(red)} "
          f"E={sum(c-1 for c in cnt if c>=1)}", flush=True)
    return unc, red, cnt


def save_cert(S, tag):
    os.makedirs(OUT, exist_ok=True)
    p = os.path.join(OUT, f"n9_62_certificate_{tag}.txt")
    with open(p, "w") as f:
        f.write(f"# n=9 覆盖证书 track={tag} |C|={len(S)}\n")
        for v in sorted(S):
            f.write(" ".join(str((v >> i) & 1) for i in range(N)) + "\n")
    print(f"  证书：{os.path.relpath(p)}", flush=True)
    return p


# ───────────── ① 从零可行性（CP-SAT，Σx ≤ k）─────────────
def feas_cpsat(k, limit=60):
    from ortools.sat.python import cp_model
    m = cp_model.CpModel()
    x = [m.NewBoolVar(f"x{v}") for v in range(Q)]
    for t in range(Q):
        m.Add(sum(x[v] for v in NB[t]) >= 1)
    m.Add(sum(x) <= k)                      # 只问可行性，不优化 ⟹ 大幅易化
    s = cp_model.CpSolver()
    s.parameters.max_time_in_seconds = limit
    s.parameters.num_search_workers = 1
    t0 = time.time()
    st = s.Solve(m)
    dt = time.time() - t0
    if st in (cp_model.OPTIMAL, cp_model.FEASIBLE):
        S = {v for v in range(Q) if s.Value(x[v]) > 0}
        print(f"  CP-SAT k≤{k}: {s.StatusName(st)} |C|={len(S)} {dt:.1f}s", flush=True)
        return S, dt
    print(f"  CP-SAT k≤{k}: {s.StatusName(st)}（无解/未决） {dt:.1f}s", flush=True)
    return None, dt


# ───────────── ② 规模下降搜索 ─────────────
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


def crit(S, cnt):
    r = {}
    for v in S:
        r[v] = sum(1 for x in NB[v] if cnt[x] == 1)
    return r


def reduce_pass2(S):
    """2-for-1 / 2-for-0：删 2 补 ≤1"""
    cnt = to_count(S)
    crits = crit(S, cnt)
    L = sorted(S, key=lambda v: crits[v])
    for i in range(len(L)):
        for j in range(i + 1, len(L)):
            w1, w2 = L[i], L[j]
            R = set(S)
            R.discard(w1)
            R.discard(w2)
            U = umask(R)
            if U == 0:
                return ("2-for-0", w1, w2, None, R)
            for v in cands_for(U, S):
                if U & ~NM[v] == 0:
                    R.add(v)
                    return ("2-for-1", w1, w2, v, R)
    return None


def reduce_pass3(S, rng, budget=120, tries=60000):
    """3-for-2：删 3 补 ≤2（候选三元组优先低 crit）"""
    t0 = time.time()
    cnt = to_count(S)
    crits = crit(S, cnt)
    L = sorted(S, key=lambda v: crits[v])
    n = len(L)
    for t in range(tries):
        if time.time() - t0 > budget:
            break
        if t < 800:                                  # 先穷举低 crit 区
            i, j, k = rng.sample(range(min(n, 22)), 3)
        else:
            i, j, k = rng.sample(range(n), 3)
        R = set(S)
        for w in (L[i], L[j], L[k]):
            R.discard(w)
        U = umask(R)
        if U == 0:
            return ("3-for-0", (L[i], L[j], L[k]), (), R)
        if bin(U).count("1") > 24:                   # U 太大 ⟹ 2 词难补，跳过
            continue
        cs = list(cands_for(U, S))
        if len(cs) > 260:
            cs = cs[:260]
        found = None
        for a in range(len(cs)):
            ma = NM[cs[a]]
            if U & ~ma == 0:
                found = [cs[a]]
                break
            for b in range(a + 1, len(cs)):
                if U & ~(ma | NM[cs[b]]) == 0:
                    found = [cs[a], cs[b]]
                    break
            if found:
                break
        if found:
            for v in found:
                R.add(v)
            return ("3-for-2", (L[i], L[j], L[k]), tuple(found), R)
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
    print(f"  HiGHS seed: obj={r.fun} |C|={len(S)} gap={getattr(r,'mip_gap',None)}", flush=True)
    return S


def main():
    t_all = time.time()
    print("=" * 74)
    print("§5.4a 二阶段：从零可行性 + 规模下降搜索   |   判据：62 词覆盖")
    print("=" * 74)

    print("\n[1] 从零可行性（CP-SAT, Σx ≤ k）")
    win = None
    for k in (62, 63, 64, 65):
        S, dt = feas_cpsat(k, limit=45)
        if S is not None:
            report(S, f"  k≤{k}: ")
            if len(S) <= 62:
                win = ("cpsat_feas", S)
                break
        if time.time() - t_all > 200:
            break
    if win:
        save_cert(win[1], win[0])
    else:
        print("   ⟹ CP-SAT 可行性轨道未得 ≤62")

    print("\n[2] 规模下降搜索（自 HiGHS 种子起步）")
    S = hiGHS_seed(limit=90)
    report(S, "  seed: ")
    best = set(S)
    rng = random.Random(20260929)
    t0 = time.time()
    it = 0
    while time.time() - t0 < 200 and len(S) > 61:
        it += 1
        r = reduce_pass2(S)
        if r is None:
            r = reduce_pass3(S, rng, budget=45)
        if r is None:
            print(f"   第 {it} 轮：无改进 ⟹ 停（|C|={len(S)}）", flush=True)
            break
        kind, *rest = r
        S = r[-1]
        report(S, f"   第 {it} 轮 [{kind}]: ")
        if len(S) < len(best):
            best = set(S)
        if len(S) <= 62:
            break
    if len(best) <= 62:
        save_cert(best, "reduce")
        print(f"★ 判据达成：|C|={len(best)}")
    else:
        print(f"✗ 判据未达成：最小 |C|={len(best)}（起点 66）")

    print(f"\n总耗时 {time.time()-t_all:.1f}s")


if __name__ == "__main__":
    main()
