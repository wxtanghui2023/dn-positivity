#!/usr/bin/env python3
"""核验唐先生 §5 的 ladder 论断：
 ① 传播引理 |C∩S2(m)| ≥ ⌈(n-2)/2⌉  ✓?
 ② ladder 论断 |C∩S2(m)∩S2(m')| ≥ n-2  ✗?
 ③ "覆盖 e_l 须由 u_l 或 v_l"  ✗?"""
import itertools, random
def setup(n):
    N=1<<n; L1=[[x^(1<<i) for i in range(n)]+[x] for x in range(N)]
    B1=[0]*N
    for x in range(N):
        m=0
        for y in L1[x]: m|=1<<y
        B1[x]=m
    return N,L1,B1,(1<<N)-1
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
random.seed(555)
import math
for n,M,how in ((4,4,"enum"),(5,8,"search")):
    N,L1,B1,full=setup(n)
    cs=enum_codes(n,M) if how=="enum" else search_codes(n,M)
    zero=[]
    for C in cs:
        Cs=set(C); cm=0
        for c in C: cm|=1<<c
        b=[bin(B1[x]&cm).count('1') for x in range(N)]
        if any(v==0 for v in b): continue
        if sum((v-1)*(v-2)//2 for v in b)==0: zero.append((C,Cs,b))
    bound=math.ceil((n-2)/2)
    ok1=True; lad=[]; ok3=True; cnt3=0
    for C,Cs,b in zero:
        for a,c2 in itertools.combinations(sorted(C),2):
            diff=[i for i in range(n) if (a^c2)>>i & 1]
            if len(diff)!=2: continue
            i,j=diff
            m=a^(1<<i); mm=a^(1<<j)   # 两中点
            assert m not in Cs and mm not in Cs
            S2m={z for z in C if bin(z^m).count('1')==2}
            S2mm={z for z in C if bin(z^mm).count('1')==2}
            if len(S2m)<bound: ok1=False
            shared=len(S2m & S2mm)
            lad.append((shared, n-2))
            # ③ 对每个 l∉{i,j}: u=e_i+e_l (以 a 为原点) 或 v=e_j+e_l 是否在 C
            for l in range(n):
                if l in (i,j): continue
                u=a^(1<<i)^(1<<l); v=a^(1<<j)^(1<<l)
                e_l=a^(1<<l)
                # e_l 的覆盖者是否只能是 u 或 v？
                covs=[z for z in C if bin(z^e_l).count('1')<=1]
                cnt3+=1
                if not (u in Cs or v in Cs):
                    # 记录反例：e_l 被覆盖却没占 u/v
                    ok3=False
    print(f"=== n={n} M={M}: Q=0 码 {len(zero)} 个（bound=⌈(n-2)/2⌉={bound}）===")
    print(f"  ① 传播引理 |C∩S2(m)| ≥ {bound}: {'全部成立 ✓✓' if ok1 else '存在反例 ✗'}")
    if lad:
        mn=min(x[0] for x in lad); mx=max(x[0] for x in lad)
        print(f"  ② |C∩S2(m)∩S2(m')| 实测范围 [{mn},{mx}]；唐先生断言 ≥ n-2 = {n-2} ⟹ {'成立 ✓' if mn>=n-2 else '**不成立 ✗**'}")
    print(f"  ③ 'e_l 必经 u_l 或 v_l': {'成立 ✓' if ok3 else '**不成立 ✗**（存在 e_l 被覆盖但 u_l,v_l 均不在 C）'}")
    print()
