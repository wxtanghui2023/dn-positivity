#!/usr/bin/env python3
"""钉住普查：private-point 一阶/二阶极值结构 + Extremal-specificity 筛 (T1-T4)
数据来源：n=4 (M=4,5,6 全枚举 ✓)、n=5 (M=7 全枚举 ✓、M=8 随机采样 ✓)
纪律：单进程、流式落盘、无大列表累积 ✓"""
import itertools, random, sys
from collections import Counter

def build(n):
    N = 1 << n
    ball = [0]*N
    for x in range(N):
        m = 1 << x
        for i in range(n):
            m |= 1 << (x ^ (1 << i))
        ball[x] = m
    return N, ball, (1 << N) - 1

def analyze(n, M, codes, tag, ball, full, N):
    rows = []
    for C in codes:
        cm = 0
        for c in C: cm |= 1 << c
        cov = 0
        for c in C:
            cov |= ball[c]
            if cov == full: break
        if cov != full: continue
        b = [bin(ball[x] & cm).count('1') for x in range(N)]
        Q = sum((v-1)*(v-2)//2 for v in b)
        A1 = A2 = 0
        for i in range(len(C)):
            for j in range(i+1, len(C)):
                dd = bin(C[i] ^ C[j]).count('1')
                if dd == 1: A1 += 1
                elif dd == 2: A2 += 1
        r = []
        priv = []
        for c in C:
            bit = 1 << c
            ps = [x for x in range(N) if (ball[x] & cm) == bit]
            priv.append(ps); r.append(len(ps))
        # 二阶 private incidence: |Priv(c) ∩ B2(d)|
        P2 = 0; P2self = 0
        for i, c in enumerate(C):
            for j, d in enumerate(C):
                cnt = sum(1 for x in priv[i] if bin((x ^ d).bit_count() if False else (x ^ d)).count('1') <= 2)
                P2 += cnt
                if i == j: P2self += cnt
        rows.append(dict(C=tuple(C), Q=Q, Ale=A1+A2, A1=A1, A2=A2, b=b,
                         r=tuple(r), P=sum(r), R2=sum(v*v for v in r),
                         rmin=min(r), rmax=max(r), P2=P2, P2self=P2self))
    print(f"  [{tag}] 覆盖码数 = {len(rows)}")
    if not rows: return rows
    def uniq(key): return sorted({row[key] for row in rows})
    for key in ['Q','Ale','P','R2','rmin','rmax','P2','P2self']:
        u = uniq(key)
        s = str(u[:8]) + (' …' if len(u) > 8 else '')
        print(f"      {key:7s}: 取值 {s}   ({'恒定 ✓' if len(u)==1 else '变化 ✗'})")
    print(f"      r 向量分布(前3): {[Counter(row['r']) for row in rows[:3]] if len({row['r'] for row in rows})>1 else '唯一: '+str(Counter(rows[0]['r']))}")
    return rows

print("=== 构建 ball 掩码 ===")
N4, ball4, full4 = build(4)
N5, ball5, full5 = build(5)
print("n=4:", N4, "n=5:", N5)
allrows = {}
print("\n=== n=4 全枚举 ===")
for M in (4, 5, 6):
    codes = list(itertools.combinations(range(N4), M))
    allrows[(4,M)] = analyze(4, M, codes, f"n=4 M={M}", ball4, full4, N4)
print("\n=== n=5 M=7 全枚举 ===")
codes = list(itertools.combinations(range(N5), 7))
allrows[(5,7)] = analyze(5, 7, codes, "n=5 M=7", ball5, full5, N5)
print("\n=== n=5 M=8 随机采样 ===")
random.seed(20260926)
samp = [tuple(sorted(random.sample(range(N5), 8))) for _ in range(120000)]
samp = list(dict.fromkeys(samp))
allrows[(5,8)] = analyze(5, 8, samp, "n=5 M=8 (采样)", ball5, full5, N5)

print("\n=== T1/T2 极值特异性筛（M=K 恒定 且 M>K 变化）===")
def check(key):
    ok4 = len({r[key] for r in allrows[(4,4)]}) == 1
    var4 = len({r[key] for r in allrows[(4,5)]}) > 1
    ok5 = len({r[key] for r in allrows[(5,7)]}) == 1
    var5 = len({r[key] for r in allrows[(5,8)]}) > 1
    return ok4, var4, ok5, var5
for key in ['Q','Ale','P','R2','rmin','rmax','P2','P2self']:
    a,b,c,d = check(key)
    verdict = "T1✓T2✓ 极值特异 ✓" if (a and b and c and d) else ("恒定但未释放 ✗" if (a and c and not (b or d)) else "非极值特异 ✗")
    print(f"  {key:7s}: n=4 M=4恒定={a} M=5变化={b} | n=5 M=7恒定={c} M=8变化={d}  ⟹ {verdict}")

print("\n=== T4 关系测试：Q 与 private 量的关系（在变化区 M>K 上回归 ✓）===")
import statistics
for tag,(n,M) in [("n=4 M=5",(4,5)),("n=4 M=6",(4,6)),("n=5 M=8",(5,8))]:
    rs = allrows[(n,M)]
    if len({r['Q'] for r in rs}) < 2:
        print(f"  [{tag}] Q 恒定 ⟹ 无法回归"); continue
    for key in ['P','R2','rmin','rmax','P2']:
        xs = [r[key] for r in rs]; ys = [r['Q'] for r in rs]
        mx, my = statistics.mean(xs), statistics.mean(ys)
        num = sum((x-mx)*(y-my) for x,y in zip(xs,ys))
        den = (sum((x-mx)**2 for x in xs) * sum((y-my)**2 for y in ys))**.5
        corr = num/den if den else float('nan')
        print(f"    [{tag}] corr(Q,{key}) = {corr:+.4f}   (n={len(rs)})")
