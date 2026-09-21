# c380_48_harmonic9_entrance.py -- H1: entrance audit for r=9
# F_r = Re sum_j z_j^r = sum_j cos(r psi_j); constraints F_1..F_8 <= -1/2
import numpy as np, itertools
from scipy.optimize import root, minimize

def F(th, R=12):
    th = np.asarray(th, dtype=float)
    return np.array([np.sum(np.cos(r * th)) for r in range(1, R + 1)])

def check(th):
    f = F(th, 12)
    return f, bool(np.all(f[:8] <= -0.5 + 1e-9))

print("=== A. reference: 16 cyclotomic points (n=9) ===", flush=True)
n9 = [S for S in itertools.combinations(range(9), 4)]
good = []
for S in n9:
    th = np.array([2 * np.pi * j / 9 for j in S])
    f = F(th, 12)
    if np.all(f[:8] <= -0.5 + 1e-9):
        good.append(S)
print("   n=9 subsets feasible for r<=8 :", len(good), flush=True)
print("   their F_9 values:", sorted(set(round(float(F(np.array([2*np.pi*j/9 for j in S]),12)[8]), 9) for S in good)), flush=True)

print()
print("=== B. enumeration: all 4-tight boundary solutions (active sets C(8,4)=70) ===", flush=True)
rng = np.random.default_rng(11)
sols = []
for active in itertools.combinations(range(1, 9), 4):
    for t in range(40):
        th0 = rng.uniform(0, 2 * np.pi, 4) if t else np.array([2 * np.pi * j / 9 for j in (1, 2, 3, 4)])
        try:
            s = root(lambda th: F(th, 12)[[a - 1 for a in active]] + 0.5, th0, method='hybr', tol=1e-13)
        except Exception:
            continue
        if not s.success:
            continue
        th = s.x
        f = F(th, 12)
        if np.all(f[:8] <= -0.5 + 1e-8):
            thm = np.sort(np.mod(th, 2 * np.pi))
            if not any(np.allclose(thm, u, atol=1e-6) for u in sols):
                sols.append(thm)
print("   distinct feasible boundary solutions found :", len(sols), flush=True)
for thm in sols[:20]:
    f = F(thm, 12)
    print("     th/pi = %s   F[1..9] = %s   F9 = %+.9f" % (np.round(thm / np.pi, 6), np.round(f[:9], 6), f[8]), flush=True)
if sols:
    print("   min/max F_9 over found solutions :", float(min(F(u, 12)[8] for u in sols)), float(max(F(u, 12)[8] for u in sols)), flush=True)

print()
print("=== C. global: minimize F_9 s.t. F_1..F_8 <= -1/2 (SLSQP, multistart) ===", flush=True)
cons = [{'type': 'ineq', 'fun': (lambda th, r=r: -0.5 - np.sum(np.cos(r * th)))} for r in range(1, 9)]
best = None
for t in range(400):
    th0 = rng.uniform(0, 2 * np.pi, 4)
    try:
        res = minimize(lambda th: np.sum(np.cos(9 * th)), th0, method='SLSQP',
                       constraints=cons, options={'maxiter': 400, 'ftol': 1e-14})
    except Exception:
        continue
    if res.success and np.all(F(res.x, 12)[:8] <= -0.5 + 1e-7):
        if best is None or res.fun < best[0]:
            best = (res.fun, np.sort(np.mod(res.x, 2 * np.pi)))
if best:
    print("   best (min) F_9 = %+.9f  at th/pi = %s" % (best[0], np.round(best[1] / np.pi, 6)), flush=True)
    print("   F[1..12] there =", np.round(F(best[1], 12), 6), flush=True)
else:
    print("   no feasible point found by SLSQP multistart", flush=True)

print()
print("=== D. sum-identity bound check (why the coarse method fails) ===", flush=True)
ps = np.linspace(1e-4, 2 * np.pi - 1e-4, 400000)
g = np.array([np.sum(np.cos(r * p) for r in range(1, 9)) for p in ps])
print("   min over psi of sum_{r<=8} cos(r psi) = %.6f ; 4 nodes lower bound = %.4f (need <= -4)" % (g.min(), 4 * g.min()), flush=True)
print("DONE", flush=True)
