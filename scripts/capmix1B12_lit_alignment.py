## CAP-MIX-1B · B12: 已知理论对照 —— λ = d²/Q + O(√Q)，Q=p^{ord_d(p)}（最小包含域）
import itertools
from math import gcd as igcd
exec(open("scripts/capmix1i_case4_and_falsewall.py").read().split("def main()")[0])
def ord_p_of_d(p,d):
    o=1;x=p%d
    while x!=1: x=x*p%d;o+=1
    return o
def main():
    R={"cases":0,"dev_gt_sqrtQ":0,"dev_gt_2sqrtQ":0,"maxratio":0.0,"maxcase":None,
       "mean_absdev":0.0,"sum_absdev":0.0,"subfield_devs":[]}
    out=open("out/capmix1B12_lit.txt","w")
    rows=[]
    for (p,nmax,qmax) in ((2,14,16384),(3,9,19683),(5,6,15625),(7,5,16807),(11,4,14641),(13,4,28561)):
        for n in range(2,nmax+1):
            q=p**n
            if q>qmax: continue
            _,tomul=mk(p,n)
            els=list(itertools.product(range(p),repeat=n))
            enc={e:i for i,e in enumerate(els)}
            one=enc[tuple([1]+[0]*(n-1))]
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
                lam=sum(1 for a in G if negi(addi(one,a)) in Sset)
                r=ord_p_of_d(p,d); Q=p**r
                main=d*d/Q
                dev=abs(lam-main); sq=Q**0.5
                ratio=dev/sq if sq>0 else 0
                R["cases"]+=1; R["sum_absdev"]+=dev
                if dev>sq: R["dev_gt_sqrtQ"]+=1
                if dev>2*sq: R["dev_gt_2sqrtQ"]+=1
                if ratio>R["maxratio"]: R["maxratio"]=ratio; R["maxcase"]=(p,n,q,d,r,Q,lam,main,round(dev,1),sq)
                if d==Q-1: R["subfield_devs"].append(round(dev,3))
                rows.append((ratio,p,n,d,Q,lam,main,dev,sq))
                out.write("p=%2d n=%2d d=%6d Q=%7d λ=%6d main=%.1f dev=%.1f √Q=%.1f ratio=%.3f\n"%(
                    p,n,d,Q,lam,main,dev,sq,ratio))
    R["mean_absdev"]=R["sum_absdev"]/max(1,R["cases"])
    print("STATS:",{k:v for k,v in R.items() if k not in ("subfield_devs",)})
    print("子域案例偏差样本:",R["subfield_devs"][:8])
    print("\n=== dev/√Q 最大的 12 例 ===")
    for z in sorted(rows,key=lambda t:-t[0])[:12]:
        print("  ratio=%.3f p=%2d d=%6d Q=%7d λ=%6d main=%.1f dev=%.1f √Q=%.1f"%(z[0],z[1],z[3],z[4],z[5],z[6],z[7],z[8]))
    print("\n=== dev>√Q 的案例（应极少）===")
    for z in sorted(rows,key=lambda t:-t[0]):
        if z[7]>z[8]: print("  ratio=%.3f p=%2d d=%6d Q=%7d λ=%6d main=%.1f dev=%.1f √Q=%.1f"%(z[0],z[1],z[3],z[4],z[5],z[6],z[7],z[8]))
    out.write("STATS: "+str({k:v for k,v in R.items() if k!='subfield_devs'})+"\n");out.close()
main()
