#!/usr/bin/env python3
"""
d=3 全量 Γ-census（照唐先生 20:36 的五项锁定）
  估算: 280,840 例 × (U_of + 664 新字球交) ≈ 0.8 ms/例 ≈ 4 min；内存目标 <200 MB
  五项输出:
    ① 精确 Γ 分布
    ② 全部 argmin 构型（含达到 M 的 w 的贡献谱 (m_1..m_d)）
    ③ P-vector 与排序 partition P↓
    ④ Δ(D) 与 mult_excess(D)（此处二者恒等，见注释）对 argmin 的验证
    ⑤ Γ_min 对应的 (|U|,M) 唯一性；以及 P↓ → max M 的关系表
  全部逐例记录流式写入 gamma_d3_full.jsonl（不累积在内存）
"""
import itertools, json, sys
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
NEWW = [w for w in range(1024) if w not in CODE]        # 664 个新字
NEWB = [BALL[w] for w in NEWW]

# 预计算每个点的 min owner 与 |S(v)|（点级）
MINOWN = [min(owners[v]) for v in range(1024)]
SZ = [len(owners[v]) for v in range(1024)]
PTS = list(range(1024))

GammaDist = Counter()
Mdist = Counter()
PdM = defaultdict(Counter)          # P↓ -> Counter(M)
argmin = None
argmin_rows = []
rows_written = 0

fh = open('/home/node/.openclaw/workspace/dn-project/work/k10/gamma_d3_full.jsonl', 'w')

for D in itertools.combinations(range(120), 3):
    U = U_of(D)
    if U == 0:
        continue
    pts = [v for v in PTS if (U >> v) & 1]
    u = len(pts)
    # M(D) + 全部达到者
    best, ach = 0, []
    for idx, w in enumerate(NEWW):
        ov = (NEWB[idx] & U).bit_count()
        if ov > best:
            best, ach = ov, [w]
        elif ov == best:
            ach.append(w)
    # P-vector（首个 owner 分层）与 Δ
    Pi = Counter(MINOWN[v] for v in pts)
    Pvec = tuple(Pi[x] for x in D)
    Pd = tuple(sorted(Pvec, reverse=True))
    delta = sum(SZ[v] - 1 for v in pts)          # = Σ_x a_x - |U|（恒等，见 docstring）
    g = u - 2 * best
    GammaDist[g] += 1
    Mdist[best] += 1
    PdM[Pd][best] += 1
    fh.write(json.dumps({"D": list(D), "U": u, "M": best, "G": g, "P": list(Pvec),
                         "Pd": list(Pd), "delta": delta}, separators=(',', ':')) + "\n")
    rows_written += 1
    if argmin is None or g < argmin:
        argmin, argmin_rows = g, []
    if g == argmin:
        # 记录 argmin 构型（含 M 达到者的贡献谱）
        spec = []
        for w in ach[:12]:
            bw = BALL[w]
            m_x = [sum(1 for v in pts if ((bw >> v) & 1) and (x in owners[v])) for x in D]
            spec.append({"w": w, "m_x": m_x})
        argmin_rows.append({"D": list(D), "U": u, "M": best, "G": g, "P": list(Pvec),
                            "Pd": list(Pd), "delta": delta, "n_ach": len(ach), "spec": spec})
fh.close()

print(f"=== d=3 全量 ({rows_written} 例) ===")
print(f"① Γ 分布: {dict(sorted(GammaDist.items()))}")
print(f"   ⟹ Γ_min = {min(GammaDist)}")
print(f"② argmin 构型数 = {len(argmin_rows)}")
for r in argmin_rows[:10]:
    print(f"   D={r['D']} |U|={r['U']} M={r['M']} Γ={r['G']} P={r['P']} P↓={r['Pd']} "
          f"Δ={r['delta']} n_ach={r['n_ach']}")
    for s in r["spec"][:3]:
        print(f"        w={s['w']} m_x={s['m_x']}")
delta_all0 = all(r["delta"] == 0 for r in argmin_rows)
print(f"④ argmin 全部 Δ=0 ? {delta_all0}")
print(f"⑤ Γ_min 对应的 (|U|,M) 组合: {sorted({(r['U'], r['M']) for r in argmin_rows})}")
print(f"   M 分布（全体）: {dict(sorted(Mdist.items()))}")
print("③ P↓ → max M 关系表（前 20 个 P↓ 形态）:")
for pd, c in sorted(PdM.items(), key=lambda kv: -sum(kv[1].values()))[:20]:
    print(f"   P↓={pd}: 例数={sum(c.values())}  M 分布={dict(sorted(c.items()))}")
json.dump({"rows": rows_written, "GammaDist": dict(GammaDist), "Mdist": dict(Mdist),
           "gamma_min": min(GammaDist), "argmin_rows": argmin_rows,
           "Pd_to_M": {str(k): dict(v) for k, v in PdM.items()}},
          open('/home/node/.openclaw/workspace/dn-project/work/k10/gamma_d3_summary.json', 'w'), indent=1)
print("已写 gamma_d3_full.jsonl + gamma_d3_summary.json")
