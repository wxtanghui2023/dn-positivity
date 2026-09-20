#!/usr/bin/env python3
"""D-C 之 C1：严格区间版（两层：float 分区 + 逐终端箱区间复核）
纪律：① 排除球 = {z0, σz0}（C_2）✓；② 阻尼乘积整体区间 ✓（42a）；③ 与球相交的箱一律 split；④ 未决 ≠ 认证
"""
import mpmath as mp, numpy as np, math, json
mp.mp.dps=40; SLK=mp.mpf('1e-30')
PI=math.pi; K=15
z0=[0.79051323395036623846,0.83020729481457293027,0.10911016482862308881*PI,
    0.8206637095202066754*PI,0.46171937101861024265*PI]
sig=[z0[1],z0[0],z0[2],z0[4],z0[3]]
rho=1.9782244e-3
BX=[(0.79051286581601794606,0.79051360208471453086),(0.83020687425353775941,0.83020771537560810112),
    (0.34277956127726486534,0.34277982323788260943),(2.5781907738197263300,2.5781913879731323768),
    (1.4505338517301991052,1.4505345162941329502)]
def cosr(k,lo,hi):
    a,b=k*lo,k*hi
    if a>b: a,b=b,a
    mn=min(math.cos(a),math.cos(b)); mx=max(math.cos(a),math.cos(b))
    for j in range(int(math.floor(a/PI)),int(math.ceil(b/PI))+1):
        t=PI*j
        if a<=t<=b and j%2!=0: mn=-1.0
    for j in range(int(math.floor(a/(2*PI))),int(math.ceil(b/(2*PI)))+1):
        t=2*PI*j
        if a<=t<=b: mx=1.0
    return mn,mx
def LB_float(box):
    best=-1e18
    for k in range(1,K+1):
        c1=cosr(k,box[2][0],box[2][1]); c2=cosr(k,box[3][0],box[3][1]); c3=cosr(k,box[4][0],box[4][1])
        p2=[box[0][0]**k*c2[0],box[0][0]**k*c2[1],box[0][1]**k*c2[0],box[0][1]**k*c2[1]]
        p3=[box[1][0]**k*c3[0],box[1][0]**k*c3[1],box[1][1]**k*c3[0],box[1][1]**k*c3[1]]
        s=c1[0]+min(p2)+min(p3)
        if s>best: best=s
    return best
def supF_float(box):
    best=-1e18
    for k in range(1,K+1):
        c1=cosr(k,box[2][0],box[2][1]); c2=cosr(k,box[3][0],box[3][1]); c3=cosr(k,box[4][0],box[4][1])
        p2=[box[0][0]**k*c2[0],box[0][0]**k*c2[1],box[0][1]**k*c2[0],box[0][1]**k*c2[1]]
        p3=[box[1][0]**k*c3[0],box[1][0]**k*c3[1],box[1][1]**k*c3[0],box[1][1]**k*c3[1]]
        s=c1[1]+max(p2)+max(p3)
        if s>best: best=s
    return best
supX0=supF_float(BX); TC=supX0+1e-9
print("="*100); print("C1 严格区间版（D-C）"); print("="*100)
print(f"T_C = sup F(X0) + 1e-9 = {TC:.15f}")
# ---- 区间层 ----
class Iv:
    __slots__=('a','b')
    def __init__(s,a,b): s.a=min(a,b)-SLK; s.b=max(a,b)+SLK
    @staticmethod
    def pt(x): return Iv(x,x)
    @staticmethod
    def _iv(o): return o if isinstance(o,Iv) else Iv.pt(o)
    def __add__(s,o): o=Iv._iv(o); return Iv(s.a+o.a,s.b+o.b)
    __radd__=__add__
    def __mul__(s,o):
        o=Iv._iv(o); c=[s.a*o.a,s.a*o.b,s.b*o.a,s.b*o.b]; return Iv(min(c),max(c))
    __rmul__=__mul__
