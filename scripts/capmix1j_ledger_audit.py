## CAP-MIX-1A(6): 账本审计 —— 204 = processed + skipped，每条 continue 路径都计数
import itertools
from math import gcd as igcd
exec(open("scripts/capmix1i_case4_and_falsewall.py").read().split("def main()")[0])  # 复用工具函数
def main():
    L={"cases_after_d_filter":0,"blind_J_empty":0,"mu1_some_hj_Xm1":0,
       "skip_dgs_gt200":0,"skip_dgs_lt2":0,"skip_dgs_eq0":0,"skip_dgs_eq1":0,
       "processed":0,"cls_T_gt0":0,"cls_Fwall":0,"cls_degen":0}
    rows=[]
    plan=[(3,range(2,8)),(5,range(2,5)),(7,range(2,5)),(11,range(2,4)),(13,range(2,4)),(17,range(2,3)),(19,range(2,3))]
    for p,nr in plan:
        for n in nr:
            q=p**n
            if q>4000: continue
            _,tomul=mk(p,n)
            els=[tuple((i//(p**k))%p for k in range(n)) for i in range(q)]
            enc={e:i for i,e in enumerate(els)}
            one=enc[(1,)+(0,)*(n-1)];zero=enc[tuple([0]*n)]
            scal=[enc[(c,)+(0,)*(n-1)] for c in range(p)]
            addi=lambda a,b: enc[tuple((x+y)%p for x,y in zip(els[a],els[b]))]
            negi=lambda a: enc[tuple((-x)%p for x in els[a])]
            muli=lambda a,b: enc[tomul(els[a],els[b])]
            def powi(a,e):
                r=one;b=a
                while e:
                    if e&1:r=muli(r,b)
                    b=muli(b,b);e>>=1
                return r
            def ev(poly,x):
                v=zero
                for c in reversed(poly):
                    v=muli(v,x)
                    if c%p: v=addi(v,scal[c%p])
                return v
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
                L["cases_after_d_filter"]+=1
                step=(q-1)//d;g=powi(gen,step)
                G=[];x=one
                for i in range(d): G.append(x);x=muli(x,g)
                S=set(G)
                J=[];Xdm=Xd(d,p)
                for j in range(1,(ordm(p,d) or d)+1):
                    r=pow(p,j,d)
                    if r==0 or ispp(r,p): continue
                    sgn=-1 if (p**j+r)%2 else 1
                    J.append(gc(Qj(r,sgn,p),Xdm,p))
                if not J: L["blind_J_empty"]+=1; continue
                if any(isXm1(h,p) for h in J): L["mu1_some_hj_Xm1"]+=1; continue
                gs=J[0]
                for h in J[1:]: gs=gc(gs,h,p)
                dgs=len(gs)-1
                if dgs>200: L["skip_dgs_gt200"]+=1; continue
                if dgs<2:
                    if dgs==0: L["skip_dgs_eq0"]+=1
                    else: L["skip_dgs_eq1"]+=1
                    L["skip_dgs_lt2"]+=1; continue
                L["processed"]+=1
                R=[xx for xx in G if ev(gs,xx)==0]
                T=0;F=0;degen=[]
                for xx in R:
                    if xx==one: continue
                    y=negi(addi(xx,one))
                    if y==one or y==xx: degen.append(xx)
                    elif y in S: T+=1
                    else: F+=1
                cls = "T>0" if T>0 else ("Fwall" if F>0 else "degen")
                if T>0: L["cls_T_gt0"]+=1
                elif F>0: L["cls_Fwall"]+=1
                else: L["cls_degen"]+=1
                rows.append((p,q,d,dgs,len(R),T,F,len(degen),cls))
    print("LEDGER:",L)
    print("check: processed =",L["processed"],"  sum classes =",L["cls_T_gt0"]+L["cls_Fwall"]+L["cls_degen"])
    print("check: skip total =",L["blind_J_empty"]+L["mu1_some_hj_Xm1"]+L["skip_dgs_gt200"]+L["skip_dgs_lt2"])
    print("check: total =",L["cases_after_d_filter"])
    print("--- degen 行 ---")
    for r in rows:
        if r[8]=="degen": print(r)
    print("--- Fwall 行 ---")
    for r in rows:
        if r[8]=="Fwall": print(r)
main()
