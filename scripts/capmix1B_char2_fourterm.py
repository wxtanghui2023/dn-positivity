## CAP-MIX-1B B1: char 2 四项关系 —— Frobenius 信息指数 / 退化因子 / 二维 survivor / 真值交叉
import itertools
from math import gcd as igcd
exec(open("scripts/capmix1i_case4_and_falsewall.py").read().split("def main()")[0])
def main():
    S={"case":0,"blind":0,"compress":0,"wall":0,"valid_not_in_Vstar":0,
       "cap_with_valid":0,"noncap_no_valid":0}
    rows=[]
    out=open("out/capmix1B_char2_fourterm.txt","w")
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
            S["case"]+=1
            step=(q-1)//d;g=powi(gen,step)
            G=[];x=one
            for i in range(d): G.append(x);x=muli(x,g)
            Sset=set(G)
            # B1-A: 信息指数
            Jin=[]
            for j in range(1,(ordm(2,d) or d)+1):
                r=pow(2,j,d)
                if r==0 or ispp(r,2): continue
                Jin.append(r)
            Jin=sorted(set(Jin))
            blind = (len(Jin)==0)
            # 非退化对
            pairs=[(a,b) for a in G for b in G if a!=b and a!=one and b!=one]
            # 真值：有效四项关系（z=1+x+y ∈ G）
            valid=set()
            for (a,b) in pairs:
                z=addi(addi(one,a),b)
                if z in Sset: valid.add((a,b))
            # B1-C: V_* = 非退化对上所有信息 j 的 Q_j=0
            V=set(pairs)
            if not blind:
                for r in Jin:
                    if not V: break
                    bad=set()
                    for (a,b) in V:
                        z=addi(addi(one,a),b)
                        qv=addi(addi(addi(powi(a,r),powi(b,r)),powi(z,r)),one)
                        if qv!=zero: bad.add((a,b))
                    V-=bad
            truth="CAP" if not valid else "NONCAP"
            if blind: S["blind"]+=1
            elif len(V)<=max(4,2*len(valid)) and len(V)*4<=len(pairs): S["compress"]+=1
            else: S["wall"]+=1
            for v in valid:
                if v not in V: S["valid_not_in_Vstar"]+=1
            if truth=="CAP" and valid: S["cap_with_valid"]+=1
            if truth=="NONCAP" and not valid: S["noncap_no_valid"]+=1
            rows.append((n,q,d,len(pairs),len(valid),len(V),blind,truth))
            out.write("n=%2d q=%5d d=%4d pairs=%6d |valid|=%5d |V*|=%6d blind=%-5s truth=%-7s %s\n"%(
                n,q,d,len(pairs),len(valid),len(V),str(blind),truth,
                "valid⊆V*" if all(v in V for v in valid) else "VIOLATION"))
    print("STATS:",S)
    print("前 10 行:")
    for r in rows[:10]: print(r)
    print("非盲且 truth=CAP 的行:")
    for r in rows:
        if (not r[6]) and r[7]=="CAP": print(r)
    out.write("STATS: "+str(S)+"\n");out.close()
main()
