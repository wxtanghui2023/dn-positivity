#!/usr/bin/env python3
"""D-B：11×11 Krawczyk 严格认证（阻尼 M=3，A={1,2,3,4,5,15}）
四门独立输出：B1 existence(K⊂int X) / B2 uniqueness(‖I−YJ‖<1) / B3 λ-positivity / B4 six-way tie(唯一根满足)
纪律：B4 不得写成"X0 内六值恒等"；正确表述＝Krawczyk 认证唯一根 z0，且该根满足五条 tie 方程
"""
import mpmath as mp, json
mp.mp.dps=60
SLK=mp.mpf('1e-45')
K=15; A=[1,2,3,4,5,15]
PIV=mp.pi; TWOPI=2*PIV
class Iv:
    __slots__=('a','b')
    def __init__(s,a,b): s.a=min(a,b)-SLK; s.b=max(a,b)+SLK
    @staticmethod
    def pt(x): return Iv(x,x)
    @staticmethod
    def _iv(o): return o if isinstance(o,Iv) else Iv.pt(o)
    def __add__(s,o): o=Iv._iv(o); return Iv(s.a+o.a,s.b+o.b)
    __radd__=__add__
    def __neg__(s): return Iv(-s.b,-s.a)
    def __sub__(s,o): o=Iv._iv(o); return Iv(s.a-o.b,s.b-o.a)
    def __rsub__(s,o): return Iv._iv(o).__sub__(s)
    def __mul__(s,o):
        o=Iv._iv(o); c=[s.a*o.a,s.a*o.b,s.b*o.a,s.b*o.b]; return Iv(min(c),max(c))
    __rmul__=__mul__
    def mid(s): return (s.a+s.b)/2
    def wid(s): return s.b-s.a
def cosr(k,c):
    a=k*c.a; b=k*c.b
    mn=min(mp.cos(a),mp.cos(b)); mx=max(mp.cos(a),mp.cos(b))
    for j in range(int(mp.floor(a/PIV)),int(mp.ceil(b/PIV))+1):
        t=PIV*j
        if a<=t<=b and j%2!=0: mn=mp.mpf(-1)
    for j in range(int(mp.floor(a/TWOPI)),int(mp.ceil(b/TWOPI))+1):
        t=TWOPI*j
        if a<=t<=b: mx=mp.mpf(1)
    return Iv(mn,mx)
def sinr(k,c):
    a=k*c.a; b=k*c.b
    mn=min(mp.sin(a),mp.sin(b)); mx=max(mp.sin(a),mp.sin(b)); HP=PIV/2
    for j in range(int(mp.floor((a-HP)/TWOPI)),int(mp.ceil((b-HP)/TWOPI))+1):
        t=TWOPI*j+HP
        if a<=t<=b: mx=mp.mpf(1)
    for j in range(int(mp.floor((a-3*HP)/TWOPI)),int(mp.ceil((b-3*HP)/TWOPI))+1):
        t=TWOPI*j+3*HP
        if a<=t<=b: mn=mp.mpf(-1)
    return Iv(mn,mx)
def rk(rI,k):           # r^k（r≥0 单调）
    lo=max(rI.a,mp.mpf(0)); return Iv(lo**k, max(rI.b,mp.mpf(0))**k) if lo>=0 else Iv(mp.mpf(0),max(abs(rI.a),abs(rI.b))**k)
def Sr(k,z):            # S_k 的区间
    r2,r3,p1,p2,p3=z[0],z[1],z[2],z[3],z[4]
    return cosr(k,p1)+rk(r2,k)*cosr(k,p2)+rk(r3,k)*cosr(k,p3)
def gr(k,z):
    r2,r3,p1,p2,p3=z[0],z[1],z[2],z[3],z[4]; ki=Iv.pt(k)
    return [ ki*rk(r2,k-1)*cosr(k,p2), ki*rk(r3,k-1)*cosr(k,p3),
            -ki*sinr(k,p1), -ki*rk(r2,k)*sinr(k,p2), -ki*rk(r3,k)*sinr(k,p3) ]
