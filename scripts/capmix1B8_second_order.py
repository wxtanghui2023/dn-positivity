## CAP-MIX-1B · B8: 二阶加法 incidence —— I2(=λ) / I3(=N(G)) / E2(加法能量) + 反例筛选
import itertools
from math import gcd as igcd
exec(open("scripts/capmix1i_case4_and_falsewall.py").read().split("def main()")[0])
def main():
    rows=[]
    out=open("out/capmix1B8_second_order.txt","w")
    A_ok=A_bad=0
    for n in range(2,13):
        q=2**n
        if q>4096: continue
        _,tomul=mk(2,n)
        els=[tuple((i//(2**k))%2 for k in range(n)) for i in range(q)]
        enc={e:i for i,e in enumerate(els)}
        one=enc[(1,)+(0,)*(n-1)]
        zero=enc[tuple([0]*n)]
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
            if d<3 or d>100: continue
            step=(q-1)//d;g=powi(gen,step)
            G=[];x=one
            for i in range(d): G.append(x);x=muli(x,g)
            Sset=set(G)
            Jin=set(r for r in (pow(2,j,d) for j in range(1,(ordm(2,d) or d)+1)) if r!=0 and not ispp(r,2))
            blind=(len(Jin)==0)
            # I2 = λ = #{x∈G: 1+x∈G}
            I2=sum(1 for a in G if addi(one,a) in Sset)
            # I3 = N(G) = #{(x,y)∈G^2 : 1+x+y∈G}  （= |Valid| 有序计数）
            I3=0
            for a in G:
                for b in G:
                    if addi(addi(one,a),b) in Sset: I3+=1
            # Valid（非退化：x≠1,y≠1,x≠y 且 z∉{1,x,y} 自动）
            V=0
            for a in G:
                if a==one: continue
                for b in G:
                    if b==one or b==a: continue
                    if addi(addi(one,a),b) in Sset: V+=1
            if abs(I3-V)<=2*d: A_ok+=1
            else: A_bad+=1
            # E2 = Σ_s r(s)^2, r(s)=#{(x1,x2)∈G²: x1+x2=s}
            cnt={}
            for a in G:
                for b in G:
                    s=addi(a,b); cnt[s]=cnt.get(s,0)+1
            E2=sum(v*v for v in cnt.values())
            ndeg=I3-V
            rows.append((n,q,d,blind,I2,I3,V,E2,ndeg))
            out.write("n=%2d q=%5d d=%4d blind=%-5s I2=%4d I3=%4d Valid=%5d E2=%9d 退化差=%d\n"%(
                n,q,d,str(blind),I2,I3,V,E2,ndeg))
    print("B8-A: |I3 - Valid| 属退化差范围:",A_ok," 超范围:",A_bad)
    print("\nclass | n  | I2 取值        | I3 取值       | cap(I3>0?)")
    for k in (True,False):
        sub=[r for r in rows if r[3]==k]
        if not sub: continue
        print("  %-9s n=%2d  I2=%s  I3=%s  cap数=%d"%("blind" if k else "nonblind",len(sub),
            sorted(set(r[4] for r in sub)),sorted(set(r[5] for r in sub)),sum(1 for r in sub if r[5]==0)))
    # B8-C 反例：I2 相同但 I3 零性不同
    print("\n=== B8-C 反例（I2=0 但 I3>0）===")
    for r in rows:
        if r[4]==0 and r[5]>0: print("  n=%2d q=%5d d=%4d blind=%s I2=0 I3=%d"%(r[0],r[1],r[2],r[3]))
    print("\n=== I2 相同而 I3 零性不同（同 I2 值对照）===")
    for r in rows:
        if r[4]>0 and r[5]==0: print("  非cap 侧: n=%2d d=%4d I2=%d I3=%d (cap)"%(r[0],r[2],r[4],r[5]))
    out.write("ROWS: "+str(rows)+"\n");out.close()
main()
