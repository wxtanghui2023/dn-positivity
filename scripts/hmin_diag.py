import itertools, numpy as np, time
from scipy import sparse
from scipy.optimize import milp, LinearConstraint, Bounds
from math import comb
def jensen(r,m):
    q=comb(r,2);cap=r-2
    if m==0: return 0
    tot=3*m
    if tot>=q*cap: return q*comb(cap,2)
    L,s=divmod(tot,q); return q*comb(L,2)+s*L
def hyper_min(r,m,tl=60):
    """(b) 只求 m 个三元组（无闭合）之 min sum_e C(t_e,2)"""
    E=list(itertools.combinations(range(r),2)); ei={e:i for i,e in enumerate(E)}; nE=len(E)
    T=list(itertools.combinations(range(r),3)); nT=len(T)
    eof=[(ei[(a,b)],ei[(a,c)],ei[(b,c)]) for a,b,c in T]
    byedge={i:[] for i in range(nE)}
    for t,tr in enumerate(eof):
        for e in tr: byedge[e].append(t)
    pairs=[(e,a,b) for e,lst in byedge.items() for i,a in enumerate(lst) for b in lst[i+1:]]
    n=nT+len(pairs); rows=[];lo=[];hi=[]
    row=np.zeros(n)
    for t in range(nT): row[t]=1
    rows.append(row); lo.append(m); hi.append(m)
    for k,(e,a,b) in enumerate(pairs):
        row=np.zeros(n); row[nT+k]=-1; row[a]=1; row[b]=1
        rows.append(row); lo.append(-np.inf); hi.append(1)
    A=sparse.csr_matrix(np.array(rows)); c=np.zeros(n)
    for k in range(len(pairs)): c[nT+k]=1.0
    res=milp(c=c,constraints=[LinearConstraint(A,lo,hi)],integrality=np.ones(n),bounds=Bounds(0,1),options={"time_limit":tl})
    return (int(round(res.fun)) if res.success else None)
known={10:13,11:16,12:18,13:23,14:None,15:None,16:None,17:None,18:None}
lb={14:22,15:25,16:28,17:31,18:34}
print("r=8: (a)Jensen  <  (b)超图min(无闭合)  <=  (c)图min(闭合)",flush=True)
for m in (10,13,14,16,18):
    a=jensen(8,m); b=hyper_min(8,m,60)
    c=known.get(m); cl=lb.get(m)
    cs = f"EXACT={c}" if c is not None else (f"lb>={cl}" if cl else "?")
    print(f"  m={m:3d}: J={a:4d}  hyper<={b if b is not None else 'TL'}  graph:{cs}",flush=True)
print("DIAG DONE",flush=True)
