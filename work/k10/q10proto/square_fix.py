#!/usr/bin/env python3
"""修正 square 计数（规范形：每面唯一"自由位全 0"顶点 ✓）；核验 r(x)≤C(b-1,2)、4S≤Q_ours"""
import itertools
from collections import Counter
def setup(n):
    N=1<<n; NB=[[x^(1<<i) for i in range(n)] for x in range(N)]
    BM=[1<<x for x in range(N)]
    for x in range(N):
        for y in NB[x]: BM[x]|=1<<y
    return N,NB,BM
def census(n,C):
    N,NB,BM=setup(n); Cs=set(C); CW=0
    for w in C: CW|=1<<w
    b=[bin(BM[x]&CW).count('1') for x in range(N)]
    E=sum(v-1 for v in b); Qour=sum((v-1)*(v-2)//2 for v in b)
    N1=sum(1 for v in b if v==1); N2=sum(1 for v in b if v==2); N3=sum(1 for v in b if v>=3)
    faces=set()
    for u in Cs:
        for i,j in itertools.combinations(range(n),2):
            if not (u>>i)&1 and not (u>>j)&1:          # 规范形：自由位全 0 ✓ 每面恰一次
                a,bv,c=u^(1<<i),u^(1<<j),u^(1<<i)^(1<<j)
                if a in Cs and bv in Cs and c in Cs:
                    faces.add((u,i,j))
    S=len(faces)
    r=Counter()
    for (u,i,j) in faces:
        for z in (u,u^(1<<i),u^(1<<j),u^(1<<i)^(1<<j)): r[z]+=1
    V=len(r)
    viol_r=[(z,r[z],b[z]) for z in r if r[z] > (b[z]-1)*(b[z]-2)//2]
    return dict(M=len(C),E=E,Qour=Qour,N1=N1,N2=N2,N3=N3,S=S,V=V,
                rsum=sum(r.values()),viol_r=len(viol_r),
                ok4S=(4*S<=Qour),dist=dict(sorted(Counter(b).items())))
def enum_codes(n,M,cap=40):
    N,NB,BM=setup(n); out=[]; full=(1<<N)-1
    for C in itertools.combinations(range(N),M):
        cov=0
        for c in C: cov|=BM[c]
        if cov==full:
            out.append(list(C))
            if len(out)>=cap: break
    return out
print("=== 修正后 square 普查 ===")
for n,M in ((4,4),(4,5),(5,7)):
    rs=[census(n,C) for C in enum_codes(n,M)]
    print(f"[n={n} M={M}] 样本{len(rs)}: S∈{sorted(set(r['S'] for r in rs))} V∈{sorted(set(r['V'] for r in rs))} "
          f"Q_our∈{sorted(set(r['Qour'] for r in rs))} 4S≤Q_our全过={all(r['ok4S'] for r in rs)} ✓ "
          f"r(x)违反={sum(r['viol_r'] for r in rs)}")
def syn(x):
    s=0
    for i in range(7):
        if (x>>i)&1: s^=(i+1)
    return s
H7=[x for x in range(128) if syn(x)==0]
C9=[((((h<<1)|bb)<<1)|cc) for h in H7 for bb in (0,1) for cc in (0,1)]
r=census(9,C9)
print(f"\n[n=9 M=64 我方构造] E={r['E']} Q_our={r['Qour']} N1={r['N1']} N2={r['N2']} N≥3={r['N3']}")
print(f"   **S(修正后)={r['S']}**（上轮误报 32 ✗）  V={r['V']}  Σr=4S={r['rsum']} ✓")
print(f"   r(x) 违反={r['viol_r']}（0 ⟹ r(x)≤C(b-1,2) ✓）  **4S={4*r['S']} ≤ Q_our={r['Qour']}** {'✓ 成立' if r['ok4S'] else '✗'}")
print(f"   b 分布={r['dist']}")
print(f"\n=== M=62 预测（E=108）===")
print(f"  若 b∈{{1,3}} ⟹ N₃=54, Q_our=54 ⟹ **S ≤ 13** ✓（严格必要 ✓）")
print(f"  注意 ⚠️ 唐先生式 'Q_our=Σ_x C(d_C(x),2)' 仅对 x∈C 成立 ✗——非码字 x 的贡献是 C(b(x)−1,2) ✓")
