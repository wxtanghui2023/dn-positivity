#!/usr/bin/env python3
"""决定性判定: 均匀-cell 条件下的分数覆盖数
   min Σ_c x_c  s.t.  A x ≥ 1,  0≤x≤1,  cell 和相等（线性）"""
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import lil_matrix
n=9;N=512
A=np.zeros((N,N),dtype=np.int8)
for u in range(N):
    A[u,u]=1
    for i in range(n): A[u,u^(1<<i)]=1
print("=== 均匀-cell 条件下的分数覆盖数（= OB 型下界的连续版）===")
base=None
for m in range(0,7):
    t=1<<m
    # 变量: x_c (512) + M (1)  ; 目标 min M
    cols=N+1
    rows=N+(t-1 if m>0 else 0)
    Aub=lil_matrix((rows,cols)); bub=np.zeros(rows)
    for u in range(N):
        for c in range(N):
            if A[u,c]: Aub[u,c]=-1.0
        bub[u]=-1.0
    # cell 和相等: Σ_{W_S} x - Σ_{W_0} x = 0
    if m>0:
        s=N//t
        r=N
        for S in range(1,t):
            for c in range(S*s,(S+1)*s): Aub[r,c]=1.0
            for c in range(0,s): Aub[r,c]-=1.0
            r+=1
    # Σ_c x_c - M = 0  (定义 M)
    r_eq=1 if m==0 else 1
    Aeq=lil_matrix((1,cols)); beq=np.zeros(1)
    for c in range(N): Aeq[0,c]=1.0
    Aeq[0,N]=-1.0
    cobj=np.zeros(cols); cobj[N]=1.0
    bounds=[(0,1)]*N+[(0,200)]
    res=linprog(c=cobj,A_ub=Aub.tocsr(),b_ub=bub,A_eq=Aeq.tocsr(),b_eq=beq,bounds=bounds,method='highs')
    if res.status==0:
        print(f"   m={m}: 分数下界 = {res.fun:.6f}")
    else:
        print(f"   m={m}: ✗ status={res.status} {res.message[:70]}")
