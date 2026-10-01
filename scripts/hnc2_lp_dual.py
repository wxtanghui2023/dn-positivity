#!/usr/bin/env python3
"""HN-C2 L4/L2-a：LP 对偶权重法求 M >= lambda
max sum_T w_T  s.t.  for all blocks B: sum_{T subset B} w_T <= 1,  w_T >= 0
=> M >= ceil(sum w).  再对解做有理化并以精确整数算术复核（严格证书）。
"""
import itertools, numpy as np
from scipy.optimize import linprog
from scipy.sparse import csr_matrix
from fractions import Fraction
V,K,T=12,6,4
blocks=[tuple(c) for c in itertools.combinations(range(V),K)]
subs=[tuple(c) for c in itertools.combinations(range(V),T)]
si={s:i for i,s in enumerate(subs)}
rows=[];cols=[]
for bi,B in enumerate(blocks):
    for c in itertools.combinations(B,T):
        rows.append(bi); cols.append(si[c])
A=csr_matrix((np.ones(len(rows)),(rows,cols)),shape=(len(blocks),len(subs)))
print(f"约束(块) {len(blocks)}  变量(4-子集) {len(subs)}  非零 {len(rows)}")
res=linprog(-np.ones(len(subs)),A_ub=A,b_ub=np.ones(len(blocks)),bounds=(0,None),method='highs')
lam=-res.fun
print(f"[LP] status={res.status} lambda={lam:.10f}  ceil={int(np.ceil(lam-1e-9))}")
w=res.x
print(f"     支撑大小 {int((w>1e-12).sum())}  最大权 {w.max():.6f}  等式块数(紧) {int((np.abs(A@w-1)<1e-9).sum())}")
# 有理化：找最小分母 q 使整数解严格满足 A w_int <= q
best=None
for q in [1,2,3,4,5,6,8,10,12,15,20,24,30,40,60,120,360,840,2520,5040,10080,10**4,10**5,10**6]:
    wi=np.round(w*q).astype(np.int64)
    s=int(wi.sum())
    if s<=0: continue
    if np.all(A@wi<=q):
        frac=Fraction(s,q)
        if best is None or frac>best[0]: best=(frac,s,q,int((wi>0).sum()))
if best:
    fr,s,q,sup=best
    print(f"[严格证书] sum = {fr.numerator}/{fr.denominator} = {float(fr):.10f}  整数支撑 {sup}  (q={q})")
    print(f"           验证：A w <= 1 逐块通过 ✓ ；总权 {fr} {'> 40 ✓✓' if fr>40 else '<= 40 ✗'}")
else:
    print("[严格证书] 未找到可用有理化（报告浮点界）")
print(f"[结论] M >= {int(np.ceil(float(best[0])-1e-9)) if best else int(np.ceil(lam-1e-9))}")
