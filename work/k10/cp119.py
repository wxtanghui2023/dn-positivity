#!/usr/bin/env python3
"""
X1 / K(10,1) <= 119 : GLOBAL exact CP-SAT model.

Model (exactly as specified):
    x_c in {0,1},  c in {0,...,1023}          (all words of {0,1}^10)
    sum_c x_c == 119                          (exact size, not min-cover)
    for each vertex v in {0,1}^10:
        sum_{c : d_H(c,v) <= 1} x_c >= 1      (each constraint touches exactly 11 vars)
Symmetry breaking: x_0 == 1  (word 00..0), WLOG by Aut(Q_10) = C_2^10 : S_10.
Warm hint: the verified 120-code minus one word, after a coordinate flip that sends one of
its words to 0 (flip = automorphism, so it stays a cover of size 119 iff it was).
Delivery rule: every feasible solution is INDEPENDENTLY re-verified (1024/1024 coverage);
the solver reporting a solution is not a certificate - only verify()==True is.

Verdict discipline:
  found+verified -> K(10,1) <= 119  (new upper bound record)
  not found      -> "global CP-SAT did not find 119 within the given model/symmetry/budget"
                    (NOT "119 does not exist"; that needs an UNSAT certificate / proof)
Usage: cp119.py seconds seed
"""
import sys, time, json
from ortools.sat.python import cp_model

n = 10
N = 1 << n
FULL = (1 << N) - 1


def ball_mask(w):
    m = 0
    for v in (w, *[w ^ (1 << i) for i in range(n)]):
        m |= 1 << v
    return m


BALL = [ball_mask(w) for w in range(N)]


def verify(code):
    """independent coverage verifier (do not trust the solver)"""
    if len(code) != len(set(code)):
        return False, "duplicate words"
    cov = 0
    for w in code:
        cov |= BALL[w]
    if cov != FULL:
        unc = bin(FULL & ~cov).count("1")
        return False, f"{unc} uncovered"
    return True, "1024/1024 covered"


def flip_to_zero(code, word):
    """coordinate flip (automorphism) mapping `word` to 0"""
    return [c ^ word for c in code]


def main():
    secs = float(sys.argv[1]) if len(sys.argv) > 1 else 600.0
    seed = int(sys.argv[2]) if len(sys.argv) > 2 else 1

    model = cp_model.CpModel()
    x = [model.NewBoolVar(f"x{c}") for c in range(N)]
    model.Add(sum(x) == 119)                      # exact size
    for v in range(N):
        model.Add(sum(x[c] for c in (v, *[v ^ (1 << i) for i in range(n)])) >= 1)
    model.Add(x[0] == 1)                          # symmetry breaking (WLOG)

    # warm hint: 120-code minus its least-private word, flipped so that it contains 0
    words = [int(s, 2) for s in open("kamenetsky120.txt").read().split()]
    cnt = {}
    for w in words:
        for v in (w, *[w ^ (1 << i) for i in range(n)]):
            cnt[v] = cnt.get(v, 0) + 1
    priv = sorted((sum(1 for v in (w, *[w ^ (1 << i) for i in range(n)]) if cnt[v] == 1), w) for w in words)
    drop = priv[0][1]
    hint119 = [c for c in words if c != drop]
    ok, msg = verify(hint119)
    print(f"hint(119) 独立验证: {ok} ({msg});  (dropped {drop:010b})", flush=True)
    hint = flip_to_zero(hint119, hint119[0])
    ok2, msg2 = verify(hint)
    print(f"flip 后 hint 仍为覆盖: {ok2} ({msg2}); 含零字: {0 in hint}", flush=True)
    for c in range(N):
        model.add_hint(x[c], 1 if c in set(hint) else 0)

    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = secs
    solver.parameters.num_search_workers = 4
    solver.parameters.random_seed = seed
    solver.parameters.log_search_progress = True

    found = {}


    class CB(cp_model.CpSolverSolutionCallback):
        def __init__(self):
            super().__init__()
            self.best = None

        def on_solution_callback(self):
            code = [c for c in range(N) if self.Value(x[c]) == 1]
            ok, msg = verify(code)
            print(f"[incumbent] size={len(code)} verify={ok} ({msg}) t={self.WallTime():.1f}s", flush=True)
            if ok:
                self.best = sorted(code)
                json.dump({"n": n, "k": len(code), "code": self.best, "verified": True},
                          open("code119_GLOBAL.json", "w"))
                print("★★★ 已验证 119-cover ⟹ K(10,1) <= 119 写出 code119_GLOBAL.json", flush=True)
                self.StopSearch()

    cb = CB()
    t0 = time.time()
    status = solver.Solve(model, cb)
    print("status:", solver.StatusName(status), f"wall={time.time()-t0:.1f}s")
    print("conflicts:", solver.NumConflicts(), "branches:", solver.NumBranches())
    if cb.best:
        ok, msg = verify(cb.best)
        print(f"最终交付验证: {ok} ({msg}); size={len(cb.best)}")
        print("code:", " ".join(format(c, '010b') for c in cb.best))
    else:
        print("→ 未在预算内找到 119-cover。")
        print("   判定（锁死）: 全局 CP-SAT 在给定模型/对称性/预算下未找到 119；")
        print("   **不得**表述为“119 不存在”（那需要 UNSAT 证书或独立数学下界 120）。")


main()
