#!/usr/bin/env python3
"""D-A′ 收敛审计（甲）：① x* 处 15 个 S_k 的完整 gap spectrum（高精度）
② 真 KKT 可行性（G_A^T λ=0, 1^T λ=1, λ≥0，非零齐次解）③ 用【不预设 tie】的方式推高精度候选：
   以近-active 假设做 11×11 KKT Newton（11 未知：5 变量 + 6 λ；11 方程：5 梯度 + 5 tie + 1 归一化），
   然后在解处【独立复核】exact argmax 与 gap spectrum —— 决定"六分支近簇"是真结构还是未收敛
"""
import mpmath as mp, numpy as np, json, itertools
from scipy.optimize import linprog
mp.mp.dps=60
K=15; PI=np.pi
def Sv(k,x):
    r2,r3,p1,p2,p3=x
    return mp.cos(k*p1)+r2**k*mp.cos(k*p2)+r3**k*mp.cos(k*p3)
def gv(k,x):
    r2,r3,p1,p2,p3=x
    return [k*r2**(k-1)*mp.cos(k*p2), k*r3**(k-1)*mp.cos(k*p3),
            -k*mp.sin(k*p1), -k*r2**k*mp.sin(k*p2), -k*r3**k*mp.sin(k*p3)]
xs=np.array([0.7905132461,0.8302071370,0.1091101624*PI,0.8206636560*PI,0.4617193264*PI])
x=[mp.mpf(repr(float(t))) for t in xs]
print("="*100); print("D-A′：收敛审计（不预设 tie）"); print("="*100)
print(f"起点 x* = ({xs[0]:.10f}, {xs[1]:.10f}, {xs[2]/PI:.10f}π, {xs[3]/PI:.10f}π, {xs[4]/PI:.10f}π)")
# ① gap spectrum at x*
vals={k:Sv(k,x) for k in range(1,K+1)}
mx=max(vals.values()); am=[k for k in range(1,K+1) if vals[k]==mx]
print(f"\n① x* 处 gap spectrum（Δ_k = S_max − S_k，dps={mp.mp.dps}）：")
for k in sorted(range(1,K+1), key=lambda t:-vals[t]):
    d=mx-vals[k]
    mark=" ← argmax (exact)" if vals[k]==mx else ""
    print(f"   k={k:2d}  S_k={mp.nstr(vals[k],25)}   Δ_k={mp.nstr(d,6) if d>0 else '0'}{mark}")
print(f"   exact argmax A_exact = {am}")
order=sorted(range(1,K+1), key=lambda t:-vals[t])
print(f"   Δ 谱（降序）：" + ", ".join(mp.nstr(mx-vals[k],4) for k in order[:9]))
# ② 真 KKT 可行性（float 层，随后高精度复核）
A=[int(t) for t in order[:6]]
Gn=np.array([[float(t) for t in gv(k,x)] for k in A])
print(f"\n② 真 KKT feasibility（假设 A={A}，|A|=6）：")
res=linprog(c=np.zeros(len(A)), A_eq=np.vstack([np.ones((1,len(A)))]), b_eq=np.array([1.0]),
            bounds=[(0,None)]*len(A), method='highs')  # 仅确认可行域
# 真正要的是 G^T λ = 0 且 Σλ=1、λ≥0 ⟹ 用约束最小二乘
from scipy.optimize import minimize as _mn
def obj(l): return float(np.linalg.norm(Gn.T@l))
cons=[dict(type='eq',fun=lambda l: l.sum()-1.0)]
bnds=[(0,1)]*len(A)
best=None
for t in range(60):
    l0=np.random.default_rng(1000+t).dirichlet(np.ones(len(A)))
    r=_mn(obj,l0,method='SLSQP',bounds=bnds,constraints=cons,options=dict(maxiter=800,ftol=1e-16))
    if r.success and (best is None or r.fun<best.fun): best=r
