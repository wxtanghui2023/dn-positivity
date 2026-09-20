#!/usr/bin/env python3
"""D-A（甲第一刀）：阻尼 M=3 的 candidate / active-set census
定义（沿用已注册，不改目标函数）：
  F(r2,r3,φ1,φ2,φ3) = max_{1<=k<=15}[ cos(kφ1) + r2^k cos(kφ2) + r3^k cos(kφ3) ]
  C_3 = inf 于 [0,1]^2 x [0,π]^3
本刀只做 census：多起点定位、簇归并、active set（含容差扫描）、正权 KKT、c_X、R、ρ_iso
硬门槛：active-set/KKT 结构【不稳定】⟹ 立即 STOP（不进 D-B/C）
"""
import numpy as np, json
from scipy.optimize import minimize
K=15; PI=np.pi
def S(k,x):
    r2,r3,p1,p2,p3=x
    return np.cos(k*p1)+r2**k*np.cos(k*p2)+r3**k*np.cos(k*p3)
def F(x):
    return max(S(k,x) for k in range(1,K+1))
def Sall(x): return np.array([S(k,x) for k in range(1,K+1)])
def grad(k,x):
    r2,r3,p1,p2,p3=x
    return np.array([ k*r2**(k-1)*np.cos(k*p2),          # ∂/∂r2
                      k*r3**(k-1)*np.cos(k*p3),          # ∂/∂r3
                     -k*np.sin(k*p1),                    # ∂/∂φ1
                     -k*r2**k*np.sin(k*p2),              # ∂/∂φ2
                     -k*r3**k*np.sin(k*p3) ])            # ∂/∂φ3
def canon(x):
    y=x.copy()
    if (y[0],y[2])>(y[1],y[3]): y[[0,1]]=y[[1,0]]; y[[2,3]]=y[[3,2]]
    return y
def clip(x):
    y=np.array(x,float); y[0]=min(max(y[0],0),1); y[1]=min(max(y[1],0),1)
    y[2:]=(y[2:]+PI/2)%PI-PI/2
    return y
print("="*104); print("D-A：阻尼 M=3 candidate/active-set census"); print("="*104)
rng=np.random.default_rng(20260920)
known=np.array([0.7905132461,0.8302071370,0.1091101624*PI,0.8206636560*PI,0.4617193264*PI])
best_pool=[(F(known),known,"known x**")]
for t in range(600):
    if t<200: x0=np.array([rng.uniform(0,1),rng.uniform(0,1),rng.uniform(0,PI),rng.uniform(0,PI),rng.uniform(0,PI)])
    elif t<400: x0=np.array([rng.uniform(0.6,1),rng.uniform(0.6,1)]+list(rng.uniform(0,PI,3)))
    else: x0=known+rng.normal(0,[0.05,0.05,0.15,0.15,0.15])
    res=minimize(F,clip(x0),method='Nelder-Mead',options=dict(maxiter=1200,xatol=1e-11,fatol=1e-13))
    x=clip(res.x); best_pool.append((F(x),x,f"start{t}"))
print(f"① 多起点：600+1 次 NM；函数评估最低 5 个（原始值，未归并）：")
for v,x,tag in sorted(best_pool,key=lambda z:z[0])[:5]:
    print(f"    F={v:.15f}  x=({x[0]:.7f},{x[1]:.7f},{x[2]/PI:.7f}π,{x[3]/PI:.7f}π,{x[4]/PI:.7f}π)  [{tag}]")
# 簇归并（按 canon 后的 5 维距离）
clusters=[]
for v,x,tag in sorted(best_pool,key=lambda z:z[0]):
    c=canon(x); placed=False
    for cl in clusters:
        if np.linalg.norm(c-cl['c'])<=2e-3: cl['n']+=1; placed=True; break
    if not placed: clusters.append(dict(c=c,v=v,n=1,tag=tag))
print(f"\n② 归并（canon 后 5 维距离 ≤2e-3）：簇数 = {len(clusters)}")
print(f"   {'F':>18} {'计数':>5}  {'(r2,r3)':>18}  {'φ/π':>34}")
for cl in clusters[:6]:
    c=cl['c']
    print(f"   {cl['v']:18.15f} {cl['n']:5d}  ({c[0]:.7f},{c[1]:.7f})  ({c[2]/PI:.7f},{c[3]/PI:.7f},{c[4]/PI:.7f})")
