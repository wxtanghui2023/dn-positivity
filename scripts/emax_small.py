import itertools
from math import comb
from collections import defaultdict, Counter
def C2(x): return x*(x-1)//2
def H(e,m):
    if e==0: return 0
    L,s=divmod(3*m,e)
    return e*C2(L)+s*L
def J(r,m): return H(comb(r,2),m)
def enum(r):
    E=list(itertools.combinations(range(r),2)); ne=len(E)
    edict={e:i for i,e in enumerate(E)}
    tris=[(edict[(a,b)],edict[(a,c)],edict[(b,c)]) for a,b,c in itertools.combinations(range(r),3)]
    best=defaultdict(lambda: (0,10**9,None))  # m -> (e_max, h_min, e_of_hmin)
    for mask in range(1<<ne):
        e=bin(mask).count('1')
        m=0; ld=Counter()
        for (x,y,z) in tris:
            if (mask>>x)&1 and (mask>>y)&1 and (mask>>z)&1:
                m+=1; ld[x]+=1; ld[y]+=1; ld[z]+=1
        h=sum(C2(v) for v in ld.values())
        cur=best[m]
        if e>cur[0]: best[m]=(e,cur[1],cur[2])
        if h<cur[1]: best[m]=(best[m][0],h,e)
    return best
print("r | m | e_max | H(e_max,m) | J(r,m) | 解释Δ? | 精确h_min | H<=h_min?")
for r in (4,5,6):
    b=enum(r); Q=comb(r,2)
    for m in sorted(b):
        emax,hmin,_=b[m]
        He=H(emax,m); Jr=J(r,m)
        print(f"{r} | {m:2d} | {emax:2d} | {He:4d} | {Jr:4d} | {'Δ>0 ✓' if He>Jr else 'Δ=0 ✗'} | {hmin:4d} | {'✓' if He<=hmin else '✗违背'}")
    print()
print("DONE",flush=True)
