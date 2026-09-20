#!/usr/bin/env python3
"""T13-A-EQ 第一刀：M=3（窗口 5M=15）近极小层结构审计
 Phase A 粗网格定位盆地 → Phase B 精修+模 S₃ 聚类 → Phase C active set / 梯度秩 / 严格正凸组合 / 二阶方向
"""
import numpy as np, itertools, json
from scipy.optimize import minimize, linprog
np.set_printoptions(precision=8, suppress=True)
K=15; D=3
def Sv(x):  return np.array([sum(np.cos(k*x[j]) for j in range(D)) for k in range(1,K+1)])
def F(x):   return float(Sv(x).max())

print("="*90); print("T13-A-EQ   M=3, 窗口 5M=15, F_3 = max_k Σ_j cos(kφ_j)"); print("="*90)

# ---------- Phase A: 粗网格 ----------
N=80
g=np.linspace(0,np.pi,N+1)
best=[]
gx,gy,gz=np.meshgrid(g[:N],g[:N],g[:N],indexing='ij')
pts=np.stack([gx.ravel(),gy.ravel(),gz.ravel()],axis=1)
V=np.full(len(pts),-9.)
for k in range(1,K+1):
    V=np.maximum(V, np.cos(k*pts[:,0])+np.cos(k*pts[:,1])+np.cos(k*pts[:,2]))
print(f"[A] 网格 {N}³ = {len(pts):,} 点；网格最小 F = {V.min():.9f}")
order=np.argsort(V)[:400]
starts=[pts[i] for i in order]+[np.random.default_rng(7).uniform(0,np.pi,3) for _ in range(150)]
print(f"[B] 精修起点 {len(starts)} 个（最低 400 格点 + 150 随机）…", flush=True)

found=[]
for i,s in enumerate(starts):
    r=minimize(F,s,method='Nelder-Mead',options={'xatol':1e-11,'fatol':1e-14,'maxiter':1200})
    found.append((float(r.fun), (r.x % np.pi)))
    if i%150==0: print(f"    …{i}/{len(starts)}", flush=True)
found.sort(key=lambda t:t[0])
print(f"[B] 收敛点 {len(found)} 个；最低 5 个值：{ [round(v,10) for v,_ in found[:5]] }")

# ---------- 聚类（模 S₃ 置换）----------
clusters=[]
for v,x in found:
    xs=np.sort(x)
    hit=False
    for cl in clusters:
        if abs(cl['v']-v)<3e-5 and np.allclose(cl['x'],xs,atol=5e-3): cl['n']+=1; hit=True; break
    if not hit: clusters.append(dict(v=v,x=xs,n=1))
clusters.sort(key=lambda d:d['v'])
print(f"[C] 去重后候选簇 {len(clusters)} 个（模 S₃）\n")

# ---------- Phase C: 审计四项 ----------
def audit(x):
    sv=Sv(x); mx=sv.max(); A=[k for k in range(1,K+1) if mx-sv[k-1]<1e-9]
    G=np.array([[-k*np.sin(k*x[j]) for j in range(D)] for k in A])
    # (a) 差分秩
    r_diff = int(np.linalg.matrix_rank(G-G[0], tol=1e-8)) if len(A)>1 else 0
    # (b) 严格正凸组合 sum λ_k ∇S_k = 0, λ>0, Σλ=1  (LP: 先找可行解再最大化最小 λ)
    lam=None; res_pos=False
    if len(A)>=D+1:
        Ab=np.hstack([G.T, -np.ones((D,1))])       # G^T λ - t*1 = 0
        Aeq=np.zeros((D+1,len(A)+1)); Aeq[:D,:len(A)]=G.T; Aeq[D,:len(A)]=1
        beq=np.zeros(D+1); beq[:D]=0; beq[D]=1
        c=np.zeros(len(A)+1); c[-1]=-1
        bnd=[(0,None)]*len(A)+[(None,None)]
        r=linprog(c,A_eq=Aeq,b_eq=beq,bounds=bnd,method='highs')
        if r.success: res_pos = r.x[-1] > 1e-12; lam=r.x[:len(A)]
    # (c) covering 常数 c = min_|u|=1 max_k <g_k,u>
    th=np.linspace(0,2*np.pi,181); ph=np.linspace(-1,1,41)
    cbest=1e9
    for t in th:
        for z in ph:
            u=np.array([np.cos(t)*np.sqrt(1-z*z),np.sin(t)*np.sqrt(1-z*z),z])
            cbest=min(cbest,(G@u).max())
    # (d) 二阶方向：F(x+δ)-F(x) 随 |δ| 的增长
    growth=[]
    for r_ in (1e-3,3e-3,1e-2):
        vals=[]
        for _ in range(400):
            d=np.random.default_rng(int(1e6*r_)+_).normal(size=3); d/=np.linalg.norm(d)
            vals.append(F(x+r_*d)-mx)
        growth.append((r_, float(np.min(vals)), float(np.median(vals))))
    return A,G,r_diff,res_pos,cbest,lam,growth

print(f"  {'#':>2} {'F(x)':>13} {'n':>4} | active A            |A| rank(Δ) 严格正λ?    c        二阶增长 dF(min)@r")
for i,cl in enumerate(clusters[:8]):
    x=cl['x']; A,G,rdiff,rpos,cb,lam,gr=audit(x)
    gtxt=" ".join(f"{r:.0e}:{v:+.2e}({m:+.2e})" for r,v,m in gr)
    print(f"  {i:2d} {cl['v']:13.10f} {cl['n']:4d} | {str(A):20s} {len(A):2d} {rdiff:7d}  {'YES' if rpos else 'no':9s} {cb:+.6f}  {gtxt}")
print()
best=clusters[0]
print(f"═══ 最佳簇（F={best['v']:.12f}）详细 ═══")
x=best['x']; A,G,rdiff,rpos,cb,lam,gr=audit(x)
print(f"  构型 φ/π = {np.round(x/np.pi,9)}")
print(f"  active A = {A}   |A| = {len(A)}   （M+1 = 4 为一般非退化签名）")
print(f"  差分秩 rank[∇S_k − ∇S_{{k0}}] = {rdiff}   ⟹ {'满秩(=3) ⟹ 孤立' if rdiff==3 else '不满秩 ⟹ 可能退化/连续'}")
print(f"  严格正凸组合（LP）: {'存在 ✓' if rpos else '不存在 ✗'}")
if rpos: print(f"     λ = {np.round(lam,8)}  （min λ = {lam.min():.3e}）")
print(f"  covering 常数 c = min_|u|=1 max_k⟨g_k,u⟩ = {cb:+.6f}   ⟹ {'c>0 非退化 ✓' if cb>1e-6 else 'c≈0 退化 ✗'}")
print(f"  二阶方向增长：")
for r_,v,m in gr: print(f"     |δ|={r_:.0e}: min dF={v:+.4e}  （线性系数 {v/r_:+.6f}）  中位 dF={m:+.4e}")
json.dump(dict(clusters=[dict(v=c['v'],x=[float(t) for t in c['x']],n=c['n']) for c in clusters[:12]]),
          open('/tmp/t13aeq_clusters.json','w'),indent=2)
print("\n（已写 /tmp/t13aeq_clusters.json）")