if best is not None:
    lam=best.x; resn=obj(lam)
    print(f"   λ = {np.round(lam,8)}   min λ = {lam.min():.3e}   ‖G^Tλ‖ = {resn:.3e}")
    print(f"   ⟹ {'λ>0 且残差小 ✓（KKT 可行，结构自洽）' if lam.min()>1e-6 and resn<1e-8 else '⚠️ 未达 KKT 可行（残差或正性不足）'}")
else:
    lam=None; print("   ⚠️ SLSQP 未找到可行 λ")
# ③ 11×11 KKT Newton（dps=60），A 固定为 {1,2,3,4,5,15} 形式（= order[:6]）
A6=[int(t) for t in order[:6]]
print(f"\n③ 11×11 KKT Newton（A={A6}；不预设其正确性，解后独立复核）：")
z0=[x[j] for j in range(5)]+[mp.mpf(repr(float(t))) for t in (lam if lam is not None else np.ones(6)/6)]
def Gsys(z):
    xx=z[:5]; ll=z[5:]
    out=[sum(ll[i]*gv(A6[i],xx)[j] for i in range(6)) for j in range(5)]
    S0=Sv(A6[0],xx)
    out+= [S0-Sv(A6[i],xx) for i in range(1,6)]
    out+= [sum(ll)-1]
    return out
z=z0[:]
for it in range(40):
    Gz=mp.matrix(Gsys(z)); nrm=max(abs(t) for t in Gz)
    if nrm<mp.mpf('1e-45'): print(f"   收敛 it={it}  残差={mp.nstr(nrm,5)}"); break
    J=mp.matrix(11,11)
    h=mp.mpf('1e-25')
    for j in range(11):
        zp=z[:]; zp[j]+=h; zm=z[:]; zm[j]-=h
        gp=Gsys(zp); gm=Gsys(zm)
        for i in range(11): J[i,j]=(gp[i]-gm[i])/(2*h)
    try: dz=mp.lu_solve(J,-Gz)
    except Exception as e: print("   求解失败：",e); break
    z=[z[i]+dz[i] for i in range(11)]
    if it==39: print(f"   未收敛，残差={mp.nstr(nrm,5)}")
    if it%5==0: print(f"   it={it:2d} 残差={mp.nstr(nrm,6)}")
xx=z[:5]; ll=z[5:]
print(f"   解后 x = ({mp.nstr(xx[0],18)}, {mp.nstr(xx[1],18)}, {mp.nstr(xx[2]/mp.pi,18)}π, {mp.nstr(xx[3]/mp.pi,18)}π, {mp.nstr(xx[4]/mp.pi,18)}π)")
print(f"   λ = {[mp.nstr(t,10) for t in ll]}   min λ = {mp.nstr(min(ll),8)}")
print(f"\n④ ⭐ 解处独立复核（不预设 tie）：")
vals2={k:Sv(k,xx) for k in range(1,K+1)}
mx2=max(vals2.values()); am2=[k for k in range(1,K+1) if vals2[k]==mx2]
for k in sorted(range(1,K+1), key=lambda t:-vals2[t])[:9]:
    d=mx2-vals2[k]
    print(f"   k={k:2d}  S_k={mp.nstr(vals2[k],25)}   Δ_k={mp.nstr(d,6) if d>0 else '0'}")
print(f"   exact argmax at solution = {am2}   （|A_exact| = {len(am2)}）")
print(f"   F(x) at solution = {mp.nstr(mx2,25)}")
print(f"   ⟹ {'六分支【精确并列】✓（真 nonsmooth 结构）' if len(am2)==6 else f'仅 {len(am2)} 个精确并列 ⟹ 结构与假设不同 ⚠️'}")
json.dump(dict(x_star_gap={str(k):mp.nstr(mx-vals[k],10) for k in range(1,K+1)},
               A_exact_star=am, A6=A6, lam=[float(t) for t in (lam if lam is not None else [])],
               x_solved=[mp.nstr(t,20) for t in xx], lam_solved=[mp.nstr(t,12) for t in ll],
               A_exact_solved=am2, F_solved=mp.nstr(mx2,25),
               gap_solved={str(k):mp.nstr(mx2-vals2[k],10) for k in range(1,K+1)}),
          open('/tmp/dAp_audit.json','w'), indent=1)
