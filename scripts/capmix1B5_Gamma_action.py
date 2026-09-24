## CAP-MIX-1B · B5: Γ=<F,T> 合并作用（F(x)=x^2, T(x)=1+x^{-1}）
import itertools
from math import gcd as igcd
exec(open("scripts/capmix1i_case4_and_falsewall.py").read().split("def main()")[0])
def main():
    R={"case":0,"FT_commute_ok":0,"FT_bad":0,"lam0":0,"lam0_mixed_G":0,"lam0_nomixed_G":0,
       "orbdiv3n_bad":0,"spectra":{}}
    mixed_rows=[]
    out=open("out/capmix1B5_Gamma.txt","w")
    for n in range(2,13):
        q=2**n
        if q>4096: continue
        _,tomul=mk(2,n)
        els=[tuple((i//(2**k))%2 for k in range(n)) for i in range(q)]
        enc={e:i for i,e in enumerate(els)}
        one=enc[(1,)+(0,)*(n-1)];zero=enc[tuple([0]*n)]
        addi=lambda a,b: enc[tuple((x+y)%2 for x,y in zip(els[a],els[b]))]
        muli=lambda a,b: enc[tomul(els[a],els[b])]
        def powi(a,e):
            r=one;b=a
            while e:
                if e&1:r=muli(r,b)
                b=muli(b,b);e>>=1
            return r
        def inv(a): return powi(a,q-2)
        F=lambda a: muli(a,a)
        T=lambda a: addi(one,inv(a))
        # FT = TF 校验（全 F_q^*）
        ok=True
        for a in range(1,q):
            if T(F(a))!=F(T(a)): ok=False;break
        if ok: R["FT_commute_ok"]+=1
        else: R["FT_bad"]+=1
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
        def mixed_stab(xs, Sset):
            c=0
            for a in xs:
                hit=False
                for k in range(1,n):
                    b=powi(a,2**k)
                    if b not in Sset and False: pass
                    for _ in range(2):
                        b=T(b)
                        if b==a: hit=True;break
                    if hit: break
                if hit: c+=1
            return c
        for d in divs(q-1):
            if d<3 or d>100: continue
            R["case"]+=1
            step=(q-1)//d;g=powi(gen,step)
            G=[];x=one
            for i in range(d): G.append(x);x=muli(x,g)
            Sset=set(G)
            I=[a for a in G if addi(one,a) in Sset]
            lam=len(I); Iset=set(I)
            # Γ-轨道（BFS，双生成元）
            seen=set();sizes=[]
            for a in I:
                if a in seen: continue
                st=[a];orb=[];seen.add(a)
                while st:
                    y=st.pop();orb.append(y)
                    for z in (F(y), T(y)):
                        if z not in seen:
                            seen.add(z);st.append(z)
                sizes.append(len(orb))
                if len(orb)==0 or (3*n)%len(orb)!=0: R["orbdiv3n_bad"]+=1
            spec=tuple(sorted(sizes))
            R["spectra"][spec]=R["spectra"].get(spec,0)+1
            nmI=mixed_stab(I,Iset)
            nmG=mixed_stab(G,Sset)
            if lam==0:
                R["lam0"]+=1
                if nmG>0: R["lam0_mixed_G"]+=1
                else: R["lam0_nomixed_G"]+=1
            out.write("n=%2d q=%5d d=%4d λ=%4d |Γorbs|=%s mixed(I)=%d mixed(G)=%d\n"%(
                n,q,d,lam,str(spec),nmI,nmG))
            if (n==11 and d in (23,89)) or (n==11):
                mixed_rows.append((n,q,d,lam,spec,nmI,nmG))
    print("STATS:",R)
    print("轨道谱直方图:",R["spectra"])
    print("n=11 行:")
    for r in mixed_rows: print(r)
    out.write("STATS: "+str({k:v for k,v in R.items() if k!='spectra'})+"\n");out.close()
main()
