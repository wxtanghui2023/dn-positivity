#!/usr/bin/env python3
"""
X1 / K(10,1) : directed (3,2) sweep  -- OPTIMISED version.
Pruning:
  P1  |M(D)| > 22          -> dead          (two radius-1 balls cover <= 2*11 = 22)
  P2  two-ball test done through the "vertex -> candidate coverers" index:
      pick the vertex of M(D) with the fewest coverers (<= 11), branch on those only.
Effects: candidates examined per triple <= 11 * 11 = 121 instead of 904*904.
Output: multiplicity histogram, |M(D)| distribution, prune/ survivor statistics, verdict.
"""
import time, json
from collections import Counter, defaultdict

n = 10; N = 1 << n; FULL = (1 << N) - 1
words = [int(s, 2) for s in open("kamenetsky120.txt").read().split()]
ws = set(words)

def ball(w):
    return [w] + [w ^ (1 << i) for i in range(n)]

def bmask(w):
    m = 0
    for v in ball(w):
        m |= 1 << v
    return m

# multiplicity structure
owners = [[] for _ in range(N)]
for i, w in enumerate(words):
    for v in ball(w):
        owners[v].append(i)
mult = [len(owners[v]) for v in range(N)]
hist = Counter(mult)
S = [0] * 120
D2 = defaultdict(int)
D3 = defaultdict(int)
for v in range(N):
    o = owners[v]; m = 1 << v
    if len(o) == 1: S[o[0]] |= m
    elif len(o) == 2: D2[(o[0], o[1])] |= m
    elif len(o) == 3: D3[(o[0], o[1], o[2])] |= m

cand = [w for w in range(N) if w not in ws]
CBM = [bmask(w) for w in cand]
# vertex -> candidate coverers (index over candidates)
coverers = [[] for _ in range(N)]
for ci, w in enumerate(cand):
    for v in ball(w):
        coverers[v].append(ci)

pc = int.bit_count if hasattr(int, "bit_count") else (lambda x: bin(x).count("1"))

t0 = time.time()
tot = 0; pruned = 0; survivors = 0; size_hist = Counter()
hits = []
for i in range(120):
    Si = S[i]
    for j in range(i + 1, 120):
        Sj = S[j]; D2ij = D2.get((i, j), 0)
        for k in range(j + 1, 120):
            tot += 1
            if tot % 20000 == 0:
                print(f"  ...{tot}/{280840} triples, pruned={pruned}, survivors={survivors}, t={time.time()-t0:.0f}s", flush=True)
            M = Si | Sj | S[k] | D2ij | D2.get((i, k), 0) | D2.get((j, k), 0) | D3.get((i, j, k), 0)
            sz = pc(M)
            size_hist[sz] += 1
            if sz > 22:
                pruned += 1
                continue
            survivors += 1
            if sz == 0:
                hits.append(("del3", (i, j, k), None)); continue
            # ---- fast two-ball test via coverer index ----
            # choose vertex of M with fewest candidate coverers
            mm = M; best_v = -1; best_n = 10 ** 9
            while mm:
                b = mm & -mm; v = b.bit_length() - 1; mm ^= b
                c = len(coverers[v])
                if 0 < c < best_n:
                    best_n, best_v = c, v
            if best_v < 0:
                continue
            found = None
            for x in coverers[best_v]:
                R = M & ~CBM[x]
                if R == 0:
                    found = (cand[x], None); break
                # second ball: vertex of R with fewest coverers
                mm2 = R; v2 = -1; n2 = 10 ** 9
                while mm2:
                    b = mm2 & -mm; v = b.bit_length() - 1; mm2 ^= b
                    c = len(coverers[v])
                    if 0 < c < n2:
                        n2, v2 = c, v
                if v2 < 0:
                    continue
                for y in coverers[v2]:
                    if y == x:
                        continue
                    if R & ~CBM[y] == 0:
                        found = (cand[x], cand[y]); break
                if found:
                    break
            if found:
                hits.append(("swap32", (i, j, k), found))
print("多重重数直方图 (重数:顶点数) =", dict(sorted(hist.items())))
print("单重顶点数 =", sum(pc(S[w]) for w in range(120)),
      "| D2 组数 =", len(D2), "顶点 =", sum(pc(x) for x in D2.values()),
      "| D3 组数 =", len(D3), "顶点 =", sum(pc(x) for x in D3.values()))
print("三元组总数 =", tot, "| P1 剪掉(|M|>22) =", pruned, "| 进入精确检验 =", survivors)
print("|M(D)| 分布(0..22 各档计数, 仅列非零) =", {k: v for k, v in sorted(size_hist.items()) if k <= 22})
print("|M(D)| 最大 =", max(size_hist), "| 中位档 ≈", sorted(size_hist.elements())[len(size_hist.elements()) // 2] if size_hist else None)
print(f"用时 = {time.time()-t0:.1f}s")
if hits:
    kind, D, sol = hits[0]
    C2 = [words[t] for t in range(120) if t not in D]
    if sol:
        if sol[0] is not None: C2.append(sol[0])
        if sol[1] is not None: C2.append(sol[1])
    cov = 0
    for w in C2: cov |= bmask(w)
    ok = (cov == FULL) and len(C2) == len(set(C2)) and len(C2) <= 119
    print("★★ 命中:", kind, "D=", D, "sol=", sol, "| 码字数=", len(C2), "| 验证=", ok)
    if ok:
        open("code119_candidate.txt", "w").write(" ".join(format(x, '010b') for x in sorted(C2)))
        print(">>> 写出 code119_candidate.txt ⟹ K(10,1) <= 119")
else:
    print("→ (3,2) 邻域穷举完毕：无 119-码（相对该 120-记录码）")
json.dump({"tot": tot, "pruned": pruned, "survivors": survivors, "hist": {str(k): v for k, v in hist.items()},
           "size_hist": {str(k): v for k, v in sorted(size_hist.items())}, "hits": len(hits)},
          open("sweep32_stats.json", "w"))