def H(z):
    ll=z[5:]; out=[]
    for j in range(5):
        acc=Iv.pt(0)
        for i,k in enumerate(A): acc=acc+ll[i]*gr(k,z)[j]
        out.append(acc)
    S0=Sr(A[0],z)
    for i in range(1,6): out.append(S0-Sr(A[i],z))
    out.append(sum(ll)-Iv.pt(1))
    return out
def Jm(z):
    ll=z[5:]; M=[[Iv.pt(0) for _ in range(11)] for _ in range(11)]
    # 行 0..4：Σλ_k ∂²S_k
    for j in range(5):
        acc=Iv.pt(0)
        for i,k in enumerate(A):
            ki=Iv.pt(k); r2,r3,p1,p2,p3=z[0],z[1],z[2],z[3],z[4]
            if j==0: h=ki*Iv.pt(k-1)*rk(r2,k-2)*cosr(k,p2)
            elif j==1: h=ki*Iv.pt(k-1)*rk(r3,k-2)*cosr(k,p3)
            elif j==2: h=-(ki*ki)*cosr(k,p1)
            elif j==3: h=-(ki*ki)*rk(r2,k)*cosr(k,p2)
            else: h=-(ki*ki)*rk(r3,k)*cosr(k,p3)
            acc=acc+ll[i]*h
        M[j][j]=acc
        for i,k in enumerate(A): M[j][5+i]=gr(k,z)[j]
    # 行 5..9：S_{A[0]} − S_{A[i]} 对配置变量的导数
    for r in range(5):
        g0=gr(A[0],z); gi=gr(A[r+1],z)
        for j in range(5): M[5+r][j]=g0[j]-gi[j]
    # 行 10：Σλ−1
    for i in range(6): M[10][5+i]=Iv.pt(1)
    return M
# 数值层
def Sn(k,x):
    r2,r3,p1,p2,p3=x
    return mp.cos(k*p1)+r2**k*mp.cos(k*p2)+r3**k*mp.cos(k*p3)
def gn(k,x):
    r2,r3,p1,p2,p3=x
    return [ k*r2**(k-1)*mp.cos(k*p2), k*r3**(k-1)*mp.cos(k*p3),
            -k*mp.sin(k*p1), -k*r2**k*mp.sin(k*p2), -k*r3**k*mp.sin(k*p3) ]
def Hn(z):
    x=z[:5]; ll=z[5:]; out=[]
    for j in range(5): out.append(sum(ll[i]*gn(k,x)[j] for i,k in enumerate(A)))
    S0=Sn(A[0],x)
    out+= [S0-Sn(A[i],x) for i in range(1,6)]
    out+= [sum(ll)-1]
    return out
def Jn(z):
    x=z[:5]; ll=z[5:]; M=mp.zeros(11,11)
    for j in range(5):
        for i,k in enumerate(A):
            r2,r3,p1,p2,p3=x
            if j==0: h=k*(k-1)*r2**(k-2)*mp.cos(k*p2)
            elif j==1: h=k*(k-1)*r3**(k-2)*mp.cos(k*p3)
            elif j==2: h=-k*k*mp.cos(k*p1)
            elif j==3: h=-k*k*r2**k*mp.cos(k*p2)
            else: h=-k*k*r3**k*mp.cos(k*p3)
            M[j,j]+=ll[i]*h
            M[j,5+i]=gn(k,x)[j]
    for r in range(5):
        g0=gn(A[0],x); gi=gn(A[r+1],x)
        for j in range(5): M[5+r,j]=g0[j]-gi[j]
    for i in range(6): M[10,5+i]=1
    return M
z0=[mp.mpf('0.79051323395036623846'),mp.mpf('0.83020729481457293027'),
    mp.mpf('0.10911016482862308881')*PIV,mp.mpf('0.8206637095202066754')*PIV,
    mp.mpf('0.46171937101861024265')*PIV,
    mp.mpf('0.200053655481'),mp.mpf('0.178487601084'),mp.mpf('0.165510017089'),
    mp.mpf('0.194818621224'),mp.mpf('0.11186012226'),mp.mpf('0.149269982863')]   # 顺序对齐 A=[1,2,3,4,5,15] ✓
