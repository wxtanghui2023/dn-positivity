#!/usr/bin/env python3
"""C-211b：先高精度重收敛代表点，再重跑免容差自洽性审计"""
import json, numpy as np, itertools
from scipy.optimize import minimize
K=15; D=3
def Sv(x): return np.array([sum(np.cos(k*x[j]) for j in range(D)) for k in range(1,K+1)])
def F(x): return float(Sv(x).max())
PERMS=list(itertools.permutations(range(3)))
def dS3(a,b):
    a=np.asarray(a); b=np.asarray(b)
    return min(float(np.linalg.norm(a[list(p)]-b)) for p in PERMS)
cl=json.load(open('/tmp/t13aeq_clusters.json'))['clusters']
rho_up={0:1.465756e-03,3:2.050227e-04,5:1.858471e-03}
rng=np.random.default_rng(4242)
print("="*110); print("C-211b：重收敛 + 重审计"); print("="*110)
for i,lbl in ((0,"簇 0"),(3,"簇 3"),(5,"簇 5")):
    x=np.array(cl[i]['x']); ru=rho_up[i]
    print(f"\n{lbl}: 初始 F = {F(x):.15f}")
    best=(F(x), x.copy())
    for t in range(250):
        sc = 10**(-7 + 2.5*(t%9)/9)                     # 抖动尺度 1e-7 → 1e-4.?
        s = x + rng.normal(scale=sc, size=3)
        s = np.clip(s, 0, np.pi)
        r = minimize(F, s, method='Nelder-Mead', options={'xatol':1e-15,'fatol':1e-18,'maxiter':6000})
        if r.fun < best[0]: best=(float(r.fun), np.asarray(r.x)%np.pi)
    xb=best[1]; Fb=best[0]
    print(f"   重收敛后 F* = {Fb:.15f}   改进 = {Fb-F(x):+.3e}   位移 = {dS3(xb,x):.3e}")
    # 重跑自洽性审计（在 xb 的球内）
    N=500000
    r=ru*rng.random(N)**(1/3); u=rng.normal(size=(N,3)); u/=np.linalg.norm(u,axis=1,keepdims=True)
    Y=xb+r[:,None]*u; m=np.all((Y>=0)&(Y<=np.pi),axis=1); Y=Y[m]; rr=r[m]
    V=np.full(len(Y),-9.)
    for k in range(1,K+1): V=np.maximum(V, np.cos(k*Y[:,0])+np.cos(k*Y[:,1])+np.cos(k*Y[:,2]))
    jm=int(np.argmin(V)); Vmin=float(V.min())
    drop=Vmin-Fb; dnear=float(rr[jm])
    # 从 30 个最低采样点做局部下降（找更低谷）
    idx=np.argsort(V)[:30]; lowbest=(1e9,None)
    for j in idx:
        r2=minimize(F,Y[j],method='Nelder-Mead',options={'xatol':1e-14,'fatol':1e-17,'maxiter':4000})
        if r2.fun<lowbest[0]: lowbest=(float(r2.fun), np.asarray(r2.x)%np.pi)
    lv,ly=lowbest; ld=dS3(xb,ly)
    print(f"   球内采样 {len(Y):,} 点：min F = {Vmin:.15f}  ΔF = {drop:+.3e}  最近点距离 = {dnear:.3e}")
    print(f"   30 个最低点再局部下降：最低 F = {lv:.15f}  ΔF = {lv-Fb:+.3e}  距 x* = {ld:.3e}")
    if lv < Fb-1e-11: print(f"   ⟹ ❌ 否决（跌幅 {Fb-lv:.3e} ≫ 噪声，距离 {ld:.3e}）")
    elif lv < Fb-1e-13: print(f"   ⟹ ⚠️ 仅噪声级下降（{Fb-lv:.3e}）⟹ 视为收敛残差 ✓")
    else: print(f"   ⟹ ⭕ 未发现更低点（最佳 = 自身）⟹ 自洽性通过 ✓")
