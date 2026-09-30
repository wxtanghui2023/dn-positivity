import itertools, numpy as np, sys
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
def dtru(r,tl=30):
    nE,nT,eof,byedge,pairs=base(r); n=nE+nT; rows=[];lo=[];hi=[]
    for t,tr in enumerate(eof):
        for e in tr:
            row=np.zeros(n); row[nE+t]=1; row[e]=-1; rows.append(row); lo.append(-np.inf); hi.append(0)
    for t,tr in enumerate(eof):
        row=np.zeros(n); row[nE+t]=-1
        for e in tr: row[e]=1
        rows.append(row); lo.append(-np.inf); hi.append(2)
    for e,lst in byedge.items():
        row=np.zeros(n)
        for t in lst: row[nE+t]=1
        rows.append(row); lo.append(-np.inf); hi.append(1)
    A=sparse.csr_matrix(np.array(rows)); c=np.zeros(n)
    for t in range(nT): c[nE+t]=-1.0
    res=milp(c=c,constraints=[LinearConstraint(A,lo,hi)],integrality=np.ones(n),bounds=Bounds(0,1),options={"time_limit":tl})
    return int(round(-res.fun)) if res.success else None
def hmin(r,m,tl=60):
    nE,nT,eof,byedge,pairs=base(r); nP=len(pairs); n=nE+nT+nP; rows=[];lo=[];hi=[]
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
    res=milp(c=c,constraints=[LinearConstraint(A,lo,hi)],integrality=np.ones(n),bounds=Bounds(0,1),options={"time_limit":tl})
    return int(round(res.fun)) if res.success else None
if __name__=="__main__":
    print("== D_true(r) MILP ==",flush=True)
    for r in range(3,10):
        print(f"  r={r}: D_true={dtru(r)}  (packing={comb(r,2)//3}, 早期数值={[1,1,2,4,7,8,12][r-3]})",flush=True)
    print("== r=8,9 h_min MILP ==",flush=True)
    for r in (8,9):
        print(f"  r={r} m_max={comb(r,3)}",flush=True)
        for m in (0,3,5,9,12,20,30,40,56,84):
            if m>comb(r,3): continue
            print(f"    m={m:3d} -> h_min={hmin(r,m)}",flush=True)
    print("DONE",flush=True)
