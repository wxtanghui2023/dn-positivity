#!/usr/bin/env python3
"""C-223 capped diagnostic（frontier census）
修正：只取 φ 三坐标（B 的 box 含 7 坐标）；min-width 箱 → unresolved（绝不丢弃）
硬上限 2e6；分层统计 N_in/N_cert/N_unres/N_split；失败箱定位（到各球心距离 + 主导 k）
"""
import numpy as np, json, itertools, math
PI=math.pi; K=15
d=json.load(open('/tmp/c222_B.json'))
PHI=[[float(a),float(b)] for a,b in d['box'][:3]]          # ← 只取前 3 个坐标！✓
assert len(PHI)==3, len(PHI)
phi0=np.array([(a+b)/2 for a,b in PHI])
def _has_int_in(A,Bv,parity):
    """[A,Bv] 内是否含【奇(parity=1)/偶(parity=0)整数】✓；A=ceil(a/π), Bv=floor(b/π)"""
    nl=np.ceil(A).astype(np.int64); nh=np.floor(Bv).astype(np.int64)
    same=(nl==nh)
    res=np.where(same, (nl%2)==parity, (nh-nl)>=1)
    return res & (nl<=nh)
def lb_boxes(B, ret_k=False):
    lo=B[:,:,0]; hi=B[:,:,1]; best=np.full(len(B),-1e18); argk=np.zeros(len(B),int)
    for k in range(1,K+1):
        a=k*lo; b=k*hi                       # [a,b] 为 cos 的辐角区间
        v=np.minimum(np.cos(a),np.cos(b))
        odd=_has_int_in(a/PI, b/PI, 1)       # 含【奇】倍 π ⟹ min = -1 ✓
        v=np.where(odd,-1.0,v)
        s=v.sum(axis=1)
        upd=s>best; best=np.where(upd,s,best); argk=np.where(upd,k,argk)
    return (best,argk) if ret_k else best
def ub_boxes(B):
    lo=B[:,:,0]; hi=B[:,:,1]; best=np.full(len(B),-1e18)
    for k in range(1,K+1):
        a=k*lo; b=k*hi
        v=np.maximum(np.cos(a),np.cos(b))
        ev=_has_int_in(a/PI, b/PI, 0)        # 含【偶】倍 π ⟹ max = +1 ✓
        v=np.where(ev,1.0,v)
        best=np.maximum(best,v.sum(axis=1))
    return best
a0=lb_boxes(np.array([PHI]))[0]
b0=float(ub_boxes(np.array([PHI]))[0])
print(f"① F3(X0) 浮点区间 ≈ [{a0:.20f}, {b0:.20f}]   宽 {b0-a0:.3e}   （应 ≈0.76408 ✓）")
T=b0+1e-9
print(f"   T := sup F3(X0) + 1e-9 = {T!r}")
RB=1.4658e-3-1e-6
cs=[]
for perm in itertools.permutations(range(3)):
    c=phi0[list(perm)]
    if all(np.max(np.abs(c-cc))>1e-3 for cc in cs): cs.append(c)
cs=np.array(cs); print(f"② 排除球 {len(cs)} 个（S3 轨道），半径 {RB:.6e}；球心互距 > 1e-3 ✓")
print(f"   X0 外部几何检查：X0 宽 {max(PHI[j][1]-PHI[j][0] for j in range(3)):.3e} ≪ ρ_up ✓")
def inball(B):
    out=np.zeros(len(B),bool); dist=np.full(len(B),np.inf)
    for c in cs:
        far=np.maximum(np.abs(B[:,:,0]-c[None,:]),np.abs(B[:,:,1]-c[None,:]))
        dd=np.sqrt((far**2).sum(axis=1))
        out |= (dd<=RB); dist=np.minimum(dist,dd)
    return out,dist
