## CAP-MIX-1B · B7: 盲类交叉检验（char 2）：λ_raw vs λ_valid，按 blind/non-blind 分表
import itertools
from math import gcd as igcd
exec(open("scripts/capmix1i_case4_and_falsewall.py").read().split("def main()")[0])
def main():
    T={"blind":{"n":0,"eq":0,"zero_agree":0,"dne0":0,"cap":0,"noncap":0,"valid_pos":0},
       "nonblind":{"n":0,"eq":0,"zero_agree":0,"dne0":0,"cap":0,"noncap":0,"valid_pos":0}}
    deltas=[]
    out=open("out/capmix1B7_blind.txt","w")
    for n in range(2,13):
        q=2**n
        if q>4096: continue
        _,tomul=mk(2,n)
        els=[tuple((i//(2**k))%2 for k in range(n)) for i in range(q)]
        enc={e:i for i,e in enumerate(els)}
        one=enc[(1,)+(0,)*(n-1)]
        addi=lambda a,b: enc[tuple((x+y)%2 for x,y in zip(els[a],els[b]))]
        negi=lambda a: a   # char 2: -x = x
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
            if d<3 or d>100: continue
            step=(q-1)//d;g=powi(gen,step)
            G=[];x=one
            for i in range(d): G.append(x);x=muli(x,g)
            Sset=set(G)
            # blind?
            Jin=[pow(2,j,d) for j in range(1,(ordm(2,d) or d)+1)]
            Jin=[r for r in Jin if r!=0 and not ispp(r,2)]
            blind = (len(set(Jin))==0)
            # λ_raw / λ_valid（char 2: -1=1, -2=0, -1/2=1）
            lam_raw=0;lam_val=0
            for a in G:
                if addi(one,a) in Sset:
                    lam_raw+=1
                    if a!=one and a!=0: lam_val+=1     # 退化点为 x=1(x=-1/2 同点) 与 x=-2=0
            D=0
            for cand in (one,):                     # x=1 需 1+1=0∈G，恒否
                if cand in Sset and addi(one,cand) in Sset: D+=1
            if 0 in Sset: D+=1                      # x=-2=0（恒否）
            theo=lam_raw-D
            # 真值 & |Valid|
            pairs=[(a,b) for a in G for b in G if a!=b and a!=one and b!=one]
            nvalid=0
            for (a,b) in pairs:
                if addi(addi(one,a),b) in Sset: nvalid+=1
            cap = (nvalid==0)
            key="blind" if blind else "nonblind"
            T[key]["n"]+=1
            if lam_raw==lam_val: T[key]["eq"]+=1
            if (lam_raw==0)==(lam_val==0): T[key]["zero_agree"]+=1
            if lam_raw!=lam_val: T[key]["dne0"]+=1; deltas.append((n,q,d,lam_raw,lam_val))
            if cap: T[key]["cap"]+=1
            else: T[key]["noncap"]+=1
            if nvalid>0: T[key]["valid_pos"]+=1
            out.write("n=%2d q=%5d d=%4d blind=%-5s λraw=%4d λvalid=%4d D=%d |Valid|=%5d cap=%s\n"%(
                n,q,d,str(blind),lam_raw,lam_val,D,nvalid,str(cap)))
    print("TABLE:")
    for k in ("blind","nonblind"):
        v=T[k]; print("  %-8s n=%2d  λraw=λvalid: %2d/%2d  零性一致: %2d/%2d  Δ≠0: %d  cap=%d noncap=%d |Valid|>0: %d"%(
            k,v["n"],v["eq"],v["n"],v["zero_agree"],v["n"],v["dne0"],v["cap"],v["noncap"],v["valid_pos"]))
    print("Δ≠0 列表:",deltas)
    out.write("TABLE: "+str(T)+"\n");out.close()
main()
