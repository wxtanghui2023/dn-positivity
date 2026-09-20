#!/usr/bin/env python3
"""GLOBAL-CENSUS-1：M=3 候选穷尽性搜索（阈值 F<0.78）
流程：低网格布种 + 随机布种 → 多起点精修 → 合并 S3 轨道 → active-set 分类 → 输出 M_cand 清单
"""
import numpy as np, json, itertools
from scipy.optimize import minimize
K=15; D=3
def Sv(x): return np.array([sum(np.cos(k*x[j]) for j in range(D)) for k in range(1,K+1)])
def F(x): return float(Sv(x).max())
PERMS=list(itertools.permutations(range(3)))
def canon(x): return np.sort(np.asarray(x)%np.pi)
def distS3(a,b): return min(float(np.linalg.norm(np.asarray(a)[list(p)]-np.asarray(b))) for p in PERMS)

# ---- 网格 ----
N=60; g=np.linspace(0,np.pi,N+1)[:N]
P=np.stack(np.meshgrid(g,g,g,indexing='ij'),axis=-1).reshape(-1,3)
V=np.full(len(P),-9.)
for k in range(1,K+1): V=np.maximum(V, np.cos(k*P[:,0])+np.cos(k*P[:,1])+np.cos(k*P[:,2]))
sel=np.where(V<0.78)[0]
print(f"[1] 网格 {N}^3={len(P):,}；F<0.78 的格点 = {len(sel):,}；最小值 = {V.min():.9f}", flush=True)

# ---- 布种：低格点(取样) + 随机 ----
rng=np.random.default_rng(20260920)
low=sel[np.argsort(V[sel])][:1200]
seeds=[P[i] for i in low]+[rng.uniform(0,np.pi,3) for _ in range(800)]
print(f"[2] 多起点精修：{len(seeds)} 起点（maxiter=1000）…", flush=True)
found=[]
for i,s in enumerate(seeds):
    r=minimize(F,s,method='Nelder-Mead',options={'xatol':1e-11,'fatol':1e-14,'maxiter':1000})
    found.append((float(r.fun), np.asarray(r.x)%np.pi))
    if i%400==0: print(f"    …{i}/{len(seeds)}", flush=True)
found.sort(key=lambda t:t[0])

# ---- 合并 S3 轨道 ----
orbits=[]
for v,x in found:
    xs=canon(x); hit=False
    for o in orbits:
        if abs(o['v']-v)<1e-7 and distS3(o['x'],xs)<3e-3: o['n']+=1; hit=True; break
    if not hit: orbits.append(dict(v=v,x=xs,n=1))
orbits.sort(key=lambda o:o['v'])
print(f"[3] 合并后轨道数 = {len(orbits)}（阈值 F<0.78 内共 {sum(1 for o in orbits if o['v']<0.78)} 个）", flush=True)

# ---- 分类 ----
def classify(x):
    sv=Sv(x); mx=sv.max(); A=[k for k in range(1,K+1) if mx-sv[k-1]<1e-5]
    G=np.array([[-k*np.sin(k*x[j]) for j in range(D)] for k in A])
    Dm=np.array([G[j]-G[0] for j in range(1,len(A))]) if len(A)>1 else np.zeros((1,3))
    rk=int(np.linalg.matrix_rank(Dm,tol=1e-8)) if len(A)>1 else 0
    lam_ok=False; c=None
    if len(A)>=4:
        try:
            Mx=np.vstack([G.T,np.ones(len(A))]); lam=np.linalg.solve(Mx,np.r_[np.zeros(3),1.0])
            lam_ok=bool(lam.min()>1e-9)
        except Exception: pass
        # facet 法求 c
        best=(1e9,None)
        for comb in itertools.combinations(range(len(A)),3):
            rest=[j for j in range(len(A)) if j not in comb]
            v1,v2,v3=G[comb[0]],G[comb[1]],G[comb[2]]
            nrm=np.cross(v2-v1,v3-v1); nn=np.linalg.norm(nrm)
            if nn<1e-9: continue
            sg=[float(np.dot(nrm,G[j]-v1)) for j in rest]
            if not (all(t>0 for t in sg) or all(t<0 for t in sg)): continue
            d=abs(float(np.dot(nrm,v1)))/nn
            if d<best[0]: best=(d,nrm/nn)
        if best[1] is not None: c=best[0]
    r=minimize(F,x,method='Nelder-Mead',options={'xatol':1e-13,'fatol':1e-16,'maxiter':3000})
    drop=F(x)-r.fun
    return A,rk,lam_ok,c,drop
print(f"\n[4] 分类（F<0.78 全部 + 已知伪簇对照）")
print(f"  {'#':>3} {'F':>13} {'n':>4} | {'|A|':>3} {'rank':>4} {'λ>0':>5} {'c':>11} {'下降':>10} | 类型")
rows=[]
for i,o in enumerate(orbits):
    if o['v']>=0.78: continue
    A,rk,lam_ok,c,drop=classify(o['x'])
    typ = ("A 孤立非退化 ✓" if (len(A)==4 and rk==3 and lam_ok and c and c>0) else
           "真极小(非A)" if drop<1e-10 else "伪停点")
    print(f"  {i:3d} {o['v']:13.10f} {o['n']:4d} | {len(A):3d} {rk:4d} {str(lam_ok):>5} "
          f"{(f'{c:.9f}' if c is not None else '   —   '):>11} {drop:10.2e} | {typ}")
    rows.append(dict(idx=i,F=o['v'],n=o['n'],A=A,rank=rk,lam_pos=lam_ok,c=c,drop=drop,type=typ,
                     x=[float(t) for t in o['x']]))
json.dump(rows,open('/tmp/census1.json','w'),indent=2)
print(f"\n[5] M_cand 清单已写 /tmp/census1.json（{len(rows)} 条）")
