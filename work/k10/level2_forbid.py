#!/usr/bin/env python3
"""Level II 最小禁形 census：
   对紧型每个 C_i，记录 T_i（归一化坐标集）与 owner 集 O(a)=S(e_a)\\{x_i}；
   对保留的两个 q（q_j,q_k）算 A_j,A_k = T_i ∩ supp(·)（相对 x_i）；
   筛 |A_j∪A_k|>=3 → 输出禁形详情（含重量型与 owner 容量）。
"""
import random, sys, itertools
from collections import Counter
sys.argv = ['x', '5', 'none']
exec(open('/home/node/.openclaw/workspace/dn-project/work/k10/exact_pack.py').read().split('def main()')[0])


def S_idx(q):
    return set(i for i, w in enumerate(WORDS) if (w ^ q).bit_count() <= 1)


def supp_rel(z, xi):
    return {a for a in range(10) if ((z ^ xi) >> a) & 1}


random.seed(31337)
weight_hist = Counter()
viol = []
n_ci = 0
n_bad = 0
for _ in range(120):
    D = tuple(sorted(random.sample(range(120), 4)))
    Xw = [WORDS[i] for i in D]
    U = U_of(D)
    if U == 0:
        continue
    pts = [v for v in range(1024) if (U >> v) & 1]
    Cs = [[q for q in pts if (q ^ x).bit_count() <= 1] for x in Xw]
    for t in range(4):
        x = Xw[t]
        other_idx = [i for i in range(4) if i != t]
        for Q in itertools.product(*[Cs[i] for i in other_idx]):
            if min((Q[a] ^ Q[b]).bit_count() for a, b in itertools.combinations(range(3), 2)) < 3:
                continue
            rs = tuple(sorted((q ^ x).bit_count() for q in Q))
            if rs not in ((2, 3, 3), (3, 3, 3)):
                continue
            B1x = [x] + [x ^ (1 << j) for j in range(10)]
            F = [v for v in B1x if all((v ^ q).bit_count() >= 3 for q in Q)]
            if len(F) != 2:
                continue
            if not [v for v in F if v not in pts]:
                continue
            for ci in other_idx:
                xi = Xw[ci]
                Ci = Cs[ci]
                n_ci += 1
                T_i = {a for a in range(10) if (xi ^ (1 << a)) in Ci}
                O = {a: sorted(S_idx(xi ^ (1 << a)) - {ci}) for a in T_i}
                for k in [other_idx.index(ci)]:      # ★ 必须限定为本簇对应的 k
                    keep = [Q[j] for j in range(3) if j != k]
                    # 真实覆盖：e_a ∈ B₂(z) ⟺ d(xi^e_a, z) ≤ 2（不要用支撑公式，对 |supp|≥4 会越界）
                    Aj = {a for a in T_i if ((xi ^ (1 << a)) ^ keep[0]).bit_count() <= 2}
                    Ak = {a for a in T_i if ((xi ^ (1 << a)) ^ keep[1]).bit_count() <= 2}
                    if len(Aj | Ak) < 3:
                        continue
                    n_bad += 1
                    wj, wk = len(supp_rel(keep[0], xi)), len(supp_rel(keep[1], xi))
                    weight_hist[(wj, wk)] += 1
                    if len(viol) < 10:
                        viol.append({
                            "D": list(D), "ci": ci, "Ti": sorted(T_i),
                            "w": (wj, wk), "Aj": sorted(Aj), "Ak": sorted(Ak),
                            "AjAk": len(Aj & Ak), "union": sorted(Aj | Ak),
                            "owners": {a: O[a] for a in sorted(Aj | Ak)},
                        })
print(f"检查的簇数 = {n_ci};  |A_j∪A_k| >= 3 的禁形候选数 = {n_bad}")
print(f"重量型分布 (|supp(q_j)|,|supp(q_k)|) 相对 x_i = {dict(sorted(weight_hist.items()))}")
print(f"\n禁形样例（含 owner 容量）:")
for r in viol:
    print(f"  D={r['D']} 簇={r['ci']} T_i={r['Ti']}")
    print(f"    重量={r['w']}  A_j={r['Aj']}  A_k={r['Ak']}  交={r['AjAk']}  union={r['union']}")
    print(f"    owners(除 x_i 外): {r['owners']}")
