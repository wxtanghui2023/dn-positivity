## CAP-MIX-1B · B3: 1A↔1B 对接四项硬检验（A 集合恒等 / B Q_j 自动消失 / C 计数 / D 退化集空）
import itertools
from math import gcd as igcd
exec(open("scripts/capmix1i_case4_and_falsewall.py").read().split("def main()")[0])
def main():
    R={"case":0,"A_I_neq":0,"A_I_minus_P":0,"A_P_minus_I":0,"sumI":0,"sumPx":0,
       "B_viol_x":0,"B_viol_pairs":0,"C_eq1":0,"C_ne1":0,"C_eq2":0,"C_ne2":0,
       "D_degen_contrib":0,"lam2_zero_caps":0,"lam2_pos":0}
    rows=[]
    out=open("out/capmix1B3_bridge.txt","w")
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
            R["case"]+=1
            step=(q-1)//d;g=powi(gen,step)
            G=[];x=one
            for i in range(d): G.append(x);x=muli(x,g)
            Sset=set(G)
            Jin=sorted({pow(2,j,d) for j in range(1,(ordm(2,d) or d)+1) if pow(2,j,d)!=0 and not ispp(pow(2,j,d),2)})
            pairs=[(a,b) for a in G for b in G if a!=b and a!=one and b!=one]
            valid=set()
            for (a,b) in pairs:
                if addi(addi(one,a),b) in Sset: valid.add((a,b))
            V=set(pairs)
            for r in Jin:
                if not V: break
                bad=set()
                for (a,b) in V:
                    z=addi(addi(one,a),b)
                    if addi(addi(addi(powi(a,r),powi(b,r)),powi(z,r)),one)!=zero: bad.add((a,b))
                V-=bad
            P=V-valid
            # A: I 与 P_x
            I=[a for a in G if addi(one,a) in Sset]
            Px=set(a for (a,b) in P if b==addi(one,a))
            Iset=set(I)
            d1=len(Iset-Px); d2=len(Px-Iset)
            R["sumI"]+=len(Iset); R["sumPx"]+=len(Px)
            if d1: R["A_I_minus_P"]+=1
            if d2: R["A_P_minus_I"]+=1
            if not (d1==0 and d2==0): R["A_I_neq"]+=1
            # B: Q_j(x,1+x) 自动消失
            for a in I:
                y=addi(one,a)
                for r in Jin:
                    if addi(addi(powi(a,r),powi(y,r)),one)!=zero:
                        R["B_viol_pairs"]+=1; R["B_viol_x"]+=1; break
            # C: 计数
            if len(P)==len(Iset): R["C_eq1"]+=1
            else: R["C_ne1"]+=1
            if len(V)==len(valid)+len(Iset): R["C_eq2"]+=1
            else: R["C_ne2"]+=1
            # D: char 2 退化集（x=1 -> y=0）恒空
            if addi(one,one) in Sset: R["D_degen_contrib"]+=1
            lam2=len(Iset)
            if lam2==0: R["lam2_zero_caps"]+=1
            else: R["lam2_pos"]+=1
            rows.append((n,q,d,len(Iset),len(Px),d1,d2,len(V),len(valid),len(P),lam2))
            out.write("n=%2d q=%5d d=%4d |I|=%4d |Px|=%4d |I-Px|=%d |Px-I|=%d |V*|=%5d |valid|=%5d |P*|=%3d λ2=%4d\n"%(
                n,q,d,len(Iset),len(Px),d1,d2,len(V),len(valid),len(P),lam2))
    print("STATS:",R)
    print("前 8 行:")
    for r in rows[:8]: print(r)
    print("A 不等的行:")
    for r in rows:
        if r[5] or r[6]: print(r)
    out.write("STATS: "+str(R)+"\n");out.close()
main()
