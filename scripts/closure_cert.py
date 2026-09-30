import itertools, random, sys
from collections import Counter
from math import comb
def C2(x): return x*(x-1)//2
def greedy_hyper(r,m,restarts=30):
    tris=list(itertools.combinations(range(r),3))
    best=None
    for _ in range(restarts):
        t=tris[:]; random.shuffle(t)
        load=Counter(); chosen=[]
        for _ in range(m):
            bt=None; bs=None
            for tr in t:
                if tr in chosen: continue
                s=sum(load[e] for e in itertools.combinations(tr,2))
                if bs is None or s<bs: bs=s; bt=tr
            chosen.append(bt)
            for e in itertools.combinations(bt,2): load[e]+=1
        h=sum(C2(l) for l in load.values())
        if best is None or h<best[0]: best=(h,chosen)
    return best
def closure(r,chosen):
    edges=set()
    for tr in chosen: edges|=set(itertools.combinations(tr,2))
    mG=0; te=Counter()
    for tr in itertools.combinations(range(r),3):
        if all(e in edges for e in itertools.combinations(tr,2)):
            mG+=1
            for e in itertools.combinations(tr,2): te[e]+=1
    return mG, sum(C2(v) for v in te.values()), len(edges)
print("r  m  |  v_hyp(超图贪心上界) | 闭合后 m_G | 多出三角形 m_G-m | 闭合后 h_G | h_G - v_hyp",flush=True)
for r,ms in ((8,[20,25,30,35,40,45,50,56]),(9,[15,20,25,30,40,50,60,70,84])):
    for m in ms:
        vh,ch=greedy_hyper(r,m,25)
        mG,hG,ne=closure(r,ch)
        print(f"{r} {m:3d} | {vh:4d} | {mG:4d} | {mG-m:+3d} | {hG:5d} | {hG-vh:+5d}",flush=True)
print("CERT DONE",flush=True)
