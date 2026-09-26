#!/usr/bin/env python3
"""逐点饱和: ∀z∈X3: h3(z)+h4(z)=3?  + X4 侧 equality 结构 + N4=9 可行性"""
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
    X3=[x for x in range(N) if bl[x]==3]; X4=[x for x in range(N) if bl[x]==4]
    h3=Counter(); h4=Counter()
    for x in range(N):
        if bl[x]<3: continue
        S=sorted(c for c in C if (BALL[x]>>c)&1)
        for u,v in itertools.combinations(S,2):
            for z in range(N):
                if (BALL[u]>>z)&1 and (BALL[v]>>z)&1 and z!=x:
                    if bl[x]==3: h3[z]+=1
                    else:
                        if bl[z] in (3,4): h4[z]+=1
    print(f"[{tag}] N3={len(X3)} N4={len(X4)}")
    # A. 逐点饱和
    sat=[(bl[z],h3[z]+h4[z]) for z in X3]
    print(f"   **逐点**: X3 点的 (h3+h4) 分布 = {dict(Counter(s for _,s in sat))} (期望全为 3)")
    print(f"   X3 点 h3 分布={dict(Counter(h3[z] for z in X3))} h4 分布={dict(Counter(h4[z] for z in X3))}")
    ok=all(s==3 for _,s in sat)
    print(f"   ⟹ **逐点饱和 h3+h4=3 {'✓✓ 成立（新定理候选）' if ok else '✗ 不成立'}**")
    # B. h3>=1
    print(f"   h3(z)≥1 ∀z∈X3? {'✓' if all(h3[z]>=1 for z in X3) else '✗'} | 故 h4 ≤ 2? {'✓' if all(h4[z]<=2 for z in X3) else '✗'}")
    # C. X4 侧结构: 每个 X4 点的 h3-load 与 h4-load 及总量/容量
    print(f"   X4 侧逐点: (h3, h4, 总, 容量6)")
    for y in sorted(X4):
        print(f"      {format(y,'09b')}: h3={h3[y]} h4={h4[y]} 总={h3[y]+h4[y]} {'**满**' if h3[y]+h4[y]==6 else ''}")
    print(f"   X4 点总负载分布={dict(Counter(h3[y]+h4[y] for y in X4))} (容量 6)")
    return X3,X4,h3,h4,bl
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
print("\n"+"="*60); print("N4=9 可行性（逐点饱和假设下）"); print("="*60)
N3=11;N4=9
print(f"  N4=9 ⟹ N3=11 | X3容量=3·11=33 | in-load=N3+I43=11+22=33 ✓ 自洽")
print(f"  逐点: 每 X3 点需 h3+h4=3；若 h3=1 强制 ⟹ h4=2 ⟹ I43=22 ✓")
print(f"  X4 侧: 22 个 X3-load 分给 9 点，容量 6 各 ⟹ 需 Σh3(y)=22 ≤ 9·6=54 ✓ 无矛盾")
print(f"  平均 22/9=2.44 ≤ 6 ✓ | 即使某点取 4（如实测），余量 2 仍足 ⟹ **无矛盾** ✗")
