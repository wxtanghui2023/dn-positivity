#!/usr/bin/env python3
"""
C-199: T13-B / w=2 —— 远场证书（自适应两尺度；Phase1 float 建分区 / Phase2 区间验证 / Phase3 体积核对）
"""
import sys, json, time, math
from fractions import Fraction as F
import numpy as np
import mpmath as mp

mp.iv.prec = 130
KMAX = 10
PI_LO = F(314159265358979323846, 10**20)
PI_UP = F(314159265358979323847, 10**20)
R2    = F(9604, 1000000)   # (0.098)^2 = 9604/10^6 = 0.009604；丢弃半径 = 0.098 < 0.1
A1,B1 = -PI_UP/3, 2*PI_UP/3
A2,B2 = -PI_UP/2, PI_UP/2

def in_ball_box(a1,b1,a2,b2):
    for x in (a1,b1):
        for y in (a2,b2):
            if x*x+y*y > R2: return False
    return True

# ---------------- Phase 1 ----------------
PI=float(PI_UP); P3=PI/3; P2=PI/2
def _m1(k,lo,hi):
    x0,x1 = k*(P3+lo), k*(P3+hi)
    if k*(hi-lo)>=2*math.pi-1e-12: return -1.0
    nA=math.ceil((x0-math.pi)/(2*math.pi)); nB=math.floor((x1-math.pi)/(2*math.pi))
    return -1.0 if nA<=nB else min(math.cos(x0),math.cos(x1))
def _m2(k,lo,hi):
    y0,y1 = k*(P2+lo), k*(P2+hi)
    if k*(hi-lo)>=2*math.pi-1e-12: return -1.0
    nA=math.ceil((y0-math.pi)/(2*math.pi)); nB=math.floor((y1-math.pi)/(2*math.pi))
    return -1.0 if nA<=nB else min(math.cos(y0),math.cos(y1))
def LB_f(a1,b1,a2,b2):
    best=-9.0
    for k in range(1,KMAX+1):
        best=max(best, 2*_m1(k,float(a1),float(b1)) + _m2(k,float(a2),float(b2)))
    return best

N0 = int(sys.argv[1]) if len(sys.argv)>1 else 40
MAXD = int(sys.argv[2]) if len(sys.argv)>2 else 60
print("="*82); print("C-199 远场证书（T13-B / w=2）"); print("="*82)
print(f"域 δ1∈[{float(A1):.9f},{float(B1):.9f}]  δ2∈[{float(A2):.9f},{float(B2):.9f}]   闭球 r=0.1")
g1=[A1+(B1-A1)*i/N0 for i in range(N0+1)]; g2=[A2+(B2-A2)*j/N0 for j in range(N0+1)]
stack=[((g1[i],g1[i+1],g2[j],g2[j+1]),0) for i in range(N0) for j in range(N0)]
t0=time.time(); term=[]; disc=[]; nev=0; maxd=0; minv=1e30; minbox=None; bad=None
while stack:
    bx,d = stack.pop(); a1,b1,a2,b2 = bx; nev+=1; maxd=max(maxd,d)
    if in_ball_box(a1,b1,a2,b2): disc.append(bx); continue
    v=LB_f(a1,b1,a2,b2)
    if v>=1.0:
        term.append((a1,b1,a2,b2,v))
        if v<minv: minv,minbox=v,bx
        continue
    if d>=MAXD or nev>4_000_000: bad=(bx,v); break
    if (b1-a1)>=(b2-a2):
        m=(a1+b1)/2; stack.append(((a1,m,a2,b2),d+1)); stack.append(((m,b1,a2,b2),d+1))
    else:
        m=(a2+b2)/2; stack.append(((a1,b1,a2,m),d+1)); stack.append(((a1,b1,m,b2),d+1))
