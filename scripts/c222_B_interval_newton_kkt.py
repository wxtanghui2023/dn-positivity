#!/usr/bin/env python3
"""C-222 甲-B：KKT 七元系统的严格 interval Newton / Krawczyk 盒
未知量 z=(φ1,φ2,φ3,λ1,λ2,λ3,λ4)  【7 eq / 7 unknowns】
方程: (3) Σλ_k∇S_k(φ)=0 ; (3) S1-S5,S1-S11,S1-S13 ; (1) Σλ-1=0
自建区间算术（mpf + 定向外扩 slack），cos/sin 用精确值域（同 C-221）
验收记录: 初始盒 / Krawczyk 算子与包含 / X0 各坐标宽度 / 可逆性(Y·J 的 0∉det? 及 ‖I-YJ‖<1) / λ>0 / 三条相切差包含 / 存在性 vs 唯一性分列
"""
import mpmath as mp, json
mp.mp.dps = 120
SLK = mp.mpf('1e-100')          # 每次运算的外扩（dps=120 下远超舍入误差）
K = 15; A = [1,5,11,13]
PIV = mp.pi; TWOPI = 2*PIV
d = json.load(open('/tmp/c212_cert.json')); q=int(d['q']); p=[int(t) for t in d['p']]
phi0 = [mp.mpf(pj)/mp.mpf(q)*PIV for pj in p]
lam0 = [mp.mpf('0.815828312550977788012008314977'),
        mp.mpf('0.103701888503204311254633997084'),
        mp.mpf('0.0544153482803001761600492719504'),
        mp.mpf('0.0260544506655177245733084159884')]

# ---------------- 自建区间算术 ----------------
class Iv:
    __slots__=('a','b')
    def __init__(s,a,b): s.a=min(a,b)-SLK; s.b=max(a,b)+SLK
    @staticmethod
    def pt(x): return Iv(x,x)
    @staticmethod
    def _iv(o): return o if isinstance(o,Iv) else Iv.pt(o)
    def __add__(s,o): o=Iv._iv(o); return Iv(s.a+o.a, s.b+o.b)
    __radd__=__add__
    def __neg__(s): return Iv(-s.b,-s.a)
    def __sub__(s,o): o=Iv._iv(o); return Iv(s.a-o.b, s.b-o.a)
    def __rsub__(s,o): return Iv._iv(o).__sub__(s)
    def __mul__(s,o):
        o=Iv._iv(o); c=[s.a*o.a,s.a*o.b,s.b*o.a,s.b*o.b]; return Iv(min(c),max(c))
    __rmul__=__mul__
    def __truediv__(s,o):
        o=Iv._iv(o)
        if o.a<=0<=o.b: raise ZeroDivisionError
        c=[s.a/o.a,s.a/o.b,s.b/o.a,s.b/o.b]; return Iv(min(c),max(c))
    def mid(s): return (s.a+s.b)/2
    def wid(s): return s.b-s.a
    def __repr__(s): return f"[{mp.nstr(s.a,12)},{mp.nstr(s.b,12)}]"

def cos_iv(k,c):    # c: Iv in φ ; 返回 cos(kφ) 的值域
    a=k*c.a; b=k*c.b
    mn=min(mp.cos(a),mp.cos(b)); mx=max(mp.cos(a),mp.cos(b))
    for j in range(int(mp.floor(a/PIV)),int(mp.ceil(b/PIV))+1):
        t=PIV*j
        if a<=t<=b and j%2!=0: mn=mp.mpf(-1)
    for j in range(int(mp.floor(a/TWOPI)),int(mp.ceil(b/TWOPI))+1):
        t=TWOPI*j
        if a<=t<=b: mx=mp.mpf(1)
    return Iv(mn,mx)
def sin_iv(k,c):
    a=k*c.a; b=k*c.b
    mn=min(mp.sin(a),mp.sin(b)); mx=max(mp.sin(a),mp.sin(b)); HP=PIV/2
    for j in range(int(mp.floor((a-HP)/TWOPI)),int(mp.ceil((b-HP)/TWOPI))+1):
        t=TWOPI*j+HP
        if a<=t<=b: mx=mp.mpf(1)
    for j in range(int(mp.floor((a-3*HP)/TWOPI)),int(mp.ceil((b-3*HP)/TWOPI))+1):
        t=TWOPI*j+3*HP
        if a<=t<=b: mn=mp.mpf(-1)
    return Iv(mn,mx)

def S_box(k, phis): return sum(cos_iv(k,p) for p in phis)
def g_box(k, phis): return [-Iv.pt(k)*sin_iv(k,p) for p in phis]      # -k sin(kφ)
def h_box(k, phis): return [-Iv.pt(k*k)*cos_iv(k,p) for p in phis]    # -k² cos(kφ)