low=clusters[0]; x0=low['c']
print(f"\n③ 最低候选：F={low['v']:.15f}   x=({x0[0]:.10f},{x0[1]:.10f},{x0[2]/PI:.10f}π,{x0[3]/PI:.10f}π,{x0[4]/PI:.10f}π)")
print(f"   距 bracket 上端 {0.373092075762:.15f} 之差 = {0.373092075762-low['v']:+.3e}")
print(f"   距 bracket 下端 {0.3730918:.7f} 之差 = {low['v']-0.3730918:+.3e}")
SV=Sall(x0); order=np.argsort(-SV)
print(f"\n④ active-set 容差扫描（硬门槛用）：")
verdicts=[]
for tol in (1e-12,1e-10,1e-9,1e-8,1e-7,1e-6,1e-5,1e-4,1e-3):
    A=[int(k+1) for k in range(K) if SV[k]>=SV.max()-tol]
    verdicts.append((tol,A))
    print(f"   tol={tol:.0e}:  |A|={len(A):2d}   A={A}   第 |A|+1 项 gap={SV.max()-SV[order[len(A)]]:.3e}")
lens=set(len(a) for _,a in verdicts); Aset=set(tuple(a) for _,a in verdicts)
print(f"\n⑤ ⭐ 稳定性判定：不同 tol 下 |A| 取值集合 = {sorted(lens)}；A 取值个数 = {len(Aset)}")
stable = (len(lens)==1)
print(f"   ⟹ {'稳定 ✓（可进 D-B）' if stable else '⚠️ 不稳定 ⟹ 按硬门槛【立即 STOP】✗（不进 D-B/C）'}")
# 对最稳定/最可能的那组做 KKT / c / R
A=[int(k+1) for k in range(K) if SV[k]>=SV.max()-1e-6]
G=np.array([grad(k,x0) for k in A])
print(f"\n⑥ 候选 A（tol=1e-6）={A}，|A|={len(A)}（5 变量 ⟹ 单纯形签名应为 |A|=6）")
print(f"   λ 求解（最小二乘 + 正性检查）：")
lw,res_,rk,sv_=np.linalg.lstsq(G.T,np.zeros(5),rcond=None)
lw=np.abs(lw); lw=lw/lw.sum() if lw.sum()>0 else lw
print(f"     λ≈{np.round(lw,6)}  min={lw.min():.3e}  残差 ‖Σλ∇S_k‖={np.linalg.norm(G.T@lw):.3e}")
# 5 维 Hessian 范数
def hess(k,x):
    r2,r3,p1,p2,p3=x; H=np.zeros((5,5))
    H[0,0]= k*(k-1)*r2**(k-2)*np.cos(k*p2); H[1,1]= k*(k-1)*r3**(k-2)*np.cos(k*p3)
    H[2,2]=-k*k*np.cos(k*p1); H[3,3]=-k*k*r2**k*np.cos(k*p2); H[4,4]=-k*k*r3**k*np.cos(k*p3)
    H[0,3]=H[3,0]=-k*k*r2**(k-1)*np.sin(k*p2); H[1,4]=H[4,1]=-k*k*r3**(k-1)*np.sin(k*p3)
    return H
Rn={k:np.linalg.norm(hess(k,x0),2) for k in A}
R=max(Rn.values())
print(f"\n⑦ 二阶余项常数 R = max_(k∈A)‖∇²S_k‖₂ = {R:.6f}  （最大者 k={max(Rn,key=Rn.get)}）")
print(f"   各 k：{ {k:round(v,3) for k,v in Rn.items()} }")
json.dump(dict(low_F=low['v'], low_x=list(x0), nclusters=len(clusters),
               active_verdicts=[[t,a] for t,a in verdicts], stable=bool(stable),
               A_tol1e6=A, lam=list(map(float,lw)), R=float(R), Rn={str(k):float(v) for k,v in Rn.items()}),
          open('/tmp/dA_census.json','w'), indent=1)
