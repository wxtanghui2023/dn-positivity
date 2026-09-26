#!/usr/bin/env python3
"""P1-LB.3 (修订): 矩松弛 LP — 枚举基本解 (3 约束 ⟹ 3 个非零变量)"""
import itertools, fractions as F
def solve(n,M,Q2):
    N=1<<n; E=M*(n+1)-N
    js=list(range(0,n+2))          # b=0..n+1
    best=None; worst=None; feas=[]
    for idx in itertools.combinations(range(len(js)),3):
        J=[js[i] for i in idx]
        # 解 Σ N_j = N, Σ(j-1)N_j = E, ΣC(j-1,2)N_j = Q2
        a=[[1,1,1],[j-1 for j in J],[(j-1)*(j-2)//2 for j in J]]
        b=[N,E,Q2]
        # 高斯消元
        import copy
        A=[row[:]+[b[i]] for i,row in enumerate(a)]
        ok=True
        for c in range(3):
            p=None
            for r in range(c,3):
                if A[r][c]!=0: p=r; break
            if p is None: ok=False; break
            A[c],A[p]=A[p],A[c]
            piv=A[c][c]
            for r in range(3):
                if r!=c and A[r][c]!=0:
                    f=A[r][c]/piv
                    for k in range(4): A[r][k]-=f*A[c][k]
        if not ok: continue
        sol=[A[i][3]/A[i][i] for i in range(3)]
        if any(s<-1e-9 for s in sol): continue
        vals={J[i]:sol[i] for i in range(3)}
        T3=sum((j*(j-1)*(j-2)//6)*v for j,v in vals.items())
        feas.append((T3,vals))
    return E,feas
print("="*66); print("P1-LB.3 矩松弛: min/max T3（仅用三矩 + 非负性）"); print("="*66)
for (n,M,Q2) in ((9,62,38),(6,12,4),(5,7,2),(4,4,0)):
    E,feas=solve(n,M,Q2)
    if not feas: print(f"[n={n}] 无解 ✗"); continue
    T3s=[f[0] for f in feas]
    mn=min(feas); mx=max(feas)
    print(f"[n={n},M={M}] E={E} Q2={Q2} | 基本可行解={len(feas)} | **min T3={min(T3s):.0f}** max T3={max(T3s):.0f}")
    print(f"   min 剖面: { {k:round(v,1) for k,v in mn[1].items()} }")
    print(f"   max 剖面: { {k:round(v,1) for k,v in mx[1].items()} }")
    if (n,M)==(9,62):
        print(f"   ⟹ **矩松弛只给 T3 ≥ {min(T3s):.0f}** ⟹ {'✗ 弱于 48，需几何输入' if min(T3s)<48 else '✓'}")
        n4=[v.get(4,0) for _,v in feas]
        print(f"   矩可行族中 N4 取值 = {sorted(set(round(x,2) for x in n4))}")
