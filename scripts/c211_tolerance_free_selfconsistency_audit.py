#!/usr/bin/env python3
"""C-211 甲：免容差自洽性审计（三簇）
判据：exists y: F(y)<F(x) and 0<d_S3(x,y)<rho_upper(x)  =>  x 不是局部极小
"""
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
info={0:dict(A=[1,5,11,13],c=0.540247961,R=169),3:dict(A=[2,7,10,15],c=1.218503802,R=225),5:dict(A=[1,3,13,15],c=0.750466653,R=225)}
# rho_upper（C-210 更正版）
rho_up={0:1.465756e-03,3:2.050227e-04,5:1.858471e-03}
# 所有已知候选（census2 的 60 个 + 三簇代表）
rows=json.load(open('/tmp/census2.json'))
known=[np.array(r['x']) for r in rows]+[np.array(cl[i]['x']) for i in (0,3,5)]
print("="*112)
print("C-211 甲：免容差自洽性审计  判据：∃y, F(y)<F(x) 且 0<d_S3(x,y)<ρ_upper(x) ⟹ x 非局部极小")
print("="*112)
res=[]
rng=np.random.default_rng(20260920)
for i,lbl in ((0,"簇 0"),(3,"簇 3"),(5,"簇 5")):
    x=np.array(cl[i]['x']); Fx=F(x); ru=rho_up[i]
    A=info[i]['A']; c=info[i]['c']; R=info[i]['R']
    sv=Sv(x); dA=Fx-min(sv[k-1] for k in A)
    rho_low_q=(c-np.sqrt(max(c*c-2*R*dA,0)))/R       # 二次根
    rho_low_s=dA/c                                    # 简化式（用户建议）
    # (a) 球内随机采样（批量向量化）
    N=400000
    r=ru*rng.random(N)**(1/3)                          # 球内均匀
    u=rng.normal(size=(N,3)); u/=np.linalg.norm(u,axis=1,keepdims=True)
    Y=x+r[:,None]*u
    inside=np.all((Y>=0)&(Y<=np.pi),axis=1)
    Y=Y[inside]; rr=r[inside]
    V=np.full(len(Y),-9.)
    for k in range(1,K+1): V=np.maximum(V, np.cos(k*Y[:,0])+np.cos(k*Y[:,1])+np.cos(k*Y[:,2]))
    jmin=int(np.argmin(V)); Vmin=float(V.min())
    # (b) 已知候选里找球内、值更低的
    cands=[]
    for z in known:
        d=dS3(x,z)
        if 0<d<ru and F(z)<Fx-1e-12: cands.append((F(z),d,z))
    cands.sort(key=lambda t:t[1])
    # (c) 球内多起点局部下降（找更低的谷）
    lows=[]
    for t in range(120):
        s=Y[int(np.argmin(V))].copy() if t==0 else x+ru*rng.random()**(1/3)*rng.normal(size=3)/np.linalg.norm(rng.normal(size=3))
        s=np.clip(s,0,np.pi)
        r2=minimize(F,s,method='Nelder-Mead',options={'xatol':1e-12,'fatol':1e-15,'maxiter':1500})
        lows.append((float(r2.fun), np.asarray(r2.x)%np.pi))
    lows.sort(key=lambda t:t[0])
    low_val=lows[0][0]; low_d=dS3(x,lows[0][1])
    veto = (Vmin < Fx-1e-12) or (low_val < Fx-1e-12 and low_d < ru) or (len(cands)>0)
    print(f"\n{lbl}: F(x)={Fx:.12f}   ρ_upper={ru:.6e}   ρ_lower(二次根)={rho_low_q:.4e}   ρ_lower(δ_A/c)={rho_low_s:.4e}")
    print(f"   δ_A = {dA:.6e}")
    print(f"   (a) 球内采样 {len(Y):,} 点：min F = {Vmin:.12f}   ⟹ Δ = {Vmin-Fx:+.3e}  {'【低于 F(x) ✗ 反例】' if Vmin<Fx-1e-12 else '≥ F(x) ✓'}")
    print(f"       最近采样点距离 = {float(rr[jmin]):.3e}")
    print(f"   (b) 已知候选中球内且值更低者：{len(cands)} 个")
    for v,d,z in cands[:3]: print(f"       F={v:.12f}  ΔF={v-Fx:+.3e}  d_S3={d:.3e}")
    print(f"   (c) 球内 120 起点局部下降：最低 F = {low_val:.12f}  ΔF = {low_val-Fx:+.3e}  距 x = {low_d:.3e}")
    verdict = "❌ 发现反例 ⟹ 非局部极小" if veto else "⭕ 未发现反例 ⟹ 自洽性检查通过（≠证明）"
    print(f"   ⟹ 判定：{verdict}")
    res.append(dict(label=lbl,F=Fx,rho_up=ru,rho_low_q=rho_low_q,rho_low_s=rho_low_s,dA=dA,
                    Vmin=Vmin,near_sample_d=float(rr[jmin]),n_lower_cands=len(cands),
                    low_val=low_val,low_d=low_d,veto=bool(veto)))
print("\n"+"="*112)
print("汇总表（唐先生指定格式）")
print(f"  {'簇':>6} {'F(x)':>14} {'ρ_upper':>12} {'球内 min F':>14} {'ΔF':>11} {'最近候选 y':>26} {'d_S3':>10}  判定")
for r in res:
    y = "—" if not r['veto'] else "见上"
    print(f"  {r['label']:>6} {r['F']:14.10f} {r['rho_up']:12.3e} {r['Vmin']:14.10f} {r['Vmin']-r['F']:+11.3e} {y:>26} {'—':>10}  {'❌ 反例' if r['veto'] else '⭕ 通过'}")
json.dump(res,open('/tmp/c211_audit.json','w'),indent=2)
