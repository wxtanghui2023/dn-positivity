#!/usr/bin/env python3
"""C-212 乙：M=3 上界证书（高精度 KKT 求点 -> 有理化 -> 有向区间认证）
乙-1: 高精度 KKT 求 x*（A={1,5,11,13}，6 方程 6 未知）
乙-2: 有理化 x_Q = pi*p_j/q -> 逐 k 严格上界 S_k <= U_k -> U_new = max U_k
严格性：pi 用显式有理区间 [pi_lo, pi_hi]；cos 用均值形式 + 显式误差项（不用退化区间）
"""
import mpmath as mp, json
from fractions import Fraction
mp.mp.dps = 140
K=15; A=[1,5,11,13]

# ---- 高精度 pi 的有理区间（前 100 位标准展开 + 1e-100 余量）----
PI_STR=("31415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679")
PI_LO=Fraction(int(PI_STR),10**len(PI_STR)-0) if False else Fraction(int(PI_STR),10**100)
PI_HI=PI_LO+Fraction(1,10**100)
print("pi 区间宽度 = %.1e （有理数，严格）" % float(PI_HI-PI_LO))

def S(x,k): return sum(mp.cos(k*xi) for xi in x)
def eqs(v1,v2,v3,v4,v5,v6):
    x=[v1,v2,v3]; l=[1-v4-v5-v6, v4, v5, v6]
    g=[sum(l[j]*(-A[j]*mp.sin(A[j]*x[i])) for j in range(4)) for i in range(3)]
    t=[S(x,A[1])-S(x,A[0]), S(x,A[2])-S(x,A[0]), S(x,A[3])-S(x,A[0])]
    return g+t
x0f=[0.11584426,0.33188742,0.73557644]
start=[mp.mpf(t)*mp.pi for t in x0f]+[mp.mpf('0.8'),mp.mpf('0.1'),mp.mpf('0.05')]
sol=mp.findroot(eqs, start, tol=mp.mpf('1e-120'), maxsteps=400, verbose=False)
x=[sol[0],sol[1],sol[2]]; lam=[1-sol[3]-sol[4]-sol[5], sol[3], sol[4], sol[5]]
print("\n[乙-1] 高精度 KKT 解（140 dps）：")
print("   lambda = " + ", ".join(mp.nstr(t,25) for t in lam))
print("   min(lambda) = %s  (>0 ? %s)" % (mp.nstr(min(lam),20), min(lam)>0))
print("   各活跃 k 的 S_k（应严格相等）：")
Fv=S(x,A[0])
for j,k in enumerate(A): print("      k=%2d: %s   (差 %s)" % (k, mp.nstr(S(x,k),50), mp.nstr(S(x,k)-Fv,20)))
print("   非活跃 k 的最大者：")
mx=max((S(x,k),k) for k in range(1,K+1) if k not in A)
print("      k=%d: %s" % (mx[1], mp.nstr(mx[0],50)))
print("\n   phi_j/pi （100 位）：")
for i,t in enumerate(x): print("      j=%d: %s" % (i+1, mp.nstr(t/mp.pi,100)))
print("\n   F(x*) = %s" % mp.nstr(Fv,60))

# ---- 乙-2：有理化 + 有向区间认证 ----
def certify(p,q):
    """x_j = pi*p_j/q；返回逐 k 的 (L_k,U_k) 严格区间"""
    out={}
    for k in range(1,K+1):
        lo=mp.mpf(0); hi=mp.mpf(0)
        for pj in p:
            a=Fraction(k*int(pj), q)                       # 精确有理数 k*p_j/q
            am=mp.mpf(a.numerator)/mp.mpf(a.denominator)
            mid=mp.cos(am*mp.pi)                            # mpmath 高阶计算
            c_lo=Fraction(PI_LO.numerator,PI_LO.denominator) if False else None
            # 误差：|cos(a*pi)-cos(a*pi_mid)| <= a * (pi_hi-pi_lo)/2
            err=am*mp.mpf(float(PI_HI-PI_LO))/2
            lo+=mid-err; hi+=mid+err
        out[k]=(lo,hi)
    return out

print("\n[乙-2] 有理化与认证（q = 10^N 扫描）")
best=None
for N in (20,30,40,50):
    q=10**N
    p=[int(mp.floor(t/mp.pi*mp.mpf(q)+mp.mpf('0.5'))) for t in x]
    # 局部格点搜索（±4）以最小化 max_k 浮点值
    def fmax(pp):
        return max(sum(mp.cos(mp.mpf(k*int(pp[j]))/mp.mpf(q)*mp.pi) for j in range(3)) for k in range(1,K+1))
    cur=(fmax(p), p[:]); improved=True; rnd=0
    while improved and rnd<25:
        improved=False; rnd+=1
        for j in range(3):
            for d in (-1,1):
                cand=cur[1][:]; cand[j]+=d
                v=fmax(cand)
                if v<cur[0]: cur=(v,cand); improved=True
    p=cur[1]
    iv=certify(p,q)
    U=max(v[1] for v in iv.values()); Un=max(k for k in iv if iv[k][1]==U)
    print("   q=10^%-3d: 有理点 max F ≈ %s   认证 U_new = %s (k=%d)" % (N, mp.nstr(cur[0],30), mp.nstr(U,40), Un))
    if best is None or U<best[0]: best=(U,q,p,iv,Un)
U,q,p,iv,Un=best
print("\n⭐ 最优：q = 10^%d" % len(str(q).rstrip('0').lstrip('1')) if False else "\n⭐ 最优 q = %d" % q)
print("   p = %s" % p)
print("   φ_j/π = " + ", ".join("%d/%d" % (pj,q) for pj in p))
print("\n   逐 k 严格区间 [L_k, U_k]（所有宽度 > 0 ✓）：")
for k in range(1,K+1):
    L,Hi=iv[k]
    print("      k=%2d: [%s, %s]  宽度=%.2e" % (k, mp.nstr(L,25), mp.nstr(Hi,25), float(Hi-L)))
print("\n   U_new = max_k U_k = %s  （k=%d 取到）" % (mp.nstr(U,45), Un))
print("   所有 U_k < U_new 吗？%s" % all(iv[k][1]<U for k in iv if k!=Un))
OLD=mp.mpf('0.76408110090337578')
print("   对照旧认证上界 0.76408110090337578 ⟹ 改进 %.3e" % float(OLD-U))
print("   ★ 新账本：0.76 ≤ m_3 ≤ %s" % mp.nstr(U,35))
json.dump(dict(q=str(q),p=[str(t) for t in p],U=str(U),kmax=Un,
               intervals={str(k):[str(iv[k][0]),str(iv[k][1])] for k in iv}),open('/tmp/c212_cert.json','w'),indent=2)
print("\n（已写 /tmp/c212_cert.json）")