print("="*100); print("D-B：11×11 Krawczyk 严格认证（A={1,2,3,4,5,15}）"); print("="*100)
print(f"基点残差 max|H| = {mp.nstr(max(abs(t) for t in Hn(z0)),5)}")
Y=Jn(z0)**-1
def kraw(r):
    X=[Iv(z0[i]-r,z0[i]+r) for i in range(11)]
    m=[Iv.pt(z0[i]) for i in range(11)]
    Hm=H(m); JX=Jm(X)
    R=[[Iv.pt(1 if i==j else 0) for j in range(11)] for i in range(11)]
    for i in range(11):
        for j in range(11):
            acc=Iv.pt(0)
            for l in range(11): acc=acc+Iv.pt(Y[i,l])*JX[l][j]
            R[i][j]=Iv.pt(1 if i==j else 0)-acc
    K=[]
    for i in range(11):
        acc=Iv.pt(0)
        for j in range(11): acc=acc+Iv.pt(Y[i,j])*Hm[j]
        v=Iv.pt(z0[i])-acc
        for j in range(11): v=v+R[i][j]*(X[j]-Iv.pt(z0[j]))
        K.append(v)
    nrm=max(sum(max(abs(R[i][j].a),abs(R[i][j].b)) for j in range(11)) for i in range(11))
    return X,K,R,nrm
print(f"\n{'r0':>10} {'B1 K⊂intX':>10} {'B2 ‖I−YJ‖<1':>14} {'B3 λmin_lo':>14} {'B4 tie 含 0':>12}")
res={}
for rr in ('1e-4','1e-6','1e-8','1e-10','1e-12'):
    r=mp.mpf(rr); X,K,R,nrm=kraw(r)
    B1=all(K[i].a>X[i].a and K[i].b<X[i].b for i in range(11))
    B2=nrm<1
    lamlo=min(K[5+i].a for i in range(6))
    B3=lamlo>0
    HX=H(X); B4=all(HX[5+i].a<=0<=HX[5+i].b for i in range(5))
    print(f"{rr:>10} {str(B1):>10} {mp.nstr(nrm,6):>14} {mp.nstr(lamlo,8):>14} {str(B4):>12}")
    res[rr]=dict(B1=bool(B1),B2=bool(nrm<1),B3=bool(lamlo>0),B4=bool(B4),nrm=mp.nstr(nrm,8),lamlo=mp.nstr(lamlo,10),
                 wid=max(K[i].wid() for i in range(11)))
best=[k for k,v in res.items() if v['B1'] and v['B2'] and v['B3'] and v['B4']]
print(f"\n【四门同时通过的档】= {best}")
if best:
    r=mp.mpf(best[0]); X,K,R,nrm=kraw(r)
    print(f"\n⭐ 采纳 r0={best[0]}：终盒最大宽 = {mp.nstr(max(K[i].wid() for i in range(11)),6)}")
    for i,nm in enumerate(('r2','r3','φ1','φ2','φ3','λ1','λ2','λ3','λ4','λ5','λ15')):
        print(f"   {nm:>4}: [{mp.nstr(K[i].a,20)}, {mp.nstr(K[i].b,20)}]  宽 {mp.nstr(K[i].wid(),4)}")
    HX=H(X)
    print(f"\n【B4 表】唯一根满足 tie（区间含 0）: " + ", ".join(f"S{A[0]}−S{A[i+1]}: [{mp.nstr(HX[5+i].a,8)},{mp.nstr(HX[5+i].b,8)}]" for i in range(5)))
    json.dump(dict(r0=best[0], nrm=mp.nstr(nrm,10), lam_lo=mp.nstr(min(K[5+i].a for i in range(6)),12),
                   box=[[mp.nstr(K[i].a,22),mp.nstr(K[i].b,22)] for i in range(11)]), open('/tmp/dB.json','w'), indent=1)
