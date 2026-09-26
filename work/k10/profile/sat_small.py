#!/usr/bin/env python3
"""饱和检验 T3 = #triangles(G≤2) 在小 n 极值码上"""
import itertools
from collections import Counter
def build(n):
    N=1<<n; BALL=[0]*N
    for x in range(N):
        m=1<<x
        for i in range(n): m|=1<<(x^(1<<i))
        BALL[x]=m
    return N,BALL
def sat(n,C,tag):
    N,BALL=build(n); Cs=set(C); FULL=(1<<N)-1
    cov=0
    for c in C: cov|=BALL[c]
    if cov!=FULL: return None
    b={x:sum(1 for c in C if (BALL[c]>>x)&1) for x in range(N)}
    Nj=Counter(b.values())
    E=sum(v-1 for v in b.values()); Q2=sum((v-1)*(v-2)//2 for v in b.values())
    T3=sum(v*(v-1)*(v-2)//6 for v in b.values())
    adj={u:set(v for v in C if 1<=bin(u^v).count('1')<=2) for u in C}
    tri=sum(1 for u,v,w in itertools.combinations(C,3) if v in adj[u] and w in adj[u] and w in adj[v])
    A1=sum(1 for u,v in itertools.combinations(C,2) if bin(u^v).count('1')==1)
    A2=sum(1 for u,v in itertools.combinations(C,2) if bin(u^v).count('1')==2)
    # 若 b<=4: t 参数
    t=Nj.get(4,0); N3=Nj.get(3,0)
    print(f"[{tag}] n={n} M={len(C)} 剖面={[Nj.get(j,0) for j in range(1,max(b.values())+1)]} maxb={max(b.values())}")
    print(f"    E={E} Q2={Q2} | **T3={T3}** | #三角形(G≤2)={tri} | **饱和 T3==#tri? {T3==tri}** | A1={A1} A2={A2}")
    if max(b.values())<=4:
        print(f"    t=N4={t} N3={N3} | 族预测 T3=38+t? n=9专属; 此处 3阶恒等 T3=N3+4N4={N3+4*t} ✓")
    return dict(n=n,M=len(C),T3=T3,tri=tri,sat=(T3==tri),E=E,Q2=Q2,t=t,N3=N3)
res=[]
n=4;N,BALL=build(n);FULL=(1<<N)-1
for C in itertools.combinations(range(N),4):
    cov=0
    for c in C: cov|=BALL[c]
    if cov==FULL: res.append(sat(n,list(C),"(4,4)=K")); break
n=5;N,BALL=build(n);FULL=(1<<N)-1
for C in itertools.combinations(range(N),7):
    cov=0
    for c in C: cov|=BALL[c]
    if cov==FULL: res.append(sat(n,list(C),"(5,7)=K")); break
c1=[int(x,2) for x in "000000 000001 000010 001111 010111 011100 100111 101100 110100 111001 111010 111011".split()]
c2=[int(x,2) for x in "000100 000010 000001 100111 010111 001111 011000 101000 110000 111011 111101 111110".split()]
res.append(sat(6,c1,"(6,12)=K 类#1")); res.append(sat(6,c2,"(6,12)=K 类#2"))
print("\n=== 饱和汇总 ===")
for r in res:
    if r: print(f"  n={r['n']} M={r['M']}: T3={r['T3']} #tri={r['tri']} 饱和={'✓✓' if r['sat'] else '✗'} | E={r['E']} Q2={r['Q2']} N4={r['t']} N3={r['N3']}")
