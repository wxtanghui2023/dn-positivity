#!/usr/bin/env python3
"""
d=4 packing 结构 census：找出所有"紧情形" α₂(U_D)=4（即不存在 5-packing），并刻画其结构。
  说明：d=4 已知 α₂≥4 全量成立（先前 pack_cert 穷举 + 精确 K4 判定）⟹ 本脚本补上"紧族"的结构画像。
  估算: 8,214,570 × (U_of 3µs + 贪心 5-packing ~10µs + 罕见精确) ≈ 2–5 min；内存 <300 MB
  判据: 贪心能建 5-packing ⟹ α₂≥5；贪心失败 ⟹ 精确 5-clique decision；仍无 ⟹ α₂=4（紧）
输出: gamma_d4_tight.json（紧族统计 + 样例）
"""
import itertools, json, sys, time
from collections import Counter, defaultdict
sys.argv = ['x', '5', 'none']
exec(open('/home/node/.openclaw/workspace/dn-project/work/k10/exact_pack.py').read().split('def main()')[0])
CODE = set(WORDS)
BALL = {}
for w in range(1024):
    m = 1 << w
    for b in range(10):
        m |= 1 << (w ^ (1 << b))
    BALL[w] = m
NEWW = [w for w in range(1024) if w not in CODE]
NEWB = [BALL[w] for w in NEWW]


def pack_greedy(pts, target):
    rem = pts
    got = []
    while len(got) < target and rem:
        v = (rem & -rem).bit_length() - 1
        got.append(v)
        nxt = 0
        t = rem
        while t:
            u = (t & -t).bit_length() - 1
            t &= t - 1
            if (u ^ v).bit_count() >= 3:
                nxt |= 1 << u
        rem = nxt
    return got if len(got) >= target else None


def has_clique_exact(pts, target):
    n = len(pts)
    if n < target:
        return False
    adj = [0] * n
    for i in range(n):
        for j in range(i + 1, n):
            if (pts[i] ^ pts[j]).bit_count() >= 3:
                adj[i] |= 1 << j
                adj[j] |= 1 << i

    def rec(cand, need):
        if need == 0:
            return True
        if cand.bit_count() < need:
            return False
        t = cand
        while t:
            v = (t & -t).bit_length() - 1
            t &= t - 1
            if rec(cand & adj[v], need - 1):
                return True
            cand &= ~(1 << v)
            if cand.bit_count() < need:
                return False
        return False
    return rec((1 << n) - 1, target)


t0 = time.time()
tight = 0
stat = Counter()
sz_dist = Counter()
examples = []
ge5 = 0
n = 0
for D in itertools.combinations(range(120), 4):
    U = U_of(D)
    if U == 0:
        continue
    n += 1
    pts_all = [v for v in range(1024) if (U >> v) & 1]
    if pack_greedy(U, 5):
        ge5 += 1
        continue
    if has_clique_exact(pts_all, 5):
        ge5 += 1
        continue
    # 紧情形 α₂ = 4
    tight += 1
    u = len(pts_all)
    sz_dist[u] += 1
    best = 0; ach = None
    for idx in range(len(NEWW)):
        ov = (NEWB[idx] & U).bit_count()
        if ov > best:
            best, ach = ov, NEWW[idx]
    Pvec = tuple(sorted((Counter(min(owners[v]) for v in pts_all)[x] for x in D), reverse=True))
    delta = sum(len(owners[v]) - 1 for v in pts_all)
    stat[(u, best, u - 3 * best)] += 1
    if len(examples) < 40 and (u <= 26 or tight <= 8):
        examples.append({"D": list(D), "U": u, "M": best, "G": u - 3 * best,
                         "Pd": list(Pvec), "delta": delta, "w": ach})
    if n % 500000 == 0:
        print(f"  n={n:,} 紧={tight} {time.time()-t0:.0f}s", flush=True)

print(f"=== d=4 全量 {n} 例：α₂≥5 者 {ge5}，紧情形 α₂=4 者 {tight} ===")
print("紧族 |U_D| 分布:", dict(sorted(sz_dist.items())))
print("紧族 (|U|, M, Γ) 分布 top20:")
for k, v in Counter(stat).most_common(20):
    print(f"   (|U|={k[0]}, M={k[1]}, Γ={k[2]}): {v}")
print("样例:", examples[:8])
json.dump({"n": n, "ge5": ge5, "tight": tight, "sz_dist": dict(sz_dist),
           "stat": {str(k): v for k, v in stat.items()}, "examples": examples},
          open('/home/node/.openclaw/workspace/dn-project/work/k10/gamma_d4_tight.json', 'w'), indent=1)
print(f"用时 {time.time()-t0:.0f}s ⟹ gamma_d4_tight.json")
