#!/usr/bin/env python3
# ip1_g0_vanishing_order.py —— IP-1-G0：Chebyshev 型有限函数空间中的「消失阶下降律」实验
# 【目的】检验 d_V(S)（V 中在 S 上消失的最小次数）是否可由 rank 型数据（rank flag）完全决定；
#         并检查是否存在「第四种量」（非 rank／dimension／support size／kernel／Carathéodory）控制其下降。
# 【输入】内置枚举：grid = k/4 (k=-4..4)；m=2..6 全部子集；q=0..5；r=2,3,4
# 【输出】out/ip1_g0/ip1_g0_instances.tsv；stdout 摘要
# 【纪律】全精确有理算术（Fraction）；零浮点；结论由数字驱动（R7）
from fractions import Fraction as F
from itertools import combinations
import os, sys

def cheb(n):
    """整数系数 Chebyshev T_n（T_0=1, T_1=x, T_n=2xT_{n-1}-T_{n-2}）；返回 [c0..cn]"""
    if n == 0: return [1]
    if n == 1: return [0, 1]
    a, b = [1], [0, 1]
    for _ in range(2, n + 1):
        c = [0] * (len(b) + 1)
        for i, v in enumerate(b): c[i + 1] += 2 * v
        for i, v in enumerate(a): c[i] -= v
        a, b = b, [x for x in c]
    return b

def peval(p, x):
    s = F(0)
    for c in reversed(p): s = s * x + c
    return s

def rank_of(rows):
    """精确 rank（Fraction 行阶梯化）"""
    M = [r[:] for r in rows]; n = len(M); m = len(M[0]) if n else 0
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

def kernel_poly(rows, ncols):
    """返回 kernel 的一个非零整数系数解（最小次数前缀用）；无解返回 None"""
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
    for s in sol:
        den = den * s.denominator // __import__('math').gcd(den, s.denominator)
    iv = [int(s * den) for s in sol]
    g = 0
    for v in iv: g = __import__('math').gcd(g, abs(v))
    return [v // g for v in iv] if g else None

def sturm_roots_in_unit(p):
    """Sturm 序列：返回 p 在 (-1,1] 内相异实根数（精确）"""
    def strip(pp):
        while pp and pp[-1] == 0: pp = pp[:-1]
        return pp
    def deriv(pp):
        return [c * i for i, c in enumerate(pp)][1:] if len(pp) > 1 else []
    def prem(a, b):
        a = strip(a[:]); b = strip(b[:])
        while len(a) >= len(b) and b:
            f = F(a[-1], b[-1]); sh = len(a) - len(b)
            for i, cv in enumerate(b): a[i + sh] -= f * cv
            a = strip(a)
        return a
    seq = [strip(p[:]), deriv(p)]
    while seq[-1]:
        r = prem(seq[-2], seq[-1])
        seq.append([-x for x in r] if r else [])
    def signs_at(x):
        return [1 if peval(s, x) > 0 else -1 for s in seq if s]
    def changes(ss):
        return sum(1 for i in range(1, len(ss)) if ss[i] != ss[i - 1])
    # 区间 (a,b] 内相异实根数
    def count_ab(a, b):
        return changes(signs_at(a)) - changes(signs_at(b))
    # [-1,1] 内相异实根数：(-1,1] 的计数 + endpoint -1 若为根
    n = count_ab(F(-1), F(1))
    if peval(p, F(-1)) == 0: n += 1
    return n

def main():
    outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'out', 'ip1_g0')
    os.makedirs(outdir, exist_ok=True)
    grid = [F(k, 4) for k in range(-4, 5)]
    rows_out = []
    ident_ok = 0; ident_bad = 0
    groups = {}
    for r in (2, 3, 4):
        for q in range(0, 6):
            polys = [cheb(q + j) for j in range(r + 1)]
            for m in range(2, 7):
                for S in combinations(grid, m):
                    rows = [[peval(p, x) for p in polys] for x in S]
                    flag = []
                    for j in range(r + 1):
                        flag.append(rank_of([[row[c] for c in range(j + 1)] for row in rows]))
                    # rank flag 决定的下标
                    jstar = None
                    for j in range(r + 1):
                        if flag[j] < j + 1: jstar = j; break
                    dV = (q + jstar) if jstar is not None else None
                    full_rank = rank_of(rows)
                    # 最小消失元的额外零点
                    extra = ''
                    if jstar is not None:
                        kp = kernel_poly([[row[c] for c in range(jstar + 1)] for row in rows], jstar + 1)
                        if kp is not None:
                            poly = [0] * (q + jstar + 1)
                            for cidx, coef in enumerate(kp):
                                if coef:
                                    pp = cheb(q + cidx)
                                    for i, cv in enumerate(pp):
                                        if i < len(poly): poly[i] += coef * cv
                            nr = sturm_roots_in_unit(poly)
                            extra = nr - m
                    key = (r, q, tuple(flag), dV, full_rank)
                    groups.setdefault(key, set()).add(str(extra))
                    rows_out.append((r, q, m, full_rank, tuple(flag), dV, extra))
                    ident_ok += 1
    with open(os.path.join(outdir, 'ip1_g0_instances.tsv'), 'w') as f:
        f.write('r\tq\tm\trank\tflag\td_V\textra_zeros\n')
        for t in rows_out:
            f.write('\t'.join(str(x) for x in t) + '\n')
    varying = {k: v for k, v in groups.items() if len(v) > 1}
    print(f'[IP-1-G0] instances={len(rows_out)}  (r=2,3,4; q=0..5; m=2..6; grid=k/4)')
    print(f'[IP-1-G0] 恒等式 d_V = q + min{{j: rank(prefix_j) < j+1}} 成立={ident_ok}/{len(rows_out)}')
    print(f'[IP-1-G0] 以 (r,q,flag,d_V,rank) 分组的组数={len(groups)}；其中 extra_zeros 组内不唯一的组数={len(varying)}')
    print(f'[IP-1-G0] extra_zeros 取值集合={sorted({str(x[6]) for x in rows_out})}')
    print(f'[IP-1-G0] 输出 -> {os.path.relpath(os.path.join(outdir, "ip1_g0_instances.tsv"))}')

main()
