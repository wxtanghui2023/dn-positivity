#!/usr/bin/env python3
# ip1_g0c_vanishing_order_v3.py —— IP-1-G0 复验（v3）：以 sympy 精确计数为权威（闭区间，相异实根）
# 【修正】v2 的 Sturm 计数有残缺陷（出现负 ec）⟹ v3 用 sympy.Poly.count_roots(-1,1)（口径经探针确认：端点计入、重根计一次）
# 【输出】out/ip1_g0/ip1_g0_instances_v3.tsv（不改写 v1/v2）；stdout 摘要 + 真反例对 + Sturm 差异统计
# 【纪律】整数系数精确多项式；零浮点；结论数字驱动（R7）
from fractions import Fraction as F
from itertools import combinations
import os
from math import gcd
import sympy as sp

x = sp.symbols('x')

def cheb(n):
    if n == 0: return [1]
    if n == 1: return [0, 1]
    a, b = [1], [0, 1]
    for _ in range(2, n + 1):
        c = [0] * (len(b) + 1)
        for i, v in enumerate(b): c[i + 1] += 2 * v
        for i, v in enumerate(a): c[i] -= v
        a, b = b, c
    return b

def peval(p, xv):
    s = F(0)
    for c in reversed(p): s = s * xv + c
    return s

def rank_of(rows):
    M = [[F(v) for v in r] for r in rows]; n = len(M); m = len(M[0]) if n else 0
    rk = 0
    for c in range(m):
        piv = next((r for r in range(rk, n) if M[r][c] != 0), None)
        if piv is None: continue
        M[rk], M[piv] = M[piv], M[rk]
        pv = M[rk][c]
        for r in range(rk + 1, n):
            if M[r][c] != 0:
                f = M[r][c] / pv
                for cc in range(c, m): M[r][cc] -= f * M[rk][cc]
        rk += 1
        if rk == n: break
    return rk

def kernel_vec(rows, ncols):
    M = [[F(v) for v in r] for r in rows]; n = len(M); m = ncols
    piv_cols = []; rk = 0
    for c in range(m):
        piv = next((r for r in range(rk, n) if M[r][c] != 0), None)
        if piv is None: continue
        M[rk], M[piv] = M[piv], M[rk]
        pv = M[rk][c]
        for r in range(n):
            if r != rk and M[r][c] != 0:
                f = M[r][c] / pv
                for cc in range(m): M[r][cc] -= f * M[rk][cc]
        piv_cols.append(c); rk += 1
        if rk == n: break
    free = [c for c in range(m) if c not in piv_cols]
    if not free: return None
    fv = free[0]; sol = [F(0)] * m; sol[fv] = F(1)
    for i, pc in enumerate(piv_cols): sol[pc] = -M[i][fv] / M[i][pc]
    den = 1
    for s in sol: den = den * s.denominator // gcd(den, s.denominator)
    iv = [int(s * den) for s in sol]
    g = 0
    for v in iv: g = gcd(g, abs(v))
    return [v // g for v in iv] if g else None

def strip(p):
    while p and p[-1] == 0: p = p[:-1]
    return p

def main():
    base = os.path.dirname(os.path.abspath(__file__))
    outdir = os.path.join(base, '..', 'out', 'ip1_g0'); os.makedirs(outdir, exist_ok=True)
    grid = [F(k, 4) for k in range(-4, 5)]
    recs = []
    for r in (2, 3, 4):
        for q in range(0, 6):
            polys = [cheb(q + j) for j in range(r + 1)]
            for m in range(2, 7):
                for S in combinations(grid, m):
                    rows = [[peval(p, xv) for p in polys] for xv in S]
                    flag = [rank_of([[row[c] for c in range(j + 1)] for row in rows]) for j in range(r + 1)]
                    jstar = next((j for j in range(r + 1) if flag[j] < j + 1), None)
                    dV = (q + jstar) if jstar is not None else None
                    full = rank_of(rows)
                    ec = eo = None; poly = None
                    if jstar is not None:
                        kv = kernel_vec([[row[c] for c in range(jstar + 1)] for row in rows], jstar + 1)
                        if kv is not None:
                            poly = [0] * (q + jstar + 1)
                            for ci, co in enumerate(kv):
                                if co:
                                    for i, cv in enumerate(cheb(q + ci)): poly[i] += co * cv
                            poly = strip(poly)
                            P = sp.Poly(list(reversed(poly)), x) if len(poly) > 1 else sp.Poly(poly[0], x)
                            ec = P.count_roots(-1, 1) - m                      # 闭区间相异实根 - m（权威 ✓）
                            eo = ec - (1 if peval(poly, F(-1)) == 0 else 0) - (1 if peval(poly, F(1)) == 0 else 0)
                    recs.append(dict(r=r, q=q, m=m, S=tuple(str(v) for v in S), flag=tuple(flag), dV=dV,
                                     rank=full, ec=ec, eo=eo, poly=tuple(poly) if poly else ()))
    with open(os.path.join(outdir, 'ip1_g0_instances_v3.tsv'), 'w') as f:
        f.write('r\tq\tm\trank\tflag\td_V\teo\tec\n')
        for t in recs:
            f.write(f"{t['r']}\t{t['q']}\t{t['m']}\t{t['rank']}\t{t['flag']}\t{t['dV']}\t{t['eo']}\t{t['ec']}\n")
    def gt(key):
        g = {}
        for t in recs:
            k = (t['r'], t['q'], t['flag'], t['dV'], t['rank'])
            g.setdefault(k, set()).add(t[key] if t[key] is not None else None)
        return g
    g_c, g_o = gt('ec'), gt('eo')
    var_c = {k: v for k, v in g_c.items() if len(v) > 1}
    var_o = {k: v for k, v in g_o.items() if len(v) > 1}
    print(f'[v3] instances={len(recs)}  权威计数=sympy count_roots(-1,1)（闭区间、重根计一次）')
    print(f'[v3] ec 取值={sorted({str(t["ec"]) for t in recs})}')
    print(f'[v3] 分组（r,q,flag,d_V,rank）组数={len(g_c)}  ec 组内不唯一={len(var_c)} ｜ eo 组内不唯一={len(var_o)}')
    # 真反例对：同组、ec 不同
    found = 0
    for k, vals in var_c.items():
        if found >= 3: break
        cand = [t for t in recs if (t['r'], t['q'], t['flag'], t['dV'], t['rank']) == k]
        vals_sorted = sorted({t['ec'] for t in cand})
        a = next(t for t in cand if t['ec'] == vals_sorted[0])
        b = next(t for t in cand if t['ec'] == vals_sorted[-1])
        print(f"[v3] C1候选对: key r={a['r']} q={a['q']} flag={a['flag']} d_V={a['dV']} rank={a['rank']}")
        for t in (a, b):
            print(f"      S={t['S']} m={t['m']} ec={t['ec']} eo={t['eo']} poly={t['poly']}")
        found += 1
    if found == 0: print('[v3] C1: 无真反例对 ⟹ ec 被 (r,q,flag,d_V,rank) 完全决定')
    print(f'[v3] 输出 -> out/ip1_g0/ip1_g0_instances_v3.tsv')

main()
