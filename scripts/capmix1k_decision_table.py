## CAP-MIX-1A(7): 75 例非盲逐例判定表（witness certificate vs cap certificate）
import itertools
from math import gcd as igcd
exec(open("scripts/capmix1i_case4_and_falsewall.py").read().split("def main()")[0])
def main():
    S_={"witness":0,"certificate":0,"FP":0,"FN":0,"rows":0}
    cert_break={"one":0,"zero":0,"m2":0,"mhalf":0,"other_false":0,"size_hist":{},"decomp_ok":0,"decomp_bad":0}
    out=open("out/capmix1K_decision_table.txt","w")
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
            mtwo=negi(addi(one,one))
            inv2=pow(2,p-2,p)
            hlf=enc[tuple((inv2*c)%p for c in els[one])]
            mhalf=negi(hlf)
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
                if not J: continue
                if any(isXm1(h,p) for h in J): continue
                gs=J[0]
                for h in J[1:]: gs=gc(gs,h,p)
                dgs=len(gs)-1
                R=[xx for xx in G if ev(gs,xx)==0]
                wit=[];degen=[];other=[];has1=False
                for xx in R:
                    if xx==one: has1=True
                    y=negi(addi(xx,one))
                    if xx!=one and y in S and y!=one and y!=xx: wit.append((xx,y))
                    elif xx==mtwo or xx==mhalf: degen.append(xx)
                    elif xx!=one: other.append(xx)
                concl = "NONCAP" if wit else "CAP"
                # 独立真值
                truth="CAP"
                for xx in G:
                    y=negi(addi(xx,one))
                    if y in S and y!=xx and xx!=one and y!=one: truth="NONCAP";break
                ok = (concl==truth)
                if concl=="CAP": S_["certificate"]+=1
                else: S_["witness"]+=1
                if concl=="CAP" and truth!="CAP": S_["FN"]+=1
                if concl=="NONCAP" and truth!="NONCAP": S_["FP"]+=1
                S_["rows"]+=1
                if concl=="CAP":
                    cert_break["size_hist"][len(R)]=cert_break["size_hist"].get(len(R),0)+1
                    if has1: cert_break["one"]+=1
                    else: cert_break["zero"]+=1
                    cert_break["m2"]+= (1 if mtwo in degen else 0)
                    cert_break["mhalf"]+= (1 if mhalf in degen else 0)
                    cert_break["other_false"]+=len(other)
                    # 分解检查：R* = 有效端点 ⊔ 退化 ⊔ 伪根（此处无有效端点）
                    if (len(degen)+len(other)+(1 if has1 else 0))==len(R): cert_break["decomp_ok"]+=1
                    else: cert_break["decomp_bad"]+=1
                rr=[str(els[v]) for v in R]
                out.write("p=%2d n=%d q=%5d d=%5d |G|=%4d deg_gs=%3d |R*|=%2d R*=%s wit=%s conj=%-6s truth=%-6s %s\n"%(
                    p,n,q,d,d,dgs,len(R),",".join(rr) if rr else "EMPTY",
                    ";".join("%s->%s"%(els[a],els[b]) for a,b in wit[:2]) if wit else "-",
                    concl,truth,"OK" if ok else "MISMATCH"))
    print("SUMMARY:",S_)
    print("CERT BREAKDOWN:",{k:v for k,v in cert_break.items() if k!="size_hist"})
    print("CERT |R*| hist:",cert_break["size_hist"])
    out.write("SUMMARY: "+str(S_)+"\nCERT: "+str(cert_break)+"\n");out.close()
main()
