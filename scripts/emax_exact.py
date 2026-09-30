import itertools, numpy as np, time
from scipy import sparse
from scipy.optimize import milp, LinearConstraint, Bounds
from math import comb
def C2(x): return x*(x-1)//2
def H(e,m):
    if e<=0: return 0
    L,s=divmod(3*m,e); return e*C2(L)+s*L
def J(r,m): return H(comb(r,2),m)
r=8
E=list(itertools.combinations(range(r),2)); ne=len(E); ei={e:i for i,e in enumerate(E)}
T=list(itertools.combinations(range(r),3)); nT=len(T)
eof=[(ei[(a,b)],ei[(a,c)],ei[(b,c)]) for a,b,c in T]
# 静态行：闭合 y<=e ; sum e - y <= 2
rows=[];lo=[];hi=[]
for t,tr in enumerate(eof):
    for e in tr:
        row=np.zeros(ne+nT); row[ne+t]=1; row[e]=-1; rows.append(row); lo.append(-np.inf); hi.append(0)
for t,tr in enumerate(eof):
    row=np.zeros(ne+nT); row[ne+t]=-1
    for e in tr: row[e]=1
    rows.append(row); lo.append(-np.inf); hi.append(2)
STATIC=(np.array(rows),np.array(lo),np.array(hi))
def feas(m,Emin,tl=25):
    rows,lo,hi=STATIC
    A=np.vstack([rows, np.concatenate([np.ones(ne),np.zeros(nT)])[None,:], np.concatenate([np.zeros(ne),np.ones(nT)])[None,:]])
    L=np.concatenate([lo,[Emin,m]]); Hh=np.concatenate([hi,[np.inf,m]])
    res=milp(c=np.zeros(ne+nT),constraints=[LinearConstraint(sparse.csr_matrix(A),L,Hh)],
             integrality=np.ones(ne+nT),bounds=Bounds(0,1),options={"time_limit":tl})
    return res.status==0
def emax_for(m,loE=16,hiE=28,tl=25):
    best=None; trace=[]
    lo,hi=loE,hiE
    while lo<=hi:
        mid=(lo+hi)//2
        ok=feas(m,mid,tl)
        trace.append((mid,ok))
        if ok: best=mid; lo=mid+1
        else: hi=mid-1
    return best,trace
print("m | e_max | H(e_max,m) | J(8,m) | Delta_cert | 审计",flush=True)
for m in [21,25]+[x for x in range(14,36) if x not in (21,25)]:
    t0=time.time()
    em,tr=emax_for(m)
    if em is None:
        print(f"{m:3d} | 失败/全不可行 | trace={tr}",flush=True); continue
    He=H(em,m); Jr=J(8,m)
    print(f"{m:3d} | {em:3d} | {He:5d} | {Jr:4d} | {He-Jr:5d} | {time.time()-t0:.0f}s trace={tr}",flush=True)
print("EMAX DONE",flush=True)
