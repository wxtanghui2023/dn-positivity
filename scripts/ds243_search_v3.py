#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Z_3 x Z_9 x Z_9 (243,121,60)-差集搜索 v3 —— 修正移动可行性
   |D| = 121 = 1 不动点 + 40 个 3-轨道（或 4 + 39 等）
"""
import numpy as np, random, sys, time
G = [(a,b,c) for a in range(3) for b in range(9) for c in range(9)]
sig = lambda x: ((7*x[0])%3, (7*x[1])%9, (7*x[2])%9)
seen=set(); orbits=[]
for x in G:
    if x in seen: continue
    o=[]; y=x
    while y not in seen: seen.add(y); o.append(y); y=sig(y)
    orbits.append(o)
NO=len(orbits); sizes=np.array([len(o) for o in orbits])
fixed=[i for i in range(NO) if sizes[i]==1]; tri=[i for i in range(NO) if sizes[i]==3]
nz=[z for z in G if z!=(0,0,0)]; nzidx={z:t for t,z in enumerate(nz)}
print(f"轨道 {NO}（不动点 {len(fixed)}, 3-轨道 {len(tri)}）", flush=True)
W=np.zeros((NO,NO,len(nz)),dtype=np.int32)
diff=lambda u,v: ((u[0]-v[0])%3,(u[1]-v[1])%9,(u[2]-v[2])%9)
for i in range(NO):
    for j in range(i,NO):
        for u in orbits[i]:
            for v in orbits[j]:
                z=diff(u,v)
                if z!=(0,0,0): W[i,j,nzidx[z]]+=1
                if i!=j:
                    z2=diff(v,u)
                    if z2!=(0,0,0): W[i,j,nzidx[z2]]+=1
A=np.zeros((NO,NO,len(nz)),dtype=np.float32); Diag=np.zeros((NO,len(nz)),dtype=np.float32)
for i in range(NO):
    Diag[i]=W[i,i]
    for j in range(i+1,NO): A[i,j]=W[i,j]; A[j,i]=W[i,j]
def counts(y): return 0.5*np.einsum('i,ijz,j->z',y,A,y)+y@Diag
def objective(c):
    d=c-60.0; return float(d@d)

rng=random.Random(int(sys.argv[1]) if len(sys.argv)>1 else 1)
LIMIT=float(sys.argv[2]) if len(sys.argv)>2 else 180.0

def init():
    y=np.zeros(NO,dtype=np.float32)
    # 1 个不动点 + 40 个 3-轨道 = 121
    f=rng.choice(fixed); y[f]=1
    for i in rng.sample(tri,40): y[i]=1
    return y,y@np.array([len(o) for o in orbits])
y,sz=init(); c=counts(y); cur=objective(c); best=cur; besty=y.copy()
print(f"初始 |D|={int(sz)}, obj={cur:.0f}", flush=True)
t0=time.time(); T=500.0; iters=0; ok_moves=0
while time.time()-t0<LIMIT:
    iters+=1
    y2=y.copy(); mv=rng.random()
    if mv<0.4:
        # 3 个已选不动点 ↔ 1 个未选 3-轨道
        ch=[i for i in fixed if y2[i]==1]
        if len(ch)<3: continue
        unch=[i for i in tri if y2[i]==0]
        if not unch: continue
        for i in rng.sample(ch,3): y2[i]=0
        y2[rng.choice(unch)]=1
    elif mv<0.8:
        # 1 个已选 3-轨道 ↔ 3 个未选不动点
        ch=[i for i in tri if y2[i]==1]
        unch=[i for i in fixed if y2[i]==0]
        if not ch or len(unch)<3: continue
        y2[rng.choice(ch)]=0
        for i in rng.sample(unch,3): y2[i]=1
    else:
        # 不动点对换
        ch=[i for i in fixed if y2[i]==1]; unch=[i for i in fixed if y2[i]==0]
        if not ch or not unch: continue
        y2[rng.choice(ch)]=0; y2[rng.choice(unch)]=1
    ok_moves+=1
    c2=counts(y2); nc=objective(c2)
    if nc<=cur or rng.random()<np.exp(-(nc-cur)/max(T,1e-9)):
        y,c,cur=y2,c2,nc
        if cur<best:
            best=cur; besty=y2.copy()
            print(f"  [{time.time()-t0:.0f}s] obj={best:.0f} |D|={int(y2@np.array([len(o) for o in orbits]))}", flush=True)
            if best==0:
                D=[e for i in range(NO) if besty[i]==1 for e in orbits[i]]
                print("**FOUND** D =", D, flush=True); break
    T*=0.9995
print(f"结束: iters={iters} (可行移动 {ok_moves}), best obj={best:.0f}, |D|={int(besty@np.array([len(o) for o in orbits]))}", flush=True)
