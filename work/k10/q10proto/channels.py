#!/usr/bin/env python3
"""① 验证 Q = Q_in + Q_out 恒等 ② (Q_in,Q_out) 类型普查 ③ 验证 Q=0 时的中点引理"""
import itertools, random
from collections import Counter
def setup(n):
    N=1<<n; L1=[[x^(1<<i) for i in range(n)]+[x] for x in range(N)]
    B1=[0]*N
    for x in range(N):
        m=0
        for y in L1[x]: m|=1<<y
        B1[x]=m
    return N,L1,B1,(1<<N)-1
def analyze(n,C,L1,B1,N,full):
    Cs=set(C); cm=0
    for c in C: cm|=1<<c
    b=[bin(B1[x]&cm).count('1') for x in range(N)]
    if any(v==0 for v in b): return None
    Q=sum((v-1)*(v-2)//2 for v in b)
    Qin=sum((b[c]-1)*(b[c]-2)//2 for c in C)
    Qout=sum((b[x]-1)*(b[x]-2)//2 for x in range(N) if x not in Cs)
    ident = (Qin+Qout==Q)
    # 中点引理检验（仅对 Q=0 的码）
    midok=None
    if Q==0:
        midok=True
        for a,c2 in itertools.combinations(sorted(C),2):
            if bin(a^c2).count('1')==2:
                for m in (a ^ (a^c2) & ~(a^c2) if False else None,) if False else ():
                    pass
                # 两个中点: a 与 c2 的公共邻点中非码字者
                common=[y for y in range(N) if (bin(y^a).count('1')<=1 and bin(y^c2).count('1')<=1)]
                for m in common:
                    if m in Cs: midok=False
                    if b[m]!=2: midok=False
                    # 除 a,c2 外无其他码字距 m 为 1
                    if sum(1 for o in C if o!=a and o!=c2 and bin(o^m).count('1')<=1)>0: midok=False
    return Q,Qin,Qout,ident,midok
def enum_codes(n,M):
    N,L1,B1,full=setup(n); out=[]
    for C in itertools.combinations(range(N),M):
        cov=0
        for c in C: cov|=B1[c]
        if cov==full: out.append(list(C))
    return out
def search_codes(n,M,tries=250):
    N,L1,B1,full=setup(n); out=set()
    for t in range(tries):
        C=set(random.sample(range(N),M)); cnt=[0]*N
        for c in C:
            for y in L1[c]: cnt[y]+=1
        for st in range(2500):
            zeros=[x for x in range(N) if cnt[x]==0]
            if not zeros: break
            x=random.choice(zeros); w=random.choice(L1[x])
            if w in C: continue
            for y in L1[w]: cnt[y]+=1
            C.add(w)
            rem=[c for c in C if c!=w and all(cnt[y]>=2 for y in L1[c])]
            c=random.choice(rem) if rem else random.choice([c for c in C if c!=w])
            for y in L1[c]: cnt[y]-=1
            C.discard(c)
        if all(cnt[x]>0 for x in range(N)): out.add(frozenset(C))
    return [list(s) for s in out]
random.seed(2027)
for n,M,how,K in ((4,4,"enum",True),(4,5,"enum",False),(5,7,"enum",True),(5,8,"search",False),(6,12,"search",True)):
    N,L1,B1,full=setup(n)
    cs=enum_codes(n,M) if how=="enum" else search_codes(n,M)
    rows=[r for r in (analyze(n,C,L1,B1,N,full) for C in cs) if r]
    if not rows: print(f"[n={n} M={M}] 无"); continue
    tag=f"n={n} M={M}"+(" (=K ✓)" if K else " (>K)")
    ident=all(r[3] for r in rows)
    types=Counter((r[1],r[2]) for r in rows)
    qs=sorted({r[0] for r in rows})
    print(f"[{tag}] 码 {len(rows)}")
    print(f"   恒等 Q=Qin+Qout: {'全部成立 ✓✓' if ident else '失败 ✗'}")
    print(f"   Q 取值 {qs[:6]}")
    print(f"   (Qin,Qout) 类型: {dict(list(types.items())[:6])}")
    zero=[r for r in rows if r[0]==0]
    if zero:
        print(f"   Q=0 的码 {len(zero)} 个；中点引理全部成立? {'是 ✓✓' if all(r[4] for r in zero) else '否 ✗'}")
    print()
