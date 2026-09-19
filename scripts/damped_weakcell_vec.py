#!/usr/bin/env python3
"""C-190 Step 7 诊断（向量化）：T0 认证 + T1 弱格清单。用法: damped_weakcell_vec.py [T0] [T1] [N0] [BUDGET]"""
import sys, itertools, numpy as np, time
T0=float(sys.argv[1]) if len(sys.argv)>1 else 0.35
T1=float(sys.argv[2]) if len(sys.argv)>2 else 0.3730721881
N0=int(sys.argv[3]) if len(sys.argv)>3 else 6
BUDGET=int(sys.argv[4]) if len(sys.argv)>4 else 8000000
PI=float(np.pi); K=15; SLACK,TE=1e-12,1e-9
XA=np.array([0.79051,0.83021,0.10911*PI,0.82066*PI,0.46172*PI]); RHO=0.004412
def mincos_v(k,lo,hi):
    """min cos(kφ) over [lo,hi]：区间含 kφ≡π (mod 2π) 则为 −1（判据已修正）"""
    out=-np.ones_like(lo); wide=(k*(hi-lo)>=2*PI-TE)
    t0,t1=k*lo,k*hi
    nA=np.ceil((t0-PI)/(2*PI)); nB=np.floor((t1-PI)/(2*PI))
    hit=(nA<=nB)&(~wide); out[hit]=-1.0
    ok=(~wide)&(~hit)
    out[ok]=np.minimum(np.cos(t0[ok]),np.cos(t1[ok]))-SLACK
    return out
def boxlb(lo,hi):
    best=-1e18*np.ones(lo.shape[0])
    for k in range(1,K+1):
        c1=mincos_v(k,lo[:,2],hi[:,2]); c2=mincos_v(k,lo[:,3],hi[:,3]); c3=mincos_v(k,lo[:,4],hi[:,4])
        r2=np.where(c2<0,hi[:,0],lo[:,0])**k; r3=np.where(c3<0,hi[:,1],lo[:,1])**k
        best=np.maximum(best,c1+r2*c2+r3*c3)
    return best-3*SLACK
def dist_box(lo,hi):
    d=np.maximum(np.maximum(XA-lo,0.0),np.maximum(lo-XA,0.0)); return np.linalg.norm(d,axis=1)
g=[np.linspace(0,1,N0+1),np.linspace(0,1,N0+1)]+[np.linspace(0,PI,N0+1)]*3
LO=[];HI=[]
for i in itertools.product(*[range(N0)]*5):
    LO.append([g[0][i[0]],g[1][i[1]],g[2][i[2]],g[3][i[3]],g[4][i[4]]])
    HI.append([g[0][i[0]+1],g[1][i[1]+1],g[2][i[2]+1],g[3][i[3]+1],g[4][i[4]+1]])
slo,s_hi=np.array(LO),np.array(HI)
neval=len(slo); strong=0; weak=[]; t0=time.time()
tlast=time.time()
while len(slo)>0 and neval<BUDGET:
    lb=boxlb(slo,s_hi); neval+=len(slo)
    if time.time()-tlast>10:
        print(f"   ... neval={neval:,} stack={len(slo):,} cert={strong:,} weak={len(weak):,}",flush=True); tlast=time.time()
    cert=lb>=T0
    if cert.any():
        strong+=int(cert.sum()); w=cert&(lb<T1)
        if w.any():
            idx=np.where(w)[0]; d=dist_box(slo[idx],s_hi[idx])
            for j,i in enumerate(idx): weak.append((float(lb[i]),slo[i].copy(),s_hi[i].copy(),float(d[j])))
    todo=~cert
    if not todo.any(): slo=np.empty((0,5)); s_hi=np.empty((0,5)); break
    lo2,hi2=slo[todo],s_hi[todo]
    j=np.argmax(hi2-lo2,axis=1); r=np.arange(len(lo2))
    mid=0.5*(lo2[r,j]+hi2[r,j])
    L=[];H=[]
    for k_ in (0,1):
        l3=lo2.copy(); h3=hi2.copy()
        if k_==0: h3[r,j]=mid
        else: l3[r,j]=mid
        L.append(l3); H.append(h3)
    slo=np.vstack(L); s_hi=np.vstack(H)
print(f"=== 旧证书 weak-cell inventory（T0={T0}, T1={T1:.10f}, N0={N0}）===")
print(f"  评估盒数 {neval} | 认证 {strong} | 弱格 |W| {len(weak)} | 未认证残留 {len(slo)} | {time.time()-t0:.1f}s")
print(f"  ⟹ {'✅ 目标达成：全部格子在 T0 下认证' if len(slo)==0 else '⚠️ 预算耗尽，仍有残留'}")
if weak:
    ds=np.array([w[3] for w in weak]); lbs=np.array([w[0] for w in weak])
    print(f"\n  |W|/N = {len(weak)}/{strong} = {100*len(weak)/strong:.2f}%")
    print(f"  距离：min {ds.min():.6f} | q50 {np.percentile(ds,50):.6f} | q90 {np.percentile(ds,90):.6f} | q99 {np.percentile(ds,99):.6f} | max {ds.max():.6f}")
    print(f"  弱格 LB：min {lbs.min():.6f} | q50 {np.percentile(lbs,50):.6f} | max {lbs.max():.6f}")
    touch=int((ds<=RHO).sum())
    print(f"\n  ★ 触及 B_rho(x_*) 的弱格 = {touch}/{len(weak)} = {100*touch/len(weak):.1f}%")
    for thr in (0.004412,0.009574,0.05,0.1,0.3,0.5,1.0):
        print(f"     距离 <= {thr:.6f}: {int((ds<=thr).sum()):7d}  ({100*(ds<=thr).mean():5.1f}%)")
    c=np.array([0.5*(lo+hi) for _,lo,hi,_ in weak])
    print(f"\n  (r2,r3) 投影：")
    for lab,mask in [("r2>=0.9",c[:,0]>=0.9),("r3>=0.9",c[:,1]>=0.9),("r2,r3均>=0.9",(c[:,0]>=0.9)&(c[:,1]>=0.9)),
                     ("r2>=0.99",c[:,0]>=0.99),("r3>=0.99",c[:,1]>=0.99),("r2<0.5",c[:,0]<0.5)]:
        print(f"     {lab:<14} {int(mask.sum()):7d}  ({100*mask.mean():5.1f}%)")
    np.save('/tmp/weak_cells.npy',np.array([[w[0],*w[1],*w[2],w[3]] for w in weak]))
    print(f"  已存 /tmp/weak_cells.npy")
