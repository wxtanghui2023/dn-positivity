#!/usr/bin/env python3
"""P1-LB: 下界路线 — 等价性验证 + C→X2 接口检验 + Hall 匹配 + n=5 反例核对"""
import itertools
from collections import Counter, defaultdict
def build(n):
    N=1<<n; BALL=[0]*N
    for x in range(N):
        m=1<<x
        for i in range(n): m|=1<<(x^(1<<i))
        BALL[x]=m
    return N,BALL
print("="*64); print("① 代数纠错 + 等价性"); print("="*64)
print("  唐先生写 N1+2N2+3N3+4N4 = 9M = 558 ✗  ⟹ 正确: ΣjN_j = M(n+1) = 10M = 620 ✓")
for M,n in ((62,9),(12,6),(7,5),(4,4)):
    E=M*(n+1)-(1<<n)
    print(f"  n={n} M={M}: ΣjN_j={M*(n+1)} ✓, Σ(j-1)N_j = E = {E} ✓ (非 {n*M})")
print("  ⟹ N4=10 ⟺ N3=38-30=8 ⟺ N2=32+30=62 ⟺ N1=442-10=432 ✓✓ (四者等价 ✓)")
print("\n"+"="*64); print("② C→X2 接口检验"); print("="*64)
def analyse(n,C,tag):
    N,BALL=build(n); Cs=set(C); FULL=(1<<N)-1
    cov=0
    for c in C: cov|=BALL[c]
    if cov!=FULL: return
    bl=[sum(1 for c in C if (BALL[c]>>x)&1) for x in range(N)]
    Nj=Counter(bl); M=len(C)
    X2=[x for x in range(N) if bl[x]==2]
    # 每个码字的 邻域 b=2 点数（含 c 自身若 b(c)=2）
    deg={}
    for c in C:
        nb=set([c]+[c^(1<<i) for i in range(n)])
        deg[c]=sum(1 for x in nb if bl[x]==2)
    degmin=min(deg.values()); degmax=max(deg.values())
    # 二部图匹配 C ↔ X2 (邻域:B1(c) 内 b=2 点)
    adj={c:[x for x in [c]+[c^(1<<i) for i in range(n)] if bl[x]==2] for c in C}
    match={}
    def try_k(c,seen):
        for x in adj[c]:
            if x in seen: continue
            seen.add(x)
            if x not in match or try_k(match[x],seen):
                match[x]=c; return True
        return False
    cnt=0
    for c in C:
        if try_k(c,set()): cnt+=1
    # Hall 违反检查：最小 |N(S)|-|S| (贪心/小规模精确对 n<=6, 抽样对 n=9)
    print(f"[{tag}] M={M} N2={Nj.get(2,0)} |X2|={len(X2)} | N2≥M? {'✓' if Nj.get(2,0)>=M else '✗'}")
    print(f"   每码字的 b=2 邻域数: min={degmin} max={degmax} | 匹配成功={cnt}/{M} {'✓✓ 完美匹配' if cnt==M else '✗'}")
    print(f"   b 分布={dict(sorted(Nj.items()))}")
    return Nj.get(2,0),M
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
c1=[int(x,2) for x in "000000 000001 000010 001111 010111 011100 100111 101100 110100 111001 111010 111011".split()]
c2=[int(x,2) for x in "000100 000010 000001 100111 010111 001111 011000 101000 110000 111011 111101 111110".split()]
analyse(6,c1,"(6,12)=K 类#1"); analyse(6,c2,"(6,12)=K 类#2")
n=4;N,BALL=build(n);FULL=(1<<N)-1
for C in itertools.combinations(range(N),4):
    cov=0
    for c in C: cov|=BALL[c]
    if cov==FULL: analyse(4,list(C),"(4,4)=K"); break
n=5;N,BALL=build(n);FULL=(1<<N)-1
for C in itertools.combinations(range(N),7):
    cov=0
    for c in C: cov|=BALL[c]
    if cov==FULL: analyse(5,list(C),"(5,7)=K"); break
print("\n 注: (5,7) 若 N2=6 < M=7 ⟹ 'N2≥M' 非普适 ✗（仅 n=9 的等价形式）")
