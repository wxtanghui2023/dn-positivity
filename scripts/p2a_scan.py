import re, itertools, random
from collections import Counter
def C2(x): return x*(x-1)//2
def load(path,n):
    out=set()
    for line in open(path,encoding='utf-8',errors='ignore'):
        b=re.sub(r'[^01]','',line.replace('\r',''))
        if len(b)==n: out.add(b)
    return out
def flip(w,ks):
    z=list(w)
    for k in ks: z[k]='1' if z[k]=='0' else '0'
    return ''.join(z)
C=load('sources/K10-1-120-cover-CERTIFICATE.txt',10)
C=sorted(C); n=10
print("|C| =",len(C),flush=True)
def scan(i, trials=40):
    stats=[]
    for t in range(trials):
        random.seed(1000+t)
        R=set(random.sample(C,i)); U=set(C)-R
        # 2A_2(R)
        rl=sorted(R); a2r=sum(1 for x,y in itertools.combinations(rl,2) if sum(a!=b for a,b in zip(x,y))==2)
        # 局部图
        sumh=0; summ=0; rs=Counter(); mx=0
        for q in U:
            V=[k for k in range(n) if flip(q,[k]) in R]
            r=len(V)
            if r<2: continue
            rs[r]+=1
            idx={k:j for j,k in enumerate(V)}
            E=set()
            for a,b in itertools.combinations(V,2):
                if flip(q,[a,b]) in U: E.add((idx[a],idx[b]))
            m=0; load=Counter()
            for a,b,c in itertools.combinations(range(r),3):
                if (a,b) in E and (a,c) in E and (b,c) in E:
                    m+=1; load[(a,b)]+=1; load[(a,c)]+=1; load[(b,c)]+=1
            h=sum(C2(v) for v in load.values())
            sumh+=h; summ+=m; mx=max(mx,m)
        stats.append((2*a2r, sumh, summ, mx, dict(rs)))
    return stats
print("i  | 2A_2(R) 均值 | Σh_q 均值 | Σm_q 均值 | 最大m_q | Σh_q/(2A_2) 比值范围",flush=True)
for i in (30,40,45,50,60,75):
    st=scan(i,30)
    a2=[s[0] for s in st]; sh=[s[1] for s in st]; sm=[s[2] for s in st]; mm=max(s[3] for s in st)
    ratio=[ (s[1]/s[0] if s[0] else 0) for s in st]
    print(f"{i:3d} | {sum(a2)/len(a2):8.1f} | {sum(sh)/len(sh):8.1f} | {sum(sm)/len(sm):8.1f} | {mm:3d} | {min(ratio):.3f}–{max(ratio):.3f}",flush=True)
print("DONE",flush=True)
