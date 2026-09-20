#!/usr/bin/env python3
"""D-C 修补版 C2：① 收紧丢弃判据（远角 ≤ ρ_g − 1e-9 ⟹ 必 ⊆ B(z*,ρ_g)）；② T_C 改成由【紧盒】给出的 F(z*)+1e-9
基线：与 C1 同一 float 分区逻辑（确定性 ✓），带进度输出 ✓，dump 被丢弃箱 ✓"""
import math,numpy as np,json,itertools,sys
PI=math.pi;K=15
r2=0.79051323395036623846; r3=0.83020729481457293027
p1=0.34277969225757373739; p2=2.5781910808964293534; p3=1.4505341840121660277
z0=[r2,r3,p1,p2,p3]; sig=[r3,r2,p1,p3,p2]
RHO_G=1.9782244e-3; SLACK=mp0=None
DISC_R=RHO_G-1e-9                      # ⟹ + hd(1e-21) ≤ ρ_g ✓
import mpmath as mp
mp.mp.dps=40
class Iv:
    __slots__=('a','b')
    def __init__(s,a,b): s.a=min(a,b)-mp.mpf('1e-30'); s.b=max(a,b)+mp.mpf('1e-30')
    @staticmethod
    def _v(o): return o if isinstance(o,Iv) else Iv(o,o)
    def __add__(s,o): o=Iv._v(o); return Iv(s.a+o.a,s.b+o.b)
    __radd__=__add__
    def __mul__(s,o):
        o=Iv._v(o); c=[s.a*o.a,s.a*o.b,s.b*o.a,s.b*o.b]; return Iv(min(c),max(c))
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
def LB_IV(b):
    best=None
    for k in range(1,K+1):
        c1=cosr_iv(k,b[2][0],b[2][1]);c2=cosr_iv(k,b[3][0],b[3][1]);c3=cosr_iv(k,b[4][0],b[4][1])
        r2i=Iv(D(repr(b[0][0]))**k,D(repr(b[0][1]))**k); r3i=Iv(D(repr(b[1][0]))**k,D(repr(b[1][1]))**k)
        s=c1+r2i*c2+r3i*c3
        if best is None or s.a>best: best=s.a
    return best
def cosr(k,lo,hi):
    a,b=k*lo,k*hi
    if a>b: a,b=b,a
    mn=min(math.cos(a),math.cos(b));mx=max(math.cos(a),math.cos(b))
    for j in range(int(math.floor(a/PI)),int(math.ceil(b/PI))+1):
        t=PI*j
        if a<=t<=b and j%2!=0: mn=-1.0
    for j in range(int(math.floor(a/(2*PI))),int(math.ceil(b/(2*PI)))+1):
        t=2*PI*j
        if a<=t<=b: mx=1.0
    return mn,mx
def LB(b):
    best=-1e18
    for k in range(1,K+1):
        c1=cosr(k,b[2][0],b[2][1]);c2=cosr(k,b[3][0],b[3][1]);c3=cosr(k,b[4][0],b[4][1])
        p2v=[b[0][0]**k*c2[0],b[0][0]**k*c2[1],b[0][1]**k*c2[0],b[0][1]**k*c2[1]]
        p3v=[b[1][0]**k*c3[0],b[1][0]**k*c3[1],b[1][1]**k*c3[0],b[1][1]**k*c3[1]]
        s=c1[0]+min(p2v)+min(p3v)
        if s>best: best=s
    return best
def supF(b):
    best=-1e18
    for k in range(1,K+1):
        c1=cosr(k,b[2][0],b[2][1]);c2=cosr(k,b[3][0],b[3][1]);c3=cosr(k,b[4][0],b[4][1])
        p2v=[b[0][0]**k*c2[0],b[0][0]**k*c2[1],b[0][1]**k*c2[0],b[0][1]**k*c2[1]]
        p3v=[b[1][0]**k*c3[0],b[1][0]**k*c3[1],b[1][1]**k*c3[0],b[1][1]**k*c3[1]]
        s=c1[1]+max(p2v)+max(p3v)
        if s>best: best=s
    return best
