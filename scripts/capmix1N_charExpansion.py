## CAP-MIX-1A(10): λ_raw 精确角色展开的数值验证 + 𝒥_H 的 Jacobi→有限域压缩是否闭合
import itertools
from math import gcd as igcd
exec(open("scripts/capmix1i_case4_and_falsewall.py").read().split("def main()")[0])
def main():
    S={"case":0,"branch_ok":0,"branch_bad":0,"Jmatch":0,"Jmismatch":0}
    bad=[]
    out=open("out/capmix1N_charExpansion_fixed.txt","w")
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
            def inv(a): return powi(a,q-2)
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
            for d in divs(q-1):
                if d<3 or d>1200: continue
                S["case"]+=1
                mm=(q-1)//d
                step=(q-1)//d;g=powi(gen,step)
                G=[];x=one
                for i in range(d): G.append(x);x=muli(x,g)
                Sset=set(G)
                lam_raw=0
                for xx in G:
                    if negi(addi(xx,one)) in Sset: lam_raw+=1
                # A_H = Σ_{χ≠ε} χ(-1) ; = m-1 if -1∈G else -1
                neg1=negi(one)
                A=(mm-1) if neg1 in Sset else -1
                # 分支公式检验
                pred = (q-3*mm+1+0) if neg1 in Sset else (q+1+0)   # 仅结构项（J_H=0 时的核）
                JH = lam_raw*mm*mm - q + 2 + 3*A
                # 独立压缩：J_H' = m^2 * N* - m*|G\{-1}| + A
                Nstar=0
                for z in G:
                    if z==neg1: continue
                    w=negi(inv(addi(z,one)))
                    if w in Sset: Nstar+=1
                size=len(G)-(1 if neg1 in Sset else 0)
                JHp = mm*mm*Nstar - mm*size + 2*A
                okbr = (lam_raw*mm*mm == pred + JH)
                if okbr: S["branch_ok"]+=1
                else: S["branch_bad"]+=1
                okJ = (JH==JHp)
                if okJ: S["Jmatch"]+=1
                else: S["Jmismatch"]+=1; bad.append((p,q,d,lam_raw,mm,A,JH,JHp,Nstar,size))
                out.write("p=%2d q=%5d d=%5d m=%4d -1∈G=%-5s λraw=%5d A=%5d J_H=%8d J_H'=%8d N*=%5d %s\n"%(
                    p,q,d,mm,str(neg1 in Sset),lam_raw,A,JH,JHp,Nstar,"OK" if okJ else "MISMATCH"))
    print("STATS:",S)
    print("BAD(前6):",bad[:6])
    out.write("STATS: "+str(S)+"\n");out.close()
main()
