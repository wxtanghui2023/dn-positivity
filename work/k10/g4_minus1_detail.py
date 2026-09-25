#!/usr/bin/env python3
"""Γ=-1（d=4）7 例的逐项分析：α₂、4-packing、锚映射、距离矩阵、逃逸检查。"""
import json, sys
sys.argv = ['x', '5', 'none']
exec(open('/home/node/.openclaw/workspace/dn-project/work/k10/exact_pack.py').read().split('def main()')[0])
CODE = set(WORDS)
BALL = {}
for w in range(1024):
    m = 1 << w
    for b in range(10):
        m |= 1 << (w ^ (1 << b))
    BALL[w] = m


def pack_exact(pts, target):
    n = len(pts)
    if n < target:
        return None
    adj = [0] * n
    for i in range(n):
        for j in range(i + 1, n):
            if (pts[i] ^ pts[j]).bit_count() >= 3:
                adj[i] |= 1 << j
                adj[j] |= 1 << i

    def rec(cand, need, ch):
        if need == 0:
            return ch
        if cand.bit_count() < need:
            return None
        t = cand
        while t:
            v = (t & -t).bit_length() - 1
            t &= t - 1
            r = rec(cand & adj[v], need - 1, ch + [v])
            if r:
                return r
            cand &= ~(1 << v)
            if cand.bit_count() < need:
                return None
        return None
    return rec((1 << n) - 1, target, [])


rows = []
for k in (0, 1):
    X = json.load(open(f'/home/node/.openclaw/workspace/dn-project/work/k10/gamma_d4_agg_{k}.json'))
    for r in X['argmin_rows']:
        if r['G'] == -1:
            rows.append(r)
print(f"## Γ=-1 共 {len(rows)} 例（片0: 4 | 片1: 3）\n")
res = []
for r in rows:
    D = r['D']
    Xw = [WORDS[i] for i in D]
    U = U_of(D)
    pts = [v for v in range(1024) if (U >> v) & 1]
    a = 0
    while pack_exact(pts, a + 1):
        a += 1
    Pi = pack_exact(pts, a)
    P = [pts[i] for i in Pi] if Pi else []
    Sx = {i: {v for v in pts if i in owners[v]} for i in D}
    best, ach = 0, None
    for w in range(1024):
        if w in CODE:
            continue
        ov = (BALL[w] & U).bit_count()
        if ov > best:
            best, ach = ov, w
    M4 = [[(p ^ x).bit_count() for x in Xw] for p in P]
    anch = [[i for i, x in enumerate(D) if (p ^ Xw[i]).bit_count() <= 1] for p in P]
    print(f"### D={D} |U|={r['U']} M={r['M']} Γ={r['G']} P↓={r['Pd']} Δ={r['delta']}")
    print(f"  α₂(U_D)={a}")
    print(f"  4-packing P={P}")
    print(f"  锚映射 p→(D 中的位置): {anch}")
    print(f"  |S(x_i)∩U_D|={[len(Sx[i]) for i in D]}")
    print(f"  pairwise overlap={[len(Sx[D[i]] & Sx[D[j]]) for i in range(4) for j in range(i + 1, 4)]}")
    print(f"  M witness w={ach}; m_x={[sum(1 for v in pts if ((BALL[ach] >> v) & 1) and (i in owners[v])) for i in D]}")
    print(f"  距离矩阵 d(p_i,x_j)={M4}\n")
    res.append({"D": D, "U": r['U'], "M": r['M'], "alpha2": a, "P": P, "anch": anch, "dist": M4})
json.dump(res, open('/home/node/.openclaw/workspace/dn-project/work/k10/gamma_d4_minus1_details.json', 'w'), indent=1)
print("已写 gamma_d4_minus1_details.json")
