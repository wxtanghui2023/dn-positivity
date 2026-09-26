#!/usr/bin/env python3
"""P1.3: H4 重叠图完全分类 — 验证恒等式组 + 图结构"""
import itertools
from collections import Counter, defaultdict
def build(n):
    N=1<<n; BALL=[0]*N
    for x in range(N):
        m=1<<x
        for i in range(n): m|=1<<(x^(1<<i))
        BALL[x]=m
    return N,BALL
def analyse(n,C,tag):
    N,BALL=build(n); Cs=set(C); FULL=(1<<N)-1
    cov=0
    for c in C: cov|=BALL[c]
    if cov!=FULL: return
    bl=[sum(1 for c in C if (BALL[c]>>x)&1) for x in range(N)]
    X4=[x for x in range(N) if bl[x]==4]
    Sx={x:frozenset(c for c in C if (BALL[x]>>c)&1) for x in X4}
    # r(z)
    r=Counter()
    for x in X4:
        for z in Sx[x]: r[z]+=1
    rvals=Counter(r.values())
    s_r1=sum(v-1 for v in r.values() if v>=2)   # Σ(r-1)_+
    U=len(set().union(*Sx.values())) if Sx else 0
    # 公式验证 r(z) = 1_{b(z)=4} + #{i: b(z+e_i)=4}  (仅对 z∈C)
    ok=True; bad=[]
    for z in C:
        pred=(1 if bl[z]==4 else 0)+sum(1 for i in range(n) if bl[z^(1<<i)]==4)
        if pred!=r.get(z,0): ok=False; bad.append((z,pred,r.get(z,0)))
    # H4
    E=[]; 
    for x,y in itertools.combinations(X4,2):
        if Sx[x]&Sx[y]: E.append((bin(x^y).count('1'),x,y,len(Sx[x]&Sx[y])))
    deg=Counter()
    for d,x,y,ov in E: deg[x]+=1; deg[y]+=1
    # 连通分量
    par={x:x for x in X4}
    def find(a):
        while par[a]!=a: par[a]=par[par[a]]; a=par[a]
        return a
    for d,x,y,ov in E:
        ra,rb=find(x),find(y)
        if ra!=rb: par[ra]=rb
    comp=Counter(find(x) for x in X4)
    sumC2=sum(v*(v-1)//2 for v in r.values())
    print(f"[{tag}] N4={len(X4)} | 4N4={4*len(X4)} |∪Sx|={U} 差={4*len(X4)-U} | **Σ(r-1)+={s_r1}**")
    print(f"   r(z) 分布={dict(sorted(rvals.items()))} | Σ C(r,2)={sumC2} | r(z)≤2? {max(rvals)<=2 if rvals else True}")
    print(f"   公式 r(z)=1_(b=4)+#{{i:b(z+e_i)=4}} 验证: {'✓✓ 全对' if ok else '✗ '+str(bad[:3])}")
    print(f"   **H4: |V|={len(X4)} |E|={len(E)}** (边距离分布={dict(Counter(d for d,_,_,_ in E))})")
    print(f"   边交叠大小分布={dict(Counter(ov for _,_,_,ov in E))} | 度分布={dict(sorted(Counter(deg.values()).items()))} | Σdeg={sum(deg.values())}=2|E| ✓")
    print(f"   **连通分量大小={sorted(comp.values(),reverse=True)}** (分量数={len(comp)})")
    print(f"   界检查: |E|≤Σ C(r,2)={sumC2} {'✓' if len(E)<=sumC2 else '✗'} | Σdeg≤16 {'✓' if sum(deg.values())<=16 else '✗'} | H4⊆G≤2 {'✓' if all(d<=2 for d,_,_,_ in E) else '✗'}")
    # 关键: 孤立点 + 分量结构
    iso=[x for x in X4 if deg[x]==0]
    print(f"   孤立顶点(不与任何其他 b=4 中心重叠)={len(iso)} | 非孤立={len(X4)-len(iso)}")
    return dict(V=len(X4),E=len(E),comp=sorted(comp.values(),reverse=True),s_r1=s_r1,iso=len(iso))
def load62():
    codes=[];cur=[]
    for line in open('../c62/K_9_1_classif.txt'):
        a=line.split()
        if len(a)==9 and all(c in '01' for c in a): cur.append(int("".join(a),2))
        else:
            if len(cur)>=10: codes.append(cur)
            cur=[]
    if len(cur)>=10: codes.append(cur)
    return codes
for i,c in enumerate(load62(),1): analyse(9,c,f"(9,62)=K 码#{i}")
for s in "000000 000001 000010 001111 010111 011100 100111 101100 110100 111001 111010 111011","000100 000010 000001 100111 010111 001111 011000 101000 110000 111011 111101 111110":
    analyse(6,[int(x,2) for x in s.split()],"(6,12)=K")
