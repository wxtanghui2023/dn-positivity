#!/usr/bin/env python3
"""
C-190 严格化 ③（终版）：一次到位
  Gate 1A 域覆盖（含精确铺砌体积校验）
  Gate 1B 逐盒区间下界 + 【固定最小余量格】（cell ID + 五维区间）
  Gate 2  区间层双实现抽样（A: mpmath.iv / B: mpf+显式外向误差）
用法: damped_T1_interval_verify_v3.py [T] [N0] [SAMPLE]
"""
import sys, itertools, numpy as np, time, hashlib, json
from fractions import Fraction as F
T=float(sys.argv[1]) if len(sys.argv)>1 else 0.3730721881
N0=int(sys.argv[2]) if len(sys.argv)>2 else 10
SAMPLE=int(sys.argv[3]) if len(sys.argv)>3 else 2000
PI=float(np.pi); PI_UP=float(np.nextafter(np.pi,np.inf)); K=15; SLACK,TE=1e-12,1e-9
print(f"=== v3  Term T={T:.10f}  N0={N0} ===",flush=True)
print(f"[Gate 1A] φ 网格上界 = {PI_UP!r}  (> π = {PI!r})  ⟹ [0,PI_UP] ⊇ [0,π] ✓",flush=True)
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
g=[np.linspace(0,1,N0+1),np.linspace(0,1,N0+1)]+[np.linspace(0,PI_UP,N0+1)]*3
assert g[0][0]==0.0 and g[0][-1]==1.0 and g[1][0]==0.0 and g[1][-1]==1.0
assert g[2][0]==0.0 and g[2][-1]==PI_UP
print(f"[Gate 1A] r 端点: 0.0 / 1.0 精确 ✓；φ 端点: 0.0 / PI_UP ✓（无 float 偷换数学端点）",flush=True)
LO=[];HI=[]
for i in itertools.product(*[range(N0)]*5):
    LO.append([g[0][i[0]],g[1][i[1]],g[2][i[2]],g[3][i[3]],g[4][i[4]]])
    HI.append([g[0][i[0]+1],g[1][i[1]+1],g[2][i[2]+1],g[3][i[3]+1],g[4][i[4]+1]])
slo,s_hi=np.array(LO),np.array(HI); TL=[];TH=[];neval=len(slo);t0=time.time()
while len(slo)>0:
    lb=boxlb(slo,s_hi); neval+=len(slo); cert=lb>=T
    if cert.any(): TL.append(slo[cert]); TH.append(s_hi[cert])
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
TL=np.vstack(TL); TH=np.vstack(TH)
print(f"  P1 完成: {neval:,} 盒 / 终端 {len(TL):,} / {time.time()-t0:.0f}s",flush=True)
# Gate 1A 精确体积校验（Fraction，坐标皆为二进制有理 ⟹ 精确）
vol=sum((F(h[0])-F(l[0]))*(F(h[1])-F(l[1]))*(F(h[2])-F(l[2]))*(F(h[3])-F(l[3]))*(F(h[4])-F(l[4])) for l,h in zip(TL,TH))
target=F(1)*F(1)*(F(PI_UP)**3)
print(f"[Gate 1A] 终端盒总体积 = {float(vol):.12f}；初始域体积(1·1·PI_UP³) = {float(target):.12f}",flush=True)
print(f"[Gate 1A] 体积相等(精确) = {vol==target}  ⟹ {'✅ 铺砌无缝无叠' if vol==target else '⚠️ 铺砌有问题'}",flush=True)
hash16=hashlib.sha256(TL.tobytes()).hexdigest()[:32]
print(f"  终端铺砌 sha256[:32] = {hash16}",flush=True)
# Gate 1B: 逐盒区间下界 + 记录最小余量格
from mpmath import iv, mp
mp.dps=30; iv.prec=60
def lbA(l,h):
    best=None
    for k in range(1,K+1):
        c1=iv.cos(k*iv.mpf([float(l[2]),float(h[2])])).a
        c2i=iv.cos(k*iv.mpf([float(l[3]),float(h[3])])); clo2=c2i.a
        c3i=iv.cos(k*iv.mpf([float(l[4]),float(h[4])])); clo3=c3i.a
        r2t=(iv.mpf(float(h[0]))**k).b if clo2<0 else (iv.mpf(float(l[0]))**k).a
        r3t=(iv.mpf(float(h[1]))**k).b if clo3<0 else (iv.mpf(float(l[1]))**k).a
        v=c1+iv.mpf(r2t)*iv.mpf(clo2)+iv.mpf(r3t)*iv.mpf(clo3)
        if best is None or v.a>best: best=v.a
    return best
