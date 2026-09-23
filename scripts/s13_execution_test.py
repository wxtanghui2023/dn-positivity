# S(13) execution test: verifier (0-1 principle) + space quantification + naive search baseline
# No RH. Pure execution test per operator ruling 2026-09-23.
import numpy as np, random, math, time, itertools
N = 13
ALL = np.array([[(k >> i) & 1 for i in range(N)] for k in range(1 << N)], dtype=np.int8)  # 8192 x 13

def apply_net(net, vecs=ALL):
    v = vecs.copy()
    for (i, j) in net:
        a = v[:, i].copy(); b = v[:, j].copy()
        v[:, i] = np.minimum(a, b); v[:, j] = np.maximum(a, b)
    return v

def sorts(net):
    v = apply_net(net)
    return bool(np.all(v[:, :-1] <= v[:, 1:]))

def bad_count(net):
    v = apply_net(net)
    return int(np.any(v[:, :-1] > v[:, 1:], axis=1).sum())

# ---- Batcher odd-even mergesort (classical construction) ----
def oddeven_merge(lo, n, r):
    step = r * 2
    if step < n:
        yield from oddeven_merge(lo, n, step)
        yield from oddeven_merge(lo + r, n, step)
        for i in range(lo + r, lo + n - r, step):
            yield (i, i + r)
    else:
        yield (lo, lo + r)

def batcher(lo, n):
    if n > 1:
        m = n // 2
        yield from batcher(lo, m)
        yield from batcher(lo + m, n - m)
        yield from oddeven_merge(lo, n, 1)

# Batcher on the next power of two, then project onto the first 13 lines (standard for non-powers)
M = 16
B_full = list(batcher(0, M))
B = [(i, j) for (i, j) in B_full if i < N and j < N]
print("=== [1] Batcher odd-even mergesort for n=13 ===")
print(f"size = {len(B)} comparators ; sorts(0-1 principle) = {sorts(B)}")

# ---- space quantification with standard reductions ----
print("\n=== [2] search-space quantification ===")
total_all = 78 ** 44
# telephone numbers T(n) = number of matchings (involutions) on n labelled points
T = [1, 1]
for k in range(2, N + 1):
    T.append(T[k-1] + (k-1) * T[k-2])
print(f"possible comparators on 13 lines     : C(13,2) = 78")
print(f"raw sequences, 44 comparators        : 78^44 = 10^{math.log10(total_all):.1f}")
print(f"max matchings per layer (13 odd)     : T(13) = {T[N]}")
# layered networks: layers are matchings; ~44/6 = 8 layers
print(f"layered upper bound (8 layers of max) : ~10^{8*math.log10(T[N]):.1f}")
print(f"even with canonical first layer (/T(13)): ~10^{8*math.log10(T[N])-math.log10(T[N]):.1f}")

print("\n=== [3] random-network needle test (how rare is 'sorting'?) ===")
random.seed(7)
for size in (30, 40, 44, 50):
    hits = 0; trials = 300
    for _ in range(trials):
        net = [(lambda ij: (min(ij), max(ij)))(tuple(random.sample(range(N), 2))) for _ in range(size)]
        if sorts(net): hits += 1
    print(f"size {size:3d}: sorting fraction over {trials} random networks = {hits}/{trials}")

print("\n=== [4] naive search baseline: can we shrink below the construction? ===")
t0 = time.time()
best = list(B); best_sz = len(best)
cur = list(B); budget = 150
it = 0; improved = True
while improved and time.time() - t0 < budget:
    improved = False
    for idx in range(len(cur) - 1, -1, -1):
        if time.time() - t0 > budget: break
        cand = cur[:idx] + cur[idx+1:]
        if sorts(cand):
            cur = cand; improved = True
    it += 1
print(f"construction size          : {best_sz}")
print(f"after deletion-only pruning: {len(cur)}   (elapsed {time.time()-t0:.1f}s)")
print(f"gap to 44                  : {len(cur)-44}")

print("\n=== [5] budget reality check ===")
t0 = time.time(); n_eval = 0
while time.time() - t0 < 3.0:
    net = [(lambda ij: (min(ij), max(ij)))(tuple(random.sample(range(N), 2))) for _ in range(44)]
    bad_count(net); n_eval += 1
rate = n_eval / 3.0
print(f"verified networks/sec (this machine): {rate:.0f}")
print(f"networks verifiable/day            : {rate*86400:.3e}")
print(f"raw 44-search space                : {total_all:.3e}")
print(f"ratio (space / daily capacity)     : {total_all/(rate*86400):.3e}")
