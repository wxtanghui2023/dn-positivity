#!/usr/bin/env python3
"""
d=4 全量 Γ-census（2 分片 · 断点续跑 · 低内存）
  估算: 8,214,570 例 × ~0.7 ms ÷ 2 片 ≈ 45 min；内存 <300 MB（只存聚合 + argmin）
  用法: python3 gamma_d4_full.py <mod_k> <mod_n>
输出:
  gamma_d4_agg_<k>.json     逐片聚合（Γ 分布、M 分布、P↓→M、argmin 列表）
  gamma_d4_state_<k>.json   断点（已完成的 i1 值）
"""
import itertools, json, os, sys, time
from collections import Counter, defaultdict

K = int(sys.argv[1]); NMOD = int(sys.argv[2])
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
MINOWN = [min(owners[v]) for v in range(1024)]
SZ = [len(owners[v]) for v in range(1024)]

STATE = f'/home/node/.openclaw/workspace/dn-project/work/k10/gamma_d4_state_{K}.json'
OUT = f'/home/node/.openclaw/workspace/dn-project/work/k10/gamma_d4_agg_{K}.json'
done = set(json.load(open(STATE))) if os.path.exists(STATE) else set()
if done:
    print(f"续跑：已完成 i1 {sorted(done)[:5]}... 共 {len(done)}", flush=True)

GammaDist = Counter(); Mdist = Counter(); PdM = defaultdict(Counter)
gamma_min = None; argmin_rows = []
t0 = time.time(); n = 0
for i1 in range(120):
    if i1 % NMOD != K or i1 in done:
        continue
    for rest in itertools.combinations(range(i1 + 1, 120), 3):
        D = (i1,) + rest
        U = U_of(D)
        if U == 0:
            continue
        pts = [v for v in range(1024) if (U >> v) & 1]
        u = len(pts)
        best, ach = 0, []
        for idx in range(len(NEWW)):
            ov = (NEWB[idx] & U).bit_count()
            if ov > best:
                best, ach = ov, [NEWW[idx]]
            elif ov == best:
                ach.append(NEWW[idx])
        Pvec = tuple(sorted((Counter(MINOWN[v] for v in pts)[x] for x in D), reverse=True))
        delta = sum(SZ[v] - 1 for v in pts)
        g = u - 3 * best
        GammaDist[g] += 1; Mdist[best] += 1; PdM[Pvec][best] += 1
        n += 1
        if gamma_min is None or g < gamma_min:
            gamma_min, argmin_rows = g, []
        if g == gamma_min and len(argmin_rows) < 400:
            spec = []
            for w in ach[:6]:
                bw = BALL[w]
                spec.append({"w": w, "m_x": [sum(1 for v in pts if ((bw >> v) & 1) and (x in owners[v])) for x in D]})
            argmin_rows.append({"D": list(D), "U": u, "M": best, "G": g, "Pd": list(Pvec),
                                "delta": delta, "n_ach": len(ach), "spec": spec})
    done.add(i1); json.dump(sorted(done), open(STATE, 'w'))
    print(f"  i1={i1} n={n:,} Γ_min={gamma_min} {time.time()-t0:.0f}s", flush=True)

json.dump({"K": K, "n": n, "GammaDist": dict(GammaDist), "Mdist": dict(Mdist),
           "gamma_min": gamma_min, "argmin_rows": argmin_rows,
           "Pd_to_M": {str(k): dict(v) for k, v in PdM.items()}, "sec": round(time.time() - t0, 1)},
          open(OUT, 'w'), indent=1)
print(f"[片 {K}/{NMOD}] n={n:,} Γ_min={gamma_min} {time.time()-t0:.0f}s ⟹ {OUT}", flush=True)