print(f"\n[Gate 1B] 区间验证开始（{len(TL):,} 盒）...",flush=True)
bad=0; minm=None; minidx=-1; margins=[]; t1=time.time()
for i in range(len(TL)):
    l=lbA(TL[i],TH[i]); m=float(l)-T; margins.append(m)
    if m<0: bad+=1
    if minm is None or m<minm: minm=m; minidx=i; minlb=float(l)
    if i%40000==0 and i>0: print(f"   ... {i:,}/{len(TL):,}  当前最小余量 {minm:.3e}  {time.time()-t1:.0f}s",flush=True)
margins=np.array(margins)
print(f"\n[Gate 1B] 完成: 验证 {len(TL):,} | 违反 {bad} | 最小余量 {minm:.6e} | {time.time()-t1:.0f}s",flush=True)
print(f"[Gate 1B] ★ 最危险格 id={minidx}  LB_IV={minlb:.12f}  余量={minm:.6e}",flush=True)
print(f"[Gate 1B]   五维区间 lo={list(TL[minidx])}",flush=True)
print(f"[Gate 1B]            hi={list(TH[minidx])}",flush=True)
# Gate 2: 区间层双实现（B: mpf + 显式外向误差）
import math
from mpmath import mpf
mp.dps=60
EPS=mpf(10)**-50
def lbB(l,h):
    best=None
    for k in range(1,K+1):
        l2,l3,l4=mpf(float(l[2])),mpf(float(l[3])),mpf(float(l[4]))
        h2,h3,h4=mpf(float(h[2])),mpf(float(h[3])),mpf(float(h[4]))
        def cmin(a,b):
            kk=mpf(k)
            if kk*(b-a)>=2*mp.pi-mpf('1e-9') or (mp.ceil((kk*a-mp.pi)/(2*mp.pi))<=mp.floor((kk*b-mp.pi)/(2*mp.pi))):
                return mpf(-1)
            return min(mp.cos(kk*a),mp.cos(kk*b))
        c1=cmin(l2,h2); c2=cmin(l3,h3); c3=cmin(l4,h4)
        def rk(a,b,kk):
            if kk<0: return None
            return mpf(float(h[0]))**k if kk<0 else None
        r2t=(mpf(float(h[0]))**k) if c2<0 else (mpf(float(l[0]))**k)
        r3t=(mpf(float(h[1]))**k) if c3<0 else (mpf(float(l[1]))**k)
        v=c1+r2t*c2+r3t*c3-3*EPS
        if best is None or v>best: best=v
    return best
rng=np.random.default_rng(11)
idx=list(rng.choice(len(TL),size=min(SAMPLE,len(TL)),replace=False))
if minidx not in idx: idx.append(minidx)
diffs=[]
t2=time.time()
for i in idx:
    a=lbA(TL[i],TH[i]); b=lbB(TL[i],TH[i])
    diffs.append(abs(float(a)-float(b)))
diffs=np.array(diffs)
print(f"\n[Gate 2] 区间层双实现抽样 {len(idx)} 盒（含最危险格）：",flush=True)
print(f"   最大 |LB_A^IV − LB_B^IV| = {diffs.max():.3e}  | 中位 = {np.median(diffs):.3e}  | {time.time()-t2:.0f}s",flush=True)
print(f"   两者对 T 判定一致 = {bool(np.all(np.array([lbA(TL[i],TH[i])>=mpf(T) for i in idx]))==np.all(np.array([lbB(TL[i],TH[i])>=mpf(T) for i in idx])))}",flush=True)
json.dump({"T":T,"N0":N0,"n_box":int(len(TL)),"violations":int(bad),"min_margin":float(minm),
           "min_cell_id":int(minidx),"min_cell_lo":[float(x) for x in TL[minidx]],"min_cell_hi":[float(x) for x in TH[minidx]],
           "tiling_sha":hash16,"tiling_volume_exact_ok":bool(vol==target),
           "gate2_max_iv_diff":float(diffs.max()),"gate2_sample":int(len(idx))},
          open('/tmp/t1iv3_result.json','w'),indent=1)
print("  已存 /tmp/t1iv3_result.json",flush=True)
