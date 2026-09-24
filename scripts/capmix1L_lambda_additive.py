## CAP-MIX-1A(8): 加法像 λ_G = |G ∩ (−1−G)| 全 204 + blind 重点 + 与 R* 交叉
import itertools
from math import gcd as igcd
exec(open("scripts/capmix1i_case4_and_falsewall.py").read().split("def main()")[0])
def main():
    S={"case":0,"mis_raw":0,"mis_val":0,"blind":0,"blind_cap":0,"blind_noncap":0,
       "nb":0,"nb_cap":0,"nb_noncap":0,"cross_eq":0,"cross_neq":0}
    blind_rows=[];nb_rows=[]
    lam_hist={};lamd=[]
    out=open("out/capmix1L_lambda.txt","w")
    plan=[(3,range(2,8)),(5,range(2,5)),(7,range(2,5)),(11,range(2,4)),(13,range(2,4)),(17,range(2,3)),(19,range(2,3))]
    for p,nr in plan:
        for n in nr:
            q=p**n
            if q>4000: continue
            _,tomul=mk(p,n)
            els=[tuple((i//(p**k))%p for k in range(n)) for i in range(q)]
            enc={e:i for i,e in enumerate(els)}
            one=enc[(1,)+(0,)*(n-1)];zero=enc[tuple([0]*n)]
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
            for d in divs(q-1):
                if d<3 or d>1200: continue
                S["case"]+=1
                step=(q-1)//d;g=powi(gen,step)
                G=[];x=one
                for i in range(d): G.append(x);x=muli(x,g)
                Sset=set(G)
                # truth
                cap=True
                for xx in G:
                    y=negi(addi(xx,one))
                    if y in Sset and y!=xx and xx!=one and y!=one: cap=False;break
                # lambda
                lam_raw=0;lam_val=0
                for xx in G:
                    y=negi(addi(xx,one))
                    if y in Sset:
                        lam_raw+=1
                        if xx!=one and y!=one and y!=xx: lam_val+=1
                # blind?
                J=[]
                for j in range(1,(ordm(p,d) or d)+1):
                    r=pow(p,j,d)
                    if r==0 or ispp(r,p): continue
                    J.append(j)
                blind = (len(J)==0)
                od=ordm(p,d);gd=igcd(d,p-1);mm=(q-1)//d
                if (lam_raw==0)!=cap: S["mis_raw"]+=1
                if (lam_val==0)!=cap: S["mis_val"]+=1
                if blind:
                    S["blind"]+=1
                    if cap: S["blind_cap"]+=1
                    else: S["blind_noncap"]+=1
                    blind_rows.append((p,n,q,d,cap,lam_raw,lam_val,round(lam_raw/d,4),mm,od,gd))
                    lam_hist[lam_raw]=lam_hist.get(lam_raw,0)+1
                else:
                    S["nb"]+=1
                    if cap: S["nb_cap"]+=1
                    else: S["nb_noncap"]+=1
                    nb_rows.append((p,n,q,d,cap,lam_raw,lam_val,round(lam_raw/d,4),mm,od,gd))
                    # cross-check: valid endpoints in R*
                    gs=None
                    Xdm=Xd(d,p)
                    for j in J:
                        r=pow(p,j,d);sgn=-1 if (p**j+r)%2 else 1
                        h=gc(Qj(r,sgn,p),Xdm,p)
                        gs=h if gs is None else gc(gs,h,p)
                    R=[xx for xx in G if all(0==0 for _ in [0]) and (lambda xx: gs is not None and (lambda v: v==zero)(None))(xx)] if False else None
                    # 正确求根
                    def ev2(poly,x):
                        v=zero
                        for c in reversed(poly):
                            v=muli(v,x)
                            if c%p: v=addi(v,[enc[(c,)+(0,)*(n-1)]] and enc[(c,)+(0,)*(n-1)])
                        return v
                    R=[xx for xx in G if ev2(gs,xx)==zero]
                    v_in_R=sum(1 for xx in R if (lambda y: y in Sset and xx!=one and y!=one and y!=xx)(negi(addi(xx,one))))
                    if v_in_R==lam_val: S["cross_eq"]+=1
                    else: S["cross_neq"]+=1
    print("STATS:",S)
    print("BLIND 行(前8):",blind_rows[:8])
    print("NONBLIND 行(前5):",nb_rows[:5])
    print("blind λ_raw 直方图:",lam_hist)
    print("blind λ_max:",max(lam_hist) if lam_hist else None)
    out.write("STATS: "+str(S)+"\nBLIND:\n")
    for r in blind_rows: out.write(str(r)+"\n")
    out.write("NONBLIND:\n")
    for r in nb_rows: out.write(str(r)+"\n")
    out.close()
main()