print(f"[Phase1] N0={N0} 评估箱={nev:,} 终端认证={len(term):,} 球内丢弃={len(disc):,} 深度={maxd} {time.time()-t0:.2f}s")
print(f"         终端 LB 最小值={minv:.9f} (余量 {minv-1:+.4e})  最小箱 δ1∈[{float(minbox[0]):.6f},{float(minbox[1]):.6f}] δ2∈[{float(minbox[2]):.6f},{float(minbox[3]):.6f}]")
if bad: print(f"         ✗ 未决箱 {bad[0]} LB={bad[1]:.9f}"); sys.exit(1)
w=[float(b-a) for a,b,c,d,v in term]
nz=len([x for x in term if (float((x[0]+x[1])/2)**2+float((x[2]+x[3])/2)**2)**0.5<0.25])
print(f"         两尺度结构：终端箱宽度 min={min(w):.3e} 中位={np.median(w):.3e} max={max(w):.3e}；边界层(距原点<0.25) {nz} 个 / bulk {len(term)-nz} 个")

# ---------------- Phase 2 ----------------
print(); print("="*82); print("[Phase2] 区间算术逐终端箱验证（端点精确有理；π 用区间）"); print("="*82)
PIIV = mp.iv.pi
def ivq(fr): return mp.iv.mpf(fr.numerator)/mp.iv.mpf(fr.denominator)

def cos_min_lb(k, off_iv, a, b):
    """min_{t∈[a,b]} cos(k*(off+t)) 的严格下界；off_iv 为区间（π/3 或 π/2）"""
    XI = k*(off_iv + mp.iv.mpf([ivq(a).a, ivq(b).b]))
    Y  = XI/PIIV
    y0,y1 = Y.a, Y.b
    # 紧检测：区间 [y0,y1] 内是否存在奇数整数（y0,y1 由外区间得到，双向保守）
    m = mp.ceil(y0); j0 = m if (int(m) % 2 != 0) else m + 1
    if j0 <= y1:
        return -1.0
    c_lo = mp.iv.cos(k*(off_iv + ivq(a)))
    c_hi = mp.iv.cos(k*(off_iv + ivq(b)))
    return float(min(c_lo.a, c_hi.a))

t1=time.time(); nviol=0; miniv=1e30; vb=None
P3I = PIIV/mp.iv.mpf(3); P2I = PIIV/mp.iv.mpf(2)
for (a1,b1,a2,b2,v) in term:
    best=-9.0
    for k in range(1,KMAX+1):
        m1 = cos_min_lb(k,P3I,a1,b1); m2 = cos_min_lb(k,P2I,a2,b2)
        best = max(best, 2*m1+m2)
    if best<miniv: miniv,vb = best,(a1,b1,a2,b2)
    if best<1.0: nviol+=1
print(f"  终端箱 {len(term):,}：违反数={nviol}   区间下界最小值={miniv:.9f} (余量 {miniv-1:+.4e})  {time.time()-t1:.2f}s")
print(f"  最小值箱 δ1∈[{float(vb[0]):.6f},{float(vb[1]):.6f}] δ2∈[{float(vb[2]):.6f},{float(vb[3]):.6f}]")

# ---------------- Phase 3 ----------------
vt = sum((b-a)*(d-c) for a,b,c,d,v in term); vd = sum((b-a)*(d-c) for a,b,c,d in disc)
vdm = (B1-A1)*(B2-A2)
print(); print("="*82); print("[Phase3] 精确有理体积核对"); print("="*82)
print(f"  域体积={float(vdm):.12f}  终端={float(vt):.12f}  丢弃={float(vd):.12f}  和={float(vt+vd):.12f}")
print(f"  体积精确相等？ {vt+vd==vdm}   ⟹ 铺砌无孔无叠 ✓" if vt+vd==vdm else "  ⚠️ 不等")
print()
ok = (nviol==0)
print("【结论】" + ("远场 F ≥ 1（严格，区间算术认证）✓" if ok else "未通过 ✗"))
print("  结合 C-197 局部引理 ⟹ 全域 F ≥ 1 ⟹ g_2(10) ≥ 1")
print("  候选点 (π/3, π/2) 给 F = 1 ⟹ 【g_2(10) = 1】" if ok else "")
json.dump(dict(nterm=len(term),ndisc=len(disc),maxdepth=maxd,float_min=minv,
               iv_min=miniv,violations=nviol,volume_exact=bool(vt+vd==vdm),
               boundary_layer=nz,bulk=len(term)-nz), open("/tmp/c199_result.json","w"), indent=2, default=float)
