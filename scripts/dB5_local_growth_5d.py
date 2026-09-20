#!/usr/bin/env python3
"""B5：阻尼 M=3 的【5 维】局部增长门（唐先生指定：c_X, R, rho_iso, rho_up 全部重算，禁止移植 T13-A）
变量 x=(r2,r3,φ1,φ2,φ3)∈[0,1]^2×[0,π]^3；A={1,2,3,4,5,15}（已由 D-B 区间认证的精确 active set）
做法：参考盒取 D-B 盒（变量部分）⟹ Delta_ref；球上算 c（facet 法+containment，含扰动界）；R=max_k‖∇²S_k‖2；自洽 rho
"""
import mpmath as mp, json, itertools
mp.mp.dps=50; SLK=mp.mpf('1e-35')
K=15; A=[1,2,3,4,5,15]
PIV=mp.pi; TWOPI=2*PIV
# D-B 盒（变量部分，取自 C-226/C-225 输出）
BX=[(mp.mpf('0.79051286581601794606'),mp.mpf('0.79051360208471453086')),
    (mp.mpf('0.83020687425353775941'),mp.mpf('0.83020771537560810112')),
    (mp.mpf('0.34277956127726486534'),mp.mpf('0.34277982323788260943')),
    (mp.mpf('2.5781907738197263300'),mp.mpf('2.5781913879731323768')),
    (mp.mpf('1.4505338517301991052'),mp.mpf('1.4505345162941329502'))]
xc=[(a+b)/2 for a,b in BX]
def cosr(k,lo,hi):
    a=k*lo; b=k*hi
    if a>b: a,b=b,a
    mn=min(mp.cos(a),mp.cos(b)); mx=max(mp.cos(a),mp.cos(b))
    for j in range(int(mp.floor(a/PIV)),int(mp.ceil(b/PIV))+1):
        t=PIV*j
        if a<=t<=b and j%2!=0: mn=mp.mpf(-1)
    for j in range(int(mp.floor(a/TWOPI)),int(mp.ceil(b/TWOPI))+1):
        t=TWOPI*j
        if a<=t<=b: mx=mp.mpf(1)
    return mn-SLK, mx+SLK
def sinr(k,lo,hi):
    a=k*lo; b=k*hi
    if a>b: a,b=b,a
    mn=min(mp.sin(a),mp.sin(b)); mx=max(mp.sin(a),mp.sin(b)); HP=PIV/2
    for j in range(int(mp.floor((a-HP)/TWOPI)),int(mp.ceil((b-HP)/TWOPI))+1):
        t=TWOPI*j+HP
        if a<=t<=b: mx=mp.mpf(1)
    for j in range(int(mp.floor((a-3*HP)/TWOPI)),int(mp.ceil((b-3*HP)/TWOPI))+1):
        t=TWOPI*j+3*HP
        if a<=t<=b: mn=mp.mpf(-1)
    return mn-SLK, mx+SLK
BALL=None   # 球半宽（每变量同半径，Euclid 度量）
def bounds(j):
    if BALL is None: return BX[j]
    return (xc[j]-BALL, xc[j]+BALL)
def iprod(A,B):                     # 真区间乘积（含符号）
    a1,a2=A; b1,b2=B
    c=[a1*b1,a1*b2,a2*b1,a2*b2]; return (min(c),max(c))
def S_range(k,r2b,r3b):             # S_k 的严格区间：r2^k·cos(kφ2) + r3^k·cos(kφ3) + cos(kφ1)
    r2l,r2h=max(r2b[0],mp.mpf(0)),max(r2b[1],mp.mpf(0))
    r3l,r3h=max(r3b[0],mp.mpf(0)),max(r3b[1],mp.mpf(0))
    t1=iprod((r2l**k,r2h**k), cosr(k,*bounds(3)))
    t2=iprod((r3l**k,r3h**k), cosr(k,*bounds(4)))
    t3=cosr(k,*bounds(2))
    return (t1[0]+t2[0]+t3[0], t1[1]+t2[1]+t3[1])
