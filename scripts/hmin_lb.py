import itertools, numpy as np, time
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
    n=nE+nT+len(pairs); rows=[];lo=[];hi=[]
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
def decide(r,m,v,tl=45):
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
    return res.status==0, time.time()-t0
def jensen(r,m):
    q=comb(r,2);cap=r-2
    if m==0: return 0
    tot=3*m
    if tot>=q*cap: return q*comb(cap,2)
    L,s=divmod(tot,q); return q*comb(L,2)+s*L
targets=[(8,m) for m in range(14,31)]+[(9,m) for m in range(6,26)]
print(f"lb-batch: {len(targets)} targets",flush=True)
for (r,m) in targets:
    J=jensen(r,m); lo=J; v=J; step=1; feas=None
    while v <= comb(r,2)*comb(r-2,2):
        ok,dt=decide(r,m,v,45)
        if dt>=44.9:
            print(f"r={r} m={m:3d} J={J:4d} -> lb>={lo+1} (v={v} TIMEOUT)",flush=True); lo=None; break
        if ok: feas=v; break
        lo=v; v+=step; step=min(step*2,8)
    if lo is not None and feas is not None:
        print(f"r={r} m={m:3d} J={J:4d} -> h_min in [{lo+1},{feas}]{'  EXACT='+str(feas) if lo+1==feas else ''}",flush=True)
print("LB BATCH DONE",flush=True)
