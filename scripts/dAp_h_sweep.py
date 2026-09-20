#!/usr/bin/env python3
"""D-A′ 补充：Jacobian 中心差分的 h 三档稳定性检查（唐先生 2026-09-20 15:00 指定）
h ∈ {1e-20, 1e-25, 1e-30}；比较 Newton 步与解；若稳定才可继续（最终认证仍需解析/区间 Jacobian）
"""
import mpmath as mp, numpy as np, json
mp.mp.dps=60
K=15; A6=[15,1,3,5,2,4]
def Sv(k,x):
    r2,r3,p1,p2,p3=x
    return mp.cos(k*p1)+r2**k*mp.cos(k*p2)+r3**k*mp.cos(k*p3)
def gv(k,x):
    r2,r3,p1,p2,p3=x
    return [k*r2**(k-1)*mp.cos(k*p2), k*r3**(k-1)*mp.cos(k*p3),
            -k*mp.sin(k*p1), -k*r2**k*mp.sin(k*p2), -k*r3**k*mp.sin(k*p3)]
def Gsys(z):
    xx=z[:5]; ll=z[5:]
    out=[sum(ll[i]*gv(A6[i],xx)[j] for i in range(6)) for j in range(5)]
    S0=Sv(A6[0],xx)
    out+=[S0-Sv(A6[i],xx) for i in range(1,6)]
    out+=[sum(ll)-1]
    return out
xs=[0.790513233950366238,0.83020729481457293,0.109110164828623089*np.pi,
    0.820663709520206675*np.pi,0.461719371018610243*np.pi]
lams=[0.1492699829,0.2000536555,0.1655100171,0.1118601223,0.1784876011,0.1948186212]
z0=[mp.mpf(repr(t)) for t in xs]+[mp.mpf(repr(t)) for t in lams]
print("="*96); print("D-A′ 补充：中心差分 h 三档稳定性检查"); print("="*96)
sols={}
for h in (mp.mpf('1e-20'), mp.mpf('1e-25'), mp.mpf('1e-30')):
    z=z0[:]; first=None; iters=0
    for it in range(30):
        Gz=mp.matrix(Gsys(z)); nrm=max(abs(t) for t in Gz)
        if nrm<mp.mpf('1e-45'): break
        J=mp.matrix(11,11)
        for j in range(11):
            zp=z[:]; zp[j]+=h; zm=z[:]; zm[j]-=h
            gp=Gsys(zp); gm=Gsys(zm)
            for i in range(11): J[i,j]=(gp[i]-gm[i])/(2*h)
        dz=mp.lu_solve(J,-Gz)
        if first is None: first=[dz[i] for i in range(11)]
        z=[z[i]+dz[i] for i in range(11)]; iters=it+1
    sols[str(h)]=dict(z=z, iters=iters, resid=max(abs(t) for t in Gsys(z)), first=first)
    print(f"\nh={mp.nstr(h,3)}：{iters} 步收敛，末残差={mp.nstr(sols[str(h)]['resid'],5)}")
    print(f"   首步 dz(前 5) = {[mp.nstr(t,12) for t in first[:5]]}")
    print(f"   解 x = ({mp.nstr(z[0],20)}, {mp.nstr(z[1],20)}, {mp.nstr(z[2]/mp.pi,20)}π, {mp.nstr(z[3]/mp.pi,20)}π, {mp.nstr(z[4]/mp.pi,20)}π)")
    print(f"   λ = {[mp.nstr(t,12) for t in z[5:]]}  min={mp.nstr(min(z[5:]),8)}")
ks=list(sols.keys())
key25=[k for k in ks if '25' in k][0]
print("\n" + "="*96)
print("【稳定性判定】三档解之间的最大偏差：")
for i in range(11):
    vals=[sols[k]['z'][i] for k in ks]
    spread=max(vals)-min(vals)
    print(f"   z[{i}] 三档跨度 = {mp.nstr(spread,6)}")
print("\n【首步 dz 的三档跨度】（Jacobian 质量的敏感指标）：")
for i in range(11):
    vals=[sols[k]['first'][i] for k in ks]
    print(f"   dz[{i}] 跨度 = {mp.nstr(max(vals)-min(vals),6)}")
# F 值
xsol=sols[key25]['z']
F=mp.mpf(0)
best=max(Sv(k,xsol[:5]) for k in range(1,K+1))
print(f"\n【解处 F】= {mp.nstr(best,25)}")
print(f"   bracket 检查：0.3730918 ≤ F ≤ 0.373092075762 ⟹ {mp.mpf('0.3730918')<=best<=mp.mpf('0.373092075762')}")
gaps={k:best-Sv(k,xsol[:5]) for k in range(1,K+1)}
print(f"   六分支 Δ（应 ~1e-50）：" + ", ".join(f"k={k}:{mp.nstr(gaps[k],4)}" for k in A6))
print(f"   外部最小 Δ（非 A6）：min = {mp.nstr(min(gaps[k] for k in range(1,K+1) if k not in A6),8)}")
json.dump(dict(h_sols={k:dict(iters=v['iters'], resid=mp.nstr(v['resid'],8),
                              x=[mp.nstr(t,22) for t in v['z'][:5]],
                              lam=[mp.nstr(t,14) for t in v['z'][5:]]) for k,v in sols.items()},
               F=mp.nstr(best,25), gaps={str(k):mp.nstr(gaps[k],8) for k in range(1,K+1)}),
          open('/tmp/dAp_hsweep.json','w'), indent=1)
