#!/usr/bin/env python3
"""C-190 严格化 ②：第二独立实现（纯 Python，无 numpy）交叉验证
与 numpy 向量化实现逐盒比对 LB 值（浮点一致性与逻辑一致性）"""
import itertools, math, numpy as np, sys
T=0.3730721881; N0=10; PI=float(np.pi); PI_UP=float(np.nextafter(np.pi,np.inf)); TEST=20000
def mincos_B(k,lo,hi):
    if k*(hi-lo)>=2*math.pi-1e-9: return -1.0
    nA=math.ceil((k*lo-math.pi)/(2*math.pi)); nB=math.floor((k*hi-math.pi)/(2*math.pi))
    if nB>=nA: return -1.0
    return min(math.cos(k*lo),math.cos(k*hi))-1e-12
def lb_B(lo,hi):
    best=-1e18
    for k in range(1,16):
        c1=mincos_B(k,lo[2],hi[2]); c2=mincos_B(k,lo[3],hi[3]); c3=mincos_B(k,lo[4],hi[4])
        r2=(hi[0]**k if c2<0 else lo[0]**k); r3=(hi[1]**k if c3<0 else lo[1]**k)
        v=c1+r2*c2+r3*c3
        if v>best: best=v
    return best-3e-12
# 复用 A 实现的向量化（独立复制，避免 import 污染）
def mincos_A(k,lo,hi):
    out=-np.ones_like(lo); wide=(k*(hi-lo)>=2*PI-1e-9); t0,t1=k*lo,k*hi
    nA=np.ceil((t0-PI)/(2*PI)); nB=np.floor((t1-PI)/(2*PI))
    hit=(nA<=nB)&(~wide); out[hit]=-1.0
    ok=(~wide)&(~hit); out[ok]=np.minimum(np.cos(t0[ok]),np.cos(t1[ok]))-1e-12
    return out
def lb_A(lo,hi):
    best=-1e18*np.ones(lo.shape[0])
    for k in range(1,16):
        c1=mincos_A(k,lo[:,2],hi[:,2]); c2=mincos_A(k,lo[:,3],hi[:,3]); c3=mincos_A(k,lo[:,4],hi[:,4])
        r2=np.where(c2<0,hi[:,0],lo[:,0])**k; r3=np.where(c3<0,hi[:,1],lo[:,1])**k
        best=np.maximum(best,c1+r2*c2+r3*c3)
    return best-3e-12
# 生成终端盒（同上，确定性）
g=[np.linspace(0,1,N0+1),np.linspace(0,1,N0+1)]+[np.linspace(0,PI_UP,N0+1)]*3
LO=[];HI=[]
for i in itertools.product(*[range(N0)]*5):
    LO.append([g[0][i[0]],g[1][i[1]],g[2][i[2]],g[3][i[3]],g[4][i[4]]])
    HI.append([g[0][i[0]+1],g[1][i[1]+1],g[2][i[2]+1],g[3][i[3]+1],g[4][i[4]+1]])
slo,s_hi=np.array(LO),np.array(HI); TL=[];TH=[]
while len(slo)>0:
    lb=lb_A(slo,s_hi); cert=lb>=T
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
print(f"终端盒 {len(TL):,}；抽样 {TEST} 个做双实现比对")
rng=np.random.default_rng(7); idx=rng.choice(len(TL),size=min(TEST,len(TL)),replace=False)
vA=lb_A(TL[idx],TH[idx])
vB=np.array([lb_B(TL[i],TH[i]) for i in idx])
diff=np.abs(vA-vB)
print(f"  最大绝对差 = {diff.max():.3e}；中位差 = {np.median(diff):.3e}")
print(f"  双实现对 T 的判定是否一致：{bool(np.all((vA>=T)==(vB>=T)))}")
print(f"  A 端最小 LB = {vA.min():.6e}；B 端最小 LB = {vB.min():.6e}")
print(f"  ⟹ {'✅ 双实现一致（逻辑等价，实现独立）' if diff.max()<1e-9 else '⚠️ 存在差异，需查'}")