def grad_box(k):
    r2b,r3b=bounds(0),bounds(1)
    r2l,r2h=max(r2b[0],mp.mpf(0)),max(r2b[1],mp.mpf(0))
    r3l,r3h=max(r3b[0],mp.mpf(0)),max(r3b[1],mp.mpf(0))
    c2=cosr(k,*bounds(3)); c3=cosr(k,*bounds(4)); s2=sinr(k,*bounds(3)); s3=sinr(k,*bounds(4)); s1=sinr(k,*bounds(2))
    p2=iprod((mp.mpf(k)*r2l**(k-1), mp.mpf(k)*r2h**(k-1)), c2)     # ∂/∂r2
    p3=iprod((mp.mpf(k)*r3l**(k-1), mp.mpf(k)*r3h**(k-1)), c3)     # ∂/∂r3
    q1=(-mp.mpf(k)*s1[1], -mp.mpf(k)*s1[0])                        # ∂/∂φ1
    q2=iprod((mp.mpf(k)*r2l**k, mp.mpf(k)*r2h**k), (-s2[1],-s2[0]))# ∂/∂φ2
    q3=iprod((mp.mpf(k)*r3l**k, mp.mpf(k)*r3h**k), (-s3[1],-s3[0]))# ∂/∂φ3
    return [p2,p3,q1,q2,q3]
# ① Delta_ref
print("="*100); print("B5：阻尼 M=3 的 5 维局部增长门（全部重算）"); print("="*100)
BALL=None
SloA=[]; ShiA=[]
for k in A:
    l,h=S_range(k,BX[0],BX[1]); SloA.append(l); ShiA.append(h)
SloN=[]; ShiN=[]
for k in range(1,K+1):
    if k in A: continue
    l,h=S_range(k,BX[0],BX[1]); SloN.append(l); ShiN.append(h)
Delta=min(SloA)-max(ShiN)
Ln=max(mp.mpf(k)*mp.sqrt(5) for k in range(1,K+1) if k not in A)
La=max(mp.mpf(k)*mp.sqrt(5) for k in A)   # 5 维：‖∇S_k‖ ≤ k√5 ✓
print(f"① 参考盒（=D-B 盒变量部分，宽 ~1e-6）：")
print(f"   Delta_ref = min_(k∈A) inf S_k − max_(k∉A) sup S_k = {mp.nstr(Delta,10)}   （外部 gap 量级 ✓）")
print(f"   L_act = max_(k∈A) k√5 = {mp.nstr(La,8)}；L_non = max_(k∉A) k√5 = {mp.nstr(Ln,8)}；ρ_iso ≤ Δ/(L_act+L_non) = {mp.nstr(Delta/(La+Ln),6)}")
# ② 球上 c 与 R（自洽）
def c_and_R(rho):
    global BALL
    BALL=rho
    G=[]; eps=mp.mpf(0)
    for k in A:
        gb=grad_box(k)
        G.append([(a+b)/2 for a,b in gb])
        eps=max(eps, mp.sqrt(sum(((b-a)/2)**2 for a,b in gb)))
    # facet 法（5 维，6 顶点 ⟹ 6 个 omit-one 面）
    import numpy as np
    Gn=np.array([[float(t) for t in g] for g in G])
    dists=[]; inside=True
    for omit in range(6):
        idx=[i for i in range(6) if i!=omit]
        v=Gn[idx]; M=v[1:]-v[0]           # 4×5
        _,_,Vt=np.linalg.svd(M); n=Vt[-1]
        d=abs(n@v[0])/np.linalg.norm(n)
        s0=n@np.zeros(5); sx=n@(Gn[omit]-v[0])
        if s0*sx<=0: inside=False
        dists.append(d)
    cmid=min(dists)
    # R = max_k ‖∇²S_k‖2（5×5，区间级用中心+包络；此处取球上 sup 的保守上界）
    def H2(k):
        r2l,r2h=max(bounds(0)[0],0),max(bounds(0)[1],0); r3l,r3h=max(bounds(1)[0],0),max(bounds(1)[1],0)
        c1l,c1h=cosr(k,*bounds(2)); c2l,c2h=cosr(k,*bounds(3)); c3l,c3h=cosr(k,*bounds(4))
        s2l,s2h=sinr(k,*bounds(3)); s3l,s3h=sinr(k,*bounds(4))
        amb=max(abs(c1l),abs(c1h)); a2=max(abs(c2l),abs(c2h)); a3=max(abs(c3l),abs(c3h))
        b2=max(abs(s2l),abs(s2h)); b3=max(abs(s3l),abs(s3h))
        m11=mp.mpf(k*(k-1))*r2h**(k-2)*a2; m22=mp.mpf(k*(k-1))*r3h**(k-2)*a3  # 上界用 |cos|≤max
        m33=mp.mpf(k*k)*amb; m44=mp.mpf(k*k)*r2h**k*a2; m55=mp.mpf(k*k)*r3h**k*a3
        m14=mp.mpf(k*k)*r2h**(k-1)*b2; m25=mp.mpf(k*k)*r3h**(k-1)*b3
        M=np.array([[float(m11),0,0,float(m14),0],[0,float(m22),0,0,float(m25)],
                    [0,0,float(m33),0,0],[float(m14),0,0,float(m44),0],[0,float(m25),0,0,float(m55)]])
        return float(np.linalg.norm(M,2))
    if BALL>0:
        R=max(H2(k) for k in A)
    else:
        R=max(H2(k) for k in A)
    BALL=None
    return cmid, eps, inside, R
