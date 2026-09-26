#!/usr/bin/env python3
"""生死检验: 完整 incidence 矩阵 + 容量饱和 + N4=8/9 整数可行性"""
import itertools
from collections import Counter, defaultdict
def build(n):
    N=1<<n; BALL=[0]*N
    for x in range(N):
        m=1<<x
        for i in range(n): m|=1<<(x^(1<<i))
        BALL[x]=m
    return N,BALL
def analyse(n,C,tag,verbose=True):
    N,BALL=build(n); Cs=set(C); FULL=(1<<N)-1
    cov=0
    for c in C: cov|=BALL[c]
    if cov!=FULL: return
    bl=[sum(1 for c in C if (BALL[c]>>x)&1) for x in range(N)]
    X={j:[x for x in range(N) if bl[x]==j] for j in range(0,6)}
    # 全部 second-center incidence: x 遍历 b>=3 点, 每对 {u,v} 的所有公共点(≠x)
    I=defaultdict(int); inflow=Counter()
    for x in range(N):
        if bl[x]<3: continue
        S=sorted(c for c in C if (BALL[x]>>c)&1)
        for u,v in itertools.combinations(S,2):
            for z in range(N):
                if (BALL[u]>>z)&1 and (BALL[v]>>z)&1 and z!=x:
                    I[(bl[x],bl[z])]+=1; inflow[z]+=1
    out=Counter()
    for x in range(N):
        if bl[x]>=3: out[bl[x]]+=1
    A1=sum(1 for u,v in itertools.combinations(C,2) if bin(u^v).count('1')==1)
    print(f"[{tag}] N3={len(X[3])} N4={len(X[4])} N2={len(X[2])} | A1={A1}")
    print(f"   **完整 incidence 矩阵 I_ij** (行=源 X_i, 列=靶 X_j):")
    for i in range(3,6):
        if not X[i] and i>4: continue
        row={j:I[(i,j)] for j in range(0,6) if I[(i,j)]}
        if row: print(f"     X{i} -> {row}  (总出射={sum(row.values())}, 期望={len(X[i])*i*(i-1)//2})")
    # 容量: 每个 z 的 in-load ≤ C(b(z),2)
    viol=[(z,inflow[z],bl[z]*(bl[z]-1)//2) for z in inflow if inflow[z]>bl[z]*(bl[z]-1)//2]
    print(f"   容量检查 in-load(z) ≤ C(b(z),2): 违反={len(viol)} {'✓' if not viol else '✗'+str(viol[:3])}")
    # 按 X_j 分组的容量饱和度
    for j in (3,4):
        if not X[j]: continue
        cap=sum(bl[z]*(bl[z]-1)//2 for z in X[j]); used=sum(inflow[z] for z in X[j])
        print(f"     X{j}: 容量={cap} 已用={used} 饱和度={used/cap:.3f} {'**满** ✓✓' if used==cap else ''}")
    return len(X[3]),len(X[4]),I,bl
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
res=[analyse(9,c,f"(9,62)=K 码#{i}") for i,c in enumerate(load62(),1)]
print("\n"+"="*60); print("第二刀: N4=8/9 的整数可行性（仅用已立关系）"); print("="*60)
for t in (8,9):
    N3=38-3*t
    # 关系: (3,4,4) 模式 ⟹ I34=2N3; X3容量 = C(3,2)N3 = 3N3;  in-load(X3)=H3+I43=N3+2N3=3N3 恰好饱和
    print(f"  N4={t}: N3={N3} | I34=2N3={2*N3} | X3 in-load = N3+I43 = {N3}+{2*N3}={3*N3} = X3容量 3N3={3*N3} ✓ 饱和")
    print(f"      X4 侧: 需接收 I34={2*N3} ≤ 容量 6N4={6*t}? {'✓ 无矛盾' if 2*N3<=6*t else '✗ 矛盾'}")
    print(f"      X4 每点平均收 {2*N3/t:.2f} 个 X3-incidence (上限 β=4)")
    print(f"      ⟹ {'**无矛盾** ✗' if 2*N3<=4*t else '矛盾 ✓'}")
