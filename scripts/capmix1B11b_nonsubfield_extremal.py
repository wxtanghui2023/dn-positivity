## CAP-MIX-1B · B11.1/2: 非子域极值分析 + E_{1/2} 反例搜索
import itertools
from math import gcd as igcd
exec(open("scripts/capmix1i_case4_and_falsewall.py").read().split("def main()")[0])
def ord2(d):
    o=1;x=2%d
    while x!=1: x=x*2%d;o+=1
    return o
def issub(d):
    k=1
    while 2**k-1<=d:
        if 2**k-1==d: return True
        k+=1
    return False
def main():
    rows=[];out=open("out/capmix1B11b_nonsub.txt","w")
    for n in range(3,15):
        q=2**n
        if q>16384: continue
        _,tomul=mk(2,n)
        els=[tuple((i//(2**k))%2 for k in range(n)) for i in range(q)]
        enc={e:i for i,e in enumerate(els)}
        one=enc[(1,)+(0,)*(n-1)]
        addi=lambda a,b: enc[tuple((x+y)%2 for x,y in zip(els[a],els[b]))]
        muli=lambda a,b: enc[tomul(els[a],els[b])]
        def powi(a,e):
            r=one;b=a
            while e:
                if e&1:r=muli(r,b)
                b=muli(b,b);e>>=1
            return r
        M=q-1;prs=[];t=2
        while t*t<=M:
            if M%t==0:
                prs.append(t)
                while M%t==0: M//=t
            t+=1
        if M>1: prs.append(M)
        gen=None
        for e in range(1,q):
            if all(powi(e,(q-1)//pr)!=one for pr in prs): gen=e;break
        for d in divs(q-1):
            if d<3 or issub(d): continue
            step=(q-1)//d;g=powi(gen,step)
            G=[];x=one
            for i in range(d): G.append(x);x=muli(x,g)
            Sset=set(G)
            A=[a for a in G if addi(one,a) in Sset]
            lam=len(A)
            # A ∩ A^{-1}: x ∈ A 且 x^{-1} ∈ A（即 1+x^{-1} ∈ G）
            Ainv=sum(1 for a in A if addi(one,powi(a,q-2)) in Sset)
            r=ord2(d)
            rows.append((n,q,d,r,d/(q-1),d%3==0,lam,lam/d,Ainv))
            out.write("n=%2d q=%6d d=%5d r=%3d α=%.5f 3|d=%-5s λ=%5d ρ=%.4f |A∩A⁻¹|=%4d\n"%(
                n,q,d,r,d/(q-1),str(d%3==0),lam,lam/d,Ainv))
    rows.sort(key=lambda z:-z[7])
    print("非子域案例总数:",len(rows))
    print("\n=== top-20 非子域（按 ρ 降序）===")
    for z in rows[:20]:
        print("  n=%2d d=%5d r=%3d α=%.5f 3|d=%-5s λ=%5d ρ=%.4f |A∩A⁻¹|=%d"%(z[0],z[2],z[3],z[4],str(z[5]),z[6],z[7],z[8]))
    print("\n=== 极值 ===")
    print("  ρ_max = %.4f  (n=%d, d=%d, λ=%d, r=%d, 3|d=%s)"%(rows[0][7],rows[0][0],rows[0][2],rows[0][6],rows[0][3],rows[0][5]))
    over_half=[z for z in rows if z[7]>0.5]; over_38=[z for z in rows if z[7]>3/8]
    print("  ρ > 1/2 的案例数:",len(over_half))
    print("  ρ > 3/8 的案例数:",len(over_38))
    for z in over_38[:10]:
        print("     n=%2d d=%4d λ=%3d ρ=%.4f r=%d"%(z[0],z[2],z[6],z[7],z[3]))
    print("\n=== |A∩A⁻¹| 与 λ 的关系（top-10）===")
    for z in rows[:10]:
        print("  d=%5d λ=%5d |A∩A⁻¹|=%4d  比值=%.3f"%(z[2],z[6],z[8],z[8]/z[6]))
    out.write("NONSUB=%d rho_max=%.4f over_half=%d over_38=%d\n"%(len(rows),rows[0][7],len(over_half),len(over_38)))
    out.close()
main()
