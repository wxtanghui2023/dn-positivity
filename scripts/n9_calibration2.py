#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""n=9 上界侧搜索校准 · v2（交接档 §5.4a / PLAN-119-DETAILED-V2 §U1）

判据：**从零**得到覆盖 512/512 的 **62** 词码（真值 K(9,1)=62）
三条轨道：①锚点核验 ②局部搜索（修好温度/接受律）③精确搜索（CP-SAT / HiGHS-MILP，U1 允许的"ILP 子问题"）
纪律：pyguard 受控运行；单线程；种子可复跑
"""
import random, time, os, math

N = 9
Q = 1 << N
MASK = [1 << i for i in range(N)]
NB = [[v] + [v ^ m for m in MASK] for v in range(Q)]
NBS = [frozenset(s) for s in NB]
HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "..", "sources",
                   "KERI-CD-K_9_1-the-optimal-9-62-binary-covering-code.txt")
OUT = os.path.join(HERE, "..", "out")


def load_known():
    C = []
    for line in open(SRC):
        t = line.split()
        if len(t) != N:
            continue
        C.append(sum(int(b) << i for i, b in enumerate(t)))
    return C


def counts(C):
    cnt = [0] * Q
    for v in C:
        for x in NB[v]:
            cnt[x] += 1
    return cnt


def report(C, tag=""):
    cnt = counts(C)
    unc = sum(1 for c in cnt if c == 0)
    red = [v for v in C if all(cnt[x] > 1 for x in NB[v])]
    E = sum(c - 1 for c in cnt if c >= 1)
    print(f"  {tag}|C|={len(C)} dist={len(set(C))} 覆盖={Q-unc}/512 未覆盖={unc} "
          f"可删={len(red)} E={E}")
    return Q - unc, unc, red, cnt


def save_cert(C, seed, tag):
    os.makedirs(OUT, exist_ok=True)
    p = os.path.join(OUT, f"n9_62_certificate_{tag}.txt")
    with open(p, "w") as f:
        f.write(f"# n=9 62 词覆盖证书 (track={tag} seed={seed})\n")
        for v in sorted(C):
            f.write(" ".join(str((v >> i) & 1) for i in range(N)) + "\n")
    return p


# ─────────────────── 局部搜索（修好版） ───────────────────
class St:
    __slots__ = ("inS", "cnt", "S", "U", "E")

    def __init__(self, S):
        self.inS = [False] * Q
        self.S = list(S)
        for v in self.S:
            self.inS[v] = True
        self.cnt = counts(self.S)
        self.U = sum(1 for c in self.cnt if c == 0)
        self.E = sum(c - 1 for c in self.cnt if c >= 1)

    def cost(self):
        return self.U * 1000 + self.E

    def rm(self, v):
        self.S.remove(v)
        self.inS[v] = False
        for x in NB[v]:
            c = self.cnt[x]
            self.cnt[x] = c - 1
            if c == 1:
                self.U += 1
            else:
                self.E -= 1

    def ad(self, v):
        self.S.append(v)
        self.inS[v] = True
        for x in NB[v]:
            c = self.cnt[x]
            self.cnt[x] = c + 1
            if c == 0:
                self.U -= 1
            else:
                self.E += 1

    def dswap(self, w, v):
        Sw, Sv = NBS[w], NBS[v]
        du = de = 0
        for x in Sw - Sv:
            if self.cnt[x] == 1:
                du += 1
            else:
                de -= 1
        for x in Sv - Sw:
            if self.cnt[x] == 0:
                du -= 1
            else:
                de += 1
        return du, de, du * 1000 + de

    def snapshot(self):
        return (list(self.S), list(self.cnt), self.U, self.E)

    def restore(self, snap):
        self.S, self.cnt, self.U, self.E = list(snap[0]), list(snap[1]), snap[2], snap[3]
        self.inS = [False] * Q
        for v in self.S:
            self.inS[v] = True


def local_search(k, seed, secs=20.0, noise=0.80, T0=0.8, T1=0.06):
    """WalkSAT 型：噪声分支=定向修未覆盖点（无条件接受）；降温分支=1-for-1 SA"""
    rng = random.Random(seed)
    st = St(rng.sample(range(Q), k))
    T, best, best_cost = T0, st.snapshot(), st.cost()
    t0, it, stall = time.time(), 0, 0
    while time.time() - t0 < secs:
        it += 1
        if it % 20000 == 0:
            T = max(T1, T * 0.85)
            if it % 100000 == 0:
                print(f"      [it {it}] U={st.U} E={st.E} T={T:.3f} best U={best[2]}", flush=True)
        if st.U == 0:
            return st, it, time.time() - t0, True
        if rng.random() < noise:
            x = rng.choice([z for z in range(Q) if st.cnt[z] == 0])
            cands = [u for u in NB[x] if not st.inS[u]]
            if not cands:
                continue
            v = rng.choice(cands)
            w = min(rng.sample(st.S, min(10, len(st.S))), key=lambda z: st.dswap(z, v)[2])
            st.rm(w)
            st.ad(v)
        else:
            w = rng.choice(st.S)
            v = rng.randrange(Q)
            if st.inS[v]:
                continue
            _, _, d = st.dswap(w, v)
            if d <= 0 or rng.random() < math.exp(-min(50.0, d / max(T, 1e-6))):
                st.rm(w)
                st.ad(v)
        c = st.cost()
        if c < best_cost:
            best_cost, best, stall = c, st.snapshot(), 0
        else:
            stall += 1
        if stall > 60000:                       # 卡住 ⟹ 回滚 + 升温 + 加噪
            st.restore(best)
            stall, noise, T = 0, min(0.97, noise + 0.05), min(2.0, T * 2.0)
    return st, it, time.time() - t0, False


# ─────────────────── 精确搜索轨道 ───────────────────
def exact_cpsat(limit=90):
    from ortools.sat.python import cp_model
    m = cp_model.CpModel()
    x = [m.NewBoolVar(f"x{v}") for v in range(Q)]
    for t in range(Q):
        m.Add(sum(x[v] for v in NB[t]) >= 1)
    m.Minimize(sum(x))
    s = cp_model.CpSolver()
    s.parameters.max_time_in_seconds = limit
    s.parameters.num_search_workers = 1
    t0 = time.time()
    st = s.Solve(m)
    dt = time.time() - t0
    C = [v for v in range(Q) if s.Value(x[v]) > 0]
    print(f"  CP-SAT: status={s.StatusName(st)} obj={s.ObjectiveValue()} "
          f"bound={s.BestObjectiveBound()} |C|={len(C)} {dt:.1f}s")
    return C, s.ObjectiveValue(), s.BestObjectiveBound(), dt


def exact_milp(limit=90):
    import numpy as np
    from scipy.optimize import milp, LinearConstraint, Bounds
    A = np.zeros((Q, Q))
    for t in range(Q):
        for v in NB[t]:
            A[t, v] = 1.0
    t0 = time.time()
    res = milp(c=np.ones(Q), constraints=LinearConstraint(A, lb=1.0, ub=np.inf),
               integrality=np.ones(Q), bounds=Bounds(0, 1),
               options={"time_limit": limit, "presolve": True})
    dt = time.time() - t0
    C = [v for v in range(Q) if res.x[v] > 0.5]
    print(f"  HiGHS: status={res.status} obj={res.fun} |C|={len(C)} "
          f"mip_gap={getattr(res,'mip_gap',None)} {dt:.1f}s")
    return C, res.fun, dt


def main():
    t_all = time.time()
    print("=" * 74)
    print("§5.4a  n=9 上界侧校准 v2  |  判据：从零得 62 词覆盖（真值 62）")
    print("=" * 74)

    print("\n[0] 锚点核验（KERI 已知 62-码）")
    known = load_known()
    report(known, "anchor: ")

    print("\n[1] 局部搜索（WalkSAT 型，k=62，从零）")
    ls_win = None
    t0 = time.time()
    for seed in (11, 202, 3033, 40404):
        if time.time() - t0 > 75:
            print("   [局部搜索总预算用尽]")
            break
        st, it, dt, ok = local_search(62, seed, secs=18.0)
        print(f"   seed={seed}: U={st.U} E={st.E} iters={it} {dt:.1f}s "
              f"{'✓ 62-cover' if ok else '✗'}", flush=True)
        if ok:
            ls_win = (seed, sorted(st.S))
            report(ls_win[1], "   局部搜索结果: ")
            break
    if ls_win:
        p = save_cert(ls_win[1], ls_win[0], "localsa")
        print(f"   证书：{os.path.relpath(p)}")

    print("\n[2] 精确搜索：CP-SAT（512 布尔变量，逐点覆盖约束）")
    try:
        C, obj, bound, dt = exact_cpsat(limit=90)
        report(C, "   CP-SAT 结果: ")
        if len(C) <= 62:
            save_cert(C, "cpsat", "cpsat")
        print(f"   ⟹ 上界 {len(C)}；对偶界 {bound} ⟹ "
              f"{'已证 min=62（与文献一致 ✓✓）' if bound >= 62 else '对偶界未闭合'}")
    except Exception as e:
        print("   CP-SAT 失败:", e)

    print("\n[3] 精确搜索：HiGHS MILP")
    try:
        C, obj, dt = exact_milp(limit=90)
        report(C, "   HiGHS 结果: ")
    except Exception as e:
        print("   HiGHS 失败:", e)

    print(f"\n总耗时 {time.time()-t_all:.1f}s")


if __name__ == "__main__":
    main()
