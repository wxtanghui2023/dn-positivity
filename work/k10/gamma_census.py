#!/usr/bin/env python3
"""
Γ-census（照唐先生 20:27 的第 17–20 条）：
  Γ(D) = |U_D| - (d-1)*M(D)                ← 联合不等式裕度
  M(D) = max_{w∉C120} |B(w) ∩ U_D|
  分解：
    P_i    = 首个 owner 为 x_i 的 U_D 点（按 D 的自然序）→ |U_D| = Σ|P_i|
    a_x    = |{v ∈ U_D : x ∈ S(v)}|          → Δ = Σ_x a_x - |U_D| = Σ_{v∈U_D}(|S(v)|-1)
  对 argmin Γ 的 D：打印完整结构 + 达到 M(D) 的 w 的贡献谱 (m_x(w))
输出：gamma_census.json（含全部逐例记录，便于后续极值分类）
"""
import itertools, json, random, sys

sys.argv = ['x', '5', 'none']
exec(open('/home/node/.openclaw/workspace/dn-project/work/k10/exact_pack.py').read().split('def main()')[0])
CODE = set(WORDS)
BALL = [0] * 1024
for w in range(1024):
    m = 1 << w
    for b in range(10):
        m |= 1 << (w ^ (1 << b))
    BALL[w] = m
NEWW = [w for w in range(1024) if w not in CODE]     # 664 个新字

random.seed(31)
rows = []
for d in (3, 4, 5):
    n = {3: 300, 4: 300, 5: 60}[d]
    for _ in range(n):
        D = tuple(sorted(random.sample(range(120), d)))
        U = U_of(D)
        if U == 0:
            continue
        sizes = [len(owners[v]) for v in range(1024) if (U >> v) & 1]
        # M(D) 与全部达到者
        best, achievers = 0, []
        for w in NEWW:
            ov = (BALL[w] & U).bit_count()
            if ov > best:
                best, achievers = ov, [w]
            elif ov == best:
                achievers.append(w)
        Pi = []
        for x in D:
            Pi.append(sum(1 for v in range(1024)
                          if (U >> v) & 1 and min(owners[v]) == x))
        ax = {x: sum(1 for v in range(1024) if (U >> v) & 1 and x in owners[v]) for x in D}
        delta = sum(ax.values()) - U.bit_count()
        gamma = U.bit_count() - (d - 1) * best
        rows.append({"d": d, "D": list(D), "U": U.bit_count(), "M": best,
                     "gamma": gamma, "Pi": Pi, "ax": [ax[x] for x in D], "delta": delta,
                     "mult_excess": sum(s - 1 for s in sizes),
                     "achievers": achievers[:8], "n_achievers": len(achievers)})

from collections import Counter
print("=== Γ(D) census ===", flush=True)
for d in (3, 4, 5):
    rs = [r for r in rows if r["d"] == d]
    gs = [r["gamma"] for r in rs]
    print(f"d={d} (n={len(rs)}): Γ ∈ [{min(gs)},{max(gs)}] 均{sum(gs)/len(gs):.2f} | "
          f"|U| 均{sum(r['U'] for r in rs)/len(rs):.1f} | M 分布{dict(sorted(Counter(r['M'] for r in rs).items()))}")
    mn = min(rs, key=lambda r: r["gamma"])
    print(f"   ★ argmin Γ={mn['gamma']}: |U|={mn['U']} M={mn['M']} D={mn['D']}")
    print(f"      Pi={mn['Pi']} ax={mn['ax']} delta={mn['delta']} mult_excess={mn['mult_excess']}")
    print(f"      achievers(M) n={mn['n_achievers']} 例={mn['achievers'][:4]}")
    # Γ=最小值 的全体
    same = [r for r in rs if r["gamma"] == mn["gamma"]]
    print(f"      Γ 取最小值的例数 = {len(same)}/{len(rs)}  (U 范围 {min(r['U'] for r in same)}-{max(r['U'] for r in same)}, "
          f"M 分布 {dict(sorted(Counter(r['M'] for r in same).items()))})", flush=True)
json.dump(rows, open('/home/node/.openclaw/workspace/dn-project/work/k10/gamma_census.json', 'w'), indent=1)
print("已写 gamma_census.json（逐例记录，供极值分类）")
