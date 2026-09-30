import itertools
from math import comb
from collections import defaultdict, Counter
def C2(x): return x*(x-1)//2
def H(e,m):
    if e==0: return 0
    L,s=divmod(3*m,e); return e*C2(L)+s*L
def J(r,m): return H(comb(r,2),m)
def emax_formula(r,m):
    if r%2==0:
        h=r//2; return h*h + m//h
    else:
        a=(r+1)//2; b=(r-1)//2
        # K_{a,b} + edges inside the larger part (each creates b triangles)
        return a*b + m//b
def emax_enum(r):
    E=list(itertools.combinations(range(r),2)); ne=len(E); ed={e:i for i,e in enumerate(E)}
    tris=[(ed[(a,b)],ed[(a,c)],ed[(b,c)]) for a,b,c in itertools.combinations(range(r),3)]
    best=defaultdict(int)
    for mask in range(1<<ne):
        e=bin(mask).count('1'); m=0
        for (x,y,z) in tris:
            if (mask>>x)&1 and (mask>>y)&1 and (mask>>z)&1: m+=1
        if e>best[m]: best[m]=e
    return best
print("=== 桥验证：公式 vs 枚举 ===")
for r in (4,5,6):
    be=emax_enum(r)
    ok=all(be[m]==emax_formula(r,m) for m in be)
    print(f"r={r}: {'全部吻合 ✓✓' if ok else '有偏差 ✗'}  (共 {len(be)} 个 m)")
    if not ok:
        for m in sorted(be):
            f=emax_formula(r,m)
            if f!=be[m]: print(f"    m={m}: 枚举 {be[m]} vs 公式 {f}")
print()
print("=== r=8: 闭式 e_max 与 Delta 下界 ===")
cert={20:44,21:66,22:64,23:70,24:76,25:90,26:88}
print(" m | e_max=16+m//4 | H(e_max,m) | J(8,m) | Delta下界 | 先前MILP认证")
for m in range(14,36):
    e=emax_formula(8,m); He=H(e,m); Jr=J(8,m)
    c=cert.get(m)
    print(f"{m:3d} | {e:5d} | {He:6d} | {Jr:6d} | {He-Jr:6d} | {c if c else '-'}")
print("BRIDGE DONE",flush=True)
