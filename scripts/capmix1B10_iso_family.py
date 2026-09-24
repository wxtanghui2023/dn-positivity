## CAP-MIX-1B · B10: (23,89) 边界机制 —— 同型族扫描（整数侧筛选 + 仅对命中者算 λ）
from math import gcd as igcd
import itertools
exec(open("scripts/capmix1i_case4_and_falsewall.py").read().split("def main()")[0])
def ord_d_2(d):
    o=1;x=2%d
    while x!=1: x=x*2%d;o+=1
    return o
def minus1_in_2(d):
    if d<=2: return False
    x=2%d
    for _ in range(d+2):
        if x==d-1: return True
        x=x*2%d
        if x==2%d: break
    return False
def divisors(k):
    ds=[]
    i=1
    while i*i<=k:
        if k%i==0:
            ds.append(i)
            if i!=k//i: ds.append(k//i)
        i+=1
    return sorted(ds)
def main():
    out=open("out/capmix1B10_iso.txt","w")
    hits=[]
    for n in range(3,15):
        q=2**n; M=q-1
        ds=[d for d in divisors(M) if 3<=d<=M//3]
        for d in ds:
            m=M//d
            if d>m: continue
            if ord_d_2(d)!=n or ord_d_2(m)!=n: continue
            if minus1_in_2(d) or minus1_in_2(m): continue
            hits.append((n,q,d,m))
        print("n=%2d q=%6d 同型候选对数=%d"%(n,q,len(hits)),flush=True)
    print("\n=== 同型族（ord_d=ord_m=n, 两边 -1∉<2>）逐对 λ ===",flush=True)
    for (n,q,d,m) in hits:
        lam={}
        for dd in (d,m):
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
            M2=q-1;prs=[];t=2
            while t*t<=M2:
                if M2%t==0:
                    prs.append(t)
                    while M2%t==0: M2//=t
                t+=1
            if M2>1: prs.append(M2)
            gen=None
            for e in range(1,q):
                if all(powi(e,(q-1)//pr)!=one for pr in prs): gen=e;break
            step=(q-1)//dd;g=powi(gen,step)
            G=[];x=one
            for i in range(dd): G.append(x);x=muli(x,g)
            Sset=set(G)
            lam[dd]=sum(1 for a in G if addi(one,a) in Sset)
        cls=("00" if lam[d]==0 and lam[m]==0 else ("0+" if lam[d]==0 else ("+0" if lam[m]==0 else "++")))
        print("  n=%2d q=%6d (d=%5d,m=%5d) ord=(%d,%d) λ=(%d,%d) %s | d素=%s m素=%s"%(
            n,q,d,m,ord_d_2(d),ord_d_2(m),lam[d],lam[m],cls,d in (23,89,31,41,7,5,3,11,13,17,19,29,37,43),0),flush=True)
        out.write("n=%2d q=%6d d=%5d m=%5d ord=(%d,%d) lam=(%d,%d) cls=%s\n"%(
            n,q,d,m,ord_d_2(d),ord_d_2(m),lam[d],lam[m],cls))
    out.write("TOTAL: %d pairs\n"%len(hits));out.close()
    print("总同型对数:",len(hits))
main()