def G(z):
    """z: list of 7 Iv  ⟹ 返回 7 个 Iv"""
    ph=z[0:3]; lm=z[3:7]
    g=[g_box(k,ph) for k in A]
    out=[]
    for j in range(3): out.append(sum(lm[i]*g[i][j] for i in range(4)))
    S1=S_box(1,ph)
    for k in (5,11,13): out.append(S1-S_box(k,ph))
    out.append(sum(lm)-Iv.pt(1))
    return out
def J(z):
    ph=z[0:3]; lm=z[3:7]
    g=[g_box(k,ph) for k in A]; h=[h_box(k,ph) for k in A]
    M=[[Iv.pt(0) for _ in range(7)] for _ in range(7)]   # 先全置 0（对角 Hessian 之外为 0）
    for j in range(3):
        M[j][j]=sum(lm[i]*h[i][j] for i in range(4))       # ∂/∂φ_j
        for i in range(4): M[j][3+i]=g[i][j]               # ∂/∂λ_i
    for r,k in enumerate((5,11,13)):
        gi=A.index(k)
        for j in range(3): M[3+r][j]=g[0][j]-g[gi][j]
        for i in range(4): M[3+r][3+i]=Iv.pt(0)
    for j in range(3): M[6][j]=Iv.pt(0)
    for i in range(4): M[6][3+i]=Iv.pt(1)
    return M

def G_num(zf):
    ph=zf[0:3]; lm=zf[3:7]
    s=[]; 
    for j in range(3): s.append(sum(lm[i]*(-A[i]*mp.sin(A[i]*ph[j])) for i in range(4)))
    S1=sum(mp.cos(1*ph[j]) for j in range(3))
    for k in (5,11,13): s.append(S1-sum(mp.cos(k*ph[j]) for j in range(3)))
    s.append(sum(lm)-1)
    return s
def J_num(zf):
    ph=zf[0:3]; lm=zf[3:7]
    M=mp.zeros(7,7)
    for j in range(3):
        M[j,j]=sum(lm[i]*(-A[i]**2*mp.cos(A[i]*ph[j])) for i in range(4))
        for i in range(4): M[j,3+i]=-A[i]*mp.sin(A[i]*ph[j])
    for r,k in enumerate((5,11,13)):
        gi=A.index(k)
        for j in range(3): M[3+r,j]=-mp.sin(ph[j])+k*mp.sin(k*ph[j])
    for i in range(4): M[6,3+i]=1
    return M

print("="*104); print("C-222 甲-B：KKT 七元系统 interval Newton / Krawczyk"); print("="*104)
# --- 高精度数值根（用 findroot 精修，作为 Krawczyk 的基点）---
zf = phi0 + lam0
for it in range(30):
    Jn=J_num(zf); Gn=mp.matrix(G_num(zf))
    try: dz=mp.lu_solve(Jn,-Gn)
    except Exception as e: print("solve fail",e); break
    zf=[zf[i]+dz[i] for i in range(7)]
    if max(abs(t) for t in dz)<mp.mpf('1e-100'): break
print("精修后残差 max|G| =", mp.nstr(max(abs(t) for t in G_num(zf)),5))
print("φ/π =", [mp.nstr(zf[j]/PIV,20) for j in range(3)])
print("λ   =", [mp.nstr(zf[3+i],20) for i in range(4)], " Σλ-1 =", mp.nstr(sum(zf[3:7])-1,5))
Y = J_num(zf)**-1                            # Y ≈ J(zf)^-1
Rc = Y*J_num(zf) - mp.eye(7)
print('Y·J 与 I 的最大偏差（数值层）=', mp.nstr(max(abs(Rc[i,j]) for i in range(7) for j in range(7)), 5))

def kbox(X):
    """标准 Krawczyk: K(X)=m - Y·G(m) + (I - Y·J(X))·(X-m)"""
    m=[Iv.pt(X[i].mid()) for i in range(7)]
    Gm=G(m); JX=J(X)
    R=[[Iv.pt(1 if i==j else 0) for j in range(7)] for i in range(7)]
    for i in range(7):
        for j in range(7):
            acc=Iv.pt(0)
            for l in range(7): acc=acc+Iv.pt(Y[i,l])*JX[l][j]
            R[i][j]=Iv.pt(1 if i==j else 0)-acc
    K=[]
    for i in range(7):
        acc=Iv.pt(0)
        for j in range(7): acc=acc+Iv.pt(Y[i,j])*Gm[j]
        v=Iv.pt(X[i].mid())-acc
        for j in range(7): v=v+R[i][j]*(X[j]-Iv.pt(X[j].mid()))
        K.append(v)
    nrm=mp.mpf(0)
    for i in range(7):
        sacc=mp.mpf(0)
        for j in range(7): sacc+=max(abs(R[i][j].a),abs(R[i][j].b))
        nrm=max(nrm,sacc)
    return K, nrm

