#!/usr/bin/env python3
"""H1 vs H2: 覆盖 LP 松弛 + 逐层 cell 计数条件 —— 数值判定
变量 x_c ∈[0,1] (512)；约束 Σ_{c∈B(u)}x_c ≥ 1 (512) + Σ_{c∈W_S}x_c = y_S (2^m)"""
import numpy as np, itertools
from scipy.optimize import linprog
from scipy.sparse import lil_matrix
n=9;N=512
# 覆盖矩阵 A[u][c]=1 iff d(c,u)<=1
A=np.zeros((N,N),dtype=np.int8)
for u in range(N):
    A[u,u]=1
    for i in range(n): A[u,u^(1<<i)]=1
print("=== H2: distribution-conditioned covering LP（M=62 的连续性下界）===")
print("   m=0 表示无 cell 约束（= H1）")
for m in range(0,7):
    M=62
    t=1<<m
    rows=N+t; cols=N
    Aub=lil_matrix((rows,cols)); bub=np.zeros(rows)
    # 覆盖约束: -Σ A[u,c] x_c <= -1
    for u in range(N):
        Aub[u,:]=-A[u,:]; bub[u]=-1.0
    beq=[];Aeq=lil_matrix((t,cols))
    if m>0:
        s=N//t
        for S in range(t):
            for c in range(S*s,(S+1)*s): Aeq[S,c]=1.0
        # 均匀 y（分数）：y_S = M/t
        beq=[M/t]*t
    Aub=Aub.tocsr(); Aeq=Aeq.tocsr() if m>0 else None
    res=linprog(c=np.ones(cols),A_ub=Aub,b_ub=bub,A_eq=Aeq,b_eq=np.array(beq) if beq else None,
                bounds=[(0,1)]*cols, method='highs')
    if res.status==0:
        print(f"   m={m:2d}: LP 最优 = {res.fun:.6f}   (体积界 512/10 = 51.2)")
    else:
        print(f"   m={m:2d}: infeasible/✗ status={res.status} {res.message[:60]}")
