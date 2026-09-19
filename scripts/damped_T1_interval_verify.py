#!/usr/bin/env python3
"""
C-190 Step 7 严格化 ①：把 T1=0.3730721881 的浮点 B&B 证书升级为【区间算术验证】
两阶段：
  P1 浮点 B&B 生成【终端盒清单】（确定性、可复现）——仅作组织装置
  P2 对每个终端盒用 mpmath.iv 计算【严格下界】并核对 ≥ T
用法: damped_T1_interval_verify.py [T] [N0] [P2_ONLY_FILE] [LIMIT]
"""
import sys, itertools, numpy as np, time, hashlib, json
T=float(sys.argv[1]) if len(sys.argv)>1 else 0.3730721881
N0=int(sys.argv[2]) if len(sys.argv)>2 else 10
LIMIT=int(sys.argv[3]) if len(sys.argv)>3 else 0     # >0 时只验前 LIMIT 个盒（基准用）
PI=float(np.pi); K=15; SLACK,TE=1e-12,1e-9
def mincos_v(k,lo,hi):
    out=-np.ones_like(lo); wide=(k*(hi-lo)>=2*PI-TE); t0,t1=k*lo,k*hi
    nA=np.ceil((t0-PI)/(2*PI)); nB=np.floor((t1-PI)/(2*PI))
    hit=(nA<=nB)&(~wide); out[hit]=-1.0
    ok=(~wide)&(~hit); out[ok]=np.minimum(np.cos(t0[ok]),np.cos(t1[ok]))-SLACK
    return out
def boxlb(lo,hi):
    best=-1e18*np.ones(lo.shape[0])
    for k in range(1,K+1):
        c1=mincos_v(k,lo[:,2],hi[:,2]); c2=mincos_v(k,lo[:,3],hi[:,3]); c3=mincos_v(k,lo[:,4],hi[:,4])
        r2=np.where(c2<0,hi[:,0],lo[:,0])**k; r3=np.where(c3<0,hi[:,1],lo[:,1])**k
        best=np.maximum(best,c1+r2*c2+r3*c3)
    return best-3*SLACK
print(f"=== P1: 浮点 B&B 生成终端盒清单（T={T:.10f}, N0={N0}）===",flush=True)
g=[np.linspace(0,1,N0+1),np.linspace(0,1,N0+1)]+[np.linspace(0,PI,N0+1)]*3
LO=[];HI=[]
for i in itertools.product(*[range(N0)]*5):
    LO.append([g[0][i[0]],g[1][i[1]],g[2][i[2]],g[3][i[3]],g[4][i[4]]])
    HI.append([g[0][i[0]+1],g[1][i[1]+1],g[2][i[2]+1],g[3][i[3]+1],g[4][i[4]+1]])
slo,s_hi=np.array(LO),np.array(HI)
term_lo=[];term_hi=[];neval=len(slo);t0=time.time()
while len(slo)>0:
    lb=boxlb(slo,s_hi); neval+=len(slo); cert=lb>=T
    if cert.any(): term_lo.append(slo[cert]); term_hi.append(s_hi[cert])
    todo=~cert
    if not todo.any(): break
    lo2,hi2=slo[todo],s_hi[todo]; j=np.argmax(hi2-lo2,axis=1); r=np.arange(len(lo2)); mid=0.5*(lo2[r,j]+hi2[r,j])
    L=[];H=[]
    for k_ in (0,1):
        l3=lo2.copy(); h3=hi2.copy()
        if k_==0: h3[r,j]=mid
        else: l3[r,j]=mid
        L.append(l3);H.append(h3)
    slo=np.vstack(L); s_hi=np.vstack(H)
TL=np.vstack(term_lo); TH=np.vstack(term_hi)
TIL=TL.tobytes(); print(f"  P1 完成：{neval:,} 盒评估 / 终端盒 {len(TL):,} / {time.time()-t0:.1f}s",flush=True)
print(f"  终端清单 sha256 = {hashlib.sha256(TIL).hexdigest()[:32]}",flush=True)
if LIMIT>0: TL=TL[:LIMIT]; TH=TH[:LIMIT]
print(f"\n=== P2: 区间算术（mpmath.iv）逐盒严格下界 ===",flush=True)
from mpmath import iv, mp
mp.dps=30; iv.prec=60
def lb_iv(lo,hi):
    """该盒的严格下界（interval）"""
    best=None
    for k in range(1,K+1):
        c1=iv.cos(k*iv.mpf([float(lo[2]),float(hi[2])])).a
        c2i=iv.cos(k*iv.mpf([float(lo[3]),float(hi[3])])); clo2=c2i.a
        c3i=iv.cos(k*iv.mpf([float(lo[4]),float(hi[4])])); clo3=c3i.a
        # r^k 项：cos 负 ⟹ 用 r 上端的上包络；否则用 r 下端的下包络
        if clo2<0:
            r2t=(iv.mpf(float(hi[0]))**k).b
        else:
            r2t=(iv.mpf(float(lo[0]))**k).a
        if clo3<0:
            r3t=(iv.mpf(float(hi[1]))**k).b
        else:
            r3t=(iv.mpf(float(lo[1]))**k).a
        v=c1 + iv.mpf(r2t)*iv.mpf(clo2) + iv.mpf(r3t)*iv.mpf(clo3)
        vl=v.a
        if best is None or vl>best: best=vl
    return best
t0=time.time(); bad=0; margins=[]; Nv=len(TL)
for i in range(Nv):
    l=lb_iv(TL[i],TH[i]); m=float(l)-T
    margins.append(m)
    if m<0: bad+=1
    if i%20000==0 and i>0:
        print(f"   ... {i:,}/{Nv:,} 最小余量 {min(margins):.3e} 用时 {time.time()-t0:.0f}s",flush=True)
margins=np.array(margins)
print(f"\n  P2 完成：验证盒 {Nv:,} | 违反(严格下界<T) {bad} | {time.time()-t0:.1f}s")
print(f"  最小严格余量 = {margins.min():.6e}（≥0 ⟹ 全部通过 ✓）")
print(f"  ⟹ {'✅ 区间验证通过：F ≥ T 严格成立' if bad==0 else '⚠️ 有盒未通过'}")
json.dump({"T":T,"N0":N0,"n_box":int(Nv),"violations":int(bad),"min_margin":float(margins.min()),
           "tiling_sha":hashlib.sha256(TIL).hexdigest()},open('/tmp/t1_interval_result.json','w'),indent=1)
print("  已存 /tmp/t1_interval_result.json")
