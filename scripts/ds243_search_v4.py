#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""v4 = v3 + 硬约束: 三个 H-陪集(按 Z_3 分量)尺寸恰为 {36,40,45} + σ-不变
   移动: 陪集内轨道互换（自动保值）; 目标 Σ_z (c_z − 60)² = 0
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
coset_of=np.array([o[0][0] for o in orbits])   # 元素第一分量 = 陪集标签
byc={c:[i for i in range(NO) if coset_of[i]==c] for c in range(3)}
print(f"轨道 {NO}; 各陪集轨道数 = {{{', '.join(f'{c}:{len(byc[c])}' for c in range(3))}}}", flush=True)
for c in range(3):
    ss=[sizes[i] for i in byc[c]]
    print(f"  陪集{c}: 轨道大小集合 {sorted(set(ss))}, 总元素 {sum(ss)}", flush=True)

nz=[z for z in G if z!=(0,0,0)]; nzidx={z:t for t,z in enumerate(nz)}
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

TARGET={0:36,1:40,2:45}
rng=random.Random(int(sys.argv[1]) if len(sys.argv)>1 else 1)
LIMIT=float(sys.argv[2]) if len(sys.argv)>2 else 240.0

def init():
    y=np.zeros(NO,dtype=np.float32)
    for c in range(3):
        need=TARGET[c]; pool=byc[c][:]; rng.shuffle(pool)
        for i in pool:
            if need>=sizes[i]: y[i]=1; need-=sizes[i]
        if need!=0: return None
    return y
y=None
for _ in range(200):
    y=init()
    if y is not None and int(y@np.array([len(o) for o in orbits]))==121: break
print(f"初始 |D| = {int(y@np.array([len(o) for o in orbits]))}; 各陪集 = {[int(sum(sizes[i] for i in byc[c] if y[i]==1)) for c in range(3)]}", flush=True)
c=counts(y); cur=objective(c); best=cur; besty=y.copy()
t0=time.time(); T=500.0; iters=0; okm=0
while time.time()-t0<LIMIT:
    iters+=1
    cc=rng.randrange(3)
    ch=[i for i in byc[cc] if y[i]==1]; un=[i for i in byc[cc] if y[i]==0]
    if not ch or not un: continue
    # 等尺寸互换（保陪集尺寸）
    a=rng.choice(ch); cand=[j for j in un if sizes[j]==sizes[a]]
    if not cand: continue
    b=rng.choice(cand)
    y2=y.copy(); y2[a]=0; y2[b]=1; okm+=1
    c2=counts(y2); nc=objective(c2)
    if nc<=cur or rng.random()<np.exp(-(nc-cur)/max(T,1e-9)):
        y,c,cur=y2,c2,nc
        if cur<best:
            best=cur; besty=y2.copy()
            print(f"  [{time.time()-t0:.0f}s] obj={best:.0f} 陪集={[int(sum(sizes[i] for i in byc[cc2] if y2[i]==1)) for cc2 in range(3)]}", flush=True)
            if best==0:
                D=[e for i in range(NO) if besty[i]==1 for e in orbits[i]]
                print("**FOUND** |D| =",len(D), flush=True); print("D =",D, flush=True); break
    T*=0.9995
print(f"结束: iters={iters} (可行互换 {okm}), best obj={best:.0f}, 各陪集={[int(sum(sizes[i] for i in byc[cc2] if besty[i]==1)) for cc2 in range(3)]}", flush=True)
