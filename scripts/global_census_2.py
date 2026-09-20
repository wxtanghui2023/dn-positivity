#!/usr/bin/env python3
"""GLOBAL-CENSUS-2：更大规模 + 用 c(KKT/covering) 判据（不用 Nelder-Mead 下降检验）
   另含：x0 盆地半径直接估计
"""
import numpy as np, json, itertools
from scipy.optimize import minimize
K=15; D=3
def Sv(x): return np.array([sum(np.cos(k*x[j]) for j in range(D)) for k in range(1,K+1)])
def F(x): return float(Sv(x).max())
PERMS=list(itertools.permutations(range(3)))
def canon(x): return np.sort(np.asarray(x)%np.pi)
def distS3(a,b): return min(float(np.linalg.norm(np.asarray(a)[list(p)]-np.asarray(b))) for p in PERMS)

def cval(A,G):
    """c = min_|u|=1 max_k <g_k,u>  (facet 法：以0为心最大内切球半径)"""
    if len(A)<D+1: return None
    best=1e18
    for comb in itertools.combinations(range(len(A)),3):
        rest=[j for j in range(len(A)) if j not in comb]
        v1,v2,v3=G[comb[0]],G[comb[1]],G[comb[2]]
        nrm=np.cross(v2-v1,v3-v1); nn=np.linalg.norm(nrm)
        if nn<1e-10: continue
        sg=[float(np.dot(nrm,G[j]-v1)) for j in rest]
        if not (all(t>0 for t in sg) or all(t<0 for t in sg)): continue
        d=abs(float(np.dot(nrm,v1)))/nn
        best=min(best,d)
    return None if best>1e17 else best

def classify(x):
    sv=Sv(x); mx=sv.max(); A=[k for k in range(1,K+1) if mx-sv[k-1]<1e-5]
    G=np.array([[-k*np.sin(k*x[j]) for j in range(D)] for k in A])
    c=cval(A,G)
    rk=int(np.linalg.matrix_rank(np.array([G[j]-G[0] for j in range(1,len(A))]),tol=1e-8)) if len(A)>1 else 0
    return A,rk,c,mx

# ---------- (a) x0 盆地半径估计 ----------
cl=json.load(open('/tmp/t13aeq_clusters.json'))['clusters']
x0=np.array(cl[0]['x'])                      # 簇 0（当前最佳）
mirror=np.array([x0[2],x0[1],x0[0]])         # σ: (r2,r3,φ2,φ3) 对称；此处取排序前的镜像近似
rng=np.random.default_rng(77)
print("[a] x0 盆地半径估计（起点均匀落在半径 r 的球内，看多少落入 F≈0.7640811 的谷）")
print(f"   x0 = {np.round(x0/np.pi,8)} (φ/π)")
for r in (3e-3, 1e-2, 3e-2, 0.1, 0.3):
    hit=0; N=400
    for _ in range(N):
        d=rng.normal(size=3); d/=np.linalg.norm(d); s=x0+r*rng.random()**(1/3)*d
        s=np.clip(s,0,np.pi)
        rr=minimize(F,s,method='Nelder-Mead',options={'xatol':1e-11,'fatol':1e-14,'maxiter':1200})
        if abs(rr.fun-0.7640811032)<1e-6: hit+=1
    print(f"   r={r:.1e}: 落入比例 = {hit}/{N} = {hit/N:.3f}")

# ---------- (b) 大规模 census ----------
print("\n[b] GLOBAL-CENSUS-2：3000 随机起点（c 判据分类）", flush=True)
seeds=[np.random.default_rng(1000+i).uniform(0,np.pi,3) for i in range(3000)]
found=[]
for i,s in enumerate(seeds):
    r=minimize(F,s,method='Nelder-Mead',options={'xatol':1e-11,'fatol':1e-14,'maxiter':1000})
    found.append((float(r.fun), np.asarray(r.x)%np.pi))
    if i%600==0: print(f"    …{i}/{len(seeds)}", flush=True)
found.sort(key=lambda t:t[0])
orbits=[]
for v,x in found:
    xs=canon(x); hit=False
    for o in orbits:
        if abs(o['v']-v)<1e-6 and distS3(o['x'],xs)<3e-3: o['n']+=1; hit=True; break
    if not hit: orbits.append(dict(v=v,x=xs,n=1))
sub=[o for o in orbits if o['v']<0.78]
print(f"\n[c] F<0.78 的轨道 {len(sub)} 个；按 c 判据分类：")
print(f"  {'#':>3} {'F':>13} {'n':>4} | {'A':22s} | {'|A|':>3} {'rank':>4} {'c':>12} | 判定")
out=[]
for i,o in enumerate(sorted(sub,key=lambda o:o['v'])):
    A,rk,c,mx=classify(o['x'])
    verdict = (f"A. 孤立非退化 ✓ (c>0)" if (len(A)>=D+1 and c and c>0 and rk==D) else
               f"c>0 但 rank={rk} (退化?) ⚠️" if (c and c>0) else
               f"非 KKT (c={('%.3e'%c) if c is not None else 'None'}≤0) ⟹ 非极小 ✗")
    print(f"  {i:3d} {o['v']:13.10f} {o['n']:4d} | {str(A):22s} | {len(A):3d} {rk:4d} "
          f"{(f'{c:.9f}' if c is not None else '    —    '):>12} | {verdict}")
    out.append(dict(F=o['v'],n=o['n'],A=A,rank=rk,c=c,x=[float(t) for t in o['x']],verdict=verdict))
json.dump(out,open('/tmp/census2.json','w'),indent=2)
A_orbits=[o for o in out if o['c'] and o['c']>0 and o['rank']==D]
print(f"\n[d] ⟹ 本刀 Type-A 轨道数 = {len(A_orbits)}；值 = {[round(o['F'],10) for o in A_orbits]}")
print(f"    对照已知：0.7640811032 / 0.7755338917 / 0.7768817151")
