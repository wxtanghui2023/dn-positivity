## CAP-MIX-1B · B9: B4 定理化核验 —— (ord_d(2) 偶 ∧ 3∤d) ⟹ λ=0；边界与最小性
import itertools
from math import gcd as igcd
exec(open("scripts/capmix1i_case4_and_falsewall.py").read().split("def main()")[0])
def minus1_in_group2(d):
    if d<=1 or igcd(2,d)!=1: return False
    x=2%d
    for _ in range(d+1):
        if x==(d-1)%d: return True
        x=x*2%d
        if x==2%d: break
    return False
def ord2(d):
    if d<=1 or igcd(2,d)!=1: return None
    o=1;x=2%d
    while x!=1: x=x*2%d;o+=1
    return o
def main():
    S={"cases":0,"hyp":0,"hyp_lam0":0,"hyp_viol":0,
       "noHyp_lam0":0,"noHyp_lam_pos":0,
       "ord_odd_lam0":0,"ord_odd_lam_pos":0,
       "d3_total":0,"d3_lam_pos":0,
       "cond2_only_drop_viol":0,"cond1_only_drop_viol":0}
    viol=[];odd_lam0=[];d3=[]
    out=open("out/capmix1B9b_theorem.txt","w")
    for n in range(2,14):
        q=2**n
        if q>8192: continue
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
            S["cases"]+=1
            step=(q-1)//d;g=powi(gen,step)
            G=[];x=one
            for i in range(d): G.append(x);x=muli(x,g)
            Sset=set(G)
            lam=sum(1 for a in G if addi(one,a) in Sset)
            o=ord2(d); even=minus1_in_group2(d); n3=(d%3!=0)
            hyp=even and n3
            if hyp:
                S["hyp"]+=1
                if lam==0: S["hyp_lam0"]+=1
                else: S["hyp_viol"]+=1; viol.append((n,q,d,o,lam))
            else:
                if lam==0: S["noHyp_lam0"]+=1
                else: S["noHyp_lam_pos"]+=1
            if not even:
                if lam==0: S["ord_odd_lam0"]+=1; odd_lam0.append((n,q,d,o))
                else: S["ord_odd_lam_pos"]+=1
            if d==3:
                S["d3_total"]+=1
                if lam>0: S["d3_lam_pos"]+=1; d3.append((n,q,d,lam))
            # 最小性：仅去掉条件②（保留 ord 偶，允许 3|d）
            if even and (d%3==0) and lam>0: S["cond2_only_drop_viol"]+=1
            # 仅去掉条件①（保留 3∤d，允许 ord 奇）
            if (not even) and n3 and lam>0: S["cond1_only_drop_viol"]+=1
            out.write("n=%2d q=%5d d=%5d ord2=%s 3∤d=%-5s λ=%4d hyp=%-5s\n"%(
                n,q,d,str(o),str(n3),lam,str(hyp)))
    print("STATS:",S)
    print("假设成立却违例:",viol)
    print("ord 奇但 λ=0（B4 未覆盖）:",odd_lam0)
    print("d=3 且 λ>0 的例:",d3[:6])
    out.write("STATS: "+str(S)+"\n");out.close()
main()
