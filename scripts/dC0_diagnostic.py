#!/usr/bin/env python3
"""D-C 之 C0：float diagnostic（五维混合域 [0,1]^2×[0,π]^3）
纪律：① 排除球＝{z0, σz0} 两点（C_2 对称，非 S3 六点）；② 阻尼乘积用【整体区间乘积】✓（42a）；③ 与球相交的 box 一律 split，不得直接丢
"""
import numpy as np, json, math
PI=np.pi; K=15
z0=np.array([0.79051323395036623846,0.83020729481457293027,
             0.10911016482862308881*PI,0.8206637095202066754*PI,0.461719371018243 if False else 0.46171937101861024265*PI])
rho=1.9782244e-3
def Fv(x):
    r2,r3,p1,p2,p3=x
    return max(math.cos(k*p1)+r2**k*math.cos(k*p2)+r3**k*math.cos(k*p3) for k in range(1,K+1))
def Sall(x):
    r2,r3,p1,p2,p3=x
    return [math.cos(k*p1)+r2**k*math.cos(k*p2)+r3**k*math.cos(k*p3) for k in range(1,K+1)]
# ① 对称性数值核验
sig=np.array([z0[1],z0[0],z0[2],z0[4],z0[3]])
print("="*100); print("C0 diagnostic（阻尼 M=3 全局排除）"); print("="*100)
print(f"① 对称性核验：")
print(f"   F(z0)      = {Fv(z0):.15f}")
print(f"   F(σz0)     = {Fv(sig):.15f}     ⟹ 相等? {abs(Fv(z0)-Fv(sig))<1e-14} ✓（C_2 配对互换 ✓）")
zbad=np.array([z0[0],z0[1],z0[3],z0[2],z0[4]])
print(f"   F(仅换φ1↔φ2) = {Fv(zbad):.15f}   ⟹ 与 F(z0) 差 {abs(Fv(z0)-Fv(zbad)):.6e} ⟹ 【不是对称】✗（证否你的表述 ✓）")
print(f"② 轨道点 = {{z0, σz0}}（2 点 ✓，非 6 点 ✗）")
# ③ 阈值
BX=[(0.79051286581601794606,0.79051360208471453086),(0.83020687425353775941,0.83020771537560810112),
    (0.34277956127726486534,0.34277982323788260943),(2.5781907738197263300,2.5781913879731323768),
    (1.4505338517301991052,1.4505345162941329502)]
supF=max(max(math.cos(k*BX[2][1]),math.cos(k*BX[2][0]))+
         max(BX[0][1]**k*math.cos(k*BX[3][1]), BX[0][1]**k*math.cos(k*BX[3][0]),
             BX[0][0]**k*math.cos(k*BX[3][1]), BX[0][0]**k*math.cos(k*BX[3][0]))+
         max(BX[1][1]**k*math.cos(k*BX[4][1]), BX[1][1]**k*math.cos(k*BX[4][0]),
             BX[1][0]**k*math.cos(k*BX[4][1]), BX[1][0]**k*math.cos(k*BX[4][0])) for k in range(1,K+1))
TC=supF+1e-9
print(f"③ T_C = sup F(X0) + 1e-9 = {TC:.15f}   （F(z0)={Fv(z0):.15f} ⟹ T_C > F(z0)? {TC>Fv(z0)} ✓）")
# ④ LB（整体区间乘积）
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
def LB(box):
    best=-1e18
    for k in range(1,K+1):
        c1=cosr(k,box[2][0],box[2][1])
        c2=cosr(k,box[3][0],box[3][1]); c3=cosr(k,box[4][0],box[4][1])
        p2=[ (box[0][0]**k)*c2[0],(box[0][0]**k)*c2[1],(box[0][1]**k)*c2[0],(box[0][1]**k)*c2[1] ]
        p3=[ (box[1][0]**k)*c3[0],(box[1][0]**k)*c3[1],(box[1][1]**k)*c3[0],(box[1][1]**k)*c3[1] ]
        s=c1[0]+min(p2)+min(p3)
        if s>best: best=s
    return best
def inball(box):
    for c in (z0,sig):
        far=0.0
        for j in range(5):
            far+=max(abs(box[j][0]-c[j]),abs(box[j][1]-c[j]))**2
        if math.sqrt(far)<=rho: return True
    return False
N0=8
g=[(0.0,1.0),(0.0,1.0),(0.0,PI),(0.0,PI),(0.0,PI)]
B=[[[g[j][0]+(g[j][1]-g[j][0])*i/N0, g[j][0]+(g[j][1]-g[j][0])*(i+1)/N0] for i in range(N0)] for j in range(5)]
import itertools
stack=[[B[j][idx[j]] for j in range(5)] for idx in itertools.product(range(N0),repeat=5)]
print(f"\n④ 初始分区 {len(stack):,} 箱（N0={N0}，5 维）")
CAP=2_000_000; MINW=1e-7
ne=0; nc=0; nd=0; ns=0; nu=0; best=None; depth=0
while stack:
    ne+=1
    if ne>CAP: nu+=len(stack); print(f"   ⚠️ 超上限 {CAP:,} ⟹ 停止（未决 {nu:,}）"); break
    box=stack.pop()
    if inball(box): nd+=1; continue
    lb=LB(box)
    if lb>=TC:
        nc+=1
        m=lb-TC
        if best is None or m<best[0]: best=(m,box)
        continue
    w=max(box[j][1]-box[j][0] for j in range(5))
    if w<MINW: nu+=1; continue
    ns+=1
    j=int(np.argmax([box[t][1]-box[t][0] for t in range(5)]))
    mid=(box[j][0]+box[j][1])/2
    b1=[r[:] for r in box]; b1[j][1]=mid
    b2=[r[:] for r in box]; b2[j][0]=mid
    stack.append(b1); stack.append(b2)
    if ne%500000==0: print(f"   ... 评估 {ne:,}  认证 {nc:,}  丢弃 {nd:,}  分裂 {ns:,}  未决 {nu:,}  frontier {len(stack):,}")
print(f"\n⑤ C0 结果：评估 {ne:,}  认证 {nc:,}  球内丢弃 {nd:,}  分裂 {ns:,}  未决 {nu:,}  frontier {len(stack):,}")
if best: print(f"   认证最小余量 = {best[0]:.6e}（箱 {[[round(t,6) for t in r] for r in best[1]]}）")
print(f"   口径：未决={nu} ⟹ {'✓ 无未决（C0 通过，可进 C1 严格版）' if nu==0 else '⚠️ 有未决 ⟹ 需调参'}（注意：C0 是 float，非证书 ✗）")
json.dump(dict(Fz0=Fv(z0),Fsigma=Fv(sig),Fswap_phi=Fv(zbad),TC=TC,ne=ne,nc=nc,nd=nd,ns=ns,nu=nu,
               min_margin=None if not best else best[0], rho=rho), open('/tmp/dC0.json','w'), indent=1)
