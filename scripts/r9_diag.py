import itertools, numpy as np, time
from scipy import sparse
from scipy.optimize import milp, LinearConstraint, Bounds
from math import comb
def mk(r):
    E=list(itertools.combinations(range(r),2)); ei={e:i for i,e in enumerate(E)}; nE=len(E)
    T=list(itertools.combinations(range(r),3)); nT=len(T)
    eof=[(ei[(a,b)],ei[(a,c)],ei[(b,c)]) for a,b,c in T]
    byedge={i:[] for i in range(nE)}
    for t,tr in enumerate(eof):
        for e in tr: byedge[e].append(t)
    pairs=[(e,a,b) for e,lst in byedge.items() for i,a in enumerate(lst) for b in lst[i+1:]]
    return nE,nT,eof,byedge,pairs
def jensen(r,m):
    q=comb(r,2);cap=r-2
    if m==0: return 0
    tot=3*m
    if tot>=q*cap: return q*comb(cap,2)
    L,s=divmod(tot,q); return q*comb(L,2)+s*L
def hyper(r,m,tl=60):
    nE,nT,eof,byedge,pairs=mk(r); n=nT+len(pairs); rows=[];lo=[];hi=[]
    row=np.zeros(n)
    for t in range(nT): row[t]=1
    rows.append(row); lo.append(m); hi.append(m)
    for k,(e,a,b) in enumerate(pairs):
        row=np.zeros(n); row[nT+k]=-1; row[a]=1; row[b]=1
        rows.append(row); lo.append(-np.inf); hi.append(1)
    A=sparse.csr_matrix(np.array(rows)); c=np.zeros(n)
    for k in range(len(pairs)): c[nT+k]=1.0
    res=milp(c=c,constraints=[LinearConstraint(A,lo,hi)],integrality=np.ones(n),bounds=Bounds(0,1),options={"time_limit":tl})
    return int(round(res.fun)) if res.success else None
def graphok(r,m,v,tl=75):
    nE,nT,eof,byedge,pairs=mk(r); nP=len(pairs); n=nE+nT+nP; rows=[];lo=[];hi=[]
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
    row=np.zeros(n)
    for k in range(nP): row[nE+nT+k]=1
    rows.append(row); lo.append(-np.inf); hi.append(v)
    A=sparse.csr_matrix(np.array(rows)); c=np.zeros(n)
    t0=time.time()
    res=milp(c=c,constraints=[LinearConstraint(A,lo,hi)],integrality=np.ones(n),bounds=Bounds(0,1),options={"time_limit":tl})
    return res.status==0, time.time()-t0
print("r=9 单探针: 在 v=hyper-min 处图是否可行（不可行⟹闭合咬✓）",flush=True)
for m in (6,9,12,15,20,30):
    J=jensen(9,m); b=hyper(9,m,60)
    if b is None:
        print(f"  m={m:3d}: J={J:4d} hyper=TIMEOUT",flush=True); continue
    ok,dt=graphok(9,m,b,75)
    verdict="FEASIBLE(闭合不咬✗)" if ok else ("INFEASIBLE(闭合咬✓)" if dt<74.5 else "TIMEOUT")
    print(f"  m={m:3d}: J={J:4d}  hyper-min={b:4d}  图在v={b}: {verdict}  ({dt:.1f}s)",flush=True)
print("R9 DONE",flush=True)
