#!/usr/bin/env python3
"""X1 (3,2) sweep -- final version: prune + indexed two-ball test + progress logging."""
import time, json
from collections import Counter, defaultdict

n = 10; N = 1 << n
words = [int(s, 2) for s in open("kamenetsky120.txt").read().split()]

def ball(w): return [w] + [w ^ (1 << i) for i in range(n)]
def bmask(w):
    m = 0
    for v in ball(w): m |= 1 << v
    return m

owners = [[] for _ in range(N)]
for i, w in enumerate(words):
    for v in ball(w): owners[v].append(i)

S = [0] * 120; D2 = defaultdict(int); D3 = defaultdict(int)
for v in range(N):
    o = owners[v]; m = 1 << v
    if len(o) == 1: S[o[0]] |= m
    elif len(o) == 2: D2[(o[0], o[1])] |= m
    elif len(o) == 3: D3[(o[0], o[1], o[2])] |= m

P = [[0] * 120 for _ in range(120)]
for (a, b), m in D2.items(): P[a][b] = m; P[b][a] = m

ws = set(words)
cand = [w for w in range(N) if w not in ws]
CBM = [bmask(w) for w in cand]
coverers = [[] for _ in range(N)]
for ci, w in enumerate(cand):
    for v in ball(w): coverers[v].append(ci)

pc = int.bit_count
t0 = time.time()
tot = pruned = surv = 0
sh = Counter(); hits = []; checked = 0

for i in range(120):
    Si = S[i]; Pi = P[i]
    for j in range(i + 1, 120):
        Sj = S[j]; Pij = Pi[j]
        for k in range(j + 1, 120):
            tot += 1
            M = Si | Sj | S[k] | Pij | Pi[k] | P[j][k]
            d3 = D3.get((i, j, k), 0)
            if d3: M |= d3
            sz = pc(M); sh[sz] += 1
            if sz > 22:
                pruned += 1; continue
            surv += 1
            if sz == 0:
                hits.append(("del3", (i, j, k), None)); continue
            # ---- indexed two-ball test ----
            mv = M; bv = -1; bn = 10 ** 9
            while mv:
                b = mv & -mv; v = b.bit_length() - 1; mv ^= b
                c = len(coverers[v])
                if 0 < c < bn: bn, bv = c, v
            if bv < 0: continue
            found = None
            for x in coverers[bv]:
                R = M & ~CBM[x]
                if R == 0: found = (cand[x], None); break
                m2 = R; v2 = -1; n2 = 10 ** 9
                while m2:
                    b = m2 & -m2; v = b.bit_length() - 1; m2 ^= b
                    c = len(coverers[v])
                    if 0 < c < n2: n2, v2 = c, v
                if v2 < 0: continue
                for y in coverers[v2]:
                    if y == x: continue
                    if R & ~CBM[y] == 0: found = (cand[x], cand[y]); break
                if found: break
            checked += 1
            if found: hits.append(("swap32", (i, j, k), found))
            if checked % 20000 == 0:
                print(f"  精确检验 {checked}/{surv}  hits={len(hits)}  t={time.time()-t0:.1f}s", flush=True)

print(f"三元组总数={tot}  剪掉={pruned}  精确检验={surv}")
print("|M| 分布(≤22):", {k: v for k, v in sorted(sh.items()) if k <= 22}, " 最大=", max(sh))
print(f"总用时={time.time()-t0:.1f}s  hits={len(hits)}")
if hits:
    kind, D, sol = hits[0]
    C2 = [words[t] for t in range(120) if t not in D]
    if sol:
        if sol[0] is not None: C2.append(sol[0])
        if sol[1] is not None: C2.append(sol[1])
    cov = 0
    for w in C2: cov |= bmask(w)
    ok = (cov == (1 << N) - 1) and len(C2) == len(set(C2)) and len(C2) <= 119
    print("★★ 命中:", kind, "D=", D, "| 字数=", len(C2), "| 验证=", ok)
    if ok:
        open("code119_candidate.txt", "w").write(" ".join(format(x, '010b') for x in sorted(C2)))
        print(">>> 写出 code119_candidate.txt ⟹ K(10,1) <= 119")
else:
    print("→ (3,2) 邻域穷举完毕：无 119-码（相对该 120-记录码）")
json.dump({"tot": tot, "pruned": pruned, "survivors": surv, "hits": len(hits),
           "size_hist": {str(k): v for k, v in sorted(sh.items())}},
          open("sweep32_stats.json", "w"))