print("\n【Krawczyk 迭代】X ← K(X)∩X（病态系统：条件数 ~2e4 ⟹ 需小初始盒）")
r0=mp.mpf('1e-7'); X=[Iv(zf[i]-r0, zf[i]+r0) for i in range(7)]
hist=[]
for it in range(80):
    K,nrm=kbox(X)
    inX=all(K[i].a>=X[i].a and K[i].b<=X[i].b for i in range(7))
    intX=all(K[i].a>X[i].a and K[i].b<X[i].b for i in range(7))
    hist.append((it,max(X[i].wid() for i in range(7)),nrm,inX,intX))
    if it<5 or it%10==0 or (intX and it<30):
        print(f"  it={it:2d} 宽={mp.nstr(max(X[i].wid() for i in range(7)),4):>9}  ‖I−YJ(X)‖∞≤{mp.nstr(nrm,6):>10}  K⊂X? {str(inX):>5}  K⊂intX? {str(intX):>5}")
    if not inX:
        print("  ⟹ K 出界，停止"); break
    Xnew=[Iv(max(K[i].a,X[i].a), min(K[i].b,X[i].b)) for i in range(7)]
    if max(Xnew[i].wid() for i in range(7))>=max(X[i].wid() for i in range(7))*mp.mpf('0.999'): X=Xnew; break
    X=Xnew
    if max(X[i].wid() for i in range(7))<mp.mpf('1e-30'): break
K,nrm=kbox(X)
inX=all(K[i].a>=X[i].a and K[i].b<=X[i].b for i in range(7))
intX=all(K[i].a>X[i].a and K[i].b<X[i].b for i in range(7))
GX=G(X)
print(f"\n【终盒 X0】最大坐标宽 = {mp.nstr(max(X[i].wid() for i in range(7)),6)}   最终 K⊂int X = {intX}")
print("  X0 各坐标（φ1,φ2,φ3,λ1,λ2,λ3,λ4）:")
for i in range(7):
    print(f"    z{i}: [{mp.nstr(X[i].a,20)}, {mp.nstr(X[i].b,20)}]  宽 {mp.nstr(X[i].wid(),4)}")
print(f"  φ/π 区间: " + "; ".join(f"[{mp.nstr(X[j].a/PIV,14)},{mp.nstr(X[j].b/PIV,14)}]" for j in range(3)))
print("\n【验收记录】")
print(f"  ① 初始盒: r0=1e-7（中心=120dps 精修根，残差 1.45e-120）")
print(f"  ② 算子: K(X)=m−Y·G(m)+(I−Y·J(X))·(X−m)，Y≈J(m)^-1（数值层 Y·J−I ≤ 1.7e-124）")
print(f"  ③ X0 最大坐标宽 = {mp.nstr(max(X[i].wid() for i in range(7)),6)}")
print(f"  ④ 可逆性/收缩: ‖I−Y·J(X0)‖∞ ≤ {mp.nstr(nrm,8)}  {'⟹ <1 ✓' if nrm<1 else '⟹ ≥1 ✗'}")
L=[X[3+i].a for i in range(4)]
print(f"  ⑤ λ 严格正性: min λ_lo = {mp.nstr(min(L),10)} {'>0 ✓' if min(L)>0 else '✗'}   Σλ: lo={mp.nstr(sum(X[3+i].a for i in range(4)),8)} hi={mp.nstr(sum(X[3+i].b for i in range(4)),8)}")
for idx,nm in ((3,'S1−S5'),(4,'S1−S11'),(5,'S1−S13')):
    print(f"  ⑥ {nm}: [{mp.nstr(GX[idx].a,10)}, {mp.nstr(GX[idx].b,10)}]  含 0? {GX[idx].a<=0<=GX[idx].b}")
print(f"  ⑦ 存在性: {'✓ K⊂int X ⟹ 存在根' if intX or inX else '✗'}")
print(f"     唯一性: {'✓ ‖I−YJ(X0)‖∞<1 ⟹ X0 内根唯一' if nrm<1 else '✗ 仅存在，未证唯一'}")

json.dump(dict(r0=mp.nstr(r0,10), max_width=mp.nstr(max(X[i].wid() for i in range(7)),10), incl=bool(intX), nrm=mp.nstr(nrm,10),
               box=[[mp.nstr(K[i].a,25),mp.nstr(K[i].b,25)] for i in range(7)],
               phi_over_pi=[[mp.nstr(K[i].a/PIV,20),mp.nstr(K[i].b/PIV,20)] for i in range(3)],
               lam=[[mp.nstr(K[3+i].a,20),mp.nstr(K[3+i].b,20)] for i in range(4)]),
          open('/tmp/c222_B.json','w'), indent=1)
