import itertools, random
from collections import Counter
from math import comb
def check(r,trials):
    bad=Counter(); tot=0
    for _ in range(trials):
        es=set(e for e in itertools.combinations(range(r),2) if random.random()<0.5)
        m=0; te=Counter()
        for (a,b,c) in itertools.combinations(range(r),3):
            if (a,b) in es and (a,c) in es and (b,c) in es:
                m+=1; te[(a,b)]+=1; te[(a,c)]+=1; te[(b,c)]+=1
        h=sum(v*(v-1)//2 for v in te.values()); tot+=1
        deg={v:sum(1 for w in range(r) if w!=v and (min(v,w),max(v,w)) in es) for v in range(r)}
        tau={}
        for v in range(r):
            N=[w for w in range(r) if w!=v and (min(v,w),max(v,w)) in es]
            tau[v]=sum(1 for a,b in itertools.combinations(N,2) if (min(a,b),max(a,b)) in es)
        if sum(tau.values())!=3*m: bad['(ii) Στ=3m']+=1
        if any(tau[v]>comb(deg[v],2) for v in range(r)): bad['(iii) τ≤C(d,2)']+=1
        s=0
        for (a,b) in te:
            Na=set(w for w in range(r) if w!=a and (min(a,w),max(a,w)) in es)
            Nb=set(w for w in range(r) if w!=b and (min(b,w),max(b,w)) in es)
            s+=comb(len(Na&Nb),2)
        if s!=h: bad['(iv) h=Σ_{vw∈E}C(|N(v)∩N(w)|,2)']+=1
        # (iv') 有序版（含因子2）
        s2=0
        for (a,b) in te:
            Na=set(w for w in range(r) if w!=a and (min(a,w),max(a,w)) in es)
            Nb=set(w for w in range(r) if w!=b and (min(b,w),max(b,w)) in es)
            s2+=comb(len(Na&Nb),2)
        if 2*s2!=h and s2!=h: bad['(iv-bug)']+=1
    return bad,tot
for r in (8,9,10,11):
    b,t=check(r,300)
    print(f"r={r} ({t} 随机图): {'全零 ✓✓' if not b else dict(b)}")
