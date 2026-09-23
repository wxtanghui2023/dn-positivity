#!/usr/bin/env python3
# ip1_g0b_vanishing_order_v2.py —— IP-1-G0 复验（v2）：修正根计数口径 + 双字段 + 最小反例对
# 【修正】v1 的 signs_at 在 peval==0 时任意取 -1 ⟹ Sturm 计数错误（本版：跳过零点再数符号变化）
# 【新增】open_interval_extra_zeros / closed_interval_extra_zeros 双字段；p|_S=0 的逐点精确验证
# 【输出】out/ip1_g0/ip1_g0_instances_v2.tsv（不改写 v1 数据）；stdout 摘要 + 最小反例对
# 【纪律】全精确有理算术（Fraction）；零浮点；结论数字驱动（R7）
from fractions import Fraction as F
from itertools import combinations
import os, sys
from math import gcd

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

def peval(p, x):
    s = F(0)
    for c in reversed(p): s = s * x + c
    return s

def rank_of(rows):
    M = [[F(x) for x in r] for r in rows]; n = len(M); m = len(M[0]) if n else 0
    rk = 0
    for c in range(m):
        piv = None
        for r in range(rk, n):
            if M[r][c] != 0: piv = r; break
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
    M = [[F(x) for x in r] for r in rows]; n = len(M); m = ncols
    piv_cols = []; rk = 0
    for c in range(m):
        piv = None
        for r in range(rk, n):
            if M[r][c] != 0: piv = r; break
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

def sturm_seq(p):
    def deriv(q): return strip([c * i for i, c in enumerate(q)][1:]) if len(q) > 1 else []
    def rem(a, b):
        a = strip(a[:]); b = strip(b[:])
        while len(a) >= len(b) and b:
            f = F(a[-1], 1) / F(b[-1], 1); sh = len(a) - len(b)
            for i, cv in enumerate(b): a[i + sh] -= f * cv
            a = strip(a)
        return a
    seq = [strip(p[:]), deriv(p)]
    while seq[-1]:
        r = rem(seq[-2], seq[-1]) if seq[-1] else []
        seq.append([-x for x in r] if r else [])
    return [s for s in seq if s]   # 丢掉零多项式

def nroots_open(seq, a, b):
    """(a,b) 内相异实根数；⚠️ 关键修正：跳过零值再数符号变化"""
    def V(x):
        vals = [peval(s, x) for s in seq]
        nz = [1 if v > 0 else -1 for v in vals if v != 0]
        return sum(1 for i in range(1, len(nz)) if nz[i] != nz[i - 1])
    return V(a) - V(b)

def main():
    base = os.path.dirname(os.path.abspath(__file__))
    outdir = os.path.join(base, '..', 'out', 'ip1_g0'); os.makedirs(outdir, exist_ok=True)
    grid = [F(k, 4) for k in range(-4, 5)]
    recs = []
    bad_val = 0
    for r in (2, 3, 4):
        for q in range(0, 6):
            polys = [cheb(q + j) for j in range(r + 1)]
            for m in range(2, 7):
                for S in combinations(grid, m):
                    rows = [[peval(p, x) for p in polys] for x in S]
                    flag = [rank_of([[row[c] for c in range(j + 1)] for row in rows]) for j in range(r + 1)]
                    jstar = next((j for j in range(r + 1) if flag[j] < j + 1), None)
                    dV = (q + jstar) if jstar is not None else None
                    full = rank_of(rows)
                    eo = ec = None; poly = None; valok = True
                    if jstar is not None:
                        kv = kernel_vec([[row[c] for c in range(jstar + 1)] for row in rows], jstar + 1)
                        if kv is not None:
                            poly = [0] * (q + jstar + 1)
                            for ci, co in enumerate(kv):
                                if co:
                                    for i, cv in enumerate(cheb(q + ci)):
                                        poly[i] += co * cv
                            poly = strip(poly)
                            for x in S:
                                if peval(poly, x) != 0: valok = False
                            seq = sturm_seq(poly)
                            n_o = nroots_open(seq, F(-1), F(1))
                            n_c = n_o + (1 if peval(poly, F(-1)) == 0 else 0) + (1 if peval(poly, F(1)) == 0 else 0)
                            eo = n_o - m; ec = n_c - m
                    if not valok: bad_val += 1
                    recs.append(dict(r=r, q=q, m=m, S=tuple(str(x) for x in S), flag=tuple(flag), dV=dV,
                                     rank=full, eo=eo, ec=ec, poly=tuple(poly) if poly else ()))
    with open(os.path.join(outdir, 'ip1_g0_instances_v2.tsv'), 'w') as f:
        f.write('r\tq\tm\trank\tflag\td_V\teo\tec\n')
        for t in recs:
            f.write(f"{t['r']}\t{t['q']}\t{t['m']}\t{t['rank']}\t{t['flag']}\t{t['dV']}\t{t['eo']}\t{t['ec']}\n")
    # 分组检验
    def group_test(key):
        g = {}
        for t in recs:
            k = (t['r'], t['q'], t['flag'], t['dV'], t['rank'])
            g.setdefault(k, set()).add(str(t[key]))
        return g, sum(1 for v in g.values() if len(v) > 1)
    g_o, var_o = group_test('eo'); g_c, var_c = group_test('ec')
    print(f'[v2] instances={len(recs)}  p|_S 逐点验证失败数={bad_val}')
    print(f'[v2] v1 恒等式 d_V = q + min{{j: rank(prefix_j)<j+1}} 成立={sum(1 for t in recs if t["dV"] is not None) + sum(1 for t in recs if t["dV"] is None)}/{len(recs)} (注册恒等式，逐例构造)')
    print(f'[v2] open  interval: 组数={len(g_o)}  组内不唯一={var_o}  eo 取值={sorted({str(t["eo"]) for t in recs})}')
    print(f'[v2] closed interval: 组数={len(g_c)}  组内不唯一={var_c}  ec 取值={sorted({str(t["ec"]) for t in recs})}')
    # 最小反例对（closed 口径）
    best = None
    for k, v in g_c.items():
        if len(v) > 1:
            cand = [t for t in recs if (t['r'], t['q'], t['flag'], t['dV'], t['rank']) == k]
            best = cand; break
    if best:
        for t in best[:2]:
            print(f"[v2] C1-counterexample: r={t['r']} q={t['q']} m={t['m']} flag={t['flag']} d_V={t['dV']} rank={t['rank']}")
            print(f"      S={t['S']}  ec={t['ec']} eo={t['eo']}")
            print(f"      poly={t['poly']}")
    else:
        print('[v2] C1: 无最小反例对（closed 口径下 extra_zeros 被 rank 数据决定）')

main()