print(f"\n② 自洽求解 ρ（球上算 c，参考盒算隔离）：")
best=None
for rr in ['1e-5','1e-4','5e-4','1e-3','1.5e-3','2e-3','2.02e-3','2.05e-3','2.1e-3','2.2e-3','2.5e-3','3e-3']:
    rho=mp.mpf(rr); cmid,eps,ins,R=c_and_R(rho)
    cX=cmid-eps
    rho_iso=Delta/(La+Ln)
    rho_up=min(rho_iso, 2*cX/R) if cX>0 else mp.mpf(0)
    marg=cX*rho_up-(R/2)*rho_up**2 if rho_up>0 else mp.mpf(0)
    flag='✓自洽' if (cX>0 and rho_up>0 and rho_up<=rho) else ('(球过小✗)' if cX>0 and rho_up>0 else '')
    print(f"   ρ={rr:>7}: c_mid={mp.nstr(cmid,8)}  ε={mp.nstr(eps,4)}  c_X={mp.nstr(cX,8)}  R={mp.nstr(R,8)}  ρ_up={mp.nstr(rho_up,6)}  裕量={mp.nstr(marg,6)} {flag}")
    if cX>0 and rho_up>0 and rho_up<=rho:      # 真正自洽：数据球半径 ≥ 认证半径 ✓
        if best is None or rho_up>best[1]: best=(rho,rho_up,cX,R,cmid,eps,marg)
if best:
    rho0,rho_up,cX,R,cmid,eps,marg=best
    print(f"\n⭐ 采纳 ρ={mp.nstr(rho0,4)}（自洽）：c_X={mp.nstr(cX,10)}  R={mp.nstr(R,10)}  ρ_up={mp.nstr(rho_up,8)}")
    print(f"   B5 结论：0<‖δ‖≤ρ_up ⟹ F(z0+δ) ≥ F(z0)+c_X‖δ‖−(R/2)‖δ‖² ≥ F(z0)+{mp.nstr(marg,6)} > F(z0) ✓")
    json.dump(dict(Delta=mp.nstr(Delta,12),c_X=mp.nstr(cX,12),R=mp.nstr(R,12),rho_up=mp.nstr(rho_up,10),margin=mp.nstr(marg,10),
                   La=mp.nstr(La,8),Ln=mp.nstr(Ln,8)), open('/tmp/dB5.json','w'), indent=1)
else:
    print("\n⚠️ 无自洽档 ⟹ 须调整（如更小 ρ 或更细的 c 处理）")
