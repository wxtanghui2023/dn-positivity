import itertools, numpy as np, time
from scipy import sparse
from scipy.optimize import milp, LinearConstraint, Bounds
from math import comb
exec(open('scripts/hmin_lb.py').read().split('targets=')[0])
def fine(r,m,v0,v1,tl=45):
    res=[]
    for v in range(v0,v1+1):
        ok,dt,st=decide3(r,m,v,tl)
        res.append((v,ok,dt,st))
        if ok: break
    return res
# 复用 decide 但返回状态
def decide3(r,m,v,tl=45):
    nE,nT,pairs,rows,lo,hi,n=base(r)
    A=list(rows);L=list(lo);H=list(hi)
    row=np.zeros(n)
    for t in range(nT): row[nE+t]=1
    A.append(row);L.append(m);H.append(m)
    row=np.zeros(n)
    for k in range(len(pairs)): row[nE+nT+k]=1
    A.append(row);L.append(-np.inf);H.append(v)
    A=sparse.csr_matrix(np.array(A)); c=np.zeros(n)
    t0=time.time()
    res=milp(c=c,constraints=[LinearConstraint(A,L,H)],integrality=np.ones(n),bounds=Bounds(0,1),options={"time_limit":tl})
    return res.status==0, time.time()-t0, res.status
print("细步探针（步长 1）",flush=True)
for (r,m,v0,v1) in [(8,14,22,29),(8,15,25,32),(8,16,28,34)]:
    print(f"-- r={r} m={m} --",flush=True)
    for v,ok,dt,st in fine(r,m,v0,v1,45):
        print(f"   v={v:3d} -> {'FEASIBLE' if ok else ('INFEASIBLE' if dt<44.5 else 'TIMEOUT')}  ({dt:.1f}s)",flush=True)
print("FINE DONE",flush=True)
