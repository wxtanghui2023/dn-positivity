# c380_49_fejer_rigidity.py -- verification of the Fejer-kernel proof of the H1 rigidity lemma
# K_9(psi) = (1/9)|sum_{k=0}^{8} e^{ik psi}|^2 = 1 + (2/9) sum_{r=1}^{8}(9-r) cos(r psi)
import numpy as np, itertools
import mpmath as mp
mp.mp.dps = 50

def F(th, R=9):
    th = np.asarray(th, dtype=float)
    return np.array([np.sum(np.cos(r * th)) for r in range(1, R + 1)])

def K9_arr(th):
    th = np.asarray(th, dtype=float)
    return np.array([np.abs(np.sum(np.exp(1j * k * t) for k in range(9)))**2 / 9.0 for t in th])

print("=== A. Fejer identity: sum_j K_9(psi_j) == 4 + (2/9) sum_{r<=8}(9-r) F_r ===", flush=True)
rng = np.random.default_rng(5)
mx1 = mx2 = 0.0
for _ in range(20000):
    th = rng.uniform(0, 2 * np.pi, 4)
    f = F(th, 8)
    lhs = K9_arr(th).sum()
    rhs = 4 + (2.0 / 9.0) * sum((9 - r) * f[r - 1] for r in range(1, 9))
    mx1 = max(mx1, abs(lhs - rhs))
    lhs2 = sum((9 - r) * (f[r - 1] + 0.5) for r in range(1, 9))
    mx2 = max(mx2, abs(lhs2 - 4.5 * lhs))
print("   max residual (identity)      = %.3e" % mx1, flush=True)
print("   max residual (weighted form) = %.3e" % mx2, flush=True)

print()
print("=== B. exact combinatorial classification: 4-subsets of mu_9 \\ {1} ===", flush=True)
w = mp.e**(2j * mp.pi / 9)
hits = []
for S in itertools.combinations(range(1, 9), 4):
    Q = [mp.re(sum(w**(j * r) for j in S)) for r in range(1, 9)]
    if all(q <= mp.mpf(-1) / 2 + mp.mpf('1e-40') for q in Q):
        hits.append(S)
print("   #subsets with F_r<=-1/2 (r<=8) :", len(hits), flush=True)
f9 = {mp.nstr(mp.re(sum(w**(9 * j) for j in S)), 20) for S in hits}
print("   F_9 values at those subsets    :", f9, flush=True)
tight = all(all(abs(mp.re(sum(w**(j * r) for j in S)) + mp.mpf(1) / 2) < mp.mpf('1e-40') for r in range(1, 9)) for S in hits)
print("   all 8 constraints tight (exactly)?", tight, flush=True)
pair = [S for S in itertools.combinations(range(1, 9), 4)
        if all(((k in S) + ((9 - k) in S)) == 1 for k in (1, 2, 3, 4))]
print("   'one from each conjugate pair {k,9-k}' :", len(pair), "subsets (2^4 = 16 expected)", flush=True)
print("   matches the feasible list exactly?", sorted(pair) == sorted(hits), flush=True)
print("   list:", hits, flush=True)

print()
print("=== C. the sandwich on the 16 extremal points ===", flush=True)
for S in hits[:3]:
    th = np.array([2 * np.pi * j / 9 for j in S])
    f = F(th, 12)
    lhs = sum((9 - r) * (f[r - 1] + 0.5) for r in range(1, 9))
    print("   S=%-12s  sum_r (9-r)(F_r+1/2) = %+.3e   sum_j K_9 = %.3e   F_9 = %+.12f"
          % (str(S), lhs, K9_arr(th).sum(), f[8]), flush=True)
print("DONE", flush=True)
