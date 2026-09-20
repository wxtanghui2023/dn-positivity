#!/usr/bin/env python3
"""C-214：纯 B&B 下界阶梯探测 + 失败箱定位（回答"为什么只能到 0.76"）
LB(box) = max_k sum_j min_{phi in I_j} cos(k phi_j)   （可分下界，严格）
"""
import numpy as np, json, time, itertools
from fractions import Fraction
K=15; D=3
PI_F=Fraction(31415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679,10**100)

PIF=float(PI_F)
def cosmin(a,b,k):
    if b<a: a,b=b,a
    lo=k*a; hi=k*b
    j0=int(np.ceil(lo/PIF)); j1=int(np.floor(hi/PIF))
    if j1>=j0:
        for j in range(j0,j1+1):
            if j%2!=0: return -1.0
    return float(min(np.cos(k*a), np.cos(k*b)))

def bb(T, N0=12, guard=3_000_000, maxdepth=55, want_survivors=False):
    ts=time.time()
    lo=np.array([Fraction(0)]*3); hi=np.array([PI_F]*3)
    # 用 float 区间表示（下界保守：只影响 LB 计算，见 cosmin 的 -1 保守）
    boxes=[(0.0,float(PI_F),0.0,float(PI_F),0.0,float(PI_F),0)]  # a1,b1,a2,b2,a3,b3,depth
    nterm=0; peak=1; surviv=[]
    while boxes:
        x1,x2,y1,y2,z1,z2,dep=boxes.pop()
        lb=-1e9
        for k in range(1,K+1):
            v=cosmin(x1,x2,k)+cosmin(y1,y2,k)+cosmin(z1,z2,k)
            if v>lb: lb=v
        if lb>=T: nterm+=1; continue
        if dep>=maxdepth:
            surviv.append((x1,x2,y1,y2,z1,z2,lb)); continue
        # 分裂最宽维
        w=[x2-x1,y2-y1,z2-z1]; j=int(np.argmax(w))
        if j==0: mid=(x1+x2)/2; boxes.append((x1,mid,y1,y2,z1,z2,dep+1)); boxes.append((mid,x2,y1,y2,z1,z2,dep+1))
        elif j==1: mid=(y1+y2)/2; boxes.append((x1,x2,y1,mid,z1,z2,dep+1)); boxes.append((x1,x2,mid,y2,z1,z2,dep+1))
        else: mid=(z1+z2)/2; boxes.append((x1,x2,y1,y2,z1,mid,dep+1)); boxes.append((x1,x2,y1,y2,mid,z2,dep+1))
        peak=max(peak,len(boxes))
        if len(boxes)>guard: return dict(T=T,converged=False,peak=peak,surv=None,sec=time.time()-ts,nterm=nterm,nfront=len(boxes))
    return dict(T=T,converged=True,peak=peak,surv=surviv,sec=time.time()-ts,nterm=nterm,nfront=0)

cl=json.load(open('/tmp/t13aeq_clusters.json'))['clusters']
x0=np.array(cl[0]['x'])/np.pi     # phi/pi
PERMS=list(itertools.permutations(range(3)))
def dS3(a,b): return min(float(np.linalg.norm(np.asarray(a)[list(p)]-np.asarray(b))) for p in PERMS)
print("="*100); print("C-214：纯 B&B 阶梯（可分下界）—— 找分辨率墙"); print("="*100)
print(f"  m_3 的数值上界（簇 0）= 0.7640811007，所以 T>该值必然不可能收敛")
print(f"\n  {'T':>10} {'收敛':>6} {'终端箱':>10} {'峰值前沿':>10} {'耗时s':>8}   未决箱数")
res=[]
for T in (0.760,0.761,0.762,0.763,0.7635,0.764,0.76405,0.76408):
    r=bb(T)
    print(f"  {T:10.5f} {str(r['converged']):>6} {r['nterm']:10d} {r['peak']:10d} {r['sec']:8.1f}   {len(r['surv']) if r['surv'] else '-'}")
    res.append(dict(T=T,converged=r['converged'],nterm=r['nterm'],peak=r['peak'],sec=r['sec'],nsurv=(len(r['surv']) if r['surv'] else None)))
    if not r['converged'] and r['surv'] is None: break
json.dump(res,open('/tmp/c214_ladder.json','w'),indent=2)
# 若某档收敛但有未决箱（depth 上限），定位它们
last=[r for r in res if r['converged']]
print("\n（阶梯完成）")
