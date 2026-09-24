## CAP-MIX-1B · B11: 大容量结构第一刀 —— λ≤d 审计 + 分层表(ρ=λ/d vs r,3|d,subfield,d/(q-1))
import itertools
from math import gcd as igcd
exec(open("scripts/capmix1i_case4_and_falsewall.py").read().split("def main()")[0])
def ord2(d):
    o=1;x=2%d
    while x!=1: x=x*2%d;o+=1
    return o
def is_mersenne(d):
    k=1
    while 2**k-1<d: k+=1
    return 2**k-1==d
def main():
    rows=[];out=open("out/capmix1B11_capacity.txt","w")
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
            if d<3: continue
            step=(q-1)//d;g=powi(gen,step)
            G=[];x=one
            for i in range(d): G.append(x);x=muli(x,g)
            Sset=set(G)
            lam=sum(1 for a in G if addi(one,a) in Sset)
            r=ord2(d); mer=is_mersenne(d)
            rows.append((n,q,d,r,3 if d%3==0 else 0,mer,lam,lam/d,d/(q-1)))
            out.write("n=%2d q=%6d d=%5d r=%4d 3|d=%-5s sub=% -5s λ=%5d ρ=%.4f α=%.5f\n"%(
                n,q,d,r,str(d%3==0),str(mer),lam,lam/d,d/(q-1)))
    # λ<=d 审计
    bad=[r for r in rows if r[6]>r[2]]
    print("λ<=d 违例数:",len(bad))
    print("总案例:",len(rows))
    # ρ 分层
    import statistics
    def group(pred): 
        s=[r[7] for r in rows if pred(r)]
        return (len(s), round(statistics.mean(s),3) if s else None, round(max(s),3) if s else None)
    print("\n分层（n, mean ρ, max ρ）:")
    print("  subfield(Mersenne)   :",group(lambda r: r[5]))
    print("  非子域               :",group(lambda r: not r[5]))
    print("  3|d                  :",group(lambda r: r[4]==3))
    print("  3∤d                  :",group(lambda r: r[4]==0))
    print("  r=n                  :",group(lambda r: r[3]==r[0]))
    print("  r<n                  :",group(lambda r: r[3]<r[0]))
    print("\nρ>=0.9 的案例:")
    for r in sorted([x for x in rows if x[7]>=0.9],key=lambda z:z[2]):
        print("  n=%2d d=%5d r=%3d 3|d=%-5s sub=%-5s λ=%5d ρ=%.4f"%(r[0],r[2],r[3],str(r[4]==3),str(r[5]),r[6],r[7]))
    print("\nρ 最大 10 例:")
    for r in sorted(rows,key=lambda z:-z[7])[:10]:
        print("  n=%2d d=%5d r=%3d 3|d=%-5s sub=%-5s λ=%5d ρ=%.4f α=%.5f"%(r[0],r[2],r[3],str(r[4]==3),str(r[5]),r[6],r[7],r[9]))
    out.write("SUMMARY: rows=%d viol=%d\n"%(len(rows),len(bad)));out.close()
main()