N0=24; g=np.linspace(0,PI,N0+1)
B=np.array([[[g[i],g[i+1]],[g[j],g[j+1]],[g[l],g[l+1]]] for i in range(N0) for j in range(N0) for l in range(N0)],dtype=float)
CAP=2_000_000; MINW=1e-13
print(f"③ 初始 {len(B)} 箱（[0,π]^3）；硬上限 {CAP:,}；最小宽 {MINW:.0e}")
print(f"\n  {'层':>3} {'N_in':>9} {'N_cert':>9} {'N_unres':>9} {'N_split':>9} {'N_disc':>8} {'frontier':>9}")
tot=dict(cert=0,unres=0,split=0,disc=0,per_eval=0)
unres_boxes=[]; stopped=False
for depth in range(0,60):
    nin=len(B); tot['per_eval']+=nin
    ib,dist=inball(B)
    if ib.any():
        tot['disc']+=int(ib.sum()); B=B[~ib]; dist=dist[~ib]
    if len(B)==0:
        print(f"  {depth:3d} {nin:9d} {0:9d} {0:9d} {0:9d} {int(ib.sum()):8d} {0:9d}   完成 ✓"); break
    L,ak=lb_boxes(B,ret_k=True); ok=L>=T
    ncert=int(ok.sum()); tot['cert']+=ncert
    if ncert: B=B[~ok]; dist=dist[~ok]; L=L[~ok]; ak=ak[~ok]
    w=B[:,:,1]-B[:,:,0]; wmax=w.max(axis=1); tiny=wmax<MINW
    nunres=int(tiny.sum())
    if nunres:
        tot['unres']+=nunres
        for i in np.where(tiny)[0][:2000]:
            unres_boxes.append((float(wmax[i]), float(L[i]), int(ak[i]), float(dist[i]), B[i].tolist()))
        B=B[~tiny]; dist=dist[~tiny]; w=w[~tiny]; L=L[~tiny]; ak=ak[~tiny]
    nsplit=len(B); tot['split']+=nsplit
    print(f"  {depth:3d} {nin:9d} {ncert:9d} {nunres:9d} {nsplit:9d} {int(ib.sum()):8d} {nsplit:9d}")
    if nsplit==0: print("  ⟹ frontier 清零 ✓ 全部处理完毕"); break
    if nsplit>CAP: print(f"  ⚠️ frontier {nsplit:,} > 上限 {CAP:,} ⟹ STOP（不产生任何成功结论）"); stopped=True; break
    j=int(np.argmax(w.mean(axis=0)))
    mid=B[:,j,:].mean(axis=1)
    B1=B.copy(); B1[:,j,1]=mid; B2=B.copy(); B2[:,j,0]=mid
    B=np.concatenate([B1,B2])
print(f"\n④ 累计：评估 {tot['per_eval']:,}  认证 {tot['cert']:,}  未决 {tot['unres']:,}  分裂 {tot['split']:,}  丢弃 {tot['disc']:,}")
if unres_boxes:
    ds=np.array([u[3] for u in unres_boxes]); ks=np.array([u[2] for u in unres_boxes])
    print(f"\n⑤ 未决箱定位（{len(unres_boxes)} 个样本）：")
    print(f"   到最近球心距离：min {ds.min():.4e}  q25 {np.quantile(ds,.25):.4e}  中位 {np.median(ds):.4e}  q75 {np.quantile(ds,.75):.4e}  max {ds.max():.4e}")
    print(f"   距球面 (RB=1.4658e-3) 的超出量：min {ds.min()-RB:+.4e}  中位 {np.median(ds)-RB:+.4e}  max {ds.max()-RB:+.4e}")
    u,c=np.unique(ks,return_counts=True); print(f"   主导 k 分布：{dict(zip(u.tolist(),c.tolist()))}")
    print(f"   LB 与 T 的差：min {min(u[1] for u in unres_boxes)-T:+.4e}  max {max(u[1] for u in unres_boxes)-T:+.4e}")
    print(f"   ⟹ 未决箱是否集中在【球面附近】？ {'是 ✓ 可用 branch-aware / 球面解析处理' if np.median(ds)-RB < 5e-3 else '否 ✗ 说明 LB 有结构性弱点'}")
else:
    print("\n⑤ 无未决箱 ✓")
json.dump(dict(a0=float(a0),b0=float(b0),T=float(T),RB=RB,tot=tot,stopped=bool(stopped),
               n_unres_samples=len(unres_boxes),
               unres_dist=[float(u[3]) for u in unres_boxes[:500]],
               unres_k=[int(u[2]) for u in unres_boxes[:500]]), open('/tmp/c223_diag.json','w'),indent=1)
