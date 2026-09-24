## CAP-MIX-1B · B11.3: E_{1/2} 触发搜索（跨特征）+ 命题 AA\{1}⊆A 的检验
import itertools
from math import gcd as igcd
exec(open("scripts/capmix1i_case4_and_falsewall.py").read().split("def main()")[0])
def issub(d,p,n):
    k=1
    while p**k-1<=d:
        if p**k-1==d and n%k==0: return True
        k+=1
    return p-1==d
def main():
    out=open("out/capmix1B11c_half.txt","w")
    hits=[];tot=0
    for (p,nmax,qmax) in ((2,14,16384),(3,9,19683),(5,6,15625),(7,5,16807),(11,4,14641),(13,4,28561)):
        for n in range(2,nmax+1):
            q=p**n
            if q>qmax: continue
            _,tomul=mk(p,n)
            els=list(itertools.product(range(p),repeat=n))
            enc={e:i for i,e in enumerate(els)}
            one=enc[tuple([1]+[0]*(n-1))]
            zero=enc[tuple([0]*n)]
            addi=lambda a,b: enc[tuple((x+y)%p for x,y in zip(els[a],els[b]))]
            negi=lambda a: enc[tuple((-x)%p for x in els[a])]
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
                A=[a for a in G if negi(addi(one,a)) in Sset]
                lam=len(A); tot+=1
                rho=lam/d
                if rho>0.5:
                    sub=issub(d,p,n)
                    prop=None
                    if lam<=2000:
                        AA=set()
                        for a in A:
                            for b in A: AA.add(muli(a,b))
                        prop=all((u in Sset and u!=one and u in set(A)) for u in AA if u!=one)
                    hits.append((p,n,q,d,lam,rho,sub,prop))
                    out.write("ρ>1/2: p=%2d n=%2d q=%6d d=%5d λ=%5d ρ=%.4f subfield=%s AA\\{1}⊆A=%s\n"%(
                        p,n,q,d,lam,rho,str(sub),str(prop)))
    print("总案例数:",tot)
    print("ρ>1/2 案例数:",len(hits))
    print("\n=== ρ>1/2 明细 ===")
    for h in hits[:24]: print("  p=%2d n=%2d d=%4d λ=%5d ρ=%.4f subfield=%-5s 命题=%-5s"%(
        h[0],h[1],h[3],h[4],h[5],str(h[6]),str(h[7])))
    non=[h for h in hits if not h[6]]
    print("\n非子域且 ρ>1/2 的案例数:",len(non), non[:5])
    propfail=[h for h in hits if h[7] is False]
    print("命题失败案例数:",len(propfail),"（前 5）:",[(h[0],h[1],h[3],h[4]) for h in propfail[:5]])
    out.write("TOT=%d HITS=%d NONSUB=%d PROCFAIL=%d\n"%(tot,len(hits),len(non),len(propfail)));out.close()
main()
