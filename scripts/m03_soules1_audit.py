#!/usr/bin/env python3
"""M03 E-型审计：Soules-1（Theorem 9, map2017 (11) 式）在 Lambda_* 上的 x-存在性。
全有理算术（fractions.Fraction）。变体 A/B 由"定理自带单调性"判别。
"""
from fractions import Fraction as F
import itertools, random, sys

LAM = [F(1), F(12,25), F(12,25), F(-41,50), F(-41,50)]   # Lambda_*
N = 5

def dvals(x, variant):
    xs=[F(0)]+list(x)
    S2=sum(xs[j]**2 for j in range(1,N+1))
    out=[]
    for i in range(1,N+1):
        t1 = xs[i]**2 * LAM[0] / S2
        t2 = F(0)
        for k in range(i+1, N+1):
            num = (xs[i]*xs[k])**2 * LAM[N-k+2-1]
            pre = sum(xs[j]**2 for j in range(1,k))
            cur = sum(xs[j]**2 for j in range(1,k+1))
            t2 += (num/(pre*cur)) if variant=='A' else (num*pre/cur)
        pre_i = sum(xs[j]**2 for j in range(1,i))
        cur_i = sum(xs[j]**2 for j in range(1,i+1))
        t3 = (pre_i * LAM[N-i+2-1] / cur_i) if i>=2 else F(0)
        out.append(t1+t2+t3)
    return out

def mono(x, variant):
    d=dvals(x,variant)
    return all(d[i]<=d[i+1] for i in range(N-1)), d

print("=== 步骤1：判别解析式（用定理的单调性断言）===")
random.seed(7)
for v in ('A','B'):
    ok=0; tot=0
    for _ in range(300):
        r=sorted(F(random.randint(1,40), random.randint(1,20)) for _ in range(N))
        m,_=mono(r,v); tot+=1; ok+= (1 if m else 0)
    print(f"  变体 {v}: 单调性成立 {ok}/{tot}")

print("\n=== 步骤2：低复杂度有理族搜索（E5）。目标 d1>=0 ===")
denoms=[2,3,4,5,6,8,10,12,15,20,25,40,50]
rats=set()
for q in denoms:
    for p in range(1, 3*q+1):
        rats.add(F(p,q))
rats=sorted(rats)
best=(None,None)  # (d1, x)
found=[]
variant='A'
# 族1 (1,r,r,r,r)
for r in rats:
    x=(F(1),r,r,r,r); d=dvals(x,variant)
    if d[0]>=0: found.append(('fff',x,d))
# 族2 (1,r,r,s,s)
for r in rats:
    for s in rats:
        if s<r: continue
        x=(F(1),r,r,s,s); d=dvals(x,variant)
        if d[0]>=0: found.append(('ffss',x,d))
# 族3 (1,r,s,s,s)
for r in rats:
    for s in rats:
        if s<r: continue
        x=(F(1),r,s,s,s); d=dvals(x,variant)
        if d[0]>=0: found.append(('fsss',x,d))
print("  族1/2/3 命中数:", len(found))
for tag,x,d in found[:8]:
    print("   HIT",tag,"x=",[str(v) for v in x],"d=",[str(v) for v in d])
if not found:
    # 记录最接近的（max d1）与符号区间（E6）
    mx=None
    for r in rats:
        x=(F(1),r,r,r,r); d=dvals(x,variant)[0]
        if mx is None or d>mx[0]: mx=(d,x)
        for s in rats:
            if s<r: continue
            for xx in ((F(1),r,r,s,s),(F(1),r,s,s,s)):
                dd=dvals(xx,variant)[0]
                if dd>mx[0]: mx=(dd,xx)
    print("  ✗ 未命中。最优 (max d1) =", str(mx[0]), "at x =", [str(v) for v in mx[1]])
    print("    最优点的 d 向量 =", [str(v) for v in dvals(mx[1],variant)])
