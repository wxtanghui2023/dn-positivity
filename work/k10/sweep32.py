#!/usr/bin/env python3
"""
X1 / K(10,1): directed (3,2) neighbourhood sweep with singleton-owner + bitset gap pruning.

Record code C (120 words, Kamenetsky, verified).  For D = {i,j,k} subset of C:
   M(D) = { v : owners(v) subset of D }        # vertices that become uncovered
   pass-1 prune:  |M(D)| > 22  => dead          # two radius-1 balls cover at most 2*11 = 22
   pass-2 test :  exists x,y (x,y not in C\D) with M(D) subset of B(x) u B(y)
                  => 119-cover  (C \ D) u {x,y}
Precomputation: M(D) = S(i)|S(j)|S(k) | D2(ij)|D2(ik)|D2(jk) | D3(ijk)
  S(w)      : vertices with multiplicity 1 and owner w
  D2(a,b)   : vertices with owner set exactly {a,b}
  D3(a,b,c) : vertices with owner set exactly {a,b,c}
(vertices with multiplicity >= 4 can never be uncovered by deleting 3 words)
Outputs: multiplicity histogram, prune statistics, rigidity certificate data.
"""
import time, json
from collections import defaultdict, Counter

n = 10; N = 1 << n; FULL = (1 << N) - 1
words = [int(s, 2) for s in open("kamenetsky120.txt").read().split()]
idx = {w: i for i, w in enumerate(words)}


def ball(w):
    return [w] + [w ^ (1 << i) for i in range(n)]


def bmask(w):
    m = 0
    for v in ball(w):
        m |= 1 << v
    return m


BM = [bmask(w) for w in words]
owners = [[] for _ in range(N)]
for i, w in enumerate(words):
    for v in ball(w):
        owners[v].append(i)
mult = [len(owners[v]) for v in range(N)]
hist = Counter(mult)
print("多重重数直方图 (重数: 顶点数) =", dict(sorted(hist.items())))
print("合计 =", sum(hist.values()))

S = [0] * 120
D2 = defaultdict(int)
D3 = defaultdict(int)
for v in range(N):
    o = owners[v]
    m = 1 << v
    if len(o) == 1:
        S[o[0]] |= m
    elif len(o) == 2:
        D2[(o[0], o[1])] |= m
    elif len(o) == 3:
        D3[(o[0], o[1], o[2])] |= m
print("单重顶点总数 =", sum(bin(S[w]).count("1") for w in range(120)))
print("D2 组数 =", len(D2), " 覆盖顶点 =", sum(bin(x).count("1") for x in D2.values()))
print("D3 组数 =", len(D3), " 覆盖顶点 =", sum(bin(x).count("1") for x in D3.values()))

cand = [w for w in range(N) if w not in idx]
CBM = [bmask(w) for w in cand]
print("候选补字数 =", len(cand))

t0 = time.time()
tot = 0; pruned = 0; survivors = 0
hits = []
popcount = int.bit_count if hasattr(int, "bit_count") else (lambda x: bin(x).count("1"))

for i in range(120):
    for j in range(i + 1, 120):
        D2ij = D2.get((i, j), 0)
        for k in range(j + 1, 120):
            tot += 1
            M = S[i] | S[j] | S[k] | D2ij | D2.get((i, k), 0) | D2.get((j, k), 0) | D3.get((i, j, k), 0)
            sz = popcount(M)
            if sz > 22:
                pruned += 1
                continue
            survivors += 1
            if sz == 0:
                hits.append(("del3", (i, j, k), None)); continue
            # exact two-ball test
            best = []
            for ci, cm in enumerate(CBM):
                r = popcount(M & cm)
                if r:
                    best.append((r, ci))
            best.sort(reverse=True)
            found = None
            for r1, ci in best:
                rest = M & ~CBM[ci]
                if rest == 0:
                    found = (cand[ci], None); break
                for cj, cm2 in enumerate(CBM):
                    if cj == ci:
                        continue
                    if rest & ~cm2 == 0:
                        found = (cand[ci], cand[cj]); break
                if found:
                    break
            if found:
                hits.append(("swap32", (i, j, k), found))
print(f"(3,2) 扫描完成: 三元组总数={tot}  被 |M|>22 剪掉={pruned}  进入精确检验={survivors}  用时={time.time()-t0:.1f}s")
if hits:
    kind, D, sol = hits[0]
    C2 = [words[t] for t in range(120) if t not in D]
    if sol:
        if sol[0] is not None: C2.append(sol[0])
        if sol[1] is not None: C2.append(sol[1])
    cov = 0
    for w in C2:
        cov |= bmask(w)
    ok = (cov == FULL) and (len(C2) == len(set(C2))) and len(C2) <= 119
    print("★★ 命中:", kind, "D=", D, "sol=", sol, "| 码字数=", len(C2), "| 验证=", ok)
    if ok:
        open("code119_candidate.txt", "w").write(" ".join(format(x, '010b') for x in sorted(C2)))
        print(">>> 写出 code119_candidate.txt ⟹ K(10,1) <= 119")
else:
    print("→ (3,2) 邻域穷举完毕：无 119-码（相对该 120-记录码）")
json.dump({"tot": tot, "pruned": pruned, "survivors": survivors,
           "hist": {str(k): v for k, v in hist.items()},
           "hits": len(hits)}, open("sweep32_stats.json", "w"))
