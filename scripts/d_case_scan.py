import itertools
from collections import Counter, defaultdict
def C2(x): return x*(x-1)//2
r=8
edges=list(itertools.combinations(range(r),2)); ei={e:i for i,e in enumerate(edges)}; ne=28
tri=list(itertools.combinations(range(r),3)); tmask=[]; tri_e=[]
for t in tri:
    m=0; el=[]
    for e in itertools.combinations(t,2):
        idx=ei[e]; m|=1<<idx; el.append(idx)
    tmask.append(m); tri_e.append(el)
byT=defaultdict(Counter)      # T -> Counter(h)
for C in itertools.combinations(range(ne),7):
    Cm=0
    for i in C: Cm|=1<<i
    T=sum(1 for m in tmask if not (m & Cm))
    load=[0]*ne
    for ti,m in enumerate(tmask):
        if not (m & Cm):
            for idx in tri_e[ti]: load[idx]+=1
    h=sum(C2(v) for v in load)
    byT[T][h]+=1
print("T | #graphs(e=21) | h 最小值 | 是否有 h=63/64/65 (即 D=0/2/4) | h 取值(前12)")
for T in sorted(byT):
    c=byT[T]; hs=sorted(c)
    low=[x for x in (63,64,65) if x in c]
    print(f"{T:3d} | {sum(c.values()):7d} | {hs[0]:4d} | {'有: '+str(low) if low else '无 ✓'} | {hs[:12]}",flush=True)
print("DONE",flush=True)
