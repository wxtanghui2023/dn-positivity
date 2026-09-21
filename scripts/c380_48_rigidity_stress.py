# c380_48_rigidity_stress.py -- vectorized stress test for the rigidity claim
import numpy as np, itertools
from scipy.optimize import root

R = 12
def Fmat(th):
    # th: (N,4) -> (N,R)
    th = np.atleast_2d(np.asarray(th, dtype=float))
    rr = np.arange(1, R + 1)[None, :, None]
    return np.cos(rr * th[:, None, :]).sum(axis=2)

rng = np.random.default_rng(20240921)
N = 60000
th = rng.uniform(0, 2 * np.pi, size=(N, 4))
# seed a fraction at cyclotomic points to check they are stable attractors
k = N // 10
th[:k] = 2 * np.pi * rng.integers(0, 9, size=(k, 4)) / 9

print("=== T1 (vectorized penalty descent, N=%d) ===" % N, flush=True)
step = 0.4
best_v = np.full(N, 1e9)
best_th = th.copy()
for it in range(500):
    cur = np.maximum(Fmat(th)[:, :8] + 0.5, 0.0).sum(1)
    upd = cur < best_v
    best_v[upd] = cur[upd]; best_th[upd] = th[upd]
    j = it % 4
    th[:, j] += rng.normal(0, step)
    th = np.mod(th, 2 * np.pi)
    if it % 50 == 49: step *= 0.65
cur = np.maximum(Fmat(th)[:, :8] + 0.5, 0.0).sum(1)
upd = cur < best_v
best_v[upd] = cur[upd]; best_th[upd] = th[upd]

feas = best_th[best_v <= 1e-12]
print("   feasible points found :", len(feas), " (out of %d starts)" % N, flush=True)
if len(feas):
    key = np.round(np.sort(feas, axis=1), 6)
    uniq = np.unique(key, axis=0)
    print("   distinct feasible points :", len(uniq), flush=True)
    F9 = Fmat(uniq)[:, 8]
    print("   distinct F_9 values :", sorted(set(np.round(F9, 9))), flush=True)
    z = uniq * 9 / (2 * np.pi)
    cyc = np.all(np.abs(z - np.round(z)) < 1e-9, axis=1)
    print("   cyclotomic (multiple of 2pi/9) :", int(cyc.sum()), "/", len(uniq), flush=True)
    tight = np.sum(np.abs(Fmat(uniq)[:, :8] + 0.5) < 1e-9, axis=1)
    print("   #tight constraints (of 8) :", sorted(set(tight.tolist())), flush=True)

print()
print("=== T2. over-determined active sets (size 5..8), few starts each ===", flush=True)
for k in (5, 6, 7, 8):
    cnt = 0; seen = []
    sets = list(itertools.combinations(range(1, 9), k))
    rng.shuffle(sets)
    for active in sets[:25]:
        for t in range(3):
            th0 = 2 * np.pi * rng.integers(0, 9, size=4) / 9 + rng.normal(0, 0.2, 4)
            try:
                s = root(lambda x: Fmat(x)[0][[a - 1 for a in active]] + 0.5, th0, method='lm')
            except Exception:
                continue
            f = Fmat(s.x)[0]
            if np.all(f[:8] <= -0.5 + 1e-8):
                thm = np.sort(np.mod(s.x, 2 * np.pi))
                if not any(np.allclose(thm, u, atol=1e-5) for u in seen):
                    seen.append(thm); cnt += 1
    print("   size %d : degenerate feasible solutions found = %d" % (k, cnt), flush=True)

print()
print("=== T3. exact equivalence: F_9 = 4  <=>  all nodes are 9th roots of unity ===", flush=True)
for S in [(1, 2, 3, 4), (1, 4, 6, 7), (0, 1, 2, 3), (2, 4, 6, 8)]:
    th0 = 2 * np.pi * np.array(S) / 9
    print("   S=%-14s F_9 = %+.12f" % (str(S), Fmat(th0)[0][8]), flush=True)
print("   generic point  F_9 = %+.6f   (global max = 4)" % Fmat([0.1, 1.0, 2.0, 3.0])[0][8], flush=True)
print("DONE", flush=True)