D=mp.mpf
def cosr_iv(k,lo,hi):
    a=D(repr(k*lo)); b=D(repr(k*hi))
    if a>b: a,b=b,a
    mn=min(mp.cos(a),mp.cos(b)); mx=max(mp.cos(a),mp.cos(b))
    for j in range(int(mp.floor(a/mp.pi)),int(mp.ceil(b/mp.pi))+1):
        t=mp.pi*j
        if a<=t<=b and j%2!=0: mn=D(-1)
    for j in range(int(mp.floor(a/(2*mp.pi))),int(mp.ceil(b/(2*mp.pi)))+1):
        t=2*mp.pi*j
        if a<=t<=b: mx=D(1)
    return Iv(mn,mx)
def LB_iv(box):
    best=None
    for k in range(1,K+1):
        c1=cosr_iv(k,box[2][0],box[2][1]); c2=cosr_iv(k,box[3][0],box[3][1]); c3=cosr_iv(k,box[4][0],box[4][1])
        r2=Iv(D(repr(box[0][0]))**k, D(repr(box[0][1]))**k)
        r3=Iv(D(repr(box[1][0]))**k, D(repr(box[1][1]))**k)
        s=c1+r2*c2+r3*c3
        if best is None or s.a>best: best=s.a
    return best
def inball(box):
    for c in (z0,sig):
        far=0.0
        for j in range(5): far+=max(abs(box[j][0]-c[j]),abs(box[j][1]-c[j]))**2
        if math.sqrt(far)<=rho: return True
    return False
N0=8; CAP=1_500_000; MINW=1e-7
import itertools
g=[(0.0,1.0),(0.0,1.0),(0.0,PI),(0.0,PI),(0.0,PI)]
Bnd=[[[g[j][0]+(g[j][1]-g[j][0])*i/N0, g[j][0]+(g[j][1]-g[j][0])*(i+1)/N0] for i in range(N0)] for j in range(5)]
stack=[[Bnd[j][idx[j]] for j in range(5)] for idx in itertools.product(range(N0),repeat=5)]
ne=0;nc=0;nd=0;ns=0;nu=0;bad=[];minm=None;minb=None
while stack:
    box=stack.pop(); ne+=1
    if ne>CAP: nu+=len(stack); break
    if inball(box): nd+=1; continue
    lf=LB_float(box)
    if lf>=TC:
        li=LB_iv(box)                      # ← 严格复核
        if li>=D(repr(TC)):
            nc+=1
            m=float(li-D(repr(TC)))
            if minm is None or m<minm: minm=m; minb=box
            continue
        else:
            bad.append((lf,float(li),box))  # float 通过但区间不通过 ⟹ 需再分裂
    w=max(box[j][1]-box[j][0] for j in range(5))
    if w<MINW: nu+=1; continue
    ns+=1
    j=int(np.argmax([box[t][1]-box[t][0] for t in range(5)]))
    mid=(box[j][0]+box[j][1])/2
    b1=[r[:] for r in box]; b1[j][1]=mid
    b2=[r[:] for r in box]; b2[j][0]=mid
    stack.append(b1); stack.append(b2)
print(f"\n结果：评估 {ne:,}  认证(区间) {nc:,}  球内丢弃 {nd:,}  分裂 {ns:,}  未决 {nu:,}  frontier {len(stack):,}")
print(f"   float 通过但区间不通过 = {len(bad):,}  {'✓' if not bad else '⚠️'}")
if minm is not None: print(f"   认证最小余量（区间层）= {minm:.6e}")
print(f"   口径：未决={nu} ⟹ {'✓ D-C PASS（区间层严格）' if nu==0 and not bad else '⚠️ 未达'}")
json.dump(dict(TC=TC,ne=ne,nc=nc,nd=nd,ns=ns,nu=nu,n_bad=len(bad),min_margin=minm,rho=rho),
          open('/tmp/dC1.json','w'), indent=1)
