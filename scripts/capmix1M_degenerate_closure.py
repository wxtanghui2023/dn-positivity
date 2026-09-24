## CAP-MIX-1A(9): 退化点算术闭合 —— 验证 λ_raw − λ_valid = |{1,−2,−1/2} ∩ G|（集合计数）
import itertools
from math import gcd as igcd
exec(open("scripts/capmix1i_case4_and_falsewall.py").read().split("def main()")[0])
def main():
    S={"case":0,"match":0,"mismatch":0,"sum_diff":0}
    out=open("out/capmix1M_degenerate_fixed.txt","w")
    plan=[(3,range(2,8)),(5,range(2,5)),(7,range(2,5)),(11,range(2,4)),(13,range(2,4)),(17,range(2,3)),(19,range(2,3))]
    for p,nr in plan:
        for n in nr:
            q=p**n
            if q>4000: continue
            _,tomul=mk(p,n)
            els=[tuple((i//(p**k))%p for k in range(n)) for i in range(q)]
            enc={e:i for i,e in enumerate(els)}
            one=enc[(1,)+(0,)*(n-1)]
            addi=lambda a,b: enc[tuple((x+y)%p for x,y in zip(els[a],els[b]))]
            negi=lambda a: enc[tuple((-x)%p for x in els[a])]
            muli=lambda a,b: enc[tomul(els[a],els[b])]
            def powi(a,e):
                r=one;b=a
                while e:
                    if e&1:r=muli(r,b)
                    b=muli(b,b);e>>=1
                return r
            m=q-1;prs=[];t=2
            while t*t<=m:
                if m%t==0:
                    prs.append(t)
                    while m%t==0: m//=t
                t+=1
            if m>1: prs.append(m)
            gen=None
            for e in range(1,q):
                if all(powi(e,(q-1)//pr)!=one for pr in prs): gen=e;break
            mtwo=negi(addi(one,one))
            inv2=pow(2,p-2,p)
            hlf=enc[tuple((inv2*c)%p for c in els[one])]
            mhalf=negi(hlf)
            for d in divs(q-1):
                if d<3 or d>1200: continue
                S["case"]+=1
                step=(q-1)//d;g=powi(gen,step)
                G=[];x=one
                for i in range(d): G.append(x);x=muli(x,g)
                Sset=set(G)
                lam_raw=0;lam_val=0
                for xx in G:
                    y=negi(addi(xx,one))
                    if y in Sset:
                        lam_raw+=1
                        if xx!=one and y!=one and y!=xx: lam_val+=1
                diff=lam_raw-lam_val
                # 退化候选集（集合计数，避免 p=3 重复）
                D=set()
                for cand in (one,mtwo,mhalf):
                    if cand in Sset and negi(addi(cand,one)) in Sset: D.add(cand)
                theo=len(D)
                ok = (diff==theo)
                if ok: S["match"]+=1
                else: S["mismatch"]+=1
                S["sum_diff"]+=diff
                out.write("p=%2d n=%d q=%5d d=%5d |G|=%4d 1∈G=%s -2∈G=%s -1/2∈G=%s theo=%d meas_diff=%d %s\n"%(
                    p,n,q,d,d,"Y","Y" if mtwo in Sset else "N","Y" if mhalf in Sset else "N",theo,diff,"OK" if ok else "MISMATCH"))
    print("STATS:",S)
    out.write("STATS: "+str(S)+"\n");out.close()
main()
