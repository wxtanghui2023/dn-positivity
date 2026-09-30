import itertools, time
from collections import Counter
def C2(x): return x*(x-1)//2
def H(e,m):
    if e<=0: return 0
    L,s=divmod(3*m,e); return e*C2(L)+s*L
r=8
edges=list(itertools.combinations(range(r),2)); ei={e:i for i,e in enumerate(edges)}; ne=28
triples=list(itertools.combinations(range(r),3))
tmask=[]; tri_e=[]
for t in triples:
    m_=0; el=[]
    for e in itertools.combinations(t,2):
        idx=ei[e]; m_|=1<<idx; el.append(idx)
    tmask.append(m_); tri_e.append(el)
def J(m): return H(ne,m)
emax={14:19,15:20,16:20,17:20,18:21,19:21,20:21,21:21,22:21,23:22,24:22,25:22,26:22,27:22,28:23,29:23,30:23,31:23,32:24,33:24,34:24,35:24}
print("m | e_max | q=28-e | extremizers | H_2=min h | H_1=H(e,m) | Gamma | J",flush=True)
for m in (18,19,20,22,23,24):
    e=emax[m]; q=ne-e; t0=time.time()
    best=None; cnt=0; hs=Counter()
    for C in itertools.combinations(range(ne),q):
        Cm=0
        for i in C: Cm|=1<<i
        T=0
        for mm in tmask:
            if not (mm & Cm): T+=1
        if T!=m: continue
        cnt+=1
        load=[0]*ne
        for ti,mm in enumerate(tmask):
            if not (mm & Cm):
                for idx in tri_e[ti]: load[idx]+=1
        h=sum(C2(v) for v in load)
        hs[h]+=1
        if best is None or h<best: best=h
    H1=H(e,m)
    print(f"{m:3d} | {e:2d} | {q:2d} | {cnt:6d} | {best:4d} | {H1:4d} | {best-H1 if best is not None else '?'} | {J(m):4d}   [{time.time()-t0:.0f}s] h分布={dict(sorted(hs.items())[:8])}",flush=True)
print("GAMMA DONE",flush=True)