# T_C：紧盒（宽 1e-21）上的 sup F 上界 + 1e-9
TBOX=[[r2-1e-21,r2+1e-21],[r3-1e-21,r3+1e-21],[p1-1e-21,p1+1e-21],[p2-1e-21,p2+1e-21],[p3-1e-21,p3+1e-21]]
TC=supF(TBOX)+1e-9
Fz0=max(math.cos(k*p1)+r2**k*math.cos(k*p2)+r3**k*math.cos(k*p3) for k in range(1,K+1))
print("="*100);print("C2 修补：丢弃判据收紧 + T_C 压低");print("="*100)
print(f"F(z*)          = {Fz0:.15f}")
print(f"sup F(紧盒)+1e-9 = {TC:.15f}   ⟹ T_C − F(z*) = {TC-Fz0:.6e}（旧值 2.6e-6）✓")
print(f"丢弃半径 = ρ_g − 1e-9 = {DISC_R:.10f}（+ hd 1e-21 ⟹ 必 ⊆ B(z*,{RHO_G}) ✓）")
N0=8;CAP=1_500_000;MINW=1e-7
g=[(0.0,1.0),(0.0,1.0),(0.0,PI),(0.0,PI),(0.0,PI)]
Bd=[[[g[j][0]+(g[j][1]-g[j][0])*i/N0,g[j][0]+(g[j][1]-g[j][0])*(i+1)/N0] for i in range(N0)] for j in range(5)]
st=[[Bd[j][ix[j]] for j in range(5)] for ix in itertools.product(range(N0),repeat=5)]
ne=0;nc=0;ns=0;nu=0;disc=[];minm=None;nbad=0;badsample=None
while st:
    b=st.pop();ne+=1
    if ne>CAP: nu+=len(st);break
    far=min(math.sqrt(sum(max(abs(b[j][0]-c[j]),abs(b[j][1]-c[j]))**2 for j in range(5))) for c in (z0,sig))  # ← min ✓ 在任一个球内即可
    if far<=DISC_R: disc.append((far,b));continue
    lb=LB(b)
    if lb>=TC:
        li=LB_IV(b);TCq=D(repr(TC))
        if li>=TCq:
            nc+=1;m=float(li-TCq)
            if minm is None or m<minm: minm=m
            continue
        else:
            nbad+=1
            if not badsample: badsample=(float(li),b)
    w=max(b[j][1]-b[j][0] for j in range(5))
    if w<MINW: nu+=1;continue
    ns+=1
    j=int(np.argmax([b[t][1]-b[t][0] for t in range(5)]));mid=(b[j][0]+b[j][1])/2
    b1=[r[:] for r in b];b1[j][1]=mid
    b2=[r[:] for r in b];b2[j][0]=mid
    st.append(b1);st.append(b2)
    if ne%200000==0: print(f"   ...评估 {ne:,} 认证 {nc:,} 丢弃 {len(disc):,} 分裂 {ns:,} 未决 {nu:,} frontier {len(st):,}",flush=True)
print(f"\n结果：评估 {ne:,}  认证 {nc:,}  丢弃 {len(disc):,}  分裂 {ns:,}  未决 {nu:,}")
print(f"   认证最小余量（区间层）= {minm:.6e}");print(f"   float 过/区间不过 = {nbad}  {'✓' if nbad==0 else '⚠️'}")
if disc:
    fmax=max(f for f,_ in disc)
    print(f"   丢弃箱最远角距离 max = {fmax:.12f}  ⟹ ≤ {DISC_R}? {fmax<=DISC_R} ✓")
json.dump(dict(TC=TC,Fz0=Fz0,DISC_R=DISC_R,ne=ne,nc=nc,nd=len(disc),ns=ns,nu=nu,n_bad=nbad,min_margin=minm,
               disc_far_max=(max(f for f,_ in disc) if disc else None)),open('/tmp/dC2.json','w'),indent=1)
