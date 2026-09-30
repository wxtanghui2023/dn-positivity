import itertools, numpy as np, sys, time
from scipy import sparse
from scipy.optimize import milp, LinearConstraint, Bounds
from math import comb
def base(r):
    E=list(itertools.combinations(range(r),2)); ei={e:i for i,e in enumerate(E)}; nE=len(E)
    T=list(itertools.combinations(range(r),3)); nT=len(T)
    eof=[(ei[(a,b)],ei[(a,c)],ei[(b,c)]) for a,b,c in T]
    byedge={i:[] for i in range(nE)}
    for t,tr in enumerate(eof):
        for e in tr: byedge[e].append(t)
    pairs=[(e,a,b) for e,lst in byedge.items() for i,a in enumerate(lst) for b in lst[i+1:]]
    return nE,nT,eof,byedge,pairs
def hmin(r,m,tl):
    nE,nT,eof,byedge,pairs=base(r); nP=len(pairs); n=nE+nT+nP
    rows=[];lo=[];hi=[]
    for t,tr in enumerate(eof):
        for e in tr:
            row=np.zeros(n); row[nE+t]=1; row[e]=-1; rows.append(row); lo.append(-np.inf); hi.append(0)
    for t,tr in enumerate(eof):
        row=np.zeros(n); row[nE+t]=-1
        for e in tr: row[e]=1
        rows.append(row); lo.append(-np.inf); hi.append(2)
    row=np.zeros(n)
    for t in range(nT): row[nE+t]=1
    rows.append(row); lo.append(m); hi.append(m)
    for k,(e,a,b) in enumerate(pairs):
        row=np.zeros(n); row[nE+nT+k]=-1; row[nE+a]=1; row[nE+b]=1
        rows.append(row); lo.append(-np.inf); hi.append(1)
    A=sparse.csr_matrix(np.array(rows)); c=np.zeros(n)
    for k in range(nP): c[nE+nT+k]=1.0
    t0=time.time()
    res=milp(c=c,constraints=[LinearConstraint(A,lo,hi)],integrality=np.ones(n),bounds=Bounds(0,1),options={"time_limit":tl})
    dt=time.time()-t0
    return (int(round(res.fun)) if res.success else None), dt, res.status
order=[(8,m) for m in list(range(4,21))+list(range(21,57,3))]+[(9,m) for m in list(range(6,21))+list(range(21,85,3))]
print(f"batch: {len(order)} solves (tl=100s each)",flush=True)
for r,m in order:
    v,dt,st=hmin(r,m,100)
    print(f"r={r} m={m:3d} -> h_min={'TIMEOUT' if v is None else v}  ({dt:.1f}s, status={st})",flush=True)
print("BATCH DONE",flush=True)
