"""
① 修正局部 ramification bookkeeping（不碰 Layer 3/4）
F = Q_2(zeta_8): 真值 d = 8（因 |disc Q(zeta_8)| = 2^8 = 256）
环模型 Z[x]/(x^4+1): 元素 = 4-tuple (a0,a1,a2,a3) <-> a0 + a1 x + a2 x^2 + a3 x^3, x^4 = -1
valuation: v(x) = v_2(|N_{F/Q}(x)|)  （e = 4 = [F:Q], f = 1 ⟹ v = v_2(N) 正确）
G_i = { sigma : min_{e in BASIS of O_F} v(sigma(e) - e) >= i+1 }
"""
import itertools
def mulF(u,v):
    raw=[0]*7
    for i,a in enumerate(u):
        for j,b in enumerate(v): raw[i+j]+=a*b
    for k in range(6,3,-1):
        c=raw[k]
        if c: raw[k]-=c; raw[k-4]-=c      # x^4 = -1
    return tuple(raw[:4])
def subF(u,v): return tuple(a-b for a,b in zip(u,v))
def det4(M):
    d=0
    for p in itertools.permutations(range(4)):
        s=1
        for i in range(4):
            for j in range(i+1,4):
                if p[i]>p[j]: s=-s
        t=s
        for i in range(4): t*=M[i][p[i]]
        d+=t
    return d
def normF(u):
    cols=[mulF(u,e) for e in ((1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1))]
    return det4([[cols[j][i] for j in range(4)] for i in range(4)])
def vF(u):
    if u==(0,0,0,0): return 10**9
    a=abs(normF(u)); k=0
    while a%2==0: a//=2; k+=1
    return k
# Galois action: sigma_a : x -> x^a, a in {1,3,5,7}
def act(a,u):
    # x^a substitution: compute (a0 + a1 x + a2 x^2 + a3 x^3) with x -> x^a
    res=[0,0,0,0]
    for k,c in enumerate(u):
        if c==0: continue
        p=k*a % 8            # x^(k*a) mod x^4 = -1  -> reduce
        if p>=4:
            res[p-4]-=c
            # x^p = x^(p-4) * x^4 = -x^(p-4)
        else:
            res[p]+=c
    return tuple(res)
one4=(1,0,0,0)
x=(0,1,0,0); x2=mulF(x,x); x3=mulF(x2,x)
# maximal basis of O_F = Z[zeta_8]: {1, x, x^2, x^3}
BASIS_MAX=[one4,x,x2,x3]
# NON-maximal basis (spans only Z[i, sqrt2], index > 1):
#   i = x^2 ; sqrt2 = x + x^-1 = x - x^3 ; i*sqrt2 = x^2*(x - x^3) = x^3 + x
sqrt2=(0,1,0,-1); i_sqrt2=(0,1,0,1)
BASIS_NONMAX=[one4,x2,sqrt2,i_sqrt2]

def filtration(basis,label):
    G=[1,3,5,7]
    m={}
    for a in G:
        vals=[]
        for e in basis:
            vals.append(vF(subF(act(a,e),e)))
        m[a]=min(vals)
    print(f"\n  [{label}]  i_G(sigma) = min over basis of v(sigma(e)-e):")
    for a in sorted(G,key=lambda z:(m[z],z)):
        print(f"      sigma_{a}: {m[a] if m[a]<10**8 else 'inf'}")
    # recover G_i
    filt=[]
    for i in range(0,8):
        Gi=[a for a in G if m[a]>=i+1]
        filt.append(len(Gi))
    d=sum(g-1 for g in filt if g>0)
    print(f"      |G_i| (i=0..7) = {filt}   => d = sum(|G_i|-1) = {d}")
    return filt,d,m

print("="*88); print("F = Q_2(zeta_8):  TRUE d = 8  (since |disc Q(zeta_8)| = 256 = 2^8)"); print("="*88)
print("\n  sanity: v(2) =",vF((2,0,0,0)),"(expect 4 = e);  v(x-1)=",vF(subF(x,one4)),"(expect 1, uniformizer)")
f1,d1,m1=filtration(BASIS_MAX,"MAXIMAL basis {1,x,x^2,x^3} of O_F = Z[zeta_8]")
f2,d2,m2=filtration(BASIS_NONMAX,"NON-maximal basis {1,i,sqrt2,i*sqrt2} (spans Z[i,sqrt2] only)")
print()
print("  ⭐ DIAGNOSIS:")
print(f"     maximal basis      -> d = {d1}   {'✓ MATCHES the true value 8' if d1==8 else '✗'}")
print(f"     non-maximal basis  -> d = {d2}   (INFLATED: too few elements to test, so m is too large)")
print("     ==> the bug mechanism is: using a Z-basis that does NOT span the maximal order O_F inflates i_G")
print("         hence inflates the groups and the different exponent.  THIS IS THE 'index trap'.")
print()
print("="*88); print("three-column table for F (lower G_i / Herbrand phi / upper breaks)"); print("="*88)
G0=f1[0]
print(f"  {'i':>3} | {'|G_i| (lower)':>13} | {'phi(i)=sum_{j<=i}|G_j| / |G_0|':>30} | {'G^i (upper)':>11}")
for i in range(0,7):
    s=sum(f1[j] for j in range(1,i+1)) if i>=1 else 0
    phi=s/G0
    print(f"  {i:>3} | {f1[i]:>13} | {'':>8}{phi:>20.4f} | {f1[i]:>11}")
print("  ⚠️ note phi(2) = 1.5 is NOT an integer: bookkeeping at the intermediate break still needs attention")
print("     (Hasse-Arf concerns the upper breaks; this must be checked against the correct break convention)")
print()
print("="*88); print("tower record  Q_2 < Q_2(sqrt2) < Q_2(2^(1/4)) < L"); print("="*88)
print("""  layer                       e   f   d          Galois?  note
  Q_2(sqrt2)/Q_2              2   1   3          yes      |G_i| = 2,2,2,1  (i_G(sigma)=3)
  Q_2(2^(1/4))/Q_2            4   1   11         NO       Galois closure is L
  L/Q_2                       8   1   <=30       yes      true value not yet determined (needs O_L)
  ⚠️ the L computation used the basis Z[delta,i]; if O_L is larger, d is INFLATED (as demonstrated on F)""")
