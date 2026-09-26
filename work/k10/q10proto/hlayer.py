#!/usr/bin/env python3
"""核验: T₃ = Q_2 + H/3,  H = 3N_4 + Σ_{k≥5}(k-3)C(k-1,2)N_k；并统计各层"""
import itertools
from collections import Counter
def setup(n):
    N=1<<n; BM=[1<<x for x in range(N)]
    for x in range(N):
        for i in range(n): BM[x]|=1<<(x^(1<<i))
    return N,BM
def check(n,C):
    N,BM=setup(n)
    b=[sum(1 for c in C if (BM[c]>>x)&1) for x in range(N)]
    if any(v==0 for v in b): return None
    Nj=Counter(b)
    Q2=sum((k-1)*(k-2)//2*c for k,c in Nj.items() if k>=3)
    T3=sum(k*(k-1)*(k-2)//6*c for k,c in Nj.items() if k>=3)
    H=sum((k-3)*(k-1)*(k-2)//2*c for k,c in Nj.items() if k>=4)
    H4=3*Nj.get(4,0); H5=sum((k-3)*(k-1)*(k-2)//2*c for k,c in Nj.items() if k>=5)
    E=sum(v-1 for v in b)
    return dict(M=len(C),E=E,Q2=Q2,T3=T3,H=H,H4=H4,H5=H5,
        ok=(T3==Q2+H//3 if H%3==0 else abs(T3-(Q2+H/3))<1e-9),
        ok2=(H==H4+H5), dist=dict(sorted(Nj.items())), bmax=max(b))
def enum_codes(n,M,cap=20):
    N,BM=setup(n); out=[]; fullm=(1<<N)-1
    for C in itertools.combinations(range(N),M):
        cov=0
        for c in C: cov|=BM[c]
        if cov==fullm:
            out.append(list(C))
            if len(out)>=cap: break
    return out
print("=== 分层核验: T₃ = Q₂ + H/3 ===")
for n,M in ((4,4),(4,5),(4,6),(5,7)):
    rs=[r for r in (check(n,C) for C in enum_codes(n,M)) if r]
    ok=all(r['ok'] and r['ok2'] for r in rs)
    Hv=sorted(set(r['H'] for r in rs))
    print(f"[n={n} M={M} {'=K' if (n,M) in ((4,4),(5,7)) else '>K'}] 样本{len(rs)}: T₃=Q₂+H/3 全过={ok} ✓ | H∈{Hv} | b_max∈{sorted(set(r['bmax'] for r in rs))}")
    r=rs[0]; print(f"   样本0: E={r['E']} Q₂={r['Q2']} T₃={r['T3']} H={r['H']}(H₄={r['H4']},H≥5={r['H5']}) 分布={r['dist']}")
print()
print("=== H=0 且 E>0 的反例（否证'高k被强制'）===")
def syn(x):
    s=0
    for i in range(7):
        if (x>>i)&1: s^=(i+1)
    return s
H7=[x for x in range(128) if syn(x)==0]
C9=[((((h<<1)|bb)<<1)|cc) for h in H7 for bb in (0,1) for cc in (0,1)]
r=check(9,C9)
print(f"(9,64): E={r['E']}>0, H={r['H']}=0, b_max={r['bmax']}, 分布={r['dist']} ⟹ **H=0 而 E>0** ✗✓")
