import itertools, numpy as np, time, sys
from scipy import sparse
from scipy.optimize import milp, LinearConstraint, Bounds
def build(r):
    E=list(itertools.combinations(range(r),2)); ei={e:i for i,e in enumerate(E)}; nE=len(E)
    T=list(itertools.combinations(range(r),3)); nT=len(T)
    eof=[(ei[(a,b)],ei[(a,c)],ei[(b,c)]) for a,b,c in T]
    byedge={i:[] for i in range(nE)}
    for t,tr in enumerate(eof):
        for e in tr: byedge[e].append(t)
    pairs=[(e,a,b) for e,lst in byedge.items() for i,a in enumerate(lst) for b in lst[i+1:]]
    # static rows: closure lower, closure upper, w>=ya+yb-1
    rows=[];lo=[];hi=[]
    n=nE+nT+len(pairs)
    for t,tr in enumerate(eof):
        for e in tr:
            row=np.zeros(n); row[nE+t]=1; row[e]=-1; rows.append(row); lo.append(-np.inf); hi.append(0)
    for t,tr in enumerate(eof):
        row=np.zeros(n); row[nE+t]=-1
        for e in tr: row[e]=1
        rows.append(row); lo.append(-np.inf); hi.append(2)
    for k,(e,a,b) in enumerate(pairs):
        row=np.zeros(n); row[nE+nT+k]=-1; row[nE+a]=1; row[nE+b]=1
        rows.append(row); lo.append(-np.inf); hi.append(1)
    return nE,nT,pairs,rows,lo,hi,n
def decide(r,m,v,tl=60):
    nE,nT,pairs,rows,lo,hi,n=build(r)
    A=list(rows); L=list(lo); H=list(hi)
    row=np.zeros(n)
    for t in range(nT): row[nE+t]=1
    A.append(row); L.append(m); H.append(m)
    row=np.zeros(n)
    for k in range(len(pairs)): row[nE+nT+k]=1
    A.append(row); L.append(-np.inf); H.append(v)
    A=sparse.csr_matrix(np.array(A)); c=np.zeros(n)
    t0=time.time()
    res=milp(c=c,constraints=[LinearConstraint(A,L,H)],integrality=np.ones(n),bounds=Bounds(0,1),options={"time_limit":tl})
    return (res.status==0), time.time()-t0
print("== 判定式: h_min(8,m) <= v ? ==",flush=True)
for m in (14,15):
    for v in (30,26,24,23):
        ok,dt=decide(8,m,v,60)
        print(f"  m={m} v={v:3d} -> {'FEASIBLE' if ok else ('INFEASIBLE' if dt<59 else 'TIMEOUT')}  ({dt:.1f}s)",flush=True)
print("DONE",flush=True)
