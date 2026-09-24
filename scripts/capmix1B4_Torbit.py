## CAP-MIX-1B · B4: T(x)=1+x^{-1} 的 3-轨道审计（char 2）：T-不变性 / λ mod 3 / 固定点 / d,n 分类
import itertools
from math import gcd as igcd
exec(open("scripts/capmix1i_case4_and_falsewall.py").read().split("def main()")[0])
def main():
    R={"case":0,"T_inv_bad":0,"lam_mod3_ok":0,"lam_mod3_bad":0,"orbit3_all":0,"orbit_not3":0,
       "fix2_when_3d":0,"fix0_when_not3d":0,"lam0_cases":0,"lam0_d3":0,"lam0_n_odd":0,
       "lam0_n_even":0,"lam0_other":0}
    hist={}
    rows=[]
    out=open("out/capmix1B4_Torbit.txt","w")
    for n in range(2,13):
        q=2**n
        if q>4096: continue
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
        def inv(a): return powi(a,q-2)
        def T(a): return addi(one,inv(a))
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
            if d<3 or d>100: continue
            R["case"]+=1
            step=(q-1)//d;g=powi(gen,step)
            G=[];x=one
            for i in range(d): G.append(x);x=muli(x,g)
            Sset=set(G)
            I=[a for a in G if addi(one,a) in Sset]
            Iset=set(I)
            lam=len(I)
            # T-不变性
            badT=sum(1 for a in I if T(a) not in Iset)
            if badT: R["T_inv_bad"]+=1
            # 轨道
            seen=set();orb=[];fix=0
            for a in I:
                if a in seen: continue
                o=[];z=a
                while z not in seen:
                    seen.add(z);o.append(z);z=T(z)
                orb.append(len(o))
                if len(o)==1: fix+=1
            o3 = all(l==3 for l in orb)
            if o3: R["orbit3_all"]+=1
            elif orb: R["orbit_not3"]+=1
            hist[tuple(sorted(set(orb)))]=hist.get(tuple(sorted(set(orb))),0)+1
            # λ mod 3 与固定点预测
            pred2 = (d%3==0)
            if pred2:
                ok = (lam%3==2) and fix==2
                if ok: R["fix2_when_3d"]+=1
            else:
                ok = (lam%3==0) and fix==0
                if ok: R["fix0_when_not3d"]+=1
            if ok: R["lam_mod3_ok"]+=1
            else: R["lam_mod3_bad"]+=1
            if lam==0:
                R["lam0_cases"]+=1
                if d%3==0: R["lam0_d3"]+=1
                elif n%2==1: R["lam0_n_odd"]+=1
                else: R["lam0_n_even"]+=1
            rows.append((n,q,d,lam,lam%3,fix,sorted(set(orb)),d%3,n%2))
            out.write("n=%2d q=%5d d=%4d λ=%4d λmod3=%d fix=%d orbits=%s dmod3=%d n2=%d\n"%(
                n,q,d,lam,lam%3,fix,str(sorted(set(orb))),d%3,n%2))
    print("STATS:",R)
    print("轨道结构直方图:",hist)
    print("λ=0 的行:")
    for r in rows:
        if r[3]==0: print("  n=%2d d=%4d dmod3=%d n2=%d"%(r[0],r[2],r[7],r[8]))
    out.write("STATS: "+str(R)+"\nORBHIST: "+str(hist)+"\n");out.close()
main()
