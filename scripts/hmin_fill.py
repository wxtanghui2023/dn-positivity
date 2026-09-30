import itertools, random, sys
from math import comb
from collections import Counter
def h_of(tris):
    c=Counter()
    for tr in tris:
        for e in itertools.combinations(tr,2): c[e]+=1
    return sum(v*(v-1)//2 for v in c.values())
def jensen(r,m):
    q=comb(r,2); cap=r-2
    if m==0: return 0
    tot=3*m
    if tot>=q*cap: return q*comb(cap,2)
    L,s=divmod(tot,q)
    return q*comb(L,2)+s*L
def greedy(r,m,trials=40,swaps=300):
    alltri=list(itertools.combinations(range(r),3))
    best=None
    for t in range(trials):
        tri=alltri[:]; random.shuffle(tri)
        load={}; chosen=[]
        for _ in range(m):
            bst=None;bs=None
            for tr in tri:
                if tr in chosen: continue
                s=sum(load.get(e,0) for e in itertools.combinations(tr,2))
                if bs is None or s<bs: bs=s; bst=tr
            chosen.append(bst)
            for e in itertools.combinations(bst,2): load[e]=load.get(e,0)+1
        h=h_of(chosen); it=0
        while it<swaps:
            it+=1; imp=False
            for i in range(m):
                h0=h
                for tr in tri:
                    if tr in chosen: continue
                    new=chosen[:i]+[tr]+chosen[i+1:]
                    h2=h_of(new)
                    if h2<h0:
                        chosen=new; h=h2; imp=True; break
                if imp: break
            if not imp: break
        if best is None or h<best: best=h
    return best
print("== 补全：Jensen 下界 / 贪心上界 / 已知精确 ==",flush=True)
known={8:{0:0,3:0,5:2,9:10,12:18,40:236,56:420},9:{0:0,3:0,5:0}}
for r in (8,9):
    mmax=comb(r,3)
    print(f"-- r={r} (m_max={mmax}) --",flush=True)
    for m in range(0,mmax+1):
        j=jensen(r,m); g=greedy(r,m,6,120)
        k=known[r].get(m)
        tag=f"EXACT={k}" if k is not None else "window"
        ok=""
        if k is not None:
            ok = " OK" if (j<=k<=g) else " !!窗口违背"
        print(f"  m={m:3d}  J={j:5d}  greedy<={g:5d}  {tag}{ok}",flush=True)
print("DONE",flush=True)
