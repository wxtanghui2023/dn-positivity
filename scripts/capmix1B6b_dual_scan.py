## CAP-MIX-1B · B6b: 互补对偶扫描（收窄：λ 全除数；谱/混合仅 d≤200），B4 过滤 + I-IV 分型
import itertools, sys
from math import gcd as igcd
exec(open("scripts/capmix1i_case4_and_falsewall.py").read().split("def main()")[0])
def main():
    out=open("out/capmix1B6b_dual.txt","w")
    S={"pairs":0,"I":0,"II":0,"III":0,"IV":0,"A":0,"B":0,"C":0,"D":0,"BCD_I":0,"BCD_III":0,"BCD_II":0}
    key=[]
    def b4pred(d):
        if d%3==0 or igcd(2,d)!=1: return False
        x=2%d
        for _ in range(d+1):
            if x==(d-1)%d: return True
            x=x*2%d
            if x==2%d: break
        return False
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
        F=lambda a: muli(a,a)
        T=lambda a: addi(one,inv(a))
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
        lam={};spec={};mix={}
        for d in divs(q-1):
            if d<3: continue
            step=(q-1)//d;g=powi(gen,step)
            G=[];x=one
            for i in range(d): G.append(x);x=muli(x,g)
            Sset=set(G)
            I=[a for a in G if addi(one,a) in Sset]
            lam[d]=len(I)
            if d<=200:
                seen=set();sizes=[]
                for a in I:
                    if a in seen: continue
                    st=[a];seen.add(a);cnt=0
                    while st:
                        y=st.pop();cnt+=1
                        for z in (F(y),T(y)):
                            if z not in seen: seen.add(z);st.append(z)
                    sizes.append(cnt)
                spec[d]=tuple(sorted(sizes))
                m2=0
                for a in G:
                    hit=False
                    for k in range(1,n):
                        b=powi(a,2**k)
                        for _ in range(2):
                            b=T(b)
                            if b==a: hit=True;break
                        if hit: break
                    if hit: m2+=1
                mix[d]=m2
        for d in sorted(lam):
            m=(q-1)//d
            if m<3 or m not in lam or d>m: continue
            ld,lm_=lam[d],lam[m]
            S["pairs"]+=1
            t="I" if (ld==0 and lm_==0) else ("II" if (ld>0 and ld==lm_) else ("III" if (ld==0)!=(lm_==0) else "IV"))
            S[t]+=1
            bd,bm=b4pred(d),b4pred(m)
            k="A" if (bd and bm) else ("B" if bd else ("C" if bm else "D"))
            S[k]+=1
            if k in ("B","C","D"):
                S["BCD_"+t]=S.get("BCD_"+t,0)+1
            out.write("n=%2d q=%5d d=%5d m=%5d λd=%5d λm=%5d type=%-4s B4=%-2s spec_d=%-18s spec_m=%-18s mix=%s/%s\n"%(
                n,q,d,m,ld,lm_,t,k,str(spec.get(d,'-')),str(spec.get(m,'-')),str(mix.get(d,'-')),str(mix.get(m,'-'))))
            if k in ("B","C","D") or t in ("II","III"): key.append((n,q,d,m,ld,lm_,t,k,spec.get(d),spec.get(m)))
    print("SUMMARY:",S, flush=True)
    print("关键行:",flush=True)
    for r in key: print("  n=%2d q=%5d (d=%5d,m=%5d) λd=%5d λm=%5d type=%s B4=%s spec=%s/%s"%(
        r[0],r[1],r[2],r[3],r[4],r[5],r[6],r[7],r[8],r[9]), flush=True)
    out.write("SUMMARY: "+str(S)+"\n");out.close()
main()
