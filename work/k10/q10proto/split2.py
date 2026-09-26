#!/usr/bin/env python3
"""核验新恒等式: 2A₂ = I + Σ_{x∉C}C(b(x),2)
 并测: d_C 最大值、非码字 b 最大值、饱和情形"""
import itertools
from collections import Counter
def setup(n):
    N=1<<n; NB=[[x^(1<<i) for i in range(n)] for x in range(N)]
    BM=[1<<x for x in range(N)]
    for x in range(N):
        for y in NB[x]: BM[x]|=1<<y
    return N,NB,BM
def analyse(n,C):
    N,NB,BM=setup(n); Cs=set(C)
    b={x:sum(1 for c in C if (BM[c]>>x)&1) for x in range(N)}
    assert all(v>=1 for v in b.values())
    A1=A2=0
    for u,v in itertools.combinations(C,2):
        d=bin(u^v).count('1')
        if d==1: A1+=1
        elif d==2: A2+=1
    I=sum((b[x]-1)*(b[x]-2)//2 for x in Cs)
    S=sum(b[x]*(b[x]-1)//2 for x in range(N) if x not in Cs)
    dC={c:b[c]-1 for c in C}
    return dict(M=len(C),A1=A1,A2=A2,I=I,S=S,twoA2=2*A2,
        ok=(2*A2==I+S), dCmax=max(dC.values()), bnonC=max(b[x] for x in range(N) if x not in Cs),
        bmax=max(b.values()), sat=(I==2*A2))
def enum_codes(n,M,cap=20):
    N,NB,BM=setup(n); out=[]; fullm=(1<<N)-1
    for C in itertools.combinations(range(N),M):
        cov=0
        for c in C: cov|=BM[c]
        if cov==fullm:
            out.append(list(C))
            if len(out)>=cap: break
    return out
print("=== 核验: 2A₂ = I + Σ_{x∉C}C(b(x),2) ===")
for n,M in ((4,4),(4,5),(5,7)):
    rs=[analyse(n,C) for C in enum_codes(n,M)]
    ok=all(r['ok'] for r in rs)
    print(f"[n={n} M={M} {'=K' if (n,M) in ((4,4),(5,7)) else '>K'}] 样本{len(rs)}: 恒等式全过={ok} ✓")
    r=rs[0]; print(f"   样本0: A₂={r['A2']} 2A₂={r['twoA2']} I={r['I']} S={r['S']} (I+S={r['I']+r['S']}) 饱和={r['sat']}")
    print(f"          d_C max={r['dCmax']}  非码字 b_max={r['bnonC']}  总 b_max={r['bmax']}")
    print(f"          全体 d_C max={max(x['dCmax'] for x in rs)}  全体非码字 b_max={max(x['bnonC'] for x in rs)}  全体饱和数={sum(1 for x in rs if x['sat'])}/{len(rs)}")
def syn(x):
    s=0
    for i in range(7):
        if (x>>i)&1: s^=(i+1)
    return s
H7=[x for x in range(128) if syn(x)==0]
C9=[((((h<<1)|bb)<<1)|cc) for h in H7 for bb in (0,1) for cc in (0,1)]
r=analyse(9,C9)
print(f"[n=9 M=64] A₂={r['A2']} 2A₂={r['twoA2']} I={r['I']} S={r['S']} 恒等式✓={r['ok']} 饱和={r['sat']}")
print(f"          d_C max={r['dCmax']} 非码字 b_max={r['bnonC']}")
print()
print("=== 读数 ===")
print(" **2A₂ = I + Σ_{x∉C}C(b(x),2)** ⟹ I = 2A₂ ⟺ **∀x∉C: b(x) ≤ 1**（饱和等价，结构性 ✓✓）")
print(" 唐先生论证成立: 非码字 x 有 b(x)=k ⟹ 其 C(k,2) 个对在 x 处损失 ≥1 ⟹ I ≤ 2A₂ − C(k,2) ✓")
