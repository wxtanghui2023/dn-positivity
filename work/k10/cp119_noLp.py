#!/usr/bin/env python3
"""
B1-a : SAME model as cp119.py (sum x = 119 ; per-vertex coverage ; x_0 = 1),
        but LP subsystems are switched OFF and several seeds are used.
Rationale: run 1 gave UNKNOWN / 0 incumbent with 2.45e7 conflicts; the uniform
fractional solution x_c = 119/1024 is feasible for the LP relaxation, so LP
bounds cannot refute 119 -> LP work is pure overhead. B1-a isolates that.

Tracked per segment: status, incumbent count, conflicts, branches, propagations,
restarts, deterministic_time, walltime, and ratios conflicts/branches and
propagations/branch.

Verdict table (locked):
  found + verify(1024/1024)  -> success, K(10,1) <= 119 with explicit certificate
  0 incumbent                -> no-LP also fails to enter the feasible region
  incumbent but unverified   -> must be independently verified
  INFEASIBLE                 -> keep solver proof/response (NOT just the summary)

Usage: cp119_noLp.py total_seconds seed1,seed2,...
"""
import sys, time, json
from ortools.sat.python import cp_model

n = 10
N = 1 << n
FULL = (1 << N) - 1
BALL = []
for w in range(N):
    m = 0
    for v in (w, *[w ^ (1 << i) for i in range(n)]):
        m |= 1 << v
    BALL.append(m)


def verify(code):
    if len(code) != len(set(code)):
        return False, "duplicate words"
    cov = 0
    for w in code:
        cov |= BALL[w]
    if cov != FULL:
        return False, f"{bin(FULL & ~cov).count('1')} uncovered"
    return True, "1024/1024 covered"


def set_subsolvers(solver, names):
    """try the several python bindings for SatParameters.subsolvers"""
    for how in ("slice", "extend", "assign", "extra"):
        try:
            p = solver.parameters
            if how == "slice":
                p.subsolvers[:] = names
            elif how == "extend":
                p.subsolvers.extend(names)
            elif how == "assign":
                p.subsolvers = names
            else:
                p.extra_subsolvers[:] = names
            print(f"[cfg] subsolvers set via {how} -> {names}", flush=True)
            return how
        except Exception as e:
            print(f"[cfg] {how} failed: {type(e).__name__}", flush=True)
    return None


def build():
    model = cp_model.CpModel()
    x = [model.NewBoolVar(f"x{c}") for c in range(N)]
    model.Add(sum(x) == 119)
    for v in range(N):
        model.Add(sum(x[c] for c in (v, *[v ^ (1 << i) for i in range(n)])) >= 1)
    model.Add(x[0] == 1)
    return model, x


def main():
    total = float(sys.argv[1]) if len(sys.argv) > 1 else 3600.0
    seeds = [int(s) for s in (sys.argv[2] if len(sys.argv) > 2 else "11,22,33,44").split(",")]
    per = total / len(seeds)
    summary = []
    for seed in seeds:
        model, x = build()
        solver = cp_model.CpSolver()
        solver.parameters.max_time_in_seconds = per
        solver.parameters.num_search_workers = 4
        solver.parameters.random_seed = seed
        solver.parameters.log_search_progress = True
        set_subsolvers(solver, ["no_lp"])

        box = {"best": None, "n_inc": 0}

        class CB(cp_model.CpSolverSolutionCallback):
            def on_solution_callback(self):
                box["n_inc"] += 1
                code = [c for c in range(N) if self.Value(x[c]) == 1]
                ok, msg = verify(code)
                print(f"[incumbent] seed={seed} size={len(code)} verify={ok} ({msg}) t={self.WallTime():.1f}s", flush=True)
                if ok:
                    box["best"] = sorted(code)
                    json.dump({"n": n, "k": len(code), "code": box["best"], "verified": True, "seed": seed},
                              open("code119_B1a.json", "w"))
                    print("★★★ 已验证 119-cover ⟹ K(10,1) <= 119 (code119_B1a.json)", flush=True)
                    self.StopSearch()

        cb = CB()
        t0 = time.time()
        status = solver.Solve(model, cb)
        wt = time.time() - t0
        st = solver.StatusName(status)
        try:
            rp = solver.ResponseProto()
        except Exception:
            rp = None

        def g(name, default=None):
            if rp is not None and hasattr(rp, name):
                return getattr(rp, name)
            return default

        cf = g("num_conflicts", None)
        br = g("num_branches", None)
        pr = g("num_binary_propagations", None)
        ipr = g("num_integer_propagations", None)
        rst = g("num_restarts", None)
        dt = g("deterministic_time", None)
        if cf is None:
            cf = solver.NumConflicts() if hasattr(solver, "NumConflicts") else None
        if br is None:
            br = solver.NumBranches() if hasattr(solver, "NumBranches") else None
        row = {"seed": seed, "status": st, "incumbent": box["n_inc"],
               "conflicts": cf, "branches": br, "propagations": pr,
               "integer_propagations": ipr, "restarts": rst,
               "deterministic_time": dt, "walltime": round(wt, 2),
               "conflicts_per_branch": round(cf / br, 4) if (cf and br) else None,
               "propagations_per_branch": round(pr / br, 2) if (pr and br) else None}
        summary.append(row)
        print(f"[segment] seed={seed} status={st} incumbent={box['n_inc']} conflicts={cf} branches={br} "
              f"propagations={pr} int_prop={ipr} restarts={rst} dtime={dt} "
              f"wall={wt:.1f}s  cf/br={row['conflicts_per_branch']}  prop/br={row['propagations_per_branch']}", flush=True)
        if box["best"]:
            ok, msg = verify(box["best"])
            print(f"=== SUCCESS: verified 119-cover ({msg}) ===")
            break
        if st == "INFEASIBLE":
            print("=== INFEASIBLE: 119 不可能 ⟹ K(10,1) = 120（须保留 solver 证据）===", flush=True)
            try:
                rp = solver.ResponseProto()
                open("response_infeasible.pb", "wb").write(rp.SerializeToString())
                print("[proof] ResponseProto 已保存 response_infeasible.pb", flush=True)
            except Exception as e:
                print(f"[proof] ResponseProto 保存失败: {type(e).__name__}: {e}", flush=True)
            try:
                open("response_infeasible.txt", "w").write(str(solver.ResponseProto()))
            except Exception:
                pass
            break
    json.dump(summary, open("b1a_summary.json", "w"), indent=1)
    print("=== B1-a 汇总 ===")
    for r in summary:
        print(json.dumps(r, ensure_ascii=False))
    print("判定（锁死）：无 incumbent ⟹ “no-LP 也无法进入可行域”；**不得**表述为 119 不存在。")


main()
