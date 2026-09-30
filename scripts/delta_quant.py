import itertools, random, numpy as np, time
from collections import Counter
from scipy import sparse
from scipy.optimize import milp, LinearConstraint, Bounds
from math import comb
def C2(x): return x*(x-1)//2
def greedy_hyper(r,m,restarts=30):
    tris=list(itertools.combinations(range(r),3)); best=None
    for _ in range(restarts):
        t=tris[:]; random.shuffle(t); load=Counter(); chosen=[]
        for _ in range(m):
            bt=None; bs=None
            for tr in t:
                if tr in chosen: continue
                s=sum(load[e] for e in itertools.combinations(tr,2))
                if bs is None or s<bs: bs=s; bt=tr
            chosen.append(bt)
            for e in itertools.combinations(bt,2): load[e]+=1
        h=sum(C2(l) for l in load.values())
        if best is None or h<best: best=h
    return best
def mk(r):
    E=list(itertools.combinations(range(r),2)); ei={e:i for i,e in enumerate(E)}; nE=len(E)
    T=list(itertools.combinations(range(r),3)); nT=len(T)
    eof=[(ei[(a,b)],ei[(a,c)],ei[(b,c)]) for a,b,c in T]
    byedge={i:[] for i in range(nE)}
    for t,tr in enumerate(eof):
        for e in tr: byedge[e].append(t)
    pairs=[(e,a,b) for e,lst in byedge.items() for i,a in enumerate(lst) for b in lst[i+1:]]
    return nE,nT,eof,byedge,pairs
CACHE={}
def graphok(r,m,v,tl=40):
    if r not in CACHE: CACHE[r]=mk(r)
    nE,nT,eof,byedge,pairs=CACHE[r]; nP=len(pairs); n=nE+nT+nP; rows=[];lo=[];hi=[]
    if not CACHE.get(('rows',r)):
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
        CACHE[('rows',r)]=(rows,lo,hi)
    rows,lo,hi=CACHE[('rows',r)]
    A=list(rows); L=list(lo); H=list(hi)
    row=np.zeros(n)
    for t in range(nT): row[nE+t]=1
    A.append(row); L.append(m); H.append(m)
    row=np.zeros(n)
    for k in range(nP): row[nE+nT+k]=1
    A.append(row); L.append(-np.inf); H.append(v)
    M=sparse.csr_matrix(np.array(A)); c=np.zeros(n)
    t0=time.time()
    res=milp(c=c,constraints=[LinearConstraint(M,L,H)],integrality=np.ones(n),bounds=Bounds(0,1),options={"time_limit":tl})
    return res.status==0, time.time()-t0
print("r  m  | v_hyp | graph 首个不可行之 v | Δ下界 | 用时",flush=True)
for r,ms in ((8,[20,25,30,35]),(9,[15,20,25])):
    for m in ms:
        vh=greedy_hyper(r,m,25); found=None; t0=time.time()
        for v in range(vh, vh+6):
            ok,dt=graphok(r,m,v,40)
            if dt>=39.5: print(f"{r} {m:3d} | {vh:4d} | v={v} TIMEOUT | — | {time.time()-t0:.0f}s",flush=True); found='TO'; break
            if not ok: found=v; break
        if found!='TO' and found is not None:
            print(f"{r} {m:3d} | {vh:4d} | {found} | Δ>={found+1-vh} | {time.time()-t0:.0f}s",flush=True)
        elif found is None:
            print(f"{r} {m:3d} | {vh:4d} | 前6个v皆可行 | Δ未知 | {time.time()-t0:.0f}s",flush=True)
print("DELTA DONE",flush=True)
